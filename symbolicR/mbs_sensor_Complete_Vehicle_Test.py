#
#-------------------------------------------------------------
#
#	ROBOTRAN - Version 6.6 (build : february 22, 2008)
#
#	Copyright 
#	Universite catholique de Louvain 
#	Departement de Mecanique 
#	Unite de Production Mecanique et Machines 
#	2, Place du Levant 
#	1348 Louvain-la-Neuve 
#	http://www.robotran.be// 
#
#	==> Generation Date : Tue Mar 17 09:51:50 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 22
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 1504
#
#	==> Generation Time :  0.020 seconds
#	==> Post-Processing :  0.030 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def sensor(sens, s, isens):

  
  q = s.q
  qd = s.qd
  qdd = s.qdd

# === begin imp_aux === 

# === end imp_aux === 

# ===== BEGIN task 0 ===== 
 
# Sensor Kinematics 



# = = Block_0_0_0_0_0_1 = = 
 
# Trigonometric Variables  

  C4 = np.cos(q[4])
  S4 = np.sin(q[4])
  C5 = np.cos(q[5])
  S5 = np.sin(q[5])
  C6 = np.cos(q[6])
  S6 = np.sin(q[6])

# = = Block_0_0_0_0_0_2 = = 
 
# Trigonometric Variables  

  C7 = np.cos(q[7])
  S7 = np.sin(q[7])
  C8 = np.cos(q[8])
  S8 = np.sin(q[8])
  C9 = np.cos(q[9])
  S9 = np.sin(q[9])
  C10 = np.cos(q[10])
  S10 = np.sin(q[10])

# = = Block_0_0_0_0_0_3 = = 
 
# Trigonometric Variables  

  C11 = np.cos(q[11])
  S11 = np.sin(q[11])
  C12 = np.cos(q[12])
  S12 = np.sin(q[12])
  C13 = np.cos(q[13])
  S13 = np.sin(q[13])
  C14 = np.cos(q[14])
  S14 = np.sin(q[14])

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C15 = np.cos(q[15])
  S15 = np.sin(q[15])
  C16 = np.cos(q[16])
  S16 = np.sin(q[16])
  C17 = np.cos(q[17])
  S17 = np.sin(q[17])
  C18 = np.cos(q[18])
  S18 = np.sin(q[18])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C19 = np.cos(q[19])
  S19 = np.sin(q[19])
  C20 = np.cos(q[20])
  S20 = np.sin(q[20])
  C21 = np.cos(q[21])
  S21 = np.sin(q[21])
  C22 = np.cos(q[22])
  S22 = np.sin(q[22])

# ====== END Task 0 ====== 

# ===== BEGIN task 1 ===== 
 
# Sensor Kinematics 


 
# 
  if(isens==1): 


# = = Block_1_0_0_1_0_1 = = 
 
# Sensor Kinematics 


    ROcp0_25 = S4*S5
    ROcp0_35 = -C4*S5
    ROcp0_85 = -S4*C5
    ROcp0_95 = C4*C5
    ROcp0_16 = C5*C6
    ROcp0_26 = ROcp0_25*C6+C4*S6
    ROcp0_36 = ROcp0_35*C6+S4*S6
    ROcp0_46 = -C5*S6
    ROcp0_56 = -(ROcp0_25*S6-C4*C6)
    ROcp0_66 = -(ROcp0_35*S6-S4*C6)
    OMcp0_25 = qd[5]*C4
    OMcp0_35 = qd[5]*S4
    OMcp0_16 = qd[4]+qd[6]*S5
    OMcp0_26 = OMcp0_25+ROcp0_85*qd[6]
    OMcp0_36 = OMcp0_35+ROcp0_95*qd[6]
    OPcp0_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp0_26 = ROcp0_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp0_35*S5-ROcp0_95*qd[4])
    OPcp0_36 = ROcp0_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp0_25*S5-ROcp0_85*qd[4])

# = = Block_1_0_0_1_0_2 = = 
 
