import ROOT
import os



def writeSystematic (x, systematicDetail, all_histo_all_syst, listKeys, datacard, year) :
    
    
    if "decorrelate" not in systematicDetail[x].keys() : 
        datacard.write( writeLine(x, systematicDetail[x]["type"],    1. if "value" not in systematicDetail[x].keys()  else systematicDetail[x]["value"],  listKeys, listKeys))
    
    else :
        for g in  systematicDetail[x]["decorrelate"] :
            if "samplevalue" in systematicDetail[x].keys() : 
                datacard.write( writeLine(x, systematicDetail[x]["type"],   systematicDetail[x]["samplevalue"],  listKeys, systematicDetail[x]["decorrelate"][g]))
                #if not set(listKeys).isdisjoint(systematicDetail[x]["decorrelate"][g]) : datacard.write( writeLine(x, systematicDetail[x]["type"],   systematicDetail[x]["samplevalue"],  listKeys, systematicDetail[x]["decorrelate"][g]))
                
                
            elif "groupvalue" in systematicDetail[x].keys() : 
                datacard.write( writeLine(x, systematicDetail[x]["type"],   systematicDetail[x]["groupvalue"][g],  listKeys, systematicDetail[x]["decorrelate"][g]))
                #if not set(listKeys).isdisjoint(systematicDetail[x]["decorrelate"][g]) : datacard.write( writeLine(x, systematicDetail[x]["type"],   systematicDetail[x]["groupvalue"][g],  listKeys, systematicDetail[x]["decorrelate"][g]))
            
            else :
                datacard.write( writeLine(x, systematicDetail[x]["type"],    1. if "value" not in systematicDetail[x].keys()  else systematicDetail[x]["value"],  listKeys, systematicDetail[x]["decorrelate"][g]))
                #if not set(listKeys).isdisjoint(systematicDetail[x]["decorrelate"][g]) : datacard.write( writeLine(x, systematicDetail[x]["type"],    1. if "value" not in systematicDetail[x].keys()  else systematicDetail[x]["value"],  listKeys, systematicDetail[x]["decorrelate"][g]))
            
            
            
            




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
    line = ""
    position = []
    orderedUncertainties = [0.]*len(allSamples)

    
    for n in range(len(allSamples)) :
        for s in sampleWithSystematic : 
            if allSamples[n].startswith(s) :
                position.append(n)
                orderedUncertainties[n] = uncertainty[s] if hasattr(uncertainty, "keys") else uncertainty
        
    line += uncName + "\t\t"
    if len(uncName)<8 : line += "\t"
    line += uncType + "\t"
    if len(uncType)<8 : line += "\t"
    line += writeUncertainities (orderedUncertainties, len(allSamples), position)

    return line + "\n";







def createWorkSpace(model, all_histo_all_syst, year) :
    print "WorkSpace creation"
    nBins = all_histo_all_syst["data"+year]["nom"].GetNbinsX()
    varName = all_histo_all_syst["data"+year]["nom"].GetName().split("___")[0]
    
    os.system("mkdir -p workspace")
    datacard=open("workspace/datacard"+year+".txt","w")
    
    datacard.write("imax 1  number of channels\n")
    datacard.write("jmax *  number of backgrounds\n")
    datacard.write("kmax *  number of nuisance parameters (sources of systematical uncertainties)\n")
    datacard.write("------------\n")
    datacard.write("shapes * mu  fileCombine"+year+".root "+varName+"_$CHANNEL_$PROCESS "+varName+"_$CHANNEL_$PROCESS_$SYSTEMATIC\n")
    datacard.write("------------\n")
    datacard.write("bin mu\n")
    datacard.write("observation "+str(all_histo_all_syst["data"+year]["nom"].Integral(0, nBins+1))+"\n")
    datacard.write("------------\n")

    listSig  = []
    listBkg  = []
    for x in  model.signal :        listSig = listSig + model.signal[x]
    for x in  model.background :    listBkg = listBkg + model.background[x]
    
    listKeys = listSig + listBkg

    #remove samples with no predicted events
    emptySamples = []
    for x in listKeys :
        if all_histo_all_syst[x]["nom"].Integral(0, nBins+1) <= 0. or all_histo_all_syst[x]["JESDown"].Integral(0, nBins+1) <= 0. or all_histo_all_syst[x]["JESUp"].Integral(0, nBins+1) <= 0. : emptySamples.append(x)
    listKeys = [ x for x in listKeys if x not in emptySamples]


    datacard.write("bin \t \t \t \t")
    for x in listKeys :
        datacard.write("mu \t \t")
        
    datacard.write("\nprocess \t \t \t")
    for x in listKeys :
        datacard.write(x+"\t")
        
    datacard.write("\nprocess \t \t \t")
    for n in range(len(listKeys)) :
        datacard.write(str(n+1-len(listSig))+"\t\t")
        
    datacard.write("\nrate \t \t \t \t")
    for x in listKeys :
        datacard.write(str(all_histo_all_syst[x]["nom"].Integral(0, nBins+1))+"\t")
    datacard.write("\n------------\n")





    #datacard.write( writeLine("lumi_13TeV", "lnN",    1.025,  listKeys, listKeys))
    #datacard.write( writeLine("DY_norm",    "lnN",    1.05,  listKeys, model.background["DY"] + model.background["DYVBF"]))
    #datacard.write( writeLine("Top_norm",   "lnN",    1.10,  listKeys, model.background["Top"]))
    ##datacard.write( writeLine("ST_norm",    "lnN",    1.10,  listKeys, model.background["ST"]))
    #datacard.write( writeLine("VV_norm",    "lnN",    1.10,  listKeys, [ x for x in model.background["Other"] if x not in ["W2J_2018AMCPY","W1J_2018AMCPY","W0J_2018AMCPY"]]))
    
    
    #for sy in [ x for x in all_histo_all_syst[listKeys[0]] if x.endswith("Up")] :
        #if "QCD" not in sy : datacard.write( writeLine(sy[:-2], "shape",    1.000,  listKeys, listKeys))

    #for sy in [ x for x in all_histo_all_syst[listKeys[0]] if "QCD" in x] :
        #for samp in listKeys :
            #datacard.write( writeLine(samp+"_"+sy[:-2], "shape",    1.000,  listKeys, [samp]))
            
            
    for x in model.systematicDetail :
        writeSystematic (x, model.systematicDetail, all_histo_all_syst, listKeys, datacard, year) 
            

    datacard.write( "mu autoMCStats 0 1\n\n")
    
    
    f = ROOT.TFile ("workspace/fileCombine"+year+".root", "recreate")
    f.cd()
    for samp in listKeys :
        for sy in all_histo_all_syst[samp] :
            hname = varName + "_mu_" + samp
            if sy is not "nom" : 
                if "QCD" in sy : 
                    hname = hname + "_" + samp
                hname = hname + "_" + sy
            h = all_histo_all_syst[samp][sy].Clone(hname)
            h.Write()
    
    h_data_obs = all_histo_all_syst["data"+year]["nom"].Clone(varName+"_mu_data_obs")
    h_data_obs.Write()
    
    print "WorkSpace end"
    
    
    
