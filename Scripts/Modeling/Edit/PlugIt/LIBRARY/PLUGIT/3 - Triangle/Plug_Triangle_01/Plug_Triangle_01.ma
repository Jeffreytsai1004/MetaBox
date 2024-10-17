//Maya ASCII 2023 scene
//Name: Plug_Triangle_01.ma
//Last modified: Wed, Feb 08, 2023 12:41:37 PM
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
fileInfo "UUID" "6D8DE313-47DA-BC73-7188-88850FEBF86F";
createNode transform -n "Plug_Mesh";
	rename -uid "CAF1BE1E-439F-6F2E-D24A-4485614BA967";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "407BB833-4B23-C4AF-3A8B-7BBDA5D00488";
	setAttr -k off ".v";
	setAttr -s 7 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "e[6]" "e[8]" "e[10:11]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[0:123]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[4:123]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 1 "e[0:3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.46797329187393188 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 143 ".uvst[0].uvsp[0:142]" -type "float2" 0.5 0 0.5 0 1 1 0
		 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 0 1 0.40215349 0.10790253 0.052307963 0.71385288
		 0.03777492 0.76809072 0.053353965 0.82623243 0.5 0.052618623 0.44185829 0.068197608
		 0.59784651 0.10790253 0.55814171 0.068197608 0.5 0.88332784 0.67492282 0.88332796
		 0.84984565 0.88332796 0.90408349 0.86879492 0.94664598 0.82623243 0.09591645 0.86879492
		 0.15015429 0.88332796 0.32507718 0.88332796 0.96222508 0.76809072 0.94769204 0.71385288
		 0.081240535 0.72583711 0.077686608 0.72436512 0.42394668 0.12462497 0.4269985 0.12696671
		 0.070729017 0.72148311 0.41797209 0.12004054 0.45793033 0.096034884 0.45595706 0.092617035
		 0.5 0.080815792 0.5 0.084762335 0.45209122 0.085921288 0.5 0.073084235 0.88801169
		 0.84095752 0.88998497 0.84437537 0.84626007 0.85609317 0.84575796 0.85227942 0.8938508
		 0.85107112 0.84724307 0.8635596 0.54206967 0.096034884 0.54404294 0.092617035 0.57605326
		 0.12462497 0.5730015 0.12696671 0.54790878 0.085921288 0.58202791 0.12004054 0.32637846
		 0.8635596 0.5 0.8635596 0.058240533 0.76809072 0.071077645 0.81599951 0.10614926
		 0.85107112 0.15275693 0.8635596 0.67362154 0.8635596 0.92927098 0.72148311 0.94175947
		 0.76809072 0.92892241 0.81599951 0.06597209 0.76809072 0.069918752 0.76809072 0.077773392
		 0.81213379 0.081191242 0.8101604 0.11001503 0.84437537 0.11198831 0.84095752 0.15373993
		 0.85609317 0.15424204 0.85227942 0.32686996 0.85609341 0.5 0.85609376 0.32712102
		 0.85227942 0.5 0.85227942 0.91875947 0.72583711 0.92231345 0.72436512 0.93402791
		 0.76809072 0.93008125 0.76809072 0.92222667 0.81213379 0.9188087 0.8101604 0.67313004
		 0.85609341 0.67287898 0.85227942 0.5 0.42560655 0.5 0.41540021 0.51309311 0.41753155
		 0.50798798 0.42658603 0.5 0.40622073 0.5157094 0.40901691 0.48429054 0.40901691 0.48698324
		 0.41763425 0.47276986 0.42634809 0.46873367 0.41907233 0.49226272 0.42692351 0.48077321
		 0.43324733 0.20056432 0.786111 0.20316589 0.78108752 0.35065043 0.78116536 0.35020059
		 0.78634405 0.20480037 0.77486992 0.34883219 0.77496994 0.5 0.78626752 0.5 0.78112447
		 0.64934957 0.78116536 0.64979947 0.78634405 0.5 0.77485538 0.65116787 0.77496994
		 0.79947329 0.78616476 0.7968365 0.78105867 0.81696141 0.77759075 0.82135081 0.78201258
		 0.7951715 0.77470183 0.81239557 0.77194512 0.8388617 0.7622999 0.83057022 0.76281667
		 0.82464278 0.74962032 0.83319712 0.74720395 0.81984115 0.76486468 0.81314445 0.75320864
		 0.17864919 0.78201258 0.33673507 0.7478236 0.5 0.74677813 0.81866407 0.76709902 0.66326499
		 0.7478236 0.51887727 0.43345845 0.16640705 0.77367616 0.16130561 0.76228929 0.16680288
		 0.74720395 0.53126633 0.41907233 0.83359289 0.77367616 0.18685549 0.75320864 0.18760437
		 0.77194512 0.18133599 0.76709902 0.17986143 0.76479185 0.17535722 0.74962032 0.18303859
		 0.77759075 0.17292988 0.77083611 0.16939372 0.76279354 0.5271256 0.42641127 0.82707012
		 0.77083611;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 137 ".vt[0:136]"  -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773 1.15492928 -8.2967862e-16 1.23561382
		 0.32301602 -8.2967862e-16 -1.32426178 1.47794497 -8.2967862e-16 0.67613363 1.52592194 -8.2967862e-16 0.85518694
		 1.47449172 -8.2967862e-16 1.047127008 1.33398211 -8.2967862e-16 1.18763661 1.8452586e-16 -8.2967862e-16 -1.50676811
		 0.19194047 -8.2967862e-16 -1.45533752 -1.5131905e-16 -8.2967862e-16 1.23561382 -9.6113742e-17 0.57480264 0.78482842
		 -1.15492928 -8.2967862e-16 1.23561382 -0.32301602 -8.2967862e-16 -1.32426178 -1.47794497 -8.2967857e-16 0.67613363
		 -1.52592194 -8.2967862e-16 0.85518694 -1.47449172 -8.2967862e-16 1.047127008 -1.33398211 -8.2967862e-16 1.18763661
		 -0.19194047 -8.2967862e-16 -1.45533752 1.41713214 -8.2967862e-16 0.70132321 1.39416349 0.0090259081 0.71083713
		 1.38243115 0.031696294 0.71569687 1.45835984 -8.2967862e-16 0.85518694 1.43283582 0.009019535 0.85518694
		 1.41980708 0.03169629 0.85518694 1.41598117 -8.2967862e-16 1.013345599 1.39387679 0.0090195201 1.00058376789
		 1.38259363 0.031696305 0.9940694 1.30020106 -8.2967862e-16 1.12912607 1.28743899 0.0090195211 1.10702157
		 1.2809248 0.031696301 1.09573853 1.14633727 -8.2967862e-16 1.17035365 1.14309216 0.0090259127 1.14570522
		 1.14143467 0.031696301 1.13311458 0.15815894 -8.2967862e-16 -1.3968271 0.14539701 0.009019536 -1.37472284
		 0.13888267 0.031696301 -1.36343968 1.7153054e-16 0.031696301 -1.40065324 1.731261e-16 0.0090195378 -1.41368198
		 1.7625187e-16 -8.2967862e-16 -1.43920577 0.27079499 -8.2967862e-16 -1.28419113 0.25107124 0.0090259043 -1.26905644
		 0.24099641 0.031696305 -1.26132572 -1.4332699e-16 -8.2967862e-16 1.17035365 -1.4030861e-16 0.0090279561 1.14570689
		 -1.3876651e-16 0.031696301 1.13311458 -1.41713214 -8.2967862e-16 0.70132321 -1.39416349 0.0090259081 0.71083713
		 -1.38243115 0.031696294 0.71569687 -1.45835984 -8.2967857e-16 0.85518694 -1.43283582 0.009019535 0.85518694
		 -1.41980708 0.03169629 0.85518694 -1.41598117 -8.2967862e-16 1.013345599 -1.39387679 0.0090195211 1.00058376789
		 -1.38259363 0.031696301 0.9940694 -1.30020106 -8.2967862e-16 1.12912607 -1.28743899 0.0090195257 1.10702157
		 -1.2809248 0.03169629 1.09573853 -1.14143467 0.031696301 1.13311458 -1.14309216 0.0090259127 1.14570522
		 -1.14633727 -8.2967862e-16 1.17035365 -0.15815894 -8.2967862e-16 -1.3968271 -0.14539701 0.009019536 -1.37472284
		 -0.13888267 0.031696301 -1.36343968 -0.24099641 0.031696305 -1.26132572 -0.25107124 0.0090259043 -1.26905644
		 -0.27079499 -8.2967862e-16 -1.28419113 0.57746464 -8.2967862e-16 1.23561382 0.57316864 -8.2967862e-16 1.17035365
		 0.57154608 0.0090269381 1.14570594 0.57071733 0.031696301 1.13311458 0.53897887 0.57138056 0.78827983
		 -0.57746464 -8.2967862e-16 1.23561382 -0.57316864 -8.2967862e-16 1.17035365 -0.57154608 0.0090269381 1.14570594
		 -0.57071733 0.031696301 1.13311458 -0.53897887 0.57138056 0.78827983 4.1569194e-17 1.62073672 -0.3394379
		 2.2256334e-10 1.63831437 -0.30913407 7.2508449e-10 1.62600064 -0.27544039 -0.026370473 1.62279463 -0.27220675
		 -0.043223795 1.63192463 -0.30209804 -0.05186085 1.61290729 -0.33020699 0.025542796 1.62169051 -0.2710928
		 0.042971626 1.63158798 -0.30175894 0.051860858 1.61290729 -0.33020699 0.10321803 1.58253574 -0.29701149
		 0.089893639 1.60416722 -0.27299228 0.06347245 1.60099196 -0.25021613 0.97452873 0.48285815 0.8775664
		 0.97992456 0.45939001 0.89809233 0.98851281 0.43368718 0.91467625 0.49452579 0.43227124 0.91544545
		 0.49304083 0.458933 0.89834952 0.49904329 0.4825308 0.87789667 1.031297088 0.49243093 0.86791116
		 1.04636991 0.47037303 0.88654852 1.060860515 0.44524825 0.90114617 1.051990628 0.50829232 0.8519128
		 1.07974112 0.49083072 0.86424977 1.10127473 0.466272 0.8736254 1.05685854 0.51584375 0.84429622
		 1.091415048 0.51354802 0.83769923 1.1181159 0.49207965 0.83603448 1.03376925 0.55375528 0.80605721
		 1.071727753 0.55307955 0.79421109 1.099967957 0.52919298 0.78623414 -1.0746501e-16 0.48290551 0.87751853
		 -1.0999953e-16 0.45916542 0.89821446 -1.1207876e-16 0.43273658 0.9151926 -0.49452579 0.43227124 0.91544545
		 -0.49304083 0.458933 0.89834952 -0.49904329 0.4825308 0.87789667 -0.10321803 1.58253574 -0.29701149
		 -0.08954826 1.60396039 -0.27278373 -0.062318489 1.60030091 -0.24951926 -0.97443569 0.48340812 0.87701178
		 -0.97993237 0.45944625 0.89799732 -0.98863709 0.43336082 0.91485351 -1.060860515 0.44524825 0.90114617
		 -1.04636991 0.47037303 0.88654852 -1.031297088 0.49243093 0.86791116 -1.10127473 0.466272 0.8736254
		 -1.07974112 0.49083072 0.86424977 -1.051990628 0.50829232 0.8519128 -1.055876374 0.51560533 0.84453654
		 -1.091296077 0.51324928 0.83777553 -1.11866808 0.49123713 0.83606952 -1.099967957 0.52919298 0.78623414
		 -1.071727753 0.55307955 0.79421109 -1.03376925 0.55375528 0.80605721;
	setAttr -s 260 ".ed";
	setAttr ".ed[0:165]"  0 2 0 0 1 0 1 3 0 2 3 0 0 4 1 2 5 1 4 5 0 1 6 1 4 6 0
		 3 7 1 6 7 0 5 7 0 10 11 1 11 12 1 12 13 1 13 8 1 14 15 1 15 9 1 9 10 1 16 73 1 20 19 1
		 20 21 1 21 22 1 22 23 1 23 18 1 14 24 1 24 19 1 16 78 1 29 28 1 28 25 1 27 30 1 30 29 1
		 27 26 1 26 25 1 25 46 1 48 27 1 32 31 1 31 28 1 30 33 1 33 32 1 35 34 1 34 31 1 33 36 1
		 36 35 1 38 37 1 37 34 1 36 39 1 39 38 1 50 49 1 49 74 1 39 76 1 51 50 1 47 46 1 46 40 1
		 42 48 1 48 47 1 42 41 1 41 44 1 44 43 1 43 42 1 41 40 1 40 45 1 45 44 1 69 43 1 45 67 1
		 66 79 1 51 81 1 54 70 1 54 53 1 57 54 1 53 52 1 52 55 1 72 52 1 57 56 1 60 57 1 56 55 1
		 55 58 1 60 59 1 63 60 1 59 58 1 58 61 1 63 62 1 62 65 1 65 64 1 64 63 1 62 61 1 61 66 1
		 66 65 1 69 68 1 68 71 1 71 70 1 70 69 1 68 67 1 67 72 1 72 71 1 49 16 1 8 37 1 9 46 1
		 28 11 1 10 25 1 31 12 1 34 13 1 40 15 1 14 45 1 17 82 1 66 18 1 72 19 1 52 20 1 21 55 1
		 22 58 1 23 61 1 24 67 1 26 29 1 29 32 1 32 35 1 35 38 1 38 75 1 41 47 1 26 47 1 53 56 1
		 56 59 1 59 62 1 50 80 1 44 68 1 53 71 1 73 8 1 74 37 1 75 50 1 76 51 1 77 17 1 73 74 1
		 74 75 1 75 76 1 78 18 1 79 49 1 80 65 1 81 64 1 78 79 1 79 80 1 80 81 1 91 83 1 85 89 1
		 85 84 1 84 87 1 87 86 1 86 85 1 84 83 1 83 88 1 88 87 1 121 86 1 88 119 1 91 90 1
		 90 93 1 93 92 1 92 91 1 90 89 1 89 94 1 94 93 1 94 110 1 102 101 1 101 95 1 97 103 1
		 103 102 1 97 96 1 96 99 1 99 98 1;
	setAttr ".ed[166:259]" 98 97 1 96 95 1 95 100 1 100 99 1 115 98 1 100 113 1
		 105 104 1 104 101 1 103 106 1 106 105 1 108 107 1 107 104 1 106 109 1 109 108 1 111 110 1
		 110 107 1 109 112 1 112 111 1 112 92 1 115 114 1 114 117 1 117 116 1 116 115 1 114 113 1
		 113 118 1 118 117 1 124 116 1 118 122 1 121 120 1 120 119 1 119 134 1 124 123 1 123 126 1
		 126 125 1 125 124 1 123 122 1 122 127 1 127 126 1 129 128 1 128 125 1 127 130 1 130 129 1
		 133 128 1 130 131 1 133 132 1 132 135 1 135 134 1 134 133 1 132 131 1 131 136 1 136 135 1
		 136 121 1 91 42 1 43 83 1 36 103 1 64 124 1 100 77 1 17 113 1 118 82 1 82 136 1 69 88 1
		 33 106 1 30 109 1 27 112 1 48 92 1 76 98 1 70 119 1 81 116 1 110 77 1 84 90 1 96 102 1
		 102 105 1 105 108 1 108 111 1 111 93 1 99 114 1 87 120 1 117 123 1 126 129 1 129 132 1
		 120 135 1 134 54 1 133 57 1 128 60 1 125 63 1 115 51 1 97 39 1 77 94 1 82 121 1 17 85 1
		 0 22 0 2 19 0 1 12 0 3 9 0;
	setAttr -s 124 -ch 516 ".fc[0:123]" -type "polyFaces" 
		f 4 0 5 -7 -5
		mu 0 4 0 1 2 3
		f 4 -2 4 8 -8
		mu 0 4 4 0 5 6
		f 4 -3 7 10 -10
		mu 0 4 7 8 9 10
		f 4 3 9 -12 -6
		mu 0 4 1 11 12 13
		f 6 -23 -22 20 -258 -1 256
		mu 0 6 26 30 31 20 1 0
		f 4 32 118 -56 35
		mu 0 4 32 33 34 35
		f 4 33 34 -53 -119
		mu 0 4 33 36 37 34
		f 4 56 57 58 59
		mu 0 4 38 39 40 41
		f 4 60 61 62 -58
		mu 0 4 39 42 43 40
		f 4 81 82 83 84
		mu 0 4 44 45 46 47
		f 4 85 86 87 -83
		mu 0 4 45 48 49 46
		f 4 88 89 90 91
		mu 0 4 50 51 52 53
		f 4 92 93 94 -90
		mu 0 4 51 54 55 52
		f 4 130 -50 95 19
		mu 0 4 29 56 57 22
		f 4 -19 97 -35 -100
		mu 0 4 15 14 37 36
		f 4 -30 98 -13 99
		mu 0 4 36 58 16 15
		f 4 -38 100 -14 -99
		mu 0 4 58 59 17 16
		f 4 -42 101 -15 -101
		mu 0 4 59 60 27 17
		f 4 -46 -97 -16 -102
		mu 0 4 60 61 28 27
		f 4 -62 102 -17 103
		mu 0 4 43 42 19 18
		f 4 -54 -98 -18 -103
		mu 0 4 42 37 14 19
		f 4 105 -134 137 -66
		mu 0 4 49 24 23 62
		f 4 -73 106 -21 -108
		mu 0 4 63 55 20 31
		f 4 107 21 108 -72
		mu 0 4 63 31 30 64
		f 4 -109 22 109 -77
		mu 0 4 64 30 26 65
		f 4 -110 23 110 -81
		mu 0 4 65 26 25 48
		f 4 -111 24 -106 -87
		mu 0 4 48 25 24 49
		f 4 -104 25 111 -65
		mu 0 4 43 18 21 54
		f 4 -112 26 -107 -94
		mu 0 4 54 21 20 55
		f 4 -34 112 28 29
		mu 0 4 36 33 66 58
		f 4 -33 30 31 -113
		mu 0 4 33 32 67 66
		f 4 -29 113 36 37
		mu 0 4 58 66 68 59
		f 4 -32 38 39 -114
		mu 0 4 66 67 69 68
		f 4 -37 114 40 41
		mu 0 4 59 68 70 60
		f 4 -40 42 43 -115
		mu 0 4 68 69 71 70
		f 4 -41 115 44 45
		mu 0 4 60 70 72 61
		f 4 -44 46 47 -116
		mu 0 4 70 71 73 72
		f 4 131 127 48 49
		mu 0 4 56 74 75 57
		f 4 132 128 51 -128
		mu 0 4 74 76 77 75
		f 4 -61 117 52 53
		mu 0 4 42 39 34 37
		f 4 -57 54 55 -118
		mu 0 4 39 38 35 34
		f 4 68 119 -74 69
		mu 0 4 78 79 80 81
		f 4 70 71 -76 -120
		mu 0 4 79 63 64 80
		f 4 73 120 -78 74
		mu 0 4 81 80 82 83
		f 4 75 76 -80 -121
		mu 0 4 80 64 65 82
		f 4 77 121 -82 78
		mu 0 4 83 82 45 44
		f 4 79 80 -86 -122
		mu 0 4 82 65 48 45
		f 4 138 135 -88 65
		mu 0 4 62 84 46 49
		f 4 139 136 -84 -136
		mu 0 4 84 85 47 46
		f 4 -59 123 -89 63
		mu 0 4 41 40 51 50
		f 4 -63 64 -93 -124
		mu 0 4 40 43 54 51
		f 4 124 -95 72 -71
		mu 0 4 79 52 55 63
		f 4 -91 -125 -69 67
		mu 0 4 53 52 79 78
		f 4 -127 -131 125 96
		mu 0 4 61 56 29 28
		f 4 -45 116 -132 126
		mu 0 4 61 72 74 56
		f 4 -48 50 -133 -117
		mu 0 4 72 73 76 74
		f 4 -138 -28 -96 -135
		mu 0 4 62 23 22 57
		f 4 -49 122 -139 134
		mu 0 4 57 75 84 62
		f 4 -52 66 -140 -123
		mu 0 4 75 77 85 84
		f 4 142 143 144 145
		mu 0 4 86 87 88 89
		f 4 146 147 148 -144
		mu 0 4 87 90 91 88
		f 4 151 152 153 154
		mu 0 4 92 93 94 95
		f 4 155 156 157 -153
		mu 0 4 93 96 97 94
		f 4 163 164 165 166
		mu 0 4 98 99 100 101
		f 4 167 168 169 -165
		mu 0 4 99 102 103 100
		f 4 185 186 187 188
		mu 0 4 104 105 106 107
		f 4 189 190 191 -187
		mu 0 4 105 108 109 106
		f 4 197 198 199 200
		mu 0 4 110 111 112 113
		f 4 201 202 203 -199
		mu 0 4 111 114 115 112
		f 4 210 211 212 213
		mu 0 4 116 117 118 119
		f 4 214 215 216 -212
		mu 0 4 117 120 121 118
		f 4 -141 218 -60 219
		mu 0 4 90 92 38 41
		f 4 -162 252 -47 220
		mu 0 4 122 98 73 71
		f 4 -201 250 -85 221
		mu 0 4 110 113 44 47
		f 4 222 129 223 -172
		mu 0 4 103 123 124 108
		f 7 -216 -210 -207 -203 -194 224 225
		mu 0 7 121 120 125 115 114 109 126
		f 3 254 -218 -226
		mu 0 3 126 127 121
		f 4 -148 -220 -64 226
		mu 0 4 91 90 41 50
		f 4 -175 -221 -43 227
		mu 0 4 128 122 71 69
		f 4 -179 -228 -39 228
		mu 0 4 129 128 69 67
		f 4 -183 -229 -31 229
		mu 0 4 130 129 67 32
		f 4 -185 -230 -36 230
		mu 0 4 95 130 32 35
		f 4 -219 -155 -231 -55
		mu 0 4 38 92 95 35
		f 4 -171 251 -129 231
		mu 0 4 101 104 77 76
		f 4 -151 -227 -92 232
		mu 0 4 131 91 50 53
		f 4 -193 -222 -137 233
		mu 0 4 107 110 47 85
		f 4 -206 249 -79 -251
		mu 0 4 113 132 83 44
		f 4 -209 248 -75 -250
		mu 0 4 132 116 81 83
		f 4 -214 247 -70 -249
		mu 0 4 116 119 78 81
		f 4 -68 -248 -197 -233
		mu 0 4 53 78 119 131
		f 4 -167 -232 -51 -253
		mu 0 4 98 101 76 73
		f 7 234 -223 -169 -161 -174 -178 -182
		mu 0 7 133 123 103 102 134 135 136
		f 3 -235 -159 -254
		mu 0 3 123 133 97
		f 4 -189 -234 -67 -252
		mu 0 4 104 107 85 77
		f 4 -225 -191 -224 104
		mu 0 4 126 109 108 124
		f 5 255 -146 -150 -255 -105
		mu 0 5 124 86 89 127 126
		f 4 -147 235 -152 140
		mu 0 4 90 87 93 92
		f 4 -143 141 -156 -236
		mu 0 4 87 86 96 93
		f 4 -154 -241 -184 184
		mu 0 4 95 94 137 130
		f 4 -158 158 -181 240
		mu 0 4 94 97 133 137
		f 4 -168 236 159 160
		mu 0 4 102 99 138 134
		f 4 -164 161 162 -237
		mu 0 4 99 98 122 138
		f 4 -160 237 172 173
		mu 0 4 134 138 139 135
		f 4 -163 174 175 -238
		mu 0 4 138 122 128 139
		f 4 -173 238 176 177
		mu 0 4 135 139 140 136
		f 4 -176 178 179 -239
		mu 0 4 139 128 129 140
		f 4 -177 239 180 181
		mu 0 4 136 140 137 133
		f 4 -180 182 183 -240
		mu 0 4 140 129 130 137
		f 4 -166 241 -186 170
		mu 0 4 101 100 105 104
		f 4 -170 171 -190 -242
		mu 0 4 100 103 108 105
		f 4 -145 242 -195 149
		mu 0 4 89 88 141 127
		f 4 -149 150 -196 -243
		mu 0 4 88 91 131 141
		f 4 -188 243 -198 192
		mu 0 4 107 106 111 110
		f 4 -192 193 -202 -244
		mu 0 4 106 109 114 111
		f 4 -200 244 204 205
		mu 0 4 113 112 142 132
		f 4 -204 206 207 -245
		mu 0 4 112 115 125 142
		f 4 -205 245 -211 208
		mu 0 4 132 142 117 116
		f 4 -208 209 -215 -246
		mu 0 4 142 125 120 117
		f 4 -213 -247 195 196
		mu 0 4 119 118 141 131
		f 4 -217 217 194 246
		mu 0 4 118 121 127 141
		f 5 253 -157 -142 -256 -130
		mu 0 5 123 97 96 86 124
		f 11 -257 1 258 14 15 -126 -20 27 133 -25 -24
		mu 0 11 26 0 4 17 27 28 29 22 23 24 25
		f 6 -259 2 259 18 12 13
		mu 0 6 17 8 7 14 15 16
		f 7 -260 -4 257 -27 -26 16 17
		mu 0 7 14 11 1 20 21 18 19;
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
	rename -uid "A3B69928-4DCA-3A5F-D915-D8BCC64471DA";
createNode groupId -n "groupId1";
	rename -uid "83E2E10A-40B4-7877-8176-C497B66F108C";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "4EB35611-438D-4927-794D-5698CADBC36F";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "1B22DC2A-4BCC-F6B3-50B0-369214545430";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "F734814C-4E26-8028-1951-4092980272A7";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "BE386140-44A4-E20F-DFD2-A2AD43809B5A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "1FB0B0D4-4652-D9B9-6722-E6879D0C947D";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "8C7D09CF-4239-5F99-0EE0-AF97D9A57F9A";
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
	rename -uid "CBAFEEB2-4FDA-661A-71C2-579931CE1BB7";
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
// End of Plug_Triangle_01.ma
