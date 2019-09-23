#include "muonEfficiency.h"

TFile* fMuEff1= TFile::Open("MuonEfficiency/year2016/RunBCDEF_SF_Trigger.root");
TFile* fMuEff2= TFile::Open("MuonEfficiency/year2016/RunGH_SF_Trigger.root");

TFile* fMuEff3= TFile::Open("MuonEfficiency/year2017/RunBCDEF_SF_Trigger.root");

TFile* fMuEff4= TFile::Open("MuonEfficiency/year2018/RunABCD_SF_Trigger.root");
TFile* fMuEff5= TFile::Open("MuonEfficiency/year2018/EfficienciesAndSF_2018Data_BeforeMuonHLTUpdate.root");


TH2F* hDATA1= (TH2F*)fMuEff1->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesDATA/abseta_pt_DATA");
TH2F* hDATA2= (TH2F*)fMuEff2->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesDATA/abseta_pt_DATA");
TH2F* hDATA3= (TH2F*)fMuEff3->Get("IsoMu27_PtEtaBins/efficienciesDATA/abseta_pt_DATA");
TH2F* hDATA4= (TH2F*)fMuEff4->Get("IsoMu24_PtEtaBins/efficienciesDATA/abseta_pt_DATA");
TH2F* hDATA5= (TH2F*)fMuEff5->Get("IsoMu24_PtEtaBins/efficienciesDATA/abseta_pt_DATA");

TH2F* hMC1= (TH2F*)fMuEff1->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesMC/abseta_pt_MC");
TH2F* hMC2= (TH2F*)fMuEff2->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesMC/abseta_pt_MC");
TH2F* hMC3= (TH2F*)fMuEff3->Get("IsoMu27_PtEtaBins/efficienciesMC/abseta_pt_MC");
TH2F* hMC4= (TH2F*)fMuEff4->Get("IsoMu24_PtEtaBins/efficienciesMC/abseta_pt_MC");
TH2F* hMC5= (TH2F*)fMuEff5->Get("IsoMu24_PtEtaBins/efficienciesMC/abseta_pt_MC");


