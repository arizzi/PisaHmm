from samples2016 import *
name="H"
background={
"DY":["DY105_2016AMCPY"], ## Alternative: "DY105_2016MGPY"
"DYVBF":["DY105VBF_2016AMCPY"], ## Alternative: "DY105VBF_2016MGPY"
"EWKZ":[
   "EWKZ105_2016MGHERWIG",
   # interference with DY
   "EWKZint_2016MGPY"
],
"Top":[
   ### Single Top (s, t, tW channels) ###
   "STs_2016AMCPY",
   "STt_2016POW_MADSPIN_PY",
   "STwt_2016POWPY", 
   
   ### Single Anti-Top (s, t, tW channels) ###
   #"STsbar_2016AMCPY",
   "STtbar_2016POW_MADSPIN_PY",
   "STwtbar_2016POWPY",
   
   ### TTbar (leptonic, semileptonic, hadronic)
   "TTlep_2016POWPY",   # 2 lept
### MISSING ### "TTsemi_2016POWPY", # 1 lept
### MISSING ### "TThad_2016POWPY",  # 0 lept
   ### TTbar alternatives (inclusive): "TT_2016POWPY", "TT_2016AMCPY",
],
"Other":[
         ### W+jets ###
         #--- inclusive ---
         "W2J_2016AMCPY",
         "W1J_2016AMCPY",
         "W0J_2016AMCPY", 
         
         ### WW ###
         #--- 2 lept ---
         "WW2l2n_2016POWPY",
         #--- 1 lept ---
### MISSING ### "WWlnqq_2016AMC_MADSPIN_PY", #Alternative: "WWlnqq_2016POWPY",
         #--- incl ---
         
         ### WZ ###
         #--- 3 lept ---
         "WZ3l1n_2016AMCPY", ## Alternative: #"WZ3l1n_2016POWPY"
         #--- 2 lept ---
         "WZ2l2q_2016AMC_MADSPIN_PY",
         #--- 1 lept ---
### MISSING ### "WZ1l1n2q_2016AMCPY",
         "WZ1l3n_2016AMCPY", 
         
         ### ZZ ###
         #--- 4 lept ---
### MISSING ### "ZZ4l_2016POWPY",
         #--- 2 lept ---
         "ZZ2l2q_2016POWPY",
### MISSING ### "ZZ2l2n_2016POWPY",
         #--- 0 lept ---
### MISSING ### "ZZ2q2n_2016POWPY",

         ### Vector boson scattering ###
### LHE Weights broken "WWJJlnln_2016MGPY",          ## VBS W(lv)W(ln) + 2jets 
         "WLLJJln_2016MG_MADSPIN_PY",  ## VBS W(lv)Z(ll) + 2jets 

         ### Double scattering ###
### MISSING ### "WWdps_2016MGPY",            ## WW double scattering
],
}


#sorting
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2016AMCPY"], ## Alternative: "vbfHmm_2016POWPY"
"gg H":["ggHmm_2016AMCPY"],   ## Alternative: "ggHmm_2016POWPY"
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

#systematicsToPlot=["MuScaleUp"]
#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]
#ystematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
#systematicsToPlot=["PSWeightISRUp","PSWeightISRDown","PSWeightFSRUp","PSWeightFSRDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down"]
from jesnames import jes2016
from jernames import jernames
systematicsForDC=systematicsToPlot+[x[10:] for x in jes2016 ]+jernames
systematicsToPlot+=["JESUp","JESDown"]


linecolor=fillcolor
markercolor=fillcolor

from rebinning import *


from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)


