import ROOT
import sys,os
#from samples2016 import samples
import importlib
import postfitPlot
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("model", help="model to plot")
parser.add_argument("-p", "--postfit", help="plot postfit plot", action="store_true")
parser.add_argument("-v", "--variablesToFit", nargs="*")
parser.print_help()
args = parser.parse_args()


model=importlib.import_module(args.model)
samples=model.samples
from labelDict import *  
year="+".join(model.data.keys())
lumi = "%2.1f fb^{-1}" 
from math import *
from array import array
ROOT.gROOT.ProcessLine(".x setTDRStyle.C")
import re
import WorkSpace

ROOT.gROOT.SetBatch(True)

totev={}
totevCount={}
totevSkim={}
hnForSys={}

def makeLegend (yDown, yUp, name = "") :
    myLegend= ROOT.TLegend(0.82, yDown, 1, yUp, name) 
    myLegend.SetFillColor(0);                          
    myLegend.SetBorderSize(0);                         
    myLegend.SetTextFont(42);                          
    myLegend.SetTextSize(0.025);   
    return myLegend
    
    

def makeText (x, y, someText, font, size = 0.05) :
    tex = ROOT.TLatex(x,y,someText);
    tex.SetNDC();
    tex.SetTextAlign(35);
    tex.SetTextFont(font);
    tex.SetTextSize(size);
    tex.SetLineWidth(2);
    return tex


    
def setHistoStyle (h, gr) :
    h.SetFillColor(model.fillcolor[gr])
    h.SetTitle("")
    h.SetLineColor(model.linecolor[gr])
    h.SetFillStyle(1001) #NEW
    h.SetLineStyle(1) #NEW    
    
    
def makeRatioMCplot(h) :
    hMC = h.Clone()
    hMC.SetLineWidth(1)
    for n in range(hMC.GetNbinsX()) :
       # hMC.SetBinError(n,  hMC.GetBinError(n)/hMC.GetBinContent(n) if hMC.GetBinContent(n)>0 else 0 )
        e = hMC.GetBinError(n)/hMC.GetBinContent(n) if hMC.GetBinContent(n)>0 else 0     
        hMC.SetBinError(n,  e if e<0.5 else 0.5 )                                        
        hMC.SetBinContent(n, 0.)
    return hMC
    
def setStyle(h, isRatio=False) :
    h.SetTitle("")
    w = 0.055 * (2.5 if isRatio else 1.)
    h.GetYaxis().SetLabelSize(w)
    h.GetXaxis().SetLabelSize(w)
    h.GetYaxis().SetTitleSize(w)
    h.GetXaxis().SetTitleSize(w)
    if isRatio : 
        h.GetYaxis().SetTitle("Data/MC - 1")
        h.GetYaxis().SetTitleOffset(0.5)
#        h.GetXaxis().SetTitle(str(h.GetName()).split("___")[0])
	xKey = str(h.GetName()).split("___")[0]                                              
	h.GetXaxis().SetTitle(labelVariable[xKey] if xKey in labelVariable.keys() else xKey) 
    else :
        binWidht = str(h.GetBinWidth(1))[:4]
        if binWidht.endswith(".") : binWidht = binWidht[:3]
        h.GetXaxis().SetLabelSize(0)
        h.GetYaxis().SetTitle("Entries/"+binWidht)
        h.GetXaxis().SetLabelSize(0)
        h.GetXaxis().SetTitleSize(0)


def findSyst(hn,sy,f) :
  #  print hnForSys.keys()
    if hn in hnForSys and sy in hnForSys[hn]:
 #       print hn,sy,hnForSys[hn]
	return hnForSys[hn][sy]
    if hn not in hnForSys :
	hnForSys[hn]={}
    allh=list([x.GetName() for x in f.GetListOfKeys()])
    h1=hn+"__syst__"+sy    
    h2=re.sub("___","__syst__"+sy+"___",hn)    
    h3=re.sub("___","__syst__"+sy+"___",hn)+"__syst__"+sy    
#    print "Syst options",h1,h2,h3
    if h1 in allh:
	 hnForSys[hn][sy]=h1
	 return h1
    if h2 in allh:
	 hnForSys[hn][sy]=h2
	 return h2
    if h3 in allh:
	 hnForSys[hn][sy]=h3
	 return h3
    print "none matching",hn,sy,f
    return ""

