from samples2018 import *
from rebinning import *
name="H"
background={
"DY":["DY105_2018AMCPY"],
"DYVBF":[ "DY105VBF_2018MGPY"], #DY105VBF_2018AMCPY"],
#"DY":["DY105_2018AMCPY", "DY105VBF_2018AMCPY"],
"EWKZ":["EWKZ105_2018MGHERWIG","EWKZint_2018MGPY"],  # --------------- EWKZ_2018MGPY -> HERWIG ----------------     
#"EWKZ":["EWKZint_2018MGPY","EWKZ105_2016MGHERWIG"],  # --------------- EWKZ_2018MGPY -> HERWIG ----------------     
"Top":["STs_2018AMCPY","STwtbar_2018POWPY","STwt_2018POWPY","STtbar_2018POWPY","STt_2018POWPY","TTlep_2018POWPY","TTsemi_2018POWPY","TThad_2018POWPY"],

#"WJ":["W2J_2018AMCPY","W0J_2018AMCPY"],     # ,"W1J_2018AMCPY"   to be added when ready
#"WW" :[ "WWdps_2018MGPY","WWJJlnln_2018MGPY","WLLJJln_2018MG_MADSPIN_PY",
#         "WW2l2n_2018POWPY","WWlnqq_2018POWPY"],
#"WZ":[    "WZ1l3n_2018AMCPY","WZ2l2q_2018AMC_MADSPIN_PY","WZ3l1n_2018POWPY"],
#"ZZ":[     "ZZ2l2q_2018POWPY","ZZ2l2n_2018POWPY","ZZ4l_2018POWPY"]


#"WWdps":["WWdps_2018MGPY"],
#"WWJJnn":["WWJJlnln_2018MGPY"],
#"WWLLJJln":["WLLJJln_2018MG_MADSPIN_PY"],
#"WW2L2n":["WW2l2n_2018POWPY"],
#"WWlnqq":["WWlnqq_2018POWPY"],


"Other":[#W2J_2018AMCPY","W0J_2018AMCPY",     # ,"W1J_2018AMCPY"   to be added when ready
 #       "WWdps_2018MGPY",
"WWJJlnln_2018MGPY","WLLJJln_2018MG_MADSPIN_PY",
#        "WW2l2n_2018POWPY","WWlnqq_2018POWPY",
#"Other":[ 
"WZ1l3n_2018AMCPY",
"WZ2l2q_2018AMC_MADSPIN_PY","WZ3l1n_2018POWPY",
         "ZZ2l2q_2018POWPY",#"ZZ2l2n_2018POWPY",
"ZZ4l_2018POWPY"
],
}



#sorting
#backgroundSorted=["Top","DY","DYVBF","EWKZ"]
#backgroundSorted=["WW","WZ","ZZ","Top","DY","DYVBF","EWKZ"]

#backgroundSorted=["WWdps","WWJJnn","WWLLJJln","WW2L2n","WWlnqq","Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2018POWPY"],
#"gg H":["ggHmm_2018POWPY"],
"gg H":["ggHmm_2018AMCPY"],
#"ZH":["zHmm_2018POWPY"],
#"WH":["WplusHmm_2018POWPY","WminusHmm_2018POWPY"],
#"ttH":["ttHmm_2018POWPY"]
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
"WWdps":ROOT.kBlue,
"WWJJnn":ROOT.kCyan,
"WWLLJJln": ROOT.kCyan+4,
"WW2L2n": ROOT.kViolet,
"WWlnqq":ROOT.kMagenta,
"WJ" : ROOT.kBlue,
"WZ" : ROOT.kBlue+1,
"ZZ" : ROOT.kBlue+2,
"WW" : ROOT.kBlue+3,
"VBF H":ROOT.kRed,
"gg H":ROOT.kRed+4,
"ZH":ROOT.kPink+4,
"WH":ROOT.kPink+9,
"ttH":ROOT.kRed-4,
}

#systematicsToPlot=["MuScaleUp"]
#systematicsToPlot=["LHEScaleWeightSafe0","LHEScaleWeightSafe1","LHEScaleWeightSafe3","JERUp","JERDown","JESUp","JESDown"]+["MuScaleUp","MuScaleDown"]
#ystematicsToPlot=["JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]
#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]

systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown"]

#jesnames=[ "JESPt0To30Eta0To2","JESPt30To50Eta0To2","JESPt50To100Eta0To2","JESPt100To2000Eta0To2","JESPt0To30Eta2To2p5","JESPt30To50Eta2To2p5","JESPt50To100Eta2To2p5","JESPt100To2000Eta2To2p5","JESPt0To30Eta2p5To3p1","JESPt30To50Eta2p5To3p1","JESPt50To100Eta2p5To3p1","JESPt100To2000Eta2p5To3p1","JESPt0To30Eta3p1To5","JESPt30To50Eta3p1To5","JESPt50To100Eta3p1To5","JESPt100To2000Eta3p1To5" ]

#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown"]+[x+"Down" for x in jesnames]+[x+"Up" for x in jesnames]
systematicsToPlot=["LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]

if True  :  #use full JES?
  from jesnames import jes2016
  systematicsToPlot+=[x[10:] for x in jes2016 ]
else :
  systematicsToPlot+=["JESUp","JESDown"]






from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)







linecolor=fillcolor
markercolor=fillcolor

