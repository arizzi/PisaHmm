import ROOT
import os
import imp
import copy


workspaceFolder = "workspaceForPostFitHisto"
#workspaceFolder = "workspace"
datacardTxt = "datacard2018H.txt"
fitDiagnostic = "fitDiagnostics.root"

datacardPy   = "datacardForPostFitHisto.py"

skip_combine = False
skip_text2workspace = False

if not skip_text2workspace:
    cmd = "cd %s && text2workspace.py %s --dump-datacard | grep 'DC\.' | sed  's/DC.//g' | head -n -1 > %s"%(workspaceFolder,datacardTxt,datacardPy)
    print(cmd)
    aa = os.popen(cmd)
    aa.read()
else:
    print ("##### Skipping text2workspace.py ##############")

if not skip_combine:
    cmd = "cd %s && rm -rf fitDiagnostics.root && combine -M FitDiagnostics --saveShapes --saveWorkspace --plots  --setParameterRanges r=0.99999,1.00001 %s"%(workspaceFolder,datacardTxt)
    print(cmd)
    aa = os.popen(cmd)
    aa.read()
else:
    print ("##### Skipping combine ##############")

from systematicGrouping import systematicGrouping
systematicDetail = systematicGrouping([],[])

DCprocesses         = imp.load_source('', workspaceFolder+"/"+datacardPy).processes
DCsysts             = imp.load_source('', workspaceFolder+"/"+datacardPy).systs
DCbins              = imp.load_source('', workspaceFolder+"/"+datacardPy).bins

f = ROOT.TFile.Open(workspaceFolder+"/"+fitDiagnostic)
fit_res = f.Get("fit_b")

params = fit_res.floatParsFinal()

print(len(params))

fittedParams={}
for i in range(len(params)):
    name   = params[i].GetName()
    v      = params[i].getValV()
    v_up   = params[i].getErrorLo()
    v_down = params[i].getErrorHi()
    
    fittedParams[name] = (v, v_up, v_down)


def smoothStepFunc(x) : 
     if x >= 1: return 1
     elif x < -1 : return -1
     else: 
         xnorm = x
         xnorm2 = xnorm*xnorm
         return 0.125 * xnorm * (xnorm2 * (3.*xnorm2 - 10.) + 15)

def smoothedNusiance(x,dhi,dlo) : 
    res = x * 0.5 * ((dhi-dlo) + (dhi+dlo)*smoothStepFunc(x))
    return res

def smoothedNusianceDividedMu(x,dhi,dlo) : 
    res = 0.5 * ((dhi-dlo) + (dhi+dlo)*smoothStepFunc(x))
    return res


class Dummy(): pass

bin_ = DCbins[0]

nuisances = {}
for DCsyst in DCsysts:
    (name, boh, type_, boh2, datacardValues) = DCsyst
    nuisances[name] = Dummy()
    nuisances[name].boh = boh
    nuisances[name].type = type_
    nuisances[name].boh2 = boh2
    nuisances[name].datacardValues = datacardValues[bin_]
    nuisances[name].postfit_central = fittedParams[name][0]
    nuisances[name].postfit_down    = fittedParams[name][1]
    nuisances[name].postfit_up      = fittedParams[name][2]

print "NUISANCES: "
for nuis in nuisances:
    print(nuis,nuisances[nuis].type,nuisances[nuis].postfit_central,nuisances[nuis].postfit_down,nuisances[nuis].postfit_up,nuisances[nuis].datacardValues)

print ""

folder = "out"

newfolder = "out/postfit"
os.popen("mkdir -p %s"%(newfolder))

fNames = os.listdir(folder)



def fromNuisanceToHistoName(histos, nominalHistoName, nuis, ud):
    syst_ud = nuis + ud
    histoName  = nominalHistoName + "__syst__%s"%syst_ud
    histoName2 = nominalHistoName.replace("___","__syst__%s___"%syst_ud) + "__syst__%s"%syst_ud
    if histoName in histos:
        return histoName
    elif histoName2 in histos:
        return histoName2
    else:
        for histoName in histos:
            if histoName[:len(nominalHistoName)] == nominalHistoName:
                if histoName[-2:] == "Up":
                    lastWord = histoName.split("_")[-1]
                    if lastWord[:-2] in nuis: return histoName[:-2]+ud
    print("Failed looking for %s of %s."%(nuis,nominalHistoName))
    print("%s nor %s found in histos."%(histoName,histoName2))
