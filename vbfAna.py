from nail.nail import *
import ROOT
import traceback
nthreads=50
nprocesses=5
import sys
import copy
ROOT.gROOT.ProcessLine(".x softactivity.h")

ROOT.gInterpreter.AddIncludePath("/scratch/lgiannini/HmmPisa/lwtnn/include/lwtnn") 
ROOT.gSystem.Load("/scratch/lgiannini/HmmPisa/lwtnn/build/lib/liblwtnn.so")

from eventprocessing import getFlow
year=sys.argv[1]
flow=getFlow(year)

from histograms import histosPerSelection,histosPerSelectionFullJecs


def sumwsents(files):
   sumws=1e-9
   LHEPdfSumw=[]
   for fn in files:
	  f=ROOT.TFile.Open(fn)
	  run=f.Get("Runs")
	  hasUnderscore = ("genEventSumw_" in [x.GetName() for x in run.GetListOfBranches()])
	  if run :
		 hw=ROOT.TH1F("hw","", 5,0,5)
		 if hasUnderscore: run.Project("hw","1","genEventSumw_")
		 else : run.Project("hw","1","genEventSumw")
                 sumws+=hw.GetSumOfWeights()
                 run.GetEvent()
                 nLHEScaleSumw = 0
                 if hasUnderscore: nLHEScaleSumw = run.nLHEPdfSumw_
                 else : nLHEScaleSumw = run.nLHEPdfSumw
                 for i in range(nLHEScaleSumw):
                        if hasUnderscore: run.Project("hw","1","LHEPdfSumw_[%d]"%i)
                        else : run.Project("hw","1","LHEPdfSumw[%d]"%i)
                        if i<len(LHEPdfSumw):
                                LHEPdfSumw[i] = LHEPdfSumw[i] + hw.GetSumOfWeights()
                        else:
                                LHEPdfSumw.append(hw.GetSumOfWeights())
   if sumws < 1: sumws = 1
   return sumws, LHEPdfSumw

def isHessianPdf(LHAdown): ##Run checkLHAPdf.py and see https://lhapdf.hepforge.org/pdfsets 
    for i in [303000, 303200, 304200, 304400, 304600, 304800, 305800, 306000, 306200, 306400, 91400]:
            if LHAdown==i or LHAdown==i+1: return True
    return False

used=[]
for s in histosPerSelection:
    used.append(s)
    used.extend(histosPerSelection[s])
used=list(set(used))

ftxt=open("out/description.txt","w")
ftxt.write(flow.Describe(used))

