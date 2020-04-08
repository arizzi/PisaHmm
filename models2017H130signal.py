from samples2017 import *
name="H"
background={
"DY":["DY105_2017AMCPY"], ## Alternative: "DY105_2017MGPY"
"DYVBF":[ "DY105VBF_2017AMCPY"], ## Alternative: "DY105VBF_2017MGPY"
"EWKZ":[
   "EWKZ105FIX2_2017MGHERWIG",
   # interference with DY
   "EWKZint_2017MGPY" 
],
"Top":[
   ### Single Top (s, t, tW channels) ###
   "STs_2017AMCPY",
### MISSING ### "STt_2017POW_MADSPIN_PY",
   "STwt_2017POWPY", 
   
   ### Single Anti-Top (s, t, tW channels) ###
### MISSING ### "STsbar_2017AMCPY",
### MISSING ### "STtbar_2017POW_MADSPIN_PY",
   "STwtbar_2017POWPY",
   
   ### TTbar (leptonic, semileptonic, hadronic)
   "TTlep_2017POWPY",   # 2 lept
   "TTsemi_2017POWPY",  # 1 lept
   #"TThad_2017POWPY",  # 0 lept
   ### TTbar alternatives (inclusive): "TT_2017POWPY", "TT_2017AMCPY",
],
"Other":[
         ### W+jets ###
         #--- inclusive ---
         "W2J_2017AMCPY",
### MISSING ### "W1J_2017AMCPY",
         "W0J_2017AMCPY", 
         
         ### WW ###
         #--- 2 lept ---
         "WW2l2n_2017POWPY",
         #--- 1 lept ---
### MISSING ### "WWlnqq_2017AMC_MADSPIN_PY", ## Alternative: "WWlnqq_2017POWPY",
         #--- incl ---
         
         ### WZ ###
         #--- 3 lept ---
         "WZ3l1n_2017AMCPY", ## Alternative #"WZ3l1n_2017POWPY"
         #--- 2 lept ---
         "WZ2l2q_2017AMC_MADSPIN_PY",
         #--- 1 lept ---
         "WZ1l1n2q_2017AMCPY",
         "WZ1l3n_2017AMCPY", 
         
         ### ZZ ###
         #--- 4 lept ---
         "ZZ4l_2017POWPY",
         #--- 2 lept ---
         "ZZ2l2q_2017POWPY",
         "ZZ2l2n_2017POWPY",
         #--- 0 lept ---
### MISSING ### "ZZ2q2n_2017POWPY",

         ### Vector boson scattering ###
### MISSING ### "WWJJlnln_2017MGPY",          ## VBS W(lv)W(ln) + 2jets 
         "WLLJJln_2017MG_MADSPIN_PY",  ## VBS W(lv)Z(ll) + 2jets 

         ### Double scattering ###
### MISSING ### "WWdps_2017MGPY",             ## WW double scattering
],
}


#sorting
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfH130mm_2017AMCPY"], ## Alternative: "vbfHmm_2017POWPY"
"gg H":["ggH130mm_2017AMCPY"],   ## Alternative: "ggHmm_2017POWPY"
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
#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]
#ystematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
#systematicsToPlot=["PSWeightISRUp","PSWeightISRDown","PSWeightFSRUp","PSWeightFSRDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down","PDFX2Up","PDFX2Down"]


systematicsToPlot+=["JESUp","JESDown"]
from btagvariations import btagsys
systematicsToPlot+=btagsys

sthsNames=["Yield","PTH200","Mjj60","Mjj120","Mjj350","Mjj700","Mjj1000","Mjj1500","PTH25","JET01"]
THUs=["THU_VBF_"+x+"Up" for x in sthsNames]
THUs+=["THU_VBF_"+x+"Down" for x in sthsNames]
systematicsToPlot+=THUs


from jesnames import jesnames2017
from jernames import jernames
jesList=jesnames2017
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames

linecolor=fillcolor
markercolor=fillcolor

from rebinning import *
#rebin["DNN18Atan"]=dnn032018
from histograms import signalHistosMassScan
for i in  signalHistosMassScan :
 rebin[i]=rebin["DNN18Atan"]

from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList)


