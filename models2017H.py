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
backgroundSorted=["Other","Top","DY","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2017POWPY"],
"gg H":["ggHmm_2017POWPY"],
"ZH":["zHmm_2017POWPY"],
"WH":["WplusHmm_2017POWPY","WminusHmm_2017POWPY"],
"ttH":["ttHmm_2017POWPY"]
}

data={
"2017":["data"]
}

import ROOT
fillcolor={
"DY": ROOT.kOrange,
"DYVBF": ROOT.kOrange-3,
"EWKZ": ROOT.kViolet,
"Top": ROOT.kGreen,
"Other" : ROOT.kTeal,
"VBF H":ROOT.kRed,
"gg H":ROOT.kRed+4,
"ZH":ROOT.kPink+4,
"WH":ROOT.kPink+9,
"ttH":ROOT.kRed-4,
}

#systematicsToPlot=["MuScaleUp"]
systematicsToPlot=["JERUp","JERDown","JESUp","JESDown"]

linecolor=fillcolor
markercolor=fillcolor
