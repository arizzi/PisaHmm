from nail import *
import ROOT
import sys


def addLheScale(flow):  
    flow.Define("LHERenUp","LHEScaleWeightSafe[6+int(nLHEScaleWeight>8)+int(nLHEScaleWeight>30)*27]*lhefactor")
    flow.Define("LHERenDown","LHEScaleWeightSafe[1+int(nLHEScaleWeight>30)*4]*lhefactor")
    flow.Define("LHEFacUp","LHEScaleWeightSafe[4+int(nLHEScaleWeight>8)+int(nLHEScaleWeight>30)*19]*lhefactor")
    flow.Define("LHEFacDown","LHEScaleWeightSafe[3+int(nLHEScaleWeight>30)*12]*lhefactor")
    flow.VariationWeight("LHERenUp")
    flow.VariationWeight("LHERenDown")
    flow.VariationWeight("LHEFacUp")
    flow.VariationWeight("LHEFacDown")
 

def addLhePdf(flow):

    flow.Define("LHEPdfSquaredSum","sqrt(Sum((LHEPdfWeight*lhefactor-1.f)*(LHEPdfWeight*lhefactor-1.f)))")
    flow.Define("LHEPdfRMS","nLHEPdfWeight>0?LHEPdfSquaredSum/sqrt(nLHEPdfWeight):0.f")
    flow.Define("LHEPdfUp","LHEPdfHasHessian?(1.+LHEPdfSquaredSum):(1.+LHEPdfRMS)")	
    flow.Define("LHEPdfDown","LHEPdfHasHessian?(1.-LHEPdfSquaredSum):(1.-LHEPdfRMS)")	
    flow.VariationWeight("LHEPdfUp")
    flow.VariationWeight("LHEPdfDown")
    for i in range(0,110):
        flow.Define("LHEPdf%s"%i,"nLHEPdfWeight>%s?LHEPdfWeight[%s]:0."%(i,i))
        flow.VariationWeight("LHEPdf%s"%i)
	
	

def addPSWeights(flow):
     flow.Define("PSWeightToFix","PSWeight[0]!=1.0f && genWeight!=LHEWeight_originalXWGTUP ")
     flow.Define("PSWeightISRDown","(!PSWeightToFix)?PSWeight[0]:PSWeight[0]*LHEWeight_originalXWGTUP")
     flow.Define("PSWeightFSRDown","(!PSWeightToFix)?PSWeight[1]:PSWeight[1]*LHEWeight_originalXWGTUP")
     flow.Define("PSWeightISRUp","(!PSWeightToFix)?PSWeight[2]:PSWeight[2]*LHEWeight_originalXWGTUP")
     flow.Define("PSWeightFSRUp","(!PSWeightToFix)?PSWeight[3]:PSWeight[3]*LHEWeight_originalXWGTUP")
     flow.VariationWeight("PSWeightISRUp")
     flow.VariationWeight("PSWeightISRDown")
     flow.VariationWeight("PSWeightFSRUp")
     flow.VariationWeight("PSWeightFSRDown")

def addSTXS(flow):
    sthsNames=["Yield","PTH200","Mjj60","Mjj120","Mjj350","Mjj700","Mjj1000","Mjj1500","PTH25","JET01"]
#    flow.AddExternalCode(header="qq2Hqq_uncert_scheme.h",cppfiles=["qq2Hqq_uncert_scheme.cpp"],ipaths=["."])
    #double vbf_uncert_stage_1_1(int source, int event_STXS, double Nsigma=1.0);
    for i in range(10):
	flow.Define("THU_VBF_"+sthsNames[i]+"Up","vbf_uncert_stage_1_1(%d,HTXS_stage1_1_fine_cat_pTjet30GeV,1.)"%i)
	flow.Define("THU_VBF_"+sthsNames[i]+"Down","vbf_uncert_stage_1_1(%d,HTXS_stage1_1_fine_cat_pTjet30GeV,-1.)"%i)
        flow.VariationWeight("THU_VBF_"+sthsNames[i]+"Up")
        flow.VariationWeight("THU_VBF_"+sthsNames[i]+"Down")


def addBtag(flow):
    btagsys=["Jet_btagSF_shape_up_jes","Jet_btagSF_shape_down_jes","Jet_btagSF_shape_up_lf","Jet_btagSF_shape_down_lf","Jet_btagSF_shape_up_hf","Jet_btagSF_shape_down_hf","Jet_btagSF_shape_up_hfstats1","Jet_btagSF_shape_down_hfstats1","Jet_btagSF_shape_up_hfstats2","Jet_btagSF_shape_down_hfstats2","Jet_btagSF_shape_up_lfstats1","Jet_btagSF_shape_down_lfstats1","Jet_btagSF_shape_up_lfstats2","Jet_btagSF_shape_down_lfstats2","Jet_btagSF_shape_up_cferr1","Jet_btagSF_shape_down_cferr1","Jet_btagSF_shape_up_cferr2","Jet_btagSF_shape_down_cferr2"]
    names=[x[17:] for x in btagsys]
    print "Adding btag systematics",names
    for i in  names :
       flow.Define("SelectedJet_weight_%s"%i,"Where(abs(SelectedJet_eta) < 2.4 && isMC,SelectedJet_btagSF_shape_%s,SelectedJet_btagSF_shape*0.f+1.f)"%i)
       name=i
       if "up_" in i : 
	  name=i.replace("up_","")+"Up"
       if "down_" in i : 
	  name=i.replace("down_","")+"Down"
       
       flow.Define("btagEventWeight_%s"%name,"isMC?(std::accumulate(SelectedJet_weight_%s.begin(),SelectedJet_weight_%s.end(),1.f, std::multiplies<double>())):1.f"%(i,i))
       flow.VariationWeight("btagEventWeight_%s"%name,"btagEventWeight")

    pass
