import models2018H
from samples2018 import *
name="Z"
background={
#"DY0J":["DY0J_2018AMCPY"],
#"DY1J":["DY1J_2018AMCPY"],
#"DY2J":["DY2J_2018AMCPY"],
"DY":["DY0J_2018AMCPY", "DY1J_2018AMCPY", "DY2J_2018AMCPY"],
"VBF Z":[
   "EWKZ_2018MGHERWIG",  ## Alternative: "EWKZ_2018MGPY"
### MISSING ### "EWKZint_2018MGPY", # interference with DY
],
}

background["Top"]   = models2018H.background["Top"]
background["Other"] = models2018H.background["Other"]
signal = models2018H.signal
data = models2018H.data

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
fillcolor.update(models2018H.fillcolor)

#systematicsToPlot=["JERUp","JERDown","JESUp","JESDown","puWeightUp","puWeightDown"]
#systematicsToPlot=["JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown"]
systematicsToPlot=["PrefiringWeightUp","PrefiringWeightDown","LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown","PDFX1Up","PDFX1Down","PDFX0Up","PDFX0Down"]

systematicsToPlot+=["JESUp","JESDown"]
from btagvariations import btagsys
systematicsToPlot+=btagsys


from jesnames import jesnames2018
from jernames import jernames
jesList=jesnames2018
systematicsForDC=systematicsToPlot+[x[7:] for x in jesList ]+jernames



linecolor=fillcolor
markercolor=fillcolor


from rebinning import *
from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal,jesList,"2018")

