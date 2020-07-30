#include <TH1F.h>
extern TH1F * wDNN2016;
extern TH1F * wDNN2017;
extern TH1F * wDNN2018;

float weightDNNSB(float dnn, int year){
 TH1F *h;
 if(year==2016) h=wDNN2016;
 if(year==2017) h=wDNN2017;
 if(year==2018) h=wDNN2018;
 return h->GetBinContent(h->FindBin(dnn));
}