snap=[] 
snaplist=["Mu0_charge","Mu1_charge","Mu0_dxybs","Mu1_dxybs","event","Higgs_m_uncalib","nJet","Higgs_m","QJet0_qgl","QJet1_qgl","QJet0_eta","QJet1_eta","Mqq","Higgs_pt","Mu0_pt","Mu0_corrected_pt","Mu1_corrected_pt","Mu1_pt","Mu0_eta","Mu1_eta","Mu1_phi","Mu0_phi","nGenPart","GenPart_pdgId","GenPart_eta","GenPart_phi","GenPart_pt"]#,"twoJets","twoOppositeSignMuons","PreSel","VBFRegion","MassWindow","SignalRegion","qqDeltaEta","event","HLT_IsoMu24","QJet0_pt_nom","QJet1_pt_nom","QJet0_puId","QJet1_puId","SBClassifier","Higgs_m","Mqq_log","mmjj_pt_log","NSoft5","ll_zstar","theta2","mmjj_pz_logabs","MaxJetAbsEta","ll_zstar_log"]#,"QJet0_prefireWeight","QJet1_prefireWeight","PrefiringCorrection","CorrectedPrefiringWeight"]
#snaplist=["QJet0_prefireWeight","QJet1_prefireWeight","PrefiringCorrection","CorrectedPrefiringWeight"]
snaplist=[]# "event"]
fullsnaplist=["Mu0_charge","Mu1_charge","Mu0_dxybs","Mu1_dxybs","Mu0_pt_GeoFitCorrection","Mu1_pt_GeoFitCorrection","Mu0_eta","Mu0_pt","Mu1_eta","Mu1_pt",
    "Higgs_pt", "Higgs_eta", "Higgs_mRelReso", "Higgs_mReso", "Higgs_m", "ll_zstar_log", "ll_zstar",
    "QJet0_pt_touse", "QJet0_phi", "QJet0_eta", "QJet0_pt_nom", "QJet0_puId", "QJet0_qgl",
    "QJet1_pt_touse", "QJet1_phi", "QJet1_eta", "QJet1_pt_nom", "QJet1_puId", "QJet1_qgl",
    "qqDeltaEta", "qqDeltaPhi", "qq_pt", "Mqq", "Mqq_log", "MaxJetAbsEta", "mmjj_pt", "mmjj_pt_log", "mmjj_pz", "mmjj_pz_logabs", "CS_theta", "CS_phi","NSoft5NewNoRapClean", "SAHT2","nGenPart","GenPart_pdgId","GenPart_eta","GenPart_phi","GenPart_pt", "nLHEPart", "LHEPart_pt", "LHEPart_eta", "LHEPart_phi",  "LHEPart_pdgId", 
    "DeltaRelQQ", "DeltaEtaQQSum", "PhiHQ1", "PhiHQ2", "EtaHQ1", "EtaHQ2", "minEtaHQ", "Rpt", "theta2", "NSoft5", "NSoft5New", "SAHT",
    "SBClassifier", "DNN18Atan","year",
     #"genWeight","puWeight","btagWeight","muEffWeight","EWKreweight", "QGLweight"
]

from histobinning import binningrules
flow.binningRules = binningrules

flowData=copy.deepcopy(flow)
flowData.CentralWeight("weightDNNSB",["SignalRegionDNNWeighted","SRplusSBDNNWeighted"])
procData=flowData.CreateProcessor("eventProcessorData"+year,snaplist+["QGLweight"],histosPerSelection,snap,"SignalRegion",nthreads)
#procData=flowData.CreateProcessor("eventProcessorData"+year,snaplist,histosPerSelection,snap,"SignalRegion",nthreads)

print "Data processor created"

#define some event weights
from weights import *
addDefaultWeights(flow)
addMuEffWeight(flow)
addQGLweight(flow)
addPreFiring(flow)
flow.CentralWeight("weightDNNSB",["SignalRegionDNNWeighted","SRplusSBDNNWeighted"])

from systematics import *
if True : #switch off all systs
 addLheScale(flow)
 addPSWeights(flow)
 addBtag(flow)
 addBasicJecs(flow)
 addMuScale(flow)
 addPUvariation(flow)
 addReweightEWK(flow)
 addQGLvariation(flow)
 addPreFiringVariation(flow)


#snaplist+=["genWeight","puWeight","btagWeight","muEffWeight","EWKreweight", "PrefiringWeight", "QGLweight","QJet1_partonFlavour","QJet0_partonFlavour"]
systematics=flow.variations #take all systematic variations
print "Systematics for all plots", systematics
histosWithSystematics=flow.createSystematicBranches(systematics,histosPerSelection)
#addPtEtaJecs(flow)

if True:
 addSTXS(flow)
 addLhePdf(flow)
 addDecorrelatedJER(flow)
 addCompleteJecs(flow,year)
print "######### full systematics #######"
histosWithFullJecs=flow.createSystematicBranches(systematics,histosPerSelectionFullJecs)

for region in histosWithFullJecs:
   if region not in histosWithSystematics :
	histosWithSystematics[region]=histosWithFullJecs[region]
   else:
	histosWithSystematics[region]=list(set(histosWithSystematics[region]+histosWithFullJecs[region]))

print "The following histograms will be created in the following regions"
for sel in  histosWithSystematics:
	print sel,":",histosWithSystematics[sel]
print >> sys.stderr, "Number of known columns", len(flow.validCols)

proc=flow.CreateProcessor("eventProcessor"+year,snaplist,histosWithSystematics,snap,"",nthreads)
#proc=None