#    flow.Define("SelectedJet_btagWeight_up","vector_map(btagWeightUp,SelectedJet_btagCSVV2,SelectedJet_pt,SelectedJet_eta)")
    #flow.Define("btagEventWeightUp","std::accumulate(SelectedJet_btagWeight.begin(),SelectedJet_btagWeight.end(),1, std::multiplies<double>())")
#    flow.Systematic("BTagUp","SelectedJet_btagWeight","SelectedJet_btagWeight_up")
   #flow.createVariationBranch("BTagUp",["btagWeight"])
#    flow.VariationWeight("btagEventWeight__syst__BTagUP","btagEventWeight")


def addMuScale(flow):
#Define Systematic variations
    flow.Systematic("MuScaleDown","Muon_corrected_pt","Muon_correctedDown_pt") #name, target, replacement
    flow.Systematic("MuScaleUp","Muon_corrected_pt","Muon_correctedUp_pt") #name, target, replacement


def addBasicJecs(flow):
   if True:
      # flow.Systematic("JERDown","Jet_pt_touse","Jet_pt_jerDown") #name, target, replacement
      # flow.Systematic("JERUp","Jet_pt_touse","Jet_pt_jerUp") #name, target, replacement
      # flow.Systematic("JESDown","Jet_pt_touse","Jet_pt_jesTotalDown") #name, target, replacement
      # flow.Systematic("JESUp","Jet_pt_touse","Jet_pt_jesTotalUp") #name, target, replacement
      # flow.Systematic("WithJER","Jet_pt_touse","Jet_pt_nom") #name, target, replacement
      # #flow.Systematic("noJER","Jet_pt_touse","Jet_pt") #name, target, replacement
      # flow.Systematic("WithOutJER","Jet_pt_touse","Jet_pt") #name, target, replacement
       flow.Define("Jet_genPt","TakeDef(GenJet_pt,Jet_genJetIdx,Jet_pt)") 
       flow.Define("Jet_jerSF","(Jet_pt_nom-Jet_genPt)/(Jet_pt-Jet_genPt+(Jet_pt==Jet_genPt)*(Jet_pt_nom-Jet_pt))") 
       flow.Define("Jet_jerDownSF","(Jet_pt_jerDown-Jet_genPt)/(Jet_pt-Jet_genPt+(Jet_pt==Jet_genPt)*10.f)") 
       flow.Define("Jet_jerUpSF","(Jet_pt_jerUp-Jet_genPt)/(Jet_pt-Jet_genPt+(Jet_pt==Jet_genPt)*10.f)") 
       flow.Define("Jet_pt_jerDown_touse","Jet_genPt+(Jet_pt_touse-Jet_genPt)*(Jet_jerDownSF/Jet_jerSF)") 
       flow.Define("Jet_pt_jerUp_touse","Jet_genPt+(Jet_pt_touse-Jet_genPt)*(Jet_jerUpSF/Jet_jerSF)+(Jet_genPt==Jet_pt)*Map(Jet_pt, [](float sigma) {return float(gRandom->Gaus(0,0.15*sigma));} )") 
       flow.Define("Jet_pt_jesTotalDown_touse","Jet_pt_touse*Jet_pt_jesTotalDown/Jet_pt_nom") 
       flow.Define("Jet_pt_jesTotalUp_touse","Jet_pt_touse*Jet_pt_jesTotalUp/Jet_pt_nom") 
#       flow.Define("Jet_pt_jerDown_touseLimited","((Jet_pt_jerDown_touse/Jet_pt_touse)>0.8&& (Jet_pt_jerDown_touse/Jet_pt_touse)<1.2)?Jet_pt_jerDown_touse:Jet_pt_touse"	
#       flow.Define("Jet_pt_jerDown_touseLimited","((Jet_pt_jerDown_touse/Jet_pt_touse)>0.8&& (Jet_pt_jerDown_touse/Jet_pt_touse)<1.2)?Jet_pt_jerDown_touse:Jet_pt_touse"	

       flow.Systematic("JERDown","Jet_pt_touse","Jet_pt_jerDown_touse") #name, target, replacement 
