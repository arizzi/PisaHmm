import ROOT
import os



def writeSystematic (syst, systematicDetail, all_histo_all_syst, availableSamples, datacard, year) :
    
    listSamp = []
    for x in availableSamples : listSamp = listSamp + availableSamples[x]
    
    
    if "decorrelate" not in systematicDetail[syst].keys() : 
        datacard.write( writeLine(syst, systematicDetail[syst]["type"],    1. if "value" not in systematicDetail[syst].keys()  else systematicDetail[syst]["value"],  availableSamples, [s.split("_")[0] for s in set(listSamp)]))
    
    else :
        for g in  systematicDetail[syst]["decorrelate"] :
            sampleWithSystematic = [s.split("_")[0] for s in systematicDetail[syst]["decorrelate"][g]]
            systName = syst+(g if len(systematicDetail[syst]["decorrelate"].keys())>1 else "")
            if "samplevalue" in systematicDetail[syst].keys() : 
                datacard.write( writeLine(systName, systematicDetail[syst]["type"],   systematicDetail[syst]["samplevalue"],  availableSamples, sampleWithSystematic))
                
                
            elif "groupvalue" in systematicDetail[syst].keys() : 
                datacard.write( writeLine(systName, systematicDetail[syst]["type"],   systematicDetail[syst]["groupvalue"][g],  availableSamples, sampleWithSystematic))
            
            else :
                datacard.write( writeLine(systName, systematicDetail[syst]["type"],    1. if "value" not in systematicDetail[syst].keys()  else systematicDetail[syst]["value"],  availableSamples, sampleWithSystematic))
            
            
            
            




def writeUncertainities (orderedUncertainties, lenght, position) :
    uncLine= ""; 
    for n in range(lenght) :
        if n in position :
            uncLine += str(orderedUncertainties[n])
        else : 
            uncLine += "-"
        uncLine += "\t\t"
    
    return uncLine
    

    

            
def writeLine (uncName, uncType, uncertainty,  allSamples, sampleWithSystematic) :
    #print "uncName  ", uncName
    #print "uncType  ", uncType
    #print "uncertainty  ", uncertainty
    #print "allSamples  ", allSamples
    #print "sampleWithSystematic  ", sampleWithSystematic
    
    line = ""
    position = []
    orderedUncertainties = []
    #for x in allSamples.keys() : orderedUncertainties = [0.]*len(allSamples[x])
    
    
    n = 0
    for x in allSamples.keys() :
        for sl in allSamples[x] :
            orderedUncertainties.append(0)
            
            for s in sampleWithSystematic :
                if sl.startswith(s+"_") :
                    position.append(n)
                    orderedUncertainties[-1] = uncertainty[s] if hasattr(uncertainty, "keys") else uncertainty
            n+=1
    
    
    if len(position)==0 : return ""

    line += uncName + "\t\t"
    if len(uncName)<8 : line += "\t"
    line += uncType + "\t"
    if len(uncType)<8 : line += "\t"
    line += writeUncertainities (orderedUncertainties, len(orderedUncertainties), position)

    return line + "\n";