from samples2016 import samples as samples2016
from samples2017 import samples as samples2017
from samples2018 import samples as samples2018

if year == "2016":
   samples=samples2016
   trigger="HLT_IsoMu24 || HLT_IsoTkMu24"
if year == "2017":
   samples=samples2017
   trigger="HLT_IsoMu27"
if year == "2018":
   samples=samples2018
   trigger="HLT_IsoMu24"
 

from samplepreprocessing import flow as preflow
specificPreProcessors={}
specificPostProcessors={}
for s in samples :
   if "filter" in samples[s].keys():
	print "Specific pre processor for" ,s
	specificPreProcessors[s]=preflow.CreateProcessor(s+"Processor",[samples[s]["filter"]],{samples[s]["filter"]:[samples[s]["filter"]]},[],samples[s]["filter"],nthreads)
   if "postproc" in samples[s].keys():
       print "Specific post processor for" ,s
       flowSpec=copy.deepcopy(flow)
       specificPostProcessors[s]=samples[s]["postproc"](flowSpec,proc.produces,histosWithSystematics,snaplist,snap,nthreads)

	
import psutil
def f(ar):
#f,s,i=ar
     p = psutil.Process()
     print "Affinity",p.cpu_affinity()
     p.cpu_affinity( list(range(psutil.cpu_count())))
     ROOT.gROOT.ProcessLine('''
     ROOT::EnableImplicitMT(%s);
     '''%nthreads)
     s,f=ar
     print f
     if not "lumi" in samples[s].keys()  :
        sumws, LHEPdfSumw = sumwsents(f)
     else:
        sumws, LHEPdfSumw = 1., []
     rf=ROOT.TFile.Open(f[0])
     ev=rf.Get("Events")
     hessian=False
     PdfLHA_up, PdfLHA_down = 0, 0
     if ev :
	 br = ev.GetBranch("LHEPdfWeight")
         if br:
                 brTitle = br.GetTitle()
                 if "LHA IDs" in brTitle:
                    PdfLHA_down, PdfLHA_up = brTitle.split("LHA IDs ")[-1].split("-")
                    PdfLHA_down, PdfLHA_up = int(PdfLHA_down), int(PdfLHA_up)
                 if isHessianPdf(PdfLHA_down):
                    print "Sample",s,"has Hessian PDF"
                    hessian = True

     vf=ROOT.vector("string")()
     map(lambda x : vf.push_back(x), f)
     for x in vf:
	print x
     import jsonreader 
     rdf=ROOT.RDataFrame("Events",vf) #.Range(10000)
     if rdf :
       try:
	 rdf=rdf.Define("year",year)
	 rdf=rdf.Define("TriggerSel",trigger)
	 if  year!="2017" and ("Jet_puId17" not in list(rdf.GetColumnNames())):
		rdf=rdf.Define("Jet_puId17","ROOT::VecOps::RVec<int>(nJet, 0)")
	 if "lumi" in samples[s].keys()  :
#	   if "Muon_dxybs" not  in  list(rdf.GetColumnNames()) :
#               rdf=rdf.Define("Muon_dxybs","Muon_pt*10000.f")
#	       print "WWWWWWWWWWAAAAAAAAAAAAAARRRRRRRNINGGGGGGGGGG"
	   rdf=rdf.Filter("passJson(run,luminosityBlock)","jsonFilter")
	   rdf=rdf.Define("isMC","false")
