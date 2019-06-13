#ifndef MVA_H
#define MVA_H
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"

class MVAWrapper {
 public:
//    MVAWrapper(int ii=0) { for(int i=0;i<ii;i++) addReader();}
    MVAWrapper() {}
    void addReader(){
        TMVA::Reader * reader = new TMVA::Reader("Silent");
        reader->AddVariable("ll_mass",&a);
        reader->AddVariable("MqqLog",&a);
        reader->AddVariable("mumujj_pt",&a);
        reader->AddVariable("DeltaEtaQQ",&a);
        reader->AddVariable("softActivityEWK_njets5",&a);

        reader->AddVariable("ll_zstar",&a);
        reader->AddVariable("ll_pt",&a);
        reader->AddVariable("theta2",&a);
        reader->AddVariable("impulsoZ",&a);
        reader->AddVariable("maxAbsEta",&a);

        reader->BookMVA("BDTG", "BDT.xml");
	readers.push_back(reader);
    }


float eval(unsigned int i,std::vector<float> f){
	while(readers.size() <=i) addReader();
        return  readers[i]->EvaluateMVA(f,"BDTG");
}

        std::vector<TMVA::Reader *> readers;
        float a;
};

//MVAWrapper mva(64);
MVAWrapper mva;

#endif
