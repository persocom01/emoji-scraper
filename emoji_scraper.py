import string
import itertools
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

export_path = r'.\emojis.json'

# Copy and paste the webpage:
# https://www.unicode.org/emoji/charts/full-emoji-list.html
# ctrl+a ctrl+c ctrl+v onto a text editor to get the string below.
emoji_webpage = """
[Unicode]Emoji Charts

Adopt a Character
AAC Animation
Full Emoji List, v13.0
Index & Help | Images & Rights | Spec | Proposing Additions

This chart provides a list of the Unicode emoji characters and sequences, with images from different vendors, CLDR name, date, source, and keywords. The ordering of the emoji and the annotations are based on Unicode CLDR data. Emoji sequences have more than one code point in the Code column. Recently-added emoji are marked by a ⊛ in the name and outlined images; their images may show as a group with “…” before and after.

Emoji with skin-tones are not listed here: see Full Skin Tone List.

For counts of emoji, see Emoji Counts.

While these charts use a particular version of the Unicode Emoji data files, the images and format may be updated at any time. For any production usage, consult those data files. For information about the contents of each column, such as the CLDR Short Name, click on the column header. For further information, see Index & Help.

Smileys & Emotion
face-smiling
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1	U+1F600	😀	😀	😀	😀	😀	😀	😀	😀	😀	—	—	—	grinning face
2	U+1F603	😃	😃	😃	😃	😃	😃	😃	😃	😃	😃	😃	😃	grinning face with big eyes
3	U+1F604	😄	😄	😄	😄	😄	😄	😄	😄	😄	😄	—	—	grinning face with smiling eyes
4	U+1F601	😁	😁	😁	😁	😁	😁	😁	😁	😁	😁	😁	😁	beaming face with smiling eyes
5	U+1F606	😆	😆	😆	😆	😆	😆	😆	😆	😆	—	😆	—	grinning squinting face
6	U+1F605	😅	😅	😅	😅	😅	😅	😅	😅	😅	—	😅	—	grinning face with sweat
7	U+1F923	🤣	🤣	🤣	🤣	🤣	🤣	🤣	🤣	—	—	—	—	rolling on the floor laughing
8	U+1F602	😂	😂	😂	😂	😂	😂	😂	😂	😂	😂	—	😂	face with tears of joy
9	U+1F642	🙂	🙂	🙂	🙂	🙂	🙂	🙂	🙂	🙂	—	—	—	slightly smiling face
10	U+1F643	🙃	🙃	🙃	🙃	🙃	🙃	🙃	🙃	—	—	—	—	upside-down face
11	U+1F609	😉	😉	😉	😉	😉	😉	😉	😉	😉	😉	😉	😉	winking face
12	U+1F60A	😊	😊	😊	😊	😊	😊	😊	😊	😊	😊	—	😊	smiling face with smiling eyes
13	U+1F607	😇	😇	😇	😇	😇	😇	😇	😇	—	—	—	—	smiling face with halo
face-affection
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
14	U+1F970	🥰	🥰	🥰	🥰	🥰	🥰	🥰	🥰	—	—	—	—	smiling face with hearts
15	U+1F60D	😍	😍	😍	😍	😍	😍	😍	😍	😍	😍	😍	😍	smiling face with heart-eyes
16	U+1F929	🤩	🤩	🤩	🤩	🤩	🤩	🤩	🤩	—	—	—	—	star-struck
17	U+1F618	😘	😘	😘	😘	😘	😘	😘	😘	😘	😘	—	😘	face blowing a kiss
18	U+1F617	😗	😗	😗	😗	😗	😗	😗	😗	—	—	—	—	kissing face
19	U+263A	☺	☺	☺	☺	☺	☺	☺	☺	☺	☺	—	☺	smiling face
20	U+1F61A	😚	😚	😚	😚	😚	😚	😚	😚	😚	😚	—	😚	kissing face with closed eyes
21	U+1F619	😙	😙	😙	😙	😙	😙	😙	😙	—	—	—	—	kissing face with smiling eyes
22	U+1F972	🥲	—	🥲	—	—	—	🥲	—	—	—	—	—	⊛ smiling face with tear
face-tongue
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
23	U+1F60B	😋	😋	😋	😋	😋	😋	😋	😋	😋	—	😋	—	face savoring food
24	U+1F61B	😛	😛	😛	😛	😛	😛	😛	😛	—	—	—	—	face with tongue
25	U+1F61C	😜	😜	😜	😜	😜	😜	😜	😜	😜	😜	😜	😜	winking face with tongue
26	U+1F92A	🤪	🤪	🤪	🤪	🤪	🤪	🤪	🤪	—	—	—	—	zany face
27	U+1F61D	😝	😝	😝	😝	😝	😝	😝	😝	😝	😝	—	—	squinting face with tongue
28	U+1F911	🤑	🤑	🤑	🤑	🤑	🤑	🤑	🤑	—	—	—	—	money-mouth face
face-hand
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
29	U+1F917	🤗	🤗	🤗	🤗	🤗	🤗	🤗	🤗	—	—	—	—	hugging face
30	U+1F92D	🤭	🤭	🤭	🤭	🤭	🤭	🤭	🤭	—	—	—	—	face with hand over mouth
31	U+1F92B	🤫	🤫	🤫	🤫	🤫	🤫	🤫	🤫	—	—	—	—	shushing face
32	U+1F914	🤔	🤔	🤔	🤔	🤔	🤔	🤔	🤔	—	—	—	—	thinking face
face-neutral-skeptical
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
33	U+1F910	🤐	🤐	🤐	🤐	🤐	🤐	🤐	🤐	—	—	—	—	zipper-mouth face
34	U+1F928	🤨	🤨	🤨	🤨	🤨	🤨	🤨	🤨	—	—	—	—	face with raised eyebrow
35	U+1F610	😐	😐	😐	😐	😐	😐	😐	😐	—	—	—	—	neutral face
36	U+1F611	😑	😑	😑	😑	😑	😑	😑	😑	—	—	—	—	expressionless face
37	U+1F636	😶	😶	😶	😶	😶	😶	😶	😶	—	—	—	—	face without mouth
38	U+1F60F	😏	😏	😏	😏	😏	😏	😏	😏	😏	😏	😏	😏	smirking face
39	U+1F612	😒	😒	😒	😒	😒	😒	😒	😒	😒	😒	😒	😒	unamused face
40	U+1F644	🙄	🙄	🙄	🙄	🙄	🙄	🙄	🙄	—	—	—	—	face with rolling eyes
41	U+1F62C	😬	😬	😬	😬	😬	😬	😬	😬	—	—	—	—	grimacing face
42	U+1F925	🤥	🤥	🤥	🤥	🤥	🤥	🤥	🤥	—	—	—	—	lying face
face-sleepy
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
43	U+1F60C	😌	😌	😌	😌	😌	😌	😌	😌	😌	😌	😌	😌	relieved face
44	U+1F614	😔	😔	😔	😔	😔	😔	😔	😔	😔	😔	😔	😔	pensive face
45	U+1F62A	😪	😪	😪	😪	😪	😪	😪	😪	😪	😪	—	😪	sleepy face
46	U+1F924	🤤	🤤	🤤	🤤	🤤	🤤	🤤	🤤	—	—	—	—	drooling face
47	U+1F634	😴	😴	😴	😴	😴	😴	😴	😴	—	—	—	—	sleeping face
face-unwell
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
48	U+1F637	😷	😷	😷	😷	😷	😷	😷	😷	😷	😷	—	😷	face with medical mask
49	U+1F912	🤒	🤒	🤒	🤒	🤒	🤒	🤒	🤒	—	—	—	—	face with thermometer
50	U+1F915	🤕	🤕	🤕	🤕	🤕	🤕	🤕	🤕	—	—	—	—	face with head-bandage
51	U+1F922	🤢	🤢	🤢	🤢	🤢	🤢	🤢	🤢	—	—	—	—	nauseated face
52	U+1F92E	🤮	🤮	🤮	🤮	🤮	🤮	🤮	🤮	—	—	—	—	face vomiting
53	U+1F927	🤧	🤧	🤧	🤧	🤧	🤧	🤧	🤧	—	—	—	—	sneezing face
54	U+1F975	🥵	🥵	🥵	🥵	🥵	🥵	🥵	🥵	—	—	—	—	hot face
55	U+1F976	🥶	🥶	🥶	🥶	🥶	🥶	🥶	🥶	—	—	—	—	cold face
56	U+1F974	🥴	🥴	🥴	🥴	🥴	🥴	🥴	🥴	—	—	—	—	woozy face
57	U+1F635	😵	😵	😵	😵	😵	😵	😵	😵	😵	—	😵	😵	dizzy face
58	U+1F92F	🤯	🤯	🤯	🤯	🤯	🤯	🤯	🤯	—	—	—	—	exploding head
face-hat
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
59	U+1F920	🤠	🤠	🤠	🤠	🤠	🤠	🤠	🤠	—	—	—	—	cowboy hat face
60	U+1F973	🥳	🥳	🥳	🥳	🥳	🥳	🥳	🥳	—	—	—	—	partying face
61	U+1F978	🥸	—	🥸	—	—	—	🥸	—	—	—	—	—	⊛ disguised face
face-glasses
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
62	U+1F60E	😎	😎	😎	😎	😎	😎	😎	😎	😎	—	—	—	smiling face with sunglasses
63	U+1F913	🤓	🤓	🤓	🤓	🤓	🤓	🤓	🤓	—	—	—	—	nerd face
64	U+1F9D0	🧐	🧐	🧐	🧐	🧐	🧐	🧐	🧐	—	—	—	—	face with monocle
face-concerned
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
65	U+1F615	😕	😕	😕	😕	😕	😕	😕	😕	😕	—	—	—	confused face
66	U+1F61F	😟	😟	😟	😟	😟	😟	😟	😟	😟	—	—	—	worried face
67	U+1F641	🙁	🙁	🙁	🙁	🙁	🙁	🙁	🙁	—	—	—	—	slightly frowning face
68	U+2639	☹	☹	☹	☹	☹	☹	☹	☹	—	—	—	—	frowning face
69	U+1F62E	😮	😮	😮	😮	😮	😮	😮	😮	—	—	—	—	face with open mouth
70	U+1F62F	😯	😯	😯	😯	😯	😯	😯	😯	—	—	—	—	hushed face
71	U+1F632	😲	😲	😲	😲	😲	😲	😲	😲	😲	😲	—	😲	astonished face
72	U+1F633	😳	😳	😳	😳	😳	😳	😳	😳	😳	😳	—	😳	flushed face
73	U+1F97A	🥺	🥺	🥺	🥺	🥺	🥺	🥺	🥺	—	—	—	—	pleading face
74	U+1F626	😦	😦	😦	😦	😦	😦	😦	😦	—	—	—	—	frowning face with open mouth
75	U+1F627	😧	😧	😧	😧	😧	😧	😧	😧	—	—	—	—	anguished face
76	U+1F628	😨	😨	😨	😨	😨	😨	😨	😨	😨	😨	—	😨	fearful face
77	U+1F630	😰	😰	😰	😰	😰	😰	😰	😰	😰	😰	—	😰	anxious face with sweat
78	U+1F625	😥	😥	😥	😥	😥	😥	😥	😥	😥	😥	—	—	sad but relieved face
79	U+1F622	😢	😢	😢	😢	😢	😢	😢	😢	😢	😢	😢	😢	crying face
80	U+1F62D	😭	😭	😭	😭	😭	😭	😭	😭	😭	😭	😭	😭	loudly crying face
81	U+1F631	😱	😱	😱	😱	😱	😱	😱	😱	😱	😱	😱	😱	face screaming in fear
82	U+1F616	😖	😖	😖	😖	😖	😖	😖	😖	😖	😖	😖	😖	confounded face
83	U+1F623	😣	😣	😣	😣	😣	😣	😣	😣	😣	😣	😣	😣	persevering face
84	U+1F61E	😞	😞	😞	😞	😞	😞	😞	😞	😞	😞	😞	—	disappointed face
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
85	U+1F613	😓	😓	😓	😓	😓	😓	😓	😓	😓	😓	😓	😓	downcast face with sweat
86	U+1F629	😩	😩	😩	😩	😩	😩	😩	😩	😩	—	—	😩	weary face
87	U+1F62B	😫	😫	😫	😫	😫	😫	😫	😫	😫	—	—	😫	tired face
88	U+1F971	🥱	🥱	🥱	🥱	🥱	🥱	🥱	🥱	—	—	—	—	yawning face
face-negative
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
89	U+1F624	😤	😤	😤	😤	😤	😤	😤	😤	😤	—	—	😤	face with steam from nose
90	U+1F621	😡	😡	😡	😡	😡	😡	😡	😡	😡	😡	😡	😡	pouting face
91	U+1F620	😠	😠	😠	😠	😠	😠	😠	😠	😠	😠	😠	😠	angry face
92	U+1F92C	🤬	🤬	🤬	🤬	🤬	🤬	🤬	🤬	—	—	—	—	face with symbols on mouth
93	U+1F608	😈	😈	😈	😈	😈	😈	😈	😈	—	—	—	—	smiling face with horns
94	U+1F47F	👿	👿	👿	👿	👿	👿	👿	👿	👿	👿	—	👿	angry face with horns
95	U+1F480	💀	💀	💀	💀	💀	💀	💀	💀	💀	💀	—	💀	skull
96	U+2620	☠	☠	☠	☠	☠	☠	☠	☠	—	—	—	—	skull and crossbones
face-costume
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
97	U+1F4A9	💩	💩	💩	💩	💩	💩	💩	💩	💩	💩	—	💩	pile of poo
98	U+1F921	🤡	🤡	🤡	🤡	🤡	🤡	🤡	🤡	—	—	—	—	clown face
99	U+1F479	👹	👹	👹	👹	👹	👹	👹	👹	👹	—	—	👹	ogre
100	U+1F47A	👺	👺	👺	👺	👺	👺	👺	👺	👺	—	—	👺	goblin
101	U+1F47B	👻	👻	👻	👻	👻	👻	👻	👻	👻	👻	—	👻	ghost
102	U+1F47D	👽	👽	👽	👽	👽	👽	👽	👽	👽	👽	—	👽	alien
103	U+1F47E	👾	👾	👾	👾	👾	👾	👾	👾	👾	👾	—	👾	alien monster
104	U+1F916	🤖	🤖	🤖	🤖	🤖	🤖	🤖	🤖	—	—	—	—	robot
cat-face
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
105	U+1F63A	😺	😺	😺	😺	😺	😺	😺	😺	😺	—	—	😺	grinning cat
106	U+1F638	😸	😸	😸	😸	😸	😸	😸	😸	😸	—	—	😸	grinning cat with smiling eyes
107	U+1F639	😹	😹	😹	😹	😹	😹	😹	😹	😹	—	—	😹	cat with tears of joy
108	U+1F63B	😻	😻	😻	😻	😻	😻	😻	😻	😻	—	—	😻	smiling cat with heart-eyes
109	U+1F63C	😼	😼	😼	😼	😼	😼	😼	😼	😼	—	—	😼	cat with wry smile
110	U+1F63D	😽	😽	😽	😽	😽	😽	😽	😽	😽	—	—	😽	kissing cat
111	U+1F640	🙀	🙀	🙀	🙀	🙀	🙀	🙀	🙀	🙀	—	—	🙀	weary cat
112	U+1F63F	😿	😿	😿	😿	😿	😿	😿	😿	😿	—	—	😿	crying cat
113	U+1F63E	😾	😾	😾	😾	😾	😾	😾	😾	😾	—	—	😾	pouting cat
monkey-face
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
114	U+1F648	🙈	🙈	🙈	🙈	🙈	🙈	🙈	🙈	🙈	—	—	🙈	see-no-evil monkey
115	U+1F649	🙉	🙉	🙉	🙉	🙉	🙉	🙉	🙉	🙉	—	—	🙉	hear-no-evil monkey
116	U+1F64A	🙊	🙊	🙊	🙊	🙊	🙊	🙊	🙊	🙊	—	—	🙊	speak-no-evil monkey
emotion
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
117	U+1F48B	💋	💋	💋	💋	💋	💋	💋	💋	💋	💋	💋	💋	kiss mark
118	U+1F48C	💌	💌	💌	💌	💌	💌	💌	💌	💌	—	💌	💌	love letter
119	U+1F498	💘	💘	💘	💘	💘	💘	💘	💘	💘	💘	—	💘	heart with arrow
120	U+1F49D	💝	💝	💝	💝	💝	💝	💝	💝	💝	💝	—	💝	heart with ribbon
121	U+1F496	💖	💖	💖	💖	💖	💖	💖	💖	💖	—	—	💖	sparkling heart
122	U+1F497	💗	💗	💗	💗	💗	💗	💗	💗	💗	💗	—	—	growing heart
123	U+1F493	💓	💓	💓	💓	💓	💓	💓	💓	💓	💓	💓	💓	beating heart
124	U+1F49E	💞	💞	💞	💞	💞	💞	💞	💞	💞	—	—	💞	revolving hearts
125	U+1F495	💕	💕	💕	💕	💕	💕	💕	💕	💕	—	💕	💕	two hearts
126	U+1F49F	💟	💟	💟	💟	💟	💟	💟	💟	💟	💟	—	—	heart decoration
127	U+2763	❣	❣	❣	❣	❣	❣	❣	❣	—	—	—	—	heart exclamation
128	U+1F494	💔	💔	💔	💔	💔	💔	💔	💔	💔	💔	💔	💔	broken heart
129	U+2764	❤	❤	❤	❤	❤	❤	❤	❤	❤	❤	❤	❤	red heart
130	U+1F9E1	🧡	🧡	🧡	🧡	🧡	🧡	🧡	🧡	—	—	—	—	orange heart
131	U+1F49B	💛	💛	💛	💛	💛	💛	💛	💛	💛	💛	—	💛	yellow heart
132	U+1F49A	💚	💚	💚	💚	💚	💚	💚	💚	💚	💚	—	💚	green heart
133	U+1F499	💙	💙	💙	💙	💙	💙	💙	💙	💙	💙	—	💙	blue heart
134	U+1F49C	💜	💜	💜	💜	💜	💜	💜	💜	💜	💜	—	💜	purple heart
135	U+1F90E	🤎	🤎	🤎	🤎	🤎	🤎	🤎	🤎	—	—	—	—	brown heart
136	U+1F5A4	🖤	🖤	🖤	🖤	🖤	🖤	🖤	🖤	—	—	—	—	black heart
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
137	U+1F90D	🤍	🤍	🤍	🤍	🤍	🤍	🤍	🤍	—	—	—	—	white heart
138	U+1F4AF	💯	💯	💯	💯	💯	💯	💯	💯	💯	—	—	💯	hundred points
139	U+1F4A2	💢	💢	💢	💢	💢	💢	💢	💢	💢	💢	💢	💢	anger symbol
140	U+1F4A5	💥	💥	💥	💥	💥	💥	💥	💥	💥	—	💥	💥	collision
141	U+1F4AB	💫	💫	💫	💫	💫	💫	💫	💫	💫	—	—	💫	dizzy
142	U+1F4A6	💦	💦	💦	💦	💦	💦	💦	💦	💦	💦	💦	💦	sweat droplets
143	U+1F4A8	💨	💨	💨	💨	💨	💨	💨	💨	💨	💨	💨	💨	dashing away
144	U+1F573	🕳	🕳	🕳	🕳	🕳	🕳	🕳	🕳	—	—	—	—	hole
145	U+1F4A3	💣	💣	💣	💣	💣	💣	💣	💣	💣	💣	💣	💣	bomb
146	U+1F4AC	💬	💬	💬	💬	💬	💬	💬	💬	💬	—	—	💬	speech balloon
147	U+1F441 U+FE0F U+200D U+1F5E8 U+FE0F	👁️‍🗨️	👁️‍🗨️	👁️‍🗨️	👁️‍🗨️	👁️‍🗨️	👁️‍🗨️	👁️‍🗨️	👁️‍🗨️	—	—	—	—	eye in speech bubble
148	U+1F5E8	🗨	🗨	🗨	🗨	🗨	🗨	🗨	🗨	—	—	—	—	left speech bubble
149	U+1F5EF	🗯	🗯	🗯	🗯	🗯	🗯	🗯	🗯	—	—	—	—	right anger bubble
150	U+1F4AD	💭	💭	💭	💭	💭	💭	💭	💭	—	—	—	—	thought balloon
151	U+1F4A4	💤	💤	💤	💤	💤	💤	💤	💤	💤	💤	💤	💤	zzz
People & Body
hand-fingers-open
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
152	U+1F44B	👋	👋	👋	👋	👋	👋	👋	👋	👋	👋	—	👋	waving hand
153	U+1F91A	🤚	🤚	🤚	🤚	🤚	🤚	🤚	🤚	—	—	—	—	raised back of hand
154	U+1F590	🖐	🖐	🖐	🖐	🖐	🖐	🖐	🖐	—	—	—	—	hand with fingers splayed
155	U+270B	✋	✋	✋	✋	✋	✋	✋	✋	✋	✋	✋	✋	raised hand
156	U+1F596	🖖	🖖	🖖	🖖	🖖	🖖	🖖	🖖	—	—	—	—	vulcan salute
hand-fingers-partial
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
157	U+1F44C	👌	👌	👌	👌	👌	👌	👌	👌	👌	👌	—	👌	OK hand
158	U+1F90C	🤌	—	🤌	—	—	—	🤌	—	—	—	—	—	⊛ pinched fingers
159	U+1F90F	🤏	🤏	🤏	🤏	🤏	🤏	🤏	🤏	—	—	—	—	pinching hand
160	U+270C	✌	✌	✌	✌	✌	✌	✌	✌	✌	✌	✌	✌	victory hand
161	U+1F91E	🤞	🤞	🤞	🤞	🤞	🤞	🤞	🤞	—	—	—	—	crossed fingers
162	U+1F91F	🤟	🤟	🤟	🤟	🤟	🤟	🤟	🤟	—	—	—	—	love-you gesture
163	U+1F918	🤘	🤘	🤘	🤘	🤘	🤘	🤘	🤘	—	—	—	—	sign of the horns
164	U+1F919	🤙	🤙	🤙	🤙	🤙	🤙	🤙	🤙	—	—	—	—	call me hand
hand-single-finger
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
165	U+1F448	👈	👈	👈	👈	👈	👈	👈	👈	👈	👈	—	👈	backhand index pointing left
166	U+1F449	👉	👉	👉	👉	👉	👉	👉	👉	👉	👉	—	👉	backhand index pointing right
167	U+1F446	👆	👆	👆	👆	👆	👆	👆	👆	👆	👆	—	👆	backhand index pointing up
168	U+1F595	🖕	🖕	🖕	🖕	🖕	🖕	🖕	🖕	—	—	—	—	middle finger
169	U+1F447	👇	👇	👇	👇	👇	👇	👇	👇	👇	👇	—	👇	backhand index pointing down
170	U+261D	☝	☝	☝	☝	☝	☝	☝	☝	☝	☝	—	☝	index pointing up
hand-fingers-closed
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
171	U+1F44D	👍	👍	👍	👍	👍	👍	👍	👍	👍	👍	👍	👍	thumbs up
172	U+1F44E	👎	👎	👎	👎	👎	👎	👎	👎	👎	👎	—	👎	thumbs down
173	U+270A	✊	✊	✊	✊	✊	✊	✊	✊	✊	✊	✊	✊	raised fist
174	U+1F44A	👊	👊	👊	👊	👊	👊	👊	👊	👊	👊	👊	👊	oncoming fist
175	U+1F91B	🤛	🤛	🤛	🤛	🤛	🤛	🤛	🤛	—	—	—	—	left-facing fist
176	U+1F91C	🤜	🤜	🤜	🤜	🤜	🤜	🤜	🤜	—	—	—	—	right-facing fist
hands
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
177	U+1F44F	👏	👏	👏	👏	👏	👏	👏	👏	👏	👏	—	👏	clapping hands
178	U+1F64C	🙌	🙌	🙌	🙌	🙌	🙌	🙌	🙌	🙌	🙌	—	🙌	raising hands
179	U+1F450	👐	👐	👐	👐	👐	👐	👐	👐	👐	👐	—	—	open hands
180	U+1F932	🤲	🤲	🤲	🤲	🤲	🤲	🤲	🤲	—	—	—	—	palms up together
181	U+1F91D	🤝	🤝	🤝	🤝	🤝	🤝	🤝	🤝	—	—	—	—	handshake
182	U+1F64F	🙏	🙏	🙏	🙏	🙏	🙏	🙏	🙏	🙏	🙏	—	🙏	folded hands
hand-prop
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
183	U+270D	✍	✍	✍	✍	✍	✍	✍	✍	—	—	—	—	writing hand
184	U+1F485	💅	💅	💅	💅	💅	💅	💅	💅	💅	💅	—	💅	nail polish
185	U+1F933	🤳	🤳	🤳	🤳	🤳	🤳	🤳	🤳	—	—	—	—	selfie
body-parts
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
186	U+1F4AA	💪	💪	💪	💪	💪	💪	💪	💪	💪	💪	—	💪	flexed biceps
187	U+1F9BE	🦾	🦾	🦾	🦾	🦾	🦾	🦾	🦾	—	—	—	—	mechanical arm
188	U+1F9BF	🦿	🦿	🦿	🦿	🦿	🦿	🦿	🦿	—	—	—	—	mechanical leg
189	U+1F9B5	🦵	🦵	🦵	🦵	🦵	🦵	🦵	🦵	—	—	—	—	leg
190	U+1F9B6	🦶	🦶	🦶	🦶	🦶	🦶	🦶	🦶	—	—	—	—	foot
191	U+1F442	👂	👂	👂	👂	👂	👂	👂	👂	👂	👂	👂	👂	ear
192	U+1F9BB	🦻	🦻	🦻	🦻	🦻	🦻	🦻	🦻	—	—	—	—	ear with hearing aid
193	U+1F443	👃	👃	👃	👃	👃	👃	👃	👃	👃	👃	—	👃	nose
194	U+1F9E0	🧠	🧠	🧠	🧠	🧠	🧠	🧠	🧠	—	—	—	—	brain
195	U+1FAC0	🫀	… 🫀 🫀 🫀 …	⊛ anatomical heart
196	U+1FAC1	🫁	… 🫁 🫁 🫁 …	⊛ lungs
197	U+1F9B7	🦷	🦷	🦷	🦷	🦷	🦷	🦷	🦷	—	—	—	—	tooth
198	U+1F9B4	🦴	🦴	🦴	🦴	🦴	🦴	🦴	🦴	—	—	—	—	bone
199	U+1F440	👀	👀	👀	👀	👀	👀	👀	👀	👀	👀	👀	👀	eyes
200	U+1F441	👁	👁	👁	👁	👁	👁	👁	👁	—	—	—	—	eye
201	U+1F445	👅	👅	👅	👅	👅	👅	👅	👅	👅	—	—	👅	tongue
202	U+1F444	👄	👄	👄	👄	👄	👄	👄	👄	👄	👄	—	👄	mouth
person
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
203	U+1F476	👶	👶	👶	👶	👶	👶	👶	👶	👶	👶	—	👶	baby
204	U+1F9D2	🧒	🧒	🧒	🧒	🧒	🧒	🧒	🧒	—	—	—	—	child
205	U+1F466	👦	👦	👦	👦	👦	👦	👦	👦	👦	👦	—	—	boy
206	U+1F467	👧	👧	👧	👧	👧	👧	👧	👧	👧	👧	—	—	girl
207	U+1F9D1	🧑	🧑	🧑	🧑	🧑	🧑	🧑	🧑	—	—	—	—	person
208	U+1F471	👱	👱	👱	👱	👱	👱	👱	👱	👱	👱	—	👱	person: blond hair
209	U+1F468	👨	👨	👨	👨	👨	👨	👨	👨	👨	👨	—	👨	man
210	U+1F9D4	🧔	🧔	🧔	🧔	🧔	🧔	🧔	🧔	—	—	—	—	man: beard
211	U+1F468 U+200D U+1F9B0	👨‍🦰	👨‍🦰	👨‍🦰	👨‍🦰	👨‍🦰	👨‍🦰	👨‍🦰	👨‍🦰	—	—	—	—	man: red hair
212	U+1F468 U+200D U+1F9B1	👨‍🦱	👨‍🦱	👨‍🦱	👨‍🦱	👨‍🦱	👨‍🦱	👨‍🦱	👨‍🦱	—	—	—	—	man: curly hair
213	U+1F468 U+200D U+1F9B3	👨‍🦳	👨‍🦳	👨‍🦳	👨‍🦳	👨‍🦳	👨‍🦳	👨‍🦳	👨‍🦳	—	—	—	—	man: white hair
214	U+1F468 U+200D U+1F9B2	👨‍🦲	👨‍🦲	👨‍🦲	👨‍🦲	👨‍🦲	👨‍🦲	👨‍🦲	👨‍🦲	—	—	—	—	man: bald
215	U+1F469	👩	👩	👩	👩	👩	👩	👩	👩	👩	👩	—	👩	woman
216	U+1F469 U+200D U+1F9B0	👩‍🦰	👩‍🦰	👩‍🦰	👩‍🦰	👩‍🦰	👩‍🦰	👩‍🦰	👩‍🦰	—	—	—	—	woman: red hair
217	U+1F9D1 U+200D U+1F9B0	🧑‍🦰	🧑‍🦰	🧑‍🦰	—	—	🧑‍🦰	—	—	—	—	—	—	person: red hair
218	U+1F469 U+200D U+1F9B1	👩‍🦱	👩‍🦱	👩‍🦱	👩‍🦱	👩‍🦱	👩‍🦱	👩‍🦱	👩‍🦱	—	—	—	—	woman: curly hair
219	U+1F9D1 U+200D U+1F9B1	🧑‍🦱	🧑‍🦱	🧑‍🦱	—	—	🧑‍🦱	—	—	—	—	—	—	person: curly hair
220	U+1F469 U+200D U+1F9B3	👩‍🦳	👩‍🦳	👩‍🦳	👩‍🦳	👩‍🦳	👩‍🦳	👩‍🦳	👩‍🦳	—	—	—	—	woman: white hair
221	U+1F9D1 U+200D U+1F9B3	🧑‍🦳	🧑‍🦳	🧑‍🦳	—	—	🧑‍🦳	—	—	—	—	—	—	person: white hair
222	U+1F469 U+200D U+1F9B2	👩‍🦲	👩‍🦲	👩‍🦲	👩‍🦲	👩‍🦲	👩‍🦲	👩‍🦲	👩‍🦲	—	—	—	—	woman: bald
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
223	U+1F9D1 U+200D U+1F9B2	🧑‍🦲	🧑‍🦲	🧑‍🦲	—	—	🧑‍🦲	—	—	—	—	—	—	person: bald
224	U+1F471 U+200D U+2640 U+FE0F	👱‍♀️	👱‍♀️	👱‍♀️	👱‍♀️	👱‍♀️	👱‍♀️	👱‍♀️	👱‍♀️	—	—	—	—	woman: blond hair
225	U+1F471 U+200D U+2642 U+FE0F	👱‍♂️	👱‍♂️	👱‍♂️	👱‍♂️	👱‍♂️	👱‍♂️	👱‍♂️	👱‍♂️	—	—	—	—	man: blond hair
226	U+1F9D3	🧓	🧓	🧓	🧓	🧓	🧓	🧓	🧓	—	—	—	—	older person
227	U+1F474	👴	👴	👴	👴	👴	👴	👴	👴	👴	👴	—	👴	old man
228	U+1F475	👵	👵	👵	👵	👵	👵	👵	👵	👵	👵	—	👵	old woman
person-gesture
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
229	U+1F64D	🙍	🙍	🙍	🙍	🙍	🙍	🙍	🙍	🙍	—	—	🙍	person frowning
230	U+1F64D U+200D U+2642 U+FE0F	🙍‍♂️	🙍‍♂️	🙍‍♂️	🙍‍♂️	🙍‍♂️	🙍‍♂️	🙍‍♂️	🙍‍♂️	—	—	—	—	man frowning
231	U+1F64D U+200D U+2640 U+FE0F	🙍‍♀️	🙍‍♀️	🙍‍♀️	🙍‍♀️	🙍‍♀️	🙍‍♀️	🙍‍♀️	🙍‍♀️	—	—	—	—	woman frowning
232	U+1F64E	🙎	🙎	🙎	🙎	🙎	🙎	🙎	🙎	🙎	—	—	🙎	person pouting
233	U+1F64E U+200D U+2642 U+FE0F	🙎‍♂️	🙎‍♂️	🙎‍♂️	🙎‍♂️	🙎‍♂️	🙎‍♂️	🙎‍♂️	🙎‍♂️	—	—	—	—	man pouting
234	U+1F64E U+200D U+2640 U+FE0F	🙎‍♀️	🙎‍♀️	🙎‍♀️	🙎‍♀️	🙎‍♀️	🙎‍♀️	🙎‍♀️	🙎‍♀️	—	—	—	—	woman pouting
235	U+1F645	🙅	🙅	🙅	🙅	🙅	🙅	🙅	🙅	🙅	🙅	—	🙅	person gesturing NO
236	U+1F645 U+200D U+2642 U+FE0F	🙅‍♂️	🙅‍♂️	🙅‍♂️	🙅‍♂️	🙅‍♂️	🙅‍♂️	🙅‍♂️	🙅‍♂️	—	—	—	—	man gesturing NO
237	U+1F645 U+200D U+2640 U+FE0F	🙅‍♀️	🙅‍♀️	🙅‍♀️	🙅‍♀️	🙅‍♀️	🙅‍♀️	🙅‍♀️	🙅‍♀️	—	—	—	—	woman gesturing NO
238	U+1F646	🙆	🙆	🙆	🙆	🙆	🙆	🙆	🙆	🙆	🙆	—	🙆	person gesturing OK
239	U+1F646 U+200D U+2642 U+FE0F	🙆‍♂️	🙆‍♂️	🙆‍♂️	🙆‍♂️	🙆‍♂️	🙆‍♂️	🙆‍♂️	🙆‍♂️	—	—	—	—	man gesturing OK
240	U+1F646 U+200D U+2640 U+FE0F	🙆‍♀️	🙆‍♀️	🙆‍♀️	🙆‍♀️	🙆‍♀️	🙆‍♀️	🙆‍♀️	🙆‍♀️	—	—	—	—	woman gesturing OK
241	U+1F481	💁	💁	💁	💁	💁	💁	💁	💁	💁	💁	—	—	person tipping hand
242	U+1F481 U+200D U+2642 U+FE0F	💁‍♂️	💁‍♂️	💁‍♂️	💁‍♂️	💁‍♂️	💁‍♂️	💁‍♂️	💁‍♂️	—	—	—	—	man tipping hand
243	U+1F481 U+200D U+2640 U+FE0F	💁‍♀️	💁‍♀️	💁‍♀️	💁‍♀️	💁‍♀️	💁‍♀️	💁‍♀️	💁‍♀️	—	—	—	—	woman tipping hand
244	U+1F64B	🙋	🙋	🙋	🙋	🙋	🙋	🙋	🙋	🙋	—	—	🙋	person raising hand
245	U+1F64B U+200D U+2642 U+FE0F	🙋‍♂️	🙋‍♂️	🙋‍♂️	🙋‍♂️	🙋‍♂️	🙋‍♂️	🙋‍♂️	🙋‍♂️	—	—	—	—	man raising hand
246	U+1F64B U+200D U+2640 U+FE0F	🙋‍♀️	🙋‍♀️	🙋‍♀️	🙋‍♀️	🙋‍♀️	🙋‍♀️	🙋‍♀️	🙋‍♀️	—	—	—	—	woman raising hand
247	U+1F9CF	🧏	🧏	🧏	🧏	🧏	🧏	🧏	🧏	—	—	—	—	deaf person
248	U+1F9CF U+200D U+2642 U+FE0F	🧏‍♂️	🧏‍♂️	🧏‍♂️	🧏‍♂️	—	🧏‍♂️	🧏‍♂️	🧏‍♂️	—	—	—	—	deaf man
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
249	U+1F9CF U+200D U+2640 U+FE0F	🧏‍♀️	🧏‍♀️	🧏‍♀️	🧏‍♀️	—	🧏‍♀️	🧏‍♀️	🧏‍♀️	—	—	—	—	deaf woman
250	U+1F647	🙇	🙇	🙇	🙇	🙇	🙇	🙇	🙇	🙇	🙇	—	🙇	person bowing
251	U+1F647 U+200D U+2642 U+FE0F	🙇‍♂️	🙇‍♂️	🙇‍♂️	🙇‍♂️	🙇‍♂️	🙇‍♂️	🙇‍♂️	🙇‍♂️	—	—	—	—	man bowing
252	U+1F647 U+200D U+2640 U+FE0F	🙇‍♀️	🙇‍♀️	🙇‍♀️	🙇‍♀️	🙇‍♀️	🙇‍♀️	🙇‍♀️	🙇‍♀️	—	—	—	—	woman bowing
253	U+1F926	🤦	🤦	🤦	🤦	🤦	🤦	🤦	🤦	—	—	—	—	person facepalming
254	U+1F926 U+200D U+2642 U+FE0F	🤦‍♂️	🤦‍♂️	🤦‍♂️	🤦‍♂️	🤦‍♂️	🤦‍♂️	🤦‍♂️	🤦‍♂️	—	—	—	—	man facepalming
255	U+1F926 U+200D U+2640 U+FE0F	🤦‍♀️	🤦‍♀️	🤦‍♀️	🤦‍♀️	🤦‍♀️	🤦‍♀️	🤦‍♀️	🤦‍♀️	—	—	—	—	woman facepalming
256	U+1F937	🤷	🤷	🤷	🤷	🤷	🤷	🤷	🤷	—	—	—	—	person shrugging
257	U+1F937 U+200D U+2642 U+FE0F	🤷‍♂️	🤷‍♂️	🤷‍♂️	🤷‍♂️	🤷‍♂️	🤷‍♂️	🤷‍♂️	🤷‍♂️	—	—	—	—	man shrugging
258	U+1F937 U+200D U+2640 U+FE0F	🤷‍♀️	🤷‍♀️	🤷‍♀️	🤷‍♀️	🤷‍♀️	🤷‍♀️	🤷‍♀️	🤷‍♀️	—	—	—	—	woman shrugging
person-role
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
259	U+1F9D1 U+200D U+2695 U+FE0F	🧑‍⚕️	🧑‍⚕️	🧑‍⚕️	—	—	🧑‍⚕️	—	—	—	—	—	—	health worker
260	U+1F468 U+200D U+2695 U+FE0F	👨‍⚕️	👨‍⚕️	👨‍⚕️	👨‍⚕️	👨‍⚕️	👨‍⚕️	👨‍⚕️	👨‍⚕️	—	—	—	—	man health worker
261	U+1F469 U+200D U+2695 U+FE0F	👩‍⚕️	👩‍⚕️	👩‍⚕️	👩‍⚕️	👩‍⚕️	👩‍⚕️	👩‍⚕️	👩‍⚕️	—	—	—	—	woman health worker
262	U+1F9D1 U+200D U+1F393	🧑‍🎓	🧑‍🎓	🧑‍🎓	—	—	🧑‍🎓	—	—	—	—	—	—	student
263	U+1F468 U+200D U+1F393	👨‍🎓	👨‍🎓	👨‍🎓	👨‍🎓	👨‍🎓	👨‍🎓	👨‍🎓	👨‍🎓	—	—	—	—	man student
264	U+1F469 U+200D U+1F393	👩‍🎓	👩‍🎓	👩‍🎓	👩‍🎓	👩‍🎓	👩‍🎓	👩‍🎓	👩‍🎓	—	—	—	—	woman student
265	U+1F9D1 U+200D U+1F3EB	🧑‍🏫	🧑‍🏫	🧑‍🏫	—	—	🧑‍🏫	—	—	—	—	—	—	teacher
266	U+1F468 U+200D U+1F3EB	👨‍🏫	👨‍🏫	👨‍🏫	👨‍🏫	👨‍🏫	👨‍🏫	👨‍🏫	👨‍🏫	—	—	—	—	man teacher
267	U+1F469 U+200D U+1F3EB	👩‍🏫	👩‍🏫	👩‍🏫	👩‍🏫	👩‍🏫	👩‍🏫	👩‍🏫	👩‍🏫	—	—	—	—	woman teacher
268	U+1F9D1 U+200D U+2696 U+FE0F	🧑‍⚖️	🧑‍⚖️	🧑‍⚖️	—	—	🧑‍⚖️	—	—	—	—	—	—	judge
269	U+1F468 U+200D U+2696 U+FE0F	👨‍⚖️	👨‍⚖️	👨‍⚖️	👨‍⚖️	👨‍⚖️	👨‍⚖️	👨‍⚖️	👨‍⚖️	—	—	—	—	man judge
270	U+1F469 U+200D U+2696 U+FE0F	👩‍⚖️	👩‍⚖️	👩‍⚖️	👩‍⚖️	👩‍⚖️	👩‍⚖️	👩‍⚖️	👩‍⚖️	—	—	—	—	woman judge
271	U+1F9D1 U+200D U+1F33E	🧑‍🌾	🧑‍🌾	🧑‍🌾	—	—	🧑‍🌾	—	—	—	—	—	—	farmer
272	U+1F468 U+200D U+1F33E	👨‍🌾	👨‍🌾	👨‍🌾	👨‍🌾	👨‍🌾	👨‍🌾	👨‍🌾	👨‍🌾	—	—	—	—	man farmer
273	U+1F469 U+200D U+1F33E	👩‍🌾	👩‍🌾	👩‍🌾	👩‍🌾	👩‍🌾	👩‍🌾	👩‍🌾	👩‍🌾	—	—	—	—	woman farmer
274	U+1F9D1 U+200D U+1F373	🧑‍🍳	🧑‍🍳	🧑‍🍳	—	—	🧑‍🍳	—	—	—	—	—	—	cook
275	U+1F468 U+200D U+1F373	👨‍🍳	👨‍🍳	👨‍🍳	👨‍🍳	👨‍🍳	👨‍🍳	👨‍🍳	👨‍🍳	—	—	—	—	man cook
276	U+1F469 U+200D U+1F373	👩‍🍳	👩‍🍳	👩‍🍳	👩‍🍳	👩‍🍳	👩‍🍳	👩‍🍳	👩‍🍳	—	—	—	—	woman cook
277	U+1F9D1 U+200D U+1F527	🧑‍🔧	🧑‍🔧	🧑‍🔧	—	—	🧑‍🔧	—	—	—	—	—	—	mechanic
278	U+1F468 U+200D U+1F527	👨‍🔧	👨‍🔧	👨‍🔧	👨‍🔧	👨‍🔧	👨‍🔧	👨‍🔧	👨‍🔧	—	—	—	—	man mechanic
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
279	U+1F469 U+200D U+1F527	👩‍🔧	👩‍🔧	👩‍🔧	👩‍🔧	👩‍🔧	👩‍🔧	👩‍🔧	👩‍🔧	—	—	—	—	woman mechanic
280	U+1F9D1 U+200D U+1F3ED	🧑‍🏭	🧑‍🏭	🧑‍🏭	—	—	🧑‍🏭	—	—	—	—	—	—	factory worker
281	U+1F468 U+200D U+1F3ED	👨‍🏭	👨‍🏭	👨‍🏭	👨‍🏭	👨‍🏭	👨‍🏭	👨‍🏭	👨‍🏭	—	—	—	—	man factory worker
282	U+1F469 U+200D U+1F3ED	👩‍🏭	👩‍🏭	👩‍🏭	👩‍🏭	👩‍🏭	👩‍🏭	👩‍🏭	👩‍🏭	—	—	—	—	woman factory worker
283	U+1F9D1 U+200D U+1F4BC	🧑‍💼	🧑‍💼	🧑‍💼	—	—	🧑‍💼	—	—	—	—	—	—	office worker
284	U+1F468 U+200D U+1F4BC	👨‍💼	👨‍💼	👨‍💼	👨‍💼	👨‍💼	👨‍💼	👨‍💼	👨‍💼	—	—	—	—	man office worker
285	U+1F469 U+200D U+1F4BC	👩‍💼	👩‍💼	👩‍💼	👩‍💼	👩‍💼	👩‍💼	👩‍💼	👩‍💼	—	—	—	—	woman office worker
286	U+1F9D1 U+200D U+1F52C	🧑‍🔬	🧑‍🔬	🧑‍🔬	—	—	🧑‍🔬	—	—	—	—	—	—	scientist
287	U+1F468 U+200D U+1F52C	👨‍🔬	👨‍🔬	👨‍🔬	👨‍🔬	👨‍🔬	👨‍🔬	👨‍🔬	👨‍🔬	—	—	—	—	man scientist
288	U+1F469 U+200D U+1F52C	👩‍🔬	👩‍🔬	👩‍🔬	👩‍🔬	👩‍🔬	👩‍🔬	👩‍🔬	👩‍🔬	—	—	—	—	woman scientist
289	U+1F9D1 U+200D U+1F4BB	🧑‍💻	🧑‍💻	🧑‍💻	—	—	🧑‍💻	—	—	—	—	—	—	technologist
290	U+1F468 U+200D U+1F4BB	👨‍💻	👨‍💻	👨‍💻	👨‍💻	👨‍💻	👨‍💻	👨‍💻	👨‍💻	—	—	—	—	man technologist
291	U+1F469 U+200D U+1F4BB	👩‍💻	👩‍💻	👩‍💻	👩‍💻	👩‍💻	👩‍💻	👩‍💻	👩‍💻	—	—	—	—	woman technologist
292	U+1F9D1 U+200D U+1F3A4	🧑‍🎤	🧑‍🎤	🧑‍🎤	—	—	🧑‍🎤	—	—	—	—	—	—	singer
293	U+1F468 U+200D U+1F3A4	👨‍🎤	👨‍🎤	👨‍🎤	👨‍🎤	👨‍🎤	👨‍🎤	👨‍🎤	👨‍🎤	—	—	—	—	man singer
294	U+1F469 U+200D U+1F3A4	👩‍🎤	👩‍🎤	👩‍🎤	👩‍🎤	👩‍🎤	👩‍🎤	👩‍🎤	👩‍🎤	—	—	—	—	woman singer
295	U+1F9D1 U+200D U+1F3A8	🧑‍🎨	🧑‍🎨	🧑‍🎨	—	—	🧑‍🎨	—	—	—	—	—	—	artist
296	U+1F468 U+200D U+1F3A8	👨‍🎨	👨‍🎨	👨‍🎨	👨‍🎨	👨‍🎨	👨‍🎨	👨‍🎨	👨‍🎨	—	—	—	—	man artist
297	U+1F469 U+200D U+1F3A8	👩‍🎨	👩‍🎨	👩‍🎨	👩‍🎨	👩‍🎨	👩‍🎨	👩‍🎨	👩‍🎨	—	—	—	—	woman artist
298	U+1F9D1 U+200D U+2708 U+FE0F	🧑‍✈️	🧑‍✈️	🧑‍✈️	—	—	🧑‍✈️	—	—	—	—	—	—	pilot
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
299	U+1F468 U+200D U+2708 U+FE0F	👨‍✈️	👨‍✈️	👨‍✈️	👨‍✈️	👨‍✈️	👨‍✈️	👨‍✈️	👨‍✈️	—	—	—	—	man pilot
300	U+1F469 U+200D U+2708 U+FE0F	👩‍✈️	👩‍✈️	👩‍✈️	👩‍✈️	👩‍✈️	👩‍✈️	👩‍✈️	👩‍✈️	—	—	—	—	woman pilot
301	U+1F9D1 U+200D U+1F680	🧑‍🚀	🧑‍🚀	🧑‍🚀	—	—	🧑‍🚀	—	—	—	—	—	—	astronaut
302	U+1F468 U+200D U+1F680	👨‍🚀	👨‍🚀	👨‍🚀	👨‍🚀	👨‍🚀	👨‍🚀	👨‍🚀	👨‍🚀	—	—	—	—	man astronaut
303	U+1F469 U+200D U+1F680	👩‍🚀	👩‍🚀	👩‍🚀	👩‍🚀	👩‍🚀	👩‍🚀	👩‍🚀	👩‍🚀	—	—	—	—	woman astronaut
304	U+1F9D1 U+200D U+1F692	🧑‍🚒	🧑‍🚒	🧑‍🚒	—	—	🧑‍🚒	—	—	—	—	—	—	firefighter
305	U+1F468 U+200D U+1F692	👨‍🚒	👨‍🚒	👨‍🚒	👨‍🚒	👨‍🚒	👨‍🚒	👨‍🚒	👨‍🚒	—	—	—	—	man firefighter
306	U+1F469 U+200D U+1F692	👩‍🚒	👩‍🚒	👩‍🚒	👩‍🚒	👩‍🚒	👩‍🚒	👩‍🚒	👩‍🚒	—	—	—	—	woman firefighter
307	U+1F46E	👮	👮	👮	👮	👮	👮	👮	👮	👮	👮	—	👮	police officer
308	U+1F46E U+200D U+2642 U+FE0F	👮‍♂️	👮‍♂️	👮‍♂️	👮‍♂️	👮‍♂️	👮‍♂️	👮‍♂️	👮‍♂️	—	—	—	—	man police officer
309	U+1F46E U+200D U+2640 U+FE0F	👮‍♀️	👮‍♀️	👮‍♀️	👮‍♀️	👮‍♀️	👮‍♀️	👮‍♀️	👮‍♀️	—	—	—	—	woman police officer
310	U+1F575	🕵	🕵	🕵	🕵	🕵	🕵	🕵	🕵	—	—	—	—	detective
311	U+1F575 U+FE0F U+200D U+2642 U+FE0F	🕵️‍♂️	🕵️‍♂️	🕵️‍♂️	🕵️‍♂️	🕵️‍♂️	🕵️‍♂️	🕵️‍♂️	🕵️‍♂️	—	—	—	—	man detective
312	U+1F575 U+FE0F U+200D U+2640 U+FE0F	🕵️‍♀️	🕵️‍♀️	🕵️‍♀️	🕵️‍♀️	🕵️‍♀️	🕵️‍♀️	🕵️‍♀️	🕵️‍♀️	—	—	—	—	woman detective
313	U+1F482	💂	💂	💂	💂	💂	💂	💂	💂	💂	💂	—	—	guard
314	U+1F482 U+200D U+2642 U+FE0F	💂‍♂️	💂‍♂️	💂‍♂️	💂‍♂️	💂‍♂️	💂‍♂️	💂‍♂️	💂‍♂️	—	—	—	—	man guard
315	U+1F482 U+200D U+2640 U+FE0F	💂‍♀️	💂‍♀️	💂‍♀️	💂‍♀️	💂‍♀️	💂‍♀️	💂‍♀️	💂‍♀️	—	—	—	—	woman guard
316	U+1F977	🥷	—	🥷	—	—	—	🥷	—	—	—	—	—	⊛ ninja
317	U+1F477	👷	👷	👷	👷	👷	👷	👷	👷	👷	👷	—	👷	construction worker
318	U+1F477 U+200D U+2642 U+FE0F	👷‍♂️	👷‍♂️	👷‍♂️	👷‍♂️	👷‍♂️	👷‍♂️	👷‍♂️	👷‍♂️	—	—	—	—	man construction worker
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
319	U+1F477 U+200D U+2640 U+FE0F	👷‍♀️	👷‍♀️	👷‍♀️	👷‍♀️	👷‍♀️	👷‍♀️	👷‍♀️	👷‍♀️	—	—	—	—	woman construction worker
320	U+1F934	🤴	🤴	🤴	🤴	🤴	🤴	🤴	🤴	—	—	—	—	prince
321	U+1F478	👸	👸	👸	👸	👸	👸	👸	👸	👸	👸	—	👸	princess
322	U+1F473	👳	👳	👳	👳	👳	👳	👳	👳	👳	👳	—	👳	person wearing turban
323	U+1F473 U+200D U+2642 U+FE0F	👳‍♂️	👳‍♂️	👳‍♂️	👳‍♂️	👳‍♂️	👳‍♂️	👳‍♂️	👳‍♂️	—	—	—	—	man wearing turban
324	U+1F473 U+200D U+2640 U+FE0F	👳‍♀️	👳‍♀️	👳‍♀️	👳‍♀️	👳‍♀️	👳‍♀️	👳‍♀️	👳‍♀️	—	—	—	—	woman wearing turban
325	U+1F472	👲	👲	👲	👲	👲	👲	👲	👲	👲	👲	—	👲	person with skullcap
326	U+1F9D5	🧕	🧕	🧕	🧕	🧕	🧕	🧕	🧕	—	—	—	—	woman with headscarf
327	U+1F935	🤵	🤵	🤵	🤵	🤵	🤵	🤵	🤵	—	—	—	—	person in tuxedo
328	U+1F935 U+200D U+2642 U+FE0F	🤵‍♂️	—	🤵‍♂️	—	—	🤵‍♂️	—	—	—	—	—	—	⊛ man in tuxedo
329	U+1F935 U+200D U+2640 U+FE0F	🤵‍♀️	—	🤵‍♀️	—	—	🤵‍♀️	—	—	—	—	—	—	⊛ woman in tuxedo
330	U+1F470	👰	👰	👰	👰	👰	👰	👰	👰	👰	—	—	👰	person with veil
331	U+1F470 U+200D U+2642 U+FE0F	👰‍♂️	… 👰‍♂️ 👰‍♂️ 👰‍♂️ …	⊛ man with veil
332	U+1F470 U+200D U+2640 U+FE0F	👰‍♀️	… 👰‍♀️ 👰‍♀️ …	⊛ woman with veil
333	U+1F930	🤰	🤰	🤰	🤰	🤰	🤰	🤰	🤰	—	—	—	—	pregnant woman
334	U+1F931	🤱	🤱	🤱	🤱	🤱	🤱	🤱	🤱	—	—	—	—	breast-feeding
335	U+1F469 U+200D U+1F37C	👩‍🍼	… 👩‍🍼 👩‍🍼 👩‍🍼 …	⊛ woman feeding baby
336	U+1F468 U+200D U+1F37C	👨‍🍼	… 👨‍🍼 👨‍🍼 👨‍🍼 …	⊛ man feeding baby
337	U+1F9D1 U+200D U+1F37C	🧑‍🍼	… 🧑‍🍼 🧑‍🍼 🧑‍🍼 …	⊛ person feeding baby
person-fantasy
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
338	U+1F47C	👼	👼	👼	👼	👼	👼	👼	👼	👼	👼	—	👼	baby angel
339	U+1F385	🎅	🎅	🎅	🎅	🎅	🎅	🎅	🎅	🎅	🎅	—	🎅	Santa Claus
340	U+1F936	🤶	🤶	🤶	🤶	🤶	🤶	🤶	🤶	—	—	—	—	Mrs. Claus
341	U+1F9D1 U+200D U+1F384	🧑‍🎄	… 🧑‍🎄 🧑‍🎄 🧑‍🎄 …	⊛ mx claus
342	U+1F9B8	🦸	🦸	🦸	🦸	🦸	🦸	🦸	🦸	—	—	—	—	superhero
343	U+1F9B8 U+200D U+2642 U+FE0F	🦸‍♂️	🦸‍♂️	🦸‍♂️	🦸‍♂️	🦸‍♂️	🦸‍♂️	🦸‍♂️	🦸‍♂️	—	—	—	—	man superhero
344	U+1F9B8 U+200D U+2640 U+FE0F	🦸‍♀️	🦸‍♀️	🦸‍♀️	🦸‍♀️	🦸‍♀️	🦸‍♀️	🦸‍♀️	🦸‍♀️	—	—	—	—	woman superhero
345	U+1F9B9	🦹	🦹	🦹	🦹	🦹	🦹	🦹	🦹	—	—	—	—	supervillain
346	U+1F9B9 U+200D U+2642 U+FE0F	🦹‍♂️	🦹‍♂️	🦹‍♂️	🦹‍♂️	🦹‍♂️	🦹‍♂️	🦹‍♂️	🦹‍♂️	—	—	—	—	man supervillain
347	U+1F9B9 U+200D U+2640 U+FE0F	🦹‍♀️	🦹‍♀️	🦹‍♀️	🦹‍♀️	🦹‍♀️	🦹‍♀️	🦹‍♀️	🦹‍♀️	—	—	—	—	woman supervillain
348	U+1F9D9	🧙	🧙	🧙	🧙	🧙	🧙	🧙	🧙	—	—	—	—	mage
349	U+1F9D9 U+200D U+2642 U+FE0F	🧙‍♂️	🧙‍♂️	🧙‍♂️	🧙‍♂️	🧙‍♂️	🧙‍♂️	🧙‍♂️	🧙‍♂️	—	—	—	—	man mage
350	U+1F9D9 U+200D U+2640 U+FE0F	🧙‍♀️	🧙‍♀️	🧙‍♀️	🧙‍♀️	🧙‍♀️	🧙‍♀️	🧙‍♀️	🧙‍♀️	—	—	—	—	woman mage
351	U+1F9DA	🧚	🧚	🧚	🧚	🧚	🧚	🧚	🧚	—	—	—	—	fairy
352	U+1F9DA U+200D U+2642 U+FE0F	🧚‍♂️	🧚‍♂️	🧚‍♂️	🧚‍♂️	🧚‍♂️	🧚‍♂️	🧚‍♂️	🧚‍♂️	—	—	—	—	man fairy
353	U+1F9DA U+200D U+2640 U+FE0F	🧚‍♀️	🧚‍♀️	🧚‍♀️	🧚‍♀️	🧚‍♀️	🧚‍♀️	🧚‍♀️	🧚‍♀️	—	—	—	—	woman fairy
354	U+1F9DB	🧛	🧛	🧛	🧛	🧛	🧛	🧛	🧛	—	—	—	—	vampire
355	U+1F9DB U+200D U+2642 U+FE0F	🧛‍♂️	🧛‍♂️	🧛‍♂️	🧛‍♂️	🧛‍♂️	🧛‍♂️	🧛‍♂️	🧛‍♂️	—	—	—	—	man vampire
356	U+1F9DB U+200D U+2640 U+FE0F	🧛‍♀️	🧛‍♀️	🧛‍♀️	🧛‍♀️	🧛‍♀️	🧛‍♀️	🧛‍♀️	🧛‍♀️	—	—	—	—	woman vampire
357	U+1F9DC	🧜	🧜	🧜	🧜	🧜	🧜	🧜	🧜	—	—	—	—	merperson
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
358	U+1F9DC U+200D U+2642 U+FE0F	🧜‍♂️	🧜‍♂️	🧜‍♂️	🧜‍♂️	🧜‍♂️	🧜‍♂️	🧜‍♂️	🧜‍♂️	—	—	—	—	merman
359	U+1F9DC U+200D U+2640 U+FE0F	🧜‍♀️	🧜‍♀️	🧜‍♀️	🧜‍♀️	🧜‍♀️	🧜‍♀️	🧜‍♀️	🧜‍♀️	—	—	—	—	mermaid
360	U+1F9DD	🧝	🧝	🧝	🧝	🧝	🧝	🧝	🧝	—	—	—	—	elf
361	U+1F9DD U+200D U+2642 U+FE0F	🧝‍♂️	🧝‍♂️	🧝‍♂️	🧝‍♂️	🧝‍♂️	🧝‍♂️	🧝‍♂️	🧝‍♂️	—	—	—	—	man elf
362	U+1F9DD U+200D U+2640 U+FE0F	🧝‍♀️	🧝‍♀️	🧝‍♀️	🧝‍♀️	🧝‍♀️	🧝‍♀️	🧝‍♀️	🧝‍♀️	—	—	—	—	woman elf
363	U+1F9DE	🧞	🧞	🧞	🧞	🧞	🧞	🧞	🧞	—	—	—	—	genie
364	U+1F9DE U+200D U+2642 U+FE0F	🧞‍♂️	🧞‍♂️	🧞‍♂️	🧞‍♂️	🧞‍♂️	🧞‍♂️	🧞‍♂️	🧞‍♂️	—	—	—	—	man genie
365	U+1F9DE U+200D U+2640 U+FE0F	🧞‍♀️	🧞‍♀️	🧞‍♀️	🧞‍♀️	🧞‍♀️	🧞‍♀️	🧞‍♀️	🧞‍♀️	—	—	—	—	woman genie
366	U+1F9DF	🧟	🧟	🧟	🧟	🧟	🧟	🧟	🧟	—	—	—	—	zombie
367	U+1F9DF U+200D U+2642 U+FE0F	🧟‍♂️	🧟‍♂️	🧟‍♂️	🧟‍♂️	🧟‍♂️	🧟‍♂️	🧟‍♂️	🧟‍♂️	—	—	—	—	man zombie
368	U+1F9DF U+200D U+2640 U+FE0F	🧟‍♀️	🧟‍♀️	🧟‍♀️	🧟‍♀️	🧟‍♀️	🧟‍♀️	🧟‍♀️	🧟‍♀️	—	—	—	—	woman zombie
person-activity
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
369	U+1F486	💆	💆	💆	💆	💆	💆	💆	💆	💆	💆	—	💆	person getting massage
370	U+1F486 U+200D U+2642 U+FE0F	💆‍♂️	💆‍♂️	💆‍♂️	💆‍♂️	💆‍♂️	💆‍♂️	💆‍♂️	💆‍♂️	—	—	—	—	man getting massage
371	U+1F486 U+200D U+2640 U+FE0F	💆‍♀️	💆‍♀️	💆‍♀️	💆‍♀️	💆‍♀️	💆‍♀️	💆‍♀️	💆‍♀️	—	—	—	—	woman getting massage
372	U+1F487	💇	💇	💇	💇	💇	💇	💇	💇	💇	💇	—	💇	person getting haircut
373	U+1F487 U+200D U+2642 U+FE0F	💇‍♂️	💇‍♂️	💇‍♂️	💇‍♂️	💇‍♂️	💇‍♂️	💇‍♂️	💇‍♂️	—	—	—	—	man getting haircut
374	U+1F487 U+200D U+2640 U+FE0F	💇‍♀️	💇‍♀️	💇‍♀️	💇‍♀️	💇‍♀️	💇‍♀️	💇‍♀️	💇‍♀️	—	—	—	—	woman getting haircut
375	U+1F6B6	🚶	🚶	🚶	🚶	🚶	🚶	🚶	🚶	🚶	🚶	—	🚶	person walking
376	U+1F6B6 U+200D U+2642 U+FE0F	🚶‍♂️	🚶‍♂️	🚶‍♂️	🚶‍♂️	🚶‍♂️	🚶‍♂️	🚶‍♂️	🚶‍♂️	—	—	—	—	man walking
377	U+1F6B6 U+200D U+2640 U+FE0F	🚶‍♀️	🚶‍♀️	🚶‍♀️	🚶‍♀️	🚶‍♀️	🚶‍♀️	🚶‍♀️	🚶‍♀️	—	—	—	—	woman walking
378	U+1F9CD	🧍	🧍	🧍	🧍	🧍	🧍	🧍	🧍	—	—	—	—	person standing
379	U+1F9CD U+200D U+2642 U+FE0F	🧍‍♂️	🧍‍♂️	🧍‍♂️	🧍‍♂️	—	🧍‍♂️	🧍‍♂️	🧍‍♂️	—	—	—	—	man standing
380	U+1F9CD U+200D U+2640 U+FE0F	🧍‍♀️	🧍‍♀️	🧍‍♀️	🧍‍♀️	—	🧍‍♀️	🧍‍♀️	🧍‍♀️	—	—	—	—	woman standing
381	U+1F9CE	🧎	🧎	🧎	🧎	🧎	🧎	🧎	🧎	—	—	—	—	person kneeling
382	U+1F9CE U+200D U+2642 U+FE0F	🧎‍♂️	🧎‍♂️	🧎‍♂️	🧎‍♂️	—	🧎‍♂️	🧎‍♂️	🧎‍♂️	—	—	—	—	man kneeling
383	U+1F9CE U+200D U+2640 U+FE0F	🧎‍♀️	🧎‍♀️	🧎‍♀️	🧎‍♀️	—	🧎‍♀️	🧎‍♀️	🧎‍♀️	—	—	—	—	woman kneeling
384	U+1F9D1 U+200D U+1F9AF	🧑‍🦯	🧑‍🦯	🧑‍🦯	—	—	🧑‍🦯	—	—	—	—	—	—	person with white cane
385	U+1F468 U+200D U+1F9AF	👨‍🦯	👨‍🦯	👨‍🦯	👨‍🦯	—	👨‍🦯	👨‍🦯	👨‍🦯	—	—	—	—	man with white cane
386	U+1F469 U+200D U+1F9AF	👩‍🦯	👩‍🦯	👩‍🦯	👩‍🦯	—	👩‍🦯	👩‍🦯	👩‍🦯	—	—	—	—	woman with white cane
387	U+1F9D1 U+200D U+1F9BC	🧑‍🦼	🧑‍🦼	🧑‍🦼	—	—	🧑‍🦼	—	—	—	—	—	—	person in motorized wheelchair
388	U+1F468 U+200D U+1F9BC	👨‍🦼	👨‍🦼	👨‍🦼	👨‍🦼	👨‍🦼	👨‍🦼	👨‍🦼	👨‍🦼	—	—	—	—	man in motorized wheelchair
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
389	U+1F469 U+200D U+1F9BC	👩‍🦼	👩‍🦼	👩‍🦼	👩‍🦼	👩‍🦼	👩‍🦼	👩‍🦼	👩‍🦼	—	—	—	—	woman in motorized wheelchair
390	U+1F9D1 U+200D U+1F9BD	🧑‍🦽	🧑‍🦽	🧑‍🦽	—	—	🧑‍🦽	—	—	—	—	—	—	person in manual wheelchair
391	U+1F468 U+200D U+1F9BD	👨‍🦽	👨‍🦽	👨‍🦽	👨‍🦽	👨‍🦽	👨‍🦽	👨‍🦽	👨‍🦽	—	—	—	—	man in manual wheelchair
392	U+1F469 U+200D U+1F9BD	👩‍🦽	👩‍🦽	👩‍🦽	👩‍🦽	👩‍🦽	👩‍🦽	👩‍🦽	👩‍🦽	—	—	—	—	woman in manual wheelchair
393	U+1F3C3	🏃	🏃	🏃	🏃	🏃	🏃	🏃	🏃	🏃	🏃	🏃	🏃	person running
394	U+1F3C3 U+200D U+2642 U+FE0F	🏃‍♂️	🏃‍♂️	🏃‍♂️	🏃‍♂️	🏃‍♂️	🏃‍♂️	🏃‍♂️	🏃‍♂️	—	—	—	—	man running
395	U+1F3C3 U+200D U+2640 U+FE0F	🏃‍♀️	🏃‍♀️	🏃‍♀️	🏃‍♀️	🏃‍♀️	🏃‍♀️	🏃‍♀️	🏃‍♀️	—	—	—	—	woman running
396	U+1F483	💃	💃	💃	💃	💃	💃	💃	💃	💃	💃	—	💃	woman dancing
397	U+1F57A	🕺	🕺	🕺	🕺	🕺	🕺	🕺	🕺	—	—	—	—	man dancing
398	U+1F574	🕴	🕴	🕴	🕴	🕴	🕴	🕴	🕴	—	—	—	—	person in suit levitating
399	U+1F46F	👯	👯	👯	👯	👯	👯	👯	👯	👯	👯	—	👯	people with bunny ears
400	U+1F46F U+200D U+2642 U+FE0F	👯‍♂️	👯‍♂️	👯‍♂️	👯‍♂️	👯‍♂️	👯‍♂️	👯‍♂️	👯‍♂️	—	—	—	—	men with bunny ears
401	U+1F46F U+200D U+2640 U+FE0F	👯‍♀️	👯‍♀️	👯‍♀️	👯‍♀️	👯‍♀️	👯‍♀️	👯‍♀️	👯‍♀️	—	—	—	—	women with bunny ears
402	U+1F9D6	🧖	🧖	🧖	🧖	🧖	🧖	🧖	🧖	—	—	—	—	person in steamy room
403	U+1F9D6 U+200D U+2642 U+FE0F	🧖‍♂️	🧖‍♂️	🧖‍♂️	🧖‍♂️	🧖‍♂️	🧖‍♂️	🧖‍♂️	🧖‍♂️	—	—	—	—	man in steamy room
404	U+1F9D6 U+200D U+2640 U+FE0F	🧖‍♀️	🧖‍♀️	🧖‍♀️	🧖‍♀️	🧖‍♀️	🧖‍♀️	🧖‍♀️	🧖‍♀️	—	—	—	—	woman in steamy room
405	U+1F9D7	🧗	🧗	🧗	🧗	🧗	🧗	🧗	🧗	—	—	—	—	person climbing
406	U+1F9D7 U+200D U+2642 U+FE0F	🧗‍♂️	🧗‍♂️	🧗‍♂️	🧗‍♂️	🧗‍♂️	🧗‍♂️	🧗‍♂️	🧗‍♂️	—	—	—	—	man climbing
407	U+1F9D7 U+200D U+2640 U+FE0F	🧗‍♀️	🧗‍♀️	🧗‍♀️	🧗‍♀️	🧗‍♀️	🧗‍♀️	🧗‍♀️	🧗‍♀️	—	—	—	—	woman climbing
person-sport
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
408	U+1F93A	🤺	🤺	🤺	🤺	🤺	🤺	🤺	🤺	—	—	—	—	person fencing
409	U+1F3C7	🏇	🏇	🏇	🏇	🏇	🏇	🏇	🏇	—	—	—	—	horse racing
410	U+26F7	⛷	⛷	⛷	⛷	⛷	⛷	⛷	⛷	—	—	—	—	skier
411	U+1F3C2	🏂	🏂	🏂	🏂	🏂	🏂	🏂	🏂	🏂	—	🏂	🏂	snowboarder
412	U+1F3CC	🏌	🏌	🏌	🏌	🏌	🏌	🏌	🏌	—	—	—	—	person golfing
413	U+1F3CC U+FE0F U+200D U+2642 U+FE0F	🏌️‍♂️	🏌️‍♂️	🏌️‍♂️	🏌️‍♂️	🏌️‍♂️	🏌️‍♂️	🏌️‍♂️	🏌️‍♂️	—	—	—	—	man golfing
414	U+1F3CC U+FE0F U+200D U+2640 U+FE0F	🏌️‍♀️	🏌️‍♀️	🏌️‍♀️	🏌️‍♀️	🏌️‍♀️	🏌️‍♀️	🏌️‍♀️	🏌️‍♀️	—	—	—	—	woman golfing
415	U+1F3C4	🏄	🏄	🏄	🏄	🏄	🏄	🏄	🏄	🏄	🏄	—	🏄	person surfing
416	U+1F3C4 U+200D U+2642 U+FE0F	🏄‍♂️	🏄‍♂️	🏄‍♂️	🏄‍♂️	🏄‍♂️	🏄‍♂️	🏄‍♂️	🏄‍♂️	—	—	—	—	man surfing
417	U+1F3C4 U+200D U+2640 U+FE0F	🏄‍♀️	🏄‍♀️	🏄‍♀️	🏄‍♀️	🏄‍♀️	🏄‍♀️	🏄‍♀️	🏄‍♀️	—	—	—	—	woman surfing
418	U+1F6A3	🚣	🚣	🚣	🚣	🚣	🚣	🚣	🚣	—	—	—	—	person rowing boat
419	U+1F6A3 U+200D U+2642 U+FE0F	🚣‍♂️	🚣‍♂️	🚣‍♂️	🚣‍♂️	🚣‍♂️	🚣‍♂️	🚣‍♂️	🚣‍♂️	—	—	—	—	man rowing boat
420	U+1F6A3 U+200D U+2640 U+FE0F	🚣‍♀️	🚣‍♀️	🚣‍♀️	🚣‍♀️	🚣‍♀️	🚣‍♀️	🚣‍♀️	🚣‍♀️	—	—	—	—	woman rowing boat
421	U+1F3CA	🏊	🏊	🏊	🏊	🏊	🏊	🏊	🏊	🏊	🏊	—	🏊	person swimming
422	U+1F3CA U+200D U+2642 U+FE0F	🏊‍♂️	🏊‍♂️	🏊‍♂️	🏊‍♂️	🏊‍♂️	🏊‍♂️	🏊‍♂️	🏊‍♂️	—	—	—	—	man swimming
423	U+1F3CA U+200D U+2640 U+FE0F	🏊‍♀️	🏊‍♀️	🏊‍♀️	🏊‍♀️	🏊‍♀️	🏊‍♀️	🏊‍♀️	🏊‍♀️	—	—	—	—	woman swimming
424	U+26F9	⛹	⛹	⛹	⛹	⛹	⛹	⛹	⛹	—	—	—	—	person bouncing ball
425	U+26F9 U+FE0F U+200D U+2642 U+FE0F	⛹️‍♂️	⛹️‍♂️	⛹️‍♂️	⛹️‍♂️	⛹️‍♂️	⛹️‍♂️	⛹️‍♂️	⛹️‍♂️	—	—	—	—	man bouncing ball
426	U+26F9 U+FE0F U+200D U+2640 U+FE0F	⛹️‍♀️	⛹️‍♀️	⛹️‍♀️	⛹️‍♀️	⛹️‍♀️	⛹️‍♀️	⛹️‍♀️	⛹️‍♀️	—	—	—	—	woman bouncing ball
427	U+1F3CB	🏋	🏋	🏋	🏋	🏋	🏋	🏋	🏋	—	—	—	—	person lifting weights
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
428	U+1F3CB U+FE0F U+200D U+2642 U+FE0F	🏋️‍♂️	🏋️‍♂️	🏋️‍♂️	🏋️‍♂️	🏋️‍♂️	🏋️‍♂️	🏋️‍♂️	🏋️‍♂️	—	—	—	—	man lifting weights
429	U+1F3CB U+FE0F U+200D U+2640 U+FE0F	🏋️‍♀️	🏋️‍♀️	🏋️‍♀️	🏋️‍♀️	🏋️‍♀️	🏋️‍♀️	🏋️‍♀️	🏋️‍♀️	—	—	—	—	woman lifting weights
430	U+1F6B4	🚴	🚴	🚴	🚴	🚴	🚴	🚴	🚴	—	—	—	—	person biking
431	U+1F6B4 U+200D U+2642 U+FE0F	🚴‍♂️	🚴‍♂️	🚴‍♂️	🚴‍♂️	🚴‍♂️	🚴‍♂️	🚴‍♂️	🚴‍♂️	—	—	—	—	man biking
432	U+1F6B4 U+200D U+2640 U+FE0F	🚴‍♀️	🚴‍♀️	🚴‍♀️	🚴‍♀️	🚴‍♀️	🚴‍♀️	🚴‍♀️	🚴‍♀️	—	—	—	—	woman biking
433	U+1F6B5	🚵	🚵	🚵	🚵	🚵	🚵	🚵	🚵	—	—	—	—	person mountain biking
434	U+1F6B5 U+200D U+2642 U+FE0F	🚵‍♂️	🚵‍♂️	🚵‍♂️	🚵‍♂️	🚵‍♂️	🚵‍♂️	🚵‍♂️	🚵‍♂️	—	—	—	—	man mountain biking
435	U+1F6B5 U+200D U+2640 U+FE0F	🚵‍♀️	🚵‍♀️	🚵‍♀️	🚵‍♀️	🚵‍♀️	🚵‍♀️	🚵‍♀️	🚵‍♀️	—	—	—	—	woman mountain biking
436	U+1F938	🤸	🤸	🤸	🤸	🤸	🤸	🤸	🤸	—	—	—	—	person cartwheeling
437	U+1F938 U+200D U+2642 U+FE0F	🤸‍♂️	🤸‍♂️	🤸‍♂️	🤸‍♂️	🤸‍♂️	🤸‍♂️	🤸‍♂️	🤸‍♂️	—	—	—	—	man cartwheeling
438	U+1F938 U+200D U+2640 U+FE0F	🤸‍♀️	🤸‍♀️	🤸‍♀️	🤸‍♀️	🤸‍♀️	🤸‍♀️	🤸‍♀️	🤸‍♀️	—	—	—	—	woman cartwheeling
439	U+1F93C	🤼	🤼	🤼	🤼	🤼	🤼	🤼	🤼	—	—	—	—	people wrestling
440	U+1F93C U+200D U+2642 U+FE0F	🤼‍♂️	🤼‍♂️	🤼‍♂️	🤼‍♂️	🤼‍♂️	🤼‍♂️	🤼‍♂️	🤼‍♂️	—	—	—	—	men wrestling
441	U+1F93C U+200D U+2640 U+FE0F	🤼‍♀️	🤼‍♀️	🤼‍♀️	🤼‍♀️	🤼‍♀️	🤼‍♀️	🤼‍♀️	🤼‍♀️	—	—	—	—	women wrestling
442	U+1F93D	🤽	🤽	🤽	🤽	🤽	🤽	🤽	🤽	—	—	—	—	person playing water polo
443	U+1F93D U+200D U+2642 U+FE0F	🤽‍♂️	🤽‍♂️	🤽‍♂️	🤽‍♂️	🤽‍♂️	🤽‍♂️	🤽‍♂️	🤽‍♂️	—	—	—	—	man playing water polo
444	U+1F93D U+200D U+2640 U+FE0F	🤽‍♀️	🤽‍♀️	🤽‍♀️	🤽‍♀️	🤽‍♀️	🤽‍♀️	🤽‍♀️	🤽‍♀️	—	—	—	—	woman playing water polo
445	U+1F93E	🤾	🤾	🤾	🤾	🤾	🤾	🤾	🤾	—	—	—	—	person playing handball
446	U+1F93E U+200D U+2642 U+FE0F	🤾‍♂️	🤾‍♂️	🤾‍♂️	🤾‍♂️	🤾‍♂️	🤾‍♂️	🤾‍♂️	🤾‍♂️	—	—	—	—	man playing handball
447	U+1F93E U+200D U+2640 U+FE0F	🤾‍♀️	🤾‍♀️	🤾‍♀️	🤾‍♀️	🤾‍♀️	🤾‍♀️	🤾‍♀️	🤾‍♀️	—	—	—	—	woman playing handball
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
448	U+1F939	🤹	🤹	🤹	🤹	🤹	🤹	🤹	🤹	—	—	—	—	person juggling
449	U+1F939 U+200D U+2642 U+FE0F	🤹‍♂️	🤹‍♂️	🤹‍♂️	🤹‍♂️	🤹‍♂️	🤹‍♂️	🤹‍♂️	🤹‍♂️	—	—	—	—	man juggling
450	U+1F939 U+200D U+2640 U+FE0F	🤹‍♀️	🤹‍♀️	🤹‍♀️	🤹‍♀️	🤹‍♀️	🤹‍♀️	🤹‍♀️	🤹‍♀️	—	—	—	—	woman juggling
person-resting
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
451	U+1F9D8	🧘	🧘	🧘	🧘	🧘	🧘	🧘	🧘	—	—	—	—	person in lotus position
452	U+1F9D8 U+200D U+2642 U+FE0F	🧘‍♂️	🧘‍♂️	🧘‍♂️	🧘‍♂️	🧘‍♂️	🧘‍♂️	🧘‍♂️	🧘‍♂️	—	—	—	—	man in lotus position
453	U+1F9D8 U+200D U+2640 U+FE0F	🧘‍♀️	🧘‍♀️	🧘‍♀️	🧘‍♀️	🧘‍♀️	🧘‍♀️	🧘‍♀️	🧘‍♀️	—	—	—	—	woman in lotus position
454	U+1F6C0	🛀	🛀	🛀	🛀	🛀	🛀	🛀	🛀	🛀	🛀	—	🛀	person taking bath
455	U+1F6CC	🛌	🛌	🛌	🛌	🛌	🛌	🛌	🛌	—	—	—	—	person in bed
family
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
456	U+1F9D1 U+200D U+1F91D U+200D U+1F9D1	🧑‍🤝‍🧑	🧑‍🤝‍🧑	🧑‍🤝‍🧑	🧑‍🤝‍🧑	🧑‍🤝‍🧑	🧑‍🤝‍🧑	🧑‍🤝‍🧑	🧑‍🤝‍🧑	—	—	—	—	people holding hands
457	U+1F46D	👭	👭	👭	👭	👭	👭	👭	👭	—	—	—	—	women holding hands
458	U+1F46B	👫	👫	👫	👫	👫	👫	👫	👫	👫	👫	—	—	woman and man holding hands
459	U+1F46C	👬	👬	👬	👬	👬	👬	👬	👬	—	—	—	—	men holding hands
460	U+1F48F	💏	💏	💏	💏	💏	💏	💏	💏	💏	💏	—	💏	kiss
461	U+1F469 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F468	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	👩‍❤️‍💋‍👨	—	—	—	—	kiss: woman, man
462	U+1F468 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F468	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	👨‍❤️‍💋‍👨	—	—	—	—	kiss: man, man
463	U+1F469 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F469	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	👩‍❤️‍💋‍👩	—	—	—	—	kiss: woman, woman
464	U+1F491	💑	💑	💑	💑	💑	💑	💑	💑	💑	💑	—	💑	couple with heart
465	U+1F469 U+200D U+2764 U+FE0F U+200D U+1F468	👩‍❤️‍👨	👩‍❤️‍👨	👩‍❤️‍👨	👩‍❤️‍👨	👩‍❤️‍👨	👩‍❤️‍👨	👩‍❤️‍👨	👩‍❤️‍👨	—	—	—	—	couple with heart: woman, man
466	U+1F468 U+200D U+2764 U+FE0F U+200D U+1F468	👨‍❤️‍👨	👨‍❤️‍👨	👨‍❤️‍👨	👨‍❤️‍👨	👨‍❤️‍👨	👨‍❤️‍👨	👨‍❤️‍👨	👨‍❤️‍👨	—	—	—	—	couple with heart: man, man
467	U+1F469 U+200D U+2764 U+FE0F U+200D U+1F469	👩‍❤️‍👩	👩‍❤️‍👩	👩‍❤️‍👩	👩‍❤️‍👩	👩‍❤️‍👩	👩‍❤️‍👩	👩‍❤️‍👩	👩‍❤️‍👩	—	—	—	—	couple with heart: woman, woman
468	U+1F46A	👪	👪	👪	👪	👪	👪	👪	👪	👪	—	—	👪	family
469	U+1F468 U+200D U+1F469 U+200D U+1F466	👨‍👩‍👦	👨‍👩‍👦	👨‍👩‍👦	👨‍👩‍👦	👨‍👩‍👦	👨‍👩‍👦	👨‍👩‍👦	👨‍👩‍👦	—	—	—	—	family: man, woman, boy
470	U+1F468 U+200D U+1F469 U+200D U+1F467	👨‍👩‍👧	👨‍👩‍👧	👨‍👩‍👧	👨‍👩‍👧	👨‍👩‍👧	👨‍👩‍👧	👨‍👩‍👧	👨‍👩‍👧	—	—	—	—	family: man, woman, girl
471	U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	👨‍👩‍👧‍👦	—	—	—	—	family: man, woman, girl, boy
472	U+1F468 U+200D U+1F469 U+200D U+1F466 U+200D U+1F466	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	👨‍👩‍👦‍👦	—	—	—	—	family: man, woman, boy, boy
473	U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F467	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	👨‍👩‍👧‍👧	—	—	—	—	family: man, woman, girl, girl
474	U+1F468 U+200D U+1F468 U+200D U+1F466	👨‍👨‍👦	👨‍👨‍👦	👨‍👨‍👦	👨‍👨‍👦	👨‍👨‍👦	👨‍👨‍👦	👨‍👨‍👦	👨‍👨‍👦	—	—	—	—	family: man, man, boy
475	U+1F468 U+200D U+1F468 U+200D U+1F467	👨‍👨‍👧	👨‍👨‍👧	👨‍👨‍👧	👨‍👨‍👧	👨‍👨‍👧	👨‍👨‍👧	👨‍👨‍👧	👨‍👨‍👧	—	—	—	—	family: man, man, girl
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
476	U+1F468 U+200D U+1F468 U+200D U+1F467 U+200D U+1F466	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	👨‍👨‍👧‍👦	—	—	—	—	family: man, man, girl, boy
477	U+1F468 U+200D U+1F468 U+200D U+1F466 U+200D U+1F466	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	👨‍👨‍👦‍👦	—	—	—	—	family: man, man, boy, boy
478	U+1F468 U+200D U+1F468 U+200D U+1F467 U+200D U+1F467	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	👨‍👨‍👧‍👧	—	—	—	—	family: man, man, girl, girl
479	U+1F469 U+200D U+1F469 U+200D U+1F466	👩‍👩‍👦	👩‍👩‍👦	👩‍👩‍👦	👩‍👩‍👦	👩‍👩‍👦	👩‍👩‍👦	👩‍👩‍👦	👩‍👩‍👦	—	—	—	—	family: woman, woman, boy
480	U+1F469 U+200D U+1F469 U+200D U+1F467	👩‍👩‍👧	👩‍👩‍👧	👩‍👩‍👧	👩‍👩‍👧	👩‍👩‍👧	👩‍👩‍👧	👩‍👩‍👧	👩‍👩‍👧	—	—	—	—	family: woman, woman, girl
481	U+1F469 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	👩‍👩‍👧‍👦	—	—	—	—	family: woman, woman, girl, boy
482	U+1F469 U+200D U+1F469 U+200D U+1F466 U+200D U+1F466	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	👩‍👩‍👦‍👦	—	—	—	—	family: woman, woman, boy, boy
483	U+1F469 U+200D U+1F469 U+200D U+1F467 U+200D U+1F467	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	👩‍👩‍👧‍👧	—	—	—	—	family: woman, woman, girl, girl
484	U+1F468 U+200D U+1F466	👨‍👦	👨‍👦	👨‍👦	👨‍👦	👨‍👦	👨‍👦	👨‍👦	👨‍👦	—	—	—	—	family: man, boy
485	U+1F468 U+200D U+1F466 U+200D U+1F466	👨‍👦‍👦	👨‍👦‍👦	👨‍👦‍👦	👨‍👦‍👦	👨‍👦‍👦	👨‍👦‍👦	👨‍👦‍👦	👨‍👦‍👦	—	—	—	—	family: man, boy, boy
486	U+1F468 U+200D U+1F467	👨‍👧	👨‍👧	👨‍👧	👨‍👧	👨‍👧	👨‍👧	👨‍👧	👨‍👧	—	—	—	—	family: man, girl
487	U+1F468 U+200D U+1F467 U+200D U+1F466	👨‍👧‍👦	👨‍👧‍👦	👨‍👧‍👦	👨‍👧‍👦	👨‍👧‍👦	👨‍👧‍👦	👨‍👧‍👦	👨‍👧‍👦	—	—	—	—	family: man, girl, boy
488	U+1F468 U+200D U+1F467 U+200D U+1F467	👨‍👧‍👧	👨‍👧‍👧	👨‍👧‍👧	👨‍👧‍👧	👨‍👧‍👧	👨‍👧‍👧	👨‍👧‍👧	👨‍👧‍👧	—	—	—	—	family: man, girl, girl
489	U+1F469 U+200D U+1F466	👩‍👦	👩‍👦	👩‍👦	👩‍👦	👩‍👦	👩‍👦	👩‍👦	👩‍👦	—	—	—	—	family: woman, boy
490	U+1F469 U+200D U+1F466 U+200D U+1F466	👩‍👦‍👦	👩‍👦‍👦	👩‍👦‍👦	👩‍👦‍👦	👩‍👦‍👦	👩‍👦‍👦	👩‍👦‍👦	👩‍👦‍👦	—	—	—	—	family: woman, boy, boy
491	U+1F469 U+200D U+1F467	👩‍👧	👩‍👧	👩‍👧	👩‍👧	👩‍👧	👩‍👧	👩‍👧	👩‍👧	—	—	—	—	family: woman, girl
492	U+1F469 U+200D U+1F467 U+200D U+1F466	👩‍👧‍👦	👩‍👧‍👦	👩‍👧‍👦	👩‍👧‍👦	👩‍👧‍👦	👩‍👧‍👦	👩‍👧‍👦	👩‍👧‍👦	—	—	—	—	family: woman, girl, boy
493	U+1F469 U+200D U+1F467 U+200D U+1F467	👩‍👧‍👧	👩‍👧‍👧	👩‍👧‍👧	👩‍👧‍👧	👩‍👧‍👧	👩‍👧‍👧	👩‍👧‍👧	👩‍👧‍👧	—	—	—	—	family: woman, girl, girl
person-symbol
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
494	U+1F5E3	🗣	🗣	🗣	🗣	🗣	🗣	🗣	🗣	—	—	—	—	speaking head
495	U+1F464	👤	👤	👤	👤	👤	👤	👤	👤	👤	—	👤	—	bust in silhouette
496	U+1F465	👥	👥	👥	👥	👥	👥	👥	👥	—	—	—	—	busts in silhouette
497	U+1FAC2	🫂	—	🫂	—	—	—	🫂	—	—	—	—	—	⊛ people hugging
498	U+1F463	👣	👣	👣	👣	👣	👣	👣	👣	👣	👣	👣	👣	footprints
Component
hair-style
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
499	U+1F9B0	🦰	🦰	🦰	🦰	🦰	🦰	🦰	🦰	—	—	—	—	red hair
500	U+1F9B1	🦱	🦱	🦱	🦱	🦱	🦱	🦱	🦱	—	—	—	—	curly hair
501	U+1F9B3	🦳	🦳	🦳	🦳	🦳	🦳	🦳	🦳	—	—	—	—	white hair
502	U+1F9B2	🦲	🦲	🦲	🦲	🦲	🦲	🦲	🦲	—	—	—	—	bald
Animals & Nature
animal-mammal
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
503	U+1F435	🐵	🐵	🐵	🐵	🐵	🐵	🐵	🐵	🐵	🐵	—	🐵	monkey face
504	U+1F412	🐒	🐒	🐒	🐒	🐒	🐒	🐒	🐒	🐒	🐒	—	—	monkey
505	U+1F98D	🦍	🦍	🦍	🦍	🦍	🦍	🦍	🦍	—	—	—	—	gorilla
506	U+1F9A7	🦧	🦧	🦧	🦧	🦧	🦧	🦧	🦧	—	—	—	—	orangutan
507	U+1F436	🐶	🐶	🐶	🐶	🐶	🐶	🐶	🐶	🐶	🐶	🐶	🐶	dog face
508	U+1F415	🐕	🐕	🐕	🐕	🐕	🐕	🐕	🐕	—	—	—	—	dog
509	U+1F9AE	🦮	🦮	🦮	🦮	🦮	🦮	🦮	🦮	—	—	—	—	guide dog
510	U+1F415 U+200D U+1F9BA	🐕‍🦺	🐕‍🦺	🐕‍🦺	🐕‍🦺	🐕‍🦺	🐕‍🦺	🐕‍🦺	🐕‍🦺	—	—	—	—	service dog
511	U+1F429	🐩	🐩	🐩	🐩	🐩	🐩	🐩	🐩	🐩	—	—	🐩	poodle
512	U+1F43A	🐺	🐺	🐺	🐺	🐺	🐺	🐺	🐺	🐺	🐺	—	—	wolf
513	U+1F98A	🦊	🦊	🦊	🦊	🦊	🦊	🦊	🦊	—	—	—	—	fox
514	U+1F99D	🦝	🦝	🦝	🦝	🦝	🦝	🦝	🦝	—	—	—	—	raccoon
515	U+1F431	🐱	🐱	🐱	🐱	🐱	🐱	🐱	🐱	🐱	🐱	🐱	🐱	cat face
516	U+1F408	🐈	🐈	🐈	🐈	🐈	🐈	🐈	🐈	—	—	—	—	cat
517	U+1F408 U+200D U+2B1B	🐈‍⬛	… 🐈‍⬛ 🐈‍⬛ 🐈‍⬛ …	⊛ black cat
518	U+1F981	🦁	🦁	🦁	🦁	🦁	🦁	🦁	🦁	—	—	—	—	lion
519	U+1F42F	🐯	🐯	🐯	🐯	🐯	🐯	🐯	🐯	🐯	🐯	—	🐯	tiger face
520	U+1F405	🐅	🐅	🐅	🐅	🐅	🐅	🐅	🐅	—	—	—	—	tiger
521	U+1F406	🐆	🐆	🐆	🐆	🐆	🐆	🐆	🐆	—	—	—	—	leopard
522	U+1F434	🐴	🐴	🐴	🐴	🐴	🐴	🐴	🐴	🐴	🐴	🐴	🐴	horse face
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
523	U+1F40E	🐎	🐎	🐎	🐎	🐎	🐎	🐎	🐎	🐎	🐎	—	—	horse
524	U+1F984	🦄	🦄	🦄	🦄	🦄	🦄	🦄	🦄	—	—	—	—	unicorn
525	U+1F993	🦓	🦓	🦓	🦓	🦓	🦓	🦓	🦓	—	—	—	—	zebra
526	U+1F98C	🦌	🦌	🦌	🦌	🦌	🦌	🦌	🦌	—	—	—	—	deer
527	U+1F9AC	🦬	… 🦬 🦬 🦬 …	⊛ bison
528	U+1F42E	🐮	🐮	🐮	🐮	🐮	🐮	🐮	🐮	🐮	🐮	—	🐮	cow face
529	U+1F402	🐂	🐂	🐂	🐂	🐂	🐂	🐂	🐂	—	—	—	—	ox
530	U+1F403	🐃	🐃	🐃	🐃	🐃	🐃	🐃	🐃	—	—	—	—	water buffalo
531	U+1F404	🐄	🐄	🐄	🐄	🐄	🐄	🐄	🐄	—	—	—	—	cow
532	U+1F437	🐷	🐷	🐷	🐷	🐷	🐷	🐷	🐷	🐷	🐷	🐷	🐷	pig face
533	U+1F416	🐖	🐖	🐖	🐖	🐖	🐖	🐖	🐖	—	—	—	—	pig
534	U+1F417	🐗	🐗	🐗	🐗	🐗	🐗	🐗	🐗	🐗	🐗	—	🐗	boar
535	U+1F43D	🐽	🐽	🐽	🐽	🐽	🐽	🐽	🐽	🐽	—	—	🐽	pig nose
536	U+1F40F	🐏	🐏	🐏	🐏	🐏	🐏	🐏	🐏	—	—	—	—	ram
537	U+1F411	🐑	🐑	🐑	🐑	🐑	🐑	🐑	🐑	🐑	🐑	—	—	ewe
538	U+1F410	🐐	🐐	🐐	🐐	🐐	🐐	🐐	🐐	—	—	—	—	goat
539	U+1F42A	🐪	🐪	🐪	🐪	🐪	🐪	🐪	🐪	—	—	—	—	camel
540	U+1F42B	🐫	🐫	🐫	🐫	🐫	🐫	🐫	🐫	🐫	🐫	—	🐫	two-hump camel
541	U+1F999	🦙	🦙	🦙	🦙	🦙	🦙	🦙	🦙	—	—	—	—	llama
542	U+1F992	🦒	🦒	🦒	🦒	🦒	🦒	🦒	🦒	—	—	—	—	giraffe
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
543	U+1F418	🐘	🐘	🐘	🐘	🐘	🐘	🐘	🐘	🐘	🐘	—	🐘	elephant
544	U+1F9A3	🦣	… 🦣 🦣 🦣 …	⊛ mammoth
545	U+1F98F	🦏	🦏	🦏	🦏	🦏	🦏	🦏	🦏	—	—	—	—	rhinoceros
546	U+1F99B	🦛	🦛	🦛	🦛	🦛	🦛	🦛	🦛	—	—	—	—	hippopotamus
547	U+1F42D	🐭	🐭	🐭	🐭	🐭	🐭	🐭	🐭	🐭	🐭	—	🐭	mouse face
548	U+1F401	🐁	🐁	🐁	🐁	🐁	🐁	🐁	🐁	—	—	—	—	mouse
549	U+1F400	🐀	🐀	🐀	🐀	🐀	🐀	🐀	🐀	—	—	—	—	rat
550	U+1F439	🐹	🐹	🐹	🐹	🐹	🐹	🐹	🐹	🐹	🐹	—	—	hamster
551	U+1F430	🐰	🐰	🐰	🐰	🐰	🐰	🐰	🐰	🐰	🐰	—	🐰	rabbit face
552	U+1F407	🐇	🐇	🐇	🐇	🐇	🐇	🐇	🐇	—	—	—	—	rabbit
553	U+1F43F	🐿	🐿	🐿	🐿	🐿	🐿	🐿	🐿	—	—	—	—	chipmunk
554	U+1F9AB	🦫	… 🦫 🦫 🦫 …	⊛ beaver
555	U+1F994	🦔	🦔	🦔	🦔	🦔	🦔	🦔	🦔	—	—	—	—	hedgehog
556	U+1F987	🦇	🦇	🦇	🦇	🦇	🦇	🦇	🦇	—	—	—	—	bat
557	U+1F43B	🐻	🐻	🐻	🐻	🐻	🐻	🐻	🐻	🐻	🐻	—	🐻	bear
558	U+1F43B U+200D U+2744 U+FE0F	🐻‍❄️	—	🐻‍❄️	—	—	—	🐻‍❄️	—	—	—	—	—	⊛ polar bear
559	U+1F428	🐨	🐨	🐨	🐨	🐨	🐨	🐨	🐨	🐨	🐨	—	🐨	koala
560	U+1F43C	🐼	🐼	🐼	🐼	🐼	🐼	🐼	🐼	🐼	—	—	🐼	panda
561	U+1F9A5	🦥	🦥	🦥	🦥	🦥	🦥	🦥	🦥	—	—	—	—	sloth
562	U+1F9A6	🦦	🦦	🦦	🦦	🦦	🦦	🦦	🦦	—	—	—	—	otter
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
563	U+1F9A8	🦨	🦨	🦨	🦨	🦨	🦨	🦨	🦨	—	—	—	—	skunk
564	U+1F998	🦘	🦘	🦘	🦘	🦘	🦘	🦘	🦘	—	—	—	—	kangaroo
565	U+1F9A1	🦡	🦡	🦡	🦡	🦡	🦡	🦡	🦡	—	—	—	—	badger
566	U+1F43E	🐾	🐾	🐾	🐾	🐾	🐾	🐾	🐾	🐾	—	—	🐾	paw prints
animal-bird
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
567	U+1F983	🦃	🦃	🦃	🦃	🦃	🦃	🦃	🦃	—	—	—	—	turkey
568	U+1F414	🐔	🐔	🐔	🐔	🐔	🐔	🐔	🐔	🐔	🐔	—	🐔	chicken
569	U+1F413	🐓	🐓	🐓	🐓	🐓	🐓	🐓	🐓	—	—	—	—	rooster
570	U+1F423	🐣	🐣	🐣	🐣	🐣	🐣	🐣	🐣	🐣	—	—	🐣	hatching chick
571	U+1F424	🐤	🐤	🐤	🐤	🐤	🐤	🐤	🐤	🐤	🐤	🐤	🐤	baby chick
572	U+1F425	🐥	🐥	🐥	🐥	🐥	🐥	🐥	🐥	🐥	—	—	🐥	front-facing baby chick
573	U+1F426	🐦	🐦	🐦	🐦	🐦	🐦	🐦	🐦	🐦	🐦	—	—	bird
574	U+1F427	🐧	🐧	🐧	🐧	🐧	🐧	🐧	🐧	🐧	🐧	🐧	🐧	penguin
575	U+1F54A	🕊	🕊	🕊	🕊	🕊	🕊	🕊	🕊	—	—	—	—	dove
576	U+1F985	🦅	🦅	🦅	🦅	🦅	🦅	🦅	🦅	—	—	—	—	eagle
577	U+1F986	🦆	🦆	🦆	🦆	🦆	🦆	🦆	🦆	—	—	—	—	duck
578	U+1F9A2	🦢	🦢	🦢	🦢	🦢	🦢	🦢	🦢	—	—	—	—	swan
579	U+1F989	🦉	🦉	🦉	🦉	🦉	🦉	🦉	🦉	—	—	—	—	owl
580	U+1F9A4	🦤	… 🦤 🦤 🦤 …	⊛ dodo
581	U+1FAB6	🪶	—	🪶	—	—	—	🪶	—	—	—	—	—	⊛ feather
582	U+1F9A9	🦩	🦩	🦩	🦩	🦩	🦩	🦩	🦩	—	—	—	—	flamingo
583	U+1F99A	🦚	🦚	🦚	🦚	🦚	🦚	🦚	🦚	—	—	—	—	peacock
584	U+1F99C	🦜	🦜	🦜	🦜	🦜	🦜	🦜	🦜	—	—	—	—	parrot
animal-amphibian
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
585	U+1F438	🐸	🐸	🐸	🐸	🐸	🐸	🐸	🐸	🐸	🐸	—	🐸	frog
animal-reptile
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
586	U+1F40A	🐊	🐊	🐊	🐊	🐊	🐊	🐊	🐊	—	—	—	—	crocodile
587	U+1F422	🐢	🐢	🐢	🐢	🐢	🐢	🐢	🐢	🐢	—	—	🐢	turtle
588	U+1F98E	🦎	🦎	🦎	🦎	🦎	🦎	🦎	🦎	—	—	—	—	lizard
589	U+1F40D	🐍	🐍	🐍	🐍	🐍	🐍	🐍	🐍	🐍	🐍	—	🐍	snake
590	U+1F432	🐲	🐲	🐲	🐲	🐲	🐲	🐲	🐲	🐲	—	—	🐲	dragon face
591	U+1F409	🐉	🐉	🐉	🐉	🐉	🐉	🐉	🐉	—	—	—	—	dragon
592	U+1F995	🦕	🦕	🦕	🦕	🦕	🦕	🦕	🦕	—	—	—	—	sauropod
593	U+1F996	🦖	🦖	🦖	🦖	🦖	🦖	🦖	🦖	—	—	—	—	T-Rex
animal-marine
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
594	U+1F433	🐳	🐳	🐳	🐳	🐳	🐳	🐳	🐳	🐳	🐳	—	🐳	spouting whale
595	U+1F40B	🐋	🐋	🐋	🐋	🐋	🐋	🐋	🐋	—	—	—	—	whale
596	U+1F42C	🐬	🐬	🐬	🐬	🐬	🐬	🐬	🐬	🐬	🐬	—	🐬	dolphin
597	U+1F9AD	🦭	… 🦭 🦭 🦭 …	⊛ seal
598	U+1F41F	🐟	🐟	🐟	🐟	🐟	🐟	🐟	🐟	🐟	🐟	🐟	—	fish
599	U+1F420	🐠	🐠	🐠	🐠	🐠	🐠	🐠	🐠	🐠	🐠	—	🐠	tropical fish
600	U+1F421	🐡	🐡	🐡	🐡	🐡	🐡	🐡	🐡	🐡	—	—	🐡	blowfish
601	U+1F988	🦈	🦈	🦈	🦈	🦈	🦈	🦈	🦈	—	—	—	—	shark
602	U+1F419	🐙	🐙	🐙	🐙	🐙	🐙	🐙	🐙	🐙	🐙	—	🐙	octopus
603	U+1F41A	🐚	🐚	🐚	🐚	🐚	🐚	🐚	🐚	🐚	🐚	—	🐚	spiral shell
animal-bug
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
604	U+1F40C	🐌	🐌	🐌	🐌	🐌	🐌	🐌	🐌	🐌	—	🐌	🐌	snail
605	U+1F98B	🦋	🦋	🦋	🦋	🦋	🦋	🦋	🦋	—	—	—	—	butterfly
606	U+1F41B	🐛	🐛	🐛	🐛	🐛	🐛	🐛	🐛	🐛	🐛	—	🐛	bug
607	U+1F41C	🐜	🐜	🐜	🐜	🐜	🐜	🐜	🐜	🐜	—	—	🐜	ant
608	U+1F41D	🐝	🐝	🐝	🐝	🐝	🐝	🐝	🐝	🐝	—	—	🐝	honeybee
609	U+1FAB2	🪲	… 🪲 🪲 🪲 …	⊛ beetle
610	U+1F41E	🐞	🐞	🐞	🐞	🐞	🐞	🐞	🐞	🐞	—	—	🐞	lady beetle
611	U+1F997	🦗	🦗	🦗	🦗	🦗	🦗	🦗	🦗	—	—	—	—	cricket
612	U+1FAB3	🪳	… 🪳 🪳 🪳 …	⊛ cockroach
613	U+1F577	🕷	🕷	🕷	🕷	🕷	🕷	🕷	🕷	—	—	—	—	spider
614	U+1F578	🕸	🕸	🕸	🕸	🕸	🕸	🕸	🕸	—	—	—	—	spider web
615	U+1F982	🦂	🦂	🦂	🦂	🦂	🦂	🦂	🦂	—	—	—	—	scorpion
616	U+1F99F	🦟	🦟	🦟	🦟	🦟	🦟	🦟	🦟	—	—	—	—	mosquito
617	U+1FAB0	🪰	… 🪰 🪰 🪰 …	⊛ fly
618	U+1FAB1	🪱	… 🪱 🪱 🪱 …	⊛ worm
619	U+1F9A0	🦠	🦠	🦠	🦠	🦠	🦠	🦠	🦠	—	—	—	—	microbe
plant-flower
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
620	U+1F490	💐	💐	💐	💐	💐	💐	💐	💐	💐	💐	—	💐	bouquet
621	U+1F338	🌸	🌸	🌸	🌸	🌸	🌸	🌸	🌸	🌸	🌸	🌸	🌸	cherry blossom
622	U+1F4AE	💮	💮	💮	💮	💮	💮	💮	💮	💮	—	—	💮	white flower
623	U+1F3F5	🏵	🏵	🏵	🏵	🏵	🏵	🏵	🏵	—	—	—	—	rosette
624	U+1F339	🌹	🌹	🌹	🌹	🌹	🌹	🌹	🌹	🌹	🌹	—	🌹	rose
625	U+1F940	🥀	🥀	🥀	🥀	🥀	🥀	🥀	🥀	—	—	—	—	wilted flower
626	U+1F33A	🌺	🌺	🌺	🌺	🌺	🌺	🌺	🌺	🌺	🌺	—	🌺	hibiscus
627	U+1F33B	🌻	🌻	🌻	🌻	🌻	🌻	🌻	🌻	🌻	🌻	—	🌻	sunflower
628	U+1F33C	🌼	🌼	🌼	🌼	🌼	🌼	🌼	🌼	🌼	—	—	🌼	blossom
629	U+1F337	🌷	🌷	🌷	🌷	🌷	🌷	🌷	🌷	🌷	🌷	🌷	🌷	tulip
plant-other
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
630	U+1F331	🌱	🌱	🌱	🌱	🌱	🌱	🌱	🌱	🌱	—	🌱	🌱	seedling
631	U+1FAB4	🪴	—	🪴	—	—	—	🪴	—	—	—	—	—	⊛ potted plant
632	U+1F332	🌲	🌲	🌲	🌲	🌲	🌲	🌲	🌲	—	—	—	—	evergreen tree
633	U+1F333	🌳	🌳	🌳	🌳	🌳	🌳	🌳	🌳	—	—	—	—	deciduous tree
634	U+1F334	🌴	🌴	🌴	🌴	🌴	🌴	🌴	🌴	🌴	🌴	—	🌴	palm tree
635	U+1F335	🌵	🌵	🌵	🌵	🌵	🌵	🌵	🌵	🌵	🌵	—	🌵	cactus
636	U+1F33E	🌾	🌾	🌾	🌾	🌾	🌾	🌾	🌾	🌾	🌾	—	—	sheaf of rice
637	U+1F33F	🌿	🌿	🌿	🌿	🌿	🌿	🌿	🌿	🌿	—	—	🌿	herb
638	U+2618	☘	☘	☘	☘	☘	☘	☘	☘	—	—	—	—	shamrock
639	U+1F340	🍀	🍀	🍀	🍀	🍀	🍀	🍀	🍀	🍀	🍀	🍀	🍀	four leaf clover
640	U+1F341	🍁	🍁	🍁	🍁	🍁	🍁	🍁	🍁	🍁	🍁	🍁	🍁	maple leaf
641	U+1F342	🍂	🍂	🍂	🍂	🍂	🍂	🍂	🍂	🍂	🍂	—	🍂	fallen leaf
642	U+1F343	🍃	🍃	🍃	🍃	🍃	🍃	🍃	🍃	🍃	🍃	—	—	leaf fluttering in wind
Food & Drink
food-fruit
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
643	U+1F347	🍇	🍇	🍇	🍇	🍇	🍇	🍇	🍇	🍇	—	—	🍇	grapes
644	U+1F348	🍈	🍈	🍈	🍈	🍈	🍈	🍈	🍈	🍈	—	—	🍈	melon
645	U+1F349	🍉	🍉	🍉	🍉	🍉	🍉	🍉	🍉	🍉	🍉	—	🍉	watermelon
646	U+1F34A	🍊	🍊	🍊	🍊	🍊	🍊	🍊	🍊	🍊	🍊	—	🍊	tangerine
647	U+1F34B	🍋	🍋	🍋	🍋	🍋	🍋	🍋	🍋	—	—	—	—	lemon
648	U+1F34C	🍌	🍌	🍌	🍌	🍌	🍌	🍌	🍌	🍌	—	🍌	🍌	banana
649	U+1F34D	🍍	🍍	🍍	🍍	🍍	🍍	🍍	🍍	🍍	—	—	🍍	pineapple
650	U+1F96D	🥭	🥭	🥭	🥭	🥭	🥭	🥭	🥭	—	—	—	—	mango
651	U+1F34E	🍎	🍎	🍎	🍎	🍎	🍎	🍎	🍎	🍎	🍎	🍎	🍎	red apple
652	U+1F34F	🍏	🍏	🍏	🍏	🍏	🍏	🍏	🍏	🍏	—	—	🍏	green apple
653	U+1F350	🍐	🍐	🍐	🍐	🍐	🍐	🍐	🍐	—	—	—	—	pear
654	U+1F351	🍑	🍑	🍑	🍑	🍑	🍑	🍑	🍑	🍑	—	—	🍑	peach
655	U+1F352	🍒	🍒	🍒	🍒	🍒	🍒	🍒	🍒	🍒	—	🍒	🍒	cherries
656	U+1F353	🍓	🍓	🍓	🍓	🍓	🍓	🍓	🍓	🍓	🍓	—	🍓	strawberry
657	U+1FAD0	🫐	—	🫐	—	—	—	🫐	—	—	—	—	—	⊛ blueberries
658	U+1F95D	🥝	🥝	🥝	🥝	🥝	🥝	🥝	🥝	—	—	—	—	kiwi fruit
659	U+1F345	🍅	🍅	🍅	🍅	🍅	🍅	🍅	🍅	🍅	🍅	—	🍅	tomato
660	U+1FAD2	🫒	—	🫒	—	—	—	🫒	—	—	—	—	—	⊛ olive
661	U+1F965	🥥	🥥	🥥	🥥	🥥	🥥	🥥	🥥	—	—	—	—	coconut
food-vegetable
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
662	U+1F951	🥑	🥑	🥑	🥑	🥑	🥑	🥑	🥑	—	—	—	—	avocado
663	U+1F346	🍆	🍆	🍆	🍆	🍆	🍆	🍆	🍆	🍆	🍆	—	🍆	eggplant
664	U+1F954	🥔	🥔	🥔	🥔	🥔	🥔	🥔	🥔	—	—	—	—	potato
665	U+1F955	🥕	🥕	🥕	🥕	🥕	🥕	🥕	🥕	—	—	—	—	carrot
666	U+1F33D	🌽	🌽	🌽	🌽	🌽	🌽	🌽	🌽	🌽	—	—	🌽	ear of corn
667	U+1F336	🌶	🌶	🌶	🌶	🌶	🌶	🌶	🌶	—	—	—	—	hot pepper
668	U+1FAD1	🫑	… 🫑 🫑 🫑 …	⊛ bell pepper
669	U+1F952	🥒	🥒	🥒	🥒	🥒	🥒	🥒	🥒	—	—	—	—	cucumber
670	U+1F96C	🥬	🥬	🥬	🥬	🥬	🥬	🥬	🥬	—	—	—	—	leafy green
671	U+1F966	🥦	🥦	🥦	🥦	🥦	🥦	🥦	🥦	—	—	—	—	broccoli
672	U+1F9C4	🧄	🧄	🧄	🧄	🧄	🧄	🧄	🧄	—	—	—	—	garlic
673	U+1F9C5	🧅	🧅	🧅	🧅	🧅	🧅	🧅	🧅	—	—	—	—	onion
674	U+1F344	🍄	🍄	🍄	🍄	🍄	🍄	🍄	🍄	🍄	—	—	🍄	mushroom
675	U+1F95C	🥜	🥜	🥜	🥜	🥜	🥜	🥜	🥜	—	—	—	—	peanuts
676	U+1F330	🌰	🌰	🌰	🌰	🌰	🌰	🌰	🌰	🌰	—	—	🌰	chestnut
food-prepared
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
677	U+1F35E	🍞	🍞	🍞	🍞	🍞	🍞	🍞	🍞	🍞	🍞	🍞	🍞	bread
678	U+1F950	🥐	🥐	🥐	🥐	🥐	🥐	🥐	🥐	—	—	—	—	croissant
679	U+1F956	🥖	🥖	🥖	🥖	🥖	🥖	🥖	🥖	—	—	—	—	baguette bread
680	U+1FAD3	🫓	—	🫓	—	—	—	🫓	—	—	—	—	—	⊛ flatbread
681	U+1F968	🥨	🥨	🥨	🥨	🥨	🥨	🥨	🥨	—	—	—	—	pretzel
682	U+1F96F	🥯	🥯	🥯	🥯	🥯	🥯	🥯	🥯	—	—	—	—	bagel
683	U+1F95E	🥞	🥞	🥞	🥞	🥞	🥞	🥞	🥞	—	—	—	—	pancakes
684	U+1F9C7	🧇	🧇	🧇	🧇	🧇	🧇	🧇	🧇	—	—	—	—	waffle
685	U+1F9C0	🧀	🧀	🧀	🧀	🧀	🧀	🧀	🧀	—	—	—	—	cheese wedge
686	U+1F356	🍖	🍖	🍖	🍖	🍖	🍖	🍖	🍖	🍖	—	—	🍖	meat on bone
687	U+1F357	🍗	🍗	🍗	🍗	🍗	🍗	🍗	🍗	🍗	—	—	🍗	poultry leg
688	U+1F969	🥩	🥩	🥩	🥩	🥩	🥩	🥩	🥩	—	—	—	—	cut of meat
689	U+1F953	🥓	🥓	🥓	🥓	🥓	🥓	🥓	🥓	—	—	—	—	bacon
690	U+1F354	🍔	🍔	🍔	🍔	🍔	🍔	🍔	🍔	🍔	🍔	🍔	🍔	hamburger
691	U+1F35F	🍟	🍟	🍟	🍟	🍟	🍟	🍟	🍟	🍟	🍟	—	🍟	french fries
692	U+1F355	🍕	🍕	🍕	🍕	🍕	🍕	🍕	🍕	🍕	—	—	🍕	pizza
693	U+1F32D	🌭	🌭	🌭	🌭	🌭	🌭	🌭	🌭	—	—	—	—	hot dog
694	U+1F96A	🥪	🥪	🥪	🥪	🥪	🥪	🥪	🥪	—	—	—	—	sandwich
695	U+1F32E	🌮	🌮	🌮	🌮	🌮	🌮	🌮	🌮	—	—	—	—	taco
696	U+1F32F	🌯	🌯	🌯	🌯	🌯	🌯	🌯	🌯	—	—	—	—	burrito
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
697	U+1FAD4	🫔	—	🫔	—	—	—	🫔	—	—	—	—	—	⊛ tamale
698	U+1F959	🥙	🥙	🥙	🥙	🥙	🥙	🥙	🥙	—	—	—	—	stuffed flatbread
699	U+1F9C6	🧆	🧆	🧆	🧆	🧆	🧆	🧆	🧆	—	—	—	—	falafel
700	U+1F95A	🥚	🥚	🥚	🥚	🥚	🥚	🥚	🥚	—	—	—	—	egg
701	U+1F373	🍳	🍳	🍳	🍳	🍳	🍳	🍳	🍳	🍳	🍳	—	🍳	cooking
702	U+1F958	🥘	🥘	🥘	🥘	🥘	🥘	🥘	🥘	—	—	—	—	shallow pan of food
703	U+1F372	🍲	🍲	🍲	🍲	🍲	🍲	🍲	🍲	🍲	🍲	—	🍲	pot of food
704	U+1FAD5	🫕	—	🫕	—	—	—	🫕	—	—	—	—	—	⊛ fondue
705	U+1F963	🥣	🥣	🥣	🥣	🥣	🥣	🥣	🥣	—	—	—	—	bowl with spoon
706	U+1F957	🥗	🥗	🥗	🥗	🥗	🥗	🥗	🥗	—	—	—	—	green salad
707	U+1F37F	🍿	🍿	🍿	🍿	🍿	🍿	🍿	🍿	—	—	—	—	popcorn
708	U+1F9C8	🧈	🧈	🧈	🧈	🧈	🧈	🧈	🧈	—	—	—	—	butter
709	U+1F9C2	🧂	🧂	🧂	🧂	🧂	🧂	🧂	🧂	—	—	—	—	salt
710	U+1F96B	🥫	🥫	🥫	🥫	🥫	🥫	🥫	🥫	—	—	—	—	canned food
food-asian
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
711	U+1F371	🍱	🍱	🍱	🍱	🍱	🍱	🍱	🍱	🍱	🍱	—	🍱	bento box
712	U+1F358	🍘	🍘	🍘	🍘	🍘	🍘	🍘	🍘	🍘	🍘	—	🍘	rice cracker
713	U+1F359	🍙	🍙	🍙	🍙	🍙	🍙	🍙	🍙	🍙	🍙	🍙	🍙	rice ball
714	U+1F35A	🍚	🍚	🍚	🍚	🍚	🍚	🍚	🍚	🍚	🍚	—	🍚	cooked rice
715	U+1F35B	🍛	🍛	🍛	🍛	🍛	🍛	🍛	🍛	🍛	🍛	—	🍛	curry rice
716	U+1F35C	🍜	🍜	🍜	🍜	🍜	🍜	🍜	🍜	🍜	🍜	🍜	🍜	steaming bowl
717	U+1F35D	🍝	🍝	🍝	🍝	🍝	🍝	🍝	🍝	🍝	🍝	—	🍝	spaghetti
718	U+1F360	🍠	🍠	🍠	🍠	🍠	🍠	🍠	🍠	🍠	—	—	🍠	roasted sweet potato
719	U+1F362	🍢	🍢	🍢	🍢	🍢	🍢	🍢	🍢	🍢	🍢	—	🍢	oden
720	U+1F363	🍣	🍣	🍣	🍣	🍣	🍣	🍣	🍣	🍣	🍣	—	🍣	sushi
721	U+1F364	🍤	🍤	🍤	🍤	🍤	🍤	🍤	🍤	🍤	—	—	🍤	fried shrimp
722	U+1F365	🍥	🍥	🍥	🍥	🍥	🍥	🍥	🍥	🍥	—	—	🍥	fish cake with swirl
723	U+1F96E	🥮	🥮	🥮	🥮	🥮	🥮	🥮	🥮	—	—	—	—	moon cake
724	U+1F361	🍡	🍡	🍡	🍡	🍡	🍡	🍡	🍡	🍡	🍡	—	🍡	dango
725	U+1F95F	🥟	🥟	🥟	🥟	🥟	🥟	🥟	🥟	—	—	—	—	dumpling
726	U+1F960	🥠	🥠	🥠	🥠	🥠	🥠	🥠	🥠	—	—	—	—	fortune cookie
727	U+1F961	🥡	🥡	🥡	🥡	🥡	🥡	🥡	🥡	—	—	—	—	takeout box
food-marine
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
728	U+1F980	🦀	🦀	🦀	🦀	🦀	🦀	🦀	🦀	—	—	—	—	crab
729	U+1F99E	🦞	🦞	🦞	🦞	🦞	🦞	🦞	🦞	—	—	—	—	lobster
730	U+1F990	🦐	🦐	🦐	🦐	🦐	🦐	🦐	🦐	—	—	—	—	shrimp
731	U+1F991	🦑	🦑	🦑	🦑	🦑	🦑	🦑	🦑	—	—	—	—	squid
732	U+1F9AA	🦪	🦪	🦪	🦪	🦪	🦪	🦪	🦪	—	—	—	—	oyster
food-sweet
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
733	U+1F366	🍦	🍦	🍦	🍦	🍦	🍦	🍦	🍦	🍦	🍦	—	🍦	soft ice cream
734	U+1F367	🍧	🍧	🍧	🍧	🍧	🍧	🍧	🍧	🍧	🍧	—	🍧	shaved ice
735	U+1F368	🍨	🍨	🍨	🍨	🍨	🍨	🍨	🍨	🍨	—	—	🍨	ice cream
736	U+1F369	🍩	🍩	🍩	🍩	🍩	🍩	🍩	🍩	🍩	—	—	🍩	doughnut
737	U+1F36A	🍪	🍪	🍪	🍪	🍪	🍪	🍪	🍪	🍪	—	—	🍪	cookie
738	U+1F382	🎂	🎂	🎂	🎂	🎂	🎂	🎂	🎂	🎂	🎂	🎂	🎂	birthday cake
739	U+1F370	🍰	🍰	🍰	🍰	🍰	🍰	🍰	🍰	🍰	🍰	🍰	🍰	shortcake
740	U+1F9C1	🧁	🧁	🧁	🧁	🧁	🧁	🧁	🧁	—	—	—	—	cupcake
741	U+1F967	🥧	🥧	🥧	🥧	🥧	🥧	🥧	🥧	—	—	—	—	pie
742	U+1F36B	🍫	🍫	🍫	🍫	🍫	🍫	🍫	🍫	🍫	—	—	🍫	chocolate bar
743	U+1F36C	🍬	🍬	🍬	🍬	🍬	🍬	🍬	🍬	🍬	—	—	🍬	candy
744	U+1F36D	🍭	🍭	🍭	🍭	🍭	🍭	🍭	🍭	🍭	—	—	🍭	lollipop
745	U+1F36E	🍮	🍮	🍮	🍮	🍮	🍮	🍮	🍮	🍮	—	—	🍮	custard
746	U+1F36F	🍯	🍯	🍯	🍯	🍯	🍯	🍯	🍯	🍯	—	—	🍯	honey pot
drink
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
747	U+1F37C	🍼	🍼	🍼	🍼	🍼	🍼	🍼	🍼	—	—	—	—	baby bottle
748	U+1F95B	🥛	🥛	🥛	🥛	🥛	🥛	🥛	🥛	—	—	—	—	glass of milk
749	U+2615	☕	☕	☕	☕	☕	☕	☕	☕	☕	☕	☕	☕	hot beverage
750	U+1FAD6	🫖	… 🫖 🫖 🫖 …	⊛ teapot
751	U+1F375	🍵	🍵	🍵	🍵	🍵	🍵	🍵	🍵	🍵	🍵	🍵	🍵	teacup without handle
752	U+1F376	🍶	🍶	🍶	🍶	🍶	🍶	🍶	🍶	🍶	🍶	🍶	🍶	sake
753	U+1F37E	🍾	🍾	🍾	🍾	🍾	🍾	🍾	🍾	—	—	—	—	bottle with popping cork
754	U+1F377	🍷	🍷	🍷	🍷	🍷	🍷	🍷	🍷	🍷	—	🍷	🍷	wine glass
755	U+1F378	🍸	🍸	🍸	🍸	🍸	🍸	🍸	🍸	🍸	🍸	🍸	🍸	cocktail glass
756	U+1F379	🍹	🍹	🍹	🍹	🍹	🍹	🍹	🍹	🍹	—	—	🍹	tropical drink
757	U+1F37A	🍺	🍺	🍺	🍺	🍺	🍺	🍺	🍺	🍺	🍺	🍺	🍺	beer mug
758	U+1F37B	🍻	🍻	🍻	🍻	🍻	🍻	🍻	🍻	🍻	🍻	—	🍻	clinking beer mugs
759	U+1F942	🥂	🥂	🥂	🥂	🥂	🥂	🥂	🥂	—	—	—	—	clinking glasses
760	U+1F943	🥃	🥃	🥃	🥃	🥃	🥃	🥃	🥃	—	—	—	—	tumbler glass
761	U+1F964	🥤	🥤	🥤	🥤	🥤	🥤	🥤	🥤	—	—	—	—	cup with straw
762	U+1F9CB	🧋	—	🧋	—	—	—	🧋	—	—	—	—	—	⊛ bubble tea
763	U+1F9C3	🧃	🧃	🧃	🧃	🧃	🧃	🧃	🧃	—	—	—	—	beverage box
764	U+1F9C9	🧉	🧉	🧉	🧉	🧉	🧉	🧉	🧉	—	—	—	—	mate
765	U+1F9CA	🧊	🧊	🧊	🧊	🧊	🧊	🧊	🧊	—	—	—	—	ice
dishware
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
766	U+1F962	🥢	🥢	🥢	🥢	🥢	🥢	🥢	🥢	—	—	—	—	chopsticks
767	U+1F37D	🍽	🍽	🍽	🍽	🍽	🍽	🍽	🍽	—	—	—	—	fork and knife with plate
768	U+1F374	🍴	🍴	🍴	🍴	🍴	🍴	🍴	🍴	🍴	🍴	🍴	🍴	fork and knife
769	U+1F944	🥄	🥄	🥄	🥄	🥄	🥄	🥄	🥄	—	—	—	—	spoon
770	U+1F52A	🔪	🔪	🔪	🔪	🔪	🔪	🔪	🔪	🔪	—	—	🔪	kitchen knife
771	U+1F3FA	🏺	🏺	🏺	🏺	🏺	🏺	🏺	🏺	—	—	—	—	amphora
Travel & Places
place-map
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
772	U+1F30D	🌍	🌍	🌍	🌍	🌍	🌍	🌍	🌍	—	—	—	—	globe showing Europe-Africa
773	U+1F30E	🌎	🌎	🌎	🌎	🌎	🌎	🌎	🌎	—	—	—	—	globe showing Americas
774	U+1F30F	🌏	🌏	🌏	🌏	🌏	🌏	🌏	🌏	🌏	—	—	🌏	globe showing Asia-Australia
775	U+1F310	🌐	🌐	🌐	🌐	🌐	🌐	🌐	🌐	—	—	—	—	globe with meridians
776	U+1F5FA	🗺	🗺	🗺	🗺	🗺	🗺	🗺	🗺	—	—	—	—	world map
777	U+1F5FE	🗾	🗾	🗾	🗾	🗾	🗾	🗾	—	🗾	—	—	🗾	map of Japan
778	U+1F9ED	🧭	🧭	🧭	🧭	🧭	🧭	🧭	🧭	—	—	—	—	compass
place-geographic
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
779	U+1F3D4	🏔	🏔	🏔	🏔	🏔	🏔	🏔	🏔	—	—	—	—	snow-capped mountain
780	U+26F0	⛰	⛰	⛰	⛰	⛰	⛰	⛰	⛰	—	—	—	—	mountain
781	U+1F30B	🌋	🌋	🌋	🌋	🌋	🌋	🌋	🌋	🌋	—	—	🌋	volcano
782	U+1F5FB	🗻	🗻	🗻	🗻	🗻	🗻	🗻	🗻	🗻	🗻	🗻	🗻	mount fuji
783	U+1F3D5	🏕	🏕	🏕	🏕	🏕	🏕	🏕	🏕	—	—	—	—	camping
784	U+1F3D6	🏖	🏖	🏖	🏖	🏖	🏖	🏖	🏖	—	—	—	—	beach with umbrella
785	U+1F3DC	🏜	🏜	🏜	🏜	🏜	🏜	🏜	🏜	—	—	—	—	desert
786	U+1F3DD	🏝	🏝	🏝	🏝	🏝	🏝	🏝	🏝	—	—	—	—	desert island
787	U+1F3DE	🏞	🏞	🏞	🏞	🏞	🏞	🏞	🏞	—	—	—	—	national park
place-building
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
788	U+1F3DF	🏟	🏟	🏟	🏟	🏟	🏟	🏟	🏟	—	—	—	—	stadium
789	U+1F3DB	🏛	🏛	🏛	🏛	🏛	🏛	🏛	🏛	—	—	—	—	classical building
790	U+1F3D7	🏗	🏗	🏗	🏗	🏗	🏗	🏗	🏗	—	—	—	—	building construction
791	U+1F9F1	🧱	🧱	🧱	🧱	🧱	🧱	🧱	🧱	—	—	—	—	brick
792	U+1FAA8	🪨	—	🪨	—	—	—	🪨	—	—	—	—	—	⊛ rock
793	U+1FAB5	🪵	—	🪵	—	—	—	🪵	—	—	—	—	—	⊛ wood
794	U+1F6D6	🛖	… 🛖 🛖 🛖 …	⊛ hut
795	U+1F3D8	🏘	🏘	🏘	🏘	🏘	🏘	🏘	🏘	—	—	—	—	houses
796	U+1F3DA	🏚	🏚	🏚	🏚	🏚	🏚	🏚	🏚	—	—	—	—	derelict house
797	U+1F3E0	🏠	🏠	🏠	🏠	🏠	🏠	🏠	🏠	🏠	🏠	🏠	🏠	house
798	U+1F3E1	🏡	🏡	🏡	🏡	🏡	🏡	🏡	🏡	🏡	—	—	🏡	house with garden
799	U+1F3E2	🏢	🏢	🏢	🏢	🏢	🏢	🏢	🏢	🏢	🏢	🏢	🏢	office building
800	U+1F3E3	🏣	🏣	🏣	🏣	🏣	🏣	🏣	🏣	🏣	🏣	🏣	🏣	Japanese post office
801	U+1F3E4	🏤	🏤	🏤	🏤	🏤	🏤	🏤	🏤	—	—	—	—	post office
802	U+1F3E5	🏥	🏥	🏥	🏥	🏥	🏥	🏥	🏥	🏥	🏥	🏥	🏥	hospital
803	U+1F3E6	🏦	🏦	🏦	🏦	🏦	🏦	🏦	🏦	🏦	🏦	🏦	🏦	bank
804	U+1F3E8	🏨	🏨	🏨	🏨	🏨	🏨	🏨	🏨	🏨	🏨	🏨	🏨	hotel
805	U+1F3E9	🏩	🏩	🏩	🏩	🏩	🏩	🏩	🏩	🏩	🏩	—	🏩	love hotel
806	U+1F3EA	🏪	🏪	🏪	🏪	🏪	🏪	🏪	🏪	🏪	🏪	🏪	🏪	convenience store
807	U+1F3EB	🏫	🏫	🏫	🏫	🏫	🏫	🏫	🏫	🏫	🏫	🏫	🏫	school
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
808	U+1F3EC	🏬	🏬	🏬	🏬	🏬	🏬	🏬	🏬	🏬	🏬	—	🏬	department store
809	U+1F3ED	🏭	🏭	🏭	🏭	🏭	🏭	🏭	🏭	🏭	🏭	—	🏭	factory
810	U+1F3EF	🏯	🏯	🏯	🏯	🏯	🏯	🏯	🏯	🏯	🏯	—	🏯	Japanese castle
811	U+1F3F0	🏰	🏰	🏰	🏰	🏰	🏰	🏰	🏰	🏰	🏰	—	🏰	castle
812	U+1F492	💒	💒	💒	💒	💒	💒	💒	💒	💒	💒	—	—	wedding
813	U+1F5FC	🗼	🗼	🗼	🗼	🗼	🗼	🗼	🗼	🗼	🗼	—	🗼	Tokyo tower
814	U+1F5FD	🗽	🗽	🗽	🗽	🗽	🗽	🗽	🗽	🗽	🗽	—	—	Statue of Liberty
place-religious
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
815	U+26EA	⛪	⛪	⛪	⛪	⛪	⛪	⛪	⛪	⛪	⛪	—	⛪	church
816	U+1F54C	🕌	🕌	🕌	🕌	🕌	🕌	🕌	🕌	—	—	—	—	mosque
817	U+1F6D5	🛕	🛕	🛕	🛕	🛕	🛕	🛕	🛕	—	—	—	—	hindu temple
818	U+1F54D	🕍	🕍	🕍	🕍	🕍	🕍	🕍	🕍	—	—	—	—	synagogue
819	U+26E9	⛩	⛩	⛩	⛩	⛩	⛩	⛩	⛩	—	—	—	—	shinto shrine
820	U+1F54B	🕋	🕋	🕋	🕋	🕋	🕋	🕋	🕋	—	—	—	—	kaaba
place-other
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
821	U+26F2	⛲	⛲	⛲	⛲	⛲	⛲	⛲	⛲	⛲	⛲	—	⛲	fountain
822	U+26FA	⛺	⛺	⛺	⛺	⛺	⛺	⛺	⛺	⛺	⛺	—	⛺	tent
823	U+1F301	🌁	🌁	🌁	🌁	🌁	🌁	🌁	🌁	🌁	—	🌁	🌁	foggy
824	U+1F303	🌃	🌃	🌃	🌃	🌃	🌃	🌃	🌃	🌃	🌃	🌃	🌃	night with stars
825	U+1F3D9	🏙	🏙	🏙	🏙	🏙	🏙	🏙	🏙	—	—	—	—	cityscape
826	U+1F304	🌄	🌄	🌄	🌄	🌄	🌄	🌄	🌄	🌄	🌄	—	—	sunrise over mountains
827	U+1F305	🌅	🌅	🌅	🌅	🌅	🌅	🌅	🌅	🌅	🌅	—	🌅	sunrise
828	U+1F306	🌆	🌆	🌆	🌆	🌆	🌆	🌆	🌆	🌆	🌆	—	🌆	cityscape at dusk
829	U+1F307	🌇	🌇	🌇	🌇	🌇	🌇	🌇	🌇	🌇	🌇	—	—	sunset
830	U+1F309	🌉	🌉	🌉	🌉	🌉	🌉	🌉	🌉	🌉	—	—	🌉	bridge at night
831	U+2668	♨	♨	♨	♨	♨	♨	♨	♨	♨	♨	♨	♨	hot springs
832	U+1F3A0	🎠	🎠	🎠	🎠	🎠	🎠	🎠	🎠	🎠	—	🎠	—	carousel horse
833	U+1F3A1	🎡	🎡	🎡	🎡	🎡	🎡	🎡	🎡	🎡	🎡	—	🎡	ferris wheel
834	U+1F3A2	🎢	🎢	🎢	🎢	🎢	🎢	🎢	🎢	🎢	🎢	—	🎢	roller coaster
835	U+1F488	💈	💈	💈	💈	💈	💈	💈	💈	💈	💈	—	💈	barber pole
836	U+1F3AA	🎪	🎪	🎪	🎪	🎪	🎪	🎪	🎪	🎪	—	🎪	🎪	circus tent
transport-ground
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
837	U+1F682	🚂	🚂	🚂	🚂	🚂	🚂	🚂	🚂	—	—	—	—	locomotive
838	U+1F683	🚃	🚃	🚃	🚃	🚃	🚃	🚃	🚃	🚃	🚃	🚃	🚃	railway car
839	U+1F684	🚄	🚄	🚄	🚄	🚄	🚄	🚄	🚄	🚄	🚄	🚄	—	high-speed train
840	U+1F685	🚅	🚅	🚅	🚅	🚅	🚅	🚅	🚅	🚅	🚅	—	🚅	bullet train
841	U+1F686	🚆	🚆	🚆	🚆	🚆	🚆	🚆	🚆	—	—	—	—	train
842	U+1F687	🚇	🚇	🚇	🚇	🚇	🚇	🚇	🚇	🚇	🚇	—	🚇	metro
843	U+1F688	🚈	🚈	🚈	🚈	🚈	🚈	🚈	🚈	—	—	—	—	light rail
844	U+1F689	🚉	🚉	🚉	🚉	🚉	🚉	🚉	🚉	🚉	🚉	—	🚉	station
845	U+1F68A	🚊	🚊	🚊	🚊	🚊	🚊	🚊	🚊	—	—	—	—	tram
846	U+1F69D	🚝	🚝	🚝	🚝	🚝	🚝	🚝	🚝	—	—	—	—	monorail
847	U+1F69E	🚞	🚞	🚞	🚞	🚞	🚞	🚞	🚞	—	—	—	—	mountain railway
848	U+1F68B	🚋	🚋	🚋	🚋	🚋	🚋	🚋	🚋	—	—	—	—	tram car
849	U+1F68C	🚌	🚌	🚌	🚌	🚌	🚌	🚌	🚌	🚌	🚌	🚌	🚌	bus
850	U+1F68D	🚍	🚍	🚍	🚍	🚍	🚍	🚍	🚍	—	—	—	—	oncoming bus
851	U+1F68E	🚎	🚎	🚎	🚎	🚎	🚎	🚎	🚎	—	—	—	—	trolleybus
852	U+1F690	🚐	🚐	🚐	🚐	🚐	🚐	🚐	🚐	—	—	—	—	minibus
853	U+1F691	🚑	🚑	🚑	🚑	🚑	🚑	🚑	🚑	🚑	🚑	—	🚑	ambulance
854	U+1F692	🚒	🚒	🚒	🚒	🚒	🚒	🚒	🚒	🚒	🚒	—	🚒	fire engine
855	U+1F693	🚓	🚓	🚓	🚓	🚓	🚓	🚓	🚓	🚓	🚓	—	🚓	police car
856	U+1F694	🚔	🚔	🚔	🚔	🚔	🚔	🚔	🚔	—	—	—	—	oncoming police car
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
857	U+1F695	🚕	🚕	🚕	🚕	🚕	🚕	🚕	🚕	🚕	🚕	—	—	taxi
858	U+1F696	🚖	🚖	🚖	🚖	🚖	🚖	🚖	🚖	—	—	—	—	oncoming taxi
859	U+1F697	🚗	🚗	🚗	🚗	🚗	🚗	🚗	🚗	🚗	🚗	🚗	🚗	automobile
860	U+1F698	🚘	🚘	🚘	🚘	🚘	🚘	🚘	🚘	—	—	—	—	oncoming automobile
861	U+1F699	🚙	🚙	🚙	🚙	🚙	🚙	🚙	🚙	🚙	🚙	🚙	—	sport utility vehicle
862	U+1F6FB	🛻	… 🛻 🛻 🛻 …	⊛ pickup truck
863	U+1F69A	🚚	🚚	🚚	🚚	🚚	🚚	🚚	🚚	🚚	🚚	—	🚚	delivery truck
864	U+1F69B	🚛	🚛	🚛	🚛	🚛	🚛	🚛	🚛	—	—	—	—	articulated lorry
865	U+1F69C	🚜	🚜	🚜	🚜	🚜	🚜	🚜	🚜	—	—	—	—	tractor
866	U+1F3CE	🏎	🏎	🏎	🏎	🏎	🏎	🏎	🏎	—	—	—	—	racing car
867	U+1F3CD	🏍	🏍	🏍	🏍	🏍	🏍	🏍	🏍	—	—	—	—	motorcycle
868	U+1F6F5	🛵	🛵	🛵	🛵	🛵	🛵	🛵	🛵	—	—	—	—	motor scooter
869	U+1F9BD	🦽	🦽	🦽	🦽	🦽	🦽	🦽	🦽	—	—	—	—	manual wheelchair
870	U+1F9BC	🦼	🦼	🦼	🦼	🦼	🦼	🦼	🦼	—	—	—	—	motorized wheelchair
871	U+1F6FA	🛺	🛺	🛺	🛺	🛺	🛺	🛺	🛺	—	—	—	—	auto rickshaw
872	U+1F6B2	🚲	🚲	🚲	🚲	🚲	🚲	🚲	🚲	🚲	🚲	🚲	🚲	bicycle
873	U+1F6F4	🛴	🛴	🛴	🛴	🛴	🛴	🛴	🛴	—	—	—	—	kick scooter
874	U+1F6F9	🛹	🛹	🛹	🛹	🛹	🛹	🛹	🛹	—	—	—	—	skateboard
875	U+1F6FC	🛼	—	🛼	—	—	—	🛼	—	—	—	—	—	⊛ roller skate
876	U+1F68F	🚏	🚏	🚏	🚏	🚏	🚏	🚏	🚏	🚏	🚏	—	🚏	bus stop
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
877	U+1F6E3	🛣	🛣	🛣	🛣	🛣	🛣	🛣	🛣	—	—	—	—	motorway
878	U+1F6E4	🛤	🛤	🛤	🛤	🛤	🛤	🛤	🛤	—	—	—	—	railway track
879	U+1F6E2	🛢	🛢	🛢	🛢	🛢	🛢	🛢	🛢	—	—	—	—	oil drum
880	U+26FD	⛽	⛽	⛽	⛽	⛽	⛽	⛽	⛽	⛽	⛽	⛽	⛽	fuel pump
881	U+1F6A8	🚨	🚨	🚨	🚨	🚨	🚨	🚨	🚨	🚨	—	—	🚨	police car light
882	U+1F6A5	🚥	🚥	🚥	🚥	🚥	🚥	🚥	🚥	🚥	🚥	🚥	🚥	horizontal traffic light
883	U+1F6A6	🚦	🚦	🚦	🚦	🚦	🚦	🚦	🚦	—	—	—	—	vertical traffic light
884	U+1F6D1	🛑	🛑	🛑	🛑	🛑	🛑	🛑	🛑	—	—	—	—	stop sign
885	U+1F6A7	🚧	🚧	🚧	🚧	🚧	🚧	🚧	🚧	🚧	🚧	—	🚧	construction
transport-water
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
886	U+2693	⚓	⚓	⚓	⚓	⚓	⚓	⚓	⚓	⚓	—	—	⚓	anchor
887	U+26F5	⛵	⛵	⛵	⛵	⛵	⛵	⛵	⛵	⛵	⛵	⛵	⛵	sailboat
888	U+1F6F6	🛶	🛶	🛶	🛶	🛶	🛶	🛶	🛶	—	—	—	—	canoe
889	U+1F6A4	🚤	🚤	🚤	🚤	🚤	🚤	🚤	🚤	🚤	🚤	—	—	speedboat
890	U+1F6F3	🛳	🛳	🛳	🛳	🛳	🛳	🛳	🛳	—	—	—	—	passenger ship
891	U+26F4	⛴	⛴	⛴	⛴	⛴	⛴	⛴	⛴	—	—	—	—	ferry
892	U+1F6E5	🛥	🛥	🛥	🛥	🛥	🛥	🛥	🛥	—	—	—	—	motor boat
893	U+1F6A2	🚢	🚢	🚢	🚢	🚢	🚢	🚢	🚢	🚢	🚢	🚢	🚢	ship
transport-air
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
894	U+2708	✈	✈	✈	✈	✈	✈	✈	✈	✈	✈	✈	✈	airplane
895	U+1F6E9	🛩	🛩	🛩	🛩	🛩	🛩	🛩	🛩	—	—	—	—	small airplane
896	U+1F6EB	🛫	🛫	🛫	🛫	🛫	🛫	🛫	🛫	—	—	—	—	airplane departure
897	U+1F6EC	🛬	🛬	🛬	🛬	🛬	🛬	🛬	🛬	—	—	—	—	airplane arrival
898	U+1FA82	🪂	🪂	🪂	🪂	🪂	🪂	🪂	🪂	—	—	—	—	parachute
899	U+1F4BA	💺	💺	💺	💺	💺	💺	💺	💺	💺	💺	💺	—	seat
900	U+1F681	🚁	🚁	🚁	🚁	🚁	🚁	🚁	🚁	—	—	—	—	helicopter
901	U+1F69F	🚟	🚟	🚟	🚟	🚟	🚟	🚟	🚟	—	—	—	—	suspension railway
902	U+1F6A0	🚠	🚠	🚠	🚠	🚠	🚠	🚠	🚠	—	—	—	—	mountain cableway
903	U+1F6A1	🚡	🚡	🚡	🚡	🚡	🚡	🚡	🚡	—	—	—	—	aerial tramway
904	U+1F6F0	🛰	🛰	🛰	🛰	🛰	🛰	🛰	🛰	—	—	—	—	satellite
905	U+1F680	🚀	🚀	🚀	🚀	🚀	🚀	🚀	🚀	🚀	🚀	—	🚀	rocket
906	U+1F6F8	🛸	🛸	🛸	🛸	🛸	🛸	🛸	🛸	—	—	—	—	flying saucer
hotel
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
907	U+1F6CE	🛎	🛎	🛎	🛎	🛎	🛎	🛎	🛎	—	—	—	—	bellhop bell
908	U+1F9F3	🧳	🧳	🧳	🧳	🧳	🧳	🧳	🧳	—	—	—	—	luggage
time
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
909	U+231B	⌛	⌛	⌛	⌛	⌛	⌛	⌛	⌛	⌛	—	—	⌛	hourglass done
910	U+23F3	⏳	⏳	⏳	⏳	⏳	⏳	⏳	⏳	⏳	—	⏳	⏳	hourglass not done
911	U+231A	⌚	⌚	⌚	⌚	⌚	⌚	⌚	⌚	⌚	—	⌚	⌚	watch
912	U+23F0	⏰	⏰	⏰	⏰	⏰	⏰	⏰	⏰	⏰	—	⏰	⏰	alarm clock
913	U+23F1	⏱	⏱	⏱	⏱	⏱	⏱	⏱	⏱	—	—	—	—	stopwatch
914	U+23F2	⏲	⏲	⏲	⏲	⏲	⏲	⏲	⏲	—	—	—	—	timer clock
915	U+1F570	🕰	🕰	🕰	🕰	🕰	🕰	🕰	🕰	—	—	—	—	mantelpiece clock
916	U+1F55B	🕛	🕛	🕛	🕛	🕛	🕛	🕛	🕛	🕛	🕛	—	—	twelve o’clock
917	U+1F567	🕧	🕧	🕧	🕧	🕧	🕧	🕧	🕧	—	—	—	—	twelve-thirty
918	U+1F550	🕐	🕐	🕐	🕐	🕐	🕐	🕐	🕐	🕐	🕐	—	—	one o’clock
919	U+1F55C	🕜	🕜	🕜	🕜	🕜	🕜	🕜	🕜	—	—	—	—	one-thirty
920	U+1F551	🕑	🕑	🕑	🕑	🕑	🕑	🕑	🕑	🕑	🕑	—	—	two o’clock
921	U+1F55D	🕝	🕝	🕝	🕝	🕝	🕝	🕝	🕝	—	—	—	—	two-thirty
922	U+1F552	🕒	🕒	🕒	🕒	🕒	🕒	🕒	🕒	🕒	🕒	—	—	three o’clock
923	U+1F55E	🕞	🕞	🕞	🕞	🕞	🕞	🕞	🕞	—	—	—	—	three-thirty
924	U+1F553	🕓	🕓	🕓	🕓	🕓	🕓	🕓	🕓	🕓	🕓	—	—	four o’clock
925	U+1F55F	🕟	🕟	🕟	🕟	🕟	🕟	🕟	🕟	—	—	—	—	four-thirty
926	U+1F554	🕔	🕔	🕔	🕔	🕔	🕔	🕔	🕔	🕔	🕔	—	—	five o’clock
927	U+1F560	🕠	🕠	🕠	🕠	🕠	🕠	🕠	🕠	—	—	—	—	five-thirty
928	U+1F555	🕕	🕕	🕕	🕕	🕕	🕕	🕕	🕕	🕕	🕕	—	—	six o’clock
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
929	U+1F561	🕡	🕡	🕡	🕡	🕡	🕡	🕡	🕡	—	—	—	—	six-thirty
930	U+1F556	🕖	🕖	🕖	🕖	🕖	🕖	🕖	🕖	🕖	🕖	—	—	seven o’clock
931	U+1F562	🕢	🕢	🕢	🕢	🕢	🕢	🕢	🕢	—	—	—	—	seven-thirty
932	U+1F557	🕗	🕗	🕗	🕗	🕗	🕗	🕗	🕗	🕗	🕗	—	—	eight o’clock
933	U+1F563	🕣	🕣	🕣	🕣	🕣	🕣	🕣	🕣	—	—	—	—	eight-thirty
934	U+1F558	🕘	🕘	🕘	🕘	🕘	🕘	🕘	🕘	🕘	🕘	—	—	nine o’clock
935	U+1F564	🕤	🕤	🕤	🕤	🕤	🕤	🕤	🕤	—	—	—	—	nine-thirty
936	U+1F559	🕙	🕙	🕙	🕙	🕙	🕙	🕙	🕙	🕙	🕙	—	—	ten o’clock
937	U+1F565	🕥	🕥	🕥	🕥	🕥	🕥	🕥	🕥	—	—	—	—	ten-thirty
938	U+1F55A	🕚	🕚	🕚	🕚	🕚	🕚	🕚	🕚	🕚	🕚	—	—	eleven o’clock
939	U+1F566	🕦	🕦	🕦	🕦	🕦	🕦	🕦	🕦	—	—	—	—	eleven-thirty
sky & weather
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
940	U+1F311	🌑	🌑	🌑	🌑	🌑	🌑	🌑	🌑	🌑	—	🌑	🌑	new moon
941	U+1F312	🌒	🌒	🌒	🌒	🌒	🌒	🌒	🌒	—	—	—	—	waxing crescent moon
942	U+1F313	🌓	🌓	🌓	🌓	🌓	🌓	🌓	🌓	🌓	—	🌓	🌓	first quarter moon
943	U+1F314	🌔	🌔	🌔	🌔	🌔	🌔	🌔	🌔	🌔	—	🌔	🌔	waxing gibbous moon
944	U+1F315	🌕	🌕	🌕	🌕	🌕	🌕	🌕	🌕	🌕	—	🌕	—	full moon
945	U+1F316	🌖	🌖	🌖	🌖	🌖	🌖	🌖	🌖	—	—	—	—	waning gibbous moon
946	U+1F317	🌗	🌗	🌗	🌗	🌗	🌗	🌗	🌗	—	—	—	—	last quarter moon
947	U+1F318	🌘	🌘	🌘	🌘	🌘	🌘	🌘	🌘	—	—	—	—	waning crescent moon
948	U+1F319	🌙	🌙	🌙	🌙	🌙	🌙	🌙	🌙	🌙	🌙	🌙	🌙	crescent moon
949	U+1F31A	🌚	🌚	🌚	🌚	🌚	🌚	🌚	🌚	—	—	—	—	new moon face
950	U+1F31B	🌛	🌛	🌛	🌛	🌛	🌛	🌛	🌛	🌛	—	—	🌛	first quarter moon face
951	U+1F31C	🌜	🌜	🌜	🌜	🌜	🌜	🌜	🌜	—	—	—	—	last quarter moon face
952	U+1F321	🌡	🌡	🌡	🌡	🌡	🌡	🌡	🌡	—	—	—	—	thermometer
953	U+2600	☀	☀	☀	☀	☀	☀	☀	☀	☀	☀	☀	☀	sun
954	U+1F31D	🌝	🌝	🌝	🌝	🌝	🌝	🌝	🌝	—	—	—	—	full moon face
955	U+1F31E	🌞	🌞	🌞	🌞	🌞	🌞	🌞	🌞	—	—	—	—	sun with face
956	U+1FA90	🪐	🪐	🪐	🪐	🪐	🪐	🪐	🪐	—	—	—	—	ringed planet
957	U+2B50	⭐	⭐	⭐	⭐	⭐	⭐	⭐	⭐	—	⭐	—	⭐	star
958	U+1F31F	🌟	🌟	🌟	🌟	🌟	🌟	🌟	🌟	🌟	🌟	—	—	glowing star
959	U+1F320	🌠	🌠	🌠	🌠	🌠	🌠	🌠	🌠	🌠	—	—	🌠	shooting star
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
960	U+1F30C	🌌	🌌	🌌	🌌	🌌	🌌	🌌	🌌	🌌	—	—	🌌	milky way
961	U+2601	☁	☁	☁	☁	☁	☁	☁	☁	☁	☁	☁	☁	cloud
962	U+26C5	⛅	⛅	⛅	⛅	⛅	⛅	⛅	⛅	⛅	—	—	⛅	sun behind cloud
963	U+26C8	⛈	⛈	⛈	⛈	⛈	⛈	⛈	⛈	—	—	—	—	cloud with lightning and rain
964	U+1F324	🌤	🌤	🌤	🌤	🌤	🌤	🌤	🌤	—	—	—	—	sun behind small cloud
965	U+1F325	🌥	🌥	🌥	🌥	🌥	🌥	🌥	🌥	—	—	—	—	sun behind large cloud
966	U+1F326	🌦	🌦	🌦	🌦	🌦	🌦	🌦	🌦	—	—	—	—	sun behind rain cloud
967	U+1F327	🌧	🌧	🌧	🌧	🌧	🌧	🌧	🌧	—	—	—	—	cloud with rain
968	U+1F328	🌨	🌨	🌨	🌨	🌨	🌨	🌨	🌨	—	—	—	—	cloud with snow
969	U+1F329	🌩	🌩	🌩	🌩	🌩	🌩	🌩	🌩	—	—	—	—	cloud with lightning
970	U+1F32A	🌪	🌪	🌪	🌪	🌪	🌪	🌪	🌪	—	—	—	—	tornado
971	U+1F32B	🌫	🌫	🌫	🌫	🌫	🌫	🌫	🌫	—	—	—	—	fog
972	U+1F32C	🌬	🌬	🌬	🌬	🌬	🌬	🌬	🌬	—	—	—	—	wind face
973	U+1F300	🌀	🌀	🌀	🌀	🌀	🌀	🌀	🌀	🌀	🌀	🌀	🌀	cyclone
974	U+1F308	🌈	🌈	🌈	🌈	🌈	🌈	🌈	🌈	🌈	🌈	—	🌈	rainbow
975	U+1F302	🌂	🌂	🌂	🌂	🌂	🌂	🌂	🌂	🌂	🌂	🌂	🌂	closed umbrella
976	U+2602	☂	☂	☂	☂	☂	☂	☂	☂	—	—	—	—	umbrella
977	U+2614	☔	☔	☔	☔	☔	☔	☔	☔	☔	☔	☔	☔	umbrella with rain drops
978	U+26F1	⛱	⛱	⛱	⛱	⛱	⛱	⛱	⛱	—	—	—	—	umbrella on ground
979	U+26A1	⚡	⚡	⚡	⚡	⚡	⚡	⚡	⚡	⚡	⚡	⚡	⚡	high voltage
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
980	U+2744	❄	❄	❄	❄	❄	❄	❄	❄	❄	—	—	❄	snowflake
981	U+2603	☃	☃	☃	☃	☃	☃	☃	☃	—	—	—	—	snowman
982	U+26C4	⛄	⛄	⛄	⛄	⛄	⛄	⛄	⛄	⛄	⛄	⛄	⛄	snowman without snow
983	U+2604	☄	☄	☄	☄	☄	☄	☄	☄	—	—	—	—	comet
984	U+1F525	🔥	🔥	🔥	🔥	🔥	🔥	🔥	🔥	🔥	🔥	—	🔥	fire
985	U+1F4A7	💧	💧	💧	💧	💧	💧	💧	💧	💧	—	💧	💧	droplet
986	U+1F30A	🌊	🌊	🌊	🌊	🌊	🌊	🌊	🌊	🌊	🌊	🌊	🌊	water wave
Activities
event
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
987	U+1F383	🎃	🎃	🎃	🎃	🎃	🎃	🎃	🎃	🎃	🎃	—	🎃	jack-o-lantern
988	U+1F384	🎄	🎄	🎄	🎄	🎄	🎄	🎄	🎄	🎄	🎄	🎄	🎄	Christmas tree
989	U+1F386	🎆	🎆	🎆	🎆	🎆	🎆	🎆	🎆	🎆	🎆	—	🎆	fireworks
990	U+1F387	🎇	🎇	🎇	🎇	🎇	🎇	🎇	🎇	🎇	🎇	—	🎇	sparkler
991	U+1F9E8	🧨	🧨	🧨	🧨	🧨	🧨	🧨	🧨	—	—	—	—	firecracker
992	U+2728	✨	✨	✨	✨	✨	✨	✨	✨	✨	✨	✨	✨	sparkles
993	U+1F388	🎈	🎈	🎈	🎈	🎈	🎈	🎈	🎈	🎈	🎈	—	🎈	balloon
994	U+1F389	🎉	🎉	🎉	🎉	🎉	🎉	🎉	🎉	🎉	🎉	—	🎉	party popper
995	U+1F38A	🎊	🎊	🎊	🎊	🎊	🎊	🎊	🎊	🎊	—	—	🎊	confetti ball
996	U+1F38B	🎋	🎋	🎋	🎋	🎋	🎋	🎋	🎋	🎋	—	—	🎋	tanabata tree
997	U+1F38D	🎍	🎍	🎍	🎍	🎍	🎍	🎍	🎍	🎍	🎍	—	🎍	pine decoration
998	U+1F38E	🎎	🎎	🎎	🎎	🎎	🎎	🎎	🎎	🎎	🎎	—	🎎	Japanese dolls
999	U+1F38F	🎏	🎏	🎏	🎏	🎏	🎏	🎏	🎏	🎏	🎏	—	🎏	carp streamer
1000	U+1F390	🎐	🎐	🎐	🎐	🎐	🎐	🎐	🎐	🎐	🎐	—	🎐	wind chime
1001	U+1F391	🎑	🎑	🎑	🎑	🎑	🎑	🎑	🎑	🎑	🎑	—	🎑	moon viewing ceremony
1002	U+1F9E7	🧧	🧧	🧧	🧧	🧧	🧧	🧧	🧧	—	—	—	—	red envelope
1003	U+1F380	🎀	🎀	🎀	🎀	🎀	🎀	🎀	🎀	🎀	🎀	🎀	🎀	ribbon
1004	U+1F381	🎁	🎁	🎁	🎁	🎁	🎁	🎁	🎁	🎁	🎁	🎁	🎁	wrapped gift
1005	U+1F397	🎗	🎗	🎗	🎗	🎗	🎗	🎗	🎗	—	—	—	—	reminder ribbon
1006	U+1F39F	🎟	🎟	🎟	🎟	🎟	🎟	🎟	🎟	—	—	—	—	admission tickets
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1007	U+1F3AB	🎫	🎫	🎫	🎫	🎫	🎫	🎫	🎫	🎫	🎫	🎫	🎫	ticket
award-medal
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1008	U+1F396	🎖	🎖	🎖	🎖	🎖	🎖	🎖	🎖	—	—	—	—	military medal
1009	U+1F3C6	🏆	🏆	🏆	🏆	🏆	🏆	🏆	🏆	🏆	🏆	—	🏆	trophy
1010	U+1F3C5	🏅	🏅	🏅	🏅	🏅	🏅	🏅	🏅	—	—	—	—	sports medal
1011	U+1F947	🥇	🥇	🥇	🥇	🥇	🥇	🥇	🥇	—	—	—	—	1st place medal
1012	U+1F948	🥈	🥈	🥈	🥈	🥈	🥈	🥈	🥈	—	—	—	—	2nd place medal
1013	U+1F949	🥉	🥉	🥉	🥉	🥉	🥉	🥉	🥉	—	—	—	—	3rd place medal
sport
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1014	U+26BD	⚽	⚽	⚽	⚽	⚽	⚽	⚽	⚽	⚽	⚽	⚽	⚽	soccer ball
1015	U+26BE	⚾	⚾	⚾	⚾	⚾	⚾	⚾	⚾	⚾	⚾	⚾	⚾	baseball
1016	U+1F94E	🥎	🥎	🥎	🥎	🥎	🥎	🥎	🥎	—	—	—	—	softball
1017	U+1F3C0	🏀	🏀	🏀	🏀	🏀	🏀	🏀	🏀	🏀	🏀	🏀	🏀	basketball
1018	U+1F3D0	🏐	🏐	🏐	🏐	🏐	🏐	🏐	🏐	—	—	—	—	volleyball
1019	U+1F3C8	🏈	🏈	🏈	🏈	🏈	🏈	🏈	🏈	🏈	🏈	—	🏈	american football
1020	U+1F3C9	🏉	🏉	🏉	🏉	🏉	🏉	🏉	🏉	—	—	—	—	rugby football
1021	U+1F3BE	🎾	🎾	🎾	🎾	🎾	🎾	🎾	🎾	🎾	🎾	🎾	🎾	tennis
1022	U+1F94F	🥏	🥏	🥏	🥏	🥏	🥏	🥏	🥏	—	—	—	—	flying disc
1023	U+1F3B3	🎳	🎳	🎳	🎳	🎳	🎳	🎳	🎳	🎳	—	—	🎳	bowling
1024	U+1F3CF	🏏	🏏	🏏	🏏	🏏	🏏	🏏	🏏	—	—	—	—	cricket game
1025	U+1F3D1	🏑	🏑	🏑	🏑	🏑	🏑	🏑	🏑	—	—	—	—	field hockey
1026	U+1F3D2	🏒	🏒	🏒	🏒	🏒	🏒	🏒	🏒	—	—	—	—	ice hockey
1027	U+1F94D	🥍	🥍	🥍	🥍	🥍	🥍	🥍	🥍	—	—	—	—	lacrosse
1028	U+1F3D3	🏓	🏓	🏓	🏓	🏓	🏓	🏓	🏓	—	—	—	—	ping pong
1029	U+1F3F8	🏸	🏸	🏸	🏸	🏸	🏸	🏸	🏸	—	—	—	—	badminton
1030	U+1F94A	🥊	🥊	🥊	🥊	🥊	🥊	🥊	🥊	—	—	—	—	boxing glove
1031	U+1F94B	🥋	🥋	🥋	🥋	🥋	🥋	🥋	🥋	—	—	—	—	martial arts uniform
1032	U+1F945	🥅	🥅	🥅	🥅	🥅	🥅	🥅	🥅	—	—	—	—	goal net
1033	U+26F3	⛳	⛳	⛳	⛳	⛳	⛳	⛳	⛳	⛳	⛳	⛳	⛳	flag in hole
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1034	U+26F8	⛸	⛸	⛸	⛸	⛸	⛸	⛸	⛸	—	—	—	—	ice skate
1035	U+1F3A3	🎣	🎣	🎣	🎣	🎣	🎣	🎣	🎣	🎣	—	—	🎣	fishing pole
1036	U+1F93F	🤿	🤿	🤿	🤿	🤿	🤿	🤿	🤿	—	—	—	—	diving mask
1037	U+1F3BD	🎽	🎽	🎽	🎽	🎽	🎽	🎽	🎽	🎽	—	🎽	—	running shirt
1038	U+1F3BF	🎿	🎿	🎿	🎿	🎿	🎿	🎿	🎿	🎿	🎿	🎿	🎿	skis
1039	U+1F6F7	🛷	🛷	🛷	🛷	🛷	🛷	🛷	🛷	—	—	—	—	sled
1040	U+1F94C	🥌	🥌	🥌	🥌	🥌	🥌	🥌	🥌	—	—	—	—	curling stone
game
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1041	U+1F3AF	🎯	🎯	🎯	🎯	🎯	🎯	🎯	🎯	🎯	🎯	—	🎯	direct hit
1042	U+1FA80	🪀	🪀	🪀	🪀	🪀	🪀	🪀	🪀	—	—	—	—	yo-yo
1043	U+1FA81	🪁	🪁	🪁	🪁	🪁	🪁	🪁	🪁	—	—	—	—	kite
1044	U+1F3B1	🎱	🎱	🎱	🎱	🎱	🎱	🎱	🎱	🎱	🎱	—	🎱	pool 8 ball
1045	U+1F52E	🔮	🔮	🔮	🔮	🔮	🔮	🔮	🔮	🔮	—	—	🔮	crystal ball
1046	U+1FA84	🪄	—	🪄	—	—	—	🪄	—	—	—	—	—	⊛ magic wand
1047	U+1F9FF	🧿	🧿	🧿	🧿	🧿	🧿	🧿	🧿	—	—	—	—	nazar amulet
1048	U+1F3AE	🎮	🎮	🎮	🎮	🎮	🎮	🎮	🎮	🎮	—	🎮	🎮	video game
1049	U+1F579	🕹	🕹	🕹	🕹	🕹	🕹	🕹	🕹	—	—	—	—	joystick
1050	U+1F3B0	🎰	🎰	🎰	🎰	🎰	🎰	🎰	🎰	🎰	🎰	—	🎰	slot machine
1051	U+1F3B2	🎲	🎲	🎲	🎲	🎲	🎲	🎲	🎲	🎲	—	—	🎲	game die
1052	U+1F9E9	🧩	🧩	🧩	🧩	🧩	🧩	🧩	🧩	—	—	—	—	puzzle piece
1053	U+1F9F8	🧸	🧸	🧸	🧸	🧸	🧸	🧸	🧸	—	—	—	—	teddy bear
1054	U+1FA85	🪅	—	🪅	—	—	—	🪅	—	—	—	—	—	⊛ piñata
1055	U+1FA86	🪆	—	🪆	—	—	—	🪆	—	—	—	—	—	⊛ nesting dolls
1056	U+2660	♠	♠	♠	♠	♠	♠	♠	♠	♠	♠	♠	♠	spade suit
1057	U+2665	♥	♥	♥	♥	♥	♥	♥	♥	♥	♥	♥	♥	heart suit
1058	U+2666	♦	♦	♦	♦	♦	♦	♦	♦	♦	♦	♦	♦	diamond suit
1059	U+2663	♣	♣	♣	♣	♣	♣	♣	♣	♣	♣	♣	♣	club suit
1060	U+265F	♟	♟	♟	♟	♟	♟	♟	♟	—	—	—	—	chess pawn
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1061	U+1F0CF	🃏	🃏	🃏	🃏	🃏	🃏	🃏	🃏	🃏	—	—	🃏	joker
1062	U+1F004	🀄	🀄	🀄	🀄	🀄	🀄	🀄	🀄	🀄	🀄	—	🀄	mahjong red dragon
1063	U+1F3B4	🎴	🎴	🎴	🎴	🎴	🎴	🎴	🎴	🎴	—	—	🎴	flower playing cards
arts & crafts
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1064	U+1F3AD	🎭	🎭	🎭	🎭	🎭	🎭	🎭	🎭	🎭	—	—	🎭	performing arts
1065	U+1F5BC	🖼	🖼	🖼	🖼	🖼	🖼	🖼	🖼	—	—	—	—	framed picture
1066	U+1F3A8	🎨	🎨	🎨	🎨	🎨	🎨	🎨	🎨	🎨	🎨	🎨	🎨	artist palette
1067	U+1F9F5	🧵	🧵	🧵	🧵	🧵	🧵	🧵	🧵	—	—	—	—	thread
1068	U+1FAA1	🪡	—	🪡	—	—	—	🪡	—	—	—	—	—	⊛ sewing needle
1069	U+1F9F6	🧶	🧶	🧶	🧶	🧶	🧶	🧶	🧶	—	—	—	—	yarn
1070	U+1FAA2	🪢	—	🪢	—	—	—	🪢	—	—	—	—	—	⊛ knot
Objects
clothing
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1071	U+1F453	👓	👓	👓	👓	👓	👓	👓	👓	👓	—	👓	👓	glasses
1072	U+1F576	🕶	🕶	🕶	🕶	🕶	🕶	🕶	🕶	—	—	—	—	sunglasses
1073	U+1F97D	🥽	🥽	🥽	🥽	🥽	🥽	🥽	🥽	—	—	—	—	goggles
1074	U+1F97C	🥼	🥼	🥼	🥼	🥼	🥼	🥼	🥼	—	—	—	—	lab coat
1075	U+1F9BA	🦺	🦺	🦺	🦺	🦺	🦺	🦺	🦺	—	—	—	—	safety vest
1076	U+1F454	👔	👔	👔	👔	👔	👔	👔	👔	👔	👔	—	👔	necktie
1077	U+1F455	👕	👕	👕	👕	👕	👕	👕	👕	👕	👕	👕	👕	t-shirt
1078	U+1F456	👖	👖	👖	👖	👖	👖	👖	👖	👖	—	👖	👖	jeans
1079	U+1F9E3	🧣	🧣	🧣	🧣	🧣	🧣	🧣	🧣	—	—	—	—	scarf
1080	U+1F9E4	🧤	🧤	🧤	🧤	🧤	🧤	🧤	🧤	—	—	—	—	gloves
1081	U+1F9E5	🧥	🧥	🧥	🧥	🧥	🧥	🧥	🧥	—	—	—	—	coat
1082	U+1F9E6	🧦	🧦	🧦	🧦	🧦	🧦	🧦	🧦	—	—	—	—	socks
1083	U+1F457	👗	👗	👗	👗	👗	👗	👗	👗	👗	👗	—	👗	dress
1084	U+1F458	👘	👘	👘	👘	👘	👘	👘	👘	👘	👘	—	👘	kimono
1085	U+1F97B	🥻	🥻	🥻	🥻	🥻	🥻	🥻	🥻	—	—	—	—	sari
1086	U+1FA71	🩱	🩱	🩱	🩱	🩱	🩱	🩱	🩱	—	—	—	—	one-piece swimsuit
1087	U+1FA72	🩲	🩲	🩲	🩲	🩲	🩲	🩲	🩲	—	—	—	—	briefs
1088	U+1FA73	🩳	🩳	🩳	🩳	🩳	🩳	🩳	🩳	—	—	—	—	shorts
1089	U+1F459	👙	👙	👙	👙	👙	👙	👙	👙	👙	👙	—	👙	bikini
1090	U+1F45A	👚	👚	👚	👚	👚	👚	👚	👚	👚	—	—	👚	woman’s clothes
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1091	U+1F45B	👛	👛	👛	👛	👛	👛	👛	👛	👛	—	👛	👛	purse
1092	U+1F45C	👜	👜	👜	👜	👜	👜	👜	👜	👜	👜	👜	👜	handbag
1093	U+1F45D	👝	👝	👝	👝	👝	👝	👝	👝	👝	—	👝	—	clutch bag
1094	U+1F6CD	🛍	🛍	🛍	🛍	🛍	🛍	🛍	🛍	—	—	—	—	shopping bags
1095	U+1F392	🎒	🎒	🎒	🎒	🎒	🎒	🎒	🎒	🎒	🎒	—	🎒	backpack
1096	U+1FA74	🩴	—	🩴	—	—	—	🩴	—	—	—	—	—	⊛ thong sandal
1097	U+1F45E	👞	👞	👞	👞	👞	👞	👞	👞	👞	—	—	👞	man’s shoe
1098	U+1F45F	👟	👟	👟	👟	👟	👟	👟	👟	👟	👟	👟	👟	running shoe
1099	U+1F97E	🥾	🥾	🥾	🥾	🥾	🥾	🥾	🥾	—	—	—	—	hiking boot
1100	U+1F97F	🥿	🥿	🥿	🥿	🥿	🥿	🥿	🥿	—	—	—	—	flat shoe
1101	U+1F460	👠	👠	👠	👠	👠	👠	👠	👠	👠	👠	👠	👠	high-heeled shoe
1102	U+1F461	👡	👡	👡	👡	👡	👡	👡	👡	👡	👡	—	—	woman’s sandal
1103	U+1FA70	🩰	🩰	🩰	🩰	🩰	🩰	🩰	🩰	—	—	—	—	ballet shoes
1104	U+1F462	👢	👢	👢	👢	👢	👢	👢	👢	👢	👢	—	👢	woman’s boot
1105	U+1F451	👑	👑	👑	👑	👑	👑	👑	👑	👑	👑	👑	👑	crown
1106	U+1F452	👒	👒	👒	👒	👒	👒	👒	👒	👒	👒	—	👒	woman’s hat
1107	U+1F3A9	🎩	🎩	🎩	🎩	🎩	🎩	🎩	🎩	🎩	🎩	🎩	🎩	top hat
1108	U+1F393	🎓	🎓	🎓	🎓	🎓	🎓	🎓	🎓	🎓	🎓	—	🎓	graduation cap
1109	U+1F9E2	🧢	🧢	🧢	🧢	🧢	🧢	🧢	🧢	—	—	—	—	billed cap
1110	U+1FA96	🪖	—	🪖	—	—	—	🪖	—	—	—	—	—	⊛ military helmet
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1111	U+26D1	⛑	⛑	⛑	⛑	⛑	⛑	⛑	⛑	—	—	—	—	rescue worker’s helmet
1112	U+1F4FF	📿	📿	📿	📿	📿	📿	📿	📿	—	—	—	—	prayer beads
1113	U+1F484	💄	💄	💄	💄	💄	💄	💄	💄	💄	💄	💄	💄	lipstick
1114	U+1F48D	💍	💍	💍	💍	💍	💍	💍	💍	💍	💍	💍	💍	ring
1115	U+1F48E	💎	💎	💎	💎	💎	💎	💎	💎	💎	💎	—	—	gem stone
sound
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1116	U+1F507	🔇	🔇	🔇	🔇	🔇	🔇	🔇	🔇	—	—	—	—	muted speaker
1117	U+1F508	🔈	🔈	🔈	🔈	🔈	🔈	🔈	🔈	—	—	—	—	speaker low volume
1118	U+1F509	🔉	🔉	🔉	🔉	🔉	🔉	🔉	🔉	—	—	—	—	speaker medium volume
1119	U+1F50A	🔊	🔊	🔊	🔊	🔊	🔊	🔊	🔊	🔊	🔊	—	🔊	speaker high volume
1120	U+1F4E2	📢	📢	📢	📢	📢	📢	📢	📢	📢	📢	—	—	loudspeaker
1121	U+1F4E3	📣	📣	📣	📣	📣	📣	📣	📣	📣	📣	—	—	megaphone
1122	U+1F4EF	📯	📯	📯	📯	📯	📯	📯	📯	—	—	—	—	postal horn
1123	U+1F514	🔔	🔔	🔔	🔔	🔔	🔔	🔔	🔔	🔔	🔔	🔔	🔔	bell
1124	U+1F515	🔕	🔕	🔕	🔕	🔕	🔕	🔕	🔕	—	—	—	—	bell with slash
music
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1125	U+1F3BC	🎼	🎼	🎼	🎼	🎼	🎼	🎼	🎼	🎼	—	—	🎼	musical score
1126	U+1F3B5	🎵	🎵	🎵	🎵	🎵	🎵	🎵	🎵	🎵	🎵	🎵	🎵	musical note
1127	U+1F3B6	🎶	🎶	🎶	🎶	🎶	🎶	🎶	🎶	🎶	🎶	🎶	🎶	musical notes
1128	U+1F399	🎙	🎙	🎙	🎙	🎙	🎙	🎙	🎙	—	—	—	—	studio microphone
1129	U+1F39A	🎚	🎚	🎚	🎚	🎚	🎚	🎚	🎚	—	—	—	—	level slider
1130	U+1F39B	🎛	🎛	🎛	🎛	🎛	🎛	🎛	🎛	—	—	—	—	control knobs
1131	U+1F3A4	🎤	🎤	🎤	🎤	🎤	🎤	🎤	🎤	🎤	🎤	🎤	🎤	microphone
1132	U+1F3A7	🎧	🎧	🎧	🎧	🎧	🎧	🎧	🎧	🎧	🎧	🎧	🎧	headphone
1133	U+1F4FB	📻	📻	📻	📻	📻	📻	📻	📻	📻	📻	—	📻	radio
musical-instrument
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1134	U+1F3B7	🎷	🎷	🎷	🎷	🎷	🎷	🎷	🎷	🎷	🎷	—	—	saxophone
1135	U+1FA97	🪗	—	🪗	—	—	—	🪗	—	—	—	—	—	⊛ accordion
1136	U+1F3B8	🎸	🎸	🎸	🎸	🎸	🎸	🎸	🎸	🎸	🎸	—	🎸	guitar
1137	U+1F3B9	🎹	🎹	🎹	🎹	🎹	🎹	🎹	🎹	🎹	—	—	🎹	musical keyboard
1138	U+1F3BA	🎺	🎺	🎺	🎺	🎺	🎺	🎺	🎺	🎺	🎺	—	🎺	trumpet
1139	U+1F3BB	🎻	🎻	🎻	🎻	🎻	🎻	🎻	🎻	🎻	—	—	🎻	violin
1140	U+1FA95	🪕	🪕	🪕	🪕	🪕	🪕	🪕	🪕	—	—	—	—	banjo
1141	U+1F941	🥁	🥁	🥁	🥁	🥁	🥁	🥁	🥁	—	—	—	—	drum
1142	U+1FA98	🪘	—	🪘	—	—	—	🪘	—	—	—	—	—	⊛ long drum
phone
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1143	U+1F4F1	📱	📱	📱	📱	📱	📱	📱	📱	📱	📱	📱	📱	mobile phone
1144	U+1F4F2	📲	📲	📲	📲	📲	📲	📲	📲	📲	📲	📲	📲	mobile phone with arrow
1145	U+260E	☎	☎	☎	☎	☎	☎	☎	☎	☎	☎	☎	☎	telephone
1146	U+1F4DE	📞	📞	📞	📞	📞	📞	📞	📞	📞	—	—	📞	telephone receiver
1147	U+1F4DF	📟	📟	📟	📟	📟	📟	📟	📟	📟	—	📟	📟	pager
1148	U+1F4E0	📠	📠	📠	📠	📠	📠	📠	📠	📠	📠	📠	📠	fax machine
computer
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1149	U+1F50B	🔋	🔋	🔋	🔋	🔋	🔋	🔋	🔋	🔋	—	—	🔋	battery
1150	U+1F50C	🔌	🔌	🔌	🔌	🔌	🔌	🔌	🔌	🔌	—	—	🔌	electric plug
1151	U+1F4BB	💻	💻	💻	💻	💻	💻	💻	💻	💻	💻	💻	💻	laptop
1152	U+1F5A5	🖥	🖥	🖥	🖥	🖥	🖥	🖥	🖥	—	—	—	—	desktop computer
1153	U+1F5A8	🖨	🖨	🖨	🖨	🖨	🖨	🖨	🖨	—	—	—	—	printer
1154	U+2328	⌨	⌨	⌨	⌨	⌨	⌨	⌨	⌨	—	—	—	—	keyboard
1155	U+1F5B1	🖱	🖱	🖱	🖱	🖱	🖱	🖱	🖱	—	—	—	—	computer mouse
1156	U+1F5B2	🖲	🖲	🖲	🖲	🖲	🖲	🖲	🖲	—	—	—	—	trackball
1157	U+1F4BD	💽	💽	💽	💽	💽	💽	💽	💽	💽	💽	—	💽	computer disk
1158	U+1F4BE	💾	💾	💾	💾	💾	💾	💾	💾	💾	—	—	💾	floppy disk
1159	U+1F4BF	💿	💿	💿	💿	💿	💿	💿	💿	💿	💿	💿	💿	optical disk
1160	U+1F4C0	📀	📀	📀	📀	📀	📀	📀	📀	📀	📀	—	—	dvd
1161	U+1F9EE	🧮	🧮	🧮	🧮	🧮	🧮	🧮	🧮	—	—	—	—	abacus
light & video
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1162	U+1F3A5	🎥	🎥	🎥	🎥	🎥	🎥	🎥	🎥	🎥	🎥	🎥	🎥	movie camera
1163	U+1F39E	🎞	🎞	🎞	🎞	🎞	🎞	🎞	🎞	—	—	—	—	film frames
1164	U+1F4FD	📽	📽	📽	📽	📽	📽	📽	📽	—	—	—	—	film projector
1165	U+1F3AC	🎬	🎬	🎬	🎬	🎬	🎬	🎬	🎬	🎬	🎬	🎬	🎬	clapper board
1166	U+1F4FA	📺	📺	📺	📺	📺	📺	📺	📺	📺	📺	📺	📺	television
1167	U+1F4F7	📷	📷	📷	📷	📷	📷	📷	📷	📷	📷	📷	📷	camera
1168	U+1F4F8	📸	📸	📸	📸	📸	📸	📸	📸	—	—	—	—	camera with flash
1169	U+1F4F9	📹	📹	📹	📹	📹	📹	📹	📹	📹	—	—	📹	video camera
1170	U+1F4FC	📼	📼	📼	📼	📼	📼	📼	📼	📼	📼	—	📼	videocassette
1171	U+1F50D	🔍	🔍	🔍	🔍	🔍	🔍	🔍	🔍	🔍	🔍	🔍	🔍	magnifying glass tilted left
1172	U+1F50E	🔎	🔎	🔎	🔎	🔎	🔎	🔎	🔎	🔎	—	—	🔎	magnifying glass tilted right
1173	U+1F56F	🕯	🕯	🕯	🕯	🕯	🕯	🕯	🕯	—	—	—	—	candle
1174	U+1F4A1	💡	💡	💡	💡	💡	💡	💡	💡	💡	💡	💡	💡	light bulb
1175	U+1F526	🔦	🔦	🔦	🔦	🔦	🔦	🔦	🔦	🔦	—	—	🔦	flashlight
1176	U+1F3EE	🏮	🏮	🏮	🏮	🏮	🏮	🏮	🏮	🏮	—	—	🏮	red paper lantern
1177	U+1FA94	🪔	🪔	🪔	🪔	🪔	🪔	🪔	🪔	—	—	—	—	diya lamp
book-paper
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1178	U+1F4D4	📔	📔	📔	📔	📔	📔	📔	📔	📔	—	—	📔	notebook with decorative cover
1179	U+1F4D5	📕	📕	📕	📕	📕	📕	📕	📕	📕	—	—	📕	closed book
1180	U+1F4D6	📖	📖	📖	📖	📖	📖	📖	📖	📖	📖	📖	📖	open book
1181	U+1F4D7	📗	📗	📗	📗	📗	📗	📗	📗	📗	—	—	📗	green book
1182	U+1F4D8	📘	📘	📘	📘	📘	📘	📘	📘	📘	—	—	📘	blue book
1183	U+1F4D9	📙	📙	📙	📙	📙	📙	📙	📙	📙	—	—	📙	orange book
1184	U+1F4DA	📚	📚	📚	📚	📚	📚	📚	📚	📚	—	—	📚	books
1185	U+1F4D3	📓	📓	📓	📓	📓	📓	📓	📓	📓	—	—	📓	notebook
1186	U+1F4D2	📒	📒	📒	📒	📒	📒	📒	📒	📒	—	—	📒	ledger
1187	U+1F4C3	📃	📃	📃	📃	📃	📃	📃	📃	📃	—	—	📃	page with curl
1188	U+1F4DC	📜	📜	📜	📜	📜	📜	📜	📜	📜	—	—	📜	scroll
1189	U+1F4C4	📄	📄	📄	📄	📄	📄	📄	📄	📄	—	—	📄	page facing up
1190	U+1F4F0	📰	📰	📰	📰	📰	📰	📰	📰	📰	—	—	📰	newspaper
1191	U+1F5DE	🗞	🗞	🗞	🗞	🗞	🗞	🗞	🗞	—	—	—	—	rolled-up newspaper
1192	U+1F4D1	📑	📑	📑	📑	📑	📑	📑	📑	📑	—	—	📑	bookmark tabs
1193	U+1F516	🔖	🔖	🔖	🔖	🔖	🔖	🔖	🔖	🔖	—	—	🔖	bookmark
1194	U+1F3F7	🏷	🏷	🏷	🏷	🏷	🏷	🏷	🏷	—	—	—	—	label
money
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1195	U+1F4B0	💰	💰	💰	💰	💰	💰	💰	💰	💰	💰	💰	💰	money bag
1196	U+1FA99	🪙	—	🪙	—	—	—	🪙	—	—	—	—	—	⊛ coin
1197	U+1F4B4	💴	💴	💴	💴	💴	💴	💴	💴	💴	—	💴	💴	yen banknote
1198	U+1F4B5	💵	💵	💵	💵	💵	💵	💵	💵	💵	—	—	💵	dollar banknote
1199	U+1F4B6	💶	💶	💶	💶	💶	💶	💶	💶	—	—	—	—	euro banknote
1200	U+1F4B7	💷	💷	💷	💷	💷	💷	💷	💷	—	—	—	—	pound banknote
1201	U+1F4B8	💸	💸	💸	💸	💸	💸	💸	💸	💸	—	—	💸	money with wings
1202	U+1F4B3	💳	💳	💳	💳	💳	💳	💳	💳	💳	—	—	💳	credit card
1203	U+1F9FE	🧾	🧾	🧾	🧾	🧾	🧾	🧾	🧾	—	—	—	—	receipt
1204	U+1F4B9	💹	💹	💹	💹	💹	💹	💹	💹	💹	💹	—	💹	chart increasing with yen
mail
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1205	U+2709	✉	✉	✉	✉	✉	✉	✉	✉	✉	—	✉	✉	envelope
1206	U+1F4E7	📧	📧	📧	📧	📧	📧	📧	📧	📧	—	—	📧	e-mail
1207	U+1F4E8	📨	📨	📨	📨	📨	📨	📨	📨	📨	—	—	📨	incoming envelope
1208	U+1F4E9	📩	📩	📩	📩	📩	📩	📩	📩	📩	📩	📩	📩	envelope with arrow
1209	U+1F4E4	📤	📤	📤	📤	📤	📤	📤	📤	📤	—	—	📤	outbox tray
1210	U+1F4E5	📥	📥	📥	📥	📥	📥	📥	📥	📥	—	—	📥	inbox tray
1211	U+1F4E6	📦	📦	📦	📦	📦	📦	📦	📦	📦	—	—	📦	package
1212	U+1F4EB	📫	📫	📫	📫	📫	📫	📫	📫	📫	📫	—	📫	closed mailbox with raised flag
1213	U+1F4EA	📪	📪	📪	📪	📪	📪	📪	📪	📪	—	—	📪	closed mailbox with lowered flag
1214	U+1F4EC	📬	📬	📬	📬	📬	📬	📬	📬	—	—	—	—	open mailbox with raised flag
1215	U+1F4ED	📭	📭	📭	📭	📭	📭	📭	📭	—	—	—	—	open mailbox with lowered flag
1216	U+1F4EE	📮	📮	📮	📮	📮	📮	📮	📮	📮	📮	—	—	postbox
1217	U+1F5F3	🗳	🗳	🗳	🗳	🗳	🗳	🗳	🗳	—	—	—	—	ballot box with ballot
writing
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1218	U+270F	✏	✏	✏	✏	✏	✏	✏	✏	✏	—	✏	✏	pencil
1219	U+2712	✒	✒	✒	✒	✒	✒	✒	✒	✒	—	✒	✒	black nib
1220	U+1F58B	🖋	🖋	🖋	🖋	🖋	🖋	🖋	🖋	—	—	—	—	fountain pen
1221	U+1F58A	🖊	🖊	🖊	🖊	🖊	🖊	🖊	🖊	—	—	—	—	pen
1222	U+1F58C	🖌	🖌	🖌	🖌	🖌	🖌	🖌	🖌	—	—	—	—	paintbrush
1223	U+1F58D	🖍	🖍	🖍	🖍	🖍	🖍	🖍	🖍	—	—	—	—	crayon
1224	U+1F4DD	📝	📝	📝	📝	📝	📝	📝	📝	📝	📝	📝	📝	memo
office
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1225	U+1F4BC	💼	💼	💼	💼	💼	💼	💼	💼	💼	💼	—	💼	briefcase
1226	U+1F4C1	📁	📁	📁	📁	📁	📁	📁	📁	📁	—	—	📁	file folder
1227	U+1F4C2	📂	📂	📂	📂	📂	📂	📂	📂	📂	—	—	📂	open file folder
1228	U+1F5C2	🗂	🗂	🗂	🗂	🗂	🗂	🗂	🗂	—	—	—	—	card index dividers
1229	U+1F4C5	📅	📅	📅	📅	📅	📅	📅	📅	📅	—	—	📅	calendar
1230	U+1F4C6	📆	📆	📆	📆	📆	📆	📆	📆	📆	—	—	📆	tear-off calendar
1231	U+1F5D2	🗒	🗒	🗒	🗒	🗒	🗒	🗒	🗒	—	—	—	—	spiral notepad
1232	U+1F5D3	🗓	🗓	🗓	🗓	🗓	🗓	🗓	🗓	—	—	—	—	spiral calendar
1233	U+1F4C7	📇	📇	📇	📇	📇	📇	📇	📇	📇	—	—	📇	card index
1234	U+1F4C8	📈	📈	📈	📈	📈	📈	📈	📈	📈	—	—	📈	chart increasing
1235	U+1F4C9	📉	📉	📉	📉	📉	📉	📉	📉	📉	—	—	📉	chart decreasing
1236	U+1F4CA	📊	📊	📊	📊	📊	📊	📊	📊	📊	—	—	📊	bar chart
1237	U+1F4CB	📋	📋	📋	📋	📋	📋	📋	📋	📋	—	—	📋	clipboard
1238	U+1F4CC	📌	📌	📌	📌	📌	📌	📌	📌	📌	—	—	📌	pushpin
1239	U+1F4CD	📍	📍	📍	📍	📍	📍	📍	📍	📍	—	—	📍	round pushpin
1240	U+1F4CE	📎	📎	📎	📎	📎	📎	📎	📎	📎	—	📎	📎	paperclip
1241	U+1F587	🖇	🖇	🖇	🖇	🖇	🖇	🖇	🖇	—	—	—	—	linked paperclips
1242	U+1F4CF	📏	📏	📏	📏	📏	📏	📏	📏	📏	—	—	📏	straight ruler
1243	U+1F4D0	📐	📐	📐	📐	📐	📐	📐	📐	📐	—	—	📐	triangular ruler
1244	U+2702	✂	✂	✂	✂	✂	✂	✂	✂	✂	✂	✂	✂	scissors
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1245	U+1F5C3	🗃	🗃	🗃	🗃	🗃	🗃	🗃	🗃	—	—	—	—	card file box
1246	U+1F5C4	🗄	🗄	🗄	🗄	🗄	🗄	🗄	🗄	—	—	—	—	file cabinet
1247	U+1F5D1	🗑	🗑	🗑	🗑	🗑	🗑	🗑	🗑	—	—	—	—	wastebasket
lock
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1248	U+1F512	🔒	🔒	🔒	🔒	🔒	🔒	🔒	🔒	🔒	🔒	—	🔒	locked
1249	U+1F513	🔓	🔓	🔓	🔓	🔓	🔓	🔓	🔓	🔓	🔓	—	—	unlocked
1250	U+1F50F	🔏	🔏	🔏	🔏	🔏	🔏	🔏	🔏	🔏	—	—	🔏	locked with pen
1251	U+1F510	🔐	🔐	🔐	🔐	🔐	🔐	🔐	🔐	🔐	—	—	🔐	locked with key
1252	U+1F511	🔑	🔑	🔑	🔑	🔑	🔑	🔑	🔑	🔑	🔑	🔑	🔑	key
1253	U+1F5DD	🗝	🗝	🗝	🗝	🗝	🗝	🗝	🗝	—	—	—	—	old key
tool
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1254	U+1F528	🔨	🔨	🔨	🔨	🔨	🔨	🔨	🔨	🔨	🔨	—	🔨	hammer
1255	U+1FA93	🪓	🪓	🪓	🪓	🪓	🪓	🪓	🪓	—	—	—	—	axe
1256	U+26CF	⛏	⛏	⛏	⛏	⛏	⛏	⛏	⛏	—	—	—	—	pick
1257	U+2692	⚒	⚒	⚒	⚒	⚒	⚒	⚒	⚒	—	—	—	—	hammer and pick
1258	U+1F6E0	🛠	🛠	🛠	🛠	🛠	🛠	🛠	🛠	—	—	—	—	hammer and wrench
1259	U+1F5E1	🗡	🗡	🗡	🗡	🗡	🗡	🗡	🗡	—	—	—	—	dagger
1260	U+2694	⚔	⚔	⚔	⚔	⚔	⚔	⚔	⚔	—	—	—	—	crossed swords
1261	U+1F52B	🔫	🔫	🔫	🔫	🔫	🔫	🔫	🔫	🔫	🔫	—	🔫	pistol
1262	U+1FA83	🪃	—	🪃	—	—	—	🪃	—	—	—	—	—	⊛ boomerang
1263	U+1F3F9	🏹	🏹	🏹	🏹	🏹	🏹	🏹	🏹	—	—	—	—	bow and arrow
1264	U+1F6E1	🛡	🛡	🛡	🛡	🛡	🛡	🛡	🛡	—	—	—	—	shield
1265	U+1FA9A	🪚	… 🪚 🪚 🪚 …	⊛ carpentry saw
1266	U+1F527	🔧	🔧	🔧	🔧	🔧	🔧	🔧	🔧	🔧	—	🔧	🔧	wrench
1267	U+1FA9B	🪛	—	🪛	—	—	—	🪛	—	—	—	—	—	⊛ screwdriver
1268	U+1F529	🔩	🔩	🔩	🔩	🔩	🔩	🔩	🔩	🔩	—	—	🔩	nut and bolt
1269	U+2699	⚙	⚙	⚙	⚙	⚙	⚙	⚙	⚙	—	—	—	—	gear
1270	U+1F5DC	🗜	🗜	🗜	🗜	🗜	🗜	🗜	🗜	—	—	—	—	clamp
1271	U+2696	⚖	⚖	⚖	⚖	⚖	⚖	⚖	⚖	—	—	—	—	balance scale
1272	U+1F9AF	🦯	🦯	🦯	🦯	🦯	🦯	🦯	🦯	—	—	—	—	white cane
1273	U+1F517	🔗	🔗	🔗	🔗	🔗	🔗	🔗	🔗	🔗	—	—	🔗	link
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1274	U+26D3	⛓	⛓	⛓	⛓	⛓	⛓	⛓	⛓	—	—	—	—	chains
1275	U+1FA9D	🪝	—	🪝	—	—	—	🪝	—	—	—	—	—	⊛ hook
1276	U+1F9F0	🧰	🧰	🧰	🧰	🧰	🧰	🧰	🧰	—	—	—	—	toolbox
1277	U+1F9F2	🧲	🧲	🧲	🧲	🧲	🧲	🧲	🧲	—	—	—	—	magnet
1278	U+1FA9C	🪜	—	🪜	—	—	—	🪜	—	—	—	—	—	⊛ ladder
science
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1279	U+2697	⚗	⚗	⚗	⚗	⚗	⚗	⚗	⚗	—	—	—	—	alembic
1280	U+1F9EA	🧪	🧪	🧪	🧪	🧪	🧪	🧪	🧪	—	—	—	—	test tube
1281	U+1F9EB	🧫	🧫	🧫	🧫	🧫	🧫	🧫	🧫	—	—	—	—	petri dish
1282	U+1F9EC	🧬	🧬	🧬	🧬	🧬	🧬	🧬	🧬	—	—	—	—	dna
1283	U+1F52C	🔬	🔬	🔬	🔬	🔬	🔬	🔬	🔬	—	—	—	—	microscope
1284	U+1F52D	🔭	🔭	🔭	🔭	🔭	🔭	🔭	🔭	—	—	—	—	telescope
1285	U+1F4E1	📡	📡	📡	📡	📡	📡	📡	📡	📡	📡	—	📡	satellite antenna
medical
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1286	U+1F489	💉	💉	💉	💉	💉	💉	💉	💉	💉	💉	—	💉	syringe
1287	U+1FA78	🩸	🩸	🩸	🩸	🩸	🩸	🩸	🩸	—	—	—	—	drop of blood
1288	U+1F48A	💊	💊	💊	💊	💊	💊	💊	💊	💊	💊	—	💊	pill
1289	U+1FA79	🩹	🩹	🩹	🩹	🩹	🩹	🩹	🩹	—	—	—	—	adhesive bandage
1290	U+1FA7A	🩺	🩺	🩺	🩺	🩺	🩺	🩺	🩺	—	—	—	—	stethoscope
household
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1291	U+1F6AA	🚪	🚪	🚪	🚪	🚪	🚪	🚪	🚪	🚪	—	🚪	—	door
1292	U+1F6D7	🛗	—	🛗	—	—	—	🛗	—	—	—	—	—	⊛ elevator
1293	U+1FA9E	🪞	… 🪞 🪞 🪞 …	⊛ mirror
1294	U+1FA9F	🪟	… 🪟 🪟 🪟 …	⊛ window
1295	U+1F6CF	🛏	🛏	🛏	🛏	🛏	🛏	🛏	🛏	—	—	—	—	bed
1296	U+1F6CB	🛋	🛋	🛋	🛋	🛋	🛋	🛋	🛋	—	—	—	—	couch and lamp
1297	U+1FA91	🪑	🪑	🪑	🪑	🪑	🪑	🪑	🪑	—	—	—	—	chair
1298	U+1F6BD	🚽	🚽	🚽	🚽	🚽	🚽	🚽	🚽	🚽	🚽	—	—	toilet
1299	U+1FAA0	🪠	—	🪠	—	—	—	🪠	—	—	—	—	—	⊛ plunger
1300	U+1F6BF	🚿	🚿	🚿	🚿	🚿	🚿	🚿	🚿	—	—	—	—	shower
1301	U+1F6C1	🛁	🛁	🛁	🛁	🛁	🛁	🛁	🛁	—	—	—	—	bathtub
1302	U+1FAA4	🪤	… 🪤 🪤 🪤 …	⊛ mouse trap
1303	U+1FA92	🪒	🪒	🪒	🪒	🪒	🪒	🪒	🪒	—	—	—	—	razor
1304	U+1F9F4	🧴	🧴	🧴	🧴	🧴	🧴	🧴	🧴	—	—	—	—	lotion bottle
1305	U+1F9F7	🧷	🧷	🧷	🧷	🧷	🧷	🧷	🧷	—	—	—	—	safety pin
1306	U+1F9F9	🧹	🧹	🧹	🧹	🧹	🧹	🧹	🧹	—	—	—	—	broom
1307	U+1F9FA	🧺	🧺	🧺	🧺	🧺	🧺	🧺	🧺	—	—	—	—	basket
1308	U+1F9FB	🧻	🧻	🧻	🧻	🧻	🧻	🧻	🧻	—	—	—	—	roll of paper
1309	U+1FAA3	🪣	—	🪣	—	—	—	🪣	—	—	—	—	—	⊛ bucket
1310	U+1F9FC	🧼	🧼	🧼	🧼	🧼	🧼	🧼	🧼	—	—	—	—	soap
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1311	U+1FAA5	🪥	—	🪥	—	—	—	🪥	—	—	—	—	—	⊛ toothbrush
1312	U+1F9FD	🧽	🧽	🧽	🧽	🧽	🧽	🧽	🧽	—	—	—	—	sponge
1313	U+1F9EF	🧯	🧯	🧯	🧯	🧯	🧯	🧯	🧯	—	—	—	—	fire extinguisher
1314	U+1F6D2	🛒	🛒	🛒	🛒	🛒	🛒	🛒	🛒	—	—	—	—	shopping cart
other-object
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1315	U+1F6AC	🚬	🚬	🚬	🚬	🚬	🚬	🚬	🚬	🚬	🚬	🚬	🚬	cigarette
1316	U+26B0	⚰	⚰	⚰	⚰	⚰	⚰	⚰	⚰	—	—	—	—	coffin
1317	U+1FAA6	🪦	… 🪦 🪦 🪦 …	⊛ headstone
1318	U+26B1	⚱	⚱	⚱	⚱	⚱	⚱	⚱	⚱	—	—	—	—	funeral urn
1319	U+1F5FF	🗿	🗿	🗿	🗿	🗿	🗿	🗿	🗿	🗿	—	—	🗿	moai
1320	U+1FAA7	🪧	—	🪧	—	—	—	🪧	—	—	—	—	—	⊛ placard
Symbols
transport-sign
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1321	U+1F3E7	🏧	🏧	🏧	🏧	🏧	🏧	🏧	🏧	🏧	🏧	🏧	🏧	ATM sign
1322	U+1F6AE	🚮	🚮	🚮	🚮	🚮	🚮	🚮	🚮	—	—	—	—	litter in bin sign
1323	U+1F6B0	🚰	🚰	🚰	🚰	🚰	🚰	🚰	🚰	—	—	—	—	potable water
1324	U+267F	♿	♿	♿	♿	♿	♿	♿	♿	♿	♿	♿	♿	wheelchair symbol
1325	U+1F6B9	🚹	🚹	🚹	🚹	🚹	🚹	🚹	🚹	🚹	🚹	—	—	men’s room
1326	U+1F6BA	🚺	🚺	🚺	🚺	🚺	🚺	🚺	🚺	🚺	🚺	—	—	women’s room
1327	U+1F6BB	🚻	🚻	🚻	🚻	🚻	🚻	🚻	🚻	🚻	🚻	🚻	🚻	restroom
1328	U+1F6BC	🚼	🚼	🚼	🚼	🚼	🚼	🚼	🚼	🚼	🚼	—	—	baby symbol
1329	U+1F6BE	🚾	🚾	🚾	🚾	🚾	🚾	🚾	🚾	🚾	🚾	—	—	water closet
1330	U+1F6C2	🛂	🛂	🛂	🛂	🛂	🛂	🛂	🛂	—	—	—	—	passport control
1331	U+1F6C3	🛃	🛃	🛃	🛃	🛃	🛃	🛃	🛃	—	—	—	—	customs
1332	U+1F6C4	🛄	🛄	🛄	🛄	🛄	🛄	🛄	🛄	—	—	—	—	baggage claim
1333	U+1F6C5	🛅	🛅	🛅	🛅	🛅	🛅	🛅	🛅	—	—	—	—	left luggage
warning
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1334	U+26A0	⚠	⚠	⚠	⚠	⚠	⚠	⚠	⚠	⚠	⚠	⚠	⚠	warning
1335	U+1F6B8	🚸	🚸	🚸	🚸	🚸	🚸	🚸	🚸	—	—	—	—	children crossing
1336	U+26D4	⛔	⛔	⛔	⛔	⛔	⛔	⛔	⛔	⛔	—	—	⛔	no entry
1337	U+1F6AB	🚫	🚫	🚫	🚫	🚫	🚫	🚫	🚫	🚫	—	—	🚫	prohibited
1338	U+1F6B3	🚳	🚳	🚳	🚳	🚳	🚳	🚳	🚳	—	—	—	—	no bicycles
1339	U+1F6AD	🚭	🚭	🚭	🚭	🚭	🚭	🚭	🚭	🚭	🚭	🚭	🚭	no smoking
1340	U+1F6AF	🚯	🚯	🚯	🚯	🚯	🚯	🚯	🚯	—	—	—	—	no littering
1341	U+1F6B1	🚱	🚱	🚱	🚱	🚱	🚱	🚱	🚱	—	—	—	—	non-potable water
1342	U+1F6B7	🚷	🚷	🚷	🚷	🚷	🚷	🚷	🚷	—	—	—	—	no pedestrians
1343	U+1F4F5	📵	📵	📵	📵	📵	📵	📵	📵	—	—	—	—	no mobile phones
1344	U+1F51E	🔞	🔞	🔞	🔞	🔞	🔞	🔞	🔞	🔞	🔞	—	🔞	no one under eighteen
1345	U+2622	☢	☢	☢	☢	☢	☢	☢	☢	—	—	—	—	radioactive
1346	U+2623	☣	☣	☣	☣	☣	☣	☣	☣	—	—	—	—	biohazard
arrow
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1347	U+2B06	⬆	⬆	⬆	⬆	⬆	⬆	⬆	⬆	—	⬆	—	⬆	up arrow
1348	U+2197	↗	↗	↗	↗	↗	↗	↗	↗	↗	↗	↗	↗	up-right arrow
1349	U+27A1	➡	➡	➡	➡	➡	➡	➡	➡	—	➡	—	➡	right arrow
1350	U+2198	↘	↘	↘	↘	↘	↘	↘	↘	↘	↘	↘	↘	down-right arrow
1351	U+2B07	⬇	⬇	⬇	⬇	⬇	⬇	⬇	⬇	—	⬇	—	⬇	down arrow
1352	U+2199	↙	↙	↙	↙	↙	↙	↙	↙	↙	↙	↙	↙	down-left arrow
1353	U+2B05	⬅	⬅	⬅	⬅	⬅	⬅	⬅	⬅	—	⬅	—	⬅	left arrow
1354	U+2196	↖	↖	↖	↖	↖	↖	↖	↖	↖	↖	↖	↖	up-left arrow
1355	U+2195	↕	↕	↕	↕	↕	↕	↕	↕	↕	—	↕	↕	up-down arrow
1356	U+2194	↔	↔	↔	↔	↔	↔	↔	↔	↔	—	↔	↔	left-right arrow
1357	U+21A9	↩	↩	↩	↩	↩	↩	↩	↩	—	—	↩	↩	right arrow curving left
1358	U+21AA	↪	↪	↪	↪	↪	↪	↪	↪	↪	—	—	↪	left arrow curving right
1359	U+2934	⤴	⤴	⤴	⤴	⤴	⤴	⤴	⤴	⤴	—	⤴	⤴	right arrow curving up
1360	U+2935	⤵	⤵	⤵	⤵	⤵	⤵	⤵	⤵	⤵	—	⤵	⤵	right arrow curving down
1361	U+1F503	🔃	🔃	🔃	🔃	🔃	🔃	🔃	🔃	🔃	—	—	🔃	clockwise vertical arrows
1362	U+1F504	🔄	🔄	🔄	🔄	🔄	🔄	🔄	🔄	—	—	—	—	counterclockwise arrows button
1363	U+1F519	🔙	🔙	🔙	🔙	🔙	🔙	🔙	🔙	🔙	—	—	🔙	BACK arrow
1364	U+1F51A	🔚	🔚	🔚	🔚	🔚	🔚	🔚	🔚	🔚	—	🔚	—	END arrow
1365	U+1F51B	🔛	🔛	🔛	🔛	🔛	🔛	🔛	🔛	🔛	—	🔛	—	ON! arrow
1366	U+1F51C	🔜	🔜	🔜	🔜	🔜	🔜	🔜	🔜	🔜	—	🔜	—	SOON arrow
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1367	U+1F51D	🔝	🔝	🔝	🔝	🔝	🔝	🔝	🔝	🔝	🔝	—	—	TOP arrow
religion
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1368	U+1F6D0	🛐	🛐	🛐	🛐	🛐	🛐	🛐	🛐	—	—	—	—	place of worship
1369	U+269B	⚛	⚛	⚛	⚛	⚛	⚛	⚛	⚛	—	—	—	—	atom symbol
1370	U+1F549	🕉	🕉	🕉	🕉	🕉	🕉	🕉	🕉	—	—	—	—	om
1371	U+2721	✡	✡	✡	✡	✡	✡	✡	✡	—	—	—	—	star of David
1372	U+2638	☸	☸	☸	☸	☸	☸	☸	☸	—	—	—	—	wheel of dharma
1373	U+262F	☯	☯	☯	☯	☯	☯	☯	☯	—	—	—	—	yin yang
1374	U+271D	✝	✝	✝	✝	✝	✝	✝	✝	—	—	—	—	latin cross
1375	U+2626	☦	☦	☦	☦	☦	☦	☦	☦	—	—	—	—	orthodox cross
1376	U+262A	☪	☪	☪	☪	☪	☪	☪	☪	—	—	—	—	star and crescent
1377	U+262E	☮	☮	☮	☮	☮	☮	☮	☮	—	—	—	—	peace symbol
1378	U+1F54E	🕎	🕎	🕎	🕎	🕎	🕎	🕎	🕎	—	—	—	—	menorah
1379	U+1F52F	🔯	🔯	🔯	🔯	🔯	🔯	🔯	🔯	🔯	🔯	—	—	dotted six-pointed star
zodiac
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1380	U+2648	♈	♈	♈	♈	♈	♈	♈	♈	♈	♈	♈	♈	Aries
1381	U+2649	♉	♉	♉	♉	♉	♉	♉	♉	♉	♉	♉	♉	Taurus
1382	U+264A	♊	♊	♊	♊	♊	♊	♊	♊	♊	♊	♊	♊	Gemini
1383	U+264B	♋	♋	♋	♋	♋	♋	♋	♋	♋	♋	♋	♋	Cancer
1384	U+264C	♌	♌	♌	♌	♌	♌	♌	♌	♌	♌	♌	♌	Leo
1385	U+264D	♍	♍	♍	♍	♍	♍	♍	♍	♍	♍	♍	♍	Virgo
1386	U+264E	♎	♎	♎	♎	♎	♎	♎	♎	♎	♎	♎	♎	Libra
1387	U+264F	♏	♏	♏	♏	♏	♏	♏	♏	♏	♏	♏	♏	Scorpio
1388	U+2650	♐	♐	♐	♐	♐	♐	♐	♐	♐	♐	♐	♐	Sagittarius
1389	U+2651	♑	♑	♑	♑	♑	♑	♑	♑	♑	♑	♑	♑	Capricorn
1390	U+2652	♒	♒	♒	♒	♒	♒	♒	♒	♒	♒	♒	♒	Aquarius
1391	U+2653	♓	♓	♓	♓	♓	♓	♓	♓	♓	♓	♓	♓	Pisces
1392	U+26CE	⛎	⛎	⛎	⛎	⛎	⛎	⛎	⛎	⛎	⛎	—	⛎	Ophiuchus
av-symbol
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1393	U+1F500	🔀	🔀	🔀	🔀	🔀	🔀	🔀	🔀	—	—	—	—	shuffle tracks button
1394	U+1F501	🔁	🔁	🔁	🔁	🔁	🔁	🔁	🔁	—	—	—	—	repeat button
1395	U+1F502	🔂	🔂	🔂	🔂	🔂	🔂	🔂	🔂	—	—	—	—	repeat single button
1396	U+25B6	▶	▶	▶	▶	▶	▶	▶	▶	▶	▶	—	▶	play button
1397	U+23E9	⏩	⏩	⏩	⏩	⏩	⏩	⏩	⏩	⏩	⏩	—	⏩	fast-forward button
1398	U+23ED	⏭	⏭	⏭	⏭	⏭	⏭	⏭	⏭	—	—	—	—	next track button
1399	U+23EF	⏯	⏯	⏯	⏯	⏯	⏯	⏯	⏯	—	—	—	—	play or pause button
1400	U+25C0	◀	◀	◀	◀	◀	◀	◀	◀	◀	◀	—	◀	reverse button
1401	U+23EA	⏪	⏪	⏪	⏪	⏪	⏪	⏪	⏪	⏪	⏪	—	⏪	fast reverse button
1402	U+23EE	⏮	⏮	⏮	⏮	⏮	⏮	⏮	⏮	—	—	—	—	last track button
1403	U+1F53C	🔼	🔼	🔼	🔼	🔼	🔼	🔼	🔼	🔼	—	—	🔼	upwards button
1404	U+23EB	⏫	⏫	⏫	⏫	⏫	⏫	⏫	⏫	⏫	—	—	⏫	fast up button
1405	U+1F53D	🔽	🔽	🔽	🔽	🔽	🔽	🔽	🔽	🔽	—	—	🔽	downwards button
1406	U+23EC	⏬	⏬	⏬	⏬	⏬	⏬	⏬	⏬	⏬	—	—	⏬	fast down button
1407	U+23F8	⏸	⏸	⏸	⏸	⏸	⏸	⏸	⏸	—	—	—	—	pause button
1408	U+23F9	⏹	⏹	⏹	⏹	⏹	⏹	⏹	⏹	—	—	—	—	stop button
1409	U+23FA	⏺	⏺	⏺	⏺	⏺	⏺	⏺	⏺	—	—	—	—	record button
1410	U+23CF	⏏	⏏	⏏	⏏	⏏	⏏	⏏	⏏	—	—	—	—	eject button
1411	U+1F3A6	🎦	🎦	🎦	🎦	🎦	🎦	🎦	🎦	🎦	🎦	—	—	cinema
1412	U+1F505	🔅	🔅	🔅	🔅	🔅	🔅	🔅	🔅	—	—	—	—	dim button
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1413	U+1F506	🔆	🔆	🔆	🔆	🔆	🔆	🔆	🔆	—	—	—	—	bright button
1414	U+1F4F6	📶	📶	📶	📶	📶	📶	📶	📶	📶	📶	—	📶	antenna bars
1415	U+1F4F3	📳	📳	📳	📳	📳	📳	📳	📳	📳	📳	—	📳	vibration mode
1416	U+1F4F4	📴	📴	📴	📴	📴	📴	📴	📴	📴	📴	—	📴	mobile phone off
gender
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1417	U+2640	♀	—	♀	♀	♀	♀	♀	♀	—	—	—	—	female sign
1418	U+2642	♂	—	♂	♂	♂	♂	♂	♂	—	—	—	—	male sign
1419	U+26A7	⚧	—	—	—	—	⚧	⚧	—	—	—	—	—	⊛ transgender symbol
math
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1420	U+2716	✖	✖	✖	✖	✖	✖	✖	✖	—	—	—	✖	multiply
1421	U+2795	➕	➕	➕	➕	➕	➕	➕	➕	➕	—	—	➕	plus
1422	U+2796	➖	➖	➖	➖	➖	➖	➖	➖	➖	—	—	➖	minus
1423	U+2797	➗	➗	➗	➗	➗	➗	➗	➗	➗	—	—	➗	divide
1424	U+267E	♾	♾	♾	♾	♾	♾	♾	♾	—	—	—	—	infinity
punctuation
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1425	U+203C	‼	‼	‼	‼	‼	‼	‼	‼	‼	—	‼	‼	double exclamation mark
1426	U+2049	⁉	⁉	⁉	⁉	⁉	⁉	⁉	⁉	⁉	—	⁉	⁉	exclamation question mark
1427	U+2753	❓	❓	❓	❓	❓	❓	❓	❓	❓	❓	—	❓	question mark
1428	U+2754	❔	❔	❔	❔	❔	❔	❔	❔	❔	❔	—	—	white question mark
1429	U+2755	❕	❕	❕	❕	❕	❕	❕	❕	❕	❕	—	—	white exclamation mark
1430	U+2757	❗	❗	❗	❗	❗	❗	❗	❗	❗	❗	❗	❗	exclamation mark
1431	U+3030	〰	〰	〰	〰	〰	〰	〰	〰	〰	—	〰	—	wavy dash
currency
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1432	U+1F4B1	💱	💱	💱	💱	💱	💱	💱	💱	💱	💱	—	—	currency exchange
1433	U+1F4B2	💲	💲	💲	💲	💲	💲	💲	💲	💲	—	—	💲	heavy dollar sign
other-symbol
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1434	U+2695	⚕	—	⚕	⚕	⚕	⚕	⚕	⚕	—	—	—	—	medical symbol
1435	U+267B	♻	♻	♻	♻	♻	♻	♻	♻	♻	—	♻	♻	recycling symbol
1436	U+269C	⚜	⚜	⚜	⚜	⚜	⚜	⚜	⚜	—	—	—	—	fleur-de-lis
1437	U+1F531	🔱	🔱	🔱	🔱	🔱	🔱	🔱	🔱	🔱	🔱	—	—	trident emblem
1438	U+1F4DB	📛	📛	📛	📛	📛	📛	📛	📛	📛	—	—	📛	name badge
1439	U+1F530	🔰	🔰	🔰	🔰	🔰	🔰	🔰	🔰	🔰	🔰	—	🔰	Japanese symbol for beginner
1440	U+2B55	⭕	⭕	⭕	⭕	⭕	⭕	⭕	⭕	⭕	⭕	—	⭕	hollow red circle
1441	U+2705	✅	✅	✅	✅	✅	✅	✅	✅	✅	—	—	✅	check mark button
1442	U+2611	☑	☑	☑	☑	☑	☑	☑	☑	☑	—	—	☑	check box with check
1443	U+2714	✔	✔	✔	✔	✔	✔	✔	✔	—	—	—	✔	check mark
1444	U+274C	❌	❌	❌	❌	❌	❌	❌	❌	❌	❌	—	❌	cross mark
1445	U+274E	❎	❎	❎	❎	❎	❎	❎	❎	❎	—	—	❎	cross mark button
1446	U+27B0	➰	➰	➰	➰	➰	➰	➰	➰	➰	—	➰	➰	curly loop
1447	U+27BF	➿	➿	➿	➿	➿	➿	➿	➿	➿	—	—	—	double curly loop
1448	U+303D	〽	〽	〽	〽	〽	〽	〽	〽	〽	〽	—	—	part alternation mark
1449	U+2733	✳	✳	✳	✳	✳	✳	✳	✳	✳	✳	—	✳	eight-spoked asterisk
1450	U+2734	✴	✴	✴	✴	✴	✴	✴	✴	—	✴	—	✴	eight-pointed star
1451	U+2747	❇	❇	❇	❇	❇	❇	❇	❇	❇	—	—	❇	sparkle
1452	U+00A9	©	©	©	©	©	©	©	©	©	©	©	©	copyright
1453	U+00AE	®	®	®	®	®	®	®	®	®	®	®	®	registered
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1454	U+2122	™	™	™	™	™	™	™	™	™	™	™	™	trade mark
keycap
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1455	U+0023 U+FE0F U+20E3	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	#️⃣	keycap: #
1456	U+002A U+FE0F U+20E3	*️⃣	*️⃣	*️⃣	*️⃣	*️⃣	*️⃣	*️⃣	*️⃣	—	—	—	—	keycap: *
1457	U+0030 U+FE0F U+20E3	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	0️⃣	keycap: 0
1458	U+0031 U+FE0F U+20E3	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	1️⃣	keycap: 1
1459	U+0032 U+FE0F U+20E3	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	2️⃣	keycap: 2
1460	U+0033 U+FE0F U+20E3	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	3️⃣	keycap: 3
1461	U+0034 U+FE0F U+20E3	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	4️⃣	keycap: 4
1462	U+0035 U+FE0F U+20E3	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	5️⃣	keycap: 5
1463	U+0036 U+FE0F U+20E3	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	6️⃣	keycap: 6
1464	U+0037 U+FE0F U+20E3	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	7️⃣	keycap: 7
1465	U+0038 U+FE0F U+20E3	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	8️⃣	keycap: 8
1466	U+0039 U+FE0F U+20E3	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	9️⃣	keycap: 9
1467	U+1F51F	🔟	🔟	🔟	🔟	🔟	🔟	🔟	🔟	🔟	—	—	🔟	keycap: 10
alphanum
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1468	U+1F520	🔠	🔠	🔠	🔠	🔠	🔠	🔠	🔠	🔠	—	—	🔠	input latin uppercase
1469	U+1F521	🔡	🔡	🔡	🔡	🔡	🔡	🔡	🔡	🔡	—	—	🔡	input latin lowercase
1470	U+1F522	🔢	🔢	🔢	🔢	🔢	🔢	🔢	🔢	🔢	—	—	🔢	input numbers
1471	U+1F523	🔣	🔣	🔣	🔣	🔣	🔣	🔣	🔣	🔣	—	—	🔣	input symbols
1472	U+1F524	🔤	🔤	🔤	🔤	🔤	🔤	🔤	🔤	🔤	—	—	🔤	input latin letters
1473	U+1F170	🅰	🅰	🅰	🅰	🅰	🅰	🅰	🅰	🅰	🅰	—	🅰	A button (blood type)
1474	U+1F18E	🆎	🆎	🆎	🆎	🆎	🆎	🆎	🆎	🆎	🆎	—	🆎	AB button (blood type)
1475	U+1F171	🅱	🅱	🅱	🅱	🅱	🅱	🅱	🅱	🅱	🅱	—	🅱	B button (blood type)
1476	U+1F191	🆑	🆑	🆑	🆑	🆑	🆑	🆑	🆑	🆑	—	🆑	🆑	CL button
1477	U+1F192	🆒	🆒	🆒	🆒	🆒	🆒	🆒	🆒	🆒	🆒	—	🆒	COOL button
1478	U+1F193	🆓	🆓	🆓	🆓	🆓	🆓	🆓	🆓	🆓	—	🆓	🆓	FREE button
1479	U+2139	ℹ	ℹ	ℹ	ℹ	ℹ	ℹ	ℹ	ℹ	ℹ	—	—	ℹ	information
1480	U+1F194	🆔	🆔	🆔	🆔	🆔	🆔	🆔	🆔	🆔	🆔	🆔	🆔	ID button
1481	U+24C2	Ⓜ	Ⓜ	Ⓜ	Ⓜ	Ⓜ	Ⓜ	Ⓜ	Ⓜ	Ⓜ	—	Ⓜ	—	circled M
1482	U+1F195	🆕	🆕	🆕	🆕	🆕	🆕	🆕	🆕	🆕	🆕	🆕	🆕	NEW button
1483	U+1F196	🆖	🆖	🆖	🆖	🆖	🆖	🆖	🆖	🆖	—	🆖	—	NG button
1484	U+1F17E	🅾	🅾	🅾	🅾	🅾	🅾	🅾	🅾	🅾	🅾	—	🅾	O button (blood type)
1485	U+1F197	🆗	🆗	🆗	🆗	🆗	🆗	🆗	🆗	🆗	🆗	🆗	🆗	OK button
1486	U+1F17F	🅿	🅿	🅿	🅿	🅿	🅿	🅿	🅿	🅿	🅿	🅿	🅿	P button
1487	U+1F198	🆘	🆘	🆘	🆘	🆘	🆘	🆘	🆘	🆘	—	—	🆘	SOS button
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1488	U+1F199	🆙	🆙	🆙	🆙	🆙	🆙	🆙	🆙	🆙	🆙	—	🆙	UP! button
1489	U+1F19A	🆚	🆚	🆚	🆚	🆚	🆚	🆚	🆚	🆚	🆚	—	🆚	VS button
1490	U+1F201	🈁	🈁	🈁	🈁	🈁	🈁	🈁	🈁	🈁	🈁	—	—	Japanese “here” button
1491	U+1F202	🈂	🈂	🈂	🈂	🈂	🈂	🈂	🈂	🈂	🈂	—	🈂	Japanese “service charge” button
1492	U+1F237	🈷	🈷	🈷	🈷	🈷	🈷	🈷	🈷	🈷	🈷	—	—	Japanese “monthly amount” button
1493	U+1F236	🈶	🈶	🈶	🈶	🈶	🈶	🈶	🈶	🈶	🈶	—	—	Japanese “not free of charge” button
1494	U+1F22F	🈯	🈯	🈯	🈯	🈯	🈯	🈯	🈯	🈯	🈯	—	🈯	Japanese “reserved” button
1495	U+1F250	🉐	🉐	🉐	🉐	🉐	🉐	🉐	🉐	🉐	🉐	—	🉐	Japanese “bargain” button
1496	U+1F239	🈹	🈹	🈹	🈹	🈹	🈹	🈹	🈹	🈹	🈹	—	🈹	Japanese “discount” button
1497	U+1F21A	🈚	🈚	🈚	🈚	🈚	🈚	🈚	🈚	🈚	🈚	—	—	Japanese “free of charge” button
1498	U+1F232	🈲	🈲	🈲	🈲	🈲	🈲	🈲	🈲	🈲	—	🈲	—	Japanese “prohibited” button
1499	U+1F251	🉑	🉑	🉑	🉑	🉑	🉑	🉑	🉑	🉑	—	—	🉑	Japanese “acceptable” button
1500	U+1F238	🈸	🈸	🈸	🈸	🈸	🈸	🈸	🈸	🈸	🈸	—	—	Japanese “application” button
1501	U+1F234	🈴	🈴	🈴	🈴	🈴	🈴	🈴	🈴	🈴	—	🈴	—	Japanese “passing grade” button
1502	U+1F233	🈳	🈳	🈳	🈳	🈳	🈳	🈳	🈳	🈳	🈳	🈳	🈳	Japanese “vacancy” button
1503	U+3297	㊗	㊗	㊗	㊗	㊗	㊗	㊗	㊗	㊗	㊗	—	㊗	Japanese “congratulations” button
1504	U+3299	㊙	㊙	㊙	㊙	㊙	㊙	㊙	㊙	㊙	㊙	㊙	㊙	Japanese “secret” button
1505	U+1F23A	🈺	🈺	🈺	🈺	🈺	🈺	🈺	🈺	🈺	🈺	—	🈺	Japanese “open for business” button
1506	U+1F235	🈵	🈵	🈵	🈵	🈵	🈵	🈵	🈵	🈵	🈵	🈵	🈵	Japanese “no vacancy” button
geometric
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1507	U+1F534	🔴	🔴	🔴	🔴	🔴	🔴	🔴	🔴	🔴	🔴	—	🔴	red circle
1508	U+1F7E0	🟠	🟠	🟠	🟠	🟠	🟠	🟠	🟠	—	—	—	—	orange circle
1509	U+1F7E1	🟡	🟡	🟡	🟡	🟡	🟡	🟡	🟡	—	—	—	—	yellow circle
1510	U+1F7E2	🟢	🟢	🟢	🟢	🟢	🟢	🟢	🟢	—	—	—	—	green circle
1511	U+1F535	🔵	🔵	🔵	🔵	🔵	🔵	🔵	🔵	🔵	—	—	🔵	blue circle
1512	U+1F7E3	🟣	🟣	🟣	🟣	🟣	🟣	🟣	🟣	—	—	—	—	purple circle
1513	U+1F7E4	🟤	🟤	🟤	🟤	🟤	🟤	🟤	🟤	—	—	—	—	brown circle
1514	U+26AB	⚫	⚫	⚫	⚫	⚫	⚫	⚫	⚫	⚫	—	—	⚫	black circle
1515	U+26AA	⚪	⚪	⚪	⚪	⚪	⚪	⚪	⚪	⚪	—	—	⚪	white circle
1516	U+1F7E5	🟥	🟥	🟥	🟥	🟥	🟥	🟥	🟥	—	—	—	—	red square
1517	U+1F7E7	🟧	🟧	🟧	🟧	🟧	🟧	🟧	🟧	—	—	—	—	orange square
1518	U+1F7E8	🟨	🟨	🟨	🟨	🟨	🟨	🟨	🟨	—	—	—	—	yellow square
1519	U+1F7E9	🟩	🟩	🟩	🟩	🟩	🟩	🟩	🟩	—	—	—	—	green square
1520	U+1F7E6	🟦	🟦	🟦	🟦	🟦	🟦	🟦	🟦	—	—	—	—	blue square
1521	U+1F7EA	🟪	🟪	🟪	🟪	🟪	🟪	🟪	🟪	—	—	—	—	purple square
1522	U+1F7EB	🟫	🟫	🟫	🟫	🟫	🟫	🟫	🟫	—	—	—	—	brown square
1523	U+2B1B	⬛	⬛	⬛	⬛	⬛	⬛	⬛	⬛	—	—	—	⬛	black large square
1524	U+2B1C	⬜	⬜	⬜	⬜	⬜	⬜	⬜	⬜	—	—	—	⬜	white large square
1525	U+25FC	◼	◼	◼	◼	◼	◼	◼	◼	◼	—	—	◼	black medium square
1526	U+25FB	◻	◻	◻	◻	◻	◻	◻	◻	◻	—	—	◻	white medium square
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1527	U+25FE	◾	◾	◾	◾	◾	◾	◾	◾	◾	—	—	◾	black medium-small square
1528	U+25FD	◽	◽	◽	◽	◽	◽	◽	◽	◽	—	—	◽	white medium-small square
1529	U+25AA	▪	▪	▪	▪	▪	▪	▪	▪	▪	—	—	▪	black small square
1530	U+25AB	▫	▫	▫	▫	▫	▫	▫	▫	▫	—	—	▫	white small square
1531	U+1F536	🔶	🔶	🔶	🔶	🔶	🔶	🔶	🔶	🔶	—	—	🔶	large orange diamond
1532	U+1F537	🔷	🔷	🔷	🔷	🔷	🔷	🔷	🔷	🔷	—	—	🔷	large blue diamond
1533	U+1F538	🔸	🔸	🔸	🔸	🔸	🔸	🔸	🔸	🔸	—	—	🔸	small orange diamond
1534	U+1F539	🔹	🔹	🔹	🔹	🔹	🔹	🔹	🔹	🔹	—	—	🔹	small blue diamond
1535	U+1F53A	🔺	🔺	🔺	🔺	🔺	🔺	🔺	🔺	🔺	—	—	🔺	red triangle pointed up
1536	U+1F53B	🔻	🔻	🔻	🔻	🔻	🔻	🔻	🔻	🔻	—	—	🔻	red triangle pointed down
1537	U+1F4A0	💠	💠	💠	💠	💠	💠	💠	💠	💠	—	💠	—	diamond with a dot
1538	U+1F518	🔘	🔘	🔘	🔘	🔘	🔘	🔘	🔘	🔘	—	—	🔘	radio button
1539	U+1F533	🔳	🔳	🔳	🔳	🔳	🔳	🔳	🔳	🔳	🔳	—	—	white square button
1540	U+1F532	🔲	🔲	🔲	🔲	🔲	🔲	🔲	🔲	—	🔲	—	—	black square button
Flags
flag
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1541	U+1F3C1	🏁	🏁	🏁	🏁	🏁	🏁	🏁	🏁	🏁	🏁	🏁	🏁	chequered flag
1542	U+1F6A9	🚩	🚩	🚩	🚩	🚩	🚩	🚩	🚩	🚩	—	🚩	🚩	triangular flag
1543	U+1F38C	🎌	🎌	🎌	🎌	🎌	🎌	🎌	—	🎌	🎌	—	🎌	crossed flags
1544	U+1F3F4	🏴	🏴	🏴	🏴	🏴	🏴	🏴	🏴	—	—	—	—	black flag
1545	U+1F3F3	🏳	🏳	🏳	🏳	🏳	🏳	🏳	🏳	—	—	—	—	white flag
1546	U+1F3F3 U+FE0F U+200D U+1F308	🏳️‍🌈	🏳️‍🌈	🏳️‍🌈	🏳️‍🌈	🏳️‍🌈	🏳️‍🌈	🏳️‍🌈	🏳️‍🌈	—	—	—	—	rainbow flag
1547	U+1F3F3 U+FE0F U+200D U+26A7 U+FE0F	🏳️‍⚧️	—	🏳️‍⚧️	🏳️‍⚧️	—	🏳️‍⚧️	🏳️‍⚧️	—	—	—	—	—	⊛ transgender flag
1548	U+1F3F4 U+200D U+2620 U+FE0F	🏴‍☠️	🏴‍☠️	🏴‍☠️	🏴‍☠️	🏴‍☠️	🏴‍☠️	🏴‍☠️	🏴‍☠️	—	—	—	—	pirate flag
country-flag
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1549	U+1F1E6 U+1F1E8	🇦🇨	🇦🇨	🇦🇨	🇦🇨	—	🇦🇨	🇦🇨	🇦🇨	—	—	—	—	flag: Ascension Island
1550	U+1F1E6 U+1F1E9	🇦🇩	🇦🇩	🇦🇩	🇦🇩	—	🇦🇩	🇦🇩	🇦🇩	—	—	—	—	flag: Andorra
1551	U+1F1E6 U+1F1EA	🇦🇪	🇦🇪	🇦🇪	🇦🇪	—	🇦🇪	🇦🇪	🇦🇪	—	—	—	—	flag: United Arab Emirates
1552	U+1F1E6 U+1F1EB	🇦🇫	🇦🇫	🇦🇫	🇦🇫	—	🇦🇫	🇦🇫	🇦🇫	—	—	—	—	flag: Afghanistan
1553	U+1F1E6 U+1F1EC	🇦🇬	🇦🇬	🇦🇬	🇦🇬	—	🇦🇬	🇦🇬	🇦🇬	—	—	—	—	flag: Antigua & Barbuda
1554	U+1F1E6 U+1F1EE	🇦🇮	🇦🇮	🇦🇮	🇦🇮	—	🇦🇮	🇦🇮	🇦🇮	—	—	—	—	flag: Anguilla
1555	U+1F1E6 U+1F1F1	🇦🇱	🇦🇱	🇦🇱	🇦🇱	—	🇦🇱	🇦🇱	🇦🇱	—	—	—	—	flag: Albania
1556	U+1F1E6 U+1F1F2	🇦🇲	🇦🇲	🇦🇲	🇦🇲	—	🇦🇲	🇦🇲	🇦🇲	—	—	—	—	flag: Armenia
1557	U+1F1E6 U+1F1F4	🇦🇴	🇦🇴	🇦🇴	🇦🇴	—	🇦🇴	🇦🇴	🇦🇴	—	—	—	—	flag: Angola
1558	U+1F1E6 U+1F1F6	🇦🇶	🇦🇶	🇦🇶	🇦🇶	—	🇦🇶	🇦🇶	🇦🇶	—	—	—	—	flag: Antarctica
1559	U+1F1E6 U+1F1F7	🇦🇷	🇦🇷	🇦🇷	🇦🇷	—	🇦🇷	🇦🇷	🇦🇷	—	—	—	—	flag: Argentina
1560	U+1F1E6 U+1F1F8	🇦🇸	🇦🇸	🇦🇸	🇦🇸	—	🇦🇸	🇦🇸	🇦🇸	—	—	—	—	flag: American Samoa
1561	U+1F1E6 U+1F1F9	🇦🇹	🇦🇹	🇦🇹	🇦🇹	—	🇦🇹	🇦🇹	🇦🇹	—	—	—	—	flag: Austria
1562	U+1F1E6 U+1F1FA	🇦🇺	🇦🇺	🇦🇺	🇦🇺	—	🇦🇺	🇦🇺	🇦🇺	—	—	—	—	flag: Australia
1563	U+1F1E6 U+1F1FC	🇦🇼	🇦🇼	🇦🇼	🇦🇼	—	🇦🇼	🇦🇼	🇦🇼	—	—	—	—	flag: Aruba
1564	U+1F1E6 U+1F1FD	🇦🇽	🇦🇽	🇦🇽	🇦🇽	—	🇦🇽	🇦🇽	🇦🇽	—	—	—	—	flag: Åland Islands
1565	U+1F1E6 U+1F1FF	🇦🇿	🇦🇿	🇦🇿	🇦🇿	—	🇦🇿	🇦🇿	🇦🇿	—	—	—	—	flag: Azerbaijan
1566	U+1F1E7 U+1F1E6	🇧🇦	🇧🇦	🇧🇦	🇧🇦	—	🇧🇦	🇧🇦	🇧🇦	—	—	—	—	flag: Bosnia & Herzegovina
1567	U+1F1E7 U+1F1E7	🇧🇧	🇧🇧	🇧🇧	🇧🇧	—	🇧🇧	🇧🇧	🇧🇧	—	—	—	—	flag: Barbados
1568	U+1F1E7 U+1F1E9	🇧🇩	🇧🇩	🇧🇩	🇧🇩	—	🇧🇩	🇧🇩	🇧🇩	—	—	—	—	flag: Bangladesh
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1569	U+1F1E7 U+1F1EA	🇧🇪	🇧🇪	🇧🇪	🇧🇪	—	🇧🇪	🇧🇪	🇧🇪	—	—	—	—	flag: Belgium
1570	U+1F1E7 U+1F1EB	🇧🇫	🇧🇫	🇧🇫	🇧🇫	—	🇧🇫	🇧🇫	🇧🇫	—	—	—	—	flag: Burkina Faso
1571	U+1F1E7 U+1F1EC	🇧🇬	🇧🇬	🇧🇬	🇧🇬	—	🇧🇬	🇧🇬	🇧🇬	—	—	—	—	flag: Bulgaria
1572	U+1F1E7 U+1F1ED	🇧🇭	🇧🇭	🇧🇭	🇧🇭	—	🇧🇭	🇧🇭	🇧🇭	—	—	—	—	flag: Bahrain
1573	U+1F1E7 U+1F1EE	🇧🇮	🇧🇮	🇧🇮	🇧🇮	—	🇧🇮	🇧🇮	🇧🇮	—	—	—	—	flag: Burundi
1574	U+1F1E7 U+1F1EF	🇧🇯	🇧🇯	🇧🇯	🇧🇯	—	🇧🇯	🇧🇯	🇧🇯	—	—	—	—	flag: Benin
1575	U+1F1E7 U+1F1F1	🇧🇱	🇧🇱	🇧🇱	🇧🇱	—	🇧🇱	🇧🇱	🇧🇱	—	—	—	—	flag: St. Barthélemy
1576	U+1F1E7 U+1F1F2	🇧🇲	🇧🇲	🇧🇲	🇧🇲	—	🇧🇲	🇧🇲	🇧🇲	—	—	—	—	flag: Bermuda
1577	U+1F1E7 U+1F1F3	🇧🇳	🇧🇳	🇧🇳	🇧🇳	—	🇧🇳	🇧🇳	🇧🇳	—	—	—	—	flag: Brunei
1578	U+1F1E7 U+1F1F4	🇧🇴	🇧🇴	🇧🇴	🇧🇴	—	🇧🇴	🇧🇴	🇧🇴	—	—	—	—	flag: Bolivia
1579	U+1F1E7 U+1F1F6	🇧🇶	🇧🇶	🇧🇶	🇧🇶	—	🇧🇶	🇧🇶	🇧🇶	—	—	—	—	flag: Caribbean Netherlands
1580	U+1F1E7 U+1F1F7	🇧🇷	🇧🇷	🇧🇷	🇧🇷	—	🇧🇷	🇧🇷	🇧🇷	—	—	—	—	flag: Brazil
1581	U+1F1E7 U+1F1F8	🇧🇸	🇧🇸	🇧🇸	🇧🇸	—	🇧🇸	🇧🇸	🇧🇸	—	—	—	—	flag: Bahamas
1582	U+1F1E7 U+1F1F9	🇧🇹	🇧🇹	🇧🇹	🇧🇹	—	🇧🇹	🇧🇹	🇧🇹	—	—	—	—	flag: Bhutan
1583	U+1F1E7 U+1F1FB	🇧🇻	🇧🇻	🇧🇻	🇧🇻	—	🇧🇻	🇧🇻	🇧🇻	—	—	—	—	flag: Bouvet Island
1584	U+1F1E7 U+1F1FC	🇧🇼	🇧🇼	🇧🇼	🇧🇼	—	🇧🇼	🇧🇼	🇧🇼	—	—	—	—	flag: Botswana
1585	U+1F1E7 U+1F1FE	🇧🇾	🇧🇾	🇧🇾	🇧🇾	—	🇧🇾	🇧🇾	🇧🇾	—	—	—	—	flag: Belarus
1586	U+1F1E7 U+1F1FF	🇧🇿	🇧🇿	🇧🇿	🇧🇿	—	🇧🇿	🇧🇿	🇧🇿	—	—	—	—	flag: Belize
1587	U+1F1E8 U+1F1E6	🇨🇦	🇨🇦	🇨🇦	🇨🇦	—	🇨🇦	🇨🇦	🇨🇦	—	—	—	—	flag: Canada
1588	U+1F1E8 U+1F1E8	🇨🇨	🇨🇨	🇨🇨	🇨🇨	—	🇨🇨	🇨🇨	🇨🇨	—	—	—	—	flag: Cocos (Keeling) Islands
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1589	U+1F1E8 U+1F1E9	🇨🇩	🇨🇩	🇨🇩	🇨🇩	—	🇨🇩	🇨🇩	🇨🇩	—	—	—	—	flag: Congo - Kinshasa
1590	U+1F1E8 U+1F1EB	🇨🇫	🇨🇫	🇨🇫	🇨🇫	—	🇨🇫	🇨🇫	🇨🇫	—	—	—	—	flag: Central African Republic
1591	U+1F1E8 U+1F1EC	🇨🇬	🇨🇬	🇨🇬	🇨🇬	—	🇨🇬	🇨🇬	🇨🇬	—	—	—	—	flag: Congo - Brazzaville
1592	U+1F1E8 U+1F1ED	🇨🇭	🇨🇭	🇨🇭	🇨🇭	—	🇨🇭	🇨🇭	🇨🇭	—	—	—	—	flag: Switzerland
1593	U+1F1E8 U+1F1EE	🇨🇮	🇨🇮	🇨🇮	🇨🇮	—	🇨🇮	🇨🇮	🇨🇮	—	—	—	—	flag: Côte d’Ivoire
1594	U+1F1E8 U+1F1F0	🇨🇰	🇨🇰	🇨🇰	🇨🇰	—	🇨🇰	🇨🇰	🇨🇰	—	—	—	—	flag: Cook Islands
1595	U+1F1E8 U+1F1F1	🇨🇱	🇨🇱	🇨🇱	🇨🇱	—	🇨🇱	🇨🇱	🇨🇱	—	—	—	—	flag: Chile
1596	U+1F1E8 U+1F1F2	🇨🇲	🇨🇲	🇨🇲	🇨🇲	—	🇨🇲	🇨🇲	🇨🇲	—	—	—	—	flag: Cameroon
1597	U+1F1E8 U+1F1F3	🇨🇳	🇨🇳	🇨🇳	🇨🇳	—	🇨🇳	🇨🇳	🇨🇳	🇨🇳	🇨🇳	—	🇨🇳	flag: China
1598	U+1F1E8 U+1F1F4	🇨🇴	🇨🇴	🇨🇴	🇨🇴	—	🇨🇴	🇨🇴	🇨🇴	—	—	—	—	flag: Colombia
1599	U+1F1E8 U+1F1F5	🇨🇵	🇨🇵	🇨🇵	🇨🇵	—	🇨🇵	🇨🇵	🇨🇵	—	—	—	—	flag: Clipperton Island
1600	U+1F1E8 U+1F1F7	🇨🇷	🇨🇷	🇨🇷	🇨🇷	—	🇨🇷	🇨🇷	🇨🇷	—	—	—	—	flag: Costa Rica
1601	U+1F1E8 U+1F1FA	🇨🇺	🇨🇺	🇨🇺	🇨🇺	—	🇨🇺	🇨🇺	🇨🇺	—	—	—	—	flag: Cuba
1602	U+1F1E8 U+1F1FB	🇨🇻	🇨🇻	🇨🇻	🇨🇻	—	🇨🇻	🇨🇻	🇨🇻	—	—	—	—	flag: Cape Verde
1603	U+1F1E8 U+1F1FC	🇨🇼	🇨🇼	🇨🇼	🇨🇼	—	🇨🇼	🇨🇼	🇨🇼	—	—	—	—	flag: Curaçao
1604	U+1F1E8 U+1F1FD	🇨🇽	🇨🇽	🇨🇽	🇨🇽	—	🇨🇽	🇨🇽	🇨🇽	—	—	—	—	flag: Christmas Island
1605	U+1F1E8 U+1F1FE	🇨🇾	🇨🇾	🇨🇾	🇨🇾	—	🇨🇾	🇨🇾	🇨🇾	—	—	—	—	flag: Cyprus
1606	U+1F1E8 U+1F1FF	🇨🇿	🇨🇿	🇨🇿	🇨🇿	—	🇨🇿	🇨🇿	🇨🇿	—	—	—	—	flag: Czechia
1607	U+1F1E9 U+1F1EA	🇩🇪	🇩🇪	🇩🇪	🇩🇪	—	🇩🇪	🇩🇪	🇩🇪	🇩🇪	🇩🇪	—	🇩🇪	flag: Germany
1608	U+1F1E9 U+1F1EC	🇩🇬	🇩🇬	🇩🇬	🇩🇬	—	🇩🇬	🇩🇬	🇩🇬	—	—	—	—	flag: Diego Garcia
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1609	U+1F1E9 U+1F1EF	🇩🇯	🇩🇯	🇩🇯	🇩🇯	—	🇩🇯	🇩🇯	🇩🇯	—	—	—	—	flag: Djibouti
1610	U+1F1E9 U+1F1F0	🇩🇰	🇩🇰	🇩🇰	🇩🇰	—	🇩🇰	🇩🇰	🇩🇰	—	—	—	—	flag: Denmark
1611	U+1F1E9 U+1F1F2	🇩🇲	🇩🇲	🇩🇲	🇩🇲	—	🇩🇲	🇩🇲	🇩🇲	—	—	—	—	flag: Dominica
1612	U+1F1E9 U+1F1F4	🇩🇴	🇩🇴	🇩🇴	🇩🇴	—	🇩🇴	🇩🇴	🇩🇴	—	—	—	—	flag: Dominican Republic
1613	U+1F1E9 U+1F1FF	🇩🇿	🇩🇿	🇩🇿	🇩🇿	—	🇩🇿	🇩🇿	🇩🇿	—	—	—	—	flag: Algeria
1614	U+1F1EA U+1F1E6	🇪🇦	🇪🇦	🇪🇦	🇪🇦	—	🇪🇦	🇪🇦	🇪🇦	—	—	—	—	flag: Ceuta & Melilla
1615	U+1F1EA U+1F1E8	🇪🇨	🇪🇨	🇪🇨	🇪🇨	—	🇪🇨	🇪🇨	🇪🇨	—	—	—	—	flag: Ecuador
1616	U+1F1EA U+1F1EA	🇪🇪	🇪🇪	🇪🇪	🇪🇪	—	🇪🇪	🇪🇪	🇪🇪	—	—	—	—	flag: Estonia
1617	U+1F1EA U+1F1EC	🇪🇬	🇪🇬	🇪🇬	🇪🇬	—	🇪🇬	🇪🇬	🇪🇬	—	—	—	—	flag: Egypt
1618	U+1F1EA U+1F1ED	🇪🇭	🇪🇭	🇪🇭	🇪🇭	—	🇪🇭	🇪🇭	🇪🇭	—	—	—	—	flag: Western Sahara
1619	U+1F1EA U+1F1F7	🇪🇷	🇪🇷	🇪🇷	🇪🇷	—	🇪🇷	🇪🇷	🇪🇷	—	—	—	—	flag: Eritrea
1620	U+1F1EA U+1F1F8	🇪🇸	🇪🇸	🇪🇸	🇪🇸	—	🇪🇸	🇪🇸	🇪🇸	🇪🇸	🇪🇸	—	🇪🇸	flag: Spain
1621	U+1F1EA U+1F1F9	🇪🇹	🇪🇹	🇪🇹	🇪🇹	—	🇪🇹	🇪🇹	🇪🇹	—	—	—	—	flag: Ethiopia
1622	U+1F1EA U+1F1FA	🇪🇺	🇪🇺	🇪🇺	🇪🇺	—	🇪🇺	🇪🇺	🇪🇺	—	—	—	—	flag: European Union
1623	U+1F1EB U+1F1EE	🇫🇮	🇫🇮	🇫🇮	🇫🇮	—	🇫🇮	🇫🇮	🇫🇮	—	—	—	—	flag: Finland
1624	U+1F1EB U+1F1EF	🇫🇯	🇫🇯	🇫🇯	🇫🇯	—	🇫🇯	🇫🇯	🇫🇯	—	—	—	—	flag: Fiji
1625	U+1F1EB U+1F1F0	🇫🇰	🇫🇰	🇫🇰	🇫🇰	—	🇫🇰	🇫🇰	🇫🇰	—	—	—	—	flag: Falkland Islands
1626	U+1F1EB U+1F1F2	🇫🇲	🇫🇲	🇫🇲	🇫🇲	—	🇫🇲	🇫🇲	🇫🇲	—	—	—	—	flag: Micronesia
1627	U+1F1EB U+1F1F4	🇫🇴	🇫🇴	🇫🇴	🇫🇴	—	🇫🇴	🇫🇴	🇫🇴	—	—	—	—	flag: Faroe Islands
1628	U+1F1EB U+1F1F7	🇫🇷	🇫🇷	🇫🇷	🇫🇷	—	🇫🇷	🇫🇷	🇫🇷	🇫🇷	🇫🇷	—	🇫🇷	flag: France
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1629	U+1F1EC U+1F1E6	🇬🇦	🇬🇦	🇬🇦	🇬🇦	—	🇬🇦	🇬🇦	🇬🇦	—	—	—	—	flag: Gabon
1630	U+1F1EC U+1F1E7	🇬🇧	🇬🇧	🇬🇧	🇬🇧	—	🇬🇧	🇬🇧	🇬🇧	🇬🇧	🇬🇧	—	🇬🇧	flag: United Kingdom
1631	U+1F1EC U+1F1E9	🇬🇩	🇬🇩	🇬🇩	🇬🇩	—	🇬🇩	🇬🇩	🇬🇩	—	—	—	—	flag: Grenada
1632	U+1F1EC U+1F1EA	🇬🇪	🇬🇪	🇬🇪	🇬🇪	—	🇬🇪	🇬🇪	🇬🇪	—	—	—	—	flag: Georgia
1633	U+1F1EC U+1F1EB	🇬🇫	🇬🇫	🇬🇫	🇬🇫	—	🇬🇫	🇬🇫	🇬🇫	—	—	—	—	flag: French Guiana
1634	U+1F1EC U+1F1EC	🇬🇬	🇬🇬	🇬🇬	🇬🇬	—	🇬🇬	🇬🇬	🇬🇬	—	—	—	—	flag: Guernsey
1635	U+1F1EC U+1F1ED	🇬🇭	🇬🇭	🇬🇭	🇬🇭	—	🇬🇭	🇬🇭	🇬🇭	—	—	—	—	flag: Ghana
1636	U+1F1EC U+1F1EE	🇬🇮	🇬🇮	🇬🇮	🇬🇮	—	🇬🇮	🇬🇮	🇬🇮	—	—	—	—	flag: Gibraltar
1637	U+1F1EC U+1F1F1	🇬🇱	🇬🇱	🇬🇱	🇬🇱	—	🇬🇱	🇬🇱	🇬🇱	—	—	—	—	flag: Greenland
1638	U+1F1EC U+1F1F2	🇬🇲	🇬🇲	🇬🇲	🇬🇲	—	🇬🇲	🇬🇲	🇬🇲	—	—	—	—	flag: Gambia
1639	U+1F1EC U+1F1F3	🇬🇳	🇬🇳	🇬🇳	🇬🇳	—	🇬🇳	🇬🇳	🇬🇳	—	—	—	—	flag: Guinea
1640	U+1F1EC U+1F1F5	🇬🇵	🇬🇵	🇬🇵	🇬🇵	—	🇬🇵	🇬🇵	🇬🇵	—	—	—	—	flag: Guadeloupe
1641	U+1F1EC U+1F1F6	🇬🇶	🇬🇶	🇬🇶	🇬🇶	—	🇬🇶	🇬🇶	🇬🇶	—	—	—	—	flag: Equatorial Guinea
1642	U+1F1EC U+1F1F7	🇬🇷	🇬🇷	🇬🇷	🇬🇷	—	🇬🇷	🇬🇷	🇬🇷	—	—	—	—	flag: Greece
1643	U+1F1EC U+1F1F8	🇬🇸	🇬🇸	🇬🇸	🇬🇸	—	🇬🇸	🇬🇸	🇬🇸	—	—	—	—	flag: South Georgia & South Sandwich Islands
1644	U+1F1EC U+1F1F9	🇬🇹	🇬🇹	🇬🇹	🇬🇹	—	🇬🇹	🇬🇹	🇬🇹	—	—	—	—	flag: Guatemala
1645	U+1F1EC U+1F1FA	🇬🇺	🇬🇺	🇬🇺	🇬🇺	—	🇬🇺	🇬🇺	🇬🇺	—	—	—	—	flag: Guam
1646	U+1F1EC U+1F1FC	🇬🇼	🇬🇼	🇬🇼	🇬🇼	—	🇬🇼	🇬🇼	🇬🇼	—	—	—	—	flag: Guinea-Bissau
1647	U+1F1EC U+1F1FE	🇬🇾	🇬🇾	🇬🇾	🇬🇾	—	🇬🇾	🇬🇾	🇬🇾	—	—	—	—	flag: Guyana
1648	U+1F1ED U+1F1F0	🇭🇰	🇭🇰	🇭🇰	🇭🇰	—	🇭🇰	🇭🇰	🇭🇰	—	—	—	—	flag: Hong Kong SAR China
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1649	U+1F1ED U+1F1F2	🇭🇲	🇭🇲	🇭🇲	🇭🇲	—	🇭🇲	🇭🇲	🇭🇲	—	—	—	—	flag: Heard & McDonald Islands
1650	U+1F1ED U+1F1F3	🇭🇳	🇭🇳	🇭🇳	🇭🇳	—	🇭🇳	🇭🇳	🇭🇳	—	—	—	—	flag: Honduras
1651	U+1F1ED U+1F1F7	🇭🇷	🇭🇷	🇭🇷	🇭🇷	—	🇭🇷	🇭🇷	🇭🇷	—	—	—	—	flag: Croatia
1652	U+1F1ED U+1F1F9	🇭🇹	🇭🇹	🇭🇹	🇭🇹	—	🇭🇹	🇭🇹	🇭🇹	—	—	—	—	flag: Haiti
1653	U+1F1ED U+1F1FA	🇭🇺	🇭🇺	🇭🇺	🇭🇺	—	🇭🇺	🇭🇺	🇭🇺	—	—	—	—	flag: Hungary
1654	U+1F1EE U+1F1E8	🇮🇨	🇮🇨	🇮🇨	🇮🇨	—	🇮🇨	🇮🇨	🇮🇨	—	—	—	—	flag: Canary Islands
1655	U+1F1EE U+1F1E9	🇮🇩	🇮🇩	🇮🇩	🇮🇩	—	🇮🇩	🇮🇩	🇮🇩	—	—	—	—	flag: Indonesia
1656	U+1F1EE U+1F1EA	🇮🇪	🇮🇪	🇮🇪	🇮🇪	—	🇮🇪	🇮🇪	🇮🇪	—	—	—	—	flag: Ireland
1657	U+1F1EE U+1F1F1	🇮🇱	🇮🇱	🇮🇱	🇮🇱	—	🇮🇱	🇮🇱	🇮🇱	—	—	—	—	flag: Israel
1658	U+1F1EE U+1F1F2	🇮🇲	🇮🇲	🇮🇲	🇮🇲	—	🇮🇲	🇮🇲	🇮🇲	—	—	—	—	flag: Isle of Man
1659	U+1F1EE U+1F1F3	🇮🇳	🇮🇳	🇮🇳	🇮🇳	—	🇮🇳	🇮🇳	🇮🇳	—	—	—	—	flag: India
1660	U+1F1EE U+1F1F4	🇮🇴	🇮🇴	🇮🇴	🇮🇴	—	🇮🇴	🇮🇴	🇮🇴	—	—	—	—	flag: British Indian Ocean Territory
1661	U+1F1EE U+1F1F6	🇮🇶	🇮🇶	🇮🇶	🇮🇶	—	🇮🇶	🇮🇶	🇮🇶	—	—	—	—	flag: Iraq
1662	U+1F1EE U+1F1F7	🇮🇷	🇮🇷	🇮🇷	🇮🇷	—	🇮🇷	🇮🇷	🇮🇷	—	—	—	—	flag: Iran
1663	U+1F1EE U+1F1F8	🇮🇸	🇮🇸	🇮🇸	🇮🇸	—	🇮🇸	🇮🇸	🇮🇸	—	—	—	—	flag: Iceland
1664	U+1F1EE U+1F1F9	🇮🇹	🇮🇹	🇮🇹	🇮🇹	—	🇮🇹	🇮🇹	🇮🇹	🇮🇹	🇮🇹	—	🇮🇹	flag: Italy
1665	U+1F1EF U+1F1EA	🇯🇪	🇯🇪	🇯🇪	🇯🇪	—	🇯🇪	🇯🇪	🇯🇪	—	—	—	—	flag: Jersey
1666	U+1F1EF U+1F1F2	🇯🇲	🇯🇲	🇯🇲	🇯🇲	—	🇯🇲	🇯🇲	🇯🇲	—	—	—	—	flag: Jamaica
1667	U+1F1EF U+1F1F4	🇯🇴	🇯🇴	🇯🇴	🇯🇴	—	🇯🇴	🇯🇴	🇯🇴	—	—	—	—	flag: Jordan
1668	U+1F1EF U+1F1F5	🇯🇵	🇯🇵	🇯🇵	🇯🇵	—	🇯🇵	🇯🇵	🇯🇵	🇯🇵	🇯🇵	—	🇯🇵	flag: Japan
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1669	U+1F1F0 U+1F1EA	🇰🇪	🇰🇪	🇰🇪	🇰🇪	—	🇰🇪	🇰🇪	🇰🇪	—	—	—	—	flag: Kenya
1670	U+1F1F0 U+1F1EC	🇰🇬	🇰🇬	🇰🇬	🇰🇬	—	🇰🇬	🇰🇬	🇰🇬	—	—	—	—	flag: Kyrgyzstan
1671	U+1F1F0 U+1F1ED	🇰🇭	🇰🇭	🇰🇭	🇰🇭	—	🇰🇭	🇰🇭	🇰🇭	—	—	—	—	flag: Cambodia
1672	U+1F1F0 U+1F1EE	🇰🇮	🇰🇮	🇰🇮	🇰🇮	—	🇰🇮	🇰🇮	🇰🇮	—	—	—	—	flag: Kiribati
1673	U+1F1F0 U+1F1F2	🇰🇲	🇰🇲	🇰🇲	🇰🇲	—	🇰🇲	🇰🇲	🇰🇲	—	—	—	—	flag: Comoros
1674	U+1F1F0 U+1F1F3	🇰🇳	🇰🇳	🇰🇳	🇰🇳	—	🇰🇳	🇰🇳	🇰🇳	—	—	—	—	flag: St. Kitts & Nevis
1675	U+1F1F0 U+1F1F5	🇰🇵	🇰🇵	🇰🇵	🇰🇵	—	🇰🇵	🇰🇵	🇰🇵	—	—	—	—	flag: North Korea
1676	U+1F1F0 U+1F1F7	🇰🇷	🇰🇷	🇰🇷	🇰🇷	—	🇰🇷	🇰🇷	🇰🇷	🇰🇷	🇰🇷	—	🇰🇷	flag: South Korea
1677	U+1F1F0 U+1F1FC	🇰🇼	🇰🇼	🇰🇼	🇰🇼	—	🇰🇼	🇰🇼	🇰🇼	—	—	—	—	flag: Kuwait
1678	U+1F1F0 U+1F1FE	🇰🇾	🇰🇾	🇰🇾	🇰🇾	—	🇰🇾	🇰🇾	🇰🇾	—	—	—	—	flag: Cayman Islands
1679	U+1F1F0 U+1F1FF	🇰🇿	🇰🇿	🇰🇿	🇰🇿	—	🇰🇿	🇰🇿	🇰🇿	—	—	—	—	flag: Kazakhstan
1680	U+1F1F1 U+1F1E6	🇱🇦	🇱🇦	🇱🇦	🇱🇦	—	🇱🇦	🇱🇦	🇱🇦	—	—	—	—	flag: Laos
1681	U+1F1F1 U+1F1E7	🇱🇧	🇱🇧	🇱🇧	🇱🇧	—	🇱🇧	🇱🇧	🇱🇧	—	—	—	—	flag: Lebanon
1682	U+1F1F1 U+1F1E8	🇱🇨	🇱🇨	🇱🇨	🇱🇨	—	🇱🇨	🇱🇨	🇱🇨	—	—	—	—	flag: St. Lucia
1683	U+1F1F1 U+1F1EE	🇱🇮	🇱🇮	🇱🇮	🇱🇮	—	🇱🇮	🇱🇮	🇱🇮	—	—	—	—	flag: Liechtenstein
1684	U+1F1F1 U+1F1F0	🇱🇰	🇱🇰	🇱🇰	🇱🇰	—	🇱🇰	🇱🇰	🇱🇰	—	—	—	—	flag: Sri Lanka
1685	U+1F1F1 U+1F1F7	🇱🇷	🇱🇷	🇱🇷	🇱🇷	—	🇱🇷	🇱🇷	🇱🇷	—	—	—	—	flag: Liberia
1686	U+1F1F1 U+1F1F8	🇱🇸	🇱🇸	🇱🇸	🇱🇸	—	🇱🇸	🇱🇸	🇱🇸	—	—	—	—	flag: Lesotho
1687	U+1F1F1 U+1F1F9	🇱🇹	🇱🇹	🇱🇹	🇱🇹	—	🇱🇹	🇱🇹	🇱🇹	—	—	—	—	flag: Lithuania
1688	U+1F1F1 U+1F1FA	🇱🇺	🇱🇺	🇱🇺	🇱🇺	—	🇱🇺	🇱🇺	🇱🇺	—	—	—	—	flag: Luxembourg
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1689	U+1F1F1 U+1F1FB	🇱🇻	🇱🇻	🇱🇻	🇱🇻	—	🇱🇻	🇱🇻	🇱🇻	—	—	—	—	flag: Latvia
1690	U+1F1F1 U+1F1FE	🇱🇾	🇱🇾	🇱🇾	🇱🇾	—	🇱🇾	🇱🇾	🇱🇾	—	—	—	—	flag: Libya
1691	U+1F1F2 U+1F1E6	🇲🇦	🇲🇦	🇲🇦	🇲🇦	—	🇲🇦	🇲🇦	🇲🇦	—	—	—	—	flag: Morocco
1692	U+1F1F2 U+1F1E8	🇲🇨	🇲🇨	🇲🇨	🇲🇨	—	🇲🇨	🇲🇨	🇲🇨	—	—	—	—	flag: Monaco
1693	U+1F1F2 U+1F1E9	🇲🇩	🇲🇩	🇲🇩	🇲🇩	—	🇲🇩	🇲🇩	🇲🇩	—	—	—	—	flag: Moldova
1694	U+1F1F2 U+1F1EA	🇲🇪	🇲🇪	🇲🇪	🇲🇪	—	🇲🇪	🇲🇪	🇲🇪	—	—	—	—	flag: Montenegro
1695	U+1F1F2 U+1F1EB	🇲🇫	🇲🇫	🇲🇫	🇲🇫	—	🇲🇫	🇲🇫	🇲🇫	—	—	—	—	flag: St. Martin
1696	U+1F1F2 U+1F1EC	🇲🇬	🇲🇬	🇲🇬	🇲🇬	—	🇲🇬	🇲🇬	🇲🇬	—	—	—	—	flag: Madagascar
1697	U+1F1F2 U+1F1ED	🇲🇭	🇲🇭	🇲🇭	🇲🇭	—	🇲🇭	🇲🇭	🇲🇭	—	—	—	—	flag: Marshall Islands
1698	U+1F1F2 U+1F1F0	🇲🇰	🇲🇰	🇲🇰	🇲🇰	—	🇲🇰	🇲🇰	🇲🇰	—	—	—	—	flag: North Macedonia
1699	U+1F1F2 U+1F1F1	🇲🇱	🇲🇱	🇲🇱	🇲🇱	—	🇲🇱	🇲🇱	🇲🇱	—	—	—	—	flag: Mali
1700	U+1F1F2 U+1F1F2	🇲🇲	🇲🇲	🇲🇲	🇲🇲	—	🇲🇲	🇲🇲	🇲🇲	—	—	—	—	flag: Myanmar (Burma)
1701	U+1F1F2 U+1F1F3	🇲🇳	🇲🇳	🇲🇳	🇲🇳	—	🇲🇳	🇲🇳	🇲🇳	—	—	—	—	flag: Mongolia
1702	U+1F1F2 U+1F1F4	🇲🇴	🇲🇴	🇲🇴	🇲🇴	—	🇲🇴	🇲🇴	🇲🇴	—	—	—	—	flag: Macao SAR China
1703	U+1F1F2 U+1F1F5	🇲🇵	🇲🇵	🇲🇵	🇲🇵	—	🇲🇵	🇲🇵	🇲🇵	—	—	—	—	flag: Northern Mariana Islands
1704	U+1F1F2 U+1F1F6	🇲🇶	🇲🇶	🇲🇶	🇲🇶	—	🇲🇶	🇲🇶	🇲🇶	—	—	—	—	flag: Martinique
1705	U+1F1F2 U+1F1F7	🇲🇷	🇲🇷	🇲🇷	🇲🇷	—	🇲🇷	🇲🇷	🇲🇷	—	—	—	—	flag: Mauritania
1706	U+1F1F2 U+1F1F8	🇲🇸	🇲🇸	🇲🇸	🇲🇸	—	🇲🇸	🇲🇸	🇲🇸	—	—	—	—	flag: Montserrat
1707	U+1F1F2 U+1F1F9	🇲🇹	🇲🇹	🇲🇹	🇲🇹	—	🇲🇹	🇲🇹	🇲🇹	—	—	—	—	flag: Malta
1708	U+1F1F2 U+1F1FA	🇲🇺	🇲🇺	🇲🇺	🇲🇺	—	🇲🇺	🇲🇺	🇲🇺	—	—	—	—	flag: Mauritius
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1709	U+1F1F2 U+1F1FB	🇲🇻	🇲🇻	🇲🇻	🇲🇻	—	🇲🇻	🇲🇻	🇲🇻	—	—	—	—	flag: Maldives
1710	U+1F1F2 U+1F1FC	🇲🇼	🇲🇼	🇲🇼	🇲🇼	—	🇲🇼	🇲🇼	🇲🇼	—	—	—	—	flag: Malawi
1711	U+1F1F2 U+1F1FD	🇲🇽	🇲🇽	🇲🇽	🇲🇽	—	🇲🇽	🇲🇽	🇲🇽	—	—	—	—	flag: Mexico
1712	U+1F1F2 U+1F1FE	🇲🇾	🇲🇾	🇲🇾	🇲🇾	—	🇲🇾	🇲🇾	🇲🇾	—	—	—	—	flag: Malaysia
1713	U+1F1F2 U+1F1FF	🇲🇿	🇲🇿	🇲🇿	🇲🇿	—	🇲🇿	🇲🇿	🇲🇿	—	—	—	—	flag: Mozambique
1714	U+1F1F3 U+1F1E6	🇳🇦	🇳🇦	🇳🇦	🇳🇦	—	🇳🇦	🇳🇦	🇳🇦	—	—	—	—	flag: Namibia
1715	U+1F1F3 U+1F1E8	🇳🇨	🇳🇨	🇳🇨	🇳🇨	—	🇳🇨	🇳🇨	🇳🇨	—	—	—	—	flag: New Caledonia
1716	U+1F1F3 U+1F1EA	🇳🇪	🇳🇪	🇳🇪	🇳🇪	—	🇳🇪	🇳🇪	🇳🇪	—	—	—	—	flag: Niger
1717	U+1F1F3 U+1F1EB	🇳🇫	🇳🇫	🇳🇫	🇳🇫	—	🇳🇫	🇳🇫	🇳🇫	—	—	—	—	flag: Norfolk Island
1718	U+1F1F3 U+1F1EC	🇳🇬	🇳🇬	🇳🇬	🇳🇬	—	🇳🇬	🇳🇬	🇳🇬	—	—	—	—	flag: Nigeria
1719	U+1F1F3 U+1F1EE	🇳🇮	🇳🇮	🇳🇮	🇳🇮	—	🇳🇮	🇳🇮	🇳🇮	—	—	—	—	flag: Nicaragua
1720	U+1F1F3 U+1F1F1	🇳🇱	🇳🇱	🇳🇱	🇳🇱	—	🇳🇱	🇳🇱	🇳🇱	—	—	—	—	flag: Netherlands
1721	U+1F1F3 U+1F1F4	🇳🇴	🇳🇴	🇳🇴	🇳🇴	—	🇳🇴	🇳🇴	🇳🇴	—	—	—	—	flag: Norway
1722	U+1F1F3 U+1F1F5	🇳🇵	🇳🇵	🇳🇵	🇳🇵	—	🇳🇵	🇳🇵	🇳🇵	—	—	—	—	flag: Nepal
1723	U+1F1F3 U+1F1F7	🇳🇷	🇳🇷	🇳🇷	🇳🇷	—	🇳🇷	🇳🇷	🇳🇷	—	—	—	—	flag: Nauru
1724	U+1F1F3 U+1F1FA	🇳🇺	🇳🇺	🇳🇺	🇳🇺	—	🇳🇺	🇳🇺	🇳🇺	—	—	—	—	flag: Niue
1725	U+1F1F3 U+1F1FF	🇳🇿	🇳🇿	🇳🇿	🇳🇿	—	🇳🇿	🇳🇿	🇳🇿	—	—	—	—	flag: New Zealand
1726	U+1F1F4 U+1F1F2	🇴🇲	🇴🇲	🇴🇲	🇴🇲	—	🇴🇲	🇴🇲	🇴🇲	—	—	—	—	flag: Oman
1727	U+1F1F5 U+1F1E6	🇵🇦	🇵🇦	🇵🇦	🇵🇦	—	🇵🇦	🇵🇦	🇵🇦	—	—	—	—	flag: Panama
1728	U+1F1F5 U+1F1EA	🇵🇪	🇵🇪	🇵🇪	🇵🇪	—	🇵🇪	🇵🇪	🇵🇪	—	—	—	—	flag: Peru
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1729	U+1F1F5 U+1F1EB	🇵🇫	🇵🇫	🇵🇫	🇵🇫	—	🇵🇫	🇵🇫	🇵🇫	—	—	—	—	flag: French Polynesia
1730	U+1F1F5 U+1F1EC	🇵🇬	🇵🇬	🇵🇬	🇵🇬	—	🇵🇬	🇵🇬	🇵🇬	—	—	—	—	flag: Papua New Guinea
1731	U+1F1F5 U+1F1ED	🇵🇭	🇵🇭	🇵🇭	🇵🇭	—	🇵🇭	🇵🇭	🇵🇭	—	—	—	—	flag: Philippines
1732	U+1F1F5 U+1F1F0	🇵🇰	🇵🇰	🇵🇰	🇵🇰	—	🇵🇰	🇵🇰	🇵🇰	—	—	—	—	flag: Pakistan
1733	U+1F1F5 U+1F1F1	🇵🇱	🇵🇱	🇵🇱	🇵🇱	—	🇵🇱	🇵🇱	🇵🇱	—	—	—	—	flag: Poland
1734	U+1F1F5 U+1F1F2	🇵🇲	🇵🇲	🇵🇲	🇵🇲	—	🇵🇲	🇵🇲	🇵🇲	—	—	—	—	flag: St. Pierre & Miquelon
1735	U+1F1F5 U+1F1F3	🇵🇳	🇵🇳	🇵🇳	🇵🇳	—	🇵🇳	🇵🇳	🇵🇳	—	—	—	—	flag: Pitcairn Islands
1736	U+1F1F5 U+1F1F7	🇵🇷	🇵🇷	🇵🇷	🇵🇷	—	🇵🇷	🇵🇷	🇵🇷	—	—	—	—	flag: Puerto Rico
1737	U+1F1F5 U+1F1F8	🇵🇸	🇵🇸	🇵🇸	🇵🇸	—	🇵🇸	🇵🇸	🇵🇸	—	—	—	—	flag: Palestinian Territories
1738	U+1F1F5 U+1F1F9	🇵🇹	🇵🇹	🇵🇹	🇵🇹	—	🇵🇹	🇵🇹	🇵🇹	—	—	—	—	flag: Portugal
1739	U+1F1F5 U+1F1FC	🇵🇼	🇵🇼	🇵🇼	🇵🇼	—	🇵🇼	🇵🇼	🇵🇼	—	—	—	—	flag: Palau
1740	U+1F1F5 U+1F1FE	🇵🇾	🇵🇾	🇵🇾	🇵🇾	—	🇵🇾	🇵🇾	🇵🇾	—	—	—	—	flag: Paraguay
1741	U+1F1F6 U+1F1E6	🇶🇦	🇶🇦	🇶🇦	🇶🇦	—	🇶🇦	🇶🇦	🇶🇦	—	—	—	—	flag: Qatar
1742	U+1F1F7 U+1F1EA	🇷🇪	🇷🇪	🇷🇪	🇷🇪	—	🇷🇪	🇷🇪	🇷🇪	—	—	—	—	flag: Réunion
1743	U+1F1F7 U+1F1F4	🇷🇴	🇷🇴	🇷🇴	🇷🇴	—	🇷🇴	🇷🇴	🇷🇴	—	—	—	—	flag: Romania
1744	U+1F1F7 U+1F1F8	🇷🇸	🇷🇸	🇷🇸	🇷🇸	—	🇷🇸	🇷🇸	🇷🇸	—	—	—	—	flag: Serbia
1745	U+1F1F7 U+1F1FA	🇷🇺	🇷🇺	🇷🇺	🇷🇺	—	🇷🇺	🇷🇺	🇷🇺	🇷🇺	🇷🇺	—	🇷🇺	flag: Russia
1746	U+1F1F7 U+1F1FC	🇷🇼	🇷🇼	🇷🇼	🇷🇼	—	🇷🇼	🇷🇼	🇷🇼	—	—	—	—	flag: Rwanda
1747	U+1F1F8 U+1F1E6	🇸🇦	🇸🇦	🇸🇦	🇸🇦	—	🇸🇦	🇸🇦	🇸🇦	—	—	—	—	flag: Saudi Arabia
1748	U+1F1F8 U+1F1E7	🇸🇧	🇸🇧	🇸🇧	🇸🇧	—	🇸🇧	🇸🇧	🇸🇧	—	—	—	—	flag: Solomon Islands
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1749	U+1F1F8 U+1F1E8	🇸🇨	🇸🇨	🇸🇨	🇸🇨	—	🇸🇨	🇸🇨	🇸🇨	—	—	—	—	flag: Seychelles
1750	U+1F1F8 U+1F1E9	🇸🇩	🇸🇩	🇸🇩	🇸🇩	—	🇸🇩	🇸🇩	🇸🇩	—	—	—	—	flag: Sudan
1751	U+1F1F8 U+1F1EA	🇸🇪	🇸🇪	🇸🇪	🇸🇪	—	🇸🇪	🇸🇪	🇸🇪	—	—	—	—	flag: Sweden
1752	U+1F1F8 U+1F1EC	🇸🇬	🇸🇬	🇸🇬	🇸🇬	—	🇸🇬	🇸🇬	🇸🇬	—	—	—	—	flag: Singapore
1753	U+1F1F8 U+1F1ED	🇸🇭	🇸🇭	🇸🇭	🇸🇭	—	🇸🇭	🇸🇭	🇸🇭	—	—	—	—	flag: St. Helena
1754	U+1F1F8 U+1F1EE	🇸🇮	🇸🇮	🇸🇮	🇸🇮	—	🇸🇮	🇸🇮	🇸🇮	—	—	—	—	flag: Slovenia
1755	U+1F1F8 U+1F1EF	🇸🇯	🇸🇯	🇸🇯	🇸🇯	—	🇸🇯	🇸🇯	🇸🇯	—	—	—	—	flag: Svalbard & Jan Mayen
1756	U+1F1F8 U+1F1F0	🇸🇰	🇸🇰	🇸🇰	🇸🇰	—	🇸🇰	🇸🇰	🇸🇰	—	—	—	—	flag: Slovakia
1757	U+1F1F8 U+1F1F1	🇸🇱	🇸🇱	🇸🇱	🇸🇱	—	🇸🇱	🇸🇱	🇸🇱	—	—	—	—	flag: Sierra Leone
1758	U+1F1F8 U+1F1F2	🇸🇲	🇸🇲	🇸🇲	🇸🇲	—	🇸🇲	🇸🇲	🇸🇲	—	—	—	—	flag: San Marino
1759	U+1F1F8 U+1F1F3	🇸🇳	🇸🇳	🇸🇳	🇸🇳	—	🇸🇳	🇸🇳	🇸🇳	—	—	—	—	flag: Senegal
1760	U+1F1F8 U+1F1F4	🇸🇴	🇸🇴	🇸🇴	🇸🇴	—	🇸🇴	🇸🇴	🇸🇴	—	—	—	—	flag: Somalia
1761	U+1F1F8 U+1F1F7	🇸🇷	🇸🇷	🇸🇷	🇸🇷	—	🇸🇷	🇸🇷	🇸🇷	—	—	—	—	flag: Suriname
1762	U+1F1F8 U+1F1F8	🇸🇸	🇸🇸	🇸🇸	🇸🇸	—	🇸🇸	🇸🇸	🇸🇸	—	—	—	—	flag: South Sudan
1763	U+1F1F8 U+1F1F9	🇸🇹	🇸🇹	🇸🇹	🇸🇹	—	🇸🇹	🇸🇹	🇸🇹	—	—	—	—	flag: São Tomé & Príncipe
1764	U+1F1F8 U+1F1FB	🇸🇻	🇸🇻	🇸🇻	🇸🇻	—	🇸🇻	🇸🇻	🇸🇻	—	—	—	—	flag: El Salvador
1765	U+1F1F8 U+1F1FD	🇸🇽	🇸🇽	🇸🇽	🇸🇽	—	🇸🇽	🇸🇽	🇸🇽	—	—	—	—	flag: Sint Maarten
1766	U+1F1F8 U+1F1FE	🇸🇾	🇸🇾	🇸🇾	🇸🇾	—	🇸🇾	🇸🇾	🇸🇾	—	—	—	—	flag: Syria
1767	U+1F1F8 U+1F1FF	🇸🇿	🇸🇿	🇸🇿	🇸🇿	—	🇸🇿	🇸🇿	🇸🇿	—	—	—	—	flag: Eswatini
1768	U+1F1F9 U+1F1E6	🇹🇦	🇹🇦	🇹🇦	🇹🇦	—	🇹🇦	🇹🇦	🇹🇦	—	—	—	—	flag: Tristan da Cunha
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1769	U+1F1F9 U+1F1E8	🇹🇨	🇹🇨	🇹🇨	🇹🇨	—	🇹🇨	🇹🇨	🇹🇨	—	—	—	—	flag: Turks & Caicos Islands
1770	U+1F1F9 U+1F1E9	🇹🇩	🇹🇩	🇹🇩	🇹🇩	—	🇹🇩	🇹🇩	🇹🇩	—	—	—	—	flag: Chad
1771	U+1F1F9 U+1F1EB	🇹🇫	🇹🇫	🇹🇫	🇹🇫	—	🇹🇫	🇹🇫	🇹🇫	—	—	—	—	flag: French Southern Territories
1772	U+1F1F9 U+1F1EC	🇹🇬	🇹🇬	🇹🇬	🇹🇬	—	🇹🇬	🇹🇬	🇹🇬	—	—	—	—	flag: Togo
1773	U+1F1F9 U+1F1ED	🇹🇭	🇹🇭	🇹🇭	🇹🇭	—	🇹🇭	🇹🇭	🇹🇭	—	—	—	—	flag: Thailand
1774	U+1F1F9 U+1F1EF	🇹🇯	🇹🇯	🇹🇯	🇹🇯	—	🇹🇯	🇹🇯	🇹🇯	—	—	—	—	flag: Tajikistan
1775	U+1F1F9 U+1F1F0	🇹🇰	🇹🇰	🇹🇰	🇹🇰	—	🇹🇰	🇹🇰	🇹🇰	—	—	—	—	flag: Tokelau
1776	U+1F1F9 U+1F1F1	🇹🇱	🇹🇱	🇹🇱	🇹🇱	—	🇹🇱	🇹🇱	🇹🇱	—	—	—	—	flag: Timor-Leste
1777	U+1F1F9 U+1F1F2	🇹🇲	🇹🇲	🇹🇲	🇹🇲	—	🇹🇲	🇹🇲	🇹🇲	—	—	—	—	flag: Turkmenistan
1778	U+1F1F9 U+1F1F3	🇹🇳	🇹🇳	🇹🇳	🇹🇳	—	🇹🇳	🇹🇳	🇹🇳	—	—	—	—	flag: Tunisia
1779	U+1F1F9 U+1F1F4	🇹🇴	🇹🇴	🇹🇴	🇹🇴	—	🇹🇴	🇹🇴	🇹🇴	—	—	—	—	flag: Tonga
1780	U+1F1F9 U+1F1F7	🇹🇷	🇹🇷	🇹🇷	🇹🇷	—	🇹🇷	🇹🇷	🇹🇷	—	—	—	—	flag: Turkey
1781	U+1F1F9 U+1F1F9	🇹🇹	🇹🇹	🇹🇹	🇹🇹	—	🇹🇹	🇹🇹	🇹🇹	—	—	—	—	flag: Trinidad & Tobago
1782	U+1F1F9 U+1F1FB	🇹🇻	🇹🇻	🇹🇻	🇹🇻	—	🇹🇻	🇹🇻	🇹🇻	—	—	—	—	flag: Tuvalu
1783	U+1F1F9 U+1F1FC	🇹🇼	🇹🇼	🇹🇼	🇹🇼	—	🇹🇼	🇹🇼	🇹🇼	—	—	—	—	flag: Taiwan
1784	U+1F1F9 U+1F1FF	🇹🇿	🇹🇿	🇹🇿	🇹🇿	—	🇹🇿	🇹🇿	🇹🇿	—	—	—	—	flag: Tanzania
1785	U+1F1FA U+1F1E6	🇺🇦	🇺🇦	🇺🇦	🇺🇦	—	🇺🇦	🇺🇦	🇺🇦	—	—	—	—	flag: Ukraine
1786	U+1F1FA U+1F1EC	🇺🇬	🇺🇬	🇺🇬	🇺🇬	—	🇺🇬	🇺🇬	🇺🇬	—	—	—	—	flag: Uganda
1787	U+1F1FA U+1F1F2	🇺🇲	🇺🇲	🇺🇲	🇺🇲	—	🇺🇲	🇺🇲	🇺🇲	—	—	—	—	flag: U.S. Outlying Islands
1788	U+1F1FA U+1F1F3	🇺🇳	🇺🇳	🇺🇳	🇺🇳	—	🇺🇳	🇺🇳	🇺🇳	—	—	—	—	flag: United Nations
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1789	U+1F1FA U+1F1F8	🇺🇸	🇺🇸	🇺🇸	🇺🇸	—	🇺🇸	🇺🇸	🇺🇸	🇺🇸	🇺🇸	—	🇺🇸	flag: United States
1790	U+1F1FA U+1F1FE	🇺🇾	🇺🇾	🇺🇾	🇺🇾	—	🇺🇾	🇺🇾	🇺🇾	—	—	—	—	flag: Uruguay
1791	U+1F1FA U+1F1FF	🇺🇿	🇺🇿	🇺🇿	🇺🇿	—	🇺🇿	🇺🇿	🇺🇿	—	—	—	—	flag: Uzbekistan
1792	U+1F1FB U+1F1E6	🇻🇦	🇻🇦	🇻🇦	🇻🇦	—	🇻🇦	🇻🇦	🇻🇦	—	—	—	—	flag: Vatican City
1793	U+1F1FB U+1F1E8	🇻🇨	🇻🇨	🇻🇨	🇻🇨	—	🇻🇨	🇻🇨	🇻🇨	—	—	—	—	flag: St. Vincent & Grenadines
1794	U+1F1FB U+1F1EA	🇻🇪	🇻🇪	🇻🇪	🇻🇪	—	🇻🇪	🇻🇪	🇻🇪	—	—	—	—	flag: Venezuela
1795	U+1F1FB U+1F1EC	🇻🇬	🇻🇬	🇻🇬	🇻🇬	—	🇻🇬	🇻🇬	🇻🇬	—	—	—	—	flag: British Virgin Islands
1796	U+1F1FB U+1F1EE	🇻🇮	🇻🇮	🇻🇮	🇻🇮	—	🇻🇮	🇻🇮	🇻🇮	—	—	—	—	flag: U.S. Virgin Islands
1797	U+1F1FB U+1F1F3	🇻🇳	🇻🇳	🇻🇳	🇻🇳	—	🇻🇳	🇻🇳	🇻🇳	—	—	—	—	flag: Vietnam
1798	U+1F1FB U+1F1FA	🇻🇺	🇻🇺	🇻🇺	🇻🇺	—	🇻🇺	🇻🇺	🇻🇺	—	—	—	—	flag: Vanuatu
1799	U+1F1FC U+1F1EB	🇼🇫	🇼🇫	🇼🇫	🇼🇫	—	🇼🇫	🇼🇫	🇼🇫	—	—	—	—	flag: Wallis & Futuna
1800	U+1F1FC U+1F1F8	🇼🇸	🇼🇸	🇼🇸	🇼🇸	—	🇼🇸	🇼🇸	🇼🇸	—	—	—	—	flag: Samoa
1801	U+1F1FD U+1F1F0	🇽🇰	🇽🇰	🇽🇰	🇽🇰	—	🇽🇰	🇽🇰	🇽🇰	—	—	—	—	flag: Kosovo
1802	U+1F1FE U+1F1EA	🇾🇪	🇾🇪	🇾🇪	🇾🇪	—	🇾🇪	🇾🇪	🇾🇪	—	—	—	—	flag: Yemen
1803	U+1F1FE U+1F1F9	🇾🇹	🇾🇹	🇾🇹	🇾🇹	—	🇾🇹	🇾🇹	🇾🇹	—	—	—	—	flag: Mayotte
1804	U+1F1FF U+1F1E6	🇿🇦	🇿🇦	🇿🇦	🇿🇦	—	🇿🇦	🇿🇦	🇿🇦	—	—	—	—	flag: South Africa
1805	U+1F1FF U+1F1F2	🇿🇲	🇿🇲	🇿🇲	🇿🇲	—	🇿🇲	🇿🇲	🇿🇲	—	—	—	—	flag: Zambia
1806	U+1F1FF U+1F1FC	🇿🇼	🇿🇼	🇿🇼	🇿🇼	—	🇿🇼	🇿🇼	🇿🇼	—	—	—	—	flag: Zimbabwe
subdivision-flag
№	Code	Browser	Appl	Goog	FB	Wind	Twtr	Joy	Sams	GMail	SB	DCM	KDDI	CLDR Short Name
1807	U+1F3F4 U+E0067 U+E0062 U+E0065 U+E006E U+E0067 U+E007F	🏴󠁧󠁢󠁥󠁮󠁧󠁿	🏴󠁧󠁢󠁥󠁮󠁧󠁿	🏴󠁧󠁢󠁥󠁮󠁧󠁿	🏴󠁧󠁢󠁥󠁮󠁧󠁿	—	🏴󠁧󠁢󠁥󠁮󠁧󠁿	🏴󠁧󠁢󠁥󠁮󠁧󠁿	🏴󠁧󠁢󠁥󠁮󠁧󠁿	—	—	—	—	flag: England
1808	U+1F3F4 U+E0067 U+E0062 U+E0073 U+E0063 U+E0074 U+E007F	🏴󠁧󠁢󠁳󠁣󠁴󠁿	🏴󠁧󠁢󠁳󠁣󠁴󠁿	🏴󠁧󠁢󠁳󠁣󠁴󠁿	🏴󠁧󠁢󠁳󠁣󠁴󠁿	—	🏴󠁧󠁢󠁳󠁣󠁴󠁿	🏴󠁧󠁢󠁳󠁣󠁴󠁿	🏴󠁧󠁢󠁳󠁣󠁴󠁿	—	—	—	—	flag: Scotland
1809	U+1F3F4 U+E0067 U+E0062 U+E0077 U+E006C U+E0073 U+E007F	🏴󠁧󠁢󠁷󠁬󠁳󠁿	🏴󠁧󠁢󠁷󠁬󠁳󠁿	🏴󠁧󠁢󠁷󠁬󠁳󠁿	🏴󠁧󠁢󠁷󠁬󠁳󠁿	—	🏴󠁧󠁢󠁷󠁬󠁳󠁿	🏴󠁧󠁢󠁷󠁬󠁳󠁿	🏴󠁧󠁢󠁷󠁬󠁳󠁿	—	—	—	—	flag: Wales

Access to Copyright and terms of use
Last updated:  - 1/30/2020, 4:05:59 AM - Contact Us
"""

all_characters = set(emoji_webpage)

# Remove string characters and '—'.
string_characters = set(string.printable)
emojis = all_characters - string_characters
emojis.remove('—')

# Remove letter emojis.
letter_emojis = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰',
                 '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']
emojis = emojis - set(letter_emojis)

# Add all two character combinations of letter emojis to capture flags.
flag_emojis = []
length = 2
for p in itertools.permutations(letter_emojis, length):
    flag = ''.join(p)
    flag_emojis.append(flag)

# Add lists together.
emojis = list(emojis) + flag_emojis

# Export to file.
with open(export_path, 'w') as outfile:
    json.dump(list(emojis), outfile)

print('emoji list:')
print(emojis)
print('total:', len(emojis))