#	   rdf=rdf.Define("PrefireWeight","1.0f")
	   rdf=rdf.Define("isHerwig","false")
	   if year != "2018": 
		rdf=rdf.Define("Jet_pt_nom","Jet_pt")
	   else :
		rdf=rdf.Define("Jet_pt_newJEC","Jet_pt") 
	   rdf=rdf.Define("LHE_NpNLO","0")
	   rdf=rdf.Define("Jet_partonFlavour","ROOT::VecOps::RVec<int>(nJet, 0)")
	 else :
	   if year == "2018" :
		  rdf=rdf.Define("PrefiringWeight","1.f")
		  rdf=rdf.Define("PrefiringWeightUp","1.f")
		  rdf=rdf.Define("PrefiringWeightDown","1.f")
	   else: 
		  rdf=rdf.Define("PrefiringWeight","L1PreFiringWeight_Nom")
		  rdf=rdf.Define("PrefiringWeightUp","L1PreFiringWeight_Up")
		  rdf=rdf.Define("PrefiringWeightDown","L1PreFiringWeight_Dn")
	   print "Is herwig?",("true" if "HERWIG" in s else "false"), s
	   rdf=rdf.Define("isHerwig",("true" if "HERWIG" in s else "false"))
	   if  "HTXS_stage1_1_fine_cat_pTjet30GeV" not in list(rdf.GetColumnNames()) :
	       print "Add fake STXS category"
               rdf=rdf.Define("HTXS_stage1_1_fine_cat_pTjet30GeV","-1l")
	       print "Added"
	   if  "ggH" in s :
               print "Adding ggH weights"
               rdf=rdf.Define("nnlopsWeight","evalNnlopsWeight(HTXS_njets30,HTXS_Higgs_pt)")
           else :
               rdf=rdf.Define("nnlopsWeight","1.f")

	   if  s in  ["DY0J_2018AMCPY","DY0J_2017AMCPY","DY1J_2017AMCPY","DY1J_2018AMCPY"] :
	       rdf=rdf.Define("lhefactor","2.f") 
	   else:
	       rdf=rdf.Define("lhefactor","1.f") 
	   if "LHEPdfWeight" not in list(rdf.GetColumnNames()):
	       print "ADDING FAKE PDF",f
	       rdf=rdf.Define("LHEPdfWeight","ROOT::VecOps::RVec<float>(1,1)")
	       rdf=rdf.Define("nLHEPdfWeight","uint32_t(1)")
	   if hessian:
	       print "Setting LHEPdfHasHessian to true"
	       rdf=rdf.Define("LHEPdfHasHessian","true")
	   else:
	       print "Setting LHEPdfHasHessian to false"
	       rdf=rdf.Define("LHEPdfHasHessian","false")
           if year == "2016":
               rdf=rdf.Define("Muon_sf","(20.1f/36.4f*Muon_ISO_SF + 16.3f/36.4f*Muon_ISO_eraGH_SF)*(20.1f/36.4f*Muon_ID_SF + 16.3f/36.4f*Muon_ID_eraGH_SF)")
           else :
               rdf=rdf.Define("Muon_sf","Muon_ISO_SF*Muon_ID_SF")
	   if "btagWeight_DeepCSVB" in  list(rdf.GetColumnNames()) :
               rdf=rdf.Define("btagWeight","btagWeight_DeepCSVB")
	   else :
               rdf=rdf.Define("btagWeight","btagWeight_CMVA")

	   if "Muon_dxybs" not  in  list(rdf.GetColumnNames()) :
               rdf=rdf.Define("Muon_dxybs","Muon_pt*10000.f")
	
	   rdf=rdf.Define("isMC","true")
	   if "LHEWeight_originalXWGTUP" not in list(rdf.GetColumnNames()):
	       rdf=rdf.Define("LHEWeight_originalXWGTUP","genWeight")
	   if "LHEScaleWeight" not in list(rdf.GetColumnNames()):
	       print "ADDING FAKE LHE",f
	       rdf=rdf.Define("LHEScaleWeight","ROOT::VecOps::RVec<float>(9,1)")
	       rdf=rdf.Define("nLHEScaleWeight","uint32_t(0)")
	   if "PSWeight" not in list(rdf.GetColumnNames()):
	       print "ADDING FAKE PS WEIGHT",f
	       rdf=rdf.Define("PSWeight","ROOT::VecOps::RVec<float>(9,1)")
	       rdf=rdf.Define("nPSWeight","uint32_t(1)")
	   if "LHE_NpNLO" not in list(rdf.GetColumnNames()):
	       rdf=rdf.Define("LHE_NpNLO","-1")

	 if s.startswith("EWKZ_") and s.endswith("MGPY") : 
             #rdf=rdf.Define("EWKreweight","weightSofAct5(1)")
             rdf=rdf.Define("EWKreweight","weightGenJet(nGenJet)")
         else :
             rdf=rdf.Define("EWKreweight","1.f")
	 
	 if "filter" in samples[s] :
           ou=specificPreProcessors[s](rdf)
           print "res fetched"
           rdf=ou.rdf[""]
           rdf=rdf.Filter(samples[s]["filter"])

	 if "lumi" in samples[s].keys() :
   	    ou=procData(rdf)
	 else :
            ou=proc(rdf)
	 ouspec=None
         if s in specificPostProcessors.keys():
	    print "adding postproc",s
	    ouspec=specificPostProcessors[s](ou.rdf[""])
	    print "added"

         normalizationHandle = ou.rdf[""].Filter("twoJets","twoJets").Mean("QGLweight")
         normalizationHandleSR = ou.rdf["SignalRegion"].Mean("QGLweight")
         normalizationHandleSB = ou.rdf["SideBand"].Mean("QGLweight")
	 #Event loop should not be triggered anove this point

         #snaplist=["nJet","nGenJet","Jet_pt_touse","GenJet_pt","Jet_genJetIdx","Jet_pt_touse","Jet_pt","Jet_pt_nom","Jet_genPt","LHERenUp","LHERenDown","LHEFacUp","LHEFacDown","PrefiringWeight","DNN18Atan","QJet0_prefireWeight","QJet1_prefireWeight", "QJet0_pt_touse","QJet1_pt_touse","QJet0_eta","QJet1_eta","QGLweight","genWeight","btagWeight","muEffWeight"]