def totevents(s):
    if s not in totev:
       totev[s]=1e-9
       totevCount[s]=1e-9
       totevSkim[s]=1e-9
       for fn in samples[s]["files"]:
	  f=ROOT.TFile.Open(fn)
	  run=f.Get("Runs")
	  totevSkim[s]+=f.Get("Events").GetEntries()
	  if run :
  	    hw=ROOT.TH1F("hw","", 5,0,5)
	    run.Project("hw","1","genEventSumw")
	    totev[s]+=hw.GetSumOfWeights()
	    run.Project("hw","1","genEventCount")
	    totevCount[s]+=hw.GetSumOfWeights()
	    print totev[s]
#    print "returning",totev[s], "for",s
    return totev[s]



def writeYields(ftxt, gr, integral, error, dataEvents) :
    line = "%s\t%s +- %s\t%s "%(gr,round(integral[gr]["nom"],5), round(error[gr],5),round(integral[gr]["nom"]/dataEvents,5))
    for sy in integral[gr].keys()  : 
        if sy is not 'nom' : line+="\t%s "%(round(integral[gr][sy],5))
    ftxt.write(line+"\n")

def setName (d, sv) :
    if "decorrelate" not in model.systematicDetail[sv].keys() : return sv
    elif model.systematicDetail[sv]["decorrelate"] : return sv
    else :
        for g in model.systematicDetail[sv]["decorrelate"].keys() :
            for x in model.systematicDetail[sv]["decorrelate"][g] :
                if d.startswith(x) : return sv+g
    return  "notSysToApply" #this means that the systematic sv does not affect the sample d.    e.g. d=DY  sv= VVxsec
    
    
    
def computeSingleSystVariation(d, hn, sv, syVar="nom") :
    x = postFit.postfitValue(sv, syVar)
    histoSingleSyst[hn][d][sv]["variation"] = histoSingleSyst[hn][d][sv]["sum"].Clone()
    histoSingleSyst[hn][d][sv]["variation"].Scale(postFit.smoothStepFunc(x))
    histoSingleSyst[hn][d][sv]["variation"].Add(histoSingleSyst[hn][d][sv]["diff"])
    histoSingleSyst[hn][d][sv]["variation"].Scale(0.5 * x)
    return histoSingleSyst[hn][d][sv]["variation"]

def computeSingleSyst(model, f, d, hn, h, histoSingleSyst) :
    for sv in model.systematicDetail.keys() :
        svName = setName(d, sv)
        if svName == "notSysToApply" : continue
        hsUp=h.Clone()
        hsDown=h.Clone()
        if model.systematicDetail[sv]["type"]=="lnN" :
            hsUp.Scale(model.systematicDetail[sv]["value"])
            hsDown.Scale(1./model.systematicDetail[sv]["value"])
        if model.systematicDetail[sv]["type"]=="shape" :
            if all(x in model.systematicsToPlot for x in [sv+"Up", sv+"Down"]): 
                hsUp=f[d].Get(findSyst(hn,sv+"Up",f[d]))
                hsDown=f[d].Get(findSyst(hn,sv+"Down",f[d]))
                if hsUp and hsDown :
                    if hn.split("___")[0] in model.rebin.keys() : 
                        hsUp = (hsUp.Rebin(len(model.rebin[hn.split("___")[0]])-1,"hnew"+sv,array('d',model.rebin[hn.split("___")[0]]))).Clone(hsUp.GetName())
                        hsDown = (hsDown.Rebin(len(model.rebin[hn.split("___")[0]])-1,"hnew"+sv,array('d',model.rebin[hn.split("___")[0]]))).Clone(hsDown.GetName())
            
        histoSingleSyst[hn][d][svName] = {}
        histoSingleSyst[hn][d][svName]["Up"] = hsUp.Clone()
        histoSingleSyst[hn][d][svName]["Down"] = hsDown.Clone()
        #histoSingleSyst[hn][d][svName]["Down"] = hsUp.Clone()
        #histoSingleSyst[hn][d][svName]["Up"] = hsDown.Clone()
        
    for sv in histoSingleSyst[hn][d].keys() :
        hDiff = histoSingleSyst[hn][d][sv]["Up"].Clone()
        hSum  = histoSingleSyst[hn][d][sv]["Up"].Clone()
        hDiff.Add(histoSingleSyst[hn][d][sv]["Down"], -1)
        hSum.Add(histoSingleSyst[hn][d][sv]["Down"])
        hSum.Add(h, -2)
        
        if "diff" not in histoSingleSyst[hn][d].keys() :  
            histoSingleSyst[hn][d][sv]["diff"] =  hDiff.Clone()
            histoSingleSyst[hn][d][sv]["sum"]  =  hSum.Clone()
        else :
            histoSingleSyst[hn][d][sv]["diff"].Add(hDiff)
            histoSingleSyst[hn][d][sv]["sum"].Add(hSum)
        
        if "nominalVariation" not in histoSingleSyst[hn][d].keys() : histoSingleSyst[hn][d]["nominalVariation"] = computeSingleSystVariation(d, hn, sv).Clone()
        else : histoSingleSyst[hn][d]["nominalVariation"].Add(computeSingleSystVariation(d, hn, sv))

