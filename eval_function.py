#import numpy as np
import keras

print "load model"
model=keras.models.load_model('/scratch/mandorli/Hmumu/AddNNinformationToMVAnTuples/CMSSW_9_4_4/src/andreaCode/MODEL_atEpoch10.h5', custom_objects={"keras":keras})
print "loaded model"

def evalh5(model, inputArr):
    return model.predict(inputArr)[0,0] #solo un float