#"QJet0_pt_touse","QJet1_pt_touse","QJet0_eta","QJet1_eta","Mqq","Higgs_pt","twoJets","twoOppositeSignMuons","PreSel","VBFRegion","MassWindow","SignalRegion"]

 #        snaplist=["nJet","SelectedJet_pt_touse","Jet_pt","Jet_pt_nom","Jet_puId","Jet_eta","Jet_jetId","PreSel","VBFRegion","MassWindow","SignalRegion","jetIdx1","jetIdx2","Jet_muonIdx1","Jet_muonIdx2","LHEPdfUp","LHEPdfDown","LHEPdfSquaredSum","LHEPdfRMS","nLHEPdfWeight","LHEPdfWeight","PrefiringWeight","DNN18Atan__syst__MuScaleDown","Higgs_eta__syst__MuScaleUp","Higgs_mRelReso__syst__MuScaleUp","Higgs_mReso__syst__MuScaleUp","Higgs_m__syst__MuScaleUp","Higgs_pt__syst__MuScaleUp","Mqq","Mqq_log","NSoft5__syst__MuScaleUp","QJet0_eta","QJet0_phi","QJet0_pt_touse","QJet0_qgl","QJet1_eta","QJet1_phi","QJet1_pt_touse","QJet1_qgl","Rpt__syst__MuScaleUp","event","ll_zstar__syst__MuScaleUp","minEtaHQ__syst__MuScaleUp","qqDeltaEta"]
	 snaplist=["run","event","Higgs_m","QJet0_pt_touse","QJet1_pt_touse","QJet0_eta","QJet1_eta","Mqq","Higgs_pt","Higgs_m","qqDeltaEta","SelectedMuon_GFp4_pt0","SelectedMuon_GFp4_pt1","SignalRegionWeight__Central","QGLweight","DNN18Atan"]
         branchList = ROOT.vector('string')()
	 map(lambda x : branchList.push_back(x), snaplist)
 #        if "lumi" not in samples[s].keys()  :
 #        rep=ou.rdf[""].Filter("twoMuons","twoMuons").Filter("twoOppositeSignMuons","twoOppositeSignMuons").Filter("twoJets","twoJets").Filter("MassWindow","MassWindow").Filter("VBFRegion","VBFRegion").Filter("PreSel","PreSel").Filter("SignalRegion","ZRegion").Report() 
#	 rep.Print()
	 print "Above the cutflow for",s
