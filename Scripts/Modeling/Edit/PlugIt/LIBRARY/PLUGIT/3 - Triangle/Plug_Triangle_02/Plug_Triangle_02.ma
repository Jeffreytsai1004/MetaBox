//Maya ASCII 2023 scene
//Name: Plug_Triangle_02.ma
//Last modified: Wed, Feb 08, 2023 12:45:02 PM
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
fileInfo "UUID" "8B705560-4AED-350A-D21D-95BB3279782D";
createNode transform -n "Plug_Mesh";
	rename -uid "C4CE5D55-4990-3F78-FBA2-B190D07DB52A";
createNode mesh -n "Plug_MeshShape" -p "Plug_Mesh";
	rename -uid "CDEE1201-4C11-451D-07AF-AB99B566956C";
	setAttr -k off ".v";
	setAttr -s 8 ".iog[0].og";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 3 "e[250]" "e[252]" "e[254:255]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 4 "f[55:66]" "f[70:72]" "f[87:88]" "f[90:116]";
	setAttr ".iog[0].og[4].gcl" -type "componentList" 1 "f[0:123]";
	setAttr ".iog[0].og[5].gcl" -type "componentList" 2 "f[0:116]" "f[121:123]";
	setAttr ".iog[0].og[6].gcl" -type "componentList" 1 "e[244:247]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.50008365511894226 0.59369304776191711 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 143 ".uvst[0].uvsp[0:142]" -type "float2" 0.053353965 0.82623243
		 0.09591645 0.86879492 0.15015429 0.88332796 0.052307963 0.71385288 0.40215349 0.10790253
		 0.5 0.052618623 0.44185829 0.068197608 0.03777492 0.76809072 0.84984565 0.88332796
		 0.90408349 0.86879492 0.94664598 0.82623243 0.59784651 0.10790253 0.94769204 0.71385288
		 0.55814171 0.068197608 0.96222508 0.76809072 0.081240535 0.72583711 0.077686608 0.72436512
		 0.070729017 0.72148311 0.45793033 0.096034884 0.45595706 0.092617035 0.5 0.080815792
		 0.5 0.084762335 0.45209122 0.085921288 0.5 0.073084235 0.88801169 0.84095752 0.88998497
		 0.84437537 0.84626007 0.85609317 0.84575796 0.85227942 0.8938508 0.85107112 0.84724307
		 0.8635596 0.54206967 0.096034884 0.54404294 0.092617035 0.57605326 0.12462497 0.5730015
		 0.12696671 0.54790878 0.085921288 0.58202791 0.12004054 0.32507718 0.88332796 0.32637846
		 0.8635596 0.5 0.8635596 0.5 0.88332784 0.41797209 0.12004054 0.058240533 0.76809072
		 0.071077645 0.81599951 0.10614926 0.85107112 0.15275693 0.8635596 0.33673507 0.7478236
		 0.5 0.74677813 0.67492282 0.88332796 0.67362154 0.8635596 0.92927098 0.72148311 0.94175947
		 0.76809072 0.92892241 0.81599951 0.06597209 0.76809072 0.069918752 0.76809072 0.077773392
		 0.81213379 0.081191242 0.8101604 0.11001503 0.84437537 0.11198831 0.84095752 0.15373993
		 0.85609317 0.15424204 0.85227942 0.32686996 0.85609341 0.5 0.85609376 0.32712102
		 0.85227942 0.5 0.85227942 0.42394668 0.12462497 0.4269985 0.12696671 0.92231345 0.72436512
		 0.91875947 0.72583711 0.93402791 0.76809072 0.93008125 0.76809072 0.92222667 0.81213379
		 0.9188087 0.8101604 0.67313004 0.85609341 0.67287898 0.85227942 0.66326499 0.7478236
		 0.5 0.42560655 0.5 0.41540021 0.51309311 0.41753155 0.50798798 0.42658603 0.5 0.40622073
		 0.5157094 0.40901691 0.48429054 0.40901691 0.48698324 0.41763425 0.47276986 0.42634809
		 0.46873367 0.41907233 0.49226272 0.42692351 0.48077321 0.43324733 0.20056432 0.786111
		 0.20316589 0.78108752 0.35065043 0.78116536 0.35020059 0.78634405 0.20480037 0.77486992
		 0.34883219 0.77496994 0.5 0.78626752 0.5 0.78112447 0.64934957 0.78116536 0.64979947
		 0.78634405 0.5 0.77485538 0.65116787 0.77496994 0.79947329 0.78616476 0.7968365 0.78105867
		 0.81696141 0.77759075 0.82135081 0.78201258 0.7951715 0.77470183 0.81239557 0.77194512
		 0.8388617 0.7622999 0.83057022 0.76281667 0.82464278 0.74962032 0.83319712 0.74720395
		 0.81984115 0.76486468 0.81314445 0.75320864 0.17864919 0.78201258 0.81866407 0.76709902
		 0.51887727 0.43345845 0.16640705 0.77367616 0.16130561 0.76228929 0.16680288 0.74720395
		 0.53126633 0.41907233 0.83359289 0.77367616 0.18685549 0.75320864 0.18760437 0.77194512
		 0.18133599 0.76709902 0.17986143 0.76479185 0.18303859 0.77759075 0.17292988 0.77083611
		 0.16939372 0.76279354 0.17535722 0.74962032 0.5271256 0.42641127 0.82707012 0.77083611
		 0.5 0 0.5 0 1 1 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 0 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 137 ".vt[0:136]"  1.19561219 8.7000137e-23 1.2791388 0.3343944 0 -1.37090945
		 1.53000629 1.1600019e-22 0.69995075 1.57967329 5.8000096e-23 0.88531125 1.52643132 1.1600019e-22 1.084012628
		 1.38097227 8.7000137e-23 1.22947168 1.9102587e-16 -3.2196528e-39 -1.55984461 0.19870165 0 -1.50660253
		 -1.5664932e-16 3.2196528e-39 1.2791388 -9.9499392e-17 -0.77750653 0.81247437 -1.19561219 2.9000048e-23 1.2791388
		 -0.3343944 1.4500024e-23 -1.37090945 -1.53000629 -2.9000048e-23 0.69995075 -1.57967329 0 0.88531125
		 -1.52643132 0 1.084012628 -1.38097227 0 1.22947168 -0.19870165 7.2500119e-24 -1.50660253
		 1.46705127 1.1600019e-22 0.72602767 1.44327354 -0.012208894 0.73587668 1.43112791 -0.042873994 0.74090761
		 1.50973117 8.7000137e-23 0.88531125 1.4833082 -0.01220026 0.88531125 1.4698205 -0.042873997 0.88531125
		 1.46585977 1.1600019e-22 1.049041152 1.44297683 -0.012200268 1.035829782 1.43129623 -0.042874005 1.029085994
		 1.34600115 8.7000137e-23 1.16890001 1.33278966 -0.012200268 1.14601696 1.32604587 -0.042874001 1.13433635
		 1.18671751 5.8000096e-23 1.21157992 1.18335807 -0.012208899 1.18606329 1.18164217 -0.042874005 1.17302907
		 0.16373016 0 -1.44603097 0.15051867 -0.012200265 -1.42314804 0.14377487 -0.042874001 -1.41146743
		 1.7757277e-16 -0.042874005 -1.44999182 1.7922455e-16 -0.012200272 -1.46347952 1.8246043e-16 -3.2196528e-39 -1.48990238
		 0.28033388 7.2500119e-24 -1.32942736 0.25991535 -0.012208897 -1.31375957 0.24948561 -0.042874005 -1.30575657
		 -1.4837575e-16 3.2196528e-39 1.21157992 -1.4525105e-16 -0.012211659 1.18606484 -1.4365462e-16 -0.042874005 1.17302907
		 -1.46705127 0 0.72602767 -1.44327354 -0.012208894 0.73587668 -1.43112791 -0.042873994 0.74090761
		 -1.50973117 -2.9000048e-23 0.88531125 -1.4833082 -0.01220026 0.88531125 -1.4698205 -0.042873997 0.88531125
		 -1.46585977 2.9000048e-23 1.049041152 -1.44297683 -0.012200268 1.035829782 -1.43129623 -0.042874001 1.029085994
		 -1.34600115 0 1.16890001 -1.33278966 -0.012200264 1.14601696 -1.32604587 -0.042873997 1.13433635
		 -1.18164217 -0.042874005 1.17302907 -1.18335807 -0.012208899 1.18606329 -1.18671751 2.9000048e-23 1.21157992
		 -0.16373016 3.625006e-24 -1.44603097 -0.15051867 -0.012200265 -1.42314804 -0.14377487 -0.042874001 -1.41146743
		 -0.24948561 -0.042874005 -1.30575657 -0.25991535 -0.012208897 -1.31375957 -0.28033388 1.4500024e-23 -1.32942736
		 0.5978061 0 1.2791388 0.59335876 0 1.21157992 0.59167904 -0.01221028 1.18606389 0.59082109 -0.042874005 1.17302907
		 0.55796468 -0.77287859 0.81604731 -0.5978061 1.4500024e-23 1.2791388 -0.59335876 1.4500024e-23 1.21157992
		 -0.59167904 -0.01221028 1.18606389 -0.59082109 -0.042874005 1.17302907 -0.55796468 -0.77287859 0.81604731
		 4.3033489e-17 -2.19228959 -0.35139477 2.3040324e-10 -2.21606612 -0.32002345 7.5062595e-10 -2.19940996 -0.28514293
		 -0.027299384 -2.19507337 -0.28179535 -0.044746373 -2.20742345 -0.31273955 -0.053687673 -2.1816988 -0.34183869
		 0.026442552 -2.19357944 -0.28064218 0.044485319 -2.20696712 -0.31238857 0.053687681 -2.1816988 -0.34183869
		 0.10685394 -2.14061809 -0.30747387 0.093060181 -2.16987753 -0.28260857 0.065708295 -2.16558194 -0.2590301
		 1.0088568926 -0.65313822 0.90847903 1.014442801 -0.6213938 0.92972803 1.023333669 -0.58662707 0.94689614
		 0.51194566 -0.58471191 0.94769239 0.5104084 -0.62077558 0.92999429 0.5166223 -0.6526953 0.90882099
		 1.067624927 -0.66608673 0.89848375 1.083228707 -0.63625008 0.9177776 1.098229766 -0.60226518 0.93288946
		 1.089047432 -0.6875416 0.88192177 1.11777556 -0.66392219 0.89469337 1.1400677 -0.63070285 0.90439922
		 1.094086885 -0.69775605 0.87403697 1.12986064 -0.69465095 0.86720759 1.15750206 -0.66561162 0.86548418
		 1.070184231 -0.74903709 0.83445096 1.1094799 -0.74812359 0.82218754 1.13871479 -0.71581286 0.81392962
		 -1.1125051e-16 -0.65320206 0.9084295 -1.1387432e-16 -0.62109017 0.92985451 -1.1602678e-16 -0.5853411 0.94743067
		 -0.51194566 -0.58471191 0.94769239 -0.5104084 -0.62077558 0.92999429 -0.5166223 -0.6526953 0.90882099
		 -0.10685394 -2.14061809 -0.30747387 -0.092702642 -2.16959763 -0.28239268 -0.064513683 -2.16464734 -0.25830868
		 -1.0087606907 -0.65388203 0.90790486 -1.014450908 -0.62146997 0.92962968 -1.023462296 -0.58618557 0.94707966
		 -1.098229766 -0.60226518 0.93288946 -1.083228707 -0.63625008 0.9177776 -1.067624927 -0.66608673 0.89848375
		 -1.1400677 -0.63070285 0.90439922 -1.11777556 -0.66392219 0.89469337 -1.089047432 -0.6875416 0.88192177
		 -1.093070149 -0.69743353 0.8742857 -1.1297375 -0.69424659 0.8672865 -1.15807366 -0.66447186 0.86552048
		 -1.13871479 -0.71581286 0.81392962 -1.1094799 -0.74812359 0.82218754 -1.070184231 -0.74903709 0.83445096
		 -2 -1.6391277e-07 2 2 -1.6391277e-07 2 -2 -1.6391277e-07 -2 2 -1.6391277e-07 -2 -2.19846773 1.2068358e-07 2.19846773
		 -2.19846773 1.4873604e-07 -2.19846773 2.19846773 1.4894431e-07 2.19846773 2.19846773 1.620956e-07 -2.19846773;
	setAttr -s 260 ".ed";
	setAttr ".ed[0:165]"  2 3 1 3 4 1 4 5 1 5 0 1 6 7 1 7 1 1 1 2 1 8 65 1 12 11 1
		 12 13 1 13 14 1 14 15 1 15 10 1 6 16 1 16 11 1 8 70 1 21 20 1 20 17 1 19 22 1 22 21 1
		 19 18 1 18 17 1 17 38 1 40 19 1 24 23 1 23 20 1 22 25 1 25 24 1 27 26 1 26 23 1 25 28 1
		 28 27 1 30 29 1 29 26 1 28 31 1 31 30 1 42 41 1 41 66 1 31 68 1 43 42 1 39 38 1 38 32 1
		 34 40 1 40 39 1 34 33 1 33 36 1 36 35 1 35 34 1 33 32 1 32 37 1 37 36 1 61 35 1 37 59 1
		 58 71 1 43 73 1 46 62 1 46 45 1 49 46 1 45 44 1 44 47 1 64 44 1 49 48 1 52 49 1 48 47 1
		 47 50 1 52 51 1 55 52 1 51 50 1 50 53 1 55 54 1 54 57 1 57 56 1 56 55 1 54 53 1 53 58 1
		 58 57 1 61 60 1 60 63 1 63 62 1 62 61 1 60 59 1 59 64 1 64 63 1 41 8 1 0 29 1 1 38 1
		 20 3 1 2 17 1 23 4 1 26 5 1 32 7 1 6 37 1 9 74 1 58 10 1 64 11 1 44 12 1 13 47 1
		 14 50 1 15 53 1 16 59 1 18 21 1 21 24 1 24 27 1 27 30 1 30 67 1 33 39 1 18 39 1 45 48 1
		 48 51 1 51 54 1 42 72 1 36 60 1 45 63 1 65 0 1 66 29 1 67 42 1 68 43 1 69 9 1 65 66 1
		 66 67 1 67 68 1 70 10 1 71 41 1 72 57 1 73 56 1 70 71 1 71 72 1 72 73 1 83 75 1 77 81 1
		 77 76 1 76 79 1 79 78 1 78 77 1 76 75 1 75 80 1 80 79 1 113 78 1 80 111 1 83 82 1
		 82 85 1 85 84 1 84 83 1 82 81 1 81 86 1 86 85 1 86 102 1 94 93 1 93 87 1 89 95 1
		 95 94 1 89 88 1 88 91 1 91 90 1 90 89 1 88 87 1 87 92 1 92 91 1 107 90 1 92 105 1
		 97 96 1 96 93 1 95 98 1 98 97 1 100 99 1 99 96 1;
	setAttr ".ed[166:259]" 98 101 1 101 100 1 103 102 1 102 99 1 101 104 1 104 103 1
		 104 84 1 107 106 1 106 109 1 109 108 1 108 107 1 106 105 1 105 110 1 110 109 1 116 108 1
		 110 114 1 113 112 1 112 111 1 111 126 1 116 115 1 115 118 1 118 117 1 117 116 1 115 114 1
		 114 119 1 119 118 1 121 120 1 120 117 1 119 122 1 122 121 1 125 120 1 122 123 1 125 124 1
		 124 127 1 127 126 1 126 125 1 124 123 1 123 128 1 128 127 1 128 113 1 83 34 1 35 75 1
		 28 95 1 56 116 1 92 69 1 9 105 1 110 74 1 74 128 1 61 80 1 25 98 1 22 101 1 19 104 1
		 40 84 1 68 90 1 62 111 1 73 108 1 102 69 1 76 82 1 88 94 1 94 97 1 97 100 1 100 103 1
		 103 85 1 91 106 1 79 112 1 109 115 1 118 121 1 121 124 1 112 127 1 126 46 1 125 49 1
		 120 52 1 117 55 1 107 43 1 89 31 1 69 86 1 74 113 1 9 77 1 129 131 0 129 130 0 130 132 0
		 131 132 0 129 133 1 131 134 1 133 134 0 130 135 1 133 135 0 132 136 1 135 136 0 134 136 0
		 11 131 0 14 129 0 1 132 0 4 130 0;
	setAttr -s 124 -ch 516 ".fc[0:123]" -type "polyFaces" 
		f 6 -11 -10 8 256 -245 -258
		mu 0 6 10 14 12 11 130 129
		f 4 20 106 -44 23
		mu 0 4 15 16 64 65
		f 4 21 22 -41 -107
		mu 0 4 16 17 40 64
		f 4 44 45 46 47
		mu 0 4 18 19 20 21
		f 4 48 49 50 -46
		mu 0 4 19 22 23 20
		f 4 69 70 71 72
		mu 0 4 24 25 26 27
		f 4 73 74 75 -71
		mu 0 4 25 28 29 26
		f 4 76 77 78 79
		mu 0 4 30 31 32 33
		f 4 80 81 82 -78
		mu 0 4 31 34 35 32
		f 4 118 -38 83 7
		mu 0 4 36 37 38 39
		f 4 -7 85 -23 -88
		mu 0 4 3 4 40 17
		f 4 -18 86 -1 87
		mu 0 4 17 41 7 3
		f 4 -26 88 -2 -87
		mu 0 4 41 42 0 7
		f 4 -30 89 -3 -89
		mu 0 4 42 43 1 0
		f 4 -34 -85 -4 -90
		mu 0 4 43 44 2 1
		f 4 -50 90 -5 91
		mu 0 4 23 22 6 5
		f 4 -42 -86 -6 -91
		mu 0 4 22 40 4 6
		f 4 93 -122 125 -54
		mu 0 4 29 8 47 48
		f 4 -61 94 -9 -96
		mu 0 4 49 35 11 12
		f 4 95 9 96 -60
		mu 0 4 49 12 14 50
		f 4 -97 10 97 -65
		mu 0 4 50 14 10 51
		f 4 -98 11 98 -69
		mu 0 4 51 10 9 28
		f 4 -99 12 -94 -75
		mu 0 4 28 9 8 29
		f 4 -92 13 99 -53
		mu 0 4 23 5 13 34
		f 4 -100 14 -95 -82
		mu 0 4 34 13 11 35
		f 4 -22 100 16 17
		mu 0 4 17 16 52 41
		f 4 -21 18 19 -101
		mu 0 4 16 15 53 52
		f 4 -17 101 24 25
		mu 0 4 41 52 54 42
		f 4 -20 26 27 -102
		mu 0 4 52 53 55 54
		f 4 -25 102 28 29
		mu 0 4 42 54 56 43
		f 4 -28 30 31 -103
		mu 0 4 54 55 57 56
		f 4 -29 103 32 33
		mu 0 4 43 56 58 44
		f 4 -32 34 35 -104
		mu 0 4 56 57 59 58
		f 4 119 115 36 37
		mu 0 4 37 60 61 38
		f 4 120 116 39 -116
		mu 0 4 60 62 63 61
		f 4 -49 105 40 41
		mu 0 4 22 19 64 40
		f 4 -45 42 43 -106
		mu 0 4 19 18 65 64
		f 4 56 107 -62 57
		mu 0 4 67 66 68 69
		f 4 58 59 -64 -108
		mu 0 4 66 49 50 68
		f 4 61 108 -66 62
		mu 0 4 69 68 70 71
		f 4 63 64 -68 -109
		mu 0 4 68 50 51 70
		f 4 65 109 -70 66
		mu 0 4 71 70 25 24
		f 4 67 68 -74 -110
		mu 0 4 70 51 28 25
		f 4 126 123 -76 53
		mu 0 4 48 72 26 29
		f 4 127 124 -72 -124
		mu 0 4 72 73 27 26
		f 4 -47 111 -77 51
		mu 0 4 21 20 31 30
		f 4 -51 52 -81 -112
		mu 0 4 20 23 34 31
		f 4 112 -83 60 -59
		mu 0 4 66 32 35 49
		f 4 -79 -113 -57 55
		mu 0 4 33 32 66 67
		f 4 -115 -119 113 84
		mu 0 4 44 37 36 2
		f 4 -33 104 -120 114
		mu 0 4 44 58 60 37
		f 4 -36 38 -121 -105
		mu 0 4 58 59 62 60
		f 4 -126 -16 -84 -123
		mu 0 4 48 47 39 38
		f 4 -37 110 -127 122
		mu 0 4 38 61 72 48
		f 4 -40 54 -128 -111
		mu 0 4 61 63 73 72
		f 4 130 131 132 133
		mu 0 4 75 76 77 78
		f 4 134 135 136 -132
		mu 0 4 76 79 80 77
		f 4 139 140 141 142
		mu 0 4 81 82 83 84
		f 4 143 144 145 -141
		mu 0 4 82 85 86 83
		f 4 151 152 153 154
		mu 0 4 87 88 89 90
		f 4 155 156 157 -153
		mu 0 4 88 91 92 89
		f 4 173 174 175 176
		mu 0 4 93 94 95 96
		f 4 177 178 179 -175
		mu 0 4 94 97 98 95
		f 4 185 186 187 188
		mu 0 4 99 100 101 102
		f 4 189 190 191 -187
		mu 0 4 100 103 104 101
		f 4 198 199 200 201
		mu 0 4 105 106 107 108
		f 4 202 203 204 -200
		mu 0 4 106 109 110 107
		f 4 -129 206 -48 207
		mu 0 4 79 81 18 21
		f 4 -150 240 -35 208
		mu 0 4 111 87 59 57
		f 4 -189 238 -73 209
		mu 0 4 99 102 24 27
		f 4 210 117 211 -160
		mu 0 4 92 45 46 97
		f 7 -204 -198 -195 -191 -182 212 213
		mu 0 7 110 109 112 104 103 98 74
		f 3 242 -206 -214
		mu 0 3 74 113 110
		f 4 -136 -208 -52 214
		mu 0 4 80 79 21 30
		f 4 -163 -209 -31 215
		mu 0 4 114 111 57 55
		f 4 -167 -216 -27 216
		mu 0 4 115 114 55 53
		f 4 -171 -217 -19 217
		mu 0 4 116 115 53 15
		f 4 -173 -218 -24 218
		mu 0 4 84 116 15 65
		f 4 -207 -143 -219 -43
		mu 0 4 18 81 84 65
		f 4 -159 239 -117 219
		mu 0 4 90 93 63 62
		f 4 -139 -215 -80 220
		mu 0 4 117 80 30 33
		f 4 -181 -210 -125 221
		mu 0 4 96 99 27 73
		f 4 -194 237 -67 -239
		mu 0 4 102 118 71 24
		f 4 -197 236 -63 -238
		mu 0 4 118 105 69 71
		f 4 -202 235 -58 -237
		mu 0 4 105 108 67 69
		f 4 -56 -236 -185 -221
		mu 0 4 33 67 108 117
		f 4 -155 -220 -39 -241
		mu 0 4 87 90 62 59
		f 7 222 -211 -157 -149 -162 -166 -170
		mu 0 7 119 45 92 91 120 121 122
		f 3 -223 -147 -242
		mu 0 3 45 119 86
		f 4 -177 -222 -55 -240
		mu 0 4 93 96 73 63
		f 4 -213 -179 -212 92
		mu 0 4 74 98 97 46
		f 5 243 -134 -138 -243 -93
		mu 0 5 46 75 78 113 74
		f 4 -135 223 -140 128
		mu 0 4 79 76 82 81
		f 4 -131 129 -144 -224
		mu 0 4 76 75 85 82
		f 4 -142 -229 -172 172
		mu 0 4 84 83 126 116
		f 4 -146 146 -169 228
		mu 0 4 83 86 119 126
		f 4 -156 224 147 148
		mu 0 4 91 88 123 120
		f 4 -152 149 150 -225
		mu 0 4 88 87 111 123
		f 4 -148 225 160 161
		mu 0 4 120 123 124 121
		f 4 -151 162 163 -226
		mu 0 4 123 111 114 124
		f 4 -161 226 164 165
		mu 0 4 121 124 125 122
		f 4 -164 166 167 -227
		mu 0 4 124 114 115 125
		f 4 -165 227 168 169
		mu 0 4 122 125 126 119
		f 4 -168 170 171 -228
		mu 0 4 125 115 116 126
		f 4 -154 229 -174 158
		mu 0 4 90 89 94 93
		f 4 -158 159 -178 -230
		mu 0 4 89 92 97 94
		f 4 -133 230 -183 137
		mu 0 4 78 77 127 113
		f 4 -137 138 -184 -231
		mu 0 4 77 80 117 127
		f 4 -176 231 -186 180
		mu 0 4 96 95 100 99
		f 4 -180 181 -190 -232
		mu 0 4 95 98 103 100
		f 4 -188 232 192 193
		mu 0 4 102 101 128 118
		f 4 -192 194 195 -233
		mu 0 4 101 104 112 128
		f 4 -193 233 -199 196
		mu 0 4 118 128 106 105
		f 4 -196 197 -203 -234
		mu 0 4 128 112 109 106
		f 4 -201 -235 183 184
		mu 0 4 108 107 127 117
		f 4 -205 205 182 234
		mu 0 4 107 110 113 127
		f 5 241 -145 -130 -244 -118
		mu 0 5 45 86 85 75 46
		f 4 244 249 -251 -249
		mu 0 4 129 130 131 132
		f 4 -246 248 252 -252
		mu 0 4 133 129 134 135
		f 4 -247 251 254 -254
		mu 0 4 136 137 138 139
		f 4 247 253 -256 -250
		mu 0 4 130 140 141 142
		f 7 258 -248 -257 -15 -14 4 5
		mu 0 7 4 140 130 11 13 5 6
		f 6 259 246 -259 6 0 1
		mu 0 6 0 137 136 4 3 7
		f 11 257 245 -260 2 3 -114 -8 15 121 -13 -12
		mu 0 11 10 129 133 0 1 2 36 39 47 8 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 2 
		129 0 
		130 0 ;
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
createNode transform -n "PlugIt_PlugCountNumber_18";
	rename -uid "B993BBC9-4545-A048-3EC1-F19485BAAFCE";
