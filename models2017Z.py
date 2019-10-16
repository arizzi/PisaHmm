from samples2017 import *
name="Z"
background={
"DY0J":["DY0J_2017AMCPY"],
"DY1J":["DY1J_2017AMCPY"],
"DY2J":["DY2J_2017AMCPY"],
#"EWKZ":["EWKZ_2017MGPY","EWKZint_2017MGPY"],  # --------------- EWKZ_2017MGPY -> HERWIG ----------------     
"EWKZ":["EWKZ_2017MGHERWIG","EWKZint_2017MGPY"],  # --------------- EWKZ_2017MGPY -> HERWIG ----------------     
"Top":["STs_2017AMCPY","STwtbar_2017POWPY","STwt_2017POWPY","STtbar_2017POWPY","STt_2017POWPY","TTlep_2017POWPY","TTsemi_2017POWPY"],
"Other":["W2J_2017AMCPY",#"W0J_2017AMCPY",     # ,"W1J_2017AMCPY"   to be added when ready
#         "WWdps_2017MGPY",
"WWJJlnln_2017MGPY","WLLJJln_2017MG_MADSPIN_PY",
         "WW2l2n_2017POWPY","WWlnqq_2017POWPY",
         "WZ1l1n2q_2017AMCPY","WZ1l3n_2017AMCPY","WZ2l2q_2017AMC_MADSPIN_PY","WZ3l1n_2017POWPY",
         "ZZ2l2q_2017POWPY","ZZ2l2n_2017POWPY","ZZ4l_2017POWPY"
],
}





#sorting
backgroundSorted=["Other","Top","DY0J","DY1J","DY2J","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2017POWPY"],
"gg H":["ggHmm_2017POWPY"],
}

data={
"2017":["data2017"]
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

#systematicsToPlot=["PSWeightISRUp","PSWeightISRDown","PSWeightFSRUp","PSWeightFSRDown","JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
#systematicsToPlot=["LHEPdfUp","LHEPdfDown","NoPrefiringWeight","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
#systematicsToPlot=["PrefiringWeight","JERUp","JERDown"]
#systematicsToPlot=["JERUp","JERDown"]
#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","puWeightUp","puWeightDown"]#,"LHERenUp","LHERenDown","LHEFacUp","LHEFacDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown"]

from jesnames import jes2016
from jernames import jernames
systematicsForDC=systematicsToPlot+[x[10:] for x in jes2016 ]+jernames
systematicsToPlot+=["JESUp","JESDown"]


linecolor=fillcolor
markercolor=fillcolor



from rebinning import *


from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)

