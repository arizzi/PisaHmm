#include <TGraph.h>
#include <TFile.h>
#include <algorithm>
extern TFile* f_nn;
extern TGraph * gr_NNLOPSratio_pt_mcatnlo_0jet;
extern TGraph * gr_NNLOPSratio_pt_mcatnlo_1jet;
extern TGraph * gr_NNLOPSratio_pt_mcatnlo_2jet;
extern TGraph * gr_NNLOPSratio_pt_mcatnlo_3jet;
float evalNnlopsWeight(int njets, float hpt){
  float weight=1.;
    if (njets==0){
      weight = gr_NNLOPSratio_pt_mcatnlo_0jet->Eval(std::min(hpt,125.f));}
    if (njets==1){
      weight = gr_NNLOPSratio_pt_mcatnlo_1jet->Eval(std::min(hpt,625.f));}
    if (njets==2){
      weight = gr_NNLOPSratio_pt_mcatnlo_2jet->Eval(std::min(hpt,800.f));}
    if (njets>=3){
      weight = gr_NNLOPSratio_pt_mcatnlo_3jet->Eval(std::min(hpt,925.f));}
 return weight;
}
