import ROOT
import array

#fil = ROOT.TFile.Open("outFSR_lowstat17noPUnew_18tofixPtNom/DY1J_2018AMCPYHistos.root")
#hName = "DNN18AtanNoMass___ZRegion__syst__LHEPdfHessian"
fil = ROOT.TFile.Open("/scratch/arizzi/hmmNail/nail/PisaHmm/outReferenceFeb12/DY105VBF_2017AMCPYHistos.root")
#fil = ROOT.TFile.Open("/scratch/arizzi/hmmNail/nail/PisaHmm/outReferenceFeb12/DY105_2018AMCPYHistos.root")
#fil = ROOT.TFile.Open("/scratch/arizzi/hmmNail/nail/PisaHmm/outReferenceFeb12/EWKZ105_2018MGPYHistos.root")
#fil = ROOT.TFile.Open("/scratch/arizzi/hmmNail/nail/PisaHmm/outReferenceFeb12/DY2J_2018AMCPYHistos.root")

hName = "DNN18AtanNoMass___SignalRegion__syst__LHEPdfReplica"
#hName = "DNN18AtanNoMass___SideBand__syst__LHEPdfHessian"
fil.cd()
histoNom = fil.Get("DNN18AtanNoMass___SignalRegion")
#histoNom = fil.Get(hName+"0")
#x1, x2 = 2.8400000, 3.0500000
#x1, x2 = 0., 1.
x1, x2 = 0.18166666666666667, 0.2066666666666667
#x1, x2 = 2.3866666666666667, 2.5833333333333335
bin1 = histoNom.FindBin(x1)
bin2 = histoNom.FindBin(x2)
#bin1 = histoNom.FindBin(0.)
#bin2 = histoNom.FindBin(1.)


colors = [
ROOT.kBlack,

ROOT.kYellow+1,
ROOT.kRed,
ROOT.kMagenta,
ROOT.kBlue,
ROOT.kCyan+1,
ROOT.kGreen+1,

ROOT.kOrange,
ROOT.kPink,
ROOT.kViolet,
ROOT.kAzure,
ROOT.kTeal,
ROOT.kSpring,

ROOT.kGray,
] 

colors = colors*10

bins = [0]

binVal = 0
for i in range(len(histoNom)):
    binVal += histoNom.GetBinContent(i)
    if binVal>1E-4:
        bins.append(histoNom.GetBinLowEdge(i))
        binVal = 0

bins.append(histoNom.GetBinLowEdge(i))
#bins = [1.*i/10 for i in range(0,40)]
#bins = [0, 0.38833333333333336, 0.67, 0.9966666666666667, 1.4583333333333335, 2.47, 5.0]
bins = [0 , 1.09 , 1.43333333333 , 1.72666666667 , 2.00333333333 , 2.21166666667 , 2.38 , 2.555 , 2.71833333333 , 2.885 , 3.095 , 3.34 , 5.0 ]
print bins


fil.cd()
histoNomReb = histoNom.Rebin(len(bins)-1, "aa", array.array('d',bins)).Clone("histoNomReb")

print fil.GetName(), x1, x2
#histo1 = ROOT.TH1F("histo1","",100,-0.03,0.03)
rat = []
sumSquared = 0
sum = 0.
histos=[]

ratio = histoNomReb.Clone("ratio")
ratio.Reset()
sums = [0]*len(ratio)
sumSquares = [0]*len(ratio)
i = 0 ## nominal is the first entry.
fil.cd()
hs = fil.Get(hName+"0").Clone(hName+"0")
print fil.ls(hName+"0")
print hs
print hs.GetMaximum()
print hs.GetName()
hs = hs.Rebin(len(bins)-1, "aa", array.array('d',bins))
hs0= hs
c2 = ROOT.TCanvas("c2")
ROOT.gStyle.SetOptStat(0)
c2.SetGridx()
c2.SetGridy()
histoNomReb.SetLineColor(ROOT.kBlack)
histoNomReb.SetLineWidth(2)
#histoNomReb.Draw()
j=0
ratioN = {} 
funct = ROOT.TF1("funct","[0]+[1]*x*x",0, 5)
funct.SetParameters(1, 0)
fitN = {} 
while hs and hs.GetMaximum()>0:
    print "hs,",hs.GetNbinsX()
    hs = hs.Rebin(len(bins)-1, "aa", array.array('d',bins))
    print "hs,",hs.GetNbinsX()
    ratioN[j] = hs.Clone("rat%d"%j)
    ratioN[j].SetTitle("Fit of PDF variations")
    print ratioN[j].GetNbinsX()
    print histoNomReb.GetNbinsX()
    print hs.GetNbinsX()
    ratioN[j].Divide(hs,hs0)
    #ratioN[j].Divide(hs,histoNomReb)
    color = colors[j]
    ratioN[j].SetMarkerStyle(20)
    ratioN[j].SetLineColor(color)
    ratioN[j].SetMarkerColor(color)
    ratioN[j].GetYaxis().SetRangeUser(0.98, 1.02)
    if j==0:
        ratioN[j].Draw("P, HIST")
    else:
        ratioN[j].Draw("P, same, HIST")
    fitN[j] = funct.Clone("fit%d"%j)
    fitN[j].SetLineColor(color)
    ratioN[j].Fit( fitN[j] )
    fitN[j].Draw("same")
#    input()
    print hs.GetName(), hs.GetMaximum()
    for bin_ in range(len(ratio)):
        rat =  hs.GetBinContent(bin_)/hs0.GetBinContent(bin_) if hs0.GetBinContent(bin_)>0 else 0. 
        sums[bin_] += rat
        sumSquares[bin_] += rat**2
        binVal = 0
        for i in range(len(histoNom)):
            binVal += histoNom.GetBinContent(i)
            if binVal>1E-4:
#                bins.append(histoNom.GetBinLowEdge(i))
                binVal = 0
    j = j + 1
    hs = fil.Get(hName+str(j))

meanrms=0.
ngood=0
for bin_ in range(len(ratio)):
    if sumSquares[bin_]>0:
        rms = (sumSquares[bin_]/i - (sums[bin_]/i)**2)**0.5 
#        rms = rms*(i**0.5)
        meanrms+=rms	
        ngood+=1
    else:
        rms = 10. ## large error if no MC stat
    ratio.SetBinContent(bin_, 0.)
    ratio.SetBinError(bin_, rms)

c2.SaveAs("plot1.root")
c1 = ROOT.TCanvas("c1")
ratio.SetMaximum(+0.01)
ratio.SetMinimum(-0.01)
ratio.Draw()
c1.SaveAs("sumSquares_DY105_rebinned.png")

print "StdDev",(sumSquared/i - (sum/i)**2)**0.5 

print "StdDev",(sumSquared/i - (sum/i)**2)**0.5 

print "StdDev * SQRT(N)",(sumSquared/i - (sum/i)**2)**0.5 * i**0.5

#histo1.Draw()

#