# Sensor Kinematics 


    ROcp0_47 = ROcp0_46*C7+S5*S7
    ROcp0_57 = ROcp0_56*C7+ROcp0_85*S7
    ROcp0_67 = ROcp0_66*C7+ROcp0_95*S7
    ROcp0_77 = -(ROcp0_46*S7-S5*C7)
    ROcp0_87 = -(ROcp0_56*S7-ROcp0_85*C7)
    ROcp0_97 = -(ROcp0_66*S7-ROcp0_95*C7)
    ROcp0_18 = ROcp0_16*C8+ROcp0_47*S8
    ROcp0_28 = ROcp0_26*C8+ROcp0_57*S8
    ROcp0_38 = ROcp0_36*C8+ROcp0_67*S8
    ROcp0_48 = -(ROcp0_16*S8-ROcp0_47*C8)
    ROcp0_58 = -(ROcp0_26*S8-ROcp0_57*C8)
    ROcp0_68 = -(ROcp0_36*S8-ROcp0_67*C8)
    ROcp0_49 = ROcp0_48*C9+ROcp0_77*S9
    ROcp0_59 = ROcp0_58*C9+ROcp0_87*S9
    ROcp0_69 = ROcp0_68*C9+ROcp0_97*S9
    ROcp0_79 = -(ROcp0_48*S9-ROcp0_77*C9)
    ROcp0_89 = -(ROcp0_58*S9-ROcp0_87*C9)
    ROcp0_99 = -(ROcp0_68*S9-ROcp0_97*C9)
    ROcp0_110 = ROcp0_18*C10-ROcp0_79*S10
    ROcp0_210 = ROcp0_28*C10-ROcp0_89*S10
    ROcp0_310 = ROcp0_38*C10-ROcp0_99*S10
    ROcp0_710 = ROcp0_18*S10+ROcp0_79*C10
    ROcp0_810 = ROcp0_28*S10+ROcp0_89*C10
    ROcp0_910 = ROcp0_38*S10+ROcp0_99*C10
    RLcp0_17 = ROcp0_16*s.dpt[1,1]+ROcp0_46*s.dpt[2,1]+s.dpt[3,1]*S5
    RLcp0_27 = ROcp0_26*s.dpt[1,1]+ROcp0_56*s.dpt[2,1]+ROcp0_85*s.dpt[3,1]
    RLcp0_37 = ROcp0_36*s.dpt[1,1]+ROcp0_66*s.dpt[2,1]+ROcp0_95*s.dpt[3,1]
    OMcp0_17 = OMcp0_16+ROcp0_16*qd[7]
    OMcp0_27 = OMcp0_26+ROcp0_26*qd[7]
    OMcp0_37 = OMcp0_36+ROcp0_36*qd[7]
    ORcp0_17 = OMcp0_26*RLcp0_37-OMcp0_36*RLcp0_27
    ORcp0_27 = -(OMcp0_16*RLcp0_37-OMcp0_36*RLcp0_17)
    ORcp0_37 = OMcp0_16*RLcp0_27-OMcp0_26*RLcp0_17
    OPcp0_17 = OPcp0_16+ROcp0_16*qdd[7]+qd[7]*(OMcp0_26*ROcp0_36-OMcp0_36*ROcp0_26)
    OPcp0_27 = OPcp0_26+ROcp0_26*qdd[7]-qd[7]*(OMcp0_16*ROcp0_36-OMcp0_36*ROcp0_16)
    OPcp0_37 = OPcp0_36+ROcp0_36*qdd[7]+qd[7]*(OMcp0_16*ROcp0_26-OMcp0_26*ROcp0_16)
    RLcp0_18 = ROcp0_47*s.dpt[2,13]
    RLcp0_28 = ROcp0_57*s.dpt[2,13]
    RLcp0_38 = ROcp0_67*s.dpt[2,13]
    POcp0_18 = RLcp0_17+RLcp0_18+q[1]
    POcp0_28 = RLcp0_27+RLcp0_28+q[2]
    POcp0_38 = RLcp0_37+RLcp0_38+q[3]
    OMcp0_18 = OMcp0_17+ROcp0_77*qd[8]
    OMcp0_28 = OMcp0_27+ROcp0_87*qd[8]
    OMcp0_38 = OMcp0_37+ROcp0_97*qd[8]
    ORcp0_18 = OMcp0_27*RLcp0_38-OMcp0_37*RLcp0_28
    ORcp0_28 = -(OMcp0_17*RLcp0_38-OMcp0_37*RLcp0_18)
    ORcp0_38 = OMcp0_17*RLcp0_28-OMcp0_27*RLcp0_18
    VIcp0_18 = ORcp0_17+ORcp0_18+qd[1]
    VIcp0_28 = ORcp0_27+ORcp0_28+qd[2]
    VIcp0_38 = ORcp0_37+ORcp0_38+qd[3]
    ACcp0_18 = qdd[1]+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_36*ORcp0_27-OMcp0_37*ORcp0_28+OPcp0_26*RLcp0_37+OPcp0_27*\
   RLcp0_38-OPcp0_36*RLcp0_27-OPcp0_37*RLcp0_28
    ACcp0_28 = qdd[2]-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_36*ORcp0_17+OMcp0_37*ORcp0_18-OPcp0_16*RLcp0_37-OPcp0_17*\
   RLcp0_38+OPcp0_36*RLcp0_17+OPcp0_37*RLcp0_18
    ACcp0_38 = qdd[3]+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_26*ORcp0_17-OMcp0_27*ORcp0_18+OPcp0_16*RLcp0_27+OPcp0_17*\
   RLcp0_28-OPcp0_26*RLcp0_17-OPcp0_27*RLcp0_18
    OMcp0_19 = OMcp0_18+ROcp0_18*qd[9]
    OMcp0_29 = OMcp0_28+ROcp0_28*qd[9]
    OMcp0_39 = OMcp0_38+ROcp0_38*qd[9]
    OMcp0_110 = OMcp0_19+ROcp0_49*qd[10]
    OMcp0_210 = OMcp0_29+ROcp0_59*qd[10]
    OMcp0_310 = OMcp0_39+ROcp0_69*qd[10]
    OPcp0_110 = OPcp0_17+ROcp0_18*qdd[9]+ROcp0_49*qdd[10]+ROcp0_77*qdd[8]+qd[10]*(OMcp0_29*ROcp0_69-OMcp0_39*ROcp0_59)+\
   qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(OMcp0_28*ROcp0_38-OMcp0_38*ROcp0_28)
    OPcp0_210 = OPcp0_27+ROcp0_28*qdd[9]+ROcp0_59*qdd[10]+ROcp0_87*qdd[8]-qd[10]*(OMcp0_19*ROcp0_69-OMcp0_39*ROcp0_49)-\
   qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(OMcp0_18*ROcp0_38-OMcp0_38*ROcp0_18)
    OPcp0_310 = OPcp0_37+ROcp0_38*qdd[9]+ROcp0_69*qdd[10]+ROcp0_97*qdd[8]+qd[10]*(OMcp0_19*ROcp0_59-OMcp0_29*ROcp0_49)+\
   qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(OMcp0_18*ROcp0_28-OMcp0_28*ROcp0_18)

