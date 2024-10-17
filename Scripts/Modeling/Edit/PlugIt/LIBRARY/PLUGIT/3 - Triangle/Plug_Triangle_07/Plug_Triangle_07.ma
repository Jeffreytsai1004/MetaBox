//Maya ASCII 2023 scene
//Name: Plug_Triangle_07.ma
//Last modified: Wed, Feb 08, 2023 12:52:44 PM
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
fileInfo "UUID" "18C7D537-45A1-EF5C-75B8-7183224ACA04";
createNode transform -n "Plug_Mesh";
	rename -uid "6411DE43-4C31-F296-E92D-0AB9280DC47F";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "4CDBC0FE-47D0-B8DF-2752-C8A41CC10347";
	setAttr -k off ".v";
	setAttr -s 7 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "e[6]" "e[8]" "e[10:11]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[0:133]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[4:133]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 1 "e[0:3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.026656499132514 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 208 ".uvst[0].uvsp[0:207]" -type "float2" 0.5 0 0.5 0 1 1 0
		 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 0 1 0.578125 0.97906601 0.578125 0.97906601
		 0.578125 0.97906601 0.578125 0.97906601 0 0 0.025619 0.053098999 0 0.019029999 0
		 0 0.578125 0.70843399 0.578125 0.70843399 0.578125 0.70843399 0.578125 0.70843399
		 1 0 0.99758297 0.039205998 0.72433901 0.038688999 0 0 0.421875 0.97906601 0.421875
		 0.97906601 0.421875 0.97906601 0.421875 0.97906601 1 0 1 0.031406999 0.044613 0.053312998
		 0 0 0.34375 0.84375 0.34375 0.84375 0.403218 0.74074799 0.403216 0.74075198 0.345759
		 0.840271 0.40261999 0.74178499 0.57463503 0.70843399 0.578125 0.70843399 0.578125
		 0.70843399 0.57452101 0.70843399 0.578125 0.70843399 0.578125 0.70843399 0.578125
		 0.70843399 0.578125 0.70843399 0.64050603 0.81647998 0.640508 0.81648302 0.57997102
		 0.711631 0.64008898 0.815759 0.65625 0.84375 0.65625 0.84375 0.59520102 0.94949001
		 0.59520102 0.94949001 0.65455502 0.84668499 0.59587997 0.94831401 0.421821 0.70852703
		 0.421875 0.70843399 0.41238701 0.72486699 0.41202199 0.72549999 0.421875 0.70843399
		 0.41239801 0.72484797 0.656196 0.843844 0.65625 0.84375 0.64825702 0.82990497 0.64803803
		 0.82952702 0.65625 0.84375 0.64826602 0.82992202 0.578125 0.97906601 0.578125 0.97906601
		 0.58690703 0.96385503 0.58730102 0.96317297 0.578125 0.97906601 0.58688903 0.96388698
		 0.421875 0.70843399 0.45419699 0.70843399 0.43829599 0.70843399 0.65625 0.84375 0.58012003
		 0.97561198 0.58010399 0.97563899 0.63699502 0.877101 0.64639997 0.86080998 0.578125
		 0.97906601 0.42524701 0.97906601 0.425235 0.97906601 0.542615 0.97906601 0.55978203
		 0.97906601 0.89494401 0.018138999 0.40319401 0.74079102 0.34375 0.84375 0.34375 0.84375
		 0.34375 0.84375 0.45332599 0.70843399 0.45335999 0.70843399 0.64052498 0.816513 0.578125
		 0.70843399 0.578125 0.70843399 0.578125 0.70843399 0.578125 0.97906601 0.578125 0.97906601
		 0.63756901 0.87610698 0.637591 0.876068 0.421875 0.97906601 0.421875 0.97906601 0.54397303
		 0.97906601 0.54397303 0.97906601 0.59520102 0.94949001 0.65625 0.84375 0.65625 0.84375
		 0.65625 0.84375 0.437621 0.70843399 0.43784401 0.70843399 0.421875 0.70843399 0.41252401
		 0.72462898 0.64689898 0.85994601 0.64677101 0.86016798 0.65625 0.84375 0.648377 0.83011299
		 0.56101203 0.97906601 0.56058598 0.97906601 0.578125 0.97906601 0.58668101 0.96424699
		 0.345745 0.84029502 0.579871 0.71145701 0.65456003 0.84667701 1 0 0.34375 0.84375
		 0.34375 0.84375 0 0.013707 0 0 0 0 0 0.012165 0.40319201 0.740794 0 0.029727999 0
		 0 0 0 0 0.053312 0.65625 0.84375 0.65625 0.84375 0.45332199 0.70843399 0 0.011213
		 0 0 0.63756698 0.87611097 1 0 1 0.014622 0.239691 0.012936 0.23914801 0 0.004063
		 0.048232999 0 0 0 0 0.046808999 0.046808999 0.578125 0.70843399 0.578125 0.70843399
		 0 0 0.011796 0.011796 0.640526 0.81651598 0.54397303 0.97906601 0 0 0 0 0 0 0 0 0.59520102
		 0.94949001 0.34375 0.84375 0.578125 0.97906601 0.578125 0.97906601 0.453363 0.70843399
		 0.578125 0.70843399 0.421875 0.97906601 0.421875 0.97906601 0.63759297 0.87606502
		 0.54397303 0.97906601 0.65625 0.84375 0.43760201 0.70843399 0 0.01129 0 0 0.43786299
		 0.70843399 0.64691001 0.859927 0.121164 0.012529 0.119546 0 0.64675999 0.86018801
		 0.56104898 0.97906601 0 0 0 0 0.56054801 0.97906601 0.421875 0.70843399 0 0.011537
		 0 0 0.41253501 0.72460997 0 0.011839 0 0 0.65625 0.84375 0.012177 0.012177 0 0 0.648386
		 0.83012998 0.011932 0.011932 0 0 0.578125 0.97906601 0 0 0 0 0.58666301 0.96427798
		 0 0 0 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 153 ".vt[0:152]"  -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2
		 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773 -2.19846773 1.4873604e-07 -2.19846773
		 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773 -0.068369776 -0.28625965 0.31338483
		 -0.068369776 0 -1.50171936 -0.068369776 -0.014198454 -1.4655869 -0.068369776 -0.052814573 -1.44081867
		 0.1094782 0 -1.39823198 0.084155299 -0.013859287 -1.37744188 0.06514889 -0.051465068 -1.36419404
		 0.50818229 0 -0.39762896 0.47972506 -0.0057753995 -0.38463381 0.45361403 -0.022769596 -0.37069446
		 1.63434851 0 1.44747794 1.60305762 -0.014198454 1.42941117 1.58160496 -0.052814573 1.4170289
		 1.58201492 -0.051443573 1.26308239 1.6030463 -0.013858092 1.25349033 1.63386106 0 1.24261463
		 -0.20189072 -0.051463872 -1.36419404 -0.22087435 -0.013859287 -1.37748063 -0.24613348 0 -1.3983767
		 -1.77109504 0 1.44747794 -1.73979962 -0.014198454 1.42941117 -1.71835124 -0.052814573 1.4170289
		 -1.77037287 0 1.24216592 -1.73972666 -0.013855704 1.25336957 -1.71875668 -0.051443573 1.26308239
		 -0.96639311 0 0.17404054 -0.94062829 -0.0055950675 0.19175085 -0.91536003 -0.022082901 0.20732568
		 -1.58523345 -0.051651366 1.49427891 -1.58657277 -0.013897503 1.51783979 -1.59020829 0 1.55135381
		 1.45346653 0 1.55135381 1.44982648 -0.013897503 1.51783979 1.44849169 -0.051651366 1.49428225
		 0.25554556 0 1.2132144 0.26123565 -0.0057336004 1.18235528 0.26317635 -0.0225606 1.15268052
		 -0.03892624 -0.28625965 -1.30050981 -0.0097879367 -0.2722666 -1.31996262 0.010726413 -0.23422611 -1.33277678
		 0.1908659 -0.26297891 -0.21853614 0.1637025 -0.28032184 -0.20594873 0.13327265 -0.28625965 -0.19749674
		 -0.068369776 -0.28625965 -1.31780553 -0.068369776 -0.2720612 -1.35394025 -0.068369776 -0.23344629 -1.37870955
		 1.52781558 -0.23344629 1.3859725 1.50636959 -0.2720612 1.37358892 1.47507191 -0.28625965 1.35552216
		 1.47549558 -0.28625965 1.31982708 1.50639474 -0.27232274 1.30545723 1.5275172 -0.23444825 1.29454184
		 -1.61148345 -0.28625965 1.32016313 -1.64293838 -0.27232394 1.30555069 -1.66426361 -0.23444825 1.29454184
		 -0.64142764 -0.26395103 0.36590645 -0.61682451 -0.28058696 0.38272154 -0.59349477 -0.28625965 0.40376893
		 -1.61181831 -0.28625965 1.35552216 -1.64311147 -0.2720612 1.37358892 -1.66456199 -0.23344506 1.3859725
		 -0.098353155 -0.28625965 -1.30087757 -0.1270974 -0.2722654 -1.32006061 -0.14746824 -0.23422611 -1.33277321
		 -1.58408999 -0.28625965 1.37168479 -1.58492601 -0.2721436 1.40719187 -1.58523345 -0.23375678 1.43166745
		 1.44733441 -0.28625965 1.37141705 1.44817948 -0.2721436 1.40712357 1.44849169 -0.23375678 1.43166745
		 0.26317635 -0.26328108 0.8425746 0.26654536 -0.28038156 0.81279397 0.27635148 -0.28625965 0.78268421
		 0.77859998 -0.02209962 0.20733592 0.80388188 -0.0055986498 0.19175541 0.82965124 0 0.17404054
		 0.45675063 -0.28625965 0.40376893 0.48011914 -0.2805559 0.38270107 0.50482702 -0.26383042 0.36582443
		 -0.5903331 -0.022791089 -0.37068081 -0.61646235 -0.0057801763 -0.38462925 -0.64492416 0 -0.39762896
		 -0.27001446 -0.28625965 -0.19749674 -0.30044433 -0.28032184 -0.2059453 -0.32761002 -0.26297891 -0.21853955
		 -0.3999182 -0.022643004 1.15257454 -0.39797744 -0.0057550976 1.18232894 -0.39228737 0 1.21321332
		 -0.4130933 -0.28625965 0.78268421 -0.40328714 -0.28031707 0.81287938 -0.3999182 -0.26302907 0.8429004
		 0.68341988 -0.020895815 0.071392491 0.70896375 -0.0052845618 0.055995334 0.73533666 0 0.039238304
		 0.33925211 -0.28625965 0.27792206 0.36443833 -0.28096074 0.25938264 0.38961321 -0.26532561 0.2433659
		 0.59718031 -0.020639051 -0.070813917 0.62309319 -0.005217684 -0.085684881 0.65030444 0 -0.10109001
		 0.29747173 -0.26558837 0.10246127 0.27143586 -0.28103361 0.11722177 0.24394903 -0.28625965 0.13225445
		 0.52036881 -0.021251703 -0.21847121 0.54656643 -0.0053777136 -0.23276249 0.57456809 0 -0.24679063
		 0.17416468 -0.28625965 -0.028206661 0.20380639 -0.28077924 -0.03962668 0.2308559 -0.2646437 -0.053199269
		 -0.65713799 -0.02122901 -0.21848831 -0.68330145 -0.0053717424 -0.23275906 -0.71124613 0 -0.24676099
		 -0.31137574 -0.28625965 -0.028360417 -0.34061882 -0.28082103 -0.039639208 -0.36740184 -0.26480851 -0.053085379
		 -0.73393124 -0.020631885 -0.070818469 -0.75983727 -0.0052152951 -0.085684881 -0.78703713 0 -0.10108203
		 -0.43427733 -0.26553822 0.1024271 -0.4081777 -0.28102165 0.11722177 -0.38062477 -0.28625965 0.13228862
		 -0.82012528 -0.020924477 0.071412988 -0.84570551 -0.0052917274 0.055995334 -0.87211955 0 0.039213251
		 -0.47571379 -0.28625965 0.27813846 -0.50118017 -0.28090224 0.25939628 -0.52663064 -0.26509634 0.24320416
		 -0.23591958 -0.02122901 1.11858213 -0.23464626 -0.0053741308 1.14844596 -0.23134565 0 1.17955804
		 -0.24629064 -0.28625965 0.72251582 -0.2406484 -0.2808091 0.75339437 -0.23857327 -0.26477507 0.78340852
		 -0.068369776 -0.020752506 1.10722136 -0.068369776 -0.0052463464 1.13713181 -0.068369776 0 1.16844893
		 -0.068369776 -0.26542357 0.76307184 -0.068369776 -0.28099182 0.73303604 -0.068369776 -0.28625965 0.70157433
		 0.099177748 -0.021312609 1.11846828 0.097895309 -0.0053956276 1.14847553 0.094567366 0 1.17981207
		 0.10973331 -0.28625965 0.72174591 0.1039544 -0.28074342 0.75329077 0.10182689 -0.26451471 0.78376842;
	setAttr -s 286 ".ed";
	setAttr ".ed[0:165]"  0 2 0 0 1 0 1 3 0 2 3 0 0 4 1 2 5 1 4 5 0 1 6 1 4 6 0
		 3 7 1 6 7 0 5 7 0 11 10 1 10 25 1 25 24 1 24 11 1 10 9 1 9 26 1 26 25 1 20 19 1 19 22 1
		 22 21 1 21 20 1 19 18 1 18 23 1 23 22 1 29 28 1 28 37 1 37 36 1 36 29 1 28 27 1 27 38 1
		 38 37 1 47 46 1 46 49 1 49 48 1 48 47 1 46 45 1 45 50 1 50 49 1 56 55 1 55 58 1 58 57 1
		 57 56 1 55 54 1 54 59 1 59 58 1 62 61 1 61 64 1 64 63 1 63 62 1 61 60 1 60 65 1 65 64 1
		 77 76 1 76 79 1 79 78 1 78 77 1 76 75 1 75 80 1 80 79 1 110 109 1 109 115 1 115 114 1
		 114 110 1 109 108 1 108 116 1 116 115 1 128 127 1 127 133 1 133 132 1 132 128 1 127 126 1
		 126 134 1 134 133 1 146 145 1 145 151 1 151 150 1 150 146 1 145 144 1 144 152 1 152 151 1
		 8 56 1 57 84 1 84 102 1 102 110 1 110 8 1 8 51 1 51 69 1 69 90 1 90 120 1 120 128 1
		 128 8 1 8 66 1 66 72 1 72 96 1 96 138 1 138 146 1 146 8 1 9 12 1 48 17 1 17 14 1
		 14 47 1 14 11 1 11 53 1 53 47 1 21 59 1 54 20 1 21 81 1 81 86 1 86 59 1 63 35 1 35 32 1
		 32 62 1 32 29 1 29 68 1 68 62 1 24 71 1 71 53 1 24 87 1 87 92 1 92 71 1 36 74 1 74 68 1
		 36 93 1 93 98 1 98 74 1 78 44 1 44 41 1 41 77 1 41 20 1 54 77 1 81 99 1 99 104 1
		 104 86 1 99 105 1 105 108 1 108 104 1 105 111 1 111 116 1 111 17 1 48 116 1 87 117 1
		 117 122 1 122 92 1 117 123 1 123 126 1 126 122 1 123 129 1 129 134 1 129 35 1 63 134 1
		 93 135 1 135 140 1 140 98 1 135 141 1 141 144 1 144 140 1 141 147 1 147 152 1 147 44 1
		 78 152 1 114 50 1 45 51 1 132 65 1 60 66 1;
	setAttr ".ed[166:285]" 150 80 1 75 56 1 10 13 1 13 12 1 14 13 1 13 16 1 16 15 1
		 15 12 1 17 16 1 19 40 1 40 39 1 39 18 1 41 40 1 22 82 1 82 81 1 23 83 1 83 82 1 25 88 1
		 88 87 1 26 89 1 89 88 1 28 31 1 31 30 1 30 27 1 32 31 1 31 34 1 34 33 1 33 30 1 35 34 1
		 37 94 1 94 93 1 38 95 1 95 94 1 40 43 1 43 42 1 42 39 1 44 43 1 46 52 1 52 51 1 53 52 1
		 52 70 1 70 69 1 71 70 1 58 85 1 85 84 1 86 85 1 61 67 1 67 66 1 68 67 1 67 73 1 73 72 1
		 74 73 1 70 91 1 91 90 1 92 91 1 73 97 1 97 96 1 98 97 1 55 76 1 82 100 1 100 99 1
		 83 101 1 101 100 1 85 103 1 103 102 1 104 103 1 88 118 1 118 117 1 89 119 1 119 118 1
		 91 121 1 121 120 1 122 121 1 94 136 1 136 135 1 95 137 1 137 136 1 97 139 1 139 138 1
		 140 139 1 100 106 1 106 105 1 101 107 1 107 106 1 106 112 1 112 111 1 107 113 1 113 112 1
		 103 109 1 16 112 1 113 15 1 49 115 1 118 124 1 124 123 1 119 125 1 125 124 1 124 130 1
		 130 129 1 125 131 1 131 130 1 121 127 1 34 130 1 131 33 1 64 133 1 136 142 1 142 141 1
		 137 143 1 143 142 1 142 148 1 148 147 1 143 149 1 149 148 1 139 145 1 43 148 1 149 42 1
		 79 151 1 0 27 0 2 26 0 1 18 0 3 12 0;
	setAttr -s 134 -ch 568 ".fc[0:133]" -type "polyFaces" 
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
		mu 0 4 18 19 20 21
		f 4 19 20 21 22
		mu 0 4 22 23 24 25
		f 4 23 24 25 -21
		mu 0 4 26 27 28 29
		f 4 26 27 28 29
		mu 0 4 30 31 32 33
		f 4 30 31 32 -28
		mu 0 4 34 35 36 37
		f 4 33 34 35 36
		mu 0 4 38 39 40 41
		f 4 37 38 39 -35
		mu 0 4 39 42 43 40
		f 4 40 41 42 43
		mu 0 4 44 45 46 47
		f 4 44 45 46 -42
		mu 0 4 45 48 49 46
		f 4 47 48 49 50
		mu 0 4 50 51 52 53
		f 4 51 52 53 -49
		mu 0 4 51 54 55 52
		f 4 54 55 56 57
		mu 0 4 56 57 58 59
		f 4 58 59 60 -56
		mu 0 4 57 60 61 58
		f 4 61 62 63 64
		mu 0 4 62 63 64 65
		f 4 65 66 67 -63
		mu 0 4 63 66 67 64
		f 4 68 69 70 71
		mu 0 4 68 69 70 71
		f 4 72 73 74 -70
		mu 0 4 69 72 73 70
		f 4 75 76 77 78
		mu 0 4 74 75 76 77
		f 4 79 80 81 -77
		mu 0 4 75 78 79 76
		f 6 82 -44 83 84 85 86
		mu 0 6 80 44 47 81 82 62
		f 6 87 88 89 90 91 92
		mu 0 6 83 84 85 86 87 68
		f 6 93 94 95 96 97 98
		mu 0 6 88 89 90 91 92 74
		f 5 -18 99 -286 -4 283
		mu 0 5 20 19 93 11 1
		f 4 100 101 102 -37
		mu 0 4 41 94 95 38
		f 4 103 104 105 -103
		mu 0 4 95 96 97 38
		f 4 -23 106 -46 107
		mu 0 4 22 25 49 48
		f 4 108 109 110 -107
		mu 0 4 25 98 99 49
		f 4 111 112 113 -51
		mu 0 4 53 100 101 50
		f 4 114 115 116 -114
		mu 0 4 101 102 103 50
		f 4 -16 117 118 -105
		mu 0 4 14 17 104 105
		f 4 119 120 121 -118
		mu 0 4 17 106 107 104
		f 4 -30 122 123 -116
		mu 0 4 30 33 108 109
		f 4 124 125 126 -123
		mu 0 4 33 110 111 108
		f 4 127 128 129 -58
		mu 0 4 59 112 113 56
		f 4 130 -108 131 -130
		mu 0 4 113 114 115 56
		f 4 132 133 134 -110
		mu 0 4 98 116 117 99
		f 4 135 136 137 -134
		mu 0 4 116 118 66 117
		f 4 138 139 -67 -137
		mu 0 4 118 119 67 66
		f 4 140 -101 141 -140
		mu 0 4 119 94 41 67
		f 4 142 143 144 -121
		mu 0 4 106 120 121 107
		f 4 145 146 147 -144
		mu 0 4 120 122 72 121
		f 4 148 149 -74 -147
		mu 0 4 122 123 73 72
		f 4 150 -112 151 -150
		mu 0 4 123 100 53 73
		f 4 152 153 154 -126
		mu 0 4 110 124 125 111
		f 4 155 156 157 -154
		mu 0 4 124 126 78 125
		f 4 158 159 -81 -157
		mu 0 4 126 127 79 78
		f 4 160 -128 161 -160
		mu 0 4 127 112 59 79
		f 6 -87 -65 162 -39 163 -88
		mu 0 6 80 62 65 43 42 128
		f 6 -93 -72 164 -53 165 -94
		mu 0 6 83 68 71 55 54 129
		f 6 -99 -79 166 -60 167 -83
		mu 0 6 88 74 77 61 60 130
		f 4 -17 168 169 -100
		mu 0 4 19 18 131 93
		f 4 -13 -104 170 -169
		mu 0 4 132 96 95 133
		f 4 -170 171 172 173
		mu 0 4 134 135 136 137
		f 4 -171 -102 174 -172
		mu 0 4 133 95 94 138
		f 4 -24 175 176 177
		mu 0 4 139 140 141 142
		f 4 -20 -131 178 -176
		mu 0 4 143 114 113 144
		f 4 -22 179 180 -109
		mu 0 4 25 24 145 98
		f 4 -26 181 182 -180
		mu 0 4 29 28 146 147
		f 4 -15 183 184 -120
		mu 0 4 17 16 148 106
		f 4 -19 185 186 -184
		mu 0 4 149 150 151 152
		f 4 -31 187 188 189
		mu 0 4 153 154 155 156
		f 4 -27 -115 190 -188
		mu 0 4 157 102 101 158
		f 4 -189 191 192 193
		mu 0 4 156 155 159 160
		f 4 -191 -113 194 -192
		mu 0 4 158 101 100 161
		f 4 -29 195 196 -125
		mu 0 4 33 32 162 110
		f 4 -33 197 198 -196
		mu 0 4 37 36 163 164
		f 4 -177 199 200 201
		mu 0 4 142 141 165 166
		f 4 -179 -129 202 -200
		mu 0 4 144 113 112 167
		f 4 -38 203 204 -164
		mu 0 4 42 39 168 128
		f 4 -34 -106 205 -204
		mu 0 4 39 38 97 168
		f 4 -205 206 207 -89
		mu 0 4 84 169 170 85
		f 4 -206 -119 208 -207
		mu 0 4 169 105 104 170
		f 4 -43 209 210 -84
		mu 0 4 47 46 171 81
		f 4 -47 -111 211 -210
		mu 0 4 46 49 99 171
		f 4 -52 212 213 -166
		mu 0 4 54 51 172 129
		f 4 -48 -117 214 -213
		mu 0 4 51 50 103 172
		f 4 -214 215 216 -95
		mu 0 4 89 173 174 90
		f 4 -215 -124 217 -216
		mu 0 4 173 109 108 174
		f 4 -208 218 219 -90
		mu 0 4 85 170 175 86
		f 4 -209 -122 220 -219
		mu 0 4 170 104 107 175
		f 4 -217 221 222 -96
		mu 0 4 90 174 176 91
		f 4 -218 -127 223 -222
		mu 0 4 174 108 111 176
		f 4 -45 224 -55 -132
		mu 0 4 115 177 57 56
		f 4 -41 -168 -59 -225
		mu 0 4 177 130 60 57
		f 4 -181 225 226 -133
		mu 0 4 98 145 178 116
		f 4 -183 227 228 -226
		mu 0 4 147 146 179 180
		f 4 -211 229 230 -85
		mu 0 4 81 171 181 82
		f 4 -212 -135 231 -230
		mu 0 4 171 99 117 181
		f 4 -185 232 233 -143
		mu 0 4 106 148 182 120
		f 4 -187 234 235 -233
		mu 0 4 152 151 183 184
		f 4 -220 236 237 -91
		mu 0 4 86 175 185 87
		f 4 -221 -145 238 -237
		mu 0 4 175 107 121 185
		f 4 -197 239 240 -153
		mu 0 4 110 162 186 124
		f 4 -199 241 242 -240
		mu 0 4 164 163 187 188
		f 4 -223 243 244 -97
		mu 0 4 91 176 189 92
		f 4 -224 -155 245 -244
		mu 0 4 176 111 125 189
		f 4 -227 246 247 -136
		mu 0 4 116 178 190 118
		f 4 -229 248 249 -247
		mu 0 4 180 179 191 192
		f 4 -248 250 251 -139
		mu 0 4 118 190 193 119
		f 4 -250 252 253 -251
		mu 0 4 192 191 194 195
		f 4 -231 254 -62 -86
		mu 0 4 82 181 63 62
		f 4 -232 -138 -66 -255
		mu 0 4 181 117 66 63
		f 4 -173 255 -254 256
		mu 0 4 137 136 195 194
		f 4 -175 -141 -252 -256
		mu 0 4 138 94 119 193
		f 4 -36 257 -68 -142
		mu 0 4 41 40 64 67
		f 4 -40 -163 -64 -258
		mu 0 4 40 43 65 64
		f 4 -234 258 259 -146
		mu 0 4 120 182 196 122
		f 4 -236 260 261 -259
		mu 0 4 184 183 197 198
		f 4 -260 262 263 -149
		mu 0 4 122 196 199 123
		f 4 -262 264 265 -263
		mu 0 4 198 197 200 201
		f 4 -238 266 -69 -92
		mu 0 4 87 185 69 68
		f 4 -239 -148 -73 -267
		mu 0 4 185 121 72 69
		f 4 -193 267 -266 268
		mu 0 4 160 159 201 200
		f 4 -195 -151 -264 -268
		mu 0 4 161 100 123 199
		f 4 -50 269 -75 -152
		mu 0 4 53 52 70 73
		f 4 -54 -165 -71 -270
		mu 0 4 52 55 71 70
		f 4 -241 270 271 -156
		mu 0 4 124 186 202 126
		f 4 -243 272 273 -271
		mu 0 4 188 187 203 204
		f 4 -272 274 275 -159
		mu 0 4 126 202 205 127
		f 4 -274 276 277 -275
		mu 0 4 204 203 206 207
		f 4 -245 278 -76 -98
		mu 0 4 92 189 75 74
		f 4 -246 -158 -80 -279
		mu 0 4 189 125 78 75
		f 4 -201 279 -278 280
		mu 0 4 166 165 207 206
		f 4 -203 -161 -276 -280
		mu 0 4 167 112 127 205
		f 4 -57 281 -82 -162
		mu 0 4 59 58 76 79
		f 4 -61 -167 -78 -282
		mu 0 4 58 61 77 76
		f 11 -178 -202 -281 -277 -273 -242 -198 -32 -283 1 284
		mu 0 11 139 142 166 206 203 187 163 36 35 0 4
		f 10 -190 -194 -269 -265 -261 -235 -186 -284 -1 282
		mu 0 10 153 156 160 200 197 183 151 150 1 0
		f 10 -174 -257 -253 -249 -228 -182 -25 -285 2 285
		mu 0 10 134 137 194 191 179 146 28 27 8 7;
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
createNode transform -n "PlugIt_PlugCountNumber_24";
	rename -uid "C804ED30-4BFA-0A84-6927-45AF9147414D";
createNode groupId -n "groupId1";
	rename -uid "441FD6FD-4CF4-2851-BB0B-128410F80147";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "14874761-4E7E-76C1-06AA-5084EDF5730C";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "7851F761-4977-7142-FFC7-A68AFDA42C42";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "14227EBE-4087-D0C5-1218-2B9315F68AD9";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "79B894E4-44F7-D31C-F5C5-AB85DE3C3BF5";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "F77D7F5B-412C-9BD4-DBAA-5EB1569EBD28";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "1635D342-4C82-A9B8-FC4F-3594B3DD2117";
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
	rename -uid "CA2DAB54-40EC-6352-6F74-03951FAB9193";
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
// End of Plug_Triangle_07.ma
