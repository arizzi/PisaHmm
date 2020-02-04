import models2017H
from samples2017 import *
name="Z"
background={
"DY0J":["DY0J_2017AMCPY"],
"DY1J":["DY1J_2017AMCPY"],
"DY2J":["DY2J_2017AMCPY"],
"EWKZ":[
   "EWKZ_2017MGHERWIG",  ## Alternative: "EWKZ_2017MGPY"
   "EWKZint_2017MGPY", # interference with DY
],
}

background["Top"]   = models2017H.background["Top"]
background["Other"] = models2017H.background["Other"]
signal = models2017H.signal
data = models2017H.data

#sorting
backgroundSorted=["Other","Top","DY0J","DY1J","DY2J","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]

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
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down"]

systematicsToPlot+=["JESUp","JESDown"]
from jesnames import jesnames2017
from jernames import jernames
jesList=jesnames2017
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames



linecolor=fillcolor
markercolor=fillcolor


from rebinning import *
from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList)

