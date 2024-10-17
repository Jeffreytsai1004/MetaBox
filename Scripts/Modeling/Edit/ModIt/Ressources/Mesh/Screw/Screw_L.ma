//Maya ASCII 2023 scene
//Name: Screw_L.ma
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
fileInfo "UUID" "7E26EA2B-4A2E-0C2C-5160-DFBC5BF18311";
createNode transform -n "Screw_L";
	rename -uid "FFB7F145-41FC-43E9-EE4B-0BB53244C93F";
	setAttr -s 2 ".rlio[0:1]" 12 yes 0 11 yes 0;
	setAttr ".sp" -type "double3" 0 -2.2204460492503131e-16 0 ;
createNode mesh -n "Screw_LShape" -p "Screw_L";
	rename -uid "65D7E0E3-489C-3735-EBED-11A121EB6051";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.14591420069336891 0.85955715179443359 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr ".ugsdt" no;
	setAttr -s 504 ".pt";
	setAttr ".pt[18]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[19]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[20]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[21]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[22]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[23]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[24]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[25]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[26]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[27]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[28]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[29]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[30]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[31]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[32]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[33]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[34]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[35]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[36]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[37]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[38]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[39]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[40]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[41]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[42]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[43]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[44]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[45]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[46]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[47]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[48]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[49]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[50]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[51]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[52]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[53]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[54]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[55]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[56]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[57]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[58]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[59]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[60]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[61]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[62]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[63]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[64]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[65]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[66]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[67]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[68]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[69]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[70]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[71]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[72]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[73]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[74]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[75]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[76]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[77]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[78]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[79]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[80]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[81]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[82]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[83]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[84]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[85]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[86]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[87]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[88]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[89]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[90]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[91]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[92]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[93]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[94]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[95]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[96]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[97]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[98]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[99]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[100]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[101]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[102]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[103]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[104]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[105]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[106]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[107]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[108]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[109]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[110]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[111]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[112]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[113]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[114]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[115]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[116]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[117]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[118]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[119]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[120]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[121]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[122]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[123]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[124]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[125]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[126]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[127]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[128]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[129]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[130]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[131]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[132]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[133]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[134]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[135]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[136]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[137]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[138]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[139]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[140]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[141]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[142]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[143]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[144]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[145]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[146]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[147]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[148]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[149]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[150]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[151]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[152]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[153]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[154]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[155]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[156]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[157]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[158]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[159]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[160]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[161]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[162]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[163]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[164]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[165]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[166]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[167]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[168]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[169]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[170]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[171]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[172]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[173]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[174]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[175]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[176]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[177]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[178]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[179]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[180]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[181]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[182]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[183]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[184]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[185]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[186]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[187]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[188]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[189]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[190]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[191]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[192]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[193]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[194]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[195]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[196]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[197]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[198]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[199]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[200]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[201]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[202]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[203]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[204]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[205]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[206]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[207]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[208]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[209]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[210]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[211]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[212]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[213]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[214]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[215]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[216]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[217]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[218]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[219]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[220]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[221]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[222]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[223]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[224]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[225]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[226]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[227]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[228]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[229]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[230]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[231]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[232]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[233]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[234]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[235]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[236]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[237]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[238]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[239]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[240]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[241]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[242]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[243]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[244]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[245]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[246]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[247]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[248]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[249]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[250]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[251]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[252]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[253]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[254]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[255]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[256]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[257]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[258]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[259]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[260]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[261]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[262]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[263]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[264]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[265]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[266]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[267]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[268]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[269]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[270]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[271]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[272]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[273]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[274]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[275]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[276]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[277]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[278]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[279]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[280]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[281]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[282]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[283]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[284]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[285]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[286]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[287]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[396]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[397]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[398]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[399]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[400]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[401]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[402]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[403]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[404]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[405]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[406]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[407]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[408]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[409]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[410]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[411]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[412]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[413]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[414]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[415]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[416]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[417]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[418]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[419]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[420]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[421]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[422]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[423]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[424]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[425]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[426]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[427]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[428]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[429]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[430]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[431]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[432]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[433]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[434]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[435]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[436]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[437]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[438]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[439]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[440]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[441]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[442]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[443]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[444]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[445]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[446]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[447]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[448]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[449]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[450]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[451]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[452]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[453]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[454]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[455]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[456]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[457]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[458]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[459]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[460]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[461]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[462]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[463]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[464]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[465]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[466]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[467]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[468]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[469]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[470]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[471]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[472]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[473]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[474]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[475]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[476]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[477]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[478]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[479]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[480]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[481]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[482]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[483]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[484]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[485]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[486]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[487]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[488]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[489]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[490]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[491]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[492]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[493]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[494]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[495]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[496]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[497]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[498]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[499]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[500]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[501]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[502]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[503]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[504]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[505]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[506]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[507]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[508]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[509]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[510]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[511]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[512]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[513]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[514]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[515]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[516]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[517]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[518]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[519]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[520]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[521]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[522]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[523]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[524]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[525]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[526]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[527]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[528]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[529]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[530]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[531]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[532]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[533]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[534]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[535]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[536]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[537]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[538]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[539]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[540]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[541]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[542]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[543]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[544]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[545]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[546]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[547]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[548]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[549]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[550]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[551]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[552]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[553]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[554]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[555]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[556]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[557]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[558]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[559]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[560]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[561]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[562]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[563]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[564]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[565]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[566]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[567]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[568]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[569]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[570]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[571]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[572]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[573]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[574]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[575]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[576]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[577]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[578]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[579]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[580]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[581]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[582]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[583]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[584]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[585]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[586]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[587]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[588]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[589]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[590]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[591]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[592]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[593]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[594]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[595]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[596]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[597]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[598]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[599]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[600]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[601]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[602]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[603]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[604]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[605]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[606]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[607]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[608]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[609]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[610]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[611]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[612]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[613]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[614]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[615]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[616]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[617]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[618]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[619]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[620]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[621]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[622]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[623]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[624]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[625]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[626]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[627]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[628]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[629]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".db" yes;
	setAttr ".vbc" no;
	setAttr ".vs" 8;
	setAttr ".usz" 8;
	setAttr ".bw" 4;
	setAttr ".dr" 1;
	setAttr ".vnm" 0;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "polySurfaceShape14" -p "Screw_L";
	rename -uid "66746DC2-4C4A-2164-3BB3-10A8B40BAE4F";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.095346860587596893 0.19485187530517578 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 109 ".uvst[0].uvsp[0:108]" -type "float2" 0.10112422 0.25575879
		 0.079898909 0.25417352 0.087556064 0.22404481 0.09809649 0.22469008 0.060734447 0.24558616
		 0.07699509 0.22161549 0.045521636 0.23098794 0.070518002 0.21282351 0.036228351 0.2115168
		 0.066047713 0.20322272 0.034326442 0.19049878 0.063222721 0.19268084 0.039568171
		 0.17008561 0.06802842 0.1829125 0.051691696 0.15242496 0.073944829 0.17411596 0.068805784
		 0.14014208 0.081415892 0.1662135 0.089092121 0.13429829 0.092278868 0.16501367 0.11061519
		 0.1359922 0.10280426 0.16595078 0.1298191 0.14486367 0.11337541 0.16878816 0.14501521
		 0.1596162 0.11982265 0.17764154 0.15439166 0.17938909 0.12440823 0.18723482 0.1562086
		 0.20001134 0.127471 0.19774014 0.15076882 0.22070843 0.1226398 0.20750104 0.13843112
		 0.238231 0.11658752 0.21615395 0.1212461 0.25017244 0.10890715 0.2238885 0.089796364
		 0.21432903 0.097454756 0.21502601 0.08274658 0.21333447 0.079188392 0.20692703 0.075778708
		 0.2001268 0.073122174 0.19340327 0.076751933 0.18721275 0.081236742 0.18091094 0.085919268
		 0.17525904 0.093025684 0.17545444 0.1006865 0.17590106 0.10787614 0.17662174 0.11147711
		 0.18309644 0.11470984 0.19004214 0.11695519 0.19687805 0.11342569 0.20298754 0.10911296
		 0.20928738 0.10476585 0.21488616 0.16585691 0.29661486 0.16413927 0.2771579 0.20404482
		 0.27363664 0.20569643 0.29301399 0.16757454 0.31607187 0.20739256 0.31234419 0.16929217
		 0.33552873 0.20917541 0.3315973 0.17100984 0.35498589 0.21140131 0.35089183 0.14181004
		 0.024216956 0.1400924 0.0047598593 0.18057644 0.0017144307 0.18176523 0.021100495
		 0.1435277 0.043674029 0.18338302 0.040368166 0.14524528 0.063130908 0.18509957 0.05969651
		 0.14696293 0.08258795 0.18686821 0.079063609 0.14868057 0.10204493 0.18864492 0.098484516
		 0.15039822 0.12150181 0.19039825 0.11793385 0.15211584 0.14095888 0.1921379 0.13741049
		 0.15383348 0.16041598 0.19386387 0.15687403 0.19557825 0.17633939 0.19730058 0.19580409
		 0.15898637 0.21878697 0.19901113 0.21526891 0.160704 0.23824394 0.20071054 0.23474911
		 0.16242161 0.25770092 0.20239167 0.25420487 0.20995879 0.29264277 0.21163759 0.31196159
		 0.20667958 0.25383618 0.20832163 0.27327216 0.20500077 0.23437974 0.20330328 0.21489172
		 0.201592 0.195426 0.19986784 0.17596082 0.19815516 0.15649432 0.19642988 0.13703005
		 0.19468692 0.11754596 0.19293109 0.098096237 0.19114265 0.078673132 0.18936124 0.059315234
		 0.18762937 0.04000102 0.18596217 0.020818429 0.1848959 0.0021578544 0.21335678 0.33113971
		 0.21557638 0.34969869;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 90 ".vt[0:89]"  -28.52999496 1.56376135 -90.50305176 -28.82939911 1.56376135 -91.021652222
		 -29.11804962 1.56376135 -91.52753448 -29.70062256 1.56376135 -91.52456665 -30.29945755 1.56376135 -91.52456665
		 -30.88188934 1.56376135 -91.52753448 -31.17061996 1.56376135 -91.021514893 -31.47002411 1.56376135 -90.50291443
		 -31.76381302 1.56376135 -90 -31.469944 1.56376135 -89.49694824 -31.17053986 1.56376135 -88.97834778
		 -30.88188934 1.56376135 -88.47245789 -30.29930115 1.56376135 -88.47543335 -29.70048141 1.56376135 -88.47543335
		 -29.11804962 1.56376135 -88.47245789 -28.829319 1.56376135 -88.97848511 -28.52991486 1.56376135 -89.49708557
		 -28.23611832 1.56376135 -90 -28.47135925 2.79976988 -90.53049469 -28.77623749 2.79976988 -91.058570862
		 -29.083366394 2.79976988 -91.58760071 -29.6950798 2.79976988 -91.58906555 -30.30485153 2.79976988 -91.58906555
		 -30.91657257 2.79976988 -91.58760071 -31.22370148 2.79976988 -91.058563232 -31.52857208 2.79976988 -90.53049469
		 -31.83317566 2.79976988 -90 -31.52857971 2.79976988 -89.46950531 -31.22370148 2.79976988 -88.94143677
		 -30.91657257 2.79976988 -88.41239166 -30.30485153 2.79976988 -88.41093445 -29.69508743 2.79976988 -88.41093445
		 -29.083366394 2.79976988 -88.41239166 -28.77623749 2.79976988 -88.94143677 -28.47135925 2.79976988 -89.46950531
		 -28.16675568 2.79976988 -90 -26.49933624 2.78094888 -91.27349854 -27.14677429 2.78094888 -92.3948822
		 -28.13742447 2.78094888 -93.22601318 -29.35253143 2.78094888 -93.66838074 -30.6473999 2.78094888 -93.66838074
		 -31.8625145 2.78094888 -93.22601318 -32.85316849 2.78094888 -92.3948822 -33.50060272 2.78094888 -91.27349854
		 -33.72504425 2.78094888 -90 -33.50060272 2.78094888 -88.72650146 -32.85316849 2.78094888 -87.6051178
		 -31.8625145 2.78094888 -86.77398682 -30.6473999 2.78094888 -86.33161926 -29.35253906 2.78094888 -86.33161926
		 -28.13742447 2.78094888 -86.77398682 -27.14677429 2.78094888 -87.6051178 -26.49933624 2.78094888 -88.72650146
		 -26.27489471 2.78094888 -90 -26.49954605 0.052473545 -91.27404785 -27.14638519 0.052473545 -92.39443207
		 -28.13742447 0.052473545 -93.22601318 -29.35310745 0.052473545 -93.66848755 -30.64682388 0.052473545 -93.66848755
		 -31.8625145 0.052473545 -93.22601318 -32.85354614 0.052473545 -92.39443207 -33.50039291 0.052473545 -91.27404785
		 -33.72504425 0.052473545 -90 -33.50039291 0.052473545 -88.72595215 -32.85354614 0.052473545 -87.6055603
		 -31.8625145 0.052473545 -86.77398682 -30.64682388 0.052473545 -86.33151245 -29.35311508 0.052473545 -86.33151245
		 -28.13742447 0.052473545 -86.77398682 -27.14638519 0.052473545 -87.6055603 -26.49954605 0.052473545 -88.72595215
		 -26.27489471 0.052473545 -90 -26.74224854 7.1525574e-07 -91.18571472 -26.53318024 7.1525574e-07 -90
		 -26.74224854 7.1525574e-07 -88.81428528 -27.34423828 7.1525574e-07 -87.77158356 -28.26656342 7.1525574e-07 -86.99766541
		 -29.39795685 7.1525574e-07 -86.58586884 -30.60198212 7.1525574e-07 -86.58586884 -31.73336792 7.1525574e-07 -86.99766541
		 -32.65568542 7.1525574e-07 -87.77158356 -33.25769043 7.1525574e-07 -88.81428528 -33.46676636 7.1525574e-07 -90
		 -33.2576828 7.1525574e-07 -91.18571472 -32.65568542 7.1525574e-07 -92.22841644 -31.73336792 7.1525574e-07 -93.0023345947
		 -30.60197449 7.1525574e-07 -93.41412354 -29.39795685 7.1525574e-07 -93.41412354 -28.26656342 7.1525574e-07 -93.0023345947
		 -27.34423828 7.1525574e-07 -92.22841644;
	setAttr -s 162 ".ed[0:161]"  1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0 7 8 0
		 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 0 0 0 1 0
		 18 0 1 19 1 1 20 2 0 21 3 1 22 4 1 23 5 0 24 6 1 25 7 1 26 8 0 27 9 1 28 10 1 29 11 0
		 30 12 1 31 13 1 32 14 0 33 15 1 34 16 1 35 17 0 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0
		 23 24 0 24 25 0 25 26 0 26 27 0 27 28 0 28 29 0 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0
		 34 35 0 35 18 0 36 54 0 36 18 1 37 55 0 37 19 1 38 56 0 38 20 0 39 57 0 39 21 1 40 58 0
		 40 22 1 41 59 0 41 23 0 42 60 0 42 24 1 43 61 0 43 25 1 44 62 0 44 26 0 45 63 0 45 27 1
		 46 64 0 46 28 1 47 65 0 47 29 0 48 66 0 48 30 1 49 67 0 49 31 1 50 68 0 50 32 0 51 69 0
		 51 33 1 52 70 0 52 34 1 53 71 0 53 35 0 54 72 1 55 89 1 56 88 1 57 87 1 58 86 1 59 85 1
		 60 84 1 61 83 1 62 82 1 63 81 1 64 80 1 65 79 1 66 78 1 67 77 1 68 76 1 69 75 1 70 74 1
		 71 73 1 36 53 0 37 36 0 38 37 0 39 38 0 40 39 0 41 40 0 42 41 0 43 42 0 44 43 0 45 44 0
		 46 45 0 47 46 0 48 47 0 49 48 0 50 49 0 51 50 0 52 51 0 53 52 0 54 71 0 55 54 0 56 55 0
		 57 56 0 58 57 0 59 58 0 60 59 0 61 60 0 62 61 0 63 62 0 64 63 0 65 64 0 66 65 0 67 66 0
		 68 67 0 69 68 0 70 69 0 71 70 0 72 73 0 73 74 0 74 75 0 75 76 0 76 77 0 77 78 0 78 79 0
		 79 80 0 80 81 0 81 82 0 82 83 0 83 84 0 84 85 0 85 86 0 86 87 0 87 88 0 88 89 0 89 72 0;
	setAttr -s 73 -ch 306 ".fc[0:72]" -type "polyFaces" 
		f 4 -110 57 -37 -56
		mu 0 4 0 1 2 3
		f 4 -111 59 -38 -58
		mu 0 4 1 4 5 2
		f 4 -112 61 -39 -60
		mu 0 4 4 6 7 5
		f 4 -113 63 -40 -62
		mu 0 4 6 8 9 7
		f 4 -114 65 -41 -64
		mu 0 4 8 10 11 9
		f 4 -115 67 -42 -66
		mu 0 4 10 12 13 11
		f 4 -116 69 -43 -68
		mu 0 4 12 14 15 13
		f 4 -117 71 -44 -70
		mu 0 4 14 16 17 15
		f 4 -118 73 -45 -72
		mu 0 4 16 18 19 17
		f 4 -119 75 -46 -74
		mu 0 4 18 20 21 19
		f 4 -120 77 -47 -76
		mu 0 4 20 22 23 21
		f 4 -121 79 -48 -78
		mu 0 4 22 24 25 23
		f 4 -122 81 -49 -80
		mu 0 4 24 26 27 25
		f 4 -123 83 -50 -82
		mu 0 4 26 28 29 27
		f 4 -124 85 -51 -84
		mu 0 4 28 30 31 29
		f 4 -125 87 -52 -86
		mu 0 4 30 32 33 31
		f 4 -126 89 -53 -88
		mu 0 4 32 34 35 33
		f 4 -109 55 -54 -90
		mu 0 4 34 0 3 35
		f 4 36 19 -18 -19
		mu 0 4 3 2 36 37
		f 4 37 20 -1 -20
		mu 0 4 2 5 38 36
		f 4 38 21 -2 -21
		mu 0 4 5 7 39 38
		f 4 39 22 -3 -22
		mu 0 4 7 9 40 39
		f 4 40 23 -4 -23
		mu 0 4 9 11 41 40
		f 4 41 24 -5 -24
		mu 0 4 11 13 42 41
		f 4 42 25 -6 -25
		mu 0 4 13 15 43 42
		f 4 43 26 -7 -26
		mu 0 4 15 17 44 43
		f 4 44 27 -8 -27
		mu 0 4 17 19 45 44
		f 4 45 28 -9 -28
		mu 0 4 19 21 46 45
		f 4 46 29 -10 -29
		mu 0 4 21 23 47 46
		f 4 47 30 -11 -30
		mu 0 4 23 25 48 47
		f 4 48 31 -12 -31
		mu 0 4 25 27 49 48
		f 4 49 32 -13 -32
		mu 0 4 27 29 50 49
		f 4 50 33 -14 -33
		mu 0 4 29 31 51 50
		f 4 51 34 -15 -34
		mu 0 4 31 33 52 51
		f 4 52 35 -16 -35
		mu 0 4 33 35 53 52
		f 4 53 18 -17 -36
		mu 0 4 35 3 37 53
		f 4 109 54 -128 -57
		mu 0 4 54 55 56 57
		f 4 110 56 -129 -59
		mu 0 4 58 54 57 59
		f 4 111 58 -130 -61
		mu 0 4 60 58 59 61
		f 4 112 60 -131 -63
		mu 0 4 62 60 61 63
		f 4 113 62 -132 -65
		mu 0 4 64 65 66 67
		f 4 114 64 -133 -67
		mu 0 4 68 64 67 69
		f 4 115 66 -134 -69
		mu 0 4 70 68 69 71
		f 4 116 68 -135 -71
		mu 0 4 72 70 71 73
		f 4 117 70 -136 -73
		mu 0 4 74 72 73 75
		f 4 118 72 -137 -75
		mu 0 4 76 74 75 77
		f 4 119 74 -138 -77
		mu 0 4 78 76 77 79
		f 4 120 76 -139 -79
		mu 0 4 80 78 79 81
		f 4 121 78 -140 -81
		mu 0 4 26 80 81 82
		f 4 122 80 -141 -83
		mu 0 4 28 26 82 83
		f 4 123 82 -142 -85
		mu 0 4 84 28 83 85
		f 4 124 84 -143 -87
		mu 0 4 86 84 85 87
		f 4 125 86 -144 -89
		mu 0 4 88 86 87 89
		f 4 108 88 -127 -55
		mu 0 4 55 88 89 56
		f 18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		mu 0 18 36 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 37
		f 4 126 107 -145 -91
		mu 0 4 56 89 92 93
		f 4 143 106 -146 -108
		mu 0 4 89 87 94 92
		f 4 142 105 -147 -107
		mu 0 4 87 85 95 94
		f 4 141 104 -148 -106
		mu 0 4 85 83 96 95
		f 4 140 103 -149 -105
		mu 0 4 83 82 97 96
		f 4 139 102 -150 -104
		mu 0 4 82 81 98 97
		f 4 138 101 -151 -103
		mu 0 4 81 79 99 98
		f 4 137 100 -152 -102
		mu 0 4 79 77 100 99
		f 4 136 99 -153 -101
		mu 0 4 77 75 101 100
		f 4 135 98 -154 -100
		mu 0 4 75 73 102 101
		f 4 134 97 -155 -99
		mu 0 4 73 71 103 102
		f 4 133 96 -156 -98
		mu 0 4 71 69 104 103
		f 4 132 95 -157 -97
		mu 0 4 69 67 105 104
		f 4 131 94 -158 -96
		mu 0 4 67 66 106 105
		f 4 130 93 -159 -95
		mu 0 4 63 61 107 108
		f 4 129 92 -160 -94
		mu 0 4 61 59 91 107
		f 4 128 91 -161 -93
		mu 0 4 59 57 90 91
		f 4 127 90 -162 -92
		mu 0 4 57 56 93 90;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".db" yes;
	setAttr ".vbc" no;
	setAttr ".vs" 8;
	setAttr ".usz" 8;
	setAttr ".bw" 4;
	setAttr ".vnm" 0;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "polySurfaceShape26" -p "Screw_L";
	rename -uid "753908E6-4128-B005-02B7-21B28670839F";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.14591420069336891 0.85955715179443359 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 646 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0.1377916 0.83713156 0.13875473
		 0.83753544 0.13890198 0.83856463 0.13906741 0.83981401 0.13919902 0.84084958 0.13838086
		 0.841492 0.1373817 0.84225851 0.13655061 0.8428914 0.13558483 0.8425048 0.13442102
		 0.84202141 0.13345739 0.8416186 0.13330978 0.84058946 0.13314593 0.8393392 0.13301346
		 0.83830363 0.13383126 0.83766198 0.13483152 0.83689421 0.1356627 0.83626229 0.13662738
		 0.83665007 0.13888136 0.8353979 0.13871637 0.83575052 0.13694507 0.83497888 0.13707981
		 0.83459479 0.14050692 0.83800393 0.1409066 0.83792847 0.14111322 0.83988899 0.14072543
		 0.83992285 0.13967076 0.84260064 0.13993648 0.84290892 0.13834098 0.84406853 0.13811752
		 0.84374958 0.13526922 0.84417552 0.13513491 0.84455967 0.13333231 0.84375733 0.13349694
		 0.84340435 0.13170424 0.8411507 0.13130423 0.84122634 0.13109824 0.83926409 0.1314863
		 0.83923036 0.13254255 0.83655149 0.13227713 0.83624285 0.13387382 0.83508372 0.13409689
		 0.83540291 0.13782966 0.83157879 0.13789988 0.8311941 0.14069796 0.83230025 0.14048463
		 0.83261591 0.14389062 0.83706933 0.14425766 0.8369385 0.14470303 0.83990461 0.14432317
		 0.83987981 0.1421794 0.84506017 0.14247847 0.8453123 0.14012465 0.84718627 0.13995636
		 0.84684438 0.13438997 0.84757739 0.13432044 0.84796232 0.13152075 0.84686011 0.13173321
		 0.84654349 0.12831718 0.842089 0.12794888 0.8422212 0.12750497 0.83924574 0.12788537
		 0.83927149 0.13003743 0.83408684 0.12973899 0.83383387 0.13209501 0.83196265 0.13226262
		 0.83230501 0.13777032 0.83183557 0.14035335 0.83283395 0.1389986 0.83515662 0.13717061
		 0.83432817 0.14363939 0.83714598 0.1440689 0.83987623 0.14138082 0.83986956 0.14118266
		 0.83787376 0.14198601 0.84488124 0.13983226 0.84662217 0.13849187 0.84429049 0.14012232
		 0.84312052 0.13444874 0.8473205 0.13186398 0.84632498 0.13321534 0.84399897 0.1350444
		 0.84482628 0.12856916 0.84201163 0.12814003 0.83927554 0.13083044 0.83928359 0.13102797
		 0.84128124 0.13023043 0.83426642 0.13238627 0.83252758 0.13372317 0.83486158 0.13209155
		 0.83603102 0.1394996 0.82381046 0.13934487 0.82452649 0.13400707 0.82434589 0.13390768
		 0.82361954 0.14470744 0.82594389 0.14431602 0.8265633 0.12892056 0.82596546 0.12857893
		 0.8253172 0.14884728 0.82972986 0.14826584 0.83017749 0.15146065 0.83476001 0.15075958
		 0.83494788 0.15219474 0.84004682 0.15146327 0.84005487 0.15104389 0.84559721 0.1503641
		 0.84532315 0.14809144 0.85036808 0.14754772 0.8498773 0.14365029 0.85382473 0.14330813
		 0.85317677 0.13832313 0.85553151 0.13822311 0.85480529 0.13273343 0.85535067 0.13288727
		 0.8546344 0.12752756 0.85323071 0.12791792 0.85261053 0.12339056 0.84947032 0.12396965
		 0.84902066 0.1207555 0.84453911 0.12145276 0.8443144 0.11999089 0.83897108 0.1207232
		 0.83899921 0.12118123 0.83350879 0.12186012 0.83378547 0.12413654 0.82876199 0.12467972
		 0.82925355 0.16890627 0.82092744 0.16925031 0.82157987 0.16537321 0.82459694 0.16482663
		 0.82410169 0.17382467 0.81934017 0.17392492 0.82007092 0.17898917 0.8195309 0.17883348
		 0.82025188 0.16276109 0.82875991 0.16207796 0.82848179 0.16173613 0.83357602 0.16099977
		 0.83355528 0.16240102 0.83840019 0.16169739 0.83861822 0.16469735 0.84275603 0.16411412
		 0.84320778 0.16834205 0.84605366 0.1679489 0.84667784 0.17289317 0.84790438 0.17273736
		 0.84862536 0.17780221 0.84808689 0.17790228 0.84881771 0.18247741 0.84657943 0.18282139
		 0.84723198 0.18635511 0.84356391 0.18690163 0.84405929 0.18896699 0.83940417 0.18964994
		 0.83968288 0.18999839 0.83460182 0.19073552 0.83463019 0.18932492 0.82973629 0.19002718
		 0.82951063 0.18702781 0.82539469 0.18761057 0.82494253 0.18338424 0.82210082 0.18377727
		 0.82147664 0.15042335 0.82461232 0.14972121 0.81954092 0.15112293 0.82966775 0.15178567
		 0.83467525 0.15253234 0.84004027 0.15323925 0.84504169 0.15394145 0.85009676 0.15464336
		 0.85516816 0.15534395 0.86023551 0.15604538 0.86530316 0.15674722 0.87037718 0.15744781
		 0.87544507 0.1581493 0.88051289 0.15885109 0.88558692 0.15955168 0.89065486 0.16025311
		 0.89572269 0.16095495 0.90079671 0.16165555 0.90586466 0.16940975 0.82188147 0.17397165
		 0.82040888 0.17423803 0.82233196 0.17031783 0.82359737 0.1787619 0.82058537 0.17835444
		 0.8224836 0.1832028 0.82238966 0.18217069 0.82403404 0.18675852 0.82560408 0.18522626
		 0.82679623 0.18900025 0.82984102 0.18715262 0.83043712 0.18965751 0.83458912 0.18771744
		 0.83451736 0.18865097 0.83927566 0.18685246 0.83854455 0.18610215 0.84333509 0.18466216
		 0.84203297 0.18231797 0.84627789 0.18141025 0.84456176 0.17775548 0.84774894 0.1774894
		 0.84582585 0.17296481 0.84757096 0.17337251 0.84567279 0.16852355 0.84576494 0.1695562
		 0.84412104 0.16496688 0.84254682 0.16650087 0.84135687 0.16272616 0.83829862 0.16457641
		 0.83771533 0.16207659 0.83358556 0.16401297 0.83364421 0.16307724 0.82888812 0.16487712
		 0.82961673 0.16562623 0.8248257 0.16706675 0.82612741 0.13927341 0.82485825 0.144135
		 0.82685059 0.14799631 0.83038503 0.15043497 0.83503741 0.15112478 0.84005708 0.15004849
		 0.84519643 0.14729565 0.84965014 0.14314908 0.8528766 0.13817641 0.8544687 0.13295835
		 0.85430253 0.12809843 0.85232276 0.12423787 0.84881204 0.12177575 0.84421009 0.12106264
		 0.83901173 0.12217496 0.83391351 0.12493155 0.82948112 0.12907934 0.82626575 0.13405344
		 0.82468253 0.13857716 0.83598739 0.13952118 0.8364194 0.13985869 0.83668202 0.14023319
		 0.83808202 0.14045066 0.83992106 0.14054936 0.84095401 0.14049092 0.84137768 0.13946593
		 0.84240276 0.13798147 0.84351069 0.13713565 0.84411305 0.13673931 0.84427428 0.13533828
		 0.84389931 0.13363594 0.84316713 0.13269129 0.84273571 0.13235348 0.84247309 0.13197809
		 0.8410725;
	setAttr ".uvst[0].uvsp[250:499]" 0.13176125 0.83923215 0.13166282 0.83819848
		 0.1317215 0.83777469 0.13274723 0.83674961 0.13423267 0.83564192 0.13507894 0.83504015
		 0.13547537 0.8348791 0.13687572 0.83525509 0.13865292 0.83587247 0.13690364 0.83511525
		 0.13893965 0.83527678 0.13712552 0.83446151 0.14104477 0.83790141 0.1412473 0.83987874
		 0.14036822 0.83803624 0.1405881 0.83992893 0.14002922 0.84301502 0.13841704 0.84417945
		 0.13957328 0.84249669 0.1380434 0.84363371 0.13508931 0.84469301 0.13327414 0.84387869
		 0.1353105 0.84403914 0.1335603 0.84328228 0.13116595 0.84125346 0.13096404 0.83927441
		 0.13184303 0.8411184 0.13162374 0.83922416 0.13218451 0.8361367 0.13379788 0.83497268
		 0.13264 0.83665556 0.13417086 0.83551884 0.13792384 0.83105713 0.14077532 0.83218747
		 0.13794467 0.83091813 0.14085659 0.83207506 0.13780454 0.83170885 0.14041439 0.8327232
		 0.14438784 0.83689106 0.14483929 0.83991438 0.1445182 0.83683997 0.14497721 0.83992773
		 0.14376581 0.83711237 0.14419526 0.83987314 0.14258552 0.84540099 0.14018413 0.84730935
		 0.1426959 0.84548813 0.14024144 0.84743571 0.142079 0.84497386 0.13989809 0.84673017
		 0.13429683 0.84809941 0.13144371 0.84697312 0.13427621 0.84823853 0.13136277 0.84708589
		 0.13441482 0.84744734 0.13180321 0.84643596 0.12781832 0.84226918 0.12736854 0.83923542
		 0.12768748 0.84232086 0.12723041 0.83922166 0.12844232 0.84204549 0.12801349 0.8392784
		 0.12963217 0.83374482 0.13203576 0.83183938 0.12952206 0.83365732 0.13197872 0.83171278
		 0.13013765 0.8341735 0.13232064 0.8324194 0.13930914 0.82469225 0.13403022 0.82451409
		 0.12899986 0.82611555 0.13953525 0.82364434 0.1447981 0.82580024 0.13388455 0.82345122
		 0.14898181 0.8296259 0.14422554 0.82670683 0.12480552 0.82936722 0.12849969 0.82516694
		 0.15162367 0.83471733 0.14813119 0.8302812 0.15236408 0.8400436 0.15059733 0.83499247
		 0.15120149 0.84566087 0.15129411 0.84005612 0.14821768 0.85048181 0.15020645 0.84525985
		 0.14372963 0.85397494 0.14742178 0.84976381 0.13834643 0.85569984 0.14322871 0.85302681
		 0.13269791 0.85551673 0.13819978 0.85463709 0.12743708 0.85337448 0.1329228 0.85446852
		 0.12325645 0.84957463 0.12800816 0.85246676 0.12059388 0.84459144 0.12410364 0.84891647
		 0.11982117 0.83896464 0.12161417 0.8442623 0.12102387 0.83344471 0.1208928 0.83900541
		 0.12401045 0.82864815 0.12201739 0.83384949 0.16932988 0.82173055 0.16549957 0.8247112
		 0.16291893 0.82882398 0.16882706 0.82077748 0.17380148 0.81917214 0.15857261 0.81831998
		 0.15787166 0.81324983 0.16470087 0.8239879 0.15927279 0.82339221 0.17902482 0.81936508
		 0.16980648 0.89957047 0.17394823 0.82023972 0.18386751 0.82133299 0.16910511 0.8945002
		 0.17879772 0.82041842 0.16190606 0.83358079 0.16192085 0.82841796 0.15997016 0.82846779
		 0.16256332 0.83834952 0.16083056 0.83355087 0.16066241 0.83354658 0.16483194 0.84265155
		 0.16153556 0.83866817 0.16137481 0.83871788 0.16843271 0.84590948 0.16398013 0.84331185
		 0.16208506 0.84379429 0.17292893 0.84773791 0.1678586 0.84682137 0.16279173 0.84886855
		 0.1777789 0.84791815 0.17270172 0.84879118 0.16349453 0.85394055 0.18239784 0.84642881
		 0.17792547 0.84898573 0.16419607 0.8590107 0.18622881 0.84344965 0.18290061 0.84738201
		 0.16489738 0.86408055 0.18880916 0.83934003 0.18702739 0.84417313 0.16559875 0.86915094
		 0.18982822 0.8345955 0.189807 0.83974677 0.1663 0.87422061 0.18916285 0.82978857
		 0.19090497 0.83463657 0.16700125 0.8792904 0.18689328 0.82549924 0.19018859 0.82945865
		 0.16770262 0.88436067 0.18329358 0.82224506 0.1877445 0.82483846 0.16840386 0.88943046
		 0.13546667 0.83032334 0.13482293 0.83028239 0.1342133 0.83049196 0.12776875 0.83550662
		 0.12741175 0.83604378 0.12728882 0.83667642 0.12841344 0.84476346 0.12870032 0.84534091
		 0.12918699 0.8457635 0.13675532 0.84882993 0.13739908 0.84886998 0.13800845 0.84865946
		 0.14444679 0.84363657 0.14480287 0.84309894 0.14492375 0.84246701 0.14379996 0.83440179
		 0.14351553 0.83382434 0.14302981 0.83340079 0.14071527 0.83653837 0.14051214 0.83616811
		 0.1406109 0.83608967 0.14083344 0.83647317 0.14019668 0.83588773 0.14028662 0.83578759
		 0.14015347 0.83697063 0.13997608 0.83659035 0.1400896 0.83650142 0.14027083 0.83687967
		 0.13964483 0.83633071 0.1397616 0.8362394 0.13506398 0.83488864 0.13545462 0.83473164
		 0.1358729 0.83476812 0.13589954 0.83491832 0.14104462 0.8420468 0.1412634 0.84168547
		 0.14138079 0.84173161 0.14116037 0.84211642 0.14134797 0.84127206 0.14147967 0.84129971
		 0.14038867 0.84177727 0.14062911 0.84143329 0.14076298 0.84148699 0.14052635 0.84183317
		 0.14068806 0.84101659 0.14082557 0.8410719 0.13643622 0.84508842 0.13685876 0.84509724
		 0.13687751 0.84522194 0.13643375 0.84522337 0.13725945 0.84496385 0.13730136 0.84509176
		 0.13634181 0.84438556 0.13676021 0.8444218 0.13678062 0.8445645 0.13636217 0.84453267
		 0.13715076 0.84426445 0.13717166 0.84441119 0.13149661 0.84261757 0.13170019 0.8429879
		 0.13160148 0.84306651 0.13137841 0.8426829 0.13201603 0.84326822 0.13192618 0.84336847
		 0.13205841 0.84218448 0.13223612 0.842565 0.13212264 0.84265399 0.13194105 0.84227568
		 0.1325677 0.84282452 0.13245097 0.84291595 0.13116816 0.83710474 0.13094911 0.83746618
		 0.13083169 0.83741993 0.13105249 0.837035 0.13086414 0.83787972 0.13073242 0.83785206
		 0.13182405 0.83737487 0.13158333 0.8377189 0.13144943 0.83766514 0.13168642 0.83731884
		 0.13152415 0.83813578 0.13138661 0.83808047 0.13577923 0.83406514 0.13535672 0.83405602
		 0.13533813 0.83393127 0.13578182 0.83393008 0.13495603 0.83418918 0.13491422 0.83406121
		 0.14367169 0.83452898 0.14336523 0.83394009 0.14287481 0.83349228 0.13428998 0.83147848;
	setAttr ".uvst[0].uvsp[500:645]" 0.13496515 0.83131725 0.13498712 0.83147842
		 0.13433471 0.83162129 0.13565931 0.83129805 0.13565433 0.83144778 0.13421547 0.83067185
		 0.1348488 0.83047026 0.13487348 0.83064973 0.1342271 0.83084434 0.13551337 0.8304981
		 0.13554886 0.83066803 0.14305136 0.83505279 0.14268863 0.83446199 0.14282355 0.83435804
		 0.14317515 0.83495301 0.14221224 0.83395833 0.14234009 0.83386427 0.14427173 0.84359044
		 0.14462668 0.84302837 0.14476657 0.84237987 0.14350426 0.84332007 0.1438334 0.84270954
		 0.14399153 0.84277326 0.14365321 0.84337658 0.14402986 0.84204501 0.14417553 0.84210759
		 0.13670829 0.84865528 0.13737291 0.84868211 0.13800594 0.84847957 0.13656077 0.84785539
		 0.13725498 0.84783536 0.13727838 0.84800416 0.13658598 0.84801263 0.13792995 0.84767324
		 0.13794813 0.84783083 0.12854135 0.84463543 0.12885007 0.84522432 0.12934166 0.84567136
		 0.12916082 0.84410793 0.12952504 0.8446992 0.12939039 0.84480375 0.1290372 0.84420842
		 0.13000265 0.84520274 0.12987512 0.84529728 0.12794355 0.83555347 0.12758753 0.83611518
		 0.12744585 0.8367644 0.12870994 0.83582652 0.12837976 0.8364374 0.12822187 0.83637303
		 0.1285612 0.83576959 0.12818214 0.83710271 0.12803659 0.83703941 0.1400882 0.83597928
		 0.14060104 0.83662307 0.14121431 0.84122413 0.14091402 0.84199041 0.13723415 0.84482414
		 0.1364198 0.84494704 0.13212445 0.84317642 0.13161084 0.84253269 0.13099784 0.83792788
		 0.13129872 0.83716124 0.13498116 0.83432895 0.13504323 0.83474189 0.13585269 0.83462089
		 0.1357955 0.8342064 0.13563439 0.83114082 0.14273095 0.83358818 0.14354211 0.83464408
		 0.14461118 0.84230465 0.14410639 0.84353691 0.13799402 0.84830719 0.13667241 0.84848535
		 0.12948516 0.84557492 0.12867069 0.84451944 0.12760112 0.83684045 0.12810859 0.83560759
		 0.1342721 0.83132082 0.14211068 0.83406812 0.14291927 0.83512288 0.14388371 0.84201294
		 0.1433768 0.84324151 0.13788494 0.84753054 0.13656548 0.84770578 0.13010389 0.84509248
		 0.12929288 0.84403723 0.12832826 0.83713526 0.12883714 0.83590561 0.14003676 0.8370688
		 0.14024523 0.84172541 0.13631502 0.84423536 0.13217509 0.84208626 0.13196746 0.83742684
		 0.14040661 0.83625168 0.13543433 0.83458883 0.14113811 0.84163606 0.13683897 0.84496397
		 0.13180572 0.84290415 0.13107437 0.83751565 0.13537642 0.83418924 0.1432218 0.83405066
		 0.13494205 0.83114845 0.14255989 0.83456117 0.14445853 0.84296089 0.1436826 0.84264868
		 0.13734791 0.8485027 0.13723272 0.84767431 0.12899303 0.8451131 0.12965351 0.84459943
		 0.1277554 0.83618337 0.12853038 0.8364988 0.13386157 0.82328409 0.14901978 0.81447357
		 0.17377847 0.81900531 0.17050773 0.9046402 0.18395722 0.82119042 0.18787754 0.82473511
		 0.19034892 0.82940692 0.1910733 0.83464295 0.18996304 0.83981031 0.18715233 0.84428614
		 0.18297923 0.8475309 0.17794847 0.84915262 0.17266625 0.84895593 0.1677689 0.84696394
		 0.16384709 0.8434152 0.1617648 0.82835448 0.17906022 0.81920034 0.16457587 0.82387489
		 0.16874838 0.82062846 0.12086759 0.83338112 0.12388525 0.82853502 0.11965258 0.8389582
		 0.12043337 0.84464341 0.12312321 0.84967822 0.12734726 0.85351729 0.13266265 0.85568172
		 0.13836953 0.85586697 0.14380842 0.85412413 0.14834297 0.85059482 0.15135789 0.84572411
		 0.14911538 0.82952279 0.12842101 0.82501769 0.14488816 0.82565761 0.13957074 0.82347947;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 504 ".pt";
	setAttr ".pt[18]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[19]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[20]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[21]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[22]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[23]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[24]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[25]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[26]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[27]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[28]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[29]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[30]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[31]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[32]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[33]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[34]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[35]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[36]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[37]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[38]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[39]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[40]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[41]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[42]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[43]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[44]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[45]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[46]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[47]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[48]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[49]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[50]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[51]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[52]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[53]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[54]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[55]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[56]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[57]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[58]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[59]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[60]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[61]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[62]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[63]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[64]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[65]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[66]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[67]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[68]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[69]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[70]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[71]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[72]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[73]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[74]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[75]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[76]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[77]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[78]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[79]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[80]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[81]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[82]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[83]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[84]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[85]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[86]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[87]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[88]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[89]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[90]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[91]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[92]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[93]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[94]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[95]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[96]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[97]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[98]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[99]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[100]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[101]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[102]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[103]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[104]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[105]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[106]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[107]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[108]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[109]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[110]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[111]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[112]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[113]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[114]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[115]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[116]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[117]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[118]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[119]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[120]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[121]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[122]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[123]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[124]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[125]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[126]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[127]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[128]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[129]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[130]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[131]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[132]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[133]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[134]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[135]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[136]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[137]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[138]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[139]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[140]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[141]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[142]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[143]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[144]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[145]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[146]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[147]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[148]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[149]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[150]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[151]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[152]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[153]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[154]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[155]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[156]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[157]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[158]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[159]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[160]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[161]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[162]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[163]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[164]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[165]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[166]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[167]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[168]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[169]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[170]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[171]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[172]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[173]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[174]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[175]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[176]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[177]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[178]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[179]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[180]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[181]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[182]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[183]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[184]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[185]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[186]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[187]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[188]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[189]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[190]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[191]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[192]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[193]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[194]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[195]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[196]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[197]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[198]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[199]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[200]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[201]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[202]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[203]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[204]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[205]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[206]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[207]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[208]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[209]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[210]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[211]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[212]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[213]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[214]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[215]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[216]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[217]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[218]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[219]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[220]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[221]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[222]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[223]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[224]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[225]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[226]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[227]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[228]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[229]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[230]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[231]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[232]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[233]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[234]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[235]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[236]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[237]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[238]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[239]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[240]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[241]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[242]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[243]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[244]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[245]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[246]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[247]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[248]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[249]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[250]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[251]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[252]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[253]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[254]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[255]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[256]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[257]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[258]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[259]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[260]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[261]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[262]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[263]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[264]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[265]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[266]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[267]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[268]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[269]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[270]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[271]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[272]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[273]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[274]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[275]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[276]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[277]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[278]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[279]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[280]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[281]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[282]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[283]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[284]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[285]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[286]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[287]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[396]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[397]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[398]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[399]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[400]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[401]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[402]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[403]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[404]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[405]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[406]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[407]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[408]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[409]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[410]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[411]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[412]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[413]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[414]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[415]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[416]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[417]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[418]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[419]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[420]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[421]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[422]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[423]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[424]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[425]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[426]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[427]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[428]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[429]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[430]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[431]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[432]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[433]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[434]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[435]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[436]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[437]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[438]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[439]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[440]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[441]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[442]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[443]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[444]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[445]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[446]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[447]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[448]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[449]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[450]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[451]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[452]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[453]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[454]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[455]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[456]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[457]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[458]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[459]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[460]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[461]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[462]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[463]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[464]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[465]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[466]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[467]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[468]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[469]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[470]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[471]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[472]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[473]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[474]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[475]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[476]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[477]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[478]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[479]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[480]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[481]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[482]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[483]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[484]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[485]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[486]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[487]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[488]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[489]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[490]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[491]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[492]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[493]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[494]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[495]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[496]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[497]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[498]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[499]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[500]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[501]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[502]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[503]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[504]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[505]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[506]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[507]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[508]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[509]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[510]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[511]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[512]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[513]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[514]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[515]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[516]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[517]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[518]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[519]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[520]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[521]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[522]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[523]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[524]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[525]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[526]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[527]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[528]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[529]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[530]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[531]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[532]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[533]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[534]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[535]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[536]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[537]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[538]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[539]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[540]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[541]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[542]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[543]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[544]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[545]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[546]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[547]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[548]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[549]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[550]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[551]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[552]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[553]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[554]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[555]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[556]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[557]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[558]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[559]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[560]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[561]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[562]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[563]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[564]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[565]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[566]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[567]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[568]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[569]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[570]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[571]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[572]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[573]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[574]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[575]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[576]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[577]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[578]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[579]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[580]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[581]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[582]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[583]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[584]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[585]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[586]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[587]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[588]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[589]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[590]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[591]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[592]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[593]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[594]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[595]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[596]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[597]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[598]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[599]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[600]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[601]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[602]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[603]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[604]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[605]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[606]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[607]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[608]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[609]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[610]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[611]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[612]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[613]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[614]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[615]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[616]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[617]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[618]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[619]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[620]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[621]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[622]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[623]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[624]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[625]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[626]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[627]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[628]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr ".pt[629]" -type "float3" 0 3.5762787e-07 0 ;
	setAttr -s 612 ".vt";
	setAttr ".vt[0:165]"  0.78528214 1.9917009e-07 -0.28581619 0.8356781 1.9917009e-07 0
		 0.78528214 1.9917009e-07 0.28581619 0.64017296 1.9917009e-07 0.53715897 0.41784477 1.9917009e-07 0.72371292
		 0.14512253 1.9917009e-07 0.82297707 -0.14510727 1.9917009e-07 0.82297707 -0.41782761 1.9917009e-07 0.72371292
		 -0.64015198 1.9917009e-07 0.53715897 -0.78526688 1.9917009e-07 0.28581619 -0.83566284 1.9917009e-07 0
		 -0.78526306 1.9917009e-07 -0.28581619 -0.64015198 1.9917009e-07 -0.53715897 -0.41782761 1.9917009e-07 -0.72371292
		 -0.14510536 1.9917009e-07 -0.82297516 0.14512253 1.9917009e-07 -0.82297516 0.41784477 1.9917009e-07 -0.72371292
		 0.64017296 1.9917009e-07 -0.53715897 0.14638519 0.43544653 -0.2535305 0.19166565 0.43544653 -0.17426872
		 0.055007935 0.43544653 -0.25311852 -0.055084229 0.43544653 -0.25311852 -0.14636803 0.43544653 -0.2535305
		 -0.19169807 0.43544653 -0.1741848 -0.24674034 0.43544653 -0.07884407 -0.29274368 0.43544653 0
		 -0.24669266 0.43544653 0.078927994 -0.19164848 0.43544653 0.17426872 -0.14636803 0.43544653 0.25353432
		 -0.054986954 0.43544653 0.25311089 0.055101395 0.43544653 0.25311089 0.14638519 0.43544653 0.25353432
		 0.19171524 0.43544653 0.1741848 0.24675751 0.43544653 0.078845978 0.29276276 0.43544653 0
		 0.24670982 0.43544653 -0.078927994 0.31985092 0.46765703 -0.281147 0.32582092 0.47730234 -0.2846241
		 0.32826042 0.4888216 -0.28608704 0.29845238 0.44418275 -0.26874352 0.29011917 0.43771634 -0.26310921
		 0.28110123 0.43544653 -0.25559425 0.38191032 0.44418681 -0.12419701 0.37285042 0.43771726 -0.1198101
		 0.36182404 0.43544653 -0.1157589 0.40337563 0.46765658 -0.13647079 0.40938187 0.47730181 -0.13988876
		 0.41186905 0.48882091 -0.14126396 0.083509445 0.46765658 -0.41756248 0.083553314 0.47730181 -0.42447281
		 0.083602905 0.48882097 -0.42731667 0.083404541 0.44418681 -0.39283752 0.082675934 0.43771726 -0.38280106
		 0.080669403 0.43544653 -0.37122154 -0.0835495 0.46765697 -0.41756248 -0.083576202 0.47730231 -0.42447281
		 -0.083620071 0.48882151 -0.42731667 -0.083507538 0.44418281 -0.3928318 -0.082794189 0.43771636 -0.38280106
		 -0.080791473 0.43544653 -0.37122917 -0.31986427 0.46765664 -0.28109169 -0.32582664 0.4773019 -0.28458405
		 -0.32826233 0.48882103 -0.2860527 -0.29850388 0.44418681 -0.26863861 -0.29017448 0.43771726 -0.26298904
		 -0.28115082 0.43544653 -0.25546265 -0.40339088 0.46765715 -0.1364212 -0.40938759 0.47730252 -0.13985252
		 -0.41187096 0.48882172 -0.14123344 -0.38195038 0.44418263 -0.12409019 -0.37290382 0.43771634 -0.11968803
		 -0.36188316 0.43544653 -0.11563873 -0.40335846 0.46765658 0.13647079 -0.4093647 0.47730181 0.13988876
		 -0.41185379 0.48882091 0.14126396 -0.38189316 0.44418681 0.12419701 -0.37283325 0.43771726 0.1198101
		 -0.36180687 0.43544653 0.1157589 -0.31983376 0.46765712 0.28114319 -0.32580566 0.47730243 0.28462219
		 -0.32824326 0.48882172 0.28607941 -0.29843521 0.44418275 0.26874352 -0.29010201 0.43771634 0.2631073
		 -0.28108406 0.43544653 0.25559044 -0.083488464 0.46765658 0.41756248 -0.083532333 0.47730181 0.42447281
		 -0.083581924 0.48882097 0.42731667 -0.08338356 0.44418684 0.3928318 -0.082654953 0.43771726 0.38279343
		 -0.080648422 0.43544653 0.37122154 0.083566666 0.46765697 0.41756248 0.083591461 0.47730231 0.42447281
		 0.083637238 0.48882151 0.42731667 0.083522797 0.44418281 0.3928318 0.082811356 0.43771636 0.38279343
		 0.08080864 0.43544653 0.37122726 0.31988144 0.46765664 0.28109169 0.32584381 0.4773019 0.28458405
		 0.3282795 0.48882103 0.28604889 0.29851913 0.44418681 0.26863861 0.29018974 0.43771726 0.26298714
		 0.28116798 0.43544653 0.25546265 0.40340614 0.46765703 0.13641357 0.40940285 0.47730231 0.13984871
		 0.41188812 0.48882157 0.14123344 0.38196754 0.44418263 0.12408829 0.37292099 0.43771634 0.11968803
		 0.36190033 0.43544653 0.11563873 0.45571899 0.7705555 -0.15900803 0.46520042 0.77697027 -0.16261292
		 0.47623825 0.77914268 -0.16679192 0.36556244 0.77055627 -0.31515121 0.37342453 0.77697039 -0.321558
		 0.38256454 0.77914268 -0.32902527 0.43227005 0.74694949 -0.15007019 0.42577171 0.73730546 -0.1475811
		 0.42311096 0.72576272 -0.14652634 0.34610176 0.74695766 -0.29931831 0.34069633 0.73731351 -0.29493904
		 0.33845139 0.72577119 -0.2931633 0.09016037 0.77055544 -0.47416306 0.091779709 0.77697027 -0.48417664
		 0.093679428 0.77914268 -0.49582672 0.086177826 0.74694949 -0.4493885 0.085084915 0.7373054 -0.44251442
		 0.084665298 0.72576272 -0.43968391 -0.090143204 0.77055627 -0.47415543 -0.091760635 0.77697039 -0.4841671
		 -0.093658447 0.77914268 -0.49581528 -0.086162567 0.74695766 -0.4493885 -0.085071564 0.73731351 -0.44251442
		 -0.084653854 0.72577119 -0.43968391 -0.3655529 0.77055544 -0.31515121 -0.37341499 0.77697027 -0.32156181
		 -0.38255501 0.77914268 -0.32903099 -0.34608841 0.74694937 -0.29931259 -0.34068298 0.73730516 -0.29493141
		 -0.33843994 0.72576261 -0.29315376 -0.4556942 0.77055603 -0.1590023 -0.46517372 0.77697039 -0.1626091
		 -0.47621155 0.77914268 -0.16679001 -0.43225479 0.7469576 -0.15006638 -0.42575645 0.73731351 -0.14757347
		 -0.4230957 0.72577095 -0.14651871 -0.45570183 0.7705555 0.15900803 -0.46518517 0.77697027 0.1626091
		 -0.47622108 0.77914268 0.16679192 -0.43225288 0.74694949 0.15006638 -0.42575455 0.73730546 0.14757538
		 -0.4230938 0.72576272 0.14652634 -0.36554527 0.77055627 0.31514931 -0.37340927 0.77697039 0.32155609
		 -0.38254929 0.77914268 0.32902336 -0.3460865 0.7469576 0.29931831 -0.34067917 0.73731351 0.29493713
		 -0.33843613 0.72577095 0.29315567 -0.090143204 0.77055544 0.47416306 -0.091760635 0.77697027 0.48417473
		 -0.093660355 0.77914268 0.49582672 -0.086158752 0.74694949 0.44938087 -0.085065842 0.7373054 0.44251442
		 -0.084648132 0.72576272 0.43967819 0.090158463 0.77055615 0.47415352 0.091775894 0.77697039 0.4841671
		 0.093673706 0.77914268 0.49581528 0.086179733 0.74695766 0.44938087;
	setAttr ".vt[166:331]" 0.085086823 0.73731351 0.44251442 0.084671021 0.72577119 0.43967819
		 0.36557007 0.77055544 0.31515121 0.37343216 0.77697027 0.32156181 0.38257217 0.77914268 0.32902908
		 0.34610367 0.74694937 0.29931259 0.34069824 0.73730516 0.29493141 0.3384552 0.72576261 0.29315376
		 0.45571327 0.77055627 0.1590023 0.46519279 0.77697039 0.1626091 0.47622871 0.77914268 0.1667881
		 0.43227196 0.74695766 0.15006638 0.42577553 0.73731351 0.14757347 0.42311287 0.72577119 0.14651871
		 0.93190384 0.76592177 -0.33901215 0.92251778 0.77257794 -0.33559418 0.91141891 0.77498573 -0.33155251
		 0.99167633 0.76597458 0 0.98169327 0.77263677 0 0.96988487 0.77505505 0 0.96632957 0.72951555 -0.35155106
		 0.97258949 0.71961701 -0.35382843 0.97478867 0.70796621 -0.35463333 1.028291702 0.72954851 0
		 1.034952164 0.71964753 0 1.03729248 0.70799661 0 0.78761673 0.72951806 -0.66108513
		 0.79272461 0.71961927 -0.66536713 0.79451752 0.70796806 -0.66687202 0.75955009 0.76592201 -0.63754082
		 0.75189781 0.772578 -0.63112068 0.74284935 0.77498573 -0.62353325 0.93190765 0.76592201 0.33901215
		 0.92251968 0.77257794 0.33559608 0.91142273 0.77498573 0.33155441 0.96632767 0.72951782 0.35154343
		 0.97258949 0.71961904 0.35382843 0.97478867 0.70796788 0.35462952 0.51415253 0.72954834 -0.8905201
		 0.51748276 0.71964747 -0.89628983 0.51865196 0.70799661 -0.89831543 0.49584579 0.76597464 -0.85881233
		 0.49085236 0.77263683 -0.85016441 0.48494911 0.77505505 -0.8399353 0.17872047 0.72951585 -1.012630463
		 0.17987633 0.71961719 -1.019195557 0.18028069 0.70796639 -1.021499634 0.17236519 0.76592171 -0.97655296
		 0.17063141 0.77257788 -0.96671486 0.16858101 0.77498573 -0.95508194 -0.1787014 0.72951806 -1.012630463
		 -0.17985725 0.71961927 -1.019195557 -0.18026161 0.70796806 -1.021499634 -0.17234612 0.76592201 -0.97655487
		 -0.17061234 0.77257794 -0.96671867 -0.16856384 0.77498573 -0.95508766 -0.51413727 0.72954851 -0.8905201
		 -0.5174675 0.71964753 -0.89628983 -0.5186367 0.70799661 -0.89831543 -0.49582863 0.76597464 -0.85881233
		 -0.49083519 0.77263683 -0.85016441 -0.48493195 0.77505505 -0.8399353 -0.78760147 0.72951555 -0.66108513
		 -0.79270744 0.71961713 -0.66536713 -0.79450226 0.70796627 -0.66687202 -0.75953293 0.76592195 -0.637537
		 -0.75187874 0.77257794 -0.63111877 -0.74283028 0.77498573 -0.62352753 -0.96631241 0.72951782 -0.35155106
		 -0.97257423 0.71961904 -0.35382843 -0.97477341 0.70796788 -0.35463333 -0.93189049 0.76592201 -0.33901215
		 -0.92250443 0.77257794 -0.33559608 -0.91140556 0.77498573 -0.33155441 -1.028276443 0.72954857 0
		 -1.034936905 0.71964753 0 -1.037275314 0.70799661 0 -0.99166107 0.7659744 0 -0.9816761 0.77263677 0
		 -0.96986771 0.77505505 0 -0.96631241 0.72951555 0.35154343 -0.97257423 0.71961701 0.35382843
		 -0.97477341 0.70796621 0.35462952 -0.93188858 0.76592177 0.33901215 -0.92250252 0.77257794 0.33559418
		 -0.91140366 0.77498573 0.33155251 -0.78760147 0.72951794 0.66107941 -0.79270744 0.71961921 0.66536522
		 -0.79450226 0.70796806 0.6668644 -0.75953484 0.76592201 0.63754082 -0.75188255 0.772578 0.63111877
		 -0.74283409 0.77498573 0.62352562 -0.51413727 0.72954851 0.8905201 -0.5174675 0.71964753 0.89628792
		 -0.5186367 0.70799661 0.89831543 -0.49582863 0.76597464 0.85880661 -0.49083519 0.77263683 0.85016441
		 -0.48493195 0.77505505 0.8399353 -0.1787014 0.72951585 1.012630463 -0.17985725 0.71961719 1.019193649
		 -0.18026161 0.70796639 1.021499634 -0.17234612 0.76592171 0.97655296 -0.17061234 0.77257788 0.96671104
		 -0.16856384 0.77498573 0.95508003 0.17871857 0.72951806 1.012630463 0.17987442 0.71961927 1.019193649
		 0.18027878 0.70796806 1.021499634 0.17236328 0.76592201 0.97655296 0.1706295 0.77257794 0.96671104
		 0.1685791 0.77498573 0.95508003 0.51415253 0.72954834 0.8905201 0.51748276 0.71964747 0.89628792
		 0.51865196 0.70799661 0.89831543 0.49584579 0.76597464 0.85880661 0.49085236 0.77263683 0.85016441
		 0.48494911 0.77505505 0.8399353 0.78761673 0.72951579 0.66107941 0.79272461 0.71961737 0.66536522
		 0.79451752 0.70796651 0.6668644 0.75954819 0.76592195 0.637537 0.751894 0.77257794 0.63111877
		 0.74284744 0.77498573 0.62352562 0.93347549 0.0193823 -0.33975029 0.92442131 0.012276255 -0.33645821
		 0.91352272 0.0090999706 -0.33249092 0.76098251 0.019382255 -0.63853645 0.75359917 0.012276359 -0.63234138
		 0.74471664 0.0091001447 -0.62488365 0.9666729 0.057286013 -0.35182762 0.97265053 0.067350373 -0.35400009
		 0.97474098 0.07900133 -0.35475922 0.78803444 0.057284139 -0.66124344 0.79290581 0.067348763 -0.66533279
		 0.79460716 0.079000019 -0.66676521 1.028707504 0.057285015 0 1.035068512 0.067349546 0
		 1.03729248 0.079000592 0 0.99338531 0.019382447 0 0.98374939 0.012276395 0 0.9721508 0.0091001336 0
		 0.9666729 0.057283994 0.35182762 0.97265053 0.067348614 0.35400009 0.97474098 0.078999855 0.35475922
		 0.9334774 0.019382253 0.3397541 0.92442131 0.012276362 0.33645821 0.91352272 0.0091001503 0.33249283
		 0.49669838 0.01938241 -0.86029243 0.49188042 0.012276373 -0.85194588 0.48608017 0.0091001112 -0.84189987
		 0.51435852 0.057285018 -0.89088058 0.51753998 0.067349546 -0.89639091 0.51865196 0.079000592 -0.89831543
		 0.17251015 0.019382484 -0.97828674 0.17083549 0.012276353 -0.96879959 0.16882133 0.0091000507 -0.95737457
		 0.17865181 0.057286099 -1.01307106 0.17975807 0.067350507 -1.0193367 0.18014717 0.079001479 -1.021524429
		 -0.17249298 0.01938224 -0.97828674 -0.17081833 0.012276403 -0.96879959 -0.16880226 0.0091002183 -0.95737457
		 -0.17863274 0.057284202 -1.01307106 -0.179739 0.067348793 -1.0193367 -0.1801281 0.079000033 -1.021524429
		 -0.49668312 0.019382425 -0.86029243 -0.49186516 0.012276391 -0.85194588;
	setAttr ".vt[332:497]" -0.48606491 0.0091001336 -0.84189987 -0.51434326 0.057285033 -0.89088058
		 -0.51752472 0.067349561 -0.89639091 -0.5186367 0.079000615 -0.89831543 -0.76096153 0.019382447 -0.63853645
		 -0.75358009 0.012276316 -0.63234138 -0.74469566 0.0091000106 -0.62488365 -0.78801537 0.057286028 -0.66124344
		 -0.79288673 0.067350447 -0.66533279 -0.79459 0.079001404 -0.66676521 -0.93346214 0.01938232 -0.33975029
		 -0.92440605 0.01227642 -0.33645821 -0.91350746 0.0091002146 -0.33249092 -0.96665573 0.057284024 -0.35182762
		 -0.97263336 0.067348629 -0.35400009 -0.97472572 0.078999855 -0.35475922 -0.99336815 0.019382328 0
		 -0.98373222 0.012276312 0 -0.97213364 0.0091000507 0 -1.028690338 0.057285015 0 -1.035053253 0.067349531 0
		 -1.037275314 0.079000577 0 -0.93346024 0.0193823 0.33975029 -0.92440414 0.012276255 0.33645821
		 -0.91350555 0.0090999706 0.33248901 -0.96665573 0.057286013 0.35182762 -0.97263336 0.067350373 0.35400009
		 -0.97472572 0.07900133 0.35475922 -0.76096344 0.019382313 0.63853264 -0.753582 0.012276423 0.63233757
		 -0.74469566 0.0091002183 0.62488365 -0.78801537 0.057284154 0.66124535 -0.79288673 0.067348771 0.66533089
		 -0.79459 0.079000019 0.66676521 -0.49668312 0.019382453 0.86029243 -0.49186516 0.012276403 0.85194397
		 -0.48606491 0.0091001401 0.84189987 -0.51434326 0.057285007 0.89087677 -0.51752472 0.067349546 0.89638901
		 -0.5186367 0.079000592 0.89831543 -0.17249298 0.019382438 0.97828293 -0.17081833 0.012276299 0.96879578
		 -0.16880226 0.0090999855 0.95737267 -0.17863274 0.05728605 1.01307106 -0.179739 0.067350477 1.019332886
		 -0.1801281 0.079001456 1.021524429 0.17250824 0.019382395 0.97828293 0.17083359 0.012276406 0.96879959
		 0.16881943 0.0091001634 0.95737267 0.1786499 0.057284042 1.01307106 0.17975616 0.067348726 1.019332886
		 0.18014526 0.078999966 1.021524429 0.49669838 0.019382432 0.86029243 0.49188042 0.012276378 0.85194397
		 0.48608017 0.0091001112 0.84189987 0.51435852 0.057285003 0.89087677 0.51753998 0.067349531 0.89638901
		 0.51865196 0.079000592 0.89831543 0.76098061 0.019382467 0.63853264 0.75359917 0.012276328 0.63233757
		 0.74471474 0.0091000181 0.62488365 0.78803444 0.057286132 0.66124535 0.79290581 0.067350574 0.66533089
		 0.79460716 0.079001538 0.66676521 0.26246643 0.4677012 -0.38151741 0.23575974 0.46770865 -0.40833664
		 0.1991806 0.46770108 -0.41805458 0.26645279 0.47736403 -0.3884182 0.23974228 0.47737414 -0.41523552
		 0.20316696 0.47736394 -0.42495728 0.20480156 0.48888662 -0.4277916 0.24137688 0.48889732 -0.41806602
		 0.26808739 0.48888677 -0.39125443 0.24234009 0.43768781 -0.34665489 0.21563148 0.43768206 -0.37347603
		 0.17905617 0.43768808 -0.38319588 0.23560905 0.43544653 -0.33499908 0.20889473 0.43544653 -0.36180115
		 0.17232323 0.43544653 -0.37153244 0.18483925 0.44412655 -0.39321709 0.22141266 0.44411466 -0.3834877
		 0.24812317 0.44412538 -0.35667801 0.4329586 0.44412655 -0.03653717 0.4428215 0.44411454 0
		 0.4329567 0.44412535 0.03653717 0.42138672 0.43768808 -0.03653717 0.43125725 0.43768206 0
		 0.42138672 0.43768781 0.03653717 0.40792656 0.43544653 0.03653717 0.41778183 0.43544653 0
		 0.40792465 0.43544653 -0.03653717 -0.19916534 0.46770114 -0.41805458 -0.23574448 0.46770859 -0.40833664
		 -0.26244926 0.46770108 -0.38151741 -0.2031498 0.47736394 -0.42495728 -0.23972702 0.47737408 -0.41523552
		 -0.26643562 0.47736388 -0.3884182 -0.26807213 0.48888659 -0.39125443 -0.24136162 0.4888972 -0.41806602
		 -0.2047863 0.48888671 -0.4277916 -0.179039 0.43768784 -0.38319588 -0.21561623 0.43768209 -0.37347603
		 -0.24232292 0.43768808 -0.34665871 -0.17230797 0.43544653 -0.37153625 -0.20887756 0.43544653 -0.36180115
		 -0.23559189 0.43544653 -0.33499908 -0.24810791 0.44412655 -0.35668373 -0.2213974 0.44411466 -0.3834877
		 -0.18482208 0.44412544 -0.39321709 -0.46162224 0.4677012 -0.03653717 -0.47149658 0.46770859 0
		 -0.46162224 0.46770105 0.03653717 -0.46959305 0.47736403 -0.03653717 -0.47946167 0.47737414 0
		 -0.46959305 0.47736388 0.03653717 -0.47286606 0.48888659 0.03653717 -0.48273277 0.48889723 0
		 -0.47286606 0.48888677 -0.03653717 -0.42136955 0.43768781 -0.03653717 -0.43124008 0.43768206 0
		 -0.42136955 0.43768808 0.03653717 -0.40790939 0.43544653 -0.03653717 -0.41776466 0.43544653 0
		 -0.40790558 0.43544653 0.03653717 -0.43294144 0.44412655 0.03653717 -0.44280434 0.44411454 0
		 -0.43293953 0.44412535 -0.03653717 -0.26244926 0.4677012 0.38151932 -0.23574448 0.46770865 0.40833664
		 -0.19916344 0.46770108 0.41805458 -0.26643372 0.47736403 0.3884201 -0.23972702 0.47737414 0.41523552
		 -0.2031498 0.47736394 0.42495728 -0.20478439 0.48888662 0.42778778 -0.24136162 0.48889732 0.41806793
		 -0.26807022 0.48888683 0.39125061 -0.24232292 0.43768781 0.34665108 -0.21561623 0.43768206 0.37347412
		 -0.17903709 0.43768808 0.38319397 -0.2355938 0.43544653 0.33500099 -0.20887756 0.43544653 0.36180305
		 -0.17230606 0.43544653 0.37153625 -0.18482208 0.44412658 0.39321518 -0.2213974 0.44411466 0.38348961
		 -0.24810791 0.44412538 0.3566761 0.1991806 0.46770114 0.41805458 0.23575974 0.46770856 0.40833664
		 0.26246643 0.46770105 0.38151932 0.20316696 0.47736394 0.42495728 0.23974228 0.47737408 0.41523552
		 0.26645088 0.47736388 0.3884201 0.26808739 0.48888659 0.39125061 0.24137688 0.4888972 0.41806793
		 0.20480156 0.48888671 0.42778778 0.17905426 0.43768784 0.38319397 0.21563148 0.43768209 0.37347412
		 0.24234009 0.43768808 0.3466568 0.17232323 0.43544653 0.37153816 0.20889473 0.43544653 0.36180305
		 0.23560715 0.43544653 0.33499908 0.24812508 0.44412655 0.3566761 0.22141266 0.44411466 0.38348961
		 0.18483925 0.44412544 0.39321518 0.4616394 0.4677012 0.03653717 0.47151375 0.46770868 0
		 0.4616394 0.46770114 -0.03653717;
	setAttr ".vt[498:611]" 0.46961212 0.47736403 0.03653717 0.47948074 0.47737414 0
		 0.46961212 0.47736388 -0.03653717 0.47288322 0.48888659 -0.03653717 0.48275185 0.48889729 0
		 0.47288322 0.48888674 0.03653717 0.2948246 0.77053976 -0.43755913 0.26807404 0.77053744 -0.46430016
		 0.23153877 0.7705397 -0.47410011 0.30060768 0.77691197 -0.44758034 0.27385902 0.77690417 -0.47432137
		 0.23732376 0.77691191 -0.48411751 0.24406433 0.77903783 -0.4957943 0.28059959 0.77902418 -0.48600006
		 0.30734825 0.77903783 -0.4592514 0.49767876 0.74705952 -0.03653717 0.5074501 0.74707651 0
		 0.49767876 0.74706149 0.03653717 0.48970795 0.73741508 -0.03653717 0.49947548 0.7374323 0
		 0.48970795 0.73741698 0.03653717 0.48643494 0.72588897 0.03653717 0.49620056 0.72590655 0
		 0.48643494 0.72588682 -0.03653717 0.53792572 0.77691197 -0.03653717 0.54771042 0.77690423 0
		 0.53792572 0.77691203 0.03653717 0.55140686 0.77903783 -0.03653717 0.56119156 0.77902418 0
		 0.55140305 0.77903783 0.03653717 0.52635765 0.77053994 0.03653717 0.53614044 0.77053779 0
		 0.52635956 0.77053976 -0.03653717 0.2765007 0.73741698 -0.40582275 0.2497406 0.7374323 -0.43255043
		 0.21321487 0.73741508 -0.44236183 0.2748642 0.72588897 -0.40298843 0.2481041 0.72590655 -0.4297142
		 0.21157837 0.72588682 -0.4395256 0.21719933 0.74705952 -0.44926453 0.25372887 0.74707657 -0.43945694
		 0.28048515 0.74706149 -0.41272545 -0.23152161 0.77053988 -0.4740963 -0.26805687 0.77053756 -0.46430016
		 -0.29480934 0.77053976 -0.43755913 -0.23730659 0.77691197 -0.48411751 -0.27384186 0.77690417 -0.47432137
		 -0.30059242 0.77691191 -0.44758034 -0.30733299 0.77903783 -0.45925331 -0.28058243 0.77902418 -0.48600006
		 -0.24404716 0.77903783 -0.4957943 -0.21319962 0.73741716 -0.44236183 -0.24972534 0.73743254 -0.43255043
		 -0.27648354 0.73741508 -0.40582275 -0.2115612 0.72588897 -0.4395256 -0.24808884 0.72590655 -0.4297142
		 -0.27484703 0.72588694 -0.40298843 -0.28046799 0.74705952 -0.41272545 -0.2537117 0.74707669 -0.43945694
		 -0.21718407 0.74706161 -0.44926453 -0.52633858 0.77053994 -0.03653717 -0.53612137 0.77053779 0
		 -0.52634048 0.77053976 0.036539078 -0.53790665 0.77691203 -0.03653717 -0.54769135 0.77690423 0
		 -0.53791046 0.77691197 0.03653717 -0.55138779 0.77903783 0.03653717 -0.56117439 0.77902418 0
		 -0.55138397 0.77903783 -0.03653717 -0.48968887 0.73741698 -0.03653717 -0.49945831 0.73743236 0
		 -0.48968887 0.73741508 0.03653717 -0.48641586 0.72588897 -0.03653717 -0.4961834 0.72590655 0
		 -0.48641586 0.72588694 0.03653717 -0.49765968 0.74705952 0.036539078 -0.50743294 0.74707669 0
		 -0.49765968 0.74706155 -0.03653717 -0.29480743 0.77053946 0.43756294 -0.26805687 0.77053714 0.46430588
		 -0.23152351 0.77053928 0.47410202 -0.30059242 0.77691156 0.44758034 -0.27384186 0.77690381 0.47432327
		 -0.23730659 0.7769115 0.48411942 -0.24404716 0.77903736 0.4957943 -0.28058243 0.77902371 0.48600006
		 -0.30733109 0.77903736 0.4592514 -0.27648354 0.73741651 0.40582466 -0.24972534 0.73743182 0.43255234
		 -0.21319771 0.7374146 0.44236374 -0.27484703 0.72588849 0.40299225 -0.24808884 0.72590607 0.42971802
		 -0.2115612 0.72588634 0.4395256 -0.21718216 0.74705905 0.44926071 -0.2537117 0.74707603 0.43945885
		 -0.28046799 0.74706101 0.41272354 0.23153877 0.77053946 0.47410202 0.26807404 0.77053732 0.46430397
		 0.2948246 0.77053928 0.43756485 0.23732376 0.77691156 0.48411942 0.27385902 0.77690381 0.47432327
		 0.30060959 0.7769115 0.44758415 0.30734825 0.77903736 0.4592514 0.28059769 0.77902371 0.48600006
		 0.24406242 0.77903736 0.49579048 0.21321487 0.73741663 0.44236374 0.2497406 0.73743188 0.43255234
		 0.2765007 0.7374146 0.40582466 0.21157837 0.72588849 0.4395256 0.2481041 0.72590607 0.42971802
		 0.2748642 0.72588634 0.40299225 0.28048515 0.74705905 0.41272354 0.25372887 0.74707615 0.43945885
		 0.21719933 0.74706101 0.44926071;
	setAttr -s 1194 ".ed";
	setAttr ".ed[0:165]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0 7 8 0 8 9 0
		 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 0 0 18 19 1 20 18 1
		 21 20 1 22 21 1 23 22 1 24 23 1 25 24 1 26 25 1 27 26 1 28 27 1 29 28 1 30 29 1 31 30 1
		 32 31 1 33 32 1 34 33 1 35 34 1 19 35 1 38 37 1 47 38 1 37 36 1 36 45 1 49 48 1 50 49 1
		 43 42 1 42 39 1 41 44 1 44 43 1 41 40 1 40 39 1 53 410 1 44 422 1 47 46 1 46 45 1
		 55 54 1 54 48 1 50 56 1 56 55 1 53 52 1 59 53 1 52 51 1 51 57 1 59 58 1 58 57 1 61 60 1
		 62 61 1 65 437 1 67 66 1 66 60 1 62 68 1 68 67 1 65 64 1 71 65 1 64 63 1 63 69 1
		 71 70 1 70 69 1 73 72 1 74 73 1 77 455 1 79 78 1 78 72 1 74 80 1 80 79 1 77 76 1
		 83 77 1 76 75 1 75 81 1 83 82 1 82 81 1 85 84 1 86 85 1 89 473 1 91 90 1 90 84 1
		 86 92 1 92 91 1 89 88 1 95 89 1 88 87 1 87 93 1 95 94 1 94 93 1 97 96 1 98 97 1 101 491 1
		 103 102 1 102 96 1 98 104 1 104 103 1 101 100 1 107 101 1 100 99 1 99 105 1 107 106 1
		 106 105 1 112 111 1 111 108 1 110 113 1 113 112 1 110 109 1 109 108 1 113 512 1 116 115 1
		 119 116 1 115 114 1 114 117 1 119 118 1 118 117 1 178 177 1 179 178 1 176 527 1 121 120 1
		 122 121 1 127 126 1 126 120 1 122 128 1 128 127 1 125 124 1 131 125 1 124 123 1 123 129 1
		 128 548 1 131 130 1 130 129 1 133 132 1 134 133 1 139 138 1 138 132 1 134 140 1 140 139 1
		 137 136 1 143 137 1 136 135 1 135 141 1 140 566 1 143 142 1 142 141 1 145 144 1 146 145 1
		 151 150 1 150 144 1 146 152 1 152 151 1 149 148 1 155 149 1 148 147 1 147 153 1;
	setAttr ".ed[166:331]" 152 584 1 155 154 1 154 153 1 157 156 1 158 157 1 163 162 1
		 162 156 1 158 164 1 164 163 1 161 160 1 167 161 1 160 159 1 159 165 1 164 602 1 167 166 1
		 166 165 1 169 168 1 170 169 1 175 174 1 174 168 1 170 176 1 176 175 1 173 172 1 179 173 1
		 172 171 1 171 177 1 184 183 1 183 180 1 182 185 1 185 184 1 182 181 1 197 182 1 181 180 1
		 180 195 1 199 198 1 198 183 1 185 200 1 200 199 1 193 192 1 192 186 1 188 194 1 194 193 1
		 188 187 1 191 188 1 187 186 1 186 189 1 191 190 1 203 191 1 190 189 1 189 201 1 205 204 1
		 204 192 1 194 206 1 206 205 1 197 196 1 209 197 1 196 195 1 195 207 1 286 285 1 285 198 1
		 200 287 1 287 286 1 203 202 1 284 203 1 202 201 1 201 282 1 211 210 1 210 204 1 206 212 1
		 212 211 1 209 208 1 215 209 1 208 207 1 207 213 1 217 216 1 216 210 1 212 218 1 218 217 1
		 215 214 1 221 215 1 214 213 1 213 219 1 223 222 1 222 216 1 218 224 1 224 223 1 221 220 1
		 227 221 1 220 219 1 219 225 1 229 228 1 228 222 1 224 230 1 230 229 1 227 226 1 233 227 1
		 226 225 1 225 231 1 235 234 1 234 228 1 230 236 1 236 235 1 233 232 1 239 233 1 232 231 1
		 231 237 1 241 240 1 240 234 1 236 242 1 242 241 1 239 238 1 245 239 1 238 237 1 237 243 1
		 247 246 1 246 240 1 242 248 1 248 247 1 245 244 1 251 245 1 244 243 1 243 249 1 253 252 1
		 252 246 1 248 254 1 254 253 1 251 250 1 257 251 1 250 249 1 249 255 1 259 258 1 258 252 1
		 254 260 1 260 259 1 257 256 1 263 257 1 256 255 1 255 261 1 265 264 1 264 258 1 260 266 1
		 266 265 1 263 262 1 269 263 1 262 261 1 261 267 1 271 270 1 270 264 1 266 272 1 272 271 1
		 269 268 1 275 269 1 268 267 1 267 273 1 277 276 1 276 270 1 272 278 1 278 277 1 275 274 1
		 281 275 1 274 273 1 273 279 1 283 282 1 282 276 1 278 284 1 284 283 1;
	setAttr ".ed[332:497]" 281 280 1 287 281 1 280 279 1 279 285 1 292 291 1 291 288 1
		 290 293 1 293 292 1 290 289 1 305 290 1 289 288 1 288 303 1 313 312 1 312 291 1 293 314 1
		 314 313 1 301 300 1 300 294 1 296 302 1 302 301 1 296 295 1 299 296 1 295 294 1 294 297 1
		 299 298 1 317 299 1 298 297 1 297 315 1 307 306 1 306 300 1 302 308 1 308 307 1 305 304 1
		 311 305 1 304 303 1 303 309 1 394 393 1 393 306 1 308 395 1 395 394 1 311 310 1 392 311 1
		 310 309 1 309 390 1 319 318 1 318 312 1 314 320 1 320 319 1 317 316 1 323 317 1 316 315 1
		 315 321 1 325 324 1 324 318 1 320 326 1 326 325 1 323 322 1 329 323 1 322 321 1 321 327 1
		 331 330 1 330 324 1 326 332 1 332 331 1 329 328 1 335 329 1 328 327 1 327 333 1 337 336 1
		 336 330 1 332 338 1 338 337 1 335 334 1 341 335 1 334 333 1 333 339 1 343 342 1 342 336 1
		 338 344 1 344 343 1 341 340 1 347 341 1 340 339 1 339 345 1 349 348 1 348 342 1 344 350 1
		 350 349 1 347 346 1 353 347 1 346 345 1 345 351 1 355 354 1 354 348 1 350 356 1 356 355 1
		 353 352 1 359 353 1 352 351 1 351 357 1 361 360 1 360 354 1 356 362 1 362 361 1 359 358 1
		 365 359 1 358 357 1 357 363 1 367 366 1 366 360 1 362 368 1 368 367 1 365 364 1 371 365 1
		 364 363 1 363 369 1 373 372 1 372 366 1 368 374 1 374 373 1 371 370 1 377 371 1 370 369 1
		 369 375 1 379 378 1 378 372 1 374 380 1 380 379 1 377 376 1 383 377 1 376 375 1 375 381 1
		 385 384 1 384 378 1 380 386 1 386 385 1 383 382 1 389 383 1 382 381 1 381 387 1 391 390 1
		 390 384 1 386 392 1 392 391 1 389 388 1 395 389 1 388 387 1 387 393 1 39 36 1 42 45 1
		 48 51 1 54 57 1 60 63 1 66 69 1 72 75 1 78 81 1 84 87 1 90 93 1 96 99 1 102 105 1
		 114 108 1 111 117 1 120 123 1 126 129 1 132 135 1 138 141 1;
	setAttr ".ed[498:663]" 144 147 1 150 153 1 156 159 1 162 165 1 168 171 1 174 177 1
		 119 38 1 47 116 1 125 50 1 131 56 1 137 62 1 143 68 1 149 74 1 155 80 1 161 86 1
		 167 92 1 173 98 1 179 104 1 186 180 1 183 189 1 192 195 1 198 201 1 204 207 1 210 213 1
		 216 219 1 222 225 1 228 231 1 234 237 1 240 243 1 246 249 1 252 255 1 258 261 1 264 267 1
		 270 273 1 276 279 1 282 285 1 294 288 1 291 297 1 300 303 1 306 309 1 312 315 1 318 321 1
		 324 327 1 330 333 1 336 339 1 342 345 1 348 351 1 354 357 1 360 363 1 366 369 1 372 375 1
		 378 381 1 384 387 1 390 393 1 188 296 1 299 194 1 317 206 1 323 212 1 329 218 1 335 224 1
		 341 230 1 347 236 1 353 242 1 359 248 1 365 254 1 371 260 1 377 266 1 383 272 1 389 278 1
		 395 284 1 308 203 1 302 191 1 305 1 1 0 290 1 311 2 1 392 3 1 386 4 1 380 5 1 374 6 1
		 368 7 1 362 8 1 356 9 1 350 10 1 344 11 1 338 12 1 332 13 1 326 14 1 320 15 1 314 16 1
		 293 17 1 197 113 1 110 182 1 19 41 1 53 20 1 59 21 1 65 23 1 71 24 1 77 26 1 83 27 1
		 89 29 1 95 30 1 101 32 1 107 33 1 44 35 1 40 43 1 37 46 1 49 55 1 52 58 1 61 67 1
		 64 70 1 73 79 1 76 82 1 85 91 1 88 94 1 97 103 1 100 106 1 109 112 1 115 118 1 121 127 1
		 124 130 1 133 139 1 136 142 1 145 151 1 148 154 1 157 163 1 160 166 1 169 175 1 172 178 1
		 181 184 1 184 199 1 187 193 1 187 190 1 193 205 1 181 196 1 199 286 1 190 202 1 205 211 1
		 196 208 1 211 217 1 208 214 1 217 223 1 214 220 1 223 229 1 220 226 1 229 235 1 226 232 1
		 235 241 1 232 238 1 241 247 1 238 244 1 247 253 1 244 250 1 253 259 1 250 256 1 259 265 1
		 256 262 1 265 271 1 262 268 1 271 277 1 268 274 1 277 283 1 274 280 1 202 283 1 280 286 1
		 289 292 1 292 313 1;
	setAttr ".ed[664:829]" 295 301 1 295 298 1 301 307 1 289 304 1 307 394 1 304 310 1
		 313 319 1 298 316 1 319 325 1 316 322 1 325 331 1 322 328 1 331 337 1 328 334 1 337 343 1
		 334 340 1 343 349 1 340 346 1 349 355 1 346 352 1 355 361 1 352 358 1 361 367 1 358 364 1
		 367 373 1 364 370 1 373 379 1 370 376 1 379 385 1 376 382 1 385 391 1 382 388 1 310 391 1
		 388 394 1 200 176 1 287 170 1 275 164 1 269 158 1 257 152 1 251 146 1 239 140 1 233 134 1
		 221 128 1 215 122 1 408 41 1 420 107 1 435 59 1 453 71 1 471 83 1 489 95 1 510 122 1
		 525 110 1 546 134 1 564 146 1 582 158 1 600 170 1 413 396 1 398 411 1 398 397 1 401 398 1
		 397 396 1 396 399 1 401 400 1 400 403 1 403 402 1 402 401 1 400 399 1 399 404 1 404 403 1
		 536 402 1 404 534 1 409 408 1 408 405 1 407 410 1 410 409 1 407 406 1 406 412 1 412 411 1
		 411 407 1 406 405 1 405 413 1 413 412 1 497 414 1 416 495 1 416 415 1 419 416 1 415 414 1
		 414 417 1 419 418 1 418 421 1 421 420 1 420 419 1 418 417 1 417 422 1 422 421 1 440 423 1
		 425 438 1 425 424 1 428 425 1 424 423 1 423 426 1 428 427 1 427 430 1 430 429 1 429 428 1
		 427 426 1 426 431 1 431 430 1 554 429 1 431 552 1 436 435 1 435 432 1 434 437 1 437 436 1
		 434 433 1 433 439 1 439 438 1 438 434 1 433 432 1 432 440 1 440 439 1 458 441 1 443 456 1
		 443 442 1 446 443 1 442 441 1 441 444 1 446 445 1 445 448 1 448 447 1 447 446 1 445 444 1
		 444 449 1 449 448 1 572 447 1 449 570 1 454 453 1 453 450 1 452 455 1 455 454 1 452 451 1
		 451 457 1 457 456 1 456 452 1 451 450 1 450 458 1 458 457 1 476 459 1 461 474 1 461 460 1
		 464 461 1 460 459 1 459 462 1 464 463 1 463 466 1 466 465 1 465 464 1 463 462 1 462 467 1
		 467 466 1 590 465 1 467 588 1 472 471 1 471 468 1 470 473 1 473 472 1;
	setAttr ".ed[830:995]" 470 469 1 469 475 1 475 474 1 474 470 1 469 468 1 468 476 1
		 476 475 1 494 477 1 479 492 1 479 478 1 482 479 1 478 477 1 477 480 1 482 481 1 481 484 1
		 484 483 1 483 482 1 481 480 1 480 485 1 485 484 1 608 483 1 485 606 1 490 489 1 489 486 1
		 488 491 1 491 490 1 488 487 1 487 493 1 493 492 1 492 488 1 487 486 1 486 494 1 494 493 1
		 497 496 1 500 497 1 496 495 1 495 498 1 500 499 1 499 502 1 502 501 1 501 500 1 499 498 1
		 498 503 1 503 502 1 521 501 1 503 519 1 539 504 1 506 537 1 506 505 1 509 506 1 505 504 1
		 504 507 1 509 508 1 508 511 1 511 510 1 510 509 1 508 507 1 507 512 1 512 511 1 530 513 1
		 515 528 1 515 514 1 518 515 1 514 513 1 513 516 1 518 517 1 517 520 1 520 519 1 519 518 1
		 517 516 1 516 521 1 521 520 1 526 525 1 525 522 1 524 527 1 527 526 1 524 523 1 523 529 1
		 529 528 1 528 524 1 523 522 1 522 530 1 530 529 1 535 534 1 534 531 1 533 536 1 536 535 1
		 533 532 1 532 538 1 538 537 1 537 533 1 532 531 1 531 539 1 539 538 1 557 540 1 542 555 1
		 542 541 1 545 542 1 541 540 1 540 543 1 545 544 1 544 547 1 547 546 1 546 545 1 544 543 1
		 543 548 1 548 547 1 553 552 1 552 549 1 551 554 1 554 553 1 551 550 1 550 556 1 556 555 1
		 555 551 1 550 549 1 549 557 1 557 556 1 575 558 1 560 573 1 560 559 1 563 560 1 559 558 1
		 558 561 1 563 562 1 562 565 1 565 564 1 564 563 1 562 561 1 561 566 1 566 565 1 571 570 1
		 570 567 1 569 572 1 572 571 1 569 568 1 568 574 1 574 573 1 573 569 1 568 567 1 567 575 1
		 575 574 1 593 576 1 578 591 1 578 577 1 581 578 1 577 576 1 576 579 1 581 580 1 580 583 1
		 583 582 1 582 581 1 580 579 1 579 584 1 584 583 1 589 588 1 588 585 1 587 590 1 590 589 1
		 587 586 1 586 592 1 592 591 1 591 587 1 586 585 1 585 593 1 593 592 1;
	setAttr ".ed[996:1161]" 611 594 1 596 609 1 596 595 1 599 596 1 595 594 1 594 597 1
		 599 598 1 598 601 1 601 600 1 600 599 1 598 597 1 597 602 1 602 601 1 607 606 1 606 603 1
		 605 608 1 608 607 1 605 604 1 604 610 1 610 609 1 609 605 1 604 603 1 603 611 1 611 610 1
		 36 396 1 413 39 1 398 48 1 51 411 1 54 423 1 440 57 1 425 60 1 63 438 1 66 441 1
		 458 69 1 443 72 1 75 456 1 78 459 1 476 81 1 461 84 1 87 474 1 90 477 1 494 93 1
		 479 96 1 99 492 1 102 495 1 416 105 1 497 45 1 42 414 1 114 513 1 530 108 1 111 504 1
		 539 117 1 506 120 1 123 537 1 126 540 1 557 129 1 542 132 1 135 555 1 138 558 1 575 141 1
		 560 144 1 147 573 1 150 576 1 593 153 1 578 156 1 159 591 1 162 594 1 611 165 1 596 168 1
		 171 609 1 174 528 1 515 177 1 119 534 1 404 38 1 536 125 1 50 402 1 131 552 1 431 56 1
		 554 137 1 62 429 1 143 570 1 449 68 1 572 149 1 74 447 1 155 588 1 467 80 1 590 161 1
		 86 465 1 167 606 1 485 92 1 608 173 1 98 483 1 179 519 1 503 104 1 521 116 1 47 501 1
		 37 399 1 401 49 1 40 405 1 43 417 1 407 52 1 55 426 1 428 61 1 58 432 1 434 64 1
		 67 444 1 446 73 1 70 450 1 452 76 1 79 462 1 464 85 1 82 468 1 470 88 1 91 480 1
		 482 97 1 94 486 1 488 100 1 103 498 1 46 500 1 106 419 1 112 507 1 115 516 1 518 178 1
		 109 522 1 509 121 1 118 531 1 533 124 1 127 543 1 545 133 1 130 549 1 551 136 1 139 561 1
		 563 145 1 142 567 1 569 148 1 151 579 1 581 157 1 154 585 1 587 160 1 163 597 1 599 169 1
		 166 603 1 605 172 1 524 175 1 409 18 1 421 34 1 436 22 1 454 25 1 472 28 1 490 31 1
		 511 209 1 526 185 1 547 227 1 565 245 1 583 263 1 601 281 1 397 400 1 406 409 1 397 412 1
		 415 418 1 424 427 1 433 436 1 424 439 1 442 445 1 451 454 1 442 457 1;
	setAttr ".ed[1162:1193]" 460 463 1 469 472 1 460 475 1 478 481 1 487 490 1 478 493 1
		 415 496 1 496 499 1 505 508 1 514 517 1 502 520 1 523 526 1 514 529 1 532 535 1 403 535 1
		 505 538 1 541 544 1 550 553 1 430 553 1 541 556 1 559 562 1 568 571 1 448 571 1 559 574 1
		 577 580 1 586 589 1 466 589 1 577 592 1 595 598 1 604 607 1 484 607 1 595 610 1;
	setAttr -s 612 ".n";
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
	setAttr ".n[498:611]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 583 -ch 2370 ".fc";
	setAttr ".fc[0:499]" -type "polyFaces" 
		f 18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 -33 -34 -35 -36
		mu 0 18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		f 4 -481 -44 481 -40
		mu 0 4 18 19 20 21
		f 4 -483 -54 483 -60
		mu 0 4 22 23 24 25
		f 4 -485 -67 485 -73
		mu 0 4 26 27 28 29
		f 4 -487 -80 487 -86
		mu 0 4 30 31 32 33
		f 4 -489 -93 489 -99
		mu 0 4 34 35 36 37
		f 4 -491 -106 491 -112
		mu 0 4 38 39 40 41
		f 4 492 -116 493 -125
		mu 0 4 42 43 44 45
		f 4 -495 -134 495 -140
		mu 0 4 46 47 48 49
		f 4 -497 -147 497 -153
		mu 0 4 50 51 52 53
		f 4 -499 -160 499 -166
		mu 0 4 54 55 56 57
		f 4 -501 -173 501 -179
		mu 0 4 58 59 60 61
		f 4 -503 -186 503 -192
		mu 0 4 62 63 64 65
		f 4 -123 504 -38 505
		mu 0 4 66 67 68 69
		f 4 -138 507 -55 -507
		mu 0 4 70 71 72 73
		f 4 -151 509 -68 -509
		mu 0 4 74 75 76 77
		f 4 -164 511 -81 -511
		mu 0 4 78 79 80 81
		f 4 -177 513 -94 -513
		mu 0 4 82 83 84 85
		f 4 -190 515 -107 -515
		mu 0 4 86 87 88 89
		f 4 516 -194 517 -212
		mu 0 4 90 91 92 93
		f 4 -517 -206 518 -200
		mu 0 4 91 90 94 95
		f 4 -518 -202 519 -216
		mu 0 4 93 92 96 97
		f 4 -519 -218 520 -224
		mu 0 4 95 94 98 99
		f 4 -521 -234 521 -240
		mu 0 4 99 98 100 101
		f 4 -522 -242 522 -248
		mu 0 4 101 100 102 103
		f 4 -523 -250 523 -256
		mu 0 4 103 102 104 105
		f 4 -524 -258 524 -264
		mu 0 4 105 104 106 107
		f 4 -525 -266 525 -272
		mu 0 4 107 106 108 109
		f 4 -526 -274 526 -280
		mu 0 4 109 108 110 111
		f 4 -527 -282 527 -288
		mu 0 4 111 110 112 113
		f 4 -528 -290 528 -296
		mu 0 4 113 112 114 115
		f 4 -529 -298 529 -304
		mu 0 4 115 114 116 117
		f 4 -530 -306 530 -312
		mu 0 4 117 116 118 119
		f 4 -531 -314 531 -320
		mu 0 4 119 118 120 121
		f 4 -532 -322 532 -328
		mu 0 4 121 120 122 123
		f 4 -533 -330 533 -336
		mu 0 4 123 122 124 125
		f 4 -534 -232 -520 -226
		mu 0 4 125 124 97 96
		f 4 534 -338 535 -356
		mu 0 4 126 127 128 129
		f 4 -535 -350 536 -344
		mu 0 4 127 126 130 131
		f 4 -537 -362 537 -368
		mu 0 4 131 130 132 133
		f 4 -536 -346 538 -360
		mu 0 4 129 128 134 135
		f 4 -539 -378 539 -384
		mu 0 4 135 134 136 137
		f 4 -540 -386 540 -392
		mu 0 4 137 136 138 139
		f 4 -541 -394 541 -400
		mu 0 4 139 138 140 141
		f 4 -542 -402 542 -408
		mu 0 4 141 140 142 143
		f 4 -543 -410 543 -416
		mu 0 4 143 142 144 145
		f 4 -544 -418 544 -424
		mu 0 4 145 144 146 147
		f 4 -545 -426 545 -432
		mu 0 4 147 146 148 149
		f 4 -546 -434 546 -440
		mu 0 4 149 148 150 151
		f 4 -547 -442 547 -448
		mu 0 4 151 150 152 153
		f 4 -548 -450 548 -456
		mu 0 4 153 152 154 155
		f 4 -549 -458 549 -464
		mu 0 4 155 154 156 157
		f 4 -550 -466 550 -472
		mu 0 4 157 156 158 159
		f 4 -551 -474 551 -480
		mu 0 4 159 158 160 161
		f 4 -552 -376 -538 -370
		mu 0 4 161 160 133 132
		f 4 -207 552 -354 553
		mu 0 4 162 163 359 362
		f 4 -219 -554 -358 554
		mu 0 4 164 162 362 371
		f 4 -235 -555 -382 555
		mu 0 4 165 164 371 374
		f 4 -243 -556 -390 556
		mu 0 4 166 165 374 377
		f 4 -251 -557 -398 557
		mu 0 4 167 166 377 380
		f 4 -259 -558 -406 558
		mu 0 4 168 167 380 383
		f 4 -267 -559 -414 559
		mu 0 4 169 168 383 386
		f 4 -275 -560 -422 560
		mu 0 4 170 169 386 389
		f 4 -283 -561 -430 561
		mu 0 4 171 170 389 392
		f 4 -291 -562 -438 562
		mu 0 4 172 171 392 395
		f 4 -299 -563 -446 563
		mu 0 4 173 172 395 398
		f 4 -307 -564 -454 564
		mu 0 4 174 173 398 401
		f 4 -315 -565 -462 565
		mu 0 4 175 174 401 404
		f 4 -323 -566 -470 566
		mu 0 4 176 175 404 407
		f 4 -331 -567 -478 567
		mu 0 4 177 176 407 367
		f 4 -230 -568 -371 568
		mu 0 4 178 177 367 364
		f 4 -214 -569 -363 569
		mu 0 4 179 178 364 615
		f 4 -553 -210 -570 -351
		mu 0 4 359 163 613 360
		f 4 -342 570 -1 571
		mu 0 4 180 181 182 183
		f 4 -366 572 -2 -571
		mu 0 4 181 184 185 182
		f 4 -374 573 -3 -573
		mu 0 4 184 186 187 185
		f 4 -475 574 -4 -574
		mu 0 4 186 188 189 187
		f 4 -467 575 -5 -575
		mu 0 4 188 190 191 189
		f 4 -459 576 -6 -576
		mu 0 4 190 192 193 191
		f 4 -451 577 -7 -577
		mu 0 4 192 194 195 193
		f 4 -443 578 -8 -578
		mu 0 4 194 196 197 195
		f 4 -435 579 -9 -579
		mu 0 4 196 198 199 197
		f 4 -427 580 -10 -580
		mu 0 4 198 200 201 199
		f 4 -419 581 -11 -581
		mu 0 4 200 202 203 201
		f 4 -411 582 -12 -582
		mu 0 4 202 204 205 203
		f 4 -403 583 -13 -583
		mu 0 4 204 206 207 205
		f 4 -395 584 -14 -584
		mu 0 4 206 208 209 207
		f 4 -387 585 -15 -585
		mu 0 4 208 210 211 209
		f 4 -379 586 -16 -586
		mu 0 4 210 212 213 211
		f 4 -347 587 -17 -587
		mu 0 4 212 214 215 213
		f 4 -339 -572 -18 -588
		mu 0 4 214 180 183 215
		f 4 -198 588 -117 589
		mu 0 4 216 217 285 284
		f 5 -589 -222 -1147 -889 -121
		mu 0 5 285 217 218 424 425
		f 5 -238 707 -715 -885 1146
		mu 0 5 218 219 290 423 424
		f 4 -246 706 -135 -708
		mu 0 4 219 220 291 290
		f 5 -254 -1149 -937 -141 -707
		mu 0 5 220 221 421 422 291
		f 5 -262 705 -717 -933 1148
		mu 0 5 221 222 296 420 421
		f 4 -270 704 -148 -706
		mu 0 4 222 223 297 296
		f 5 -278 -1150 -961 -154 -705
		mu 0 5 223 224 418 419 297
		f 5 -286 703 -718 -957 1149
		mu 0 5 224 225 302 417 418
		f 4 -294 702 -161 -704
		mu 0 4 225 226 303 302
		f 5 -302 -1151 -985 -167 -703
		mu 0 5 226 227 415 416 303
		f 5 -310 701 -719 -981 1150
		mu 0 5 227 228 308 414 415
		f 4 -318 700 -174 -702
		mu 0 4 228 229 309 308
		f 5 -326 -1152 -1009 -180 -701
		mu 0 5 229 230 412 413 309
		f 5 -334 699 -720 -1005 1151
		mu 0 5 230 231 314 411 412
		f 4 -227 698 -187 -700
		mu 0 4 231 232 315 314
		f 5 -203 -1148 -906 -130 -699
		mu 0 5 232 233 409 410 315
		f 5 -195 -590 -716 -903 1147
		mu 0 5 233 216 284 408 409
		f 5 18 590 -709 -736 1140
		mu 0 5 1 0 234 235 236
		f 4 -58 592 20 -592
		mu 0 4 237 238 3 2
		f 5 21 -593 -711 -775 1142
		mu 0 5 4 3 238 239 240
		f 4 -71 594 23 -594
		mu 0 4 241 242 6 5
		f 5 24 -595 -712 -801 1143
		mu 0 5 7 6 242 243 244
		f 4 -84 596 26 -596
		mu 0 4 245 246 9 8
		f 5 27 -597 -713 -827 1144
		mu 0 5 10 9 246 247 248
		f 4 -97 598 29 -598
		mu 0 4 249 250 12 11
		f 5 30 -599 -714 -853 1145
		mu 0 5 13 12 250 251 252
		f 4 -110 600 32 -600
		mu 0 4 253 254 15 14
		f 5 33 -601 -710 -755 1141
		mu 0 5 16 15 254 255 256
		f 4 -45 -591 35 -602
		mu 0 4 257 234 0 17
		f 4 -48 602 42 43
		mu 0 4 19 258 259 20
		f 4 -47 44 45 -603
		mu 0 4 258 234 257 259
		f 4 36 603 -51 37
		mu 0 4 68 260 261 69
		f 4 38 39 -52 -604
		mu 0 4 260 18 21 261
		f 4 -41 604 52 53
		mu 0 4 23 262 263 24
		f 4 -42 54 55 -605
		mu 0 4 262 73 72 263
		f 4 56 605 -61 57
		mu 0 4 237 264 265 238
		f 4 58 59 -62 -606
		mu 0 4 264 22 25 265
		f 4 -63 606 65 66
		mu 0 4 27 266 267 28
		f 4 -64 67 68 -607
		mu 0 4 266 77 76 267
		f 4 69 607 -74 70
		mu 0 4 241 268 269 242
		f 4 71 72 -75 -608
		mu 0 4 268 26 29 269
		f 4 -76 608 78 79
		mu 0 4 31 270 271 32
		f 4 -77 80 81 -609
		mu 0 4 270 81 80 271
		f 4 82 609 -87 83
		mu 0 4 245 272 273 246
		f 4 84 85 -88 -610
		mu 0 4 272 30 33 273
		f 4 -89 610 91 92
		mu 0 4 35 274 275 36
		f 4 -90 93 94 -611
		mu 0 4 274 85 84 275
		f 4 95 611 -100 96
		mu 0 4 249 276 277 250
		f 4 97 98 -101 -612
		mu 0 4 276 34 37 277
		f 4 -102 612 104 105
		mu 0 4 39 278 279 40
		f 4 -103 106 107 -613
		mu 0 4 278 89 88 279
		f 4 108 613 -113 109
		mu 0 4 253 280 281 254
		f 4 110 111 -114 -614
		mu 0 4 280 38 41 281
		f 4 -120 614 114 115
		mu 0 4 43 282 283 44
		f 4 -119 116 117 -615
		mu 0 4 282 284 285 283
		f 4 121 615 -126 122
		mu 0 4 66 286 287 67
		f 4 123 124 -127 -616
		mu 0 4 286 42 45 287
		f 4 -131 616 132 133
		mu 0 4 47 288 289 48
		f 4 -132 134 135 -617
		mu 0 4 288 290 291 289
		f 4 136 617 -142 137
		mu 0 4 70 292 293 71
		f 4 138 139 -143 -618
		mu 0 4 292 46 49 293
		f 4 -144 618 145 146
		mu 0 4 51 294 295 52
		f 4 -145 147 148 -619
		mu 0 4 294 296 297 295
		f 4 149 619 -155 150
		mu 0 4 74 298 299 75
		f 4 151 152 -156 -620
		mu 0 4 298 50 53 299
		f 4 -157 620 158 159
		mu 0 4 55 300 301 56
		f 4 -158 160 161 -621
		mu 0 4 300 302 303 301
		f 4 162 621 -168 163
		mu 0 4 78 304 305 79
		f 4 164 165 -169 -622
		mu 0 4 304 54 57 305
		f 4 -170 622 171 172
		mu 0 4 59 306 307 60
		f 4 -171 173 174 -623
		mu 0 4 306 308 309 307
		f 4 175 623 -181 176
		mu 0 4 82 310 311 83
		f 4 177 178 -182 -624
		mu 0 4 310 58 61 311
		f 4 -183 624 184 185
		mu 0 4 63 312 313 64
		f 4 -184 186 187 -625
		mu 0 4 312 314 315 313
		f 4 188 625 -129 189
		mu 0 4 86 316 317 87
		f 4 190 191 -128 -626
		mu 0 4 316 62 65 317
		f 4 -199 626 192 193
		mu 0 4 91 318 319 92
		f 4 -197 194 195 -627
		mu 0 4 318 216 233 319
		f 4 -193 627 200 201
		mu 0 4 92 319 320 96
		f 4 -196 202 203 -628
		mu 0 4 319 233 232 320
		f 4 -211 628 204 205
		mu 0 4 90 321 322 94
		f 4 -209 206 207 -629
		mu 0 4 321 645 644 322
		f 4 208 629 -213 209
		mu 0 4 645 321 323 612
		f 4 210 211 -215 -630
		mu 0 4 321 90 93 323
		f 4 -205 630 216 217
		mu 0 4 94 322 324 98
		f 4 -208 218 219 -631
		mu 0 4 322 644 642 324
		f 4 196 631 -221 197
		mu 0 4 216 318 325 217
		f 4 198 199 -223 -632
		mu 0 4 318 91 95 325
		f 4 -201 632 224 225
		mu 0 4 96 320 326 125
		f 4 -204 226 227 -633
		mu 0 4 320 232 231 326
		f 4 212 633 -229 213
		mu 0 4 612 323 327 643
		f 4 214 215 -231 -634
		mu 0 4 323 93 97 327
		f 4 -217 634 232 233
		mu 0 4 98 324 328 100
		f 4 -220 234 235 -635
		mu 0 4 324 642 165 328
		f 4 220 635 -237 221
		mu 0 4 217 325 329 218
		f 4 222 223 -239 -636
		mu 0 4 325 95 99 329
		f 4 -233 636 240 241
		mu 0 4 100 328 330 102
		f 4 -236 242 243 -637
		mu 0 4 328 165 166 330
		f 4 236 637 -245 237
		mu 0 4 218 329 331 219
		f 4 238 239 -247 -638
		mu 0 4 329 99 101 331
		f 4 -241 638 248 249
		mu 0 4 102 330 332 104
		f 4 -244 250 251 -639
		mu 0 4 330 166 641 332
		f 4 244 639 -253 245
		mu 0 4 219 331 333 220
		f 4 246 247 -255 -640
		mu 0 4 331 101 103 333
		f 4 -249 640 256 257
		mu 0 4 104 332 334 106
		f 4 -252 258 259 -641
		mu 0 4 332 641 640 334
		f 4 252 641 -261 253
		mu 0 4 220 333 335 221
		f 4 254 255 -263 -642
		mu 0 4 333 103 105 335
		f 4 -257 642 264 265
		mu 0 4 106 334 336 108
		f 4 -260 266 267 -643
		mu 0 4 334 640 639 336
		f 4 260 643 -269 261
		mu 0 4 221 335 337 222
		f 4 262 263 -271 -644
		mu 0 4 335 105 107 337
		f 4 -265 644 272 273
		mu 0 4 108 336 338 110
		f 4 -268 274 275 -645
		mu 0 4 336 639 638 338
		f 4 268 645 -277 269
		mu 0 4 222 337 339 223
		f 4 270 271 -279 -646
		mu 0 4 337 107 109 339
		f 4 -273 646 280 281
		mu 0 4 110 338 340 112
		f 4 -276 282 283 -647
		mu 0 4 338 638 637 340
		f 4 276 647 -285 277
		mu 0 4 223 339 341 224
		f 4 278 279 -287 -648
		mu 0 4 339 109 111 341
		f 4 -281 648 288 289
		mu 0 4 112 340 342 114
		f 4 -284 290 291 -649
		mu 0 4 340 637 636 342
		f 4 284 649 -293 285
		mu 0 4 224 341 343 225
		f 4 286 287 -295 -650
		mu 0 4 341 111 113 343
		f 4 -289 650 296 297
		mu 0 4 114 342 344 116
		f 4 -292 298 299 -651
		mu 0 4 342 636 635 344
		f 4 292 651 -301 293
		mu 0 4 225 343 345 226
		f 4 294 295 -303 -652
		mu 0 4 343 113 115 345
		f 4 -297 652 304 305
		mu 0 4 116 344 346 118
		f 4 -300 306 307 -653
		mu 0 4 344 635 634 346
		f 4 300 653 -309 301
		mu 0 4 226 345 347 227
		f 4 302 303 -311 -654
		mu 0 4 345 115 117 347
		f 4 -305 654 312 313
		mu 0 4 118 346 348 120
		f 4 -308 314 315 -655
		mu 0 4 346 634 633 348
		f 4 308 655 -317 309
		mu 0 4 227 347 349 228
		f 4 310 311 -319 -656
		mu 0 4 347 117 119 349
		f 4 -313 656 320 321
		mu 0 4 120 348 350 122
		f 4 -316 322 323 -657
		mu 0 4 348 633 631 350
		f 4 316 657 -325 317
		mu 0 4 228 349 351 229
		f 4 318 319 -327 -658
		mu 0 4 349 119 121 351
		f 4 -321 658 328 329
		mu 0 4 122 350 352 124
		f 4 -324 330 331 -659
		mu 0 4 350 631 632 352
		f 4 324 659 -333 325
		mu 0 4 229 351 353 230
		f 4 326 327 -335 -660
		mu 0 4 351 121 123 353
		f 4 228 660 -332 229
		mu 0 4 643 327 352 632
		f 4 230 231 -329 -661
		mu 0 4 327 97 124 352
		f 4 332 661 -228 333
		mu 0 4 230 353 326 231
		f 4 334 335 -225 -662
		mu 0 4 353 123 125 326
		f 4 -343 662 336 337
		mu 0 4 127 354 355 128
		f 4 -341 338 339 -663
		mu 0 4 354 180 214 355
		f 4 -337 663 344 345
		mu 0 4 128 355 356 134
		f 4 -340 346 347 -664
		mu 0 4 355 214 212 356
		f 4 -355 664 348 349
		mu 0 4 126 357 358 130
		f 4 -353 350 351 -665
		mu 0 4 357 630 614 358
		f 4 352 665 -357 353
		mu 0 4 630 357 361 629
		f 4 354 355 -359 -666
		mu 0 4 357 126 129 361
		f 4 -349 666 360 361
		mu 0 4 130 358 363 132
		f 4 -352 362 363 -667
		mu 0 4 358 614 628 363
		f 4 340 667 -365 341
		mu 0 4 180 354 365 181
		f 4 342 343 -367 -668
		mu 0 4 354 127 131 365
		f 4 -361 668 368 369
		mu 0 4 132 363 366 161
		f 4 -364 370 371 -669
		mu 0 4 363 628 616 366
		f 4 364 669 -373 365
		mu 0 4 181 365 368 184
		f 4 366 367 -375 -670
		mu 0 4 365 131 133 368
		f 4 -345 670 376 377
		mu 0 4 134 356 369 136
		f 4 -348 378 379 -671
		mu 0 4 356 212 210 369
		f 4 356 671 -381 357
		mu 0 4 629 361 370 627
		f 4 358 359 -383 -672
		mu 0 4 361 129 135 370
		f 4 -377 672 384 385
		mu 0 4 136 369 372 138
		f 4 -380 386 387 -673
		mu 0 4 369 210 208 372
		f 4 380 673 -389 381
		mu 0 4 627 370 373 374
		f 4 382 383 -391 -674
		mu 0 4 370 135 137 373
		f 4 -385 674 392 393
		mu 0 4 138 372 375 140
		f 4 -388 394 395 -675
		mu 0 4 372 208 206 375
		f 4 388 675 -397 389
		mu 0 4 374 373 376 377
		f 4 390 391 -399 -676
		mu 0 4 373 137 139 376
		f 4 -393 676 400 401
		mu 0 4 140 375 378 142
		f 4 -396 402 403 -677
		mu 0 4 375 206 204 378
		f 4 396 677 -405 397
		mu 0 4 377 376 379 626
		f 4 398 399 -407 -678
		mu 0 4 376 139 141 379
		f 4 -401 678 408 409
		mu 0 4 142 378 381 144
		f 4 -404 410 411 -679
		mu 0 4 378 204 202 381
		f 4 404 679 -413 405
		mu 0 4 626 379 382 625
		f 4 406 407 -415 -680
		mu 0 4 379 141 143 382
		f 4 -409 680 416 417
		mu 0 4 144 381 384 146
		f 4 -412 418 419 -681
		mu 0 4 381 202 200 384
		f 4 412 681 -421 413
		mu 0 4 625 382 385 624
		f 4 414 415 -423 -682
		mu 0 4 382 143 145 385
		f 4 -417 682 424 425
		mu 0 4 146 384 387 148
		f 4 -420 426 427 -683
		mu 0 4 384 200 198 387
		f 4 420 683 -429 421
		mu 0 4 624 385 388 623
		f 4 422 423 -431 -684
		mu 0 4 385 145 147 388
		f 4 -425 684 432 433
		mu 0 4 148 387 390 150
		f 4 -428 434 435 -685
		mu 0 4 387 198 196 390
		f 4 428 685 -437 429
		mu 0 4 623 388 391 622
		f 4 430 431 -439 -686
		mu 0 4 388 147 149 391
		f 4 -433 686 440 441
		mu 0 4 150 390 393 152
		f 4 -436 442 443 -687
		mu 0 4 390 196 194 393
		f 4 436 687 -445 437
		mu 0 4 622 391 394 621
		f 4 438 439 -447 -688
		mu 0 4 391 149 151 394
		f 4 -441 688 448 449
		mu 0 4 152 393 396 154
		f 4 -444 450 451 -689
		mu 0 4 393 194 192 396
		f 4 444 689 -453 445
		mu 0 4 621 394 397 620
		f 4 446 447 -455 -690
		mu 0 4 394 151 153 397
		f 4 -449 690 456 457
		mu 0 4 154 396 399 156
		f 4 -452 458 459 -691
		mu 0 4 396 192 190 399
		f 4 452 691 -461 453
		mu 0 4 620 397 400 619
		f 4 454 455 -463 -692
		mu 0 4 397 153 155 400
		f 4 -457 692 464 465
		mu 0 4 156 399 402 158
		f 4 -460 466 467 -693
		mu 0 4 399 190 188 402
		f 4 460 693 -469 461
		mu 0 4 619 400 403 618
		f 4 462 463 -471 -694
		mu 0 4 400 155 157 403
		f 4 -465 694 472 473
		mu 0 4 158 402 405 160
		f 4 -468 474 475 -695
		mu 0 4 402 188 186 405
		f 4 468 695 -477 469
		mu 0 4 618 403 406 617
		f 4 470 471 -479 -696
		mu 0 4 403 157 159 406
		f 4 372 696 -476 373
		mu 0 4 184 368 405 186
		f 4 374 375 -473 -697
		mu 0 4 368 133 160 405
		f 4 476 697 -372 477
		mu 0 4 617 406 366 616
		f 4 478 479 -369 -698
		mu 0 4 406 159 161 366
		f 4 726 727 728 729
		mu 0 4 426 427 428 429
		f 4 730 731 732 -728
		mu 0 4 427 430 431 428
		f 4 739 740 741 742
		mu 0 4 432 433 434 435
		f 4 743 744 745 -741
		mu 0 4 433 436 437 434
		f 4 752 753 754 755
		mu 0 4 438 439 256 255
		f 4 756 757 758 -754
		mu 0 4 439 440 441 256
		f 4 765 766 767 768
		mu 0 4 442 443 444 445
		f 4 769 770 771 -767
		mu 0 4 443 446 447 444
		f 4 778 779 780 781
		mu 0 4 448 449 450 451
		f 4 782 783 784 -780
		mu 0 4 449 452 453 450
		f 4 791 792 793 794
		mu 0 4 454 455 456 457
		f 4 795 796 797 -793
		mu 0 4 455 458 459 456
		f 4 804 805 806 807
		mu 0 4 460 461 462 463
		f 4 808 809 810 -806
		mu 0 4 461 464 465 462
		f 4 817 818 819 820
		mu 0 4 466 467 468 469
		f 4 821 822 823 -819
		mu 0 4 467 470 471 468
		f 4 830 831 832 833
		mu 0 4 472 473 474 475
		f 4 834 835 836 -832
		mu 0 4 473 476 477 474
		f 4 843 844 845 846
		mu 0 4 478 479 480 481
		f 4 847 848 849 -845
		mu 0 4 479 482 483 480
		f 4 856 857 858 859
		mu 0 4 484 485 486 487
		f 4 860 861 862 -858
		mu 0 4 485 488 489 486
		f 4 867 868 869 870
		mu 0 4 490 491 492 493
		f 4 871 872 873 -869
		mu 0 4 491 494 495 492
		f 4 882 883 884 885
		mu 0 4 496 497 424 423
		f 4 886 887 888 -884
		mu 0 4 497 498 425 424
		f 4 895 896 897 898
		mu 0 4 499 500 501 502
		f 4 899 900 901 -897
		mu 0 4 500 503 504 501
		f 4 906 907 908 909
		mu 0 4 505 506 507 508
		f 4 910 911 912 -908
		mu 0 4 506 509 510 507
		f 4 917 918 919 920
		mu 0 4 511 512 513 514
		f 4 921 922 923 -919
		mu 0 4 512 515 516 513
		f 4 930 931 932 933
		mu 0 4 517 518 421 420
		f 4 934 935 936 -932
		mu 0 4 518 519 422 421
		f 4 941 942 943 944
		mu 0 4 520 521 522 523
		f 4 945 946 947 -943
		mu 0 4 521 524 525 522
		f 4 954 955 956 957
		mu 0 4 526 527 418 417
		f 4 958 959 960 -956
		mu 0 4 527 528 419 418
		f 4 965 966 967 968
		mu 0 4 529 530 531 532
		f 4 969 970 971 -967
		mu 0 4 530 533 534 531
		f 4 978 979 980 981
		mu 0 4 535 536 415 414
		f 4 982 983 984 -980
		mu 0 4 536 537 416 415
		f 4 989 990 991 992
		mu 0 4 538 539 540 541
		f 4 993 994 995 -991
		mu 0 4 539 542 543 540
		f 4 1002 1003 1004 1005
		mu 0 4 544 545 412 411
		f 4 1006 1007 1008 -1004
		mu 0 4 545 546 413 412
		f 4 1013 1014 1015 1016
		mu 0 4 547 548 549 550
		f 4 1017 1018 1019 -1015
		mu 0 4 548 551 552 549
		f 4 480 1020 -721 1021
		mu 0 4 19 18 553 437
		f 4 -722 1022 482 1023
		mu 0 4 435 554 23 22
		f 4 -484 1024 -760 1025
		mu 0 4 25 24 555 453
		f 4 -761 1026 484 1027
		mu 0 4 451 556 27 26
		f 4 -486 1028 -786 1029
		mu 0 4 29 28 557 465
		f 4 -787 1030 486 1031
		mu 0 4 463 558 31 30
		f 4 -488 1032 -812 1033
		mu 0 4 33 32 559 477
		f 4 -813 1034 488 1035
		mu 0 4 475 560 35 34
		f 4 -490 1036 -838 1037
		mu 0 4 37 36 561 489
		f 4 -839 1038 490 1039
		mu 0 4 487 562 39 38
		f 4 -492 1040 -748 1041
		mu 0 4 41 40 563 564
		f 4 -747 1042 -482 1043
		mu 0 4 565 566 21 20
		f 4 -493 1044 -890 1045
		mu 0 4 43 42 567 510
		f 4 -494 1046 -877 1047
		mu 0 4 45 44 568 516
		f 4 -878 1048 494 1049
		mu 0 4 514 569 47 46
		f 4 -496 1050 -925 1051
		mu 0 4 49 48 570 525
		f 4 -926 1052 496 1053
		mu 0 4 523 571 51 50
		f 4 -498 1054 -949 1055
		mu 0 4 53 52 572 534
		f 4 -950 1056 498 1057
		mu 0 4 532 573 55 54
		f 4 -500 1058 -973 1059
		mu 0 4 57 56 574 543
		f 4 -974 1060 500 1061
		mu 0 4 541 575 59 58
		f 4 -502 1062 -997 1063
		mu 0 4 61 60 576 552
		f 4 -998 1064 502 1065
		mu 0 4 550 577 63 62
		f 4 -504 1066 -891 1067
		mu 0 4 65 64 508 578
		f 4 1068 -735 1069 -505
		mu 0 4 67 579 431 68
		f 4 1070 506 1071 -734
		mu 0 4 580 70 73 429
		f 4 1072 -774 1073 -508
		mu 0 4 71 581 447 72
		f 4 1074 508 1075 -773
		mu 0 4 582 74 77 445
		f 4 1076 -800 1077 -510
		mu 0 4 75 583 459 76
		f 4 1078 510 1079 -799
		mu 0 4 584 78 81 457
		f 4 1080 -826 1081 -512
		mu 0 4 79 585 471 80
		f 4 1082 512 1083 -825
		mu 0 4 586 82 85 469
		f 4 1084 -852 1085 -514
		mu 0 4 83 587 483 84
		f 4 1086 514 1087 -851
		mu 0 4 588 86 89 481
		f 4 1088 -876 1089 -516
		mu 0 4 87 502 495 88
		f 4 1090 -506 1091 -875
		mu 0 4 504 66 69 493
		f 4 -39 1092 -726 -1021
		mu 0 4 18 260 430 553
		f 4 -37 -1070 -732 -1093
		mu 0 4 260 68 431 430
		f 4 -724 1093 40 -1023
		mu 0 4 554 426 262 23
		f 4 -730 -1072 41 -1094
		mu 0 4 426 429 73 262
		f 4 46 1094 -737 708
		mu 0 4 234 258 436 235
		f 4 47 -1022 -745 -1095
		mu 0 4 258 19 437 436
		f 4 -43 1095 -752 -1044
		mu 0 4 20 259 440 565
		f 4 -46 49 -758 -1096
		mu 0 4 259 257 441 440
		f 4 -738 1096 -57 48
		mu 0 4 589 432 264 237
		f 4 -743 -1024 -59 -1097
		mu 0 4 432 435 22 264
		f 4 -53 1097 -765 -1025
		mu 0 4 24 263 446 555
		f 4 -56 -1074 -771 -1098
		mu 0 4 263 72 447 446
		f 4 -763 1098 62 -1027
		mu 0 4 556 442 266 27
		f 4 -769 -1076 63 -1099
		mu 0 4 442 445 77 266
		f 4 60 1099 -776 710
		mu 0 4 238 265 452 239
		f 4 61 -1026 -784 -1100
		mu 0 4 265 25 453 452
		f 4 -777 1100 -70 64
		mu 0 4 590 448 268 241
		f 4 -782 -1028 -72 -1101
		mu 0 4 448 451 26 268
		f 4 -66 1101 -791 -1029
		mu 0 4 28 267 458 557
		f 4 -69 -1078 -797 -1102
		mu 0 4 267 76 459 458
		f 4 -789 1102 75 -1031
		mu 0 4 558 454 270 31
		f 4 -795 -1080 76 -1103
		mu 0 4 454 457 81 270
		f 4 73 1103 -802 711
		mu 0 4 242 269 464 243
		f 4 74 -1030 -810 -1104
		mu 0 4 269 29 465 464
		f 4 -803 1104 -83 77
		mu 0 4 591 460 272 245
		f 4 -808 -1032 -85 -1105
		mu 0 4 460 463 30 272
		f 4 -79 1105 -817 -1033
		mu 0 4 32 271 470 559
		f 4 -82 -1082 -823 -1106
		mu 0 4 271 80 471 470
		f 4 -815 1106 88 -1035
		mu 0 4 560 466 274 35
		f 4 -821 -1084 89 -1107
		mu 0 4 466 469 85 274
		f 4 86 1107 -828 712
		mu 0 4 246 273 476 247
		f 4 87 -1034 -836 -1108
		mu 0 4 273 33 477 476
		f 4 -829 1108 -96 90
		mu 0 4 592 472 276 249
		f 4 -834 -1036 -98 -1109
		mu 0 4 472 475 34 276
		f 4 -92 1109 -843 -1037
		mu 0 4 36 275 482 561
		f 4 -95 -1086 -849 -1110
		mu 0 4 275 84 483 482
		f 4 -841 1110 101 -1039
		mu 0 4 562 478 278 39
		f 4 -847 -1088 102 -1111
		mu 0 4 478 481 89 278
		f 4 99 1111 -854 713
		mu 0 4 250 277 488 251
		f 4 100 -1038 -862 -1112
		mu 0 4 277 37 489 488
		f 4 -855 1112 -109 103
		mu 0 4 593 484 280 253
		f 4 -860 -1040 -111 -1113
		mu 0 4 484 487 38 280
		f 4 -105 1113 -867 -1041
		mu 0 4 40 279 494 563
		f 4 -108 -1090 -873 -1114
		mu 0 4 279 88 495 494
		f 4 50 1114 -871 -1092
		mu 0 4 69 261 490 493
		f 4 51 -1043 -865 -1115
		mu 0 4 261 21 566 490
		f 4 112 1115 -756 709
		mu 0 4 254 281 438 255
		f 4 113 -1042 -750 -1116
		mu 0 4 281 41 564 438
		f 4 -115 1116 -882 -1047
		mu 0 4 44 283 498 568
		f 4 -118 120 -888 -1117
		mu 0 4 283 285 425 498
		f 4 -124 1117 -895 -1045
		mu 0 4 42 286 503 567
		f 4 -122 -1091 -901 -1118
		mu 0 4 286 66 504 503
		f 4 -893 1118 127 -1068
		mu 0 4 578 499 317 65
		f 4 -899 -1089 128 -1119
		mu 0 4 499 502 87 317
		f 4 118 1119 -904 715
		mu 0 4 284 282 509 408
		f 4 119 -1046 -912 -1120
		mu 0 4 282 43 510 509
		f 4 -880 1120 130 -1049
		mu 0 4 569 496 288 47
		f 4 -886 714 131 -1121
		mu 0 4 496 423 290 288
		f 4 125 1121 -915 -1069
		mu 0 4 67 287 515 579
		f 4 126 -1048 -923 -1122
		mu 0 4 287 45 516 515
		f 4 -916 1122 -137 -1071
		mu 0 4 580 511 292 70
		f 4 -921 -1050 -139 -1123
		mu 0 4 511 514 46 292
		f 4 -133 1123 -930 -1051
		mu 0 4 48 289 519 570
		f 4 -136 140 -936 -1124
		mu 0 4 289 291 422 519
		f 4 -928 1124 143 -1053
		mu 0 4 571 517 294 51
		f 4 -934 716 144 -1125
		mu 0 4 517 420 296 294
		f 4 141 1125 -939 -1073
		mu 0 4 71 293 524 581
		f 4 142 -1052 -947 -1126
		mu 0 4 293 49 525 524
		f 4 -940 1126 -150 -1075
		mu 0 4 582 520 298 74
		f 4 -945 -1054 -152 -1127
		mu 0 4 520 523 50 298
		f 4 -146 1127 -954 -1055
		mu 0 4 52 295 528 572
		f 4 -149 153 -960 -1128
		mu 0 4 295 297 419 528
		f 4 -952 1128 156 -1057
		mu 0 4 573 526 300 55
		f 4 -958 717 157 -1129
		mu 0 4 526 417 302 300
		f 4 154 1129 -963 -1077
		mu 0 4 75 299 533 583
		f 4 155 -1056 -971 -1130
		mu 0 4 299 53 534 533
		f 4 -964 1130 -163 -1079
		mu 0 4 584 529 304 78
		f 4 -969 -1058 -165 -1131
		mu 0 4 529 532 54 304
		f 4 -159 1131 -978 -1059
		mu 0 4 56 301 537 574
		f 4 -162 166 -984 -1132
		mu 0 4 301 303 416 537
		f 4 -976 1132 169 -1061
		mu 0 4 575 535 306 59
		f 4 -982 718 170 -1133
		mu 0 4 535 414 308 306
		f 4 167 1133 -987 -1081
		mu 0 4 79 305 542 585
		f 4 168 -1060 -995 -1134
		mu 0 4 305 57 543 542
		f 4 -988 1134 -176 -1083
		mu 0 4 586 538 310 82
		f 4 -993 -1062 -178 -1135
		mu 0 4 538 541 58 310
		f 4 -172 1135 -1002 -1063
		mu 0 4 60 307 546 576
		f 4 -175 179 -1008 -1136
		mu 0 4 307 309 413 546
		f 4 -1000 1136 182 -1065
		mu 0 4 577 544 312 63
		f 4 -1006 719 183 -1137
		mu 0 4 544 411 314 312
		f 4 180 1137 -1011 -1085
		mu 0 4 83 311 551 587
		f 4 181 -1064 -1019 -1138
		mu 0 4 311 61 552 551
		f 4 -1012 1138 -189 -1087
		mu 0 4 588 547 316 86
		f 4 -1017 -1066 -191 -1139
		mu 0 4 547 550 62 316
		f 4 -905 1139 -188 129
		mu 0 4 410 505 313 315
		f 4 -910 -1067 -185 -1140
		mu 0 4 505 508 64 313
		f 5 -1141 -739 -49 591 19
		mu 0 5 1 236 589 237 2
		f 5 -1142 -759 -50 601 34
		mu 0 5 16 256 441 257 17
		f 5 -1143 -778 -65 593 22
		mu 0 5 4 240 590 241 5
		f 5 -1144 -804 -78 595 25
		mu 0 5 7 244 591 245 8
		f 5 -1145 -830 -91 597 28
		mu 0 5 10 248 592 249 11
		f 5 -1146 -856 -104 599 31
		mu 0 5 13 252 593 253 14
		f 4 722 1152 -727 723
		mu 0 4 554 594 427 426;
	setAttr ".fc[500:582]"
		f 4 724 725 -731 -1153
		mu 0 4 594 553 430 427
		f 4 -744 1153 735 736
		mu 0 4 436 433 236 235
		f 4 -740 737 738 -1154
		mu 0 4 433 432 589 236
		f 4 -725 1154 -746 720
		mu 0 4 553 594 434 437
		f 4 -723 721 -742 -1155
		mu 0 4 594 554 435 434
		f 4 748 1155 -753 749
		mu 0 4 564 595 439 438
		f 4 750 751 -757 -1156
		mu 0 4 595 565 440 439
		f 4 761 1156 -766 762
		mu 0 4 556 596 443 442
		f 4 763 764 -770 -1157
		mu 0 4 596 555 446 443
		f 4 -783 1157 774 775
		mu 0 4 452 449 240 239
		f 4 -779 776 777 -1158
		mu 0 4 449 448 590 240
		f 4 -764 1158 -785 759
		mu 0 4 555 596 450 453
		f 4 -762 760 -781 -1159
		mu 0 4 596 556 451 450
		f 4 787 1159 -792 788
		mu 0 4 558 597 455 454
		f 4 789 790 -796 -1160
		mu 0 4 597 557 458 455
		f 4 -809 1160 800 801
		mu 0 4 464 461 244 243
		f 4 -805 802 803 -1161
		mu 0 4 461 460 591 244
		f 4 -790 1161 -811 785
		mu 0 4 557 597 462 465
		f 4 -788 786 -807 -1162
		mu 0 4 597 558 463 462
		f 4 813 1162 -818 814
		mu 0 4 560 598 467 466
		f 4 815 816 -822 -1163
		mu 0 4 598 559 470 467
		f 4 -835 1163 826 827
		mu 0 4 476 473 248 247
		f 4 -831 828 829 -1164
		mu 0 4 473 472 592 248
		f 4 -816 1164 -837 811
		mu 0 4 559 598 474 477
		f 4 -814 812 -833 -1165
		mu 0 4 598 560 475 474
		f 4 839 1165 -844 840
		mu 0 4 562 599 479 478
		f 4 841 842 -848 -1166
		mu 0 4 599 561 482 479
		f 4 -861 1166 852 853
		mu 0 4 488 485 252 251
		f 4 -857 854 855 -1167
		mu 0 4 485 484 593 252
		f 4 -842 1167 -863 837
		mu 0 4 561 599 486 489
		f 4 -840 838 -859 -1168
		mu 0 4 599 562 487 486
		f 4 -751 1168 -864 746
		mu 0 4 565 595 600 566
		f 4 -749 747 -866 -1169
		mu 0 4 595 564 563 600
		f 4 863 1169 -868 864
		mu 0 4 566 600 491 490
		f 4 865 866 -872 -1170
		mu 0 4 600 563 494 491
		f 4 878 1170 -883 879
		mu 0 4 569 601 497 496
		f 4 880 881 -887 -1171
		mu 0 4 601 568 498 497
		f 4 891 1171 -896 892
		mu 0 4 578 602 500 499
		f 4 893 894 -900 -1172
		mu 0 4 602 567 503 500
		f 4 -870 1172 -902 874
		mu 0 4 493 492 501 504
		f 4 -874 875 -898 -1173
		mu 0 4 492 495 502 501
		f 4 -911 1173 902 903
		mu 0 4 509 506 409 408
		f 4 -907 904 905 -1174
		mu 0 4 506 505 410 409
		f 4 -894 1174 -913 889
		mu 0 4 567 602 507 510
		f 4 -892 890 -909 -1175
		mu 0 4 602 578 508 507
		f 4 -922 1175 913 914
		mu 0 4 515 512 603 579
		f 4 -918 915 916 -1176
		mu 0 4 512 511 580 603
		f 4 -729 1176 -917 733
		mu 0 4 429 428 603 580
		f 4 -733 734 -914 -1177
		mu 0 4 428 431 579 603
		f 4 -881 1177 -924 876
		mu 0 4 568 601 513 516
		f 4 -879 877 -920 -1178
		mu 0 4 601 569 514 513
		f 4 926 1178 -931 927
		mu 0 4 571 604 518 517
		f 4 928 929 -935 -1179
		mu 0 4 604 570 519 518
		f 4 -946 1179 937 938
		mu 0 4 524 521 605 581
		f 4 -942 939 940 -1180
		mu 0 4 521 520 582 605
		f 4 -768 1180 -941 772
		mu 0 4 445 444 605 582
		f 4 -772 773 -938 -1181
		mu 0 4 444 447 581 605
		f 4 -929 1181 -948 924
		mu 0 4 570 604 522 525
		f 4 -927 925 -944 -1182
		mu 0 4 604 571 523 522
		f 4 950 1182 -955 951
		mu 0 4 573 606 527 526
		f 4 952 953 -959 -1183
		mu 0 4 606 572 528 527
		f 4 -970 1183 961 962
		mu 0 4 533 530 607 583
		f 4 -966 963 964 -1184
		mu 0 4 530 529 584 607
		f 4 -794 1184 -965 798
		mu 0 4 457 456 607 584
		f 4 -798 799 -962 -1185
		mu 0 4 456 459 583 607
		f 4 -953 1185 -972 948
		mu 0 4 572 606 531 534
		f 4 -951 949 -968 -1186
		mu 0 4 606 573 532 531
		f 4 974 1186 -979 975
		mu 0 4 575 608 536 535
		f 4 976 977 -983 -1187
		mu 0 4 608 574 537 536
		f 4 -994 1187 985 986
		mu 0 4 542 539 609 585
		f 4 -990 987 988 -1188
		mu 0 4 539 538 586 609
		f 4 -820 1188 -989 824
		mu 0 4 469 468 609 586
		f 4 -824 825 -986 -1189
		mu 0 4 468 471 585 609
		f 4 -977 1189 -996 972
		mu 0 4 574 608 540 543
		f 4 -975 973 -992 -1190
		mu 0 4 608 575 541 540
		f 4 998 1190 -1003 999
		mu 0 4 577 610 545 544
		f 4 1000 1001 -1007 -1191
		mu 0 4 610 576 546 545
		f 4 -1018 1191 1009 1010
		mu 0 4 551 548 611 587
		f 4 -1014 1011 1012 -1192
		mu 0 4 548 547 588 611
		f 4 -846 1192 -1013 850
		mu 0 4 481 480 611 588
		f 4 -850 851 -1010 -1193
		mu 0 4 480 483 587 611
		f 4 -1001 1193 -1020 996
		mu 0 4 576 610 549 552
		f 4 -999 997 -1016 -1194
		mu 0 4 610 577 550 549;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".db" yes;
	setAttr ".vbc" no;
	setAttr ".vs" 8;
	setAttr ".usz" 8;
	setAttr ".bw" 4;
	setAttr ".dr" 1;
	setAttr ".vnm" 0;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode polySoftEdge -n "polySoftEdge12";
	rename -uid "46B966E0-4761-34FF-2A99-CBB1782D7573";
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
connectAttr "polySoftEdge12.out" "Screw_LShape.i";
connectAttr "polySurfaceShape26.o" "polySoftEdge12.ip";
connectAttr "Screw_LShape.wm" "polySoftEdge12.mp";
connectAttr "Screw_LShape.iog" ":initialShadingGroup.dsm" -na;
// End of Screw_L.ma
