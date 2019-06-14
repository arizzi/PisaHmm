#ifndef MURESOLUTION_H
#define MURESOLUTION_H

#include <TH1F.h>
#include <TFile.h>
#include <math.h> 

//-rw-r--r-- 1 lgiannini cms 6.5K Jun 13 10:40 ngenjetweight.root
//-rw-r--r-- 1 lgiannini cms 6.5K Jun 13 11:31 softactivityweight.root


TFile* f1= TFile::Open("ngenjetweight.root");
TFile* f2= TFile::Open("softactivityweight.root");

TH1F* hratio1= (TH1F*)f1->Get("hratio");
TH1F* hratio2= (TH1F*)f2->Get("hratio");

float weightGenJet(int n){return hratio1->GetBinContent(n+1);}
float weightSofAct5(int n){return hratio2->GetBinContent(n+1);}



#endif
