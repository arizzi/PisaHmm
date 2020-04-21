import models2016H
from samples2016 import *
name="Z"
background={
#"DY0J":["DY0J_2016AMCPY"],
#"DY1J":["DY1J_2016AMCPY"],
#"DY2J":["DY2J_2016AMCPY"],
"DY":["DY0J_2016AMCPY", "DY1J_2016AMCPY", "DY2J_2016AMCPY"],
"VBF Z":[
   "EWKZ_2016MGHERWIG",  ## Alternative: "EWKZ_2016MGPY"
   "EWKZint_2016MGPY", # interference with DY
],
}

background["Top"]   = models2016H.background["Top"]
background["Other"] = models2016H.background["Other"]
signal = models2016H.signal
data = models2016H.data

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
fillcolor.update(models2016H.fillcolor)

#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","puWeightUp","puWeightDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down"]

systematicsToPlot+=["JESUp","JESDown"]
from btagvariations import btagsys
systematicsToPlot+=btagsys


from jesnames import jesnames2016
from jernames import jernames
jesList=jesnames2016
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames



linecolor=fillcolor
markercolor=fillcolor


from rebinning import *
from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList,"2016")

