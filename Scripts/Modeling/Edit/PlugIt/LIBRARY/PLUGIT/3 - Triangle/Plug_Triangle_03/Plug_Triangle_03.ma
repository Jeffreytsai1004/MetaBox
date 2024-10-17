//Maya ASCII 2023 scene
//Name: Plug_Triangle_03&.ma
//Last modified: Wed, Feb 08, 2023 12:41:03 PM
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
fileInfo "UUID" "FB1E308F-437C-C7C4-701D-49BB44CEC547";
createNode transform -n "Plug_Mesh";
	rename -uid "E3F7C7C3-441F-8244-F10A-01B9123D6B3D";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "35147355-4AF7-7268-06AC-48A263B5D74D";
	setAttr -k off ".v";
	setAttr -s 8 ".iog[0].og";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 3 "e[261]" "e[263]" "e[265:266]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 2 "f[22:34]" "f[89:124]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[0:131]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 2 "f[0:125]" "f[130:131]";
	setAttr ".iog[0].og[6].gcl" -type "componentList" 1 "e[255:258]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.49974490702152252 0.50034360782592557 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 146 ".uvst[0].uvsp[0:145]" -type "float2" 0.039911069 0.079822138
		 0.45034134 0.90068269 0.54965866 0.90068269 0.96008897 0.079822093 0.079494402 0
		 0.90165436 0 0.45125031 0.90250063 0.12049246 0.078871243 0.9594236 0.081152752 0.5
		 0.83045614 0.87909472 0.079141393 0.55984068 1 0.040576637 0.081153274 0.077273346
		 0 0.90440208 0 0.55051029 0.89897943 0.44015706 1 0.53469586 1 0.50000328 1 0.46531072
		 1 0.062785514 0.017049057 0.049972307 0.036414031 0.043494035 0.059206344 0.03671021
		 0.10416578 0.032823913 0.12873487 0.028347904 0.1536933 0.10608051 0.0012664777 0.095966101
		 0.0012642611 0.086447231 0.00089172379 0.47387832 0.91286033 0.50004262 0.91796976
		 0.52610475 0.91292816 0.55639774 0.91775781 0.55962944 0.94139808 0.56038851 0.96941572
		 0.43960229 0.96943378 0.44015855 0.94079274 0.44338199 0.91729033 0.95283049 0.05951415
		 0.94285476 0.036096472 0.9247005 0.017046798 0.89877081 0.00087989378 0.8926273 0.0012701529
		 0.88588691 0.0012644036 0.97124428 0.1541259 0.96691835 0.12891318 0.96316028 0.10417998
		 0.08691477 0.01795019 0.096645541 0.036591183 0.10858319 0.057161812 0.098968685
		 0.080401398 0.07763081 0.079841547 0.058572687 0.079796061 0.045450363 0.058659006
		 0.052862607 0.036571302 0.065555818 0.017599156 0.51277363 0.85114765 0.52479315
		 0.87139267 0.53688818 0.88697475 0.52504158 0.90925986 0.500166 0.9146809 0.47577542
		 0.91028863 0.4643462 0.89035958 0.47592834 0.87375462 0.4875342 0.85267323 0.9412635
		 0.079824246 0.92178065 0.080099843 0.90053362 0.080600254 0.88637215 0.057338718
		 0.89401942 0.036546994 0.89894813 0.018043252 0.92164099 0.017391661 0.93931699 0.036501564
		 0.95063692 0.05857724 0.023431959 0.1789442 0.019650012 0.12629111 0.029882366 0.057998572
		 0.074197687 0.022891475 0.11623596 0.00068721565 0.87902433 0.00069881993 0.92219275
		 0.022917876 0.96885175 0.057883643 0.9798398 0.12641297 0.9762103 0.17915921 0.058484875
		 0.012693077 0.03154562 0.025456542 0.034578852 0.069068864 0.024634084 0.080334373
		 0.022172701 0.10261565 0.022324126 0.03773183 0.06714081 0.019155495 0.058281351
		 0.011636534 0 0 0.46942744 0.93604249 0.50002557 0.94920707 0.530792 0.93639576 0.53279072
		 0.96725875 0.53288013 0.9900685 0.49980399 0.99466747 0.46673572 0.9893707 0.46736512
		 0.96908516 0.5 1 0.96312803 0.068788379 0.96350372 0.026060566 0.93253505 0.012538412
		 0.93557853 0.011381134 0.92811543 0.018963864 0.97621399 0.037950862 0.97713751 0.1025973
		 0.97434109 0.080198228 1 0 0.058955796 0.016645461 0.059378024 0.02446533 0.082557261
		 0.055137072 0.051855877 0.050218541 0.040681269 0.051451568 0.040443324 0.02805749
		 0 0 0.50001413 0.88010418 0.51349515 0.9154281 0.52127433 0.92096525 0.5001604 0.93536699
		 0.47921169 0.92166471 0.48651949 0.92068636 0.5 1 0.95672232 0.051711868 0.94963372
		 0.048760451 0.91404676 0.055413801 0.93217063 0.026171396 0.93146247 0.016099419
		 0.95379585 0.027917722 1 0 0.5 0 0.5 0 1 1 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1
		 1 0 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 140 ".vt[0:139]"  -1.23914993 -0.16064906 1.24994826 -1.28464246 -0.16683896 1.19729018
		 -1.29901516 -0.17314392 1.12563026 -1.27755952 -0.17799729 1.052132964 -1.29796839 -0.10742494 1.040649533
		 -1.33626842 -0.050246898 1.019156814 -1.38799822 -0.012965903 0.99015832 -1.17646194 -0.010996004 1.41689563
		 -1.17647159 -0.042754423 1.35281861 -1.17648101 -0.09241052 1.3022753 -1.17648983 -0.15631965 1.26939011
		 -0.11724751 -0.18519707 -1.036702156 -0.068008803 -0.18537126 -1.087245822 -4.6031269e-05 -0.18543522 -1.10579741
		 0.067916736 -0.18537126 -1.087245822 0.11715546 -0.18519707 -1.036702156 0.12932539 -0.10791298 -1.077960968
		 0.14376472 -0.048930611 -1.14432132 0.15943958 -0.011835788 -1.23069274 0.17468512 4.2131943e-16 -1.32759964
		 -0.17477719 4.2131943e-16 -1.32759964 -0.1598662 -0.011783469 -1.22985053 -0.14428075 -0.048932973 -1.14300668
		 -0.12971744 -0.107975 -1.076872587 0.10126001 4.4033836e-16 -1.40287745 -3.3669898e-05 4.4731842e-16 -1.43050575
		 -0.10133303 4.403391e-16 -1.40288067 1.29892313 -0.17314392 1.12563026 1.28455007 -0.16683896 1.19729018
		 1.2390579 -0.16064906 1.24994826 1.17639768 -0.15631965 1.26939011 1.17640662 -0.092415519 1.30224705
		 1.1764158 -0.042755168 1.35270953 1.1764257 -0.010995235 1.41665399 1.38766432 -0.012965197 0.99032539
		 1.3360672 -0.050247237 1.019238472 1.29785037 -0.10742858 1.040673852 1.27746761 -0.17799729 1.052132964
		 -0.98479992 -0.66110831 1.087666273 -0.95734358 -0.71155274 1.036502957 -0.92680836 -0.7440657 0.9726755
		 -0.89573759 -0.75624949 0.90158957 -0.97040468 -0.74087441 0.89524412 -1.038046837 -0.7031433 0.895643
		 -1.09230566 -0.64642638 0.90279418 -1.12860537 -0.57528496 0.91615146 -1.14630699 -0.57946324 0.98551607
		 -1.1272682 -0.58523691 1.054453731 -1.076527476 -0.59107679 1.10470366 -1.007514596 -0.59543687 1.12296152
		 0.044076618 -0.7424528 -0.76285678 0.081051469 -0.70510215 -0.82312274 0.10687172 -0.64786237 -0.87125838
		 0.11916548 -0.57543439 -0.90295064 0.069543943 -0.57686156 -0.95486885 0.0015637338 -0.57872373 -0.97473037
		 -0.066321522 -0.58051592 -0.95749557 -0.11510225 -0.58173704 -0.90833819 -0.10381359 -0.65193206 -0.87683731
		 -0.07906305 -0.70717961 -0.82776809 -0.04311889 -0.74314439 -0.7654798 -4.6031269e-05 -0.75624949 -0.696917
		 1.092100143 -0.64645457 0.90261996 1.037629724 -0.70317084 0.89530867 0.96968609 -0.74089283 0.89477265
		 0.89467144 -0.75624949 0.90101504 0.92602754 -0.74406832 0.9723621 0.95683688 -0.71156085 1.036390901
		 0.98452455 -0.66112494 1.087655783 1.0074222088 -0.59543687 1.12296152 1.076410294 -0.59116513 1.10470426
		 1.12714148 -0.58535814 1.054462314 1.14618933 -0.57955265 0.98553139 1.1285131 -0.57528496 0.91615146
		 -1.44686592 -1.5567398e-16 0.95718098 -1.49643874 -2.008508e-16 1.13603723 -1.45622647 -2.4524643e-16 1.31173801
		 -1.33817852 -2.778146e-16 1.44056785 -1.17645311 -2.8984914e-16 1.48809028 1.17643476 -2.901658e-16 1.48768926
		 1.33789146 -2.7819291e-16 1.44018817 1.45573032 -2.4570464e-16 1.3115195 1.49586451 -2.0138106e-16 1.13606262
		 1.44637299 -1.5624338e-16 0.95744675 -1.25234663 -0.095586196 1.27601683 -1.30358589 -0.10038068 1.21379185
		 -1.32176089 -0.10418157 1.13112867 -1.36621308 -0.048343886 1.13477135 -1.42701864 -0.012132898 1.1364038
		 -1.39491451 -0.01214996 1.27426779 -1.30479658 -0.011327622 1.37645626 -1.275015 -0.04432489 1.31950629
		 -1.34180856 -0.046957284 1.24031138 -0.075147539 -0.10824362 -1.13146293 -0.00014757905 -0.10837701 -1.15167522
		 0.074850656 -0.10820462 -1.1320101 0.083157152 -0.049439494 -1.20396233 0.092287071 -0.012246625 -1.29779923
		 -0.00015927714 -0.012443034 -1.32229197 -0.092614323 -0.012221433 -1.29738033 -0.083545201 -0.049445655 -1.20330536
		 -0.00019105087 -0.049700491 -1.22563851 1.3216362 -0.10418667 1.13113272 1.30346727 -0.1003833 1.21378374
		 1.25224161 -0.095591664 1.27599537 1.27487016 -0.044326879 1.31940949 1.30458796 -0.011327559 1.37623274
		 1.39458072 -0.012147904 1.27414346 1.42663586 -0.012134135 1.13642275 1.3659879 -0.048347019 1.13478279
		 1.34160674 -0.046956398 1.24026144 -1.048535347 -0.65163702 1.076397419 -1.012321591 -0.70405662 1.027921677
		 -0.99223727 -0.73283869 0.9603827 -1.057800412 -0.69875604 0.94913 -1.11341906 -0.64244515 0.96523887
		 -1.10214412 -0.63820869 1.034156799 -1.063858747 -0.68544161 1.006978035 0.00067236181 -0.7335878 -0.81793427
		 0.045973759 -0.69981223 -0.86897355 0.064968087 -0.64191318 -0.92236227 0.0012583905 -0.63392633 -0.94854242
		 -0.062519304 -0.64442235 -0.92515898 -0.0441687 -0.7010923 -0.87128729 0.00098889647 -0.68368822 -0.90452677
		 1.11323893 -0.64252168 0.96514505 1.057453752 -0.69880867 0.94891638 0.99167532 -0.73286813 0.96010703
		 1.01193285 -0.70409924 1.027814746 1.048317671 -0.65171587 1.07638216 1.10197389 -0.63831502 1.034124136
		 1.063577533 -0.68551308 1.0068718195 -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773;
	setAttr -s 271 ".ed";
	setAttr ".ed[0:165]"  19 24 1 24 25 1 25 26 1 26 20 1 3 2 1 2 46 1 46 45 1
		 45 3 1 2 1 1 1 47 1 47 46 1 1 0 1 0 48 1 48 47 1 0 10 1 10 49 1 49 48 1 6 21 1 21 20 1
		 20 74 1 6 5 1 5 22 1 22 21 1 5 4 1 4 23 1 23 22 1 4 3 1 3 11 1 11 23 1 10 9 1 9 31 1
		 31 30 1 30 10 1 9 8 1 8 32 1 32 31 1 8 7 1 7 33 1 33 32 1 15 14 1 14 54 1 54 53 1
		 53 15 1 14 13 1 13 55 1 55 54 1 13 12 1 12 56 1 56 55 1 12 11 1 11 57 1 57 56 1 19 18 1
		 18 34 1 18 17 1 17 35 1 35 34 1 17 16 1 16 36 1 36 35 1 16 15 1 15 37 1 37 36 1 30 29 1
		 29 70 1 70 69 1 69 30 1 29 28 1 28 71 1 71 70 1 28 27 1 27 72 1 72 71 1 27 37 1 37 73 1
		 73 72 1 41 40 1 40 66 1 66 65 1 65 41 1 40 39 1 39 67 1 67 66 1 39 38 1 38 68 1 68 67 1
		 38 49 1 49 69 1 69 68 1 45 44 1 44 58 1 58 57 1 57 45 1 44 43 1 43 59 1 59 58 1 43 42 1
		 42 60 1 60 59 1 42 41 1 41 61 1 61 60 1 53 52 1 52 62 1 62 73 1 73 53 1 52 51 1 51 63 1
		 63 62 1 51 50 1 50 64 1 64 63 1 50 61 1 61 65 1 65 64 1 74 6 1 78 79 1 7 78 1 78 77 1
		 77 76 1 76 75 1 75 74 1 79 33 1 83 19 1 34 83 1 83 82 1 82 81 1 81 80 1 80 79 1 0 84 1
		 84 9 1 1 85 1 85 84 1 2 86 1 86 85 1 4 86 1 5 87 1 87 86 1 6 88 1 88 87 1 75 88 1
		 76 89 1 89 88 1 77 90 1 90 89 1 7 90 1 8 91 1 91 90 1 84 91 1 85 92 1 92 91 1 87 92 1
		 89 92 1 12 93 1 93 23 1 13 94 1 94 93 1 14 95 1 95 94 1 16 95 1 17 96 1 96 95 1 18 97 1
		 97 96 1 24 97 1 25 98 1;
	setAttr ".ed[166:270]" 98 97 1 26 99 1 99 98 1 21 99 1 22 100 1 100 99 1 93 100 1
		 94 101 1 101 100 1 96 101 1 98 101 1 27 102 1 102 36 1 28 103 1 103 102 1 29 104 1
		 104 103 1 31 104 1 32 105 1 105 104 1 33 106 1 106 105 1 80 106 1 81 107 1 107 106 1
		 82 108 1 108 107 1 34 108 1 35 109 1 109 108 1 102 109 1 103 110 1 110 109 1 105 110 1
		 107 110 1 38 111 1 111 48 1 39 112 1 112 111 1 40 113 1 113 112 1 42 113 1 43 114 1
		 114 113 1 44 115 1 115 114 1 46 115 1 47 116 1 116 115 1 111 116 1 112 117 1 117 116 1
		 114 117 1 50 118 1 118 60 1 51 119 1 119 118 1 52 120 1 120 119 1 54 120 1 55 121 1
		 121 120 1 56 122 1 122 121 1 58 122 1 59 123 1 123 122 1 118 123 1 119 124 1 124 123 1
		 121 124 1 62 125 1 125 72 1 63 126 1 126 125 1 64 127 1 127 126 1 66 127 1 67 128 1
		 128 127 1 68 129 1 129 128 1 70 129 1 71 130 1 130 129 1 125 130 1 126 131 1 131 130 1
		 128 131 1 132 134 0 132 133 0 133 135 0 134 135 0 132 136 1 134 137 1 136 137 0 133 138 1
		 136 138 0 135 139 1 138 139 0 137 139 0 20 134 0 76 132 0 19 135 0 81 133 0;
	setAttr -s 132 -ch 538 ".fc[0:131]" -type "polyFaces" 
		f 6 -124 125 126 270 257 -270
		mu 0 6 11 83 82 81 140 139
		f 4 4 5 6 7
		mu 0 4 0 22 53 12
		f 4 8 9 10 -6
		mu 0 4 22 21 54 53
		f 4 11 12 13 -10
		mu 0 4 21 20 55 54
		f 4 14 15 16 -13
		mu 0 4 20 13 4 55
		f 4 20 21 22 -18
		mu 0 4 25 24 36 35
		f 4 23 24 25 -22
		mu 0 4 24 23 37 36
		f 4 26 27 28 -25
		mu 0 4 23 0 1 37
		f 4 29 30 31 32
		mu 0 4 13 28 41 14
		f 4 33 34 35 -31
		mu 0 4 28 27 42 41
		f 4 36 37 38 -35
		mu 0 4 27 26 43 42
		f 4 39 40 41 42
		mu 0 4 2 31 59 15
		f 4 43 44 45 -41
		mu 0 4 31 30 60 59
		f 4 46 47 48 -45
		mu 0 4 30 29 61 60
		f 4 49 50 51 -48
		mu 0 4 29 1 6 61
		f 4 54 55 56 -54
		mu 0 4 34 33 45 44
		f 4 57 58 59 -56
		mu 0 4 33 32 46 45
		f 4 60 61 62 -59
		mu 0 4 32 2 3 46
		f 4 63 64 65 66
		mu 0 4 14 40 71 5
		f 4 67 68 69 -65
		mu 0 4 40 39 72 71
		f 4 70 71 72 -69
		mu 0 4 39 38 73 72
		f 4 73 74 75 -72
		mu 0 4 38 3 8 73
		f 4 76 77 78 79
		mu 0 4 7 49 68 10
		f 4 80 81 82 -78
		mu 0 4 49 48 69 68
		f 4 83 84 85 -82
		mu 0 4 48 47 70 69
		f 4 86 87 88 -85
		mu 0 4 47 4 5 70
		f 4 89 90 91 92
		mu 0 4 12 52 62 6
		f 4 93 94 95 -91
		mu 0 4 52 51 63 62
		f 4 96 97 98 -95
		mu 0 4 51 50 64 63
		f 4 99 100 101 -98
		mu 0 4 50 7 9 64
		f 4 102 103 104 105
		mu 0 4 15 58 65 8
		f 4 106 107 108 -104
		mu 0 4 58 57 66 65
		f 4 109 110 111 -108
		mu 0 4 57 56 67 66
		f 4 112 113 114 -111
		mu 0 4 56 9 10 67
		f 3 -101 -80 -114
		mu 0 3 9 7 10
		f 4 -51 -28 -8 -93
		mu 0 4 6 1 0 12
		f 4 -33 -67 -88 -16
		mu 0 4 13 14 5 4
		f 4 -62 -43 -106 -75
		mu 0 4 3 2 15 8
		f 4 17 18 19 115
		mu 0 4 25 35 16 74
		f 4 117 116 122 -38
		mu 0 4 26 78 79 43
		f 4 52 53 124 123
		mu 0 4 11 34 44 83
		f 4 -30 -15 129 130
		mu 0 4 28 13 20 84
		f 4 -130 -12 131 132
		mu 0 4 84 20 21 85
		f 4 -132 -9 133 134
		mu 0 4 85 21 22 86
		f 4 -5 -27 135 -134
		mu 0 4 22 0 23 86
		f 4 -136 -24 136 137
		mu 0 4 86 23 24 87
		f 4 -137 -21 138 139
		mu 0 4 87 24 25 88
		f 4 -116 -122 140 -139
		mu 0 4 25 74 75 88
		f 4 -141 -121 141 142
		mu 0 4 88 75 76 89
		f 4 -142 -120 143 144
		mu 0 4 89 76 77 90
		f 4 -119 -118 145 -144
		mu 0 4 77 78 26 90
		f 4 -146 -37 146 147
		mu 0 4 90 26 27 91
		f 4 -147 -34 -131 148
		mu 0 4 91 27 28 84
		f 4 -149 -133 149 150
		mu 0 4 91 84 85 92
		f 4 -135 -138 151 -150
		mu 0 4 85 86 87 92
		f 4 -140 -143 152 -152
		mu 0 4 87 88 89 92
		f 4 -145 -148 -151 -153
		mu 0 4 89 90 91 92
		f 4 -29 -50 153 154
		mu 0 4 37 1 29 93
		f 4 -154 -47 155 156
		mu 0 4 93 29 30 94
		f 4 -156 -44 157 158
		mu 0 4 94 30 31 95
		f 4 -40 -61 159 -158
		mu 0 4 31 2 32 95
		f 4 -160 -58 160 161
		mu 0 4 95 32 33 96
		f 4 -161 -55 162 163
		mu 0 4 96 33 34 97
		f 4 -53 0 164 -163
		mu 0 4 34 11 17 97
		f 4 -165 1 165 166
		mu 0 4 97 17 18 98
		f 4 -166 2 167 168
		mu 0 4 98 18 19 99
		f 4 3 -19 169 -168
		mu 0 4 19 16 35 99
		f 4 -170 -23 170 171
		mu 0 4 99 35 36 100
		f 4 -171 -26 -155 172
		mu 0 4 100 36 37 93
		f 4 -173 -157 173 174
		mu 0 4 100 93 94 101
		f 4 -159 -162 175 -174
		mu 0 4 94 95 96 101
		f 4 -164 -167 176 -176
		mu 0 4 96 97 98 101
		f 4 -169 -172 -175 -177
		mu 0 4 98 99 100 101
		f 4 -63 -74 177 178
		mu 0 4 46 3 38 102
		f 4 -178 -71 179 180
		mu 0 4 102 38 39 103
		f 4 -180 -68 181 182
		mu 0 4 103 39 40 104
		f 4 -64 -32 183 -182
		mu 0 4 40 14 41 104
		f 4 -184 -36 184 185
		mu 0 4 104 41 42 105
		f 4 -185 -39 186 187
		mu 0 4 105 42 43 106
		f 4 -123 -129 188 -187
		mu 0 4 43 79 80 106
		f 4 -189 -128 189 190
		mu 0 4 106 80 81 107
		f 4 -190 -127 191 192
		mu 0 4 107 81 82 108
		f 4 -126 -125 193 -192
		mu 0 4 82 83 44 108
		f 4 -194 -57 194 195
		mu 0 4 108 44 45 109
		f 4 -195 -60 -179 196
		mu 0 4 109 45 46 102
		f 4 -197 -181 197 198
		mu 0 4 109 102 103 110
		f 4 -183 -186 199 -198
		mu 0 4 103 104 105 110
		f 4 -188 -191 200 -200
		mu 0 4 105 106 107 110
		f 4 -193 -196 -199 -201
		mu 0 4 107 108 109 110
		f 4 -17 -87 201 202
		mu 0 4 55 4 47 111
		f 4 -202 -84 203 204
		mu 0 4 111 47 48 112
		f 4 -204 -81 205 206
		mu 0 4 112 48 49 113
		f 4 -77 -100 207 -206
		mu 0 4 49 7 50 113
		f 4 -208 -97 208 209
		mu 0 4 113 50 51 114
		f 4 -209 -94 210 211
		mu 0 4 114 51 52 115
		f 4 -90 -7 212 -211
		mu 0 4 52 12 53 115
		f 4 -213 -11 213 214
		mu 0 4 115 53 54 116
		f 4 -214 -14 -203 215
		mu 0 4 116 54 55 111
		f 4 -216 -205 216 217
		mu 0 4 116 111 112 117
		f 4 -207 -210 218 -217
		mu 0 4 112 113 114 117
		f 4 -212 -215 -218 -219
		mu 0 4 114 115 116 117
		f 4 -102 -113 219 220
		mu 0 4 64 9 56 118
		f 4 -220 -110 221 222
		mu 0 4 118 56 57 119
		f 4 -222 -107 223 224
		mu 0 4 119 57 58 120
		f 4 -103 -42 225 -224
		mu 0 4 58 15 59 120
		f 4 -226 -46 226 227
		mu 0 4 120 59 60 121
		f 4 -227 -49 228 229
		mu 0 4 121 60 61 122
		f 4 -52 -92 230 -229
		mu 0 4 61 6 62 122
		f 4 -231 -96 231 232
		mu 0 4 122 62 63 123
		f 4 -232 -99 -221 233
		mu 0 4 123 63 64 118
		f 4 -234 -223 234 235
		mu 0 4 123 118 119 124
		f 4 -225 -228 236 -235
		mu 0 4 119 120 121 124
		f 4 -230 -233 -236 -237
		mu 0 4 121 122 123 124
		f 4 -76 -105 237 238
		mu 0 4 73 8 65 125
		f 4 -238 -109 239 240
		mu 0 4 125 65 66 126
		f 4 -240 -112 241 242
		mu 0 4 126 66 67 127
		f 4 -115 -79 243 -242
		mu 0 4 67 10 68 127
		f 4 -244 -83 244 245
		mu 0 4 127 68 69 128
		f 4 -245 -86 246 247
		mu 0 4 128 69 70 129
		f 4 -89 -66 248 -247
		mu 0 4 70 5 71 129
		f 4 -249 -70 249 250
		mu 0 4 129 71 72 130
		f 4 -250 -73 -239 251
		mu 0 4 130 72 73 125
		f 4 -252 -241 252 253
		mu 0 4 130 125 126 131
		f 4 -243 -246 254 -253
		mu 0 4 126 127 128 131
		f 4 -248 -251 -254 -255
		mu 0 4 128 129 130 131
		f 8 127 128 -117 118 119 268 256 -271
		mu 0 8 81 80 79 78 77 76 132 136
		f 4 255 260 -262 -260
		mu 0 4 132 133 134 135
		f 4 -257 259 263 -263
		mu 0 4 136 132 137 138
		f 4 -258 262 265 -265
		mu 0 4 139 140 141 142
		f 4 258 264 -267 -261
		mu 0 4 133 143 144 145
		f 6 267 -256 -269 120 121 -20
		mu 0 6 16 133 132 76 75 74
		f 7 269 -259 -268 -4 -3 -2 -1
		mu 0 7 11 143 133 16 19 18 17;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 2 
		132 0 
		133 0 ;
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
createNode transform -n "PlugIt_PlugCountNumber_15";
	rename -uid "3A5B4FE1-4AF5-4877-F600-F3B6421EBD6D";