def fitVariation (model, f, d, hn, h, histoSingleSyst, sy = "noSystematic") :
        
    if len(histoSingleSyst[hn][d].keys()) == 0 : computeSingleSyst(model, f, d, hn, h, histoSingleSyst)

    sv = sy.replace("Up", "").replace("Down", "")

    if sv in model.systematicDetail and (sy.endswith("Up") or sy.endswith("Down") ):
        hv = histoSingleSyst[hn][d]["nominalVariation"].Clone()
        hv.Add(histoSingleSyst[hn][d][sv]["variation"], -1.)
        hv.Add(computeSingleSystVariation(d, hn, sv, "Up" if sy.endswith("Up") else "Down"))
        return hv
    else : return  histoSingleSyst[hn][d]["nominalVariation"]


def addFitVariation(h, variationToAdd) :
    for n in range(h.GetNbinsX()+2) :
        relE = 0 if h.GetBinContent(n)<=0. else h.GetBinError(n)/h.GetBinContent(n)
        h.SetBinContent(n, h.GetBinContent(n)+variationToAdd.GetBinContent(n))
        if h.GetBinContent(n)>0 : h.SetBinError(n, h.GetBinContent(n)*relE)
    


f={}
for group in model.signal :
    for s in model.signal[group] :
        f[s]=ROOT.TFile.Open("out/%sHistos.root"%s)
for group in model.background :
    for b in model.background[group] :
        f[b]=ROOT.TFile.Open("out/%sHistos.root"%b)
for group in model.data :
    for d in model.data[group] :
        f[d]=ROOT.TFile.Open("out/%sHistos.root"%d)

histoNames=list(set([x.GetName() for y in f.keys() for x in f[y].GetListOfKeys() ]))

canvas={}
datastack={}
datasum={}
histos={}
histosum={}
histosSig={}
histoSigsum={}

datasumSyst={}
histosumSyst={}
histoSigsumSyst={}
histosSignal={}
all_histo_all_syst={}

integral={}
error={}

histoSingleSyst={}

#i=1
ROOT.gStyle.SetOptStat(0)


postFit = postfitPlot.PostFit()


#def superImposedPlot (stackB, stackS, outpath)  :
    #directory = outpath+"/superImposed"
    #os.system("mkdir -p "+directory)
    #canvas=ROOT.TCanvas("canvas_","",900,750) 
    

    #stackB.GetHists()[0].DrawNormalized()

    #for hb in stackB.GetHists() :
        #hb.DrawNormalized("same")
    #for hs in stackS.GetHists() :
        #hs.DrawNormalized("same")
    
    #canvas.Print(directory+"/a.png")
    

def addHistoInTStack (hs, stackSys, all_histo_all_syst, gr, hn, sy, d, makeWorkspace) :
    if sy not in stackSys[hn].keys() : stackSys[hn][sy]=hs.Clone()
    else : stackSys[hn][sy].Add(hs)
    
    if sy not in integral[gr].keys() : integral[gr][sy]=hs.Integral(0,hs.GetNbinsX()+1)
    else : integral[gr][sy]+=hs.Integral(0,hs.GetNbinsX()+1)
    
    if makeWorkspace : all_histo_all_syst[hn][d][sy]=hs.Clone()
    


