import ROOT




def writeUncertainities (uncertainty, lenght, position) :
    uncLine= ""; 
    for n in range(lenght) :
        if n in position :
            uncLine += str(uncertainty)
        else : 
            uncLine += "-"
        uncLine += "\t\t"
    
    return uncLine
    

    
    
    
def writeLine (uncName, uncType, uncertainty,  allSamples, sampleWithSystematic) :
    line = ""
    position = []
    for s in sampleWithSystematic : 
        try :
            position.append(allSamples.index(s))
        except :
            pass
        
    line += uncName + "\t\t"
    if len(uncName)<8 : line += "\t"
    line += uncType + "\t"
    line += writeUncertainities (uncertainty, len(allSamples), position)

    return line + "\n";






def WorkSpace(model, all_histo_all_syst) :
    print "WorkSpace creation"
    nBins = all_histo_all_syst["data"]["nom"].GetNbinsX()
    varName = all_histo_all_syst["data"]["nom"].GetName().split("___")[0]
    
    datacard=open("figure/datacard.txt","w")
    
    datacard.write("imax 1  number of channels\n")
    datacard.write("jmax *  number of backgrounds\n")
    datacard.write("kmax *  number of nuisance parameters (sources of systematical uncertainties)\n")
    datacard.write("------------\n")
    datacard.write("shapes * mu  fileCombine.root "+varName+"_$CHANNEL_$PROCESS "+varName+"_$CHANNEL_$PROCESS_$SYSTEMATIC\n")
    datacard.write("------------\n")
    datacard.write("bin mu\n")
    datacard.write("observation "+str(all_histo_all_syst["data"]["nom"].Integral(0, nBins+1))+"\n")
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





    datacard.write( writeLine("lumi_13TeV", "lnN",    1.025,  listKeys, listKeys))
    datacard.write( writeLine("DY_norm",    "lnN",    1.05,  listKeys, model.background["DY"] + model.background["DYVBF"]))
    datacard.write( writeLine("Top_norm",   "lnN",    1.10,  listKeys, model.background["Top"]))
    #datacard.write( writeLine("ST_norm",    "lnN",    1.10,  listKeys, model.background["ST"]))
    datacard.write( writeLine("VV_norm",    "lnN",    1.10,  listKeys, [ x for x in model.background["Other"] if x not in ["W2J_2018AMCPY","W1J_2018AMCPY","W0J_2018AMCPY"]]))
    
    
    for sy in [ x for x in all_histo_all_syst[listKeys[0]] if x.endswith("Up")] :
        if "QCD" not in sy : datacard.write( writeLine(sy[:-2], "shape",    1.000,  listKeys, listKeys))

    for sy in [ x for x in all_histo_all_syst[listKeys[0]] if "QCD" in x] :
        for samp in listKeys :
            datacard.write( writeLine(samp+"_"+sy[:-2], "shape",    1.000,  listKeys, [samp]))

    datacard.write( "mu autoMCStats 0 1\n\n")
    
    
    f = ROOT.TFile ("figure/fileCombine.root", "recreate")
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
    
    h_data_obs = all_histo_all_syst["data"]["nom"].Clone(varName+"_mu_data_obs")
    h_data_obs.Write()
    
    
    
    
    
