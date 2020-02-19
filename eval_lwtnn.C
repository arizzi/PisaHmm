#include <eval_lwtnn.h>
#include <mva.h>
std::vector<std::string> v = {"/scratch/lgiannini/HmmPisa/model_for_lwtnn/output_fix_finalepoch.json"} ;
LwtnnWrapper lwtnn = LwtnnWrapper(v);

std::vector<std::string> v18 = {
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt0.json",
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt1.json",
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt2.json",
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt3.json"};
LwtnnWrapper lwtnn18 = LwtnnWrapper(v18);

std::vector<std::string> vall = {
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt0_all.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt1_all.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt2_all.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt3_all.json"
};



// std::vector<std::string> vall = {
// "/scratch/mandorli/Hmumu/allYearsTraining/nn_evt0_focal.json",
// "/scratch/mandorli/Hmumu/allYearsTraining/nn_evt1_focal.json",
// "/scratch/mandorli/Hmumu/allYearsTraining/nn_evt2_focal.json",
// "/scratch/mandorli/Hmumu/allYearsTraining/nn_evt3_focal.json"
// };
LwtnnWrapper lwtnn_all = LwtnnWrapper(vall);



std::vector<std::string> vZ = {
"/scratch/mandorli/Hmumu/allYearsTraining/NNZpeak_evt0.json",
"/scratch/mandorli/Hmumu/allYearsTraining/NNZpeak_evt1.json",
"/scratch/mandorli/Hmumu/allYearsTraining/NNZpeak_evt2.json",
"/scratch/mandorli/Hmumu/allYearsTraining/NNZpeak_evt3.json"
};
LwtnnWrapper lwtnn_Z = LwtnnWrapper(vZ);


std::vector<std::string> vWithZ = {
"/scratch/mandorli/Hmumu/allYearsTraining/nn_withZpeak_evt0.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_withZpeak_evt1.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_withZpeak_evt2.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_withZpeak_evt3.json"
};
LwtnnWrapper lwtnn_withZ = LwtnnWrapper(vWithZ);


std::vector<std::string> vNov = {
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt0_nov.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt1_nov.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt2_nov.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt3_nov.json"
};
LwtnnWrapper lwtnn_nov = LwtnnWrapper(vNov);

std::vector<std::string> vFeb = {
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt0_feb.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt1_feb.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt2_feb.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt3_feb.json"
};

std::vector<std::string> vFeb2 = {
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt0_febNLO20.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt1_febNLO20.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt2_febNLO20.json",
"/scratch/mandorli/Hmumu/allYearsTraining/nn_evt3_febNLO20.json"};

LwtnnWrapper lwtnn_feb2 = LwtnnWrapper(vFeb2);
LwtnnWrapper lwtnn_feb = LwtnnWrapper(vFeb);


