import samples2016
import samples2017
import samples2018

samples = {}
samples.update(samples2016.samples)
samples.update(samples2017.samples)
samples.update(samples2018.samples)

import models2016Z as models2016
import models2017Z as models2017
import models2018Z as models2018
name="Z"


background={}
signal={}
data = {'All': ['data2016','data2017','data2018']}


for models in [models2016,models2017,models2018]:
   for mapToFillName in ["background","signal"]:
      mapToRead = getattr(models,mapToFillName)
      mapToFill = globals()[mapToFillName]
      for sampleSet in mapToRead:
         if sampleSet in mapToFill:
            for sample in mapToRead[sampleSet]:
               if not sample in mapToFill[sampleSet]: mapToFill[sampleSet].append(sample)
         else: mapToFill[sampleSet] = mapToRead[sampleSet]

import pprint

print "\nbackground = ",
pprint.pprint(background)
print "\nsignal = ",
pprint.pprint(signal)
print "\ndata = ",
pprint.pprint(data)
print



#sorting
backgroundSorted=["Other","Top","DY0J","DY1J","DY2J","EWKZ"]
backgroundSorted+=[x for x in background if x not in backgroundSorted]

fillcolor={}
fillcolor.update(models2016.fillcolor)
fillcolor.update(models2017.fillcolor)
fillcolor.update(models2018.fillcolor)


systematicsToPlot=["LHEPdfUp","LHEPdfDown","QGLweightUp","QGLweightDown","JERUp","JERDown","puWeightUp","puWeightDown","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","MuScaleUp","MuScaleDown","AlternativeUp","AlternativeDown"]

from jesnames import jes2016
from jernames import jernames
systematicsForDC=systematicsToPlot+[x[10:] for x in jes2016 ]+jernames
systematicsToPlot+=["JESUp","JESDown"]

from rebinning import *
#possibly change the rebinning here

from systematicGrouping import *
systematicDetail = systematicGrouping(background, signal)



linecolor=fillcolor
markercolor=fillcolor