# = = Block_1_0_0_1_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp0_18
    sens.P[2] = POcp0_28
    sens.P[3] = POcp0_38
    sens.R[1,1] = ROcp0_110
    sens.R[1,2] = ROcp0_210
    sens.R[1,3] = ROcp0_310
    sens.R[2,1] = ROcp0_49
    sens.R[2,2] = ROcp0_59
    sens.R[2,3] = ROcp0_69
    sens.R[3,1] = ROcp0_710
    sens.R[3,2] = ROcp0_810
    sens.R[3,3] = ROcp0_910
    sens.V[1] = VIcp0_18
    sens.V[2] = VIcp0_28
    sens.V[3] = VIcp0_38
    sens.OM[1] = OMcp0_110
    sens.OM[2] = OMcp0_210
    sens.OM[3] = OMcp0_310
    sens.A[1] = ACcp0_18
    sens.A[2] = ACcp0_28
    sens.A[3] = ACcp0_38
    sens.OMP[1] = OPcp0_110
    sens.OMP[2] = OPcp0_210
    sens.OMP[3] = OPcp0_310
 
# 
  elif(isens==2): 


# = = Block_1_0_0_2_0_1 = = 
 
# Sensor Kinematics 


    ROcp1_25 = S4*S5
    ROcp1_35 = -C4*S5
    ROcp1_85 = -S4*C5
    ROcp1_95 = C4*C5
    ROcp1_16 = C5*C6
    ROcp1_26 = ROcp1_25*C6+C4*S6
    ROcp1_36 = ROcp1_35*C6+S4*S6
    ROcp1_46 = -C5*S6
    ROcp1_56 = -(ROcp1_25*S6-C4*C6)
    ROcp1_66 = -(ROcp1_35*S6-S4*C6)
    OMcp1_25 = qd[5]*C4
    OMcp1_35 = qd[5]*S4
    OMcp1_16 = qd[4]+qd[6]*S5
    OMcp1_26 = OMcp1_25+ROcp1_85*qd[6]
    OMcp1_36 = OMcp1_35+ROcp1_95*qd[6]
    OPcp1_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp1_26 = ROcp1_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp1_35*S5-ROcp1_95*qd[4])
    OPcp1_36 = ROcp1_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp1_25*S5-ROcp1_85*qd[4])

# = = Block_1_0_0_2_0_3 = = 
 
