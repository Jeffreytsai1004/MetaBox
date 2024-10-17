//Maya ASCII 2023 scene
//Name: Plug_Long_01.ma
//Last modified: Tue, Feb 07, 2023 01:09:40 PM
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
fileInfo "UUID" "7A752B66-47D5-6B8D-1455-9BA63B151E1D";
createNode transform -n "Plug_Mesh";
	rename -uid "468BFAA2-487A-E57F-DC21-7AB286151DB9";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "45D68668-4DC3-F2FD-3CE8-F39BAD6A1D3E";
	setAttr -k off ".v";
	setAttr -s 9 ".iog[0].og";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 3 "e[138]" "e[140]" "e[142:143]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "e[132:135]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 1 "f[0:68]";
	setAttr ".iog[0].og[6].gcl" -type "componentList" 1 "f[0:64]";
	setAttr ".iog[0].og[7].gcl" -type "componentList" 1 "e[132:135]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 86 ".uvst[0].uvsp[0:85]" -type "float2" 0.5782001 0.81487691
		 0.59552705 0.81022382 0.60356116 0.79909301 0.59429431 0.79509783 0.59723365 0.79654348
		 0.59062064 0.80625355 0.58820903 0.80426788 0.57517469 0.81029034 0.5735445 0.80807102
		 0.56143177 0.79000032 0.56887186 0.78445077 0.56649792 0.78866434 0.57855034 0.79594159
		 0.58397555 0.78702664 0.56549203 0.79964089 0.57908404 0.7858448 0.57459319 0.79341531
		 0.5638938 0.79643178 0.40447295 0.81022382 0.42179996 0.81487691 0.39643884 0.79909301
		 0.40570569 0.79509783 0.41179103 0.80426788 0.40937936 0.80625355 0.40276641 0.79654348
		 0.42482531 0.81029034 0.42645544 0.80807102 0.43856817 0.79000032 0.43350208 0.78866434
		 0.43112814 0.78445077 0.41602445 0.78702664 0.42144966 0.79594159 0.43450797 0.79964089
		 0.42540675 0.79341531 0.42091596 0.7858448 0.4361062 0.79643178 0.59552705 0.1897763
		 0.5782001 0.18512309 0.60356116 0.20090699 0.59429431 0.20490205 0.58820903 0.19573212
		 0.59062064 0.19374645 0.59723365 0.20345652 0.57517469 0.18970972 0.5735445 0.19192904
		 0.56143177 0.20999968 0.56649792 0.21133572 0.56887186 0.21554935 0.58397555 0.21297336
		 0.57855034 0.20405847 0.56549203 0.20035917 0.57459319 0.20658463 0.57908404 0.2141552
		 0.5638938 0.20356822 0.42179996 0.18512309 0.40447295 0.1897763 0.39643884 0.20090699
		 0.40570569 0.20490205 0.40276641 0.20345652 0.40937936 0.19374645 0.41179103 0.19573212
		 0.42482531 0.18970972 0.42645544 0.19192904 0.43856817 0.20999968 0.43112814 0.21554935
		 0.43350208 0.21133572 0.42144966 0.20405847 0.41602445 0.21297336 0.43450797 0.20035917
		 0.42091596 0.2141552 0.42540675 0.20658463 0.4361062 0.20356822 0.5 0 0.5 0 1 1 0
		 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 0 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 80 ".vt[0:79]"  -1.44590747 0.056364711 -0.42832944 -1.46926403 0.024157016 -0.44939274
		 -1.49736834 0 -0.48566046 -1.52488434 0.056675121 -0.33407435 -1.55301476 0.025113588 -0.34730759
		 -1.5936234 0.0030903425 -0.36644629 -1.50248563 0.056728285 -0.40104339 -1.52937078 0.024889678 -0.41917434
		 -1.56626391 0.0022558304 -0.44825432 -1.22551203 0.45558742 -0.25302452 -1.23515117 0.44255 -0.29124486
		 -1.24647152 0.41002658 -0.31135687 -1.25753248 0.45558742 -0.22569089 -1.29606247 0.4427422 -0.23523107
		 -1.31919885 0.41049835 -0.24275014 -1.24982381 0.45558742 -0.24430299 -1.27885723 0.44278315 -0.27470672
		 -1.29838467 0.41056648 -0.29139808 -1.44590747 0.056364711 0.42832986 -1.46926403 0.024157016 0.44939321
		 -1.49736834 0 0.48566046 -1.52488434 0.056675121 0.33407474 -1.55301476 0.025113588 0.34730792
		 -1.5936234 0.0030903425 0.36644644 -1.50248563 0.056728285 0.40104336 -1.52937078 0.024889678 0.41917443
		 -1.56626391 0.0022558304 0.44825512 -1.22551203 0.45558742 0.25302488 -1.23515117 0.44255 0.29124513
		 -1.24647152 0.41002658 0.31135708 -1.25753248 0.45558742 0.22569114 -1.29606247 0.4427422 0.23523118
		 -1.31919885 0.41049835 0.24275047 -1.24982381 0.45558742 0.24430346 -1.27885723 0.44278315 0.27470708
		 -1.29838467 0.41056648 0.29139832 1.44590724 0.056364711 -0.42832944 1.46926439 0.024157016 -0.44939274
		 1.49736857 0 -0.48566046 1.52488434 0.056675121 -0.33407435 1.55301499 0.025113588 -0.34730759
		 1.5936234 0.0030903425 -0.36644629 1.50248599 0.056728285 -0.40104339 1.52937126 0.024889678 -0.41917434
		 1.56626356 0.0022558304 -0.44825432 1.22551179 0.45558742 -0.25302452 1.23515141 0.44255 -0.29124486
		 1.24647152 0.41002658 -0.31135687 1.25753272 0.45558742 -0.22569089 1.29606271 0.4427422 -0.23523107
		 1.3191992 0.41049835 -0.24275014 1.24982405 0.45558742 -0.24430299 1.27885735 0.44278315 -0.27470672
		 1.29838514 0.41056648 -0.29139808 1.44590724 0.056364711 0.42832986 1.46926439 0.024157016 0.44939321
		 1.49736857 0 0.48566046 1.52488434 0.056675121 0.33407474 1.55301499 0.025113588 0.34730792
		 1.5936234 0.0030903425 0.36644644 1.50248599 0.056728285 0.40104336 1.52937126 0.024889678 0.41917443
		 1.56626356 0.0022558304 0.44825512 1.22551179 0.45558742 0.25302488 1.23515141 0.44255 0.29124513
		 1.24647152 0.41002658 0.31135708 1.25753272 0.45558742 0.22569114 1.29606271 0.4427422 0.23523118
		 1.3191992 0.41049835 0.24275047 1.24982405 0.45558742 0.24430346 1.27885735 0.44278315 0.27470708
		 1.29838514 0.41056648 0.29139832 -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773;
	setAttr -s 148 ".ed[0:147]"  1 0 1 2 1 1 7 6 1 6 0 1 2 8 1 8 7 1 5 4 1
		 8 5 1 4 3 1 3 6 1 1 7 1 4 7 1 10 9 1 11 10 1 16 15 1 15 9 1 11 17 1 17 16 1 14 13 1
		 17 14 1 13 12 1 12 15 1 0 11 1 14 3 1 6 17 1 10 16 1 13 16 1 19 18 1 20 19 1 25 24 1
		 24 18 1 20 26 1 26 25 1 3 21 1 23 22 1 26 23 1 22 21 1 21 24 1 19 25 1 4 22 1 22 25 1
		 28 27 1 29 28 1 34 33 1 33 27 1 29 35 1 35 34 1 12 30 1 32 31 1 35 32 1 31 30 1 30 33 1
		 18 29 1 32 21 1 24 35 1 28 34 1 13 31 1 31 34 1 32 14 1 23 5 1 37 36 1 38 37 1 43 42 1
		 42 36 1 38 44 1 44 43 1 41 40 1 44 41 1 40 39 1 39 42 1 37 43 1 40 43 1 46 45 1 47 46 1
		 52 51 1 51 45 1 47 53 1 53 52 1 66 48 1 50 49 1 53 50 1 49 48 1 48 51 1 36 47 1 50 39 1
		 42 53 1 46 52 1 49 52 1 2 38 1 55 54 1 56 55 1 61 60 1 60 54 1 56 62 1 62 61 1 59 41 1
		 59 58 1 62 59 1 58 57 1 57 60 1 55 61 1 58 61 1 64 63 1 65 64 1 70 69 1 69 63 1 65 71 1
		 71 70 1 68 50 1 68 67 1 71 68 1 67 66 1 66 69 1 54 65 1 68 57 1 60 71 1 64 70 1 67 70 1
		 49 67 1 39 57 1 40 58 1 63 27 1 37 1 1 36 0 1 46 10 1 54 18 1 45 9 1 20 56 1 19 55 1
		 29 65 1 28 64 1 11 47 1 72 74 0 72 73 0 73 75 0 74 75 0 72 76 1 74 77 1 76 77 0 73 78 1
		 76 78 0 75 79 1 78 79 0 77 79 0 8 74 0 26 72 0 44 75 0 62 73 0;
	setAttr -s 69 -ch 292 ".fc[0:68]" -type "polyFaces" 
		f 4 -1 10 2 3
		mu 0 4 3 4 5 6
		f 4 -2 4 5 -11
		mu 0 4 4 2 1 5
		f 4 -7 -60 34 -40
		mu 0 4 7 0 19 25
		f 4 -9 39 36 -34
		mu 0 4 8 7 25 26
		f 4 6 11 -6 7
		mu 0 4 0 7 5 1
		f 4 8 9 -3 -12
		mu 0 4 7 8 6 5
		f 4 23 33 -54 58
		mu 0 4 14 8 26 32
		f 4 -4 24 -17 -23
		mu 0 4 3 6 12 13
		f 4 -10 -24 -20 -25
		mu 0 4 6 8 14 12
		f 4 -13 25 14 15
		mu 0 4 10 15 16 11
		f 4 -14 16 17 -26
		mu 0 4 15 13 12 16
		f 4 -19 -59 48 -57
		mu 0 4 17 14 32 35
		f 4 -21 56 50 -48
		mu 0 4 9 17 35 27
		f 4 18 26 -18 19
		mu 0 4 14 17 16 12
		f 4 20 21 -15 -27
		mu 0 4 17 9 11 16
		f 6 35 59 -8 144 -133 -146
		mu 0 6 18 19 0 1 73 72
		f 4 -31 -30 -39 27
		mu 0 4 21 22 23 24
		f 4 38 -33 -32 28
		mu 0 4 24 23 18 20
		f 4 -36 32 -41 -35
		mu 0 4 19 18 23 25
		f 4 40 29 -38 -37
		mu 0 4 25 23 22 26
		f 4 52 45 -55 30
		mu 0 4 21 30 31 22
		f 4 54 49 53 37
		mu 0 4 22 31 32 26
		f 4 -45 -44 -56 41
		mu 0 4 29 28 33 34
		f 4 55 -47 -46 42
		mu 0 4 34 33 31 30
		f 4 -50 46 -58 -49
		mu 0 4 32 31 33 35
		f 4 57 43 -52 -51
		mu 0 4 35 33 28 27
		f 4 127 90 -129 -29
		mu 0 4 20 56 58 24
		f 4 128 89 125 -28
		mu 0 4 24 58 57 21
		f 4 113 -130 -53 -126
		mu 0 4 57 67 30 21
		f 4 129 103 -131 -43
		mu 0 4 30 67 69 34
		f 4 130 102 121 -42
		mu 0 4 34 69 64 29
		f 4 -64 -63 -71 60
		mu 0 4 39 40 41 42
		f 4 70 -66 -65 61
		mu 0 4 42 41 36 38
		f 4 -68 65 -72 -67
		mu 0 4 37 36 41 43
		f 4 71 62 -70 -69
		mu 0 4 43 41 40 44
		f 4 83 76 -86 63
		mu 0 4 39 48 49 40
		f 4 85 80 84 69
		mu 0 4 40 49 50 44
		f 4 -76 -75 -87 72
		mu 0 4 47 46 51 52
		f 4 86 -78 -77 73
		mu 0 4 52 51 49 48
		f 4 -81 77 -88 -80
		mu 0 4 50 49 51 53
		f 4 87 74 -83 -82
		mu 0 4 53 51 46 45
		f 4 -62 -89 1 -123
		mu 0 4 42 38 2 4
		f 4 -61 122 0 -124
		mu 0 4 39 42 4 3
		f 4 131 -84 123 22
		mu 0 4 13 48 39 3
		f 4 -74 -132 13 -125
		mu 0 4 52 48 13 15
		f 4 -127 -73 124 12
		mu 0 4 10 47 52 15
		f 6 -5 88 64 146 -136 -145
		mu 0 6 1 2 38 36 83 73
		f 4 -90 100 91 92
		mu 0 4 57 58 59 60
		f 4 -91 93 94 -101
		mu 0 4 58 56 55 59
		f 4 120 -97 95 66
		mu 0 4 43 61 54 37
		f 4 119 -99 -121 68
		mu 0 4 44 62 61 43
		f 4 96 101 -95 97
		mu 0 4 54 61 59 55
		f 4 98 99 -92 -102
		mu 0 4 61 62 60 59
		f 4 -109 114 -120 -85
		mu 0 4 50 68 62 44
		f 4 -93 115 -107 -114
		mu 0 4 57 60 66 67
		f 4 -100 -115 -111 -116
		mu 0 4 60 62 68 66
		f 4 -103 116 104 105
		mu 0 4 64 69 70 65
		f 4 -104 106 107 -117
		mu 0 4 69 67 66 70
		f 4 118 -110 108 79
		mu 0 4 53 71 68 50
		f 4 -112 -119 81 -79
		mu 0 4 63 71 53 45
		f 4 109 117 -108 110
		mu 0 4 68 71 70 66
		f 4 111 112 -105 -118
		mu 0 4 71 63 65 70
		f 6 67 -96 -98 147 134 -147
		mu 0 6 36 37 54 55 80 79
		f 12 -106 -113 78 82 75 126 -16 -22 47 51 44 -122
		mu 0 12 64 65 63 45 46 47 10 11 9 27 28 29
		f 6 -94 -128 31 145 133 -148
		mu 0 6 55 56 20 18 72 76
		f 4 132 137 -139 -137
		mu 0 4 72 73 74 75
		f 4 -134 136 140 -140
		mu 0 4 76 72 77 78
		f 4 -135 139 142 -142
		mu 0 4 79 80 81 82
		f 4 135 141 -144 -138
		mu 0 4 73 83 84 85;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
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
	rename -uid "6792C4CD-4B41-AB73-520E-309B19B3867B";
