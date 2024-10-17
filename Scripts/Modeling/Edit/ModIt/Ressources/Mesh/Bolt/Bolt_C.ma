//Maya ASCII 2023 scene
//Name: Bolt_C.ma
//Last modified: Wed, Nov 02, 2022 08:44:46 AM
//Codeset: 1252
requires maya "2023";
requires "stereoCamera" "10.0";
requires "mtoa" "5.1.3.3";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202202161415-df43006fd3";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19044)";
fileInfo "UUID" "9DDB4A24-4B56-1F04-7571-929A191AE83B";
createNode transform -n "Bolt_C";
	rename -uid "54EFF774-433C-FD0D-F87A-EC9B57E96851";
createNode mesh -n "Bolt_CShape" -p "Bolt_C";
	rename -uid "BE6D9180-45A5-D3C9-73EA-0DA0CDD926FA";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "UVChannel_1";
	setAttr ".cuvs" -type "string" "UVChannel_1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode mesh -n "polySurfaceShape31" -p "Bolt_C";
	rename -uid "BFD13468-4067-4BF5-6041-4BA0DAECA05A";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "UVChannel_1";
	setAttr -s 187 ".uvst[0].uvsp[0:186]" -type "float2" 0.40000004 1 0.5
		 0.64758354 0.69999993 0.64758354 0.90000004 0.64758354 0.10000004 0.64758354 0.30000001
		 0.64758354 0.5 0.91189581 0.5 0.8237918 0.5 0.73568767 0.69999993 0.91189581 0.69999993
		 0.8237918 0.69999993 0.73568767 0.90000004 0.91189581 0.90000004 0.8237918 0.90000004
		 0.73568767 0.10000004 0.91189581 0.10000004 0.8237918 0.10000004 0.73568767 0.30000004
		 0.91189581 0.30000001 0.8237918 0.30000001 0.73568767 0.54870278 0.66877341 0.59999996
		 0.67620814 0.65129721 0.66877341 0.74870276 0.66877341 0.80000001 0.67620814 0.8512972
		 0.66877347 0.94870275 0.66877341 3.7945494e-08 0.67620814 0.051297262 0.66877341
		 0.14870282 0.66877347 0.20000002 0.6762082 0.25129724 0.66877341 0.34870282 0.66877341
		 0.40000001 0.67620814 0.45129722 0.66877341 0.52640474 0.57467562 0.54999995 0.5
		 0.72640473 0.57467562 0.75 0.5 0.92640477 0.57467562 0.95000005 0.5 0.12640479 0.57467562
		 0.15000005 0.5 0.32640475 0.57467562 0.34999996 0.5 0.47359523 0.57467562 0.44999999
		 0.5 0.67359525 0.57467562 0.65000004 0.5 0.8735953 0.57467562 0.85000002 0.5 0.073595285
		 0.57467562 0.050000019 0.5 0.27359527 0.57467562 0.25000003 0.5 0.59999996 0.8524164
		 0.56441385 0.76536298 0.6355862 0.76536298 0.80000001 0.8524164 0.76441377 0.76536298
		 0.83558619 0.76536298 3.7945494e-08 0.8524164 0.96441388 0.76536298 0.035586193 0.76536298
		 0.20000002 0.8524164 0.16441384 0.76536298 0.2355862 0.76536298 0.40000001 0.8524164
		 0.36441383 0.76536298 0.43558618 0.76536298 0.5 0.5 0.69999993 0.5 0.90000004 0.5
		 0.10000004 0.5 0.30000001 0.5 0.59999996 0.5 0.62463111 0.58211619 0.57536888 0.58211619
		 0.80000001 0.5 0.82463115 0.58211619 0.77536881 0.58211619 3.7945494e-08 0.5 0.02463118
		 0.58211619 0.97536886 0.58211619 0.20000003 0.5 0.22463116 0.58211619 0.17536889
		 0.58211619 0.40000001 0.5 0.42463115 0.58211619 0.37536889 0.58211619 0.59999996
		 1 0.79999995 1 3.7252903e-08 1 -0.099999964 0.91189581 -0.099999964 0.91189581 -0.099999964
		 0.8237918 -0.099999964 0.91189581 -0.099999964 0.8237918 -0.035586119 0.76536298
		 -0.035586119 0.76536298 -0.035586119 0.76536298 -0.051297247 0.66877341 -0.035586119
		 0.76536298 0.20000005 1 -0.024631143 0.58211619 -0.024631143 0.58211619 -0.049999952
		 0.5 -0.024631143 0.58211619 -0.024631143 0.58211619 -0.051297247 0.66877341 0.75710398
		 0.057191484 0.90956271 0.05719148 0.90956265 0.94280851 0.75710398 0.94280851 0.92377067
		 0.057191484 1.076229334 0.05719148 1.076229334 0.94280851 0.92377067 0.94280851 0.090437353
		 0.057191476 0.24289604 0.05719148 0.24289604 0.94280851 0.090437353 0.94280851 0.25710401
		 0.05719148 0.40956268 0.057191484 0.40956271 0.94280851 0.25710404 0.94280851 0.4237707
		 0.057191484 0.57622933 0.057191484 0.57622927 0.94280851 0.42377067 0.94280851 0.59043729
		 0.057191484 0.74289602 0.057191484 0.74289596 0.94280851 0.59043729 0.94280851 0.91170073
		 0.73769552 0.91170073 0.26230454 0.50000006 0.02460896 0.088299267 0.26230443 0.088299237
		 0.73769552 0.49999997 0.97539103 0.49999997 0.97539103 0.088299237 0.73769552 0.088299267
		 0.26230443 0.50000006 0.024608964 0.91170073 0.26230454 0.91170073 0.73769552 0.75
		 0.026224243 0.91666669 0.026224252 0.05297184 0.29493293 0.052971832 0.24550743 0.25000003
		 0.026224239 0.41666669 0.026224243 0.58333331 0.026224257 0.75 0.97377574 0.91666669
		 0.97377574 0.058651052 0.98179024 0.049213655 0.91554153 0.25000003 0.97377574 0.41666669
		 0.97377574 0.58333331 0.97377574 0.45260021 0.96725297 0.055086624 0.73998499 0.14714581
		 0.71338886 0.54419971 0.94078964 0.15001282 0.72850323 0.14987686 0.26639068 0.18949589
		 0.057191473 0.18949589 0.94280851 0.14885005 0.28079912 0.14934666 0.73785079 0.057704426
		 0.28873944 0.45674315 0.061291501 0.52032596 -0.0030656396 0.11999136 0.22569394
		 0.54132169 0.028934764 0.93864095 0.25653166 0.99991602 0.39531547 0.60843921 0.15993369
		 0.87188095 0.14887473 0.86545974 0.60999578 0.9459933 0.72850323 0.94585735 0.26639077
		 0.88757241 0.78938532 0.49276921 1.019635081 0.46345937 0.83836555 0.85505128 0.6107024;
	setAttr ".cuvs" -type "string" "UVChannel_1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 127 ".vt[0:126]"  0 1.20978928 0 0.5114131 0.89371872 0 0.15803528 0.89371872 -0.48638272
		 -0.41374183 0.89371872 -0.30060089 -0.41374171 0.89371872 0.30060112 0.15803528 0.89371872 0.48638272
		 0.15624762 1.18802643 0 0.30060101 1.12439442 0 0.4220717 1.023737907 0 0.0482831 1.18802643 -0.14860022
		 0.092890978 1.12439442 -0.28588843 0.13042736 1.023737907 -0.40141404 -0.12640691 1.18802643 -0.09183991
		 -0.24319148 1.12439442 -0.17668879 -0.34146321 1.023737907 -0.24808753 -0.12640691 1.18802643 0.091840029
		 -0.24319148 1.12439442 0.17668891 -0.34146309 1.023737907 0.24808764 0.0482831 1.18802643 0.14860034
		 0.092890978 1.12439442 0.28588855 0.13042736 1.023737907 0.40141404 0.4703548 0.92717171 -0.14860022
		 0.39349174 0.93861389 -0.28588843 0.28667498 0.92717171 -0.40141404 0.0040204525 0.92717171 -0.49325395
		 -0.1503005 0.93861389 -0.46257734 -0.29317999 0.92717171 -0.39668775 -0.46787012 0.92717171 -0.1562475
		 -0.4863826 0.93861389 1.1920929e-07 -0.46787 0.92717171 0.15624762 -0.29317999 0.92717171 0.39668787
		 -0.1503005 0.93861389 0.46257734 0.0040204525 0.92717171 0.49325413 0.28667498 0.92717171 0.40141404
		 0.39349198 0.93861294 0.28588855 0.4703548 0.92717171 0.14860034 0.5484786 0.77092457 -0.09183991
		 0.54379249 0.63801193 -0.17668879 0.082144022 0.77092457 -0.55001426 0 0.63801193 -0.57177722
		 -0.49771059 0.77092457 -0.24808753 -0.54379249 0.63801193 -0.17668867 -0.38974619 0.77092457 0.39668787
		 -0.33608222 0.63801193 0.46257758 0.25683427 0.77092457 0.49325413 0.33608222 0.63801193 0.46257734
		 0.5484786 0.77092457 0.091840029 0.54379225 0.63801193 0.17668891 0.25683427 0.77092457 -0.49325418
		 0.33608222 0.63801193 -0.46257734 -0.38974643 0.77092457 -0.39668775 -0.33608234 0.63801193 -0.46257734
		 -0.4977107 0.77092457 0.24808764 -0.54379225 0.63801193 0.17668891 0.08214426 0.77092457 0.55001432
		 2.3841858e-07 0.63801193 0.57177722 0.20687103 1.14942551 -0.1503005 0.35328078 1.061355591 -0.15133595
		 0.25309896 1.061355591 -0.28922486 -0.079017639 1.14942551 -0.24319124 -0.034759283 1.061355591 -0.38275552
		 -0.19685745 1.061355591 -0.33008659 -0.25570655 1.14942551 0 -0.37476337 1.061355591 -0.08521986
		 -0.37476325 1.061355591 0.085220098 -0.079017639 1.14942551 0.24319136 -0.19685721 1.061355591 0.33008683
		 -0.034759045 1.061355591 0.38275564 0.20687103 1.14942551 0.1503005 0.25309896 1.061355591 0.28922486
		 0.35328102 1.061355591 0.15133595 0.57177687 0.63801193 0 0.17668891 0.63801193 -0.54379225
		 -0.46257734 0.63801193 -0.3360821 -0.46257746 0.63801193 0.33608222 0.17668891 0.63801193 0.54379243
		 0.46257734 0.63801193 -0.3360821 0.39183331 0.78388596 -0.39002109 0.49201536 0.78388596 -0.2521323
		 -0.17668891 0.63801193 -0.54379225 -0.24984908 0.78388596 -0.49317861 -0.08775115 0.78388596 -0.54584765
		 -0.57177699 0.63801193 1.1920929e-07 -0.54624844 0.78388596 0.085220098 -0.54624844 0.78388596 -0.08521986
		 -0.17668891 0.63801193 0.54379249 -0.087750912 0.78388596 0.54584777 -0.24984884 0.78388596 0.4931789
		 0.46257734 0.63801193 0.33608222 0.49201536 0.78388596 0.25213242 0.39183331 0.78388596 0.3900212
		 0.84906816 0.036978722 -0.032024503 0.41242886 0 -0.71434808 -0.41242909 0 -0.71434808
		 -0.82485819 0 1.1920929e-07 -0.41242886 0 0.7143482 0.45226812 0.036978722 0.71930242
		 0.84906816 0.60959911 -0.032024503 0.39680004 0.60959911 -0.75132704 -0.45226836 0.60959911 -0.71930242
		 -0.84906816 0.60959911 0.032024622 -0.3967998 0.60959911 0.75132704 0.45226812 0.60959911 0.71930242
		 0.84906816 0.036978722 0.032024622 0.82485819 0 0 0.39680004 0.036978722 -0.75132704
		 0.45226836 0.036978722 -0.71930242 -0.45226836 0.036978722 -0.71930242 -0.39680004 0.036978722 -0.75132704
		 -0.84906816 0.036978722 0.032024622 -0.84906816 0.036978722 -0.032024384 -0.3967998 0.036978722 0.75132704
		 -0.45226812 0.036978722 0.71930242 0.3967998 0.036978722 0.75132704 0.41242886 0 0.7143482
		 0.82485819 0.64657784 0 0.84906816 0.60959911 0.032024622 0.41242886 0.64657784 -0.71434808
		 0.45226836 0.60959911 -0.71930242 -0.41242909 0.64657784 -0.71434808 -0.39680004 0.60959911 -0.75132704
		 -0.82485819 0.64657784 1.1920929e-07 -0.84906816 0.60959911 -0.032024384 -0.41242886 0.64657784 0.7143482
		 -0.45226812 0.60959911 0.71930242 0.41242886 0.64657784 0.7143482 0.3967998 0.60959911 0.75132704;
	setAttr -s 322 ".ed";
	setAttr ".ed[0:165]"  0 6 1 6 9 1 9 0 1 6 7 1 7 56 1 56 6 1 56 9 1 56 10 1
		 10 9 1 7 8 1 8 57 1 57 7 1 57 56 1 57 58 1 58 56 1 58 10 1 58 11 1 11 10 1 8 1 1
		 1 21 1 21 8 1 21 57 1 21 22 1 22 57 1 22 58 1 22 23 1 23 58 1 23 11 1 23 2 1 2 11 1
		 9 12 1 12 0 1 10 59 1 59 9 1 59 12 1 59 13 1 13 12 1 11 60 1 60 10 1 60 59 1 60 61 1
		 61 59 1 61 13 1 61 14 1 14 13 1 2 24 1 24 11 1 24 60 1 24 25 1 25 60 1 25 61 1 25 26 1
		 26 61 1 26 14 1 26 3 1 3 14 1 12 15 1 15 0 1 13 62 1 62 12 1 62 15 1 62 16 1 16 15 1
		 14 63 1 63 13 1 63 62 1 63 64 1 64 62 1 64 16 1 64 17 1 17 16 1 3 27 1 27 14 1 27 63 1
		 27 28 1 28 63 1 28 64 1 28 29 1 29 64 1 29 17 1 29 4 1 4 17 1 15 18 1 18 0 1 16 65 1
		 65 15 1 65 18 1 65 19 1 19 18 1 17 66 1 66 16 1 66 65 1 66 67 1 67 65 1 67 19 1 67 20 1
		 20 19 1 4 30 1 30 17 1 30 66 1 30 31 1 31 66 1 31 67 1 31 32 1 32 67 1 32 20 1 32 5 1
		 5 20 1 18 6 1 19 68 1 68 18 1 68 6 1 68 7 1 20 69 1 69 19 1 69 68 1 69 70 1 70 68 1
		 70 7 1 70 8 1 5 33 1 33 20 1 33 69 1 33 34 1 34 69 1 34 70 1 34 35 1 35 70 1 35 8 1
		 35 1 1 1 46 1 46 36 1 36 1 1 46 47 1 47 71 1 71 46 1 71 36 1 71 37 1 37 36 1 2 48 1
		 48 38 1 38 2 1 48 49 1 49 72 1 72 48 1 72 38 1 72 39 1 39 38 1 3 50 1 50 40 1 40 3 1
		 50 51 1 51 73 1 73 50 1 73 40 1 73 41 1 41 40 1 4 52 1 52 42 1 42 4 1 52 53 1 53 74 1
		 74 52 1 74 42 1 74 43 1 43 42 1;
	setAttr ".ed[166:321]" 5 54 1 54 44 1 44 5 1 54 55 1 55 75 1 75 54 1 75 44 1
		 75 45 1 45 44 1 48 77 1 77 49 1 77 76 1 76 49 1 77 78 1 78 76 1 78 37 1 37 76 1 78 36 1
		 23 48 1 23 77 1 22 77 1 22 78 1 21 78 1 21 36 1 50 80 1 80 51 1 80 79 1 79 51 1 80 81 1
		 81 79 1 81 39 1 39 79 1 81 38 1 26 50 1 26 80 1 25 80 1 25 81 1 24 81 1 24 38 1 52 83 1
		 83 53 1 83 82 1 82 53 1 83 84 1 84 82 1 84 41 1 41 82 1 84 40 1 29 52 1 29 83 1 28 83 1
		 28 84 1 27 84 1 27 40 1 54 86 1 86 55 1 86 85 1 85 55 1 86 87 1 87 85 1 87 43 1 43 85 1
		 87 42 1 32 54 1 32 86 1 31 86 1 31 87 1 30 87 1 30 42 1 46 89 1 89 47 1 89 88 1 88 47 1
		 89 90 1 90 88 1 90 45 1 45 88 1 90 44 1 35 46 1 35 89 1 34 89 1 34 90 1 33 90 1 33 44 1
		 91 106 1 106 118 1 118 97 1 97 91 1 105 108 1 108 120 1 120 98 1 98 105 1 107 110 1
		 110 122 1 122 99 1 99 107 1 109 112 1 112 124 1 124 100 1 100 109 1 111 113 1 113 126 1
		 126 101 1 101 111 1 96 103 1 103 116 1 116 102 1 102 96 1 114 95 1 95 94 1 94 93 1
		 93 92 1 92 104 1 104 114 1 115 117 1 117 119 1 119 121 1 121 123 1 123 125 1 125 115 1
		 91 103 1 103 104 1 104 91 1 92 105 1 105 106 1 106 92 1 93 107 1 107 108 1 108 93 1
		 94 109 1 109 110 1 110 94 1 95 111 1 111 112 1 112 95 1 96 113 1 113 114 1 114 96 1
		 97 115 1 115 116 1 116 97 1 98 117 1 117 118 1 118 98 1 99 119 1 119 120 1 120 99 1
		 100 121 1 121 122 1 122 100 1 101 123 1 123 124 1 124 101 1 102 125 1 125 126 1 126 102 1;
	setAttr -s 127 ".n[0:126]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 199 -ch 644 ".fc[0:198]" -type "polyFaces" 
		f 3 0 1 2
		mu 0 3 91 6 9
		f 3 3 4 5
		mu 0 3 6 7 56
		f 3 -6 6 -2
		mu 0 3 6 56 9
		f 3 -7 7 8
		mu 0 3 9 56 10
		f 3 9 10 11
		mu 0 3 7 8 57
		f 3 -12 12 -5
		mu 0 3 7 57 56
		f 3 -13 13 14
		mu 0 3 56 57 58
		f 3 -15 15 -8
		mu 0 3 56 58 10
		f 3 -16 16 17
		mu 0 3 10 58 11
		f 3 18 19 20
		mu 0 3 8 1 21
		f 3 -21 21 -11
		mu 0 3 8 21 57
		f 3 -22 22 23
		mu 0 3 57 21 22
		f 3 -24 24 -14
		mu 0 3 57 22 58
		f 3 -25 25 26
		mu 0 3 58 22 23
		f 3 -27 27 -17
		mu 0 3 58 23 11
		f 3 -28 28 29
		mu 0 3 11 23 2
		f 3 -3 30 31
		mu 0 3 92 9 12
		f 3 -9 32 33
		mu 0 3 9 10 59
		f 3 -34 34 -31
		mu 0 3 9 59 12
		f 3 -35 35 36
		mu 0 3 12 59 13
		f 3 -18 37 38
		mu 0 3 10 11 60
		f 3 -39 39 -33
		mu 0 3 10 60 59
		f 3 -40 40 41
		mu 0 3 59 60 61
		f 3 -42 42 -36
		mu 0 3 59 61 13
		f 3 -43 43 44
		mu 0 3 13 61 14
		f 3 -30 45 46
		mu 0 3 11 2 24
		f 3 -47 47 -38
		mu 0 3 11 24 60
		f 3 -48 48 49
		mu 0 3 60 24 25
		f 3 -50 50 -41
		mu 0 3 60 25 61
		f 3 -51 51 52
		mu 0 3 61 25 26
		f 3 -53 53 -44
		mu 0 3 61 26 14
		f 3 -54 54 55
		mu 0 3 14 26 3
		f 3 -32 56 57
		mu 0 3 93 94 15
		f 3 -37 58 59
		mu 0 3 95 96 62
		f 3 -60 60 -57
		mu 0 3 97 62 15
		f 3 -61 61 62
		mu 0 3 15 62 16
		f 3 -45 63 64
		mu 0 3 13 14 63
		f 3 -65 65 -59
		mu 0 3 98 99 62
		f 3 -66 66 67
		mu 0 3 62 100 64
		f 3 -68 68 -62
		mu 0 3 62 64 16
		f 3 -69 69 70
		mu 0 3 16 64 17
		f 3 -56 71 72
		mu 0 3 14 3 27
		f 3 -73 73 -64
		mu 0 3 14 27 63
		f 3 -74 74 75
		mu 0 3 101 102 28
		f 3 -76 76 -67
		mu 0 3 103 28 64
		f 3 -77 77 78
		mu 0 3 64 28 29
		f 3 -79 79 -70
		mu 0 3 64 29 17
		f 3 -80 80 81
		mu 0 3 17 29 4
		f 3 -58 82 83
		mu 0 3 104 15 18
		f 3 -63 84 85
		mu 0 3 15 16 65
		f 3 -86 86 -83
		mu 0 3 15 65 18
		f 3 -87 87 88
		mu 0 3 18 65 19
		f 3 -71 89 90
		mu 0 3 16 17 66
		f 3 -91 91 -85
		mu 0 3 16 66 65
		f 3 -92 92 93
		mu 0 3 65 66 67
		f 3 -94 94 -88
		mu 0 3 65 67 19
		f 3 -95 95 96
		mu 0 3 19 67 20
		f 3 -82 97 98
		mu 0 3 17 4 30
		f 3 -99 99 -90
		mu 0 3 17 30 66
		f 3 -100 100 101
		mu 0 3 66 30 31
		f 3 -102 102 -93
		mu 0 3 66 31 67
		f 3 -103 103 104
		mu 0 3 67 31 32
		f 3 -105 105 -96
		mu 0 3 67 32 20
		f 3 -106 106 107
		mu 0 3 20 32 5
		f 3 -84 108 -1
		mu 0 3 0 18 6
		f 3 -89 109 110
		mu 0 3 18 19 68
		f 3 -111 111 -109
		mu 0 3 18 68 6
		f 3 -112 112 -4
		mu 0 3 6 68 7
		f 3 -97 113 114
		mu 0 3 19 20 69
		f 3 -115 115 -110
		mu 0 3 19 69 68
		f 3 -116 116 117
		mu 0 3 68 69 70
		f 3 -118 118 -113
		mu 0 3 68 70 7
		f 3 -119 119 -10
		mu 0 3 7 70 8
		f 3 -108 120 121
		mu 0 3 20 5 33
		f 3 -122 122 -114
		mu 0 3 20 33 69
		f 3 -123 123 124
		mu 0 3 69 33 34
		f 3 -125 125 -117
		mu 0 3 69 34 70
		f 3 -126 126 127
		mu 0 3 70 34 35
		f 3 -128 128 -120
		mu 0 3 70 35 8
		f 3 -129 129 -19
		mu 0 3 8 35 1
		f 3 130 131 132
		mu 0 3 1 46 36
		f 3 133 134 135
		mu 0 3 46 47 71
		f 3 -136 136 -132
		mu 0 3 46 71 36
		f 3 -137 137 138
		mu 0 3 36 71 37
		f 3 139 140 141
		mu 0 3 2 48 38
		f 3 142 143 144
		mu 0 3 48 49 72
		f 3 -145 145 -141
		mu 0 3 48 72 38
		f 3 -146 146 147
		mu 0 3 38 72 39
		f 3 148 149 150
		mu 0 3 3 50 40
		f 3 151 152 153
		mu 0 3 50 51 73
		f 3 -154 154 -150
		mu 0 3 50 73 40
		f 3 -155 155 156
		mu 0 3 40 73 41
		f 3 157 158 159
		mu 0 3 4 52 42
		f 3 160 161 162
		mu 0 3 52 53 74
		f 3 -163 163 -159
		mu 0 3 52 74 42
		f 3 -164 164 165
		mu 0 3 42 74 43
		f 3 166 167 168
		mu 0 3 5 54 44
		f 3 169 170 171
		mu 0 3 54 55 75
		f 3 -172 172 -168
		mu 0 3 54 75 44
		f 3 -173 173 174
		mu 0 3 44 75 45
		f 3 -143 175 176
		mu 0 3 49 48 77
		f 3 -177 177 178
		mu 0 3 49 77 76
		f 3 -178 179 180
		mu 0 3 76 77 78
		f 3 -181 181 182
		mu 0 3 76 78 37
		f 3 -182 183 -139
		mu 0 3 37 78 36
		f 3 -140 -29 184
		mu 0 3 48 2 23
		f 3 -185 185 -176
		mu 0 3 48 23 77
		f 3 -186 -26 186
		mu 0 3 77 23 22
		f 3 -187 187 -180
		mu 0 3 77 22 78
		f 3 -188 -23 188
		mu 0 3 78 22 21
		f 3 -189 189 -184
		mu 0 3 78 21 36
		f 3 -190 -20 -133
		mu 0 3 36 21 1
		f 3 -152 190 191
		mu 0 3 51 50 80
		f 3 -192 192 193
		mu 0 3 51 80 79
		f 3 -193 194 195
		mu 0 3 79 80 81
		f 3 -196 196 197
		mu 0 3 79 81 39
		f 3 -197 198 -148
		mu 0 3 39 81 38
		f 3 -149 -55 199
		mu 0 3 50 3 26
		f 3 -200 200 -191
		mu 0 3 50 26 80
		f 3 -201 -52 201
		mu 0 3 80 26 25
		f 3 -202 202 -195
		mu 0 3 80 25 81
		f 3 -203 -49 203
		mu 0 3 81 25 24
		f 3 -204 204 -199
		mu 0 3 81 24 38
		f 3 -205 -46 -142
		mu 0 3 38 24 2
		f 3 -161 205 206
		mu 0 3 53 52 83
		f 3 -207 207 208
		mu 0 3 53 83 82
		f 3 -208 209 210
		mu 0 3 82 83 105
		f 3 -211 211 212
		mu 0 3 82 106 107
		f 3 -212 213 -157
		mu 0 3 41 84 40
		f 3 -158 -81 214
		mu 0 3 52 4 29
		f 3 -215 215 -206
		mu 0 3 52 29 83
		f 3 -216 -78 216
		mu 0 3 83 29 28
		f 3 -217 217 -210
		mu 0 3 83 28 108
		f 3 -218 -75 218
		mu 0 3 109 28 110
		f 3 -219 219 -214
		mu 0 3 84 27 40
		f 3 -220 -72 -151
		mu 0 3 40 27 3
		f 3 -170 220 221
		mu 0 3 55 54 86
		f 3 -222 222 223
		mu 0 3 55 86 85
		f 3 -223 224 225
		mu 0 3 85 86 87
		f 3 -226 226 227
		mu 0 3 85 87 43
		f 3 -227 228 -166
		mu 0 3 43 87 42
		f 3 -167 -107 229
		mu 0 3 54 5 32
		f 3 -230 230 -221
		mu 0 3 54 32 86
		f 3 -231 -104 231
		mu 0 3 86 32 31
		f 3 -232 232 -225
		mu 0 3 86 31 87
		f 3 -233 -101 233
		mu 0 3 87 31 30
		f 3 -234 234 -229
		mu 0 3 87 30 42
		f 3 -235 -98 -160
		mu 0 3 42 30 4
		f 3 -134 235 236
		mu 0 3 47 46 89
		f 3 -237 237 238
		mu 0 3 47 89 88
		f 3 -238 239 240
		mu 0 3 88 89 90
		f 3 -241 241 242
		mu 0 3 88 90 45
		f 3 -242 243 -175
		mu 0 3 45 90 44
		f 3 -131 -130 244
		mu 0 3 46 1 35
		f 3 -245 245 -236
		mu 0 3 46 35 89
		f 3 -246 -127 246
		mu 0 3 89 35 34
		f 3 -247 247 -240
		mu 0 3 89 34 90
		f 3 -248 -124 248
		mu 0 3 90 34 33
		f 3 -249 249 -244
		mu 0 3 90 33 44
		f 3 -250 -121 -169
		mu 0 3 44 33 5
		f 20 -239 -243 -174 -171 -224 -228 -165 -162 -209 -213 -156 -153 -194 -198 -147 -144
		 -179 -183 -138 -135
		mu 0 20 47 88 45 75 55 85 43 74 53 82 107 73 51 79 39 72 49 76 37 71
		f 4 250 251 252 253
		mu 0 4 111 112 113 114
		f 4 254 255 256 257
		mu 0 4 115 116 117 118
		f 4 258 259 260 261
		mu 0 4 119 120 121 122
		f 4 262 263 264 265
		mu 0 4 123 124 125 126
		f 4 266 267 268 269
		mu 0 4 127 128 129 130
		f 4 270 271 272 273
		mu 0 4 131 132 133 134
		f 6 274 275 276 277 278 279
		mu 0 6 135 136 137 138 139 140
		f 6 280 281 282 283 284 285
		mu 0 6 141 142 143 144 145 146
		f 3 286 287 288
		mu 0 3 111 132 147
		f 3 289 290 291
		mu 0 3 148 115 112
		f 3 292 293 294
		mu 0 3 138 149 150
		f 3 295 296 297
		mu 0 3 151 123 120
		f 3 298 299 300
		mu 0 3 152 127 124
		f 3 301 302 303
		mu 0 3 131 128 153
		f 3 304 305 306
		mu 0 3 114 154 133
		f 3 307 308 309
		mu 0 3 118 155 113
		f 3 310 311 312
		mu 0 3 122 156 157
		f 3 313 314 315
		mu 0 3 126 158 121
		f 3 316 317 318
		mu 0 3 130 159 125
		f 3 319 320 321
		mu 0 3 134 160 129
		f 4 -289 -279 -292 -251
		mu 0 4 161 140 139 162
		f 4 -291 -258 -310 -252
		mu 0 4 112 115 118 113
		f 4 -309 -281 -305 -253
		mu 0 4 163 142 141 164
		f 4 -307 -272 -287 -254
		mu 0 4 114 133 132 111
		f 4 -290 -278 -295 -255
		mu 0 4 165 139 138 166
		f 4 -294 -262 -313 -256
		mu 0 4 167 119 122 168
		f 4 -312 -282 -308 -257
		mu 0 4 169 143 142 170
		f 4 -293 -277 -298 -259
		mu 0 4 171 138 137 172
		f 4 -297 -266 -316 -260
		mu 0 4 120 123 126 121
		f 4 -315 -283 -311 -261
		mu 0 4 173 144 143 174
		f 4 -296 -276 -301 -263
		mu 0 4 175 137 136 176
		f 4 -300 -270 -319 -264
		mu 0 4 124 127 130 125
		f 4 -318 -284 -314 -265
		mu 0 4 177 145 144 178
		f 4 -299 -275 -303 -267
		mu 0 4 179 136 135 180
		f 4 -302 -274 -322 -268
		mu 0 4 128 131 134 129
		f 4 -321 -285 -317 -269
		mu 0 4 181 146 145 182
		f 4 -304 -280 -288 -271
		mu 0 4 183 135 140 184
		f 4 -306 -286 -320 -273
		mu 0 4 185 141 146 186;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode polySoftEdge -n "polySoftEdge17";
	rename -uid "C85141DC-43C3-F619-9167-D5BB7D990E74";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "e[*]";
	setAttr ".ix" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".a" 45;
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
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".st";
	setAttr -k on ".an";
	setAttr -k on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 9 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :lightList1;
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
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -s 52 ".dsm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -s 3 ".aovs";
	setAttr ".aovs[0].aov_name" -type "string" "direct";
	setAttr ".aovs[1].aov_name" -type "string" "specular";
	setAttr ".aovs[2].aov_name" -type "string" "sss";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
	setAttr ".aal" -type "attributeAlias" {"ai_aov_direct","aiCustomAOVs[0].aovName"
		,"ai_aov_specular","aiCustomAOVs[1].aovName","ai_aov_sss","aiCustomAOVs[2].aovName"
		} ;
