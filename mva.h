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
/*        reader->AddVariable("ll_mass",&a);
        reader->AddVariable("MqqLog",&a);
        reader->AddVariable("mumujj_pt",&a);
        reader->AddVariable("DeltaEtaQQ",&a);
        reader->AddVariable("softActivityEWK_njets5",&a);

        reader->AddVariable("ll_zstar",&a);
        reader->AddVariable("ll_pt",&a);
        reader->AddVariable("theta2",&a);
        reader->AddVariable("impulsoZ",&a);
        reader->AddVariable("maxAbsEta",&a);
*/
//mll_MqqLog_Rpt_DEtajj_Zstar_softN5_minEtaHQ

/*        reader->AddVariable("ll_mass",&a);
        reader->AddVariable("MqqLog",&a);
        reader->AddVariable("Rpt",&a);
        reader->AddVariable("DeltaEtaQQ",&a);
        reader->AddVariable("ll_star",&a);
        reader->AddVariable("softActivityEWK_njets5",&a);
        reader->AddVariable("min(EtaHQ1,EtaHQ2)",&a);
        //reader->AddSpectator("weightEWK",&a);
       // reader->AddSpectator("genweight",&a);
        reader->BookMVA("BDTG", "BDT.xml");
	readers.push_back(reader);*/
        reader->AddVariable("Higgs_m",&a);   
        reader->AddVariable("Mqq_log",&a);
        reader->AddVariable("Rpt",&a);
        reader->AddVariable("qqDeltaEta",&a);
        reader->AddVariable("ll_zstar_log",&a);
        reader->AddVariable("NSoft5New",&a);   
        reader->AddVariable("minEtaHQ",&a);
        reader->AddVariable("qqDeltaPhi",&a);
        reader->AddVariable("QJet1_pt_touse",&a);
/*
        reader->AddVariable("ll_mass",&a);   
        reader->AddVariable("MqqLog",&a);
        reader->AddVariable("Rpt",&a);
        reader->AddVariable("DeltaEtaQQ",&a);
        reader->AddVariable("ll_zstar",&a);
        reader->AddVariable("softActivityEWK_njets5",&a);   
        reader->AddVariable("min(EtaHQ1,EtaHQ2)",&a);
        reader->AddSpectator("weightEWK",&a);
        reader->AddSpectator("genweight",&a);*/
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
extern MVAWrapper mva;
//MVAWrapper mva;

#endif
