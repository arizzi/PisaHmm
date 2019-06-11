




def WorkSpace(all_histo_all_syst) :
    print "begin of WorkSpace "

    datacard=open("figure/datacard.txt","w")
    
    datacard.write("imax 1  number of channels")
    datacard.write("jmax *  number of backgrounds")
    datacard.write("kmax *  number of nuisance parameters (sources of systematical uncertainties)")
    datacard.write("------------")
    datacard.write("shapes * mu  fileCombine.root AAAAAAAAAAAAAAAAAAAAAA_$CHANNEL_$PROCESS hBDT_VBF_atanh_$CHANNEL_$PROCESS_$SYSTEMATIC")
    datacard.write("------------")
    datacard.write("bin mu")


    print "---------------------------------------------------------------------"
    print all_histo_all_syst
    print all_histo_all_syst.keys()

