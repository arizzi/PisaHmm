#!/usr/bin/env python
import re,sys
import os.path
from math import *
from HiggsAnalysis.CombinedLimit.DatacardParser import parseCard, addDatacardParserOptions
from collections import defaultdict
from optparse import OptionParser
try:
  from vv import v 
except :
  v={}

parser = OptionParser()
addDatacardParserOptions(parser)
parser.remove_option("--fix-pars")
parser.remove_option("--ascii")
parser.remove_option("--stat")
parser.add_option("-f", "--format",  type="string",   dest="format", default="html", help="Format for output number (choose html or brief)")
parser.add_option("-p", "--process",    dest="process",     default=None,  type="string",  help="Higgs process to use. Will also be written in the Workspace as RooRealVar 'MH'.")
parser.add_option("-s", "--search", "--grep", dest="grep", default=[], action="append",  type="string",  help="Selection of nuisance parameters (regexp, can be used multiple times)")
parser.add_option("-a", "--all", dest="all", default=False,action='store_true',  help="Report all nuisances (default is only lnN)")
parser.add_option("--noshape", dest="noshape", default=False,action='store_true',  help="Counting experiment only (alternatively, build a shape analysis from combineCards.py -S card.txt > newcard.txt )")
parser.add_option("--bbb", dest="bbb", default=False,action='store_true',  help="For shape nuisances, look at bin-by-bin effect")
parser.add_option("--vtol", "--val-tolerance", dest="vtol", default=2.5, type="float", help="Higlight nuisances whose kappa is larger than this amount (def.: 2.5) ")
parser.add_option("--atol", "--asym-tolerance", dest="atol", default=0.5, type="float", help="Report nuisances which are highly asymmetric: ln(kup*kdown) > X, default = 0.5")
parser.add_option("--sstol", "--samesign-tolerance", dest="sstol", default=0.05, type="float", help="Report nuisances which go both on the same direction, if both are at least x (default 0.05)")
parser.add_option("--plot", dest="plotShapes", default=[], action="append",  type="string",  help="Make plots of shapes for the nuisances for this nuisance (regexp, can specify multilple times)")
parser.add_option("--plot-flagged", dest="plotFlagged", default=False, action='store_true', help="Make plots of shapes for the nuisances, bins and processes that are flagged")
parser.add_option("--icon-plot-url", dest="plotIconUrl", default="https://twiki.cern.ch//twiki/pub/TWiki/TWikiDocGraphics/chart-bar.gif", type="string",  help="URL of icon used to link to plots") 

(options, args) = parser.parse_args()
real_out = options.out if options.out else "-"
options.stat = False
options.bin = True # fake that is a binary output, so that we parse shape lines
options.out = "tmp.root"
options.fileName = args[0]
options.cexpr = False
options.fixpars = False
options.libs = []
options.verbose = 0
options.poisson = 0
options.noJMax = True
options.allowNoSignal = True
options.modelparams = [] 

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True

if options.plotShapes or options.plotFlagged:
    if real_out == "-" or options.format != "html": 
        sys.stderr.write("ERROR, --plot requires to save the output to a file with -o / --out, and to use -f html\n")
        exit(1)
    else:
        plotdir = real_out.replace(".html","")+".dir"
        sys.stderr.write("Info: plots will be saved in %s\n" % plotdir)
        if not os.path.isdir(plotdir): os.system("mkdir -p "+plotdir)
        if os.path.exists("/afs/cern.ch"): os.system("cp /afs/pi.infn.it/user/arizzi/public_html/template/index.php "+plotdir) # better way of getting this?
        c1 = ROOT.TCanvas("c1","c1")
	c1.Divide(1,2)
	p1=ROOT.TPad("p1","",0,0.2,1,1)#c1.cd(1)
	p2=ROOT.TPad("p2","",0,0.0,1,0.2)#c1.cd(2)
	p1.Draw()
	p2.Draw()
        ROOT.gErrorIgnoreLevel = ROOT.kWarning
if real_out != "-" and os.path.dirname(real_out) and not os.path.isdir(os.path.dirname(real_out)): 
    os.system("mkdir -p "+os.path.dirname(real_out))

ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")

