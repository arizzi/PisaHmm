
bdtbinning= [0 , 0.404 , 0.488 , 0.534 , 0.567333333333 , 0.595333333333 , 0.62 , 0.642 , 0.662 , 0.680666666667 , 0.698 , 0.714666666667 , 0.730666666667 , 0.746666666667 , 0.762666666667 , 0.778 , 0.793333333333 , 0.809333333333 , 0.825333333333 , 0.841333333333 , 0.858 , 0.875333333333 , 0.894 , 0.913333333333 , 0.934 , 0.956666666667 , 0.980666666667 , 1.00733333333 , 1.03733333333 , 1.072 , 1.11333333333 , 1.16666666667 , 1.238 , 1.35133333333 , 2.0 ]

dnnbinning=[0 , 0.340277777778 , 0.741666666667 , 1.01388888889 , 1.22361111111 , 1.39583333333 , 1.54722222222 , 1.68611111111 , 1.81111111111 , 1.93194444444 , 2.04722222222 , 2.15833333333 , 2.27361111111 , 2.38888888889 , 2.50833333333 , 2.63194444444 , 2.76666666667 , 2.91527777778 , 3.08055555556 , 3.28472222222 , 3.57361111111 , 5.0 ]

dnn18=[0 , 0.17333333333, 0.346666666667 , 0.575 , 0.746666666667 , 0.88 , 1.01 , 1.135 , 1.255 , 1.36833333333 , 1.475 , 1.57833333333 , 1.68 , 1.785 , 1.89166666667 , 2.00333333333 , 2.11833333333 , 2.24166666667 , 2.38333333333 , 2.54833333333 , 2.77833333333 , 4.0 ]
dnn18few=[0 ,  0.346666666667 ,0.746666666667 , 1.01 , 1.255 ,  1.475  , 1.68 ,  1.89166666667 ,  2.11833333333 ,  2.38333333333 , 2.54833333333 , 2.77833333333 , 4.0 ]
dnn18more=[0 ,  0.346666666667 ,0.746666666667 , 1.01 , 1.255 ,  1.475  , 1.68 ,  1.89166666667 ,  2.11833333333 ,  2.38333333333 , 2.54833333333 , 2.77833333333 ,3, 4.0 ]

dnnnew=[0 , 0.186666666667 , 0.413333333333 , 0.586666666667 , 0.726666666667 , 0.821666666667 , 0.935 , 1.04333333333 , 1.12833333333 , 1.20333333333 , 1.275 , 1.345 , 1.415 , 1.48333333333 , 1.55166666667 , 1.62 , 1.68666666667 , 1.755 , 1.82166666667 , 1.88666666667 , 1.94833333333 , 2.00833333333 , 2.06833333333 , 2.12666666667 , 2.185 , 2.245 , 2.305 , 2.36666666667 , 2.42833333333 , 2.49333333333 , 2.56333333333 , 2.63833333333 , 2.72166666667 , 2.81833333333 , 2.93666666667 , 3.1 , 5.0 ]

dnnnewfew=[0 , 0.413333333333 , 0.726666666667 ,  0.935 ,  1.12833333333  , 1.275  , 1.415  , 1.55166666667  , 1.68666666667  , 1.82166666667  , 1.94833333333  , 2.06833333333  , 2.185  , 2.305  , 2.42833333333  , 2.56333333333  , 2.72166666667 , 2.81833333333 , 2.93666666667 , 3.1 , 5.0 ]

dnnnewfew16=[0 ,  0.693333333333 ,  1.09  , 1.365  , 1.62166666667  , 1.87333333333 , 2.10666666667  , 2.325  , 2.55666666667 , 2.68666666667 , 2.84  , 3.05, 5.0 ]
#dnnnewfew16=[0 ,  0.693333333333 ,  1.09  , 1.365  , 1.62166666667  , 1.87333333333 , 2.10666666667  , 2.325  , 2.55666666667  , 2.84  , 5.0 ]
#bdtbinning16= [0 , 0.504 ,  0.59 ,  0.651333333333 ,  0.702666666667 , 0.750666666667 ,  0.798 ,  0.846666666667 ,  0.900666666667 ,  0.931333333333, 0.967333333333 , 1.01 , 1.068 , 2.0 ]
#bdtbinning16= [0 , 0.432 ,  0.552 ,  0.622  , 0.678  , 0.727333333333  , 0.774666666667  , 0.822 , 0.872666666667  , 0.931333333333 , 0.967333333333 , 1.01 , 1.068 , 2.0 ]

bdtbinning16=             [0 , 0.451333333333  , 0.558666666667  , 0.626  , 0.680666666667 , 0.729333333333 , 0.776  , 0.823333333333 , 0.874, 0.932666666667 , 0.968666666667 , 1.01133333333 , 1.06933333333 , 2.0 ]
qgl = [0 ,  0.541666666667 ,  1.03833333333 ,  1.32666666667 ,  1.57666666667 ,  1.815 ,  2.02666666667 ,  2.21666666667  , 2.40333333333 , 2.61 , 2.73 , 2.875 , 3.07 , 5.0 ]


rebin = {   
    "BDTAtan" : bdtbinning16,
    "DNNAtan" : dnnbinning,
    "DNNAtanNoMass" : dnnbinning,
    "BDTAtanNoMass" : bdtbinning16,
    "BDTAtanNoMassNoNSJ" : bdtbinning,
    "DNN18Atan": dnnnewfew16,
    "DNN18AtanNoQGL": qgl,
    "DNN18AtanNoMass": dnnnewfew16
}
