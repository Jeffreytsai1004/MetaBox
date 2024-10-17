//Maya ASCII 2023 scene
//Name: Plug_Long_08.ma
//Last modified: Tue, Feb 07, 2023 05:52:57 PM
//Codeset: 1252
requires maya "2023";
requires "stereoCamera" "10.0";
requires "mtoa" "5.2.2.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202202161415-df43006fd3";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19045)";
fileInfo "UUID" "D6F57E55-4651-88B6-926E-BC8B1E5C3467";
createNode transform -n "Plug_Mesh";
	rename -uid "AE272114-4A7D-FDD2-C9FC-3C9AAEF927D2";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "6ED3425B-4174-15AD-C4A8-44B2D4C26159";
	setAttr -k off ".v";
	setAttr -s 8 ".iog[0].og";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 3 "e[140]" "e[142]" "e[144:145]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "e[134:137]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[0:70]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 2 "f[0:64]" "f[69:70]";
	setAttr ".iog[0].og[6].gcl" -type "componentList" 1 "e[134:137]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 86 ".uvst[0].uvsp[0:85]" -type "float2" 0.088768363 7.024632e-09
		 6.8480732e-10 0.088832863 1 0.088768363 0.91123158 6.8431066e-10 0.91123164 1 1 0.91123158
		 1.0476442e-14 0.089221179 1.3095553e-15 0.90456706 0.10141337 0 0.91077566 0 1 0.10141337
		 1 0.90455717 0.90458798 1 0.088768438 1 0.095442854 1 7.0246058e-09 0.91122824 7.7089419e-09
		 1 0 1 0 0 0 7.7089419e-09 1 0 1 0 1 1 1 1 0.069267318 0.12227398 0.061817802 0.19145127
		 0 0 0.061753951 0.061753951 0.09986189 3.4311074e-09 0.93825591 0.061744049 1 0.099861942
		 0.80884314 0.061617248 1 2.0896811e-08 0.94142008 0.94142002 0.9001382 1 0.94138831
		 0.81330079 1 1 0.058919538 0.94108039 1.9807422e-09 0.90015423 0.1885314 0.94015408
		 0 1 0.90015113 2.1371012e-08 0.19113714 0.061620418 0.058698647 0.81317073 7.6449274e-09
		 0.099845737 1 0.90015113 0.93820357 0.19143611 0.099848911 1 0.81154734 0.94019145
		 0.12210461 0.091127299 0.21455687 0.088609897 0.77554345 0.088621266 0.86517459 0.088221475
		 0.91745901 0.121178 0.73496276 0.85500574 0.71927255 0.91488701 0.69378901 0.91880554
		 0.2565161 0.9167521 0.21685883 0.91329986 0.19848712 0.85709828 0.064130329 0.19487812
		 0.064130299 0.80512178 0.19485494 0.064130329 0.8051191 0.064130314 0.93586963 0.19489472
		 0.93586957 0.80512315 0.80514503 0.93586963 0.19488081 0.93586963 0.064130336 0.064130336
		 0.93586963 0.064130306 0.93586963 0.93586963 0.064130306 0.93586963 0 0 0.5 0 1 1
		 0 1 0 0 1 0 1 1 0 1 0.5 0 1 0 1 1 0 1 1 1 0 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 80 ".vt[0:79]"  1.22931576 -8.5381202e-16 -0.34587452 1.35044813 -8.7436014e-16 -0.32401568
		 1.40062273 -8.8285842e-16 -0.27124277 1.15510738 0.016873915 -0.31354451 1.27623999 0.016873915 -0.29168552
		 1.32641459 0.016873915 -0.23891109 1.28272891 0.061853569 -0.21987936 1.23255444 0.061853569 -0.27265283
		 1.1114217 0.061853569 -0.29451182 -1.20226073 0.016873915 -0.71617061 -1.31550813 0.016873915 -0.6630969
		 -1.36241746 0.016873915 -0.53497112 -1.14742458 0.061853569 -0.67269784 -1.26855707 0.061853569 -0.62276834
		 -1.31873178 0.061853569 -0.50222808 -1.4366256 -5.5478742e-16 -0.61954731 -1.38645089 -5.6331524e-16 -0.74008656
		 -1.26531863 -5.8390333e-16 -0.79001653 -1.36241746 0.016873915 0.58291233 -1.30908442 0.016873915 0.6829868
		 -1.18032718 0.016873915 0.72443956 -1.31873178 0.061853569 0.53445542 -1.26855719 0.061853569 0.64149737
		 -1.14742458 0.061853569 0.68583477 -1.26531863 -5.8390439e-16 0.79001617 -1.38645089 -5.6331614e-16 0.74567854
		 -1.4366256 -5.5478816e-16 0.63863665 1.15510738 0.016873915 0.31716499 1.27623987 0.016873915 0.29775327
		 1.32641459 0.016873915 0.25088969 1.1114217 0.061853569 0.30026406 1.23255444 0.061853569 0.28085229
		 1.28272891 0.061853569 0.23398878 1.40062273 -8.8269499e-16 0.2796002 1.35044813 -8.7416675e-16 0.32646343
		 1.22931576 -8.536064e-16 0.34587452 -0.70930302 0.82885516 -0.29484949 -0.71723878 0.82210559 -0.34361187
		 -0.72981912 0.80269003 -0.36975285 0.75873262 0.34887126 -0.16857275 0.73352385 0.36856648 -0.1413357
		 0.72017723 0.37729999 -0.089211993 -0.88355285 0.84634876 -0.20024946 -0.85645604 0.86407095 -0.18645521
		 -0.81687057 0.86283392 -0.17066973 -0.81684119 0.86282468 0.23685364 -0.85645074 0.86404991 0.25309476
		 -0.88357425 0.8463034 0.26630646 -0.729967 0.8024258 0.41690999 -0.71755058 0.82208657 0.3914772
		 -0.71022052 0.82914299 0.34287697 0.72011405 0.37732053 0.10887261 0.73367697 0.36843029 0.16170721
		 0.75925654 0.34844545 0.18859343 0.90501964 0.30962792 0.12003737 0.87621224 0.32564875 0.10592789
		 0.84448415 0.33803314 0.080476187 0.84048909 0.33929539 -0.058104962 0.87465042 0.32632422 -0.078303523
		 0.90478361 0.30978268 -0.091477968 -0.78715521 0.8534472 -0.25176495 -0.81626928 0.85247183 -0.29537687
		 -0.8379845 0.83453715 -0.32013586 -0.79151559 0.85482544 0.30901092 -0.81755209 0.85282397 0.3498807
		 -0.83805329 0.83441371 0.37279639 0.83685124 0.34044418 0.089520708 0.844266 0.33427998 0.14182718
		 0.86786938 0.3173528 0.16924146 0.83375442 0.34142265 -0.069887348 0.84263092 0.33508283 -0.11976134
		 0.86575323 0.31883559 -0.14623916 -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773;
	setAttr -s 150 ".ed[0:149]"  15 26 1 33 2 1 2 1 1 5 2 1 1 0 1 0 3 1 5 4 1
		 4 7 1 7 6 1 6 5 1 4 3 1 3 8 1 8 7 1 13 12 1 12 9 1 11 14 1 14 13 1 11 10 1 10 16 1
		 16 15 1 15 11 1 10 9 1 9 17 1 17 16 1 22 21 1 21 18 1 20 23 1 23 22 1 20 19 1 19 25 1
		 25 24 1 24 20 1 19 18 1 18 26 1 26 25 1 31 30 1 30 27 1 29 32 1 32 31 1 29 28 1 28 34 1
		 34 33 1 33 29 1 28 27 1 27 35 1 35 34 1 14 21 1 23 30 1 32 6 1 9 3 1 11 18 1 20 27 1
		 29 5 1 1 4 1 10 13 1 19 22 1 28 31 1 61 60 1 60 36 1 38 62 1 62 61 1 38 37 1 37 40 1
		 40 39 1 37 36 1 36 41 1 41 40 1 71 39 1 41 69 1 62 42 1 44 60 1 44 43 1 43 46 1 46 45 1
		 45 44 1 43 42 1 42 47 1 47 46 1 64 63 1 63 45 1 47 65 1 65 64 1 65 48 1 50 63 1 50 49 1
		 49 52 1 52 51 1 49 48 1 48 53 1 53 52 1 67 66 1 66 51 1 53 68 1 68 67 1 68 54 1 56 66 1
		 56 55 1 55 58 1 58 57 1 57 56 1 55 54 1 54 59 1 59 58 1 70 69 1 69 57 1 59 71 1 71 70 1
		 38 12 1 13 62 1 14 42 1 65 22 1 23 48 1 47 21 1 68 31 1 32 54 1 53 30 1 71 7 1 8 39 1
		 59 6 1 37 61 1 46 64 1 52 67 1 58 70 1 43 61 1 49 64 1 55 67 1 40 70 1 0 17 1 8 12 1
		 39 38 1 51 50 1 24 35 1 36 50 1 41 51 1 72 74 0 72 73 0 73 75 0 74 75 0 72 76 1 74 77 1
		 76 77 0 73 78 1 76 78 0 75 79 1 78 79 0 77 79 0 1 75 0 16 74 0 34 73 0 25 72 0;
	setAttr -s 71 -ch 296 ".fc[0:70]" -type "polyFaces" 
		f 6 -35 -1 -20 147 -135 -150
		mu 0 6 21 3 0 19 73 72
		f 6 -46 -132 -31 149 135 -149
		mu 0 6 23 5 2 21 77 76
		f 4 6 7 8 9
		mu 0 4 14 17 40 47
		f 4 10 11 12 -8
		mu 0 4 17 7 38 40
		f 4 17 18 19 20
		mu 0 4 8 18 19 0
		f 4 21 22 23 -19
		mu 0 4 18 6 1 19
		f 4 28 29 30 31
		mu 0 4 10 20 21 2
		f 4 32 33 34 -30
		mu 0 4 20 9 3 21
		f 4 39 40 41 42
		mu 0 4 12 22 23 4
		f 4 43 44 45 -41
		mu 0 4 22 11 5 23
		f 4 -6 127 -23 49
		mu 0 4 7 15 1 6
		f 4 -12 -50 -15 -129
		mu 0 4 38 7 6 44
		f 4 -16 50 -26 -47
		mu 0 4 28 8 9 41
		f 4 -21 0 -34 -51
		mu 0 4 8 0 3 9
		f 4 -37 -48 -27 51
		mu 0 4 11 45 30 10
		f 4 131 -45 -52 -32
		mu 0 4 2 5 11 10
		f 4 -38 52 -10 -49
		mu 0 4 34 12 14 47
		f 4 -43 1 -4 -53
		mu 0 4 12 4 13 14
		f 4 2 53 -7 3
		mu 0 4 13 16 17 14
		f 4 4 5 -11 -54
		mu 0 4 16 15 7 17
		f 4 -22 54 13 14
		mu 0 4 6 18 26 44
		f 4 -18 15 16 -55
		mu 0 4 18 8 28 26
		f 4 -33 55 24 25
		mu 0 4 9 20 32 41
		f 4 -29 26 27 -56
		mu 0 4 20 10 30 32
		f 4 -44 56 35 36
		mu 0 4 11 22 36 45
		f 4 -40 37 38 -57
		mu 0 4 22 12 34 36
		f 4 63 129 61 62
		mu 0 4 61 43 25 60
		f 4 66 -63 64 65
		mu 0 4 59 61 60 24
		f 4 71 72 73 74
		mu 0 4 50 62 63 51
		f 4 75 76 77 -73
		mu 0 4 62 42 31 63
		f 4 86 130 84 85
		mu 0 4 65 54 53 64
		f 4 89 -86 87 88
		mu 0 4 35 65 64 46
		f 4 96 97 98 99
		mu 0 4 56 66 67 57
		f 4 100 101 102 -98
		mu 0 4 66 48 39 67
		f 4 -60 107 -14 108
		mu 0 4 27 25 44 26
		f 4 -70 -109 -17 109
		mu 0 4 42 27 26 28
		f 4 -83 110 -28 111
		mu 0 4 46 29 32 30
		f 4 -81 112 -25 -111
		mu 0 4 29 31 41 32
		f 4 -95 113 -39 114
		mu 0 4 48 33 36 34
		f 4 -93 115 -36 -114
		mu 0 4 33 35 45 36
		f 4 -68 116 -13 117
		mu 0 4 43 37 40 38
		f 4 -106 118 -9 -117
		mu 0 4 37 39 47 40
		f 4 -113 -77 -110 46
		mu 0 4 41 31 42 28
		f 4 -118 128 -108 -130
		mu 0 4 43 38 44 25
		f 4 -116 -89 -112 47
		mu 0 4 45 35 46 30
		f 4 -119 -102 -115 48
		mu 0 4 47 39 48 34
		f 6 133 -92 -96 -100 -105 -69
		mu 0 6 59 54 55 56 57 58
		f 4 -65 119 57 58
		mu 0 4 24 60 68 49
		f 4 -62 59 60 -120
		mu 0 4 60 25 27 68
		f 4 -74 120 78 79
		mu 0 4 51 63 69 52
		f 4 -78 80 81 -121
		mu 0 4 63 31 29 69
		f 4 -87 121 90 91
		mu 0 4 54 65 70 55
		f 4 -90 92 93 -122
		mu 0 4 65 35 33 70
		f 4 -99 122 103 104
		mu 0 4 57 67 71 58
		f 4 -103 105 106 -123
		mu 0 4 67 39 37 71
		f 4 -76 123 -61 69
		mu 0 4 42 62 68 27
		f 4 -72 70 -58 -124
		mu 0 4 62 50 49 68
		f 4 -88 124 -82 82
		mu 0 4 46 64 69 29
		f 4 -85 83 -79 -125
		mu 0 4 64 53 52 69
		f 4 -101 125 -94 94
		mu 0 4 48 66 70 33
		f 4 -97 95 -91 -126
		mu 0 4 66 56 55 70
		f 4 -64 126 -107 67
		mu 0 4 43 61 71 37
		f 4 -67 68 -104 -127
		mu 0 4 61 59 58 71
		f 6 -59 -71 -75 -80 -84 -133
		mu 0 6 24 49 50 51 52 53
		f 4 -134 -66 132 -131
		mu 0 4 54 59 24 53
		f 4 134 139 -141 -139
		mu 0 4 72 73 74 75
		f 4 -136 138 142 -142
		mu 0 4 76 77 78 79
		f 4 -137 141 144 -144
		mu 0 4 80 81 82 83
		f 4 137 143 -146 -140
		mu 0 4 73 80 84 85
		f 6 146 -138 -148 -24 -128 -5
		mu 0 6 16 80 73 19 1 15
		f 6 148 136 -147 -3 -2 -42
		mu 0 6 23 81 80 16 13 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 2 
		73 0 
		80 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".db" yes;
	setAttr ".vs" 4;
	setAttr ".bw" 4;
