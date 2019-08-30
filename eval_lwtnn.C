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
MVAWrapper mva;

