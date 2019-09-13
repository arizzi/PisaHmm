#ifndef PREFIRING_H
#define PREFIRING_H

#include <TH2F.h>
#include <TFile.h>
#include <math.h> 
#include <TEfficiency.h>
#include <iostream>
 
extern TFile* f_forwardJetWeight;
extern TEfficiency *h_forwardJetWeight;
extern TFile* f_IsoEG30;
extern TEfficiency *h_IsoEG30Weight;
        
extern TFile* f_forwardJetWeight_2017;
extern TH2F *h_forwardJetWeight_2017;

inline float prefiringJetWeight(float year,float pt, float eta) {
    float w = 0;
    float ptToUse=pt;
    do {
      if (year==2016) w = h_forwardJetWeight->GetEfficiency(h_forwardJetWeight->FindFixBin(abs(eta),ptToUse));
      else if(year==2017) {
                                if (ptToUse>40) {
                                    w = h_forwardJetWeight_2017->GetBinContent(h_forwardJetWeight_2017->FindBin(eta,ptToUse));
                                }
                                else w = 0;
                          }
      else if (year == 2018) {w = 0;}
      else {std::cout << "era is not correct" << std::endl; w = 0;}
      ptToUse = ptToUse * 0.9;
    }
    while (w == 0 && ptToUse > 100.);
 return 1.-w;
}  


#endif
