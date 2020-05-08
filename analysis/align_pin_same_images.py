import matplotlib.pyplot as plt
from beamline.rasor import alignPin


pin = alignPin.alignPin(43)
pin.analysePinImages()
pin.fitPinCoords()





"""

[[Fit Statistics]]
    # function evals   = 73
    # data points      = 23
    # variables        = 6
    chi-square         = 85.999
    reduced chi-square = 5.059
[[Variables]]
    xc:       18.4560407 +/- 0.163134 (0.88%) (init= 18.6)
    yc:      -0.14822983 +/- 0.021645 (14.60%) (init= 0)
    zc:      -0.15285881 +/- 0.056805 (37.16%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.756005 +/- 0.396566 (0.09%) (init= 448)
    cx_top:   858.380865 +/- 3.068914 (0.36%) (init= 834)
    m_top:   -18.7805975 +/- 0.478585 (2.55%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.996 
    C(yc, cy_top)                =  0.879 
    C(zc, cy_top)                = -0.362 
    C(yc, zc)                    = -0.307 
    C(yc, m_top)                 = -0.199 
    C(xc, m_top)                 = -0.134 
    C(cx_top, m_top)             =  0.131 
    C(xc, yc)                    =  0.121 
    C(yc, cx_top)                = -0.119 
offset x : -25.4178 	 -25.2738 
offset y : -7.4468 	 -7.2986 
offset z : 4.7260 	 4.8789 



[[Fit Statistics]]
    # function evals   = 66
    # data points      = 23
    # variables        = 6
    chi-square         = 16.948
    reduced chi-square = 0.997
[[Variables]]
    xc:       18.4967424 +/- 0.077108 (0.42%) (init= 18.6)
    yc:      -0.09645062 +/- 0.027400 (28.41%) (init= 0)
    zc:      -0.13174936 +/- 0.072968 (55.38%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   457.338263 +/- 0.508216 (0.11%) (init= 448)
    cx_top:   856.908323 +/- 1.423428 (0.17%) (init= 834)
    m_top:   -18.3496132 +/- 0.311750 (1.70%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.997 
    C(yc, cy_top)                =  0.985 
    C(zc, cy_top)                = -0.381 
    C(yc, zc)                    = -0.374 
    C(cy_top, m_top)             =  0.264 
    C(yc, m_top)                 =  0.211 
    C(cx_top, m_top)             =  0.203 
    C(xc, m_top)                 = -0.199 
    C(zc, m_top)                 = -0.132 
offset x : -25.4178 	 -25.3145 
offset y : -7.4468 	 -7.3503 
offset z : 4.7260 	 4.8577 





[[Fit Statistics]]
    # function evals   = 73
    # data points      = 23
    # variables        = 6
    chi-square         = 40.408
    reduced chi-square = 2.377
[[Variables]]
    xc:       18.5124407 +/- 0.101574 (0.55%) (init= 18.6)
    yc:      -0.10670527 +/- 0.027599 (25.86%) (init= 0)
    zc:      -0.10849944 +/- 0.036101 (33.27%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   457.286778 +/- 0.525213 (0.11%) (init= 448)
    cx_top:   856.863407 +/- 1.978386 (0.23%) (init= 834)
    m_top:   -19.2636599 +/- 0.506981 (2.63%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.995 
    C(yc, cy_top)                =  0.971 
    C(zc, cy_top)                = -0.728 
    C(yc, zc)                    = -0.696 
    C(cx_top, m_top)             =  0.212 
    C(xc, m_top)                 = -0.201 
    C(yc, m_top)                 = -0.136 
offset x : -25.4178 	 -25.3302 
offset y : -7.4468 	 -7.3401 
offset z : 4.7260 	 4.8345 



[[Fit Statistics]]
    # function evals   = 94
    # data points      = 23
    # variables        = 6
    chi-square         = 50.057
    reduced chi-square = 2.945
[[Variables]]
    xc:       18.8129329 +/- 0.122890 (0.65%) (init= 18.6)
    yc:      -0.10531142 +/- 0.024818 (23.57%) (init= 0)
    zc:      -0.14102938 +/- 0.054163 (38.41%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   457.099600 +/- 0.470522 (0.10%) (init= 448)
    cx_top:   850.769181 +/- 2.377848 (0.28%) (init= 834)
    m_top:   -18.9551791 +/- 0.528874 (2.79%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.994 
    C(yc, cy_top)                =  0.956 
    C(zc, cy_top)                = -0.448 
    C(yc, zc)                    = -0.419 
    C(cx_top, m_top)             =  0.225 
    C(xc, m_top)                 = -0.162 
    C(zc, m_top)                 = -0.106 
offset x : -25.4178 	 -25.6307 
offset y : -7.4468 	 -7.3415 
offset z : 4.7260 	 4.8670 




[[Fit Statistics]]
    # function evals   = 66
    # data points      = 23
    # variables        = 6
    chi-square         = 56.396
    reduced chi-square = 3.317
[[Variables]]
    xc:       18.3600057 +/- 0.158586 (0.86%) (init= 18.6)
    yc:      -0.11345309 +/- 0.038906 (34.29%) (init= 0)
    zc:      -0.10651761 +/- 0.057040 (53.55%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.569728 +/- 0.683840 (0.15%) (init= 448)
    cx_top:   859.443400 +/- 2.789784 (0.32%) (init= 834)
    m_top:   -17.6205466 +/- 0.444858 (2.52%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.997 
    C(yc, cy_top)                =  0.969 
    C(zc, cy_top)                = -0.674 
    C(yc, zc)                    = -0.651 
    C(xc, m_top)                 = -0.171 
    C(cx_top, m_top)             =  0.161 
offset x : -25.4178 	 -25.1778 
offset y : -7.4468 	 -7.3333 
offset z : 4.7260 	 4.8325 




[[Fit Statistics]]
    # function evals   = 59
    # data points      = 23
    # variables        = 6
    chi-square         = 95.767
    reduced chi-square = 5.633
[[Variables]]
    xc:       18.3816670 +/- 0.198874 (1.08%) (init= 18.6)
    yc:      -0.08359731 +/- 0.024625 (29.46%) (init= 0)
    zc:      -0.09694700 +/- 0.076237 (78.64%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   457.028069 +/- 0.450673 (0.10%) (init= 448)
    cx_top:   859.307712 +/- 3.538466 (0.41%) (init= 834)
    m_top:   -17.8961200 +/- 0.964779 (5.39%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.995 
    C(yc, cy_top)                =  0.880 
    C(zc, cy_top)                = -0.334 
    C(yc, zc)                    = -0.287 
    C(xc, m_top)                 = -0.251 
    C(cy_top, m_top)             =  0.240 
    C(cx_top, m_top)             =  0.190 
    C(xc, cy_top)                = -0.189 
    C(cy_top, cx_top)            =  0.182 
    C(yc, m_top)                 =  0.145 
    C(zc, m_top)                 = -0.144 
offset x : -25.4178 	 -25.1995 
offset y : -7.4468 	 -7.3632 
offset z : 4.7260 	 4.8229 


[[Fit Statistics]]
    # function evals   = 80
    # data points      = 23
    # variables        = 6
    chi-square         = 144.207
    reduced chi-square = 8.483
[[Variables]]
    xc:       18.5889185 +/- 0.232794 (1.25%) (init= 18.6)
    yc:      -0.11804819 +/- 0.044279 (37.51%) (init= 0)
    zc:      -0.13676673 +/- 0.098849 (72.28%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.428827 +/- 0.814224 (0.18%) (init= 448)
    cx_top:   855.795614 +/- 4.307352 (0.50%) (init= 834)
    m_top:   -18.4575985 +/- 0.753500 (4.08%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.998 
    C(yc, cy_top)                =  0.956 
    C(zc, cy_top)                = -0.437 
    C(yc, zc)                    = -0.414 
    C(cx_top, m_top)             =  0.113 
    C(yc, m_top)                 = -0.106 
offset x : -25.4178 	 -25.4067 
offset y : -7.4468 	 -7.3288 
offset z : 4.7260 	 4.8628 



[[Fit Statistics]]
    # function evals   = 66
    # data points      = 23
    # variables        = 6
    chi-square         = 50.282
    reduced chi-square = 2.958
[[Variables]]
    xc:       17.8094580 +/- 0.125344 (0.70%) (init= 18.6)
    yc:      -0.10871217 +/- 0.016480 (15.16%) (init= 0)
    zc:      -0.09695398 +/- 0.032953 (33.99%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.312057 +/- 0.294344 (0.06%) (init= 448)
    cx_top:   870.446639 +/- 2.347669 (0.27%) (init= 834)
    m_top:   -19.1556564 +/- 0.417489 (2.18%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.993 
    C(yc, cy_top)                =  0.900 
    C(yc, m_top)                 = -0.645 
    C(cy_top, m_top)             = -0.566 
    C(zc, cy_top)                = -0.430 
    C(yc, zc)                    = -0.379 
    C(xc, m_top)                 = -0.316 
    C(xc, yc)                    =  0.242 
    C(cx_top, m_top)             =  0.233 
    C(zc, m_top)                 =  0.203 
    C(yc, cx_top)                = -0.193 
offset x : -25.4178 	 -24.6273 
offset y : -7.4468 	 -7.3381 
offset z : 4.7260 	 4.8230 




[[Fit Statistics]]
    # function evals   = 122
    # data points      = 23
    # variables        = 6
    chi-square         = 95.120
    reduced chi-square = 5.595
[[Variables]]
    xc:       19.2290324 +/- 0.210798 (1.10%) (init= 18.6)
    yc:      -0.16403874 +/- 0.039958 (24.36%) (init= 0)
    zc:      -0.06866088 +/- 0.079615 (115.95%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.121610 +/- 0.716712 (0.16%) (init= 448)
    cx_top:   844.022152 +/- 3.846327 (0.46%) (init= 834)
    m_top:   -18.1098309 +/- 0.587085 (3.24%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.989 
    C(yc, cy_top)                =  0.947 
    C(zc, cy_top)                = -0.492 
    C(yc, zc)                    = -0.462 
    C(yc, m_top)                 = -0.215 
    C(cx_top, m_top)             =  0.170 
    C(cy_top, m_top)             = -0.125 
offset x : -25.4178 	 -26.0468 
offset y : -7.4468 	 -7.2828 
offset z : 4.7260 	 4.7947 




[[Fit Statistics]]
    # function evals   = 87
    # data points      = 23
    # variables        = 6
    chi-square         = 62.492
    reduced chi-square = 3.676
[[Variables]]
    xc:       18.8236925 +/- 0.202282 (1.07%) (init= 18.6)
    yc:      -0.09199722 +/- 0.024378 (26.50%) (init= 0)
    zc:      -0.12939508 +/- 0.088143 (68.12%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.415821 +/- 0.399880 (0.09%) (init= 448)
    cx_top:   851.419986 +/- 3.338166 (0.39%) (init= 834)
    m_top:   -16.4965452 +/- 0.687093 (4.17%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.997 
    C(yc, cy_top)                =  0.859 
    C(zc, cy_top)                = -0.259 
    C(yc, zc)                    = -0.218 
offset x : -25.4178 	 -25.6415 
offset y : -7.4468 	 -7.3548 
offset z : 4.7260 	 4.8554 


MORE


[[Fit Statistics]]
    # function evals   = 59
    # data points      = 23
    # variables        = 6
    chi-square         = 4.233
    reduced chi-square = 0.249
[[Variables]]
    xc:       18.8879747 +/- 0.035650 (0.19%) (init= 18.6)
    yc:      -0.13489096 +/- 0.011319 (8.39%) (init= 0)
    zc:      -0.11183869 +/- 0.026656 (23.83%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.177765 +/- 0.214641 (0.05%) (init= 448)
    cx_top:   849.582666 +/- 0.706451 (0.08%) (init= 834)
    m_top:   -19.2705898 +/- 0.180484 (0.94%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.991 
    C(yc, cy_top)                =  0.977 
    C(zc, cy_top)                = -0.422 
    C(yc, zc)                    = -0.406 
    C(cx_top, m_top)             =  0.299 
    C(yc, m_top)                 = -0.212 
    C(xc, m_top)                 = -0.199 
    C(cy_top, m_top)             = -0.104 
offset x : -25.4178 	 -25.7058 
offset y : -7.4468 	 -7.3119 
offset z : 4.7260 	 4.8378 




[[Fit Statistics]]
    # function evals   = 101
    # data points      = 23
    # variables        = 6
    chi-square         = 40.170
    reduced chi-square = 2.363
[[Variables]]
    xc:       18.5185034 +/- 0.092106 (0.50%) (init= 18.6)
    yc:      -0.12073036 +/- 0.020348 (16.85%) (init= 0)
    zc:       0.03390705 +/- 0.123696 (364.81%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.064667 +/- 0.399048 (0.09%) (init= 448)
    cx_top:   856.466013 +/- 1.819546 (0.21%) (init= 834)
    m_top:   -19.4973764 +/- 0.477139 (2.45%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.995 
    C(yc, cy_top)                =  0.958 
    C(cx_top, m_top)             =  0.289 
    C(xc, m_top)                 = -0.263 
    C(zc, cy_top)                = -0.156 
    C(yc, zc)                    = -0.155 
    C(cy_top, m_top)             =  0.110 
offset x : -25.4178 	 -25.3363 
offset y : -7.4468 	 -7.3261 
offset z : 4.7260 	 4.6921 


[[Fit Statistics]]
    # function evals   = 66
    # data points      = 23
    # variables        = 6
    chi-square         = 16.430
    reduced chi-square = 0.966
[[Variables]]
    xc:       18.5146375 +/- 0.075518 (0.41%) (init= 18.6)
    yc:      -0.11455457 +/- 0.013452 (11.74%) (init= 0)
    zc:      -0.18318204 +/- 0.031829 (17.38%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.012129 +/- 0.255402 (0.06%) (init= 448)
    cx_top:   856.924295 +/- 1.415650 (0.17%) (init= 834)
    m_top:   -18.5807376 +/- 0.274731 (1.48%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.995 
    C(yc, cy_top)                =  0.943 
    C(zc, cy_top)                = -0.457 
    C(yc, zc)                    = -0.422 
    C(cy_top, m_top)             =  0.241 
    C(cx_top, m_top)             =  0.202 
    C(zc, m_top)                 = -0.191 
    C(xc, m_top)                 = -0.176 
    C(yc, m_top)                 =  0.127 
offset x : -25.4178 	 -25.3324 
offset y : -7.4468 	 -7.3322 
offset z : 4.7260 	 4.9092 


[[Fit Statistics]]
    # function evals   = 101
    # data points      = 23
    # variables        = 6
    chi-square         = 72.224
    reduced chi-square = 4.248
[[Variables]]
    xc:       18.1160468 +/- 0.141571 (0.78%) (init= 18.6)
    yc:      -0.11857461 +/- 0.030162 (25.44%) (init= 0)
    zc:      -0.04669537 +/- 0.059835 (128.14%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.670766 +/- 0.574935 (0.13%) (init= 448)
    cx_top:   864.416375 +/- 2.639481 (0.31%) (init= 834)
    m_top:   -18.7319854 +/- 0.535423 (2.86%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.995 
    C(yc, cy_top)                =  0.958 
    C(zc, cy_top)                = -0.520 
    C(yc, zc)                    = -0.496 
    C(cy_top, m_top)             =  0.305 
    C(yc, m_top)                 =  0.236 
    C(xc, m_top)                 = -0.214 
    C(zc, m_top)                 = -0.200 
    C(cx_top, m_top)             =  0.171 
    C(xc, cy_top)                = -0.114 
    C(cy_top, cx_top)            =  0.103 
offset x : -25.4178 	 -24.9338 
offset y : -7.4468 	 -7.3282 
offset z : 4.7260 	 4.7727 



[[Fit Statistics]]
    # function evals   = 73
    # data points      = 23
    # variables        = 6
    chi-square         = 75.611
    reduced chi-square = 4.448
[[Variables]]
    xc:       18.9385174 +/- 0.139434 (0.74%) (init= 18.6)
    yc:      -0.11362521 +/- 0.028393 (24.99%) (init= 0)
    zc:      -0.16460190 +/- 0.067615 (41.08%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.264623 +/- 0.535649 (0.12%) (init= 448)
    cx_top:   848.546599 +/- 2.697983 (0.32%) (init= 834)
    m_top:   -19.0355091 +/- 0.451519 (2.37%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(xc, cx_top)                = -0.992 
    C(yc, cy_top)                =  0.956 
    C(zc, cy_top)                = -0.396 
    C(yc, zc)                    = -0.370 
    C(cx_top, m_top)             =  0.125 
    C(yc, m_top)                 = -0.111 
offset x : -25.4178 	 -25.7563 
offset y : -7.4468 	 -7.3332 
offset z : 4.7260 	 4.8906 






[[Fit Statistics]]
    # function evals   = 73
    # data points      = 23
    # variables        = 6
    chi-square         = 33.961
    reduced chi-square = 1.998
[[Variables]]
    xc:       19.7539467 +/- 0.181422 (0.92%) (init= 18.6)
    yc:      -0.08753448 +/- 0.059843 (68.37%) (init= 0)
    zc:       0.12902728 +/- 0.133050 (103.12%) (init= 0)
    th:       0 (fixed)
    chi:      90 (fixed)
    cy_top:   456.100237 +/- 0.770144 (0.17%) (init= 448)
    cx_top:   840.242574 +/- 2.235285 (0.27%) (init= 834)
    m_top:   -12.8896218 +/- 0.382749 (2.97%) (init=-19)
[[Correlations]] (unreported correlations are <  0.100)
    C(yc, cy_top)                =  0.986 
    C(xc, cx_top)                = -0.983 
    C(zc, cy_top)                = -0.435 
    C(yc, zc)                    = -0.430 
    C(xc, m_top)                 =  0.332 
    C(cx_top, m_top)             = -0.158 
    C(xc, yc)                    =  0.115 
    C(xc, cy_top)                =  0.113 
    C(yc, cx_top)                = -0.113 
    C(cy_top, cx_top)            = -0.105 
offset x : -25.4178 	 -26.5717 
offset y : -7.4468 	 -7.3593 
offset z : 4.7260 	 4.5970 



"""

