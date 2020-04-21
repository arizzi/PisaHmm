import ROOT
ROOT.gStyle.SetOptStat(0)

_file0 = ROOT.TFile.Open("DNN18AtanNoMass___SideBand_PDFX0Down_TTlep_2018POWPY.root")
_file1 = ROOT.TFile.Open("DNN18AtanNoMass___SideBand_PDFX1Down_TTlep_2018POWPY.root")
_file2 = ROOT.TFile.Open("DNN18AtanNoMass___SideBand_PDFX2Down_TTlep_2018POWPY.root")
_file3 = ROOT.TFile.Open("DNN18AtanNoMass___SideBand_PDFX0Up_TTlep_2018POWPY.root")
_file4 = ROOT.TFile.Open("DNN18AtanNoMass___SideBand_PDFX1Up_TTlep_2018POWPY.root")
_file5 = ROOT.TFile.Open("DNN18AtanNoMass___SideBand_PDFX2Up_TTlep_2018POWPY.root")

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

c1 = ROOT.TCanvas()

_file0.Get("ratio1").SetMaximum(1.05)
_file0.Get("ratio1").SetMinimum(0.95)
_file0.Get("ratio1").Draw("HISTO,P")
for i in range(1,33):
    _file0.Get("ratio%d"%i).SetMarkerStyle(22)
    _file0.Get("ratio%d"%i).SetMarkerColor(colors[i%len(colors)])
    _file0.Get("ratio%d"%i).Draw("HISTO,P,same")

c1.Update()
for f in [_file0,_file1,_file2,_file3,_file4,_file5]:
    f.Get("funct").Draw("same")

c1.Update()

c1.SaveAs("c1.png")
c1.SaveAs("c1.C")
c1.SaveAs("c1.root")