createNode groupId -n "groupId2";
	rename -uid "55DA8A13-474F-B8F5-645B-C2AA7F13D232";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "9B548C6E-4E9C-FA8D-3ADF-A3ADA2A4B0A6";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Interior_set";
	rename -uid "2C0B072E-442C-8565-E227-4BB0BF221F33";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId5";
	rename -uid "9D3187EC-48D9-3743-0C46-5599E4AEC6BE";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "EA8C78B7-4564-8FCC-C62E-E19F10B3AC6D";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "774555EF-4C4F-AB89-418C-F5B101018D18";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "C00EE882-4429-A0BE-99B0-CC9A1E914C53";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "AB44C731-43C8-5C0E-C150-35A7545469CB";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "A85CE5D4-4285-81CF-6732-C1A74493B008";
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
	rename -uid "36BFFFBE-412F-CC2E-1DDE-14BC02C9D292";
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
connectAttr "groupId2.id" "Plug_MeshShape.iog.og[2].gid";
connectAttr "Plug_EdgeBorder_set.mwc" "Plug_MeshShape.iog.og[2].gco";
connectAttr "groupId4.id" "Plug_MeshShape.iog.og[4].gid";
connectAttr "Plug_Interior_set.mwc" "Plug_MeshShape.iog.og[4].gco";
connectAttr "groupId5.id" "Plug_MeshShape.iog.og[5].gid";
connectAttr "Plug_AllFaces_set.mwc" "Plug_MeshShape.iog.og[5].gco";
connectAttr "groupId6.id" "Plug_MeshShape.iog.og[6].gid";
connectAttr "Plug_Selection_set.mwc" "Plug_MeshShape.iog.og[6].gco";
connectAttr "groupId7.id" "Plug_MeshShape.iog.og[7].gid";
connectAttr "Plug_ExtraSecure_set.mwc" "Plug_MeshShape.iog.og[7].gco";
connectAttr "groupId2.msg" "Plug_EdgeBorder_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[2]" "Plug_EdgeBorder_set.dsm" -na;
connectAttr "groupId4.msg" "Plug_Interior_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[4]" "Plug_Interior_set.dsm" -na;
connectAttr "groupId5.msg" "Plug_AllFaces_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[5]" "Plug_AllFaces_set.dsm" -na;
connectAttr "groupId6.msg" "Plug_Selection_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[6]" "Plug_Selection_set.dsm" -na;
connectAttr "groupId7.msg" "Plug_ExtraSecure_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[7]" "Plug_ExtraSecure_set.dsm" -na;
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
// End of Plug_Long_01.ma