# Sensor Kinematics 


    ROcp1_411 = ROcp1_46*C11+S11*S5
    ROcp1_511 = ROcp1_56*C11+ROcp1_85*S11
    ROcp1_611 = ROcp1_66*C11+ROcp1_95*S11
    ROcp1_711 = -(ROcp1_46*S11-C11*S5)
    ROcp1_811 = -(ROcp1_56*S11-ROcp1_85*C11)
    ROcp1_911 = -(ROcp1_66*S11-ROcp1_95*C11)
    ROcp1_112 = ROcp1_16*C12+ROcp1_411*S12
    ROcp1_212 = ROcp1_26*C12+ROcp1_511*S12
    ROcp1_312 = ROcp1_36*C12+ROcp1_611*S12
    ROcp1_412 = -(ROcp1_16*S12-ROcp1_411*C12)
    ROcp1_512 = -(ROcp1_26*S12-ROcp1_511*C12)
    ROcp1_612 = -(ROcp1_36*S12-ROcp1_611*C12)
    ROcp1_413 = ROcp1_412*C13+ROcp1_711*S13
    ROcp1_513 = ROcp1_512*C13+ROcp1_811*S13
    ROcp1_613 = ROcp1_612*C13+ROcp1_911*S13
    ROcp1_713 = -(ROcp1_412*S13-ROcp1_711*C13)
    ROcp1_813 = -(ROcp1_512*S13-ROcp1_811*C13)
    ROcp1_913 = -(ROcp1_612*S13-ROcp1_911*C13)
    ROcp1_114 = ROcp1_112*C14-ROcp1_713*S14
    ROcp1_214 = ROcp1_212*C14-ROcp1_813*S14
    ROcp1_314 = ROcp1_312*C14-ROcp1_913*S14
    ROcp1_714 = ROcp1_112*S14+ROcp1_713*C14
    ROcp1_814 = ROcp1_212*S14+ROcp1_813*C14
    ROcp1_914 = ROcp1_312*S14+ROcp1_913*C14
    RLcp1_111 = ROcp1_16*s.dpt[1,4]+ROcp1_46*s.dpt[2,4]+s.dpt[3,4]*S5
    RLcp1_211 = ROcp1_26*s.dpt[1,4]+ROcp1_56*s.dpt[2,4]+ROcp1_85*s.dpt[3,4]
    RLcp1_311 = ROcp1_36*s.dpt[1,4]+ROcp1_66*s.dpt[2,4]+ROcp1_95*s.dpt[3,4]
    OMcp1_111 = OMcp1_16+ROcp1_16*qd[11]
    OMcp1_211 = OMcp1_26+ROcp1_26*qd[11]
    OMcp1_311 = OMcp1_36+ROcp1_36*qd[11]
    ORcp1_111 = OMcp1_26*RLcp1_311-OMcp1_36*RLcp1_211
    ORcp1_211 = -(OMcp1_16*RLcp1_311-OMcp1_36*RLcp1_111)
    ORcp1_311 = OMcp1_16*RLcp1_211-OMcp1_26*RLcp1_111
    OPcp1_111 = OPcp1_16+ROcp1_16*qdd[11]+qd[11]*(OMcp1_26*ROcp1_36-OMcp1_36*ROcp1_26)
    OPcp1_211 = OPcp1_26+ROcp1_26*qdd[11]-qd[11]*(OMcp1_16*ROcp1_36-OMcp1_36*ROcp1_16)
    OPcp1_311 = OPcp1_36+ROcp1_36*qdd[11]+qd[11]*(OMcp1_16*ROcp1_26-OMcp1_26*ROcp1_16)
    RLcp1_112 = ROcp1_411*s.dpt[2,17]
    RLcp1_212 = ROcp1_511*s.dpt[2,17]
    RLcp1_312 = ROcp1_611*s.dpt[2,17]
    POcp1_112 = RLcp1_111+RLcp1_112+q[1]
    POcp1_212 = RLcp1_211+RLcp1_212+q[2]
    POcp1_312 = RLcp1_311+RLcp1_312+q[3]
    OMcp1_112 = OMcp1_111+ROcp1_711*qd[12]
    OMcp1_212 = OMcp1_211+ROcp1_811*qd[12]
    OMcp1_312 = OMcp1_311+ROcp1_911*qd[12]
    ORcp1_112 = OMcp1_211*RLcp1_312-OMcp1_311*RLcp1_212
    ORcp1_212 = -(OMcp1_111*RLcp1_312-OMcp1_311*RLcp1_112)
    ORcp1_312 = OMcp1_111*RLcp1_212-OMcp1_211*RLcp1_112
    VIcp1_112 = ORcp1_111+ORcp1_112+qd[1]
    VIcp1_212 = ORcp1_211+ORcp1_212+qd[2]
    VIcp1_312 = ORcp1_311+ORcp1_312+qd[3]
    ACcp1_112 = qdd[1]+OMcp1_211*ORcp1_312+OMcp1_26*ORcp1_311-OMcp1_311*ORcp1_212-OMcp1_36*ORcp1_211+OPcp1_211*RLcp1_312+\
   OPcp1_26*RLcp1_311-OPcp1_311*RLcp1_212-OPcp1_36*RLcp1_211
    ACcp1_212 = qdd[2]-OMcp1_111*ORcp1_312-OMcp1_16*ORcp1_311+OMcp1_311*ORcp1_112+OMcp1_36*ORcp1_111-OPcp1_111*RLcp1_312-\
   OPcp1_16*RLcp1_311+OPcp1_311*RLcp1_112+OPcp1_36*RLcp1_111
    ACcp1_312 = qdd[3]+OMcp1_111*ORcp1_212+OMcp1_16*ORcp1_211-OMcp1_211*ORcp1_112-OMcp1_26*ORcp1_111+OPcp1_111*RLcp1_212+\
   OPcp1_16*RLcp1_211-OPcp1_211*RLcp1_112-OPcp1_26*RLcp1_111
    OMcp1_113 = OMcp1_112+ROcp1_112*qd[13]
    OMcp1_213 = OMcp1_212+ROcp1_212*qd[13]
    OMcp1_313 = OMcp1_312+ROcp1_312*qd[13]
    OMcp1_114 = OMcp1_113+ROcp1_413*qd[14]
    OMcp1_214 = OMcp1_213+ROcp1_513*qd[14]
    OMcp1_314 = OMcp1_313+ROcp1_613*qd[14]
    OPcp1_114 = OPcp1_111+ROcp1_112*qdd[13]+ROcp1_413*qdd[14]+ROcp1_711*qdd[12]+qd[12]*(OMcp1_211*ROcp1_911-OMcp1_311*\
   ROcp1_811)+qd[13]*(OMcp1_212*ROcp1_312-OMcp1_312*ROcp1_212)+qd[14]*(OMcp1_213*ROcp1_613-OMcp1_313*ROcp1_513)
    OPcp1_214 = OPcp1_211+ROcp1_212*qdd[13]+ROcp1_513*qdd[14]+ROcp1_811*qdd[12]-qd[12]*(OMcp1_111*ROcp1_911-OMcp1_311*\
   ROcp1_711)-qd[13]*(OMcp1_112*ROcp1_312-OMcp1_312*ROcp1_112)-qd[14]*(OMcp1_113*ROcp1_613-OMcp1_313*ROcp1_413)
    OPcp1_314 = OPcp1_311+ROcp1_312*qdd[13]+ROcp1_613*qdd[14]+ROcp1_911*qdd[12]+qd[12]*(OMcp1_111*ROcp1_811-OMcp1_211*\
   ROcp1_711)+qd[13]*(OMcp1_112*ROcp1_212-OMcp1_212*ROcp1_112)+qd[14]*(OMcp1_113*ROcp1_513-OMcp1_213*ROcp1_413)

# = = Block_1_0_0_2_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp1_112
    sens.P[2] = POcp1_212
    sens.P[3] = POcp1_312
    sens.R[1,1] = ROcp1_114
    sens.R[1,2] = ROcp1_214
    sens.R[1,3] = ROcp1_314
    sens.R[2,1] = ROcp1_413
    sens.R[2,2] = ROcp1_513
    sens.R[2,3] = ROcp1_613
    sens.R[3,1] = ROcp1_714
    sens.R[3,2] = ROcp1_814
    sens.R[3,3] = ROcp1_914
    sens.V[1] = VIcp1_112
    sens.V[2] = VIcp1_212
    sens.V[3] = VIcp1_312
    sens.OM[1] = OMcp1_114
    sens.OM[2] = OMcp1_214
    sens.OM[3] = OMcp1_314
    sens.A[1] = ACcp1_112
    sens.A[2] = ACcp1_212
    sens.A[3] = ACcp1_312
    sens.OMP[1] = OPcp1_114
    sens.OMP[2] = OPcp1_214
    sens.OMP[3] = OPcp1_314
 
# 
  elif(isens==3): 


# = = Block_1_0_0_3_0_1 = = 
 