def fill_datasum(f, gr, samplesToPlot, SumTH1, stack, stackSys, hn, myLegend, ftxt, lumi=0, data=False) :
    integral[gr]={}
    integral[gr]["nom"]=0
    error[gr]=0
    for d in samplesToPlot[gr]: 
      if makeWorkspace : all_histo_all_syst[hn][d]={}
      nevents = 1 if data else totevents(d)
      lumi_over_nevents = lumi/nevents
      if f[d] :
        h=f[d].Get(hn)
        histoSingleSyst[hn][d] = {}
        if  h:
            if hn.split("___")[0] in model.rebin.keys() : 
                #print "Rebin",hn
                h = (h.Rebin(len(model.rebin[hn.split("___")[0]])-1,"hnew",array('d',model.rebin[hn.split("___")[0]]))).Clone(hn)
            if data : h.SetMarkerStyle(10)
            else : 
                if postfit : addFitVariation( h, fitVariation(model, f, d, hn, h, histoSingleSyst))
                h.Scale(samples[d]["xsec"]*lumi_over_nevents)
                error_b = ROOT.Double(0)
                integral[gr]["nom"]+=h.IntegralAndError(0,h.GetNbinsX()+1,error_b)
                error[gr] = sqrt(error[gr]*error[gr] + error_b*error_b)
                setHistoStyle (h, gr) 
            if hn not in SumTH1 :
                SumTH1[hn]=h.Clone()
                stackSys[hn]={}
                for sy in model.systematicsToPlot :
                    if not data :
                        hs=f[d].Get(findSyst(hn,sy,f[d]))
                        if postfit : 
                            hs=f[d].Get(hn).Clone()
                        if hn.split("___")[0] in model.rebin.keys() : 
                            hs = (hs.Rebin(len(model.rebin[hn.split("___")[0]])-1,"hnew"+sy,array('d',model.rebin[hn.split("___")[0]]))).Clone(hs.GetName())
                        if hs:
                            if postfit : addFitVariation( hs, fitVariation(model, f, d, hn, h, histoSingleSyst, sy))
                            hs.Scale(samples[d]["xsec"]*lumi_over_nevents)
                            addHistoInTStack (hs, stackSys, all_histo_all_syst, gr, hn, sy, d, makeWorkspace) 
                        else : 
                            addHistoInTStack (h, stackSys, all_histo_all_syst, gr, hn, sy, d, makeWorkspace) 
                    else :
                        addHistoInTStack (h, stackSys, all_histo_all_syst, gr, hn, sy, d, makeWorkspace) 
            else :
                SumTH1[hn].Add(h)	
                for sy in model.systematicsToPlot :
                    hs=f[d].Get(findSyst(hn,sy,f[d]))
                    if postfit : 
                        hs=f[d].Get(hn).Clone()
                    if hs:
                        if hn.split("___")[0] in model.rebin.keys() : 
                            hs = (hs.Rebin(len(model.rebin[hn.split("___")[0]])-1,"hnew"+sy,array('d',model.rebin[hn.split("___")[0]]))).Clone(hs.GetName())
                        if postfit : addFitVariation( hs, fitVariation(model, f, d, hn, h, histoSingleSyst, sy))
                        if not data : hs.Scale(samples[d]["xsec"]*lumi_over_nevents)
                        addHistoInTStack (hs, stackSys, all_histo_all_syst, gr, hn, sy, d, makeWorkspace) 
                    else :
                        addHistoInTStack (h, stackSys, all_histo_all_syst, gr, hn, sy, d, makeWorkspace) 
            stack[hn].Add(h)
            if makeWorkspace : all_histo_all_syst[hn][d]["nom"]=h.Clone()
        else:
            print "Cannot open",d,hn
            exit(1)
        if gr in model.signal : 
            if gr not in histosSignal[hn].keys() : histosSignal[hn][gr] = h.Clone()
            else : histosSignal[hn][gr].Add(h)
    if not data : writeYields(ftxt, gr, integral, error, datasum[hn].Integral(0,datasum[hn].GetNbinsX()+1))
    #if not data : 
        #ftxt.write("%s\t%s +- %s\t%s \n"%(gr,integral[gr]["nom"], error[gr],integral[gr]["nom"]/datasum[hn].Integral(0,datasum[hn].GetNbinsX()+1)))
        #for sy in integral[gr].keys() : ftxt.write("%s\t%s +- %s\t%s \n"%(gr,integral[gr]["nom"], error[gr],integral[gr]["nom"]/datasum[hn].Integral(0,datasum[hn].GetNbinsX()+1)))
    if (data) : myLegend.AddEntry(h,"data","P")
    else : myLegend.AddEntry(h,gr,"f")





