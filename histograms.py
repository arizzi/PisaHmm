#define hist mapping
genericHistos=["Higgs_m","pTbalanceAll","LeadMuon_pt","LeadMuon_eta","SubMuon_pt","SubMuon_eta","QJet0_eta","QJet1_eta","QJet0_pt_touse","QJet1_pt_touse","PV_npvs","LeadingSAJet_pt","SAHT","SAHT5","nFootprintSAJet","FootHT"]
bdtInputHistos=["Mqq_log","mmjj_pt","qqDeltaEta","NSoft5","ll_zstar","Higgs_pt","theta2","mmjj_pz","MaxJetAbsEta","Higgs_m_uncalib","NSoft5New","ll_zstar_log", "Higgs_mReso","QJet0_qgl","QJet1_qgl","Jet_jetId","Jet_puId"]
signalHistosVariations=["SBClassifierNoMass","BDTAtanNoMass","SBClassifierNoMassNoNSJ","BDTAtanNoMassNoNSJ","DNNClassifierNoMass", "DNNAtanNoMass","DNN18AtanNoMass"]
signalHistos=["SBClassifier","BDTAtan","LHE_NpNLO","DNNClassifier", "DNNAtan", "DNN18Atan"]

#signalHistos=["SBClassifier"]

histosPerSelection={
#"PreSel" : genericHistos+["Mqq"],
"SignalRegion": signalHistos+ genericHistos+signalHistosVariations+bdtInputHistos+["CorrectedPrefiringWeight"],
"ZRegion": signalHistosVariations+genericHistos+bdtInputHistos,
"ZRegionSMP": signalHistosVariations+["pTbalanceAll"]+bdtInputHistos,
"SideBand" : signalHistos+signalHistosVariations+genericHistos+bdtInputHistos,
"BDT1p1" : bdtInputHistos,
"BDT1p2" : bdtInputHistos,
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
#"SignalRegion":["DNNAtan"],
#"SideBand":["DNNAtanNoMass"],
#"ZRegion":["pTbalanceAll","DNNAtanNoMass"],
#"ZRegionSMP":["pTbalanceAll","DNNAtanNoMass"],
"SignalRegion":["BDTAtan","DNNAtan","DNN18Atan"],
"SideBand":["BDTAtanNoMass","DNNAtanNoMass","DNN18AtanNoMass"],
"ZRegion":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass","DNN18AtanNoMass"],
#ZRegionSMP":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass"],
}


#quick override for missing plots
if False:
  histosPerSelectionFullJecs={}
  histosPerSelection={
"SignalRegion":["QJet0_qgl","QJet1_qgl"],
"SideBand":["QJet0_qgl","QJet1_qgl"],
"ZRegion":["QJet0_qgl","QJet1_qgl"],
  }




