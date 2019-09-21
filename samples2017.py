path2017 = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_nanoV5/"
#/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_tmp/"
#path2018 = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_tmp/"
path2017data = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_nanoV5/"
# "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_Z/"


samples={
#"DY105Inclusive_2017AMCPY"     : {"files":[path2017+"DYJetsToLL_M-105To160-amcatnloFXFX_nano2017.root"],"xsec": 41.81, "filter": "MqqGen < 350"},
#"DY105Inclusive_2017MGPY"      : {"files":[path2017+"DYJetsToLL_M-105To160-madgraphMLM_nano2017.root"],"xsec": 41.25, "filter": "MqqGen < 350"},

"DY105_2017AMCPY"     : {"files":[path2017+"DYJetsToLL_M-105To160-amcatnloFXFX_nano2017.root"],"xsec": 41.81, "filter":  "VBFFilterAntiFlag"},
"DY105_2017MGPY"      : {"files":[path2017+"DYJetsToLL_M-105To160-madgraphMLM_nano2017.root"],"xsec": 41.25, "filter":  "VBFFilterAntiFlag"},
"DY105VBF_2017AMCPY"  : {"files":[path2017+"DYJetsToLL_M-105To160_VBFFilter-amcatnloFXFX_nano2017.root"],"xsec": 41.81*0.0425242, "filter":  "VBFFilterFlag"},
#"DY105VBF_2017AMCPYnew"  : {"files":["/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_nanoV5_v2/DYJetsToLL_M-105To160_VBFFilter-amcatnloFXFX_nano2017.root"],"xsec": 41.81*0.0425242, "filter":  "VBFFilterFlag"},
"DY105VBF_2017MGPY"   : {"files":[path2017+"DYJetsToLL_M-105To160_VBFFilter-madgraphMLM_nano2017.root"],"xsec": 41.25*0.0419533, "filter":  "VBFFilterFlag"},

"DY0J_2017AMCPY"  : {"files":[path2017+"DYJetsToLL_0J_nano2017.root"],"xsec": 4620.52},
"DY1J_2017AMCPY"  : {"files":[path2017+"DYJetsToLL_1J_nano2017.root"],"xsec":859.59},
"DY2J_2017AMCPY"  : {"files":[path2017+"DYJetsToLL_2J_nano2017.root"],"xsec":338.26},
"DYTau_2017AMCPY" : {"files":[path2017+"DYJetsToTauTau_ForcedMuDecay_nano2017.root"],"xsec":5765.40 / 3. * 0.1739 * 0.1739},
#"DYM50_2017AMCPY" : {"files":[path2017+"DYJetstoLL_amc_M-50_nano2017.root"],"xsec":5765.40},
"EWKZ105_2017MGHERWIG"     : {"files":[path2017+"EWK_LLJJ_MLL_105-160_herwig_nano2017.root"],"xsec":0.0508896},
"EWKZ_2017MGHERWIG" : {"files":[path2017+"EWK_LLJJ_herwig_nano2017.root"],"xsec":1.664}, #it does not exist yet
"EWKZ_2017MGPY"     : {"files":[path2017+"EWK_LLJJ_pythia8_nano2017.root"],"xsec":1.664},
"EWKZint_2017MGPY"  : {"files":[path2017+"EWK_LLJJ_INT_nano2017.root"],"xsec":0.128},

"STs_2017AMCPY"             : {"files":[path2017+"ST_s_nano2017.root"],"xsec":3.36},
"STwtbar_2017POWPY"         : {"files":[path2017+"ST_tW_antitop_nano2017.root"],"xsec":35.85},
"STwt_2017POWPY"            : {"files":[path2017+"ST_tW_top_nano2017.root"],"xsec":35.85},
"STtbar_2017POWPY"          : {"files":[path2017+"ST_t_antitop_nano2017.root"],"xsec":80.95}, ##or 26.38!??  80.95 is for inclusive decays (used), 26.38 is for lepton decays (not used)
"STt_2017POWPY"             : {"files":[path2017+"ST_t_top_nano2017.root"],"xsec":136.02}, ##or 44.33   136.02 is for inclusive decays (used), 44.33 is for lepton decays (not used)

"data2017": {"files":[path2017data+"SingleMuon_nano2017.root"],"lumi":41530.,"data":True},

"TT_2017AMCPY"      : {"files":[path2017+"TT_nano2017.root"],"xsec":809.},    #generator is different from 2016
"TT_2017MGPY"       : {"files":[path2017+"TT_madgraph_nano2017.root"],"xsec":809.},
"TTlep_2017POWPY"   : {"files":[path2017+"TTTo2L2Nu_nano2017.root"],"xsec":85.65},
"TTsemi_2017POWPY"  : {"files":[path2017+"TTToSemiLeptonic_nano2017.root"],"xsec":356.18677888},
"TThad_2017POWPY"   : {"files":[path2017+"TTToHadronic_nano2017.root"],"xsec":366.20181056}, # it does not exist

"W2J_2017AMCPY"  : {"files":[path2017+"WToLNu_2J_nano2017.root"],"xsec":3172.96},
#"W1J_2017AMCPY"  : {"files":[path2017+"WToLNu_1J_nano2017.root"],"xsec":8426.09}, # NANOAOD not produced yet
"W0J_2017AMCPY"  : {"files":[path2017+"WToLNu_0J_nano2017.root"],"xsec":50131.98},




#"WWdps_2017MGPY"    : {"files":[path2017+"WWTo2L2Nu_DoubleScattering_nano2017.root"],"xsec":1.62},
"WWJJlnln_2017MGPY" : {"files":[path2017+"WWJJToLNuLNu_EWK_nano2017.root"],"xsec":0.3452},
"WLLJJln_2017MG_MADSPIN_PY"  : {"files":[path2017+"WLLJJ_WToLNu_EWK_nano2017.root"],"xsec":0.0176},
#"WWJJlnlnNoT_2017MGPY": {"files":[path2017+"WWJJToLNuLNu_EWK_noTop_nano2017.root"],"xsec":0.3452},


#"WW2l2n_2017POWHERWIG"      : {"files":[path2017+"WWTo2L2Nu_nano2017.root"],"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WW2l2n_2017POWPY"          : {"files":[path2017+"WWTo2L2Nu_nano2017.root"],"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WWlnqq_2017POWPY"          : {"files":[path2017+"WWTo1L1Nu2Q_nano2017.root"],"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},
#"WWlnqq_2017POWPY"          : {"files":[path2017+"WWTo4Q_nano2017.root"],"xsec":118.7 * 67.41 * 67.41 / 10000.},      # useless




"WZ1l1n2q_2017AMCPY"            : {"files":[path2017+"WZTo1L1Nu2Q_nano2017.root"],"xsec":47.13 * 21.34 * 69.91 / 10000.},
"WZ1l3n_2017AMCPY"              : {"files":[path2017+"WZTo1L3Nu_nano2017.root"],"xsec":47.13 * 21.34 * 20.00 / 10000.},
"WZ2l2q_2017AMC_MADSPIN_PY"     : {"files":[path2017+"WZTo2L2Q_nano2017.root"],"xsec":47.13 * 6.729 * 67.41 / 10000.},
"WZ3l1n_2017POWPY"              : {"files":[path2017+"WZTo3LNu_powheg_nano2017.root"],"xsec":47.13 * 21.34 * 10.099 / 10000.},
"WZ3l1n_2017AMCPY"              : {"files":[path2017+"WZTo3LNu_nano2017.root"],"xsec":47.13 * 21.34 * 10.099 / 10000.},



"ZZ2l2n_2017POWPY": {"files":[path2017+"ZZTo2L2Nu_nano2017.root"],"xsec":16.523 * 20.000 * 10.099 / 10000.},    # not ready yet
"ZZ2l2q_2017POWPY": {"files":[path2017+"ZZTo2L2Q_nano2017.root"],"xsec":16.523 * 2. * 6.729 * 69.91 / 10000.},
#"ZZ2q2n_2017POWPY": {"files":[path2017+"ZZTo2Q2Nu_nano2017.root"],"xsec": },    # not ready yet
#"ZZ2q2n_2017AMCPY": {"files":[path2017+"ZZTo2Q2Nu_nano2017.root"],"xsec": },    # not ready yet
"ZZ4l_2017POWPY": {"files":[path2017+"ZZTo4L_nano2017.root"],"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet
#"ZZ4l_2017AMCPY": {"files":[path2017+"ZZTo4L_nano2017.root"],"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet


#"ZZ_2017AMCPY": {"files":[path2017+"ZZ_nano2017.root"],"xsec":16.523},
#"WZ_2017AMCPY": {"files":[path2017+"WZ_nano2017.root"],"xsec":47.13}, 
#"WW_2017AMCPY": {"files":[path2017+"WW_nano2017.root"],"xsec":118.7}, 

"ggHmm_2017AMCPY"       : {"files":[path2017+"GluGluHToMuMu_amc_nano2017.root"],"xsec":0.009582794}, #This name is different from 2016
"ggHmm_2017POWPY"       : {"files":[path2017+"GluGlu_HToMuMu_nano2017.root"],"xsec":0.009582794},
"ggHmm_2017POWPY2"      : {"files":[path2017+"GluGlu_HToMuMu_PSweights_nano2017.root"],"xsec":0.009582794},
"ggHmm_2017AMCPY2"      : {"files":[path2017+"GluGlu_HToMuMu_PSweights_amc_nano2017.root"],"xsec":0.009582794},

"vbfHmm_2017POWPY"      : {"files":[path2017+"VBF_HToMuMu_nano2017.root"],"xsec":0.0008210722},
"vbfHmm_2017AMCPY"      : {"files":[path2017+"VBF_HToMuMu_amc_nano2017.root"],"xsec":0.0008210722},
"vbfHmm_2017AMCPY2"     : {"files":[path2017+"VBF_HToMuMu_PSweights_amc_nano2017.root"],"xsec":0.0008210722},

"zHmm_2017POWPY"        : {"files":[path2017+"ZH_HToMuMu_nano2017.root"],"xsec":0.00019201024},
"ttHmm_2017POWPY"       : {"files":[path2017+"ttHToMuMu_nano2017.root"],"xsec":0.00011034496},
"WplusHmm_2017POWPY"    : {"files":[path2017+"WplusH_HToMuMu_nano2017.root"],"xsec":0.000182784},
"WminusHmm_2017POWPY"   : {"files":[path2017+"WminusH_HToMuMu_nano2017.root"],"xsec":0.00011593728},
#"vbfHtautau_2017POWPY"  : {"files":[path2017+"VBFHToTauTau_nano2017"],"xsec":0.23720704},

}


