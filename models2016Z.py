from samples2016 import *
name="Z"
background={
"DY":["DY105_2016AMCPY"],#["DY105_2016AMCPY"]
"DYVBF":["DY105VBF_2016AMCPY"],
"EWKZ":["EWKZ_2016MGHERWIG","EWKZint_2016MGPY"],
"Top":["STs_2016AMCPY","STwtbar_2016POWPY","STwt_2016POWPY","STtbar_2016POW_MADSPIN_PY","STt_2016POW_MADSPIN_PY","TTlep_2016POWPY","TTsemi_2016POWPY"],
"Other":["W2J_2016AMCPY","W1J_2016AMCPY","W0J_2016AMCPY", 
         "WWdps_2016MGPY","WWJJlnln_2016MGPY","WLLJJln_2016MG_MADSPIN_PY",
         "WW2l2n_2016POWPY",#"WWlnqq_2016AMC_MADSPIN_PY",
         "WZ1l1n2q_2016AMCPY","WZ1l3n_2016AMCPY","WZ2l2q_2016AMC_MADSPIN_PY","WZ3l1n_2016POWPY",
         "ZZ2l2q_2016POWPY"#,"ZZ2q2n_2016POWPY","ZZ4l_2016POWPY"
],
}




#sorting
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2016POWPY"],
"gg H":["ggHmm_2016AMCPY"],
"ZH":["zHmm_2016POWPY"],
"WH":["WplusHmm_2016POWPY","WminusHmm_2016POWPY"],
"ttH":["ttHmm_2016POWPY"]
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



rebin = {
    "BDTAtan" : [0 , 0.404 , 0.488 , 0.534 , 0.567333333333 , 0.595333333333 , 0.62 , 0.642 , 0.662 , 0.680666666667 , 0.698 , 0.714666666667 , 0.730666666667 , 0.746666666667 , 0.762666666667 , 0.778 , 0.793333333333 , 0.809333333333 , 0.825333333333 , 0.841333333333 , 0.858 , 0.875333333333 , 0.894 , 0.913333333333 , 0.934 , 0.956666666667 , 0.980666666667 , 1.00733333333 , 1.03733333333 , 1.072 , 1.11333333333 , 1.16666666667 , 1.238 , 1.35133333333 , 2.0 ]
}
