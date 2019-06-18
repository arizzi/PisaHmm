

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


    systematicDetail={
    "QCDScale" : {
            "type": "ShapeOn", #NormOnly, ShapeNorm
            "decorrelate":legendGrouping
            },
    "puWeight" : {
            "type": "ShapeOn" #NormOnly, ShapeNorm
            },
    "lumi":{
            "type": "lnN",
            "value":1.025
        },
    "VVxsec":{
            "type": "lnN",
            "decorrelate":{"ZZ":["ZZ2l2q","ZZ2l2n","ZZ4l"],"WZ":["WZ1l3n","WZ2l2q","WZ3l1n", "WZ1l1n2q"],"WW":["WWdps","WWJJlnln","WLLJJln", "WW2l2n","WWlnqq"]},
            "value":1.10,
            "groupvalue":{"ZZ":2.,"WZ":3.,"WW":4.},
            #"samplevalue":{}
    },
    "WJetsxsec":{
            "type": "lnN",
            "decorrelate":{"WJets":["W2J","W1J","W0J"]},
            "value":1.10,
            #"groupvalue":{},
            "samplevalue":{"W2J":2.,"W1J":3.,"W0J":4.}
    }
    }
    
    return systematicDetail