from HiggsAnalysis.CombinedLimit.ShapeTools import ShapeBuilder
if options.fileName.endswith(".gz"):
    import gzip
    file = gzip.open(options.fileName, "rb")
    options.fileName = options.fileName[:-3]
else:
    file = open(options.fileName, "r")

DC = parseCard(file, options)

if not DC.hasShapes: DC.hasShapes = True
MB = ShapeBuilder(DC, options)
if not options.noshape: MB.prepareAllShapes()

def commonStems(list, sep="_"):
    hits = {}
    for item in list:
        base = ""
        for token in item.split(sep):
            base = base + sep + token if base else token
            if base not in hits: hits[base] = 0
            hits[base] += 1
    veto = {}
    for k,v in hits.iteritems():
        pieces = k.split(sep)
        for i in xrange(1, len(pieces)):
            k2 = "_".join(pieces[:-i])
            if hits[k2] == v: 
                veto[k2] = True
            else:
                veto[k] = True
    ret = []
    for k,v in hits.iteritems():
       if k not in veto: ret.append((k,v))
    ret.sort()
    return ret 
    
report = {}; errlines = {}; outParams = {}
warn = set()
warn_chann = set()
warn_chann_proc = set()
warn_proc = set()
droplines = []
def dowarn(s,c,p,X):
    warn.add(s)
    warn_chann.add((s,c))
    warn_proc.add((s,p))
    warn_chann_proc.add((s,c,p))
    sys.stderr.write("WARNING for nuisance %s, channel %s, process %s (yield %g): %s\n" % (s,c,p,DC.exp[c][p],X))
    droplines.append("nuisance edit drop %s %s %s # Warning %s "%(p,c,s,X))