#    for histo in histos: print(histo)
    return "HistoSystNotFound"

def fromHistoNameToNuisance(histoName, nuisances, sample):
    sampleShort = sample.split("_")[0]
    histoName = histoName.replace("Up","").replace("Down","")
    lastWord = histoName.split("_")[-1]
    if lastWord in nuisances:
        return lastWord
    matchingNuisances = [nuis for nuis in nuisances if lastWord in nuis and nuisances[nuis].type=='shape']
    if len(matchingNuisances)==1:
        return matchingNuisances[0]
    elif len(matchingNuisances)==0:
        return "UnfittedNuisance"+lastWord
    else:
        if not (lastWord in systematicDetail):
            print "Warning7 %s not found in %s. %s"%(lastWord, systematicDetail.keys(), matchingNuisances)
            return "UnfittedNuisance"+lastWord
        if not ('decorrelate' in systematicDetail[lastWord]):
            print "Error %s has no 'decorrelate'. %s"%(lastWord,matchingNuisances)
            return 1
        for group in systematicDetail[lastWord]['decorrelate']:
            if  group == sampleShort: return lastWord+group
            else:
#                print systematicDetail[lastWord]['decorrelate'][group]
                if sampleShort in systematicDetail[lastWord]['decorrelate'][group]:
                    return lastWord+group
        print "Error %s not found in 'decorrelate'"%(lastWord)
        return 1
    print "Error with %s\t%s"%(histoName, sample)
    return 1


def applyNuisance(newHisto,histos,nominalHistoName,nuisHistoNameDown,nuisHistoNameUp,fitValue):
    up_norm      = 1.
    down_norm    = 1.
    if histos[nominalHistoName].Integral()>0:
        up_norm      = histos[nuisHistoNameUp].Integral()    / histos[nominalHistoName].Integral()
        down_norm    = histos[nuisHistoNameDown].Integral()  / histos[nominalHistoName].Integral()
#    print(newHisto, nominalHistoName, nuisHistoNameDown, nuisHistoNameUp, fitValue)
    for i in range(len(newHisto)):
        nom     = histos[nominalHistoName].GetBinContent(i)
        if nom <=0 : continue
        up           = histos[nuisHistoNameUp].GetBinContent(i)
        down         = histos[nuisHistoNameDown].GetBinContent(i)
        try:
           var  = smoothedNusiance(fitValue,up/up_norm-nom,down/down_norm-nom) 
           sf  = pow(1.+smoothedNusianceDividedMu(fitValue,up_norm-1,down_norm-1),fitValue)
        except:
            print("Warning. Histo %s. Bin %d. nom=%f up=%f down=%f. %s=%f. Forcing sf=1"%(nominalHistoName, i, nom, up, down, nuisHistoNameDown, fitValue))
            sf  = 1
            var = 1 
        newHisto.SetBinContent(i, newHisto.GetBinContent(i)*sf + var*sf)

    
def calculatePostFitHisto(sample, nominalHistoName, histos, nuisances):
    newHisto = histos[nominalHistoName].Clone()
    normSyst = 1.0
    for nuis in nuisances:
        if sample in nuisances[nuis].datacardValues:
            if nuisances[nuis].datacardValues[sample]!=0:
                postFit = nuisances[nuis].postfit_central
                if nuisances[nuis].type == "shape":
                    ud = "Up" if postFit>0 else "Down"
                    nuisHistoNameDown = fromNuisanceToHistoName(histos, nominalHistoName, nuis, "Down")
                    nuisHistoNameUp = nuisHistoNameDown.replace("Down","Up")
                    if nuisHistoNameDown=='HistoSystNotFound' or nuisHistoNameUp=='HistoSystNotFound':
                        print "Warning6: Systematic histo not found %s\t%s"%(str(nominalHistoName),str(nuis))
                        continue
                    applyNuisance(newHisto,histos,nominalHistoName,nuisHistoNameDown,nuisHistoNameUp,postFit)
                elif nuisances[nuis].type == "lnN":
                    normSyst = normSyst * pow(nuisances[nuis].datacardValues[sample], postFit)
                else:
		    pass
        else:
            print("Warning3: ",sample,nuis)
            pass
        
    newHisto.Scale(normSyst)
    return newHisto

