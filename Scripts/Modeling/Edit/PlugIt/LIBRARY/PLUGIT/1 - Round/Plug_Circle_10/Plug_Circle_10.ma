//Maya ASCII 2023 scene
//Name: Plug_Circle_10.ma
//Last modified: Sat, Feb 04, 2023 03:45:40 PM
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
fileInfo "UUID" "3EE63C59-4C52-79EF-C2D2-0E897456D850";
createNode transform -n "Plug_Mesh";
	rename -uid "C1381A8C-4750-575E-E063-22B695CE810A";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "8CAAFF86-4899-C1E5-F557-C686568FC835";
	setAttr -k off ".v";
	setAttr -s 8 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "e[6]" "e[8]" "e[10:11]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "map[0:1]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[0:93]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 1 "f[4:93]";
	setAttr ".iog[0].og[6].gcl" -type "componentList" 1 "e[0:3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 110 ".uvst[0].uvsp[0:109]" -type "float2" 0.5 0 0.5 0 1 1 0
		 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 0 1 0 0.037089907 0.0084742326 0.016948555
		 0.0083871 0.016700802 0 0.036686543 0.01854495 0 0.018544948 0 0 0.080582775 0 0.96291012
		 0 0.93973786 0.019893698 0.014255499 0.47760975 1.7556114e-05 0.48145503 0 0.50000006
		 0 0.50000006 0 0.48165673 0 0.51854497 0 0.51834327 0 0.52239037 7.6289011e-06 0.98010647
		 0.0061949193 0.98145503 0 0.99152553 0.016948801 0.99167103 0.016658066 0.98165673
		 0 1 0.037089899 1 0.036686543 1 0.06026122 1 0.91941911 1 0.96291012 0.99152559 0.98305112
		 0.99167097 0.98334199 1 0.96331346 0.98145509 1 0.98165673 1 0.98010647 0.98574489
		 0.52239007 0.99998242 0.51854497 1 0.018544948 1 0.0084743993 0.98305106 0.0083288625
		 0.98334229 0.018343262 1 0 0.96331346 0.019893605 0.99380481 0.48145503 1 0.47760972
		 0.99999237 0.50000006 1 0.49996325 1 0.51834327 1 0.48145506 1 0.012442735 0.047469892
		 0.012440103 0.96497893 0.024760479 0.049521219 0.024760544 0.9752394 0.02389624 0.024861597
		 0.48867202 0.012515158 0.5 0.024760485 0.51132935 0.012515085 0.9762314 0.024803732
		 0.9752394 0.049521234 0.51132989 0.98755687 0.97623134 0.9875595 0.50000006 0.9752394
		 0.9752394 0.9752394 0.4885743 0.98752928 0.023767956 0.98755956 0.98756033 0.047460936
		 0.98756033 0.96497875 0.021306001 0.028713141 0.47367141 0 0.52632856 0 0.97869414
		 0.012478689 0.9983604 0.026253369 0.5 0 0.0016396416 0.055417601 1 0.083943486 1
		 0.8751753 0 0.91605657 0 0.12482484 0.9786942 0.97128654 0.52632856 1 0.47367141
		 1 0.021305859 0.98752153 0 0 0.5 0 1 0 1 1 0.9983604 0.94458246 0 1 0.0016396306
		 0.97374666 0.5 1 0.5 1 0 0 0.5 0 0.5 1 0 1 1 0 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 104 ".vt[0:103]"  -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773 -1.40007389 -0.1091873 0.80833304
		 -1.41412771 -0.1091873 0.75588316 -1.43463898 -0.048141718 0.75588316 -1.37193358 -0.048141718 0.86449212
		 -1.361678 -0.1091873 0.84672898 5.8308309e-08 -0.1091873 1.61666596 -0.052449796 -0.1091873 1.60261202
		 -0.062705368 -0.048141718 1.62037504 0.06270548 -0.048141718 1.62037504 0.052449908 -0.1091873 1.60261202
		 1.40007389 -0.1091873 0.80833286 1.361678 -0.1091873 0.8467288 1.37193358 -0.048141718 0.864492
		 1.43463898 -0.048141718 0.75588298 1.41412771 -0.1091873 0.75588298 1.40007365 -0.1091873 -0.80833316
		 1.41412771 -0.1091873 -0.75588334 1.43463886 -0.048141718 -0.75588334 1.37193346 -0.048141718 -0.86449224
		 1.36167777 -0.1091873 -0.8467291 -1.40007365 -0.1091873 -0.80833304 -1.36167777 -0.1091873 -0.84672898
		 -1.37193346 -0.048141718 -0.86449218 -1.43463886 -0.048141718 -0.75588316 -1.41412771 -0.1091873 -0.75588316
		 8.42563e-08 -0.1091873 -1.61666608 0.052449938 -0.1091873 -1.60261214 0.062705509 -0.048141718 -1.62037528
		 -0.062705338 -0.048141718 -1.62037528 -0.05244977 -0.1091873 -1.60261214 -1.39205551 -1.042066932 0.75873697
		 -1.41412771 -0.98122591 0.75654179 -1.40007448 -0.98074895 0.80851007 -1.361678 -0.98028708 0.84672898
		 -1.35280406 -1.041756153 0.82640481 -1.34409845 -1.066618681 0.77601552 0.038942222 -1.042066932 1.58492374
		 5.131416e-08 -1.066618681 1.55203104 -0.03894211 -1.042066932 1.58492374 -0.051879417 -0.98122591 1.60294127
		 5.0297277e-08 -0.98123455 1.61684239 0.051879529 -0.98122591 1.60294127 0.038942255 -1.042066932 -1.58492386
		 0.051879562 -0.98122591 -1.60294151 -0.00015293006 -0.98074895 -1.61675525 -0.05244977 -0.98028708 -1.60261214
		 -0.0392855 -1.041756153 -1.58476508 8.4823014e-08 -1.066618681 -1.55203116 -1.39205539 -1.042066932 -0.75873697
		 -1.34409833 -1.066618681 -0.77601558 -1.35311317 -1.042066932 -0.8261869 -1.3622483 -0.98122591 -0.84639966
		 -1.40022659 -0.98123455 -0.80842131 -1.41412771 -0.98122591 -0.75654179 1.39205551 -1.042066932 0.75873679
		 1.34409845 -1.066618681 0.7760154 1.35311329 -1.042066932 0.82618666 1.36224842 -0.98122591 0.84639955
		 1.40022671 -0.98122591 0.80842108 1.41412771 -0.98122591 0.75654167 1.35311317 -1.042066932 -0.82618695
		 1.34409833 -1.066618681 -0.77601564 1.39205539 -1.042066932 -0.75873709 1.41412771 -0.98122591 -0.75654191
		 1.40022659 -0.98122591 -0.80842143 1.3622483 -0.98122591 -0.84639984 -1.4841572 -0.022855639 0.75588316
		 -1.46072102 -0.022855639 0.84334767 -1.39669263 -0.022855639 0.90737617 -0.087464496 -0.022855639 1.66325915
		 5.8662092e-08 -0.022855639 1.68669522 0.087464601 -0.022855639 1.66325915 1.39669263 -0.022855639 0.90737605
		 1.46072102 -0.022855639 0.84334749 1.4841572 -0.022855639 0.75588298 1.48415697 -0.022855639 -0.75588334
		 1.4607209 -0.022855639 -0.84334785 1.39669251 -0.022855639 -0.90737629 -1.39669251 -0.022855639 -0.90737617
		 -1.4607209 -0.022855639 -0.84334767 -1.48415697 -0.022855639 -0.75588316 0.087464638 -0.022855639 -1.66325939
		 8.4349125e-08 -0.022855639 -1.68669534 -0.087464467 -0.022855639 -1.66325939 -1.41783714 -0.048141718 0.81858861
		 5.869013e-08 -0.048141718 1.63717711 1.41783714 -0.048141718 0.81858838 1.41783702 -0.048141718 -0.81858873
		 -1.41783702 -0.048141718 -0.81858861 8.422677e-08 -0.048141718 -1.63717723 -1.38811886 -1.030775905 0.80159235
		 1.7525021e-07 -1.030998945 1.60300004 -0.00013982103 -1.030775905 -1.60294235 -1.38823891 -1.030998945 -0.80150008
		 1.38823903 -1.030995369 0.80150002 1.38823903 -1.030995369 -0.80150038;
	setAttr -s 197 ".ed";
	setAttr ".ed[0:165]"  0 2 0 0 1 0 1 3 0 2 3 0 0 4 1 2 5 1 4 5 0 1 6 1 4 6 0
		 3 7 1 6 7 0 5 7 0 9 8 1 8 40 1 40 39 1 39 9 1 8 12 1 12 41 1 41 40 1 10 31 1 10 9 1
		 9 32 1 32 31 1 12 11 1 11 15 1 15 14 1 14 12 1 14 13 1 13 48 1 48 47 1 47 14 1 13 17 1
		 17 49 1 49 48 1 17 16 1 16 20 1 20 19 1 19 17 1 19 18 1 18 66 1 66 65 1 65 19 1 18 22 1
		 22 67 1 67 66 1 22 21 1 21 25 1 25 24 1 24 22 1 24 23 1 23 72 1 72 71 1 71 24 1 23 27 1
		 27 73 1 73 72 1 27 26 1 26 35 1 35 34 1 34 27 1 29 28 1 28 60 1 60 59 1 59 29 1 28 32 1
		 32 61 1 61 60 1 30 36 1 30 29 1 29 37 1 37 36 1 34 33 1 33 52 1 52 51 1 51 34 1 33 37 1
		 37 53 1 53 52 1 39 38 1 38 56 1 56 61 1 61 39 1 38 43 1 43 57 1 57 56 1 43 42 1 42 46 1
		 46 45 1 45 43 1 42 41 1 41 47 1 47 46 1 45 44 1 44 64 1 64 63 1 63 45 1 44 49 1 49 65 1
		 65 64 1 51 50 1 50 68 1 68 73 1 73 51 1 50 55 1 55 69 1 69 68 1 55 54 1 54 58 1 58 57 1
		 57 55 1 54 53 1 53 59 1 59 58 1 63 62 1 62 70 1 70 69 1 69 63 1 62 67 1 67 71 1 71 70 1
		 45 55 1 74 10 1 76 77 1 11 76 1 76 75 1 75 74 1 77 15 1 79 80 1 16 79 1 79 78 1 78 77 1
		 80 20 1 82 83 1 21 82 1 82 81 1 81 80 1 83 25 1 85 89 1 26 85 1 85 84 1 84 83 1 86 30 1
		 88 74 1 31 88 1 88 87 1 87 86 1 89 35 1 91 86 1 36 91 1 91 90 1 90 89 1 8 92 1 92 11 1
		 10 92 1 75 92 1 13 93 1 93 16 1 15 93 1 78 93 1 18 94 1 94 21 1 20 94 1 81 94 1 23 95 1
		 95 26 1 25 95 1;
	setAttr ".ed[166:196]" 84 95 1 28 96 1 96 31 1 30 96 1 87 96 1 33 97 1 97 36 1
		 35 97 1 90 97 1 38 98 1 98 42 1 40 98 1 44 99 1 99 48 1 46 99 1 50 100 1 100 54 1
		 52 100 1 56 101 1 101 60 1 58 101 1 62 102 1 102 66 1 64 102 1 68 103 1 103 72 1
		 70 103 1 0 75 0 2 87 0 1 81 0 3 84 0;
	setAttr -s 94 -ch 390 ".fc[0:93]" -type "polyFaces" 
		f 4 0 5 -7 -5
		mu 0 4 0 1 2 3
		f 4 -2 4 8 -8
		mu 0 4 4 0 5 6
		f 4 -3 7 10 -10
		mu 0 4 7 8 9 10
		f 4 3 9 -12 -6
		mu 0 4 1 11 12 13
		f 4 12 13 14 15
		mu 0 4 14 15 16 17
		f 4 16 17 18 -14
		mu 0 4 15 18 19 16
		f 4 20 21 22 -20
		mu 0 4 20 14 21 22
		f 4 23 24 25 26
		mu 0 4 18 23 24 25
		f 4 27 28 29 30
		mu 0 4 25 26 27 28
		f 4 31 32 33 -29
		mu 0 4 26 29 30 27
		f 4 34 35 36 37
		mu 0 4 29 31 32 33
		f 4 38 39 40 41
		mu 0 4 33 34 35 36
		f 4 42 43 44 -40
		mu 0 4 34 37 38 35
		f 4 45 46 47 48
		mu 0 4 37 39 40 41
		f 4 49 50 51 52
		mu 0 4 41 42 43 44
		f 4 53 54 55 -51
		mu 0 4 42 45 46 43
		f 4 56 57 58 59
		mu 0 4 45 47 48 49
		f 4 60 61 62 63
		mu 0 4 50 51 52 53
		f 4 64 65 66 -62
		mu 0 4 51 21 54 52
		f 4 68 69 70 -68
		mu 0 4 55 50 56 57
		f 4 71 72 73 74
		mu 0 4 49 58 59 60
		f 4 75 76 77 -73
		mu 0 4 58 56 61 59
		f 4 78 79 80 81
		mu 0 4 17 62 63 54
		f 4 82 83 84 -80
		mu 0 4 62 64 65 63
		f 4 85 86 87 88
		mu 0 4 64 66 67 68
		f 4 89 90 91 -87
		mu 0 4 66 19 28 67
		f 4 92 93 94 95
		mu 0 4 68 69 70 71
		f 4 96 97 98 -94
		mu 0 4 69 30 36 70
		f 4 99 100 101 102
		mu 0 4 60 72 73 46
		f 4 103 104 105 -101
		mu 0 4 72 74 75 73
		f 4 106 107 108 109
		mu 0 4 74 76 77 65
		f 4 110 111 112 -108
		mu 0 4 76 61 53 77
		f 4 113 114 115 116
		mu 0 4 71 78 79 75
		f 4 117 118 119 -115
		mu 0 4 78 38 44 79
		f 4 -89 120 -110 -84
		mu 0 4 64 68 74 65
		f 4 -121 -96 -117 -105
		mu 0 4 74 68 71 75
		f 4 -27 -31 -91 -18
		mu 0 4 18 25 28 19
		f 4 -70 -64 -112 -77
		mu 0 4 56 50 53 61
		f 4 -22 -16 -82 -66
		mu 0 4 21 14 17 54
		f 4 -38 -42 -98 -33
		mu 0 4 29 33 36 30
		f 4 -49 -53 -119 -44
		mu 0 4 37 41 44 38
		f 4 -60 -75 -103 -55
		mu 0 4 45 49 60 46
		f 4 123 122 126 -25
		mu 0 4 23 80 81 24
		f 4 128 127 131 -36
		mu 0 4 31 82 83 32
		f 9 135 -128 129 130 -123 124 -194 1 195
		mu 0 9 84 83 82 85 81 80 86 0 4
		f 4 133 132 136 -47
		mu 0 4 39 87 88 40
		f 4 19 143 142 121
		mu 0 4 20 22 89 90
		f 4 138 137 146 -58
		mu 0 4 47 91 92 48
		f 4 67 148 147 141
		mu 0 4 55 57 93 94
		f 4 -24 -17 151 152
		mu 0 4 23 18 15 95
		f 4 -13 -21 153 -152
		mu 0 4 15 14 20 95
		f 4 -122 -126 154 -154
		mu 0 4 20 90 86 95
		f 4 -125 -124 -153 -155
		mu 0 4 86 80 23 95
		f 4 -35 -32 155 156
		mu 0 4 31 29 26 96
		f 4 -28 -26 157 -156
		mu 0 4 26 25 24 96
		f 4 -127 -131 158 -158
		mu 0 4 24 81 85 96
		f 4 -130 -129 -157 -159
		mu 0 4 85 82 31 96
		f 4 -46 -43 159 160
		mu 0 4 39 37 34 97
		f 4 -39 -37 161 -160
		mu 0 4 34 33 32 97
		f 4 -132 -136 162 -162
		mu 0 4 32 83 84 97
		f 4 -135 -134 -161 -163
		mu 0 4 84 87 39 97
		f 4 -57 -54 163 164
		mu 0 4 47 45 42 98
		f 4 -50 -48 165 -164
		mu 0 4 42 41 40 98
		f 4 -137 -141 166 -166
		mu 0 4 40 88 99 98
		f 4 -140 -139 -165 -167
		mu 0 4 99 91 47 98
		f 4 -23 -65 167 168
		mu 0 4 22 21 51 100
		f 4 -61 -69 169 -168
		mu 0 4 51 50 55 100
		f 4 -142 -146 170 -170
		mu 0 4 55 94 101 100
		f 4 -145 -144 -169 -171
		mu 0 4 101 89 22 100
		f 4 -71 -76 171 172
		mu 0 4 57 56 58 102
		f 4 -72 -59 173 -172
		mu 0 4 58 49 48 102
		f 4 -147 -151 174 -174
		mu 0 4 48 92 103 102
		f 4 -150 -149 -173 -175
		mu 0 4 103 93 57 102
		f 4 -86 -83 175 176
		mu 0 4 66 64 62 104
		f 4 -79 -15 177 -176
		mu 0 4 62 17 16 104
		f 4 -19 -90 -177 -178
		mu 0 4 16 19 66 104
		f 4 -34 -97 178 179
		mu 0 4 27 30 69 105
		f 4 -93 -88 180 -179
		mu 0 4 69 68 67 105
		f 4 -92 -30 -180 -181
		mu 0 4 67 28 27 105
		f 4 -107 -104 181 182
		mu 0 4 76 74 72 106
		f 4 -100 -74 183 -182
		mu 0 4 72 60 59 106
		f 4 -78 -111 -183 -184
		mu 0 4 59 61 76 106
		f 4 -67 -81 184 185
		mu 0 4 52 54 63 107
		f 4 -85 -109 186 -185
		mu 0 4 63 65 77 107
		f 4 -113 -63 -186 -187
		mu 0 4 77 53 52 107
		f 4 -45 -118 187 188
		mu 0 4 35 38 78 108
		f 4 -114 -95 189 -188
		mu 0 4 78 71 70 108
		f 4 -99 -41 -189 -190
		mu 0 4 70 36 35 108
		f 4 -56 -102 190 191
		mu 0 4 43 46 73 109
		f 4 -106 -116 192 -191
		mu 0 4 73 75 79 109
		f 4 -120 -52 -192 -193
		mu 0 4 79 44 43 109
		f 6 140 -133 134 -196 2 196
		mu 0 6 99 88 87 84 8 7
		f 6 -195 -1 193 125 -143 144
		mu 0 6 101 1 0 86 90 89
		f 9 -197 -4 194 145 -148 149 150 -138 139
		mu 0 9 99 11 1 101 94 93 103 92 91;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 2 
		0 0 
		1 0 ;
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
createNode transform -n "PlugIt_PlugCountNumber_18";
	rename -uid "71DD5DFD-4455-C4F9-FACF-FA8CC7A3ABCF";
