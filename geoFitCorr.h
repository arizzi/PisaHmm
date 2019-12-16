#include <math.h>

namespace GeoFit{
  float PtCorrGeoFit(float d0_BS_charge, float pt_Roch, float eta, int year) {
    float pt_cor = 0.0;
    if (year == 2016) {
      if      (abs(eta) < 0.9) pt_cor = 411.34 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = 673.40 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
      else                     pt_cor = 1099.0 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
    }
    else if (year == 2017) {
      if      (abs(eta) < 0.9) pt_cor = 582.32 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = 974.05 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
      else                     pt_cor = 1263.4 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
    }
    else if (year == 2018) {
      if      (abs(eta) < 0.9) pt_cor = 650.84 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = 988.37 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
      else                     pt_cor = 1484.6 * d0_BS_charge * pt_Roch * pt_Roch / 10000.0;
    }
    return (pt_Roch - pt_cor);
  } // end of float PtCorrGeoFit(float d0_BS_charge, float pt_Roch, float eta, int year) 

}
