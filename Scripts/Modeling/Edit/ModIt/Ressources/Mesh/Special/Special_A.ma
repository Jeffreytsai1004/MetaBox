//Maya ASCII 2023 scene
//Name: Special_A.ma
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
fileInfo "UUID" "9A17120D-4F2E-D371-4702-ABA3D4E309A7";
createNode transform -n "Special_A";
	rename -uid "C9B23972-4F60-E3F7-4199-849A63DB55B6";
createNode mesh -n "Special_AShape" -p "Special_A";
	rename -uid "8B702C33-426B-0B9D-35EB-4DA13BB75E8B";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.48809218406677246 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 713 ".pt";
	setAttr ".pt[0]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[2]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[3]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[4]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[5]" -type "float3" 0 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[6]" -type "float3" 5.9604645e-08 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[7]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[8]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[9]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[10]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[11]" -type "float3" 2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[12]" -type "float3" 2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[13]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[14]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[15]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[16]" -type "float3" 2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[17]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[18]" -type "float3" -2.9802322e-08 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[19]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[20]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[21]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[22]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[23]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[24]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[26]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[27]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[29]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[31]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[32]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[34]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[36]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[37]" -type "float3" 0 -2.3283064e-10 2.9802322e-08 ;
	setAttr ".pt[39]" -type "float3" 1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[40]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[41]" -type "float3" 1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[42]" -type "float3" -1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[43]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[44]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[45]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[46]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[47]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[48]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[49]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[50]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[51]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[52]" -type "float3" -2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[53]" -type "float3" 0 -2.3283064e-10 1.4901161e-08 ;
	setAttr ".pt[54]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[55]" -type "float3" 0 -1.8626451e-09 -7.1054274e-15 ;
	setAttr ".pt[57]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[58]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[59]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[60]" -type "float3" -2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[61]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[62]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[63]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[64]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[65]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[66]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[67]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[68]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[69]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[70]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[71]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[72]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[73]" -type "float3" 1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[74]" -type "float3" -1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[76]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[77]" -type "float3" 0 -2.3283064e-10 -2.9802322e-08 ;
	setAttr ".pt[79]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[80]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[81]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[83]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[84]" -type "float3" -2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[86]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[87]" -type "float3" -5.9604645e-08 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[88]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[89]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[91]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[92]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[93]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[94]" -type "float3" -7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[95]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[96]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[97]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[98]" -type "float3" 2.9802322e-08 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[99]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[100]" -type "float3" 0 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[101]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[103]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[104]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[105]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[107]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[108]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[109]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[110]" -type "float3" 2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[111]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[112]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[113]" -type "float3" 0 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[114]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[115]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[116]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[117]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[118]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[119]" -type "float3" -7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[120]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[122]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[123]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[124]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[126]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[128]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[129]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[130]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[131]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[132]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[133]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[134]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[135]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[136]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[137]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[138]" -type "float3" -2.9802322e-08 7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[141]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[143]" -type "float3" -1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[146]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[149]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[151]" -type "float3" 0 -7.4505806e-09 -7.1054274e-15 ;
	setAttr ".pt[152]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[155]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[158]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[161]" -type "float3" -1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[165]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[167]" -type "float3" 0 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[168]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[170]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[171]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[172]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[173]" -type "float3" -1.4901161e-08 2.9802322e-08 0 ;
	setAttr ".pt[174]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[176]" -type "float3" 2.9802322e-08 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[177]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[179]" -type "float3" -2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[180]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[181]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[182]" -type "float3" 2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[183]" -type "float3" 2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[184]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[185]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[186]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[187]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[188]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[189]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[190]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[191]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[192]" -type "float3" 0 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[193]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[195]" -type "float3" 2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[196]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[198]" -type "float3" 2.9802322e-08 2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[199]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[201]" -type "float3" -1.4901161e-08 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[202]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[204]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[205]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[207]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[208]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[209]" -type "float3" 1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[210]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[211]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[212]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[214]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[215]" -type "float3" -1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[216]" -type "float3" 1.1920929e-07 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[217]" -type "float3" 1.1920929e-07 0 7.1054274e-15 ;
	setAttr ".pt[218]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[219]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[220]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[221]" -type "float3" 1.1920929e-07 5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[222]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[224]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[225]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[226]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[227]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[228]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[229]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[230]" -type "float3" 0 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[231]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[232]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[233]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[234]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[235]" -type "float3" -5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[236]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[238]" -type "float3" -5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[239]" -type "float3" -5.9604645e-08 0 -7.4505806e-09 ;
	setAttr ".pt[240]" -type "float3" -5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[241]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[243]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[244]" -type "float3" -5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[245]" -type "float3" -5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[246]" -type "float3" 5.9604645e-08 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[247]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[248]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[249]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[250]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[252]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[253]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[254]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[256]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[257]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[258]" -type "float3" -5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[259]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[261]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[262]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[263]" -type "float3" 5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[264]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[265]" -type "float3" 5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[266]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[267]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[268]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[269]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[270]" -type "float3" -5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[271]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[272]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[273]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[274]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[275]" -type "float3" 0 -5.9604645e-08 -1.4901161e-08 ;
	setAttr ".pt[280]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[285]" -type "float3" -5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[286]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[288]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[290]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[291]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[292]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[293]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[294]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[295]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[296]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[297]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[298]" -type "float3" -2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[299]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[300]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[301]" -type "float3" 0 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[303]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[305]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[306]" -type "float3" -5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[307]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[308]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[309]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[310]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[311]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[312]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[313]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[314]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[315]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[316]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[317]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[318]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[319]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[320]" -type "float3" 7.4505806e-09 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[321]" -type "float3" -7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[322]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[323]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[324]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[325]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[326]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[327]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[328]" -type "float3" 2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[329]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[331]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[332]" -type "float3" 2.9802322e-08 0 -7.1054274e-15 ;
	setAttr ".pt[333]" -type "float3" 0 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[334]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[335]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[337]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[338]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[339]" -type "float3" 0 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[340]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[341]" -type "float3" 1.4901161e-08 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[342]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[343]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[344]" -type "float3" 7.4505806e-09 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[345]" -type "float3" -7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[346]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[347]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[348]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[349]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[350]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[351]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[352]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[353]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[354]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[355]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[356]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[357]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[359]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[360]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[361]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[362]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[363]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[364]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[365]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[366]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[368]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[369]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[370]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[371]" -type "float3" 0 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[372]" -type "float3" -5.9604645e-08 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[373]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[374]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[375]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[376]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[377]" -type "float3" -2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[378]" -type "float3" -2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[379]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[380]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[381]" -type "float3" -2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[382]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[383]" -type "float3" 2.9802322e-08 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[384]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[385]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[386]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[387]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[389]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[390]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[392]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[394]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[395]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[397]" -type "float3" -1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[398]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[399]" -type "float3" -1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[400]" -type "float3" 1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[401]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[402]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[403]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[404]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[405]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[406]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[407]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[408]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[409]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[410]" -type "float3" 2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[411]" -type "float3" 0 -2.3283064e-10 1.4901161e-08 ;
	setAttr ".pt[412]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[413]" -type "float3" 0 -1.8626451e-09 -7.1054274e-15 ;
	setAttr ".pt[415]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[416]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[417]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[418]" -type "float3" 2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[419]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[420]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[421]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[422]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[423]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[424]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[425]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[426]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[427]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[428]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[429]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[430]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[431]" -type "float3" -1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[432]" -type "float3" 1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[433]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[434]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[435]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[437]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[438]" -type "float3" 2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[440]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[441]" -type "float3" 5.9604645e-08 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[442]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[443]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[444]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[445]" -type "float3" 7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[446]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[447]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[448]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[449]" -type "float3" -2.9802322e-08 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[450]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[451]" -type "float3" 0 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[452]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[454]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[455]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[456]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[458]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[459]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[460]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[461]" -type "float3" -2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[462]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[463]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[464]" -type "float3" 0 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[465]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[466]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[467]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[468]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[469]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[470]" -type "float3" 7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[471]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[472]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[474]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[476]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[477]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[478]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[479]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[480]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[481]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[482]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[483]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[484]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[485]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[486]" -type "float3" 2.9802322e-08 7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[488]" -type "float3" 1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[491]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[494]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[496]" -type "float3" 0 -7.4505806e-09 -7.1054274e-15 ;
	setAttr ".pt[497]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[500]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[503]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[506]" -type "float3" 1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[509]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[510]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[511]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[512]" -type "float3" 1.4901161e-08 2.9802322e-08 0 ;
	setAttr ".pt[513]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[515]" -type "float3" -2.9802322e-08 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[516]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[518]" -type "float3" 2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[519]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[520]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[521]" -type "float3" -2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[522]" -type "float3" -2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[523]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[524]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[525]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[526]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[527]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[528]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[529]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[530]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[531]" -type "float3" 0 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[532]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[534]" -type "float3" -2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[535]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[537]" -type "float3" -2.9802322e-08 2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[538]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[540]" -type "float3" 1.4901161e-08 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[541]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[543]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[544]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[545]" -type "float3" -1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[546]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[547]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[548]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[550]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[551]" -type "float3" 1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[552]" -type "float3" -1.1920929e-07 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[553]" -type "float3" -1.1920929e-07 0 7.1054274e-15 ;
	setAttr ".pt[554]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[555]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[556]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[557]" -type "float3" -1.1920929e-07 5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[558]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[560]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[561]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[562]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[563]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[564]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[565]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[566]" -type "float3" 0 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[567]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[568]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[569]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[570]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[571]" -type "float3" 5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[572]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[574]" -type "float3" 5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[575]" -type "float3" 5.9604645e-08 0 -7.4505806e-09 ;
	setAttr ".pt[576]" -type "float3" 5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[577]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[579]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[580]" -type "float3" 5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[581]" -type "float3" 5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[582]" -type "float3" -5.9604645e-08 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[583]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[584]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[585]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[586]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[588]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[589]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[590]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[592]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[593]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[594]" -type "float3" 5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[595]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[597]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[598]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[599]" -type "float3" -5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[600]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[601]" -type "float3" -5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[602]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[603]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[604]" -type "float3" -5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[605]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[606]" -type "float3" 5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[607]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[608]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[609]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[610]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[611]" -type "float3" 0 -5.9604645e-08 -1.4901161e-08 ;
	setAttr ".pt[616]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[621]" -type "float3" 5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[622]" -type "float3" -5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[624]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[626]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[627]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[628]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[629]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[630]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[631]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[632]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[633]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[634]" -type "float3" 2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[635]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[636]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[637]" -type "float3" 0 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[639]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[641]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[642]" -type "float3" 5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[643]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[644]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[645]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[646]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[647]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[648]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[649]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[650]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[651]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[652]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[653]" -type "float3" -7.4505806e-09 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[654]" -type "float3" 7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[655]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[656]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[657]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[658]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[659]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[660]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[661]" -type "float3" -2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[662]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[664]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[665]" -type "float3" -2.9802322e-08 0 -7.1054274e-15 ;
	setAttr ".pt[666]" -type "float3" 0 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[667]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[668]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[670]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[671]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[672]" -type "float3" 0 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[673]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[674]" -type "float3" -1.4901161e-08 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[675]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[676]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[677]" -type "float3" -7.4505806e-09 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[678]" -type "float3" 7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[679]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[680]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[681]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[682]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[683]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[684]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[685]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[686]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[687]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[689]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[690]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[691]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[692]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[693]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[694]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[695]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[696]" -type "float3" -2.220446e-16 0 -2.9802322e-08 ;
	setAttr ".pt[698]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[699]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[700]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[701]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[702]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[703]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[704]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[706]" -type "float3" -2.220446e-16 0 2.9802322e-08 ;
	setAttr ".pt[708]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[709]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[710]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[711]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[712]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[713]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[714]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[716]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[717]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[718]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[719]" -type "float3" -3.7252903e-09 2.9802322e-08 9.3132257e-10 ;
	setAttr ".pt[720]" -type "float3" 3.7252903e-09 2.9802322e-08 0 ;
	setAttr ".pt[721]" -type "float3" -3.7252903e-09 2.9802322e-08 -9.3132257e-10 ;
	setAttr ".pt[722]" -type "float3" 0 2.9802322e-08 1.8626451e-09 ;
	setAttr ".pt[723]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[724]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[725]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[726]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[727]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[728]" -type "float3" 0 2.9802322e-08 1.8626451e-09 ;
	setAttr ".pt[729]" -type "float3" 3.7252903e-09 2.9802322e-08 -9.3132257e-10 ;
	setAttr ".pt[730]" -type "float3" -3.7252903e-09 2.9802322e-08 0 ;
	setAttr ".pt[731]" -type "float3" 3.7252903e-09 2.9802322e-08 9.3132257e-10 ;
	setAttr ".pt[732]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[733]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[734]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[735]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[736]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[737]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[739]" -type "float3" 7.4505806e-09 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[740]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[741]" -type "float3" 1.4901161e-08 0 -1.4901161e-08 ;
	setAttr ".pt[742]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[743]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[744]" -type "float3" -1.4901161e-08 0 1.4901161e-08 ;
	setAttr ".pt[745]" -type "float3" 0 0 3.7252903e-09 ;
	setAttr ".pt[746]" -type "float3" 1.4901161e-08 2.9802322e-08 0 ;
	setAttr ".pt[748]" -type "float3" 0 0 3.5527137e-15 ;
	setAttr ".pt[749]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[750]" -type "float3" 1.4901161e-08 0 7.1054274e-15 ;
	setAttr ".pt[751]" -type "float3" 1.4901161e-08 -2.9802322e-08 -3.7252903e-09 ;
	setAttr ".pt[752]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[753]" -type "float3" -2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[754]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[755]" -type "float3" 1.4901161e-08 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[757]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[758]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[761]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[762]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[763]" -type "float3" 5.5511151e-17 0 0 ;
	setAttr ".pt[764]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[766]" -type "float3" -3.7252903e-09 0 -1.4901161e-08 ;
	setAttr ".pt[767]" -type "float3" 7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[768]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[769]" -type "float3" -7.4505806e-09 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[770]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[772]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[773]" -type "float3" -1.4901161e-08 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[774]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[776]" -type "float3" -1.4901161e-08 2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[777]" -type "float3" 2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[778]" -type "float3" 0 0 3.5527137e-15 ;
	setAttr ".pt[779]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[780]" -type "float3" -1.4901161e-08 0 7.1054274e-15 ;
	setAttr ".pt[781]" -type "float3" -1.4901161e-08 -2.9802322e-08 3.7252903e-09 ;
	setAttr ".pt[782]" -type "float3" 1.4901161e-08 0 -7.4505806e-09 ;
	setAttr ".pt[784]" -type "float3" 0 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[785]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[787]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[788]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[791]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[792]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[794]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[796]" -type "float3" -2.220446e-16 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[797]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[798]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[799]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[800]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[801]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[802]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[803]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[804]" -type "float3" 1.4901161e-08 0 -1.4901161e-08 ;
	setAttr ".pt[805]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[807]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[808]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[809]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[810]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[811]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[812]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[813]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[814]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[815]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[816]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[817]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[818]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[819]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[820]" -type "float3" 0 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[823]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[824]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[825]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[826]" -type "float3" -2.220446e-16 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[827]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[828]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[829]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[830]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[831]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[832]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[835]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[836]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[837]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[838]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[839]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[840]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[841]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[842]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[843]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[844]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[845]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[846]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[847]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[848]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[849]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[850]" -type "float3" 0 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[851]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[852]" -type "float3" 1.4901161e-08 0 1.4901161e-08 ;
	setAttr ".pt[853]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[854]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[855]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".db" yes;
	setAttr ".vs" 4;
	setAttr ".bw" 4;
	setAttr ".dr" 1;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "polySurfaceShape59" -p "Special_A";
	rename -uid "9C5B3D44-4C10-D537-540E-67B7DE486E9A";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.48809218406677246 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 924 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0.86968678 0.068829119 0.86169571
		 0.060390025 0.86635321 0.055744648 0.87448424 0.06390518 0.87741488 0.077352583 0.88201636
		 0.0721156 0.8851738 0.08547467 0.88920194 0.07957375 0.89383191 0.091774583 0.89678019
		 0.085028678 0.90506196 0.094280869 0.90595096 0.087174714 0.43322408 0.076292485
		 0.43029067 0.082918048 0.42278859 0.074264869 0.42121565 0.081124097 0.41171008 0.074104667
		 0.41100499 0.080972254 0.40029538 0.074354634 0.4000172 0.081236333 0.38874146 0.074296832
		 0.38861105 0.081442535 0.86100537 0.061078578 0.86901975 0.069529772 0.85963142 0.062449008
		 0.86031747 0.061764687 0.86835307 0.070228428 0.86768526 0.070925713 0.87678087 0.078094184
		 0.87614673 0.078832269 0.87551105 0.079566777 0.88461488 0.086317778 0.88405508 0.08715874
		 0.88349354 0.087996721 0.89337873 0.092740715 0.89291483 0.09370622 0.89243853 0.09466967
		 0.44320729 0.082083732 0.44374862 0.081322595 0.4442462 0.080541328 0.43361956 0.07529968
		 0.4340066 0.074300796 0.43438262 0.073296204 0.4230119 0.073283195 0.42323315 0.072302997
		 0.42345142 0.071324289 0.41180998 0.073131353 0.41190988 0.072160572 0.41200897 0.0711914
		 0.4003374 0.073382944 0.40037987 0.072413206 0.40042266 0.071444049 0.38875905 0.073333964
		 0.3887766 0.072370589 0.38879424 0.071404561 0.85933125 0.10948718 0.85990834 0.10917002
		 0.86536396 0.11879921 0.8645342 0.11907822 0.86047912 0.10884371 0.86616057 0.11845845
		 0.86473376 0.11984557 0.85959017 0.12114412 0.85912651 0.12041438 0.86662179 0.11902443
		 0.88672262 0.10338897 0.88704824 0.10395136 0.43398881 0.037792891 0.43471304 0.037751913
		 0.43747392 0.063029945 0.43682882 0.063165873 0.43401998 0.0358015 0.43331522 0.036178321
		 0.43061909 0.031281233 0.43145862 0.031140476 0.88867188 0.10398936 0.88863432 0.10309088
		 0.44740877 0.074808657 0.44773948 0.074452907 0.88822865 0.10261682 0.90252244 0.10277116
		 0.43689477 0.064233184 0.42492741 0.062806249 0.42500001 0.062184423 0.43730712 0.064810336
		 0.42484683 0.063429236 0.85427296 0.11163026 0.85488045 0.11140287 0.85822088 0.12073693
		 0.8575967 0.12143588 0.85548288 0.11116487 0.4329603 0.02005747 0.85285544 0.12991038
		 0.43100172 0.029334217 0.43032908 0.029515862 0.85318393 0.13011909 0.43197373 0.02940613
		 0.9093383 0.17378443 0.90969682 0.1733242 0.5154869 0.034608185 0.51564294 0.033819675
		 0.90993315 0.17280352 0.9191705 0.1800372 0.90885425 0.17285079 0.90902913 0.17336851
		 0.90605187 0.17592216 0.90571702 0.17538798 0.90634263 0.17648315 0.50397116 0.032330036
		 0.5034523 0.03238374 0.5033282 0.028466225 0.50393856 0.028302789 0.50295073 0.032605827
		 0.50270784 0.028579056 0.49986535 0.0052989721 0.88729936 0.1893276 0.49645591 0.01316613
		 0.49584928 0.012958169 0.88802385 0.18957299 0.49696365 0.013531268 0.89076561 0.18133348
		 0.89079314 0.18067938 0.89468449 0.18045247 0.89483231 0.18109429 0.89049572 0.18010527
		 0.89441466 0.1798501 0.4983719 0.017231226 0.49900511 0.017019808 0.50203502 0.022508621
		 0.5014348 0.022731721 0.49958035 0.016695619 0.50261086 0.022249997 0.90525848 0.15291548
		 0.9059388 0.15281045 0.90835166 0.16327167 0.90766895 0.1633057 0.90662694 0.1527552
		 0.90903908 0.16328323 0.46523026 0.051426142 0.46553689 0.052018791 0.45469707 0.055400103
		 0.45438528 0.054787815 0.46589842 0.052587688 0.45501009 0.056010604 0.48706603 0.012524486
		 0.48702887 0.013182223 0.4757767 0.014281452 0.47578198 0.01361686 0.48711669 0.013825059
		 0.47581345 0.01494354 0.86816269 0.14408898 0.86759555 0.14439291 0.86413807 0.1329264
		 0.86466485 0.13251066 0.86705309 0.14475799 0.86361319 0.13335723 0.85335332 0.068711758
		 0.86144596 0.077334583 0.8464306 0.091289341 0.83870363 0.083329648 0.8694945 0.08626765
		 0.85374159 0.099763513 0.87790591 0.09545666 0.42309904 0.040066004 0.41275638 0.062252551
		 0.41164249 0.04151085 0.40077609 0.06251052 0.40042552 0.042141497 0.38895902 0.062377989
		 0.38932604 0.042276412 0.83786541 0.084166259 0.84550321 0.092059374 0.84248286 0.094510198
		 0.8350898 0.086936772 0.85272139 0.10043865 0.84937507 0.1025362 0.42274436 0.038816482
		 0.42129037 0.03485027 0.41144621 0.040311366 0.41069019 0.036443591 0.40034544 0.040939599
		 0.4000544 0.037053108 0.38934842 0.041050106 0.38941884 0.03719306 0.90097797 0.17958522
		 0.51279795 0.017689466 0.50780469 0.011165202 0.51542908 0.025579333 0.49537459 0.054547668
		 0.50608301 0.047359705 0.90303952 0.14228553 0.48431075 0.059791952 0.89860964 0.1319927
		 0.47340238 0.063784838 0.89376944 0.12163484 0.4631027 0.067066878 0.49601316 0.039192557
		 0.50364327 0.03343457 0.48877907 0.0036082268 0.88332146 0.17466331 0.88956124 0.18085563
		 0.4385843 0.064194471 0.85664892 0.13919806 0.44322315 0.02584219 0.85864371 0.1227079
		 0.8897481 0.17078322 0.88431591 0.1738236 0.48855501 0.019958377 0.49592456 0.014155507
		 0.47647423 0.048918247 0.4866156 0.044507831 0.45632848 0.030759335 0.4448922 0.034330934
		 0.4433136 0.027189344 0.45423815 0.021956265 0.46742937 0.027003706 0.46491185 0.017721176
		 0.4781802 0.023319244 0.45397902 0.020679116 0.85972238 0.15003407 0.46472925 0.016413927
		 0.8640911 0.16121036 0.87006545 0.17200035 0.87114578 0.15555906 0.87652594 0.16559863
		 0.87079525 0.12891594 0.87597984 0.13971773 0.88074201 0.15042108 0.87222815 0.15481478
		 0.88527644 0.16083822 0.87752271 0.16473007 0.8342526 0.087772518 0.84154719 0.095259935
		 0.84116119 0.095496625 0.83395046 0.088074118 0.84832829 0.10315779 0.84789771 0.10335582
		 0.85377634 0.11177045 0.85704988 0.12142411 0.85226202 0.12974539 0.42993644 0.029114425
		 0.42077842 0.033667892 0.42053336 0.033214599 0.41042662 0.035261631 0.41027594 0.034814656
		 0.39994767 0.035856575 0.39985189 0.035413235 0.38944107 0.035974801 0.389449 0.035539836
		 0.83304065 0.088982284;
	setAttr ".uvst[0].uvsp[250:499]" 0.84014618 0.096299827 0.83366549 0.10136187
		 0.82735193 0.094661653 0.84675902 0.1040093 0.83953255 0.10805097 0.85245115 0.11221081
		 0.84389526 0.11465919 0.85531032 0.12126458 0.84636885 0.12102237 0.43198106 0.019561321
		 0.42632663 0.016442329 0.42862633 0.027951896 0.42236367 0.021645784 0.41993144 0.031960487
		 0.41604063 0.024376243 0.40997374 0.033543825 0.40794423 0.025434643 0.39973089 0.034119278
		 0.39894024 0.025799483 0.3894729 0.03422907 0.38962868 0.025690734 0.86230242 0.076480925
		 0.85420471 0.067862421 0.87033379 0.085394055 0.87869596 0.094462633 0.41267744 0.063465625
		 0.40073487 0.063720167 0.38893676 0.063597977 0.49510589 0.038165271 0.48581383 0.043393433
		 0.47577408 0.047763944 0.89244634 0.12200153 0.89729398 0.13228571 0.90170985 0.14254877
		 0.90054089 0.17839211 0.83828431 0.083748162 0.84596753 0.091674864 0.85323262 0.10010266
		 0.88724518 0.10465956 0.86707354 0.11954659 0.864923 0.12057897 0.86005855 0.12183988
		 0.86615753 0.12011606 0.4322843 0.031024903 0.43468535 0.035447359 0.43540648 0.037733316
		 0.43812791 0.062704742 0.43520018 0.036681831 0.43368757 0.036980033 0.42292663 0.039440155
		 0.41154668 0.040910959 0.40038645 0.041540593 0.38933721 0.041663706 0.8537786 0.068287492
		 0.86187452 0.07690841 0.86991489 0.085832417 0.87830317 0.094962358 0.88753605 0.10271233
		 0.43791252 0.064779192 0.41271827 0.062858671 0.40075606 0.063115001 0.38894787 0.062988073
		 0.83467156 0.087354302 0.84201556 0.094885409 0.84885275 0.10284823 0.8579244 0.12204885
		 0.43024427 0.030416846 0.42103952 0.03425765 0.41056019 0.035852551 0.40000162 0.036455214
		 0.38942993 0.036584139 0.50387096 0.032908082 0.89014125 0.18118978 0.90078068 0.17898566
		 0.49652141 0.01398468 0.90236777 0.14239037 0.90936613 0.17270017 0.89794195 0.13211071
		 0.89310813 0.12181717 0.88792813 0.10423207 0.50318462 0.033085465 0.49554113 0.038692594
		 0.48619348 0.043963939 0.47609955 0.048353434 0.43827039 0.063495427 0.49573791 0.013591468
		 0.46479413 0.017072678 0.45407695 0.021327198 0.44326213 0.026520133 0.43206003 0.030223787
		 0.88995355 0.18034637 0.88378209 0.17419225 0.87701231 0.16514707 0.8716746 0.15516305
		 0.85930687 0.12221962 0.83349776 0.088526011 0.84065479 0.09589836 0.84732926 0.10368374
		 0.85311174 0.11199498 0.85614884 0.1213738 0.43240893 0.01970014 0.42928332 0.028491139
		 0.42023209 0.032583892 0.41012567 0.0341793 0.39979163 0.034767449 0.38946098 0.034883857
		 0.86574918 0.11949545 0.43446207 0.036796898 0.88785481 0.10333398 0.43756691 0.064045668
		 0.85865223 0.12148553 0.43107933 0.030236185 0.9093672 0.17311448 0.50349236 0.032806218
		 0.89031035 0.18072057 0.49623302 0.013602555 0.85327411 0.052380443 0.8582105 0.047595769
		 0.84476739 0.044633716 0.85001624 0.040045619 0.83666223 0.036857456 0.8425734 0.032844007
		 0.83038175 0.028186113 0.83713537 0.025254458 0.33456838 0.080861717 0.3389827 0.086476237
		 0.34421492 0.074667647 0.34690443 0.081395924 0.35471773 0.073022485 0.35603923 0.079934552
		 0.36579493 0.073266774 0.36624891 0.080155507 0.37719306 0.07393308 0.37721995 0.080820352
		 0.85257167 0.05304569 0.85117227 0.054376572 0.85187125 0.05371058 0.84402418 0.045265883
		 0.84254831 0.046532094 0.84328449 0.045898199 0.83581769 0.037414312 0.83413595 0.038531601
		 0.83497536 0.037972093 0.82941443 0.028637022 0.82748306 0.029572636 0.8284477 0.02909857
		 0.33402666 0.080090374 0.8251549 0.017531872 0.33351347 0.07931 0.34385592 0.073661089
		 0.34316653 0.071631059 0.34350562 0.072648719 0.35453042 0.072033316 0.35416269 0.070059657
		 0.35434508 0.071045697 0.36573061 0.07229045 0.36560258 0.070344523 0.36566621 0.071316689
		 0.37718654 0.072960511 0.37717208 0.071019799 0.37717947 0.071989879 0.81259072 0.062648058
		 0.80301112 0.05742541 0.80329186 0.0565961 0.81290907 0.062071532 0.80363429 0.055800021
		 0.81323659 0.061501414 0.80166376 0.062830985 0.80093503 0.06236583 0.80224413 0.057224363
		 0.80306923 0.055337757 0.81818795 0.034941971 0.81874955 0.035268903 0.34485698 0.036165863
		 0.3410919 0.061418146 0.34045216 0.061258733 0.34413475 0.03609848 0.34489861 0.034174711
		 0.34762847 0.029610366 0.34846228 0.029781699 0.3455891 0.034577012 0.81815386 0.033318251
		 0.81841886 0.019592136 0.33009344 0.072666645 0.81905222 0.033357859 0.33038056 0.073079139
		 0.81952536 0.033764541 0.35294887 0.060869366 0.3529987 0.061493397 0.340987 0.062482327
		 0.35305649 0.062118918 0.34055382 0.063044041 0.8104375 0.067702502 0.80063933 0.064359009
		 0.80133945 0.063736111 0.81066608 0.067095369 0.81090528 0.066493362 0.79228109 0.069483727
		 0.34881657 0.028028071 0.34815106 0.027822018 0.79215598 0.069085181 0.34717709 0.027858377
		 0.3457723 0.018755913 0.74840444 0.012500942 0.74080372 0.003513813 0.26353025 0.030001462
		 0.74886549 0.012143493 0.26377463 0.030782998 0.74938679 0.011908412 0.7493369 0.012987196
		 0.74679255 0.016118646 0.74625915 0.015782535 0.74881965 0.012811124 0.74569887 0.015490472
		 0.27512169 0.028146446 0.27530169 0.024123013 0.27590567 0.024308741 0.27563822 0.028219104
		 0.27652144 0.024444222 0.27613139 0.02845937 0.73314875 0.035196364 0.28394711 0.00908494
		 0.2833333 0.0092704892 0.73281068 0.034504533 0.28281248 0.0096167922 0.27880436
		 0.0018834472 0.74081278 0.031056821 0.74106127 0.026990533 0.7417028 0.027139843
		 0.74146694 0.031030774 0.7423045 0.027411044 0.74204034 0.031329572 0.28126979 0.013262689
		 0.27800763 0.018647373 0.27741599 0.018402457 0.28064477 0.013028264 0.27684999 0.018122971
		 0.28008175 0.012683213 0.76926357 0.016627967 0.75887907 0.01419431 0.75891471 0.013511598
		 0.7693702 0.015947878 0.75890476 0.012824178 0.76942706 0.015259862 0.31313801 0.04864794
		 0.3238529 0.052404106 0.32351893 0.053004563 0.31280994 0.049228966 0.3231838 0.053603232
		 0.31242776 0.049784243;
	setAttr ".uvst[0].uvsp[500:749]" 0.29274023 0.0089730024 0.30397663 0.010477602
		 0.30395758 0.011141956 0.29275334 0.0096316934 0.30389664 0.011802256 0.292642 0.010270834
		 0.77800792 0.053744316 0.78957897 0.057267249 0.78916216 0.05779326 0.77770287 0.054310858
		 0.78873032 0.058317274 0.77733666 0.054852545 0.83076048 0.07558614 0.84474808 0.0606004
		 0.8223021 0.0682576 0.83583272 0.052532822 0.82666224 0.044102103 0.35565639 0.038835138
		 0.36705244 0.040697187 0.36518198 0.06138438 0.37823886 0.041736692 0.37714496 0.06207931
		 0.82753205 0.079527915 0.8299886 0.076512009 0.81952083 0.072619021 0.82162488 0.069276541
		 0.35765427 0.033688903 0.35605642 0.037599385 0.3681891 0.035668075 0.36729237 0.039505661
		 0.37879547 0.036665201 0.37836277 0.04053849 0.2720654 0.0068554878 0.26683664 0.013192534
		 0.74258447 0.020848155 0.26391852 0.020980835 0.27246106 0.043088615 0.28289926 0.05066371
		 0.29376376 0.056309462 0.77988839 0.018870234 0.30451882 0.060699224 0.79017133 0.023322284
		 0.31469208 0.064356148 0.80051863 0.028184205 0.27540892 0.029262185 0.2828232 0.035295665
		 0.29135466 0 0.74128783 0.032262325 0.74746603 0.038516641 0.33929995 0.062381953
		 0.3360658 0.023885757 0.7828756 0.065269887 0.79936939 0.063309401 0.75136077 0.032098591
		 0.74830806 0.037524104 0.28382802 0.010278702 0.29098022 0.016347408 0.30199331 0.045730144
		 0.29202002 0.040951371 0.3227897 0.028320432 0.32520053 0.019599676 0.33592618 0.025228709
		 0.33408755 0.032307833 0.31183374 0.02416122 0.31468913 0.014976978 0.30122501 0.020085752
		 0.32550618 0.018332899 0.77204543 0.062172294 0.31491944 0.013677299 0.76087779 0.057778537
		 0.75010002 0.051779509 0.7665441 0.050735891 0.75651592 0.045333087 0.7931866 0.051143736
		 0.7823959 0.045935988 0.76729071 0.049655139 0.77170283 0.041150451 0.75738668 0.044338286
		 0.76129568 0.036592841 0.82654315 0.0808478 0.82678056 0.080462188 0.81869829 0.074094921
		 0.81889719 0.073664635 0.81029636 0.06819886 0.80065006 0.064905882 0.34670049 0.018370092
		 0.34922361 0.027641267 0.3584705 0.032081962 0.35820904 0.032525986 0.36866251 0.034055322
		 0.36849561 0.034496486 0.37905768 0.035033822 0.37894577 0.035473377 0.8206653 0.088333845
		 0.82573813 0.081861347 0.81398892 0.082452238 0.81804276 0.075232416 0.80739057 0.078075171
		 0.80985343 0.069523335 0.80103332 0.075588554 0.80080622 0.06664598 0.79461795 0.076635212
		 0.79264963 0.070508629 0.35706383 0.020454049 0.3505753 0.026527345 0.36328277 0.023413479
		 0.35911778 0.030850679 0.37133488 0.024766624 0.3690109 0.032796383 0.38031942 0.025459737
		 0.37922582 0.03374514 0.84560382 0.059745967 0.83670837 0.051695526 0.82765818 0.043314308
		 0.36521658 0.06259954 0.37714198 0.063289672 0.28376746 0.034302294 0.29286206 0.039867073
		 0.30273521 0.044602156 0.80014902 0.029506594 0.78987533 0.024637312 0.77962214 0.020199299
		 0.74377662 0.021287978 0.830374 0.076048464 0.82196194 0.068765938 0.80254805 0.05488494
		 0.81748027 0.034743488 0.80024016 0.061896086 0.80151111 0.057033688 0.80197656 0.055799991
		 0.34424663 0.033796489 0.3468076 0.029464722 0.33981046 0.060909867 0.34344247 0.036054552
		 0.34368703 0.035011321 0.3558515 0.038215995 0.34518772 0.035364598 0.36717013 0.040101171
		 0.37829989 0.041137576 0.84517527 0.060172856 0.83626896 0.052113414 0.8271575 0.04370594
		 0.81942821 0.034456968 0.33994994 0.062990785 0.36519796 0.061991483 0.37714294 0.062684119
		 0.82715595 0.07999447 0.81920773 0.07314074 0.80002701 0.064030081 0.35792658 0.03310585
		 0.34886846 0.028931558 0.36834058 0.035082161 0.37887004 0.036069632 0.27520072 0.02872771
		 0.740955 0.031681538 0.74318361 0.021046817 0.28323781 0.010086119 0.77978206 0.019541711
		 0.74948877 0.012475669 0.79005182 0.023989707 0.80033487 0.028845161 0.81790936 0.034061491
		 0.28331321 0.034813285 0.27588004 0.028930187 0.29246175 0.040423304 0.30238837 0.045179397
		 0.33963919 0.061694831 0.28403521 0.0097218156 0.31483048 0.014333248 0.32538462
		 0.018976927 0.33600205 0.024561822 0.34706101 0.028672338 0.7479381 0.038057029 0.74179798
		 0.0318712 0.75696856 0.044847786 0.76694125 0.050207973 0.79985899 0.062647104 0.82614052
		 0.081353456 0.81836933 0.074662775 0.81007051 0.068863034 0.80069864 0.065807164
		 0.34709668 0.018142998 0.34989905 0.02704221 0.3587946 0.031462699 0.3688359 0.033425868
		 0.37914145 0.034390688 0.80259639 0.056209505 0.34442043 0.03515327 0.8188073 0.034136832
		 0.34032214 0.062270403 0.80059177 0.063303262 0.34804055 0.028720528 0.74907446 0.012473583
		 0.27558279 0.028639793 0.74142462 0.031513512 0.28354001 0.0097147822 0.54750949
		 0.03151232 0.54793191 0.030657172 0.54859471 0.029976815 0.54943168 0.029538929 0.55036169
		 0.029640734 0.55129051 0.02953583 0.55213273 0.029971123 0.55280364 0.030649215 0.55323714
		 0.031502545 0.5533908 0.032442272 0.55325007 0.033382744 0.55282772 0.034237891 0.55216491
		 0.034918249 0.55132794 0.035356134 0.55039793 0.035254329 0.54946911 0.035359263
		 0.5486269 0.034923941 0.54795599 0.034245849 0.54752249 0.033392489 0.54736888 0.032452792
		 0.53887302 0.02874881 0.53403264 0.027218938 0.53643751 0.022419244 0.54057479 0.0253461
		 0.5291779 0.025697321 0.53227806 0.019498527 0.54323667 0.022620261 0.54672277 0.021221995
		 0.55031115 0.021589398 0.55401999 0.020808339 0.55740052 0.022587478 0.56009364 0.025302172
		 0.56183624 0.02869907 0.56245244 0.032421291 0.56188506 0.036145747 0.5601849 0.039548963
		 0.55752295 0.042274803 0.55403692 0.043673068 0.55044854 0.043305695 0.54673964 0.044086725
		 0.5433591 0.042307585 0.54066598 0.039592862 0.53892338 0.036195964 0.53830719 0.032473773
		 0.54022878 0.018573165 0.53718728 0.014587075 0.54503369 0.016048849 0.54326969 0.011029452
		 0.55028194 0.016385734 0.55025625 0.011050344 0.55557805 0.015884876 0.55724072 0.011009485
		 0.56036955 0.018511146 0.56339002 0.014487028;
	setAttr ".uvst[0].uvsp[750:923]" 0.56418896 0.022350281 0.56831026 0.019409359
		 0.56665283 0.027138233 0.57148302 0.025577009 0.56752807 0.032404155 0.57261062 0.032378852
		 0.56672698 0.037676066 0.57158339 0.039198101 0.56432217 0.04247576 0.56848162 0.045396447
		 0.5605309 0.046321869 0.56357241 0.05030793 0.55572599 0.048846245 0.55748999 0.053865612
		 0.55047768 0.048509359 0.55050337 0.05384475 0.54518157 0.049010217 0.5435189 0.053885579
		 0.54039007 0.046383917 0.53736955 0.050408006 0.53657061 0.042544782 0.53244936 0.045485646
		 0.53410679 0.037756771 0.52927655 0.039317966 0.53323156 0.032490849 0.52814907 0.032516122
		 0.51575452 0.032721639 0.51730376 0.02210474 0.52491367 0.024363577 0.52368736 0.032547772
		 0.52205628 0.012391448 0.52863133 0.016910255 0.52950144 0.0044803917 0.53452468
		 0.011125922 0.53929406 0 0.54178721 0.0071414113 0.55026001 0.00019749999 0.55024338
		 0.0069788992 0.56119281 2.2560358e-05 0.55866879 0.0071230829 0.5707103 0.0046038032
		 0.56606013 0.010970533 0.57830268 0.012095243 0.57192975 0.01682052 0.58323354 0.021618426
		 0.57572532 0.024196357 0.5850051 0.032173127 0.57707226 0.032347113 0.51752603 0.043276399
		 0.52503431 0.040698558 0.52245682 0.052799642 0.52882981 0.048074454 0.53004926 0.060291171
		 0.53469944 0.053924501 0.53956676 0.064872503 0.54209077 0.057771981 0.55049968 0.064697593
		 0.55051631 0.057916164 0.56146574 0.064895034 0.55897254 0.057753652 0.57125843 0.060414523
		 0.56623507 0.053769052 0.57870352 0.052503407 0.57212842 0.04798466 0.58345598 0.042790055
		 0.57584602 0.040531337 0.52612692 0.024744391 0.52966863 0.017653018 0.53528023 0.012116671
		 0.54220837 0.0083294809 0.55024654 0.0083461106 0.55826557 0.0083121061 0.56529945
		 0.011977911 0.57089841 0.017559975 0.57451785 0.024591088 0.57580233 0.03235653 0.57463276
		 0.040150523 0.57109112 0.047241926 0.56547952 0.052778304 0.55855137 0.056565553
		 0.55051315 0.056548983 0.54249406 0.056582958 0.53546011 0.052917123 0.52986115 0.047334999
		 0.52624178 0.040303826 0.5249573 0.032538384 0.52431989 0.032543182 0.52563572 0.040501624
		 0.52551782 0.024553716 0.52914762 0.017280877 0.53490049 0.011620015 0.54197758 0.0077404976
		 0.55024475 0.0076628625 0.55848658 0.0077238977 0.56568146 0.011472195 0.57141608
		 0.017189056 0.57512385 0.02439329 0.57643974 0.032351732 0.52934349 0.047705919 0.53507811
		 0.053422838 0.54227298 0.057171166 0.55051488 0.057232201 0.5587821 0.057154566 0.56585926
		 0.053274989 0.57161212 0.047614038 0.57524186 0.040341198 0.33304474 0.078511059
		 0.81940454 0.019470453 0.34752929 0.018019885 0.3532936 0.01510942 0.34653264 0.018480003
		 0.79232013 0.069679141 0.79194778 0.068756104 0.33680922 0.014825702 0.32977593 0.072299063
		 0.80203921 0.014569163 0.28021407 0.0012838244 0.74017692 0.043931484 0.75700325
		 0 0.74217486 0.0026540756 0.26340318 0.029207766 0.7353906 0.0097302794 0.7312662
		 0.025503874 0.73256701 0.033779442 0.79243523 0.070117712 0.27948737 0.0015386343
		 0.7414518 0.003038466 0.34615737 0.018671811 0.81890661 0.019557893 0.83501172 0.016079187
		 0.82790273 0.016950637 0.82697183 0.017112285 0.82605439 0.017300069 0.32689044 0.0094073415
		 0.31583482 0.004684329 0.3039372 0.0013826489 0.79221106 0.010005772 0.78146207 0.0055636764
		 0.76975709 0.0019439459 0.73199618 0.017322361 0.90447408 0.097026795 0.44710681
		 0.075210363 0.8514334 0.12941474 0.84531116 0.12743676 0.85245728 0.12978464 0.4327966
		 0.019941539 0.43371016 0.020360976 0.44281143 0.016761005 0.90239841 0.10375628 0.90738809
		 0.1201449 0.88660836 0.18898791 0.87789017 0.18194026 0.92185873 0.1652146 0.51521409
		 0.035380304 0.91830754 0.18140629 0.91207862 0.18680501 0.89629596 0.19089282 0.50125211
		 0.0059497952 0.85182381 0.12962967 0.50058222 0.0055802464 0.91878444 0.18075931
		 0.43332839 0.020262867 0.90243375 0.10326874 0.43802142 0.088284299 0.44263777 0.08283478
		 0.90489799 0.095211238 0.90470803 0.096128047 0.45292214 0.011708915 0.46414348 0.007393539
		 0.47615421 0.0045294166 0.9119308 0.12998313 0.91634965 0.14074224 0.91994357 0.15245581
		 0.90447891 0.19018179;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 713 ".pt";
	setAttr ".pt[0]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[2]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[3]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[4]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[5]" -type "float3" 0 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[6]" -type "float3" 5.9604645e-08 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[7]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[8]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[9]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[10]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[11]" -type "float3" 2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[12]" -type "float3" 2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[13]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[14]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[15]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[16]" -type "float3" 2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[17]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[18]" -type "float3" -2.9802322e-08 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[19]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[20]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[21]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[22]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[23]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[24]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[26]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[27]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[29]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[31]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[32]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[34]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[36]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[37]" -type "float3" 0 -2.3283064e-10 2.9802322e-08 ;
	setAttr ".pt[39]" -type "float3" 1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[40]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[41]" -type "float3" 1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[42]" -type "float3" -1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[43]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[44]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[45]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[46]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[47]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[48]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[49]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[50]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[51]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[52]" -type "float3" -2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[53]" -type "float3" 0 -2.3283064e-10 1.4901161e-08 ;
	setAttr ".pt[54]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[55]" -type "float3" 0 -1.8626451e-09 -7.1054274e-15 ;
	setAttr ".pt[57]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[58]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[59]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[60]" -type "float3" -2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[61]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[62]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[63]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[64]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[65]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[66]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[67]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[68]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[69]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[70]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[71]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[72]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[73]" -type "float3" 1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[74]" -type "float3" -1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[76]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[77]" -type "float3" 0 -2.3283064e-10 -2.9802322e-08 ;
	setAttr ".pt[79]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[80]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[81]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[83]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[84]" -type "float3" -2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[86]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[87]" -type "float3" -5.9604645e-08 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[88]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[89]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[91]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[92]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[93]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[94]" -type "float3" -7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[95]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[96]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[97]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[98]" -type "float3" 2.9802322e-08 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[99]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[100]" -type "float3" 0 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[101]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[103]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[104]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[105]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[107]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[108]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[109]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[110]" -type "float3" 2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[111]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[112]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[113]" -type "float3" 0 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[114]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[115]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[116]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[117]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[118]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[119]" -type "float3" -7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[120]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[122]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[123]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[124]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[126]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[128]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[129]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[130]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[131]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[132]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[133]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[134]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[135]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[136]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[137]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[138]" -type "float3" -2.9802322e-08 7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[141]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[143]" -type "float3" -1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[146]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[149]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[151]" -type "float3" 0 -7.4505806e-09 -7.1054274e-15 ;
	setAttr ".pt[152]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[155]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[158]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[161]" -type "float3" -1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[165]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[167]" -type "float3" 0 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[168]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[170]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[171]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[172]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[173]" -type "float3" -1.4901161e-08 2.9802322e-08 0 ;
	setAttr ".pt[174]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[176]" -type "float3" 2.9802322e-08 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[177]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[179]" -type "float3" -2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[180]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[181]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[182]" -type "float3" 2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[183]" -type "float3" 2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[184]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[185]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[186]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[187]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[188]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[189]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[190]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[191]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[192]" -type "float3" 0 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[193]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[195]" -type "float3" 2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[196]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[198]" -type "float3" 2.9802322e-08 2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[199]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[201]" -type "float3" -1.4901161e-08 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[202]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[204]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[205]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[207]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[208]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[209]" -type "float3" 1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[210]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[211]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[212]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[214]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[215]" -type "float3" -1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[216]" -type "float3" 1.1920929e-07 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[217]" -type "float3" 1.1920929e-07 0 7.1054274e-15 ;
	setAttr ".pt[218]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[219]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[220]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[221]" -type "float3" 1.1920929e-07 5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[222]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[224]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[225]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[226]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[227]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[228]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[229]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[230]" -type "float3" 0 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[231]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[232]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[233]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[234]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[235]" -type "float3" -5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[236]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[238]" -type "float3" -5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[239]" -type "float3" -5.9604645e-08 0 -7.4505806e-09 ;
	setAttr ".pt[240]" -type "float3" -5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[241]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[243]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[244]" -type "float3" -5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[245]" -type "float3" -5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[246]" -type "float3" 5.9604645e-08 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[247]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[248]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[249]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[250]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[252]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[253]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[254]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[256]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[257]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[258]" -type "float3" -5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[259]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[261]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[262]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[263]" -type "float3" 5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[264]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[265]" -type "float3" 5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[266]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[267]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[268]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[269]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[270]" -type "float3" -5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[271]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[272]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[273]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[274]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[275]" -type "float3" 0 -5.9604645e-08 -1.4901161e-08 ;
	setAttr ".pt[280]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[285]" -type "float3" -5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[286]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[288]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[290]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[291]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[292]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[293]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[294]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[295]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[296]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[297]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[298]" -type "float3" -2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[299]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[300]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[301]" -type "float3" 0 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[303]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[305]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[306]" -type "float3" -5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[307]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[308]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[309]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[310]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[311]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[312]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[313]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[314]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[315]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[316]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[317]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[318]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[319]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[320]" -type "float3" 7.4505806e-09 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[321]" -type "float3" -7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[322]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[323]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[324]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[325]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[326]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[327]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[328]" -type "float3" 2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[329]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[331]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[332]" -type "float3" 2.9802322e-08 0 -7.1054274e-15 ;
	setAttr ".pt[333]" -type "float3" 0 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[334]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[335]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[337]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[338]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[339]" -type "float3" 0 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[340]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[341]" -type "float3" 1.4901161e-08 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[342]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[343]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[344]" -type "float3" 7.4505806e-09 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[345]" -type "float3" -7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[346]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[347]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[348]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[349]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[350]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[351]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[352]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[353]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[354]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[355]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[356]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[357]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[359]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[360]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[361]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[362]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[363]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[364]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[365]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[366]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[368]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[369]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[370]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[371]" -type "float3" 0 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[372]" -type "float3" -5.9604645e-08 -2.9802322e-08 7.1054274e-15 ;
	setAttr ".pt[373]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[374]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[375]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[376]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[377]" -type "float3" -2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[378]" -type "float3" -2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[379]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[380]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[381]" -type "float3" -2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[382]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[383]" -type "float3" 2.9802322e-08 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[384]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[385]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[386]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[387]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[389]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[390]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[392]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[394]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[395]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[397]" -type "float3" -1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[398]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[399]" -type "float3" -1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[400]" -type "float3" 1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[401]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[402]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[403]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[404]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[405]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[406]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[407]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[408]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[409]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[410]" -type "float3" 2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[411]" -type "float3" 0 -2.3283064e-10 1.4901161e-08 ;
	setAttr ".pt[412]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[413]" -type "float3" 0 -1.8626451e-09 -7.1054274e-15 ;
	setAttr ".pt[415]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[416]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[417]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[418]" -type "float3" 2.9802322e-08 9.3132257e-10 0 ;
	setAttr ".pt[419]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[420]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[421]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[422]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[423]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[424]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[425]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[426]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[427]" -type "float3" 0 -2.3283064e-10 0 ;
	setAttr ".pt[428]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[429]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[430]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[431]" -type "float3" -1.4901161e-08 -2.3283064e-10 0 ;
	setAttr ".pt[432]" -type "float3" 1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[433]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[434]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[435]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[437]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[438]" -type "float3" 2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[440]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[441]" -type "float3" 5.9604645e-08 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[442]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[443]" -type "float3" 1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[444]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[445]" -type "float3" 7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[446]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[447]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[448]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[449]" -type "float3" -2.9802322e-08 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[450]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[451]" -type "float3" 0 -2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[452]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[454]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[455]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[456]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[458]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[459]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[460]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[461]" -type "float3" -2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[462]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[463]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[464]" -type "float3" 0 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[465]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[466]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[467]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[468]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[469]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[470]" -type "float3" 7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[471]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[472]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[474]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[476]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[477]" -type "float3" 0 -7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[478]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[479]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[480]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[481]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[482]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[483]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[484]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[485]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[486]" -type "float3" 2.9802322e-08 7.4505806e-09 -1.4901161e-08 ;
	setAttr ".pt[488]" -type "float3" 1.4901161e-08 0 2.9802322e-08 ;
	setAttr ".pt[491]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[494]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[496]" -type "float3" 0 -7.4505806e-09 -7.1054274e-15 ;
	setAttr ".pt[497]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[500]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[503]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[506]" -type "float3" 1.4901161e-08 0 -2.9802322e-08 ;
	setAttr ".pt[509]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[510]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[511]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[512]" -type "float3" 1.4901161e-08 2.9802322e-08 0 ;
	setAttr ".pt[513]" -type "float3" 0 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[515]" -type "float3" -2.9802322e-08 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[516]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[518]" -type "float3" 2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[519]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[520]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[521]" -type "float3" -2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[522]" -type "float3" -2.9802322e-08 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[523]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[524]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[525]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[526]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[527]" -type "float3" 0 0 -7.1054274e-15 ;
	setAttr ".pt[528]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[529]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[530]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[531]" -type "float3" 0 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[532]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[534]" -type "float3" -2.9802322e-08 0 7.4505806e-09 ;
	setAttr ".pt[535]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[537]" -type "float3" -2.9802322e-08 2.9802322e-08 1.4901161e-08 ;
	setAttr ".pt[538]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[540]" -type "float3" 1.4901161e-08 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[541]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[543]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[544]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[545]" -type "float3" -1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[546]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[547]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[548]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[550]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[551]" -type "float3" 1.1920929e-07 5.9604645e-08 0 ;
	setAttr ".pt[552]" -type "float3" -1.1920929e-07 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[553]" -type "float3" -1.1920929e-07 0 7.1054274e-15 ;
	setAttr ".pt[554]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[555]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[556]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[557]" -type "float3" -1.1920929e-07 5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[558]" -type "float3" 0 -5.9604645e-08 1.4901161e-08 ;
	setAttr ".pt[560]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[561]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[562]" -type "float3" 1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[563]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[564]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[565]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[566]" -type "float3" 0 5.9604645e-08 7.1054274e-15 ;
	setAttr ".pt[567]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[568]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[569]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[570]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[571]" -type "float3" 5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[572]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[574]" -type "float3" 5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[575]" -type "float3" 5.9604645e-08 0 -7.4505806e-09 ;
	setAttr ".pt[576]" -type "float3" 5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[577]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[579]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[580]" -type "float3" 5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[581]" -type "float3" 5.9604645e-08 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[582]" -type "float3" -5.9604645e-08 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[583]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[584]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[585]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[586]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[588]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[589]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[590]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[592]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[593]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[594]" -type "float3" 5.9604645e-08 5.9604645e-08 0 ;
	setAttr ".pt[595]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[597]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[598]" -type "float3" -1.1920929e-07 0 -1.4901161e-08 ;
	setAttr ".pt[599]" -type "float3" -5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[600]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[601]" -type "float3" -5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[602]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[603]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[604]" -type "float3" -5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[605]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[606]" -type "float3" 5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[607]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[608]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[609]" -type "float3" -1.1920929e-07 0 0 ;
	setAttr ".pt[610]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[611]" -type "float3" 0 -5.9604645e-08 -1.4901161e-08 ;
	setAttr ".pt[616]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[621]" -type "float3" 5.9604645e-08 -2.9802322e-08 0 ;
	setAttr ".pt[622]" -type "float3" -5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[624]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[626]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[627]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[628]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[629]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[630]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[631]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[632]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[633]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[634]" -type "float3" 2.9802322e-08 5.9604645e-08 0 ;
	setAttr ".pt[635]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[636]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[637]" -type "float3" 0 5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[639]" -type "float3" 0 5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[641]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[642]" -type "float3" 5.9604645e-08 0 7.4505806e-09 ;
	setAttr ".pt[643]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[644]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[645]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[646]" -type "float3" 0 -5.9604645e-08 -7.4505806e-09 ;
	setAttr ".pt[647]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[648]" -type "float3" 0 -5.9604645e-08 7.4505806e-09 ;
	setAttr ".pt[649]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[650]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[651]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[652]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[653]" -type "float3" -7.4505806e-09 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[654]" -type "float3" 7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[655]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[656]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[657]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[658]" -type "float3" 0 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[659]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[660]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[661]" -type "float3" -2.9802322e-08 -2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[662]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[664]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[665]" -type "float3" -2.9802322e-08 0 -7.1054274e-15 ;
	setAttr ".pt[666]" -type "float3" 0 -2.9802322e-08 -7.1054274e-15 ;
	setAttr ".pt[667]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[668]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[670]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[671]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[672]" -type "float3" 0 2.9802322e-08 -1.4901161e-08 ;
	setAttr ".pt[673]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[674]" -type "float3" -1.4901161e-08 -2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[675]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[676]" -type "float3" -1.4901161e-08 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[677]" -type "float3" -7.4505806e-09 -2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[678]" -type "float3" 7.4505806e-09 2.9802322e-08 0 ;
	setAttr ".pt[679]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[680]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[681]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[682]" -type "float3" 0 2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[683]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[684]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[685]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[686]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[687]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[689]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[690]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[691]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[692]" -type "float3" 1.1920929e-07 0 0 ;
	setAttr ".pt[693]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[694]" -type "float3" 0 5.9604645e-08 0 ;
	setAttr ".pt[695]" -type "float3" 0 -5.9604645e-08 0 ;
	setAttr ".pt[696]" -type "float3" -2.220446e-16 0 -2.9802322e-08 ;
	setAttr ".pt[698]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[699]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[700]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[701]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[702]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[703]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[704]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[706]" -type "float3" -2.220446e-16 0 2.9802322e-08 ;
	setAttr ".pt[708]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[709]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[710]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[711]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[712]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[713]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[714]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[716]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[717]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[718]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[719]" -type "float3" -3.7252903e-09 2.9802322e-08 9.3132257e-10 ;
	setAttr ".pt[720]" -type "float3" 3.7252903e-09 2.9802322e-08 0 ;
	setAttr ".pt[721]" -type "float3" -3.7252903e-09 2.9802322e-08 -9.3132257e-10 ;
	setAttr ".pt[722]" -type "float3" 0 2.9802322e-08 1.8626451e-09 ;
	setAttr ".pt[723]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[724]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[725]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[726]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[727]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[728]" -type "float3" 0 2.9802322e-08 1.8626451e-09 ;
	setAttr ".pt[729]" -type "float3" 3.7252903e-09 2.9802322e-08 -9.3132257e-10 ;
	setAttr ".pt[730]" -type "float3" -3.7252903e-09 2.9802322e-08 0 ;
	setAttr ".pt[731]" -type "float3" 3.7252903e-09 2.9802322e-08 9.3132257e-10 ;
	setAttr ".pt[732]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[733]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[734]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[735]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[736]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[737]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[739]" -type "float3" 7.4505806e-09 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[740]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[741]" -type "float3" 1.4901161e-08 0 -1.4901161e-08 ;
	setAttr ".pt[742]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[743]" -type "float3" 1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[744]" -type "float3" -1.4901161e-08 0 1.4901161e-08 ;
	setAttr ".pt[745]" -type "float3" 0 0 3.7252903e-09 ;
	setAttr ".pt[746]" -type "float3" 1.4901161e-08 2.9802322e-08 0 ;
	setAttr ".pt[748]" -type "float3" 0 0 3.5527137e-15 ;
	setAttr ".pt[749]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[750]" -type "float3" 1.4901161e-08 0 7.1054274e-15 ;
	setAttr ".pt[751]" -type "float3" 1.4901161e-08 -2.9802322e-08 -3.7252903e-09 ;
	setAttr ".pt[752]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[753]" -type "float3" -2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[754]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[755]" -type "float3" 1.4901161e-08 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[757]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[758]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[761]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[762]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[763]" -type "float3" 5.5511151e-17 0 0 ;
	setAttr ".pt[764]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[766]" -type "float3" -3.7252903e-09 0 -1.4901161e-08 ;
	setAttr ".pt[767]" -type "float3" 7.4505806e-09 -2.9802322e-08 0 ;
	setAttr ".pt[768]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[769]" -type "float3" -7.4505806e-09 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[770]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[772]" -type "float3" 0 -2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[773]" -type "float3" -1.4901161e-08 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[774]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[776]" -type "float3" -1.4901161e-08 2.9802322e-08 7.4505806e-09 ;
	setAttr ".pt[777]" -type "float3" 2.9802322e-08 0 -7.4505806e-09 ;
	setAttr ".pt[778]" -type "float3" 0 0 3.5527137e-15 ;
	setAttr ".pt[779]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[780]" -type "float3" -1.4901161e-08 0 7.1054274e-15 ;
	setAttr ".pt[781]" -type "float3" -1.4901161e-08 -2.9802322e-08 3.7252903e-09 ;
	setAttr ".pt[782]" -type "float3" 1.4901161e-08 0 -7.4505806e-09 ;
	setAttr ".pt[784]" -type "float3" 0 -2.9802322e-08 -7.4505806e-09 ;
	setAttr ".pt[785]" -type "float3" -1.4901161e-08 -2.9802322e-08 0 ;
	setAttr ".pt[787]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[788]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[791]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[792]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[794]" -type "float3" 0 -2.9802322e-08 0 ;
	setAttr ".pt[796]" -type "float3" -2.220446e-16 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[797]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[798]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[799]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[800]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[801]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[802]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[803]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[804]" -type "float3" 1.4901161e-08 0 -1.4901161e-08 ;
	setAttr ".pt[805]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[807]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[808]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[809]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[810]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[811]" -type "float3" -2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[812]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[813]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[814]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[815]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[816]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[817]" -type "float3" 2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[818]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[819]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[820]" -type "float3" 0 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[823]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[824]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[825]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[826]" -type "float3" -2.220446e-16 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[827]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[828]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[829]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[830]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[831]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[832]" -type "float3" 0 2.9802322e-08 2.9802322e-08 ;
	setAttr ".pt[835]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[836]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[837]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[838]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[839]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[840]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[841]" -type "float3" 2.9802322e-08 -2.9802322e-08 0 ;
	setAttr ".pt[842]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[843]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[844]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[845]" -type "float3" 0 0 -7.4505806e-09 ;
	setAttr ".pt[846]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[847]" -type "float3" -2.9802322e-08 2.9802322e-08 0 ;
	setAttr ".pt[848]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[849]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[850]" -type "float3" 0 2.9802322e-08 -2.9802322e-08 ;
	setAttr ".pt[851]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[852]" -type "float3" 1.4901161e-08 0 1.4901161e-08 ;
	setAttr ".pt[853]" -type "float3" 0 2.9802322e-08 0 ;
	setAttr ".pt[854]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[855]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr -s 856 ".vt";
	setAttr ".vt[0:165]"  -1.45257628 1.41625166 1.3147157e-07 -1.56086981 1.36016774 1.3258267e-07
		 -1.64238274 1.27006435 1.3680587e-07 -1.58820677 0.96203381 1.4723105e-07 -1.47484791 0.79817647 1.5048283e-07
		 -1.34836912 0.64351654 1.5280892e-07 -1.20937586 0.49874344 1.5420048e-07 -1.059008479 0.36500251 1.5464816e-07
		 -1.16543245 1.36802888 1.1753799e-07 -0.99738419 1.25921535 1.1753799e-07 -0.84421438 1.12914002 1.1753799e-07
		 -0.7080425 0.97969228 1.1753799e-07 -0.5913434 0.81368858 1.1753799e-07 3.693631e-09 0.43278256 -0.48659113
		 -0.14950241 0.43278256 -0.46277589 -0.28514892 0.43278256 -0.39366058 -0.39279795 0.43278256 -0.2860111
		 -0.46191329 0.43278256 -0.15036465 -0.44542673 0.46571332 1.3319521e-07 -0.46191329 0.43278256 0.15036502
		 -0.39279795 0.43278256 0.28601155 -0.28514844 0.43278256 0.39366058 -0.14950241 0.43278256 0.46277589
		 3.693631e-09 0.43278256 0.48659164 0 0 -0.55238116 -0.17069538 0 -0.5253455 -0.32468188 0 -0.44688606
		 -0.44688606 0 -0.32468188 -0.5253455 0 -0.17069513 -0.55238116 0 1.2000429e-07 -0.5253455 0 0.17069538
		 -0.44688606 0 0.32468188 -0.32468188 0 0.44688606 -0.17069538 0 0.5253455 0 0 0.55238116
		 0 0.030542828 -0.71425194 0 0.014802977 -0.70674682 0 0.0038974679 -0.69303691 0 0 -0.67587477
		 -0.22071615 0.030542828 -0.67929351 -0.21839687 0.014802977 -0.67215598 -0.21416035 0.0038974679 -0.6591177
		 -0.20885664 0 -0.64279544 -0.41982701 0.030542828 -0.577842 -0.41541517 0.014802977 -0.57176942
		 -0.40735677 0.0038974679 -0.56067836 -0.39726931 0 -0.54679346 -0.577842 0.030542828 -0.41982654
		 -0.57177037 0.014802977 -0.41541517 -0.56067836 0.0038974679 -0.40735677 -0.54679346 0 -0.39726856
		 -0.67929596 0.030548673 -0.22071654 -0.67215753 0.014806874 -0.21839711 -0.6591211 0.0038974679 -0.21416122
		 -0.64280277 0 -0.20885904 -0.72104961 0.025089098 1.4900033e-07 -0.71039051 0.011770315 1.4833412e-07
		 -0.69568735 0.0030424013 1.4789732e-07 -0.67881393 0 1.4774517e-07 -0.67929596 0.030548673 0.22071677
		 -0.67215753 0.014806874 0.21839736 -0.6591211 0.0038974679 0.21416159 -0.64280277 0 0.20885904
		 -0.577842 0.030542828 0.41982728 -0.57176942 0.014802977 0.41541517 -0.56067836 0.0038974679 0.40735748
		 -0.54679346 0 0.39726931 -0.41982654 0.030542828 0.577842 -0.41541517 0.014802977 0.57177037
		 -0.40735677 0.0038974679 0.56067836 -0.39726931 0 0.54679346 -0.22071593 0.030542828 0.67929351
		 -0.21839687 0.014802977 0.67215598 -0.21416035 0.0038974679 0.6591177 -0.20885664 0 0.64279544
		 0 0.030542828 0.71425194 0 0.014802977 0.70674682 0 0.0038974679 0.69303691 0 0 0.67587477
		 -1.26747561 1.22458017 0.17919675 -1.1273967 1.089168072 0.18207918 -0.98517126 0.95012903 0.18291125
		 -0.84244961 0.80943459 0.18215722 -0.70140547 0.6690712 0.17960441 -0.69899619 0.67144752 -0.17916143
		 -0.84128046 0.81059545 -0.18195988 -0.98465514 0.95063943 -0.18282518 -1.12700486 1.089553833 -0.18201029
		 -1.26652527 1.22551918 -0.17900635 0 0.5433861 -0.61235976 0 0.55300027 -0.60652816
		 0 0.55977845 -0.59750074 -0.18922991 0.5433861 -0.58238864 -0.18742737 0.55300027 -0.57684183
		 -0.18463793 0.55977845 -0.56825709 -0.35993683 0.5433861 -0.49540985 -0.35650805 0.55300027 -0.49069121
		 -0.35120207 0.55977845 -0.48338807 -0.49540985 0.5433861 -0.35993612 -0.49069121 0.55300027 -0.35650805
		 -0.48338807 0.55977845 -0.35120207 -0.56693214 0.56379479 -0.1867291 -0.56209755 0.55980968 -0.19658245
		 -0.57077408 0.55297303 -0.19931979 -0.57638264 0.54324979 -0.20112574 -0.58394921 0.54487431 -0.19221509
		 -0.58397746 0.54493266 0.19218551 -0.5764187 0.54330826 0.20101203 -0.57076478 0.55298084 0.19933073
		 -0.56197917 0.55984867 0.19666158 -0.56681716 0.56381428 0.18670949 -0.49540985 0.5433861 0.35993683
		 -0.49069121 0.55300027 0.35650805 -0.48338807 0.55977845 0.35120207 -0.35993612 0.5433861 0.49540985
		 -0.35650805 0.55300027 0.49069121 -0.35120207 0.55977845 0.48338807 -0.18922991 0.5433861 0.58239007
		 -0.18742737 0.55300027 0.57684183 -0.18463793 0.55977845 0.56825709 0 0.5433861 0.61235976
		 0 0.55300027 0.60652816 0 0.55977845 0.59750074 -0.71404499 0.17273125 -0.2210865
		 -0.72383296 0.18396398 -0.21729006 -0.72049016 0.18998453 -0.22653133 -0.71678597 0.2010147 -0.22932757
		 -0.70742017 0.19314185 -0.23275504 -0.70077693 0.18968068 -0.24124603 -0.70486814 0.17486405 -0.23887503
		 -0.70799088 0.1674061 -0.23003975 -0.70477462 0.17486796 0.23902401 -0.70060396 0.1898696 0.24143253
		 -0.70737147 0.19323534 0.23279643 -0.71676165 0.200929 0.22933368 -0.72033048 0.18985403 0.22662374
		 -0.72351015 0.18384324 0.2176168 -0.71386242 0.17261441 0.22132826 -0.7079699 0.16731066 0.23003364
		 0 0.18981507 -0.74301791 0 0.17894463 -0.74534988 0 0.16786577 -0.74452651 -0.22960502 0.18981507 -0.70665228
		 -0.23032558 0.17894463 -0.70886981 -0.23007138 0.16786577 -0.70808631 -0.43673506 0.18981507 -0.60111433
		 -0.43810531 0.17894463 -0.60300028 -0.4376218 0.16786577 -0.60233414 -0.60111433 0.18981507 -0.43673506
		 -0.60300028 0.17894463 -0.43810531 -0.60233414 0.16786577 -0.4376218 -0.79012108 0.14415568 1.5460205e-07
		 -0.78227502 0.13632569 1.5447655e-07 -0.77610695 0.12716343 1.5410772e-07 -0.60111433 0.18981507 0.43673506
		 -0.60300028 0.17894463 0.43810531 -0.60233414 0.16786577 0.4376218 -0.43673506 0.18981507 0.60111433
		 -0.43810531 0.17894463 0.60300028 -0.4376218 0.16786577 0.60233414 -0.22960502 0.18981507 0.70665228
		 -0.23032558 0.17894463 0.70886981 -0.23007138 0.16786577 0.70808631 0 0.18981507 0.74301791
		 0 0.17894463 0.74534988 0 0.16786577 0.74452651;
	setAttr ".vt[166:331]" 0 0.59178406 -0.53208524 0 0.59552777 -0.52153468 0 0.59679365 -0.5103991
		 -0.16442335 0.59178406 -0.50604272 -0.1611634 0.59552777 -0.49600956 -0.15772207 0.59679365 -0.48541841
		 -0.31275186 0.59178406 -0.43046552 -0.30655044 0.59552777 -0.42193088 -0.30000523 0.59679365 -0.41292155
		 -0.43046597 0.59178406 -0.31275111 -0.42193061 0.59552777 -0.30655044 -0.41292155 0.59679365 -0.30000475
		 -0.48951134 0.59503293 -0.17006284 -0.49950412 0.59181136 -0.1771231 -0.50696135 0.59450316 -0.16822512
		 -0.51464379 0.60226691 -0.16494863 -0.50585938 0.6070078 -0.15898153 -0.50164926 0.61023724 -0.14878404
		 -0.49179801 0.60016727 -0.15072194 -0.48415813 0.59679365 -0.15741104 -0.48520383 0.6404897 1.1753799e-07
		 -0.47700962 0.63260913 1.1687853e-07 -0.46601284 0.62973428 1.1506816e-07 -0.49191004 0.60018671 0.15076455
		 -0.50164926 0.61023724 0.14878429 -0.5057773 0.60694933 0.15897766 -0.51439834 0.60220063 0.16489968
		 -0.50676316 0.59455764 0.16804326 -0.49941206 0.59194767 0.17667061 -0.48958752 0.59509915 0.16973671
		 -0.48433957 0.59679365 0.15746887 -0.43046597 0.59178406 0.31275186 -0.42193061 0.59552777 0.30655044
		 -0.41292155 0.59679365 0.30000523 -0.31275186 0.59178406 0.43046597 -0.30655044 0.59552777 0.42193061
		 -0.30000523 0.59679365 0.41292155 -0.16442335 0.59178406 0.50604272 -0.16116303 0.59552777 0.49600956
		 -0.15772207 0.59679365 0.48541841 0 0.59178406 0.53208524 0 0.59552777 0.52153468
		 0 0.59679365 0.5103991 -1.62989628 1.1259768 -0.22624379 -1.63620436 1.12392771 -0.21634126
		 -1.63956523 1.13490534 -0.21672571 -1.63608634 1.14622188 -0.21653715 -1.6301409 1.14231074 -0.22585911
		 -1.62227976 1.13374448 -0.22933999 -1.70540738 1.16855097 1.4232332e-07 -1.70844173 1.15754604 1.4282355e-07
		 -1.70511305 1.14643216 1.4316421e-07 -1.57832956 1.20107841 -0.22109586 -1.58701766 1.20819569 -0.21805531
		 -1.59227645 1.21310794 -0.2088896 -1.62989628 1.1259768 0.22624417 -1.62227976 1.13374448 0.22934026
		 -1.63012338 1.14236915 0.2258238 -1.63605917 1.14630747 0.2164311 -1.63956809 1.13493252 0.21667103
		 -1.63620436 1.12392771 0.2163416 -1.59227645 1.21310794 0.20888987 -1.58701766 1.20819569 0.21805565
		 -1.57832956 1.20107841 0.2210961 -1.33464813 1.45273304 1.1876605e-07 -1.32348943 1.45380819 1.1785794e-07
		 -1.31276798 1.45039189 1.1753799e-07 -1.31787014 1.38425756 -0.15960653 -1.32633996 1.37844551 -0.16484016
		 -1.33490133 1.38539124 -0.16131058 -1.33792627 1.39179158 -0.15181902 -1.32632542 1.39360297 -0.15011656
		 -1.31476545 1.39034247 -0.14968854 -1.31787014 1.38426924 0.15960264 -1.31476545 1.39034247 0.1496889
		 -1.32584429 1.39350557 0.15045048 -1.33717239 1.39177203 0.15241358 -1.33440065 1.38535225 0.16152933
		 -1.32633996 1.37844551 0.1648404 -1.40799785 1.36441398 -0.16844583 -1.40298533 1.35906529 -0.17745471
		 -1.39513874 1.35123134 -0.18076909 -1.40799499 1.36440206 0.16845787 -1.40296781 1.35901463 0.17746189
		 -1.39507353 1.35103655 0.18078077 -1.51093018 1.30365539 -0.19272381 -1.50618351 1.29803419 -0.20173584
		 -1.49900293 1.28926528 -0.20492093 -1.49900293 1.28926528 0.20492117 -1.50618351 1.29803419 0.20173623
		 -1.51093018 1.30365539 0.19272403 -1.40863287 0.81244969 -0.21690623 -1.40239525 0.81572986 -0.22635932
		 -1.39314437 0.82256639 -0.22903834 -1.51321781 0.98052585 -0.22878805 -1.52279484 0.97414112 -0.22613813
		 -1.52898967 0.97121167 -0.21651815 -1.27736926 0.66262025 -0.21713886 -1.27119017 0.66628587 -0.22647107
		 -1.26241255 0.67371076 -0.2291317 -1.1358763 0.52244771 -0.21720301 -1.12981677 0.52649903 -0.2264908
		 -1.12153053 0.53450823 -0.22911419 -0.98293132 0.39105377 -0.21715164 -0.97839409 0.39653668 -0.22644186
		 -0.97111136 0.40533867 -0.2289972 -1.52898967 0.97121167 0.21651839 -1.52279484 0.97414112 0.22613837
		 -1.51321781 0.98052585 0.22878844 -1.40862405 0.81244969 0.21694334 -1.40240681 0.81571031 0.22637258
		 -1.39320469 0.82251966 0.22904807 -1.27735579 0.66262025 0.21717964 -1.27120376 0.66626644 0.22648568
		 -1.26247287 0.67365235 0.22914231 -1.13584709 0.52245551 0.2172903 -1.12982464 0.5264796 0.22651891
		 -1.12159336 0.53444201 0.22912538 -0.97111136 0.4053328 0.22899756 -0.97839409 0.39653668 0.2264421
		 -0.98293132 0.39105377 0.21715188 -1.18730009 1.30325806 0.16312577 -1.18024731 1.31108427 0.15838397
		 -1.1770072 1.31669366 0.14881729 -1.0081889629 1.21101213 0.14876129 -1.010940075 1.20515716 0.15830056
		 -1.01678443 1.19629872 0.16288644 -0.85429251 1.083430052 0.14851172 -0.85743231 1.077929497 0.15819964
		 -0.86433518 1.069803357 0.16283178 -0.71760213 0.93586373 0.14830466 -0.72109586 0.93073714 0.15813914
		 -0.72893953 0.9234916 0.16287377 -0.6007126 0.77128965 0.14789087 -0.60397559 0.76589042 0.15807998
		 -0.6112237 0.75793201 0.16303238 -1.1770072 1.31669366 -0.14881729 -1.18024731 1.31108427 -0.1583837
		 -1.18730009 1.30325806 -0.16312553 -1.0081889629 1.21101213 -0.14876103 -1.010924578 1.20517659 -0.15829691
		 -1.016726494 1.1963768 -0.16287377 -0.85429251 1.083430052 -0.1485116 -0.85740894 1.077948809 -0.15819538
		 -0.86424947 1.069892883 -0.16281694 -0.71760213 0.93586373 -0.14830466 -0.72106421 0.93076444 -0.15813401
		 -0.72882557 0.92358893 -0.16285625 -0.6112237 0.75793201 -0.16303216 -0.60397559 0.76589042 -0.15807961
		 -0.6007126 0.77128965 -0.14789087 0 0.59679365 -0.50234026 0 0.59223986 -0.4912039
		 0 0.5812428 -0.48659113 -0.154369 0.59679365 -0.47775367 -0.15092781 0.59223986 -0.46716249
		 -0.14950241 0.5812428 -0.46277589 -0.2944054 0.59679365 -0.40640166 -0.28785998 0.59223986 -0.39739251
		 -0.28514892 0.5812428 -0.39366058 -0.40553924 0.59679365 -0.29526803 -0.39652988 0.59223986 -0.2887221
		 -0.39279795 0.5812428 -0.2860111 -0.47717083 0.59679365 -0.15519814 -0.46638218 0.59229439 -0.15178043
		 -0.46191329 0.58143377 -0.15036502;
	setAttr ".vt[332:497]" -0.46089044 0.62973428 1.1406422e-07 -0.44995624 0.62512195 1.119211e-07
		 -0.44542673 0.61400026 1.1103342e-07 -0.47717083 0.59679365 0.15519814 -0.46638218 0.59229439 0.15178068
		 -0.46191329 0.58143377 0.15036502 -0.40553924 0.59679365 0.29526803 -0.39652988 0.59223986 0.28872257
		 -0.39279795 0.5812428 0.28601155 -0.2944054 0.59679365 0.40640166 -0.28785998 0.59223986 0.39739251
		 -0.28514844 0.5812428 0.39366058 -0.154369 0.59679365 0.47775367 -0.15092781 0.59223986 0.46716249
		 -0.14950241 0.5812428 0.46277589 0 0.59679365 0.50234026 0 0.59223986 0.49120447
		 0 0.5812428 0.48659113 -0.59409368 0.548127 -0.18909295 -0.58583665 0.56210017 -0.18649037
		 -0.57277393 0.5722481 -0.18250659 -0.57262981 0.57220912 0.18245012 -0.58591986 0.56202233 0.18649426
		 -0.59418809 0.5482049 0.18909684 -0.57734382 0.55582452 -0.19008009 -0.57736433 0.55580509 0.19007912
		 -0.7109924 0.17963219 -0.23019105 -0.71089208 0.17957765 0.23029841 -0.49697176 0.59809095 -0.16174614
		 -0.49696568 0.59811819 0.16164547 -1.63450503 1.13422751 -0.22464286 -1.63450193 1.13425469 0.22461778
		 -1.32639253 1.38842583 -0.15822594 -1.32601082 1.38835955 0.15839186 1.45257628 1.41625166 1.3147157e-07
		 1.56086981 1.36016774 1.3258267e-07 1.64238274 1.27006435 1.3680587e-07 1.58820677 0.96203381 1.4723105e-07
		 1.47484791 0.79817647 1.5048283e-07 1.34836912 0.64351654 1.5280892e-07 1.20937586 0.49874344 1.5420048e-07
		 1.059008479 0.36500251 1.5464816e-07 1.16543245 1.36802888 1.1753799e-07 0.99738419 1.25921535 1.1753799e-07
		 0.84421438 1.12914002 1.1753799e-07 0.7080425 0.97969228 1.1753799e-07 0.5913434 0.81368858 1.1753799e-07
		 0.14950241 0.43278256 -0.46277589 0.28514892 0.43278256 -0.39366058 0.39279795 0.43278256 -0.2860111
		 0.46191329 0.43278256 -0.15036465 0.44542673 0.46571332 1.3319521e-07 0.46191329 0.43278256 0.15036502
		 0.39279795 0.43278256 0.28601155 0.28514844 0.43278256 0.39366058 0.14950241 0.43278256 0.46277589
		 0.17069538 0 -0.5253455 0.32468188 0 -0.44688606 0.44688606 0 -0.32468188 0.5253455 0 -0.17069513
		 0.55238116 0 1.2000429e-07 0.5253455 0 0.17069538 0.44688606 0 0.32468188 0.32468188 0 0.44688606
		 0.17069538 0 0.5253455 0.22071615 0.030542828 -0.67929351 0.21839687 0.014802977 -0.67215598
		 0.21416035 0.0038974679 -0.6591177 0.20885664 0 -0.64279544 0.41982701 0.030542828 -0.577842
		 0.41541517 0.014802977 -0.57176942 0.40735677 0.0038974679 -0.56067836 0.39726931 0 -0.54679346
		 0.577842 0.030542828 -0.41982654 0.57177037 0.014802977 -0.41541517 0.56067836 0.0038974679 -0.40735677
		 0.54679346 0 -0.39726856 0.67929596 0.030548673 -0.22071654 0.67215753 0.014806874 -0.21839711
		 0.6591211 0.0038974679 -0.21416122 0.64280277 0 -0.20885904 0.72104961 0.025089098 1.4900033e-07
		 0.71039051 0.011770315 1.4833412e-07 0.69568735 0.0030424013 1.4789732e-07 0.67881393 0 1.4774517e-07
		 0.67929596 0.030548673 0.22071677 0.67215753 0.014806874 0.21839736 0.6591211 0.0038974679 0.21416159
		 0.64280277 0 0.20885904 0.577842 0.030542828 0.41982728 0.57176942 0.014802977 0.41541517
		 0.56067836 0.0038974679 0.40735748 0.54679346 0 0.39726931 0.41982654 0.030542828 0.577842
		 0.41541517 0.014802977 0.57177037 0.40735677 0.0038974679 0.56067836 0.39726931 0 0.54679346
		 0.22071593 0.030542828 0.67929351 0.21839687 0.014802977 0.67215598 0.21416035 0.0038974679 0.6591177
		 0.20885664 0 0.64279544 1.26747561 1.22458017 0.17919675 1.1273967 1.089168072 0.18207918
		 0.98517126 0.95012903 0.18291125 0.84244961 0.80943459 0.18215722 0.70140547 0.6690712 0.17960441
		 0.69899619 0.67144752 -0.17916143 0.84128046 0.81059545 -0.18195988 0.98465514 0.95063943 -0.18282518
		 1.12700486 1.089553833 -0.18201029 1.26652527 1.22551918 -0.17900635 0.18922991 0.5433861 -0.58238864
		 0.18742737 0.55300027 -0.57684183 0.18463793 0.55977845 -0.56825709 0.35993683 0.5433861 -0.49540985
		 0.35650805 0.55300027 -0.49069121 0.35120207 0.55977845 -0.48338807 0.49540985 0.5433861 -0.35993612
		 0.49069121 0.55300027 -0.35650805 0.48338807 0.55977845 -0.35120207 0.56693214 0.56379479 -0.1867291
		 0.56209755 0.55980968 -0.19658245 0.57077408 0.55297303 -0.19931979 0.57638264 0.54324979 -0.20112574
		 0.58394921 0.54487431 -0.19221509 0.58397746 0.54493266 0.19218551 0.5764187 0.54330826 0.20101203
		 0.57076478 0.55298084 0.19933073 0.56197917 0.55984867 0.19666158 0.56681716 0.56381428 0.18670949
		 0.49540985 0.5433861 0.35993683 0.49069121 0.55300027 0.35650805 0.48338807 0.55977845 0.35120207
		 0.35993612 0.5433861 0.49540985 0.35650805 0.55300027 0.49069121 0.35120207 0.55977845 0.48338807
		 0.18922991 0.5433861 0.58239007 0.18742737 0.55300027 0.57684183 0.18463793 0.55977845 0.56825709
		 0.71404499 0.17273125 -0.2210865 0.72383296 0.18396398 -0.21729006 0.72049016 0.18998453 -0.22653133
		 0.71678597 0.2010147 -0.22932757 0.70742017 0.19314185 -0.23275504 0.70077693 0.18968068 -0.24124603
		 0.70486814 0.17486405 -0.23887503 0.70799088 0.1674061 -0.23003975 0.70477462 0.17486796 0.23902401
		 0.70060396 0.1898696 0.24143253 0.70737147 0.19323534 0.23279643 0.71676165 0.200929 0.22933368
		 0.72033048 0.18985403 0.22662374 0.72351015 0.18384324 0.2176168 0.71386242 0.17261441 0.22132826
		 0.7079699 0.16731066 0.23003364 0.22960502 0.18981507 -0.70665228 0.23032558 0.17894463 -0.70886981
		 0.23007138 0.16786577 -0.70808631 0.43673506 0.18981507 -0.60111433 0.43810531 0.17894463 -0.60300028
		 0.4376218 0.16786577 -0.60233414 0.60111433 0.18981507 -0.43673506 0.60300028 0.17894463 -0.43810531
		 0.60233414 0.16786577 -0.4376218 0.79012108 0.14415568 1.5460205e-07 0.78227502 0.13632569 1.5447655e-07;
	setAttr ".vt[498:663]" 0.77610695 0.12716343 1.5410772e-07 0.60111433 0.18981507 0.43673506
		 0.60300028 0.17894463 0.43810531 0.60233414 0.16786577 0.4376218 0.43673506 0.18981507 0.60111433
		 0.43810531 0.17894463 0.60300028 0.4376218 0.16786577 0.60233414 0.22960502 0.18981507 0.70665228
		 0.23032558 0.17894463 0.70886981 0.23007138 0.16786577 0.70808631 0.16442335 0.59178406 -0.50604272
		 0.1611634 0.59552777 -0.49600956 0.15772207 0.59679365 -0.48541841 0.31275186 0.59178406 -0.43046552
		 0.30655044 0.59552777 -0.42193088 0.30000523 0.59679365 -0.41292155 0.43046597 0.59178406 -0.31275111
		 0.42193061 0.59552777 -0.30655044 0.41292155 0.59679365 -0.30000475 0.48951134 0.59503293 -0.17006284
		 0.49950412 0.59181136 -0.1771231 0.50696135 0.59450316 -0.16822512 0.51464379 0.60226691 -0.16494863
		 0.50585938 0.6070078 -0.15898153 0.50164926 0.61023724 -0.14878404 0.49179801 0.60016727 -0.15072194
		 0.48415813 0.59679365 -0.15741104 0.48520383 0.6404897 1.1753799e-07 0.47700962 0.63260913 1.1687853e-07
		 0.46601284 0.62973428 1.1506816e-07 0.49191004 0.60018671 0.15076455 0.50164926 0.61023724 0.14878429
		 0.5057773 0.60694933 0.15897766 0.51439834 0.60220063 0.16489968 0.50676316 0.59455764 0.16804326
		 0.49941206 0.59194767 0.17667061 0.48958752 0.59509915 0.16973671 0.48433957 0.59679365 0.15746887
		 0.43046597 0.59178406 0.31275186 0.42193061 0.59552777 0.30655044 0.41292155 0.59679365 0.30000523
		 0.31275186 0.59178406 0.43046597 0.30655044 0.59552777 0.42193061 0.30000523 0.59679365 0.41292155
		 0.16442335 0.59178406 0.50604272 0.16116303 0.59552777 0.49600956 0.15772207 0.59679365 0.48541841
		 1.62989628 1.1259768 -0.22624379 1.63620436 1.12392771 -0.21634126 1.63956523 1.13490534 -0.21672571
		 1.63608634 1.14622188 -0.21653715 1.6301409 1.14231074 -0.22585911 1.62227976 1.13374448 -0.22933999
		 1.70540738 1.16855097 1.4232332e-07 1.70844173 1.15754604 1.4282355e-07 1.70511305 1.14643216 1.4316421e-07
		 1.57832956 1.20107841 -0.22109586 1.58701766 1.20819569 -0.21805531 1.59227645 1.21310794 -0.2088896
		 1.62989628 1.1259768 0.22624417 1.62227976 1.13374448 0.22934026 1.63012338 1.14236915 0.2258238
		 1.63605917 1.14630747 0.2164311 1.63956809 1.13493252 0.21667103 1.63620436 1.12392771 0.2163416
		 1.59227645 1.21310794 0.20888987 1.58701766 1.20819569 0.21805565 1.57832956 1.20107841 0.2210961
		 1.33464813 1.45273304 1.1876605e-07 1.32348943 1.45380819 1.1785794e-07 1.31276798 1.45039189 1.1753799e-07
		 1.31787014 1.38425756 -0.15960653 1.32633996 1.37844551 -0.16484016 1.33490133 1.38539124 -0.16131058
		 1.33792627 1.39179158 -0.15181902 1.32632542 1.39360297 -0.15011656 1.31476545 1.39034247 -0.14968854
		 1.31787014 1.38426924 0.15960264 1.31476545 1.39034247 0.1496889 1.32584429 1.39350557 0.15045048
		 1.33717239 1.39177203 0.15241358 1.33440065 1.38535225 0.16152933 1.32633996 1.37844551 0.1648404
		 1.40799785 1.36441398 -0.16844583 1.40298533 1.35906529 -0.17745471 1.39513874 1.35123134 -0.18076909
		 1.40799499 1.36440206 0.16845787 1.40296781 1.35901463 0.17746189 1.39507353 1.35103655 0.18078077
		 1.51093018 1.30365539 -0.19272381 1.50618351 1.29803419 -0.20173584 1.49900293 1.28926528 -0.20492093
		 1.49900293 1.28926528 0.20492117 1.50618351 1.29803419 0.20173623 1.51093018 1.30365539 0.19272403
		 1.40863287 0.81244969 -0.21690623 1.40239525 0.81572986 -0.22635932 1.39314437 0.82256639 -0.22903834
		 1.51321781 0.98052585 -0.22878805 1.52279484 0.97414112 -0.22613813 1.52898967 0.97121167 -0.21651815
		 1.27736926 0.66262025 -0.21713886 1.27119017 0.66628587 -0.22647107 1.26241255 0.67371076 -0.2291317
		 1.1358763 0.52244771 -0.21720301 1.12981677 0.52649903 -0.2264908 1.12153053 0.53450823 -0.22911419
		 0.98293132 0.39105377 -0.21715164 0.97839409 0.39653668 -0.22644186 0.97111136 0.40533867 -0.2289972
		 1.52898967 0.97121167 0.21651839 1.52279484 0.97414112 0.22613837 1.51321781 0.98052585 0.22878844
		 1.40862405 0.81244969 0.21694334 1.40240681 0.81571031 0.22637258 1.39320469 0.82251966 0.22904807
		 1.27735579 0.66262025 0.21717964 1.27120376 0.66626644 0.22648568 1.26247287 0.67365235 0.22914231
		 1.13584709 0.52245551 0.2172903 1.12982464 0.5264796 0.22651891 1.12159336 0.53444201 0.22912538
		 0.97111136 0.4053328 0.22899756 0.97839409 0.39653668 0.2264421 0.98293132 0.39105377 0.21715188
		 1.18730009 1.30325806 0.16312577 1.18024731 1.31108427 0.15838397 1.1770072 1.31669366 0.14881729
		 1.0081889629 1.21101213 0.14876129 1.010940075 1.20515716 0.15830056 1.01678443 1.19629872 0.16288644
		 0.85429251 1.083430052 0.14851172 0.85743231 1.077929497 0.15819964 0.86433518 1.069803357 0.16283178
		 0.71760213 0.93586373 0.14830466 0.72109586 0.93073714 0.15813914 0.72893953 0.9234916 0.16287377
		 0.6007126 0.77128965 0.14789087 0.60397559 0.76589042 0.15807998 0.6112237 0.75793201 0.16303238
		 1.1770072 1.31669366 -0.14881729 1.18024731 1.31108427 -0.1583837 1.18730009 1.30325806 -0.16312553
		 1.0081889629 1.21101213 -0.14876103 1.010924578 1.20517659 -0.15829691 1.016726494 1.1963768 -0.16287377
		 0.85429251 1.083430052 -0.1485116 0.85740894 1.077948809 -0.15819538 0.86424947 1.069892883 -0.16281694
		 0.71760213 0.93586373 -0.14830466 0.72106421 0.93076444 -0.15813401 0.72882557 0.92358893 -0.16285625
		 0.6112237 0.75793201 -0.16303216 0.60397559 0.76589042 -0.15807961 0.6007126 0.77128965 -0.14789087
		 0.154369 0.59679365 -0.47775367 0.15092781 0.59223986 -0.46716249 0.14950241 0.5812428 -0.46277589
		 0.2944054 0.59679365 -0.40640166 0.28785998 0.59223986 -0.39739251 0.28514892 0.5812428 -0.39366058
		 0.40553924 0.59679365 -0.29526803 0.39652988 0.59223986 -0.2887221 0.39279795 0.5812428 -0.2860111
		 0.47717083 0.59679365 -0.15519814 0.46638218 0.59229439 -0.15178043;
	setAttr ".vt[664:829]" 0.46191329 0.58143377 -0.15036502 0.46089044 0.62973428 1.1406422e-07
		 0.44995624 0.62512195 1.119211e-07 0.44542673 0.61400026 1.1103342e-07 0.47717083 0.59679365 0.15519814
		 0.46638218 0.59229439 0.15178068 0.46191329 0.58143377 0.15036502 0.40553924 0.59679365 0.29526803
		 0.39652988 0.59223986 0.28872257 0.39279795 0.5812428 0.28601155 0.2944054 0.59679365 0.40640166
		 0.28785998 0.59223986 0.39739251 0.28514844 0.5812428 0.39366058 0.154369 0.59679365 0.47775367
		 0.15092781 0.59223986 0.46716249 0.14950241 0.5812428 0.46277589 0.59409368 0.548127 -0.18909295
		 0.58583665 0.56210017 -0.18649037 0.57277393 0.5722481 -0.18250659 0.57262981 0.57220912 0.18245012
		 0.58591986 0.56202233 0.18649426 0.59418809 0.5482049 0.18909684 0.57734382 0.55582452 -0.19008009
		 0.57736433 0.55580509 0.19007912 0.7109924 0.17963219 -0.23019105 0.71089208 0.17957765 0.23029841
		 0.49697176 0.59809095 -0.16174614 0.49696568 0.59811819 0.16164547 1.63450503 1.13422751 -0.22464286
		 1.63450193 1.13425469 0.22461778 1.32639253 1.38842583 -0.15822594 1.32601082 1.38835955 0.15839186
		 3.5801364e-09 0.43328509 -0.47163993 -0.14490874 0.43328509 -0.44855627 -0.27638707 0.43328509 -0.38156497
		 -0.3807289 0.43328509 -0.27722302 -0.44772017 0.43328509 -0.14574468 -0.43174031 0.46521083 1.2713843e-07
		 -0.44772017 0.43328509 0.14574493 -0.3807289 0.43328509 0.27722302 -0.27638707 0.43328509 0.38156497
		 -0.14490874 0.43328509 0.44855627 3.5801364e-09 0.43328509 0.47163993 0.14490874 0.43328509 -0.44855627
		 0.27638707 0.43328509 -0.38156497 0.3807289 0.43328509 -0.27722302 0.44772017 0.43328509 -0.14574468
		 0.43174031 0.46521083 1.2713843e-07 0.44772017 0.43328509 0.14574493 0.3807289 0.43328509 0.27722302
		 0.27638707 0.43328509 0.38156497 0.14490874 0.43328509 0.44855627 -0.016950307 0.65439677 -0.052469101
		 -0.032329913 0.65439677 -0.044632286 -0.044534046 0.65439677 -0.032427348 -0.052370742 0.65439677 -0.017047703
		 -0.05050122 0.65439677 1.4871609e-08 -0.052370742 0.65439677 0.017047703 -0.044534046 0.65439677 0.032427803
		 -0.032329913 0.65439677 0.044632286 -0.016950307 0.65439677 0.052469101 4.1877957e-10 0.65439677 0.05516921
		 0.016950307 0.65439677 0.052469101 0.032329913 0.65439677 0.044632286 0.044534046 0.65439677 0.032427803
		 0.052370742 0.65439677 0.017047703 0.05050122 0.65439677 1.4871609e-08 0.052370742 0.65439677 -0.017047703
		 0.044534046 0.65439677 -0.032427348 0.032329913 0.65439677 -0.044632286 0.016950307 0.65439677 -0.052469101
		 4.1877957e-10 0.65439677 -0.05516921 -0.12343779 0.608118 -0.38209382 -0.095609277 0.62624383 -0.29611239
		 -0.067365237 0.63828492 -0.2091634 -0.12869388 0.63829267 -0.17789295 -0.1824204 0.62624383 -0.25189579
		 -0.23548029 0.60811019 -0.32509047 -0.17734429 0.63829267 -0.12924996 -0.25131059 0.62624383 -0.18301861
		 -0.32440507 0.60809851 -0.23621169 -0.20152403 0.63902897 -0.065601081 -0.29419869 0.62631011 -0.095769182
		 -0.38496581 0.60722983 -0.12531622 -0.19415602 0.63904846 8.6626855e-08 -0.28487623 0.62601012 9.1262713e-08
		 -0.3743965 0.60641569 1.1025186e-07 -0.20861545 0.63829267 0.067909569 -0.29685718 0.6259712 0.096634775
		 -0.38496509 0.60722983 0.12531632 -0.17735611 0.63829267 0.1292589 -0.25131059 0.62624383 0.18301922
		 -0.32439336 0.60809851 0.23620379 -0.1287058 0.63829267 0.17790927 -0.1824204 0.62624383 0.25189579
		 -0.23546851 0.60811019 0.32507461 -0.067365237 0.63828492 0.2091634 -0.095609277 0.62624383 0.29611239
		 -0.12343767 0.608118 0.38209382 9.1294333e-10 0.63828492 0.21989471 2.1740798e-09 0.62624383 0.3113429
		 3.0496687e-09 0.608118 0.40175745 0.067356005 0.63828492 0.20913526 0.095609166 0.62624383 0.29611239
		 0.12344655 0.608118 0.38212162 0.12869388 0.63829267 0.17789295 0.1824204 0.62624383 0.25189579
		 0.23547995 0.60811019 0.32509091 0.17734429 0.63829267 0.12925047 0.25131059 0.62624383 0.18301922
		 0.32440555 0.60809851 0.23621196 0.20152403 0.63902897 0.065601237 0.29419869 0.62631011 0.095769368
		 0.38496509 0.60722983 0.12531632 0.19415602 0.63904846 8.6626855e-08 0.28487623 0.62601012 9.1262713e-08
		 0.3743965 0.60641569 1.1025186e-07 0.20861545 0.63829267 -0.067909569 0.29685718 0.6259712 -0.096634664
		 0.38496581 0.60722983 -0.12531622 0.17735611 0.63829267 -0.1292586 0.25131059 0.62624383 -0.18301861
		 0.32439336 0.60809851 -0.23620318 0.1287058 0.63829267 -0.1779089 0.1824204 0.62624383 -0.25189579
		 0.23546851 0.60811019 -0.32507461 0.067365237 0.63828492 -0.2091634 0.095609277 0.62624383 -0.29611239
		 0.12343767 0.608118 -0.38209382 9.1293645e-10 0.63828492 -0.21989471 2.174076e-09 0.62624383 -0.3113429
		 3.0496687e-09 0.608118 -0.40175745 3.5801364e-09 0.57790434 -0.47163993 3.5512995e-09 0.58870661 -0.46784076
		 3.4772452e-09 0.59485763 -0.45808524 -0.14490874 0.57790434 -0.44855627 -0.14374179 0.58870661 -0.44494316
		 -0.14074412 0.59485763 -0.43566498 -0.27638707 0.57790434 -0.38156497 -0.27415955 0.58870661 -0.37848946
		 -0.26843935 0.59485763 -0.37059253 -0.3807289 0.57790434 -0.27722302 -0.3776595 0.58870661 -0.2749877
		 -0.36977571 0.59485763 -0.26924819 -0.44772017 0.57770181 -0.14574468 -0.44405574 0.58865988 -0.14455169
		 -0.43464464 0.59490836 -0.14148822 -0.43174031 0.57800949 1.2713843e-07 -0.42802516 0.58880401 1.260444e-07
		 -0.4184376 0.5950914 1.2322114e-07 -0.44772017 0.57770181 0.14574493 -0.44405574 0.58865988 0.14455205
		 -0.43464464 0.59490836 0.14148858 -0.3807289 0.57790434 0.27722302 -0.37765875 0.58870661 0.2749877
		 -0.36977473 0.59485763 0.26924694 -0.27638707 0.57790434 0.38156497 -0.27415892 0.58870661 0.37848926
		 -0.26843762 0.59485763 0.3705906 -0.14490874 0.57790434 0.44855627 -0.14374119 0.58870661 0.44494268
		 -0.1407429 0.59485763 0.43566141 3.5801364e-09 0.57790434 0.47163993 3.5512995e-09 0.58870661 0.46784076
		 3.4772452e-09 0.59485763 0.45808524 0.14490874 0.57790434 -0.44855627;
	setAttr ".vt[830:855]" 0.14374119 0.58870661 -0.44494197 0.1407429 0.59485763 -0.43566141
		 0.27638707 0.57790434 -0.38156497 0.27415892 0.58870661 -0.37848878 0.26843762 0.59485763 -0.37059012
		 0.3807289 0.57790434 -0.27722302 0.37765875 0.58870661 -0.2749877 0.36977473 0.59485763 -0.26924694
		 0.44772017 0.57770181 -0.14574468 0.44405574 0.58865988 -0.14455169 0.43464464 0.59490836 -0.14148822
		 0.43174031 0.57800949 1.2713843e-07 0.42802516 0.58880401 1.260444e-07 0.4184376 0.5950914 1.2322114e-07
		 0.44772017 0.57770181 0.14574493 0.44405574 0.58865988 0.14455205 0.43464464 0.59490836 0.14148858
		 0.3807289 0.57790434 0.27722302 0.3776595 0.58870661 0.27498835 0.36977595 0.59485763 0.26924819
		 0.27638707 0.57790434 0.38156497 0.27415955 0.58870661 0.37849 0.26843888 0.59485763 0.37059253
		 0.14490874 0.57790434 0.44855627 0.14374141 0.58870661 0.44494316 0.14074412 0.59485763 0.43566498;
	setAttr -s 1664 ".ed";
	setAttr ".ed[0:165]"  1 0 1 2 1 1 4 3 1 5 4 1 6 5 1 7 6 1 9 8 1 10 9 1 11 10 1
		 12 11 1 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0
		 24 25 0 25 26 0 26 27 0 27 28 0 28 29 0 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 36 35 1
		 37 36 1 38 37 1 40 39 1 39 35 1 41 40 1 38 42 1 42 41 1 44 43 1 43 39 1 45 44 1 42 46 1
		 46 45 1 48 47 1 47 43 1 49 48 1 46 50 1 50 49 1 52 51 1 51 47 1 53 52 1 50 54 1 54 53 1
		 56 55 1 55 51 1 57 56 1 54 58 1 58 57 1 60 59 1 59 55 1 61 60 1 58 62 1 62 61 1 64 63 1
		 63 59 1 65 64 1 62 66 1 66 65 1 68 67 1 67 63 1 69 68 1 66 70 1 70 69 1 72 71 1 71 67 1
		 73 72 1 70 74 1 74 73 1 76 75 1 75 71 1 77 76 1 74 78 1 78 77 1 24 38 1 25 42 1 26 46 1
		 27 50 1 28 54 1 29 58 1 30 62 1 31 66 1 32 70 1 33 74 1 34 78 1 37 41 1 36 40 1 41 45 1
		 40 44 1 45 49 1 44 48 1 49 53 1 48 52 1 53 57 1 52 56 1 57 61 1 56 60 1 61 65 1 60 64 1
		 65 69 1 64 68 1 69 73 1 68 72 1 73 77 1 72 76 1 79 80 1 80 81 1 81 82 1 82 83 1 84 85 1
		 85 86 1 86 87 1 87 88 1 91 90 1 94 91 1 90 89 1 89 92 1 94 93 1 97 94 1 93 92 1 92 95 1
		 97 96 1 100 97 1 96 95 1 95 98 1 100 99 1 99 103 1 103 102 1 102 100 1 99 98 1 98 104 1
		 104 103 1 102 101 1 101 180 1 180 179 1 179 102 1 181 180 1 105 127 1 127 126 1 126 350 1
		 105 104 1 104 128 1 128 127 1 107 106 1 106 133 1 133 132 1 132 107 1 134 133 1 109 108 1
		 113 109 1 108 107 1 107 111 1 110 193 1 193 192 1 192 353 1 110 109 1 109 194 1;
	setAttr ".ed[166:331]" 194 193 1 113 112 1 116 113 1 112 111 1 111 114 1 116 115 1
		 119 116 1 115 114 1 114 117 1 119 118 1 122 119 1 118 117 1 117 120 1 122 121 1 121 120 1
		 124 123 1 123 152 1 152 151 1 151 124 1 123 130 1 130 153 1 153 152 1 126 125 1 271 126 1
		 125 124 1 124 269 1 130 129 1 150 130 1 129 128 1 128 148 1 132 131 1 131 155 1 155 154 1
		 154 132 1 131 138 1 138 156 1 156 155 1 136 135 1 286 136 1 135 134 1 134 284 1 138 137 1
		 153 138 1 137 136 1 136 151 1 140 139 1 141 140 1 143 142 1 142 139 1 141 144 1 144 143 1
		 146 145 1 145 142 1 144 147 1 147 146 1 149 148 1 148 145 1 147 150 1 150 149 1 158 157 1
		 157 154 1 156 159 1 159 158 1 161 160 1 160 157 1 159 162 1 162 161 1 164 163 1 163 160 1
		 162 165 1 165 164 1 168 167 1 171 168 1 167 166 1 166 169 1 171 170 1 174 171 1 170 169 1
		 169 172 1 174 173 1 177 174 1 173 172 1 172 175 1 177 176 1 176 178 1 178 185 1 185 177 1
		 176 175 1 175 179 1 179 178 1 183 182 1 316 183 1 182 181 1 181 314 1 185 184 1 188 185 1
		 184 183 1 183 186 1 188 187 1 187 189 1 189 196 1 196 188 1 187 186 1 186 190 1 190 189 1
		 192 191 1 301 192 1 191 190 1 190 299 1 196 195 1 199 196 1 195 194 1 194 197 1 199 198 1
		 202 199 1 198 197 1 197 200 1 202 201 1 205 202 1 201 200 1 200 203 1 205 204 1 208 205 1
		 204 203 1 203 206 1 208 207 1 207 206 1 210 209 1 262 210 1 209 214 1 214 260 1 212 211 1
		 211 216 1 216 215 1 215 212 1 211 210 1 210 217 1 217 216 1 214 213 1 213 219 1 219 218 1
		 218 214 1 213 212 1 212 220 1 220 219 1 225 224 1 224 215 1 217 226 1 226 225 1 253 218 1
		 220 251 1 222 221 1 274 222 1 221 226 1 226 272 1 224 223 1 223 228 1 228 227 1 227 224 1
		 223 222 1 222 229 1 229 228 1 256 227 1 229 254 1 237 236 1 236 230 1;
	setAttr ".ed[332:497]" 232 238 1 238 237 1 232 231 1 231 241 1 241 240 1 240 232 1
		 231 230 1 230 242 1 242 241 1 234 233 1 304 234 1 233 238 1 238 302 1 236 235 1 235 246 1
		 246 245 1 245 236 1 235 234 1 234 247 1 247 246 1 240 239 1 289 240 1 239 244 1 244 287 1
		 244 243 1 250 244 1 243 242 1 242 248 1 252 251 1 251 245 1 247 253 1 253 252 1 250 249 1
		 249 255 1 255 254 1 254 250 1 249 248 1 248 256 1 256 255 1 264 263 1 263 257 1 259 265 1
		 265 264 1 259 258 1 258 261 1 261 260 1 260 259 1 258 257 1 257 262 1 262 261 1 267 266 1
		 266 263 1 265 268 1 268 267 1 270 269 1 269 266 1 268 271 1 271 270 1 274 273 1 277 274 1
		 273 272 1 272 275 1 277 276 1 280 277 1 276 275 1 275 278 1 280 279 1 283 280 1 279 278 1
		 278 281 1 283 282 1 282 285 1 285 284 1 284 283 1 282 281 1 281 286 1 286 285 1 289 288 1
		 288 291 1 291 290 1 290 289 1 288 287 1 287 292 1 292 291 1 294 293 1 293 290 1 292 295 1
		 295 294 1 297 296 1 296 293 1 295 298 1 298 297 1 300 299 1 299 296 1 298 301 1 301 300 1
		 304 303 1 307 304 1 303 302 1 302 305 1 307 306 1 310 307 1 306 305 1 305 308 1 310 309 1
		 313 310 1 309 308 1 308 311 1 313 312 1 312 315 1 315 314 1 314 313 1 312 311 1 311 316 1
		 316 315 1 319 318 1 322 319 1 318 317 1 317 320 1 322 321 1 325 322 1 321 320 1 320 323 1
		 325 324 1 328 325 1 324 323 1 323 326 1 328 327 1 331 328 1 327 326 1 326 329 1 331 330 1
		 334 331 1 330 329 1 329 332 1 334 333 1 337 334 1 333 332 1 332 335 1 337 336 1 340 337 1
		 336 335 1 335 338 1 340 339 1 343 340 1 339 338 1 338 341 1 343 342 1 346 343 1 342 341 1
		 341 344 1 346 345 1 349 346 1 345 344 1 344 347 1 349 348 1 348 347 1 139 89 1 142 92 1
		 145 95 1 148 98 1 154 111 1 157 114 1 160 117 1 163 120 1 91 166 1;
	setAttr ".ed[498:663]" 94 169 1 97 172 1 100 175 1 113 197 1 116 200 1 119 203 1
		 122 206 1 251 1 1 0 245 1 220 2 1 0 230 1 0 248 1 215 2 1 227 2 1 1 256 1 257 4 1
		 3 262 1 263 5 1 266 6 1 269 7 1 3 217 1 3 272 1 8 302 1 232 8 1 289 8 1 151 7 1 286 7 1
		 301 83 1 186 12 1 12 299 1 316 12 1 84 314 1 88 247 1 304 88 1 250 79 1 79 287 1
		 281 6 1 278 5 1 4 275 1 298 82 1 295 81 1 80 292 1 11 296 1 10 293 1 290 9 1 311 11 1
		 308 10 1 9 305 1 85 313 1 86 310 1 87 307 1 168 317 1 171 320 1 174 323 1 177 326 1
		 185 329 1 188 332 1 196 335 1 199 338 1 202 341 1 205 344 1 208 347 1 319 13 1 322 14 1
		 325 15 1 328 16 1 331 17 1 334 18 1 337 19 1 340 20 1 343 21 1 346 22 1 349 23 1
		 35 141 1 39 144 1 43 147 1 47 150 1 51 130 1 55 153 1 59 138 1 63 156 1 67 159 1
		 71 162 1 75 165 1 274 79 1 277 80 1 280 81 1 283 82 1 284 83 1 271 84 1 268 85 1
		 265 86 1 259 87 1 260 88 1 90 93 1 93 96 1 96 99 1 350 105 1 352 181 1 101 352 1
		 352 351 1 351 350 1 353 110 1 355 134 1 106 355 1 355 354 1 354 353 1 108 112 1 112 115 1
		 115 118 1 118 121 1 140 143 1 143 146 1 146 149 1 129 149 1 137 152 1 155 158 1 158 161 1
		 161 164 1 167 170 1 170 173 1 173 176 1 184 187 1 195 198 1 198 201 1 201 204 1 204 207 1
		 216 225 1 231 237 1 246 252 1 243 249 1 219 252 1 228 255 1 258 264 1 209 261 1 264 267 1
		 267 270 1 125 270 1 221 273 1 273 276 1 276 279 1 279 282 1 135 285 1 239 288 1 291 294 1
		 294 297 1 297 300 1 191 300 1 233 303 1 303 306 1 306 309 1 309 312 1 182 315 1 318 321 1
		 321 324 1 324 327 1 327 330 1 330 333 1 333 336 1 336 339 1 339 342 1 342 345 1 345 348 1
		 101 356 1 356 351 1 103 356 1;
	setAttr ".ed[664:829]" 105 356 1 106 357 1 357 354 1 108 357 1 110 357 1 123 358 1
		 358 129 1 125 358 1 127 358 1 131 359 1 359 137 1 133 359 1 135 359 1 178 360 1 360 184 1
		 180 360 1 182 360 1 189 361 1 361 195 1 191 361 1 193 361 1 209 362 1 362 213 1 211 362 1
		 221 363 1 363 225 1 223 363 1 233 364 1 364 237 1 235 364 1 239 365 1 365 243 1 241 365 1
		 83 354 1 84 351 1 367 366 1 368 367 1 370 369 1 371 370 1 372 371 1 373 372 1 375 374 1
		 376 375 1 377 376 1 378 377 1 13 379 0 379 380 0 380 381 0 381 382 0 382 383 0 383 384 0
		 384 385 0 385 386 0 386 387 0 387 23 0 24 388 0 388 389 0 389 390 0 390 391 0 391 392 0
		 392 393 0 393 394 0 394 395 0 395 396 0 396 34 0 398 397 1 397 35 1 399 398 1 38 400 1
		 400 399 1 402 401 1 401 397 1 403 402 1 400 404 1 404 403 1 406 405 1 405 401 1 407 406 1
		 404 408 1 408 407 1 410 409 1 409 405 1 411 410 1 408 412 1 412 411 1 414 413 1 413 409 1
		 415 414 1 412 416 1 416 415 1 418 417 1 417 413 1 419 418 1 416 420 1 420 419 1 422 421 1
		 421 417 1 423 422 1 420 424 1 424 423 1 426 425 1 425 421 1 427 426 1 424 428 1 428 427 1
		 430 429 1 429 425 1 431 430 1 428 432 1 432 431 1 75 429 1 432 78 1 388 400 1 389 404 1
		 390 408 1 391 412 1 392 416 1 393 420 1 394 424 1 395 428 1 396 432 1 37 399 1 36 398 1
		 399 403 1 398 402 1 403 407 1 402 406 1 407 411 1 406 410 1 411 415 1 410 414 1 415 419 1
		 414 418 1 419 423 1 418 422 1 423 427 1 422 426 1 427 431 1 426 430 1 431 77 1 430 76 1
		 433 434 1 434 435 1 435 436 1 436 437 1 438 439 1 439 440 1 440 441 1 441 442 1 445 91 1
		 89 443 1 445 444 1 448 445 1 444 443 1 443 446 1 448 447 1 451 448 1 447 446 1 446 449 1
		 451 450 1 450 454 1 454 453 1 453 451 1 450 449 1 449 455 1 455 454 1;
	setAttr ".ed[830:995]" 453 452 1 452 519 1 519 518 1 518 453 1 520 519 1 456 475 1
		 475 474 1 474 680 1 456 455 1 455 476 1 476 475 1 458 457 1 457 481 1 481 480 1 480 458 1
		 482 481 1 460 459 1 464 460 1 459 458 1 458 462 1 461 532 1 532 531 1 531 683 1 461 460 1
		 460 533 1 533 532 1 464 463 1 467 464 1 463 462 1 462 465 1 467 466 1 470 467 1 466 465 1
		 465 468 1 470 469 1 122 470 1 469 468 1 468 120 1 472 471 1 471 497 1 497 496 1 496 472 1
		 471 478 1 478 498 1 498 497 1 474 473 1 607 474 1 473 472 1 472 605 1 478 477 1 495 478 1
		 477 476 1 476 493 1 480 479 1 479 500 1 500 499 1 499 480 1 479 486 1 486 501 1 501 500 1
		 484 483 1 622 484 1 483 482 1 482 620 1 486 485 1 498 486 1 485 484 1 484 496 1 488 487 1
		 487 139 1 141 489 1 489 488 1 491 490 1 490 487 1 489 492 1 492 491 1 494 493 1 493 490 1
		 492 495 1 495 494 1 503 502 1 502 499 1 501 504 1 504 503 1 506 505 1 505 502 1 504 507 1
		 507 506 1 163 505 1 507 165 1 510 168 1 166 508 1 510 509 1 513 510 1 509 508 1 508 511 1
		 513 512 1 516 513 1 512 511 1 511 514 1 516 515 1 515 517 1 517 524 1 524 516 1 515 514 1
		 514 518 1 518 517 1 522 521 1 652 522 1 521 520 1 520 650 1 524 523 1 527 524 1 523 522 1
		 522 525 1 527 526 1 526 528 1 528 535 1 535 527 1 526 525 1 525 529 1 529 528 1 531 530 1
		 637 531 1 530 529 1 529 635 1 535 534 1 538 535 1 534 533 1 533 536 1 538 537 1 541 538 1
		 537 536 1 536 539 1 541 540 1 544 541 1 540 539 1 539 542 1 544 543 1 208 544 1 543 542 1
		 542 206 1 546 545 1 598 546 1 545 550 1 550 596 1 548 547 1 547 552 1 552 551 1 551 548 1
		 547 546 1 546 553 1 553 552 1 550 549 1 549 555 1 555 554 1 554 550 1 549 548 1 548 556 1
		 556 555 1 561 560 1 560 551 1 553 562 1 562 561 1 589 554 1 556 587 1;
	setAttr ".ed[996:1161]" 558 557 1 610 558 1 557 562 1 562 608 1 560 559 1 559 564 1
		 564 563 1 563 560 1 559 558 1 558 565 1 565 564 1 592 563 1 565 590 1 573 572 1 572 566 1
		 568 574 1 574 573 1 568 567 1 567 577 1 577 576 1 576 568 1 567 566 1 566 578 1 578 577 1
		 570 569 1 640 570 1 569 574 1 574 638 1 572 571 1 571 582 1 582 581 1 581 572 1 571 570 1
		 570 583 1 583 582 1 576 575 1 625 576 1 575 580 1 580 623 1 580 579 1 586 580 1 579 578 1
		 578 584 1 588 587 1 587 581 1 583 589 1 589 588 1 586 585 1 585 591 1 591 590 1 590 586 1
		 585 584 1 584 592 1 592 591 1 600 599 1 599 593 1 595 601 1 601 600 1 595 594 1 594 597 1
		 597 596 1 596 595 1 594 593 1 593 598 1 598 597 1 603 602 1 602 599 1 601 604 1 604 603 1
		 606 605 1 605 602 1 604 607 1 607 606 1 610 609 1 613 610 1 609 608 1 608 611 1 613 612 1
		 616 613 1 612 611 1 611 614 1 616 615 1 619 616 1 615 614 1 614 617 1 619 618 1 618 621 1
		 621 620 1 620 619 1 618 617 1 617 622 1 622 621 1 625 624 1 624 627 1 627 626 1 626 625 1
		 624 623 1 623 628 1 628 627 1 630 629 1 629 626 1 628 631 1 631 630 1 633 632 1 632 629 1
		 631 634 1 634 633 1 636 635 1 635 632 1 634 637 1 637 636 1 640 639 1 643 640 1 639 638 1
		 638 641 1 643 642 1 646 643 1 642 641 1 641 644 1 646 645 1 649 646 1 645 644 1 644 647 1
		 649 648 1 648 651 1 651 650 1 650 649 1 648 647 1 647 652 1 652 651 1 655 319 1 317 653 1
		 655 654 1 658 655 1 654 653 1 653 656 1 658 657 1 661 658 1 657 656 1 656 659 1 661 660 1
		 664 661 1 660 659 1 659 662 1 664 663 1 667 664 1 663 662 1 662 665 1 667 666 1 670 667 1
		 666 665 1 665 668 1 670 669 1 673 670 1 669 668 1 668 671 1 673 672 1 676 673 1 672 671 1
		 671 674 1 676 675 1 679 676 1 675 674 1 674 677 1 679 678 1 349 679 1;
	setAttr ".ed[1162:1327]" 678 677 1 677 347 1 487 443 1 490 446 1 493 449 1 499 462 1
		 502 465 1 505 468 1 445 508 1 448 511 1 451 514 1 464 536 1 467 539 1 470 542 1 587 367 1
		 366 581 1 556 368 1 366 566 1 366 584 1 551 368 1 563 368 1 367 592 1 593 370 1 369 598 1
		 599 371 1 602 372 1 605 373 1 369 553 1 369 608 1 374 638 1 568 374 1 625 374 1 496 373 1
		 622 373 1 637 437 1 525 378 1 378 635 1 652 378 1 438 650 1 442 583 1 640 442 1 586 433 1
		 433 623 1 617 372 1 614 371 1 370 611 1 634 436 1 631 435 1 434 628 1 377 632 1 376 629 1
		 626 375 1 647 377 1 644 376 1 375 641 1 439 649 1 440 646 1 441 643 1 510 653 1 513 656 1
		 516 659 1 524 662 1 527 665 1 535 668 1 538 671 1 541 674 1 544 677 1 655 379 1 658 380 1
		 661 381 1 664 382 1 667 383 1 670 384 1 673 385 1 676 386 1 679 387 1 397 489 1 401 492 1
		 405 495 1 409 478 1 413 498 1 417 486 1 421 501 1 425 504 1 429 507 1 610 433 1 613 434 1
		 616 435 1 619 436 1 620 437 1 607 438 1 604 439 1 601 440 1 595 441 1 596 442 1 90 444 1
		 444 447 1 447 450 1 680 456 1 682 520 1 452 682 1 682 681 1 681 680 1 683 461 1 685 482 1
		 457 685 1 685 684 1 684 683 1 459 463 1 463 466 1 466 469 1 469 121 1 140 488 1 488 491 1
		 491 494 1 477 494 1 485 497 1 500 503 1 503 506 1 506 164 1 167 509 1 509 512 1 512 515 1
		 523 526 1 534 537 1 537 540 1 540 543 1 543 207 1 552 561 1 567 573 1 582 588 1 579 585 1
		 555 588 1 564 591 1 594 600 1 545 597 1 600 603 1 603 606 1 473 606 1 557 609 1 609 612 1
		 612 615 1 615 618 1 483 621 1 575 624 1 627 630 1 630 633 1 633 636 1 530 636 1 569 639 1
		 639 642 1 642 645 1 645 648 1 521 651 1 318 654 1 654 657 1 657 660 1 660 663 1 663 666 1
		 666 669 1 669 672 1 672 675 1 675 678 1 678 348 1 452 686 1 686 681 1;
	setAttr ".ed[1328:1493]" 454 686 1 456 686 1 457 687 1 687 684 1 459 687 1 461 687 1
		 471 688 1 688 477 1 473 688 1 475 688 1 479 689 1 689 485 1 481 689 1 483 689 1 517 690 1
		 690 523 1 519 690 1 521 690 1 528 691 1 691 534 1 530 691 1 532 691 1 545 692 1 692 549 1
		 547 692 1 557 693 1 693 561 1 559 693 1 569 694 1 694 573 1 571 694 1 575 695 1 695 579 1
		 577 695 1 437 684 1 438 681 1 696 697 0 697 698 0 698 699 0 699 700 0 700 701 0 701 702 0
		 702 703 0 703 704 0 704 705 0 705 706 0 696 707 0 707 708 0 708 709 0 709 710 0 710 711 0
		 711 712 0 712 713 0 713 714 0 714 715 0 715 706 0 716 717 1 717 718 1 718 719 1 719 720 1
		 720 721 1 721 722 1 722 723 1 723 724 1 724 725 1 726 725 1 727 726 1 728 727 1 729 728 1
		 730 729 1 731 730 1 732 731 1 733 732 1 734 733 1 735 734 1 735 716 1 795 736 1 738 793 1
		 738 737 1 737 740 1 740 739 1 739 738 1 737 736 1 736 741 1 741 740 1 743 742 1 742 739 1
		 741 744 1 744 743 1 746 745 1 745 742 1 744 747 1 747 746 1 749 748 1 748 745 1 747 750 1
		 750 749 1 752 751 1 751 748 1 750 753 1 753 752 1 755 754 1 754 751 1 753 756 1 756 755 1
		 758 757 1 757 754 1 756 759 1 759 758 1 761 760 1 760 757 1 759 762 1 762 761 1 764 763 1
		 763 760 1 762 765 1 765 764 1 767 766 1 766 763 1 765 768 1 768 767 1 770 769 1 769 766 1
		 768 771 1 771 770 1 773 772 1 772 769 1 771 774 1 774 773 1 776 775 1 775 772 1 774 777 1
		 777 776 1 779 778 1 778 775 1 777 780 1 780 779 1 782 781 1 781 778 1 780 783 1 783 782 1
		 785 784 1 784 781 1 783 786 1 786 785 1 788 787 1 787 784 1 786 789 1 789 788 1 791 790 1
		 790 787 1 789 792 1 792 791 1 794 793 1 793 790 1 792 795 1 795 794 1 739 717 1 716 738 1
		 742 718 1 745 719 1 748 720 1 751 721 1 754 722 1 757 723 1 760 724 1;
	setAttr ".ed[1494:1659]" 763 725 1 766 726 1 769 727 1 772 728 1 775 729 1 778 730 1
		 781 731 1 784 732 1 787 733 1 790 734 1 793 735 1 740 743 1 743 746 1 746 749 1 749 752 1
		 752 755 1 755 758 1 758 761 1 761 764 1 764 767 1 767 770 1 770 773 1 773 776 1 776 779 1
		 779 782 1 782 785 1 785 788 1 788 791 1 791 794 1 737 794 1 830 829 1 829 796 1 798 831 1
		 831 830 1 798 797 1 801 798 1 797 796 1 796 799 1 801 800 1 804 801 1 800 799 1 799 802 1
		 804 803 1 807 804 1 803 802 1 802 805 1 807 806 1 810 807 1 806 805 1 805 808 1 810 809 1
		 813 810 1 809 808 1 808 811 1 813 812 1 816 813 1 812 811 1 811 814 1 816 815 1 819 816 1
		 815 814 1 814 817 1 819 818 1 822 819 1 818 817 1 817 820 1 822 821 1 825 822 1 821 820 1
		 820 823 1 825 824 1 828 825 1 824 823 1 823 826 1 828 827 1 855 828 1 827 826 1 826 853 1
		 833 832 1 832 829 1 831 834 1 834 833 1 836 835 1 835 832 1 834 837 1 837 836 1 839 838 1
		 838 835 1 837 840 1 840 839 1 842 841 1 841 838 1 840 843 1 843 842 1 845 844 1 844 841 1
		 843 846 1 846 845 1 848 847 1 847 844 1 846 849 1 849 848 1 851 850 1 850 847 1 849 852 1
		 852 851 1 854 853 1 853 850 1 852 855 1 855 854 1 697 799 1 796 696 1 698 802 1 699 805 1
		 700 808 1 701 811 1 702 814 1 703 817 1 704 820 1 705 823 1 706 826 1 829 707 1 832 708 1
		 835 709 1 838 710 1 841 711 1 844 712 1 847 713 1 850 714 1 853 715 1 804 741 1 736 801 1
		 807 744 1 810 747 1 813 750 1 816 753 1 819 756 1 822 759 1 825 762 1 828 765 1 855 768 1
		 852 771 1 849 774 1 846 777 1 843 780 1 840 783 1 837 786 1 834 789 1 831 792 1 798 795 1
		 797 830 1 797 800 1 800 803 1 803 806 1 806 809 1 809 812 1 812 815 1 815 818 1 818 821 1
		 821 824 1 824 827 1 830 833 1 833 836 1 836 839 1 839 842 1 842 845 1;
	setAttr ".ed[1660:1663]" 845 848 1 848 851 1 851 854 1 827 854 1;
	setAttr -s 856 ".n";
	setAttr ".n[0:165]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[166:331]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[332:497]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[498:663]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[664:829]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[830:855]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr -s 809 -ch 3268 ".fc";
	setAttr ".fc[0:499]" -type "polyFaces" 
		f 4 -37 -84 20 84
		mu 0 4 0 1 2 3
		f 4 -42 -85 21 85
		mu 0 4 4 0 3 5
		f 4 -47 -86 22 86
		mu 0 4 6 4 5 7
		f 4 -52 -87 23 87
		mu 0 4 8 6 7 9
		f 4 -57 -88 24 88
		mu 0 4 10 8 9 11
		f 4 -62 -89 25 89
		mu 0 4 12 914 913 13
		f 4 -67 -90 26 90
		mu 0 4 14 12 13 15
		f 4 -72 -91 27 91
		mu 0 4 16 14 15 17
		f 4 -77 -92 28 92
		mu 0 4 18 16 17 19
		f 4 -82 -93 29 93
		mu 0 4 20 18 19 21
		f 4 -33 36 37 -95
		mu 0 4 22 1 0 23
		f 4 -31 95 33 34
		mu 0 4 24 25 26 27
		f 4 -32 94 35 -96
		mu 0 4 25 22 23 26
		f 4 -38 41 42 -97
		mu 0 4 23 0 4 28
		f 4 -34 97 38 39
		mu 0 4 27 26 29 30
		f 4 -36 96 40 -98
		mu 0 4 26 23 28 29
		f 4 -43 46 47 -99
		mu 0 4 28 4 6 31
		f 4 -39 99 43 44
		mu 0 4 30 29 32 33
		f 4 -41 98 45 -100
		mu 0 4 29 28 31 32
		f 4 -48 51 52 -101
		mu 0 4 31 6 8 34
		f 4 -44 101 48 49
		mu 0 4 33 32 35 36
		f 4 -46 100 50 -102
		mu 0 4 32 31 34 35
		f 4 -53 56 57 -103
		mu 0 4 34 8 10 915
		f 4 -49 103 53 54
		mu 0 4 36 35 916 890
		f 4 -51 102 55 -104
		mu 0 4 35 34 915 916
		f 4 -58 61 62 -105
		mu 0 4 37 914 12 40
		f 4 -54 105 58 59
		mu 0 4 39 38 41 42
		f 4 -56 104 60 -106
		mu 0 4 38 37 40 41
		f 4 -63 66 67 -107
		mu 0 4 40 12 14 43
		f 4 -59 107 63 64
		mu 0 4 42 41 44 45
		f 4 -61 106 65 -108
		mu 0 4 41 40 43 44
		f 4 -68 71 72 -109
		mu 0 4 43 14 16 46
		f 4 -64 109 68 69
		mu 0 4 45 44 47 48
		f 4 -66 108 70 -110
		mu 0 4 44 43 46 47
		f 4 -73 76 77 -111
		mu 0 4 46 16 18 49
		f 4 -69 111 73 74
		mu 0 4 48 47 50 51
		f 4 -71 110 75 -112
		mu 0 4 47 46 49 50
		f 4 -78 81 82 -113
		mu 0 4 49 18 20 52
		f 4 -74 113 78 79
		mu 0 4 51 50 53 54
		f 4 -76 112 80 -114
		mu 0 4 50 49 52 53
		f 4 134 135 136 137
		mu 0 4 55 56 57 58
		f 4 138 139 140 -136
		mu 0 4 56 59 60 57
		f 4 141 142 143 144
		mu 0 4 58 61 62 63
		f 4 149 150 151 -147
		mu 0 4 64 60 65 66
		f 4 152 153 154 155
		mu 0 4 67 68 69 70
		f 4 164 165 166 -162
		mu 0 4 71 72 73 74
		f 4 181 182 183 184
		mu 0 4 75 76 912 898
		f 4 185 186 187 -183
		mu 0 4 76 79 80 912
		f 4 196 197 198 199
		mu 0 4 70 81 82 83
		f 4 200 201 202 -198
		mu 0 4 81 84 85 82
		f 4 249 250 251 252
		mu 0 4 86 87 88 89
		f 4 253 254 255 -251
		mu 0 4 87 90 63 88
		f 4 264 265 266 267
		mu 0 4 91 911 93 94
		f 4 268 269 270 -266
		mu 0 4 911 896 96 93
		f 4 297 298 299 300
		mu 0 4 97 98 910 904
		f 4 301 302 303 -299
		mu 0 4 98 101 102 910
		f 4 304 305 306 307
		mu 0 4 103 104 105 106
		f 4 308 309 310 -306
		mu 0 4 104 97 107 105
		f 4 321 322 323 324
		mu 0 4 108 109 110 111
		f 4 325 326 327 -323
		mu 0 4 109 112 113 110
		f 4 334 335 336 337
		mu 0 4 114 909 116 117
		f 4 338 339 340 -336
		mu 0 4 909 907 119 116
		f 4 345 346 347 348
		mu 0 4 120 121 122 123
		f 4 349 350 351 -347
		mu 0 4 121 124 125 122
		f 4 364 365 366 367
		mu 0 4 126 127 128 129
		f 4 368 369 370 -366
		mu 0 4 127 130 131 128
		f 4 375 376 377 378
		mu 0 4 132 133 134 135
		f 4 379 380 381 -377
		mu 0 4 133 136 137 134
		f 4 402 403 404 405
		mu 0 4 138 139 140 141
		f 4 406 407 408 -404
		mu 0 4 139 142 143 140
		f 4 409 410 411 412
		mu 0 4 144 145 146 147
		f 4 413 414 415 -411
		mu 0 4 145 148 149 146
		f 4 440 441 442 443
		mu 0 4 150 151 152 153
		f 4 444 445 446 -442
		mu 0 4 151 154 155 152
		f 4 -215 490 -126 -490
		mu 0 4 156 157 158 159
		f 4 -219 491 -130 -491
		mu 0 4 157 160 161 158
		f 4 -223 492 -134 -492
		mu 0 4 160 162 59 161
		f 4 -196 -151 -140 -493
		mu 0 4 162 65 60 59
		f 4 -200 493 -161 -156
		mu 0 4 70 83 163 67
		f 4 -227 494 -171 -494
		mu 0 4 83 164 165 163
		f 4 -231 495 -175 -495
		mu 0 4 164 166 167 165
		f 4 -235 496 -179 -496
		mu 0 4 166 168 169 167
		f 4 -124 498 -241 -498
		mu 0 4 170 171 172 173
		f 4 -128 499 -245 -499
		mu 0 4 171 174 175 172
		f 4 -132 500 -249 -500
		mu 0 4 174 55 90 175
		f 4 -138 -145 -255 -501
		mu 0 4 55 58 63 90
		f 4 -159 501 -279 -166
		mu 0 4 72 176 177 73
		f 4 -169 502 -283 -502
		mu 0 4 176 178 179 177
		f 4 -173 503 -287 -503
		mu 0 4 178 180 181 179
		f 4 -177 504 -291 -504
		mu 0 4 180 182 183 181
		f 4 -362 505 0 506
		mu 0 4 123 184 923 906
		f 4 -317 507 1 -506
		mu 0 4 184 107 905 923
		f 4 -332 -349 -507 508
		mu 0 4 118 120 123 906
		f 4 -340 -509 509 -360
		mu 0 4 119 907 186 130
		f 4 -301 510 -508 -310
		mu 0 4 97 904 905 107
		f 4 -313 -325 511 -511
		mu 0 4 100 108 111 187
		f 4 -1 512 -370 -510
		mu 0 4 186 185 131 130
		f 4 -2 -512 -329 -513
		mu 0 4 185 187 111 131
		f 4 -381 513 2 514
		mu 0 4 137 136 922 902
		f 4 -373 515 3 -514
		mu 0 4 136 190 921 922
		f 4 -384 516 4 -516
		mu 0 4 190 192 920 921
		f 4 -388 517 5 -517
		mu 0 4 192 194 899 920
		f 4 -515 518 -303 -295
		mu 0 4 137 902 102 101
		f 4 519 -321 -314 -519
		mu 0 4 189 196 197 903
		f 4 520 -345 -333 521
		mu 0 4 901 199 200 900
		f 4 522 -522 -338 -354
		mu 0 4 144 198 114 117
		f 4 -185 523 -518 -192
		mu 0 4 75 898 899 194
		f 4 -211 -205 524 -524
		mu 0 4 78 201 143 195
		f 4 -270 526 527 -275
		mu 0 4 96 896 897 203
		f 4 -264 -258 528 -527
		mu 0 4 95 204 155 202
		f 4 530 -351 -343 531
		mu 0 4 205 125 124 206
		f 4 532 533 -356 -358
		mu 0 4 126 207 148 208
		f 4 -6 -525 -408 534
		mu 0 4 193 195 143 142
		f 4 -5 -535 -402 535
		mu 0 4 191 193 142 209
		f 4 -3 536 -394 -520
		mu 0 4 189 188 210 196
		f 4 -4 -536 -398 -537
		mu 0 4 188 191 209 210
		f 4 117 -526 -427 537
		mu 0 4 211 212 213 214
		f 4 116 -538 -423 538
		mu 0 4 215 211 214 216
		f 4 114 539 -415 -534
		mu 0 4 207 217 149 148
		f 4 115 -539 -419 -540
		mu 0 4 217 215 216 149
		f 4 -426 -528 9 540
		mu 0 4 218 203 897 917
		f 4 -422 -541 8 541
		mu 0 4 220 218 917 918
		f 4 -413 542 6 -523
		mu 0 4 144 147 919 198
		f 4 -418 -542 7 -543
		mu 0 4 147 220 918 919
		f 4 -10 -529 -446 543
		mu 0 4 219 202 155 154
		f 4 -9 -544 -440 544
		mu 0 4 221 219 154 223
		f 4 -7 545 -432 -521
		mu 0 4 901 222 224 199
		f 4 -8 -545 -436 -546
		mu 0 4 222 221 223 224
		f 4 118 546 -444 -530
		mu 0 4 225 226 150 153
		f 4 119 547 -438 -547
		mu 0 4 226 227 228 150
		f 4 120 548 -434 -548
		mu 0 4 227 229 230 228
		f 4 121 -532 -430 -549
		mu 0 4 229 205 206 230
		f 4 -239 550 -451 -550
		mu 0 4 231 232 233 234
		f 4 -243 551 -455 -551
		mu 0 4 232 235 236 233
		f 4 -247 552 -459 -552
		mu 0 4 235 86 237 236
		f 4 -253 553 -463 -553
		mu 0 4 86 89 238 237
		f 4 -262 554 -467 -554
		mu 0 4 89 894 239 238
		f 4 -268 555 -471 -555
		mu 0 4 91 94 240 895
		f 4 -277 556 -475 -556
		mu 0 4 94 241 242 240
		f 4 -281 557 -479 -557
		mu 0 4 241 243 244 242
		f 4 -285 558 -483 -558
		mu 0 4 243 245 246 244
		f 4 -289 559 -487 -559
		mu 0 4 245 247 248 246
		f 4 -449 561 -11 -561
		mu 0 4 249 250 251 252
		f 4 -453 562 -12 -562
		mu 0 4 250 253 254 251
		f 4 -457 563 -13 -563
		mu 0 4 253 255 256 254
		f 4 -461 564 -14 -564
		mu 0 4 255 257 258 256
		f 4 -465 565 -15 -565
		mu 0 4 257 892 893 258
		f 4 -469 566 -16 -566
		mu 0 4 259 261 262 260
		f 4 -473 567 -17 -567
		mu 0 4 261 263 264 262
		f 4 -477 568 -18 -568
		mu 0 4 263 265 266 264
		f 4 -481 569 -19 -569
		mu 0 4 265 267 268 266
		f 4 -485 570 -20 -570
		mu 0 4 267 269 270 268
		f 4 -35 572 -216 -572
		mu 0 4 24 27 271 272
		f 4 -40 573 -220 -573
		mu 0 4 27 30 273 271
		f 4 -45 574 -224 -574
		mu 0 4 30 33 274 273
		f 4 -50 575 -194 -575
		mu 0 4 33 36 79 274
		f 4 -55 576 -187 -576
		mu 0 4 36 890 80 79
		f 4 -60 577 -209 -577
		mu 0 4 39 42 84 891
		f 4 -65 578 -202 -578
		mu 0 4 42 45 85 84
		f 4 -70 579 -228 -579
		mu 0 4 45 48 275 85
		f 4 -75 580 -232 -580
		mu 0 4 48 51 276 275
		f 4 -80 581 -236 -581
		mu 0 4 51 54 277 276
		f 6 -330 -327 -319 582 -533 -368
		mu 0 6 129 113 112 278 207 126
		f 4 -392 583 -115 -583
		mu 0 4 278 279 217 207
		f 4 -396 584 -116 -584
		mu 0 4 279 280 215 217
		f 4 -400 585 -117 -585
		mu 0 4 280 138 211 215
		f 4 -406 586 -118 -586
		mu 0 4 138 141 212 211
		f 4 -389 588 -119 -588
		mu 0 4 281 282 226 225
		f 4 -385 589 -120 -589
		mu 0 4 282 283 227 226
		f 4 -374 590 -121 -590
		mu 0 4 283 132 229 227
		f 4 -379 591 -122 -591
		mu 0 4 132 135 205 229
		f 6 -363 -531 -592 -297 -308 -316
		mu 0 6 284 125 205 135 103 106
		f 4 122 592 -127 123
		mu 0 4 170 285 286 171
		f 4 124 125 -129 -593
		mu 0 4 285 159 158 286
		f 4 126 593 -131 127
		mu 0 4 171 286 287 174
		f 4 128 129 -133 -594
		mu 0 4 286 158 161 287
		f 4 130 594 -135 131
		mu 0 4 174 287 56 55
		f 4 132 133 -139 -595
		mu 0 4 287 161 59 56
		f 4 146 147 148 595
		mu 0 4 64 66 288 289
		f 4 597 596 145 -143
		mu 0 4 61 290 291 62
		f 5 698 599 -149 -190 587
		mu 0 5 225 292 289 288 281
		f 4 161 162 163 600
		mu 0 4 71 74 293 294
		f 4 602 601 156 -154
		mu 0 4 68 295 296 69
		f 5 697 604 -164 -273 525
		mu 0 5 212 297 294 293 213
		f 4 157 605 -168 158
		mu 0 4 72 298 299 176
		f 4 159 160 -170 -606
		mu 0 4 298 67 163 299
		f 4 167 606 -172 168
		mu 0 4 176 299 300 178
		f 4 169 170 -174 -607
		mu 0 4 299 163 165 300
		f 4 171 607 -176 172
		mu 0 4 178 300 301 180
		f 4 173 174 -178 -608
		mu 0 4 300 165 167 301
		f 4 175 608 -180 176
		mu 0 4 180 301 302 182
		f 4 177 178 -181 -609
		mu 0 4 301 167 169 302
		f 4 -212 609 213 214
		mu 0 4 156 303 304 157
		f 4 -213 215 216 -610
		mu 0 4 303 272 271 304
		f 4 -214 610 217 218
		mu 0 4 157 304 305 160
		f 4 -217 219 220 -611
		mu 0 4 304 271 273 305
		f 4 -218 611 221 222
		mu 0 4 160 305 306 162
		f 4 -221 223 224 -612
		mu 0 4 305 273 274 306
		f 4 192 612 -225 193
		mu 0 4 79 307 306 274
		f 4 194 195 -222 -613
		mu 0 4 307 65 162 306
		f 4 207 613 -188 208
		mu 0 4 84 308 77 891
		f 4 209 210 -184 -614
		mu 0 4 308 201 78 77
		f 4 -199 614 225 226
		mu 0 4 83 82 309 164
		f 4 -203 227 228 -615
		mu 0 4 82 85 275 309
		f 4 -226 615 229 230
		mu 0 4 164 309 310 166
		f 4 -229 231 232 -616
		mu 0 4 309 275 276 310
		f 4 -230 616 233 234
		mu 0 4 166 310 311 168
		f 4 -233 235 236 -617
		mu 0 4 310 276 277 311
		f 4 237 617 -242 238
		mu 0 4 231 312 313 232
		f 4 239 240 -244 -618
		mu 0 4 312 173 172 313
		f 4 241 618 -246 242
		mu 0 4 232 313 314 235
		f 4 243 244 -248 -619
		mu 0 4 313 172 175 314
		f 4 245 619 -250 246
		mu 0 4 235 314 87 86
		f 4 247 248 -254 -620
		mu 0 4 314 175 90 87
		f 4 260 620 -265 261
		mu 0 4 89 315 92 894
		f 4 262 263 -269 -621
		mu 0 4 315 204 95 92
		f 4 275 621 -280 276
		mu 0 4 94 316 317 241
		f 4 277 278 -282 -622
		mu 0 4 316 73 177 317
		f 4 279 622 -284 280
		mu 0 4 241 317 318 243
		f 4 281 282 -286 -623
		mu 0 4 317 177 179 318
		f 4 283 623 -288 284
		mu 0 4 243 318 319 245
		f 4 285 286 -290 -624
		mu 0 4 318 179 181 319
		f 4 287 624 -292 288
		mu 0 4 245 319 320 247
		f 4 289 290 -293 -625
		mu 0 4 319 181 183 320
		f 4 -300 625 311 312
		mu 0 4 100 99 321 108
		f 4 -304 313 314 -626
		mu 0 4 99 903 197 321
		f 4 -339 626 330 331
		mu 0 4 118 115 322 120
		f 4 -335 332 333 -627
		mu 0 4 115 900 200 322
		f 4 -348 627 360 361
		mu 0 4 123 122 323 184
		f 4 -352 362 363 -628
		mu 0 4 122 125 284 323
		f 4 356 628 -365 357
		mu 0 4 208 324 127 126
		f 4 358 359 -369 -629
		mu 0 4 324 119 130 127
		f 4 -307 629 -364 315
		mu 0 4 106 105 323 284
		f 4 -311 316 -361 -630
		mu 0 4 105 107 184 323
		f 4 -324 630 -371 328
		mu 0 4 111 110 128 131
		f 4 -328 329 -367 -631
		mu 0 4 110 113 129 128
		f 4 -380 631 371 372
		mu 0 4 136 133 325 190
		f 4 -376 373 374 -632
		mu 0 4 133 132 283 325
		f 4 293 632 -382 294
		mu 0 4 101 326 134 137
		f 4 295 296 -378 -633
		mu 0 4 326 103 135 134
		f 4 -372 633 382 383
		mu 0 4 190 325 327 192
		f 4 -375 384 385 -634
		mu 0 4 325 283 282 327
		f 4 -383 634 386 387
		mu 0 4 192 327 328 194
		f 4 -386 388 389 -635
		mu 0 4 327 282 281 328
		f 4 188 635 -390 189
		mu 0 4 288 329 328 281
		f 4 190 191 -387 -636
		mu 0 4 329 75 194 328
		f 4 317 636 -391 318
		mu 0 4 112 330 331 278
		f 4 319 320 -393 -637
		mu 0 4 330 197 196 331
		f 4 390 637 -395 391
		mu 0 4 278 331 332 279
		f 4 392 393 -397 -638
		mu 0 4 331 196 210 332
		f 4 394 638 -399 395
		mu 0 4 279 332 333 280
		f 4 396 397 -401 -639
		mu 0 4 332 210 209 333
		f 4 398 639 -403 399
		mu 0 4 280 333 139 138
		f 4 400 401 -407 -640
		mu 0 4 333 209 142 139
		f 4 203 640 -409 204
		mu 0 4 201 334 140 143
		f 4 205 206 -405 -641
		mu 0 4 334 296 141 140
		f 4 352 641 -410 353
		mu 0 4 117 335 145 144
		f 4 354 355 -414 -642
		mu 0 4 335 208 148 145
		f 4 -412 642 416 417
		mu 0 4 147 146 336 220
		f 4 -416 418 419 -643
		mu 0 4 146 149 216 336
		f 4 -417 643 420 421
		mu 0 4 220 336 337 218
		f 4 -420 422 423 -644
		mu 0 4 336 216 214 337
		f 4 -421 644 424 425
		mu 0 4 218 337 338 203
		f 4 -424 426 427 -645
		mu 0 4 337 214 213 338
		f 4 271 645 -428 272
		mu 0 4 293 339 338 213
		f 4 273 274 -425 -646
		mu 0 4 339 96 203 338
		f 4 341 646 -429 342
		mu 0 4 124 340 341 206
		f 4 343 344 -431 -647
		mu 0 4 340 200 199 341
		f 4 428 647 -433 429
		mu 0 4 206 341 342 230
		f 4 430 431 -435 -648
		mu 0 4 341 199 224 342
		f 4 432 648 -437 433
		mu 0 4 230 342 343 228
		f 4 434 435 -439 -649
		mu 0 4 342 224 223 343
		f 4 436 649 -441 437
		mu 0 4 228 343 151 150
		f 4 438 439 -445 -650
		mu 0 4 343 223 154 151
		f 4 256 650 -447 257
		mu 0 4 204 344 152 155
		f 4 258 259 -443 -651
		mu 0 4 344 291 153 152
		f 4 447 651 -452 448
		mu 0 4 249 345 346 250
		f 4 449 450 -454 -652
		mu 0 4 345 234 233 346
		f 4 451 652 -456 452
		mu 0 4 250 346 347 253
		f 4 453 454 -458 -653
		mu 0 4 346 233 236 347
		f 4 455 653 -460 456
		mu 0 4 253 347 348 255
		f 4 457 458 -462 -654
		mu 0 4 347 236 237 348
		f 4 459 654 -464 460
		mu 0 4 255 348 349 257
		f 4 461 462 -466 -655
		mu 0 4 348 237 238 349
		f 4 463 655 -468 464
		mu 0 4 257 349 908 892
		f 4 465 466 -470 -656
		mu 0 4 349 238 239 908
		f 4 467 656 -472 468
		mu 0 4 259 350 351 261
		f 4 469 470 -474 -657
		mu 0 4 350 895 240 351
		f 4 471 657 -476 472
		mu 0 4 261 351 352 263
		f 4 473 474 -478 -658
		mu 0 4 351 240 242 352
		f 4 475 658 -480 476
		mu 0 4 263 352 353 265
		f 4 477 478 -482 -659
		mu 0 4 352 242 244 353
		f 4 479 659 -484 480
		mu 0 4 265 353 354 267
		f 4 481 482 -486 -660
		mu 0 4 353 244 246 354
		f 4 483 660 -488 484
		mu 0 4 267 354 355 269
		f 4 485 486 -489 -661
		mu 0 4 354 246 248 355
		f 4 -599 -598 661 662
		mu 0 4 292 290 61 356
		f 4 -142 -137 663 -662
		mu 0 4 61 58 57 356
		f 4 -141 -150 664 -664
		mu 0 4 57 60 64 356
		f 4 -596 -600 -663 -665
		mu 0 4 64 289 292 356
		f 4 -604 -603 665 666
		mu 0 4 297 295 68 357
		f 4 -153 -160 667 -666
		mu 0 4 68 67 298 357
		f 4 -158 -165 668 -668
		mu 0 4 298 72 71 357
		f 4 -601 -605 -667 -669
		mu 0 4 71 294 297 357
		f 4 -193 -186 669 670
		mu 0 4 307 79 76 358
		f 4 -182 -191 671 -670
		mu 0 4 76 75 329 358
		f 4 -189 -148 672 -672
		mu 0 4 329 288 66 358
		f 4 -152 -195 -671 -673
		mu 0 4 66 65 307 358
		f 4 -208 -201 673 674
		mu 0 4 308 84 81 359
		f 4 -197 -155 675 -674
		mu 0 4 81 70 69 359
		f 4 -157 -206 676 -676
		mu 0 4 69 296 334 359
		f 4 -204 -210 -675 -677
		mu 0 4 334 201 308 359
		f 4 -261 -252 677 678
		mu 0 4 315 89 88 360
		f 4 -256 -144 679 -678
		mu 0 4 88 63 62 360
		f 4 -146 -259 680 -680
		mu 0 4 62 291 344 360
		f 4 -257 -263 -679 -681
		mu 0 4 344 204 315 360
		f 4 -276 -267 681 682
		mu 0 4 316 94 93 361
		f 4 -271 -274 683 -682
		mu 0 4 93 96 339 361
		f 4 -272 -163 684 -684
		mu 0 4 339 293 74 361
		f 4 -167 -278 -683 -685
		mu 0 4 74 73 316 361
		f 4 -305 -296 685 686
		mu 0 4 104 103 326 362
		f 4 -294 -302 687 -686
		mu 0 4 326 101 98 362
		f 4 -298 -309 -687 -688
		mu 0 4 98 97 104 362
		f 4 -315 -320 688 689
		mu 0 4 321 197 330 363
		f 4 -318 -326 690 -689
		mu 0 4 330 112 109 363
		f 4 -322 -312 -690 -691
		mu 0 4 109 108 321 363
		f 4 -334 -344 691 692
		mu 0 4 322 200 340 364
		f 4 -342 -350 693 -692
		mu 0 4 340 124 121 364
		f 4 -346 -331 -693 -694
		mu 0 4 121 120 322 364
		f 4 -357 -355 694 695
		mu 0 4 324 208 335 365
		f 4 -353 -337 696 -695
		mu 0 4 335 117 116 365
		f 4 -341 -359 -696 -697
		mu 0 4 116 119 324 365
		f 5 603 -698 -587 -207 -602
		mu 0 5 295 297 212 141 296
		f 5 598 -699 529 -260 -597
		mu 0 5 290 292 225 153 291
		f 4 -777 -720 83 732
		mu 0 4 366 367 2 1
		f 4 -778 -721 776 737
		mu 0 4 368 369 367 366
		f 4 -779 -722 777 742
		mu 0 4 370 371 369 368
		f 4 -780 -723 778 747
		mu 0 4 372 373 371 370
		f 4 -781 -724 779 752
		mu 0 4 880 879 373 372
		f 4 -782 -725 780 757
		mu 0 4 376 377 375 374
		f 4 -783 -726 781 762
		mu 0 4 378 379 377 376
		f 4 -784 -727 782 767
		mu 0 4 380 381 379 378
		f 4 -785 -728 783 772
		mu 0 4 382 383 381 380
		f 4 -94 -729 784 775
		mu 0 4 20 21 383 382
		f 4 785 -734 -733 32
		mu 0 4 22 384 366 1
		f 4 -731 -730 -787 30
		mu 0 4 24 385 386 25
		f 4 786 -732 -786 31
		mu 0 4 25 386 384 22
		f 4 787 -739 -738 733
		mu 0 4 384 387 368 366
		f 4 -736 -735 -789 729
		mu 0 4 385 388 389 386
		f 4 788 -737 -788 731
		mu 0 4 386 389 387 384
		f 4 789 -744 -743 738
		mu 0 4 387 390 370 368
		f 4 -741 -740 -791 734
		mu 0 4 388 391 392 389
		f 4 790 -742 -790 736
		mu 0 4 389 392 390 387
		f 4 791 -749 -748 743
		mu 0 4 390 393 372 370
		f 4 -746 -745 -793 739
		mu 0 4 391 394 395 392
		f 4 792 -747 -792 741
		mu 0 4 392 395 393 390
		f 4 793 -754 -753 748
		mu 0 4 393 881 880 372
		f 4 -751 -750 -795 744
		mu 0 4 394 397 882 395
		f 4 794 -752 -794 746
		mu 0 4 395 882 881 393
		f 4 795 -759 -758 753
		mu 0 4 396 399 376 374
		f 4 -756 -755 -797 749
		mu 0 4 856 400 401 398
		f 4 796 -757 -796 751
		mu 0 4 398 401 399 396
		f 4 797 -764 -763 758
		mu 0 4 399 402 378 376
		f 4 -761 -760 -799 754
		mu 0 4 400 403 404 401
		f 4 798 -762 -798 756
		mu 0 4 401 404 402 399
		f 4 799 -769 -768 763
		mu 0 4 402 405 380 378
		f 4 -766 -765 -801 759
		mu 0 4 403 406 407 404
		f 4 800 -767 -800 761
		mu 0 4 404 407 405 402
		f 4 801 -774 -773 768
		mu 0 4 405 408 382 380
		f 4 -771 -770 -803 764
		mu 0 4 406 409 410 407
		f 4 802 -772 -802 766
		mu 0 4 407 410 408 405
		f 4 803 -83 -776 773
		mu 0 4 408 52 20 382
		f 4 -775 -79 -805 769
		mu 0 4 409 54 53 410
		f 4 804 -81 -804 771
		mu 0 4 410 53 52 408
		f 4 -827 -826 -825 -824
		mu 0 4 411 412 413 414
		f 4 824 -830 -829 -828
		mu 0 4 414 413 415 416
		f 4 -834 -833 -832 -831
		mu 0 4 412 417 418 419
		f 4 835 -841 -840 -839
		mu 0 4 420 421 422 415
		f 4 -845 -844 -843 -842
		mu 0 4 423 424 425 426
		f 4 850 -856 -855 -854
		mu 0 4 427 428 429 430
		f 4 -872 -871 -870 -869
		mu 0 4 431 432 878 434
		f 4 869 -875 -874 -873
		mu 0 4 434 878 857 436
		f 4 -887 -886 -885 -884
		mu 0 4 424 437 438 439
		f 4 884 -890 -889 -888
		mu 0 4 439 438 440 441
		f 4 -934 -933 -932 -931
		mu 0 4 442 443 444 445
		f 4 931 -937 -936 -935
		mu 0 4 445 444 417 446
		f 4 -949 -948 -947 -946
		mu 0 4 860 448 449 877
		f 4 946 -952 -951 -950
		mu 0 4 877 449 451 452
		f 4 -980 -979 -978 -977
		mu 0 4 453 454 876 456
		f 4 977 -983 -982 -981
		mu 0 4 456 876 869 458
		f 4 -987 -986 -985 -984
		mu 0 4 459 460 461 462
		f 4 984 -990 -989 -988
		mu 0 4 462 461 463 453
		f 4 -1004 -1003 -1002 -1001
		mu 0 4 464 465 466 467
		f 4 1001 -1007 -1006 -1005
		mu 0 4 467 466 468 469
		f 4 -1017 -1016 -1015 -1014
		mu 0 4 866 471 472 875
		f 4 1014 -1020 -1019 -1018
		mu 0 4 875 472 474 475
		f 4 -1028 -1027 -1026 -1025
		mu 0 4 476 477 478 479
		f 4 1025 -1031 -1030 -1029
		mu 0 4 479 478 480 481
		f 4 -1047 -1046 -1045 -1044
		mu 0 4 482 483 484 485
		f 4 1044 -1050 -1049 -1048
		mu 0 4 485 484 486 487
		f 4 -1058 -1057 -1056 -1055
		mu 0 4 488 489 490 491
		f 4 1055 -1061 -1060 -1059
		mu 0 4 491 490 492 493
		f 4 -1085 -1084 -1083 -1082
		mu 0 4 494 495 496 497
		f 4 1082 -1088 -1087 -1086
		mu 0 4 497 496 498 499
		f 4 -1092 -1091 -1090 -1089
		mu 0 4 500 501 502 503
		f 4 1089 -1095 -1094 -1093
		mu 0 4 503 502 504 505
		f 4 -1123 -1122 -1121 -1120
		mu 0 4 506 507 508 509
		f 4 1120 -1126 -1125 -1124
		mu 0 4 509 508 510 511
		f 4 489 814 -1165 899
		mu 0 4 156 159 512 513
		f 4 1164 818 -1166 903
		mu 0 4 513 512 514 515
		f 4 1165 822 -1167 907
		mu 0 4 515 514 416 516
		f 4 1166 828 839 882
		mu 0 4 516 416 415 422
		f 4 844 849 -1168 886
		mu 0 4 424 423 517 437
		f 4 1167 859 -1169 911
		mu 0 4 437 517 518 519
		f 4 1168 863 -1170 915
		mu 0 4 519 518 520 521
		f 4 1169 867 -497 918
		mu 0 4 521 520 169 168
		f 4 497 921 -1171 813
		mu 0 4 170 173 522 523
		f 4 1170 925 -1172 816
		mu 0 4 523 522 524 525
		f 4 1171 929 -1173 820
		mu 0 4 525 524 446 411
		f 4 1172 935 833 826
		mu 0 4 411 446 417 412
		f 4 854 959 -1174 847
		mu 0 4 430 429 526 527
		f 4 1173 963 -1175 857
		mu 0 4 527 526 528 529
		f 4 1174 967 -1176 861
		mu 0 4 529 528 530 531
		f 4 1175 971 -505 865
		mu 0 4 531 530 183 182
		f 4 -1178 -700 -1177 1040
		mu 0 4 477 872 889 534
		f 4 1176 -701 -1179 995
		mu 0 4 534 889 871 463
		f 4 -1180 1177 1027 1010
		mu 0 4 873 872 477 476
		f 4 1038 -1181 1179 1018
		mu 0 4 474 487 532 475
		f 4 988 1178 -1182 979
		mu 0 4 453 463 871 454
		f 4 1181 -1183 1003 991
		mu 0 4 870 535 465 464
		f 4 1180 1048 -1184 699
		mu 0 4 532 487 486 533
		f 4 1183 1007 1182 700
		mu 0 4 533 486 465 535
		f 4 -1186 -702 -1185 1059
		mu 0 4 492 868 888 493
		f 4 1184 -703 -1187 1051
		mu 0 4 493 888 887 539
		f 4 1186 -704 -1188 1062
		mu 0 4 539 887 886 541
		f 4 1187 -705 -1189 1066
		mu 0 4 541 886 865 543
		f 4 973 981 -1190 1185
		mu 0 4 492 458 869 868
		f 4 1189 992 999 -1191
		mu 0 4 536 457 544 545
		f 4 -1193 1011 1023 -1192
		mu 0 4 867 470 547 548
		f 4 1032 1016 1192 -1194
		mu 0 4 500 471 866 546
		f 4 878 1188 -1195 871
		mu 0 4 431 543 865 432
		f 4 1194 -1196 891 897
		mu 0 4 864 542 498 549
		f 4 955 -1199 -1198 950
		mu 0 4 451 550 863 452
		f 4 1197 -1200 938 944
		mu 0 4 862 551 510 552
		f 4 -1203 1021 1029 -1202
		mu 0 4 553 554 481 480
		f 4 1036 1034 -1205 -1204
		mu 0 4 482 555 505 556
		f 4 -1206 1086 1195 704
		mu 0 4 540 499 498 542
		f 4 -1207 1080 1205 703
		mu 0 4 538 557 499 540
		f 4 1190 1072 -1208 701
		mu 0 4 536 545 558 537
		f 4 1207 1076 1206 702
		mu 0 4 537 558 557 538
		f 4 -1209 1105 1196 -809
		mu 0 4 559 560 561 562
		f 4 -1210 1101 1208 -808
		mu 0 4 563 564 560 559
		f 4 1204 1093 -1211 -806
		mu 0 4 556 505 504 565
		f 4 1210 1097 1209 -807
		mu 0 4 565 504 564 563
		f 4 -1212 -709 1198 1104
		mu 0 4 566 883 863 550
		f 4 -1213 -708 1211 1100
		mu 0 4 568 884 883 566
		f 4 1193 -706 -1214 1091
		mu 0 4 500 546 885 501
		f 4 1213 -707 1212 1096
		mu 0 4 501 885 884 568
		f 4 -1215 1124 1199 708
		mu 0 4 567 511 510 551
		f 4 -1216 1118 1214 707
		mu 0 4 569 571 511 567
		f 4 1191 1110 -1217 705
		mu 0 4 867 548 572 570
		f 4 1216 1114 1215 706
		mu 0 4 570 572 571 569
		f 4 1200 1122 -1218 -810
		mu 0 4 573 507 506 574
		f 4 1217 1116 -1219 -811
		mu 0 4 574 506 575 576
		f 4 1218 1112 -1220 -812
		mu 0 4 576 575 577 578
		f 4 1219 1108 1202 -813
		mu 0 4 578 577 554 553
		f 4 549 1127 -1221 920
		mu 0 4 231 234 579 580
		f 4 1220 1131 -1222 923
		mu 0 4 580 579 581 582
		f 4 1221 1135 -1223 927
		mu 0 4 582 581 583 442
		f 4 1222 1139 -1224 933
		mu 0 4 442 583 584 443
		f 4 1223 1143 -1225 942
		mu 0 4 443 584 861 447
		f 4 1224 1147 -1226 948
		mu 0 4 860 585 586 448
		f 4 1225 1151 -1227 957
		mu 0 4 448 586 587 588
		f 4 1226 1155 -1228 961
		mu 0 4 588 587 589 590
		f 4 1227 1159 -1229 965
		mu 0 4 590 589 591 592
		f 4 1228 1163 -560 969
		mu 0 4 592 591 248 247
		f 4 560 709 -1230 1126
		mu 0 4 249 252 593 594
		f 4 1229 710 -1231 1129
		mu 0 4 594 593 595 596
		f 4 1230 711 -1232 1133
		mu 0 4 596 595 597 598
		f 4 1231 712 -1233 1137
		mu 0 4 598 597 599 600
		f 4 1232 713 -1234 1141
		mu 0 4 600 599 601 602
		f 4 1233 714 -1235 1145
		mu 0 4 858 859 603 604
		f 4 1234 715 -1236 1149
		mu 0 4 604 603 605 606
		f 4 1235 716 -1237 1153
		mu 0 4 606 605 607 608
		f 4 1236 717 -1238 1157
		mu 0 4 608 607 609 610
		f 4 1237 718 -571 1161
		mu 0 4 610 609 270 269
		f 4 571 900 -1239 730
		mu 0 4 24 272 611 385
		f 4 1238 904 -1240 735
		mu 0 4 385 611 612 388
		f 4 1239 908 -1241 740
		mu 0 4 388 612 613 391
		f 4 1240 880 -1242 745
		mu 0 4 391 613 436 394
		f 4 1241 873 -1243 750
		mu 0 4 394 436 857 397
		f 4 1242 895 -1244 755
		mu 0 4 856 435 441 400
		f 4 1243 888 -1245 760
		mu 0 4 400 441 440 403
		f 4 1244 912 -1246 765
		mu 0 4 403 440 614 406
		f 4 1245 916 -1247 770
		mu 0 4 406 614 615 409
		f 4 1246 919 -582 774
		mu 0 4 409 615 277 54
		f 6 1046 1203 -1248 997 1005 1008
		mu 0 6 483 482 556 616 469 468
		f 4 1247 805 -1249 1070
		mu 0 4 616 556 565 617
		f 4 1248 806 -1250 1074
		mu 0 4 617 565 563 618
		f 4 1249 807 -1251 1078
		mu 0 4 618 563 559 494;
	setAttr ".fc[500:808]"
		f 4 1250 808 -1252 1084
		mu 0 4 494 559 562 495
		f 4 1252 809 -1254 1067
		mu 0 4 619 573 574 620
		f 4 1253 810 -1255 1063
		mu 0 4 620 574 576 621
		f 4 1254 811 -1256 1052
		mu 0 4 621 576 578 488
		f 4 1255 812 -1257 1057
		mu 0 4 488 578 553 489
		f 6 994 986 975 1256 1201 1041
		mu 0 6 622 460 459 489 553 480
		f 4 -814 815 -1258 -123
		mu 0 4 170 523 623 285
		f 4 1257 817 -815 -125
		mu 0 4 285 623 512 159
		f 4 -817 819 -1259 -816
		mu 0 4 523 525 624 623
		f 4 1258 821 -819 -818
		mu 0 4 623 624 514 512
		f 4 -821 823 -1260 -820
		mu 0 4 525 411 414 624
		f 4 1259 827 -823 -822
		mu 0 4 624 414 416 514
		f 4 -1261 -838 -837 -836
		mu 0 4 420 625 626 421
		f 4 831 -835 -1262 -1263
		mu 0 4 419 418 627 628
		f 5 -1253 876 837 -1265 -1364
		mu 0 5 573 619 626 625 629
		f 4 -1266 -853 -852 -851
		mu 0 4 427 630 631 428
		f 4 842 -846 -1267 -1268
		mu 0 4 426 425 632 633
		f 5 -1197 953 852 -1270 -1363
		mu 0 5 562 561 631 630 634
		f 4 -848 856 -1271 -847
		mu 0 4 430 527 635 636
		f 4 1270 858 -850 -849
		mu 0 4 636 635 517 423
		f 4 -858 860 -1272 -857
		mu 0 4 527 529 637 635
		f 4 1271 862 -860 -859
		mu 0 4 635 637 518 517
		f 4 -862 864 -1273 -861
		mu 0 4 529 531 638 637
		f 4 1272 866 -864 -863
		mu 0 4 637 638 520 518
		f 4 -866 179 -1274 -865
		mu 0 4 531 182 302 638
		f 4 1273 180 -868 -867
		mu 0 4 638 302 169 520
		f 4 -900 -899 -1275 211
		mu 0 4 156 513 639 303
		f 4 1274 -902 -901 212
		mu 0 4 303 639 611 272
		f 4 -904 -903 -1276 898
		mu 0 4 513 515 640 639
		f 4 1275 -906 -905 901
		mu 0 4 639 640 612 611
		f 4 -908 -907 -1277 902
		mu 0 4 515 516 641 640
		f 4 1276 -910 -909 905
		mu 0 4 640 641 613 612
		f 4 -881 909 -1278 -880
		mu 0 4 436 613 641 642
		f 4 1277 906 -883 -882
		mu 0 4 642 641 516 422
		f 4 -896 874 -1279 -895
		mu 0 4 441 435 433 643
		f 4 1278 870 -898 -897
		mu 0 4 643 433 864 549
		f 4 -912 -911 -1280 885
		mu 0 4 437 519 644 438
		f 4 1279 -914 -913 889
		mu 0 4 438 644 614 440
		f 4 -916 -915 -1281 910
		mu 0 4 519 521 645 644
		f 4 1280 -918 -917 913
		mu 0 4 644 645 615 614
		f 4 -919 -234 -1282 914
		mu 0 4 521 168 311 645
		f 4 1281 -237 -920 917
		mu 0 4 645 311 277 615
		f 4 -921 922 -1283 -238
		mu 0 4 231 580 646 312
		f 4 1282 924 -922 -240
		mu 0 4 312 646 522 173
		f 4 -924 926 -1284 -923
		mu 0 4 580 582 647 646
		f 4 1283 928 -926 -925
		mu 0 4 646 647 524 522
		f 4 -928 930 -1285 -927
		mu 0 4 582 442 445 647
		f 4 1284 934 -930 -929
		mu 0 4 647 445 446 524
		f 4 -943 945 -1286 -942
		mu 0 4 443 447 450 648
		f 4 1285 949 -945 -944
		mu 0 4 648 450 862 552
		f 4 -958 960 -1287 -957
		mu 0 4 448 588 649 650
		f 4 1286 962 -960 -959
		mu 0 4 650 649 526 429
		f 4 -962 964 -1288 -961
		mu 0 4 588 590 651 649
		f 4 1287 966 -964 -963
		mu 0 4 649 651 528 526
		f 4 -966 968 -1289 -965
		mu 0 4 590 592 652 651
		f 4 1288 970 -968 -967
		mu 0 4 651 652 530 528
		f 4 -970 291 -1290 -969
		mu 0 4 592 247 320 652
		f 4 1289 292 -972 -971
		mu 0 4 652 320 183 530
		f 4 -992 -991 -1291 978
		mu 0 4 870 464 653 455
		f 4 1290 -994 -993 982
		mu 0 4 455 653 544 457
		f 4 -1011 -1010 -1292 1017
		mu 0 4 873 476 654 473
		f 4 1291 -1013 -1012 1013
		mu 0 4 473 654 547 470
		f 4 -1041 -1040 -1293 1026
		mu 0 4 477 534 655 478
		f 4 1292 -1043 -1042 1030
		mu 0 4 478 655 622 480
		f 4 -1037 1043 -1294 -1036
		mu 0 4 555 482 485 656
		f 4 1293 1047 -1039 -1038
		mu 0 4 656 485 487 474
		f 4 -995 1042 -1295 985
		mu 0 4 460 622 655 461
		f 4 1294 1039 -996 989
		mu 0 4 461 655 534 463
		f 4 -1008 1049 -1296 1002
		mu 0 4 465 486 484 466
		f 4 1295 1045 -1009 1006
		mu 0 4 466 484 483 468
		f 4 -1052 -1051 -1297 1058
		mu 0 4 493 539 657 491
		f 4 1296 -1054 -1053 1054
		mu 0 4 491 657 621 488
		f 4 -974 1060 -1298 -973
		mu 0 4 458 492 490 658
		f 4 1297 1056 -976 -975
		mu 0 4 658 490 489 459
		f 4 -1063 -1062 -1299 1050
		mu 0 4 539 541 659 657
		f 4 1298 -1065 -1064 1053
		mu 0 4 657 659 620 621
		f 4 -1067 -1066 -1300 1061
		mu 0 4 541 543 660 659
		f 4 1299 -1069 -1068 1064
		mu 0 4 659 660 619 620
		f 4 -877 1068 -1301 -876
		mu 0 4 626 619 660 661
		f 4 1300 1065 -879 -878
		mu 0 4 661 660 543 431
		f 4 -998 1069 -1302 -997
		mu 0 4 469 616 662 663
		f 4 1301 1071 -1000 -999
		mu 0 4 663 662 545 544
		f 4 -1071 1073 -1303 -1070
		mu 0 4 616 617 664 662
		f 4 1302 1075 -1073 -1072
		mu 0 4 662 664 558 545
		f 4 -1075 1077 -1304 -1074
		mu 0 4 617 618 665 664
		f 4 1303 1079 -1077 -1076
		mu 0 4 664 665 557 558
		f 4 -1079 1081 -1305 -1078
		mu 0 4 618 494 497 665
		f 4 1304 1085 -1081 -1080
		mu 0 4 665 497 499 557
		f 4 -892 1087 -1306 -891
		mu 0 4 549 498 496 666
		f 4 1305 1083 -894 -893
		mu 0 4 666 496 495 632
		f 4 -1033 1088 -1307 -1032
		mu 0 4 471 500 503 667
		f 4 1306 1092 -1035 -1034
		mu 0 4 667 503 505 555
		f 4 -1097 -1096 -1308 1090
		mu 0 4 501 568 668 502
		f 4 1307 -1099 -1098 1094
		mu 0 4 502 668 564 504
		f 4 -1101 -1100 -1309 1095
		mu 0 4 568 566 669 668
		f 4 1308 -1103 -1102 1098
		mu 0 4 668 669 560 564
		f 4 -1105 -1104 -1310 1099
		mu 0 4 566 550 670 669
		f 4 1309 -1107 -1106 1102
		mu 0 4 669 670 561 560
		f 4 -954 1106 -1311 -953
		mu 0 4 631 561 670 671
		f 4 1310 1103 -956 -955
		mu 0 4 671 670 550 451
		f 4 -1022 1107 -1312 -1021
		mu 0 4 481 554 672 673
		f 4 1311 1109 -1024 -1023
		mu 0 4 673 672 548 547
		f 4 -1109 1111 -1313 -1108
		mu 0 4 554 577 674 672
		f 4 1312 1113 -1111 -1110
		mu 0 4 672 674 572 548
		f 4 -1113 1115 -1314 -1112
		mu 0 4 577 575 675 674
		f 4 1313 1117 -1115 -1114
		mu 0 4 674 675 571 572
		f 4 -1117 1119 -1315 -1116
		mu 0 4 575 506 509 675
		f 4 1314 1123 -1119 -1118
		mu 0 4 675 509 511 571
		f 4 -939 1125 -1316 -938
		mu 0 4 552 510 508 676
		f 4 1315 1121 -941 -940
		mu 0 4 676 508 507 627
		f 4 -1127 1128 -1317 -448
		mu 0 4 249 594 677 345
		f 4 1316 1130 -1128 -450
		mu 0 4 345 677 579 234
		f 4 -1130 1132 -1318 -1129
		mu 0 4 594 596 678 677
		f 4 1317 1134 -1132 -1131
		mu 0 4 677 678 581 579
		f 4 -1134 1136 -1319 -1133
		mu 0 4 596 598 679 678
		f 4 1318 1138 -1136 -1135
		mu 0 4 678 679 583 581
		f 4 -1138 1140 -1320 -1137
		mu 0 4 598 600 680 679
		f 4 1319 1142 -1140 -1139
		mu 0 4 679 680 584 583
		f 4 -1142 1144 -1321 -1141
		mu 0 4 600 602 874 680
		f 4 1320 1146 -1144 -1143
		mu 0 4 680 874 861 584
		f 4 -1146 1148 -1322 -1145
		mu 0 4 858 604 682 681
		f 4 1321 1150 -1148 -1147
		mu 0 4 681 682 586 585
		f 4 -1150 1152 -1323 -1149
		mu 0 4 604 606 683 682
		f 4 1322 1154 -1152 -1151
		mu 0 4 682 683 587 586
		f 4 -1154 1156 -1324 -1153
		mu 0 4 606 608 684 683
		f 4 1323 1158 -1156 -1155
		mu 0 4 683 684 589 587
		f 4 -1158 1160 -1325 -1157
		mu 0 4 608 610 685 684
		f 4 1324 1162 -1160 -1159
		mu 0 4 684 685 591 589
		f 4 -1162 487 -1326 -1161
		mu 0 4 610 269 355 685
		f 4 1325 488 -1164 -1163
		mu 0 4 685 355 248 591
		f 4 -1328 -1327 1262 1263
		mu 0 4 629 686 419 628
		f 4 1326 -1329 825 830
		mu 0 4 419 686 413 412
		f 4 1328 -1330 838 829
		mu 0 4 413 686 420 415
		f 4 1329 1327 1264 1260
		mu 0 4 420 686 629 625
		f 4 -1332 -1331 1267 1268
		mu 0 4 634 687 426 633
		f 4 1330 -1333 848 841
		mu 0 4 426 687 636 423
		f 4 1332 -1334 853 846
		mu 0 4 636 687 427 430
		f 4 1333 1331 1269 1265
		mu 0 4 427 687 634 630
		f 4 -1336 -1335 872 879
		mu 0 4 642 688 434 436
		f 4 1334 -1337 877 868
		mu 0 4 434 688 661 431
		f 4 1336 -1338 836 875
		mu 0 4 661 688 421 626
		f 4 1337 1335 881 840
		mu 0 4 421 688 642 422
		f 4 -1340 -1339 887 894
		mu 0 4 643 689 439 441
		f 4 1338 -1341 843 883
		mu 0 4 439 689 425 424
		f 4 1340 -1342 892 845
		mu 0 4 425 689 666 632
		f 4 1341 1339 896 890
		mu 0 4 666 689 643 549
		f 4 -1344 -1343 932 941
		mu 0 4 648 690 444 443
		f 4 1342 -1345 832 936
		mu 0 4 444 690 418 417
		f 4 1344 -1346 939 834
		mu 0 4 418 690 676 627
		f 4 1345 1343 943 937
		mu 0 4 676 690 648 552
		f 4 -1348 -1347 947 956
		mu 0 4 650 691 449 448
		f 4 1346 -1349 954 951
		mu 0 4 449 691 671 451
		f 4 1348 -1350 851 952
		mu 0 4 671 691 428 631
		f 4 1349 1347 958 855
		mu 0 4 428 691 650 429
		f 4 -1352 -1351 974 983
		mu 0 4 462 692 658 459
		f 4 1350 -1353 980 972
		mu 0 4 658 692 456 458
		f 4 1352 1351 987 976
		mu 0 4 456 692 462 453
		f 4 -1355 -1354 998 993
		mu 0 4 653 693 663 544
		f 4 1353 -1356 1004 996
		mu 0 4 663 693 467 469
		f 4 1355 1354 990 1000
		mu 0 4 467 693 653 464
		f 4 -1358 -1357 1022 1012
		mu 0 4 654 694 673 547
		f 4 1356 -1359 1028 1020
		mu 0 4 673 694 479 481
		f 4 1358 1357 1009 1024
		mu 0 4 479 694 654 476
		f 4 -1361 -1360 1033 1035
		mu 0 4 656 695 667 555
		f 4 1359 -1362 1015 1031
		mu 0 4 667 695 472 471
		f 4 1361 1360 1037 1019
		mu 0 4 472 695 656 474
		f 5 1266 893 1251 1362 -1269
		mu 0 5 633 632 495 562 634
		f 5 1261 940 -1201 1363 -1264
		mu 0 5 628 627 507 573 629
		f 20 1384 1385 1386 1387 1388 1389 1390 1391 1392 -1394 -1395 -1396 -1397 -1398 -1399
		 -1400 -1401 -1402 -1403 1403
		mu 0 20 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 711 712 713 714 715
		f 4 1406 1407 1408 1409
		mu 0 4 716 717 718 719
		f 4 1410 1411 1412 -1408
		mu 0 4 717 720 721 718
		f 4 -1410 1485 -1385 1486
		mu 0 4 716 719 697 696
		f 4 -1415 1487 -1386 -1486
		mu 0 4 719 722 698 697
		f 4 -1419 1488 -1387 -1488
		mu 0 4 722 723 699 698
		f 4 -1423 1489 -1388 -1489
		mu 0 4 723 724 700 699
		f 4 -1427 1490 -1389 -1490
		mu 0 4 724 725 701 700
		f 4 -1431 1491 -1390 -1491
		mu 0 4 725 726 702 701
		f 4 -1435 1492 -1391 -1492
		mu 0 4 726 727 703 702
		f 4 -1439 1493 -1392 -1493
		mu 0 4 727 728 704 703
		f 4 -1443 1494 -1393 -1494
		mu 0 4 728 729 705 704
		f 4 -1447 1495 1393 -1495
		mu 0 4 729 730 706 705
		f 4 -1451 1496 1394 -1496
		mu 0 4 730 731 707 706
		f 4 -1455 1497 1395 -1497
		mu 0 4 731 732 708 707
		f 4 -1459 1498 1396 -1498
		mu 0 4 732 733 709 708
		f 4 -1463 1499 1397 -1499
		mu 0 4 733 734 710 709
		f 4 -1467 1500 1398 -1500
		mu 0 4 734 735 711 710
		f 4 -1471 1501 1399 -1501
		mu 0 4 735 736 712 711
		f 4 -1475 1502 1400 -1502
		mu 0 4 736 737 713 712
		f 4 -1479 1503 1401 -1503
		mu 0 4 737 738 714 713
		f 4 -1483 1504 1402 -1504
		mu 0 4 738 739 715 714
		f 4 -1406 -1487 -1404 -1505
		mu 0 4 739 716 696 715
		f 4 -1409 1505 1413 1414
		mu 0 4 719 718 740 722
		f 4 -1413 1415 1416 -1506
		mu 0 4 718 721 741 740
		f 4 -1414 1506 1417 1418
		mu 0 4 722 740 742 723
		f 4 -1417 1419 1420 -1507
		mu 0 4 740 741 743 742
		f 4 -1418 1507 1421 1422
		mu 0 4 723 742 744 724
		f 4 -1421 1423 1424 -1508
		mu 0 4 742 743 745 744
		f 4 -1422 1508 1425 1426
		mu 0 4 724 744 746 725
		f 4 -1425 1427 1428 -1509
		mu 0 4 744 745 747 746
		f 4 -1426 1509 1429 1430
		mu 0 4 725 746 748 726
		f 4 -1429 1431 1432 -1510
		mu 0 4 746 747 749 748
		f 4 -1430 1510 1433 1434
		mu 0 4 726 748 750 727
		f 4 -1433 1435 1436 -1511
		mu 0 4 748 749 751 750
		f 4 -1434 1511 1437 1438
		mu 0 4 727 750 752 728
		f 4 -1437 1439 1440 -1512
		mu 0 4 750 751 753 752
		f 4 -1438 1512 1441 1442
		mu 0 4 728 752 754 729
		f 4 -1441 1443 1444 -1513
		mu 0 4 752 753 755 754
		f 4 -1442 1513 1445 1446
		mu 0 4 729 754 756 730
		f 4 -1445 1447 1448 -1514
		mu 0 4 754 755 757 756
		f 4 -1446 1514 1449 1450
		mu 0 4 730 756 758 731
		f 4 -1449 1451 1452 -1515
		mu 0 4 756 757 759 758
		f 4 -1450 1515 1453 1454
		mu 0 4 731 758 760 732
		f 4 -1453 1455 1456 -1516
		mu 0 4 758 759 761 760
		f 4 -1454 1516 1457 1458
		mu 0 4 732 760 762 733
		f 4 -1457 1459 1460 -1517
		mu 0 4 760 761 763 762
		f 4 -1458 1517 1461 1462
		mu 0 4 733 762 764 734
		f 4 -1461 1463 1464 -1518
		mu 0 4 762 763 765 764
		f 4 -1462 1518 1465 1466
		mu 0 4 734 764 766 735
		f 4 -1465 1467 1468 -1519
		mu 0 4 764 765 767 766
		f 4 -1466 1519 1469 1470
		mu 0 4 735 766 768 736
		f 4 -1469 1471 1472 -1520
		mu 0 4 766 767 769 768
		f 4 -1470 1520 1473 1474
		mu 0 4 736 768 770 737
		f 4 -1473 1475 1476 -1521
		mu 0 4 768 769 771 770
		f 4 -1474 1521 1477 1478
		mu 0 4 737 770 772 738
		f 4 -1477 1479 1480 -1522
		mu 0 4 770 771 773 772
		f 4 -1478 1522 1481 1482
		mu 0 4 738 772 774 739
		f 4 -1481 1483 1484 -1523
		mu 0 4 772 773 775 774
		f 4 -1411 1523 -1485 1404
		mu 0 4 720 717 774 775
		f 4 -1407 1405 -1482 -1524
		mu 0 4 717 716 739 774
		f 4 1364 1604 -1532 1605
		mu 0 4 776 777 778 779
		f 4 1365 1606 -1536 -1605
		mu 0 4 777 780 781 778
		f 4 1366 1607 -1540 -1607
		mu 0 4 780 782 783 781
		f 4 1367 1608 -1544 -1608
		mu 0 4 782 784 785 783
		f 4 1368 1609 -1548 -1609
		mu 0 4 784 786 787 785
		f 4 1369 1610 -1552 -1610
		mu 0 4 786 788 789 787
		f 4 1370 1611 -1556 -1611
		mu 0 4 788 790 791 789
		f 4 1371 1612 -1560 -1612
		mu 0 4 790 792 793 791
		f 4 1372 1613 -1564 -1613
		mu 0 4 792 794 795 793
		f 4 1373 1614 -1568 -1614
		mu 0 4 794 796 797 795
		f 4 -1375 -1606 -1526 1615
		mu 0 4 798 776 779 799
		f 4 -1376 -1616 -1574 1616
		mu 0 4 800 798 799 801
		f 4 -1377 -1617 -1578 1617
		mu 0 4 802 800 801 803
		f 4 -1378 -1618 -1582 1618
		mu 0 4 804 802 803 805
		f 4 -1379 -1619 -1586 1619
		mu 0 4 806 804 805 807
		f 4 -1380 -1620 -1590 1620
		mu 0 4 808 806 807 809
		f 4 -1381 -1621 -1594 1621
		mu 0 4 810 808 809 811
		f 4 -1382 -1622 -1598 1622
		mu 0 4 812 810 811 813
		f 4 -1383 -1623 -1602 1623
		mu 0 4 814 812 813 815
		f 4 -1384 -1624 -1572 -1615
		mu 0 4 796 814 815 797
		f 4 -1534 1624 -1412 1625
		mu 0 4 816 817 721 720
		f 4 -1538 1626 -1416 -1625
		mu 0 4 817 818 741 721
		f 4 -1542 1627 -1420 -1627
		mu 0 4 818 819 743 741
		f 4 -1546 1628 -1424 -1628
		mu 0 4 819 820 745 743
		f 4 -1550 1629 -1428 -1629
		mu 0 4 820 821 747 745
		f 4 -1554 1630 -1432 -1630
		mu 0 4 821 822 749 747
		f 4 -1558 1631 -1436 -1631
		mu 0 4 822 823 751 749
		f 4 -1562 1632 -1440 -1632
		mu 0 4 823 824 753 751
		f 4 -1566 1633 -1444 -1633
		mu 0 4 824 825 755 753
		f 4 -1570 1634 -1448 -1634
		mu 0 4 825 826 757 755
		f 4 -1603 1635 -1452 -1635
		mu 0 4 826 827 759 757
		f 4 -1599 1636 -1456 -1636
		mu 0 4 827 828 761 759
		f 4 -1595 1637 -1460 -1637
		mu 0 4 828 829 763 761
		f 4 -1591 1638 -1464 -1638
		mu 0 4 829 830 765 763
		f 4 -1587 1639 -1468 -1639
		mu 0 4 830 831 767 765
		f 4 -1583 1640 -1472 -1640
		mu 0 4 831 832 769 767
		f 4 -1579 1641 -1476 -1641
		mu 0 4 832 833 771 769
		f 4 -1575 1642 -1480 -1642
		mu 0 4 833 834 773 771
		f 4 -1527 1643 -1484 -1643
		mu 0 4 834 835 775 773
		f 4 -1530 -1626 -1405 -1644
		mu 0 4 835 816 720 775
		f 4 -1531 1644 1524 1525
		mu 0 4 779 836 837 799
		f 4 -1529 1526 1527 -1645
		mu 0 4 836 835 834 837
		f 4 1528 1645 -1533 1529
		mu 0 4 835 836 838 816
		f 4 1530 1531 -1535 -1646
		mu 0 4 836 779 778 838
		f 4 1532 1646 -1537 1533
		mu 0 4 816 838 839 817
		f 4 1534 1535 -1539 -1647
		mu 0 4 838 778 781 839
		f 4 1536 1647 -1541 1537
		mu 0 4 817 839 840 818
		f 4 1538 1539 -1543 -1648
		mu 0 4 839 781 783 840
		f 4 1540 1648 -1545 1541
		mu 0 4 818 840 841 819
		f 4 1542 1543 -1547 -1649
		mu 0 4 840 783 785 841
		f 4 1544 1649 -1549 1545
		mu 0 4 819 841 842 820
		f 4 1546 1547 -1551 -1650
		mu 0 4 841 785 787 842
		f 4 1548 1650 -1553 1549
		mu 0 4 820 842 843 821
		f 4 1550 1551 -1555 -1651
		mu 0 4 842 787 789 843
		f 4 1552 1651 -1557 1553
		mu 0 4 821 843 844 822
		f 4 1554 1555 -1559 -1652
		mu 0 4 843 789 791 844
		f 4 1556 1652 -1561 1557
		mu 0 4 822 844 845 823
		f 4 1558 1559 -1563 -1653
		mu 0 4 844 791 793 845
		f 4 1560 1653 -1565 1561
		mu 0 4 823 845 846 824
		f 4 1562 1563 -1567 -1654
		mu 0 4 845 793 795 846
		f 4 1564 1654 -1569 1565
		mu 0 4 824 846 847 825
		f 4 1566 1567 -1571 -1655
		mu 0 4 846 795 797 847
		f 4 -1525 1655 1572 1573
		mu 0 4 799 837 848 801
		f 4 -1528 1574 1575 -1656
		mu 0 4 837 834 833 848
		f 4 -1573 1656 1576 1577
		mu 0 4 801 848 849 803
		f 4 -1576 1578 1579 -1657
		mu 0 4 848 833 832 849
		f 4 -1577 1657 1580 1581
		mu 0 4 803 849 850 805
		f 4 -1580 1582 1583 -1658
		mu 0 4 849 832 831 850
		f 4 -1581 1658 1584 1585
		mu 0 4 805 850 851 807
		f 4 -1584 1586 1587 -1659
		mu 0 4 850 831 830 851
		f 4 -1585 1659 1588 1589
		mu 0 4 807 851 852 809
		f 4 -1588 1590 1591 -1660
		mu 0 4 851 830 829 852
		f 4 -1589 1660 1592 1593
		mu 0 4 809 852 853 811
		f 4 -1592 1594 1595 -1661
		mu 0 4 852 829 828 853
		f 4 -1593 1661 1596 1597
		mu 0 4 811 853 854 813
		f 4 -1596 1598 1599 -1662
		mu 0 4 853 828 827 854
		f 4 -1597 1662 1600 1601
		mu 0 4 813 854 855 815
		f 4 -1600 1602 1603 -1663
		mu 0 4 854 827 826 855
		f 4 1568 1663 -1604 1569
		mu 0 4 825 847 855 826
		f 4 1570 1571 -1601 -1664
		mu 0 4 847 797 815 855;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".db" yes;
	setAttr ".vs" 4;
	setAttr ".bw" 4;
	setAttr ".dr" 1;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode polySoftEdge -n "polySoftEdge81";
	rename -uid "AAABF76A-419C-2787-7E16-4882C6EFC389";
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
connectAttr "polySoftEdge81.out" "Special_AShape.i";
connectAttr "polySurfaceShape59.o" "polySoftEdge81.ip";
connectAttr "Special_AShape.wm" "polySoftEdge81.mp";
connectAttr "Special_AShape.iog" ":initialShadingGroup.dsm" -na;
// End of Special_A.ma