createNode groupId -n "groupId1";
	rename -uid "B065D6F5-41E9-2FB3-9C8E-FBA7ECE5AFC4";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "C116D837-4271-E895-985B-6A9E62F00790";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Hole_set";
	rename -uid "C288407C-402B-BD01-11F3-2ABC809C6DBC";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "3EFF5113-4119-4A0C-ED63-D7B9D306530F";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "1885B011-41A6-0D79-69E1-83B3F2A490D7";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "1066E37B-4534-A350-4020-618959FDF680";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "973342B3-4255-BDB5-3F95-04845BBD473A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "FA95C6FF-45CC-811C-B4C0-F18CC56842CD";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "74E7E75E-4171-9445-3E95-01B5F86ACC30";
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
	rename -uid "F5B13A06-4C6E-99E7-E89B-309F5AD7D00E";
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
connectAttr "groupId1.id" "Plug_MeshShape.iog.og[0].gid";
connectAttr "Plug_EdgeBorder_set.mwc" "Plug_MeshShape.iog.og[0].gco";
connectAttr "groupId4.id" "Plug_MeshShape.iog.og[3].gid";
connectAttr "Plug_Hole_set.mwc" "Plug_MeshShape.iog.og[3].gco";
connectAttr "groupId5.id" "Plug_MeshShape.iog.og[4].gid";
connectAttr "Plug_AllFaces_set.mwc" "Plug_MeshShape.iog.og[4].gco";
connectAttr "groupId6.id" "Plug_MeshShape.iog.og[5].gid";
connectAttr "Plug_Selection_set.mwc" "Plug_MeshShape.iog.og[5].gco";
connectAttr "groupId7.id" "Plug_MeshShape.iog.og[6].gid";
connectAttr "Plug_ExtraSecure_set.mwc" "Plug_MeshShape.iog.og[6].gco";
connectAttr "groupId1.msg" "Plug_EdgeBorder_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[0]" "Plug_EdgeBorder_set.dsm" -na;
connectAttr "groupId4.msg" "Plug_Hole_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[3]" "Plug_Hole_set.dsm" -na;
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
// End of Plug_Circle_10.ma
