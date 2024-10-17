//Maya ASCII 2023 scene
//Name: Plug_Square_04.ma
//Last modified: Tue, Feb 07, 2023 12:38:06 AM
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
fileInfo "UUID" "B2AFAE61-47D6-5B02-698C-31B772FD5057";
createNode transform -n "Plug_Mesh";
	rename -uid "C1B3C1DB-43B6-B29E-F94D-A6902528BA3F";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "8086C1DA-4BE7-1757-0182-0DB314074A3D";
	setAttr -k off ".v";
	setAttr -s 7 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "map[1]" "map[8]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[0:140]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 3 "f[1]" "f[5:137]" "f[140]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 15 "e[4]" "e[6:7]" "e[10:11]" "e[13]" "e[120]" "e[122]" "e[124]" "e[131]" "e[250]" "e[252]" "e[254]" "e[259]" "e[267]" "e[278]" "e[294:295]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 162 ".uvst[0].uvsp[0:161]" -type "float2" 0 0 0.5 0 1 1 0 1
		 0 0 1 0 1 1 0 1 0.5 0 1 0 1 1 0 1 1 1 0 1 4.1127205e-06 0 0 0.99999589 1.541901e-07
		 0.96250504 2.0394864e-06 0.5041008 3.9247825e-06 0.045696564 0 0.035611194 0 0.035611194
		 0.015099123 0.015098882 0.014794881 0.014794652 0.035611764 0 0.035611741 0 0 1 3.101896e-08
		 0.96880865 1.9621411e-06 0.031257927 9.9658007e-07 0.50003326 0 0.49999973 0.13031028
		 1 0.10258456 1 0.04373635 0.98488128 0.053942394 0.98535323 0 0.96438825 0 0.96438825
		 0 0.49999973 0.032828398 0.50090843 0.01602735 0.036863357 0.067828253 0.50169402
		 0.033071939 0.038999189 0.15078177 1 0.14157681 0.98873943 0.089669146 0.98998564
		 0.16120975 0.96387994 0.10258456 0.96438885 0.22002788 0.96651268 0.22002789 0.8724975
		 0.22002789 0.87043959 0.19452721 0.96660316 0.20281459 0.8368057 0.24875316 1 0.25064328
		 1 0.2328504 0.98484623 0.23218602 0.9866786 0.22002788 0.96006906 0.24653238 0.96240306
		 0.24423799 0.89607924 0.22002788 0.88164592 0.22930419 0.96541137 0.22002788 0.87960261
		 0.077910565 0.99999899 0.034695029 0.99999601 0.22002789 0.84177798 0.22002789 0.84177798
		 0.25993779 0.84177798 0.25620532 0.84177798 0.22002789 0.84177798 0.20914681 0.8135891
		 0.25309187 0.87610489 0.22002789 0.84177798 0.25513712 0.84177798 0.24731804 0.80878615
		 0.2698468 0.86823165 0.26100671 0.84177798 0.031259108 0 0 0 0 0 0.033996526 0.018872069
		 0.049629442 0.96495348 0 1 0.24359328 1 0.22002788 1 0.20087066 1 0.24475944 1 0.22002788
		 1 0.24931374 0.98302048 0.039888933 0 0 0.99999589 0.034695029 0.99999601 0.077910565
		 0.99999899 0.13031028 1 0.10258456 1 0.15078177 1 0.20087066 1 0.24475944 1 0.24359328
		 1 0.24875316 1 0.25064328 1 0.24931374 0.98302048 0.24653238 0.96240306 0.24423799
		 0.89607924 0.25309187 0.87610489 0.2698468 0.86823165 0.26100671 0.84177798 0.25993779
		 0.84177798 0.25620532 0.84177798 0.25513712 0.84177798 0.24731804 0.80878615 0.067828253
		 0.50169402 0.033071939 0.038999189 0.033996526 0.018872069 0.035611764 0 0.035611741
		 0 0.031259108 0 0.039888933 0 4.1127205e-06 0 3.9247825e-06 0.045696564 2.0394864e-06
		 0.5041008 1.541901e-07 0.96250504 0 0.035611194 0.014794881 0.014794652 0.015099123
		 0.015098882 0 0.035611194 3.101896e-08 0.96880865 0 1 1.9621411e-06 0.031257927 0
		 0.49999973 9.9658007e-07 0.50003326 0.053942394 0.98535323 0.04373635 0.98488128
		 0 0.96438825 0 0.96438825 0.01602735 0.036863357 0.032828398 0.50090843 0 0.49999973
		 0.089669146 0.98998564 0.14157681 0.98873943 0.10258456 0.96438885 0.16120975 0.96387994
		 0.22002788 0.96651268 0.19452721 0.96660316 0.22002789 0.87043959 0.22002789 0.8724975
		 0.20281459 0.8368057 0.23218602 0.9866786 0.2328504 0.98484623 0.22002788 0.96006906
		 0.22930419 0.96541137 0.22002788 0.88164592 0.22002788 0.87960261 0.22002789 0.84177798
		 0.22002789 0.84177798 0.22002789 0.84177798 0.20914681 0.8135891 0.22002789 0.84177798
		 0 0 0 0 0.049629442 0.96495348 0 1 0.22002788 1 0.22002788 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 156 ".vt[0:155]"  -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773 1.37698698 -0.034424424 1.44844317
		 1.31779134 -0.1175326 1.41884506 1.38924682 -0.1175326 1.38924718 1.4188447 -0.1175326 1.31779158
		 1.44844282 -0.034424424 1.37698734 1.51989841 1.1433455e-07 1.51989877 1.31779134 -0.1175326 -1.41884506
		 1.37698698 -0.034424424 -1.44844317 1.51989841 1.1433455e-07 -1.51989877 1.44844282 -0.034424424 -1.37698734
		 1.4188447 -0.1175326 -1.31779158 1.38919997 -0.1160074 -1.38928223 1.31779134 -0.72095853 1.38924718
		 1.31779134 -0.75538307 1.31779158 1.38924682 -0.72095853 1.31779158 1.4188447 -0.63785034 1.31779158
		 1.38924682 -0.63785034 1.38924718 1.31779134 -0.63785034 1.41884506 1.31779134 -0.72095853 -1.38924718
		 1.31779134 -0.63785034 -1.41884506 1.38924217 -0.63736558 -1.38925076 1.4188447 -0.63785034 -1.31779158
		 1.38923931 -0.72096497 -1.31831491 1.31779134 -0.75538307 -1.31779158 1.1959343 -0.65152627 -1.41884506
		 1.27031338 -0.63895029 -1.41884506 1.27202702 -0.7217167 -1.38788307 1.260041 -0.75538307 -1.3163476
		 1.18393648 -0.77858579 -1.31196046 1.13085032 -0.84168702 -1.30827522 1.11712146 -0.83763325 -1.38413715
		 1.045551419 -0.83308721 -1.41884506 1.10070884 -0.73735392 -1.41884506 1.12155521 -0.66410238 -1.41884506
		 1.001314044 -0.83693171 -0.8123858 1.041378975 -0.77726048 -0.77536637 1.10294819 -0.75538307 -0.7383914
		 0.89946067 -1.58372557 -1.38742197 0.92893618 -1.50586021 -1.41884506 0.99723178 -1.51800346 -1.38322139
		 1.0061696768 -1.53127313 -1.30553353 0.95254791 -1.59498894 -1.30859423 0.87563354 -1.61840963 -1.31215596
		 0.80711412 -1.61840963 -1.018020749 0.86676329 -1.59673262 -0.97818279 0.90596634 -1.53744054 -0.94028395
		 0.94022602 -0.83514243 -0.72628266 0.97396666 -0.77656192 -0.68079263 1.018407106 -0.75538307 -0.62017971
		 0.76582253 -1.61840963 -0.96565276 0.80838716 -1.59726763 -0.90393579 0.84141791 -1.53879631 -0.85808879
		 0.83964562 -0.83619851 -0.69418263 0.86386186 -0.77704698 -0.64362437 0.88131315 -0.75538307 -0.57092899
		 0.70048678 -1.61840963 -0.94943672 0.71735573 -1.59672344 -0.8767277 0.74136841 -1.53754163 -0.82614225
		 1.40651584 -0.049343769 1.40651619 1.4068023 -0.048885792 -1.40445507 1.37611425 -0.70568407 1.37611461
		 1.37608349 -0.70535946 -1.37663972 1.18269694 -0.74344003 -1.39437103 0.95963717 -1.57628846 -1.37054563
		 1.41443241 1.1433455e-07 -1.51989877 1.51989841 1.1433455e-07 -1.40593338 1.51989841 1.1433455e-07 1.38098979
		 1.39865601 1.1433455e-07 1.51989877 -1.37698698 -0.034424424 1.44844317 -1.31779134 -0.1175326 1.41884506
		 -1.38924682 -0.1175326 1.38924718 -1.4188447 -0.1175326 1.31779158 -1.44844282 -0.034424424 1.37698734
		 -1.51989841 1.1433455e-07 1.51989877 -1.31779134 -0.1175326 -1.41884506 -1.37698698 -0.034424424 -1.44844317
		 -1.51989841 1.1433455e-07 -1.51989877 -1.44844282 -0.034424424 -1.37698734 -1.4188447 -0.1175326 -1.31779158
		 -1.38919997 -0.1160074 -1.38928223 -1.31779134 -0.72095853 1.38924718 -1.31779134 -0.75538307 1.31779158
		 -1.38924682 -0.72095853 1.31779158 -1.4188447 -0.63785034 1.31779158 -1.38924682 -0.63785034 1.38924718
		 -1.31779134 -0.63785034 1.41884506 -1.31779134 -0.72095853 -1.38924718 -1.31779134 -0.63785034 -1.41884506
		 -1.38924217 -0.63736558 -1.38925076 -1.4188447 -0.63785034 -1.31779158 -1.38923931 -0.72096497 -1.31831491
		 -1.31779134 -0.75538307 -1.31779158 -1.19593418 -0.65152627 -1.41884506 -1.27031338 -0.63895029 -1.41884506
		 -1.27202713 -0.7217167 -1.38788307 -1.260041 -0.75538307 -1.3163476 -1.18393648 -0.77858579 -1.31196046
		 -1.13085032 -0.84168702 -1.30827522 -1.11712146 -0.83763325 -1.38413715 -1.045551419 -0.83308721 -1.41884506
		 -1.10070884 -0.73735392 -1.41884506 -1.12155521 -0.66410238 -1.41884506 -1.001314044 -0.83693171 -0.8123858
		 -1.041378975 -0.77726048 -0.77536637 -1.10294819 -0.75538307 -0.7383914 -0.89946067 -1.58372557 -1.38742197
		 -0.92893618 -1.50586021 -1.41884506 -0.99723178 -1.51800346 -1.38322139 -1.0061696768 -1.53127313 -1.30553353
		 -0.95254791 -1.59498894 -1.30859423 -0.87563354 -1.61840963 -1.31215596 -0.80711412 -1.61840963 -1.018020749
		 -0.86676329 -1.59673262 -0.97818279 -0.90596634 -1.53744054 -0.94028395 -0.94022602 -0.83514243 -0.72628266
		 -0.97396666 -0.77656192 -0.68079263 -1.018407106 -0.75538307 -0.62017971 -0.76582253 -1.61840963 -0.96565276
		 -0.80838716 -1.59726763 -0.90393579 -0.84141791 -1.53879631 -0.85808879 -0.83964562 -0.83619851 -0.69418263
		 -0.86386186 -0.77704698 -0.64362437 -0.88131315 -0.75538307 -0.57092899 -0.70048678 -1.61840963 -0.94943672
		 -0.71735573 -1.59672344 -0.8767277 -0.74136841 -1.53754163 -0.82614225 -1.40651584 -0.049343769 1.40651619
		 -1.4068023 -0.048885792 -1.40445507 -1.37611425 -0.70568407 1.37611461 -1.37608349 -0.70535946 -1.37663972
		 -1.18269694 -0.74344003 -1.39437103 -0.95963717 -1.57628846 -1.37054563 -1.41443241 1.1433455e-07 -1.51989877
		 -1.51989841 1.1433455e-07 -1.40593338 -1.51989841 1.1433455e-07 1.38098979 -1.39865601 1.1433455e-07 1.51989877
		 1.51989841 1.1433455e-07 -0.012471815 1.44844282 -0.034424424 0 1.4188447 -0.1175326 0
		 1.4188447 -0.63785034 0 1.38924313 -0.72096175 -0.00026158747 1.31779134 -0.75538307 0
		 -1.31779134 -0.75538307 0 -1.38924325 -0.72096175 -0.00026158747 -1.4188447 -0.63785034 0
		 -1.4188447 -0.1175326 0 -1.44844282 -0.034424424 0 -1.51989841 1.1433455e-07 -0.012471815;
	setAttr -s 296 ".ed";
	setAttr ".ed[0:165]"  0 2 0 0 1 0 1 3 0 2 3 0 0 4 1 2 5 1 4 5 0 1 6 1 4 6 0
		 3 7 1 6 7 0 5 7 0 18 146 1 13 74 1 9 8 1 11 10 1 10 24 1 24 23 1 23 11 1 10 9 1 9 25 1
		 25 24 1 12 145 1 12 11 1 18 17 1 15 14 1 14 19 1 19 28 1 28 27 1 27 14 1 19 18 1
		 18 29 1 29 28 1 21 20 1 20 25 1 23 22 1 22 148 1 30 29 1 29 147 1 22 21 1 21 149 1
		 31 30 1 27 26 1 26 34 1 34 33 1 33 27 1 26 31 1 31 35 1 35 34 1 33 32 1 32 41 1 37 36 1
		 36 43 1 43 42 1 42 37 1 36 35 1 35 44 1 44 43 1 39 38 1 38 47 1 47 46 1 46 39 1 38 37 1
		 37 48 1 48 47 1 41 40 1 40 39 1 55 54 1 54 42 1 44 56 1 56 55 1 46 45 1 45 50 1 50 49 1
		 49 52 1 52 51 1 51 50 1 49 48 1 48 53 1 53 52 1 58 57 1 57 51 1 53 59 1 59 58 1 61 60 1
		 60 54 1 56 62 1 62 61 1 64 63 1 63 57 1 59 65 1 65 64 1 65 60 1 42 53 1 54 59 1 43 55 1
		 52 58 1 55 61 1 58 64 1 8 66 1 66 12 1 10 66 1 15 67 1 67 19 1 17 67 1 20 68 1 68 24 1
		 22 68 1 26 69 1 69 30 1 28 69 1 32 70 1 70 40 1 34 70 1 36 70 1 38 70 1 45 71 1 71 49 1
		 47 71 1 16 67 1 72 16 1 15 72 1 73 16 1 73 17 1 74 144 1 74 12 1 75 13 1 8 75 1 13 66 1
		 77 9 1 86 153 1 81 142 1 77 76 1 76 8 1 79 78 1 78 92 1 92 91 1 91 79 1 78 77 1 77 93 1
		 93 92 1 80 154 1 80 79 1 86 85 1 83 82 1 82 87 1 87 96 1 96 95 1 95 82 1 87 86 1
		 86 97 1 97 96 1 89 88 1 88 20 1 88 93 1 93 25 1 91 90 1 90 151 1 98 97 1 97 152 1
		 90 89 1 89 150 1 99 98 1 95 94 1 94 102 1 102 101 1;
	setAttr ".ed[166:295]" 101 95 1 94 99 1 99 103 1 103 102 1 101 100 1 100 109 1
		 105 104 1 104 111 1 111 110 1 110 105 1 104 103 1 103 112 1 112 111 1 107 106 1 106 115 1
		 115 114 1 114 107 1 106 105 1 105 116 1 116 115 1 109 108 1 108 40 1 108 107 1 107 39 1
		 123 122 1 122 110 1 112 124 1 124 123 1 114 113 1 113 45 1 113 118 1 118 50 1 118 117 1
		 117 120 1 120 119 1 119 118 1 117 116 1 116 121 1 121 120 1 126 125 1 125 119 1 121 127 1
		 127 126 1 129 128 1 128 122 1 124 130 1 130 129 1 132 131 1 131 125 1 127 133 1 133 132 1
		 130 62 1 133 65 1 82 14 1 133 128 1 110 121 1 122 127 1 111 123 1 120 126 1 123 129 1
		 126 132 1 129 61 1 132 64 1 76 134 1 134 80 1 78 134 1 83 135 1 135 87 1 85 135 1
		 88 136 1 136 92 1 90 136 1 94 137 1 137 98 1 96 137 1 100 138 1 138 108 1 102 138 1
		 104 138 1 106 138 1 113 139 1 139 117 1 115 139 1 84 135 1 140 84 1 83 140 1 141 84 1
		 141 85 1 142 155 1 142 80 1 143 81 1 76 143 1 81 134 1 72 140 1 15 83 1 41 109 1
		 46 114 1 63 131 1 60 128 1 21 89 1 75 143 1 144 73 1 145 17 1 146 11 1 147 23 1 148 30 1
		 149 31 1 150 99 1 151 98 1 152 91 1 153 79 1 154 85 1 155 141 1 144 145 1 145 146 1
		 146 147 1 147 148 1 148 149 1 149 150 1 150 151 1 151 152 1 152 153 1 153 154 1 154 155 1
		 124 150 1 56 149 1 2 84 0 3 16 0 0 81 0 1 13 0;
	setAttr -s 141 -ch 588 ".fc[0:140]" -type "polyFaces" 
		f 4 0 5 -7 -5
		mu 0 4 0 1 2 3
		f 4 -2 4 8 -8
		mu 0 4 4 5 6 7
		f 4 -3 7 10 -10
		mu 0 4 8 9 10 11
		f 4 3 9 -12 -6
		mu 0 4 1 8 12 13
		f 7 -123 -268 -125 -14 -296 2 293
		mu 0 7 15 16 17 18 14 9 8
		f 4 -19 -18 -17 -16
		mu 0 4 19 20 21 22
		f 4 16 -22 -21 -20
		mu 0 4 22 21 23 24
		f 4 119 -105 -124 122
		mu 0 4 15 25 26 16
		f 4 22 280 269 -24
		mu 0 4 27 28 29 19
		f 4 -30 -29 -28 -27
		mu 0 4 30 31 32 33
		f 4 27 -33 -32 -31
		mu 0 4 33 32 34 35
		f 4 -271 282 -37 -36
		mu 0 4 20 36 37 38
		f 4 36 283 -41 -40
		mu 0 4 38 37 39 40
		f 4 -46 -45 -44 -43
		mu 0 4 31 41 42 43
		f 4 43 -49 -48 -47
		mu 0 4 43 42 44 45
		f 4 -55 -54 -53 -52
		mu 0 4 46 47 48 49
		f 4 52 -58 -57 -56
		mu 0 4 49 48 50 44
		f 4 -62 -61 -60 -59
		mu 0 4 51 52 53 54
		f 4 59 -65 -64 -63
		mu 0 4 54 53 55 46
		f 4 -77 -76 -75 -74
		mu 0 4 56 57 58 59
		f 4 74 -80 -79 -78
		mu 0 4 59 58 60 55
		f 4 102 -120 -121 -122
		mu 0 4 61 25 15 62
		f 4 63 78 -94 54
		mu 0 4 46 55 60 47
		f 4 93 82 -95 68
		mu 0 4 47 60 63 64
		f 4 94 90 92 85
		mu 0 4 64 63 65 66
		f 4 281 270 18 -270
		mu 0 4 29 36 20 19
		f 4 -69 -68 -96 53
		mu 0 4 47 64 67 48
		f 4 95 -71 -70 57
		mu 0 4 48 67 68 50
		f 4 -82 -81 -97 75
		mu 0 4 57 69 70 58
		f 4 96 -84 -83 79
		mu 0 4 58 70 63 60
		f 4 -86 -85 -98 67
		mu 0 4 64 66 71 67
		f 4 97 -88 -87 70
		mu 0 4 67 71 72 68
		f 4 -90 -89 -99 80
		mu 0 4 69 73 74 70
		f 4 98 -92 -91 83
		mu 0 4 70 74 65 63
		f 4 99 -102 19 14
		mu 0 4 75 76 22 24
		f 4 101 100 23 15
		mu 0 4 22 76 27 19
		f 4 -104 -103 25 26
		mu 0 4 33 25 61 30
		f 4 104 103 30 24
		mu 0 4 26 25 33 35
		f 4 -107 -106 34 21
		mu 0 4 21 77 78 23
		f 4 105 -108 39 33
		mu 0 4 78 77 38 40
		f 4 107 106 17 35
		mu 0 4 38 77 21 20
		f 4 -110 -109 46 41
		mu 0 4 79 80 43 45
		f 4 108 -111 28 42
		mu 0 4 43 80 32 31
		f 4 110 109 37 32
		mu 0 4 32 80 79 34
		f 4 -113 -112 50 65
		mu 0 4 81 82 83 84
		f 4 111 -114 44 49
		mu 0 4 83 82 42 41
		f 4 113 -115 55 48
		mu 0 4 42 82 49 44
		f 4 114 -116 62 51
		mu 0 4 49 82 54 46
		f 4 115 112 66 58
		mu 0 4 54 82 81 51
		f 4 -118 -117 72 73
		mu 0 4 59 85 86 56
		f 4 116 -119 60 71
		mu 0 4 86 85 53 52
		f 4 118 117 77 64
		mu 0 4 53 85 59 55
		f 4 124 279 -23 -126
		mu 0 4 18 17 28 27
		f 4 -101 -129 13 125
		mu 0 4 27 76 14 18
		f 4 128 -100 127 126
		mu 0 4 14 76 75 87
		f 4 121 259 -252 -261
		mu 0 4 61 62 89 90
		f 4 -26 260 144 219
		mu 0 4 30 61 90 91
		f 10 -51 -50 45 29 -220 -149 -167 170 171 -262
		mu 0 10 84 83 41 31 30 91 92 93 94 95
		f 4 -66 261 186 187
		mu 0 4 81 84 95 96
		f 4 -67 -188 188 189
		mu 0 4 51 81 96 97
		f 4 61 -190 -183 -263
		mu 0 4 52 51 97 98
		f 4 -72 262 194 195
		mu 0 4 86 52 98 99
		f 4 -73 -196 196 197
		mu 0 4 56 86 99 100
		f 8 89 81 76 -198 -202 -207 -215 -264
		mu 0 8 73 69 57 56 100 101 102 103
		f 4 88 263 -214 228
		mu 0 4 74 73 103 104
		f 4 91 -229 -217 218
		mu 0 4 65 74 104 105
		f 4 -93 -219 220 -265
		mu 0 4 66 65 105 106
		f 4 84 264 -210 227
		mu 0 4 71 66 106 107
		f 4 87 -228 -213 217
		mu 0 4 72 71 107 108
		f 4 40 284 -162 -266
		mu 0 4 40 39 109 110
		f 4 -34 265 152 153
		mu 0 4 78 40 110 111
		f 4 -35 -154 154 155
		mu 0 4 23 78 111 112
		f 4 20 -156 -140 129
		mu 0 4 24 23 112 113
		f 4 -15 -130 132 133
		mu 0 4 75 24 113 114
		f 4 -128 -134 257 -267
		mu 0 4 87 75 114 115
		f 4 134 135 136 137
		mu 0 4 120 121 122 123
		f 4 138 139 140 -136
		mu 0 4 121 113 112 122
		f 4 -253 253 234 -250
		mu 0 4 88 119 124 125
		f 4 142 -277 288 -142
		mu 0 4 126 120 127 128
		f 4 145 146 147 148
		mu 0 4 91 129 130 92
		f 4 149 150 151 -147
		mu 0 4 129 131 132 130
		f 4 156 157 286 275
		mu 0 4 123 133 134 135
		f 4 160 161 285 -158
		mu 0 4 133 110 109 134
		f 4 163 164 165 166
		mu 0 4 92 136 137 93
		f 4 167 168 169 -165
		mu 0 4 136 138 139 137
		f 4 172 173 174 175
		mu 0 4 140 141 142 143
		f 4 176 177 178 -174
		mu 0 4 141 139 144 142
		f 4 179 180 181 182
		mu 0 4 97 145 146 98
		f 4 183 184 185 -181
		mu 0 4 145 140 147 146
		f 4 198 199 200 201
		mu 0 4 100 148 149 101
		f 4 202 203 204 -200
		mu 0 4 148 147 150 149
		f 4 251 250 249 -233
		mu 0 4 90 89 88 125
		f 4 -176 221 -204 -185
		mu 0 4 140 143 150 147
		f 4 -192 222 -208 -222
		mu 0 4 143 151 152 150
		f 4 -211 -221 -216 -223
		mu 0 4 151 106 105 152
		f 4 287 276 -138 -276
		mu 0 4 135 127 120 123
		f 4 -175 223 190 191
		mu 0 4 143 142 153 151
		f 4 -179 192 193 -224
		mu 0 4 142 144 154 153
		f 4 -201 224 205 206
		mu 0 4 101 149 155 102
		f 4 -205 207 208 -225
		mu 0 4 149 150 152 155
		f 4 -191 225 209 210
		mu 0 4 151 153 107 106
		f 4 -194 211 212 -226
		mu 0 4 153 154 108 107
		f 4 -206 226 213 214
		mu 0 4 102 155 104 103
		f 4 -209 215 216 -227
		mu 0 4 155 152 105 104
		f 4 -133 -139 231 -230
		mu 0 4 114 113 121 156
		f 4 -135 -143 -231 -232
		mu 0 4 121 120 126 156
		f 4 -146 -145 232 233
		mu 0 4 129 91 90 125
		f 4 -144 -150 -234 -235
		mu 0 4 124 131 129 125
		f 4 -141 -155 235 236
		mu 0 4 122 112 111 157
		f 4 -153 -161 237 -236
		mu 0 4 111 110 133 157
		f 4 -157 -137 -237 -238
		mu 0 4 133 123 122 157
		f 4 -163 -168 238 239
		mu 0 4 158 138 136 159
		f 4 -164 -148 240 -239
		mu 0 4 136 92 130 159
		f 4 -152 -159 -240 -241
		mu 0 4 130 132 158 159
		f 4 -187 -172 241 242
		mu 0 4 96 95 94 160
		f 4 -171 -166 243 -242
		mu 0 4 94 93 137 160
		f 4 -170 -177 244 -244
		mu 0 4 137 139 141 160
		f 4 -173 -184 245 -245
		mu 0 4 141 140 145 160
		f 4 -180 -189 -243 -246
		mu 0 4 145 97 96 160
		f 4 -199 -197 246 247
		mu 0 4 148 100 99 161
		f 4 -195 -182 248 -247
		mu 0 4 99 98 146 161
		f 4 -186 -203 -248 -249
		mu 0 4 146 147 148 161
		f 4 255 141 289 -255
		mu 0 4 117 126 128 118
		f 4 -256 -132 258 230
		mu 0 4 126 117 116 156
		f 4 -257 -258 229 -259
		mu 0 4 116 115 114 156
		f 4 -280 267 123 -269
		mu 0 4 28 17 16 26
		f 4 -281 268 -25 12
		mu 0 4 29 28 26 35
		f 4 38 -282 -13 31
		mu 0 4 34 36 29 35
		f 4 -283 -39 -38 -272
		mu 0 4 37 36 34 79
		f 4 -284 271 -42 -273
		mu 0 4 39 37 79 45
		f 5 291 272 47 56 69
		mu 0 5 68 39 45 44 50
		f 4 -286 273 162 -275
		mu 0 4 134 109 138 158
		f 4 -287 274 158 159
		mu 0 4 135 134 158 132
		f 4 -151 130 -288 -160
		mu 0 4 132 131 127 135
		f 4 -289 -131 143 -278
		mu 0 4 128 127 131 124
		f 4 -290 277 -254 -279
		mu 0 4 118 128 124 119
		f 5 -291 -193 -178 -169 -274
		mu 0 5 109 154 144 139 138
		f 6 -285 -292 86 -218 -212 290
		mu 0 6 109 39 68 72 108 154
		f 6 -294 -4 292 -251 -260 120
		mu 0 6 15 8 1 88 89 62
		f 7 -293 -1 294 131 254 278 252
		mu 0 7 88 1 0 116 117 118 119
		f 6 -295 1 295 -127 266 256
		mu 0 6 116 5 4 14 87 115;
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
createNode transform -n "PlugIt_PlugCountNumber_20";
	rename -uid "4789062D-4A25-00AF-6446-8DA401250F9B";
createNode groupId -n "groupId1";
	rename -uid "EF52262A-4735-E497-1DE7-D0AF4D08DED0";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "A9003414-41E6-0CE5-C178-618321FC8815";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "AECE883C-4A94-80C7-74FF-F4A9EEA67959";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "C1D68661-4F64-A123-A59C-52AD52242E44";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "D861D73A-4FC2-3E7B-3657-29908ED7E35E";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "E1D322BA-48BD-4F8D-2AD4-95A3B509E161";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "B77CF6DA-406A-3D6A-6A61-90840515C9E1";
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
	rename -uid "F3400CE5-4402-F69B-3411-47984472EF20";
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
// End of Plug_Square_04.ma