def createWorkSpace(model, all_histo_all_syst, year) :
    print "WorkSpace creation"
    nBins = {}
    varName = {}
    region = {}
    
    print  all_histo_all_syst.keys() 
    for x in all_histo_all_syst.keys() : 
        nBins[x] = all_histo_all_syst[x]["data"+year]["nom"].GetNbinsX()-1
        varName[x] = all_histo_all_syst[x]["data"+year]["nom"].GetName().split("___")[0]
        region[x] = x.split("___")[-1]
    
    
    os.system("mkdir -p workspace")
    datacard=open("workspace/datacard"+year+model.name+".txt","w")
    
    datacard.write("imax "+str(len(all_histo_all_syst.keys()))+"  number of channels\n")
    datacard.write("jmax *  number of backgrounds\n")
    datacard.write("kmax *  number of nuisance parameters (sources of systematical uncertainties)\n")
    datacard.write("------------\n")
    for x in region.keys() : datacard.write("shapes * "+region[x]+"  fileCombine"+year+model.name+".root "+varName[x]+"_$CHANNEL_$PROCESS "+varName[x]+"_$CHANNEL_$PROCESS_$SYSTEMATIC\n")
    datacard.write("------------\n")
    datacard.write("bin \t\t")
    for x in region.keys() : datacard.write(region[x] + " \t" )
    datacard.write("\nobservation \t")
    for x in region.keys() : datacard.write(str(all_histo_all_syst[x]["data"+year]["nom"].Integral(0, nBins[x]+1)) + " \t\t" )
    datacard.write("\n------------\n")

    listSig  = []
    listBkg  = []
    for s in  model.signal :        listSig = listSig + model.signal[s]
    for s in  model.background :    listBkg = listBkg + model.background[s]
    
    listAllSample = listSig + listBkg
    availableSamples = {}
    processNumber = {}
    for n in range(len(listSig)) : processNumber[listSig[n]] = -n
    for n in range(len(listBkg)) : processNumber[listBkg[n]] = n+1
        #if listBkg[n].startswith("EWK") : processNumber[listBkg[n]] = -n
        #else : processNumber[listBkg[n]] = n+1
    
    #remove samples with no predicted events
    emptySamples = {}
    for x in region.keys() : 
        emptySamples[x] = []
        for s in listAllSample :
            #if all_histo_all_syst[s]["nom"].Integral(0, nBins+1) <= 0. or all_histo_all_syst[s]["JESDown"].Integral(0, nBins+1) <= 0. or all_histo_all_syst[s]["JESUp"].Integral(0, nBins+1) <= 0. : emptySamples[x].append(s)
            if all_histo_all_syst[x][s]["nom"].Integral(0, nBins[x]+1) <= 0. or all_histo_all_syst[x][s]["JESDown"].Integral(0, nBins[x]+1) <= 0. or all_histo_all_syst[x][s]["JESUp"].Integral(0, nBins[x]+1) <= 0. : emptySamples[x].append(s)
            #if  "vbf" not in s and "lep" not in s and "VBF" not in s: emptySamples[x].append(s)
        availableSamples[x] = [ s for s in listAllSample if s not in emptySamples[x]]




    datacard.write("bin \t \t \t \t")
    for x in region.keys() : 
        for s in availableSamples[x] :
            datacard.write(region[x]+" \t")
        
    datacard.write("\nprocess \t \t \t")
    for x in region.keys() : 
        for s in availableSamples[x] :
            datacard.write(s+"\t")
        
    datacard.write("\nprocess \t \t \t")
    for x in region.keys() : 
        for s in availableSamples[x] :
            datacard.write(str(processNumber[s])+"\t\t")
        
    datacard.write("\nrate \t \t \t \t")
    for x in region.keys() : 
        for s in availableSamples[x] :
            datacard.write(str(all_histo_all_syst[x][s]["nom"].Integral(0, nBins[x]+1))+"\t")
    datacard.write("\n------------\n")




            
            
    for syst in model.systematicDetail :
        writeSystematic (syst, model.systematicDetail, all_histo_all_syst, availableSamples, datacard, year) 
        #if all(s in all_histo_all_syst[all_histo_all_syst.keys()[0]][availableSamples[0]].keys() for s in [syst+"Down", syst+"Up"]) or model.systematicDetail[syst]["type"] is not "shape" : writeSystematic (syst, model.systematicDetail, all_histo_all_syst, availableSamples, datacard, year) 
            

    for x in region.keys() : datacard.write( region[x]+" autoMCStats 0 1\n\n")
    
    
    f = ROOT.TFile ("workspace/fileCombine"+year+model.name+".root", "recreate")
    f.cd()
    for x in region.keys() : 
        for samp in availableSamples[x] :
            for sy in all_histo_all_syst[x][samp] :
                hname = varName[x] + "_" + region[x] + "_" + samp
                if sy is not "nom" : 
                    if "QCD" in sy : 
                        hname = hname + "_" + samp
                    hname = hname + "_" + sy
                h = all_histo_all_syst[x][samp][sy].Clone(hname)
                h.Write()
    
        h_data_obs = all_histo_all_syst[x]["data"+year]["nom"].Clone(varName[x]+"_"+region[x]+"_data_obs")
        h_data_obs.Write()
    
    print "WorkSpace end"
    
    
    
