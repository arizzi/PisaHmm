

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

        "EWKZJJxsec":{
                "type": "lnN",
                "decorrelate":{"EWK":EWK},
                "value":10.,
        },

        #"LHEPdf":{
                #"decorrelate":allSamples, #{x:allSamples[x] for x in allSamples if "EWK" not in x},
                #"type": "normalizationOnly",
                #"value":1.1, #AR: Giulio questo non ha senso... 
        #},

        "LHERen":{
                #"type": "shapeAndNorm",                 #  <--- Questa opzione divide la sistematica in due, una solo normalizzazione e una solo shape
                #"type": "shape",                 
                "type": "normalizationOnly",                 
                "decorrelate": {"Hmm":Hmm, "DY":DY, "EWK":EWK, "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                "value":1.0,
        },

        
# ----------------------------        PROVA I DUE ESEMPI        ---------------------------- 
        
        "EXAMPLE1":{
                "type": "lnN",
                "decorrelate": {"Hmm":Hmm, "DY":DY, "EWK":EWK, "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},   # unisce i valori in "value" (in questo caso il valore di default 1) con i valori di LHERenDY, LHERenEWK, ecc
                #"additionalNormalizations": ["LHERen", "LHEPdf"],
                "additionalNormalizations": ["LHERen"],
                "groupValues":  {"Hmm":1.05, "DY":2., "EWK":10},
        },
        

        #"EXAMPLE2":{
                #"type": "lnN",
                ##"value":50., # se scommenti questo, combina 50 ai valori delle altre sistematiche
                #"decorrelate": {"Hmm":Hmm, "DY":DY, "EWK":EWK, "TT":TT ,"ST":ST, "WJets":WJets, "ZZ":ZZ, "WZ":WZ, "WW":WW},
                #"additionalNormalizations": ["LHERen", "EWKZJJxsec"]   # unisce anche la sistematica EWKZJJxsec ma solamente per EWK
        #},
        

    }



    return systematicDetail







