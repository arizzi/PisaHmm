path2016 = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_tmp/"
path2016data = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_Z/"


samples={
#"DY105Inclusuve_2016AMCPY"     : {"files":[path2016+"DYJetsToLL_M-105To160-amcatnloFXFX_nano2016.root"],"xsec": 41.81},
#"DY105Inclusuve_2016MGPY"      : {"files":[path2016+"DYJetsToLL_M-105To160-madgraphMLM_nano2016.root"],"xsec": 41.25},

"DY105_2016AMCPY"     : {"files":[path2016+"DYJetsToLL_M-105To160-amcatnloFXFX_nano2016.root"],"xsec": 41.81, "filter": "VBFFilterAntiFlag"},
"DY105_2016MGPY"      : {"files":[path2016+"DYJetsToLL_M-105To160-madgraphMLM_nano2016.root"],"xsec": 41.25, "filter": "VBFFilterAntiFlag"},
"DY105VBF_2016AMCPY"  : {"files":[path2016+"DYJetsToLL_M-105To160-amcatnloFXFX_VBFFilter_nano2016.root"],"xsec": 41.81*0.0425242, "filter": "VBFFilterFlag"}, #this name has to change
"DY105VBF_2016MGPY"   : {"files":[path2016+"DYJetsToLL_M-105To160_VBFFilter-madgraphMLM_nano2016.root"],"xsec": 41.25*0.0419533, "filter": "VBFFilterFlag"},

"DY0J_2016AMCPY"  : {"files":[path2016+"DYJetsToLL_0J_nano2016.root"],"xsec": 4620.52},
"DY1J_2016AMCPY"  : {"files":[path2016+"DYJetsToLL_1J_nano2016.root"],"xsec":859.59},
"DY2J_2016AMCPY"  : {"files":[path2016+"DYJetsToLL_2J_nano2016.root"],"xsec":338.26},
"DYTau_2016AMCPY" : {"files":[path2016+"DYJetsToTauTau_ForcedMuDecay_nano2016.root"],"xsec":5765.40 / 3. * 0.1739 * 0.1739},
"DYM50_2016AMCPY" : {"files":[path2016+"DYJetstoLL_amc_M-50_nano2016.root"],"xsec":5765.40},

"EWKZ105_2016MGHERWIG"     : {"files":["/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_tmp/EWK_LLJJ_MLL_105-160_herwig_nano2016.root"],"xsec":0.0508896},
"EWKZ_2016MGHERWIG" : {"files":[path2016+"EWK_LLJJ_herwig_nano2016.root"],"xsec":1.664},
"EWKZ_2016MGPY"     : {"files":[path2016+"EWK_LLJJ_pythia8_nano2016.root"],"xsec":1.664},
"EWKZint_2016MGPY"  : {"files":[path2016+"EWK_LLJJ_INT_nano2016.root"],"xsec":0.128},

"STs_2016AMCPY"             : {"files":[path2016+"ST_s_nano2016.root"],"xsec":3.36},
"STwtbar_2016POWPY"         : {"files":[path2016+"ST_tW_antitop_nano2016.root"],"xsec":35.85},
"STwt_2016POWPY"            : {"files":[path2016+"ST_tW_top_nano2016.root"],"xsec":35.85},
"STtbar_2016POW_MADSPIN_PY" : {"files":[path2016+"ST_t_antitop_nano2016.root"],"xsec":80.95}, ##or 26.38!??  80.95 is for inclusive decays (used), 26.38 is for lepton decays (not used)
"STt_2016POW_MADSPIN_PY"    : {"files":[path2016+"ST_t_top_nano2016.root"],"xsec":136.02}, ##or 44.33   136.02 is for inclusive decays (used), 44.33 is for lepton decays (not used)

"data2016": {"files":[path2016data+"SingleMuon_nano2016.root"],"lumi":35900.,"data":True},

"TT_2016POWPY"      : {"files":[path2016+"TT_nano2016.root"],"xsec":809.},
"TTlep_2016POWPY"   : {"files":[path2016+"TTTo2L2Nu_nano2016.root"],"xsec":85.65},
"TTsemi_2016POWPY"  : {"files":[path2016+"TTToSemiLeptonic_nano2016.root"],"xsec":356.18677888},
#"TThad_2016POWPY"   : {"files":[path2016+"TTToHadronic_nano2016.root"],"xsec":366.20181056}, # it does not exist

"W2J_2016AMCPY"  : {"files":[path2016+"WToLNu_2J_nano2016.root"],"xsec":3172.96},
"W1J_2016AMCPY"  : {"files":[path2016+"WToLNu_1J_nano2016.root"],"xsec":8426.09},
"W0J_2016AMCPY"  : {"files":[path2016+"WToLNu_0J_nano2016.root"],"xsec":50131.98},



"WWdps_2016MGPY"    : {"files":[path2016+"WWTo2L2Nu_DoubleScattering_nano2016.root"],"xsec":1.62},
"WWJJlnln_2016MGPY" : {"files":[path2016+"WWJJToLNuLNu_EWK_nano2016.root"],"xsec":0.3452},
"WLLJJln_2016MG_MADSPIN_PY"  : {"files":[path2016+"WLLJJ_WToLNu_EWK_nano2016.root"],"xsec":0.0176},
#"WWJJlnlnNoT_2016MGPY": {"files":[path2016+"WWJJToLNuLNu_EWK_noTop_nano2016.root"],"xsec":0.3452},


#"WW2l2n_2016POWHERWIG"      : {"files":[path2016+"WWTo2L2Nu_herwigpp_nano2016.root"],"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WW2l2n_2016POWPY"          : {"files":[path2016+"WWTo2L2Nu_nano2016.root"],"xsec":118.7 * 21.34 * 21.34 / 10000.},
#"WWlnqq_2016AMC_MADSPIN_PY" : {"files":[path2016+"WWToLNuQQ_nano2016.root"],"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},



"WZ1l1n2q_2016AMCPY"            : {"files":[path2016+"WZTo1L1Nu2Q_nano2016.root"],"xsec":47.13 * 21.34 * 69.91 / 10000.},
"WZ1l3n_2016AMCPY"              : {"files":[path2016+"WZTo1L3Nu_nano2016.root"],"xsec":47.13 * 21.34 * 20.00 / 10000.},
"WZ2l2q_2016AMC_MADSPIN_PY"     : {"files":[path2016+"WZTo2L2Q_nano2016.root"],"xsec":47.13 * 6.729 * 67.41 / 10000.},
"WZ3l1n_2016POWPY"              : {"files":[path2016+"WZTo3LNu_powheg_nano2016.root"],"xsec":47.13 * 21.34 * 10.099 / 10000.},
"WZ3l1n_2016AMCPY"              : {"files":[path2016+"WZTo3LNu_nano2016.root"],"xsec":47.13 * 21.34 * 10.099 / 10000.},


#"ZZ2l2n_2016POWPY": {"files":[path2016+"ZZTo2L2Nu_nano2016.root"],"xsec":16.523 * 20.000 * 10.099 / 10000.},    # not ready yet
"ZZ2l2q_2016POWPY": {"files":[path2016+"ZZTo2L2Q_nano2016.root"],"xsec":16.523 * 2. * 6.729 * 69.91 / 10000.},
#"ZZ2q2n_2016POWPY": {"files":[path2016+"ZZTo2Q2Nu_nano2016.root"],"xsec": },    # not ready yet
#"ZZ2q2n_2016AMCPY": {"files":[path2016+"ZZTo2Q2Nu_nano2016.root"],"xsec": },    # not ready yet
#"ZZ4l_2016POWPY": {"files":[path2016+"ZZTo4L_nano2016.root"],"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet
#"ZZ4l_2016AMCPY": {"files":[path2016+"ZZTo4L_nano2016.root"],"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet


#"ZZ_2017AMCPY": {"files":[path2016+"ZZ_nano2016.root"],"xsec":16.523},
#"WZ_2017AMCPY": {"files":[path2016+"WZ_nano2016.root"],"xsec":47.13}, 
#"WW_2017AMCPY": {"files":[path2016+"WW_nano2016.root"],"xsec":118.7}, 

"ggHmm_2016AMCPY"       : {"files":[path2016+"GluGlu_HToMuMu_amc_nano2016.root"],"xsec":0.009582794}, #xsec["VBF_HToMuMu"] = 0.0008210722; xsec["GluGlu_HToMuMu"] = 0.009582794;
"ggHmm_2016POWPY"       : {"files":[path2016+"GluGlu_HToMuMu_nano2016.root"],"xsec":0.009582794},

"vbfHmm_2016POWPY"      : {"files":[path2016+"VBF_HToMuMu_nano2016.root"],"xsec":0.0008210722},
"vbfHmm_2016POWHERWIG"  : {"files":[path2016+"VBF_HToMuMu_herwigpp_nano2016.root"],"xsec":0.0008210722},
"vbfHmm_2016AMCPY"      : {"files":[path2016+"VBF_HToMuMu_amc_nano2016.root"],"xsec":0.0008210722},
"vbfHmm_2016AMCHERWIG"  : {"files":[path2016+"VBF_HToMuMu_amc_herwigpp_nano2016.root"],"xsec":0.0008210722},

"zHmm_2016POWPY"        : {"files":[path2016+"ZH_HToMuMu_nano2016.root"],"xsec":0.00019201024},
"ttHmm_2016POWPY"       : {"files":[path2016+"ttHToMuMu_nano2016.root"],"xsec":0.00011034496},
"WplusHmm_2016POWPY"    : {"files":[path2016+"WplusH_HToMuMu_nano2016.root"],"xsec":0.000182784},
"WminusHmm_2016POWPY"   : {"files":[path2016+"WminusH_HToMuMu_nano2016.root"],"xsec":0.00011593728},
#"vbfHtautau_2016POWPY"  : {"files":[path2016+"VBFHToTauTau_nano2016"],"xsec":0.23720704},

}

 
