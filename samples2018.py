path2018 = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_Z/"

samples={
#"DY105Inclusuve_2018AMCPY"     : {"files":[path2018+"DYJetsToLL_M-105To160-amcatnloFXFX_nano2018.root"],"xsec": 41.81},
#"DY105Inclusuve_2018MGPY"      : {"files":[path2018+"DYJetsToLL_M-105To160-madgraphMLM_nano2018.root"],"xsec": 41.25},

"DY105_2018AMCPY"     : {"files":[path2018+"DYJetsToLL_M-105To160-amcatnloFXFX_nano2018.root"],"xsec": 41.81, "filter": "VBFFilterAntiFlag"},
"DY105_2018MGPY"      : {"files":[path2018+"DYJetsToLL_M-105To160-madgraphMLM_nano2018.root"],"xsec": 41.25, "filter": "VBFFilterAntiFlag"},
"DY105VBF_2018AMCPY"  : {"files":[path2018+"DYJetsToLL_M-105To160-amcatnloFXFX_VBFFilter_nano2018.root"],"xsec": 41.81*0.0425242, "filter": "VBFFilterFlag"}, #this name has to change
"DY105VBF_2018MGPY"   : {"files":[path2018+"DYJetsToLL_M-105To160-madgraphMLM_VBFFilter_nano2018.root"],"xsec": 41.25*0.0419533, "filter": "VBFFilterFlag"},

"DY0J_2018AMCPY"  : {"files":[path2018+"DYJetsToLL_0J_nano2018.root"],"xsec": 4620.52},
"DY1J_2018AMCPY"  : {"files":["/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_Z/DYJetsToLL_1J_nano2017.root"],"xsec":859.59},    # DY1J 2018 NANOAOD does not exist yet 
"DY2J_2018AMCPY"  : {"files":[path2018+"DYJetsToLL_2J_nano2018.root"],"xsec":338.26},
"DYM50_2018AMCPY" : {"files":[path2018+"DYJetstoLL_amc_M-50_nano2018.root"],"xsec":5765.40},

#"EWKZ_2018MGHERWIG" : {"files":[path2018+"EWK_LLJJ_herwig_nano2018.root"],"xsec":1.664},   # DY1J 2018 NANOAOD does not exist yet 
"EWKZ_2018MGPY"     : {"files":[path2018+"EWK_LLJJ_pythia8_nano2018.root"],"xsec":1.664},
"EWKZint_2018MGPY"  : {"files":[path2018+"EWK_LLJJ_INT_nano2018.root"],"xsec":0.128},

"STs_2018AMCPY"             : {"files":[path2018+"ST_s_nano2018.root"],"xsec":3.36},
"STwtbar_2018POWPY"         : {"files":[path2018+"ST_tW_antitop_nano2018.root"],"xsec":35.85},
"STwt_2018POWPY"            : {"files":[path2018+"ST_tW_top_nano2018.root"],"xsec":35.85},
"STtbar_2018POWPY"          : {"files":[path2018+"ST_t_antitop_nano2018.root"],"xsec":80.95}, ##or 26.38!??  80.95 is for inclusive decays (used), 26.38 is for lepton decays (not used)
"STt_2018POWPY"             : {"files":[path2018+"ST_t_top_nano2018.root"],"xsec":136.02}, ##or 44.33   136.02 is for inclusive decays (used), 44.33 is for lepton decays (not used)


#"data": {"files":[path2018+"SingleMuon_nano2018.root"],"lumi":59970.,"data":True},


"TT_2018AMCPY"      : {"files":[path2018+"TT_nano2018.root"],"xsec":809.},    #generator is different from 2016
"TT_2018MGPY"       : {"files":[path2018+"TT_madgraph_nano2018.root"],"xsec":809.},
"TTlep_2018POWPY"   : {"files":[path2018+"TTTo2L2Nu_nano2018.root"],"xsec":85.65},
"TTsemi_2018POWPY"  : {"files":[path2018+"TTToSemiLeptonic_nano2018.root"],"xsec":356.18677888},
"TThad_2018POWPY"   : {"files":[path2018+"TTToHadronic_nano2018.root"],"xsec":366.20181056}, # it does not exist


"W2J_2018AMCPY"  : {"files":[path2018+"WToLNu_2J_nano2018.root"],"xsec":3172.96},
#"W1J_2018AMCPY"  : {"files":[path2018+"WToLNu_1J_nano2018.root"],"xsec":8426.09},
"W0J_2018AMCPY"  : {"files":[path2018+"WToLNu_0J_nano2018.root"],"xsec":50131.98},



"WWdps_2018MGPY"             : {"files":[path2018+"WWTo2L2Nu_DoubleScattering_nano2018.root"],"xsec":1.62},
"WWJJlnln_2018MGPY"          : {"files":[path2018+"WWJJToLNuLNu_EWK_nano2018.root"],"xsec":0.3452},
"WLLJJln_2018MG_MADSPIN_PY"  : {"files":[path2018+"WLLJJ_WToLNu_EWK_nano2018.root"],"xsec":0.0176},
#"WWJJlnlnNoT_2018MGPY"       : {"files":[path2018+"WWJJToLNuLNu_EWK_noTop_nano2018.root"],"xsec":0.3452},



"WW2l2n_2018POWPY"          : {"files":[path2018+"WWTo2L2Nu_nano2018.root"],"xsec":118.7 * 21.34 * 21.34 / 10000.},
#"WW2l2n_PSw_2018POWPY"      : {"files":[path2018+"WWTo2L2Nu_PSweights_nano2018.root"],"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WWlnqq_2018POWPY"          : {"files":[path2018+"WWTo1L1Nu2Q_nano2018.root"],"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},
#"WWlnqq_2018AMC_MADSPIN_PY" : {"files":[path2018+"WWTo1L1Nu2Q_amc_nano2018.root"],"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},



"WZ1l3n_2018AMCPY"              : {"files":[path2018+"WZTo1L3Nu_nano2018.root"],"xsec":47.13 * 21.34 * 20.00 / 10000.},
"WZ2l2q_2018AMC_MADSPIN_PY"     : {"files":[path2018+"WZTo2L2Q_nano2018.root"],"xsec":47.13 * 6.729 * 67.41 / 10000.},
"WZ3l1n_2018POWPY"              : {"files":[path2018+"WZTo3LNu_powheg_nano2018.root"],"xsec":47.13 * 21.34 * 10.099 / 10000.},
#"WZ3l1n_2018AMCPY"              : {"files":[path2018+"WZTo3LNu_nano2018.root"],"xsec":47.13 * 21.34 * 10.099 / 10000.},



"ZZ2l2n_2018POWPY": {"files":[path2018+"ZZTo2L2Nu_nano2018.root"],"xsec":16.523 * 20.000 * 10.099 / 10000.},    
"ZZ2l2q_2018POWPY": {"files":[path2018+"ZZTo2L2Q_nano2018.root"],"xsec":16.523 * 2. * 6.729 * 69.91 / 10000.},
"ZZ4l_2018POWPY": {"files":[path2018+"ZZTo4L_nano2018.root"],"xsec":16.523 * 10.099 * 10.099 / 10000.},    


#"ZZ_2018AMCPY": {"files":[path2018+"ZZ_nano2018.root"],"xsec":16.523},
#"WZ_2018AMCPY": {"files":[path2018+"WZ_nano2018.root"],"xsec":47.13}, 
#"WW_2018AMCPY": {"files":[path2018+"WW_nano2018.root"],"xsec":118.7}, 


"ggHmm_2018AMCPY"       : {"files":[path2018+"GluGlu_HToMuMu_amc_nano2018.root"],"xsec":0.009582794}, #xsec["VBF_HToMuMu"] = 0.0008210722; xsec["GluGlu_HToMuMu"] = 0.009582794;
"ggHmm_2018POWPY"       : {"files":[path2018+"GluGlu_HToMuMu_nano2018.root"],"xsec":0.009582794},

"vbfHmm_2018POWPY"      : {"files":[path2018+"VBF_HToMuMu_nano2018.root"],"xsec":0.0008210722},
#"vbfHmm_PSw_2018POWPY"      : {"files":[path2018+"VBF_HToMuMu_nano2018.root"],"xsec":0.0008210722}, # it exists but it has not been hadded
"vbfHmm_2018AMCPY"      : {"files":[path2018+"VBF_HToMuMu_amc_nano2018.root"],"xsec":0.0008210722},


"zHmm_2018POWPY"        : {"files":[path2018+"ZH_HToMuMu_nano2018.root"],"xsec":0.0008210722},
"ttHmm_2018POWPY"       : {"files":[path2018+"ttHToMuMu_nano2018.root"],"xsec":0.0008210722},
"WplusHmm_2018POWPY"    : {"files":[path2018+"WplusH_HToMuMu_nano2018.root"],"xsec":0.0008210722},
"WminusHmm_2018POWPY"   : {"files":[path2018+"WminusH_HToMuMu_nano2018.root"],"xsec":0.0008210722},


}






