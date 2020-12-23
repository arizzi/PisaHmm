import json
f=open("/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt") 
j=json.load(f) 
f=open("/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt") 
j.update(json.load(f) )
f=open("/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt") 
j.update(json.load(f) )

import ROOT    
m=ROOT.map("int","std::vector<std::pair<int,int>>")()
for run in j :
   for rang in j[run] :
       p=ROOT.pair("int","int")(rang[0],rang[1])
       m[int(run)].push_back(p)

passJsonfunc='''
std::map<int,std::vector<std::pair<int,int>>> jsonMap;
void setJsonMap(const std::map<int,std::vector<std::pair<int,int>>> & m){
 jsonMap=m;
}
bool passJson(int run, int lumi){
  for(auto r : jsonMap[run]) {
     if(r.first<= lumi and r.second >= lumi) return true; }

  return false;
}

'''
ROOT.gInterpreter.Declare(passJsonfunc)
ROOT.setJsonMap(m)

print(ROOT.passJson(1,1))

