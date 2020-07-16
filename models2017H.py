from samples2017 import *

import samples2016,samples2018
samples.update(samples2016.samples)
samples.update(samples2018.samples)

name="H"
background={
#"DY":["DY105_2017AMCPY"], ## Alternative: "DY105_2017MGPY"
#"DYVBF":[ "DY105VBF_2017AMCPY"], ## Alternative: "DY105VBF_2017MGPY"
#"DY":["DY105_2017AMCPY", "DY105VBF_2017AMCPY"], ## Alternative: "DY105VBF_2017MGPY"
"DY01J":["DY105J01_2017AMCPY", "DY105VBFJ01_2017AMCPY"],
"DY2J":["DY105J2_2017AMCPY", "DY105VBFJ2_2017AMCPY"],

"VBF Z":[
   "EWKZ105CORR_2017MGHERWIG",
   # interference with DY
  #"EWKZint_2017MGPY" 
],
"Top":[
   ### Single Top (s, t, tW channels) ###
#   "STs_2017AMCPY",
 #  "STt_2017POWPY",
   "STwt_2017POWPY", 
   
   ### Single Anti-Top (s, t, tW channels) ###
### MISSING ### "STsbar_2017AMCPY",
   #"STtbar_2017POW_MADSPIN_PY",
   "STwtbar_2017POWPY",
   
   ### TTbar (leptonic, semileptonic, hadronic)
   "TTlep_2017POWPY",   # 2 lept
#  "TTsemi_2017POWPY",  # 1 lept
   #"TThad_2017POWPY",  # 0 lept
   ### TTbar alternatives (inclusive): "TT_2017POWPY", "TT_2017AMCPY",
],
"Other":[
         ### W+jets ###
         #--- inclusive ---
    #    "W2J_2017AMCPY",
       ##"W1J_2017AMCPY",
#        "W0J_2017AMCPY", 
         
         ### WW ###
         #--- 2 lept ---
         "WW2l2n_2017POWPY",
   #      "WWlnqq_2017POWPY",
         #--- 1 lept ---
### MISSING ### "WWlnqq_2017AMC_MADSPIN_PY", ## Alternative: "WWlnqq_2017POWPY",
         #--- incl ---
         
         ### WZ ###
         #--- 3 lept ---
 #       "WZ3l1n_2017AMCPY", ## Alternative #"WZ3l1n_2017POWPY"
         #--- 2 lept ---
         ### MISSING ###"WZ2l2q_2017AMC_MADSPIN_PY",
         #--- 1 lept ---
  #      "WZ1l1n2q_2017AMCPY",
#        "WZ1l3n_2017AMCPY", 
         
         ### ZZ ###
         #--- 4 lept ---
       ##  "ZZ4l_2017POWPY",
         #--- 2 lept ---
#        "ZZ2l2q_2017POWPY",
         ### MISSING ###"ZZ2l2n_2017POWPY",
         #--- 0 lept ---
### MISSING ### "ZZ2q2n_2017POWPY",

         ### Vector boson scattering ###
### MISSING ### "WWJJlnln_2017MGPY",          ## VBS W(lv)W(ln) + 2jets 
         #"WLLJJln_2017MG_MADSPIN_PY",  ## VBS W(lv)Z(ll) + 2jets 

         ### Double scattering ###
### MISSING ### "WWdps_2017MGPY",             ## WW double scattering
],
}


#sorting
backgroundSorted=["Other","Top","DY2J","DY01J","VBF Z"]
#backgroundSorted=["Other","Top","DY","VBF Z"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]


signal={
"VBF H":["vbfHmm_2017POWPYDIPOLE"], ## Alternative: "vbfHmm_2017POWPY"
"gg H":["ggHmm_2017AMCPY"],   ## Alternative: "ggHmm_2017POWPY"
#"VH":["WplusHmm_2017POWPY","WminusHmm_2017POWPY", "zHmm_2017POWPY"],
#"ttH":["ttHmm_2017POWPY"]
}

#legend sorting
backgroundSortedForLegend=["DY2J","DY01J","VBF Z","Top", "Other"]
#backgroundSortedForLegend=["DY","VBF Z","Top", "Other"]
backgroundSortedForLegend+=[x for x in background if x not in backgroundSortedForLegend]
signalSortedForLegend=["VBF H","gg H"]
signalSortedForLegend+=[x for x in signal if x not in signalSortedForLegend]


data={
"2017":["data2017"]
}

import ROOT
fillcolor={
"DY": ROOT.kOrange,
"DY01J": ROOT.kOrange-1,
"DY2J": ROOT.kOrange-2,
"DYVBF": ROOT.kOrange-3,
"VBF Z": ROOT.kMagenta+2,
"Top": ROOT.kGreen+1,
"Other" : ROOT.kGreen+3,
"VBF H":ROOT.kRed,
"gg H":ROOT.kRed+4,
"ZH":ROOT.kPink+4,
"WH":ROOT.kPink+9,
"VH":ROOT.kPink+5,
"ttH":ROOT.kRed-4,
}

#systematicsToPlot=["MuScaleUp"]
#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","WithJER","puWeightUp","puWeightDown"]
#ystematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
#systematicsToPlot=["PSWeightISRUp","PSWeightISRDown","PSWeightFSRUp","PSWeightFSRDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down","PDFX2Up","PDFX2Down","EWKZjjPartonShowerUp","EWKZjjPartonShowerDown","SignalPartonShowerUp","SignalPartonShowerDown","DYModelUp","DYModelDown"]


systematicsToPlot+=["JESUp","JESDown"]
from btagvariations import btagsys



from jesnames import jesnames2017
from jernames import jernames
jesList=jesnames2017
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames
sthsNames=["Yield","PTH200","Mjj60","Mjj120","Mjj350","Mjj700","Mjj1000","Mjj1500","PTH25","JET01"]
THUs=["THU_VBF_"+x+"Up" for x in sthsNames]
THUs+=["THU_VBF_"+x+"Down" for x in sthsNames]
systematicsForDC+=THUs
systematicsForDC+=btagsys

systematicsToPlot=jernames+["JERUp","JERDown"]

linecolor=fillcolor
markercolor=fillcolor

from rebinning import *
#rebin["DNN18Atan"]=dnn032018
from histograms import signalHistosMassScanAll
for i in  signalHistosMassScanAll :
 rebin[i]=rebin["DNN18Atan"]

from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList,"2017")


