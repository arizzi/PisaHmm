from nail.nail import *
import ROOT
import sys

#flow=SampleProcessing("VBF Hmumu Analysis","/scratch/arizzi/Hmm/nail/samples/6B8A2AC8-35E6-1146-B8A8-B1BA90E3F3AA.root")
flow=SampleProcessing("VBF Hmumu Analysis","/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_4/vbfHmm_2016AMCPY.root")
flow.AddExpectedInput("year","int")
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

flow.SubCollection("SelJet","Jet",'''
        (year != 2017 ||  Jet_puId17 > 6 || abs(Jet_eta) < 2.6 || abs(Jet_eta) > 3.0 ) && 
        Jet_pt > 25. && ( Jet_pt > 50 
        || (  Jet_puId17  > 0  && year==2017)
        || ((Jet_puId ) > 0 && year!=2017 ) )
         &&   Jet_jetId  > 0  && abs(Jet_eta) < 4.7  &&  
        (Jet_muonIdx1==-1 || TakeDef(Muon_pfRelIso04_all,Jet_muonIdx1,100) > 0.25 || abs(TakeDef(Muon_pt,Jet_muonIdx1,0)) < 20 || abs(TakeDef(Muon_mediumId,Jet_muonIdx1,0) == 0 )) &&
        (Jet_muonIdx2==-1 || TakeDef(Muon_pfRelIso04_all,Jet_muonIdx2,100) > 0.25 || abs(TakeDef(Muon_pt,Jet_muonIdx2,0)) < 20 || abs(TakeDef(Muon_mediumId,Jet_muonIdx2,0) == 0 )) 
        ''')
flow.Define("J0Match","At(SelJet_genJetIdx,0,-1)>=0 ")
flow.Define("J1Match","At(SelJet_genJetIdx,1,-1)>=0 ")
flow.Selection("J2","J0Match and J1Match")

#flow.Selection("DY2JVBF", "LHE_Njets>=2 && VBFFilterFlag", requires=["VBFFilterFlag"])
#flow.Selection("DY01JVBF", "LHE_Njets<2 && VBFFilterFlag", requires=["VBFFilterFlag"])
#flow.Selection("DY2JAntiVBF", "LHE_Njets>=2 && VBFFilterAntiFlag", requires=["VBFFilterAntiFlag"])
#flow.Selection("DY01JAntiVBF", "LHE_Njets<2 && VBFFilterAntiFlag", requires=["VBFFilterAntiFlag"])

flow.Selection("DY2JVBF", "J2 && VBFFilterFlag", requires=["VBFFilterFlag"])
flow.Selection("DY01JVBF", "!J2 && VBFFilterFlag", requires=["VBFFilterFlag"])
flow.Selection("DY2JAntiVBF", "J2 && VBFFilterAntiFlag", requires=["VBFFilterAntiFlag"])
flow.Selection("DY01JAntiVBF", "!J2 && VBFFilterAntiFlag", requires=["VBFFilterAntiFlag"])