createNode transform -n "Plug_controler" -p "Plug_Mesh";
	rename -uid "28246CD5-44EB-01E5-45A4-039D73095DDF";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" -2.4424906541753444e-15 0 -3.9968028886505635e-15 ;
	setAttr ".sp" -type "double3" -2.4424906541753444e-15 0 -3.9968028886505635e-15 ;
createNode nurbsCurve -n "Plug_controlerShape" -p "Plug_controler";
	rename -uid "D3B7FC80-425C-B88A-E87F-A5AAE7D57753";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 0.53846669 1 ;
	setAttr ".cc" -type "nurbsCurve" 
		3 68 2 no 3
		73 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70
		71
		0.20686707830461301 1.1102230246251565e-16 -2.2324513085130748
		2.3826125097526738e-16 1.1102230246251565e-16 -2.2420153507431881
		-0.20686707830461318 1.1102230246251565e-16 -2.2324513085130873
		-0.41196923963640886 1.1102230246251565e-16 -2.2038407788589192
		-0.61355662467188965 1.1102230246251565e-16 -2.1564278567318969
		-0.80990936091964172 1.1102230246251565e-16 -2.0906170524662855
		-0.99935223606602541 1.1102230246251565e-16 -2.0069698406398429
		-1.1802689902959673 1.1102230246251565e-16 -1.9061998697706957
		-1.3511161056518295 1.1102230246251565e-16 -1.789166873719809
		-1.5104359747843905 1.1102230246251565e-16 -1.6568693367448168
		-1.6568693367448164 1.1102230246251565e-16 -1.5104359747843905
		-1.7891668737198088 5.5511151231257827e-17 -1.3511161056518293
		-1.9061998697706948 5.5511151231257827e-17 -1.1802689902959673
		-2.006969840639842 5.5511151231257827e-17 -0.99935223606602519
		-2.0906170524662842 5.5511151231257827e-17 -0.80990936091964172
		-2.1564278567318951 5.5511151231257827e-17 -0.61355662467188909
		-2.2038407788589169 0 -0.4119692396364088
		-2.232451308513085 0 -0.20686707830461323
		-2.2420153507431828 0 -2.1397042986067343e-16
		-2.232451308513085 0 0.20686707830461276
		-2.203840778858916 0 0.4119692396364083
		-2.1564278567318942 -5.5511151231257827e-17 0.61355662467188843
		-2.0906170524662833 -5.5511151231257827e-17 0.80990936091964083
		-2.0069698406398411 -5.5511151231257827e-17 0.99935223606602408
		-1.9061998697706943 -5.5511151231257827e-17 1.1802689902959664
		-1.7891668737198072 -5.5511151231257827e-17 1.3511161056518279
		-1.6568693367448144 -1.1102230246251565e-16 1.5104359747843894
		-1.5104359747843892 -1.1102230246251565e-16 1.6568693367448146
		-1.3511161056518277 -1.1102230246251565e-16 1.7891668737198068
		-1.1802689902959662 -1.1102230246251565e-16 1.9061998697706932
		-0.99935223606602408 -1.1102230246251565e-16 2.0069698406398397
		-0.80990936091964083 -1.1102230246251565e-16 2.0906170524662824
		-0.61355662467188854 -1.1102230246251565e-16 2.1564278567318929
		-0.41196923963640825 -1.1102230246251565e-16 2.2038407788589143
		-0.2068670783046129 -1.1102230246251565e-16 2.2324513085130837
		-2.8540790132205498e-17 -1.1102230246251565e-16 2.2420153507431801
		0.20686707830461282 -1.1102230246251565e-16 2.2324513085130828
		0.41196923963640808 -1.1102230246251565e-16 2.2038407788589143
		0.6135566246718881 -1.1102230246251565e-16 2.1564278567318929
		0.80990936091964039 -1.1102230246251565e-16 2.0906170524662815
		0.99935223606602375 -1.1102230246251565e-16 2.0069698406398393
		1.1802689902959653 -1.1102230246251565e-16 1.9061998697706926
		1.3511161056518268 -1.1102230246251565e-16 1.7891668737198061
		1.5104359747843876 -1.1102230246251565e-16 1.6568693367448133
		1.6568693367448128 -1.1102230246251565e-16 1.5104359747843881
		1.7891668737198057 -5.5511151231257827e-17 1.3511161056518268
		1.9061998697706912 -5.5511151231257827e-17 1.1802689902959651
		2.0069698406398384 -5.5511151231257827e-17 0.99935223606602386
		2.0906170524662802 -5.5511151231257827e-17 0.80990936091964016
		2.1564278567318911 -5.5511151231257827e-17 0.61355662467188798
		2.2038407788589121 0 0.41196923963640808
		2.2324513085130815 0 0.20686707830461298
		2.2420153507431779 0 3.5477364116248252e-16
		2.2324513085130806 0 -0.20686707830461232
		2.2038407788589121 0 -0.41196923963640736
		2.1564278567318902 5.5511151231257827e-17 -0.6135566246718871
		2.0906170524662797 5.5511151231257827e-17 -0.80990936091963917
		2.0069698406398375 5.5511151231257827e-17 -0.99935223606602208
		1.9061998697706908 5.5511151231257827e-17 -1.180268990295964
		1.7891668737198041 5.5511151231257827e-17 -1.3511161056518253
		1.6568693367448117 1.1102230246251565e-16 -1.5104359747843861
		1.5104359747843865 1.1102230246251565e-16 -1.6568693367448106
		1.3511161056518253 1.1102230246251565e-16 -1.7891668737198037
		1.1802689902959642 1.1102230246251565e-16 -1.9061998697706892
		0.99935223606602297 1.1102230246251565e-16 -2.0069698406398366
		0.80990936091963961 1.1102230246251565e-16 -2.0906170524662779
		0.61355662467188776 1.1102230246251565e-16 -2.1564278567318884
		0.4119692396364078 1.1102230246251565e-16 -2.2038407788589107
		0.20686707830461301 1.1102230246251565e-16 -2.2324513085130748
		2.3826125097526738e-16 1.1102230246251565e-16 -2.2420153507431881
		-0.20686707830461318 1.1102230246251565e-16 -2.2324513085130873
		;
