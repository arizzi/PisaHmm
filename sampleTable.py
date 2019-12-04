import samples2016
import samples2017
import samples2018

import models2016H
import models2016Z
import models2017H
import models2017Z
import models2018H
import models2018Z

import pprint

def removeYear( string ):
     string = string.replace("2016","")
     string = string.replace("2017","")
     string = string.replace("2018","")
     return string

groups = {}
for sampleGroups in [
    models2018Z.background,models2017Z.background,models2016Z.background,
    models2018Z.signal,models2017Z.signal,models2016Z.signal,
    models2018H.background,models2017H.background,models2016H.background,
    models2018H.signal,models2017H.signal,models2016H.signal]: 
    for g in sampleGroups:
        if not g in groups:
            groups [g] = []
        for s in sampleGroups[g]:
            s = removeYear(s)
            if not s in groups[g]:
                groups[g].append(s)

pprint.pprint(groups)

labels = ['2016Z','2017Z','2018Z','2016H','2017H','2018H']

table = ''

table += 'Group\tSample\t'
for label in labels: table += label+'\t'
table += '  \n'


groupsOrder = ["EWKZ",'VBF H',"gg H","ZH","WH","ttH","Top","DY0J","DY1J","DY2J","DY","DYVBF","Other"]
allGroups = groups.keys()

for group in groupsOrder:
    if group in groups:
        for sample in groups[group]:
            table += group+'\t'+sample+'\t'
            for label in labels: 
                models = globals()["models"+label]
                sampleWithYear = sample.replace("_","_"+label[:4])
                print sample,sampleWithYear, models.background , models.signal
                if (group in models.background and sampleWithYear in models.background[group]) or (group in models.signal and sampleWithYear in models.signal[group]):
#                    table += sampleWithYear+'\t'
                    table += ' X \t'
                else:
                    table += '   \t'
            table += '  \n'
        allGroups.remove(group)

if len(allGroups)==0:
    print table
    fil = open('sampleTable.txt','w')
    fil.write(table)
    fil.close()
else:
    raise Exception(allGroups)


    
