#include <TH1F.h>
#include  <TFile.h>
//TFile* fDNN2016= TFile::Open("figure/2016/H/DNN18AtanNoMass___SignalRegion_SBratio.root");
//TH1F *wDNN2016=(TH1F*)fDNN2016->Get("DNN18AtanNoMass___SignalRegionrebinned");
TFile* fDNN2016= TFile::Open("figure/2016/H/DNN18AtanNoMass___TightMassRegion_SBratio.root");
TH1F *wDNN2016=(TH1F*)fDNN2016->Get("DNN18AtanNoMass___TightMassRegionrebinned");
TFile* fDNN2017= TFile::Open("figure/2017/H/DNN18AtanNoMass___TightMassRegion_SBratio.root");
TH1F *wDNN2017=(TH1F*)fDNN2017->Get("DNN18AtanNoMass___TightMassRegionrebinned");
TFile* fDNN2018= TFile::Open("figure/2018/H/DNN18AtanNoMass___TightMassRegion_SBratio.root");
TH1F *wDNN2018=(TH1F*)fDNN2018->Get("DNN18AtanNoMass___TightMassRegionrebinned");

/*TFile* fDNN2017= TFile::Open("figure/2017/H/DNN18AtanNoMass___SignalRegion_SBratio.root");
TH1F *wDNN2017=(TH1F*)fDNN2017->Get("DNN18AtanNoMass___SignalRegionrebinned");
TFile* fDNN2018= TFile::Open("figure/2018/H/DNN18AtanNoMass___SignalRegion_SBratio.root");
TH1F *wDNN2018=(TH1F*)fDNN2018->Get("DNN18AtanNoMass___SignalRegionrebinned");
*/

