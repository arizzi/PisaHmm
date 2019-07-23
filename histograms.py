#define hist mapping
genericHistos=["Higgs_m","pTbalanceAll","LeadMuon_pt","LeadMuon_eta","SubMuon_pt","SubMuon_eta","QJet0_eta","QJet1_eta","QJet0_pt_touse","QJet1_pt_touse","PV_npvs","LeadingSAJet_pt","SAHT","SAHT5","nFootprintSAJet","FootHT"]
#missing=["Higgs_mRelReso"]
bdtInputHistos=["Mqq_log","mmjj_pt","qqDeltaEta","NSoft5","ll_zstar","Higgs_pt","theta2","mmjj_pz","MaxJetAbsEta","Higgs_m_uncalib","NSoft5New","ll_zstar_log", "Higgs_mReso","minEtaHQ","Rpt","Higgs_eta","QJet0_phi","QJet1_phi","Higgs_mRelReso","Higgs_mReso"]
signalHistosVariations=["SBClassifierNoMass","BDTAtanNoMass","SBClassifierNoMassNoNSJ","BDTAtanNoMassNoNSJ","DNNClassifierNoMass", "DNNAtanNoMass"]
signalHistos=["SBClassifier","BDTAtan","LHE_NpNLO","DNNClassifier", "DNNAtan"]

#signalHistos=["SBClassifier"]

histosPerSelection={
#"PreSel" : genericHistos+["Mqq"],
"SignalRegion": signalHistos+ genericHistos+signalHistosVariations+bdtInputHistos,
"ZRegion": signalHistosVariations+genericHistos+bdtInputHistos,
"ZRegionSMP": signalHistosVariations+["pTbalanceAll"],
"SideBand" : signalHistos+signalHistosVariations+genericHistos,
}
hh={
"ZRegionPt0To30Eta0To2":["pTbalanceAll"],
"ZRegionPt30To50Eta0To2":["pTbalanceAll"],
"ZRegionPt50To100Eta0To2":["pTbalanceAll"],
"ZRegionPt100To2000Eta0To2":["pTbalanceAll"],
"ZRegionPt0To30Eta2To2p5":["pTbalanceAll"],
"ZRegionPt30To50Eta2To2p5":["pTbalanceAll"],
"ZRegionPt50To100Eta2To2p5":["pTbalanceAll"],
"ZRegionPt100To2000Eta2To2p5":["pTbalanceAll"],
"ZRegionPt0To30Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt30To50Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt50To100Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt100To2000Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt0To30Eta3p1To5":["pTbalanceAll"],
"ZRegionPt30To50Eta3p1To5":["pTbalanceAll"],
"ZRegionPt50To100Eta3p1To5":["pTbalanceAll"],
"ZRegionPt100To2000Eta3p1To5":["pTbalanceAll"]

#"BDTNoMN1p0" : bdtInputHistos+genericHistos+signalHistosVariations+signalHistos,
#"BDTNoMN1p2" : bdtInputHistos+genericHistos+signalHistosVariations+signalHistos,
#"BDT0p8" : bdtInputHistos,
#"BDT1p0" : bdtInputHistos,
#"BDT1p1" : bdtInputHistos,
#"BDT1p2" : bdtInputHistos,
#"TwoJetsTwoMu" : genericHistos
}
histosPerSelectionFullJecs={
"SignalRegion":["BDTAtan","DNNAtan"],
"SideBand":["BDTAtanNoMass","DNNAtanNoMass"],
"ZRegion":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass"],
"ZRegionSMP":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass"],
}
histosPerSelectionBinnedJecs={
"ZRegionPt0To30Eta0To2":["pTbalanceAll"],
"ZRegionPt30To50Eta0To2":["pTbalanceAll"],
"ZRegionPt50To100Eta0To2":["pTbalanceAll"],
"ZRegionPt100To2000Eta0To2":["pTbalanceAll"],
"ZRegionPt0To30Eta2To2p5":["pTbalanceAll"],
"ZRegionPt30To50Eta2To2p5":["pTbalanceAll"],
"ZRegionPt50To100Eta2To2p5":["pTbalanceAll"],
"ZRegionPt100To2000Eta2To2p5":["pTbalanceAll"],
"ZRegionPt0To30Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt30To50Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt50To100Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt100To2000Eta2p5To3p1":["pTbalanceAll"],
"ZRegionPt0To30Eta3p1To5":["pTbalanceAll"],
"ZRegionPt30To50Eta3p1To5":["pTbalanceAll"],
"ZRegionPt50To100Eta3p1To5":["pTbalanceAll"],
"ZRegionPt100To2000Eta3p1To5":["pTbalanceAll"]
}
