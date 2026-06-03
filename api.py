import json
import os
import pathlib
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic

# Load .env file if present (ANTHROPIC_API_KEY=... in .env)
load_dotenv()

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    raise SystemExit("ERROR: ANTHROPIC_API_KEY is not set. Add it to a .env file or export it before starting.")

app = Flask(__name__)
CORS(app)

BASE = pathlib.Path(__file__).parent

# ── Load system prompt ────────────────────────────────────────────────────────
SYSTEM_PROMPT = (BASE / "crohns_system_prompt.md").read_text()

# ── Build knowledge base from datasources ────────────────────────────────────
def build_knowledge_base() -> str:
    data = json.loads((BASE / "crohns_datasources.json").read_text())
    sections = []
    for src in data["sources"]:
        content = src.get("scraped_content", "").strip()
        if not content:
            continue
        confidence = src.get("confidence_pct", 0)
        url = src.get("url", "")
        keywords = ", ".join(src.get("keywords", []))
        caveat = ""
        if confidence < 50:
            caveat = f" [LOW CONFIDENCE — partial content only: {src.get('notes', '')}]"
        sections.append(
            f"--- SOURCE ---\n"
            f"URL: {url}\n"
            f"Confidence: {confidence}%{caveat}\n"
            f"Keywords: {keywords}\n\n"
            f"{content}\n"
        )
    return "\n".join(sections)

KNOWLEDGE_BASE = build_knowledge_base()
SOURCE_COUNT = KNOWLEDGE_BASE.count("--- SOURCE ---")

# ── Combine system prompt + knowledge base into one cacheable block ───────────
FULL_SYSTEM = (
    SYSTEM_PROMPT
    + "\n\n## Approved Source Materials\n\n"
    + "The following are your ONLY permitted sources of information. "
    + "You must not answer from any knowledge outside these sources. "
    + "Always cite the source URL when you provide information.\n\n"
    + KNOWLEDGE_BASE
)

client = anthropic.Anthropic(api_key=API_KEY)

# ── In-memory conversation history ───────────────────────────────────────────
# Keyed by session_id so multiple browser tabs stay independent.
sessions: dict[str, list[dict]] = {}

def get_history(session_id: str) -> list[dict]:
    if session_id not in sessions:
        sessions[session_id] = []
    return sessions[session_id]


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/chat", methods=["POST"])
def chat():
    body = request.get_json(silent=True) or {}
    user_message = (body.get("message") or "").strip()
    session_id = body.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "message is required"}), 400

    history = get_history(session_id)
    history.append({"role": "user", "content": user_message})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1500,
            system=[
                {
                    "type": "text",
                    "text": FULL_SYSTEM,
                    # Prompt caching: system prompt + full knowledge base is large
                    # and identical on every request — cache it to cut latency and cost.
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=history,
        )

        reply = response.content[0].text
        history.append({"role": "assistant", "content": reply})

        return jsonify({
            "reply": reply,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "cache_read_input_tokens": getattr(response.usage, "cache_read_input_tokens", 0),
                "cache_creation_input_tokens": getattr(response.usage, "cache_creation_input_tokens", 0),
            }
        })

    except anthropic.APIStatusError as e:
        return jsonify({"error": f"API error {e.status_code}: {e.message}"}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset():
    """Clear conversation history for a session."""
    body = request.get_json(silent=True) or {}
    session_id = body.get("session_id", "default")
    sessions.pop(session_id, None)
    return jsonify({"status": "ok"})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "sources_loaded": SOURCE_COUNT,
        "model": "claude-sonnet-4-6",
        "system_prompt_chars": len(SYSTEM_PROMPT),
        "knowledge_base_chars": len(KNOWLEDGE_BASE),
    })


if __name__ == "__main__":
    print(f"  Sources loaded : {SOURCE_COUNT}")
    print(f"  System prompt  : {len(SYSTEM_PROMPT):,} chars")
    print(f"  Knowledge base : {len(KNOWLEDGE_BASE):,} chars")
    print(f"  Listening on   : http://localhost:5050")
    app.run(port=5050, debug=False)
