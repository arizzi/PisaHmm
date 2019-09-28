from samples2016 import *
name="Z"
background={
"DY0J":["DY0J_2016AMCPY"],
"DY1J":["DY1J_2016AMCPY"],
"DY2J":["DY2J_2016AMCPY"],
"EWKZ":["EWKZ_2016MGHERWIG","EWKZint_2016MGPY"],
"Top":["STs_2016AMCPY","STwtbar_2016POWPY","STwt_2016POWPY","STtbar_2016POW_MADSPIN_PY","STt_2016POW_MADSPIN_PY","TTlep_2016POWPY","TTsemi_2016POWPY"],
"Other":["W2J_2016AMCPY","W1J_2016AMCPY",#"W0J_2016AMCPY", 
#         "WWdps_2016MGPY",
#"WWJJlnln_2016MGPY",
"WLLJJln_2016MG_MADSPIN_PY",
         "WW2l2n_2016POWPY",#"WWlnqq_2016AMC_MADSPIN_PY",
 #        "WZ1l1n2q_2016AMCPY",
"WZ1l3n_2016AMCPY","WZ2l2q_2016AMC_MADSPIN_PY",#WZ3l1n_2016POWPY",
         "ZZ2l2q_2016POWPY"#,"ZZ2q2n_2016POWPY","ZZ4l_2016POWPY"
],
}




#sorting
backgroundSorted=["Other","Top","DY0J","DY1J","DY2J","EWKZ"]
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
"DY0J": ROOT.kOrange+2,
"DY1J": ROOT.kOrange+1,
"DY2J": ROOT.kOrange,
"EWKZ": ROOT.kViolet,
"Top": ROOT.kGreen,
"Other" : ROOT.kGreen+1,
"VBF H":ROOT.kRed,
"gg H":ROOT.kRed+4,
"ZH":ROOT.kPink+4,
"WH":ROOT.kPink+9,
"ttH":ROOT.kRed-4,
}

#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","puWeightUp","puWeightDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]

from jesnames import jes2016
from jernames import jernames
systematicsForDC=systematicsToPlot+[x[10:] for x in jes2016 ]+jernames
systematicsToPlot+=["JESUp","JESDown"]



linecolor=fillcolor
markercolor=fillcolor


from rebinning import *
from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)

