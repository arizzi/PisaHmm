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
	    std::cout << "Constructor " << NNjsons.size() << " " << NNjsons[0] <<" "  << this <<  std::endl;
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
//	   std::cerr << "QUI" << std::endl;
//	    std::cerr << "DNN in " << invec[0] << " "<< invec[3] << " dims: " << dims.size() << " ev " << event<<  " " << graphs_.size() << " " << this <<  std::endl;
//	    for(size_t j=0; j<invec.size() ; j++) std::cout << " " << invec[j];
//	    std::cerr << std::endl;
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
/*   if (outputs["out_0"] < 1e-7 && graphs_.size() == 4) {
	    std::cout << "DNN in check " << invec[0] << " " << invec[3]  << " dims: " << dims.size() << " ev " << event<<  " " << graphs_.size() <<  std::endl;
	    for(size_t j=0; j<invec.size() ; j++) std::cout << " " << invec[j];
	    std::cout << std::endl;
	    std::cout << "DNN " << which << " " << outputs["out_0"] << " " << this << std::endl;
	    abort();
  	    }*/
            return outputs["out_0"];
        }
        
        std::vector<const lwt::LightweightGraph*> graphs_;

};
extern LwtnnWrapper lwtnn;
extern LwtnnWrapper lwtnn18 ;
extern LwtnnWrapper lwtnn_all ;
extern LwtnnWrapper lwtnn_Z ;
extern LwtnnWrapper lwtnn_withZ ;
extern LwtnnWrapper lwtnn_nov ;
extern LwtnnWrapper lwtnn_feb ;
extern LwtnnWrapper lwtnn_feb2 ;
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