def makeplot(hn,saveintegrals=True):
 if "__syst__" not in hn :
   myLegend = makeLegend (0.4, 0.9)
   myLegend_sy = makeLegend (0.1, 0.15 + 0.015*len(model.systematicsToPlot))
   outpath="figure/%s/%s"%(year,model.name)
   os.system("mkdir -p "+outpath)
   os.system("cp out/description.txt "+outpath)
   os.system("git rev-parse HEAD > "+outpath+"/git_commit.txt")
   os.system("git diff HEAD > "+outpath+"/git_diff.txt")
   os.system("git status HEAD > "+outpath+"/git_status.txt")
   YieldFileName = outpath+"/"+hn+".txt"
   if postfit : YieldFileName = outpath+"/"+hn+"_postFit.txt"
   ftxt=open(YieldFileName,"w")
   #print "Making histo",hn
   histos[hn]=ROOT.THStack(hn,"") 
   histosSig[hn]=ROOT.THStack(hn,"") 
   datastack[hn]=ROOT.THStack(hn,"") 

   canvas[hn]=ROOT.TCanvas("canvas_"+hn,"",900,750)       
   #canvas[hn].SetRightMargin(.0);                        
   canvas[hn].Divide(1,2)                                 
   canvas[hn].GetPad(2).SetPad(0.0,0.,0.90,0.25)           
   canvas[hn].GetPad(1).SetPad(0.0,0.20,0.90,1.) 

   ROOT.gStyle.SetPadLeftMargin(0.15)                     
   canvas[hn].GetPad(2).SetBottomMargin(0.35)              
   canvas[hn].GetPad(2).SetTopMargin(0.)                
                   
   if makeWorkspace : all_histo_all_syst[hn] = {}

   lumitot=0
   for gr in model.data:
     for d in model.data[gr]:
       lumitot+=samples[d]["lumi"]
   
   histoSingleSyst[hn] = {}
   histosSignal[hn]={} 
   for gr in model.data:
     fill_datasum (f, gr, model.data, SumTH1=datasum, stack=datastack, stackSys=datasumSyst, hn=hn, myLegend=myLegend, ftxt=ftxt, data = True) 

   DataYieldLine = "sample \t yield  \t\tfraction"
   for sy in model.systematicsToPlot : 
       DataYieldLine = DataYieldLine + "\t" + sy + "\t"
   ftxt.write(DataYieldLine+"\n")
   #if saveintegrals:
   ftxt.write("DATA \t%s \n"%(datasum[hn].Integral(0,datasum[hn].GetNbinsX()+1)))

   
   for gr in model.backgroundSorted:
     fill_datasum (f, gr, model.background, SumTH1=histosum, stack=histos, stackSys=histosumSyst, hn=hn, myLegend=myLegend, ftxt=ftxt, lumi=lumitot) 


   
   for gr in model.signal:
     fill_datasum (f, gr, model.signal, SumTH1=histoSigsum, stack=histosSig, stackSys=histoSigsumSyst, hn=hn, myLegend=myLegend, ftxt=ftxt, lumi=lumitot)

     
   

   
   for gr in model.signal:
        h=histosSignal[hn][gr]     
        histos[hn].Add(h.Clone())
        h.SetLineColor(model.linecolor[gr])       
        h.SetFillStyle(0)                   
        h.SetLineWidth(3)                   
        h.SetLineStyle(2)                   
        h.Scale(20.)                        
        myLegend.AddEntry(h,gr+" x20","l")       
   firstBlind=100000
   lastBlind=-1
   for i in range(histosSig[hn].GetStack().Last().GetNbinsX()+1) :
	if histosSig[hn].GetStack().Last().GetBinContent(i) > 0.1*sqrt(abs(histos[hn].GetStack().Last().GetBinContent(i))) and histosSig[hn].GetStack().Last().GetBinContent(i)/(0.001+abs(histos[hn].GetStack().Last().GetBinContent(i))) > 0.05 :
		#print "to blind",hn,i,abs(histos[hn].GetStack().Last().GetBinContent(i)), histosSig[hn].GetStack().Last().GetBinContent(i)	
	        if i < firstBlind:
		    firstBlind=i
                lastBlind=i
   for i in range(firstBlind,lastBlind+1) :
       datastack[hn].GetStack().Last().SetBinContent(i,0)
       datasum[hn].SetBinContent(i,0)
       #print "blinded",i,hn
   myLegend.Draw() #NEW  
   canvas[hn].cd(1)
   histos[hn].SetTitle("") 
   datastack[hn].Draw("E P")
   #datastack[hn].GetXaxis().SetTitle(hn)
   setStyle(datastack[hn].GetHistogram())
   datastack[hn].Draw("E P")
   histos[hn].Draw("hist same")
