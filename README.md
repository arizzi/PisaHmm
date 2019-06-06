# PisaHmm
Analysis calculations and region definition are in [EventProcessing](eventprocessing.py) description 
Here are the  [Histograms](histograms.py) to make for each region
[Binning](histobinning.py) of histograms is defined with regular expresion matching

Samples and cross sections are defined for [2016](samples2016.py),[2017](samples2017.py),[2018](samples2018.py)

Models describing how to combine and group the samples, which samples to use etc are also defined in model files separatelly for the Z region ([2016](models2016Z.py),[2017](models2017Z.py),[2018](models2018Z.py) and the H region ([2016](models2016H.py),[2017](models2017H.py),[2018](models2018H.py)


[Weights](weights.py) and [systematics](systematics.py) are defined in dedicated file and are enabled in the  analysis [steering code](vbfAna.py)

