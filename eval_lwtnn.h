#ifndef LWTNNEVAL_H
#define LWTNNEVAL_H

#include "LightweightGraph.hh"
#include "parse_json.hh"
#include <fstream>   
#include <iostream>   
#include "TString.h"

class LwtnnWrapper{
    public:
        LwtnnWrapper(std::vector<std::string> NNjsons =  {"/scratch/lgiannini/HmmPisa/model_for_lwtnn/output_fix_finalepoch.json"})
        {

//             std::ifstream input("/scratch/lgiannini/HmmPisa/model_for_lwtnn/output_fix_finalepoch.json");
//             graph_ = new lwt::LightweightGraph(lwt::parse_json_graph(input));
            
            for ( auto j: NNjsons )
            {
                std::ifstream input(j);
                graphs_.push_back(new lwt::LightweightGraph(lwt::parse_json_graph(input)));
            }
            
        }
        
        float eval(int event, std::vector <float> invec, std::vector<int> dims)
        {
            std::map<std::string, std::map<std::string, double> > inputs;
            int count=0;
            for (unsigned int i=0; i<dims.size(); i++)
            {
                inputs[Form("node_%i", i)]={};
                for (int j=0; j<dims[i]; j++)
                {
                    inputs[Form("node_%i", i)].insert(std::pair<std::string,double>(Form("variable_%i", j),invec[count]));
                    count=count+1;
                }
                
            }
            
            int which = event%(graphs_.size());
            std::map<std::string, double> outputs = graphs_[which]->compute(inputs);

            return outputs["out_0"];
        }
        
        std::vector<lwt::LightweightGraph*> graphs_;

};
extern LwtnnWrapper lwtnn;
extern LwtnnWrapper lwtnn18 ;
/*
std::vector<std::string> v = {"/scratch/lgiannini/HmmPisa/model_for_lwtnn/output_fix_finalepoch.json"} ;
LwtnnWrapper lwtnn = LwtnnWrapper(v);

std::vector<std::string> v18 = {
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt0.json",
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt1.json",
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt2.json",
"/scratch/lgiannini/CMSSW_10_4_0_pre1/src/retrainVBF3/separatebg3/prova_tutto_ok18_QGL_fold3/model_preparation/nn_evt3.json"};
LwtnnWrapper lwtnn18 = LwtnnWrapper(v18);
*/
#endif
