{\rtf1\ansi\ansicpg1252\cocoartf2577
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red93\green108\blue125;\red242\green239\blue236;\red0\green0\blue0;
\red12\green99\blue153;\red135\green91\blue44;\red255\green255\blue255;\red133\green0\blue67;\red135\green135\blue135;
\red85\green138\blue3;}
{\*\expandedcolortbl;;\cssrgb\c43922\c50196\c56471;\cssrgb\c96078\c94902\c94118;\cssrgb\c0\c0\c0;
\cssrgb\c0\c46667\c66667;\cssrgb\c60392\c43137\c22745;\cssrgb\c100000\c100000\c100000\c50196;\cssrgb\c60000\c0\c33333;\cssrgb\c60000\c60000\c60000;
\cssrgb\c40000\c60000\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl540\partightenfactor0

\f0\fs36 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 # Import the modules\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
\pard\pardeftab720\sl540\partightenfactor0
\cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 import\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  sys\
\cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 import\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  random\
\
ans \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 =\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 True\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
\
\cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 while\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  ans\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    question \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 =\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 raw_input\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 (\cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "Ask the magic 8 ball a question: (press enter to quit) "\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 )\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 =\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  random\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 .\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 randint\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 (\cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 1\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ,\cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 8\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 )\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 if\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  question \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ""\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        sys\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 .\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 exit\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ()\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 1\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "It is certain"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 2\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "Outlook good"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 3\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "You may rely on it"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 4\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "Ask again later"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 5\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "Concentrate and ask again"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 6\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "Reply hazy, try again"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 7\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "My reply is no"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
    \
    \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 elif\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  answers \cf6 \cb7 \strokec6 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 ==\cf4 \cb3 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf8 \strokec8 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 8\cf9 \strokec9 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 :\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
        \cf5 \strokec5 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 print\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0  \cf10 \strokec10 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 "My sources say no"\cf4 \strokec4 \shad\shadx0\shady-20\shadr0\shado255 \shadc0 \
}