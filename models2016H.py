from samples2016 import *
name="H"
background={
"DY":["DY105_2016AMCPY"],#["DY105_2016AMCPY"]
"DYVBF":["DY105VBF_2016AMCPY"],
"EWKZ":["EWKZ_2016MGHERWIG","EWKZint_2016MGPY"],
"Top":["STs_2016AMCPY","STwtbar_2016POWPY","STwt_2016POWPY","STtbar_2016POW_MADSPIN_PY","STt_2016POW_MADSPIN_PY","TTlep_2016POWPY","TTsemi_2016POWPY"],
"Other":["W2J_2016AMCPY","W1J_2016AMCPY","W0J_2016AMCPY", 
         #"WWdps_2016MGPY","WWJJlnln_2016MGPY","WLLJJln_2016MG_MADSPIN_PY",
         "WW2l2n_2016POWPY",#"WWlnqq_2016AMC_MADSPIN_PY",
         "WZ1l1n2q_2016AMCPY","WZ1l3n_2016AMCPY","WZ2l2q_2016AMC_MADSPIN_PY","WZ3l1n_2016POWPY",
         "ZZ2l2q_2016POWPY"#,"ZZ2q2n_2016POWPY","ZZ4l_2016POWPY"
],
}




#sorting
#backgroundSorted=["Other","DY","DYVBF","EWKZ"]
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2016POWPY"],
"gg H":["ggHmm_2016AMCPY"],
#"ZH":["zHmm_2016POWPY"],
#"WH":["WplusHmm_2016POWPY","WminusHmm_2016POWPY"],
#"ttH":["ttHmm_2016POWPY"]
}

data={
"2016":["data2016"]
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

systematicsToPlot=["JERMix","JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]

linecolor=fillcolor
markercolor=fillcolor

from rebinning import *


from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)


