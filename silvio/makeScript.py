import argparse
import os

script = ""
def launch(cmd):
    global script
    script = script + cmd + "\n"

def launchNow(cmd):
    global script
    script = script + cmd + "\n"


def getBins(fName):
    f = open(fName)
    for l in f.readlines():
        if l[:3] == "bin":
            return [bin_.replace("\t","") for bin_ in l[3:].split(" ") if len(bin_)>2]

def getBinsFromScratch(inputFolder, year):
    bins = []
    if year=="Comb":
        for y in ['2016', '2017', '2018']:
            bins += ["run%s_ch1_"%y+b for b in getBins(inputFolder+"/datacard%sZ.txt"%y)]
            bins += ["run%s_ch2_"%y+b for b in getBins(inputFolder+"/datacard%sH.txt"%y)]
    else:
        for y in ['2016', '2017', '2018', 'All']:
            if y==year:
                bins += ["ch1_"+b for b in getBins(inputFolder+"/datacard%sZ.txt"%y)]
                bins += ["ch2_"+b for b in getBins(inputFolder+"/datacard%sH.txt"%y)]
    return bins

def makeMask(fitPlots, bins):
    mask = ""
    for bin_ in bins:
        if fitPlots and [plotToFit for plotToFit in fitPlots.split(",") if plotToFit in bin_]:
            mask += "mask_"+bin_+"=0"+","
        else:
            mask += "mask_"+bin_+"=1"+","
    if len(mask)>0: mask = mask[:-1]
    if len(mask.split("=0"))-1 != len(fitPlots.split(",")):
        raise Exception("No 1:1 matching between %s and %s"%(str(bins),str(fitPlots))) 
    return mask

parser = argparse.ArgumentParser(description='Make script to run fit for VBF H->mumu')
parser.add_argument('-d','--directory',     help='Directory used to run the fit. Default')
parser.add_argument('-i','--inputFolder',   help='MakeDC will use this folder as input datacards. Default: workspace', default="workspace")
parser.add_argument('-y','--years',         help='Year: 2016,2017,2018,All,Comb')
parser.add_argument('-s','--steps',         help='Steps to run: makeDC, postFitPlot, FitDiagnostic, Significance, makeSnapshot.')
parser.add_argument('-Z','--fitZ',          help="Redefine POI to fit Z (ie. --PO  'map=.*EWKZ.*:r[1.,-20,20]). Default: False'", action='store_true')
parser.add_argument('-H','--fitH',          help="Redefine POI to fit H (ie. --PO  'map=.*Hmm.*:r[1.,-20,20]). Default: False'",  action='store_true')
parser.add_argument('-f','--fitPlots',      help="Unmasked bins during the fit. Default: DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand", default="DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand")
parser.add_argument('-p','--prefitPlots',   help="Unmasked bins during the pre-fit. Default: ''", default="")
parser.add_argument('-o','--fitOptions',    help="Fit opitons. Default: --cminDefaultMinimizerStrategy 0 --robustFit 1", default="--cminDefaultMinimizerStrategy 0 --robustFit 1")
parser.add_argument('-n','--nprocesses',    help="Number of parallel processes for impacts. Default: 10", default=10)


args = parser.parse_args()

inputFolder = vars(args)["inputFolder"]
directory = vars(args)["directory"]
years = vars(args)["years"]
steps = vars(args)["steps"]
fitZ = vars(args)["fitZ"]
fitH = vars(args)["fitH"]
fitPlots = vars(args) ["fitPlots"]
prefitPlots = vars(args) ["prefitPlots"]
fitOptions = vars(args) ["fitOptions"]
nprocesses = vars(args) ["nprocesses"]

if len(inputFolder)>0 and inputFolder[0]!="/": inputFolder = os.getcwd() + "/" + inputFolder

if not (directory and years and steps):
    print "Please set --directory, --years, and --steps"
    print "Example:"
    print ""

definePOI   = "--PO  'map=.*Hmm.*:r[1.,-20,20]'"
if (fitZ and fitH) or (not fitZ and not fitH): raise Exception("Please use either --fitZ or --fitH (not both!).")
if fitZ: definePOI   = "--PO  'map=.*EWKZ.*:r[1.,-20,20]'"

print  vars(args)

