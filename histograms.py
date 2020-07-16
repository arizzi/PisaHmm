#define hist mapping
genericHistos=["Higgs_m","Higgs_m38","pTbalanceAll","LeadMuon_pt","LeadMuon_eta","SubMuon_pt","SubMuon_eta","QJet0_eta","QJet1_eta","QJet0_pt_touse","QJet1_pt_touse","PV_npvs","LeadingSAJet_pt","SAHT","SAHT5","nFootprintSAJet","FootHT", "CS_theta", "CS_phi"]
bdtInputHistos=["Mqq_over400_log","Rpt","mmjj_pt","qqDeltaEta","NSoft5","ll_zstar","Higgs_pt","theta2","mmjj_pz","MaxJetAbsEta","Higgs_m_uncalib","NSoft5New","ll_zstar_log", "Higgs_mReso","QJet0_qgl","QJet1_qgl","Jet_jetId","Jet_puId"]
#signalHistosVariations=["SBClassifierNoMass","BDTAtanNoMass","SBClassifierNoMassNoNSJ","BDTAtanNoMassNoNSJ","DNNClassifierNoMass", "DNNAtanNoMass","DNN18AtanNoMass"]
#signalHistos=["SBClassifier","BDTAtan","LHE_NpNLO","DNNClassifier", "DNNAtan", "DNN18Atan"]#,"DNN18AtanNoQGL"]
signalHistosVariations=["DNN18AtanNoMass"]#,"DNN18AtanNoMass2"]
signalHistos=["DNN18Atan","DNN18AtanNoMass"]#,"DNN18Atan2"]
#signalHistosMassScan=["DNN18AtanM%4.0f"%((x*0.5+120)*10) for x in range(0,21) if x not in [10,11,12] ]
#signalHistosMassScan=["DNN18AtanM%4.0f"%((x*0.5+120)*10) for x in range(0,10) ]
signalHistosMassScan=["DNN18AtanM%4.0f"%((x*0.1+125)*10) for x in range(0,11)]
#signalHistosMassScan=["DNN18AtanM12509","DNN18AtanM12538"]
#signalHistosMassScan=["DNN18AtanM12538"]
signalHistosMassScanAll=["DNN18AtanM%4.0f"%((x*0.5+120)*10) for x in range(0,21)]+["DNN18AtanM%4.0f"%((x*0.1+125)*10) for x in range(0,11)]+["DNN18AtanM12509","DNN18AtanM12538"]

balance=["pTbalanceAll"]#"pTbalance","pTbalanceAllLog","pTbalanceLog", "pTbalanceLead","pTbalanceLeadLog"]
snapregion="SignalRegion"
#signalHistos=["SBClassifier"]

histosPerSelection={
#"PreSel" : ["Higgs_m"],
#"SignalRegionDNNWeighted" : ["Higgs_m"],
"SRplusSBDNNWeighted" : ["Higgs_m","Higgs_m38"],
#"TightMassRegion" : ["DNN18AtanNoMass"],
"SignalRegion": signalHistos+signalHistosVariations+signalHistosMassScan, #+bdtInputHistos+ genericHistos,
#"ZRegion": signalHistosVariations+balance,#+genericHistos +bdtInputHistos,
"SideBand" : signalHistosVariations, #+ ["DNN18AtanMassSpread","DNN18AtanMassSpread2"],#+genericHistos+bdtInputHistos,
#"SignalRegionT": signalHistos+signalHistosVariations+signalHistosMassScan, #+bdtInputHistos+ genericHistos,
#"ZRegionT": signalHistosVariations+balance,#+genericHistos +bdtInputHistos,
#"SideBandT" : signalHistosVariations, #+ ["DNN18AtanMassSpread","DNN18AtanMassSpread2"],#+genericHistos+bdtInputHistos,
#"ZRegionSMP": signalHistosVariations+["pTbalanceAll"]+bdtInputHistos,
#"BDT1p1" : bdtInputHistos+genericHistos,
#"BDT1p2" : bdtInputHistos+genericHistos,
}

manyZregions={
"ZRegionSLJeta0pt0":signalHistosVariations+balance,
"ZRegionSLJeta1pt0":signalHistosVariations+balance,
"ZRegionSLJeta2pt0":signalHistosVariations+balance,
"ZRegionSLJeta2pt1":signalHistosVariations+balance,
"ZRegionSLJeta3pt0":signalHistosVariations+balance,
"ZRegionSLJeta3pt1":signalHistosVariations+balance,
}
#histosPerSelection.update(manyZregions)


histosPerSelectionFullJecs={
#"SignalRegionDNNWeighted" : ["Higgs_m"],
"SignalRegionDNNWeighted" : ["Higgs_m"],
"SRplusSBDNNWeighted" : ["Higgs_m"],
"SignalRegion":signalHistos+signalHistosMassScan,
"SideBand":signalHistosVariations, #+["DNN18AtanMassSpread","DNN18AtanMassSpread2"],
#"ZRegion":signalHistosVariations+balance,
#"SignalRegionT":signalHistos+signalHistosMassScan,
#"SideBandT":signalHistosVariations, #+["DNN18AtanMassSpread","DNN18AtanMassSpread2"],
#"ZRegionT":signalHistosVariations+balance,
#"ZRegionSMP":["pTbalanceAll","DNN18AtanNoMass"],
#"SignalRegion":["BDTAtan","DNNAtan","DNN18Atan"],#,"DNN18AtanNoQGL"],
#"SideBand":["BDTAtanNoMass","DNNAtanNoMass","DNN18AtanNoMass"],
#"ZRegion":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass","DNN18AtanNoMass"],
#ZRegionSMP":["BDTAtanNoMass","pTbalanceAll","DNNAtanNoMass"],
}
#histosPerSelectionFullJecs.update(manyZregions)

#quick override for missing plots
if False:
  histosPerSelectionFullJecs={
}
  histosPerSelection={
    "SignalRegion":      ["Higgs_m_noGF","Mqq_over400_log","DNN18Atan"],#ericHistos+bdtInputHistos,
    "SideBand":      ["Higgs_m_noGF","Mqq_over400_log","DNN18Atan"],#ericHistos+bdtInputHistos,
}




