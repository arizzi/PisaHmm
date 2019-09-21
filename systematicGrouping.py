

#TODO: separate systematics as
#shape only (remove normalization effects)
#per group 
#per sample

#default is correlated among all samples 
#and correlated nuisance for norm+shape




def systematicGrouping (background, signal) :
    
    legendGrouping = {}
    legendGrouping.update(background)
    legendGrouping.update(signal)

    DY = ["DY105","DY105VBF", "DY0J", "DY1J", "DY2J"]
    EWK= ["EWKZ", "EWKZint", "EWKZ105"] 
    TT = ["TTlep","TTsemi","TThad", "TT"]
    ST = ["STs","STwtbar","STwt","STtbar","STt"]
    WW = ["WWdps","WWJJlnln","WLLJJln", "WW2l2n","WWlnqq"]
    WZ = ["WZ1l3n","WZ2l2q","WZ3l1n", "WZ1l1n2q"]
    ZZ = ["ZZ2l2q","ZZ2l2n","ZZ4l"]
    WJets = ["W2J","W1J","W0J"]
    Hmm = ["vbfHmm","ggHmm", "zHmm", "WplusHmm", "WminusHmm", "ttHmm"]

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
        "VVxsec":{
                "type": "lnN",
                "decorrelate":{"ZZ":ZZ,"WZ":WZ,"WW":WW},
                "value":1.10,
                #"groupvalue":{"ZZ":2.,"WZ":3.,"WW":4.},
                #"samplevalue":{}
        },
        "WJetsxsec":{
                "type": "lnN",
                "decorrelate":{"WJets":WJets},
                "value":1.10,
                #"groupvalue":{},
                #"samplevalue":{"W2J":2.,"W1J":3.,"W0J":4.}
        },
        "EWKZJJxsec":{
                "type": "lnN",
                "decorrelate":{"EWK":EWK},
                "value":1.05,
        },
        "DYxsec":{
                "type": "lnN",
                "decorrelate":{"DY":DY},
                "value":1.10,
        },
        "TTxsec":{
                "type": "lnN",
                "decorrelate":{"TT":TT},
                "value":1.05,
        },
        "STxsec":{
                "type": "lnN",
                "decorrelate":{"ST":ST},
                "value":1.05,
        },
#        "JER":{
#                "type": "shape",
#                "value":1.0,
#        },
#        "JES":{
#                "type": "shape",
#                "value":1.0,
#       },
        "QGLweight":{
                "normalizationType": "shapeOnly",
                "type": "shape",
                "value":1.0,
        },
        "LHEPdf":{
                "decorrelate":allSamples,
                #"decorrelate":{"Hmm":Hmm, "DY":DY, "EWK":EWK, "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                "normalizationType": "normalizationOnly",
                "type": "lnN",
                "value":1.1, #AR: Giulio questo non ha senso... 
                "groupvalue":{},
        },
        "MuScale":{
                "type": "shape",
                "value":1.0,
        },
        "LHERen":{
                "type": "shape",
                "decorrelate":{"Hmm":Hmm, "DY":DY, "EWK":EWK, "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                "value":1.0,
        },
        "LHEFac":{
                "type": "shape",
                "decorrelate":{"Hmm":Hmm, "DY":DY, "EWK":EWK, "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                "value":1.0,
        }
    }
    from jesnames import jes2016
    jes={x[10:-4]:{"type": "shape", "value":1.0} for x in jes2016 if "Down" in x}

    jesfew={    "JES":{
                "type": "shape",
                "value":1.0,
       }}

    from jernames import jernames
    jer={x[0:-4]:{"type": "shape", "value":1.0} for x in jernames if "Down" in x}
    jerfew={    "JES":{
                "type": "shape",
                "value":1.0,
       }}
#    jesnames=[ "JESPt0To30Eta0To2","JESPt30To50Eta0To2","JESPt50To100Eta0To2","JESPt100To2000Eta0To2","JESPt0To30Eta2To2p5","JESPt30To50Eta2To2p5","JESPt50To100Eta2To2p5","JESPt100To2000Eta2To2p5","JESPt0To30Eta2p5To3p1","JESPt30To50Eta2p5To3p1","JESPt50To100Eta2p5To3p1","JESPt100To2000Eta2p5To3p1","JESPt0To30Eta3p1To5","JESPt30To50Eta3p1To5","JESPt50To100Eta3p1To5","JESPt100To2000Eta3p1To5" ]
#    jes={x:{"type": "shape", "value":1.0} for x in jesnames}

    systematicDetail.update(jes)
#    systematicDetail.update(jesfew)
    systematicDetail.update(jer)
#    systematicDetail.update(jerfew)
    return systematicDetail