for year in years.split(","):
    launch("############ YEAR: %s #################"%year)
    if [step for step in steps.split(",") if "makeDC" in step]:
        bins = getBinsFromScratch(inputFolder, year)
    else:
        bins = getBins("%s/datacard%s.txt"%(directory, year))
    print "Bins = ", bins
    mask        = makeMask(   fitPlots, bins)
    maskPrefit  = makeMask(prefitPlots, bins)
    print "Mask : %s"%mask
    for step in steps.split(","):
        if "makeDC" in step:
            launch("############ Make datacard: %s #################"%step)
            launch("cp %s/decorrelate.sh ."%(inputFolder))
            launch("ln -s ../*py .")
            if not (year == "Comb"):
                launch("cp %s/datacard%s?.txt ."%(inputFolder, year))
                launch("cp %s/fileCombine%s?.root ."%(inputFolder, year))
            else:
                launch("cp %s/datacard?????.txt %s"%(inputFolder, year))
                launch("cp %s/fileCombine?????.root ."%(inputFolder, year))
            if not (year == "Comb"):
                launch("combineCards.py datacard%sZ.txt datacard%sH.txt > datacard%s.txt"%(year, year, year))
            else:
                for y in ['2016','2017','2018']:
                    launch("combineCards.py datacard%sZ.txt datacard%sH.txt > datacard%s.txt"%(y, y, y))
                launch("combineCards.py run2016=datacard2016.txt run2017=datacard2017.txt run2018=datacardComb.txt")
            if (year == "Comb") or (year == "All"):
                launch("./decorrelate.sh >> datacard$%s.txt"%year)
            launch("text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --channel-masks datacard%s.txt %s"%(year, definePOI))
        
        if "significance" in step:
            launch("############ Significance: %s #################"%step)
            options = fitOptions
            if "asimov" in step:    
                options = options + " -t -1"
            elif "fit" in step:     
                options = options
            elif "prefit" in step:  
                launch("combine -M MultiDimFit -n%s --saveWorkspace --setParameters %s datacard$%s.root --verbose 9   %s"%(year, maskPrefit, year, options))
                snapshot ="higgsCombine%s.MultiDimFit.mH120.root"%year
                options = options + "--snapshotName MultiDimFit %s -t -1 --toysFrequentist"%snapshot
            else: raise Exception('Either "prefit" or "fit" or "asimov" must be used with postFitPlot')
            launch("combine -M Significance --setParameters %s,r=1 %s"%(year, options))
        
        if "postFitPlot" in step:
            launch("############ Post-fit plot: %s #################"%step)
            options = fitOptions
            if "prefit" in step: maskToUse = maskPrefit
            elif "fit" in step:  maskToUse = mask
            else: raise Exception('Either "prefit" or "fit" must be used with postFitPlot')
            launch("combineTool.py -M FitDiagnostics -n%s -m 125 -d datacard%s.root --there %s --saveWorkspace --verbose 9 --setParameters %s,r=1"%(year, year, options, maskToUse))
            launch("PostFitShapesFromWorkspace -d datacard%s.txt -w datacard%s.root -o shapes%s.root --print --postfit --sampling -f fitDiagnostics%s.root:fit_s"%(year, year, year, year))
            for bin_ in bins:
                ch = bin_.split("_")[0]
                plot = bin_.split("_")[1]
                for fit in ["prefit", "postfit"]:
                    launch('python ./postFitPlot.py --year=%s --file=shapes%s.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=%s --outname %s  --mode %s --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_%s_%s'%(year, year, ch, fit, plot, plot, fit))
                    launch('cp %s_shapes%s_%s_logy.png  ../figure/%s/'%(plot, year, fit, year))
        
        if "impacts" in step:
            launch("############ Impacts: %s #################"%step)
            options = fitOptions
            if "asimov" in step:    options = options + " -t -1"
            elif "prefit" in step:  options = options + " -t -1 --toysFrequentist"
            elif "fit" in step:     options = options
            else: raise Exception('Either "prefit" or "fit" or "asimov" must be used with postFitPlot')
            launch("combine  -M MultiDimFit -n%s --saveWorkspace --setParameters %s datacard%s.root --verbose 9  %s "%(year, mask, year, options))
            snapshot ="higgsCombine%s.MultiDimFit.mH120.root"%year ####### FIXME: ####################
            launch("combineTool.py -M Impacts -d %s -m 125 -n%s --setParameters %s,r=1 --doInitialFit  %s"%(snapshot, year, mask, options))
            launch("combineTool.py -M Impacts -d %s -m 125 -n%s --setParameters %s,r=1 --doFits   --parallel %s %s"%(snapshot, year, mask, nprocesses, options))
            launch("combineTool.py -M Impacts -d %s -m 125 -n%s -o impacts%s.json"%(snapshot, year, year))

os.popen("mkdir -p %s"%directory)

fName = ""
for s in [inputFolder.split("/")[-1], years, steps, fitZ, fitPlots, prefitPlots]:
    fName += "_"+str(s)
fName=fName.replace(",","_").replace("-","").replace(" ","_")
fName = "fitScript"+fName+".sh"

print directory
print fName

f = open(directory+"/"+fName, 'w')
f.write(script)
f.close()

print
print script
print
print "cd %s && source %s >& log &"%(directory,fName)
print



