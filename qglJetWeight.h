#ifndef QGLJETWEIGHT_H
#define QGLJETWEIGHT_H

#include <math.h> 



inline float qglJetWeight(int partonFlavour, float eta, float qgl) {

//     std::cout << partonFlavour  << " \t " << eta  << " \t " << qgl << std::endl;
    if (partonFlavour!=0 && abs(eta)<2 && qgl>0) {
        if (abs(partonFlavour) < 4) return -0.666978*qgl*qgl*qgl + 0.929524*qgl*qgl -0.255505*qgl + 0.981581;
        if (partonFlavour == 21)    return -55.7067*qgl*qgl*qgl*qgl*qgl*qgl*qgl + 113.218*qgl*qgl*qgl*qgl*qgl*qgl -21.1421*qgl*qgl*qgl*qgl*qgl -99.927*qgl*qgl*qgl*qgl + 92.8668*qgl*qgl*qgl -34.3663*qgl*qgl + 6.27*qgl + 0.612992;
    }
    return 1.;
}

#endif