shapes_to_plot = {}
nuis_has_plots = set()
nuis_bin_has_plots = set()
for (lsyst,nofloat,pdf,pdfargs,errline) in DC.systs:
    if ("param" in pdf) or ("Param" in pdf) or ("discrete" in pdf): 
    	 if options.all: outParams[lsyst]=[pdf,pdfargs]
    if not options.all and pdf != "lnN": continue
    if not len(errline) : continue
    if options.grep and not any(re.match(pat,lsyst) for pat in options.grep): continue
    types = []
    minEffect, maxEffect = 999.0, 1.0
    processes = {}
    channels  = []
    errlines[lsyst] = errline
    for b in DC.bins:
        numKeysFound = 0
    	types.append(pdf)
        channels.append(b)
        for p in DC.exp[b].iterkeys():
            if errline[b][p] == 0: continue
	    numKeysFound+=1
            processes[p] = True
            isShape = False
	    if "shape" in pdf and MB.isShapeSystematic(b,p,lsyst):
		vals = []
                isShape = True

		systShapeName = lsyst
		if (lsyst,b,p) in DC.systematicsShapeMap.keys(): systShapeName = DC.systematicsShapeMap[(lsyst,b,p)]

	    	objU,objD,objC = MB.getShape(b,p,systShapeName+"Up"), MB.getShape(b,p,systShapeName+"Down"), MB.getShape(b,p)
	 
		if objC.InheritsFrom("TH1"): valU,valD,valC =  objU.Integral(), objD.Integral(), objC.Integral()
		elif objC.InheritsFrom("RooDataHist"): valU,valD,valC =  objU.sumEntries(), objD.sumEntries(), objC.sumEntries()

                if any(re.match(pat, lsyst) for pat in options.plotShapes):
                    shapes_to_plot[(lsyst,b,p)] = (objU,objD,objC)
                    nuis_bin_has_plots.add((lsyst,b))
                    nuis_has_plots.add(lsyst)
                if options.bbb:
                    valU, valD, valC = 1,1,1
                    if "TH1" not in objC.ClassName(): raise RuntimeError("Not supported on "+objC.ClassName())
                    for ib in xrange(1,objC.GetNbinsX()):
                       binU, binD, binC =  objU.GetBinContent(ib), objD.GetBinContent(ib), objC.GetBinContent(ib)
                       if binC == 0:
                           if binU != 0 or binD != 0: dowarn(lsyst,b,p,"bad bin %s (zero central value +- %.4f, non-zero up or down variation)" % (ib,objC.GetBinError(ib)))
                           continue
                       if binU == 0 or binD == 0: 
                           dowarn(lsyst,b,p,"bad bin %s (zero up or down variation, central value was %.4f +- %.4f)" % (ib,binC,objC.GetBinError(ib)))
                           continue
                       binvals, binwarn = (binU/binC, binD/binC), None
		       binvals= [(x if x >0 else 0.0001) for x in binvals]
                       if max(max(binvals),1/min(binvals)) > options.vtol: 
                            binwarn = "very large or small variation"
                       elif log(max(binvals))*log(min(binvals)) > 0 and min(max(v,1/v) for v  in binvals) > 1+options.sstol: 
                            binwarn = "same-signed variation"
                       elif log(max(binvals)*min(binvals)) > options.atol:
                            binwarn = "very asymmetric variation"
                       if binwarn: dowarn(lsyst,b,p,"%s for bin %s: central %.4f +- %.4f, up : %.4f +- %.4f (ratio %.3f), down %.4f +- %.4f (ratio %.3f)" % (
                                                    binwarn, ib, binC, objC.GetBinError(ib), binU, objU.GetBinError(ib), binU/binC,  binD, objD.GetBinError(ib), binD/binC))
                       valU = max(valU, max(binvals))
                       valD = min(valU, min(binvals))
		if valC!=0: 
			errlines[lsyst][b][p] = "%.3f/%.3f"%(valU/valC,valD/valC)
			vals.append(valU/valC)
			vals.append(valD/valC if valD > 0 else 0.001)
		else: 
			errlines[lsyst][b][p] = "NAN/NAN"
			vals.append(1.)
			vals.append(1.)
            else: vals = errline[b][p] if type(errline[b][p]) == list else [ errline[b][p] ]
            for val in vals:
                if val < 1 and val >0: val = 1.0/val
                minEffect = min(minEffect, val)
                maxEffect = max(maxEffect, val)
            if max(max(vals),1/min(vals)) > options.vtol:
                dowarn(lsyst,b,p,"very large or small kappa: %s" % (" / ".join(map(str,vals))))
            elif len(vals) > 1:
                if log(max(vals))*log(min(vals)) > 0 and min(max(v,1/v) for v in vals) > 1+options.sstol:
                    dowarn(lsyst,b,p,"same-signed kappa: %s" % (" / ".join(map(str,vals))))
                elif log(max(vals)*min(vals)) > options.atol:
                    dowarn(lsyst,b,p,"very asymmetric kappa: %s" % (" / ".join(map(str,vals))))
            if options.plotFlagged and isShape and (lsyst,b,p) in warn_chann_proc:
                shapes_to_plot[(lsyst,b,p)] = (objU,objD,objC)
                nuis_bin_has_plots.add((lsyst,b))
                nuis_has_plots.add(lsyst)
        if numKeysFound == 0 : channels.remove(b)
    channelsShort = commonStems(channels)
    types = ",".join(set(types))
    report[lsyst] = { 'channels':channelsShort, 'bins' : channels, 'processes': sorted(processes.keys()), 'effect':("%5.3f"%minEffect,"%5.3f"%maxEffect), 'types':types }

# Compute total yields per channel
yields_s, yields_b, yields_t = defaultdict(float), defaultdict(float), {}
for b in DC.bins:
    for p,y in DC.exp[b].iteritems():
        (yields_s if p in DC.signals else yields_b)[b] += y
    yields_t[b] = yields_s[b] + yields_b[b] 

print "############## Drop lines ##############"
for d in droplines:
	print d
print "########################################"
# Get list
names = report.keys() 
if "brief" in options.format:
    names = [ k for (k,v) in report.iteritems()  ]
if options.process:
    names = [ k for k in names if any(p for p in report[k]['processes'] if re.match(options.process, p)) ]
if options.grep:
    names = [ n for n in names if any(p for p in options.grep if re.match(p,n)) ]

# alphabetic sort
names.sort()
# now re-sort by category (preserving alphabetic sort inside)
namesCommon = [ n for n in names if re.match(r"(pdf_|QCD|lumi|UE|BR).*", n) ]
namesCMS1   = [ n for n in names if re.match(r"CMS_(eff|scale|fake|res|trig).*", n) ]
namesCMS2   = [ n for n in names if re.match(r"CMS_.*", n) and n not in namesCMS1 ]
namesRest   = [ n for n in names if n not in namesCommon and n not in namesCMS1 and n not in namesCMS2 ]
names = namesCommon + namesCMS1 + namesCMS2 + namesRest

