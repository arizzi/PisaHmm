import ROOT

hName = "LeadMuon_pt___SignalRegion"
#sample = "EWKZ105_2018MGHERWIG"
#sample = "ttHmm_2018POWPY"
sample = "DY105_2018AMCPY"
#sample = "DY105VBF_2018MGPY"

##################################################
#fName = "DY105_2018AMCPYHistos.root"
fName = "%sHistos.root"%sample
filePrefit = ROOT.TFile.Open("out/%s"%fName)
filePostfit = ROOT.TFile.Open("out/postfit/%s"%fName)
filePrefitWS = ROOT.TFile.Open("workspaceForPostFitHisto/fileCombine2018H.root")
filePostfitWS = ROOT.TFile.Open("workspace/fileCombine2018H.root")
filePrefitPlot = ROOT.TFile.Open("figure_prefit/2018/H/LeadMuon_pt___SignalRegion_log.root")
filePostfitPlot = ROOT.TFile.Open("figure_postfit/2018/H/LeadMuon_pt___SignalRegion_log.root")
fitDiag = ROOT.TFile.Open("workspaceForPostFitHisto/fitDiagnostics.root")


print("out and out/postfit")
print(filePrefit.GetName())
print(filePostfit.GetName())

prefit = filePrefit.Get(hName).GetBinContent(8)
postfit = filePostfit.Get(hName).GetBinContent(8)
print("prefit ",prefit)
print("postfit ",postfit)
print("postfit/prefit ",postfit/prefit)


##################################################

#~ #fName = "DY105_2018AMCPYHistos.root"
#~ fName = "%sHistos.root"%sample


#~ prefit_WS = filePrefitWS.Get("LeadMuon_pt_LeadMuon_pt___SignalRegion_%s"%sample).Clone()
#~ postfit_WS = filePostfitWS.Get("LeadMuon_pt_LeadMuon_pt___SignalRegion_%s"%sample).Clone()
#~ prefit = prefit_WS.GetBinContent(8)
#~ postfit = postfit_WS.GetBinContent(8)
#~ print("WORKSPACE ",prefit)
#~ print(filePrefitWS.GetName())
#~ print(filePostfitWS.GetName())
#~ print("prefit ",prefit)
#~ print("postfit ",postfit)
#~ print("postfit/prefit ",postfit/prefit)

##################################################

#LeadMuon_pt___SignalRegion->GetBinContent(8)


print("FitDiagnostic")
print(fitDiag.GetName())

prefit_FD = fitDiag.Get("shapes_prefit/%s/%s"%(hName,sample)).Clone()
postfit_FD = fitDiag.Get("shapes_fit_b/%s/%s"%(hName,sample)).Clone()
prefit = prefit_FD.GetBinContent(8)
postfit = postfit_FD.GetBinContent(8)

print("prefit ",prefit)
print("postfit ",postfit)
print("postfit/prefit ",postfit/prefit)


for sample in [
    "DY105_2018AMCPY",
    "DY105VBF_2018MGPY",
    "EWKZ105_2018MGHERWIG",
    "EWKZint_2018MGPY",
    "STwt_2018POWPY",
    "STwtbar_2018POWPY",
    "TTlep_2018POWPY",
    "vbfHmm_2018POWPY"
    ]:
    
    fName = "%sHistos.root"%sample
    print fName
    filePrefit = ROOT.TFile.Open("out/%s"%fName)
    filePostfit = ROOT.TFile.Open("out/postfit/%s"%fName)
    prefit_FD = fitDiag.Get("shapes_prefit/%s/%s"%(hName,sample)).Clone()
    postfit_FD = fitDiag.Get("shapes_fit_b/%s/%s"%(hName,sample)).Clone()
    print sample
    for i in range(1,len(filePrefit.Get(hName))):
        prefit  = filePrefit.Get(hName).GetBinContent(i)
        postfit = filePostfit.Get(hName).GetBinContent(i)
        prefit_FD_val  = prefit_FD.GetBinContent(i)
        postfit_FD_val = postfit_FD.GetBinContent(i)
        if prefit>0 and postfit_FD_val>0: print "i=%d\tpostfit/prefit=%f\tfitDiag=%f\tdiff=%f"%(i,postfit/prefit,postfit_FD_val/prefit_FD_val,100.*(postfit/prefit - postfit_FD_val/prefit_FD_val))

##################################################

#~ print("DATA/MC (fitDiag) ")

#~ finalplot_prefit = filePrefitPlot.Get("canvas_LeadMuon_pt___SignalRegion").GetListOfPrimitives().At(1).GetListOfPrimitives().At(1)
#~ finalplot_postfit = filePostfitPlot.Get("canvas_LeadMuon_pt___SignalRegion").GetListOfPrimitives().At(1).GetListOfPrimitives().At(1)

#~ for i in range(1,len(fitDiag.Get("shapes_prefit/%s/%s"%(hName,"data")).GetY())):
    #~ dat = fitDiag.Get("shapes_prefit/%s/%s"%(hName,"data")).GetY()[i-1]
    #~ prefit = fitDiag.Get("shapes_prefit/%s/%s"%(hName,"total_background")).GetBinContent(i)
    #~ postfit = fitDiag.Get("shapes_fit_b/%s/%s"%(hName,"total_background")).GetBinContent(i)
    #~ prefit_finalratio = finalplot_prefit.GetBinContent(i)
    #~ postfit_finalratio = finalplot_postfit.GetBinContent(i)
    #~ prefit_FDratio = (dat-prefit)/prefit
    #~ postfit_FDratio = (dat-postfit)/postfit
    #~ if dat>0:    print "i="+str(i)+"\tprefit "+str(prefit_FDratio)+"\tpostfit "+str(postfit_FDratio)+"Final plot i="+str(i)+"\tprefit "+str(prefit_finalratio)+"\tpostfit "+str(postfit_finalratio)+"\tDIFF(%): prefit "+str(100.*(prefit_finalratio-prefit_FDratio))+"\tpostfit "+str(100*(postfit_finalratio-postfit_FDratio))

#~ ###############################################

#~ prefit_WS.SetLineColor(ROOT.kBlack)
#~ postfit_WS.SetLineColor(ROOT.kBlack)
#~ prefit_WS.SetMarkerColor(ROOT.kBlack)
#~ postfit_WS.SetMarkerColor(ROOT.kBlack)

#~ prefit_FD.SetLineColor(ROOT.kBlue)
#~ postfit_FD.SetLineColor(ROOT.kBlue)
#~ prefit_FD.SetMarkerColor(ROOT.kBlue)
#~ postfit_FD.SetMarkerColor(ROOT.kBlue)

#~ prefit_WS.Draw("ERR")
#~ postfit_WS.Draw("ERR,same")

#~ prefit_FD.Draw("ERR,same")
#~ postfit_FD.Draw("ERR,same")
