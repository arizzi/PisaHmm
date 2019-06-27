#define hist mapping
genericHistos=["Higgs_m","pTbalanceAll","LeadMuon_pt","LeadMuon_eta","SubMuon_pt","SubMuon_eta","QJet0_eta","QJet1_eta","QJet0_pt_touse","QJet1_pt_touse","PV_npvs","LeadingSAJet_pt","SAHT","SAHT5","nFootprintSAJet","FootHT"]
bdtInputHistos=["Mqq_log","mmjj_pt","qqDeltaEta","NSoft5","ll_zstar","Higgs_pt","theta2","mmjj_pz","MaxJetAbsEta","Higgs_m_uncalib","NSoft5New","ll_zstar_log", "Higgs_mReso"]
signalHistosVariations=["SBClassifierNoMass","BDTAtanNoMass","SBClassifierNoMassNoNSJ","BDTAtanNoMassNoNSJ"]
signalHistos=["SBClassifier","BDTAtan","LHE_NpNLO","DNNClassifier", "DNNAtan"]

#signalHistos=["SBClassifier"]

histosPerSelection={
#"PreSel" : genericHistos+["Mqq"],
"SignalRegion": signalHistos+ genericHistos+signalHistosVariations+bdtInputHistos,
"ZRegion": signalHistosVariations+genericHistos+bdtInputHistos,
"ZRegionSMP": signalHistosVariations,
"SideBand" : signalHistos+signalHistosVariations+genericHistos,
#"BDTNoMN1p0" : bdtInputHistos+genericHistos+signalHistosVariations+signalHistos,
#"BDTNoMN1p2" : bdtInputHistos+genericHistos+signalHistosVariations+signalHistos,
#"BDT0p8" : bdtInputHistos,
#"BDT1p0" : bdtInputHistos,
#"BDT1p1" : bdtInputHistos,
#"BDT1p2" : bdtInputHistos,
#"TwoJetsTwoMu" : genericHistos
}

