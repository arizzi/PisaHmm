from samples2017 import *
name="H"
background={
#"DY":["DY105_2017AMCPY", "DY105VBF_2017AMCPY"],
"DY":["DY105_2017AMCPY"],
"DYVBF":[ "DY105VBF_2017AMCPY"],
"EWKZ":["EWKZ_2017MGPY","EWKZint_2017MGPY"],  # --------------- EWKZ_2017MGPY -> HERWIG ----------------     
"Top":["STs_2017AMCPY","STwtbar_2017POWPY","STwt_2017POWPY","STtbar_2017POWPY","STt_2017POWPY","TTlep_2017POWPY","TTsemi_2017POWPY"],
"Other":["W2J_2017AMCPY","W0J_2017AMCPY",     # ,"W1J_2017AMCPY"   to be added when ready
         "WWdps_2017MGPY","WWJJlnln_2017MGPY","WLLJJln_2017MG_MADSPIN_PY",
         "WW2l2n_2017POWPY","WWlnqq_2017POWPY",
         "WZ1l1n2q_2017AMCPY","WZ1l3n_2017AMCPY","WZ2l2q_2017AMC_MADSPIN_PY","WZ3l1n_2017POWPY",
         "ZZ2l2q_2017POWPY","ZZ2l2n_2017POWPY","ZZ4l_2017POWPY"
],
}



#sorting
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2017POWPY"],
"gg H":["ggHmm_2017POWPY"],
"ZH":["zHmm_2017POWPY"],
"WH":["WplusHmm_2017POWPY","WminusHmm_2017POWPY"],
"ttH":["ttHmm_2017POWPY"]
}

data={
"2017":["data2017"]
}

import ROOT
fillcolor={
"DY": ROOT.kOrange,
"DYVBF": ROOT.kOrange-3,
"EWKZ": ROOT.kViolet,
"Top": ROOT.kGreen,
"Other" : ROOT.kGreen+1,
"VBF H":ROOT.kRed,
"gg H":ROOT.kRed+4,
"ZH":ROOT.kPink+4,
"WH":ROOT.kPink+9,
"ttH":ROOT.kRed-4,
}

#systematicsToPlot=["MuScaleUp"]
systematicsToPlot=["JERMix","JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]

linecolor=fillcolor
markercolor=fillcolor



rebin = {
    "BDTAtan" : [0 , 0.404 , 0.488 , 0.534 , 0.567333333333 , 0.595333333333 , 0.62 , 0.642 , 0.662 , 0.680666666667 , 0.698 , 0.714666666667 , 0.730666666667 , 0.746666666667 , 0.762666666667 , 0.778 , 0.793333333333 , 0.809333333333 , 0.825333333333 , 0.841333333333 , 0.858 , 0.875333333333 , 0.894 , 0.913333333333 , 0.934 , 0.956666666667 , 0.980666666667 , 1.00733333333 , 1.03733333333 , 1.072 , 1.11333333333 , 1.16666666667 , 1.238 , 1.35133333333 , 2.0 ]
}