ostream = open(real_out, "w") if real_out != "-" else sys.stdout

if "html" in options.format:
    ostream.write("""
<html>
<head>
<style type="text/css">
body { font-family: 'Consolas', 'Courier New', courier, monospace; font-size: small; }
td, th { border-bottom: 1px solid black; padding: 1px 1em; vertical-align: top; }
td.channDetails { font-size: x-small; }
.WARN { color: red; font-weight: bold; }
a { text-decoration: none; color : black }
a:hover { text-decoration: underline }
</style>
<script type="text/javascript">
function toggleChann(id) {
    if (document.getElementById(id+"_chann_toggle").innerHTML == "[+]") {
        document.getElementById(id+"_chann").style = "";
        document.getElementById(id+"_chann_toggle").innerHTML = "[-]";
    } else {
        document.getElementById(id+"_chann").style = "display: none";
        document.getElementById(id+"_chann_toggle").innerHTML = "[+]";
    }
}
</script>
<title>Nuisance Report</title>
</head><body>
<h1>Nuisance Report</h1>
<table>
<tr><th>Nuisance (types)</th><th colspan="2">Range</th><th>Processes</th><th>Channels</th></tr>
""")
    def maywarn(x,nuis,chann=None,proc=None):
        if proc != None and chann != None: 
             iswarn = ((nuis,chann,proc) in warn_chann_proc) 
        elif proc != None:
             iswarn = ((nuis,proc) in warn_proc) 
        elif chann != None: 
             iswarn = ((nuis,chann) in warn_chann)
        else: 
             iswarn = (nuis in warn)
        return ("<span class=\"WARN\">%s</span>" % x) if iswarn else x
    plot_bin_skip = set() # bins for which we can't make plots 
    for nuis in names:
        val = report[nuis]
        link = "<a href=\"%s/index.php?match=%s-\"><img src=\"%s\"></a>" %(os.path.basename(plotdir),nuis,options.plotIconUrl) if nuis in nuis_has_plots else ""
        ostream.write( "<tr><td><a name=\"%s\"><b>%s%s</b></a></td>" % (nuis,maywarn(nuis,nuis)+"  ("+val['types']+")",link) )
        #ostream.write( "<td>%5.3f</td><td>%5.3f</td>" % ( val['effect'][0],val['effect'][1] ) )
        ostream.write( "<td>%s</td><td>%s</td>" % ( maywarn(val['effect'][0],nuis),maywarn(val['effect'][1],nuis) ) )
        ostream.write( "<td>" +  (", ".join((maywarn(p,nuis,proc=p) for p in val['processes'])) ) + "</td>" )
        ostream.write( "<td>%s" % ", ".join(["%s(%d)" % (k,v) for (k,v) in sorted(val['channels'])]) )
        ostream.write( "<a id=\"%s_chann_toggle\" href=\"#%s\" onclick=\"toggleChann(&quot;%s&quot;)\">[+]</a></td>" % (nuis,nuis,nuis) )
        ostream.write( "</tr>\n" )
        ostream.write( "<tr id=\"%s_chann\" style=\"display: none\">" % nuis )
        ostream.write( "\t<td colspan=\"5\"><table class=\"channDetails\">"  )
        for x in sorted(val["bins"]): 
            binspan="total yields: sig %.2f, bkg %.2f, tot %.2f" % (yields_s[x],yields_b[x],yields_t[x])
            binprocs = []
            for (k,v) in sorted(errlines[nuis][x].iteritems()):
                if v == 0: continue
                binprocspan = "yield: %.3f; totals: sig %.2f, bkg %.2f, tot %.2f" % (DC.exp[x][k], yields_s[x],yields_b[x],yields_t[x])
                link = "<a href=\"%s/%s-%s-%s.png\"><img src=\"%s\"></a>" %(os.path.basename(plotdir),nuis,x,k,options.plotIconUrl) if (nuis,x,k) in shapes_to_plot else ""
                binprocs.append( maywarn("<span title=\"%s\">%s(%s)%s</span>"%(binprocspan, k,v, link),nuis,x,k) )
            link = "<a href=\"%s/index.php?match=%s-%s\"><img src=\"%s\"></a>" %(os.path.basename(plotdir),nuis,x,options.plotIconUrl) if (nuis,x) in nuis_bin_has_plots else ""
            ostream.write( "\t\t<tr><td><span title=\"%s\">%s</span>%s</td><td>%s</td></tr>" % (binspan,maywarn(x,nuis,x),link, ", ".join(binprocs)) )
        ostream.write( "\t</table></td>" )
        ostream.write( "</tr>\n" )
                    
    for x in outParams.keys():
        ostream.write( "\t\t<tr><td><b>%s(%s)</b></td><td>%s</td>" % (x,  outParams[x][0] , ", ".join([a for a in outParams[x][1]])) )
        ostream.write( "</tr>\n" )
    ostream.write( """ 
</table>
</body>
</html>""" )
    ostream.close()
    print "Now I have to make %d plots." % len(shapes_to_plot)
    for nuis in names:
        for b in DC.bins:
            if b in plot_bin_skip: continue
            for p in DC.exp[b].iterkeys():
                 if (nuis,b,p) not in shapes_to_plot: continue
                 objU,objD,objC = shapes_to_plot[(nuis,b,p)]
                 if "TH1" in objC.ClassName():
                     objC.SetLineColor(ROOT.kBlack)
                     objU.SetLineColor(ROOT.kBlue)
                     objD.SetLineColor(ROOT.kRed)
                     stack = ROOT.THStack("stk","%s for bin %s, proc. %s"%(nuis,b,p))
                     for o in objU,objD,objC:
                         o.SetFillStyle(0)
                         o.SetLineWidth(2)
                         stack.Add(o)	
		     p1.cd()	
                     stack.Draw("HIST NOSTACK")
                     objC.Draw("E1 SAME")
	             p2.cd()
		     rU=objU.Clone()
		     rD=objD.Clone()
		     rU.Divide(objC)
		     rD.Divide(objC)
		     rU.SetStats(0);
		     rU.Draw("hist")
		     rU.SetTitle("")
		     rU.GetYaxis().SetRangeUser(0.9,1.10)
                     rU.GetYaxis().SetNdivisions(505);
                     rU.GetYaxis().SetTitleSize(20);
                     rU.GetYaxis().SetTitleFont(43);
                     rU.GetYaxis().SetTitleOffset(1.55);
                     rU.GetYaxis().SetLabelFont(43); 
                     rU.GetYaxis().SetLabelSize(15);
                     rU.GetXaxis().SetLabelFont(43); 
                     rU.GetXaxis().SetLabelSize(10);
		     rD.Draw("same hist")
		     p2.SetGridy()
                     stack.GetXaxis().SetTitle("(black = nominal, blue = %s up, red = %s down)" % (nuis,nuis))
                     c1.Print("%s/%s-%s-%s.png" % (plotdir,nuis,b,p))
		     p1.SetLogy(True)
                     c1.Print("%s/%s-%s-%s-log.png" % (plotdir,nuis,b,p))
		     p1.SetLogy(False)
                 else:
                     syst.sterr.write("Notice: can't plot for bin %s, class type %s\n" % (b, nuis, objC.ClassName()))
                     plot_bin_skip.add(b); break
 
else:
    if "brief" in options.format:
        ostream.write( "%-50s  [%5s, %5s]   %-40s  %-30s\n" % ("   NUISANCE (TYPE)", " MIN", " MAX", "PROCESSES", "CHANNELS(#SUBCHANNELS)" ) )
        ostream.write( "%-50s  %14s   %-40s  %-30s\n" % ("-"*50, "-"*14, "-"*30, "-"*30) )
        for nuis in names:
            val = report[nuis]
            ostream.write( "%-50s (%s)  [%s, %s]   %-40s  %-30s\n" % ( nuis,val['types'], val['effect'][0],val['effect'][1],  
                                                                ",".join(val['processes']),
                                                                ",".join(["%s(%d)" % (k,v) for (k,v) in sorted(val['channels'])])) )