#         ou.rdf["SignalRegion"].Define("SelectedMuon_GFp4_pt0","SelectedMuon_GFp4[0].Pt()").Define("SelectedMuon_GFp4_pt1","SelectedMuon_GFp4[1].Pt()").Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
          
         if "training" in samples[s].keys() and samples[s]["training"] : 
             #ou.rdf.Filter("twoMuons","twoMuons").Filter("twoOppositeSignMuons","twoOppositeSignMuons").Filter("twoJets","twoJets").Filter("MassWindow","MassWindow").Filter("VBFRegion","VBFRegion").Filter("PreSel","PreSel").Filter("SignalRegion","SignalRegion").Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
           #ou.rdf["ZRegion"].Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
           ou.rdf["PreSel"].Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
#         if "lumi" in samples[s].keys()  :
               #u.rdf["SignalRegion"].Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
#               ou.rdf["SignalRegion"].Define("Mu0_GFpt","Mu0_GFp4.pt()").Define("Mu1_GFpt","Mu1_GFp4.pt()").Snapshot("Events","out/%sSnapshot.root"%(s),branchList)


#         ou.rdf.Filter("twoJets","twoJets").Filter("VBFRegion","VBFRegion").Filter("twoMuons__syst__MuScaleDown","twoMuons__syst__MuScaleDown").Filter("twoOppositeSignMuons__syst__MuScaleDown","twoOppositeSignMuons__syst__MuScaleDown").Filter("PreSel__syst__MuScaleDown","PreSel__syst__MuScaleDown").Filter("MassWindow__syst__MuScaleDown","MassWindow__syst__MuScaleDown").Filter("SignalRegion__syst__MuScaleDown","SignalRegion__syst__MuScaleDown").Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
         #ou.rdf.Filter("event==63262831 || event == 11701422 || event== 60161978").Snapshot("Events","out/%sEventPick.root"%(s),branchList)
#	 return 1
#         print ou.histos.size()#,ouspec.histos.size()
         fff=ROOT.TFile.Open("out/%sHistos.root"%(s),"recreate")
         ROOT.gROOT.ProcessLine('''
     ROOT::EnableImplicitMT(%s);
     '''%nthreads)
         

	 normalization=normalizationHandle.GetValue()#1./(ou.rdf.Filter("twoJets","twoJets").Mean("QGLweight").GetValue())
	 normalizationSB=normalizationHandleSB.GetValue()#1./(ou.rdf.Filter("twoJets","twoJets").Mean("QGLweight").GetValue())
	 normalizationSR=normalizationHandleSR.GetValue()#1./(ou.rdf.Filter("twoJets","twoJets").Mean("QGLweight").GetValue())
	 print "Normalization = ", normalization, normalizationSB, normalizationSR, s 
	 ffftxt=open("out/%s.txt"%s,"w")
	 ffftxt.write("Normalization = %s %s %s %s \n"%( normalization, normalizationSB, normalizationSR, s))
	 ffftxt.close()
	 print "Normalization = ", normalization, normalizationSB, normalizationSR, s 
	 if normalization == 0:
	    normalization =1.
	    normalizationSR =1.
	    normalizationSB =1.
	 if ouspec is not None :
	    print "Postproc hisots"
            for h in ouspec.histos :
                hname = h.GetName()
		nor=normalization
		if "SignalRegion" in hname:
			nor=normalizationSR
		if "SideBand" in hname:
			nor=normalizationSB
                h.GetValue()
                fff.cd()
                h.Scale(1./nor/sumws)
                if "__syst__LHEPdf" in hname:
                    if h.GetMaximum()==0.: continue ## skip empty LHEPdf
                    PdfIdx = hname.split("__syst__LHEPdf")[-1]
                    if PdfIdx.isdigit():
                            if hessian: h.SetName(hname.replace("__syst__LHEPdf","__syst__LHEPdfHessian"))
                            else:     h.SetName(hname.replace("__syst__LHEPdf","__syst__LHEPdfReplica"))
                h.Write()
         for h in  ou.histos :  
            hname = h.GetName()
	    nor=normalization
	    if "SignalRegion" in hname:
	 	nor=normalizationSR
	    if "SideBand" in hname:
		nor=normalizationSB
            h.GetValue()
            fff.cd()
            h.Scale(1./nor/sumws)
            if "__syst__LHEPdf" in hname:
                if h.GetMaximum()==0.: continue ## skip empty LHEPdf
                PdfIdx = hname.split("__syst__LHEPdf")[-1]
                if PdfIdx.isdigit():
                        if hessian: h.SetName(hname.replace("__syst__LHEPdf","__syst__LHEPdfHessian"))
                        else:     h.SetName(hname.replace("__syst__LHEPdf","__syst__LHEPdfReplica"))
            h.Write()
	 
         sumWeights = getattr(ROOT,"TParameter<double>")("sumWeights", sumws)
         sumWeights.Write()
         if not "lumi" in samples[s].keys() and PdfLHA_up:
                 LHApdf_down =  getattr(ROOT,"TParameter<int>")("LHApdf_down", PdfLHA_down)
                 LHApdf_down.Write()
                 LHApdf_up   =  getattr(ROOT,"TParameter<int>")("LHApdf_up",   PdfLHA_up)
                 LHApdf_up.Write()
                 sumWeightPDF = {}
                 for i in range(len(LHEPdfSumw)):
                         sumWeightPDF[i] = getattr(ROOT,"TParameter<double>")("sumWeightsPDF%d"%i, sumws*LHEPdfSumw[i])
                         sumWeightPDF[i].Write()
         fff.Write()
         fff.Close()
	 return 0
       except Exception, e: 
	 print e
	 traceback.print_exc()
	 print "FAIL",f
	 return 1
     else :
	print "Null file",f

