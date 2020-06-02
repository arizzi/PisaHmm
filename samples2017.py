#path2017 = "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2017_nanoV5/"
#path2017 = "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2017_FSR/"
#/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_tmp/"
#path2018 = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_tmp/"
#path2017data = "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2017_nanoV5/"
#ath2017data = "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2017_FSR/"
# "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2017_Z/"

path2017     = "/scratchssd/mandorli/Hmumu/fileSkimFromNanoAOD/PROD_6_2/"
path2017     = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_10_0/"
path2017 = "/scratchssd/mandorli/Hmumu/fileSkimFromNanoAOD/PROD_8_08/" #fix skim JER
path2017 = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_4/" #reduced JES

#path2017data = path2017


samples={
#"DY105Inclusive_2017AMCPY"     : {"xsec": 41.81, "filter": "MqqGen < 350"},
#"DY105Inclusive_2017MGPY"      : {"xsec": 41.25, "filter": "MqqGen < 350"},

"DY105J01_2017AMCPY"     : {"xsec": 47.17, "filter":  "DY01JAntiVBF","nameforfile":"DY105_2017AMCPY"},
"DY105J2_2017AMCPY"     : {"xsec": 47.17, "filter":  "DY2JAntiVBF", "nameforfile":"DY105_2017AMCPY"},

"DY105_2017AMCPY"     : {"xsec": 47.17, "filter":  "VBFFilterAntiFlag"},
"DY105NEW_2017AMCPY"     : {"xsec": 47.17, "filter":  "VBFFilterAntiFlag"},
"DY105_2017MGPY"      : {"xsec": 47.17, "filter":  "VBFFilterAntiFlag", "training":False},

"DY105VBFJ01_2017AMCPY"  : {"xsec": 2.04, "filter":  "DY01JVBF", "nameforfile":"DY105VBF_2017AMCPY"},
"DY105VBFJ2_2017AMCPY"  : {"xsec": 2.04, "filter":  "DY2JVBF", "nameforfile":"DY105VBF_2017AMCPY"},
"DY105VBF_2017AMCPY"  : {"xsec": 2.04, "filter":  "VBFFilterFlag"},
#"DY105VBF_2017AMCPYnew"  : {"xsec": 2.04, "filter":  "VBFFilterFlag"},
"DY105VBF_2017MGPY"   : {"xsec": 2.04, "filter":  "VBFFilterFlag", "training":False},

"DY0J_2017AMCPY"  : {"xsec": 4620.52},
"DY1J_2017AMCPY"  : {"xsec":859.59},
"DY2J_2017AMCPY"  : {"xsec":338.26},
"DYTau_2017AMCPY" : {"xsec":5765.40 / 3. * 0.1739 * 0.1739},
#"DYM50_2017AMCPY" : {"xsec":5765.40},

"DY_2016AMCHERWIG" : {"xsec":5765.40},
"DY_2016AMCPYCUETP8M1Down" : {"xsec":5765.40},
"DY_2016AMCPYCUETP8M1Up" : {"xsec":5765.40},
"DY_2016AMCPYDownPS" : {"xsec":5765.40},
"DY_2016AMCPY" : {"xsec":5765.40},
"DY_2016AMCPYUpPS" : {"xsec":5765.40},
"DY_2016MGHERWIG" : {"xsec":5765.40},
"DY_2016MGPY" : {"xsec":5765.40},


"EWKZ105_2017MGHERWIG"     : {"xsec":0.0508896, "training":False},
"EWKZ105_2017MGPY"     : {"xsec":0.0508896, "training":False},
"EWKZ105_2017MGPYDIPOLE"     : {"xsec":0.0508896, "training":False,"files":["/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_5/EWKZ105_2017MGPYDIPOLE.root"]},
"EWKZ_2017MGHERWIG" : {"xsec":1.664}, #it does not exist yet
"EWKZ_2017MGPY"     : {"xsec":1.664},
"EWKZint_2017MGPY"  : {"xsec":0.128},
"EWKZ105FIX2_2017MGHERWIG"   : {"xsec": 0.0789 },
"EWKZ105CORR_2017MGHERWIG"   : {"xsec": 0.0789 },


"STs_2017AMCPY"             : {"xsec":3.36},
"STwtbar_2017POWPY"         : {"xsec":35.85},
"STwt_2017POWPY"            : {"xsec":35.85},
"STtbar_2017POWPY"          : {"xsec":80.95}, ##or 26.38!??  80.95 is for inclusive decays (used), 26.38 is for lepton decays (not used)
"STt_2017POWPY"             : {"xsec":136.02}, ##or 44.33   136.02 is for inclusive decays (used), 44.33 is for lepton decays (not used)

"data2017": {"lumi":41530.,"data":True, "files":["/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_12_0/data2017.root"]},
#"data2017": {"lumi":41530.,"data":True, "files":["/scratchssd/mandorli/Hmumu/fileSkimFromNanoAOD/PROD_6_2/SingleMuonRun2017.root"]},

"TT_2017AMCPY"      : {"xsec":809., "training":False},    #generator is different from 2016
"TT_2017MGPY"       : {"xsec":809.},
"TTlep_2017POWPY"   : {"xsec":85.65},
"TTsemi_2017POWPY"  : {"xsec":356.18677888},
"TThad_2017POWPY"   : {"xsec":366.20181056}, # it does not exist

"W2J_2017AMCPY"  : {"xsec":3172.96},
#"W1J_2017AMCPY"  : {"xsec":8426.09}, # NANOAOD not produced yet
"W0J_2017AMCPY"  : {"xsec":50131.98},




#"WWdps_2017MGPY"    : {"xsec":1.62},
"WWJJlnln_2017MGPY" : {"xsec":0.3452},
"WLLJJln_2017MG_MADSPIN_PY"  : {"xsec":0.0176},
#"WWJJlnlnNoT_2017MGPY": {"xsec":0.3452},


#"WW2l2n_2017POWHERWIG"      : {"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WW2l2n_2017POWPY"          : {"xsec":12.178 }, #118.7 * 21.34 * 21.34 / 10000.},
"WWlnqq_2017POWPY"          : {"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},
#"WWlnqq_2017POWPY"          : {"xsec":118.7 * 67.41 * 67.41 / 10000.},      # useless




"WZ1l1n2q_2017AMCPY"            : {"xsec":47.13 * 21.34 * 69.91 / 10000.},
"WZ1l3n_2017AMCPY"              : {"xsec":47.13 * 21.34 * 20.00 / 10000.},
"WZ2l2q_2017AMC_MADSPIN_PY"     : {"xsec": 6.321}, #47.13 * 6.729 * 67.41 / 10000.},
"WZ3l1n_2017POWPY"              : {"xsec":47.13 * 21.34 * 10.099 / 10000.},
"WZ3l1n_2017AMCPY"              : {"xsec":47.13 * 21.34 * 10.099 / 10000.},



"ZZ2l2n_2017POWPY": {"xsec":16.523 * 20.000 * 10.099 / 10000.},    # not ready yet
"ZZ2l2q_2017POWPY": {"xsec":16.523 * 2. * 6.729 * 69.91 / 10000.},
#"ZZ2q2n_2017POWPY": {"xsec": },    # not ready yet
#"ZZ2q2n_2017AMCPY": {"xsec": },    # not ready yet
"ZZ4l_2017POWPY": {"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet
#"ZZ4l_2017AMCPY": {"xsec":16.523 * 10.099 * 10.099 / 10000.},    # not ready yet


#"ZZ_2017AMCPY": {"xsec":16.523},
#"WZ_2017AMCPY": {"xsec":47.13}, 
#"WW_2017AMCPY": {"xsec":118.7}, 

"ggH120mm_2017AMCPY"       : {"xsec":5.222E+1*2.423E-04}, 
"vbfH120mm_2017AMCPY"      : {"xsec":3.935*2.423E-04}, 
"ggH130mm_2017AMCPY"       : {"xsec":45.31*1.877E-04}, 
"vbfH130mm_2017AMCPY"      : {"xsec":3.637*1.877E-04},


#xsec in 16 and 18 os :0.01057

"ggHmm_2017AMCPY"       : {"xsec":0.01057}, #This name is different from 2016
"ggHmm_2017POWPY"       : {"xsec":0.01057},
"ggHmm_2017POWPY2"      : {"xsec":0.01057},
"ggHmm_2017AMCPY2"      : {"xsec":0.01057},

"vbfHmm_2017POWPY"      : {"xsec":0.0008210722, "training":False},
"vbfHmm_2017AMCPY"      : {"xsec":0.0008210722},
"vbfHmm_2017POWPY2"     : {"xsec":0.0008210722},
"vbfHmm_2017POWHERWIG7"     : {"xsec":0.0008210722},
"vbfHmm_2017POWHERWIG"     : {"xsec":0.0008210722},
"vbfHmm_2017POWPYDIPOLE"  : {"xsec":0.0008210722},

"zHmm_2017POWPY"        : {"xsec":0.00019201024},
"ttHmm_2017POWPY"       : {"xsec":0.00011034496},
"WplusHmm_2017POWPY"    : {"xsec":0.000182784},
"WminusHmm_2017POWPY"   : {"xsec":0.00011593728},
#"vbfHtautau_2017POWPY"  : {"xsec":0.23720704},

}

## Add "files" automatically if not defined
for sample in samples:
    if not "files" in samples[sample].keys():
	if "nameforfile" in samples[sample].keys() :
            samples[sample]["files"] = [path2017+samples[sample]["nameforfile"]+".root"]
	else:
            samples[sample]["files"] = [path2017+sample+".root"]


