#include "nnlops.h"
TFile* f_nn= TFile::Open("NNLOPS_reweight.root");
TGraph * gr_NNLOPSratio_pt_mcatnlo_0jet= (TGraph *) f_nn->Get("gr_NNLOPSratio_pt_mcatnlo_0jet");
TGraph * gr_NNLOPSratio_pt_mcatnlo_1jet= (TGraph *) f_nn->Get("gr_NNLOPSratio_pt_mcatnlo_1jet");
TGraph * gr_NNLOPSratio_pt_mcatnlo_2jet= (TGraph *) f_nn->Get("gr_NNLOPSratio_pt_mcatnlo_2jet");
TGraph * gr_NNLOPSratio_pt_mcatnlo_3jet= (TGraph *) f_nn->Get("gr_NNLOPSratio_pt_mcatnlo_3jet");
