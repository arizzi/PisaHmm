#ifndef TFEVAL_H
#define TFEVAL_H

#include "TPython.h"
#include "TInterpreter.h"

//"ll_mass", "deltaMRel", "deltaM", "ll_zstar", "ll_pt", "ll_pt_Log", "ll_eta", "MqqLog", "Mqq", "Rpt","DeltaEtaQQ", "EtaHQ1", "EtaHQ2", "Jet2q_pt", "Jet1q_pt", "Jet2q_eta", "Jet1q_eta", "Jet2q_phi", "Jet1q_phi", "softActivityEWK_njets5"

// float tfeval(unsigned int i, ROOT::VecOps::RVec<float> v)
// {   
//     TPython::Exec("import eval_function, numpy");
//     gInterpreter->ProcessLine(Form("vfr%u = ((ROOT::VecOps::RVec<float>*)(%p));",i, &v));   
//     float res = TPython::Eval(Form("eval_function.evalh5(eval_function.model, numpy.array(ROOT.vfr%u).reshape(1,-1))",i));
//     return res;
// }

// float tfeval(ROOT::VecOps::RVec<float> v)
// {   
//     TPython::Exec("import eval_function, numpy");
//     gInterpreter->ProcessLine(Form("auto vr = ((ROOT::VecOps::RVec<float>*)(%p));", &v));   
//     float res = TPython::Eval("eval_function.evalh5(eval_function.model, numpy.array(ROOT.vr).reshape(1,-1))");
//     return res;
// }
        
class TFModel{
    public:
        TFModel() {std::cout << "import eval_function, numpy" << std::endl; TPython::Exec("import eval_function, numpy");};
        
        ~TFModel() {};
      
        float tfeval(unsigned int i, ROOT::VecOps::RVec<float> v)
        {   
            
//             std::cout << modelsAtSlot.size() << std::endl;
//             while(modelsAtSlot.size()<=i) modelsAtSlot.push_back(false);
//             std::cout << modelsAtSlot.size() << std::endl;
//             std::cout << modelsAtSlot[i] << std::endl;
//             std::cout << "checkckkc" << std::endl;
//             if (!modelsAtSlot[i])
//             { 
//                 std::cout << "in IFF import eval_function, numpy" << std::endl;
//                 TPython::Exec("import eval_function, numpy");
//                 modelsAtSlot[i]=true;
//                 std::cout << modelsAtSlot[i] << std::endl;
//                 std::cout << modelsAtSlot[i] <<"done??"<< std::endl;
//             }
//             TPython::Exec("import eval_function, numpy");
            std::cout << " compute ??"<< std::endl;
            gInterpreter->ProcessLine(Form("vfr%u = ((ROOT::VecOps::RVec<float>*)(%p));",i, &v));   
            TPython::Exec("print eval_function.model");
            std::cout << " processed line ??"<< std::endl;
//             TPython::Exec(Form("print eval_function.evalh5(eval_function.model, numpy.array(ROOT.vfr%u).reshape(1,-1))",i));
            float res = TPython::Eval(Form("eval_function.evalh5(eval_function.model, numpy.array(ROOT.vfr%u).reshape(1,-1))",i));
            std::cout << res<<"  re s??"<< std::endl;
            return res;
        };    
        
    private:
        std::vector <bool> modelsAtSlot;
        
};

TFModel tfmodel;

#endif
