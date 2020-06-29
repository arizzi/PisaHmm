#path2018 =     "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_nanoV5_v3/"
#path2018 =     "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2018_nanoV5/"
#/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_tmp/"
#path2018data =     "/scratchssd/arizzi/Hmumu/fileSkimFromNanoAOD/fileSkim2018_nanoV5/"
#path2018data = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_nanoV5/"
#path2018data = "/scratch/mandorli/Hmumu/fileSkimFromNanoAOD/fileSkim2018_nanoV5/"
path2018     = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_4_3/"
path2018     = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_10_0/"
path2018 = "/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_4/" #reduced JES

#path2018data = path2018

samples={
#"DY105Inclusuve_2018AMCPY"     : {"xsec": 41.81},
#"DY105Inclusuve_2018MGPY"      : {"xsec": 41.25},

"DY105J01_2018AMCPY"     : {"xsec": 47.17, "filter":  "DY01JAntiVBF","nameforfile":"DY105_2018AMCPY"},
"DY105J2_2018AMCPY"     : {"xsec": 47.17, "filter":  "DY2JAntiVBF", "nameforfile":"DY105_2018AMCPY"},
"DY105VBFJ01_2018AMCPY"  : {"xsec": 2.03, "filter":  "DY01JVBF", "nameforfile":"DY105VBF_2018AMCPY"},
"DY105VBFJ2_2018AMCPY"  : {"xsec": 2.03, "filter":  "DY2JVBF", "nameforfile":"DY105VBF_2018AMCPY"},


"DY105_2018AMCPY"     : {"xsec": 47.17, "filter": "VBFFilterAntiFlag", "training":False},
"DY105NEW_2018AMCPY"     : {"xsec": 47.17, "filter": "VBFFilterAntiFlag", "training":False},
"DY105_2018MGPY"      : {"xsec": 47.17, "filter": "VBFFilterAntiFlag"},
"DY105VBF_2018AMCPY"  : {"xsec": 2.03, "filter": "VBFFilterFlag" },# "files":["/scratchssd/mandorli/Hmumu/fileSkimFromNanoAOD/PROD_7_2/DY105VBF_2018AMCPY.root"], "training":False}, #this name has to change
"DY105VBF_2018MGPY"   : {"xsec": 2.03, "filter": "VBFFilterFlag"},

"DY0J_2018AMCPY"  : {"xsec": 4620.52},
"DY1J_2018AMCPY"  : {"xsec":859.59},   
"DY2J_2018AMCPY"  : {"xsec":338.26},
##AA"DYM50_2018AMCPY" : {"xsec":5765.40},

"EWKZ_2018MGHERWIG" : {"xsec":1.664},   # DY1J 2018 NANOAOD does not exist yet 
#"EWKZ_20187MGHERWIG" : {"xsec":1.664},   # DY1J 2018 NANOAOD does not exist yet 
"EWKZ_2018MGPY"     : {"xsec":1.664},
"EWKZ_2018MGPYDIPOLE"     : {"xsec":1.664},
"EWKZ105_2018MGPYDIPOLE"   : {"xsec": 0.0789, "files":["/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_5/EWKZ105_2018MGPYDIPOLE.root"]},
"EWKZ105_2018MGHERWIG"     : {"xsec":0.0508896, "training":False},
"EWKZint_2018MGPY"  : {"xsec":0.128},
"EWKZ105_2018MGPY"     : {"xsec":0.0508896},
"EWKZ105FIX2_2018MGHERWIG"   : {"xsec": 0.0789 },
"EWKZ105CORR_2018MGHERWIG"   : {"xsec": 0.0789 },



"STs_2018AMCPY"             : {"xsec":3.36},
"STwtbar_2018POWPY"         : {"xsec":35.85},
"STwt_2018POWPY"            : {"xsec":35.85},
"STtbar_2018POWPY"          : {"xsec":80.95}, ##or 26.38!??  80.95 is for inclusive decays (used), 26.38 is for lepton decays (not used)
"STt_2018POWPY"             : {"xsec":136.02}, ##or 44.33   136.02 is for inclusive decays (used), 44.33 is for lepton decays (not used)


#"data2018": {"lumi":59970.,"data":True,"files":["/scratchssd/mandorli/Hmumu/fileSkimFromNanoAOD/PROD_8_02/data2018.root"]},
#"data2018": {"lumi":59970.,"data":True,"files":["/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_12_0/data2018.root"]},
"data2018": {"lumi":59970.,"data":True,"files":["/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_2/data2018.root"]},
"4data2018": {"lumi":59970.,"data":True,"files":[
"/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_2/SingleMuonRun2018A.root",
"/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_2/SingleMuonRun2018B.root",
"/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_2/SingleMuonRun2018C.root",
"/scratchssd/sdonato/fileSkimFromNanoAOD/PROD_13_2/SingleMuonRun2018D.root",

]},
#data2018V16": {"lumi":59970.,"data":True},


"TT_2018AMCPY"      : {"xsec":809.},    #generator is different from 2016
"TT_2018MGPY"       : {"xsec":809.},
"TTlep_2018POWPY"   : {"xsec":85.65},
"TTsemi_2018POWPY"  : {"xsec":356.18677888},
"TThad_2018POWPY"   : {"xsec":366.20181056}, # it does not exist


"W2J_2018AMCPY"  : {"xsec":3172.96},
"W1J_2018AMCPY"  : {"xsec":8426.09},
"W0J_2018AMCPY"  : {"xsec":50131.98},



"WWdps_2018MGPY"             : {"xsec":1.62},
"WWJJlnln_2018MGPY"          : {"xsec":0.3452},
"WLLJJln_2018MG_MADSPIN_PY"  : {"xsec":0.0176},
#"WWJJlnlnNoT_2018MGPY"       : {"xsec":0.3452},



"WW2l2n_2018POWPY"          : {"xsec":12.178},#118.7 * 21.34 * 21.34 / 10000.},
#"WW2l2n_PSw_2018POWPY"      : {"xsec":118.7 * 21.34 * 21.34 / 10000.},
"WWlnqq_2018POWPY"          : {"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},
#"WWlnqq_2018AMC_MADSPIN_PY" : {"xsec":118.7 * 2 * 21.34 * 67.41 / 10000.},



"WZ1l3n_2018AMCPY"              : {"xsec":47.13 * 21.34 * 20.00 / 10000.},
"WZ2l2q_2018AMC_MADSPIN_PY"     : {"xsec":6.321}, #47.13 * 6.729 * 67.41 / 10000.},
"WZ3l1n_2018POWPY"              : {"xsec":47.13 * 21.34 * 10.099 / 10000.},
#"WZ3l1n_2018AMCPY"              : {"xsec":47.13 * 21.34 * 10.099 / 10000.},



#AA"ZZ2l2n_2018POWPY": {"xsec":16.523 * 20.000 * 10.099 / 10000.},    
"ZZ2l2q_2018POWPY": {"xsec":16.523 * 2. * 6.729 * 69.91 / 10000.},
"ZZ4l_2018POWPY": {"xsec":16.523 * 10.099 * 10.099 / 10000.},    


#"ZZ_2018AMCPY": {"xsec":16.523},
#"WZ_2018AMCPY": {"xsec":47.13}, 
#"WW_2018AMCPY": {"xsec":118.7}, 

"ggH120mm_2018AMCPY"       : {"xsec":5.222E+1*2.423E-04}, 
"vbfH120mm_2018AMCPY"      : {"xsec":3.935*2.423E-04}, 
"ggH130mm_2018AMCPY"       : {"xsec":45.31*1.877E-04}, 
"vbfH130mm_2018AMCPY"      : {"xsec":3.637*1.877E-04},


"ggHmm_2018AMCPY"       : {"xsec":0.01057}, #xsec["VBF_HToMuMu"] = 0.0008210722; xsec["GluGlu_HToMuMu"] = 0.009582794;
"ggHmm_2018POWPY"       : {"xsec":0.01057},

"vbfHmm_2018POWPY"      : {"xsec":0.0008210722, "training":False},
#"vbfHmm_PSw_2018POWPY"      : {"xsec":0.0008210722}, # it exists but it has not been hadded
"vbfHmm_2018AMCPY"      : {"xsec":0.0008210722},
"vbfHmm_2018POWPYDIPOLE"  : {"xsec":0.0008210722},
"vbfHmm_2018POWHERWIG7" : {"xsec":0.0008210722},

"zHmm_2018POWPY"        : {"xsec":0.00019201024},
"ttHmm_2018POWPY"       : {"xsec":0.00011034496},
"WplusHmm_2018POWPY"    : {"xsec":0.000182784},
"WminusHmm_2018POWPY"   : {"xsec":0.00011593728},
#"vbfHtautau_2018POWPY"  : {"xsec":0.23720704},
}

## Add "files" automatically if not defined
for sample in samples:
    if not "files" in samples[sample].keys():
        if "nameforfile" in samples[sample].keys() :
            samples[sample]["files"] = [path2018+samples[sample]["nameforfile"]+".root"]
        else:
            samples[sample]["files"] = [path2018+sample+".root"]


#----- Hmumu xSec 125.00 ------
#ggH: 48.58 * 2.176 / 10000.  = 0.010571
#VBF: 3.782 * 2.176 / 10000.  = 0.0008229632
#W+H: 0.840 * 2.176 / 10000.  = 0.000182784
#W-H: 0.5328 * 2.176 / 10000. = 0.00011593728
#ZH : 0.8824 * 2.176 / 10000. = 0.00019201024
#ttH: 0.5071 * 2.176 / 10000. = 0.00011034496
#VBFHtautau: 3.782 * 6.272 / 100.  = 0.23720704



