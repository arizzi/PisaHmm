from nail import *
import ROOT
import sys


#define some event weights
def addDefaultWeights(flow):
#   flow.Define("SelectedJet_btagWeight","vector_map(btagWeight,SelectedJet_btagCSVV2,SelectedJet_pt,SelectedJet_eta)")
#   flow.Define("btagEventWeight","isMC?(std::accumulate(SelectedJet_btagWeight.begin(),SelectedJet_btagWeight.end(),1, std::multiplies<double>())):1.f")
    flow.Define("SelectedJet_weight","Where(abs(SelectedJet_eta) < 2.4 && isMC,SelectedJet_btagSF_shape,SelectedJet_btagSF_shape*0.f+1.f)")
    flow.Define("btagEventWeight","isMC?(std::accumulate(SelectedJet_weight.begin(),SelectedJet_weight.end(),1.f, std::multiplies<double>())):1.f")
    flow.CentralWeight("genWeight")#*
    flow.CentralWeight("nnlopsWeight")
    flow.CentralWeight("btagEventWeight")
    #flow.CentralWeight("btagWeight")
    flow.CentralWeight("puWeight")

def addMuEffWeight(flow):
    #flow.AddCppCode('#include "../hmmtools/hmm_code.h"')
    #flow.Define("muEffWeight","Mu0_sf*Mu1_sf",["twoOppositeSignMuons"])
    #flow.CentralWeight("muEffWeight",["twoOppositeSignMuons"])
    flow.CentralWeight("muEffWeight",["twoOppositeSignMuons"])

def addReweightEWK(flow):
    flow.CentralWeight("EWKreweight")
    
def addQGLweight(flow):
    flow.CentralWeight("QGLweight",["twoJets"])

def addPreFiring(flow):
    flow.CentralWeight("PrefiringWeight")

