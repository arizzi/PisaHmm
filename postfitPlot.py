import json





class PostFit :
    def __init__(self):
        self.smoothRegion = 1
        self.postFitParam =  {}
        json_file = open('/scratch/mandorli/Hmumu/restartFromAndrea4/nail/PisaHmm/impacts.json')
        self.outputFit = json.load(json_file)
        for sy in self.outputFit["params"] :
            if not sy["name"].startswith("prop") :
                self.postFitParam[sy["name"]] =  {}
                self.postFitParam[sy["name"]]["Up"]     =  sy["fit"][0]
                self.postFitParam[sy["name"]]["nom"]    =  sy["fit"][1]
                self.postFitParam[sy["name"]]["Down"]   =  sy["fit"][2]
        print self.postFitParam.keys()

    def smoothStepFunc(self, x) :
        if abs(x)>self.smoothRegion : return 1 if x > 0 else -1
        xnorm  = x/self.smoothRegion
        xnorm2 = xnorm*xnorm;
        return 0.125 * xnorm * (xnorm2 * (3.*xnorm2 - 10.) + 15);


    def postfitValue (self, syName, syVar) :
        if syName in self.postFitParam.keys() :   
            if syVar in self.postFitParam[syName].keys() : 
                return self.smoothStepFunc(self.postFitParam[syName][syVar])
        print syName, syVar
        return 0.

