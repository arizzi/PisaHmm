import ROOT
#import samples2018
from samples2016 import samples as samples2016
from samples2017 import samples as samples2017
from samples2018 import samples as samples2018
import sys

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




year = sys.argv[1]
variable = sys.argv[2]

if year == "2016" :
   samples=samples2016
if year == "2017" :
   samples=samples2017
if year == "2018" :
   samples=samples2018
   
   
signalSample = "vbfHmm_"+year+"POWPYDIPOLE"
#signalSample = "vbfHmm_"+year+"AMCPY"


fSignal     =ROOT.TFile.Open("outROCCNoRetrain/"+signalSample+"Histos.root")
fBackground =ROOT.TFile.Open("outROCCNoRetrain/"+signalSample+"Histos.root")


hSignal     = fSignal.Get(variable+"___SignalRegion").Clone()
hBackground = fBackground.Get(variable+"___SignalRegion").Clone()


xMax=5.
binMinWidth = 0.01
Nbins_binning = hSignal.GetNbinsX()
MinNumberOfBin_inBinning = int(binMinWidth/xMax*Nbins_binning)
binLimitDown = Nbins_binning

minNumberOfEventPerBin = 0.6
hSignal.Scale(samples[signalSample]["xsec"]*samples["data"+year]["lumi"])
tot=hSignal.Integral(0, Nbins_binning+1)
N=13 #tot*2
print "Total number of events:  ", tot
delta=2.*(tot-minNumberOfEventPerBin*N)/N**2
print "min size",minNumberOfEventPerBin, "step",delta, "N",N,"tot",tot


#delta=0
#minNumberOfEventPerBin=0.6

binning_BDT=[xMax]


        
while binLimitDown>0 :
            binning_BDT.append((1.*binLimitDown*xMax)/Nbins_binning)
            binLimitUp = binLimitDown
            binLimitDown        = FindBinDown(hBackground, hSignal, binLimitUp, minNumberOfEventPerBin, MinNumberOfBin_inBinning)
	    minNumberOfEventPerBin+=delta

print "    \'"+variable+"\' : [0",
for n in range(len(binning_BDT)-1, 0, -1) : 
    print  ",", binning_BDT[n],
        
print "]"     
print len(binning_BDT) 

