#!/usr/bin/env python 

import argparse
import os, sys

''' Make a script to run combine to fit multiple regions, make impact plots, calculate significance. '''

# Initialize script file
script = "#!/bin/bash\n"
script += "\n"
script += "# python "+' '.join(sys.argv) + "\n"
script += "\n"

# Launch command
def launch(cmd):
    global script
    debug = False
    if debug and ">>" in cmd and not "combineCard" in cmd:
        cmd = "echo 1 >> "+cmd.split(">>")[1]
    script = script + cmd + "\n"

# Get the bins from the existing datacard (eg. ['ch1_DNN18AtanNoMass___ZRegion', 'ch1_DNNZAtan___ZRegion', 'ch2_DNN18AtanNoMass___SideBand', 'ch2_DNN18Atan___SignalRegion'])
def getBins(fName):
    f = open(fName)
    for l in f.readlines():
        if l[:3] == "bin":
            return [bin_.replace("\t","") for bin_ in l[3:].split(" ") if len(bin_)>2]

# Define the bins of the future datacard (eg. ['ch1_DNN18AtanNoMass___ZRegion', 'ch1_DNNZAtan___ZRegion', 'ch2_DNN18AtanNoMass___SideBand', 'ch2_DNN18Atan___SignalRegion'])
def getBinsFromScratch(inputDirectory, year):
    bins = []
    if year=="Comb":
        for y in ['2016', '2017', '2018']:
            bins += ["run%s_ch1_"%y+b for b in getBins(inputDirectory+"/datacard%sZ.txt"%y)]
            bins += ["run%s_ch2_"%y+b for b in getBins(inputDirectory+"/datacard%sH.txt"%y)]
    else:
        for y in ['2016', '2017', '2018', 'All']:
            if y==year:
                bins += ["ch1_"+b for b in getBins(inputDirectory+"/datacard%sZ.txt"%y)]
                bins += ["ch2_"+b for b in getBins(inputDirectory+"/datacard%sH.txt"%y)]
    return bins

# Create mask option for combine, masking all bins that are excluded from the fit (eg. mask_ch1_DNN18AtanNoMass___ZRegion=1,mask_ch1_DNNZAtan___ZRegion=1,mask_ch2_DNN18AtanNoMass___SideBand=0,mask_ch2_DNN18Atan___SignalRegion=1).
def makeMask(fitPlots, bins):
    mask = ""
    for bin_ in bins:
        if fitPlots and [plotToFit for plotToFit in fitPlots.split(",") if plotToFit in bin_]:
            mask += "mask_"+bin_+"=0"+","
        else:
            mask += "mask_"+bin_+"=1"+","
    if len(mask)>0: mask = mask[:-1]
#    if len(mask.split("=0"))-1 != len(fitPlots.split(",")):
#        raise Exception("No 1:1 matching between %s and %s"%(str(bins),str(fitPlots))) 
    return mask

# Read command line options, set default values, check consistency
parser = argparse.ArgumentParser(description='Make and run a script to use combine for VBF H->mumu.')
parser.add_argument('-d','--directory',         help='Directory used to run the fit.')
parser.add_argument('-i','--inputDirectory',    help='Directory containing the original datacards (used only in makeDC). Default: workspace', default="workspace")
parser.add_argument('-y','--years',             help='Year to run: 2016,2017,2018,All,Comb')
parser.add_argument('-s','--steps',             help='Define the steps and the type of fit using the following format: step_fittype (e.g. postFitPlot_partialfit). Available steps: makeDC, postFitPlot, FitDiagnostic, Significance, makeSnapshot. Available type of fit: asimov, partialfit, fullfit.')
parser.add_argument('-Z','--fitZ',              help="Redefine POI to fit Z (ie. --PO  'map=.*EWKZ.*:r[1.,-20,20]). Default: False'", action='store_true')
parser.add_argument('-H','--fitH',              help="Redefine POI to fit H (ie. --PO  'map=.*Hmm.*:r[1.,-20,20]). Default: False'",  action='store_true')
parser.add_argument('-f','--fullfitPlots',      help="Unmasked bins used in the final fit. Default: DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand", default="DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand")
parser.add_argument('-p','--partialfitPlots',   help="Unmasked bins used in the partial fit (eg. Z-region only). Default: 'DNN18AtanNoMass___SideBand'", default="DNN18AtanNoMass___SideBand")
parser.add_argument('-o','--fitOptions',        help="Fit options passed to combine. Default: --cminDefaultMinimizerStrategy 0", default="--cminDefaultMinimizerStrategy 0")
parser.add_argument('-n','--nprocesses',        help="Number of parallel processes for impacts. Default: 10", default='10')
parser.add_argument('-v','--verbose',           help="Verbose option passed to combine. Default: 9", default='9')


args = parser.parse_args()

