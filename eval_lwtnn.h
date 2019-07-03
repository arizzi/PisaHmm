#ifndef LWTNNEVAL_H
#define LWTNNEVAL_H

#include "LightweightGraph.hh"
#include "parse_json.hh"
#include <fstream>   
#include <iostream>   
#include "TString.h"

// variabili

// NODE0-> "MqqLog", "Rpt", "DeltaEtaQQ", "ll_zstar", "softActivityEWK_njets5", "min(EtaHQ1,EtaHQ2)", "qgl_1q", "qgl_2q",         "ll_pt","ll_pt_Log","ll_eta","Mqq","Jet2q_pt","Jet1q_pt","Jet2q_eta","Jet1q_eta","Jet2q_phi","Jet1q_phi",
           
// NODE1->  "ll_mass","deltaMRel","deltaM"

class LwtnnWrapper{
    public:
        LwtnnWrapper()
        {
//             std::ifstream input("/scratch/lgiannini/HmmPisa/model_for_lwtnn/final_file_lwtnn2.json");
            std::ifstream input("/scratch/lgiannini/HmmPisa/model_for_lwtnn/output_fix_finalepoch.json");
            graph_ = new lwt::LightweightGraph(lwt::parse_json_graph(input));
        }
        
        float eval(unsigned int slot, std::vector <float> invec, std::vector<int> dims)
        {
            std::map<std::string, std::map<std::string, double> > inputs;
            int count=0;
            for (int i=0; i<dims.size(); i++)
            {
                inputs[Form("node_%i", i)]={};
                for (int j=0; j<dims[i]; j++)
                {
                    inputs[Form("node_%i", i)].insert(std::pair<std::string,double>(Form("variable_%i", j),invec[count]));
                    count=count+1;
                }
                
            }
            
//             for (auto i: inputs["node_0"]) std::cout <<  "NODE1  " << i.first << " " << i.second << std::endl;
//             for (auto i: inputs["node_1"]) std::cout <<  "NODE0  " << i.first << " " << i.second << std::endl;
            
            std::map<std::string, double> outputs = graph_->compute(inputs);
//             std::cout << outputs["out_0"] << std::endl;
            return outputs["out_0"];
        }
        
        lwt::LightweightGraph* graph_;

};

LwtnnWrapper lwtnn;

#endif
