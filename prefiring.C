#include "prefiring.h"
 
TFile* f_forwardJetWeight= TFile::Open("forwardJetPtCorrection/Map_Jet_L1FinOReff_bxm1_looseJet_SingleMuon_Run2016B-H.root");
TEfficiency *h_forwardJetWeight= (TEfficiency*)f_forwardJetWeight->Get("prefireEfficiencyMap");
TFile* f_IsoEG30= TFile::Open("forwardJetPtCorrection/Map_Jet_L1IsoEG30eff_bxm1_looseJet_SingleMuon_Run2016B-H.root");
TEfficiency *h_IsoEG30Weight= (TEfficiency*)f_IsoEG30->Get("prefireEfficiencyMap");
        
TFile* f_forwardJetWeight_2017= TFile::Open("forwardJetPtCorrection/L1prefiring_jet_2017BtoF.root");
TH2F *h_forwardJetWeight_2017= (TH2F*)f_forwardJetWeight_2017->Get("L1prefiring_jet_2017BtoF");