inputDirectory = vars(args)["inputDirectory"]
directory = vars(args)["directory"]
verbose = vars(args)["verbose"]
years = vars(args)["years"]
steps = vars(args)["steps"]
fitZ = vars(args)["fitZ"]
fitH = vars(args)["fitH"]
fullfitPlots = vars(args) ["fullfitPlots"]
partialfitPlots = vars(args) ["partialfitPlots"]
fitOptions = vars(args) ["fitOptions"]
nprocesses = vars(args) ["nprocesses"]

if len(inputDirectory)>0 and inputDirectory[0]!="/": inputDirectory = os.getcwd() + "/" + inputDirectory

if not (directory and years and steps):
    print "Please set --directory, --years, and --steps"
    print "Example:"
    print ""

definePOI   = "--PO  'map=.*Hmm.*:r[1.,-20,20]'"
if (fitZ and fitH) or (not fitZ and not fitH): raise Exception("Please use either --fitZ or --fitH (not both!).")
if fitZ: definePOI   = "--PO  'map=.*EWKZ.*:r[1.,-20,20]'"

print  vars(args)

for stepfit in steps.split(","):
    if "_" in stepfit:
        step, fitMode = stepfit.split("_")
    else:
        step, fitMode = stepfit, ""
    
    if not (step == "makeDC" or step == "significance" or step == "postFitPlot" or step == "impacts"):
        raise Exception ("step is %s. It must be among: makeDC, significance, postFitPlot, impacts."%step)
    if not (fitMode == "" or fitMode == "partialfit" or fitMode == "fullfit" or fitMode == "asimov"):
        raise Exception ("step is %s. The fitmod must be among: asimov, partialfit, fullfit."%stepfit)

os.popen("mkdir -p %s"%directory)


for year in years.split(","):
    # Check year value, get mask options for combine
    if not(year=="2016" or year=="2017" or year=="2018" or year=="All" or year=="Comb"): raise Exception("Year is '%s'. It must be among: 2016, 2017, 2018, All, and Comb."%year)
    launch("############ YEAR: %s #################"%year)
    ### Read bins from datacard