createNode transform -n "PlugIt_PlugCountNumber_12";
	rename -uid "A0EF974B-43A6-F5F9-FFA6-5DA650A75069";
createNode groupId -n "groupId2";
	rename -uid "3FF78D1E-4238-4D72-E773-28B76064571D";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "4B2D5B18-4B23-AD22-D96E-399D87EE747C";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Interior_set";
	rename -uid "2C0B072E-442C-8565-E227-4BB0BF221F33";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId5";
	rename -uid "5FA7BAEE-4D50-59DC-B2B4-30B41348C661";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "DD9411C9-4577-751E-FF3E-8398B5AFA6C4";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "A709D687-41C5-883A-072C-5799C26279A1";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "9FD8C654-40F0-D2DF-AA21-8FB21F55AF83";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "2E547210-4B78-F858-0092-7492B727FF51";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "2301F8C2-4198-4CE3-E971-2AA12755655A";
	setAttr ".ihi" 0;
createNode materialInfo -n "materialInfo2";
	rename -uid "34A08C2E-4231-689A-3C82-9AADE04FAF22";
createNode shadingEngine -n "PlugIt_Plug_SG";
	rename -uid "FF0400C5-4732-59DB-85A4-3A97910FC6A9";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode lambert -n "PlugIt_Plug_Shd";
	rename -uid "31620B3E-439F-8FDB-53F6-87AF02806ED4";
	setAttr ".c" -type "float3" 0.89999998 0.38077497 0 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "221F346A-4F85-DE3A-960A-1CBFF73E8613";
	setAttr -s 5 ".lnk";
	setAttr -s 5 ".slnk";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".hwi" yes;
	setAttr -av ".ta";
	setAttr -av ".tq";
	setAttr -av ".etmr";
	setAttr -av ".tmr";
	setAttr -av ".aoon";
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -k on ".hff";
	setAttr -av -k on ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av -k on ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av -k on ".hfa";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".blen";
	setAttr -k on ".blat";
	setAttr -av ".msaa" yes;
	setAttr ".aasc" 4;
	setAttr ".laa" yes;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 7 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :lightList1;
	setAttr -s 3 ".l";
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :standardSurface1;
	setAttr ".b" 0.80000001192092896;
	setAttr ".bc" -type "float3" 1 1 1 ;
	setAttr ".s" 0.20000000298023224;
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".macc";
	setAttr -av -k on ".macd";
	setAttr -av -k on ".macq";
	setAttr -av -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -av -k on ".clip";
	setAttr -av -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -av ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -av -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf" 51;
	setAttr -av -cb on ".imfkey" -type "string" "exr";
	setAttr -av -k on ".gama";
	setAttr -k on ".exrc";
	setAttr -k on ".expt";
	setAttr -av -k on ".an";
	setAttr -cb on ".ar";
	setAttr -av -k on ".fs";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -av -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -k on ".ep";
	setAttr -av -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -av -k on ".pff";
	setAttr -av -cb on ".peie";
	setAttr -av -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -av -k on ".comp";
	setAttr -av -k on ".cth";
	setAttr -av -k on ".soll";
	setAttr -cb on ".sosl";
	setAttr -av -k on ".rd";
	setAttr -av -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -av -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -av -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -av -k on ".itf";
	setAttr -av -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -av -k on ".uf";
	setAttr -av -k on ".oi";
	setAttr -av -k on ".rut";
	setAttr -av -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -av -k on ".mbso";
	setAttr -av -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -av -k on ".pfb";
	setAttr -av -k on ".pram";
	setAttr -av -k on ".poam";
	setAttr -av -k on ".prlm";
	setAttr -av -k on ".polm";
	setAttr -av -cb on ".prm";
	setAttr -av -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -av -k on ".ubc";
	setAttr -av -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -av -k on ".udbx";
	setAttr -av -k on ".smc";
	setAttr -av -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -av -k on ".tlwd";
	setAttr -av -k on ".tlht";
	setAttr -av -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -av -k on ".ope";
	setAttr -av -k on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w" 268;
	setAttr -av -k on ".h" 268;
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar" 1;
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultLightSet;
	setAttr -s 3 ".dsm";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya-legacy/config.ocio";
	setAttr ".vtn" -type "string" "sRGB gamma (legacy)";
	setAttr ".vn" -type "string" "sRGB gamma";
	setAttr ".dn" -type "string" "legacy";
	setAttr ".wsn" -type "string" "scene-linear Rec 709/sRGB";
	setAttr ".ote" yes;
	setAttr ".ovt" no;
	setAttr ".povt" no;
	setAttr ".otn" -type "string" "sRGB gamma (legacy)";
	setAttr ".potn" -type "string" "sRGB gamma (legacy)";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -av -k off -cb on ".fbfm";
	setAttr -av -k off -cb on ".ehql";
	setAttr -av -k off -cb on ".eams";
	setAttr -av -k off -cb on ".eeaa";
	setAttr -av -k off -cb on ".engm";
	setAttr -av -k off -cb on ".mes";
	setAttr -av -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -av -k off -cb on ".mbs";
	setAttr -av -k off -cb on ".trm";
	setAttr -av -k off -cb on ".tshc";
	setAttr -av -k off -cb on ".enpt";
	setAttr -av -k off -cb on ".clmt";
	setAttr -av -k off -cb on ".tcov";
	setAttr -av -k off -cb on ".lith";
	setAttr -av -k off -cb on ".sobc";
	setAttr -av -k off -cb on ".cuth";
	setAttr -av -k off -cb on ".hgcd";
	setAttr -av -k off -cb on ".hgci";
	setAttr -av -k off -cb on ".mgcs";
	setAttr -av -k off -cb on ".twa";
	setAttr -av -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "groupId2.id" "Plug_MeshShape.iog.og[1].gid";
