#include <math.h>

namespace PtGeoCor{

  float PtGeoFit_mod(float d0, float pt, float eta, int year) { 
    float pt_cor = 0.0;
    if (year == 2016) { 
      if      (abs(eta) < 0.9) pt_cor = ( 1.183 * tanh(606.21*d0) + 163.53 * d0 ) * pt * pt / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = ( 2.226 * tanh(380.74*d0) + 244.43 * d0 ) * pt * pt / 10000.0;
      else                     pt_cor = ( 3.688 * tanh(233.96*d0) + 398.26 * d0 ) * pt * pt / 10000.0;
    }
    else if (year == 2017) {
      if      (abs(eta) < 0.9) pt_cor = ( 0.705 * tanh(948.94*d0) + 400.52 * d0 ) * pt * pt / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = ( 0.853 * tanh(733.68*d0) + 685.24 * d0 ) * pt * pt / 10000.0;
      else                     pt_cor = ( 5.518 * tanh(260.07*d0) + 282.20 * d0 ) * pt * pt / 10000.0;
    }
    else if (year == 2018) {
      if      (abs(eta) < 0.9) pt_cor = ( 0.969 * tanh(690.73*d0) + 294.48 * d0 ) * pt * pt / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = ( 1.466 * tanh(527.43*d0) + 472.16 * d0 ) * pt * pt / 10000.0;
      else                     pt_cor = ( 1.024 * tanh(618.79*d0) + 1025.5 * d0 ) * pt * pt / 10000.0;
    }
    return (pt - pt_cor);
  } // end of float PtGeoFit_mod(float d0, float pt, float eta, int year)


  float PtGeo_BS_Roch(float d0, float pt, float eta, int year) {
    if (abs(d0) > 1) { return pt;}
    float pt_cor = 0.0;
    if (year == 2016) {
      if      (abs(eta) < 0.9) pt_cor = 411.34 * d0 * pt * pt / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = 673.40 * d0 * pt * pt / 10000.0;
      else                     pt_cor = 1099.0 * d0 * pt * pt / 10000.0;
    }
    else if (year == 2017) {
      if      (abs(eta) < 0.9) pt_cor = 582.32 * d0 * pt * pt / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = 974.05 * d0 * pt * pt / 10000.0;
      else                     pt_cor = 1263.4 * d0 * pt * pt / 10000.0;
    }
    else if (year == 2018) {
      if      (abs(eta) < 0.9) pt_cor = 650.84 * d0 * pt * pt / 10000.0;
      else if (abs(eta) < 1.7) pt_cor = 988.37 * d0 * pt * pt / 10000.0;
      else                     pt_cor = 1484.6 * d0 * pt * pt / 10000.0;
    }
    return (pt - pt_cor);
  } // end of float PtGeo_BS_Roch(float d0, float pt, float eta, int year) 

} // end namespace PtGeoCor