# Sensor Kinematics 


    ROcp2_25 = S4*S5
    ROcp2_35 = -C4*S5
    ROcp2_85 = -S4*C5
    ROcp2_95 = C4*C5
    ROcp2_16 = C5*C6
    ROcp2_26 = ROcp2_25*C6+C4*S6
    ROcp2_36 = ROcp2_35*C6+S4*S6
    ROcp2_46 = -C5*S6
    ROcp2_56 = -(ROcp2_25*S6-C4*C6)
    ROcp2_66 = -(ROcp2_35*S6-S4*C6)
    OMcp2_25 = qd[5]*C4
    OMcp2_35 = qd[5]*S4
    OMcp2_16 = qd[4]+qd[6]*S5
    OMcp2_26 = OMcp2_25+ROcp2_85*qd[6]
    OMcp2_36 = OMcp2_35+ROcp2_95*qd[6]
    OPcp2_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp2_26 = ROcp2_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp2_35*S5-ROcp2_95*qd[4])
    OPcp2_36 = ROcp2_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp2_25*S5-ROcp2_85*qd[4])

# = = Block_1_0_0_3_0_4 = = 
 
# Sensor Kinematics 


    ROcp2_415 = ROcp2_46*C15+S15*S5
    ROcp2_515 = ROcp2_56*C15+ROcp2_85*S15
    ROcp2_615 = ROcp2_66*C15+ROcp2_95*S15
    ROcp2_715 = -(ROcp2_46*S15-C15*S5)
    ROcp2_815 = -(ROcp2_56*S15-ROcp2_85*C15)
    ROcp2_915 = -(ROcp2_66*S15-ROcp2_95*C15)
    ROcp2_416 = ROcp2_415*C16+ROcp2_715*S16
    ROcp2_516 = ROcp2_515*C16+ROcp2_815*S16
    ROcp2_616 = ROcp2_615*C16+ROcp2_915*S16
    ROcp2_716 = -(ROcp2_415*S16-ROcp2_715*C16)
    ROcp2_816 = -(ROcp2_515*S16-ROcp2_815*C16)
    ROcp2_916 = -(ROcp2_615*S16-ROcp2_915*C16)
    ROcp2_417 = ROcp2_416*C17+ROcp2_716*S17
    ROcp2_517 = ROcp2_516*C17+ROcp2_816*S17
    ROcp2_617 = ROcp2_616*C17+ROcp2_916*S17
    ROcp2_717 = -(ROcp2_416*S17-ROcp2_716*C17)
    ROcp2_817 = -(ROcp2_516*S17-ROcp2_816*C17)
    ROcp2_917 = -(ROcp2_616*S17-ROcp2_916*C17)
    ROcp2_118 = ROcp2_16*C18-ROcp2_717*S18
    ROcp2_218 = ROcp2_26*C18-ROcp2_817*S18
    ROcp2_318 = ROcp2_36*C18-ROcp2_917*S18
    ROcp2_718 = ROcp2_16*S18+ROcp2_717*C18
    ROcp2_818 = ROcp2_26*S18+ROcp2_817*C18
    ROcp2_918 = ROcp2_36*S18+ROcp2_917*C18
    RLcp2_115 = ROcp2_16*s.dpt[1,9]+ROcp2_46*s.dpt[2,9]+s.dpt[3,9]*S5
    RLcp2_215 = ROcp2_26*s.dpt[1,9]+ROcp2_56*s.dpt[2,9]+ROcp2_85*s.dpt[3,9]
    RLcp2_315 = ROcp2_36*s.dpt[1,9]+ROcp2_66*s.dpt[2,9]+ROcp2_95*s.dpt[3,9]
    OMcp2_115 = OMcp2_16+ROcp2_16*qd[15]
    OMcp2_215 = OMcp2_26+ROcp2_26*qd[15]
    OMcp2_315 = OMcp2_36+ROcp2_36*qd[15]
    ORcp2_115 = OMcp2_26*RLcp2_315-OMcp2_36*RLcp2_215
    ORcp2_215 = -(OMcp2_16*RLcp2_315-OMcp2_36*RLcp2_115)
    ORcp2_315 = OMcp2_16*RLcp2_215-OMcp2_26*RLcp2_115
    OPcp2_115 = OPcp2_16+ROcp2_16*qdd[15]+qd[15]*(OMcp2_26*ROcp2_36-OMcp2_36*ROcp2_26)
    OPcp2_215 = OPcp2_26+ROcp2_26*qdd[15]-qd[15]*(OMcp2_16*ROcp2_36-OMcp2_36*ROcp2_16)
    OPcp2_315 = OPcp2_36+ROcp2_36*qdd[15]+qd[15]*(OMcp2_16*ROcp2_26-OMcp2_26*ROcp2_16)
    RLcp2_116 = ROcp2_415*s.dpt[2,21]
    RLcp2_216 = ROcp2_515*s.dpt[2,21]
    RLcp2_316 = ROcp2_615*s.dpt[2,21]
    OMcp2_116 = OMcp2_115+ROcp2_16*qd[16]
    OMcp2_216 = OMcp2_215+ROcp2_26*qd[16]
    OMcp2_316 = OMcp2_315+ROcp2_36*qd[16]
    ORcp2_116 = OMcp2_215*RLcp2_316-OMcp2_315*RLcp2_216
    ORcp2_216 = -(OMcp2_115*RLcp2_316-OMcp2_315*RLcp2_116)
    ORcp2_316 = OMcp2_115*RLcp2_216-OMcp2_215*RLcp2_116
    OPcp2_116 = OPcp2_115+ROcp2_16*qdd[16]+qd[16]*(OMcp2_215*ROcp2_36-OMcp2_315*ROcp2_26)
    OPcp2_216 = OPcp2_215+ROcp2_26*qdd[16]-qd[16]*(OMcp2_115*ROcp2_36-OMcp2_315*ROcp2_16)
    OPcp2_316 = OPcp2_315+ROcp2_36*qdd[16]+qd[16]*(OMcp2_115*ROcp2_26-OMcp2_215*ROcp2_16)
    RLcp2_117 = ROcp2_16*s.dpt[1,23]
    RLcp2_217 = ROcp2_26*s.dpt[1,23]
    RLcp2_317 = ROcp2_36*s.dpt[1,23]
    POcp2_117 = RLcp2_115+RLcp2_116+RLcp2_117+q[1]
    POcp2_217 = RLcp2_215+RLcp2_216+RLcp2_217+q[2]
    POcp2_317 = RLcp2_315+RLcp2_316+RLcp2_317+q[3]
    OMcp2_117 = OMcp2_116+ROcp2_16*qd[17]
    OMcp2_217 = OMcp2_216+ROcp2_26*qd[17]
    OMcp2_317 = OMcp2_316+ROcp2_36*qd[17]
    ORcp2_117 = OMcp2_216*RLcp2_317-OMcp2_316*RLcp2_217
    ORcp2_217 = -(OMcp2_116*RLcp2_317-OMcp2_316*RLcp2_117)
    ORcp2_317 = OMcp2_116*RLcp2_217-OMcp2_216*RLcp2_117
    VIcp2_117 = ORcp2_115+ORcp2_116+ORcp2_117+qd[1]
    VIcp2_217 = ORcp2_215+ORcp2_216+ORcp2_217+qd[2]
    VIcp2_317 = ORcp2_315+ORcp2_316+ORcp2_317+qd[3]
    ACcp2_117 = qdd[1]+OMcp2_215*ORcp2_316+OMcp2_216*ORcp2_317+OMcp2_26*ORcp2_315-OMcp2_315*ORcp2_216-OMcp2_316*ORcp2_217-\
   OMcp2_36*ORcp2_215+OPcp2_215*RLcp2_316+OPcp2_216*RLcp2_317+OPcp2_26*RLcp2_315-OPcp2_315*RLcp2_216-OPcp2_316*RLcp2_217-\
   OPcp2_36*RLcp2_215
    ACcp2_217 = qdd[2]-OMcp2_115*ORcp2_316-OMcp2_116*ORcp2_317-OMcp2_16*ORcp2_315+OMcp2_315*ORcp2_116+OMcp2_316*ORcp2_117+\
   OMcp2_36*ORcp2_115-OPcp2_115*RLcp2_316-OPcp2_116*RLcp2_317-OPcp2_16*RLcp2_315+OPcp2_315*RLcp2_116+OPcp2_316*RLcp2_117+\
   OPcp2_36*RLcp2_115
    ACcp2_317 = qdd[3]+OMcp2_115*ORcp2_216+OMcp2_116*ORcp2_217+OMcp2_16*ORcp2_215-OMcp2_215*ORcp2_116-OMcp2_216*ORcp2_117-\
   OMcp2_26*ORcp2_115+OPcp2_115*RLcp2_216+OPcp2_116*RLcp2_217+OPcp2_16*RLcp2_215-OPcp2_215*RLcp2_116-OPcp2_216*RLcp2_117-\
   OPcp2_26*RLcp2_115
    OMcp2_118 = OMcp2_117+ROcp2_417*qd[18]
    OMcp2_218 = OMcp2_217+ROcp2_517*qd[18]
    OMcp2_318 = OMcp2_317+ROcp2_617*qd[18]
    OPcp2_118 = OPcp2_116+ROcp2_16*qdd[17]+ROcp2_417*qdd[18]+qd[17]*(OMcp2_216*ROcp2_36-OMcp2_316*ROcp2_26)+qd[18]*(\
   OMcp2_217*ROcp2_617-OMcp2_317*ROcp2_517)
    OPcp2_218 = OPcp2_216+ROcp2_26*qdd[17]+ROcp2_517*qdd[18]-qd[17]*(OMcp2_116*ROcp2_36-OMcp2_316*ROcp2_16)-qd[18]*(\
   OMcp2_117*ROcp2_617-OMcp2_317*ROcp2_417)
    OPcp2_318 = OPcp2_316+ROcp2_36*qdd[17]+ROcp2_617*qdd[18]+qd[17]*(OMcp2_116*ROcp2_26-OMcp2_216*ROcp2_16)+qd[18]*(\
   OMcp2_117*ROcp2_517-OMcp2_217*ROcp2_417)

