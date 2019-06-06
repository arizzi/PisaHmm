#define hist mapping
genericHistos=["LeadMuon_pt","LeadMuon_eta","SubMuon_pt","SubMuon_eta","QJet0_eta","QJet1_eta","QJet0_pt_touse","QJet1_pt_touse","PV_npvs","LeadingSAJet_pt","SAHT","SAHT5","nFootprintSAJet","FootHT"]
bdtInputHistos=["Mqq_log","mmjj_pt","qqDeltaEta","NSoft5","ll_zstar","Higgs_pt","theta2","mmjj_pz","MaxJetAbsEta","Higgs_m","Higgs_m_uncalib","NSoft5New","ll_zstar_log"]
signalHistosVariations=["SBClassifierNoMass","BDTAtanNoMass"]
signalHistos=["SBClassifier","BDTAtan"]

histosPerSelection={
#"PreSel" : genericHistos+["Mqq"],
"SignalRegion": genericHistos+signalHistos+bdtInputHistos,
"ZRegion": signalHistosVariations+genericHistos+bdtInputHistos,
#"ZRegionNadya": genericHistos+signalHistosZ,
"SideBand" : signalHistos+signalHistosVariations+genericHistos,
#"BDT0p8" : bdtInputHistos,
#"BDT1p0" : bdtInputHistos,
#"BDT1p1" : bdtInputHistos,
#"BDT1p2" : bdtInputHistos,
#"TwoJetsTwoMu" : genericHistos
}

