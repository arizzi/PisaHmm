from nail.nail import *
import ROOT
import sys

def getFlow(year):
	FSR=True
	FSRnew=False
	FSRnew=True
	#flow=SampleProcessing("VBF Hmumu Analysis","/scratch/arizzi/Hmm/nail/samples/6B8A2AC8-35E6-1146-B8A8-B1BA90E3F3AA.root")
	if FSR :
	    if FSRnew :
	       flow=SampleProcessing("VBF Hmumu Analysis","/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_12_0/vbfHmm_"+year+"AMCPY.root")
	    else:
	       flow=SampleProcessing("VBF Hmumu Analysis","/scratchssd/mandorli/Hmumu/fileSkim2016_FSR/VBF_HToMuMu_nano2016.root")
	else:
	    flow=SampleProcessing("VBF Hmumu Analysis","/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_nanoV5/VBF_HToMuMu_nano2016.root")
	#flow=SampleProcessing("VBF Hmumu Analysis","/scratch/arizzi/hmmNail/crab/CMSSW_9_4_6/src/PhysicsTools/NanoAODTools/python/postprocessing/examples/skimmed.root") #/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_tmp/VBF_HToMuMu_nano2016.root")
	#/scratch/mandorli/Hmumu/samplePerAndrea/GluGlu_HToMuMu_skim_nano2016.root")
	#flow.Define("LHEScaleWeight","ROOT::VecOps::RVec<float>(9,1.)") #this result in NOOP if already defined, otherwise it is a failsafe

	#variables that we will add file by file before passing the RNode to the event processor
	flow.AddExpectedInput("year","int")
	flow.AddExpectedInput("isMC","bool")
	flow.AddExpectedInput("isHerwig","bool")
	flow.AddExpectedInput("Muon_sf","ROOT::VecOps::RVec<float>")
	flow.AddExpectedInput("btagWeight","float")
	flow.AddExpectedInput("EWKreweight","float")
	flow.AddExpectedInput("TriggerSel","bool")
	flow.AddExpectedInput("lhefactor","float")
	flow.AddExpectedInput("LHEPdfHasHessian","bool")
	flow.AddExpectedInput("nnlopsWeight","float")
	flow.AddExpectedInput("PrefiringWeight","float")
	flow.AddExpectedInput("PrefiringWeightUp","float")
	flow.AddExpectedInput("PrefiringWeightDown","float")
	#flow.AddExpectedInput("Jet_puId17","ROOT::VecOps::RVec<float>")

	flow.Define("LHEScaleWeightSafe","nLHEScaleWeight>=8?LHEScaleWeight:std::vector<float>(9,1)")
	flow.Define("PSWeightSafe","nPSWeight>=4?PSWeight:std::vector<float>(4,1)")
	#flow.Define("Jet_pt_touse","Jet_pt_newJEC")
	#flow.Define("Jet_pt_touse","Jet_pt")
	if int(year)==2018:
		print "Use NEW JEC"
		flow.Define("Jet_pt_touse","Jet_pt_newJEC")
	else:
		flow.Define("Jet_pt_touse","Jet_pt")

	flow.Define("Jet_pt_mix","Jet_pt*(20.f/Jet_pt) + Jet_pt_nom*(1.f-20.f/Jet_pt)")

	#Higgs to mumu reconstruction
	#flow.DefaultConfig(muIsoCut=0.25,muIdCut=2,muPtCut=20, dzCut=1e99,dxyCut=1e99) #cuts value should not be hardcoded below but rather being declared here so that scans and optimizations are possible
	flow.Define("Muon_id","Muon_tightId*4+Muon_mediumId*2+Muon_softId") 
	flow.Define("Muon_p4_orig","vector_map_t<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> >        >(Muon_corrected_pt , Muon_eta, Muon_phi, Muon_mass)")
	flow.Define("Muon_mass_FSR","0.f*Muon_pt")

	flow.AddCppCode('\n#include "geoFitCorr.h"\n')


	#need FSR inputs
	if FSR:
	  flow.Define("FsrPhoton_mass","FsrPhoton_pt*0.f")
	  flow.Define("FsrPhoton_p4","@p4v(FsrPhoton)")
	  if FSRnew:
	    flow.Define("Muon_FSR_p4","TakeDef(FsrPhoton_p4,Muon_fsrPhotonIdx,ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> >())")
	  else :
	    flow.Define("Muon_FSR_p4","vector_map_t<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> >        >(Muon_pt_FSR , Muon_eta_FSR, Muon_phi_FSR , Muon_mass_FSR)")
	  flow.Define("Muon_FSR_pt","TakeDef(FsrPhoton_pt,Muon_fsrPhotonIdx,0)")
	  flow.Define("Muon_FSR_eta","TakeDef(FsrPhoton_eta,Muon_fsrPhotonIdx,0)")
	  flow.Define("Muon_FSR_iso","TakeDef(FsrPhoton_relIso03,Muon_fsrPhotonIdx,99.)")
	  flow.Define("Muon_FSR_drEt2","TakeDef(FsrPhoton_dROverEt2,Muon_fsrPhotonIdx,99.)")

	  #flow.Define("Muon_wFSR_p4","Where(Muon_iso_FSR < 0.8,Muon_FSR_p4+Muon_p4_orig,Muon_p4_orig)")
	##  flow.Define("Muon_wFSR_p4","Muon_FSR_p4*(Muon_iso_FSR < 0.8)+Muon_p4_orig")
	  if FSRnew:
            flow.Define("Muon_wFSR_p4","Where((Muon_fsrPhotonIdx != -1 && Muon_FSR_iso < 1.8 && Muon_FSR_drEt2 < 0.012 && Muon_FSR_pt/Muon_pt<0.4 && abs(Muon_FSR_eta)<2.4 ),Muon_FSR_p4+Muon_p4_orig,Muon_p4_orig)")
	    #flow.Define("Muon_wFSR_p4","Where((Muon_fsrPhotonIdx != -1 && Muon_FSR_iso < 0.8 && Muon_FSR_drEt2 < 0.019 ),Muon_FSR_p4+Muon_p4_orig,Muon_p4_orig)")
	    flow.Define("Muon_correctedFSR_pt","MemberMap(Muon_wFSR_p4,Pt())")
	    flow.Define("Muon_iso","Where((Muon_fsrPhotonIdx != -1 && Muon_FSR_iso < 1.8 && Muon_FSR_drEt2 < 0.012 && Muon_FSR_pt/Muon_pt<0.4 && abs(Muon_FSR_eta)<2.4 ),(Muon_pfRelIso04_all*Muon_pt-Muon_FSR_pt)/Muon_correctedFSR_pt,(Muon_pfRelIso04_all*Muon_pt)/Muon_correctedFSR_pt)")
	  else:
	    flow.Define("Muon_wFSR_p4","Where((Muon_iso_FSR < 0.8),Muon_FSR_p4+Muon_p4_orig,Muon_p4_orig)")
	    flow.Define("Muon_correctedFSR_pt","MemberMap(Muon_wFSR_p4,Pt())")
	    flow.Define("Muon_iso","Where((Muon_iso_FSR < 0.8),(Muon_pfRelIso04_all*Muon_corrected_pt-Muon_pt_FSR)/Muon_correctedFSR_pt,Muon_pfRelIso04_all)")

	  flow.Define("Muon_pt_GeoFitCorrection","Map(Muon_dxybs*Muon_charge, Muon_corrected_pt,Muon_eta, [ year](float d0, float pt, float eta) { return PtGeoCor::PtGeo_BS_Roch(d0, pt, eta, year); })")
