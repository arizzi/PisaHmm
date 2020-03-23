import models2017H
from samples2017 import *
name="Z"
background={
#"DY0J":["DY0J_2017AMCPY"],
#"DY1J":["DY1J_2017AMCPY"],
#"DY2J":["DY2J_2017AMCPY"],
"DY":["DY0J_2017AMCPY", "DY1J_2017AMCPY", "DY2J_2017AMCPY"],
"VBF Z":[
   "EWKZ_2017MGHERWIG",  ## Alternative: "EWKZ_2017MGPY"
   "EWKZint_2017MGPY", # interference with DY
],
}

background["Top"]   = models2017H.background["Top"]
background["Other"] = models2017H.background["Other"]
signal = models2017H.signal
data = models2017H.data

#sorting
backgroundSorted=["Other","Top","DY","VBF Z"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]

#legend sorting
backgroundSortedForLegend=["DY","VBF Z","Top", "Other"]
backgroundSortedForLegend+=[x for x in background if x not in backgroundSortedForLegend]
signalSortedForLegend=["VBF H","gg H"]
signalSortedForLegend+=[x for x in signal if x not in signalSortedForLegend]


import ROOT
fillcolor={
"DY0J": ROOT.kOrange+2,
"DY1J": ROOT.kOrange+1,
"DY2J": ROOT.kOrange,
}
fillcolor.update(models2017H.fillcolor)

#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","puWeightUp","puWeightDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down"]

systematicsToPlot+=["JESUp","JESDown"]
from btagvariations import btagsys
systematicsToPlot+=btagsys


from jesnames import jesnames2017
from jernames import jernames
jesList=jesnames2017
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames



linecolor=fillcolor
markercolor=fillcolor


from rebinning import *
from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList,"2017")