#  histos[hn].Draw("hist")                                                               
   histosum[hn].SetLineWidth(0)                                                           
   histosum[hn].SetFillColor(ROOT.kBlack);                                                
   histosum[hn].SetFillStyle(3004);                                                                       
   setStyle(histos[hn].GetHistogram())
   canvas[hn].Update()                
   histosum[hn].Draw("same E2")        


   datastack[hn].Draw("E P same")
   for gr in model.signal:     histosSignal[hn][gr].Draw("hist same")                                                
                                                                         
   t0 = makeText(0.65,0.85,labelRegion[hn.split("___")[1]] if hn.split("___")[1] in labelRegion.keys() else hn.split("___")[1], 61)  
   t1 = makeText(0.15,0.91,"CMS", 61)                                                           
   t2 = makeText(0.32,0.91,str(year), 42)                                                       
   t3 = makeText(0.90,0.91,lumi%(lumitot/1000.)+"  (13 TeV)", 42)                                
   t0.Draw()                                                             
   t1.Draw()                                                             
   t2.Draw()                                                             
   t3.Draw()                                     
   datastack[hn].GetHistogram().SetMarkerStyle(10)                       

   
   
   canvas[hn].Update()
   ratio=datasum[hn].Clone()
   ratio.Add(histosum[hn],-1.) 
   ratio.Divide(histosum[hn])
   ratio.SetMarkerStyle(10)

   canvas[hn].cd(2)
   setStyle(ratio, isRatio=True)

   ratio.Draw()
   ratioError = makeRatioMCplot(histosum[hn])  
   ratioError.Draw("same E2")                 

   ratio.SetAxisRange(-0.5,0.5,"Y")
   ratio.GetYaxis().SetNdivisions(5)
   ratiosy=[]
   for j,sy in enumerate(model.systematicsToPlot):
       ratiosy.append(histosumSyst[hn][sy].Clone())
       ratiosy[-1].Add(histosum[hn],-1.)
       ratiosy[-1].Divide(histosum[hn])
       ratiosy[-1].SetLineColor(1+j)
       #ratiosy[-1].SetLineStyle(j)
       ratiosy[-1].SetFillStyle(0)
       myLegend_sy.AddEntry(ratiosy[-1],sy,"l")
       ratiosy[-1].Draw("same hist")
       #print "Heu",hn,sy,histosumSyst[hn][sy].Integral(),histosum[hn].Integral(),lumitot,ratiosy[-1]
   canvas[hn].cd()
   myLegend_sy.Draw()
    
   tchi2 = makeText(0.22,0.22,"#chi^{2}="+str(round(datasum[hn].Chi2Test(histosum[hn],"UWCHI2/NDF"),2)), 42, 0.025)     
   tKS   = makeText(0.32,0.22,"KS="+str(round(datasum[hn].KolmogorovTest(histosum[hn]),2)), 42, 0.025) 
   tchi2.Draw()
   tKS.Draw()

   canvas[hn].GetPad(2).SetGridy()
   if postfit : canvas[hn].SaveAs(outpath+"/%s_postFit.png"%hn)	   
   else :
	canvas[hn].SaveAs(outpath+"/%s.png"%hn)   
	canvas[hn].SaveAs(outpath+"/%s.root"%hn)   
   #canvas[hn].SaveAs("%s.root"%hn)	   
   canvas[hn].GetPad(1).SetLogy(True)
   if postfit : canvas[hn].SaveAs(outpath+"/%s_log_postFit.png"%hn)	   
   else :       
	canvas[hn].SaveAs(outpath+"/%s_log.png"%hn)   
	canvas[hn].SaveAs(outpath+"/%s_log.root"%hn)   


variablesToFit = []
makeWorkspace = False
if args.variablesToFit != None : 
    variablesToFit = args.variablesToFit
    makeWorkspace = True
postfit = False
postfit = args.postfit


print "postfit", postfit
print "makeWorkspace", makeWorkspace
print "variablesToFit", variablesToFit



his=[x for x in histoNames if "__syst__" not in x]
print his[0]
makeplot(variablesToFit[0] if makeWorkspace else his[0],True) #do once for caching normalizations and to dump integrals

if not makeWorkspace :
 print "Preload"
 for ff in f:
   for h in histoNames :
     f[ff].Get(h)
 print "Preload-done"

if makeWorkspace:
    for hn in variablesToFit[1:] :  makeplot(hn,True)
    WorkSpace.createWorkSpace(model, all_histo_all_syst, year)
else :
   from multiprocessing import Pool
   runpool = Pool(20)
   #toproc=[(x,y,i) for y in sams for i,x in enumerate(samples[y]["files"])]
   runpool.map(makeplot, his[1:])


tot=0
for s in totevCount:
  tot+=totevSkim[s]

print tot, "input events" 
