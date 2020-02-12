

#TODO: separate systematics as
#shape only (remove normalization effects)
#per group 
#per sample

#default is correlated among all samples 
#and correlated nuisance for norm+shape




def systematicGrouping (background, signal,jesList) :
    
    legendGrouping = {}
    legendGrouping.update(background)
    legendGrouping.update(signal)

    DY = ["DY105","DY105VBF", "DY0J", "DY1J", "DY2J"]
    EWK= ["EWKZ", "EWKZint", "EWKZ105FIX","EWKZ105","EWKZ105FIX2"] 
    TT = ["TTlep","TTsemi","TThad", "TT"]
    ST = ["STs","STwtbar","STwt","STtbar","STt"]
    WW = ["WWdps","WWJJlnln","WLLJJln", "WW2l2n","WWlnqq"]
    WZ = ["WZ1l3n","WZ2l2q","WZ3l1n", "WZ1l1n2q"]
    ZZ = ["ZZ2l2q","ZZ2l2n","ZZ4l"]
    WJets = ["W2J","W1J","W0J"]
    Hmm = ["vbfHmm","ggHmm", "zHmm", "WplusHmm", "WminusHmm", "ttHmm"]
    HmmNoVBF = ["ggHmm", "zHmm", "WplusHmm", "WminusHmm", "ttHmm"]

    allSamples = {}
    for x in DY+EWK+TT+ST+WW+WZ+ZZ+WJets+Hmm : allSamples[x] = [x]
    
    systematicDetail={
        "puWeight" : {
                "type": "shape" #NormOnly, ShapeNorm
                },
        "lumi":{
                "type": "lnN",
                "value":1.025
            },
   	"XSecAndNorm" :{
                "type": "lnN",
                "decorrelate": { "Hmm": HmmNoVBF, "EWK":EWK,"DY":DY,  "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},   
                "additionalNormalizations": ["LHERen","LHEFac"],#,"PDFX0"],
                "groupValues":  {"Hmm":1.01, "EWK":1.01, "DY":1.010, "ZZ":1.01,"WZ":1.01,"WW":1.01,"WJets":1.01,"TT":1.005,"ST":1.005},
        },
        "QGLweight":{
                "type": "shapeOnly",
                "value":1.0,
        },
        "MuScale":{
                "type": "shape",
                "value":1.0,
        },
        "PrefiringWeight":{
                "type": "shape",
                "value":1.0,
        },
        "LHERen":{
                "type": "shapeOnly",
                #"type": "shape",
                "decorrelate":{ "DY":DY, "Hmm": HmmNoVBF,
"EWK":EWK,
 "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                "value":1.0,
                #"mergeToSys": ["TTxsec", "STxsec", "DYxsec","LHEPdf"]
        },
        "LHEFac":{
                #"type": "shapeAndNorm",
                "type": "shapeOnly",
                "decorrelate":{ "DY":DY, "Hmm": HmmNoVBF,
"EWK":EWK, 
"TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                "value":1.0,
        },

        "Alternative":{
                "type": "shape",
                "value": 1.0,
                "powerUp":  +1.,   ## up   = ratio^alpha_up   * nom
                "powerDown": -0.2, ## down = ratio^alpha_down * nom
                "decorrelate":{
                   "vbfHmm" :["vbfHmm"],"EWKZ" :["EWKZ105","EWKZ105FIX","EWKZ105FIX2","EWKZ"],#"EWKZ":["EWKZ"],
                },
                "alternativeSample": {
                    "vbfHmm_2016AMCPY":         ("vbfHmm_2016AMCHERWIG", "vbfHmm_2016AMCPY"),
                    "EWKZ105FIX_2016MGHERWIG":  ("EWKZ105_2016MGPY", "EWKZ105FIX_2016MGHERWIG"),
                    "EWKZ105FIX_2017MGHERWIG":  ("EWKZ105_2017MGPY", "EWKZ105FIX_2017MGHERWIG"),
                    "EWKZ105FIX_2018MGHERWIG":  ("EWKZ105_2018MGPY", "EWKZ105FIX_2018MGHERWIG"),
                    "EWKZ105FIX2_2016MGHERWIG": ("EWKZ105_2016MGPY", "EWKZ105FIX2_2016MGHERWIG"),
                    "EWKZ105FIX2_2017MGHERWIG": ("EWKZ105_2017MGPY", "EWKZ105FIX2_2017MGHERWIG"),
                    "EWKZ105FIX2_2018MGHERWIG": ("EWKZ105_2018MGPY", "EWKZ105FIX2_2018MGHERWIG"),
                    "EWKZ105_2016MGHERWIG":     ("EWKZ105_2016MGPY", "EWKZ105_2016MGHERWIG"),
                    "EWKZ105_2017MGHERWIG":     ("EWKZ105_2017MGPY", "EWKZ105_2017MGHERWIG"),
                    "EWKZ105_2018MGHERWIG":     ("EWKZ105_2018MGPY", "EWKZ105_2018MGHERWIG"),
                    "EWKZ_2016MGHERWIG":        ("EWKZ_2016MGPY",    "EWKZ_2016MGHERWIG"),
                    "EWKZ_2017MGHERWIG":        ("EWKZ_2017MGPY",    "EWKZ_2017MGHERWIG"),
                    "EWKZ_2018MGHERWIG":        ("EWKZ_2018MGPY",    "EWKZ_2018MGHERWIG")
                },
        },
        ##"Alternative":{
                ##"type": "shape",
                ##"value":1.0,
                ##"powerDown": -1., ## down = nom * (up/nom)^powerDown 
                ##"decorrelate":{
                   ##"DY" :["DY105","DY105VBF"],
                ##},
                ##"alternativeSample": {
                    ##"DY105_2018AMCPY":"DY105_2018MGPY",
                    ##"DY105VBF_2018AMCPY":"DY105VBF_2018MGPY",
                ##},
        ##},

#        "PDFX0":{
 #               "type": "shapeOnly",
  #              "decorrelate":{
   #                 "pippo":[],
    #            },
     #           "envelope": "LHEPdf",
      #          "envelopeNBins": 6,
       #         "envelopeFunction": "1.+{up}*{rms}",
       # },
#        "PDFX1":{
 #               "type": "shapeOnly",
  #              "decorrelate":{
   #                 "ggH":["ggHmm"],
    #                "vbfHmm":["vbfHmm"],
     #               "DY" :["DY105VBF","DY105"],
      #              "EWKZ" :["EWKZ","EWKZ105"],
       #         },
        #        "envelope": "LHEPdf",
         #       "envelopeNBins": 6,
          #      "envelopeFunction": "1.+{up}*2*{rms}*(x-0.5*({xmax}+{xmin}))/({xmax}-{xmin})",
       # },
    }
    jes={x[7:-4]:{"type": "shape", "value":1.0} for x in jesList if "Down" in x}

    jesfew={    "JES":{
                "type": "shape",
                "value":1.0,
       }}

    from jernames import jernames
    jer={x[0:-4]:{"type": "shape", "value":1.0} for x in jernames if "Down" in x}
    jerfew={    "JER":{
                "type": "shape",
                "value":1.0,
       }}
#    jesnames=[ "JESPt0To30Eta0To2","JESPt30To50Eta0To2","JESPt50To100Eta0To2","JESPt100To2000Eta0To2","JESPt0To30Eta2To2p5","JESPt30To50Eta2To2p5","JESPt50To100Eta2To2p5","JESPt100To2000Eta2To2p5","JESPt0To30Eta2p5To3p1","JESPt30To50Eta2p5To3p1","JESPt50To100Eta2p5To3p1","JESPt100To2000Eta2p5To3p1","JESPt0To30Eta3p1To5","JESPt30To50Eta3p1To5","JESPt50To100Eta3p1To5","JESPt100To2000Eta3p1To5" ]
#    jes={x:{"type": "shape", "value":1.0} for x in jesnames}

    systematicDetail.update(jes)
#    systematicDetail.update(jesfew)
    systematicDetail.update(jer)
#    systematicDetail.update(jerfew)

    from btagvariations import btagsys
    btag={x[0:-4]:{"type": "shape", "value":1.0} for x in btagsys if "Down" in x}
    systematicDetail.update(btag)

    sthsNames=["Yield","PTH200","Mjj60","Mjj120","Mjj350","Mjj700","Mjj1000","Mjj1500","PTH25","JET01"]
    THUs={"THU_VBF_"+x:{"type": "shape", "decorrelate": {  "vbfHmm" :["vbfHmm"] }, "value":1.0} for x in sthsNames }
    print THUs
    systematicDetail.update(THUs)


    return systematicDetail