# = = Block_1_0_0_3_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp2_117
    sens.P[2] = POcp2_217
    sens.P[3] = POcp2_317
    sens.R[1,1] = ROcp2_118
    sens.R[1,2] = ROcp2_218
    sens.R[1,3] = ROcp2_318
    sens.R[2,1] = ROcp2_417
    sens.R[2,2] = ROcp2_517
    sens.R[2,3] = ROcp2_617
    sens.R[3,1] = ROcp2_718
    sens.R[3,2] = ROcp2_818
    sens.R[3,3] = ROcp2_918
    sens.V[1] = VIcp2_117
    sens.V[2] = VIcp2_217
    sens.V[3] = VIcp2_317
    sens.OM[1] = OMcp2_118
    sens.OM[2] = OMcp2_218
    sens.OM[3] = OMcp2_318
    sens.A[1] = ACcp2_117
    sens.A[2] = ACcp2_217
    sens.A[3] = ACcp2_317
    sens.OMP[1] = OPcp2_118
    sens.OMP[2] = OPcp2_218
    sens.OMP[3] = OPcp2_318
 
# 
  elif(isens==4): 


# = = Block_1_0_0_4_0_1 = = 
 
# Sensor Kinematics 


    ROcp3_25 = S4*S5
    ROcp3_35 = -C4*S5
    ROcp3_85 = -S4*C5
    ROcp3_95 = C4*C5
    ROcp3_16 = C5*C6
    ROcp3_26 = ROcp3_25*C6+C4*S6
    ROcp3_36 = ROcp3_35*C6+S4*S6
    ROcp3_46 = -C5*S6
    ROcp3_56 = -(ROcp3_25*S6-C4*C6)
    ROcp3_66 = -(ROcp3_35*S6-S4*C6)
    OMcp3_25 = qd[5]*C4
    OMcp3_35 = qd[5]*S4
    OMcp3_16 = qd[4]+qd[6]*S5
    OMcp3_26 = OMcp3_25+ROcp3_85*qd[6]
    OMcp3_36 = OMcp3_35+ROcp3_95*qd[6]
    OPcp3_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp3_26 = ROcp3_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp3_35*S5-ROcp3_95*qd[4])
    OPcp3_36 = ROcp3_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp3_25*S5-ROcp3_85*qd[4])