select -ne :initialParticleSE;
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -s 3 ".aovs";
	setAttr ".aovs[0].aov_name" -type "string" "direct";
	setAttr ".aovs[1].aov_name" -type "string" "specular";
	setAttr ".aovs[2].aov_name" -type "string" "sss";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
	setAttr ".aal" -type "attributeAlias" {"ai_aov_direct","aiCustomAOVs[0].aovName"
		,"ai_aov_specular","aiCustomAOVs[1].aovName","ai_aov_sss","aiCustomAOVs[2].aovName"
		} ;
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
	setAttr -av -cb on ".imfkey" -type "string" "png";
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
	setAttr -av -cb on ".pff";
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
	setAttr -av -cb on ".mb";
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
	setAttr -cb on ".hbl" -type "string" "BrickIt_bin";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w" 128;
	setAttr -av -k on ".h" 128;
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al" yes;
	setAttr -av -k on ".dar" 1;
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -cb on ".isu";
	setAttr -av -cb on ".pdu";
select -ne :defaultLightSet;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "C:/Program Files/Autodesk/Maya2023/resources/OCIO-configs/Maya-legacy/config.ocio";
	setAttr ".vtn" -type "string" "sRGB gamma (legacy)";
	setAttr ".vn" -type "string" "sRGB gamma";
	setAttr ".dn" -type "string" "legacy";
	setAttr ".wsn" -type "string" "scene-linear Rec 709/sRGB";
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
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "polySoftEdge17.out" "Bolt_CShape.i";
connectAttr "polySurfaceShape31.o" "polySoftEdge17.ip";
connectAttr "Bolt_CShape.wm" "polySoftEdge17.mp";
connectAttr "Bolt_CShape.iog" ":initialShadingGroup.dsm" -na;
// End of Bolt_C.ma