def createPostFitFile(inputFile, outputFile, nuisances):
    sample = inputFile.split("/")[-1].replace(".root","").replace("Histos","")
    if sample in DCprocesses or "data" in sample:
        print("Creating %s"%outputFile)
        inFile =  ROOT.TFile.Open(inputFile)
        outFile = ROOT.TFile.Open(outputFile,"recreate")
        histos = {}
        fileSysts = set()
        nominalHistoNames = set()
        for hKey in inFile.GetListOfKeys():
            histo = hKey.ReadObj()
            hName = histo.GetName()
            ## Hack to save only one variable
            if not (("LeadMuon_pt" in hName and "SignalRegion" in hName) or ("data" in hName)):
                continue
            histos[hName] = histo
            if "_syst_" in hName:
                fileSysts.add(hName.split("_")[-1].replace("Up","").replace("Down",""))
                pass
            else:
                nominalHistoNames.add(histo.GetName())

        outFile.cd()
        
        print "fileSysts = %s"%fileSysts
        for nominalHistoName in nominalHistoNames:
            if  "data" in sample:
                newHisto = histos[nominalHistoName].Clone()
                newHisto.Write()
            else:
                newHisto = calculatePostFitHisto(sample, nominalHistoName, histos, nuisances)
                newHisto.Write()
#                fileSysts = [] ### skip systematics
                for fileSyst in fileSysts:
                    histoSysName_up = fromNuisanceToHistoName(histos, nominalHistoName, fileSyst, "Up")
                    histoSysName_down = fromNuisanceToHistoName(histos, nominalHistoName, fileSyst, "Down")
                    if histoSysName_down=='HistoSystNotFound' or histoSysName_up=='HistoSystNotFound':
                        print "Warning5: Systematic histo not found %s\t%s"%(str(nominalHistoName),str(fileSyst))
                        continue
                    newHisto_up = newHisto.Clone(histoSysName_up)
                    newHisto_down = newHisto.Clone(histoSysName_down)
                    nuis = fromHistoNameToNuisance(histoSysName_up, nuisances, sample)
                    if 'UnfittedNuisance' in nuis:
                        up_value, down_value =+1,-1
                    else:
                        up_value, down_value = nuisances[nuis].postfit_up, nuisances[nuis].postfit_down
                    print "Adding plot %s\tsyst=%s\tnominal=%s\tsample=%s, using up|down = %f|%f"%(histoSysName_up,fileSyst,nominalHistoName,sample,up_value, down_value)
                    applyNuisance(newHisto_up,  histos,nominalHistoName,histoSysName_down,histoSysName_up,up_value  )
                    applyNuisance(newHisto_down,histos,nominalHistoName,histoSysName_down,histoSysName_up,down_value)
                    newHisto_up.Write()
                    newHisto_down.Write()
                    
    #                    calculatePostFitHisto(sample, nominalHistoName, histos, nuisances):
                        #~ newHisto = histos[histoSysName].Clone()
                        #~ newHisto.Write()
        inFile.Close()
        outFile.Close()
    else:
        print "Warning4: Skipping %s, it is not among processes in the datacard"%(sample)
#        print DCprocesses

def createPostFitFileSubmit( options):
    inFile, outFile, nuisances = options
    createPostFitFile(inFile, outFile, nuisances)
    
aa = os.popen("cp %s/%s %s"%(workspaceFolder,datacardTxt,newfolder))
aa.read()
aa = os.popen("cp %s/%s %s"%(workspaceFolder,datacardPy,newfolder))
aa.read()
aa = os.popen("cp %s/%s %s"%(workspaceFolder,fitDiagnostic,newfolder))
aa.read()

todo = []
#fNames = ["DY105_2018AMCPYHistos.root"] ## run single file
multiProcess = True
for fName in fNames[:]:
    if ".root" in fName:
        todo.append(("%s/%s"%(folder,fName), "%s/%s"%(newfolder,fName), nuisances))
###     SINGLE PROCESS ###
        if not multiProcess: createPostFitFile("%s/%s"%(folder,fName), "%s/%s"%(newfolder,fName), nuisances)
    elif ".txt" in fName:
        os.popen("cp %s/%s %s/%s"%(folder,fName,newfolder,fName))
    else:
        print("Please check file %s in %s"%(fName,folder))

if multiProcess:
### MULTI PROCESS ###
    from multiprocessing import Pool
    runpool = Pool(40)
    runpool.map(createPostFitFileSubmit, todo)



