from nail.nail import *
import ROOT
import sys

#flow=SampleProcessing("VBF Hmumu Analysis","/scratch/arizzi/Hmm/nail/samples/6B8A2AC8-35E6-1146-B8A8-B1BA90E3F3AA.root")
#flow=SampleProcessing("VBF Hmumu Analysis","/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_Z/VBF_HToMuMu_nano2016.root")
flow=SampleProcessing("VBF Hmumu Analysis","/eos/user/a/arizzi/Hmm/data/VBF_HToMuMu_nano2018.root")

flow.SubCollection("GenLepton","GenPart",sel="(abs(GenPart_pdgId)==13 || abs(GenPart_pdgId)==11 || abs(GenPart_pdgId)==15)")
flow.MatchDeltaR("GenLepton","GenJet") 
flow.SubCollection("GenJetVBFFilter","GenJet",sel="GenJet_GenLeptonDr>0.3 || GenJet_GenLeptonIdx==-1 ")
flow.Define("GenJetVBFFilter_p4","@p4v(GenJetVBFFilter)")
flow.Selection("twoVBFFilterGenJet","nGenJetVBFFilter > 1")
flow.Selection("justPass","1") #this is a silly workaround for a problemi with central weight duplications
flow.Define("VBFFilterjj_mass","twoVBFFilterGenJet?(At(GenJetVBFFilter_p4,0)+At(GenJetVBFFilter_p4,1)).M():-1",requires=["justPass"])
#flow.Define("VBFFilterjj_mass","VBFFilterjj_p4.M()")
flow.Selection("VBFFilterFlag", "VBFFilterjj_mass>350")
flow.Selection("VBFFilterAntiFlag", "!VBFFilterFlag")

