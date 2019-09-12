#ifndef MURESOLUTION_H
#define MURESOLUTION_H

#include <TH2F.h>
#include <TFile.h>
#include <math.h> 

extern TFile* f_param;
extern TH2F* hmuon;

float hRelResolution(float pt1, float eta1, float pt2, float eta2) {
    float MuonPtErr1=hmuon->GetBinContent(hmuon->FindBin( (log(pt1)),abs(eta1) ));
    float MuonPtErr2=hmuon->GetBinContent(hmuon->FindBin( (log(pt2)),abs(eta2) ));    
    return sqrt(0.5*(pow(MuonPtErr1,2)+pow(MuonPtErr2,2)));
}  

float muonRelResolution(float pt, float eta) {
    return hmuon->GetBinContent(hmuon->FindBin( (log(pt)),abs(eta) ));
}

#endif
