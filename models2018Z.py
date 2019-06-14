from samples2018 import *
name="Z"
background={
"DY0J":["DY0J_2018AMCPY"],
"DY1J":["DY1J_2018AMCPY"],
"DY2J":["DY2J_2018AMCPY"],
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
backgroundSorted=["Other","Top","DY0J","DY1J","DY2J","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2018POWPY"],
"gg H":["ggHmm_2018POWPY"],
}

data={
"2018":["data2018"]
}

import ROOT
fillcolor={
"DY0J": ROOT.kOrange+2,
"DY1J": ROOT.kOrange+1,
"DY2J": ROOT.kOrange,
"EWKZ": ROOT.kViolet,
"Top": ROOT.kGreen,
"Other" : ROOT.kGreen+1,
"VBF H":ROOT.kRed,
"gg H":ROOT.kRed+4,
}

systematicsToPlot=["JERMix","JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]

bdtbinning= [0 , 0.404 , 0.488 , 0.534 , 0.567333333333 , 0.595333333333 , 0.62 , 0.642 , 0.662 , 0.680666666667 , 0.698 , 0.714666666667 , 0.730666666667 , 0.746666666667 , 0.762666666667 , 0.778 , 0.793333333333 , 0.809333333333 , 0.825333333333 , 0.841333333333 , 0.858 , 0.875333333333 , 0.894 , 0.913333333333 , 0.934 , 0.956666666667 , 0.980666666667 , 1.00733333333 , 1.03733333333 , 1.072 , 1.11333333333 , 1.16666666667 , 1.238 , 1.35133333333 , 2.0 ]
rebin = {
    #"BDTAtan" : [0,0.005,0.01,0.015,0.02]    
    #"BDTAtan" : [0,0.05,0.1,0.15,0.2]    
    "BDTAtan" : bdtbinning,
    "BDTAtanNoMass" : bdtbinning,
}


linecolor=fillcolor
markercolor=fillcolor



rebin = {
    "BDTAtan" : [0 , 0.404 , 0.488 , 0.534 , 0.567333333333 , 0.595333333333 , 0.62 , 0.642 , 0.662 , 0.680666666667 , 0.698 , 0.714666666667 , 0.730666666667 , 0.746666666667 , 0.762666666667 , 0.778 , 0.793333333333 , 0.809333333333 , 0.825333333333 , 0.841333333333 , 0.858 , 0.875333333333 , 0.894 , 0.913333333333 , 0.934 , 0.956666666667 , 0.980666666667 , 1.00733333333 , 1.03733333333 , 1.072 , 1.11333333333 , 1.16666666667 , 1.238 , 1.35133333333 , 2.0 ]
}