#	  flow.Define("Muon_pt_GeoFitCorrection","Map(Muon_dxybs*Muon_charge, Muon_pt,Muon_eta, [ year](float d0, float pt, float eta) { return PtGeoCor::PtGeo_BS_Roch(d0, pt, eta, year); })")
	  #flow.Define("Muon_pt_GeoFitCorrection","Muon_pt*2.f")
	  
	else :
	#replacements without FSR inputs
	  flow.Define("Muon_iso","Muon_pfRelIso04_all")
	  flow.Define("Muon_correctedFSR_pt","Muon_corrected_pt")
	  flow.Define("Muon_pt_GeoFitCorrection","Muon_pt*0.f")
	  
	flow.Define("Muon_p4GFcorr","vector_map_t<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > >(Muon_pt_GeoFitCorrection , Muon_eta, Muon_phi , Muon_mass)")
	#flow.Define("Muon_p4GFcorr","vector_map_t<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > >(Muon_pt_GeoFitCorrection , Muon_eta, Muon_phi , Muon_mass*0.f)")
	flow.SubCollection("SelectedMuon","Muon",sel="Muon_iso < 0.25 && Muon_mediumId && Muon_correctedFSR_pt > 20. && abs(Muon_eta) < 2.4") 

	#flow.Define("SelectedMuon_p4","vector_map_t<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> >        >(SelectedMuon_corrected_pt , SelectedMuon_eta, SelectedMuon_phi, SelectedMuon_mass)")

	#need FSR
	if FSR:
	  flow.Define("SelectedMuon_p4","SelectedMuon_wFSR_p4")
