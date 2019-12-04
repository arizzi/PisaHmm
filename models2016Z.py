import models2016H
from samples2016 import *
name="Z"
background={
"DY0J":["DY0J_2016AMCPY"],
"DY1J":["DY1J_2016AMCPY"],
"DY2J":["DY2J_2016AMCPY"],
"EWKZ":[
   "EWKZ_2016MGHERWIG",  ## Alternative: "EWKZ_2016MGPY"
   "EWKZint_2016MGPY", # interference with DY
],
}

background["Top"]   = models2016H.background["Top"]
background["Other"] = models2016H.background["Other"]
signal = models2016H.signal
data = models2016H.data

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
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown"]

systematicsToPlot+=["JESUp","JESDown"]
from jesnames import jes2016
from jernames import jernames
systematicsForDC=systematicsToPlot+[x[10:] for x in jes2016 ]+jernames



linecolor=fillcolor
markercolor=fillcolor


from rebinning import *
from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)