createNode groupId -n "groupId2";
	rename -uid "D1180723-488C-4606-0975-1DA20B030322";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "2FD88EF5-4DE4-4EEF-191D-DD80655AFB54";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Hole_set";
	rename -uid "E4236828-401C-EBC3-99A2-A5A3FD69B01E";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "20C16CE4-4B13-0491-9F03-448CEF69D917";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "1BFD9A2A-4D24-37C2-B0DC-68B835129C3A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "5DCF16BF-4673-C2AF-B68E-C08A47A888FF";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "496A9DB0-4278-AE9B-94F4-A88C772D8A6E";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "0B2602B4-4172-AB5D-718C-B1BD8D0FE75F";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "D1C92E71-49FD-8474-2AF6-3FAD59C5928D";
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
	rename -uid "1617C88F-4CAB-30AB-0EC5-728B39CC1F81";
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
connectAttr "Plug_Hole_set.mwc" "Plug_MeshShape.iog.og[3].gco";
connectAttr "groupId5.id" "Plug_MeshShape.iog.og[4].gid";
connectAttr "Plug_AllFaces_set.mwc" "Plug_MeshShape.iog.og[4].gco";
connectAttr "groupId6.id" "Plug_MeshShape.iog.og[5].gid";
connectAttr "Plug_Selection_set.mwc" "Plug_MeshShape.iog.og[5].gco";
connectAttr "groupId7.id" "Plug_MeshShape.iog.og[6].gid";
connectAttr "Plug_ExtraSecure_set.mwc" "Plug_MeshShape.iog.og[6].gco";
connectAttr "groupId2.msg" "Plug_EdgeBorder_set.gn" -na;
connectAttr "Plug_MeshShape.iog.og[1]" "Plug_EdgeBorder_set.dsm" -na;
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
// End of Plug_Triangle_03&.ma