#      flow.Systematic("JERUp","Jet_pt_touse","Jet_pt_jerUp_touse") #name, target, replacement 
       flow.Systematic("JERUp","Jet_pt_touse","Jet_pt_nom") #name, target, replacement
       flow.Systematic("JESDown","Jet_pt_touse","Jet_pt_jesTotalDown_touse") #name, target, replacement 
       flow.Systematic("JESUp","Jet_pt_touse","Jet_pt_jesTotalUp_touse") #name, target, replacement 
       #flow.Systematic("WithJER","Jet_pt_touse","Jet_pt_nom") #name, target, replacement
   else:
       flow.Define("Jet_pt_jerDown_touse","Where(Jet_genJetIdx>=0,Jet_pt_jerDown,Jet_pt_touse)") #protectd against crazy values
       flow.Systematic("JERDown","Jet_pt_touse","Jet_pt_jerDown_touse") #name, target, replacement
       flow.Systematic("JERUp","Jet_pt_touse","Jet_pt_jerUp") #name, target, replacement
       flow.Systematic("JESDown","Jet_pt_touse","Jet_pt_jesTotalDown") #name, target, replacement
       flow.Systematic("JESUp","Jet_pt_touse","Jet_pt_jesTotalUp") #name, target, replacement

       flow.Define("Jet_pt_jerUp_touse","Jet_pt_jerUp")




def addDecorrelatedJER(flow):
       etabins=[0,1.93,2.5,3.139]
       ptbins=[0,50]
       etacutstrings=[]
       ptcutstrings=[]
       for i,e in enumerate(etabins) :
	  cut="abs(Jet_eta)>%s"%e
	  if(i+1<len(etabins)): cut+="&&abs(Jet_eta)<=%s"%(etabins[i+1])
	  etacutstrings.append(cut)
       for i,e in enumerate(ptbins) :
	  cut="Jet_pt>%s"%e
	  if(i+1<len(ptbins)): cut+="&&Jet_pt<=%s"%(ptbins[i+1])
	  ptcutstrings.append(cut)

       for i,eta in enumerate(etacutstrings):
	  for j,pt in enumerate(ptcutstrings):
	    if i<2:
	       if j!=0:
		   continue  #single pt bin for central eta as JME prescribed
	       cutstring="(%s)"%(eta)
	    else :
	       cutstring="(%s)&&(%s)"%(eta,pt)
	    print "Jer cutstring",cutstring
	    name="eta%spt%s"%(i,j)
            #flow.Systematic("JER%sUp"%name,"Jet_pt_touse","Where(%s,Jet_pt_jerUp_touse,Jet_pt_touse)"%cutstring) #name, target, replacement
            flow.Systematic("JER%sDown"%name,"Jet_pt_touse","Where(%s,Jet_pt_jerDown_touse,Jet_pt_touse)"%cutstring) #name, target, replacement 
            flow.Systematic("JER%sUp"%name,"Jet_pt_touse","Where(%s,Jet_pt_nom,Jet_pt_touse)"%cutstring) #name, target, replacement
            flow.Systematic("JER%sMatchDown"%name,"Jet_pt_touse","Where(%s,Jet_pt_jerDown_touse,Jet_pt_touse)"%(cutstring+"&&Jet_genJetIdx>=0")) #name, target, replacement 
            flow.Systematic("JER%sMatchUp"%name,"Jet_pt_touse","Where(%s,Jet_pt_nom,Jet_pt_touse)"%(cutstring+"&&Jet_genJetIdx>=0")) #name, target, replacement
            flow.Systematic("JER%sNotMatchDown"%name,"Jet_pt_touse","Where(%s,Jet_pt_jerDown_touse,Jet_pt_touse)"%(cutstring+"&&Jet_genJetIdx<0")) #name, target, replacement 
            flow.Systematic("JER%sNotMatchUp"%name,"Jet_pt_touse","Where(%s,Jet_pt_nom,Jet_pt_touse)"%(cutstring+"&&Jet_genJetIdx<0")) #name, target, replacement
	  
import jesnames
def addCompleteJecs(flow,year):
    for j in getattr(jesnames,"jesnames"+year):
       print "jes:",year, j
       flow.Define("%s_touse"%j,"Jet_pt_touse*%s/Jet_pt_nom"%j)
       flow.Systematic(j[7:],"Jet_pt_touse","%s_touse"%j)



def addPUvariation(flow):
    flow.VariationWeight("puWeightDown","puWeight")  #name of the replacement, target
    flow.VariationWeight("puWeightUp","puWeight") 

def addQGLvariation(flow):
    flow.Define("QGLweightDown","1.")
    flow.Define("QGLweightUp","QGLweight*QGLweight")
    flow.VariationWeight("QGLweightDown","QGLweight")  #name of the replacement, target
    flow.VariationWeight("QGLweightUp","QGLweight")

def addPreFiringVariation(flow):
    flow.VariationWeight("PrefiringWeightDown","PrefiringWeight")
    flow.VariationWeight("PrefiringWeightUp","PrefiringWeight")
 