createNode groupId -n "groupId2";
	rename -uid "A21002C0-4E5E-3A9E-9086-2D9B68B334DA";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_EdgeBorder_set";
	rename -uid "8139E85E-4B6B-8D9F-012F-3AB64608B83B";
	setAttr ".ihi" 0;
	setAttr ".an" -type "string" "gCharacterSet";
createNode groupId -n "groupId4";
	rename -uid "D3FBE51C-4E1B-EAE4-00B9-568FD7E7CA75";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Hole_set";
	rename -uid "36E93D43-4301-EB4A-18E2-B49AD726FD8B";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "1EB081C2-455F-D82F-022E-35B1DC2A4396";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_AllFaces_set";
	rename -uid "E7691590-489C-5876-9EE1-F9AA4048A6F8";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "84796DD6-4A5B-9181-DA7D-3387A3B50531";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_Selection_set";
	rename -uid "5E52784B-4B66-FA1A-5952-779BEFF7723F";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "70EB775C-4D2B-863A-4AAA-B2BF3F388238";
	setAttr ".ihi" 0;
createNode objectSet -n "Plug_ExtraSecure_set";
	rename -uid "D12B232E-4B3F-6F86-7352-0D8195C083BB";
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
	rename -uid "E9286A17-4CB0-1ACE-251F-3884A60A038D";
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
// End of Plug_Triangle_02.ma
