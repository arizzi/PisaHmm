from samples2018 import *
from rebinning import *
name="H"
background={
"DY":["DY105_2018AMCPY"],
"DYVBF":[ "DY105VBF_2018AMCPY"],
#"DY":["DY105_2018AMCPY", "DY105VBF_2018AMCPY"],
"EWKZ":["EWKZ_2018MGPY","EWKZint_2018MGPY"],  # --------------- EWKZ_2018MGPY -> HERWIG ----------------     
"Top":["STs_2018AMCPY","STwtbar_2018POWPY","STwt_2018POWPY","STtbar_2018POWPY","STt_2018POWPY","TTlep_2018POWPY","TTsemi_2018POWPY","TThad_2018POWPY"],
"Other":["W2J_2018AMCPY","W0J_2018AMCPY",     # ,"W1J_2018AMCPY"   to be added when ready
         "WWdps_2018MGPY","WWJJlnln_2018MGPY","WLLJJln_2018MG_MADSPIN_PY",
         "WW2l2n_2018POWPY","WWlnqq_2018POWPY",
         "WZ1l3n_2018AMCPY","WZ2l2q_2018AMC_MADSPIN_PY","WZ3l1n_2018POWPY",
         "ZZ2l2q_2018POWPY","ZZ2l2n_2018POWPY","ZZ4l_2018POWPY"
],
}



#sorting
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2018POWPY"],
"gg H":["ggHmm_2018POWPY"],
"ZH":["zHmm_2018POWPY"],
"WH":["WplusHmm_2018POWPY","WminusHmm_2018POWPY"],
"ttH":["ttHmm_2018POWPY"]
}

data={
"2018":["data2018"]
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
#systematicsToPlot=["LHEScaleWeightSafe0","LHEScaleWeightSafe1","LHEScaleWeightSafe3","JERUp","JERDown","JESUp","JESDown"]+["MuScaleUp","MuScaleDown"]
#ystematicsToPlot=["JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]
systematicsToPlot=["JERMix","JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]




from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)







linecolor=fillcolor
markercolor=fillcolor