connectAttr "Plug_EdgeBorder_set.mwc" "Plug_MeshShape.iog.og[1].gco";
connectAttr "groupId4.id" "Plug_MeshShape.iog.og[3].gid";
connectAttr "Plug_Interior_set.mwc" "Plug_MeshShape.iog.og[3].gco";
connectAttr "groupId5.id" "Plug_MeshShape.iog.og[4].gid";
connectAttr "Plug_AllFaces_set.mwc" "Plug_MeshShape.iog.og[4].gco";
connectAttr "groupId6.id" "Plug_MeshShape.iog.og[5].gid";
connectAttr "Plug_Selection_set.mwc" "Plug_MeshShape.iog.og[5].gco";
connectAttr "groupId7.id" "Plug_MeshShape.iog.og[6].gid";
connectAttr "Plug_ExtraSecure_set.mwc" "Plug_MeshShape.iog.og[6].gco";
connectAttr "groupId2.msg" "Plug_EdgeBorder_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[1]" "Plug_EdgeBorder_set.dsm" -na;
connectAttr "groupId4.msg" "Plug_Interior_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[3]" "Plug_Interior_set.dsm" -na;
connectAttr "groupId5.msg" "Plug_AllFaces_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[4]" "Plug_AllFaces_set.dsm" -na;
connectAttr "groupId6.msg" "Plug_Selection_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[5]" "Plug_Selection_set.dsm" -na;
connectAttr "groupId7.msg" "Plug_ExtraSecure_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[6]" "Plug_ExtraSecure_set.dsm" -na;
connectAttr "PlugIt_Plug_SG.msg" "materialInfo2.sg";
connectAttr "PlugIt_Plug_Shd.msg" "materialInfo2.m";
connectAttr "PlugIt_Plug_Shd.oc" "PlugIt_Plug_SG.ss";
connectAttr "Plug_MeshShape.iog" "PlugIt_Plug_SG.dsm" -na;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PlugIt_Plug_SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PlugIt_Plug_SG.message" ":defaultLightSet.message";
connectAttr "PlugIt_Plug_SG.pa" ":renderPartition.st" -na;
connectAttr "PlugIt_Plug_Shd.msg" ":defaultShaderList1.s" -na;
// End of Plug_Long_08.ma