#  flow.Define("SelectedMuon_GFp4","Where((Muon_FSR_pt == 0.),SelectedMuon_p4GFcorr,SelectedMuon_p4)")
	  flow.Define("SelectedMuon_GFp4","Where((SelectedMuon_fsrPhotonIdx != -1 && SelectedMuon_FSR_iso < 1.8 && SelectedMuon_FSR_drEt2 < 0.012 && SelectedMuon_FSR_pt/SelectedMuon_corrected_pt<0.4 && abs(SelectedMuon_FSR_eta)<2.4 ) && (SelectedMuon_FSR_pt > 0.),SelectedMuon_p4,SelectedMuon_p4GFcorr)")  
	else :
	  flow.Define("SelectedMuon_p4","SelectedMuon_p4_orig")
	  flow.Define("SelectedMuon_GFp4","SelectedMuon_p4GFcorr")

	flow.Define("SelectedMuon_p4uncalib","@p4v(SelectedMuon)")
	flow.Selection("twoUnpreselMuons","nMuon>=2")
	flow.Selection("twoMuons","nSelectedMuon==2") 
	flow.Distinct("MuMu","SelectedMuon")
	flow.Define("OppositeSignMuMu","Nonzero(MuMu0_charge != MuMu1_charge)",requires=["twoMuons"])
	flow.Selection("twoOppositeSignMuons","OppositeSignMuMu.size() > 0")
	flow.TakePair("Mu","SelectedMuon","MuMu","At(OppositeSignMuMu,0,-200)",requires=["twoOppositeSignMuons"])
	flow.Define("Higgs","Mu0_GFp4+Mu1_GFp4")
	flow.Define("Higgs_noGF","Mu0_p4+Mu1_p4")
	flow.Define("HiggsUncalib","Mu0_p4uncalib+Mu1_p4uncalib")

	flow.Define("Higgs_m_GF","Higgs.M()")
	flow.Define("Higgs_m_noGF","Higgs_noGF.M()")



	flow.AddExternalCode(header="muonEfficiency.h",cppfiles=["muonEfficiency.C"])
	flow.Define("muEffWeight", "isMC?(Mu0_sf*Mu1_sf*mcMuonEffCorrection(year ,run, Mu0_pt, Mu0_eta, Mu1_pt, Mu1_eta)):1",requires=["twoOppositeSignMuons"])


	flow.AddExternalCode(header="prefiring.h",cppfiles=["prefiring.C"])
	flow.Define("Jet_prefireWeight","Map(Jet_pt,Jet_eta, [ year](float pt,float eta) { return prefiringJetWeight(year,pt,eta); }) ")

	flow.Define("Jet_p4","vector_map_t<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> >        >(Jet_pt_touse , Jet_eta, Jet_phi, Jet_mass)")
	#VBF Jets kinematics
	flow.DefaultConfig(jetPtCut=25)
	#Jet_pt_touse > jetPtCut && ( Jet_pt_touse > 50 || Jet_puId >0 ) &&   Jet_jetId > 0  && abs(Jet_eta) < 4.7 && (abs(Jet_eta)<2.5 || Jet_puId > 6  || (Jet_puId>0 && Jet_pt_touse > 50 ) ) && 
	#(year != 2017 ||  Jet_pt_touse > 50 || abs(Jet_eta) < 2.7 || abs(Jet_eta) > 3.0 ||  Jet_neEmEF<0.55 ) && 
	#flow.SubCollection("SelectedJet","Jet",'''
	#Jet_pt_touse > jetPtCut && ( Jet_pt_touse > 50 || Jet_puId >0 ) &&   Jet_jetId > 0  && abs(Jet_eta) < 4.7 && (abs(Jet_eta)<2.5 || Jet_puId > 6 || Jet_pt_touse >50) && 
	#(Jet_muonIdx1==-1 || TakeDef(Muon_pfRelIso04_all,Jet_muonIdx1,100) > 0.25 || abs(TakeDef(Muon_pt,Jet_muonIdx1,0)) < 20 || abs(TakeDef(Muon_id,Jet_muonIdx1,0) < muIdCut )) &&
	#(Jet_muonIdx2==-1 || TakeDef(Muon_pfRelIso04_all,Jet_muonIdx2,100) > 0.25 || abs(TakeDef(Muon_pt,Jet_muonIdx2,0)) < 20 || abs(TakeDef(Muon_id,Jet_muonIdx1,0) < muIdCut )) 
	#''') 
	#flow.Define("Jet_associatedMuonPt","abs(TakeDef(Muon_correctedFSR_pt,Jet_muonIdx1,0))")

	flow.SubCollection("SelectedJet","Jet",'''
	(year != 2017 ||  Jet_puId17 > 6 || abs(Jet_eta) < 2.6 || abs(Jet_eta) > 3.0) && 
	Jet_pt_touse > jetPtCut && ( Jet_pt > 50 
	|| (  Jet_puId17  > 0  && year==2017)
        || ((Jet_puId ) > 0 && year!=2017 ) )
	 &&   Jet_jetId  > 0  && abs(Jet_eta) < 4.7  &&  
	(Jet_muonIdx1==-1 || TakeDef(Muon_iso,Jet_muonIdx1,100) > 0.25 || abs(TakeDef(Muon_correctedFSR_pt,Jet_muonIdx1,0)) < 20 || abs(TakeDef(Muon_mediumId,Jet_muonIdx1,0) == 0 )) &&
	(Jet_muonIdx2==-1 || TakeDef(Muon_iso,Jet_muonIdx2,100) > 0.25 || abs(TakeDef(Muon_correctedFSR_pt,Jet_muonIdx2,0)) < 20 || abs(TakeDef(Muon_mediumId,Jet_muonIdx2,0) == 0 )) 
	''')
	#flow.SubCollection("SelectedJet","Jet",'''
	#(year != 2017 ||  abs(Jet_eta) < 2.7 || abs(Jet_eta) > 3.1 ) && 
	#Jet_pt_touse > jetPtCut && ( Jet_pt_touse > 50 || ((Jet_puId ) > 0 && year!=2017 ) ) &&   Jet_jetId  > 0  && abs(Jet_eta) < 4.7  &&  
	#(Jet_muonIdx1==-1 || TakeDef(Muon_iso,Jet_muonIdx1,100) > 0.25 || abs(TakeDef(Muon_correctedFSR_pt,Jet_muonIdx1,0)) < 20 || abs(TakeDef(Muon_mediumId,Jet_muonIdx1,0) == 0 )) &&
	#(Jet_muonIdx2==-1 || TakeDef(Muon_iso,Jet_muonIdx2,100) > 0.25 || abs(TakeDef(Muon_correctedFSR_pt,Jet_muonIdx2,0)) < 20 || abs(TakeDef(Muon_mediumId,Jet_muonIdx2,0) == 0 )) 
	#''')

	flow.Selection("twoJets","nSelectedJet>=2")



	flow.Define("GenJet_p4","@p4v(GenJet)")
	#flow.Define("SelectedJet_p4","@p4v(SelectedJet)")
	flow.Distinct("JetPair","SelectedJet")
	#flow.TakePair("QJet","SelectedJet","JetPair","Argmax(MemberMap((JetPair0_p4+JetPair1_p4),M() ))",requires=["twoJets"])
	flow.Define("SortedSelectedJetIndices","Argsort(-SelectedJet_pt_touse)")
	flow.ObjectAt("QJet0","SelectedJet",'At(SortedSelectedJetIndices,0)',requires=["twoJets"])
	flow.ObjectAt("QJet1","SelectedJet",'At(SortedSelectedJetIndices,1)',requires=["twoJets"])
	flow.AddCppCode('\n#include "qglJetWeight.h"\n')
	flow.Define("QGLweight", "isMC?qglJetWeight(QJet0_partonFlavour, QJet0_eta, QJet0_qgl,isHerwig)*qglJetWeight(QJet1_partonFlavour, QJet1_eta, QJet1_qgl,isHerwig):1",requires=["twoJets"])


	#flow.Define("PrefiringWeight","isMC?std::accumulate(Jet_prefireWeight.begin(),Jet_prefireWeight.end(),1.f, std::multiplies<float>()):1.f")
	#flow.Define("PrefiringCorrection","1.f-(1.f-QJet0_prefireWeight)*(1.f-QJet1_prefireWeight)")
	#flow.Define("CorrectedPrefiringWeight","PrefiringWeight+PrefiringCorrection")

	#compute number of softjets removing signal footprint
	flow.Define("SoftActivityJet_mass","SoftActivityJet_pt*0")
	flow.Define("SoftActivityJet_p4","@p4v(SoftActivityJet)")
	flow.Match("SelectedJet","SoftActivityJet") #associate signal jets
	flow.Match("SelectedMuon","SoftActivityJet") #associate signal muons
	flow.Define("TrigObj_mass","0.f*TrigObj_pt")
	flow.SubCollection("TrigMuon","TrigObj","abs(TrigObj_id)==13 && (TrigObj_filterBits & 8) ") #single mu
	flow.Define("TrigMuon_p4","@p4v(TrigMuon)")

	flow.Match("SelectedMuon","TrigMuon") #associate signal muons
	flow.Define("SelectedMuon_TriggerMatch","SelectedMuon_TrigMuonIdx != -1") #associate signal muons
	flow.Define("SelectedMuon_TriggerFilterBits","TakeDef(TrigObj_filterBits,SelectedMuon_TrigMuonIdx,-1)") #associate signal muons
	flow.Define("NSoft5Saved","Nonzero(SoftActivityJet_pt > 5.).size()")
	flow.SubCollection("SAJet","SoftActivityJet",'''
	! (   (SoftActivityJet_SelectedJetDr<0.4 && ( SoftActivityJet_SelectedJetIdx == QJet0 ||  SoftActivityJet_SelectedJetIdx == QJet1)) ||
		   (SoftActivityJet_SelectedMuonDr<0.4 && ( SoftActivityJet_SelectedMuonIdx == Mu0 || SoftActivityJet_SelectedMuonIdx == Mu1) ) || 
		   (SoftActivityJet_eta > std::max(QJet0_eta, QJet1_eta) || SoftActivityJet_eta < std::min(QJet0_eta, QJet1_eta)))
	''')
	flow.SubCollection("FootprintSAJet","SoftActivityJet",'''
	 (   (SoftActivityJet_SelectedJetDr<0.4 && ( SoftActivityJet_SelectedJetIdx == QJet0 ||  SoftActivityJet_SelectedJetIdx == QJet1)) ||
		   (SoftActivityJet_SelectedMuonDr<0.4 && ( SoftActivityJet_SelectedMuonIdx == Mu0 || SoftActivityJet_SelectedMuonIdx == Mu1) ) || 
		   (SoftActivityJet_eta > std::max(QJet0_eta, QJet1_eta) || SoftActivityJet_eta < std::min(QJet0_eta, QJet1_eta)))
	''')

	flow.Define("NSoft5",'''Sum( 
	 (  (SoftActivityJet_SelectedJetDr>0.2 || ( SoftActivityJet_SelectedJetIdx != QJet0 &&  SoftActivityJet_SelectedJetIdx != QJet1)) &&
		   (SoftActivityJet_SelectedMuonDr>0.2 || ( SoftActivityJet_SelectedMuonIdx != Mu0 && SoftActivityJet_SelectedMuonIdx != Mu1) ) && 
		   (SoftActivityJet_eta < std::max(QJet0_eta, QJet1_eta) && SoftActivityJet_eta > std::min(QJet0_eta, QJet1_eta))
	)&&
		   SoftActivityJet_pt > 5. 
	)''')

	flow.Define("LeadingSAJet_pt","At(SAJet_pt,0,-1)")

	flow.Define("NSoft5NewNoRapClean",'''SoftActivityJetNjets5-Sum( 
	(          (SoftActivityJet_SelectedJetDr<0.4 && ( SoftActivityJet_SelectedJetIdx == QJet0 ||  SoftActivityJet_SelectedJetIdx == QJet1)) ||
		   (SoftActivityJet_SelectedMuonDr<0.4 && ( SoftActivityJet_SelectedMuonIdx == Mu0 || SoftActivityJet_SelectedMuonIdx == Mu1) )  
	)&&
		   SoftActivityJet_pt > 5. 
	)''')


	flow.Define("NSoft5New",'''SoftActivityJetNjets5-Sum( 
	(	   (SoftActivityJet_SelectedJetDr<0.4 && ( SoftActivityJet_SelectedJetIdx == QJet0 ||  SoftActivityJet_SelectedJetIdx == QJet1)) ||
		   (SoftActivityJet_SelectedMuonDr<0.4 && ( SoftActivityJet_SelectedMuonIdx == Mu0 || SoftActivityJet_SelectedMuonIdx == Mu1) ) || 
		   (SoftActivityJet_eta > std::max(QJet0_eta, QJet1_eta) || SoftActivityJet_eta < std::min(QJet0_eta, QJet1_eta))
	)&&
		   SoftActivityJet_pt > 5. 
	)''')
	#flow.Define("NSoft5New","0.f")

	#cross checks
	#flow.Define("NSoft5New2","SoftActivityJetNjets5-Sum(FootprintSAJet_pt>5)")
	#flow.Define("NSoft2New2","SoftActivityJetNjets2-Sum(FootprintSAJet_pt>2)")
	#flow.Define("NSoft10New2","SoftActivityJetNjets10-Sum(FootprintSAJet_pt>10)")
	flow.Define("FootHT","Sum(FootprintSAJet_pt)")
	flow.Define("SAHT","SoftActivityJetHT-Sum(FootprintSAJet_pt)")
	flow.Define("SAHT2","SoftActivityJetHT2-Sum(FootprintSAJet_pt*(FootprintSAJet_pt>2.f))")
	flow.Define("SAHT5","SoftActivityJetHT5-Sum(FootprintSAJet_pt*(FootprintSAJet_pt>5.f))")



	flow.Define("qq","QJet0_p4+QJet1_p4")
	flow.Define("Mqq","qq.M()")
	flow.Define("MqqGenJet","(QJet0_genJetIdx>=0&&QJet1_genJetIdx>=0&&QJet0_genJetIdx<nGenJet&&QJet1_genJetIdx<nGenJet)?(At(GenJet_p4,QJet0_genJetIdx)+At(GenJet_p4,QJet1_genJetIdx)).M():-99")
	flow.Define("qq_pt","qq.Pt()")
	flow.Define("qqDeltaEta","abs(QJet0_eta-QJet1_eta)")
	flow.Define("qqDeltaPhi","abs(ROOT::Math::VectorUtil::DeltaPhi(QJet0_p4,QJet1_p4))")

	#QQ vs ll kinematic
	flow.Define("ll_ystar","Higgs.Rapidity() - (QJet0_p4.Rapidity() + QJet1_p4.Rapidity())/2.f")
	flow.Define("ll_zstar"," abs( ll_ystar/ (QJet0_p4.Rapidity()-QJet1_p4.Rapidity() )) ")
	flow.Define("ll_zstar_log"," log(ll_zstar) ")
	flow.Define("ll_zstarbug_log","log(abs( (  Higgs.Rapidity() - (QJet0_p4.Rapidity() + QJet1_p4.Rapidity())  )/ (QJet0_p4.Rapidity()-QJet1_p4.Rapidity() )))")
	flow.Define("DeltaEtaQQSum","abs(QJet0_eta) +  abs(QJet1_eta)")
	flow.Define("PhiHQ1","abs(ROOT::Math::VectorUtil::DeltaPhi(Higgs,QJet0_p4))")
	flow.Define("PhiHQ2","abs(ROOT::Math::VectorUtil::DeltaPhi(Higgs,QJet1_p4))")
	flow.Define("EtaHQ1","abs(Higgs.Eta() - QJet0_eta)")
	flow.Define("EtaHQ2","abs(Higgs.Eta() - QJet1_eta)")
	flow.Define("DeltaRelQQ","(QJet0_p4+QJet1_p4).Pt()/( QJet0_p4.Pt()+QJet1_p4.Pt())")
	flow.Define("Rpt","(QJet0_p4+QJet1_p4+ Higgs).Pt()/( QJet0_p4.Pt()+QJet1_p4.Pt() + Higgs.Pt())")
	flow.Define("mmjj","Higgs+qq")
	flow.Define("theta2","Higgs.Vect().Dot(QJet1_p4.Vect())/QJet1_p4.Vect().R()/Higgs.Vect().R()")
	flow.ObjectAt("LeadMuon","SelectedMuon","0",requires=["twoMuons"])
	flow.ObjectAt("SubMuon","SelectedMuon","1",requires=["twoMuons"])
	flow.Define("Higgs_pt","Higgs.Pt()")
	flow.Define("Higgs_rapidity","Higgs.Rapidity()")

	flow.Define("pTbalanceLead","QJet0_pt/Higgs_pt")
	flow.Define("pTbalance","qq.Pt()/Higgs_pt")
	flow.Define("pTbalanceAll","SumDef(SelectedJet_p4).pt()/Higgs_pt")
	flow.Define("pTbalanceAllLog","log(pTbalanceAll)")
	flow.Define("pTbalanceLog","log(pTbalance)")
	flow.Define("pTbalanceLeadLog","log(pTbalanceLead)")
	flow.Define("Higgs_m","Higgs.M()")
	flow.Define("Higgs_eta","Higgs.Eta()")
	flow.Define("Higgs_m_uncalib","HiggsUncalib.M()")
	flow.Define("Mqq_log","log(Mqq)")
	flow.Define("Mqq_over400_log","log(Mqq/400)")
	flow.Define("mmjj_pt","mmjj.Pt()")
	flow.Define("mmjj_pt_log","log(mmjj_pt)")
	flow.Define("mmjj_pz","mmjj.Pz()")
	flow.Define("mmjj_pz_logabs","log(abs(mmjj_pz))")
	flow.Define("MaxJetAbsEta","std::max(std::abs(QJet0_eta), std::abs(QJet1_eta))")
	flow.AddExternalCode(header="muresolution.h",cppfiles=["muresolution.C"],ipaths=["."])
	flow.Define("Higgs_mRelReso", "hRelResolution(LeadMuon_pt,LeadMuon_eta,SubMuon_pt,SubMuon_eta)")
	flow.Define("Higgs_mReso","Higgs_mRelReso*Higgs_m")
	#flow.Define("Higgs_mReso","2.f")
	#flow.Define("Higgs_mRelReso","Higgs_mReso/Higgs_m")
	flow.Define("minEtaHQ","std::min(abs(EtaHQ1),(EtaHQ2))")
	flow.Define("minPhiHQ","std::min(abs(PhiHQ1),abs(PhiHQ2))")

	flow.AddCppCode('\n#include "boost_to_CS.h"\n')
	#flow.Define("CS_pair", "boost_to_CS(LeadMuon_p4, SubMuon_p4)",requires=["twoOppositeSignMuons"])
	##flow.Define("CS_theta","CS_pair.first",requires=["twoOppositeSignMuons"])
	##flow.Define("CS_phi","CS_pair.second",requires=["twoOppositeSignMuons"])
	#flow.Define("CS_theta","CS_pair[0]",requires=["twoOppositeSignMuons"])
	#flow.Define("CS_phi","CS_pair[1]",requires=["twoOppositeSignMuons"])
	flow.Define("CS_theta","boost_to_CS(LeadMuon_p4, SubMuon_p4,  SubMuon_charge).first",requires=["twoOppositeSignMuons"])
	flow.Define("CS_phi","boost_to_CS(LeadMuon_p4, SubMuon_p4, SubMuon_charge).second",requires=["twoOppositeSignMuons"])

	flow.DefaultConfig(higgsMassWindowWidth=10,mQQcut=400,nominalHMass=125.03) #,btagCut=0.8)
	flow.Define("btagCut","(year==2018)?0.4184f:((year==2017)?0.4941f:0.6321f)")
	flow.Define("btagCutL","(year==2018)?0.1241f:((year==2017)?0.1522f:0.2217f)")
	#adding for sync
	flow.Define("nbtagged","int(Nonzero(SelectedJet_btagDeepB > btagCut && abs(SelectedJet_eta)< 2.5).size())")
	flow.Define("nbtaggedL","int(Nonzero(SelectedJet_btagDeepB > btagCutL && abs(SelectedJet_eta)< 2.5).size())")
	flow.Define("nelectrons","int(Nonzero(Electron_pt > 20 && abs(Electron_eta) < 2.5 && Electron_mvaFall17V2Iso_WP90 ).size())")


	flow.Selection("MassWindow","abs(Higgs.M()-nominalHMass)<higgsMassWindowWidth")
	flow.Selection("MassWindowZ","abs(Higgs.M()-91)<15")
	flow.Selection("VBFRegion","Mqq > mQQcut && QJet0_pt_touse> 35 && QJet1_pt_touse > 25")
	flow.Selection("PreSel","nelectrons==0 && nbtaggedL < 2 && VBFRegion && twoOppositeSignMuons && nbtagged < 1 && (( year == 2016 && LeadMuon_pt > 26 ) || ( year == 2017 && LeadMuon_pt > 29 ) || ( year == 2018 && LeadMuon_pt > 26 )) && SubMuon_pt > 20 && TriggerSel && abs(SubMuon_eta) <2.4 && abs(LeadMuon_eta) < 2.4",requires=["VBFRegion","twoOppositeSignMuons"])
	flow.Selection("SideBand","Higgs_m < 150 && Higgs_m > 110 && ! MassWindow && VBFRegion &&  qqDeltaEta > 2.5",requires=["VBFRegion","PreSel"])
	flow.Selection("SignalRegion","VBFRegion && MassWindow &&  qqDeltaEta > 2.5", requires=["VBFRegion","MassWindow","PreSel"])
	flow.Selection("ZRegion","VBFRegion && MassWindowZ  && qqDeltaEta > 2.5", requires=["VBFRegion","MassWindowZ","PreSel"])
	flow.Selection("ZRegionSMP","Mqq > 250 && MassWindowZ && QJet0_pt_touse> 50 && QJet1_pt_touse > 30 && twoOppositeSignMuons && twoJets && TriggerSel&& abs(SubMuon_eta) <2.4 && abs(LeadMuon_eta) < 2.4 ", requires=["twoOppositeSignMuons","twoJets"])
	flow.Selection("TwoJetsTwoMu","twoJets && twoOppositeSignMuons", requires=["twoJets","twoOppositeSignMuons"])
	flow.Selection("SignalRegionT","SignalRegion && QJet0_pt_touse>45 && QJet1_pt_touse > 27",requires=["SignalRegion"])
	flow.Selection("ZRegionT","ZRegion && QJet0_pt_touse>45 && QJet1_pt_touse > 27",requires=["ZRegion"])
	flow.Selection("SideBandT","SideBand && QJet0_pt_touse>45 && QJet1_pt_touse > 27",requires=["SideBand"])
	#with bug
	#flow.Define("SBClassifier","mva.eval(__slot,{Higgs_m,Mqq_log,mmjj_pt_log,qqDeltaEta,float(NSoft5),ll_zstarbug_log,Higgs_pt,theta2,mmjj_pz_logabs,MaxJetAbsEta})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])
	#flow.Define("SBClassifierNoMass","mva.eval(__slot,{125.,Mqq_log,mmjj_pt_log,qqDeltaEta,float(NSoft5),ll_zstarbug_log,Higgs_pt,theta2,mmjj_pz_logabs,MaxJetAbsEta})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])
	#flow.Define("SBClassifierNoMassNoNSJ","mva.eval(__slot,{125.,Mqq_log,mmjj_pt_log,qqDeltaEta,0,ll_zstarbug_log,Higgs_pt,theta2,mmjj_pz_logabs,MaxJetAbsEta})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])

	#iggs_m,Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,NSoft5New,minEtaHQ,qqDeltaPhi,QJet1_pt_touse

	flow.AddExternalCode(header= "mva.h",cppfiles=["mva.C"],libs=["TMVA"],ipaths=["."])
	flow.Define("SBClassifier","mva.eval(__slot,{Higgs_m,Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5New),minEtaHQ,qqDeltaPhi,QJet1_pt_touse})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])
	flow.Define("SBClassifierNoMass","mva.eval(__slot,{125.,Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5New),minEtaHQ,qqDeltaPhi,QJet1_pt_touse})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])
	#low.Define("SBClassifierNoMassNoNSJ","mva.eval(__slot,{125.,Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,0,minEtaHQ})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])
	#flow.Define("SBClassifierZ","mva.eval({125.,log(Mqq),mmjj.Pt(),qqDeltaEta,float(NSoft5),ll_zstar,Higgs.Pt(),theta2,mmjj.Pz(),std::max(std::abs(QJet0_eta), std::abs(QJet1_eta))})") #,inputs=["Higgs_pt","Higgs_m","Mqq","Rpt","DeltaRelQQ"])
	flow.Define("BDTAtan","atanh((SBClassifier+1.)/2.)")
	flow.Define("BDTAtanNoMass","atanh((SBClassifierNoMass+1.)/2.)")
	#low.Define("BDTAtanNoMassNoNSJ","atanh((SBClassifierNoMassNoNSJ+1.)/2.)")
	flow.Selection("SubLeadingEta2p7to3p1","abs(abs(QJet1_eta)-2.7)<0.2 && ZRegion",requires=["ZRegion"])
	flow.Selection("SubLeadingEta2p7to3p1QGL","abs(abs(QJet1_eta)-2.7)<0.2 && QJet1_qgl > 0.5 && ZRegion ",requires=["ZRegion"])
	flow.Selection("SubLeadingEta2p7to3p1Pt45","abs(abs(QJet1_eta)-2.7)<0.2 && ZRegion && QJet0_pt_touse > 45",requires=["ZRegion"])
	flow.Selection("SubLeadingEta2p7to3p1QGLPt45","abs(abs(QJet1_eta)-2.7)<0.2 && QJet1_qgl > 0.5 && ZRegion && QJet0_pt_touse > 45",requires=["ZRegion"])
	flow.Selection("BDT0p8","BDTAtanNoMass>0.8")
	flow.Selection("BDT1p0","BDTAtanNoMass>1.0")
	flow.Selection("BDT1p1","BDTAtanNoMass>1.1")
	flow.Selection("BDT1p2","BDTAtanNoMass>1.2")
	flow.Selection("BDTNoMN1p0","BDTAtanNoMassNoNSJ>1.0")
	flow.Selection("BDTNoMN1p2","BDTAtanNoMassNoNSJ>1.2")
        flow.Selection("ZRegionSLJeta0pt0","(abs(QJet1_eta)>0&&abs(QJet1_eta)<=1.93) && ZRegion",requires=["ZRegion"])
        flow.Selection("ZRegionSLJeta1pt0","(abs(QJet1_eta)>1.93&&abs(QJet1_eta)<=2.5) && ZRegion",requires=["ZRegion"])
        flow.Selection("ZRegionSLJeta2pt0","(abs(QJet1_eta)>2.5&&abs(QJet1_eta)<=3.139)&&(QJet1_pt>0&&QJet1_pt<=50) && ZRegion",requires=["ZRegion"])
        flow.Selection("ZRegionSLJeta2pt1","(abs(QJet1_eta)>2.5&&abs(QJet1_eta)<=3.139)&&(QJet1_pt>50) && ZRegion",requires=["ZRegion"])
        flow.Selection("ZRegionSLJeta3pt0","(abs(QJet1_eta)>3.139)&&(QJet1_pt>0&&QJet1_pt<=50) && ZRegion",requires=["ZRegion"])
        flow.Selection("ZRegionSLJeta3pt1","(abs(QJet1_eta)>3.139)&&(QJet1_pt>50) && ZRegion",requires=["ZRegion"])


	flow.AddExternalCode(header= "eval_lwtnn.h",cppfiles=["eval_lwtnn.C"],libs=["lwtnn"],ipaths=["/scratch/lgiannini/HmmPisa/lwtnn/include/lwtnn/"],lpaths=["/scratch/lgiannini/HmmPisa/lwtnn/build/lib/"])
	#flow.Define("DNNClassifier","lwtnn.eval(__slot, {Mqq_log,Rpt,qqDeltaEta,ll_zstar,float(NSoft5),minEtaHQ,1,1,Higgs_pt,log(Higgs_pt),Higgs.Eta(),Mqq,QJet1_pt,QJet0_pt,QJet1_eta,QJet0_eta,QJet1_phi,QJet0_phi,Higgs_m,Higgs_mRelReso,Higgs_mReso}, {18,3})")
	#flow.Define("DNN18Classifier","lwtnn_all.eval(event, {Mqq_log,Rpt,qqDeltaEta,log(ll_zstar),float(NSoft5New),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m,Higgs_mRelReso,Higgs_mReso}, {19,3})")
	flow.Define("DNN18Classifier","lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m,Higgs_mRelReso,Higgs_mReso}, {22,3})")
	flow.Define("DNN18Atan","atanh(DNN18Classifier)")
	flow.Define("DNN18Atan2","atanh(lwtnn_feb2.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m,Higgs_mRelReso,Higgs_mReso}, {22,3}))")
	flow.Define("DNN18AtanM12509","atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m-0.09f,Higgs_mRelReso,Higgs_mReso}, {22,3}))")
	flow.Define("Higgs_m38","Higgs_m+0.38f")
	flow.Define("DNN18AtanM12538","atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m-0.38f,Higgs_mRelReso,Higgs_mReso}, {22,3}))")
	for x in range(0,21) :
	   name="DNN18AtanM%4.0f"%((x*0.5+120)*10)
	   bias=5.-x/2.
	   flow.Define(name,"atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m+%ff,Higgs_mRelReso,Higgs_mReso}, {22,3}))"%bias)

	for x in range(1,10) :
	   name="DNN18AtanM%4.0f"%((x*0.1+125)*10)
	   bias=-x/10.
	   if x!=5 :
  	      flow.Define(name,"atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m+%ff,Higgs_mRelReso,Higgs_mReso}, {22,3}))"%bias)


#	flow.Define("DNNwithZClassifier","lwtnn_withZ.eval(event, {Mqq_log,Rpt,qqDeltaEta,log(ll_zstar),float(NSoft5New),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m,Higgs_mRelReso,Higgs_mReso}, {19,3})")
#	flow.Define("DNNnovClassifier_GF","lwtnn_nov.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),Higgs_m_GF,Higgs_mRelReso,Higgs_mReso}, {22,3})")

#	flow.Define("DNNClassifierZ","lwtnn_Z.eval(event, {Mqq_log,Rpt,qqDeltaEta,log(ll_zstar),float(NSoft5New),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year)}, {19})")
#	flow.Define("DNN18ClassifierNoQGL","lwtnn_all.eval(event, {Mqq_log,Rpt,qqDeltaEta,log(ll_zstar),float(NSoft5New),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,0.98,0.98,float(year),Higgs_m,Higgs_mRelReso,Higgs_mReso}, {19,3})")
	#lwtnn.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar,float(NSoft5),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,Higgs_m,Higgs_mRelReso,Higgs_mReso}, {16,3})")

#	flow.Define("DNN18ClassifierNoMass","lwtnn_all.eval(event, {Mqq_log,Rpt,qqDeltaEta,log(ll_zstar),float(NSoft5New),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),125.,Higgs_mRelReso,Higgs_mReso}, {19,3})")
#	flow.Define("DNNwithZClassifierNoMass","lwtnn_withZ.eval(event, {Mqq_log,Rpt,qqDeltaEta,log(ll_zstar),float(NSoft5New),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),125.,Higgs_mRelReso,Higgs_mReso}, {19,3})")
	flow.Define("DNN18AtanNoMass","atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),125.,Higgs_mRelReso,Higgs_mReso}, {22,3}))")
	flow.Define("DNN18AtanNoMass2","atanh(lwtnn_feb2.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),125.,Higgs_mRelReso,Higgs_mReso}, {22,3}))")

	flow.Define("DNN18AtanMassSpread","atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),(Higgs_m<115)?(Higgs_m+5.f):(Higgs_m-15.f) ,Higgs_mRelReso,Higgs_mReso}, {22,3}))")
	flow.Define("DNN18AtanMassSpread2","atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),(Higgs_m<115)?(Higgs_m+12.5f):(Higgs_m-15.f) ,Higgs_mRelReso,Higgs_mReso}, {22,3}))")
#	flow.Define("DNN18AtanMassSmear","atanh(lwtnn_feb.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar_log,float(NSoft5NewNoRapClean),SAHT2,minEtaHQ,CS_phi, CS_theta,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,float(year),115.f+(event%20),(Higgs_m<115)?(Higgs_m+5.f):(Higgs_m-15.f) ,Higgs_mRelReso,Higgs_mReso}, {22,3}))")

	#lwtnn.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar,float(NSoft5),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,125.,Higgs_mRelReso,Higgs_mReso}, {16,3})")
#	flow.Define("DNN18Atan","atanh(DNN18Classifier)")
#	flow.Define("DNNZAtan","atanh(DNNClassifierZ)")
#	flow.Define("DNNwithZAtan","atanh(DNNwithZClassifier)")
#	flow.Define("DNN18AtanNoQGL","atanh(DNN18ClassifierNoQGL)")
#	flow.Define("DNN18AtanNoMass","atanh(DNN18ClassifierNoMass)")
#	flow.Define("DNNwithZAtanNoMass","atanh(DNNwithZClassifierNoMass)")

#	flow.Define("DNNnovAtan","atanh(DNNnovClassifier)")
#	flow.Define("DNNnovGFAtan","atanh(DNNnovClassifier_GF)")
#	flow.Define("DNNnovAtanNoMass","atanh(DNNnovClassifierNoMass)")


	#flow.Define("DNNClassifier18","lwtnn18.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar,float(NSoft5),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,Higgs_m,Higgs_mRelReso,Higgs_mReso}, {18,3})")
	#flow.Define("DNN18oldAtan","atanh(DNNClassifier18)")
	#flow.Define("DNN18oldAtanNoQGL","atanh(lwtnn18.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar,float(NSoft5),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,0.98,0.8,Higgs_m,Higgs_mRelReso,Higgs_mReso}, {18,3}))")
	#flow.Define("DNN18oldAtanNoMass","atanh(lwtnn18.eval(event, {Mqq_log,Rpt,qqDeltaEta,ll_zstar,float(NSoft5),minEtaHQ,Higgs_pt,log(Higgs_pt),Higgs_eta,Mqq,QJet0_pt_touse,QJet1_pt_touse,QJet0_eta,QJet1_eta,QJet0_phi,QJet1_phi,QJet0_qgl,QJet1_qgl,125.,Higgs_mRelReso,Higgs_mReso}, {18,3}))")

	#flow.AddCppCode('\n#include "boost_to_CS.h"\n')
	#flow.Define("CS_pair", "boost_to_CS(LeadMuon_p4, SubMuon_p4)",requires=["twoOppositeSignMuons"])
	#flow.Define("CS_theta","CS_pair.first")
	#flow.Define("CS_phi","CS_pair.second")


	flow.AddExternalCode(header="weightedMass.h",cppfiles=["weightedMass.C"],ipaths=["."])
	flow.Define("weightDNNSB","weightDNNSB(DNN18AtanNoMass,year)")
	flow.Selection("SignalRegionDNNWeighted","SignalRegion",requires=["SignalRegion"])
        flow.Selection("SRplusSBDNNWeighted","Higgs_m < 150 && Higgs_m > 110 && VBFRegion &&  qqDeltaEta > 2.5",requires=["VBFRegion","PreSel"])
#flow.Selection("SRplusSBDNNWeighted","SignalRegion || SideBand")
	flow.Selection("TightMassRegion","SignalRegion && abs(Higgs_m-125.0f) < 2.f",requires=["SignalRegion"])
#	flow.CentralWeight("weightDNNSB",["SignalRegionDNNWeighted","SRplusSBDNNWeighted"])

	flow.AddExternalCode(header="nnlops.h",cppfiles=["nnlops.C"],ipaths=["."])

	#unused MC stuff
	flow.Selection("hasHiggs","Sum(GenPart_pdgId == 25) > 0")
	flow.Define("GenHiggs_idx","Nonzero(GenPart_pdgId == 25)", requires=["hasHiggs"])
	flow.SubCollection("QParton","GenPart",sel="GenPart_genPartIdxMother==At(Take(GenPart_genPartIdxMother,GenHiggs_idx),0,-100) && GenPart_pdgId!= 25")
	flow.Define("QParton_p4","@p4v(QParton)")
	flow.Distinct("QQ","QParton")
	flow.Selection("twoQ","nQParton>=2")
	flow.Define("QQ_p4","QQ0_p4+QQ1_p4",requires=["twoQ"])
	flow.Define("QQ_mass","MemberMap(QQ_p4,M())")
	flow.Define("HighestGenQQMass","At(QQ_mass,Argmax(QQ_mass),-99)")
        flow.AddExternalCode(header="qq2Hqq_uncert_scheme.h",cppfiles=["qq2Hqq_uncert_scheme.cpp"],ipaths=["."])

        return flow
