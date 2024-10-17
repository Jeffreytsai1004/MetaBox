//Maya ASCII 2023 scene
//Name: Plug_Square_02.ma
//Last modified: Tue, Feb 07, 2023 12:36:46 AM
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
fileInfo "UUID" "6A0AA980-4C1C-E3AD-3AEC-3782E0EBF206";
createNode transform -n "Plug_Mesh";
	rename -uid "3618F2F1-4600-A25F-134E-FBBC80941621";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "2FB5B172-461A-4F25-965D-07A79527B098";
	setAttr -k off ".v";
	setAttr -s 7 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "e[6]" "e[8]" "e[10:11]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[0:68]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[4:68]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 1 "e[0:3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 86 ".uvst[0].uvsp[0:85]" -type "float2" 0 0 0.5 0 1 1 0 1
		 0 0 1 0 1 1 0 1 0.5 0 1 0 1 1 0 1 1 1 0 1 0.91123158 6.8431066e-10 0.088768363 7.024632e-09
		 0 7.7089419e-09 1 0 1 0.91123158 1 0.088768363 1 1 7.7089419e-09 1 0.088768438 1
		 0.91123164 1 6.8480732e-10 0.088832863 7.0246058e-09 0.91122824 0.095442854 1 0 1
		 0 1 0.099848866 1 1.3095553e-15 0.90456706 0 0.90015423 0.10141337 0 0 0 1.0476442e-14
		 0.089221179 1 0.10141337 1 0 0.91077566 0 0.90458798 1 1 1 1 0.90455717 0 0.13415557
		 0 0 0.064130336 0.064130336 0.064130329 0.19487812 0.13414973 0 0.19485494 0.064130329
		 1 0.13414687 1 0 1 0 1 0.12630796 0.86583948 0 0.87369204 0 0.86585027 1 1 1 1 1
		 0.87369204 1 1 0.8658424 1 0.87369204 0 0.86584455 0 1 0 1 0 0.87369204 0.13416049
		 1 0.12630799 1 0.8051191 0.064130314 0.12630796 0 0.09986192 2.0867956e-09 0.90015113
		 1.8810288e-08 1 0.099861942 1 0.90015113 0.90013808 1 0 0.099845648 0 0.12630799
		 0.93586963 0.19489472 0.93586957 0.80512315 0.80514503 0.93586963 0.19488081 0.93586963
		 0.064130299 0.80512178 0.93586963 0.064130306 0.93586963 0.93586963 0.064130306 0.93586963
		 0 0 1 2.0896811e-08 1 1 0 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 80 ".vt[0:79]"  -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773 -1.27663541 6.3360955e-16 -1.070828915
		 -1.21635604 5.9994449e-16 -1.21635604 -1.070829391 5.8599973e-16 -1.27663517 -1.18748224 0.027591756 -0.98167574
		 -1.12720275 0.027591756 -1.12720275 -0.98167574 0.027591756 -1.187482 -0.92919338 0.10114128 -1.13499939
		 -1.074720383 0.10114128 -1.074720144 -1.13499892 0.10114128 -0.92919338 -1.18748224 0.027591756 0.99507171
		 -1.12340868 0.027591756 1.13112652 -0.96872169 0.027591739 1.187482 -1.13499892 0.10114128 0.92919338
		 -1.074720383 0.10114128 1.074720144 -0.92919338 0.10114127 1.13499939 -1.070829391 -2.0064268e-08 1.27663517
		 -1.21635604 1.1080737e-15 1.21635604 -1.27663541 1.0747243e-15 1.070828915 0.99507183 0.027591549 1.18748176
		 1.13112664 0.027591554 1.12340832 1.18748224 0.027591554 0.96872127 0.92919338 0.1011411 1.13499904
		 1.074720383 0.10114107 1.074719787 1.13499892 0.1011411 0.9291929 1.27663541 -2.2885712e-07 1.070828676
		 1.21635604 -2.3716792e-07 1.21635568 1.070829391 -2.2885712e-07 1.27663481 1.18748224 0.02759173 -0.98167574
		 1.12720275 0.027591756 -1.12720275 0.98167574 0.027591756 -1.187482 1.13499892 0.10114127 -0.92919338
		 1.074720383 0.10114128 -1.074720144 0.92919338 0.10114128 -1.13499939 1.070829391 5.86e-16 -1.27663517
		 1.21635604 5.9965062e-16 -1.21635604 1.27663541 -2.0064324e-08 -1.070828915 -0.6389218 0.96408886 0.84472799
		 -0.78444856 0.96408886 0.7844488 -0.84472799 0.96408886 0.63892198 -0.54976863 0.99168032 0.75557482
		 -0.7555747 0.99168032 0.54976869 -0.69529557 0.99168032 0.69529557 0.755575 0.9916805 0.54976863
		 0.54976881 0.9916805 0.75557482 0.69529575 0.9916805 0.69529557 0.6389221 0.96408838 0.84472793
		 0.7844488 0.9640885 0.78444862 0.84472823 0.96408838 0.6389218 -0.69140422 0.89053941 0.89721066
		 -0.83693147 0.89053941 0.83693147 -0.89721066 0.89053941 0.69140446 0.8972109 0.89053935 0.6914044
		 0.83693159 0.89053935 0.83693123 0.69140446 0.89053935 0.89721054 0.54976869 0.99168032 -0.75557482
		 0.755575 0.99168032 -0.54976851 0.69529569 0.99168032 -0.69529545 0.84472823 0.96408886 -0.6389218
		 0.78444862 0.96408886 -0.78444862 0.6389218 0.96408886 -0.84472793 0.69140446 0.89053941 -0.89721054
		 0.83693153 0.89053941 -0.83693123 0.89721078 0.89053941 -0.6914044 -0.54976869 0.99168032 -0.75557482
		 -0.69529557 0.99168032 -0.69529557 -0.75557482 0.99168032 -0.54976863 -0.6389218 0.96408886 -0.84472793
		 -0.78444862 0.96408886 -0.7844488 -0.84472805 0.96408886 -0.6389218 -0.89721072 0.89053941 -0.69140446
		 -0.83693147 0.89053941 -0.83693129 -0.6914044 0.89053941 -0.8972106;
	setAttr -s 148 ".ed[0:147]"  0 2 0 0 1 0 1 3 0 2 3 0 0 4 1 2 5 1 4 5 0
		 1 6 1 4 6 0 3 7 1 6 7 0 5 7 0 8 25 1 23 34 1 32 43 1 41 10 1 48 73 1 51 47 1 63 50 1
		 71 62 1 10 9 1 13 10 1 9 8 1 8 11 1 13 12 1 12 15 1 15 14 1 14 13 1 12 11 1 11 16 1
		 16 15 1 79 14 1 16 77 1 21 20 1 20 17 1 19 22 1 22 21 1 19 18 1 18 24 1 24 23 1 23 19 1
		 18 17 1 17 25 1 25 24 1 58 20 1 22 56 1 30 29 1 29 26 1 28 31 1 31 30 1 28 27 1 27 33 1
		 33 32 1 32 28 1 27 26 1 26 34 1 34 33 1 61 29 1 31 59 1 39 38 1 38 35 1 37 40 1 40 39 1
		 37 36 1 36 42 1 42 41 1 41 37 1 36 35 1 35 43 1 43 42 1 70 38 1 40 68 1 57 56 1 56 44 1
		 46 58 1 58 57 1 46 45 1 45 49 1 49 48 1 48 46 1 45 44 1 44 47 1 47 49 1 50 52 1 55 50 1
		 52 51 1 51 53 1 55 54 1 54 60 1 60 59 1 59 55 1 54 53 1 53 61 1 61 60 1 62 64 1 67 62 1
		 64 63 1 63 65 1 67 66 1 66 69 1 69 68 1 68 67 1 66 65 1 65 70 1 70 69 1 73 72 1 76 73 1
		 72 71 1 71 74 1 76 75 1 75 78 1 78 77 1 77 76 1 75 74 1 74 79 1 79 78 1 44 53 1 56 61 1
		 22 29 1 31 38 1 70 59 1 40 14 1 79 68 1 16 20 1 58 77 1 17 11 1 19 26 1 28 35 1 37 13 1
		 55 65 1 67 74 1 46 76 1 9 12 1 18 21 1 27 30 1 36 39 1 45 57 1 52 54 1 21 57 1 30 60 1
		 64 66 1 39 69 1 72 75 1 15 78 1 2 9 0 3 42 0 0 24 0 1 33 0;
	setAttr -s 69 -ch 292 ".fc[0:68]" -type "polyFaces" 
		f 4 0 5 -7 -5
		mu 0 4 0 1 2 3
		f 4 -2 4 8 -8
		mu 0 4 4 5 6 7
		f 4 -3 7 10 -10
		mu 0 4 8 9 10 11
		f 4 3 9 -12 -6
		mu 0 4 1 8 12 13
		f 6 -57 -14 -40 -147 1 147
		mu 0 6 17 14 15 16 5 4
		f 6 -70 -15 -53 -148 2 145
		mu 0 6 20 18 19 17 9 8
		f 4 24 25 26 27
		mu 0 4 26 27 28 29
		f 4 28 29 30 -26
		mu 0 4 27 30 31 28
		f 4 37 38 39 40
		mu 0 4 32 33 16 15
		f 4 41 42 43 -39
		mu 0 4 33 34 24 16
		f 4 50 51 52 53
		mu 0 4 35 36 17 19
		f 4 54 55 56 -52
		mu 0 4 36 37 14 17
		f 4 63 64 65 66
		mu 0 4 38 39 20 23
		f 4 67 68 69 -65
		mu 0 4 39 40 18 20
		f 4 76 77 78 79
		mu 0 4 41 42 43 44
		f 4 80 81 82 -78
		mu 0 4 42 45 46 43
		f 4 87 88 89 90
		mu 0 4 47 48 49 50
		f 4 91 92 93 -89
		mu 0 4 48 51 52 49
		f 4 98 99 100 101
		mu 0 4 53 54 55 56
		f 4 102 103 104 -100
		mu 0 4 54 57 58 55
		f 4 109 110 111 112
		mu 0 4 59 60 61 62
		f 4 113 114 115 -111
		mu 0 4 60 63 64 61
		f 4 -82 116 -87 17
		mu 0 4 46 45 51 65
		f 4 -74 117 -93 -117
		mu 0 4 45 66 52 51
		f 4 118 -58 -118 -46
		mu 0 4 67 68 52 66
		f 4 119 -71 120 -59
		mu 0 4 69 70 58 50
		f 4 121 -32 122 -72
		mu 0 4 71 29 64 56
		f 4 123 -45 124 -33
		mu 0 4 31 72 73 62
		f 4 -43 125 -24 12
		mu 0 4 24 34 30 25
		f 4 -35 -124 -30 -126
		mu 0 4 34 72 31 30
		f 4 -36 126 -48 -119
		mu 0 4 67 32 37 68
		f 4 -41 13 -56 -127
		mu 0 4 32 15 14 37
		f 4 -49 127 -61 -120
		mu 0 4 69 35 40 70
		f 4 -54 14 -69 -128
		mu 0 4 35 19 18 40
		f 4 -62 128 -28 -122
		mu 0 4 71 38 26 29
		f 4 -67 15 -22 -129
		mu 0 4 38 23 22 26
		f 4 -85 129 -98 18
		mu 0 4 74 47 57 75
		f 4 -91 -121 -104 -130
		mu 0 4 47 50 58 57
		f 4 -96 130 -109 19
		mu 0 4 76 53 63 77
		f 4 -102 -123 -115 -131
		mu 0 4 53 56 64 63
		f 4 -75 131 -113 -125
		mu 0 4 73 41 59 62
		f 4 -80 16 -107 -132
		mu 0 4 41 44 78 59
		f 12 -79 -83 -18 -86 -84 -19 -97 -95 -20 -108 -106 -17
		mu 0 12 44 43 46 65 79 74 75 80 76 77 81 78
		f 4 20 132 -25 21
		mu 0 4 22 21 27 26
		f 4 22 23 -29 -133
		mu 0 4 21 25 30 27
		f 4 -42 133 33 34
		mu 0 4 34 33 82 72
		f 4 -38 35 36 -134
		mu 0 4 33 32 67 82
		f 4 -55 134 46 47
		mu 0 4 37 36 83 68
		f 4 -51 48 49 -135
		mu 0 4 36 35 69 83
		f 4 -68 135 59 60
		mu 0 4 40 39 84 70
		f 4 -64 61 62 -136
		mu 0 4 39 38 71 84
		f 4 -81 136 72 73
		mu 0 4 45 42 85 66
		f 4 -77 74 75 -137
		mu 0 4 42 41 73 85
		f 4 83 137 -88 84
		mu 0 4 74 79 48 47
		f 4 85 86 -92 -138
		mu 0 4 79 65 51 48
		f 4 -34 138 -76 44
		mu 0 4 72 82 85 73
		f 4 -37 45 -73 -139
		mu 0 4 82 67 66 85
		f 4 -47 139 -94 57
		mu 0 4 68 83 49 52
		f 4 -50 58 -90 -140
		mu 0 4 83 69 50 49
		f 4 94 140 -99 95
		mu 0 4 76 80 54 53
		f 4 96 97 -103 -141
		mu 0 4 80 75 57 54
		f 4 -60 141 -105 70
		mu 0 4 70 84 55 58
		f 4 -63 71 -101 -142
		mu 0 4 84 71 56 55
		f 4 105 142 -110 106
		mu 0 4 78 81 60 59
		f 4 107 108 -114 -143
		mu 0 4 81 77 63 60
		f 4 -27 143 -116 31
		mu 0 4 29 28 61 64
		f 4 -31 32 -112 -144
		mu 0 4 28 31 62 61
		f 6 -146 -4 144 -21 -16 -66
		mu 0 6 20 8 1 21 22 23
		f 6 -145 -1 146 -44 -13 -23
		mu 0 6 21 1 0 16 24 25;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 2 
		1 0 
		8 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".db" yes;
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
	rename -uid "BBE481FC-4A2E-6B76-FD4F-3FB7F857F66C";
createNode groupId -n "groupId1";
	rename -uid "034D3C65-47ED-2955-A1CF-FD8E7C552B1A";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "E82598EA-4DE0-F064-2CCF-CAAA0313426E";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "7A5DA188-497B-E8EA-07FA-CFA8C8493A98";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "3C7CAFC9-4F5E-5540-7774-23976234CCC7";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "CDFF0480-460A-F1E1-B1F6-F6AB497F6471";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "B746CA77-44BD-B903-863E-8DB7462F2E91";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "5D0066C4-47C5-4175-2B89-2F9CCB2E3F7B";
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
	rename -uid "2AED7B80-4A86-FC8F-81B4-338FCB438817";
	setAttr -s 6 ".lnk";
	setAttr -s 6 ".slnk";
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
	setAttr -s 6 ".st";
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
connectAttr "groupId1.id" "Plug_MeshShape.iog.og[0].gid";
connectAttr "Plug_EdgeBorder_set.mwc" "Plug_MeshShape.iog.og[0].gco";
connectAttr "groupId4.id" "Plug_MeshShape.iog.og[3].gid";
connectAttr "Plug_AllFaces_set.mwc" "Plug_MeshShape.iog.og[3].gco";
connectAttr "groupId5.id" "Plug_MeshShape.iog.og[4].gid";
connectAttr "Plug_Selection_set.mwc" "Plug_MeshShape.iog.og[4].gco";
connectAttr "groupId6.id" "Plug_MeshShape.iog.og[5].gid";
connectAttr "Plug_ExtraSecure_set.mwc" "Plug_MeshShape.iog.og[5].gco";
connectAttr "groupId1.msg" "Plug_EdgeBorder_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[0]" "Plug_EdgeBorder_set.dsm" -na;
connectAttr "groupId4.msg" "Plug_AllFaces_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[3]" "Plug_AllFaces_set.dsm" -na;
connectAttr "groupId5.msg" "Plug_Selection_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[4]" "Plug_Selection_set.dsm" -na;
connectAttr "groupId6.msg" "Plug_ExtraSecure_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[5]" "Plug_ExtraSecure_set.dsm" -na;
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
// End of Plug_Square_02.ma
