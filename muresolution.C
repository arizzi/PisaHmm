#include "muresolution.h"

TFile* f_param= TFile::Open("muonresolution.root");
TH2F* hmuon= (TH2F*)f_param->Get("PtErrParametrization");

