#path2016 = "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2016_nanoV5/"
#path2016 = "/scratchssd/mandorli/Hmumu/fileSkim2016_FSR/"
#/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_tmp/"
#path2016data = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2016_nanoV5/"
#path2016data = "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2016_nanoV5/"
#path2016data = "/scratchssd/mandorli/Hmumu/fileSkim2016_FSR/"

#path2016     = "/scratchssd/mandorli/Hmumu/fileSkimFromNanoAOD/PROD_6_2/" 
path2016 = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_4/" #reduced JES
#path2016     = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_10_0/"
path2016data = path2016
#path2016data = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_12_0/"

samples={
#"DY105Inclusuve_2016AMCPY"     : {"xsec": 41.81},
#"DY105Inclusuve_2016MGPY"      : {"xsec": 41.25},

"DY105J01_2016AMCPY"     : {"xsec": 47.17, "filter":  "DY01JAntiVBF","nameforfile":"DY105_2016AMCPY"},
"DY105J2_2016AMCPY"     : {"xsec": 47.17, "filter":  "DY2JAntiVBF", "nameforfile":"DY105_2016AMCPY"},
"DY105VBFJ01_2016AMCPY"  : {"xsec": 1.77, "filter":  "DY01JVBF", "nameforfile":"DY105VBF_2016AMCPY"},
"DY105VBFJ2_2016AMCPY"  : {"xsec": 1.77, "filter":  "DY2JVBF", "nameforfile":"DY105VBF_2016AMCPY"},


"DY105_2016AMCPY"     : {"xsec": 47.17, "filter": "VBFFilterAntiFlag"},
"DY105_2016MGPY"      : {"xsec": 47.17, "filter": "VBFFilterAntiFlag", "training":False},
"DY105VBF_2016AMCPY"  : {"xsec": 1.77, "filter": "VBFFilterFlag"}, #this name has to change
"DY105VBF_2016MGPY"   : {"xsec": 1.77, "filter": "VBFFilterFlag", "training":False},


"DY0J_2016AMCPY"  : {"xsec": 4620.52},
"DY1J_2016AMCPY"  : {"xsec":859.59},
"DY2J_2016AMCPY"  : {"xsec":338.26},
#"DYTau_2016AMCPY" : {"xsec":5765.40 / 3. * 0.1739 * 0.1739},
"DYM50_2016AMCPY" : {"xsec":5765.40},

"EWKZ105FIX2_2016MGHERWIG"   : {"xsec": 0.07486,"files": [path2016+"/EWKZ105FIX3_2016MGHERWIG.root"] },
"EWKZ105CORR_2016MGHERWIG"   : {"xsec": 0.07486 },
"EWKZ105CORR_ALLMGHERWIG"   : {"xsec": 0.07486 },
"EWKZ105CORR_1718MGHERWIG"   : {"xsec": 0.07486 },
"EWKZ105_2016MGPYDIPOLE"   : {"xsec": 0.07486,"files":["/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_5/EWKZ105_2016MGPYDIPOLE.root"] },
"EWKZ105_ALLMGPYDIPOLE"   : {"xsec": 0.07486 },
"EWKZ105_1718MGPYDIPOLE"   : {"xsec": 0.07486 },
"EWKZ105_ALLMGHERWIG"   : {"xsec": 0.07486 },
"EWKZ105_2016MGHERWIG"     : {"xsec":0.0508896, "training":False},
"EWKZ105_2016MGPY"     : {"xsec":0.0508896, "training":False},
"EWKZ_2016MGHERWIG" : {"xsec":1.664},
"EWKZ_2016MGPY"     : {"xsec":1.664},
"EWKZint_2016MGPY"  : {"xsec":0.128},

"STs_2016AMCPY"             : {"xsec":3.36},
"STwtbar_2016POWPY"         : {"xsec":35.85},
"STwt_2016POWPY"            : {"xsec":35.85},
"STtbar_2016POW_MADSPIN_PY" : {"xsec":80.95}, ##or 26.38!??  80.95 is for inclusive decays (used), 26.38 is for lepton decays (not used)
"STt_2016POW_MADSPIN_PY"    : {"xsec":136.02}, ##or 44.33   136.02 is for inclusive decays (used), 44.33 is for lepton decays (not used)

"data2016": {"lumi":35900.,"data":True,"files":[path2016data+"/SingleMuonRun2016.root"]},

"TT_2016POWPY"      : {"xsec":809., "training":False},
"TTlep_2016POWPY"   : {"xsec":85.65},
"TTsemi_2016POWPY"  : {"xsec":356.18677888},
#"TThad_2016POWPY"   : {"xsec":366.20181056}, # it does not exist

"W2J_2016AMCPY"  : {"xsec":3172.96},
"W1J_2016AMCPY"  : {"xsec":8426.09},
"W0J_2016AMCPY"  : {"xsec":50131.98},



#"WWdps_2016MGPY"    : {"xsec":1.62},
"WWJJlnln_2016MGPY" : {"xsec":0.3452},
"WLLJJln_2016MG_MADSPIN_PY"  : {"xsec":0.0176},
#"WWJJlnlnNoT_2016MGPY": {"xsec":0.3452},


#"WW2l2n_2016POWHERWIG"      : {"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WW2l2n_2016POWPY"          : {"xsec": 12.178},#118.7 * 21.34 * 21.34 / 10000.},
#"WWlnqq_2016AMC_MADSPIN_PY" : {"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},



#"WZ1l1n2q_2016AMCPY"            : {"xsec":47.13 * 21.34 * 69.91 / 10000.},
"WZ1l3n_2016AMCPY"              : {"xsec":47.13 * 21.34 * 20.00 / 10000.},
"WZ2l2q_2016AMC_MADSPIN_PY"     : {"xsec": 6.321},#}47.13 * 6.729 * 67.41 / 10000.},
#"WZ3l1n_2016POWPY"              : {"xsec":47.13 * 21.34 * 10.099 / 10000.},
"WZ3l1n_2016AMCPY"              : {"xsec":47.13 * 21.34 * 10.099 / 10000.},


#"ZZ2l2n_2016POWPY": {"xsec":16.523 * 20.000 * 10.099 / 10000.},    # not ready yet
"ZZ2l2q_2016POWPY": {"xsec":16.523 * 2. * 6.729 * 69.91 / 10000.},
#"ZZ2q2n_2016POWPY": {"xsec": },    # not ready yet
#"ZZ2q2n_2016AMCPY": {"xsec": },    # not ready yet
#"ZZ4l_2016POWPY": {"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet
#"ZZ4l_2016AMCPY": {"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet


#"ZZ_2017AMCPY": {"xsec":16.523},
#"WZ_2017AMCPY": {"xsec":47.13}, 
#"WW_2017AMCPY": {"xsec":118.7}, 
"ggH120mm_2016AMCPY"       : {"xsec":5.222E+1*2.423E-04}, 
"vbfH120mm_2016AMCPY"      : {"xsec":3.935*2.423E-04}, 
"ggH130mm_2016AMCPY"       : {"xsec":45.31*1.877E-04},
"vbfH130mm_2016AMCPY"      : {"xsec":3.637*1.877E-04}, 

"ggHmm_2016AMCPY"       : {"xsec":0.01057}, #xsec["VBF_HToMuMu"] = 0.0008210722; xsec["GluGlu_HToMuMu"] = 0.009582794;
"ggHmm_2016POWPY"       : {"xsec":0.01057},

"vbfHmm_2016POWPY"      : {"xsec":0.0008210722, "training":False},
"vbfHmm_2016POWHERWIG"  : {"xsec":0.0008210722},
"vbfHmm_2016AMCPY"      : {"xsec":0.0008210722},
"vbfHmm_2016AMCHERWIG"  : {"xsec":0.0008210722},
"vbfHmm_2016POWPYDIPOLE"  : {"xsec":0.0008210722},

"zHmm_2016POWPY"        : {"xsec":0.00019201024},
"ttHmm_2016POWPY"       : {"xsec":0.00011034496},
"WplusHmm_2016POWPY"    : {"xsec":0.000182784},
"WminusHmm_2016POWPY"   : {"xsec":0.00011593728},
#"vbfHtautau_2016POWPY"  : {"xsec":0.23720704},

}

## Add "files" automatically if not defined
for sample in samples:
    if not "files" in samples[sample].keys():
        if "nameforfile" in samples[sample].keys() :
            samples[sample]["files"] = [path2016+samples[sample]["nameforfile"]+".root"]
        else:
            samples[sample]["files"] = [path2016+sample+".root"]

 
