import ROOT
#import samples2018
from samples2016 import samples as samples2016
from samples2017 import samples as samples2017
from samples2018 import samples as samples2018
import sys

def totevents(fn):
    totev=1e-9
    totevCount=1e-9
    totevSkim=1e-9
    
    print "fn ", fn
    f=ROOT.TFile.Open(fn)
    run=f.Get("Runs")
    totevSkim+=f.Get("Events").GetEntries()
    if run :
        hw=ROOT.TH1F("hw","", 5,0,5)
        run.Project("hw","1","genEventSumw")
        totev+=hw.GetSumOfWeights()
        run.Project("hw","1","genEventCount")
        totevCount+=hw.GetSumOfWeights()
        print "totev   ", totev

    return totev


def FindBinDown(hBackground, hSignal, binLimitUp, minNumberOfEventPerBin, MinNumberOfBin_inBinning) :
        
    binLimitDown = 0.
    for n in range(binLimitUp-MinNumberOfBin_inBinning-1, 0, -1) :
        error_B = ROOT.Double(0)
        error_S = ROOT.Double(0)
        integral_B = hBackground.IntegralAndError(n+1, binLimitUp, error_B)
        integral_S = hSignal.IntegralAndError(n+1, binLimitUp, error_S)
        
        integral = integral_S + integral_B
        error2 = error_B*error_B + error_S*error_S
        

        if integral_S >=  minNumberOfEventPerBin :
            binLimitDown = n
            break

    return binLimitDown




variable = "DNNAtan"
year = sys.argv[1]

if year == "2016" :
   samples=samples2016
if year == "2017" :
   samples=samples2017
if year == "2018" :
   samples=samples2018
   
   
signalSample = "vbfHmm_"+year+"POWPY"


fSignal     =ROOT.TFile.Open("out/"+signalSample+"Histos.root")
fBackground =ROOT.TFile.Open("out/"+signalSample+"Histos.root")


hSignal     = fSignal.Get(variable+"___SignalRegion").Clone()
hBackground = fBackground.Get(variable+"___SignalRegion").Clone()



minNumberOfEventPerBin = 0.3
xMax=2.
binning_BDT=[xMax]

binMinWidth = 0.01
Nbins_binning = hSignal.GetNbinsX()
MinNumberOfBin_inBinning = int(binMinWidth/xMax*Nbins_binning)
binLimitDown = Nbins_binning


hSignal.Scale(samples[signalSample]["xsec"]*samples["data"+year]["lumi"]/totevents("/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim"+year+"_Z/VBF_HToMuMu_nano"+year+".root"))
print "Total number of events:  ", hSignal.Integral(0, Nbins_binning+1)
        
while binLimitDown>0 :
            binning_BDT.append((1.*binLimitDown*xMax)/Nbins_binning)
            binLimitUp = binLimitDown
            binLimitDown        = FindBinDown(hBackground, hSignal, binLimitUp, minNumberOfEventPerBin, MinNumberOfBin_inBinning)


print "    "+variable+" : [0",
for n in range(len(binning_BDT)-1, 0, -1) : 
    print  ",", binning_BDT[n],
        
print "]"      

