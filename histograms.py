#define hist mapping
genericHistos=["Higgs_m","pTbalanceAll","LeadMuon_pt","LeadMuon_eta","SubMuon_pt","SubMuon_eta","QJet0_eta","QJet1_eta","QJet0_pt_touse","QJet1_pt_touse","PV_npvs","LeadingSAJet_pt","SAHT","SAHT5","nFootprintSAJet","FootHT", "CS_theta", "CS_phi"]
bdtInputHistos=["Mqq_log","Rpt","mmjj_pt","qqDeltaEta","NSoft5","ll_zstar","Higgs_pt","theta2","mmjj_pz","MaxJetAbsEta","Higgs_m_uncalib","NSoft5New","ll_zstar_log", "Higgs_mReso","QJet0_qgl","QJet1_qgl","Jet_jetId","Jet_puId"]
#signalHistosVariations=["SBClassifierNoMass","BDTAtanNoMass","SBClassifierNoMassNoNSJ","BDTAtanNoMassNoNSJ","DNNClassifierNoMass", "DNNAtanNoMass","DNN18AtanNoMass"]
#signalHistos=["SBClassifier","BDTAtan","LHE_NpNLO","DNNClassifier", "DNNAtan", "DNN18Atan"]#,"DNN18AtanNoQGL"]
signalHistosVariations=["DNN18AtanNoMass"]
signalHistos=["DNN18Atan"]

snapregion="SignalRegion"
#signalHistos=["SBClassifier"]

histosPerSelection={
"PreSel" : ["Higgs_m"],
"SignalRegion": signalHistos+signalHistosVariations+bdtInputHistos+ genericHistos,
"ZRegion": signalHistosVariations+["pTbalanceAll"]+genericHistos +bdtInputHistos,
#"ZRegionSMP": signalHistosVariations+["pTbalanceAll"]+bdtInputHistos,
"SideBand" : signalHistosVariations+genericHistos+bdtInputHistos,
#"BDT1p1" : bdtInputHistos+genericHistos,
#"BDT1p2" : bdtInputHistos+genericHistos,
}
histosPerSelectionFullJecs={
"SignalRegion":signalHistos,
"SideBand":signalHistosVariations,
"ZRegion":signalHistosVariations+["pTbalanceAll"],
#"ZRegionSMP":["pTbalanceAll","DNN18AtanNoMass"],
#"SignalRegion":["BDTAtan","DNNAtan","DNN18Atan"],#,"DNN18AtanNoQGL"],
#"SideBand":["BDTAtanNoMass","DNNAtanNoMass","DNN18AtanNoMass"],
#"ZRegion":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass","DNN18AtanNoMass"],
#ZRegionSMP":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass"],
}


#quick override for missing plots
if False:
  histosPerSelectionFullJecs={
}
  histosPerSelection={
    "SignalRegion":      ["Higgs_m","DNN18Atan"],#ericHistos+bdtInputHistos,
}




