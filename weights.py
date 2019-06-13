from nail import *
import ROOT
import sys


#define some event weights
def addDefaultWeights(flow):
#   flow.Define("SelectedJet_btagWeight","vector_map(btagWeight,SelectedJet_btagCSVV2,SelectedJet_pt,SelectedJet_eta)")
#   flow.Define("btagEventWeight","isMC?(std::accumulate(SelectedJet_btagWeight.begin(),SelectedJet_btagWeight.end(),1, std::multiplies<double>())):1.f")
    flow.CentralWeight("genWeight")
    flow.CentralWeight("btagWeight")
    flow.CentralWeight("puWeight")

def addMuEffWeight(flow):
    #flow.AddCppCode('#include "../hmmtools/hmm_code.h"')
    flow.Define("muEffWeight","Mu0_sf*Mu1_sf",["twoOppositeSignMuons"])
    flow.CentralWeight("muEffWeight",["twoOppositeSignMuons"])

def addReweightEWK(flow):
    flow.CentralWeight("EWKreweight")