#    if [step for step in steps.split(",") if "makeDC" in step]:
#        bins = getBins("%s/datacard%s.txt"%(directory, year))
#    else:
#        bins = getBinsFromScratch(inputDirectory, year)
    bins = getBinsFromScratch(inputDirectory, year)
    print "Bins = ", bins
    maskFullFit        = makeMask(   fullfitPlots, bins)
    maskPartialFit     = makeMask(partialfitPlots, bins)
    print "maskFullFit : %s"%maskFullFit
    print "maskPartialFit : %s"%maskPartialFit
    for step in steps.split(","):
        name = step+year
        logFile = name+".log"
        launch('echo "" > %s'%logFile)
        # Make datacard, ie. copy datacard file, run combineCards.py, run text2workspace setting the correct parameter of interested (--fitZ or --fitH).
        if "makeDC" in step:
            launch("############ Make datacard: %s #################"%step)
            launch("cp %s/decorrelate.sh ."%(inputDirectory))
            launch("ln -s ../*py .")
            launch("ln -s ../workspace/*py .")
            if not (year == "Comb"):
                launch("cp %s/datacard%s?.txt ."%(inputDirectory, year))
                launch("cp %s/fileCombine%s?.root ."%(inputDirectory, year))
            else:
                launch("cp %s/datacard?????.txt ."%(inputDirectory))
                launch("cp %s/fileCombine?????.root ."%(inputDirectory))
            if not (year == "Comb"):
                launch("combineCards.py datacard%sZ.txt datacard%sH.txt > datacard%s.txt"%(year, year, year))
            else:
                for y in ['2016','2017','2018']:
                    launch("combineCards.py datacard%sZ.txt datacard%sH.txt > datacard%s.txt"%(y, y, y))
                launch("combineCards.py run2016=datacard2016.txt run2017=datacard2017.txt run2018=datacardComb.txt")
            if (year == "Comb") or (year == "All"):
                launch("./decorrelate.sh >> datacard%s.txt"%year)
            launch("text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --channel-masks datacard%s.txt %s >> %s 2>&1"%(year, definePOI, logFile))
        
        # Calculate the significance on the parameter of interest (--fitZ or --fitH) with combine by fitting the plots defined in "--fullfitPlots".  
        # The possible datasets are: "asimov" (expected), "fullfit" (unblinded data), "partialfit" (ie. Asimov dataset generated with the post-fit nuisance parameters obtained by fitting the regions defined in "--partialfitPlots")
        elif "significance" in step:
            launch("############ Significance: %s #################"%step)
            options = fitOptions
            if "asimov" in step:    
                options = options + " datacard%s.root -t -1 "%year
            elif "partialfit" in step:  
                launch("combine -M MultiDimFit -n%s --saveWorkspace --setParameters %s datacard%s.root --verbose %s %s >> %s 2>&1"%(name, maskPartialFit, year, verbose, options, logFile))
                snapshot =" higgsCombine%s.MultiDimFit.mH120.root "%name
                options = options + " --snapshotName MultiDimFit %s -t -1 --toysFrequentist "%snapshot
            elif "fullfit" in step:     
                options = options + " datacard%s.root "%year
            else: raise Exception('Either "partialfit" or "fullfit" or "asimov" must be used with postFitPlot')
            launch("combine -M Significance -n%s --setParameters %s,r=1 %s >> %s 2>&1"%(name, maskFullFit, options, logFile))
        
        # Make the pre/post-fit plots obtained by fitting the regions defined in "--partialfitPlots" or in "--fullfitPlots"
        elif "postFitPlot" in step:
            launch("############ Post-fit plot: %s #################"%step)
            options = fitOptions
            if "partialfit" in step: maskToUse = maskPartialFit
            elif "fullfit" in step:  maskToUse = maskFullFit
            else: raise Exception('Either "partialfit" or "fullfit" must be used with postFitPlot')
            launch("combineTool.py -M FitDiagnostics -n%s -m 125 -d datacard%s.root --there %s --saveWorkspace --verbose %s --setParameters %s,r=1 >> %s 2>&1"%(name, year, options, verbose, maskToUse, logFile))
            freezeOpt = " "
            if fitH: freezeOpt += " --freeze r=1. "
            launch("PostFitShapesFromWorkspace -d datacard%s.txt -w datacard%s.root -o shapes%s.root --print --postfit --sampling -f fitDiagnostics%s.root:fit_s %s >> %s 2>&1"%(year, year, name, name, freezeOpt, logFile))
            for bin_ in bins:
                ch = "ch"+bin_.split("ch")[1][0]
                plot = bin_.split(ch+"_")[1]
                y_axis_min = '"1E-2"'
                blindOpt = ""
                if "SignalRegion" in bin_: blindOpt = " --blind --x_blind_min 1.5  --x_blind_max 4.0 "
                for fit in ["prefit", "postfit"]:
                    launch('python ./postFitPlot.py --year=%s --file=shapes%s.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=%s --outname %s  --mode %s --log_y --custom_y_range --y_axis_min %s %s --channel_label "VBF Hmm" --file_dir %s_%s_%s >> %s 2>&1'%(year, name, ch, fit, plot, y_axis_min, blindOpt, ch, plot, fit, logFile))
                    launch('cp %s_shapes%s_%s_logy.png  ../figure/%s/ >> %s 2>&1'%(plot, name, fit, year, logFile))
        
        # Calculate the impact of the systematic uncertainties with combine by fitting the parameter of interest (--fitZ or --fitH) using the regions defined in "--fullfitPlots".  
        # The possible datasets are: "asimov" (expected), "fullfit" (unblinded data), "partialfit" (ie. Asimov dataset with the post-fit nuisance parameters obtained by fitting the regions defined in "--partialfitPlots")        
        elif "impacts" in step:
            launch("############ Impacts: %s #################"%step)
            options = fitOptions
            if "asimov" in step:    options = options + " -t -1"
            elif "partialfit" in step:  options = options + " -t -1 --toysFrequentist"
            elif "fullfit" in step:     options = options
            else: raise Exception('Either "partialfit" or "fullfit" or "asimov" must be used with postFitPlot')
            launch("combine  -M MultiDimFit -n%s --saveWorkspace --setParameters %s datacard%s.root --verbose %s  %s >> %s 2>&1"%(name, maskFullFit, year, verbose, options, logFile))
            snapshot ="higgsCombine%s.MultiDimFit.mH120.root"%name ####### FIXME: ####################
            launch("combineTool.py -M Impacts -d %s -m 125 -n%s --setParameters %s,r=1 --robustFit 1 --doInitialFit  %s >> %s 2>&1"%(snapshot, name, maskFullFit, options, logFile))
            launch("combineTool.py -M Impacts -d %s -m 125 -n%s --setParameters %s,r=1 --robustFit 1 --doFits   --parallel %s %s >> %s 2>&1"%(snapshot, name, maskFullFit, nprocesses, options, logFile))
            launch("combineTool.py -M Impacts -d %s -m 125 -n%s -o impacts%s.json >> %s 2>&1"%(snapshot, name, name,logFile))
            launch("plotImpacts.py -i impacts%s.json -o impacts%s >> %s 2>&1"%(name,name,logFile))
        
        else:
            raise Exception("Unknown step: %s"%step)

# Create the script file
from datetime import datetime
fName = datetime.now().isoformat().split(".")[0].replace("-","").replace(":","")
fName = "fitScript_"+fName+".sh"

print directory
print fName

f = open(directory+"/"+fName, 'w')
f.write(script)
f.close()

print
print script
print
print "cd %s && chmod +x %s && ./%s "%(directory,fName,fName)
print

# Run the script file

os.system("cd %s && chmod +x %s && ./%s "%(directory,fName,fName))
#aaa = os.popen("cd %s && source %s > log"%(directory,fName))
#aaa.read()
print