#     return  os.system("./eventProcessor %s %s out/%s%s "%(4,f,s,i))  

#from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import Pool
runpool = Pool(nprocesses)

print samples.keys()
sams=samples.keys()

#sams=["DY2J","TTlep"]
#toproc=[(x,y,i) for y in sams for i,x in enumerate(samples[y]["files"])]
toproc=[ (s,samples[s]["files"]) for s in sams  if os.path.exists(samples[s]["files"][0])]
toproc=sorted(toproc,key=lambda x : sum(map( lambda x : ( os.path.getsize(x) if os.path.exists(x) else 0 ),x[1])),reverse=True)
print toproc

if len(sys.argv[2:]) :
   if sys.argv[2] == "fix" :
       toproc=[]
       sss=sams
       if(len(sys.argv[3:])) :
          sss=[s for s in sams if s in sys.argv[3:]]
	  print "fixing",sss
       for s in sss :
	if os.path.exists(samples[s]["files"][0]) :
	 try:
	   ff=ROOT.TFile.Open("out/%sHistos.root"%s)
	   if ff.IsZombie() or len(ff.GetListOfKeys()) == 0:
	           print "zombie or zero keys",s
	           toproc.append((s,samples[s]["files"]))
	 
	 except:
	   print "failed",s
	   toproc.append((s,samples[s]["files"]))
   else:
      if sys.argv[2][:5]=="model":
	import importlib
	model=importlib.import_module(sys.argv[2])
#	samples=model.samples
	allmc= [y for x in model.background for y in model.background[x]]+[y for x in model.signal for y in model.signal[x]]
	alldata= [y for x in model.data for y in model.data[x]]
        for x in allmc :
          print x,"\t",samples[x]["xsec"]
        for x in alldata :
          print x,"\t",samples[x]["lumi"]

        toproc=[ (s,samples[s]["files"]) for s in sams if s in allmc+alldata+sys.argv[3:]]
	
      else:
          toproc=[ (s,samples[s]["files"]) for s in sams if s in sys.argv[2:]]

print "Will process", toproc
   
if nprocesses>1:
        results=zip(runpool.map(f, toproc ),[x[0] for x in toproc])
else:
        results=zip([f(x) for x in toproc] ,[x[0] for x in toproc])

print "Results",results
print "To resubmit",[x[1] for x in results if x[0] ]
