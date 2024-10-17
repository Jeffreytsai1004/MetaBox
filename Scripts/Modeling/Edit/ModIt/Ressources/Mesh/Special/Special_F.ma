//Maya ASCII 2023 scene
//Name: Special_F.ma
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
fileInfo "UUID" "E7F75240-4436-5547-5BB0-C19D516AF97D";
createNode transform -n "Special_F";
	rename -uid "89DBF281-4EE3-130B-C91F-D3A748F11728";
createNode mesh -n "Special_FShape" -p "Special_F";
	rename -uid "BE592C24-4EA3-6D33-BC81-E39AF1A6DF9C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.46763426065444946 0.76747080683708191 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr -s 729 ".pt";
	setAttr ".pt[1]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[2]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[4]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[6]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[7]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[8]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[9]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[10]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[11]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[12]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[13]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[14]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[15]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[16]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[17]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[18]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[19]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[21]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[22]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[25]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[27]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[28]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[30]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[32]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[33]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[34]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[35]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[36]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[38]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[39]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[40]" -type "float3" -2.9802322e-08 0 4.6566129e-10 ;
	setAttr ".pt[41]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[42]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[43]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[44]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[45]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[46]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[47]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[48]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[49]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[51]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[54]" -type "float3" 5.8207661e-11 0 5.9604645e-08 ;
	setAttr ".pt[55]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[56]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[58]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[60]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[61]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[62]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[63]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[64]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[65]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[67]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[68]" -type "float3" 2.9802322e-08 0 -1.4901161e-08 ;
	setAttr ".pt[69]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[70]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[72]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[73]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[75]" -type "float3" 2.9802322e-08 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[76]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[77]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[78]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[79]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[80]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[81]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[82]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[83]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[84]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[85]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[86]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[87]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[88]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[89]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[90]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[91]" -type "float3" 0 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[92]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[93]" -type "float3" 5.9604645e-08 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[94]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[95]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[96]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[97]" -type "float3" -5.9604645e-08 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[99]" -type "float3" 0 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[101]" -type "float3" 1.4901161e-08 1.4901161e-08 0 ;
	setAttr ".pt[103]" -type "float3" 0 1.4901161e-08 5.9604645e-08 ;
	setAttr ".pt[104]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[105]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[106]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[107]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[108]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[109]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[110]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[111]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[112]" -type "float3" -1.4901161e-08 1.4901161e-08 0 ;
	setAttr ".pt[113]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[114]" -type "float3" -1.4901161e-08 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[115]" -type "float3" 0 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[116]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[117]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[118]" -type "float3" -1.8626451e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[119]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[120]" -type "float3" 0 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[121]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[122]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[123]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[124]" -type "float3" 7.4505806e-09 1.4901161e-08 0 ;
	setAttr ".pt[125]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[126]" -type "float3" -1.8626451e-09 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[127]" -type "float3" 1.8626451e-09 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[128]" -type "float3" -1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[129]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[130]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[131]" -type "float3" 1.8626451e-09 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[132]" -type "float3" 1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[133]" -type "float3" 3.6379788e-12 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[134]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[136]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[137]" -type "float3" 1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[138]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[139]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[140]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[141]" -type "float3" 5.9604645e-08 -1.4901161e-08 0 ;
	setAttr ".pt[142]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[143]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[145]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[147]" -type "float3" -2.9802322e-08 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[148]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[149]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[151]" -type "float3" 0 -1.4901161e-08 5.9604645e-08 ;
	setAttr ".pt[152]" -type "float3" 0 0 5.9604645e-08 ;
	setAttr ".pt[153]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[155]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[156]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[157]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[158]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[159]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[161]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[162]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[163]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[165]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[166]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[167]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[169]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[170]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[171]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[172]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[173]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[174]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[175]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[176]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[177]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[178]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[179]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[182]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[183]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[184]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[185]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[186]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[187]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[188]" -type "float3" -1.4901161e-08 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[189]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[190]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[191]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[192]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[194]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[195]" -type "float3" -1.8626451e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[196]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[198]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[199]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[200]" -type "float3" 0 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[201]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[202]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[204]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[206]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[207]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[208]" -type "float3" 7.4505806e-09 -1.4901161e-08 0 ;
	setAttr ".pt[209]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[211]" -type "float3" -1.8626451e-09 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[212]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[213]" -type "float3" 1.8626451e-09 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[214]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[215]" -type "float3" -1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[216]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[217]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[218]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[219]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[221]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[222]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[223]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[224]" -type "float3" 1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[225]" -type "float3" 3.6379788e-12 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[226]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[227]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[228]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[229]" -type "float3" 0 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[230]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[231]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[232]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[233]" -type "float3" 2.9802322e-08 1.4901161e-08 0 ;
	setAttr ".pt[234]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[235]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[236]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[237]" -type "float3" -2.9802322e-08 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[238]" -type "float3" -5.9604645e-08 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[239]" -type "float3" -5.9604645e-08 1.4901161e-08 2.3283064e-10 ;
	setAttr ".pt[240]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[241]" -type "float3" -2.9802322e-08 1.4901161e-08 0 ;
	setAttr ".pt[242]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[243]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[244]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[245]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[246]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[247]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[248]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[249]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[250]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[251]" -type "float3" -1.4901161e-08 1.4901161e-08 0 ;
	setAttr ".pt[252]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[253]" -type "float3" -1.4901161e-08 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[254]" -type "float3" 0 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[255]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[256]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[257]" -type "float3" -1.8626451e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[258]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[259]" -type "float3" 0 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[260]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[261]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[262]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[263]" -type "float3" 7.4505806e-09 1.4901161e-08 0 ;
	setAttr ".pt[264]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[265]" -type "float3" -1.8626451e-09 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[266]" -type "float3" 1.8626451e-09 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[267]" -type "float3" -1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[268]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[269]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[270]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[271]" -type "float3" 1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[272]" -type "float3" 3.6379788e-12 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[273]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[274]" -type "float3" 1.4901161e-08 1.8189894e-12 0 ;
	setAttr ".pt[275]" -type "float3" 2.9802322e-08 1.8189894e-12 0 ;
	setAttr ".pt[276]" -type "float3" 5.9604645e-08 1.8189894e-12 0 ;
	setAttr ".pt[277]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[278]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[279]" -type "float3" -2.9802322e-08 1.8189894e-12 -2.9802322e-08 ;
	setAttr ".pt[280]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[281]" -type "float3" 0 1.8189894e-12 5.9604645e-08 ;
	setAttr ".pt[282]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[283]" -type "float3" 2.9802322e-08 1.8189894e-12 0 ;
	setAttr ".pt[284]" -type "float3" 0 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[285]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[286]" -type "float3" 0 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[287]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[288]" -type "float3" -1.4901161e-08 1.8189894e-12 0 ;
	setAttr ".pt[289]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[290]" -type "float3" -1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[291]" -type "float3" -1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[292]" -type "float3" 1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[293]" -type "float3" 1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[294]" -type "float3" 7.4505806e-09 1.8189894e-12 1.4901161e-08 ;
	setAttr ".pt[295]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[296]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[297]" -type "float3" -1.4901161e-08 1.8189894e-12 0 ;
	setAttr ".pt[298]" -type "float3" 0 1.8189894e-12 4.6566129e-10 ;
	setAttr ".pt[299]" -type "float3" -1.4901161e-08 1.8189894e-12 7.4505806e-09 ;
	setAttr ".pt[300]" -type "float3" 0 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[301]" -type "float3" 7.4505806e-09 1.8189894e-12 1.4901161e-08 ;
	setAttr ".pt[302]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[303]" -type "float3" -1.8626451e-09 1.8189894e-12 1.4901161e-08 ;
	setAttr ".pt[304]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[305]" -type "float3" 0 1.8189894e-12 7.4505806e-09 ;
	setAttr ".pt[306]" -type "float3" 0 1.8189894e-12 4.6566129e-10 ;
	setAttr ".pt[307]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[308]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[309]" -type "float3" 7.4505806e-09 1.8189894e-12 0 ;
	setAttr ".pt[310]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[311]" -type "float3" -1.8626451e-09 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[312]" -type "float3" 1.8626451e-09 1.8189894e-12 -2.9802322e-08 ;
	setAttr ".pt[313]" -type "float3" -1.8626451e-09 1.8189894e-12 2.9802322e-08 ;
	setAttr ".pt[314]" -type "float3" 0 1.8189894e-12 -5.9604645e-08 ;
	setAttr ".pt[315]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[316]" -type "float3" 0 1.8189894e-12 -5.9604645e-08 ;
	setAttr ".pt[317]" -type "float3" 1.8626451e-09 1.8189894e-12 2.9802322e-08 ;
	setAttr ".pt[318]" -type "float3" 3.6379788e-12 1.8189894e-12 2.9802322e-08 ;
	setAttr ".pt[321]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[322]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[324]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[325]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[326]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[327]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[328]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[329]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[330]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[331]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[332]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[333]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[334]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[335]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[336]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[337]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[338]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[340]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[342]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[343]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[345]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[348]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[350]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[351]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[352]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[353]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[354]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[356]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[357]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[358]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[359]" -type "float3" -2.9802322e-08 0 4.6566129e-10 ;
	setAttr ".pt[360]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[361]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[362]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[363]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[364]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[365]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[366]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[367]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[368]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[370]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[373]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[374]" -type "float3" 5.8207661e-11 0 5.9604645e-08 ;
	setAttr ".pt[375]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[377]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[379]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[380]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[381]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[382]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[383]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[384]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[386]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[387]" -type "float3" 2.9802322e-08 0 -1.4901161e-08 ;
	setAttr ".pt[388]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[389]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[394]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[395]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[396]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[398]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[400]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[401]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[402]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[404]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[405]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[406]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[408]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[410]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[411]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[412]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[413]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[414]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[417]" -type "float3" -5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[419]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[421]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[422]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[423]" -type "float3" 0 0 5.9604645e-08 ;
	setAttr ".pt[424]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[425]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[426]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[427]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[429]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[431]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[432]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[433]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[434]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[435]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[436]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[439]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[440]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[443]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[445]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[446]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[447]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[449]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[450]" -type "float3" 1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[451]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[452]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[453]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[454]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[455]" -type "float3" 1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[456]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[458]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[459]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[460]" -type "float3" 5.9604645e-08 -1.4901161e-08 0 ;
	setAttr ".pt[461]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[462]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[464]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[466]" -type "float3" -2.9802322e-08 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[467]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[468]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[470]" -type "float3" 0 -1.4901161e-08 5.9604645e-08 ;
	setAttr ".pt[471]" -type "float3" 0 0 5.9604645e-08 ;
	setAttr ".pt[472]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[474]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[475]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[476]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[477]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[480]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[481]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[482]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[484]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[485]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[486]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[488]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[489]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[490]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[491]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[492]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[493]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[494]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[495]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[496]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[497]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[499]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[500]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[502]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[503]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[504]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[505]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[506]" -type "float3" -1.4901161e-08 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[507]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[508]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[509]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[510]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[511]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[512]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[513]" -type "float3" -1.8626451e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[514]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[516]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[518]" -type "float3" 0 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[519]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[520]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[521]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[522]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[524]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[526]" -type "float3" 7.4505806e-09 -1.4901161e-08 0 ;
	setAttr ".pt[527]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[528]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[530]" -type "float3" -1.8626451e-09 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[531]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[532]" -type "float3" 1.8626451e-09 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[533]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[534]" -type "float3" -1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[535]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[536]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[537]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[539]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[540]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[541]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[542]" -type "float3" 1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[543]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[544]" -type "float3" 3.6379788e-12 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[545]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[548]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[550]" -type "float3" -5.9604645e-08 0 2.3283064e-10 ;
	setAttr ".pt[551]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[552]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[553]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[554]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[555]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[556]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[557]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[558]" -type "float3" -5.9604645e-08 0 2.3283064e-10 ;
	setAttr ".pt[559]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[560]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[562]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[563]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[564]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[565]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[566]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[568]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[570]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[571]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[572]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[573]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[574]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[575]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[578]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[579]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[582]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[584]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[585]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[586]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[587]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[589]" -type "float3" 1.8626451e-09 0 5.9604645e-08 ;
	setAttr ".pt[590]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[591]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[592]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[593]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[594]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[595]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[596]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[597]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[598]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[601]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[602]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[604]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[605]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[606]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[607]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[608]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[609]" -type "float3" 2.9802322e-08 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[611]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[612]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[613]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[614]" -type "float3" 2.9802322e-08 -7.4505806e-09 0 ;
	setAttr ".pt[616]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[617]" -type "float3" 2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[619]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[620]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[623]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[625]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[626]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[629]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[631]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[632]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[633]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[636]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[637]" -type "float3" -5.9604645e-08 7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[639]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[640]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[641]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[642]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[643]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[644]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[645]" -type "float3" -5.9604645e-08 7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[646]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[647]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[649]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[651]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[652]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[653]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[658]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[660]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[662]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[663]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[664]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[666]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[667]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[668]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[669]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[670]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[671]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[675]" -type "float3" 0 3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[676]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[677]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[679]" -type "float3" 0 3.7252903e-09 0 ;
	setAttr ".pt[680]" -type "float3" 0 3.7252903e-09 0 ;
	setAttr ".pt[681]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[684]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[685]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[686]" -type "float3" 0 3.7252903e-09 0 ;
	setAttr ".pt[691]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[692]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[693]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[695]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[697]" -type "float3" 0 1.8626451e-09 2.9802322e-08 ;
	setAttr ".pt[700]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[701]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[702]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[703]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[705]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[706]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[707]" -type "float3" 0 1.8626451e-09 -2.9802322e-08 ;
	setAttr ".pt[709]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[710]" -type "float3" 0 1.8626451e-09 2.9802322e-08 ;
	setAttr ".pt[711]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[713]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[714]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[720]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[721]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[722]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[723]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[724]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[725]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[726]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[728]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[729]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[730]" -type "float3" -2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[731]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[732]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[733]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[734]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[735]" -type "float3" 2.9802322e-08 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[737]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[738]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[739]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[740]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[741]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[744]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[745]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[747]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[748]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[749]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[750]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[751]" -type "float3" 2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[752]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[753]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[754]" -type "float3" 0 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[755]" -type "float3" 2.9802322e-08 -7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[756]" -type "float3" -2.9802322e-08 7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[757]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[758]" -type "float3" -2.9802322e-08 -7.4505806e-09 0 ;
	setAttr ".pt[759]" -type "float3" 0 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[760]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[761]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[762]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[763]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[764]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[766]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[767]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[768]" -type "float3" -5.9604645e-08 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[769]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[770]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[771]" -type "float3" -5.9604645e-08 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[772]" -type "float3" 5.9604645e-08 7.4505806e-09 0 ;
	setAttr ".pt[773]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[774]" -type "float3" -5.9604645e-08 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[775]" -type "float3" 5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[776]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[777]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[778]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[779]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[780]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[781]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[782]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[783]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[784]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[785]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[786]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[787]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[788]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[789]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[790]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[791]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[792]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[794]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[795]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[796]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[797]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[798]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[799]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[800]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[801]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[803]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[804]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[805]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[806]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[807]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[808]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[809]" -type "float3" -5.9604645e-08 -7.4505806e-09 0 ;
	setAttr ".pt[810]" -type "float3" 5.9604645e-08 7.4505806e-09 0 ;
	setAttr ".pt[811]" -type "float3" 5.9604645e-08 -7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[812]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[813]" -type "float3" 5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[814]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[815]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[816]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[817]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[818]" -type "float3" 2.9802322e-08 -7.4505806e-09 0 ;
	setAttr ".pt[819]" -type "float3" 2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[820]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[821]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[822]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[824]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[825]" -type "float3" -2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[827]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[829]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[831]" -type "float3" -2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[833]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[834]" -type "float3" 0 7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[836]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[837]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[838]" -type "float3" 0 7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[839]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[840]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[842]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[843]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[845]" -type "float3" -5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[846]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[847]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[848]" -type "float3" 0 -1.8626451e-09 -2.9802322e-08 ;
	setAttr ".pt[851]" -type "float3" 0 -1.8626451e-09 0 ;
	setAttr ".pt[852]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[854]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[855]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[856]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[857]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[858]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[859]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[860]" -type "float3" 5.9604645e-08 3.7252903e-09 0 ;
	setAttr ".pt[861]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[862]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[863]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[864]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[865]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[866]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[867]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[868]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[869]" -type "float3" -5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[870]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[871]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[872]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[873]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[874]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[875]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[876]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[877]" -type "float3" 5.9604645e-08 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[878]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[879]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[880]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[881]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[882]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[883]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[884]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[885]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[886]" -type "float3" 5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[887]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[888]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[889]" -type "float3" 5.9604645e-08 1.8626451e-09 0 ;
	setAttr ".pt[890]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[891]" -type "float3" 5.9604645e-08 1.8626451e-09 0 ;
	setAttr ".pt[892]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[893]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[894]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[895]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[896]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".db" yes;
	setAttr ".vs" 4;
	setAttr ".bw" 4;
	setAttr ".dr" 1;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "polySurfaceShape64" -p "Special_F";
	rename -uid "736A0541-473B-38FE-1C67-DFBE8C2A7B22";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.46763426065444946 0.76747080683708191 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 988 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0.95007211 0.36263311 0.94331485
		 0.35619503 0.94833994 0.35250604 0.95129395 0.35789162 0.93690395 0.34278738 0.94352347
		 0.34057105 0.93304479 0.32788754 0.94021475 0.32688928 0.93185216 0.31203926 0.93909746
		 0.3123647 0.93344015 0.29607773 0.94035715 0.29780513 0.93765712 0.28091937 0.94376957
		 0.28406531 0.94423944 0.26763743 0.94866854 0.27218276 0.95102936 0.26151073 0.95230877
		 0.266958 0.40661097 0.54944712 0.41573554 0.54999328 0.41459173 0.55638534 0.40898776
		 0.55414963 0.4291386 0.55657625 0.42564631 0.56276721 0.44138193 0.56627375 0.43649012
		 0.57171381 0.45189053 0.57820415 0.44598651 0.58265698 0.46007916 0.59166646 0.45352554
		 0.59495282 0.46554062 0.60579395 0.45884129 0.60774618 0.46805468 0.61970842 0.46205869
		 0.6199078 0.46689013 0.62877178 0.4627319 0.62633973 0.94255549 0.38402963 0.92701524
		 0.37336582 0.91422242 0.3557564 0.906932 0.33497512 0.9047277 0.31262302 0.90748394
		 0.28987992 0.91541648 0.26767856 0.92909592 0.24702585 0.94651639 0.23392999 0.95105487
		 0.22552276 0.41623425 0.52505994 0.43852383 0.53229988 0.45773399 0.54482692 0.47342324
		 0.5611946 0.48503843 0.58038276 0.49168515 0.60151672 0.49214986 0.62392622 0.48568875
		 0.64172345 0.93321002 0.21013826 0.418679 0.50187182 0.44801998 0.51061046 0.47307491
		 0.52622777 0.49324024 0.54712683 0.50786632 0.57204509 0.5156883 0.59975201 0.51425123
		 0.62763804 0.50409842 0.64787835 0.93234253 0.40042019 0.9123885 0.38958633 0.89463407
		 0.36802375 0.8844471 0.34144354 0.88142645 0.3130725 0.8851198 0.2846747 0.89547473
		 0.25748545 0.91269767 0.23271716 0.9315787 0.40215272 0.93142503 0.40320128 0.91011792
		 0.3927964 0.91089904 0.39167047 0.89129585 0.37025422 0.89246261 0.36948717 0.88057792
		 0.34256965 0.88193887 0.34219795 0.87739992 0.31315124 0.87881744 0.31314552 0.88121486
		 0.28379053 0.8825928 0.28412259 0.89190805 0.25578827 0.89316893 0.25640631 0.90943033
		 0.2303583 0.91059333 0.23120213 0.93094164 0.20689535 0.38630319 0.49853879 0.419231
		 0.49886665 0.41898298 0.50025094 0.44926375 0.50780386 0.44870567 0.50910115 0.47500932
		 0.52379835 0.47413957 0.52492321 0.49574077 0.5452652 0.49461281 0.54613 0.5107646
		 0.57091695 0.50945646 0.57144761 0.51878065 0.59956723 0.51738346 0.59966284 0.51716644
		 0.62869883 0.51585329 0.62821615 0.50585002 0.6491183 0.5051145 0.648422 0.46640131
		 0.62978637 0.46211472 0.62676328 0.95206678 0.26134324 0.95302278 0.26716328 0.9493981
		 0.35212368 0.95211136 0.35802501 0.94474316 0.34024411 0.94151264 0.32673162 0.94040745
		 0.31241494 0.94162303 0.29807574 0.94493645 0.28453833 0.94967377 0.2727651 0.41409636
		 0.55743384 0.40833688 0.55464351 0.42495668 0.56384867 0.43559974 0.57268971 0.44493681
		 0.58348191 0.45237097 0.59560823 0.4576636 0.60823894 0.46099156 0.62028909 0.95109266
		 0.36307883 0.40565193 0.54987758 0.94351304 0.3847121 0.39495397 0.52631158 0.50459522
		 0.6488837 0.48536038 0.6428774 0.93261051 0.40156007 0.94791311 0.23404217 0.94950646
		 0.22924018 0.94836462 0.22874773 0.93106484 0.40677339 0.93111491 0.40809822 0.90674049
		 0.39792037 0.90759873 0.3965562 0.88608056 0.37375128 0.88743353 0.37280643 0.87448704
		 0.3442961 0.87607509 0.34381127 0.87103766 0.31321955 0.87269801 0.31316727 0.87502801
		 0.28235042 0.87664443 0.28269267 0.88621479 0.25307435 0.88770431 0.25375164 0.90420121
		 0.22663313 0.90556192 0.22758001 0.92630583 0.20176572 0.38604736 0.49192864 0.42042315
		 0.49267814 0.42008823 0.49427259 0.45183349 0.50201929 0.45114249 0.5035041 0.47895718
		 0.51878995 0.47790682 0.52006912 0.50082916 0.54142022 0.4994812 0.54239541 0.51666516
		 0.56858611 0.51510632 0.56916559 0.5250634 0.59919435 0.52341104 0.59926075 0.52300757
		 0.63096398 0.52148777 0.63032556 0.50882947 0.65271229 0.50813586 0.65170407 0.46456635
		 0.63294363 0.46376815 0.63425487 0.45937526 0.62962067 0.46025229 0.62877345 0.95552713
		 0.26116699 0.95704216 0.26119435 0.9568795 0.26775408 0.95568562 0.2674998 0.95293403
		 0.351421 0.9544794 0.35127538 0.95619994 0.35858643 0.954952 0.35832596 0.94881105
		 0.33939487 0.95055526 0.33910251 0.94580406 0.32630885 0.94762748 0.32616156 0.944731
		 0.31260395 0.94656456 0.31268805 0.94582081 0.29892349 0.94760817 0.29925597 0.9488582
		 0.28596205 0.95054269 0.28649122 0.95316172 0.27430576 0.95467025 0.27480197 0.41206479
		 0.5605197 0.41107225 0.5617553 0.40520632 0.55731583 0.40621924 0.55655009 0.4225117
		 0.56728506 0.42141974 0.56870621 0.43260908 0.57586372 0.4313246 0.57719231 0.44147635
		 0.58621162 0.44001645 0.58737159 0.44859859 0.59784555 0.44702473 0.59882754 0.45384169
		 0.61004317 0.45226985 0.61088705 0.45763871 0.62195939 0.45631024 0.62280393 0.95595473
		 0.36495525 0.95449257 0.3644228 0.40124077 0.55228025 0.40253663 0.55151892 0.94800711
		 0.38797271 0.94670081 0.3869862 0.3899157 0.52915633 0.95462221 0.22571188 0.50697434
		 0.6520437 0.50737804 0.65322566 0.48389253 0.64830911 0.4842816 0.64668876 0.93332434
		 0.40673333 0.93286085 0.40560091 0.9524489 0.23452663 0.95434368 0.23469412 0.95509857
		 0.2302807 0.95341909 0.23008561 0.9311375 0.40625119 0.90795791 0.3959831 0.88800466
		 0.37241948 0.87674487 0.34362596 0.87339723 0.31316251 0.87732482 0.28285897 0.88833243
		 0.25405228 0.90614104 0.22798806 0.92810655 0.20355093 0.41995502 0.4949562 0.45085704
		 0.50414407 0.47747743 0.52062637 0.49892187 0.54282141 0.51446068 0.56942743 0.52271926
		 0.59930146 0.52086025 0.63003504 0.50777692 0.65136558 0.46484086 0.63247585 0.46055645
		 0.62848568 0.95500165 0.26117694 0.95527631 0.26741904 0.95239514 0.35148978 0.95452023
		 0.35824859;
	setAttr ".uvst[0].uvsp[250:499]" 0.94820195 0.33950669 0.94516504 0.32636547
		 0.94408774 0.31257528 0.9451946 0.29880297 0.94826978 0.28576541 0.95263696 0.27411646
		 0.41239989 0.56007725 0.40656322 0.55628091 0.42288792 0.56678224 0.4330582 0.57539594
		 0.44198996 0.58580536 0.44915491 0.59750628 0.4544012 0.60975897 0.45811334 0.62167871
		 0.95398331 0.3642363 0.40299058 0.55125666 0.94624889 0.38663018 0.39193887 0.52798653
		 0.50660807 0.65157193 0.48439988 0.64611501 0.93283588 0.40499717 0.95177937 0.23446524
		 0.9528355 0.22999787 0.62801111 0.99148852 0.66628706 0.9851492 0.69561517 0.9575454
		 0.71241146 0.92363954 0.7192685 0.88782364 0.71736687 0.85201985 0.70722187 0.81785244
		 0.68990445 0.78701103 0.66921699 0.75855517 0.26026142 0.7694996 0.26797009 0.80574393
		 0.28466868 0.83857888 0.30879664 0.86599094 0.33905292 0.88681418 0.3747952 0.89915609
		 0.41473794 0.89832377 0.44743621 0.8778224 0.43391395 0.81170982 0.42801535 0.80559528
		 0.59804666 0.828174 0.59819186 0.83540124 0.59438902 0.91767561 0.59311771 0.9267267
		 0.5979777 0.90436524 0.60122693 0.89192921 0.60301995 0.87988538 0.60299069 0.86799645
		 0.60136324 0.8560307 0.59909904 0.84352255 0.36367846 0.74993479 0.35853446 0.74347472
		 0.37087309 0.76040649 0.37836373 0.76998508 0.38699877 0.7783255 0.39705253 0.78551006
		 0.40844321 0.79215133 0.42065668 0.79969406 0.59315079 0.93516988 0.35327148 0.73813736
		 0.60166472 0.96548259 0.33061469 0.72235698 0.44879842 0.87504482 0.44737935 0.84032011
		 0.62352717 0.99012864 0.60075277 0.80199319 0.60065395 0.79751486 0.61698633 0.92946178
		 0.61610019 0.92464304 0.61942792 0.91948265 0.62418193 0.92351586 0.62507564 0.90791678
		 0.63152355 0.91059297 0.62934572 0.89450133 0.6364277 0.89600253 0.63149089 0.88009173
		 0.6387409 0.88027793 0.63126767 0.86547977 0.6382885 0.86424416 0.62883759 0.85153407
		 0.6351555 0.84882617 0.62479007 0.83933628 0.62952793 0.83511412 0.62152773 0.83386391
		 0.62318832 0.82852584 0.33749998 0.75756931 0.34199417 0.76032269 0.34376192 0.76608729
		 0.33729911 0.7667073 0.3492204 0.7776252 0.3427676 0.78060192 0.35725188 0.78916574
		 0.35143316 0.79359692 0.36738372 0.79952586 0.36246693 0.80504626 0.37902415 0.80804443
		 0.37521791 0.81430811 0.39134336 0.81438547 0.38885558 0.82090402 0.40320635 0.81858021
		 0.40252256 0.82454103 0.40956736 0.81977534 0.41165113 0.8241117 0.63923484 0.94179058
		 0.62298149 0.95134056 0.6532374 0.92512351 0.66197705 0.904908 0.66575599 0.8827669
		 0.6646139 0.85988456 0.65826732 0.83717686 0.64607275 0.81561285 0.62960929 0.80133277
		 0.31240964 0.76517141 0.62564439 0.79260373 0.31780958 0.78797424 0.3287288 0.80814171
		 0.34376335 0.82511586 0.36194265 0.83826113 0.38246834 0.84661233 0.40476811 0.84890211
		 0.42303419 0.8439008 0.28909981 0.76571506 0.29073012 0.73360884 0.29541874 0.79566664
		 0.30894065 0.82190871 0.32812428 0.84371138 0.35176623 0.86032546 0.37874663 0.87038839
		 0.40666366 0.87123626 0.42766058 0.86276138 0.63203752 0.96840453 0.65269452 0.95898938
		 0.67191851 0.93873018 0.68395209 0.91293645 0.68896657 0.88485038 0.6872856 0.85626155
		 0.67887032 0.82840651 0.6634264 0.8024832 0.63267684 0.97018665 0.65403503 0.96117204
		 0.65473735 0.96235317 0.63275599 0.97124672 0.67398256 0.94034153 0.67509598 0.9411906
		 0.68640107 0.91386461 0.68773645 0.91433215 0.6915639 0.88510633 0.69298154 0.88521171
		 0.68984485 0.85588813 0.69124651 0.85565293 0.6812458 0.82749176 0.68255037 0.82696229
		 0.66563165 0.80111992 0.66685432 0.80035794 0.6459651 0.7765916 0.28689456 0.73297048
		 0.28745943 0.76588547 0.28605568 0.76602006 0.29385841 0.7962265 0.29251623 0.79667807
		 0.30755341 0.82286263 0.30635786 0.82363939 0.32701814 0.84499717 0.32606089 0.84605312
		 0.35103965 0.86186051 0.35040092 0.86312383 0.37851727 0.87207007 0.37830532 0.87345827
		 0.40710855 0.87288046 0.40748286 0.87423277 0.42812085 0.86381853 0.42875886 0.86460996
		 0.41004145 0.81919223 0.41270638 0.82370353 0.62079787 0.83401835 0.62216097 0.82828575
		 0.61527133 0.92471784 0.61839479 0.9190256 0.62387687 0.90750331 0.62805682 0.89425147
		 0.63017535 0.88004911 0.62998074 0.86566108 0.62763566 0.85192513 0.62374181 0.83984733
		 0.34254253 0.7597121 0.34485102 0.7656765 0.35035872 0.77702355 0.3583014 0.78835493
		 0.36829495 0.7985431 0.37977409 0.8069427 0.39193201 0.81324708 0.40367532 0.81754363
		 0.61593282 0.92983621 0.33800948 0.75664485 0.62197429 0.95195711 0.62497032 0.79253685
		 0.42421496 0.84366167 0.42862451 0.86334062 0.63169038 0.96952707 0.62820333 0.80134934
		 0.6281237 0.79602951 0.6269508 0.79646665 0.63286519 0.97482938 0.65698701 0.96627623
		 0.65775037 0.96770114 0.63272554 0.97615159 0.67876768 0.94400388 0.68005526 0.94504404
		 0.69213778 0.91588438 0.69369239 0.91648096 0.6976667 0.8855567 0.69932401 0.88572562
		 0.69587857 0.85487866 0.6975196 0.85465002 0.68688273 0.82522702 0.68842059 0.82465422
		 0.67090398 0.79786026 0.67233205 0.79700893 0.6506303 0.77176684 0.28008419 0.73237538
		 0.28141105 0.76649988 0.27978969 0.76670384 0.28808105 0.79819781 0.28654027 0.79876679
		 0.30240715 0.82621938 0.30104244 0.82716405 0.322896 0.84954154 0.32181025 0.85080826
		 0.34829903 0.86730248 0.34759068 0.8688122 0.37761688 0.87804317 0.37741399 0.87968922
		 0.40874743 0.87867081 0.40925992 0.88024271 0.43114889 0.86709189 0.4320972 0.86787057
		 0.41599417 0.82213247 0.4121865 0.81748891 0.41310596 0.8166821 0.41736972 0.82144123
		 0.61872345 0.82787305 0.61812013 0.8341772 0.61690718 0.83434635 0.61720622 0.82779276
		 0.61491734 0.91807634 0.61242175 0.92482686 0.61115324 0.92499787 0.6133818 0.91782159;
	setAttr ".uvst[0].uvsp[500:749]" 0.61988205 0.90636683 0.61815757 0.90595108
		 0.62381023 0.89352566 0.62199622 0.89324874 0.62585402 0.87993121 0.6240136 0.8798849
		 0.6257391 0.86620849 0.6239273 0.86641401 0.62362975 0.85306466 0.62190741 0.85347533
		 0.62016219 0.84113598 0.61861795 0.84152722 0.34808993 0.76390278 0.34460449 0.75775373
		 0.34545445 0.75680393 0.34940529 0.76301181 0.35398054 0.77487075 0.35548973 0.77389514
		 0.36170471 0.78563803 0.36313677 0.78446192 0.37129295 0.7953214 0.37257135 0.79395676
		 0.38230669 0.80337036 0.3834163 0.8018772 0.39403701 0.80959094 0.39500761 0.80808794
		 0.40560591 0.81434131 0.40655684 0.81308079 0.61244798 0.93093956 0.61094773 0.93137002
		 0.33989286 0.75367498 0.34075928 0.75244105 0.61864555 0.95400107 0.61726928 0.95489669
		 0.31764722 0.74070251 0.62071151 0.79260808 0.43158233 0.86596632 0.42809916 0.84290558
		 0.42975128 0.84265053 0.43273079 0.86646843 0.63061476 0.97464037 0.63115662 0.97353894
		 0.62365317 0.80151093 0.62174612 0.80155021 0.62299001 0.79700404 0.62129593 0.7971018
		 0.65657032 0.96551126 0.63282579 0.97414929 0.67806512 0.94345826 0.69129205 0.91558474
		 0.69676673 0.88549244 0.69498783 0.8550266 0.68604624 0.82555723 0.67012191 0.79833162
		 0.28282028 0.73249114 0.2823028 0.76639783 0.28893363 0.79790211 0.30316591 0.82572281
		 0.32350707 0.84887105 0.34870374 0.8664993 0.37774396 0.87716115 0.40846002 0.87782836
		 0.43073869 0.86660111 0.41178012 0.81784832 0.41537249 0.82243538 0.61865437 0.83411413
		 0.61939561 0.82792687 0.61297828 0.92476881 0.6156013 0.91821414 0.62065309 0.90656769
		 0.62462431 0.89365709 0.62668103 0.87995321 0.62655222 0.86611104 0.62440068 0.85286677
		 0.62085032 0.84093791 0.34422398 0.75816149 0.34748781 0.76428443 0.35329545 0.77529836
		 0.36105788 0.78616267 0.37071884 0.79593593 0.38181424 0.80404663 0.39361501 0.81027657
		 0.40520024 0.81492245 0.61312073 0.93074268 0.3395133 0.75423241 0.61925936 0.95359147
		 0.62267929 0.79267728 0.43101716 0.86543483 0.42735124 0.84300673 0.63123375 0.97275704
		 0.62451458 0.8014912 0.62375152 0.79692906 0.0094140172 0.008081615 0.0085229129
		 0.0070931315 0.027751654 0 0.027672544 0.0013290644 0.0013302565 0.02579242 0 0.025734067
		 0.0081504285 0.043986797 0.0071673691 0.044885635 0.025789738 0.052028239 0.025725901
		 0.053358972 0.043958068 0.045272112 0.044850439 0.046261191 0.052038521 0.02765274
		 0.053368658 0.027725816 0.045312226 0.0094712377 0.04630743 0.0085858703 0.027632833
		 0.0021881461 0.010000676 0.0087099671 0.95425546 0.034998447 0.95393729 0.034520715
		 0.9618578 0.022805303 0.96242386 0.0229197 0.0021905601 0.025821447 0.93993884 0.0377478
		 0.94005388 0.037182212 0.0087803602 0.043397009 0.92787027 0.029582366 0.92835438
		 0.029268071 0.025821328 0.051170647 0.92511201 0.015280619 0.92567635 0.015394911
		 0.043373138 0.04463762 0.93327147 0.0032071024 0.93359333 0.0036905259 0.051178873
		 0.027616203 0.94758135 0.00043809414 0.94746709 0.0010038912 0.044674397 0.01004678
		 0.95965427 0.0086016506 0.95917487 0.0089237541 0.95253199 0.032367766 0.95228893
		 0.031997398 0.95890844 0.022190258 0.9593426 0.022280127 0.94058233 0.034664065 0.94067228
		 0.034229547 0.93050218 0.027858526 0.9308728 0.02761513 0.92819136 0.015920833 0.92862558
		 0.016010761 0.93499821 0.0058374703 0.9352417 0.0062080622 0.94694179 0.0035224408
		 0.94685203 0.0039566457 0.95702499 0.010327861 0.95665449 0.010571405 0.95013708
		 0.028923571 0.94997454 0.028671935 0.9549135 0.021470457 0.95520747 0.02153343 0.9413299
		 0.030523628 0.94139278 0.030231267 0.93395513 0.025461584 0.93420923 0.025299817
		 0.93232757 0.016666815 0.93262094 0.016730033 0.93739671 0.0092887804 0.93756193
		 0.0095404238 0.94619745 0.0076586083 0.94613421 0.0079525933 0.95357448 0.012725145
		 0.95332223 0.012887523 0.94867802 0.026696637 0.94847709 0.026384532 0.95228028 0.020942062
		 0.95264053 0.021021605 0.94185877 0.028002173 0.94193447 0.027633369 0.93613428 0.024016231
		 0.93644726 0.023812324 0.93489349 0.0171756 0.93525833 0.017254375 0.93885553 0.011462197
		 0.93905658 0.011777662 0.94568992 0.010225482 0.94561011 0.010592863 0.95140034 0.014179505
		 0.95108747 0.014383301 0.94797957 0.025619045 0.94777018 0.025292382 0.95099032 0.020655736
		 0.95137131 0.02074191 0.94212854 0.026732437 0.94221091 0.026349783 0.93722123 0.023323864
		 0.93755209 0.023117334 0.93615454 0.017455503 0.93653464 0.017540626 0.9395479 0.012551494
		 0.93975937 0.012874588 0.94541728 0.011479847 0.94533306 0.011866041 0.95031518 0.014881603
		 0.94998544 0.015089639 0.94822413 0.020192131 0.94613665 0.023024797 0.9458729 0.022585988
		 0.94772452 0.020070046 0.94266427 0.023575768 0.94278562 0.023075923 0.93982804 0.021485329
		 0.94026971 0.021218389 0.93929881 0.018002898 0.93979979 0.018126756 0.94138157 0.015161082
		 0.94164902 0.015602931 0.94486517 0.014630184 0.94474143 0.015128359 0.94769728 0.01671575
		 0.94725835 0.016982943 0.94506443 0.021256566 0.94620734 0.019699126 0.94315761 0.021552965
		 0.94160354 0.020410836 0.94131166 0.018499374 0.94245631 0.0169411 0.9443652 0.016647816
		 0.94592017 0.017792284 0.027484208 0.0047762394 0.027466357 0.0050820112 0.011937082
		 0.010866404 0.011732206 0.010639071 0.0050882995 0.025955677 0.0047826171 0.025940895
		 0.010918766 0.041446745 0.010692418 0.041652977 0.025962502 0.048276186 0.025947511
		 0.048582375 0.041434377 0.042488158 0.041639328 0.042715847 0.048282444 0.027458131
		 0.04858844 0.027475119 0.042514995 0.011977613 0.042744204 0.011774302 0.027380615
		 0.0072745681 0.027367204 0.0074539781 0.01355058 0.012604356 0.013434425 0.012468576
		 0.007460326 0.026028514 0.0072804987 0.026016295 0.012647808 0.039818525 0.012512624
		 0.039936841 0.02603966 0.045898318 0.026028097 0.046079516 0.03981477 0.040747762
		 0.039932936 0.040883541 0.04590562 0.027362943 0.046086222 0.027376771;
	setAttr ".uvst[0].uvsp[750:987]" 0.040765762 0.013585567 0.040901199 0.013467729
		 0.027053162 0.0092161298 0.027046338 0.0094471574 0.014743939 0.014233589 0.014585823
		 0.014065146 0.0094571114 0.02633065 0.0092261434 0.026322544 0.014270693 0.038613558
		 0.014102399 0.038772225 0.026342541 0.04389596 0.026338011 0.044127345 0.038620114
		 0.039110482 0.038778454 0.039279342 0.043902457 0.027041018 0.044133723 0.027051389
		 0.039120123 0.014768839 0.03928937 0.014611185 0.017605975 0.017023981 0.027087077
		 0.013445139 0.027030855 0.014974713 0.018652707 0.0181427 0.013453692 0.026271164
		 0.01498431 0.026322722 0.017055213 0.035743177 0.018175453 0.034698486 0.026289284
		 0.039892554 0.026340425 0.038362563 0.03575477 0.036313415 0.034706652 0.035193741
		 0.039900899 0.027086556 0.038369358 0.027031422 0.036314115 0.017623782 0.035189122
		 0.018664062 0.026940688 0.018082261 0.020789474 0.020403922 0.018094689 0.026401103
		 0.020426661 0.032556653 0.026422381 0.035254061 0.032565296 0.032933354 0.035255834
		 0.026946366 0.03293027 0.020805836 0.95450246 0.035370439 0.96286166 0.023007601
		 0.93985039 0.038185865 0.92749828 0.029829532 0.92467415 0.015192538 0.93302393 0.0028353631
		 0.94766933 0 0.96002603 0.0083541125 0.027069971 0.0089381933 0.01440458 0.013853073
		 0.0089473724 0.026305556 0.013896257 0.038961112 0.026323617 0.044406354 0.038962096
		 0.039491057 0.044413149 0.027071118 0.039495766 0.014423192 0.027090713 0.013256371
		 0.017476127 0.01688683 0.013264954 0.02626425 0.016918182 0.035872877 0.026287615
		 0.040081322 0.035884798 0.036450446 0.040089816 0.027095318 0.03645137 0.017493963
		 0.027510554 0.0042890906 0.011406645 0.010271013 0.0042904913 0.025919318 0.010332823
		 0.041982055 0.025924861 0.049075842 0.041967213 0.043076694 0.049080521 0.02750057
		 0.043105632 0.011442244 0.95973718 0.022361487 0.95275295 0.032704413 0.94050092
		 0.035057545 0.93016398 0.028079361 0.92779666 0.015839338 0.93477529 0.0055004656
		 0.94702286 0.0031287521 0.95736122 0.010105848 0.95036501 0.029271334 0.95561534
		 0.021617815 0.94124502 0.030932367 0.93360692 0.025690421 0.93191946 0.016581975
		 0.93716812 0.0089404285 0.94628203 0.0072504878 0.95392281 0.012496516 0.94882387
		 0.026912659 0.95289725 0.021077231 0.94180667 0.028259858 0.93591297 0.02415584 0.93463749
		 0.017120935 0.93871057 0.011243694 0.94574457 0.0099692047 0.95162153 0.014039166
		 0.94623953 0.023191065 0.94841421 0.020237014 0.94261956 0.023766637 0.93966323 0.021589652
		 0.93910831 0.017955989 0.94128394 0.014991939 0.9449119 0.014441922 0.94786441 0.016612872
		 0.026889592 0.019759417 0.021962076 0.021636784 0.021394372 0.021031022 0.02691257
		 0.018984199 0.01976794 0.026430011 0.018965721 0.026420653 0.02162686 0.031388819
		 0.021055847 0.031951129 0.026445389 0.033579171 0.026437998 0.034382045 0.031398118
		 0.031725526 0.03195858 0.032301068 0.033581704 0.02691251 0.03438431 0.026924431
		 0.03173323 0.021941483 0.032306775 0.021379352 0.0220166 0.021694005 0.026889563
		 0.019837677 0.019846231 0.026434481 0.021684587 0.031333625 0.026445895 0.033504486
		 0.031343848 0.031666577 0.033503503 0.026907921 0.03167513 0.021995544 0.020869181
		 0.020490706 0.026936755 0.018203497 0.018212557 0.026406884 0.020512611 0.032472908
		 0.026425511 0.035136998 0.032485187 0.032842815 0.035138041 0.026940465 0.032843515
		 0.020885706 0.026838273 0.021700978 0.023291782 0.023050547 0.021712661 0.026504099
		 0.02305007 0.030063212 0.026507705 0.031639099 0.030067474 0.030304134 0.031639054
		 0.026839733 0.030307025 0.023270607 0.026676834 0.026671708 0.94375944 0.019100755
		 0.51461279 0.6699419 0.4801439 0.66569543 0.37208009 0.53972864 0.97566402 0.23213661
		 0.93932897 0.42267388 0.93476319 0.42372173 0.97525573 0.23660016 0.97613025 0.26292717
		 0.96283746 0.39962018 0.45274115 0.64996457 0.51749128 0.66881263 0.38596785 0.56359017
		 0.97344226 0.37000108 0.39085782 0.56926894 0.97406781 0.36158812 0.44712543 0.64359367
		 0.44183838 0.6357851 0.43530509 0.62299883 0.42960712 0.61109978 0.42326391 0.60048741
		 0.41565615 0.59119546 0.40672278 0.58294499 0.39687538 0.57492065 0.97547549 0.27013302
		 0.97399741 0.27817667 0.97085387 0.29050374 0.96838069 0.30233073 0.96750569 0.31418955
		 0.96843779 0.32632798 0.97079688 0.33895671 0.97343665 0.35247773 0.54057741 0.63791835
		 0.54468197 0.59819466 0.53531104 0.56156206 0.51703066 0.52969831 0.49167502 0.50340587
		 0.46030438 0.48408145 0.42480594 0.47344345 0.90999693 0.18849295 0.88737184 0.21542734
		 0.86793578 0.24497068 0.85541356 0.27833456 0.85099494 0.3139137 0.85531241 0.35012609
		 0.86968511 0.38513669 0.89701831 0.41473573 0.6499356 0.77246517 0.28185344 0.73238158
		 0.92760682 0.20297229 0.38607007 0.49268273 0.6445384 0.77852333 0.2884202 0.73317885
		 0.65201688 0.7706508 0.38891959 0.46995902 0.25971925 0.73344737 0.64703184 0.77544457
		 0.93192238 0.20811117 0.38618565 0.49016988 0.38621968 0.49700522 0.62208945 0.79264683
		 0.31720579 0.74134326 0.31863582 0.73927641 0.97618437 0.22764641 0.60044581 0.79300076
		 0.31539094 0.74406374 0.31471038 0.7450825 0.95415992 0.22567499 0.39141321 0.52828836
		 0.95599228 0.22581935 0.9517163 0.22554833 0.39602083 0.52571821 0.38654321 0.50087655
		 0.55379331 0.8922348 0.55808502 0.90162349 0.42362154 0.96308702 0.41932982 0.95369834
		 0.5495013 0.8828454 0.41503775 0.94430888 0.54520786 0.87345219 0.41074437 0.93491572
		 0.54091746 0.86406589 0.40645391 0.92552942 0.53662503 0.85467553 0.40216148 0.91613907
		 0.56667024 0.92040581 0.43220675 0.98186934 0.56237841 0.9110164 0.42791498 0.97247994
		 0.3978678 0.90674615 0.53233129 0.84528261;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr -s 729 ".pt";
	setAttr ".pt[1]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[2]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[4]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[6]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[7]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[8]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[9]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[10]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[11]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[12]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[13]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[14]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[15]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[16]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[17]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[18]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[19]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[21]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[22]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[25]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[27]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[28]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[30]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[32]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[33]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[34]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[35]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[36]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[38]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[39]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[40]" -type "float3" -2.9802322e-08 0 4.6566129e-10 ;
	setAttr ".pt[41]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[42]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[43]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[44]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[45]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[46]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[47]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[48]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[49]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[51]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[54]" -type "float3" 5.8207661e-11 0 5.9604645e-08 ;
	setAttr ".pt[55]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[56]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[58]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[60]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[61]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[62]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[63]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[64]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[65]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[67]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[68]" -type "float3" 2.9802322e-08 0 -1.4901161e-08 ;
	setAttr ".pt[69]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[70]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[72]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[73]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[75]" -type "float3" 2.9802322e-08 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[76]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[77]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[78]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[79]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[80]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[81]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[82]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[83]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[84]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[85]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[86]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[87]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[88]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[89]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[90]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[91]" -type "float3" 0 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[92]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[93]" -type "float3" 5.9604645e-08 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[94]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[95]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[96]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[97]" -type "float3" -5.9604645e-08 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[99]" -type "float3" 0 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[101]" -type "float3" 1.4901161e-08 1.4901161e-08 0 ;
	setAttr ".pt[103]" -type "float3" 0 1.4901161e-08 5.9604645e-08 ;
	setAttr ".pt[104]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[105]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[106]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[107]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[108]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[109]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[110]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[111]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[112]" -type "float3" -1.4901161e-08 1.4901161e-08 0 ;
	setAttr ".pt[113]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[114]" -type "float3" -1.4901161e-08 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[115]" -type "float3" 0 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[116]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[117]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[118]" -type "float3" -1.8626451e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[119]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[120]" -type "float3" 0 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[121]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[122]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[123]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[124]" -type "float3" 7.4505806e-09 1.4901161e-08 0 ;
	setAttr ".pt[125]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[126]" -type "float3" -1.8626451e-09 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[127]" -type "float3" 1.8626451e-09 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[128]" -type "float3" -1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[129]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[130]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[131]" -type "float3" 1.8626451e-09 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[132]" -type "float3" 1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[133]" -type "float3" 3.6379788e-12 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[134]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[136]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[137]" -type "float3" 1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[138]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[139]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[140]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[141]" -type "float3" 5.9604645e-08 -1.4901161e-08 0 ;
	setAttr ".pt[142]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[143]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[145]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[147]" -type "float3" -2.9802322e-08 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[148]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[149]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[151]" -type "float3" 0 -1.4901161e-08 5.9604645e-08 ;
	setAttr ".pt[152]" -type "float3" 0 0 5.9604645e-08 ;
	setAttr ".pt[153]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[155]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[156]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[157]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[158]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[159]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[161]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[162]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[163]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[165]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[166]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[167]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[169]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[170]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[171]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[172]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[173]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[174]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[175]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[176]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[177]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[178]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[179]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[182]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[183]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[184]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[185]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[186]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[187]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[188]" -type "float3" -1.4901161e-08 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[189]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[190]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[191]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[192]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[194]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[195]" -type "float3" -1.8626451e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[196]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[198]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[199]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[200]" -type "float3" 0 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[201]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[202]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[204]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[206]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[207]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[208]" -type "float3" 7.4505806e-09 -1.4901161e-08 0 ;
	setAttr ".pt[209]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[211]" -type "float3" -1.8626451e-09 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[212]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[213]" -type "float3" 1.8626451e-09 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[214]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[215]" -type "float3" -1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[216]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[217]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[218]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[219]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[221]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[222]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[223]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[224]" -type "float3" 1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[225]" -type "float3" 3.6379788e-12 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[226]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[227]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[228]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[229]" -type "float3" 0 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[230]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[231]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[232]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[233]" -type "float3" 2.9802322e-08 1.4901161e-08 0 ;
	setAttr ".pt[234]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[235]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[236]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[237]" -type "float3" -2.9802322e-08 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[238]" -type "float3" -5.9604645e-08 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[239]" -type "float3" -5.9604645e-08 1.4901161e-08 2.3283064e-10 ;
	setAttr ".pt[240]" -type "float3" 5.9604645e-08 1.4901161e-08 0 ;
	setAttr ".pt[241]" -type "float3" -2.9802322e-08 1.4901161e-08 0 ;
	setAttr ".pt[242]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[243]" -type "float3" 0 1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[244]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[245]" -type "float3" -1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[246]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[247]" -type "float3" 1.8626451e-09 1.4901161e-08 0 ;
	setAttr ".pt[248]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[249]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[250]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[251]" -type "float3" -1.4901161e-08 1.4901161e-08 0 ;
	setAttr ".pt[252]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[253]" -type "float3" -1.4901161e-08 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[254]" -type "float3" 0 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[255]" -type "float3" 7.4505806e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[256]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[257]" -type "float3" -1.8626451e-09 1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[258]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[259]" -type "float3" 0 1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[260]" -type "float3" 0 1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[261]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[262]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[263]" -type "float3" 7.4505806e-09 1.4901161e-08 0 ;
	setAttr ".pt[264]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[265]" -type "float3" -1.8626451e-09 1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[266]" -type "float3" 1.8626451e-09 1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[267]" -type "float3" -1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[268]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[269]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[270]" -type "float3" 0 1.4901161e-08 0 ;
	setAttr ".pt[271]" -type "float3" 1.8626451e-09 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[272]" -type "float3" 3.6379788e-12 1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[273]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[274]" -type "float3" 1.4901161e-08 1.8189894e-12 0 ;
	setAttr ".pt[275]" -type "float3" 2.9802322e-08 1.8189894e-12 0 ;
	setAttr ".pt[276]" -type "float3" 5.9604645e-08 1.8189894e-12 0 ;
	setAttr ".pt[277]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[278]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[279]" -type "float3" -2.9802322e-08 1.8189894e-12 -2.9802322e-08 ;
	setAttr ".pt[280]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[281]" -type "float3" 0 1.8189894e-12 5.9604645e-08 ;
	setAttr ".pt[282]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[283]" -type "float3" 2.9802322e-08 1.8189894e-12 0 ;
	setAttr ".pt[284]" -type "float3" 0 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[285]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[286]" -type "float3" 0 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[287]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[288]" -type "float3" -1.4901161e-08 1.8189894e-12 0 ;
	setAttr ".pt[289]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[290]" -type "float3" -1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[291]" -type "float3" -1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[292]" -type "float3" 1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[293]" -type "float3" 1.8626451e-09 1.8189894e-12 0 ;
	setAttr ".pt[294]" -type "float3" 7.4505806e-09 1.8189894e-12 1.4901161e-08 ;
	setAttr ".pt[295]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[296]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[297]" -type "float3" -1.4901161e-08 1.8189894e-12 0 ;
	setAttr ".pt[298]" -type "float3" 0 1.8189894e-12 4.6566129e-10 ;
	setAttr ".pt[299]" -type "float3" -1.4901161e-08 1.8189894e-12 7.4505806e-09 ;
	setAttr ".pt[300]" -type "float3" 0 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[301]" -type "float3" 7.4505806e-09 1.8189894e-12 1.4901161e-08 ;
	setAttr ".pt[302]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[303]" -type "float3" -1.8626451e-09 1.8189894e-12 1.4901161e-08 ;
	setAttr ".pt[304]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[305]" -type "float3" 0 1.8189894e-12 7.4505806e-09 ;
	setAttr ".pt[306]" -type "float3" 0 1.8189894e-12 4.6566129e-10 ;
	setAttr ".pt[307]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[308]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[309]" -type "float3" 7.4505806e-09 1.8189894e-12 0 ;
	setAttr ".pt[310]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[311]" -type "float3" -1.8626451e-09 1.8189894e-12 -1.4901161e-08 ;
	setAttr ".pt[312]" -type "float3" 1.8626451e-09 1.8189894e-12 -2.9802322e-08 ;
	setAttr ".pt[313]" -type "float3" -1.8626451e-09 1.8189894e-12 2.9802322e-08 ;
	setAttr ".pt[314]" -type "float3" 0 1.8189894e-12 -5.9604645e-08 ;
	setAttr ".pt[315]" -type "float3" 0 1.8189894e-12 0 ;
	setAttr ".pt[316]" -type "float3" 0 1.8189894e-12 -5.9604645e-08 ;
	setAttr ".pt[317]" -type "float3" 1.8626451e-09 1.8189894e-12 2.9802322e-08 ;
	setAttr ".pt[318]" -type "float3" 3.6379788e-12 1.8189894e-12 2.9802322e-08 ;
	setAttr ".pt[321]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[322]" -type "float3" -7.4505806e-09 0 0 ;
	setAttr ".pt[324]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[325]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[326]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[327]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[328]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[329]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[330]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[331]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[332]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[333]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[334]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[335]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[336]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[337]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[338]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[340]" -type "float3" 0 0 1.4901161e-08 ;
	setAttr ".pt[342]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[343]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[345]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[348]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[350]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[351]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[352]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[353]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[354]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[356]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[357]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[358]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[359]" -type "float3" -2.9802322e-08 0 4.6566129e-10 ;
	setAttr ".pt[360]" -type "float3" 2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[361]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[362]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[363]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[364]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[365]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[366]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[367]" -type "float3" -2.9802322e-08 0 1.4901161e-08 ;
	setAttr ".pt[368]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[370]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[373]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[374]" -type "float3" 5.8207661e-11 0 5.9604645e-08 ;
	setAttr ".pt[375]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[377]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[379]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[380]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[381]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[382]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[383]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[384]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[386]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[387]" -type "float3" 2.9802322e-08 0 -1.4901161e-08 ;
	setAttr ".pt[388]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[389]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[394]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[395]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[396]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[398]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[400]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[401]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[402]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[404]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[405]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[406]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[408]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[410]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[411]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[412]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[413]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[414]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[417]" -type "float3" -5.9604645e-08 0 1.4901161e-08 ;
	setAttr ".pt[419]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[421]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[422]" -type "float3" -1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[423]" -type "float3" 0 0 5.9604645e-08 ;
	setAttr ".pt[424]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[425]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[426]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[427]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[429]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[431]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[432]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[433]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[434]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[435]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[436]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[439]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[440]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[443]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[445]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[446]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[447]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[449]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[450]" -type "float3" 1.8626451e-09 0 -5.9604645e-08 ;
	setAttr ".pt[451]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[452]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[453]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[454]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[455]" -type "float3" 1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[456]" -type "float3" 1.4901161e-08 0 0 ;
	setAttr ".pt[458]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[459]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[460]" -type "float3" 5.9604645e-08 -1.4901161e-08 0 ;
	setAttr ".pt[461]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[462]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[464]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[466]" -type "float3" -2.9802322e-08 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[467]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[468]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[470]" -type "float3" 0 -1.4901161e-08 5.9604645e-08 ;
	setAttr ".pt[471]" -type "float3" 0 0 5.9604645e-08 ;
	setAttr ".pt[472]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[474]" -type "float3" 2.9802322e-08 -1.4901161e-08 0 ;
	setAttr ".pt[475]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[476]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[477]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[480]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[481]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[482]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[484]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[485]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[486]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[488]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[489]" -type "float3" -1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[490]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[491]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[492]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[493]" -type "float3" 1.8626451e-09 -1.4901161e-08 0 ;
	setAttr ".pt[494]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[495]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[496]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[497]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[499]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[500]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[502]" -type "float3" -1.4901161e-08 -1.4901161e-08 0 ;
	setAttr ".pt[503]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[504]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[505]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[506]" -type "float3" -1.4901161e-08 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[507]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[508]" -type "float3" 0 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[509]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[510]" -type "float3" 7.4505806e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[511]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[512]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[513]" -type "float3" -1.8626451e-09 -1.4901161e-08 1.4901161e-08 ;
	setAttr ".pt[514]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[516]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[518]" -type "float3" 0 -1.4901161e-08 7.4505806e-09 ;
	setAttr ".pt[519]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[520]" -type "float3" 0 -1.4901161e-08 4.6566129e-10 ;
	setAttr ".pt[521]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[522]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[524]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[526]" -type "float3" 7.4505806e-09 -1.4901161e-08 0 ;
	setAttr ".pt[527]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[528]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[530]" -type "float3" -1.8626451e-09 -1.4901161e-08 -1.4901161e-08 ;
	setAttr ".pt[531]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[532]" -type "float3" 1.8626451e-09 -1.4901161e-08 -2.9802322e-08 ;
	setAttr ".pt[533]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[534]" -type "float3" -1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[535]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[536]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[537]" -type "float3" 0 -1.4901161e-08 0 ;
	setAttr ".pt[539]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[540]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[541]" -type "float3" 0 -1.4901161e-08 -5.9604645e-08 ;
	setAttr ".pt[542]" -type "float3" 1.8626451e-09 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[543]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[544]" -type "float3" 3.6379788e-12 -1.4901161e-08 2.9802322e-08 ;
	setAttr ".pt[545]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[548]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[550]" -type "float3" -5.9604645e-08 0 2.3283064e-10 ;
	setAttr ".pt[551]" -type "float3" 5.9604645e-08 0 -1.4901161e-08 ;
	setAttr ".pt[552]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[553]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[554]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[555]" -type "float3" 0 0 -5.9604645e-08 ;
	setAttr ".pt[556]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[557]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[558]" -type "float3" -5.9604645e-08 0 2.3283064e-10 ;
	setAttr ".pt[559]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[560]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[562]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[563]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[564]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[565]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[566]" -type "float3" 1.8626451e-09 0 0 ;
	setAttr ".pt[568]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[570]" -type "float3" -1.4901161e-08 0 0 ;
	setAttr ".pt[571]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[572]" -type "float3" -1.4901161e-08 0 7.4505806e-09 ;
	setAttr ".pt[573]" -type "float3" 0 0 -1.4901161e-08 ;
	setAttr ".pt[574]" -type "float3" 7.4505806e-09 0 1.4901161e-08 ;
	setAttr ".pt[575]" -type "float3" -1.8626451e-09 0 1.4901161e-08 ;
	setAttr ".pt[578]" -type "float3" 0 0 7.4505806e-09 ;
	setAttr ".pt[579]" -type "float3" 0 0 4.6566129e-10 ;
	setAttr ".pt[582]" -type "float3" 7.4505806e-09 0 0 ;
	setAttr ".pt[584]" -type "float3" -1.8626451e-09 0 -1.4901161e-08 ;
	setAttr ".pt[585]" -type "float3" 1.8626451e-09 0 -2.9802322e-08 ;
	setAttr ".pt[586]" -type "float3" -1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[587]" -type "float3" -1.8626451e-09 0 0 ;
	setAttr ".pt[589]" -type "float3" 1.8626451e-09 0 5.9604645e-08 ;
	setAttr ".pt[590]" -type "float3" 1.8626451e-09 0 2.9802322e-08 ;
	setAttr ".pt[591]" -type "float3" 3.6379788e-12 0 2.9802322e-08 ;
	setAttr ".pt[592]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[593]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[594]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[595]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[596]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[597]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[598]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[601]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[602]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[604]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[605]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[606]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[607]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[608]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[609]" -type "float3" 2.9802322e-08 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[611]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[612]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[613]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[614]" -type "float3" 2.9802322e-08 -7.4505806e-09 0 ;
	setAttr ".pt[616]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[617]" -type "float3" 2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[619]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[620]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[623]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[625]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[626]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[629]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[631]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[632]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[633]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[636]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[637]" -type "float3" -5.9604645e-08 7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[639]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[640]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[641]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[642]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[643]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[644]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[645]" -type "float3" -5.9604645e-08 7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[646]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[647]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[649]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[651]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[652]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[653]" -type "float3" 0 -7.4505806e-09 0 ;
	setAttr ".pt[658]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[660]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[662]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[663]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[664]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[666]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[667]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[668]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[669]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[670]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[671]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[675]" -type "float3" 0 3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[676]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[677]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[679]" -type "float3" 0 3.7252903e-09 0 ;
	setAttr ".pt[680]" -type "float3" 0 3.7252903e-09 0 ;
	setAttr ".pt[681]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[684]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[685]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[686]" -type "float3" 0 3.7252903e-09 0 ;
	setAttr ".pt[691]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[692]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[693]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[695]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[697]" -type "float3" 0 1.8626451e-09 2.9802322e-08 ;
	setAttr ".pt[700]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[701]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[702]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[703]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[705]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[706]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[707]" -type "float3" 0 1.8626451e-09 -2.9802322e-08 ;
	setAttr ".pt[709]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[710]" -type "float3" 0 1.8626451e-09 2.9802322e-08 ;
	setAttr ".pt[711]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[713]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[714]" -type "float3" 0 1.8626451e-09 0 ;
	setAttr ".pt[720]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[721]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[722]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[723]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[724]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[725]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[726]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[728]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[729]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[730]" -type "float3" -2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[731]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[732]" -type "float3" -2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[733]" -type "float3" 2.9802322e-08 7.4505806e-09 0 ;
	setAttr ".pt[734]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[735]" -type "float3" 2.9802322e-08 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[737]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[738]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[739]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[740]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[741]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[744]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[745]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[747]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[748]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[749]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[750]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[751]" -type "float3" 2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[752]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[753]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[754]" -type "float3" 0 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[755]" -type "float3" 2.9802322e-08 -7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[756]" -type "float3" -2.9802322e-08 7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[757]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[758]" -type "float3" -2.9802322e-08 -7.4505806e-09 0 ;
	setAttr ".pt[759]" -type "float3" 0 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[760]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[761]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[762]" -type "float3" -2.9802322e-08 0 0 ;
	setAttr ".pt[763]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[764]" -type "float3" -2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[766]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[767]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[768]" -type "float3" -5.9604645e-08 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[769]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[770]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[771]" -type "float3" -5.9604645e-08 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[772]" -type "float3" 5.9604645e-08 7.4505806e-09 0 ;
	setAttr ".pt[773]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[774]" -type "float3" -5.9604645e-08 -7.4505806e-09 -2.9802322e-08 ;
	setAttr ".pt[775]" -type "float3" 5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[776]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[777]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[778]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[779]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[780]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[781]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[782]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[783]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[784]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[785]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[786]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[787]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[788]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[789]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[790]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[791]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[792]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[794]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[795]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[796]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[797]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[798]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[799]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[800]" -type "float3" 2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[801]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[803]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[804]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[805]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[806]" -type "float3" 0 7.4505806e-09 0 ;
	setAttr ".pt[807]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[808]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[809]" -type "float3" -5.9604645e-08 -7.4505806e-09 0 ;
	setAttr ".pt[810]" -type "float3" 5.9604645e-08 7.4505806e-09 0 ;
	setAttr ".pt[811]" -type "float3" 5.9604645e-08 -7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[812]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[813]" -type "float3" 5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[814]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[815]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[816]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[817]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[818]" -type "float3" 2.9802322e-08 -7.4505806e-09 0 ;
	setAttr ".pt[819]" -type "float3" 2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[820]" -type "float3" 2.9802322e-08 0 -2.9802322e-08 ;
	setAttr ".pt[821]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[822]" -type "float3" 2.9802322e-08 0 0 ;
	setAttr ".pt[824]" -type "float3" -2.9802322e-08 0 2.9802322e-08 ;
	setAttr ".pt[825]" -type "float3" -2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[827]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[829]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[831]" -type "float3" -2.9802322e-08 -3.7252903e-09 0 ;
	setAttr ".pt[833]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[834]" -type "float3" 0 7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[836]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[837]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[838]" -type "float3" 0 7.4505806e-09 2.9802322e-08 ;
	setAttr ".pt[839]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[840]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[842]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[843]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[845]" -type "float3" -5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[846]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[847]" -type "float3" 0 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[848]" -type "float3" 0 -1.8626451e-09 -2.9802322e-08 ;
	setAttr ".pt[851]" -type "float3" 0 -1.8626451e-09 0 ;
	setAttr ".pt[852]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[854]" -type "float3" 0 -3.7252903e-09 0 ;
	setAttr ".pt[855]" -type "float3" 0 0 -2.9802322e-08 ;
	setAttr ".pt[856]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[857]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[858]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[859]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[860]" -type "float3" 5.9604645e-08 3.7252903e-09 0 ;
	setAttr ".pt[861]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[862]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[863]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[864]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[865]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[866]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[867]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[868]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[869]" -type "float3" -5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[870]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[871]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[872]" -type "float3" 0 0 2.9802322e-08 ;
	setAttr ".pt[873]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[874]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[875]" -type "float3" 5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[876]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[877]" -type "float3" 5.9604645e-08 -3.7252903e-09 -2.9802322e-08 ;
	setAttr ".pt[878]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[879]" -type "float3" 0 -3.7252903e-09 2.9802322e-08 ;
	setAttr ".pt[880]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[881]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[882]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[883]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[884]" -type "float3" -5.9604645e-08 0 -2.9802322e-08 ;
	setAttr ".pt[885]" -type "float3" -5.9604645e-08 0 2.9802322e-08 ;
	setAttr ".pt[886]" -type "float3" 5.9604645e-08 -3.7252903e-09 0 ;
	setAttr ".pt[887]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[888]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[889]" -type "float3" 5.9604645e-08 1.8626451e-09 0 ;
	setAttr ".pt[890]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[891]" -type "float3" 5.9604645e-08 1.8626451e-09 0 ;
	setAttr ".pt[892]" -type "float3" -5.9604645e-08 0 0 ;
	setAttr ".pt[893]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[894]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[895]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr ".pt[896]" -type "float3" 5.9604645e-08 0 0 ;
	setAttr -s 898 ".vt";
	setAttr ".vt[0:165]"  -0.043006547 -0.25657469 0.35259426 -0.13581344 -0.25657469 0.33414412
		 -0.11196893 -0.25657469 0.27656347 -0.04301044 -0.25657469 0.29029223 -0.25098059 -0.25657469 0.25717646
		 -0.20693783 -0.25657469 0.21313561 -0.32790929 -0.25657469 0.14206378 -0.2703647 -0.25657469 0.11821736
		 -0.35493648 -0.25657469 0.0062104333 -0.29263538 -0.25657469 0.0062075122 -0.32790929 -0.25657469 -0.12960689
		 -0.2703647 -0.25657469 -0.10575802 -0.25097281 -0.25657469 -0.24476333 -0.20693004 -0.25657469 -0.20067775
		 -0.13580953 -0.25657469 -0.32169062 -0.11196893 -0.25657469 -0.26415622 -0.04300265 -0.25657469 -0.34012812
		 -0.04300265 -0.25657469 -0.27788451 0.04300265 -0.25657469 -0.34012681 0.13580564 -0.25657469 -0.32168925
		 0.11196116 -0.25657469 -0.2641522 0.04300265 -0.25657469 -0.27788389 0.25097668 -0.25657469 -0.24475798
		 0.20693004 -0.25657469 -0.20066957 0.32790154 -0.25657469 -0.12960099 0.27035689 -0.25657469 -0.10575059
		 0.35494423 -0.25657469 0.0062153027 0.29263929 -0.25657469 0.0062156683 0.32790154 -0.25657469 0.1420745
		 0.27035689 -0.25657469 0.11822467 0.25098059 -0.25657469 0.2571876 0.20693004 -0.25657469 0.21314073
		 0.13579786 -0.25657469 0.33414558 0.11196505 -0.25657469 0.2765649 0.042998753 -0.25657469 0.35259718
		 0.042998753 -0.25657469 0.29029369 -0.042593621 -0.25657469 0.59475732 -0.22848007 -0.25657469 0.55781907
		 -0.42214975 -0.25657469 0.4283962 -0.5515784 -0.25657469 0.23466226 -0.59700418 -0.25657469 0.0062065385
		 -0.55157065 -0.25657469 -0.22222774 -0.4221459 -0.25657469 -0.4159413 -0.22847617 -0.25657469 -0.54535997
		 -0.04281956 -0.25657469 -0.58651853 0.042835139 -0.25657469 -0.58651853 0.22848786 -0.25657469 -0.54535335
		 0.4221459 -0.25657469 -0.41592908 0.55157065 -0.25657469 -0.22221118 0.59700418 -0.25657469 0.0062240679
		 0.55156672 -0.25657469 0.23468113 0.42214194 -0.25657469 0.42840108 0.22848007 -0.25657469 0.55782294
		 0.04260141 -0.25657469 0.59475929 -0.00076352194 -0.25657469 -0.81208056 0.31494892 -0.25657469 -0.75415033
		 0.58193231 -0.25657469 -0.57572091 0.76035494 -0.25657469 -0.3087239 0.82299882 -0.25657469 0.0062260162
		 0.76035106 -0.25657469 0.32120684 0.58192062 -0.25657469 0.5881871 0.31492946 -0.25657469 0.7665931
		 0.042188488 -0.25657469 0.82085234 -0.042250816 -0.25657469 0.81208056 -0.31161827 -0.25657469 0.75850457
		 -0.57577348 -0.25657469 0.5819732 -0.75229901 -0.25657469 0.31781992 -0.81428069 -0.25657469 0.0062006945
		 -0.7522912 -0.25657469 -0.30536985 -0.57576573 -0.25657469 -0.56957567 -0.31159878 -0.25657469 -0.74604821
		 -0.042196278 -0.25657469 0.83695841 -0.042562455 -0.24546282 0.84392649 -0.32399821 -0.24546282 0.78796154
		 -0.32110775 -0.25657469 0.78144139 -0.59867525 -0.24546282 0.60441923 -0.59336567 -0.25657469 0.59955955
		 -0.78221661 -0.24546282 0.32977918 -0.77523977 -0.25657469 0.327362 -0.84663296 -0.24546282 0.0057975082
		 -0.8391223 -0.25657469 0.0062026423 -0.78220487 -0.24546282 -0.31820267 -0.77523589 -0.25657469 -0.31489828
		 -0.59865969 -0.24546282 -0.59286559 -0.59335786 -0.25657469 -0.58710063 -0.32398653 -0.24546282 -0.77640373
		 -0.32109219 -0.25657469 -0.76902294 7.7910408e-06 -0.24546282 -0.84081984 1.5582082e-05 -0.25657469 -0.83291149
		 0.32399434 -0.24546282 -0.77639669 0.32111943 -0.25657469 -0.76901954 0.59862465 -0.24546282 -0.59285057
		 0.59331113 -0.25657469 -0.58709049 0.78216213 -0.24546282 -0.31818223 0.77523196 -0.25657469 -0.3148759
		 0.84662122 -0.24546282 0.0058145514 0.83911848 -0.25657469 0.0062196855 0.78215033 -0.24546282 0.32979476
		 0.77522415 -0.25657469 0.32737735 0.59861684 -0.24546282 0.60443568 0.59330332 -0.25657469 0.59957027
		 0.32397485 -0.24546282 0.78796834 0.32110775 -0.25657469 0.78145307 0.042539082 -0.24546282 0.84392852
		 0.042188488 -0.25657469 0.83696127 0.042998753 -0.24546282 0.35259718 0.042998753 -0.24546282 0.29029369
		 -0.04300265 -0.24546282 -0.34012812 -0.04300265 -0.24546282 -0.27788451 -0.11196893 -0.24546282 0.27656347
		 -0.04301044 -0.24546282 0.29029223 -0.20693783 -0.24546282 0.21313561 -0.2703647 -0.24546282 0.11821736
		 -0.29263538 -0.24546282 0.0062075122 -0.2703647 -0.24546282 -0.10575802 -0.20693004 -0.24546282 -0.20067775
		 -0.11196893 -0.24546282 -0.26415622 0.11196116 -0.24546282 -0.2641522 0.04300265 -0.24546282 -0.27788389
		 0.20693004 -0.24546282 -0.20066957 0.27035689 -0.24546282 -0.10575059 0.29263929 -0.24546282 0.0062156683
		 0.27035689 -0.24546282 0.11822467 0.20693004 -0.24546282 0.21314073 0.11196505 -0.24546282 0.2765649
		 -0.043006547 -0.24546282 0.35259426 0.04300265 -0.24546282 -0.34012681 -0.042593621 -0.24546282 0.59475732
		 0.042835139 -0.24546282 -0.58651853 0.042546876 -0.24546282 0.82737929 0.04260141 -0.24546282 0.59475929
		 -0.0426092 -0.24546282 0.81836504 -0.04281956 -0.24546282 -0.58651853 5.0641767e-05 -0.24546282 -0.59692073
		 5.0641767e-05 -0.25657469 -0.59692073 -0.043832395 -0.20844053 0.86722857 -0.043832395 -0.19260623 0.86722857
		 -0.33358121 -0.19260623 0.80959141 -0.33358121 -0.20844053 0.80959141 -0.61631417 -0.19260623 0.6206674
		 -0.61631417 -0.20844053 0.6206674 -0.80523908 -0.19260623 0.33787212 -0.80523908 -0.20844053 0.33787212
		 -0.87159544 -0.19260623 0.0043483749 -0.87159544 -0.20844053 0.0043483749 -0.80523521 -0.19260623 -0.32920459
		 -0.80523521 -0.20844053 -0.32920459 -0.61629868 -0.19260623 -0.61193717 -0.61629868 -0.20844053 -0.61193717
		 -0.33356172 -0.19260623 -0.80087459 -0.33356172 -0.20844053 -0.80087459 1.5582082e-05 -0.19260623 -0.86723262
		 1.5582082e-05 -0.20844053 -0.86723262 0.33352667 -0.19260623 -0.80086303 0.33352667 -0.20844053 -0.80086303
		 0.61630642 -0.19260623 -0.61192101 0.61630642 -0.20844053 -0.61192101 0.80524302 -0.19260623 -0.32918805
		 0.80524302 -0.20844053 -0.32918805 0.87159932 -0.19260623 0.0043678521 0.87159932 -0.20844053 0.0043678521
		 0.80523521 -0.19260623 0.33788913 0.80523521 -0.20844053 0.33788913 0.61630249 -0.19260623 0.62067813
		 0.61630249 -0.20844053 0.62067813 0.33351886 -0.19260623 0.80959821;
	setAttr ".vt[166:331]" 0.33351886 -0.20844053 0.80959821 0.043816812 -0.19260623 0.86723244
		 0.043816812 -0.20844053 0.86723244 0.042998753 -0.20844053 0.35259718 0.042998753 -0.19260623 0.35259718
		 0.042998753 -0.19260623 0.29029369 0.042998753 -0.20844053 0.29029369 -0.04300265 -0.20844053 -0.34012812
		 -0.04300265 -0.19260623 -0.34012812 -0.04300265 -0.19260623 -0.27788451 -0.04300265 -0.20844053 -0.27788451
		 -0.11196893 -0.20844053 0.27656347 -0.11196893 -0.19260623 0.27656347 -0.04301044 -0.19260623 0.29029223
		 -0.04301044 -0.20844053 0.29029223 -0.20693783 -0.20844053 0.21313561 -0.20693783 -0.19260623 0.21313561
		 -0.2703647 -0.20844053 0.11821736 -0.2703647 -0.19260623 0.11821736 -0.29263538 -0.20844053 0.0062075122
		 -0.29263538 -0.19260623 0.0062075122 -0.2703647 -0.20844053 -0.10575802 -0.2703647 -0.19260623 -0.10575802
		 -0.20693004 -0.20844053 -0.20067775 -0.20693004 -0.19260623 -0.20067775 -0.11196893 -0.20844053 -0.26415622
		 -0.11196893 -0.19260623 -0.26415622 0.11196116 -0.20844053 -0.2641522 0.11196116 -0.19260623 -0.2641522
		 0.04300265 -0.19260623 -0.27788389 0.04300265 -0.20844053 -0.27788389 0.20693004 -0.20844053 -0.20066957
		 0.20693004 -0.19260623 -0.20066957 0.27035689 -0.20844053 -0.10575059 0.27035689 -0.19260623 -0.10575059
		 0.29263929 -0.20844053 0.0062156683 0.29263929 -0.19260623 0.0062156683 0.27035689 -0.20844053 0.11822467
		 0.27035689 -0.19260623 0.11822467 0.20693004 -0.20844053 0.21314073 0.20693004 -0.19260623 0.21314073
		 0.11196505 -0.20844053 0.2765649 0.11196505 -0.19260623 0.2765649 -0.043006547 -0.19260623 0.35259426
		 -0.043006547 -0.20844053 0.35259426 0.04300265 -0.19260623 -0.34012681 0.04300265 -0.20844053 -0.34012681
		 -0.042593621 -0.19260623 0.59475732 -0.042593621 -0.20844053 0.59475732 0.042835139 -0.19260623 -0.58651853
		 0.042835139 -0.20844053 -0.58651853 0.043723322 -0.20844053 0.84910071 0.043723322 -0.19260623 0.84910071
		 0.04260141 -0.19260623 0.59475929 0.04260141 -0.20844053 0.59475929 -0.043731112 -0.19260623 0.83925283
		 -0.043731112 -0.20844053 0.83925283 -0.04281956 -0.20844053 -0.58651853 -0.04281956 -0.19260623 -0.58651853
		 5.0641767e-05 -0.19260623 -0.59692073 5.0641767e-05 -0.20844053 -0.59692073 -0.043645412 -0.21397471 0.86376828
		 -0.33214766 -0.21397471 0.80637175 -0.61370808 -0.21397471 0.6182307 -0.80183047 -0.21397471 0.3366645
		 -0.86791021 -0.21397471 0.0045168558 -0.80182278 -0.21397471 -0.32754996 -0.61368859 -0.21397471 -0.60911429
		 -0.33212039 -0.21397471 -0.79723138 1.5582082e-05 -0.21397471 -0.86332285 0.33213207 -0.21397471 -0.79722315
		 0.61364567 -0.21397471 -0.60909379 0.80183047 -0.21397471 -0.32752562 0.86786735 -0.21397471 0.0045324387
		 0.80181503 -0.21397471 0.33668301 0.61363792 -0.21397471 0.61824512 0.33210871 -0.21397471 0.80637848
		 0.043622039 -0.21397471 0.86378098 0.042998753 -0.21397471 0.35259718 0.042998753 -0.21397471 0.29029369
		 -0.04300265 -0.21397471 -0.34012812 -0.04300265 -0.21397471 -0.27788451 -0.11196893 -0.21397471 0.27656347
		 -0.04301044 -0.21397471 0.29029223 -0.20693783 -0.21397471 0.21313561 -0.2703647 -0.21397471 0.11821736
		 -0.29263538 -0.21397471 0.0062075122 -0.2703647 -0.21397471 -0.10575802 -0.20693004 -0.21397471 -0.20067775
		 -0.11196893 -0.21397471 -0.26415622 0.11196116 -0.21397471 -0.2641522 0.04300265 -0.21397471 -0.27788389
		 0.20693004 -0.21397471 -0.20066957 0.27035689 -0.21397471 -0.10575059 0.29263929 -0.21397471 0.0062156683
		 0.27035689 -0.21397471 0.11822467 0.20693004 -0.21397471 0.21314073 0.11196505 -0.21397471 0.2765649
		 -0.043006547 -0.21397471 0.35259426 0.04300265 -0.21397471 -0.34012681 -0.042593621 -0.21397471 0.59475732
		 0.042835139 -0.21397471 -0.58651853 0.043536335 -0.21397471 0.8458733 0.04260141 -0.21397471 0.59475929
		 -0.043551918 -0.21397471 0.83613843 -0.04281956 -0.21397471 -0.58651853 5.0641767e-05 -0.21397471 -0.59692073
		 -0.043832395 -2.3860061e-05 0.86722857 -0.33358121 -2.3860061e-05 0.80959141 -0.61631417 -2.3860061e-05 0.6206674
		 -0.80523908 -2.3860061e-05 0.33787212 -0.87159544 -2.3860061e-05 0.0043483749 -0.80523521 -2.3860061e-05 -0.32920459
		 -0.61629868 -2.3860061e-05 -0.61193717 -0.33356172 -2.3860061e-05 -0.80087459 1.5582082e-05 -2.3860061e-05 -0.86723262
		 0.33352667 -2.3860061e-05 -0.80086303 0.61630642 -2.3860061e-05 -0.61192101 0.80524302 -2.3860061e-05 -0.32918805
		 0.87159932 -2.3860061e-05 0.0043678521 0.80523521 -2.3860061e-05 0.33788913 0.61630249 -2.3860061e-05 0.62067813
		 0.33351886 -2.3860061e-05 0.80959821 0.043816812 -2.3860061e-05 0.86723244 0.042998753 -2.3860061e-05 0.35259718
		 0.042998753 -2.3860061e-05 0.29029369 -0.04300265 -2.3860061e-05 -0.34012812 -0.04300265 -2.3860061e-05 -0.27788451
		 -0.11196893 -2.3860061e-05 0.27656347 -0.04301044 -2.3860061e-05 0.29029223 -0.20693783 -2.3860061e-05 0.21313561
		 -0.2703647 -2.3860061e-05 0.11821736 -0.29263538 -2.3860061e-05 0.0062075122 -0.2703647 -2.3860061e-05 -0.10575802
		 -0.20693004 -2.3860061e-05 -0.20067775 -0.11196893 -2.3860061e-05 -0.26415622 0.11196116 -2.3860061e-05 -0.2641522
		 0.04300265 -2.3860061e-05 -0.27788389 0.20693004 -2.3860061e-05 -0.20066957 0.27035689 -2.3860061e-05 -0.10575059
		 0.29263929 -2.3860061e-05 0.0062156683 0.27035689 -2.3860061e-05 0.11822467 0.20693004 -2.3860061e-05 0.21314073
		 0.11196505 -2.3860061e-05 0.2765649 -0.043006547 -2.3860061e-05 0.35259426 0.04300265 -2.3860061e-05 -0.34012681
		 -0.042593621 -2.3860061e-05 0.59475732 0.042835139 -2.3860061e-05 -0.58651853 0.043723322 -2.3860061e-05 0.84910071
		 0.04260141 -2.3860061e-05 0.59475929 -0.043731112 -2.3860061e-05 0.83925283 -0.04281956 -2.3860061e-05 -0.58651853
		 5.0641767e-05 -2.3860061e-05 -0.59692073 -0.043006547 0.25657457 0.35259426 -0.04301044 0.25657457 0.29029223
		 -0.11196893 0.25657457 0.27656347 -0.13581344 0.25657457 0.33414412 -0.20693783 0.25657457 0.21313561
		 -0.25098059 0.25657457 0.25717646 -0.2703647 0.25657457 0.11821736 -0.32790929 0.25657457 0.14206378
		 -0.29263538 0.25657457 0.0062075122 -0.35493648 0.25657457 0.0062104333 -0.2703647 0.25657457 -0.10575802
		 -0.32790929 0.25657457 -0.12960689 -0.20693004 0.25657457 -0.20067775;
	setAttr ".vt[332:497]" -0.25097281 0.25657457 -0.24476333 -0.11196893 0.25657457 -0.26415622
		 -0.13580953 0.25657457 -0.32169062 -0.04300265 0.25657457 -0.27788451 -0.04300265 0.25657457 -0.34012812
		 0.04300265 0.25657457 -0.34012681 0.04300265 0.25657457 -0.27788389 0.11196116 0.25657457 -0.2641522
		 0.13580564 0.25657457 -0.32168925 0.20693004 0.25657457 -0.20066957 0.25097668 0.25657457 -0.24475798
		 0.27035689 0.25657457 -0.10575059 0.32790154 0.25657457 -0.12960099 0.29263929 0.25657457 0.0062156683
		 0.35494423 0.25657457 0.0062153027 0.27035689 0.25657457 0.11822467 0.32790154 0.25657457 0.1420745
		 0.20693004 0.25657457 0.21314073 0.25098059 0.25657457 0.2571876 0.11196505 0.25657457 0.2765649
		 0.13579786 0.25657457 0.33414558 0.042998753 0.25657457 0.29029369 0.042998753 0.25657457 0.35259718
		 -0.22848007 0.25657457 0.55781907 -0.042593621 0.25657457 0.59475732 -0.42214975 0.25657457 0.4283962
		 -0.5515784 0.25657457 0.23466226 -0.59700418 0.25657457 0.0062065385 -0.55157065 0.25657457 -0.22222774
		 -0.4221459 0.25657457 -0.4159413 -0.22847617 0.25657457 -0.54535997 -0.04281956 0.25657457 -0.58651853
		 0.22848786 0.25657457 -0.54535335 0.042835139 0.25657457 -0.58651853 0.4221459 0.25657457 -0.41592908
		 0.55157065 0.25657457 -0.22221118 0.59700418 0.25657457 0.0062240679 0.55156672 0.25657457 0.23468113
		 0.42214194 0.25657457 0.42840108 0.22848007 0.25657457 0.55782294 0.04260141 0.25657457 0.59475929
		 0.31494892 0.25657457 -0.75415033 -0.00076352194 0.25657457 -0.81208056 0.58193231 0.25657457 -0.57572091
		 0.76035494 0.25657457 -0.3087239 0.82299882 0.25657457 0.0062260162 0.76035106 0.25657457 0.32120684
		 0.58192062 0.25657457 0.5881871 0.31492946 0.25657457 0.7665931 0.042188488 0.25657457 0.82085234
		 -0.042250816 0.25657457 0.81208056 -0.31161827 0.25657457 0.75850457 -0.57577348 0.25657457 0.5819732
		 -0.75229901 0.25657457 0.31781992 -0.81428069 0.25657457 0.0062006945 -0.7522912 0.25657457 -0.30536985
		 -0.57576573 0.25657457 -0.56957567 -0.31159878 0.25657457 -0.74604821 -0.042196278 0.25657457 0.83695841
		 -0.32110775 0.25657457 0.78144139 -0.32399821 0.24541779 0.78796154 -0.042562455 0.24541779 0.84392649
		 -0.59336567 0.25657457 0.59955955 -0.59867525 0.24541779 0.60441923 -0.77523977 0.25657457 0.327362
		 -0.78221661 0.24541779 0.32977918 -0.8391223 0.25657457 0.0062026423 -0.84663296 0.24541779 0.0057975082
		 -0.77523589 0.25657457 -0.31489828 -0.78220487 0.24541779 -0.31820267 -0.59335786 0.25657457 -0.58710063
		 -0.59865969 0.24541779 -0.59286559 -0.32109219 0.25657457 -0.76902294 -0.32398653 0.24541779 -0.77640373
		 1.5582082e-05 0.25657457 -0.83291149 7.7910408e-06 0.24541779 -0.84081984 0.32111943 0.25657457 -0.76901954
		 0.32399434 0.24541779 -0.77639669 0.59331113 0.25657457 -0.58709049 0.59862465 0.24541779 -0.59285057
		 0.77523196 0.25657457 -0.3148759 0.78216213 0.24541779 -0.31818223 0.83911848 0.25657457 0.0062196855
		 0.84662122 0.24541779 0.0058145514 0.77522415 0.25657457 0.32737735 0.78215033 0.24541779 0.32979476
		 0.59330332 0.25657457 0.59957027 0.59861684 0.24541779 0.60443568 0.32110775 0.25657457 0.78145307
		 0.32397485 0.24541779 0.78796834 0.042188488 0.25657457 0.83696127 0.042539082 0.24541779 0.84392852
		 0.042998753 0.24541779 0.29029369 0.042998753 0.24541779 0.35259718 -0.04300265 0.24541779 -0.27788451
		 -0.04300265 0.24541779 -0.34012812 -0.04301044 0.24541779 0.29029223 -0.11196893 0.24541779 0.27656347
		 -0.20693783 0.24541779 0.21313561 -0.2703647 0.24541779 0.11821736 -0.29263538 0.24541779 0.0062075122
		 -0.2703647 0.24541779 -0.10575802 -0.20693004 0.24541779 -0.20067775 -0.11196893 0.24541779 -0.26415622
		 0.04300265 0.24541779 -0.27788389 0.11196116 0.24541779 -0.2641522 0.20693004 0.24541779 -0.20066957
		 0.27035689 0.24541779 -0.10575059 0.29263929 0.24541779 0.0062156683 0.27035689 0.24541779 0.11822467
		 0.20693004 0.24541779 0.21314073 0.11196505 0.24541779 0.2765649 -0.043006547 0.24541779 0.35259426
		 0.04300265 0.24541779 -0.34012681 -0.042593621 0.24541779 0.59475732 0.042835139 0.24541779 -0.58651853
		 0.04260141 0.24541779 0.59475929 0.042546876 0.24541779 0.82737929 -0.0426092 0.24541779 0.81836504
		 -0.04281956 0.24541779 -0.58651853 5.0641767e-05 0.25657457 -0.59692073 5.0641767e-05 0.24541779 -0.59692073
		 -0.043832395 0.208441 0.86722857 -0.33358121 0.208441 0.80959141 -0.33358121 0.19255899 0.80959141
		 -0.043832395 0.19255899 0.86722857 -0.61631417 0.208441 0.6206674 -0.61631417 0.19255899 0.6206674
		 -0.80523908 0.208441 0.33787212 -0.80523908 0.19256093 0.33787212 -0.87159544 0.208441 0.0043483749
		 -0.87159544 0.19256093 0.0043483749 -0.80523521 0.208441 -0.32920459 -0.80523521 0.19256093 -0.32920459
		 -0.61629868 0.208441 -0.61193717 -0.61629868 0.19255899 -0.61193717 -0.33356172 0.208441 -0.80087459
		 -0.33356172 0.19255899 -0.80087459 1.5582082e-05 0.208441 -0.86723262 1.5582082e-05 0.19255899 -0.86723262
		 0.33352667 0.208441 -0.80086303 0.33352667 0.19255899 -0.80086303 0.61630642 0.208441 -0.61192101
		 0.61630642 0.19255899 -0.61192101 0.80524302 0.2084381 -0.32918805 0.80524302 0.19255899 -0.32918805
		 0.87159932 0.2084381 0.0043678521 0.87159932 0.19255899 0.0043678521 0.80523521 0.2084381 0.33788913
		 0.80523521 0.19255899 0.33788913 0.61630249 0.208441 0.62067813 0.61630249 0.19255899 0.62067813
		 0.33351886 0.208441 0.80959821 0.33351886 0.19255899 0.80959821 0.043816812 0.208441 0.86723244
		 0.043816812 0.19255899 0.86723244 0.042998753 0.208441 0.35259718 0.042998753 0.208441 0.29029369
		 0.042998753 0.19255899 0.29029369 0.042998753 0.19255899 0.35259718 -0.04300265 0.208441 -0.34012812
		 -0.04300265 0.208441 -0.27788451 -0.04300265 0.19255899 -0.27788451 -0.04300265 0.19255899 -0.34012812
		 -0.11196893 0.208441 0.27656347 -0.04301044 0.208441 0.29029223;
	setAttr ".vt[498:663]" -0.04301044 0.19255899 0.29029223 -0.11196893 0.19255899 0.27656347
		 -0.20693783 0.208441 0.21313561 -0.20693783 0.19255899 0.21313561 -0.2703647 0.208441 0.11821736
		 -0.2703647 0.19255899 0.11821736 -0.29263538 0.208441 0.0062075122 -0.29263538 0.19255899 0.0062075122
		 -0.2703647 0.208441 -0.10575802 -0.2703647 0.19255899 -0.10575802 -0.20693004 0.208441 -0.20067775
		 -0.20693004 0.19255899 -0.20067775 -0.11196893 0.208441 -0.26415622 -0.11196893 0.19255899 -0.26415622
		 0.11196116 0.208441 -0.2641522 0.04300265 0.208441 -0.27788389 0.04300265 0.19255899 -0.27788389
		 0.11196116 0.19255899 -0.2641522 0.20693004 0.208441 -0.20066957 0.20693004 0.19255899 -0.20066957
		 0.27035689 0.208441 -0.10575059 0.27035689 0.19255899 -0.10575059 0.29263929 0.208441 0.0062156683
		 0.29263929 0.19255899 0.0062156683 0.27035689 0.208441 0.11822467 0.27035689 0.19255899 0.11822467
		 0.20693004 0.208441 0.21314073 0.20693004 0.19255899 0.21314073 0.11196505 0.208441 0.2765649
		 0.11196505 0.19255899 0.2765649 -0.043006547 0.208441 0.35259426 -0.043006547 0.19255899 0.35259426
		 0.04300265 0.208441 -0.34012681 0.04300265 0.19255899 -0.34012681 -0.042593621 0.208441 0.59475732
		 -0.042593621 0.19255899 0.59475732 0.042835139 0.208441 -0.58651853 0.042835139 0.19255899 -0.58651853
		 0.043723322 0.208441 0.84910071 0.04260141 0.208441 0.59475929 0.04260141 0.19255899 0.59475929
		 0.043723322 0.19255899 0.84910071 -0.043731112 0.19255899 0.83925283 -0.043731112 0.208441 0.83925283
		 -0.04281956 0.208441 -0.58651853 -0.04281956 0.19255899 -0.58651853 5.0641767e-05 0.208441 -0.59692073
		 5.0641767e-05 0.19255899 -0.59692073 -0.33169577 0.2155484 0.80541641 -0.043606456 0.2155484 0.86273313
		 -0.61289001 0.2155484 0.61751592 -0.80079043 0.2155484 0.3362847 -0.86678451 0.2155484 0.0046298262
		 -0.8007865 0.2155484 -0.32709515 -0.61287832 0.2155484 -0.60825539 -0.3316724 0.2155484 -0.79616213
		 1.5582082e-05 0.2155484 -0.86215466 0.33168018 0.2155484 -0.79615384 0.61289001 0.2155484 -0.6082378
		 0.80078262 0.2155484 -0.32707569 0.86673766 0.2155484 0.0046454081 0.80077875 0.2155484 0.33630121
		 0.61287439 0.2155484 0.61753154 0.3316724 0.2155484 0.80542856 0.043583088 0.2155484 0.862737
		 0.042998753 0.2155484 0.29029369 0.042998753 0.2155484 0.35259718 -0.04300265 0.2155484 -0.27788451
		 -0.04300265 0.2155484 -0.34012812 -0.04301044 0.2155484 0.29029223 -0.11196893 0.2155484 0.27656347
		 -0.20693783 0.2155484 0.21313561 -0.2703647 0.2155484 0.11821736 -0.29263538 0.2155484 0.0062075122
		 -0.2703647 0.2155484 -0.10575802 -0.20693004 0.2155484 -0.20067775 -0.11196893 0.2155484 -0.26415622
		 0.04300265 0.2155484 -0.27788389 0.11196116 0.2155484 -0.2641522 0.20693004 0.2155484 -0.20066957
		 0.27035689 0.2155484 -0.10575059 0.29263929 0.2155484 0.0062156683 0.27035689 0.2155484 0.11822467
		 0.20693004 0.2155484 0.21314073 0.11196505 0.2155484 0.2765649 -0.043006547 0.2155484 0.35259426
		 0.04300265 0.2155484 -0.34012681 -0.042593621 0.2155484 0.59475732 0.042835139 0.2155484 -0.58651853
		 0.043497376 0.2155484 0.84491014 0.04260141 0.2155484 0.59475929 -0.043505169 0.2155484 0.8352055
		 -0.04281956 0.2155484 -0.58651853 5.0641767e-05 0.2155484 -0.59692073 -0.70803416 -0.092737243 0.69322538
		 -0.69705272 -0.092737243 0.69322336 -0.69705272 0.00047135798 0.73187089 -0.70803809 0.00047135798 0.73187089
		 -0.70803416 -0.13138105 0.60000366 -0.69705272 -0.13138105 0.60000551 -0.70803416 -0.092737243 0.50674295
		 -0.69705272 -0.092737243 0.50674486 -0.70803034 0.00047135798 0.46816561 -0.69706059 0.00047135798 0.46816561
		 -0.70803416 0.093727686 0.50674295 -0.69705272 0.093727686 0.50674486 -0.70803416 0.1323688 0.60000366
		 -0.69705272 0.1323688 0.60000551 -0.70803416 0.093727686 0.69322538 -0.69705272 0.093727686 0.69322336
		 -0.70803416 0.00047135798 0.7250849 -0.70803416 -0.087923855 0.6884495 0.75220162 -0.092737243 0.69324291
		 0.75219381 -0.089139 0.68962651 0.75219381 0.00047135798 0.72675788 0.75219381 0.00047135798 0.73188698
		 -0.70803416 -0.12458824 0.60000366 0.75220162 -0.13138105 0.6000219 0.75220162 -0.12625283 0.6000219
		 -0.70803416 -0.087923855 0.51156366 0.75220162 -0.092737243 0.50675958 0.75220162 -0.089139 0.51040983
		 -0.70803416 0.00047135798 0.47493991 0.75220162 0.00047135798 0.46818477 0.75220162 0.00047135798 0.47330025
		 -0.70803416 0.088913791 0.51156366 0.75220162 0.093727686 0.50675958 0.75220162 0.090083912 0.51040983
		 -0.70803416 0.12557648 0.60000366 0.75220162 0.1323688 0.6000219 0.75220162 0.12724036 0.6000219
		 -0.70803416 0.088913791 0.6884495 0.75220162 0.093727686 0.69324291 0.75219381 0.090083912 0.68962651
		 0.75220162 -0.072315224 0.67282057 0.75687623 -0.072315224 0.67281544 0.75687623 0.00047135798 0.70299703
		 0.75220162 0.00047135798 0.70299 0.75220162 -0.10245583 0.6000219 0.75688398 -0.10245583 0.60002482
		 0.75220162 -0.072315224 0.52719623 0.75687623 -0.072315224 0.52719152 0.75219381 0.00047135798 0.49706829
		 0.75688398 0.00047135798 0.49705911 0.75220162 0.073302984 0.52719623 0.75687623 0.073302984 0.52719152
		 0.75220162 0.10344361 0.6000219 0.75688398 0.10344361 0.60002482 0.75220162 0.073302984 0.67282057
		 0.75687623 0.073302984 0.67281544 0.80042034 -0.072315224 0.67282456 0.80329525 -0.071054295 0.67156196
		 0.80329525 0.00047135798 0.70119697 0.80042034 0.00047135798 0.70299399 0.80042034 -0.10245583 0.60002613
		 0.80330306 -0.10069994 0.60002261 0.80042034 -0.072315224 0.5272004 0.80330306 -0.071054295 0.52848732
		 0.80042034 0.00047135798 0.49706829 0.80329525 0.00047135798 0.49884379 0.80042034 0.073302984 0.5272004
		 0.80330306 0.07204473 0.52848732 0.80042034 0.10344361 0.60002613 0.80330306 0.10164484 0.60002261
		 0.80042034 0.073302984 0.67282456 0.80329525 0.07204473 0.67156196;
	setAttr ".vt[664:829]" 0.82606071 -0.061023086 0.66152036 0.82606846 -0.057828512 0.65836877
		 0.82606846 0.00047135798 0.68252838 0.82606071 0.00047135798 0.68697095 0.82606846 -0.086484939 0.600021
		 0.82606846 -0.081986099 0.600021 0.82606846 -0.061023086 0.53852147 0.82606846 -0.057828512 0.54168653
		 0.82606846 0.00047135798 0.51303333 0.82606846 0.00047135798 0.51751345 0.82606846 0.062011328 0.53852147
		 0.82606846 0.058818955 0.54168653 0.82606846 0.087474883 0.600021 0.82606846 0.082976535 0.600021
		 0.82606071 0.062011328 0.66152036 0.82606846 0.058818955 0.65836877 0.82606846 -0.049822241 0.65031791
		 0.82137829 -0.048652127 0.64915919 0.82137829 0.00047135798 0.66948062 0.82606071 0.00047135798 0.67116457
		 0.82606846 -0.070650861 0.600021 0.82137829 -0.068986259 0.60001922 0.82606846 -0.049822241 0.54969603
		 0.82137829 -0.048652127 0.55091023 0.82606846 0.00047135798 0.52886766 0.82137829 0.00047135798 0.53052497
		 0.82606846 0.050810248 0.54969603 0.82137829 0.049640615 0.55091023 0.82606846 0.071638621 0.600021
		 0.82137829 0.069973767 0.60001922 0.82606846 0.050810248 0.65031791 0.82137829 0.049640615 0.64915919
		 0.78705871 0.00047135798 0.65730941 0.78705871 -0.040014781 0.64050937 0.78706652 -0.035470661 0.63601553
		 0.78705871 0.00047135798 0.65089571 0.78705871 -0.056795716 0.60002226 0.78705871 -0.050405603 0.60002226
		 0.78705871 -0.040014781 0.55949426 0.78706652 -0.035470661 0.56404686 0.78706652 0.00047135798 0.54272944
		 0.78705871 0.00047135798 0.54916263 0.78705871 0.041003279 0.55949426 0.78706652 0.0364611 0.56404686
		 0.78705871 0.057783715 0.60002226 0.78705871 0.051397007 0.60002226 0.78705871 0.041003279 0.64050937
		 0.78706652 0.0364611 0.63601553 0.78705871 -0.021749664 0.62225592 0.78705871 0.00047135798 0.63142705
		 0.78705871 -0.030927995 0.60002226 0.78706652 -0.021749664 0.57779807 0.78706652 0.00047135798 0.5685854
		 0.78706652 0.022694815 0.57779807 0.78705871 0.031916 0.60002226 0.78705871 0.022694815 0.62225592
		 -0.70803416 0.00047135798 0.70297587 -0.71131814 0.00047135798 0.70297974 -0.71132594 -0.072315224 0.67280304
		 -0.70803416 -0.072315224 0.67280304 -0.71131432 -0.10245583 0.60000366 -0.70803416 -0.10245583 0.60000366
		 -0.71131432 -0.072315224 0.52717495 -0.70803034 -0.072315224 0.52717495 -0.71131814 0.00047135798 0.49704698
		 -0.70803416 0.00047135798 0.49704507 -0.71131432 0.073302984 0.52717495 -0.70803034 0.073302984 0.52717495
		 -0.71131432 0.10344361 0.60000366 -0.70803416 0.10344361 0.60000366 -0.71132594 0.073302984 0.67280304
		 -0.70803416 0.073302984 0.67280304 -0.73854005 0.00047135798 0.70297587 -0.73853219 0.00047135798 0.70706421
		 -0.73853219 -0.07519304 0.67567217 -0.73853219 -0.072315224 0.67280507 -0.73854005 -0.10654881 0.60000366
		 -0.73854005 -0.10245583 0.60000366 -0.73854005 -0.07519304 0.52430004 -0.73854005 -0.072315224 0.52717495
		 -0.73853219 0.00047135798 0.49294308 -0.73853219 0.00047135798 0.49704307 -0.73854005 0.076182745 0.52430004
		 -0.73854005 0.073302984 0.52717495 -0.73854005 0.10753634 0.60000366 -0.73854005 0.10344361 0.60000366
		 -0.73853219 0.076182745 0.67567217 -0.73853219 0.073302984 0.67280507 -0.73853219 0.00047135798 0.74481368
		 -0.74159801 0.00047135798 0.74481368 -0.74159801 -0.10191558 0.70239925 -0.73853219 -0.10191558 0.70240331
		 -0.74159026 -0.14433753 0.60000551 -0.73854005 -0.14433753 0.60000366 -0.74159026 -0.10191558 0.49760795
		 -0.73853612 -0.10191558 0.49760595 -0.74159026 0.00047135798 0.45520714 -0.73853219 0.00047135798 0.45520714
		 -0.74159026 0.10290309 0.49760795 -0.73853612 0.10290309 0.49760595 -0.74159026 0.14532532 0.60000551
		 -0.73854005 0.14532532 0.60000366 -0.74159801 0.10290309 0.70239925 -0.73853219 0.10290309 0.70240331
		 -0.79301506 -0.10191558 0.70239925 -0.79301506 0.00047135798 0.74481368 -0.79301506 0.00047135798 0.72647166
		 -0.79301506 -0.088913307 0.68943894 -0.79301882 -0.14433753 0.59999973 -0.79301882 -0.12598161 0.59999973
		 -0.79301506 -0.10191558 0.49760595 -0.79301882 -0.088913307 0.51056641 -0.79301506 0.00047135798 0.45520911
		 -0.79301506 0.00047135798 0.47354722 -0.79301506 0.10290309 0.49760595 -0.79301882 0.089903258 0.51056641
		 -0.79301882 0.14532532 0.59999973 -0.79301882 0.12697157 0.59999973 -0.79301506 0.10290309 0.70239925
		 -0.79301506 0.089903258 0.68943894 -0.79301882 0.00047135798 0.68809307 -0.79300719 -0.061787337 0.66225982
		 -0.79301882 -0.087565698 0.59999973 -0.79301882 -0.061787337 0.53770447 -0.79301506 0.00047135798 0.51192981
		 -0.79301882 0.062777288 0.53770447 -0.79301882 0.088553458 0.59999973 -0.79300719 0.062777288 0.66225982
		 0.74806458 -0.092737243 0.69323885 0.74806458 0.00047135798 0.73189062 0.74804902 -0.13138105 0.60001838
		 0.74807239 -0.092737243 0.50676334 0.74806458 0.00047135798 0.46818066 0.74807239 0.093727686 0.50676334
		 0.74804902 0.1323688 0.60001838 0.74806458 0.093727686 0.69323885 -0.73853219 0.00047135798 0.73970091
		 -0.73853219 -0.098271564 0.69880378 -0.73854005 -0.13920911 0.60000366 -0.73853219 -0.098271564 0.50122094
		 -0.73854005 0.00047135798 0.46032777 -0.73853219 0.099259324 0.50122094 -0.73854005 0.14019737 0.60000366
		 -0.73853219 0.099259324 0.69880378 -0.79077113 0.00047135798 0.74481183 -0.79076731 -0.10191558 0.70239741
		 -0.79077113 -0.14433753 0.60000366 -0.79077113 -0.10191558 0.49761185 -0.79076731 0.00047135798 0.45520714
		 -0.79077113 0.10290309 0.49761185 -0.79077113 0.14532532 0.60000366 -0.79076731 0.10290309 0.70239741
		 -0.70803416 0.00047135798 0.70742846 -0.70803034 -0.075464264 0.67599159 -0.70803416 -0.10695273 0.60000366
		 -0.70803416 -0.075464264 0.52403122 -0.70803416 0.00047135798 0.49253789 -0.70803416 0.076452024 0.52403122
		 -0.70803416 0.10794292 0.60000366 -0.70803034 0.076452024 0.67599159 0.75219381 0.00047135798 0.70686936
		 0.75219381 -0.075058401 0.67556614 0.75220162 -0.10632312 0.6000219 0.75220162 -0.075058401 0.52444041
		 0.75220162 0.00047135798 0.49318835 0.75220162 0.076048836 0.52444041;
	setAttr ".vt[830:897]" 0.75220162 0.10731331 0.6000219 0.75219381 0.076048836 0.67556614
		 0.79551983 -0.072315224 0.67282152 0.79551208 0.00047135798 0.70299137 0.79551983 -0.10245583 0.60001886
		 0.79551983 -0.072315224 0.52719724 0.79551983 0.00047135798 0.4970651 0.79551983 0.073302984 0.52719724
		 0.79551983 0.10344361 0.60001886 0.79551983 0.073302984 0.67282152 0.82345068 -0.062147427 0.66269004
		 0.82345068 0.00047135798 0.68859786 0.82345068 -0.08810401 0.60002899 0.82345843 -0.062147427 0.53735536
		 0.82345068 0.00047135798 0.51141244 0.82345843 0.063137621 0.53735536 0.82345068 0.089094445 0.60002899
		 0.82345068 0.063137621 0.66269004 0.78931034 -0.040598139 0.64109278 0.78931034 0.00047135798 0.65811032
		 0.78931034 -0.057605252 0.60001749 0.78931034 -0.040598139 0.55895466 0.78931034 0.00047135798 0.54195082
		 0.78931034 0.041589551 0.55895466 0.78931034 0.058593493 0.60001749 0.78931034 0.041589551 0.64109278
		 -0.79301882 0.00047135798 0.68327236 -0.79301882 -0.058414549 0.65890002 -0.78357613 -0.059807923 0.66033947
		 -0.78356838 0.00047135798 0.68529606 -0.79301882 -0.082795382 0.59999973 -0.78356838 -0.08482033 0.59999973
		 -0.79301506 -0.058414549 0.54111505 -0.78357613 -0.059807923 0.53968155 -0.79301882 0.00047135798 0.51674855
		 -0.78356838 0.00047135798 0.51472288 -0.79301506 0.059402306 0.54111505 -0.78357613 0.060798358 0.53968155
		 -0.79301882 0.08378534 0.59999973 -0.78356838 0.085810527 0.59999973 -0.79301882 0.059402306 0.65890002
		 -0.78357613 0.060798358 0.66033947 -0.79300719 -0.057739649 0.65822423 -0.79301882 0.00047135798 0.68232769
		 -0.79301882 -0.081851214 0.59999973 -0.79301882 -0.057739649 0.54180849 -0.79301506 0.00047135798 0.51765037
		 -0.79301882 0.058727402 0.54180849 -0.79301882 0.08284165 0.59999973 -0.79300719 0.058727402 0.65822423
		 -0.79301882 -0.060708765 0.66117889 -0.79301882 0.00047135798 0.68651927 -0.79301882 -0.086035736 0.59999973
		 -0.79301506 -0.060708765 0.53882647 -0.79301506 0.00047135798 0.51344705 -0.79301506 0.061696764 0.53882647
		 -0.79301882 0.087023482 0.59999973 -0.79301882 0.061696764 0.66117889 -0.79301882 0.00047135798 0.65989143
		 -0.79301882 -0.041814029 0.64234012 -0.79301882 -0.059358966 0.59999973 -0.79301882 -0.041814029 0.55767488
		 -0.79301506 0.00047135798 0.54013336 -0.79301882 0.042804465 0.55767488 -0.79301882 0.060348917 0.59999973
		 -0.79301882 0.042804465 0.64234012 -0.79301882 0.00047135798 0.59999973 0.78705871 0.00047135798 0.60002226;
	setAttr -s 1788 ".ed";
	setAttr ".ed[0:165]"  0 1 1 1 2 1 2 3 1 3 0 1 1 4 1 4 5 1 5 2 1 4 6 1 6 7 1
		 7 5 1 6 8 1 8 9 1 9 7 1 8 10 1 10 11 1 11 9 1 10 12 1 12 13 1 13 11 1 12 14 1 14 15 1
		 15 13 1 14 16 1 16 17 1 17 15 1 18 19 1 19 20 1 20 21 1 21 18 1 19 22 1 22 23 1 23 20 1
		 22 24 1 24 25 1 25 23 1 24 26 1 26 27 1 27 25 1 26 28 1 28 29 1 29 27 1 28 30 1 30 31 1
		 31 29 1 30 32 1 32 33 1 33 31 1 32 34 1 34 35 1 35 33 1 0 36 1 36 37 1 37 1 1 37 38 1
		 38 4 1 38 39 1 39 6 1 39 40 1 40 8 1 40 41 1 41 10 1 41 42 1 42 12 1 42 43 1 43 14 1
		 43 44 1 44 16 1 18 45 1 45 46 1 46 19 1 46 47 1 47 22 1 47 48 1 48 24 1 48 49 1 49 26 1
		 49 50 1 50 28 1 50 51 1 51 30 1 51 52 1 52 32 1 52 53 1 53 34 1 45 54 1 54 55 1 55 46 1
		 55 56 1 56 47 1 56 57 1 57 48 1 57 58 1 58 49 1 58 59 1 59 50 1 59 60 1 60 51 1 60 61 1
		 61 52 1 61 62 1 62 53 1 63 64 1 64 37 1 36 63 1 64 65 1 65 38 1 65 66 1 66 39 1 66 67 1
		 67 40 1 67 68 1 68 41 1 68 69 1 69 42 1 69 70 1 70 43 1 70 54 1 54 44 1 71 72 1 72 73 1
		 73 74 1 74 71 1 73 75 1 75 76 1 76 74 1 75 77 1 77 78 1 78 76 1 77 79 1 79 80 1 80 78 1
		 79 81 1 81 82 1 82 80 1 81 83 1 83 84 1 84 82 1 83 85 1 85 86 1 86 84 1 85 87 1 87 88 1
		 88 86 1 87 89 1 89 90 1 90 88 1 89 91 1 91 92 1 92 90 1 91 93 1 93 94 1 94 92 1 93 95 1
		 95 96 1 96 94 1 95 97 1 97 98 1 98 96 1 97 99 1 99 100 1 100 98 1 99 101 1 101 102 1
		 102 100 1 101 103 1 103 104 1;
	setAttr ".ed[166:331]" 104 102 1 34 105 1 105 106 1 106 35 1 16 107 1 107 108 1
		 108 17 1 2 109 1 109 110 1 110 3 1 5 111 1 111 109 1 7 112 1 112 111 1 9 113 1 113 112 1
		 11 114 1 114 113 1 13 115 1 115 114 1 15 116 1 116 115 1 108 116 1 20 117 1 117 118 1
		 118 21 1 23 119 1 119 117 1 25 120 1 120 119 1 27 121 1 121 120 1 29 122 1 122 121 1
		 31 123 1 123 122 1 33 124 1 124 123 1 106 124 1 110 125 1 125 0 1 118 126 1 126 18 1
		 125 127 1 127 36 1 126 128 1 128 45 1 62 129 1 129 130 1 130 53 1 130 105 1 131 72 1
		 71 63 1 63 131 1 44 132 1 132 107 1 128 133 1 133 134 1 134 45 1 135 136 1 136 137 1
		 137 138 1 138 135 1 137 139 1 139 140 1 140 138 1 139 141 1 141 142 1 142 140 1 141 143 1
		 143 144 1 144 142 1 143 145 1 145 146 1 146 144 1 145 147 1 147 148 1 148 146 1 147 149 1
		 149 150 1 150 148 1 149 151 1 151 152 1 152 150 1 151 153 1 153 154 1 154 152 1 153 155 1
		 155 156 1 156 154 1 155 157 1 157 158 1 158 156 1 157 159 1 159 160 1 160 158 1 159 161 1
		 161 162 1 162 160 1 161 163 1 163 164 1 164 162 1 163 165 1 165 166 1 166 164 1 165 167 1
		 167 168 1 168 166 1 169 170 1 170 171 1 171 172 1 172 169 1 173 174 1 174 175 1 175 176 1
		 176 173 1 177 178 1 178 179 1 179 180 1 180 177 1 181 182 1 182 178 1 177 181 1 183 184 1
		 184 182 1 181 183 1 185 186 1 186 184 1 183 185 1 187 188 1 188 186 1 185 187 1 189 190 1
		 190 188 1 187 189 1 191 192 1 192 190 1 189 191 1 175 192 1 191 176 1 193 194 1 194 195 1
		 195 196 1 196 193 1 197 198 1 198 194 1 193 197 1 199 200 1 200 198 1 197 199 1 201 202 1
		 202 200 1 199 201 1 203 204 1 204 202 1 201 203 1 205 206 1 206 204 1 203 205 1 207 208 1
		 208 206 1 205 207 1 171 208 1 207 172 1 179 209 1 209 210 1;
	setAttr ".ed[332:497]" 210 180 1 195 211 1 211 212 1 212 196 1 209 213 1 213 214 1
		 214 210 1 211 215 1 215 216 1 216 212 1 217 218 1 218 219 1 219 220 1 220 217 1 219 170 1
		 169 220 1 221 136 1 135 222 1 222 221 1 223 224 1 224 174 1 173 223 1 215 225 1 225 226 1
		 226 216 1 227 228 1 228 73 1 72 227 1 228 229 1 229 75 1 229 230 1 230 77 1 230 231 1
		 231 79 1 231 232 1 232 81 1 232 233 1 233 83 1 233 234 1 234 85 1 234 235 1 235 87 1
		 235 236 1 236 89 1 236 237 1 237 91 1 237 238 1 238 93 1 238 239 1 239 95 1 239 240 1
		 240 97 1 240 241 1 241 99 1 241 242 1 242 101 1 242 243 1 243 103 1 244 245 1 245 106 1
		 105 244 1 246 247 1 247 108 1 107 246 1 248 249 1 249 110 1 109 248 1 250 248 1 111 250 1
		 251 250 1 112 251 1 252 251 1 113 252 1 253 252 1 114 253 1 254 253 1 115 254 1 255 254 1
		 116 255 1 247 255 1 256 257 1 257 118 1 117 256 1 258 256 1 119 258 1 259 258 1 120 259 1
		 260 259 1 121 260 1 261 260 1 122 261 1 262 261 1 123 262 1 263 262 1 124 263 1 245 263 1
		 249 264 1 264 125 1 257 265 1 265 126 1 264 266 1 266 127 1 265 267 1 267 128 1 243 268 1
		 268 129 1 129 103 1 269 244 1 130 269 1 266 270 1 270 131 1 131 127 1 271 246 1 132 271 1
		 272 271 1 132 133 1 133 272 1 273 274 1 274 137 1 136 273 1 274 275 1 275 139 1 275 276 1
		 276 141 1 276 277 1 277 143 1 277 278 1 278 145 1 278 279 1 279 147 1 279 280 1 280 149 1
		 280 281 1 281 151 1 281 282 1 282 153 1 282 283 1 283 155 1 283 284 1 284 157 1 284 285 1
		 285 159 1 285 286 1 286 161 1 286 287 1 287 163 1 287 288 1 288 165 1 288 289 1 289 167 1
		 290 291 1 291 171 1 170 290 1 292 293 1 293 175 1 174 292 1 294 295 1 295 179 1 178 294 1
		 296 294 1 182 296 1 297 296 1 184 297 1 298 297 1 186 298 1 299 298 1;
	setAttr ".ed[498:663]" 188 299 1 300 299 1 190 300 1 301 300 1 192 301 1 293 301 1
		 302 303 1 303 195 1 194 302 1 304 302 1 198 304 1 305 304 1 200 305 1 306 305 1 202 306 1
		 307 306 1 204 307 1 308 307 1 206 308 1 309 308 1 208 309 1 291 309 1 295 310 1 310 209 1
		 303 311 1 311 211 1 310 312 1 312 213 1 311 313 1 313 215 1 289 314 1 314 218 1 218 167 1
		 315 290 1 219 315 1 312 316 1 316 221 1 221 213 1 317 292 1 224 317 1 318 317 1 224 225 1
		 225 318 1 74 64 1 76 65 1 78 66 1 80 67 1 82 68 1 84 69 1 86 70 1 88 54 1 134 44 1
		 222 214 1 227 270 1 270 222 1 135 227 1 272 267 1 267 216 1 226 272 1 316 273 1 313 318 1
		 90 55 1 92 56 1 94 57 1 96 58 1 98 59 1 100 60 1 102 61 1 104 62 1 217 168 1 223 226 1
		 220 269 1 269 268 1 268 217 1 314 315 1 319 320 1 320 321 1 321 322 1 322 319 1 321 323 1
		 323 324 1 324 322 1 323 325 1 325 326 1 326 324 1 325 327 1 327 328 1 328 326 1 327 329 1
		 329 330 1 330 328 1 329 331 1 331 332 1 332 330 1 331 333 1 333 334 1 334 332 1 333 335 1
		 335 336 1 336 334 1 337 338 1 338 339 1 339 340 1 340 337 1 339 341 1 341 342 1 342 340 1
		 341 343 1 343 344 1 344 342 1 343 345 1 345 346 1 346 344 1 345 347 1 347 348 1 348 346 1
		 347 349 1 349 350 1 350 348 1 349 351 1 351 352 1 352 350 1 351 353 1 353 354 1 354 352 1
		 322 355 1 355 356 1 356 319 1 324 357 1 357 355 1 326 358 1 358 357 1 328 359 1 359 358 1
		 330 360 1 360 359 1 332 361 1 361 360 1 334 362 1 362 361 1 336 363 1 363 362 1 340 364 1
		 364 365 1 365 337 1 342 366 1 366 364 1 344 367 1 367 366 1 346 368 1 368 367 1 348 369 1
		 369 368 1 350 370 1 370 369 1 352 371 1 371 370 1 354 372 1 372 371 1 364 373 1 373 374 1
		 374 365 1 366 375 1 375 373 1 367 376 1 376 375 1;
	setAttr ".ed[664:829]" 368 377 1 377 376 1 369 378 1 378 377 1 370 379 1 379 378 1
		 371 380 1 380 379 1 372 381 1 381 380 1 382 356 1 355 383 1 383 382 1 357 384 1 384 383 1
		 358 385 1 385 384 1 359 386 1 386 385 1 360 387 1 387 386 1 361 388 1 388 387 1 362 389 1
		 389 388 1 363 374 1 374 389 1 390 391 1 391 392 1 392 393 1 393 390 1 391 394 1 394 395 1
		 395 392 1 394 396 1 396 397 1 397 395 1 396 398 1 398 399 1 399 397 1 398 400 1 400 401 1
		 401 399 1 400 402 1 402 403 1 403 401 1 402 404 1 404 405 1 405 403 1 404 406 1 406 407 1
		 407 405 1 406 408 1 408 409 1 409 407 1 408 410 1 410 411 1 411 409 1 410 412 1 412 413 1
		 413 411 1 412 414 1 414 415 1 415 413 1 414 416 1 416 417 1 417 415 1 416 418 1 418 419 1
		 419 417 1 418 420 1 420 421 1 421 419 1 420 422 1 422 423 1 423 421 1 353 424 1 424 425 1
		 425 354 1 335 426 1 426 427 1 427 336 1 320 428 1 428 429 1 429 321 1 429 430 1 430 323 1
		 430 431 1 431 325 1 431 432 1 432 327 1 432 433 1 433 329 1 433 434 1 434 331 1 434 435 1
		 435 333 1 435 426 1 338 436 1 436 437 1 437 339 1 437 438 1 438 341 1 438 439 1 439 343 1
		 439 440 1 440 345 1 440 441 1 441 347 1 441 442 1 442 349 1 442 443 1 443 351 1 443 424 1
		 319 444 1 444 428 1 337 445 1 445 436 1 356 446 1 446 444 1 365 447 1 447 445 1 372 448 1
		 448 449 1 449 381 1 425 448 1 450 382 1 382 390 1 393 450 1 427 451 1 451 363 1 365 452 1
		 452 453 1 453 447 1 454 455 1 455 456 1 456 457 1 457 454 1 455 458 1 458 459 1 459 456 1
		 458 460 1 460 461 1 461 459 1 460 462 1 462 463 1 463 461 1 462 464 1 464 465 1 465 463 1
		 464 466 1 466 467 1 467 465 1 466 468 1 468 469 1 469 467 1 468 470 1 470 471 1 471 469 1
		 470 472 1 472 473 1 473 471 1 472 474 1 474 475 1 475 473 1 474 476 1;
	setAttr ".ed[830:995]" 476 477 1 477 475 1 476 478 1 478 479 1 479 477 1 478 480 1
		 480 481 1 481 479 1 480 482 1 482 483 1 483 481 1 482 484 1 484 485 1 485 483 1 484 486 1
		 486 487 1 487 485 1 488 489 1 489 490 1 490 491 1 491 488 1 492 493 1 493 494 1 494 495 1
		 495 492 1 496 497 1 497 498 1 498 499 1 499 496 1 500 496 1 499 501 1 501 500 1 502 500 1
		 501 503 1 503 502 1 504 502 1 503 505 1 505 504 1 506 504 1 505 507 1 507 506 1 508 506 1
		 507 509 1 509 508 1 510 508 1 509 511 1 511 510 1 493 510 1 511 494 1 512 513 1 513 514 1
		 514 515 1 515 512 1 516 512 1 515 517 1 517 516 1 518 516 1 517 519 1 519 518 1 520 518 1
		 519 521 1 521 520 1 522 520 1 521 523 1 523 522 1 524 522 1 523 525 1 525 524 1 526 524 1
		 525 527 1 527 526 1 489 526 1 527 490 1 497 528 1 528 529 1 529 498 1 513 530 1 530 531 1
		 531 514 1 528 532 1 532 533 1 533 529 1 530 534 1 534 535 1 535 531 1 536 537 1 537 538 1
		 538 539 1 539 536 1 537 488 1 491 538 1 540 541 1 541 454 1 457 540 1 542 492 1 495 543 1
		 543 542 1 534 544 1 544 545 1 545 535 1 392 546 1 546 547 1 547 393 1 395 548 1 548 546 1
		 397 549 1 549 548 1 399 550 1 550 549 1 401 551 1 551 550 1 403 552 1 552 551 1 405 553 1
		 553 552 1 407 554 1 554 553 1 409 555 1 555 554 1 411 556 1 556 555 1 413 557 1 557 556 1
		 415 558 1 558 557 1 417 559 1 559 558 1 419 560 1 560 559 1 421 561 1 561 560 1 423 562 1
		 562 561 1 424 563 1 563 564 1 564 425 1 426 565 1 565 566 1 566 427 1 428 567 1 567 568 1
		 568 429 1 568 569 1 569 430 1 569 570 1 570 431 1 570 571 1 571 432 1 571 572 1 572 433 1
		 572 573 1 573 434 1 573 574 1 574 435 1 574 565 1 436 575 1 575 576 1 576 437 1 576 577 1
		 577 438 1 577 578 1 578 439 1 578 579 1 579 440 1 579 580 1 580 441 1;
	setAttr ".ed[996:1161]" 580 581 1 581 442 1 581 582 1 582 443 1 582 563 1 444 583 1
		 583 567 1 445 584 1 584 575 1 446 585 1 585 583 1 447 586 1 586 584 1 423 449 1 449 587 1
		 587 562 1 564 588 1 588 448 1 450 589 1 589 585 1 446 450 1 566 590 1 590 451 1 590 591 1
		 591 453 1 453 451 1 273 457 1 456 274 1 459 275 1 461 276 1 463 277 1 465 278 1 467 279 1
		 469 280 1 471 281 1 473 282 1 475 283 1 477 284 1 479 285 1 481 286 1 483 287 1 485 288 1
		 487 289 1 290 491 1 490 291 1 292 495 1 494 293 1 294 499 1 498 295 1 296 501 1 297 503 1
		 298 505 1 299 507 1 300 509 1 301 511 1 302 515 1 514 303 1 304 517 1 305 519 1 306 521 1
		 307 523 1 308 525 1 309 527 1 529 310 1 531 311 1 533 312 1 535 313 1 487 539 1 539 314 1
		 315 538 1 533 540 1 540 316 1 317 543 1 318 545 1 545 543 1 383 391 1 384 394 1 385 396 1
		 386 398 1 387 400 1 388 402 1 389 404 1 374 406 1 363 452 1 532 541 1 547 454 1 541 589 1
		 589 547 1 591 544 1 534 586 1 586 591 1 373 408 1 375 410 1 376 412 1 377 414 1 378 416 1
		 379 418 1 380 420 1 381 422 1 486 536 1 544 542 1 587 588 1 588 537 1 536 587 1 138 228 1
		 140 229 1 142 230 1 144 231 1 146 232 1 148 233 1 150 234 1 152 235 1 154 236 1 156 237 1
		 158 238 1 160 239 1 162 240 1 164 241 1 166 242 1 168 243 1 172 245 1 244 169 1 176 247 1
		 246 173 1 180 249 1 248 177 1 250 181 1 251 183 1 252 185 1 253 187 1 254 189 1 255 191 1
		 196 257 1 256 193 1 258 197 1 259 199 1 260 201 1 261 203 1 262 205 1 263 207 1 210 264 1
		 212 265 1 214 266 1 271 223 1 546 455 1 548 458 1 549 460 1 550 462 1 551 464 1 552 466 1
		 553 468 1 554 470 1 555 472 1 556 474 1 557 476 1 558 478 1 559 480 1 560 482 1 561 484 1
		 562 486 1 488 564 1 563 489 1 492 566 1 565 493 1 496 568 1 567 497 1;
	setAttr ".ed[1162:1327]" 500 569 1 502 570 1 504 571 1 506 572 1 508 573 1 510 574 1
		 512 576 1 575 513 1 516 577 1 518 578 1 520 579 1 522 580 1 524 581 1 526 582 1 583 528 1
		 584 530 1 585 532 1 542 590 1 592 593 1 593 594 1 594 595 1 595 592 1 596 597 1 597 593 1
		 592 596 1 598 599 1 599 597 1 596 598 1 600 601 1 601 599 1 598 600 1 602 603 1 603 601 1
		 600 602 1 604 605 1 605 603 1 602 604 1 606 607 1 607 605 1 604 606 1 594 607 1 606 595 1
		 595 608 1 608 609 1 609 592 1 610 611 1 611 612 1 612 613 1 613 610 1 609 614 1 614 596 1
		 615 616 1 616 611 1 610 615 1 614 617 1 617 598 1 618 619 1 619 616 1 615 618 1 617 620 1
		 620 600 1 621 622 1 622 619 1 618 621 1 620 623 1 623 602 1 624 625 1 625 622 1 621 624 1
		 623 626 1 626 604 1 627 628 1 628 625 1 624 627 1 626 629 1 629 606 1 630 631 1 631 628 1
		 627 630 1 629 608 1 612 631 1 630 613 1 632 633 1 633 634 1 634 635 1 635 632 1 636 637 1
		 637 633 1 632 636 1 638 639 1 639 637 1 636 638 1 640 641 1 641 639 1 638 640 1 642 643 1
		 643 641 1 640 642 1 644 645 1 645 643 1 642 644 1 646 647 1 647 645 1 644 646 1 634 647 1
		 646 635 1 648 649 1 649 650 1 650 651 1 651 648 1 652 653 1 653 649 1 648 652 1 654 655 1
		 655 653 1 652 654 1 656 657 1 657 655 1 654 656 1 658 659 1 659 657 1 656 658 1 660 661 1
		 661 659 1 658 660 1 662 663 1 663 661 1 660 662 1 650 663 1 662 651 1 664 665 1 665 666 1
		 666 667 1 667 664 1 668 669 1 669 665 1 664 668 1 670 671 1 671 669 1 668 670 1 672 673 1
		 673 671 1 670 672 1 674 675 1 675 673 1 672 674 1 676 677 1 677 675 1 674 676 1 678 679 1
		 679 677 1 676 678 1 666 679 1 678 667 1 680 681 1 681 682 1 682 683 1 683 680 1 684 685 1
		 685 681 1 680 684 1 686 687 1 687 685 1 684 686 1 688 689 1 689 687 1;
	setAttr ".ed[1328:1493]" 686 688 1 690 691 1 691 689 1 688 690 1 692 693 1 693 691 1
		 690 692 1 694 695 1 695 693 1 692 694 1 682 695 1 694 683 1 696 697 1 697 698 1 698 699 1
		 699 696 1 697 700 1 700 701 1 701 698 1 700 702 1 702 703 1 703 701 1 702 704 1 704 705 1
		 705 703 1 704 706 1 706 707 1 707 705 1 706 708 1 708 709 1 709 707 1 708 710 1 710 711 1
		 711 709 1 710 696 1 699 711 1 698 712 1 712 713 1 713 699 1 701 714 1 714 712 1 703 715 1
		 715 714 1 705 716 1 716 715 1 707 717 1 717 716 1 709 718 1 718 717 1 711 719 1 719 718 1
		 713 719 1 720 721 1 721 722 1 722 723 1 723 720 1 722 724 1 724 725 1 725 723 1 724 726 1
		 726 727 1 727 725 1 726 728 1 728 729 1 729 727 1 728 730 1 730 731 1 731 729 1 730 732 1
		 732 733 1 733 731 1 732 734 1 734 735 1 735 733 1 734 721 1 720 735 1 736 737 1 737 738 1
		 738 739 1 739 736 1 738 740 1 740 741 1 741 739 1 740 742 1 742 743 1 743 741 1 742 744 1
		 744 745 1 745 743 1 744 746 1 746 747 1 747 745 1 746 748 1 748 749 1 749 747 1 748 750 1
		 750 751 1 751 749 1 750 737 1 736 751 1 752 753 1 753 754 1 754 755 1 755 752 1 754 756 1
		 756 757 1 757 755 1 756 758 1 758 759 1 759 757 1 758 760 1 760 761 1 761 759 1 760 762 1
		 762 763 1 763 761 1 762 764 1 764 765 1 765 763 1 764 766 1 766 767 1 767 765 1 766 753 1
		 752 767 1 768 769 1 769 770 1 770 771 1 771 768 1 772 768 1 771 773 1 773 772 1 774 772 1
		 773 775 1 775 774 1 776 774 1 775 777 1 777 776 1 778 776 1 777 779 1 779 778 1 780 778 1
		 779 781 1 781 780 1 782 780 1 781 783 1 783 782 1 769 782 1 783 770 1 770 784 1 784 785 1
		 785 771 1 785 786 1 786 773 1 786 787 1 787 775 1 787 788 1 788 777 1 788 789 1 789 779 1
		 789 790 1 790 781 1 790 791 1 791 783 1 791 784 1 792 793 1 793 594 1;
	setAttr ".ed[1494:1659]" 593 792 1 794 792 1 597 794 1 795 794 1 599 795 1 796 795 1
		 601 796 1 797 796 1 603 797 1 798 797 1 605 798 1 799 798 1 607 799 1 793 799 1 800 801 1
		 801 738 1 737 800 1 801 802 1 802 740 1 802 803 1 803 742 1 803 804 1 804 744 1 804 805 1
		 805 746 1 805 806 1 806 748 1 806 807 1 807 750 1 807 800 1 808 809 1 809 754 1 753 808 1
		 809 810 1 810 756 1 810 811 1 811 758 1 811 812 1 812 760 1 812 813 1 813 762 1 813 814 1
		 814 764 1 814 815 1 815 766 1 815 808 1 755 801 1 800 752 1 757 802 1 759 803 1 761 804 1
		 763 805 1 765 806 1 767 807 1 768 809 1 808 769 1 772 810 1 774 811 1 776 812 1 778 813 1
		 780 814 1 782 815 1 816 817 1 817 609 1 608 816 1 817 818 1 818 614 1 818 819 1 819 617 1
		 819 820 1 820 620 1 820 821 1 821 623 1 821 822 1 822 626 1 822 823 1 823 629 1 823 816 1
		 723 817 1 816 720 1 725 818 1 727 819 1 729 820 1 731 821 1 733 822 1 735 823 1 739 722 1
		 721 736 1 741 724 1 743 726 1 745 728 1 747 730 1 749 732 1 751 734 1 635 824 1 824 825 1
		 825 632 1 825 826 1 826 636 1 826 827 1 827 638 1 827 828 1 828 640 1 828 829 1 829 642 1
		 829 830 1 830 644 1 830 831 1 831 646 1 831 824 1 613 793 1 792 610 1 794 615 1 795 618 1
		 796 621 1 797 624 1 798 627 1 799 630 1 832 833 1 833 634 1 633 832 1 834 832 1 637 834 1
		 835 834 1 639 835 1 836 835 1 641 836 1 837 836 1 643 837 1 838 837 1 645 838 1 839 838 1
		 647 839 1 833 839 1 824 612 1 611 825 1 616 826 1 619 827 1 622 828 1 625 829 1 628 830 1
		 631 831 1 840 841 1 841 650 1 649 840 1 842 840 1 653 842 1 843 842 1 655 843 1 844 843 1
		 657 844 1 845 844 1 659 845 1 846 845 1 661 846 1 847 846 1 663 847 1 841 847 1 651 833 1
		 832 648 1 834 652 1 835 654 1 836 656 1 837 658 1 838 660 1 839 662 1;
	setAttr ".ed[1660:1787]" 667 841 1 840 664 1 842 668 1 843 670 1 844 672 1 845 674 1
		 846 676 1 847 678 1 683 666 1 665 680 1 669 684 1 671 686 1 673 688 1 675 690 1 677 692 1
		 679 694 1 848 849 1 849 682 1 681 848 1 850 848 1 685 850 1 851 850 1 687 851 1 852 851 1
		 689 852 1 853 852 1 691 853 1 854 853 1 693 854 1 855 854 1 695 855 1 849 855 1 696 849 1
		 848 697 1 850 700 1 851 702 1 852 704 1 853 706 1 854 708 1 855 710 1 856 857 1 857 858 1
		 858 859 1 859 856 1 857 860 1 860 861 1 861 858 1 860 862 1 862 863 1 863 861 1 862 864 1
		 864 865 1 865 863 1 864 866 1 866 867 1 867 865 1 866 868 1 868 869 1 869 867 1 868 870 1
		 870 871 1 871 869 1 870 856 1 859 871 1 872 857 1 856 873 1 873 872 1 874 860 1 872 874 1
		 875 862 1 874 875 1 876 864 1 875 876 1 877 866 1 876 877 1 878 868 1 877 878 1 879 870 1
		 878 879 1 879 873 1 858 880 1 880 881 1 881 859 1 861 882 1 882 880 1 863 883 1 883 882 1
		 865 884 1 884 883 1 867 885 1 885 884 1 869 886 1 886 885 1 871 887 1 887 886 1 881 887 1
		 880 785 1 784 881 1 882 786 1 883 787 1 884 788 1 885 789 1 886 790 1 887 791 1 888 889 1
		 889 872 1 873 888 1 889 890 1 890 874 1 890 891 1 891 875 1 891 892 1 892 876 1 892 893 1
		 893 877 1 893 894 1 894 878 1 894 895 1 895 879 1 895 888 1 892 896 1 896 894 1 896 888 1
		 890 896 1 897 714 1 716 897 1 897 718 1 713 897 1;
	setAttr -s 898 ".n";
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
	setAttr ".n[830:897]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
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
	setAttr -s 894 -ch 3576 ".fc";
	setAttr ".fc[0:499]" -type "polyFaces" 
		f 4 0 1 2 3
		mu 0 4 0 1 2 3
		f 4 4 5 6 -2
		mu 0 4 1 4 5 2
		f 4 7 8 9 -6
		mu 0 4 4 6 7 5
		f 4 10 11 12 -9
		mu 0 4 6 8 9 7
		f 4 13 14 15 -12
		mu 0 4 8 10 11 9
		f 4 16 17 18 -15
		mu 0 4 10 12 13 11
		f 4 19 20 21 -18
		mu 0 4 12 14 15 13
		f 4 22 23 24 -21
		mu 0 4 14 16 17 15
		f 4 25 26 27 28
		mu 0 4 18 19 20 21
		f 4 29 30 31 -27
		mu 0 4 19 22 23 20
		f 4 32 33 34 -31
		mu 0 4 22 24 25 23
		f 4 35 36 37 -34
		mu 0 4 24 26 27 25
		f 4 38 39 40 -37
		mu 0 4 26 28 29 27
		f 4 41 42 43 -40
		mu 0 4 28 30 31 29
		f 4 44 45 46 -43
		mu 0 4 30 32 33 31
		f 4 47 48 49 -46
		mu 0 4 32 34 35 33
		f 4 50 51 52 -1
		mu 0 4 0 36 37 1
		f 4 -53 53 54 -5
		mu 0 4 1 37 38 4
		f 4 -55 55 56 -8
		mu 0 4 4 38 39 6
		f 4 -57 57 58 -11
		mu 0 4 6 39 40 8
		f 4 -59 59 60 -14
		mu 0 4 8 40 41 10
		f 4 -61 61 62 -17
		mu 0 4 10 41 42 12
		f 4 -63 63 64 -20
		mu 0 4 12 42 43 14
		f 4 -23 -65 65 66
		mu 0 4 16 14 43 44
		f 4 67 68 69 -26
		mu 0 4 18 968 46 19
		f 4 -70 70 71 -30
		mu 0 4 19 46 47 22
		f 4 -72 72 73 -33
		mu 0 4 22 47 48 24
		f 4 -74 74 75 -36
		mu 0 4 24 48 49 26
		f 4 -76 76 77 -39
		mu 0 4 26 49 50 28
		f 4 -78 78 79 -42
		mu 0 4 28 50 51 30
		f 4 -80 80 81 -45
		mu 0 4 30 51 52 32
		f 4 -82 82 83 -48
		mu 0 4 32 52 53 34
		f 4 84 85 86 -69
		mu 0 4 968 969 55 46
		f 4 87 88 -71 -87
		mu 0 4 55 56 47 46
		f 4 89 90 -73 -89
		mu 0 4 56 57 48 47
		f 4 91 92 -75 -91
		mu 0 4 57 58 49 48
		f 4 93 94 -77 -93
		mu 0 4 58 59 50 49
		f 4 95 96 -79 -95
		mu 0 4 59 60 51 50
		f 4 97 98 -81 -97
		mu 0 4 60 61 52 51
		f 4 99 100 -83 -99
		mu 0 4 61 62 53 52
		f 4 101 102 -52 103
		mu 0 4 63 64 37 36
		f 4 104 105 -54 -103
		mu 0 4 64 65 38 37
		f 4 106 107 -56 -106
		mu 0 4 65 66 39 38
		f 4 108 109 -58 -108
		mu 0 4 66 67 40 39
		f 4 110 111 -60 -110
		mu 0 4 67 68 41 40
		f 4 112 113 -62 -112
		mu 0 4 68 69 42 41
		f 4 114 115 -64 -114
		mu 0 4 69 70 43 42
		f 4 116 117 -66 -116
		mu 0 4 70 54 44 43
		f 4 118 119 120 121
		mu 0 4 71 72 73 74
		f 4 -121 122 123 124
		mu 0 4 74 73 75 76
		f 4 -124 125 126 127
		mu 0 4 76 75 77 78
		f 4 -127 128 129 130
		mu 0 4 78 77 79 80
		f 4 -130 131 132 133
		mu 0 4 80 79 81 82
		f 4 -133 134 135 136
		mu 0 4 82 81 83 84
		f 4 -136 137 138 139
		mu 0 4 84 83 85 86
		f 4 -139 140 141 142
		mu 0 4 86 85 87 954
		f 4 -142 143 144 145
		mu 0 4 88 956 89 90
		f 4 -145 146 147 148
		mu 0 4 90 89 91 92
		f 4 -148 149 150 151
		mu 0 4 92 91 93 94
		f 4 -151 152 153 154
		mu 0 4 94 93 95 96
		f 4 -154 155 156 157
		mu 0 4 96 95 97 98
		f 4 -157 158 159 160
		mu 0 4 98 97 99 100
		f 4 -160 161 162 163
		mu 0 4 100 99 101 102
		f 4 -163 164 165 166
		mu 0 4 102 101 103 104
		f 4 167 168 169 -49
		mu 0 4 34 105 106 35
		f 4 170 171 172 -24
		mu 0 4 16 107 108 17
		f 4 173 174 175 -3
		mu 0 4 2 109 110 3
		f 4 176 177 -174 -7
		mu 0 4 5 111 109 2
		f 4 178 179 -177 -10
		mu 0 4 7 112 111 5
		f 4 180 181 -179 -13
		mu 0 4 9 113 112 7
		f 4 182 183 -181 -16
		mu 0 4 11 114 113 9
		f 4 184 185 -183 -19
		mu 0 4 13 115 114 11
		f 4 186 187 -185 -22
		mu 0 4 15 116 115 13
		f 4 -173 188 -187 -25
		mu 0 4 17 108 116 15
		f 4 189 190 191 -28
		mu 0 4 20 117 118 21
		f 4 192 193 -190 -32
		mu 0 4 23 119 117 20
		f 4 194 195 -193 -35
		mu 0 4 25 120 119 23
		f 4 196 197 -195 -38
		mu 0 4 27 121 120 25
		f 4 198 199 -197 -41
		mu 0 4 29 122 121 27
		f 4 200 201 -199 -44
		mu 0 4 31 123 122 29
		f 4 202 203 -201 -47
		mu 0 4 33 124 123 31
		f 4 -170 204 -203 -50
		mu 0 4 35 106 124 33
		f 4 -176 205 206 -4
		mu 0 4 3 110 125 0
		f 4 -192 207 208 -29
		mu 0 4 21 118 126 18
		f 4 -207 209 210 -51
		mu 0 4 0 125 127 36
		f 4 -209 211 212 -68
		mu 0 4 18 126 128 968
		f 4 213 214 215 -101
		mu 0 4 62 129 130 53
		f 4 -216 216 -168 -84
		mu 0 4 53 130 105 34
		f 4 217 -119 218 219
		mu 0 4 131 72 71 63
		f 4 220 221 -171 -67
		mu 0 4 44 132 107 16
		f 4 222 223 224 -213
		mu 0 4 967 133 134 45
		f 4 225 226 227 228
		mu 0 4 135 136 137 138
		f 4 -228 229 230 231
		mu 0 4 138 137 139 140
		f 4 -231 232 233 234
		mu 0 4 140 139 141 142
		f 4 -234 235 236 237
		mu 0 4 142 141 143 144
		f 4 -237 238 239 240
		mu 0 4 144 143 145 146
		f 4 -240 241 242 243
		mu 0 4 146 145 147 148
		f 4 -243 244 245 246
		mu 0 4 148 147 149 150
		f 4 -246 247 248 249
		mu 0 4 150 149 151 946
		f 4 -249 250 251 252
		mu 0 4 152 955 153 154
		f 4 -252 253 254 255
		mu 0 4 154 153 155 156
		f 4 -255 256 257 258
		mu 0 4 156 155 157 158
		f 4 -258 259 260 261
		mu 0 4 158 157 159 160
		f 4 -261 262 263 264
		mu 0 4 160 159 161 162
		f 4 -264 265 266 267
		mu 0 4 162 161 163 164
		f 4 -267 268 269 270
		mu 0 4 164 163 165 166
		f 4 -270 271 272 273
		mu 0 4 166 165 167 168
		f 4 274 275 276 277
		mu 0 4 169 170 171 172
		f 4 278 279 280 281
		mu 0 4 173 174 175 176
		f 4 282 283 284 285
		mu 0 4 177 178 179 180
		f 4 286 287 -283 288
		mu 0 4 181 182 178 177
		f 4 289 290 -287 291
		mu 0 4 183 184 182 181
		f 4 292 293 -290 294
		mu 0 4 185 186 184 183
		f 4 295 296 -293 297
		mu 0 4 187 188 186 185
		f 4 298 299 -296 300
		mu 0 4 189 190 188 187
		f 4 301 302 -299 303
		mu 0 4 191 192 190 189
		f 4 -281 304 -302 305
		mu 0 4 176 175 192 191
		f 4 306 307 308 309
		mu 0 4 193 194 195 196
		f 4 310 311 -307 312
		mu 0 4 197 198 194 193
		f 4 313 314 -311 315
		mu 0 4 199 200 198 197
		f 4 316 317 -314 318
		mu 0 4 201 202 200 199
		f 4 319 320 -317 321
		mu 0 4 203 204 202 201
		f 4 322 323 -320 324
		mu 0 4 205 206 204 203
		f 4 325 326 -323 327
		mu 0 4 207 208 206 205
		f 4 -277 328 -326 329
		mu 0 4 172 171 208 207
		f 4 -285 330 331 332
		mu 0 4 180 179 209 210
		f 4 -309 333 334 335
		mu 0 4 196 195 211 212
		f 4 -332 336 337 338
		mu 0 4 210 209 213 214
		f 4 -335 339 340 341
		mu 0 4 212 211 215 965
		f 4 342 343 344 345
		mu 0 4 217 218 219 220
		f 4 -345 346 -275 347
		mu 0 4 220 219 170 169
		f 4 348 -226 349 350
		mu 0 4 221 136 135 222
		f 4 351 352 -279 353
		mu 0 4 223 224 174 173
		f 4 -341 354 355 356
		mu 0 4 216 966 225 226
		f 4 357 358 -120 359
		mu 0 4 227 228 73 72
		f 4 360 361 -123 -359
		mu 0 4 228 229 75 73
		f 4 362 363 -126 -362
		mu 0 4 229 230 77 75
		f 4 364 365 -129 -364
		mu 0 4 230 231 79 77
		f 4 366 367 -132 -366
		mu 0 4 231 232 81 79
		f 4 368 369 -135 -368
		mu 0 4 232 233 83 81
		f 4 370 371 -138 -370
		mu 0 4 233 234 85 83
		f 4 372 373 -141 -372
		mu 0 4 234 235 87 85
		f 4 374 375 -144 -374
		mu 0 4 947 236 89 956
		f 4 376 377 -147 -376
		mu 0 4 236 237 91 89
		f 4 -378 378 379 -150
		mu 0 4 91 237 238 93
		f 4 -380 380 381 -153
		mu 0 4 93 238 239 95
		f 4 -382 382 383 -156
		mu 0 4 95 239 240 97
		f 4 -384 384 385 -159
		mu 0 4 97 240 241 99
		f 4 386 387 -162 -386
		mu 0 4 241 242 101 99
		f 4 -388 388 389 -165
		mu 0 4 101 242 243 103
		f 4 390 391 -169 392
		mu 0 4 244 245 106 105
		f 4 393 394 -172 395
		mu 0 4 246 247 108 107
		f 4 396 397 -175 398
		mu 0 4 248 249 110 109
		f 4 399 -399 -178 400
		mu 0 4 250 248 109 111
		f 4 401 -401 -180 402
		mu 0 4 251 250 111 112
		f 4 403 -403 -182 404
		mu 0 4 252 251 112 113
		f 4 405 -405 -184 406
		mu 0 4 253 252 113 114
		f 4 407 -407 -186 408
		mu 0 4 254 253 114 115
		f 4 409 -409 -188 410
		mu 0 4 255 254 115 116
		f 4 411 -411 -189 -395
		mu 0 4 247 255 116 108
		f 4 412 413 -191 414
		mu 0 4 256 257 118 117
		f 4 415 -415 -194 416
		mu 0 4 258 256 117 119
		f 4 417 -417 -196 418
		mu 0 4 259 258 119 120
		f 4 419 -419 -198 420
		mu 0 4 260 259 120 121
		f 4 421 -421 -200 422
		mu 0 4 261 260 121 122
		f 4 423 -423 -202 424
		mu 0 4 262 261 122 123
		f 4 425 -425 -204 426
		mu 0 4 263 262 123 124
		f 4 427 -427 -205 -392
		mu 0 4 245 263 124 106
		f 4 428 429 -206 -398
		mu 0 4 249 264 125 110
		f 4 430 431 -208 -414
		mu 0 4 257 265 126 118
		f 4 432 433 -210 -430
		mu 0 4 264 266 127 125
		f 4 434 435 -212 -432
		mu 0 4 265 267 128 126
		f 4 -390 436 437 438
		mu 0 4 103 243 268 129
		f 4 439 -393 -217 440
		mu 0 4 269 244 105 130
		f 4 441 442 443 -434
		mu 0 4 266 270 131 127
		f 4 444 -396 -222 445
		mu 0 4 271 246 107 132
		f 4 446 -446 447 448
		mu 0 4 272 271 132 133
		f 4 449 450 -227 451
		mu 0 4 903 943 137 136
		f 4 452 453 -230 -451
		mu 0 4 943 942 139 137
		f 4 454 455 -233 -454
		mu 0 4 942 941 141 139
		f 4 456 457 -236 -456
		mu 0 4 941 940 143 141
		f 4 458 459 -239 -458
		mu 0 4 940 939 145 143
		f 4 460 461 -242 -460
		mu 0 4 939 938 147 145
		f 4 462 463 -245 -462
		mu 0 4 938 937 149 147
		f 4 464 465 -248 -464
		mu 0 4 937 936 151 149
		f 4 466 467 -251 -466
		mu 0 4 951 935 153 955
		f 4 468 469 -254 -468
		mu 0 4 935 934 155 153
		f 4 470 471 -257 -470
		mu 0 4 934 933 157 155
		f 4 472 473 -260 -472
		mu 0 4 933 932 159 157
		f 4 474 475 -263 -474
		mu 0 4 932 931 161 159
		f 4 476 477 -266 -476
		mu 0 4 931 930 163 161
		f 4 478 479 -269 -478
		mu 0 4 930 929 165 163
		f 4 480 481 -272 -480
		mu 0 4 929 908 167 165
		f 4 482 483 -276 484
		mu 0 4 907 913 171 170
		f 4 485 486 -280 487
		mu 0 4 905 921 175 174
		f 4 488 489 -284 490
		mu 0 4 928 912 179 178
		f 4 491 -491 -288 492
		mu 0 4 927 928 178 182
		f 4 493 -493 -291 494
		mu 0 4 926 927 182 184
		f 4 495 -495 -294 496
		mu 0 4 925 926 184 186
		f 4 497 -497 -297 498
		mu 0 4 924 925 186 188
		f 4 499 -499 -300 500
		mu 0 4 923 924 188 190
		f 4 501 -501 -303 502
		mu 0 4 922 923 190 192
		f 4 503 -503 -305 -487
		mu 0 4 921 922 192 175
		f 4 504 505 -308 506
		mu 0 4 920 911 195 194
		f 4 507 -507 -312 508
		mu 0 4 919 920 194 198
		f 4 509 -509 -315 510
		mu 0 4 918 919 198 200
		f 4 511 -511 -318 512
		mu 0 4 917 918 200 202
		f 4 513 -513 -321 514
		mu 0 4 916 917 202 204
		f 4 515 -515 -324 516
		mu 0 4 915 916 204 206
		f 4 517 -517 -327 518
		mu 0 4 914 915 206 208
		f 4 519 -519 -329 -484
		mu 0 4 913 914 208 171
		f 4 520 521 -331 -490
		mu 0 4 912 910 209 179
		f 4 522 523 -334 -506
		mu 0 4 911 909 211 195
		f 4 524 525 -337 -522
		mu 0 4 910 906 213 209
		f 4 526 527 -340 -524
		mu 0 4 909 900 215 211
		f 4 528 529 530 -482
		mu 0 4 908 898 218 167
		f 4 531 -485 -347 532
		mu 0 4 899 907 170 219
		f 4 533 534 535 -526
		mu 0 4 906 902 221 213
		f 4 536 -488 -353 537
		mu 0 4 904 905 174 224
		f 4 538 -538 539 540
		mu 0 4 901 904 224 225
		f 4 -122 541 -102 -219
		mu 0 4 71 74 64 63
		f 4 -125 542 -105 -542
		mu 0 4 74 76 65 64
		f 4 -128 543 -107 -543
		mu 0 4 76 78 66 65
		f 4 -131 544 -109 -544
		mu 0 4 78 80 67 66
		f 4 -134 545 -111 -545
		mu 0 4 80 82 68 67
		f 4 -137 546 -113 -546
		mu 0 4 82 84 69 68
		f 4 -140 547 -115 -547
		mu 0 4 84 86 70 69
		f 4 -143 548 -117 -548
		mu 0 4 86 954 54 70
		f 4 549 -118 -85 -225
		mu 0 4 134 44 54 45
		f 4 -104 -211 -444 -220
		mu 0 4 63 36 127 131
		f 4 -338 -536 -351 550
		mu 0 4 214 213 221 222
		f 4 551 552 -350 553
		mu 0 4 227 270 222 135
		f 4 554 555 -357 556
		mu 0 4 272 964 216 226
		f 4 -452 -349 -535 557
		mu 0 4 903 136 221 902
		f 4 -541 -355 -528 558
		mu 0 4 901 225 966 960
		f 4 -549 -146 559 -86
		mu 0 4 969 88 90 55
		f 4 -149 560 -88 -560
		mu 0 4 90 92 56 55
		f 4 -152 561 -90 -561
		mu 0 4 92 94 57 56
		f 4 -155 562 -92 -562
		mu 0 4 94 96 58 57
		f 4 -158 563 -94 -563
		mu 0 4 96 98 59 58
		f 4 -161 564 -96 -564
		mu 0 4 98 100 60 59
		f 4 -164 565 -98 -565
		mu 0 4 100 102 61 60
		f 4 -167 566 -100 -566
		mu 0 4 102 104 62 61
		f 4 -439 -214 -567 -166
		mu 0 4 103 129 62 104
		f 4 -448 -221 -550 -224
		mu 0 4 133 132 44 134
		f 4 -531 -343 567 -273
		mu 0 4 167 218 217 168
		f 4 -356 -540 -352 568
		mu 0 4 226 225 224 223
		f 4 569 570 571 -346
		mu 0 4 220 269 268 217
		f 4 -533 -344 -530 572
		mu 0 4 899 219 218 898
		f 4 573 574 575 576
		mu 0 4 319 320 321 322
		f 4 -576 577 578 579
		mu 0 4 322 321 323 324
		f 4 -579 580 581 582
		mu 0 4 324 323 325 326
		f 4 -582 583 584 585
		mu 0 4 326 325 327 328
		f 4 -585 586 587 588
		mu 0 4 328 327 329 330
		f 4 -588 589 590 591
		mu 0 4 330 329 331 332
		f 4 -591 592 593 594
		mu 0 4 332 331 333 334
		f 4 -594 595 596 597
		mu 0 4 334 333 335 336
		f 4 598 599 600 601
		mu 0 4 337 338 339 340
		f 4 -601 602 603 604
		mu 0 4 340 339 341 342
		f 4 -604 605 606 607
		mu 0 4 342 341 343 344
		f 4 -607 608 609 610
		mu 0 4 344 343 345 346
		f 4 -610 611 612 613
		mu 0 4 346 345 347 348
		f 4 -613 614 615 616
		mu 0 4 348 347 349 350
		f 4 -616 617 618 619
		mu 0 4 350 349 351 352
		f 4 -619 620 621 622
		mu 0 4 352 351 353 354
		f 4 -577 623 624 625
		mu 0 4 319 322 355 356
		f 4 -580 626 627 -624
		mu 0 4 322 324 357 355
		f 4 -583 628 629 -627
		mu 0 4 324 326 358 357
		f 4 -586 630 631 -629
		mu 0 4 326 328 359 358
		f 4 -589 632 633 -631
		mu 0 4 328 330 360 359
		f 4 -592 634 635 -633
		mu 0 4 330 332 361 360
		f 4 -595 636 637 -635
		mu 0 4 332 334 362 361
		f 4 638 639 -637 -598
		mu 0 4 336 363 362 334
		f 4 -602 640 641 642
		mu 0 4 337 340 364 963
		f 4 -605 643 644 -641
		mu 0 4 340 342 366 364
		f 4 -608 645 646 -644
		mu 0 4 342 344 367 366
		f 4 -611 647 648 -646
		mu 0 4 344 346 368 367
		f 4 -614 649 650 -648
		mu 0 4 346 348 369 368
		f 4 -617 651 652 -650
		mu 0 4 348 350 370 369
		f 4 -620 653 654 -652
		mu 0 4 350 352 371 370
		f 4 -623 655 656 -654
		mu 0 4 352 354 372 371
		f 4 -642 657 658 659
		mu 0 4 963 364 373 374
		f 4 -658 -645 660 661
		mu 0 4 373 364 366 375
		f 4 -661 -647 662 663
		mu 0 4 375 366 367 376
		f 4 -663 -649 664 665
		mu 0 4 376 367 368 377
		f 4 -665 -651 666 667
		mu 0 4 377 368 369 378
		f 4 -667 -653 668 669
		mu 0 4 378 369 370 379
		f 4 -669 -655 670 671
		mu 0 4 379 370 371 380
		f 4 -671 -657 672 673
		mu 0 4 380 371 372 381
		f 4 674 -625 675 676
		mu 0 4 382 356 355 383
		f 4 -676 -628 677 678
		mu 0 4 383 355 357 384
		f 4 -678 -630 679 680
		mu 0 4 384 357 358 385
		f 4 -680 -632 681 682
		mu 0 4 385 358 359 386
		f 4 -682 -634 683 684
		mu 0 4 386 359 360 387
		f 4 -684 -636 685 686
		mu 0 4 387 360 361 388
		f 4 -686 -638 687 688
		mu 0 4 388 361 362 389
		f 4 -688 -640 689 690
		mu 0 4 389 362 363 948
		f 4 691 692 693 694
		mu 0 4 390 391 392 393
		f 4 695 696 697 -693
		mu 0 4 391 394 395 392
		f 4 698 699 700 -697
		mu 0 4 394 396 397 395
		f 4 701 702 703 -700
		mu 0 4 396 398 399 397
		f 4 704 705 706 -703
		mu 0 4 398 400 401 399
		f 4 707 708 709 -706
		mu 0 4 400 402 403 401
		f 4 710 711 712 -709
		mu 0 4 402 404 405 403
		f 4 713 714 715 -712
		mu 0 4 404 406 953 405
		f 4 716 717 718 -715
		mu 0 4 949 408 409 407
		f 4 719 720 721 -718
		mu 0 4 408 410 411 409
		f 4 722 723 724 -721
		mu 0 4 410 412 413 411
		f 4 725 726 727 -724
		mu 0 4 412 414 415 413
		f 4 728 729 730 -727
		mu 0 4 414 416 417 415
		f 4 731 732 733 -730
		mu 0 4 416 418 419 417
		f 4 734 735 736 -733
		mu 0 4 418 420 421 419
		f 4 737 738 739 -736
		mu 0 4 420 422 423 421
		f 4 -622 740 741 742
		mu 0 4 354 353 424 425
		f 4 -597 743 744 745
		mu 0 4 336 335 426 427
		f 4 -575 746 747 748
		mu 0 4 321 320 428 429
		f 4 -578 -749 749 750
		mu 0 4 323 321 429 430
		f 4 -581 -751 751 752
		mu 0 4 325 323 430 431
		f 4 -584 -753 753 754
		mu 0 4 327 325 431 432
		f 4 -587 -755 755 756
		mu 0 4 329 327 432 433
		f 4 -590 -757 757 758
		mu 0 4 331 329 433 434
		f 4 -593 -759 759 760
		mu 0 4 333 331 434 435
		f 4 -596 -761 761 -744
		mu 0 4 335 333 435 426
		f 4 -600 762 763 764
		mu 0 4 339 338 436 437
		f 4 -603 -765 765 766
		mu 0 4 341 339 437 438
		f 4 -606 -767 767 768
		mu 0 4 343 341 438 439
		f 4 -609 -769 769 770
		mu 0 4 345 343 439 440
		f 4 -612 -771 771 772
		mu 0 4 347 345 440 441
		f 4 -615 -773 773 774
		mu 0 4 349 347 441 442
		f 4 -618 -775 775 776
		mu 0 4 351 349 442 443
		f 4 -621 -777 777 -741
		mu 0 4 353 351 443 424
		f 4 -574 778 779 -747
		mu 0 4 320 319 444 428
		f 4 -599 780 781 -763
		mu 0 4 338 337 445 436
		f 4 -626 782 783 -779
		mu 0 4 319 356 446 444
		f 4 -643 784 785 -781
		mu 0 4 337 963 962 445
		f 4 -673 786 787 788
		mu 0 4 381 372 448 449
		f 4 -656 -743 789 -787
		mu 0 4 372 354 425 448
		f 4 790 791 -695 792
		mu 0 4 450 382 390 393
		f 4 -639 -746 793 794
		mu 0 4 363 336 427 451
		f 4 -785 795 796 797
		mu 0 4 447 365 452 453
		f 4 798 799 800 801
		mu 0 4 454 455 456 457
		f 4 802 803 804 -800
		mu 0 4 455 458 459 456
		f 4 805 806 807 -804
		mu 0 4 458 460 461 459
		f 4 808 809 810 -807
		mu 0 4 460 462 463 461
		f 4 811 812 813 -810
		mu 0 4 462 464 465 463
		f 4 814 815 816 -813
		mu 0 4 464 466 467 465
		f 4 817 818 819 -816
		mu 0 4 466 468 469 467
		f 4 820 821 822 -819
		mu 0 4 468 470 950 469
		f 4 823 824 825 -822
		mu 0 4 945 472 473 471
		f 4 826 827 828 -825
		mu 0 4 472 474 475 473
		f 4 829 830 831 -828
		mu 0 4 474 476 477 475
		f 4 832 833 834 -831
		mu 0 4 476 478 479 477
		f 4 835 836 837 -834
		mu 0 4 478 480 481 479
		f 4 838 839 840 -837
		mu 0 4 480 482 483 481
		f 4 841 842 843 -840
		mu 0 4 482 484 485 483
		f 4 844 845 846 -843
		mu 0 4 484 486 487 485
		f 4 847 848 849 850
		mu 0 4 488 489 490 491
		f 4 851 852 853 854
		mu 0 4 492 493 494 495
		f 4 855 856 857 858
		mu 0 4 496 497 498 499
		f 4 859 -859 860 861
		mu 0 4 500 496 499 501
		f 4 862 -862 863 864
		mu 0 4 502 500 501 503
		f 4 865 -865 866 867
		mu 0 4 504 502 503 505
		f 4 868 -868 869 870
		mu 0 4 506 504 505 507
		f 4 871 -871 872 873
		mu 0 4 508 506 507 509
		f 4 874 -874 875 876
		mu 0 4 510 508 509 511
		f 4 877 -877 878 -853
		mu 0 4 493 510 511 494
		f 4 879 880 881 882
		mu 0 4 512 513 514 515
		f 4 883 -883 884 885
		mu 0 4 516 512 515 517
		f 4 886 -886 887 888
		mu 0 4 518 516 517 519
		f 4 889 -889 890 891
		mu 0 4 520 518 519 521
		f 4 892 -892 893 894
		mu 0 4 522 520 521 523
		f 4 895 -895 896 897
		mu 0 4 524 522 523 525
		f 4 898 -898 899 900
		mu 0 4 526 524 525 527
		f 4 901 -901 902 -849
		mu 0 4 489 526 527 490
		f 4 903 904 905 -857
		mu 0 4 497 528 529 498
		f 4 906 907 908 -881
		mu 0 4 513 530 531 514
		f 4 909 910 911 -905
		mu 0 4 528 532 533 529
		f 4 912 913 914 -908
		mu 0 4 530 534 959 531
		f 4 915 916 917 918
		mu 0 4 536 537 538 539
		f 4 919 -851 920 -917
		mu 0 4 537 488 491 538
		f 4 921 922 -802 923
		mu 0 4 540 541 454 457
		f 4 924 -855 925 926
		mu 0 4 542 492 495 543
		f 4 927 928 929 -914
		mu 0 4 957 544 545 535
		f 4 930 931 932 -694
		mu 0 4 392 546 547 393
		f 4 933 934 -931 -698
		mu 0 4 395 548 546 392
		f 4 935 936 -934 -701
		mu 0 4 397 549 548 395
		f 4 937 938 -936 -704
		mu 0 4 399 550 549 397
		f 4 939 940 -938 -707
		mu 0 4 401 551 550 399
		f 4 941 942 -940 -710
		mu 0 4 403 552 551 401
		f 4 943 944 -942 -713
		mu 0 4 405 553 552 403
		f 4 945 946 -944 -716
		mu 0 4 953 944 553 405
		f 4 947 948 -946 -719
		mu 0 4 409 555 554 407
		f 4 949 950 -948 -722
		mu 0 4 411 556 555 409
		f 4 -725 951 952 -950
		mu 0 4 411 413 557 556
		f 4 -728 953 954 -952
		mu 0 4 413 415 558 557
		f 4 -731 955 956 -954
		mu 0 4 415 417 559 558
		f 4 -734 957 958 -956
		mu 0 4 417 419 560 559
		f 4 959 960 -958 -737
		mu 0 4 421 561 560 419
		f 4 -740 961 962 -960
		mu 0 4 421 423 562 561
		f 4 963 964 965 -742
		mu 0 4 424 563 564 425
		f 4 966 967 968 -745
		mu 0 4 426 565 566 427
		f 4 969 970 971 -748
		mu 0 4 428 567 568 429
		f 4 -972 972 973 -750
		mu 0 4 429 568 569 430
		f 4 -974 974 975 -752
		mu 0 4 430 569 570 431
		f 4 -976 976 977 -754
		mu 0 4 431 570 571 432
		f 4 -978 978 979 -756
		mu 0 4 432 571 572 433
		f 4 -980 980 981 -758
		mu 0 4 433 572 573 434
		f 4 -982 982 983 -760
		mu 0 4 434 573 574 435
		f 4 -984 984 -967 -762
		mu 0 4 435 574 565 426
		f 4 985 986 987 -764
		mu 0 4 436 575 576 437
		f 4 -988 988 989 -766
		mu 0 4 437 576 577 438
		f 4 -990 990 991 -768
		mu 0 4 438 577 578 439
		f 4 -992 992 993 -770
		mu 0 4 439 578 579 440
		f 4 -994 994 995 -772
		mu 0 4 440 579 580 441
		f 4 -996 996 997 -774
		mu 0 4 441 580 581 442
		f 4 -998 998 999 -776
		mu 0 4 442 581 582 443
		f 4 -1000 1000 -964 -778
		mu 0 4 443 582 563 424
		f 4 1001 1002 -970 -780
		mu 0 4 444 583 567 428
		f 4 1003 1004 -986 -782
		mu 0 4 445 584 575 436
		f 4 1005 1006 -1002 -784
		mu 0 4 446 585 583 444
		f 4 1007 1008 -1004 -786
		mu 0 4 962 958 584 445
		f 4 1009 1010 1011 -962
		mu 0 4 423 449 587 562
		f 4 -966 1012 1013 -790
		mu 0 4 425 564 588 448
		f 4 1014 1015 -1006 1016
		mu 0 4 450 589 585 446
		f 4 -969 1017 1018 -794
		mu 0 4 427 566 590 451
		f 4 -1019 1019 1020 1021
		mu 0 4 451 590 591 453
		f 4 1022 -801 1023 -450
		mu 0 4 273 457 456 274
		f 4 -1024 -805 1024 -453
		mu 0 4 274 456 459 275
		f 4 -1025 -808 1025 -455
		mu 0 4 275 459 461 276
		f 4 -1026 -811 1026 -457
		mu 0 4 276 461 463 277
		f 4 -1027 -814 1027 -459
		mu 0 4 277 463 465 278
		f 4 -1028 -817 1028 -461
		mu 0 4 278 465 467 279
		f 4 -1029 -820 1029 -463
		mu 0 4 279 467 469 280
		f 4 -1030 -823 1030 -465
		mu 0 4 280 469 950 281
		f 4 -1031 -826 1031 -467
		mu 0 4 952 471 473 282
		f 4 -1032 -829 1032 -469
		mu 0 4 282 473 475 283
		f 4 -1033 -832 1033 -471
		mu 0 4 283 475 477 284
		f 4 -1034 -835 1034 -473
		mu 0 4 284 477 479 285
		f 4 -1035 -838 1035 -475
		mu 0 4 285 479 481 286
		f 4 -1036 -841 1036 -477
		mu 0 4 286 481 483 287
		f 4 -1037 -844 1037 -479
		mu 0 4 287 483 485 288
		f 4 -1038 -847 1038 -481
		mu 0 4 288 485 487 289
		f 4 1039 -850 1040 -483
		mu 0 4 290 491 490 291
		f 4 1041 -854 1042 -486
		mu 0 4 292 495 494 293
		f 4 1043 -858 1044 -489
		mu 0 4 294 499 498 295
		f 4 1045 -861 -1044 -492
		mu 0 4 296 501 499 294
		f 4 1046 -864 -1046 -494
		mu 0 4 297 503 501 296
		f 4 1047 -867 -1047 -496
		mu 0 4 298 505 503 297
		f 4 1048 -870 -1048 -498
		mu 0 4 299 507 505 298
		f 4 1049 -873 -1049 -500
		mu 0 4 300 509 507 299
		f 4 1050 -876 -1050 -502
		mu 0 4 301 511 509 300
		f 4 -1043 -879 -1051 -504
		mu 0 4 293 494 511 301
		f 4 1051 -882 1052 -505
		mu 0 4 302 515 514 303
		f 4 1053 -885 -1052 -508
		mu 0 4 304 517 515 302
		f 4 1054 -888 -1054 -510
		mu 0 4 305 519 517 304
		f 4 1055 -891 -1055 -512
		mu 0 4 306 521 519 305
		f 4 1056 -894 -1056 -514
		mu 0 4 307 523 521 306
		f 4 1057 -897 -1057 -516
		mu 0 4 308 525 523 307
		f 4 1058 -900 -1058 -518
		mu 0 4 309 527 525 308
		f 4 -1041 -903 -1059 -520
		mu 0 4 291 490 527 309
		f 4 -1045 -906 1059 -521
		mu 0 4 295 498 529 310
		f 4 -1053 -909 1060 -523
		mu 0 4 303 514 531 311
		f 4 -1060 -912 1061 -525
		mu 0 4 310 529 533 312
		f 4 -1061 -915 1062 -527
		mu 0 4 311 531 959 313
		f 4 -1039 1063 1064 -529
		mu 0 4 289 487 539 314
		f 4 1065 -921 -1040 -532
		mu 0 4 315 538 491 290
		f 4 -1062 1066 1067 -534
		mu 0 4 312 533 540 316
		f 4 1068 -926 -1042 -537
		mu 0 4 317 543 495 292
		f 4 1069 1070 -1069 -539
		mu 0 4 318 545 543 317
		f 4 -792 -677 1071 -692
		mu 0 4 390 382 383 391
		f 4 -1072 -679 1072 -696
		mu 0 4 391 383 384 394
		f 4 -1073 -681 1073 -699
		mu 0 4 394 384 385 396
		f 4 -1074 -683 1074 -702
		mu 0 4 396 385 386 398
		f 4 -1075 -685 1075 -705
		mu 0 4 398 386 387 400
		f 4 -1076 -687 1076 -708
		mu 0 4 400 387 388 402
		f 4 -1077 -689 1077 -711
		mu 0 4 402 388 389 404
		f 4 -1078 -691 1078 -714
		mu 0 4 404 389 948 406
		f 4 -796 -660 -690 1079
		mu 0 4 452 365 948 363
		f 4 -791 -1017 -783 -675
		mu 0 4 382 450 446 356
		f 4 1080 -922 -1067 -911
		mu 0 4 532 541 540 533
		f 4 1081 -923 1082 1083
		mu 0 4 547 454 541 589
		f 4 1084 -928 1085 1086
		mu 0 4 591 544 957 586
		f 4 -558 -1068 -924 -1023
		mu 0 4 273 316 540 457
		f 4 -559 -1063 -930 -1070
		mu 0 4 318 961 535 545
		f 4 -659 1087 -717 -1079
		mu 0 4 374 373 408 949
		f 4 -1088 -662 1088 -720
		mu 0 4 408 373 375 410
		f 4 -1089 -664 1089 -723
		mu 0 4 410 375 376 412
		f 4 -1090 -666 1090 -726
		mu 0 4 412 376 377 414
		f 4 -1091 -668 1091 -729
		mu 0 4 414 377 378 416
		f 4 -1092 -670 1092 -732
		mu 0 4 416 378 379 418
		f 4 -1093 -672 1093 -735
		mu 0 4 418 379 380 420
		f 4 -1094 -674 1094 -738
		mu 0 4 420 380 381 422
		f 4 -739 -1095 -789 -1010
		mu 0 4 423 422 381 449
		f 4 -797 -1080 -795 -1022
		mu 0 4 453 452 363 451
		f 4 -846 1095 -919 -1064
		mu 0 4 487 486 536 539
		f 4 1096 -927 -1071 -929
		mu 0 4 544 542 543 545
		f 4 1097 1098 -916 1099
		mu 0 4 587 588 537 536
		f 4 -573 -1065 -918 -1066
		mu 0 4 315 314 539 538
		f 4 -229 1100 -358 -554
		mu 0 4 135 138 228 227
		f 4 -232 1101 -361 -1101
		mu 0 4 138 140 229 228;
	setAttr ".fc[500:893]"
		f 4 -235 1102 -363 -1102
		mu 0 4 140 142 230 229
		f 4 -238 1103 -365 -1103
		mu 0 4 142 144 231 230
		f 4 -241 1104 -367 -1104
		mu 0 4 144 146 232 231
		f 4 -244 1105 -369 -1105
		mu 0 4 146 148 233 232
		f 4 -247 1106 -371 -1106
		mu 0 4 148 150 234 233
		f 4 -250 1107 -373 -1107
		mu 0 4 150 946 235 234
		f 4 -253 1108 -375 -1108
		mu 0 4 152 154 236 947
		f 4 -256 1109 -377 -1109
		mu 0 4 154 156 237 236
		f 4 -259 1110 -379 -1110
		mu 0 4 156 158 238 237
		f 4 -262 1111 -381 -1111
		mu 0 4 158 160 239 238
		f 4 -265 1112 -383 -1112
		mu 0 4 160 162 240 239
		f 4 -268 1113 -385 -1113
		mu 0 4 162 164 241 240
		f 4 -271 1114 -387 -1114
		mu 0 4 164 166 242 241
		f 4 -274 1115 -389 -1115
		mu 0 4 166 168 243 242
		f 4 1116 -391 1117 -278
		mu 0 4 172 245 244 169
		f 4 1118 -394 1119 -282
		mu 0 4 176 247 246 173
		f 4 1120 -397 1121 -286
		mu 0 4 180 249 248 177
		f 4 -289 -1122 -400 1122
		mu 0 4 181 177 248 250
		f 4 -292 -1123 -402 1123
		mu 0 4 183 181 250 251
		f 4 -295 -1124 -404 1124
		mu 0 4 185 183 251 252
		f 4 -298 -1125 -406 1125
		mu 0 4 187 185 252 253
		f 4 -301 -1126 -408 1126
		mu 0 4 189 187 253 254
		f 4 -304 -1127 -410 1127
		mu 0 4 191 189 254 255
		f 4 -1128 -412 -1119 -306
		mu 0 4 191 255 247 176
		f 4 1128 -413 1129 -310
		mu 0 4 196 257 256 193
		f 4 -313 -1130 -416 1130
		mu 0 4 197 193 256 258
		f 4 -316 -1131 -418 1131
		mu 0 4 199 197 258 259
		f 4 -319 -1132 -420 1132
		mu 0 4 201 199 259 260
		f 4 -322 -1133 -422 1133
		mu 0 4 203 201 260 261
		f 4 -325 -1134 -424 1134
		mu 0 4 205 203 261 262
		f 4 -328 -1135 -426 1135
		mu 0 4 207 205 262 263
		f 4 -1136 -428 -1117 -330
		mu 0 4 207 263 245 172
		f 4 1136 -429 -1121 -333
		mu 0 4 210 264 249 180
		f 4 1137 -431 -1129 -336
		mu 0 4 212 265 257 196
		f 4 -339 1138 -433 -1137
		mu 0 4 210 214 266 264
		f 4 -342 -556 -435 -1138
		mu 0 4 212 965 267 265
		f 4 -572 -437 -1116 -568
		mu 0 4 217 268 243 168
		f 4 -348 -1118 -440 -570
		mu 0 4 220 169 244 269
		f 4 -551 -553 -442 -1139
		mu 0 4 214 222 270 266
		f 4 -354 -1120 -445 1139
		mu 0 4 223 173 246 271
		f 4 -1140 -447 -557 -569
		mu 0 4 223 271 272 226
		f 4 -218 -443 -552 -360
		mu 0 4 72 131 270 227
		f 4 -223 -436 -555 -449
		mu 0 4 133 967 964 272
		f 4 -441 -215 -438 -571
		mu 0 4 269 130 129 268
		f 4 -799 -1082 -932 1140
		mu 0 4 455 454 547 546
		f 4 -803 -1141 -935 1141
		mu 0 4 458 455 546 548
		f 4 -806 -1142 -937 1142
		mu 0 4 460 458 548 549
		f 4 -809 -1143 -939 1143
		mu 0 4 462 460 549 550
		f 4 -812 -1144 -941 1144
		mu 0 4 464 462 550 551
		f 4 -815 -1145 -943 1145
		mu 0 4 466 464 551 552
		f 4 -818 -1146 -945 1146
		mu 0 4 468 466 552 553
		f 4 -821 -1147 -947 1147
		mu 0 4 470 468 553 944
		f 4 -824 -1148 -949 1148
		mu 0 4 472 945 554 555
		f 4 -827 -1149 -951 1149
		mu 0 4 474 472 555 556
		f 4 -830 -1150 -953 1150
		mu 0 4 476 474 556 557
		f 4 -833 -1151 -955 1151
		mu 0 4 478 476 557 558
		f 4 -836 -1152 -957 1152
		mu 0 4 480 478 558 559
		f 4 -839 -1153 -959 1153
		mu 0 4 482 480 559 560
		f 4 -842 -1154 -961 1154
		mu 0 4 484 482 560 561
		f 4 -845 -1155 -963 1155
		mu 0 4 486 484 561 562
		f 4 1156 -965 1157 -848
		mu 0 4 488 564 563 489
		f 4 1158 -968 1159 -852
		mu 0 4 492 566 565 493
		f 4 -856 1160 -971 1161
		mu 0 4 497 496 568 567
		f 4 -860 1162 -973 -1161
		mu 0 4 496 500 569 568
		f 4 -863 1163 -975 -1163
		mu 0 4 500 502 570 569
		f 4 -866 1164 -977 -1164
		mu 0 4 502 504 571 570
		f 4 -869 1165 -979 -1165
		mu 0 4 504 506 572 571
		f 4 -872 1166 -981 -1166
		mu 0 4 506 508 573 572
		f 4 -875 1167 -983 -1167
		mu 0 4 508 510 574 573
		f 4 -878 -1160 -985 -1168
		mu 0 4 510 493 565 574
		f 4 -880 1168 -987 1169
		mu 0 4 513 512 576 575
		f 4 -884 1170 -989 -1169
		mu 0 4 512 516 577 576
		f 4 -887 1171 -991 -1171
		mu 0 4 516 518 578 577
		f 4 -890 1172 -993 -1172
		mu 0 4 518 520 579 578
		f 4 -893 1173 -995 -1173
		mu 0 4 520 522 580 579
		f 4 -896 1174 -997 -1174
		mu 0 4 522 524 581 580
		f 4 -899 1175 -999 -1175
		mu 0 4 524 526 582 581
		f 4 -902 -1158 -1001 -1176
		mu 0 4 526 489 563 582
		f 4 -1162 -1003 1176 -904
		mu 0 4 497 567 583 528
		f 4 -1170 -1005 1177 -907
		mu 0 4 513 575 584 530
		f 4 -910 -1177 -1007 1178
		mu 0 4 532 528 583 585
		f 4 -913 -1178 -1009 -1086
		mu 0 4 534 530 584 958
		f 4 -1156 -1012 -1100 -1096
		mu 0 4 486 562 587 536
		f 4 -920 -1099 -1013 -1157
		mu 0 4 488 537 588 564
		f 4 -1083 -1081 -1179 -1016
		mu 0 4 589 541 532 585
		f 4 -925 1179 -1018 -1159
		mu 0 4 492 542 590 566
		f 4 -1085 -1020 -1180 -1097
		mu 0 4 544 591 590 542
		f 4 -1015 -793 -933 -1084
		mu 0 4 589 450 393 547
		f 4 -798 -1021 -1087 -1008
		mu 0 4 447 453 591 586
		f 4 -788 -1014 -1098 -1011
		mu 0 4 449 448 588 587
		f 4 1180 1181 1182 1183
		mu 0 4 592 593 594 595
		f 4 1184 1185 -1181 1186
		mu 0 4 596 597 593 592
		f 4 1187 1188 -1185 1189
		mu 0 4 598 599 597 596
		f 4 1190 1191 -1188 1192
		mu 0 4 600 601 599 598
		f 4 1193 1194 -1191 1195
		mu 0 4 602 603 601 600
		f 4 1196 1197 -1194 1198
		mu 0 4 604 605 603 602
		f 4 1199 1200 -1197 1201
		mu 0 4 606 607 605 604
		f 4 -1183 1202 -1200 1203
		mu 0 4 595 594 607 606
		f 4 1204 1205 1206 -1184
		mu 0 4 595 608 609 592
		f 4 1207 1208 1209 1210
		mu 0 4 610 611 612 613
		f 4 -1207 1211 1212 -1187
		mu 0 4 592 609 614 596
		f 4 1213 1214 -1208 1215
		mu 0 4 615 616 611 610
		f 4 -1213 1216 1217 -1190
		mu 0 4 596 614 617 598
		f 4 1218 1219 -1214 1220
		mu 0 4 618 619 616 615
		f 4 -1218 1221 1222 -1193
		mu 0 4 598 617 620 600
		f 4 1223 1224 -1219 1225
		mu 0 4 621 622 619 618
		f 4 -1223 1226 1227 -1196
		mu 0 4 600 620 623 602
		f 4 1228 1229 -1224 1230
		mu 0 4 624 625 622 621
		f 4 -1228 1231 1232 -1199
		mu 0 4 602 623 626 604
		f 4 1233 1234 -1229 1235
		mu 0 4 627 628 625 624
		f 4 -1233 1236 1237 -1202
		mu 0 4 604 626 629 606
		f 4 1238 1239 -1234 1240
		mu 0 4 630 631 628 627
		f 4 -1238 1241 -1205 -1204
		mu 0 4 606 629 608 595
		f 4 -1210 1242 -1239 1243
		mu 0 4 613 612 631 630
		f 4 1244 1245 1246 1247
		mu 0 4 632 633 634 635
		f 4 1248 1249 -1245 1250
		mu 0 4 636 637 633 632
		f 4 1251 1252 -1249 1253
		mu 0 4 638 639 637 636
		f 4 1254 1255 -1252 1256
		mu 0 4 640 641 639 638
		f 4 1257 1258 -1255 1259
		mu 0 4 642 643 641 640
		f 4 1260 1261 -1258 1262
		mu 0 4 644 645 643 642
		f 4 1263 1264 -1261 1265
		mu 0 4 646 647 645 644
		f 4 -1247 1266 -1264 1267
		mu 0 4 635 634 647 646
		f 4 1268 1269 1270 1271
		mu 0 4 648 649 650 651
		f 4 1272 1273 -1269 1274
		mu 0 4 652 653 649 648
		f 4 1275 1276 -1273 1277
		mu 0 4 654 655 653 652
		f 4 1278 1279 -1276 1280
		mu 0 4 656 657 655 654
		f 4 1281 1282 -1279 1283
		mu 0 4 658 659 657 656
		f 4 1284 1285 -1282 1286
		mu 0 4 660 661 659 658
		f 4 1287 1288 -1285 1289
		mu 0 4 662 663 661 660
		f 4 -1271 1290 -1288 1291
		mu 0 4 651 650 663 662
		f 4 1292 1293 1294 1295
		mu 0 4 664 665 666 667
		f 4 1296 1297 -1293 1298
		mu 0 4 668 669 665 664
		f 4 1299 1300 -1297 1301
		mu 0 4 670 671 669 668
		f 4 1302 1303 -1300 1304
		mu 0 4 672 673 671 670
		f 4 1305 1306 -1303 1307
		mu 0 4 674 675 673 672
		f 4 1308 1309 -1306 1310
		mu 0 4 676 677 675 674
		f 4 1311 1312 -1309 1313
		mu 0 4 678 679 677 676
		f 4 -1295 1314 -1312 1315
		mu 0 4 667 666 679 678
		f 4 1316 1317 1318 1319
		mu 0 4 680 681 682 683
		f 4 1320 1321 -1317 1322
		mu 0 4 684 685 681 680
		f 4 1323 1324 -1321 1325
		mu 0 4 686 687 685 684
		f 4 1326 1327 -1324 1328
		mu 0 4 688 689 687 686
		f 4 1329 1330 -1327 1331
		mu 0 4 690 691 689 688
		f 4 1332 1333 -1330 1334
		mu 0 4 692 693 691 690
		f 4 1335 1336 -1333 1337
		mu 0 4 694 695 693 692
		f 4 -1319 1338 -1336 1339
		mu 0 4 683 682 695 694
		f 4 1340 1341 1342 1343
		mu 0 4 696 697 698 699
		f 4 1344 1345 1346 -1342
		mu 0 4 697 700 701 698
		f 4 1347 1348 1349 -1346
		mu 0 4 700 702 703 701
		f 4 1350 1351 1352 -1349
		mu 0 4 702 704 705 703
		f 4 1353 1354 1355 -1352
		mu 0 4 704 706 707 705
		f 4 1356 1357 1358 -1355
		mu 0 4 706 708 709 707
		f 4 1359 1360 1361 -1358
		mu 0 4 708 710 711 709
		f 4 1362 -1344 1363 -1361
		mu 0 4 710 696 699 711
		f 4 -1343 1364 1365 1366
		mu 0 4 699 698 712 713
		f 4 -1347 1367 1368 -1365
		mu 0 4 698 701 714 712
		f 4 -1350 1369 1370 -1368
		mu 0 4 701 703 715 714
		f 4 -1353 1371 1372 -1370
		mu 0 4 703 705 716 715
		f 4 -1356 1373 1374 -1372
		mu 0 4 705 707 717 716
		f 4 -1359 1375 1376 -1374
		mu 0 4 707 709 718 717
		f 4 -1362 1377 1378 -1376
		mu 0 4 709 711 719 718
		f 4 -1364 -1367 1379 -1378
		mu 0 4 711 699 713 719
		f 4 1380 1381 1382 1383
		mu 0 4 720 721 722 723
		f 4 -1383 1384 1385 1386
		mu 0 4 723 722 724 725
		f 4 -1386 1387 1388 1389
		mu 0 4 725 724 726 727
		f 4 -1389 1390 1391 1392
		mu 0 4 727 726 728 729
		f 4 -1392 1393 1394 1395
		mu 0 4 729 728 730 731
		f 4 -1395 1396 1397 1398
		mu 0 4 731 730 732 733
		f 4 -1398 1399 1400 1401
		mu 0 4 733 732 734 735
		f 4 -1401 1402 -1381 1403
		mu 0 4 735 734 721 720
		f 4 1404 1405 1406 1407
		mu 0 4 736 737 738 739
		f 4 -1407 1408 1409 1410
		mu 0 4 739 738 740 741
		f 4 -1410 1411 1412 1413
		mu 0 4 741 740 742 743
		f 4 -1413 1414 1415 1416
		mu 0 4 743 742 744 745
		f 4 -1416 1417 1418 1419
		mu 0 4 745 744 746 747
		f 4 -1419 1420 1421 1422
		mu 0 4 747 746 748 749
		f 4 -1422 1423 1424 1425
		mu 0 4 749 748 750 751
		f 4 -1425 1426 -1405 1427
		mu 0 4 751 750 737 736
		f 4 1428 1429 1430 1431
		mu 0 4 752 753 754 755
		f 4 -1431 1432 1433 1434
		mu 0 4 755 754 756 757
		f 4 -1434 1435 1436 1437
		mu 0 4 757 756 758 759
		f 4 -1437 1438 1439 1440
		mu 0 4 759 758 760 761
		f 4 -1440 1441 1442 1443
		mu 0 4 761 760 762 763
		f 4 -1443 1444 1445 1446
		mu 0 4 763 762 764 765
		f 4 -1446 1447 1448 1449
		mu 0 4 765 764 766 767
		f 4 -1449 1450 -1429 1451
		mu 0 4 767 766 753 752
		f 4 1452 1453 1454 1455
		mu 0 4 768 769 770 771
		f 4 1456 -1456 1457 1458
		mu 0 4 772 768 771 773
		f 4 1459 -1459 1460 1461
		mu 0 4 774 772 773 775
		f 4 1462 -1462 1463 1464
		mu 0 4 776 774 775 777
		f 4 1465 -1465 1466 1467
		mu 0 4 778 776 777 779
		f 4 1468 -1468 1469 1470
		mu 0 4 780 778 779 781
		f 4 1471 -1471 1472 1473
		mu 0 4 782 780 781 783
		f 4 1474 -1474 1475 -1454
		mu 0 4 769 782 783 770
		f 4 1476 1477 1478 -1455
		mu 0 4 770 784 785 771
		f 4 -1479 1479 1480 -1458
		mu 0 4 771 785 786 773
		f 4 -1481 1481 1482 -1461
		mu 0 4 773 786 787 775
		f 4 -1483 1483 1484 -1464
		mu 0 4 775 787 788 777
		f 4 -1485 1485 1486 -1467
		mu 0 4 777 788 789 779
		f 4 -1487 1487 1488 -1470
		mu 0 4 779 789 790 781
		f 4 -1489 1489 1490 -1473
		mu 0 4 781 790 791 783
		f 4 -1491 1491 -1477 -1476
		mu 0 4 783 791 784 770
		f 4 1492 1493 -1182 1494
		mu 0 4 970 971 972 973
		f 4 1495 -1495 -1186 1496
		mu 0 4 974 970 973 975
		f 4 1497 -1497 -1189 1498
		mu 0 4 976 974 975 977
		f 4 1499 -1499 -1192 1500
		mu 0 4 978 976 977 979
		f 4 1501 -1501 -1195 1502
		mu 0 4 980 978 979 981
		f 4 1503 -1503 -1198 1504
		mu 0 4 987 980 981 986
		f 4 1505 -1505 -1201 1506
		mu 0 4 984 982 983 985
		f 4 1507 -1507 -1203 -1494
		mu 0 4 971 984 985 972
		f 4 1508 1509 -1406 1510
		mu 0 4 800 801 738 737
		f 4 1511 1512 -1409 -1510
		mu 0 4 801 802 740 738
		f 4 1513 1514 -1412 -1513
		mu 0 4 802 803 742 740
		f 4 1515 1516 -1415 -1515
		mu 0 4 803 804 744 742
		f 4 1517 1518 -1418 -1517
		mu 0 4 804 805 746 744
		f 4 1519 1520 -1421 -1519
		mu 0 4 805 806 748 746
		f 4 1521 1522 -1424 -1521
		mu 0 4 806 807 750 748
		f 4 1523 -1511 -1427 -1523
		mu 0 4 807 800 737 750
		f 4 1524 1525 -1430 1526
		mu 0 4 808 809 754 753
		f 4 1527 1528 -1433 -1526
		mu 0 4 809 810 756 754
		f 4 1529 1530 -1436 -1529
		mu 0 4 810 811 758 756
		f 4 1531 1532 -1439 -1531
		mu 0 4 811 812 760 758
		f 4 1533 1534 -1442 -1533
		mu 0 4 812 813 762 760
		f 4 1535 1536 -1445 -1535
		mu 0 4 813 814 764 762
		f 4 1537 1538 -1448 -1537
		mu 0 4 814 815 766 764
		f 4 1539 -1527 -1451 -1539
		mu 0 4 815 808 753 766
		f 4 -1432 1540 -1509 1541
		mu 0 4 752 755 801 800
		f 4 -1435 1542 -1512 -1541
		mu 0 4 755 757 802 801
		f 4 -1438 1543 -1514 -1543
		mu 0 4 757 759 803 802
		f 4 -1441 1544 -1516 -1544
		mu 0 4 759 761 804 803
		f 4 -1444 1545 -1518 -1545
		mu 0 4 761 763 805 804
		f 4 -1447 1546 -1520 -1546
		mu 0 4 763 765 806 805
		f 4 -1450 1547 -1522 -1547
		mu 0 4 765 767 807 806
		f 4 -1452 -1542 -1524 -1548
		mu 0 4 767 752 800 807
		f 4 -1453 1548 -1525 1549
		mu 0 4 769 768 809 808
		f 4 -1457 1550 -1528 -1549
		mu 0 4 768 772 810 809
		f 4 -1460 1551 -1530 -1551
		mu 0 4 772 774 811 810
		f 4 -1463 1552 -1532 -1552
		mu 0 4 774 776 812 811
		f 4 -1466 1553 -1534 -1553
		mu 0 4 776 778 813 812
		f 4 -1469 1554 -1536 -1554
		mu 0 4 778 780 814 813
		f 4 -1472 1555 -1538 -1555
		mu 0 4 780 782 815 814
		f 4 -1475 -1550 -1540 -1556
		mu 0 4 782 769 808 815
		f 4 1556 1557 -1206 1558
		mu 0 4 816 817 609 608
		f 4 1559 1560 -1212 -1558
		mu 0 4 817 818 614 609
		f 4 1561 1562 -1217 -1561
		mu 0 4 818 819 617 614
		f 4 1563 1564 -1222 -1563
		mu 0 4 819 820 620 617
		f 4 1565 1566 -1227 -1565
		mu 0 4 820 821 623 620
		f 4 1567 1568 -1232 -1567
		mu 0 4 821 822 626 623
		f 4 1569 1570 -1237 -1569
		mu 0 4 822 823 629 626
		f 4 1571 -1559 -1242 -1571
		mu 0 4 823 816 608 629
		f 4 -1384 1572 -1557 1573
		mu 0 4 720 723 817 816
		f 4 -1387 1574 -1560 -1573
		mu 0 4 723 725 818 817
		f 4 -1390 1575 -1562 -1575
		mu 0 4 725 727 819 818
		f 4 -1393 1576 -1564 -1576
		mu 0 4 727 729 820 819
		f 4 -1396 1577 -1566 -1577
		mu 0 4 729 731 821 820
		f 4 -1399 1578 -1568 -1578
		mu 0 4 731 733 822 821
		f 4 -1402 1579 -1570 -1579
		mu 0 4 733 735 823 822
		f 4 -1404 -1574 -1572 -1580
		mu 0 4 735 720 816 823
		f 4 -1408 1580 -1382 1581
		mu 0 4 736 739 722 721
		f 4 -1411 1582 -1385 -1581
		mu 0 4 739 741 724 722
		f 4 -1414 1583 -1388 -1583
		mu 0 4 741 743 726 724
		f 4 -1417 1584 -1391 -1584
		mu 0 4 743 745 728 726
		f 4 -1420 1585 -1394 -1585
		mu 0 4 745 747 730 728
		f 4 -1423 1586 -1397 -1586
		mu 0 4 747 749 732 730
		f 4 -1426 1587 -1400 -1587
		mu 0 4 749 751 734 732
		f 4 -1428 -1582 -1403 -1588
		mu 0 4 751 736 721 734
		f 4 -1248 1588 1589 1590
		mu 0 4 632 635 824 825
		f 4 -1251 -1591 1591 1592
		mu 0 4 636 632 825 826
		f 4 -1254 -1593 1593 1594
		mu 0 4 638 636 826 827
		f 4 -1257 -1595 1595 1596
		mu 0 4 640 638 827 828
		f 4 -1260 -1597 1597 1598
		mu 0 4 642 640 828 829
		f 4 -1263 -1599 1599 1600
		mu 0 4 644 642 829 830
		f 4 -1266 -1601 1601 1602
		mu 0 4 646 644 830 831
		f 4 -1268 -1603 1603 -1589
		mu 0 4 635 646 831 824
		f 4 -1211 1604 -1493 1605
		mu 0 4 610 613 793 792
		f 4 -1216 -1606 -1496 1606
		mu 0 4 615 610 792 794
		f 4 -1221 -1607 -1498 1607
		mu 0 4 618 615 794 795
		f 4 -1226 -1608 -1500 1608
		mu 0 4 621 618 795 796
		f 4 -1231 -1609 -1502 1609
		mu 0 4 624 621 796 797
		f 4 -1236 -1610 -1504 1610
		mu 0 4 627 624 797 798
		f 4 -1241 -1611 -1506 1611
		mu 0 4 630 627 798 799
		f 4 -1244 -1612 -1508 -1605
		mu 0 4 613 630 799 793
		f 4 1612 1613 -1246 1614
		mu 0 4 832 833 634 633
		f 4 1615 -1615 -1250 1616
		mu 0 4 834 832 633 637
		f 4 1617 -1617 -1253 1618
		mu 0 4 835 834 637 639
		f 4 1619 -1619 -1256 1620
		mu 0 4 836 835 639 641
		f 4 1621 -1621 -1259 1622
		mu 0 4 837 836 641 643
		f 4 1623 -1623 -1262 1624
		mu 0 4 838 837 643 645
		f 4 1625 -1625 -1265 1626
		mu 0 4 839 838 645 647
		f 4 1627 -1627 -1267 -1614
		mu 0 4 833 839 647 634
		f 4 -1590 1628 -1209 1629
		mu 0 4 825 824 612 611
		f 4 -1592 -1630 -1215 1630
		mu 0 4 826 825 611 616
		f 4 -1594 -1631 -1220 1631
		mu 0 4 827 826 616 619
		f 4 -1596 -1632 -1225 1632
		mu 0 4 828 827 619 622
		f 4 -1598 -1633 -1230 1633
		mu 0 4 829 828 622 625
		f 4 -1600 -1634 -1235 1634
		mu 0 4 830 829 625 628
		f 4 -1602 -1635 -1240 1635
		mu 0 4 831 830 628 631
		f 4 -1604 -1636 -1243 -1629
		mu 0 4 824 831 631 612
		f 4 1636 1637 -1270 1638
		mu 0 4 840 841 650 649
		f 4 1639 -1639 -1274 1640
		mu 0 4 842 840 649 653
		f 4 1641 -1641 -1277 1642
		mu 0 4 843 842 653 655
		f 4 1643 -1643 -1280 1644
		mu 0 4 844 843 655 657
		f 4 1645 -1645 -1283 1646
		mu 0 4 845 844 657 659
		f 4 1647 -1647 -1286 1648
		mu 0 4 846 845 659 661
		f 4 1649 -1649 -1289 1650
		mu 0 4 847 846 661 663
		f 4 1651 -1651 -1291 -1638
		mu 0 4 841 847 663 650
		f 4 -1272 1652 -1613 1653
		mu 0 4 648 651 833 832
		f 4 -1275 -1654 -1616 1654
		mu 0 4 652 648 832 834
		f 4 -1278 -1655 -1618 1655
		mu 0 4 654 652 834 835
		f 4 -1281 -1656 -1620 1656
		mu 0 4 656 654 835 836
		f 4 -1284 -1657 -1622 1657
		mu 0 4 658 656 836 837
		f 4 -1287 -1658 -1624 1658
		mu 0 4 660 658 837 838
		f 4 -1290 -1659 -1626 1659
		mu 0 4 662 660 838 839
		f 4 -1292 -1660 -1628 -1653
		mu 0 4 651 662 839 833
		f 4 -1296 1660 -1637 1661
		mu 0 4 664 667 841 840
		f 4 -1299 -1662 -1640 1662
		mu 0 4 668 664 840 842
		f 4 -1302 -1663 -1642 1663
		mu 0 4 670 668 842 843
		f 4 -1305 -1664 -1644 1664
		mu 0 4 672 670 843 844
		f 4 -1308 -1665 -1646 1665
		mu 0 4 674 672 844 845
		f 4 -1311 -1666 -1648 1666
		mu 0 4 676 674 845 846
		f 4 -1314 -1667 -1650 1667
		mu 0 4 678 676 846 847
		f 4 -1316 -1668 -1652 -1661
		mu 0 4 667 678 847 841
		f 4 -1320 1668 -1294 1669
		mu 0 4 680 683 666 665
		f 4 -1323 -1670 -1298 1670
		mu 0 4 684 680 665 669
		f 4 -1326 -1671 -1301 1671
		mu 0 4 686 684 669 671
		f 4 -1329 -1672 -1304 1672
		mu 0 4 688 686 671 673
		f 4 -1332 -1673 -1307 1673
		mu 0 4 690 688 673 675
		f 4 -1335 -1674 -1310 1674
		mu 0 4 692 690 675 677
		f 4 -1338 -1675 -1313 1675
		mu 0 4 694 692 677 679
		f 4 -1340 -1676 -1315 -1669
		mu 0 4 683 694 679 666
		f 4 1676 1677 -1318 1678
		mu 0 4 848 849 682 681
		f 4 1679 -1679 -1322 1680
		mu 0 4 850 848 681 685
		f 4 1681 -1681 -1325 1682
		mu 0 4 851 850 685 687
		f 4 1683 -1683 -1328 1684
		mu 0 4 852 851 687 689
		f 4 1685 -1685 -1331 1686
		mu 0 4 853 852 689 691
		f 4 1687 -1687 -1334 1688
		mu 0 4 854 853 691 693
		f 4 1689 -1689 -1337 1690
		mu 0 4 855 854 693 695
		f 4 1691 -1691 -1339 -1678
		mu 0 4 849 855 695 682
		f 4 -1341 1692 -1677 1693
		mu 0 4 697 696 849 848
		f 4 -1345 -1694 -1680 1694
		mu 0 4 700 697 848 850
		f 4 -1348 -1695 -1682 1695
		mu 0 4 702 700 850 851
		f 4 -1351 -1696 -1684 1696
		mu 0 4 704 702 851 852
		f 4 -1354 -1697 -1686 1697
		mu 0 4 706 704 852 853
		f 4 -1357 -1698 -1688 1698
		mu 0 4 708 706 853 854
		f 4 -1360 -1699 -1690 1699
		mu 0 4 710 708 854 855
		f 4 -1363 -1700 -1692 -1693
		mu 0 4 696 710 855 849
		f 4 1700 1701 1702 1703
		mu 0 4 856 857 858 859
		f 4 1704 1705 1706 -1702
		mu 0 4 857 860 861 858
		f 4 1707 1708 1709 -1706
		mu 0 4 860 862 863 861
		f 4 1710 1711 1712 -1709
		mu 0 4 862 864 865 863
		f 4 1713 1714 1715 -1712
		mu 0 4 864 866 867 865
		f 4 1716 1717 1718 -1715
		mu 0 4 866 868 869 867
		f 4 1719 1720 1721 -1718
		mu 0 4 868 870 871 869
		f 4 1722 -1704 1723 -1721
		mu 0 4 870 856 859 871
		f 4 1724 -1701 1725 1726
		mu 0 4 872 857 856 873
		f 4 1727 -1705 -1725 1728
		mu 0 4 874 860 857 872
		f 4 1729 -1708 -1728 1730
		mu 0 4 875 862 860 874
		f 4 1731 -1711 -1730 1732
		mu 0 4 876 864 862 875
		f 4 1733 -1714 -1732 1734
		mu 0 4 877 866 864 876
		f 4 1735 -1717 -1734 1736
		mu 0 4 878 868 866 877
		f 4 1737 -1720 -1736 1738
		mu 0 4 879 870 868 878
		f 4 -1726 -1723 -1738 1739
		mu 0 4 873 856 870 879
		f 4 -1703 1740 1741 1742
		mu 0 4 859 858 880 881
		f 4 -1707 1743 1744 -1741
		mu 0 4 858 861 882 880
		f 4 -1710 1745 1746 -1744
		mu 0 4 861 863 883 882
		f 4 -1713 1747 1748 -1746
		mu 0 4 863 865 884 883
		f 4 -1716 1749 1750 -1748
		mu 0 4 865 867 885 884
		f 4 -1719 1751 1752 -1750
		mu 0 4 867 869 886 885
		f 4 -1722 1753 1754 -1752
		mu 0 4 869 871 887 886
		f 4 -1724 -1743 1755 -1754
		mu 0 4 871 859 881 887
		f 4 -1742 1756 -1478 1757
		mu 0 4 881 880 785 784
		f 4 -1745 1758 -1480 -1757
		mu 0 4 880 882 786 785
		f 4 -1747 1759 -1482 -1759
		mu 0 4 882 883 787 786
		f 4 -1749 1760 -1484 -1760
		mu 0 4 883 884 788 787
		f 4 -1751 1761 -1486 -1761
		mu 0 4 884 885 789 788
		f 4 -1753 1762 -1488 -1762
		mu 0 4 885 886 790 789
		f 4 -1755 1763 -1490 -1763
		mu 0 4 886 887 791 790
		f 4 -1756 -1758 -1492 -1764
		mu 0 4 887 881 784 791
		f 4 1764 1765 -1727 1766
		mu 0 4 888 889 872 873
		f 4 1767 1768 -1729 -1766
		mu 0 4 889 890 874 872
		f 4 1769 1770 -1731 -1769
		mu 0 4 890 891 875 874
		f 4 1771 1772 -1733 -1771
		mu 0 4 891 892 876 875
		f 4 1773 1774 -1735 -1773
		mu 0 4 892 893 877 876
		f 4 1775 1776 -1737 -1775
		mu 0 4 893 894 878 877
		f 4 1777 1778 -1739 -1777
		mu 0 4 894 895 879 878
		f 4 1779 -1767 -1740 -1779
		mu 0 4 895 888 873 879
		f 4 1780 1781 -1776 -1774
		mu 0 4 892 896 894 893
		f 4 1782 -1780 -1778 -1782
		mu 0 4 896 888 895 894
		f 4 1783 -1781 -1772 -1770
		mu 0 4 890 896 892 891
		f 4 -1765 -1783 -1784 -1768
		mu 0 4 889 888 896 890
		f 4 1784 -1371 -1373 1785
		mu 0 4 897 714 715 716
		f 4 1786 -1379 -1380 1787
		mu 0 4 897 718 719 713
		f 4 -1369 -1785 -1788 -1366
		mu 0 4 712 714 897 713
		f 4 -1377 -1787 -1786 -1375
		mu 0 4 717 718 897 716;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".db" yes;
	setAttr ".vs" 4;
	setAttr ".bw" 4;
	setAttr ".dr" 1;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode polySoftEdge -n "polySoftEdge86";
	rename -uid "F52DC7E2-44A2-CD23-1613-C1A61AF425AA";
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
connectAttr "polySoftEdge86.out" "Special_FShape.i";
connectAttr "polySurfaceShape64.o" "polySoftEdge86.ip";
connectAttr "Special_FShape.wm" "polySoftEdge86.mp";
connectAttr "Special_FShape.iog" ":initialShadingGroup.dsm" -na;
// End of Special_F.ma
