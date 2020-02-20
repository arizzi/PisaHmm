from samples2018 import *
name="H"
background={
"DY":["DY105_2018AMCPY"], ## Alternative: "DY105_2018MGPY"
"DYVBF":[ "DY105VBF_2018AMCPY"], ## Alternative: "DY105VBF_2018MGPY"
"EWKZ":[
   "EWKZ105FIX2_2018MGHERWIG", ## Alternative "EWKZ_2018MGPY"
   # interference with DY
 "EWKZint_2018MGPY" 
],
"Top":[
   ### Single Top (s, t, tW channels) ###
   "STs_2018AMCPY",
### MISSING ### "STt_2018POW_MADSPIN_PY",
   "STwt_2018POWPY", 
   
   ### Single Anti-Top (s, t, tW channels) ###
### MISSING ### "STsbar_2018AMCPY",
### MISSING ### "STtbar_2018POW_MADSPIN_PY",
   "STwtbar_2018POWPY",
   
   ### TTbar (leptonic, semileptonic, hadronic)
   "TTlep_2018POWPY",   # 2 lept
   "TTsemi_2018POWPY",  # 1 lept
### MISSING ### "TThad_2018POWPY",  # 0 lept
   ### TTbar alternatives (inclusive): "TT_2018POWPY", "TT_2018AMCPY",
],
"Other":[
         ### W+jets ###
         #--- inclusive ---
### MISSING ### "W2J_2018AMCPY",
### MISSING ### "W1J_2018AMCPY",
### MISSING ### "W0J_2018AMCPY", 
         
         ### WW ###
         #--- 2 lept ---
         "WW2l2n_2018POWPY",
         #--- 1 lept ---
### MISSING ### "WWlnqq_2018AMC_MADSPIN_PY", ## Alternative: "WWlnqq_2018POWPY",
         "WWlnqq_2018POWPY", ## as alternative
         #--- incl ---
         
         ### WZ ###
         #--- 3 lept ---
### MISSING ### "WZ3l1n_2018AMCPY", ## Alternative: #"WZ3l1n_2018POWPY"
         "WZ3l1n_2018POWPY", ## as alternative
         #--- 2 lept ---
         "WZ2l2q_2018AMC_MADSPIN_PY",
         #--- 1 lept ---
### MISSING ### "WZ1l1n2q_2018AMCPY",
         "WZ1l3n_2018AMCPY", 
         
         ### ZZ ###
         #--- 4 lept ---
### MISSING ### "ZZ4l_2018POWPY",
         #--- 2 lept ---
         "ZZ2l2q_2018POWPY",
### MISSING ### "ZZ2l2n_2018POWPY",
         #--- 0 lept ---
### MISSING ### "ZZ2q2n_2018POWPY",

         ### Vector boson scattering ###
### MISSING ### "WWJJlnln_2018MGPY",           ## VBS W(lv)W(ln) + 2jets 
### MISSING ### "WLLJJln_2018MG_MADSPIN_PY",   ## VBS W(lv)Z(ll) + 2jets 

         ### Double scattering ###
### MISSING ### "WWdps_2018MGPY",              ## WW double scattering
],
}


#sorting
backgroundSorted=["Other","Top","DY","DYVBF","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
### MISSING ### "VBF H":["vbfHmm_2018AMCPY"], ## Alternative: "vbfHmm_2018POWPY"
"VBF H":["vbfHmm_2018AMCPY"],
### MISSING ### "gg H":["ggHmm_2018AMCPY"],   ## Alternative: "ggHmm_2018POWPY"
"gg H":["ggHmm_2018POWPY"],
"ZH":["zHmm_2018POWPY"],
"WH":[
"WminusHmm_2018POWPY", 
### MISSING ### "WplusHmm_2018POWPY"
],
### MISSING ### "ttH":["ttHmm_2018POWPY"]
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


from jesnames import jesnames2018
from jernames import jernames
jesList=jesnames2018
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames


linecolor=fillcolor
markercolor=fillcolor

from rebinning import *
rebin["DNN18Atan"]=dnnnewfew18
rebin["DNN18AtanNoMass"]=dnnnewfew18

rebin["DNN18Atan2"]= [0 , 0.311666666667 , 0.635 , 0.845 , 1.04166666667 , 1.185 , 1.31666666667 , 1.42666666667 , 1.53166666667 , 1.645 , 1.76166666667 , 1.87 , 1.97666666667 , 2.07833333333 , 2.17666666667 , 2.27666666667 , 2.37666666667 , 2.485 , 2.61333333333 , 2.76333333333 , 2.96833333333 , 5.0 ]
#rebin["DNN18Atan2"]=  [0 , 0.49 , 0.768333333333 , 0.993333333333 , 1.15333333333 , 1.295 , 1.41 , 1.515 , 1.61833333333 , 1.73 , 1.83166666667 , 1.925 , 2.01166666667 , 2.09666666667 , 2.175 , 2.255 , 2.32666666667 , 2.40166666667 , 2.475 , 2.55666666667 , 2.645 , 2.73666666667 , 2.83833333333 , 2.96 , 3.13166666667 , 5.0 ]

#ebin["DNN18Atan"]=dnn032018
from histograms import signalHistosMassScan

for i in  signalHistosMassScan :
 rebin[i]=rebin["DNN18Atan"]

from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList)


