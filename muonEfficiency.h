#ifndef MUONEFFICIENCY_H
#define MUONEFFICIENCY_H

#include <TH2F.h>
#include <TFile.h>
#include <math.h> 


extern TFile* fMuEff1;
extern TFile* fMuEff2;
extern TFile* fMuEff3;
extern TFile* fMuEff4;
extern TFile* fMuEff5;
extern TH2F* hDATA1;
extern TH2F* hDATA2;
extern TH2F* hDATA3;
extern TH2F* hDATA4;
extern TH2F* hDATA5;
extern TH2F* hMC1;
extern TH2F* hMC2;
extern TH2F* hMC3;
extern TH2F* hMC4;
extern TH2F* hMC5;
/*
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
*/
float muEff (TH2F * effMap, float eta, float pt) {
    int binEta = effMap->GetXaxis()->FindBin(abs(eta));
    int binPt  = effMap->GetYaxis()->FindBin(pt);
    
    if (binEta == 0)  binEta = 1;
    if (binPt  == 0)  binPt = 1;
    if (binEta == effMap->GetNbinsY()+1)  return 1.; // this means to not consider the muon
    if (binPt  == effMap->GetNbinsX()+1)  binPt  = effMap->GetNbinsX();    
    
    return effMap->GetBinContent(binEta ,binPt);
}


float mcMuonEffCorrection(int year, int run, float pt1, float eta1, float pt2, float eta2) {
    
    if (year == 2016) {
        float efficiencyBCDEF = ( 1 - (1-muEff(hDATA1, eta1, pt1)) * (1-muEff(hDATA1, eta2, pt2)) ) / ( 1 - (1-muEff(hMC1, eta1, pt1)) * (1-muEff(hMC1, eta2, pt2)) );
        float efficiencyGH    = ( 1 - (1-muEff(hDATA2, eta1, pt1)) * (1-muEff(hDATA2, eta2, pt2)) ) / ( 1 - (1-muEff(hMC2, eta1, pt1)) * (1-muEff(hMC2, eta2, pt2)) );
        float r=   20.1/36.4*efficiencyBCDEF + 16.3/36.4*efficiencyGH;
	return isnan(r)?1.:r;
    }
         
    if (year == 2017) {
                           return  ( 1 - (1-muEff(hDATA3, eta1, pt1)) * (1-muEff(hDATA3, eta2, pt2)) ) / ( 1 - (1-muEff(hMC3, eta1, pt1)) * (1-muEff(hMC3, eta2, pt2)) );
    }
        
    if (year == 2018) {
        float efficiencyLS316361  = ( 1 - (1-muEff(hDATA4, eta1, pt1)) * (1-muEff(hDATA4, eta2, pt2)) ) / ( 1 - (1-muEff(hMC4, eta1, pt1)) * (1-muEff(hMC4, eta2, pt2)) );
        float efficiencyGR316361  = ( 1 - (1-muEff(hDATA5, eta1, pt1)) * (1-muEff(hDATA5, eta2, pt2)) ) / ( 1 - (1-muEff(hMC5, eta1, pt1)) * (1-muEff(hMC5, eta2, pt2)) );
        float r=   50.79/59.74*efficiencyLS316361 + 8.95/59.74*efficiencyGR316361; 
	return isnan(r)?1.:r;
        
    }
     
    
 return 1;    
}





#endif
