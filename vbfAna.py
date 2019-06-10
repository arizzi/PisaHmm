from nail.nail import *
import ROOT
nthreads=60
import sys
import copy

from eventprocessing import flow
from histograms import histosPerSelection

snap=[] 
snaplist=["QJet0_eta","QJet1_eta","Mqq","Higgs_pt","twoJets","twoOppositeSignMuons","PreSel","VBFRegion","MassWindow","SignalRegion","qqDeltaEta","event","HLT_IsoMu24","QJet0_pt_nom","QJet1_pt_nom","QJet0_puId","QJet1_puId","SBClassifier","Higgs_m","Mqq_log","mmjj_pt_log","NSoft5","ll_zstar","theta2","mmjj_pz_logabs","MaxJetAbsEta","ll_zstar_log"]

from histobinning import binningrules
flow.binningRules = binningrules

flowData=copy.deepcopy(flow)
procData=flowData.CreateProcessor("eventProcessorData",snaplist,histosPerSelection,snap,"SignalRegion",nthreads)

#define some event weights
from weights import *
addDefaultWeights(flow)
addMuEffWeight(flow)

from systematics import *
addLheScale(flow)
addBtag(flow)
addMuScale(flow)
addCompleteJecs(flow)
addPUvariation(flow)

systematics=flow.variations #take all systematic variations
histosWithSystematics=flow.createSystematicBranches(systematics,histosPerSelection)

print "The following histograms will be created in the following regions"
for sel in  histosWithSystematics:
	print sel,":",histosWithSystematics[sel]
print >> sys.stderr, "Number of known columns", len(flow.validCols)

proc=flow.CreateProcessor("eventProcessor",snaplist,histosWithSystematics,snap,"SignalRegion",nthreads)


from samples2016 import samples as samples2016
from samples2017 import samples as samples2017
from samples2018 import samples as samples2018

year=sys.argv[1]
if year == "2016":
   samples=samples2016
if year == "2017":
   samples=samples2017
if year == "2018":
   samples=samples2018
 

from samplepreprocessing import flow as preflow
specificProcessors={}
for s in samples :
   if "filter" in samples[s].keys():
	print "Specific processor for" ,s
	specificProcessors[s]=preflow.CreateProcessor(s+"Processor",[samples[s]["filter"]],{samples[s]["filter"]:[samples[s]["filter"]]},[],samples[s]["filter"],nthreads)

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
     vf=ROOT.vector("string")()
     map(lambda x : vf.push_back(x), f)
     for x in vf:
	print x
     rdf=ROOT.RDataFrame("Events",vf)
     if rdf :
       try:
	 rdf=rdf.Define("year",year)
	 if s=="data" :
	   rdf=rdf.Define("isMC","false")
	   rdf=rdf.Define("Jet_pt_nom","Jet_pt")
	 else :
           if year == "2016":
               rdf=rdf.Define("Muon_sf","ROOT::VecOps::RVec<float>((20.1/36.4*Muon_ISO_SF + 16.3/36.4*Muon_ISO_eraGH_SF)*(20.1/36.4*Muon_ID_SF + 16.3/36.4*Muon_ID_eraGH_SF)*(20.1/36.4*Muon_Trigger_SF + 16.3/36.4*Muon_Trigger_eraGH_SF))")
               rdf=rdf.Define("btagWeight","btagWeight_CMVA")
           else :
               rdf=rdf.Define("Muon_sf","Muon_ISO_SF*Muon_ID_SF*Muon_Trigger_SF")
               rdf=rdf.Define("btagWeight","btagWeight_DeepCSVB")

	   rdf=rdf.Define("isMC","true")
	   if "LHEScaleWeight" not in list(rdf.GetColumnNames()):
	       print "ADDING FAKE LHE",f
	       rdf=rdf.Define("LHEScaleWeight","ROOT::VecOps::RVec<float>(9,1)")
	       rdf=rdf.Define("nLHEScaleWeight","uint32_t(0)")

	 if "filter" in samples[s] :
	   print "Prefiltering",s
           rdf=specificProcessors[s](rdf).rdf
	   rdf=rdf.Filter(samples[s]["filter"])

	 if s=="data":
   	    ou=procData(rdf)
	 else :
            ou=proc(rdf)
         #snaplist=["QJet0_pt","QJet1_pt","QJet0_eta","QJet1_eta","Mqq","Higgs_pt","twoJets","twoOppositeSignMuons","PreSel","VBFRegion","MassWindow","SignalRegion"]
         #branchList = ROOT.vector('string')()
	 #map(lambda x : branchList.push_back(x), snaplist)
         #ou.rdf.Filter("twoMuons","twoMuons").Filter("twoOppositeSignMuons","twoOppositeSignMuons").Filter("twoJets","twoJets").Filter("MassWindow","MassWindow").Filter("VBFRegion","VBFRegion").Filter("PreSel","PreSel").Filter("SignalRegion","SignalRegion").Snapshot("Events","out/%sSnapshot.root"%(s),branchList)
         #ou.rdf.Filter("event==24331988").Snapshot("Events","out/%sEventPick.root"%(s),branchList)
         print ou.histos.size()
         fff=ROOT.TFile.Open("out/%sHistos.root"%(s),"recreate")
         ROOT.gROOT.ProcessLine('''
     ROOT::EnableImplicitMT(%s);
     '''%nthreads)
         for h in ou.histos :
	    h.GetValue()
	    fff.cd()
 	    h.Write()
         fff.Write()
         fff.Close()
	 return 0
       except Exception, e: 
	 print e
	 print "FAIL",f
	 return 1
     else :
	print "Null file",f

#     return  os.system("./eventProcessor %s %s out/%s%s "%(4,f,s,i))  

from multiprocessing import Pool
runpool = Pool(20)

print samples.keys()
sams=samples.keys()

#sams=["DY2J","TTlep"]
#toproc=[(x,y,i) for y in sams for i,x in enumerate(samples[y]["files"])]
toproc=[ (s,samples[s]["files"]) for s in sams  ]
if len(sys.argv[2:]) :
   toproc=[ (s,samples[s]["files"]) for s in sams if s in sys.argv[2:]]
   
results=zip(runpool.map(f, toproc ),sams)
print results
print "To resubmit",[x[1] for x in results if x[0] ]