# = = Block_1_0_0_4_0_5 = = 
 
# Sensor Kinematics 


    ROcp3_419 = ROcp3_46*C19+S19*S5
    ROcp3_519 = ROcp3_56*C19+ROcp3_85*S19
    ROcp3_619 = ROcp3_66*C19+ROcp3_95*S19
    ROcp3_719 = -(ROcp3_46*S19-C19*S5)
    ROcp3_819 = -(ROcp3_56*S19-ROcp3_85*C19)
    ROcp3_919 = -(ROcp3_66*S19-ROcp3_95*C19)
    ROcp3_420 = ROcp3_419*C20+ROcp3_719*S20
    ROcp3_520 = ROcp3_519*C20+ROcp3_819*S20
    ROcp3_620 = ROcp3_619*C20+ROcp3_919*S20
    ROcp3_720 = -(ROcp3_419*S20-ROcp3_719*C20)
    ROcp3_820 = -(ROcp3_519*S20-ROcp3_819*C20)
    ROcp3_920 = -(ROcp3_619*S20-ROcp3_919*C20)
    ROcp3_421 = ROcp3_420*C21+ROcp3_720*S21
    ROcp3_521 = ROcp3_520*C21+ROcp3_820*S21
    ROcp3_621 = ROcp3_620*C21+ROcp3_920*S21
    ROcp3_721 = -(ROcp3_420*S21-ROcp3_720*C21)
    ROcp3_821 = -(ROcp3_520*S21-ROcp3_820*C21)
    ROcp3_921 = -(ROcp3_620*S21-ROcp3_920*C21)
    ROcp3_122 = ROcp3_16*C22-ROcp3_721*S22
    ROcp3_222 = ROcp3_26*C22-ROcp3_821*S22
    ROcp3_322 = ROcp3_36*C22-ROcp3_921*S22
    ROcp3_722 = ROcp3_16*S22+ROcp3_721*C22
    ROcp3_822 = ROcp3_26*S22+ROcp3_821*C22
    ROcp3_922 = ROcp3_36*S22+ROcp3_921*C22
    RLcp3_119 = ROcp3_16*s.dpt[1,11]+ROcp3_46*s.dpt[2,11]+s.dpt[3,11]*S5
    RLcp3_219 = ROcp3_26*s.dpt[1,11]+ROcp3_56*s.dpt[2,11]+ROcp3_85*s.dpt[3,11]
    RLcp3_319 = ROcp3_36*s.dpt[1,11]+ROcp3_66*s.dpt[2,11]+ROcp3_95*s.dpt[3,11]
    OMcp3_119 = OMcp3_16+ROcp3_16*qd[19]
    OMcp3_219 = OMcp3_26+ROcp3_26*qd[19]
    OMcp3_319 = OMcp3_36+ROcp3_36*qd[19]
    ORcp3_119 = OMcp3_26*RLcp3_319-OMcp3_36*RLcp3_219
    ORcp3_219 = -(OMcp3_16*RLcp3_319-OMcp3_36*RLcp3_119)
    ORcp3_319 = OMcp3_16*RLcp3_219-OMcp3_26*RLcp3_119
    OPcp3_119 = OPcp3_16+ROcp3_16*qdd[19]+qd[19]*(OMcp3_26*ROcp3_36-OMcp3_36*ROcp3_26)
    OPcp3_219 = OPcp3_26+ROcp3_26*qdd[19]-qd[19]*(OMcp3_16*ROcp3_36-OMcp3_36*ROcp3_16)
    OPcp3_319 = OPcp3_36+ROcp3_36*qdd[19]+qd[19]*(OMcp3_16*ROcp3_26-OMcp3_26*ROcp3_16)
    RLcp3_120 = ROcp3_419*s.dpt[2,27]
    RLcp3_220 = ROcp3_519*s.dpt[2,27]
    RLcp3_320 = ROcp3_619*s.dpt[2,27]
    OMcp3_120 = OMcp3_119+ROcp3_16*qd[20]
    OMcp3_220 = OMcp3_219+ROcp3_26*qd[20]
    OMcp3_320 = OMcp3_319+ROcp3_36*qd[20]
    ORcp3_120 = OMcp3_219*RLcp3_320-OMcp3_319*RLcp3_220
    ORcp3_220 = -(OMcp3_119*RLcp3_320-OMcp3_319*RLcp3_120)
    ORcp3_320 = OMcp3_119*RLcp3_220-OMcp3_219*RLcp3_120
    OPcp3_120 = OPcp3_119+ROcp3_16*qdd[20]+qd[20]*(OMcp3_219*ROcp3_36-OMcp3_319*ROcp3_26)
    OPcp3_220 = OPcp3_219+ROcp3_26*qdd[20]-qd[20]*(OMcp3_119*ROcp3_36-OMcp3_319*ROcp3_16)
    OPcp3_320 = OPcp3_319+ROcp3_36*qdd[20]+qd[20]*(OMcp3_119*ROcp3_26-OMcp3_219*ROcp3_16)
    RLcp3_121 = ROcp3_16*s.dpt[1,31]
    RLcp3_221 = ROcp3_26*s.dpt[1,31]
    RLcp3_321 = ROcp3_36*s.dpt[1,31]
    POcp3_121 = RLcp3_119+RLcp3_120+RLcp3_121+q[1]
    POcp3_221 = RLcp3_219+RLcp3_220+RLcp3_221+q[2]
    POcp3_321 = RLcp3_319+RLcp3_320+RLcp3_321+q[3]
    OMcp3_121 = OMcp3_120+ROcp3_16*qd[21]
    OMcp3_221 = OMcp3_220+ROcp3_26*qd[21]
    OMcp3_321 = OMcp3_320+ROcp3_36*qd[21]
    ORcp3_121 = OMcp3_220*RLcp3_321-OMcp3_320*RLcp3_221
    ORcp3_221 = -(OMcp3_120*RLcp3_321-OMcp3_320*RLcp3_121)
    ORcp3_321 = OMcp3_120*RLcp3_221-OMcp3_220*RLcp3_121
    VIcp3_121 = ORcp3_119+ORcp3_120+ORcp3_121+qd[1]
    VIcp3_221 = ORcp3_219+ORcp3_220+ORcp3_221+qd[2]
    VIcp3_321 = ORcp3_319+ORcp3_320+ORcp3_321+qd[3]
    ACcp3_121 = qdd[1]+OMcp3_219*ORcp3_320+OMcp3_220*ORcp3_321+OMcp3_26*ORcp3_319-OMcp3_319*ORcp3_220-OMcp3_320*ORcp3_221-\
   OMcp3_36*ORcp3_219+OPcp3_219*RLcp3_320+OPcp3_220*RLcp3_321+OPcp3_26*RLcp3_319-OPcp3_319*RLcp3_220-OPcp3_320*RLcp3_221-\
   OPcp3_36*RLcp3_219
    ACcp3_221 = qdd[2]-OMcp3_119*ORcp3_320-OMcp3_120*ORcp3_321-OMcp3_16*ORcp3_319+OMcp3_319*ORcp3_120+OMcp3_320*ORcp3_121+\
   OMcp3_36*ORcp3_119-OPcp3_119*RLcp3_320-OPcp3_120*RLcp3_321-OPcp3_16*RLcp3_319+OPcp3_319*RLcp3_120+OPcp3_320*RLcp3_121+\
   OPcp3_36*RLcp3_119
    ACcp3_321 = qdd[3]+OMcp3_119*ORcp3_220+OMcp3_120*ORcp3_221+OMcp3_16*ORcp3_219-OMcp3_219*ORcp3_120-OMcp3_220*ORcp3_121-\
   OMcp3_26*ORcp3_119+OPcp3_119*RLcp3_220+OPcp3_120*RLcp3_221+OPcp3_16*RLcp3_219-OPcp3_219*RLcp3_120-OPcp3_220*RLcp3_121-\
   OPcp3_26*RLcp3_119
    OMcp3_122 = OMcp3_121+ROcp3_421*qd[22]
    OMcp3_222 = OMcp3_221+ROcp3_521*qd[22]
    OMcp3_322 = OMcp3_321+ROcp3_621*qd[22]
    OPcp3_122 = OPcp3_120+ROcp3_16*qdd[21]+ROcp3_421*qdd[22]+qd[21]*(OMcp3_220*ROcp3_36-OMcp3_320*ROcp3_26)+qd[22]*(\
   OMcp3_221*ROcp3_621-OMcp3_321*ROcp3_521)
    OPcp3_222 = OPcp3_220+ROcp3_26*qdd[21]+ROcp3_521*qdd[22]-qd[21]*(OMcp3_120*ROcp3_36-OMcp3_320*ROcp3_16)-qd[22]*(\
   OMcp3_121*ROcp3_621-OMcp3_321*ROcp3_421)
    OPcp3_322 = OPcp3_320+ROcp3_36*qdd[21]+ROcp3_621*qdd[22]+qd[21]*(OMcp3_120*ROcp3_26-OMcp3_220*ROcp3_16)+qd[22]*(\
   OMcp3_121*ROcp3_521-OMcp3_221*ROcp3_421)

# = = Block_1_0_0_4_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp3_121
    sens.P[2] = POcp3_221
    sens.P[3] = POcp3_321
    sens.R[1,1] = ROcp3_122
    sens.R[1,2] = ROcp3_222
    sens.R[1,3] = ROcp3_322
    sens.R[2,1] = ROcp3_421
    sens.R[2,2] = ROcp3_521
    sens.R[2,3] = ROcp3_621
    sens.R[3,1] = ROcp3_722
    sens.R[3,2] = ROcp3_822
    sens.R[3,3] = ROcp3_922
    sens.V[1] = VIcp3_121
    sens.V[2] = VIcp3_221
    sens.V[3] = VIcp3_321
    sens.OM[1] = OMcp3_122
    sens.OM[2] = OMcp3_222
    sens.OM[3] = OMcp3_322
    sens.A[1] = ACcp3_121
    sens.A[2] = ACcp3_221
    sens.A[3] = ACcp3_321
    sens.OMP[1] = OPcp3_122
    sens.OMP[2] = OPcp3_222
    sens.OMP[3] = OPcp3_322



# ====== END Task 1 ====== 

  

