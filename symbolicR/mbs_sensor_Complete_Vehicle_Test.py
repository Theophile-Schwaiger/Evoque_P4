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
#	==> Generation Date : Sun Mar 15 20:44:10 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 18
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 1316
#
#	==> Generation Time :  0.020 seconds
#	==> Post-Processing :  0.020 seconds
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

# = = Block_0_0_0_0_0_3 = = 
 
# Trigonometric Variables  

  C10 = np.cos(q[10])
  S10 = np.sin(q[10])
  C11 = np.cos(q[11])
  S11 = np.sin(q[11])
  C12 = np.cos(q[12])
  S12 = np.sin(q[12])

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C13 = np.cos(q[13])
  S13 = np.sin(q[13])
  C14 = np.cos(q[14])
  S14 = np.sin(q[14])
  C15 = np.cos(q[15])
  S15 = np.sin(q[15])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C16 = np.cos(q[16])
  S16 = np.sin(q[16])
  C17 = np.cos(q[17])
  S17 = np.sin(q[17])
  C18 = np.cos(q[18])
  S18 = np.sin(q[18])

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
    OPcp0_19 = OPcp0_17+ROcp0_18*qdd[9]+ROcp0_77*qdd[8]+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(OMcp0_28*\
   ROcp0_38-OMcp0_38*ROcp0_28)
    OPcp0_29 = OPcp0_27+ROcp0_28*qdd[9]+ROcp0_87*qdd[8]-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(OMcp0_18*\
   ROcp0_38-OMcp0_38*ROcp0_18)
    OPcp0_39 = OPcp0_37+ROcp0_38*qdd[9]+ROcp0_97*qdd[8]+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(OMcp0_18*\
   ROcp0_28-OMcp0_28*ROcp0_18)

# = = Block_1_0_0_1_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp0_18
    sens.P[2] = POcp0_28
    sens.P[3] = POcp0_38
    sens.R[1,1] = ROcp0_18
    sens.R[1,2] = ROcp0_28
    sens.R[1,3] = ROcp0_38
    sens.R[2,1] = ROcp0_49
    sens.R[2,2] = ROcp0_59
    sens.R[2,3] = ROcp0_69
    sens.R[3,1] = ROcp0_79
    sens.R[3,2] = ROcp0_89
    sens.R[3,3] = ROcp0_99
    sens.V[1] = VIcp0_18
    sens.V[2] = VIcp0_28
    sens.V[3] = VIcp0_38
    sens.OM[1] = OMcp0_19
    sens.OM[2] = OMcp0_29
    sens.OM[3] = OMcp0_39
    sens.A[1] = ACcp0_18
    sens.A[2] = ACcp0_28
    sens.A[3] = ACcp0_38
    sens.OMP[1] = OPcp0_19
    sens.OMP[2] = OPcp0_29
    sens.OMP[3] = OPcp0_39
 
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


    ROcp1_410 = ROcp1_46*C10+S10*S5
    ROcp1_510 = ROcp1_56*C10+ROcp1_85*S10
    ROcp1_610 = ROcp1_66*C10+ROcp1_95*S10
    ROcp1_710 = -(ROcp1_46*S10-C10*S5)
    ROcp1_810 = -(ROcp1_56*S10-ROcp1_85*C10)
    ROcp1_910 = -(ROcp1_66*S10-ROcp1_95*C10)
    ROcp1_111 = ROcp1_16*C11+ROcp1_410*S11
    ROcp1_211 = ROcp1_26*C11+ROcp1_510*S11
    ROcp1_311 = ROcp1_36*C11+ROcp1_610*S11
    ROcp1_411 = -(ROcp1_16*S11-ROcp1_410*C11)
    ROcp1_511 = -(ROcp1_26*S11-ROcp1_510*C11)
    ROcp1_611 = -(ROcp1_36*S11-ROcp1_610*C11)
    ROcp1_412 = ROcp1_411*C12+ROcp1_710*S12
    ROcp1_512 = ROcp1_511*C12+ROcp1_810*S12
    ROcp1_612 = ROcp1_611*C12+ROcp1_910*S12
    ROcp1_712 = -(ROcp1_411*S12-ROcp1_710*C12)
    ROcp1_812 = -(ROcp1_511*S12-ROcp1_810*C12)
    ROcp1_912 = -(ROcp1_611*S12-ROcp1_910*C12)
    RLcp1_110 = ROcp1_16*s.dpt[1,4]+ROcp1_46*s.dpt[2,4]+s.dpt[3,4]*S5
    RLcp1_210 = ROcp1_26*s.dpt[1,4]+ROcp1_56*s.dpt[2,4]+ROcp1_85*s.dpt[3,4]
    RLcp1_310 = ROcp1_36*s.dpt[1,4]+ROcp1_66*s.dpt[2,4]+ROcp1_95*s.dpt[3,4]
    OMcp1_110 = OMcp1_16+ROcp1_16*qd[10]
    OMcp1_210 = OMcp1_26+ROcp1_26*qd[10]
    OMcp1_310 = OMcp1_36+ROcp1_36*qd[10]
    ORcp1_110 = OMcp1_26*RLcp1_310-OMcp1_36*RLcp1_210
    ORcp1_210 = -(OMcp1_16*RLcp1_310-OMcp1_36*RLcp1_110)
    ORcp1_310 = OMcp1_16*RLcp1_210-OMcp1_26*RLcp1_110
    OPcp1_110 = OPcp1_16+ROcp1_16*qdd[10]+qd[10]*(OMcp1_26*ROcp1_36-OMcp1_36*ROcp1_26)
    OPcp1_210 = OPcp1_26+ROcp1_26*qdd[10]-qd[10]*(OMcp1_16*ROcp1_36-OMcp1_36*ROcp1_16)
    OPcp1_310 = OPcp1_36+ROcp1_36*qdd[10]+qd[10]*(OMcp1_16*ROcp1_26-OMcp1_26*ROcp1_16)
    RLcp1_111 = ROcp1_410*s.dpt[2,17]
    RLcp1_211 = ROcp1_510*s.dpt[2,17]
    RLcp1_311 = ROcp1_610*s.dpt[2,17]
    POcp1_111 = RLcp1_110+RLcp1_111+q[1]
    POcp1_211 = RLcp1_210+RLcp1_211+q[2]
    POcp1_311 = RLcp1_310+RLcp1_311+q[3]
    OMcp1_111 = OMcp1_110+ROcp1_710*qd[11]
    OMcp1_211 = OMcp1_210+ROcp1_810*qd[11]
    OMcp1_311 = OMcp1_310+ROcp1_910*qd[11]
    ORcp1_111 = OMcp1_210*RLcp1_311-OMcp1_310*RLcp1_211
    ORcp1_211 = -(OMcp1_110*RLcp1_311-OMcp1_310*RLcp1_111)
    ORcp1_311 = OMcp1_110*RLcp1_211-OMcp1_210*RLcp1_111
    VIcp1_111 = ORcp1_110+ORcp1_111+qd[1]
    VIcp1_211 = ORcp1_210+ORcp1_211+qd[2]
    VIcp1_311 = ORcp1_310+ORcp1_311+qd[3]
    ACcp1_111 = qdd[1]+OMcp1_210*ORcp1_311+OMcp1_26*ORcp1_310-OMcp1_310*ORcp1_211-OMcp1_36*ORcp1_210+OPcp1_210*RLcp1_311+\
   OPcp1_26*RLcp1_310-OPcp1_310*RLcp1_211-OPcp1_36*RLcp1_210
    ACcp1_211 = qdd[2]-OMcp1_110*ORcp1_311-OMcp1_16*ORcp1_310+OMcp1_310*ORcp1_111+OMcp1_36*ORcp1_110-OPcp1_110*RLcp1_311-\
   OPcp1_16*RLcp1_310+OPcp1_310*RLcp1_111+OPcp1_36*RLcp1_110
    ACcp1_311 = qdd[3]+OMcp1_110*ORcp1_211+OMcp1_16*ORcp1_210-OMcp1_210*ORcp1_111-OMcp1_26*ORcp1_110+OPcp1_110*RLcp1_211+\
   OPcp1_16*RLcp1_210-OPcp1_210*RLcp1_111-OPcp1_26*RLcp1_110
    OMcp1_112 = OMcp1_111+ROcp1_111*qd[12]
    OMcp1_212 = OMcp1_211+ROcp1_211*qd[12]
    OMcp1_312 = OMcp1_311+ROcp1_311*qd[12]
    OPcp1_112 = OPcp1_110+ROcp1_111*qdd[12]+ROcp1_710*qdd[11]+qd[11]*(OMcp1_210*ROcp1_910-OMcp1_310*ROcp1_810)+qd[12]*(\
   OMcp1_211*ROcp1_311-OMcp1_311*ROcp1_211)
    OPcp1_212 = OPcp1_210+ROcp1_211*qdd[12]+ROcp1_810*qdd[11]-qd[11]*(OMcp1_110*ROcp1_910-OMcp1_310*ROcp1_710)-qd[12]*(\
   OMcp1_111*ROcp1_311-OMcp1_311*ROcp1_111)
    OPcp1_312 = OPcp1_310+ROcp1_311*qdd[12]+ROcp1_910*qdd[11]+qd[11]*(OMcp1_110*ROcp1_810-OMcp1_210*ROcp1_710)+qd[12]*(\
   OMcp1_111*ROcp1_211-OMcp1_211*ROcp1_111)

# = = Block_1_0_0_2_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp1_111
    sens.P[2] = POcp1_211
    sens.P[3] = POcp1_311
    sens.R[1,1] = ROcp1_111
    sens.R[1,2] = ROcp1_211
    sens.R[1,3] = ROcp1_311
    sens.R[2,1] = ROcp1_412
    sens.R[2,2] = ROcp1_512
    sens.R[2,3] = ROcp1_612
    sens.R[3,1] = ROcp1_712
    sens.R[3,2] = ROcp1_812
    sens.R[3,3] = ROcp1_912
    sens.V[1] = VIcp1_111
    sens.V[2] = VIcp1_211
    sens.V[3] = VIcp1_311
    sens.OM[1] = OMcp1_112
    sens.OM[2] = OMcp1_212
    sens.OM[3] = OMcp1_312
    sens.A[1] = ACcp1_111
    sens.A[2] = ACcp1_211
    sens.A[3] = ACcp1_311
    sens.OMP[1] = OPcp1_112
    sens.OMP[2] = OPcp1_212
    sens.OMP[3] = OPcp1_312
 
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


    ROcp2_413 = ROcp2_46*C13+S13*S5
    ROcp2_513 = ROcp2_56*C13+ROcp2_85*S13
    ROcp2_613 = ROcp2_66*C13+ROcp2_95*S13
    ROcp2_713 = -(ROcp2_46*S13-C13*S5)
    ROcp2_813 = -(ROcp2_56*S13-ROcp2_85*C13)
    ROcp2_913 = -(ROcp2_66*S13-ROcp2_95*C13)
    ROcp2_414 = ROcp2_413*C14+ROcp2_713*S14
    ROcp2_514 = ROcp2_513*C14+ROcp2_813*S14
    ROcp2_614 = ROcp2_613*C14+ROcp2_913*S14
    ROcp2_714 = -(ROcp2_413*S14-ROcp2_713*C14)
    ROcp2_814 = -(ROcp2_513*S14-ROcp2_813*C14)
    ROcp2_914 = -(ROcp2_613*S14-ROcp2_913*C14)
    ROcp2_415 = ROcp2_414*C15+ROcp2_714*S15
    ROcp2_515 = ROcp2_514*C15+ROcp2_814*S15
    ROcp2_615 = ROcp2_614*C15+ROcp2_914*S15
    ROcp2_715 = -(ROcp2_414*S15-ROcp2_714*C15)
    ROcp2_815 = -(ROcp2_514*S15-ROcp2_814*C15)
    ROcp2_915 = -(ROcp2_614*S15-ROcp2_914*C15)
    RLcp2_113 = ROcp2_16*s.dpt[1,9]+ROcp2_46*s.dpt[2,9]+s.dpt[3,9]*S5
    RLcp2_213 = ROcp2_26*s.dpt[1,9]+ROcp2_56*s.dpt[2,9]+ROcp2_85*s.dpt[3,9]
    RLcp2_313 = ROcp2_36*s.dpt[1,9]+ROcp2_66*s.dpt[2,9]+ROcp2_95*s.dpt[3,9]
    OMcp2_113 = OMcp2_16+ROcp2_16*qd[13]
    OMcp2_213 = OMcp2_26+ROcp2_26*qd[13]
    OMcp2_313 = OMcp2_36+ROcp2_36*qd[13]
    ORcp2_113 = OMcp2_26*RLcp2_313-OMcp2_36*RLcp2_213
    ORcp2_213 = -(OMcp2_16*RLcp2_313-OMcp2_36*RLcp2_113)
    ORcp2_313 = OMcp2_16*RLcp2_213-OMcp2_26*RLcp2_113
    OPcp2_113 = OPcp2_16+ROcp2_16*qdd[13]+qd[13]*(OMcp2_26*ROcp2_36-OMcp2_36*ROcp2_26)
    OPcp2_213 = OPcp2_26+ROcp2_26*qdd[13]-qd[13]*(OMcp2_16*ROcp2_36-OMcp2_36*ROcp2_16)
    OPcp2_313 = OPcp2_36+ROcp2_36*qdd[13]+qd[13]*(OMcp2_16*ROcp2_26-OMcp2_26*ROcp2_16)
    RLcp2_114 = ROcp2_413*s.dpt[2,21]
    RLcp2_214 = ROcp2_513*s.dpt[2,21]
    RLcp2_314 = ROcp2_613*s.dpt[2,21]
    OMcp2_114 = OMcp2_113+ROcp2_16*qd[14]
    OMcp2_214 = OMcp2_213+ROcp2_26*qd[14]
    OMcp2_314 = OMcp2_313+ROcp2_36*qd[14]
    ORcp2_114 = OMcp2_213*RLcp2_314-OMcp2_313*RLcp2_214
    ORcp2_214 = -(OMcp2_113*RLcp2_314-OMcp2_313*RLcp2_114)
    ORcp2_314 = OMcp2_113*RLcp2_214-OMcp2_213*RLcp2_114
    OPcp2_114 = OPcp2_113+ROcp2_16*qdd[14]+qd[14]*(OMcp2_213*ROcp2_36-OMcp2_313*ROcp2_26)
    OPcp2_214 = OPcp2_213+ROcp2_26*qdd[14]-qd[14]*(OMcp2_113*ROcp2_36-OMcp2_313*ROcp2_16)
    OPcp2_314 = OPcp2_313+ROcp2_36*qdd[14]+qd[14]*(OMcp2_113*ROcp2_26-OMcp2_213*ROcp2_16)
    RLcp2_115 = ROcp2_16*s.dpt[1,23]
    RLcp2_215 = ROcp2_26*s.dpt[1,23]
    RLcp2_315 = ROcp2_36*s.dpt[1,23]
    POcp2_115 = RLcp2_113+RLcp2_114+RLcp2_115+q[1]
    POcp2_215 = RLcp2_213+RLcp2_214+RLcp2_215+q[2]
    POcp2_315 = RLcp2_313+RLcp2_314+RLcp2_315+q[3]
    OMcp2_115 = OMcp2_114+ROcp2_16*qd[15]
    OMcp2_215 = OMcp2_214+ROcp2_26*qd[15]
    OMcp2_315 = OMcp2_314+ROcp2_36*qd[15]
    ORcp2_115 = OMcp2_214*RLcp2_315-OMcp2_314*RLcp2_215
    ORcp2_215 = -(OMcp2_114*RLcp2_315-OMcp2_314*RLcp2_115)
    ORcp2_315 = OMcp2_114*RLcp2_215-OMcp2_214*RLcp2_115
    VIcp2_115 = ORcp2_113+ORcp2_114+ORcp2_115+qd[1]
    VIcp2_215 = ORcp2_213+ORcp2_214+ORcp2_215+qd[2]
    VIcp2_315 = ORcp2_313+ORcp2_314+ORcp2_315+qd[3]
    OPcp2_115 = OPcp2_114+ROcp2_16*qdd[15]+qd[15]*(OMcp2_214*ROcp2_36-OMcp2_314*ROcp2_26)
    OPcp2_215 = OPcp2_214+ROcp2_26*qdd[15]-qd[15]*(OMcp2_114*ROcp2_36-OMcp2_314*ROcp2_16)
    OPcp2_315 = OPcp2_314+ROcp2_36*qdd[15]+qd[15]*(OMcp2_114*ROcp2_26-OMcp2_214*ROcp2_16)
    ACcp2_115 = qdd[1]+OMcp2_213*ORcp2_314+OMcp2_214*ORcp2_315+OMcp2_26*ORcp2_313-OMcp2_313*ORcp2_214-OMcp2_314*ORcp2_215-\
   OMcp2_36*ORcp2_213+OPcp2_213*RLcp2_314+OPcp2_214*RLcp2_315+OPcp2_26*RLcp2_313-OPcp2_313*RLcp2_214-OPcp2_314*RLcp2_215-\
   OPcp2_36*RLcp2_213
    ACcp2_215 = qdd[2]-OMcp2_113*ORcp2_314-OMcp2_114*ORcp2_315-OMcp2_16*ORcp2_313+OMcp2_313*ORcp2_114+OMcp2_314*ORcp2_115+\
   OMcp2_36*ORcp2_113-OPcp2_113*RLcp2_314-OPcp2_114*RLcp2_315-OPcp2_16*RLcp2_313+OPcp2_313*RLcp2_114+OPcp2_314*RLcp2_115+\
   OPcp2_36*RLcp2_113
    ACcp2_315 = qdd[3]+OMcp2_113*ORcp2_214+OMcp2_114*ORcp2_215+OMcp2_16*ORcp2_213-OMcp2_213*ORcp2_114-OMcp2_214*ORcp2_115-\
   OMcp2_26*ORcp2_113+OPcp2_113*RLcp2_214+OPcp2_114*RLcp2_215+OPcp2_16*RLcp2_213-OPcp2_213*RLcp2_114-OPcp2_214*RLcp2_115-\
   OPcp2_26*RLcp2_113

# = = Block_1_0_0_3_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp2_115
    sens.P[2] = POcp2_215
    sens.P[3] = POcp2_315
    sens.R[1,1] = ROcp2_16
    sens.R[1,2] = ROcp2_26
    sens.R[1,3] = ROcp2_36
    sens.R[2,1] = ROcp2_415
    sens.R[2,2] = ROcp2_515
    sens.R[2,3] = ROcp2_615
    sens.R[3,1] = ROcp2_715
    sens.R[3,2] = ROcp2_815
    sens.R[3,3] = ROcp2_915
    sens.V[1] = VIcp2_115
    sens.V[2] = VIcp2_215
    sens.V[3] = VIcp2_315
    sens.OM[1] = OMcp2_115
    sens.OM[2] = OMcp2_215
    sens.OM[3] = OMcp2_315
    sens.A[1] = ACcp2_115
    sens.A[2] = ACcp2_215
    sens.A[3] = ACcp2_315
    sens.OMP[1] = OPcp2_115
    sens.OMP[2] = OPcp2_215
    sens.OMP[3] = OPcp2_315
 
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


    ROcp3_416 = ROcp3_46*C16+S16*S5
    ROcp3_516 = ROcp3_56*C16+ROcp3_85*S16
    ROcp3_616 = ROcp3_66*C16+ROcp3_95*S16
    ROcp3_716 = -(ROcp3_46*S16-C16*S5)
    ROcp3_816 = -(ROcp3_56*S16-ROcp3_85*C16)
    ROcp3_916 = -(ROcp3_66*S16-ROcp3_95*C16)
    ROcp3_417 = ROcp3_416*C17+ROcp3_716*S17
    ROcp3_517 = ROcp3_516*C17+ROcp3_816*S17
    ROcp3_617 = ROcp3_616*C17+ROcp3_916*S17
    ROcp3_717 = -(ROcp3_416*S17-ROcp3_716*C17)
    ROcp3_817 = -(ROcp3_516*S17-ROcp3_816*C17)
    ROcp3_917 = -(ROcp3_616*S17-ROcp3_916*C17)
    ROcp3_418 = ROcp3_417*C18+ROcp3_717*S18
    ROcp3_518 = ROcp3_517*C18+ROcp3_817*S18
    ROcp3_618 = ROcp3_617*C18+ROcp3_917*S18
    ROcp3_718 = -(ROcp3_417*S18-ROcp3_717*C18)
    ROcp3_818 = -(ROcp3_517*S18-ROcp3_817*C18)
    ROcp3_918 = -(ROcp3_617*S18-ROcp3_917*C18)
    RLcp3_116 = ROcp3_16*s.dpt[1,11]+ROcp3_46*s.dpt[2,11]+s.dpt[3,11]*S5
    RLcp3_216 = ROcp3_26*s.dpt[1,11]+ROcp3_56*s.dpt[2,11]+ROcp3_85*s.dpt[3,11]
    RLcp3_316 = ROcp3_36*s.dpt[1,11]+ROcp3_66*s.dpt[2,11]+ROcp3_95*s.dpt[3,11]
    OMcp3_116 = OMcp3_16+ROcp3_16*qd[16]
    OMcp3_216 = OMcp3_26+ROcp3_26*qd[16]
    OMcp3_316 = OMcp3_36+ROcp3_36*qd[16]
    ORcp3_116 = OMcp3_26*RLcp3_316-OMcp3_36*RLcp3_216
    ORcp3_216 = -(OMcp3_16*RLcp3_316-OMcp3_36*RLcp3_116)
    ORcp3_316 = OMcp3_16*RLcp3_216-OMcp3_26*RLcp3_116
    OPcp3_116 = OPcp3_16+ROcp3_16*qdd[16]+qd[16]*(OMcp3_26*ROcp3_36-OMcp3_36*ROcp3_26)
    OPcp3_216 = OPcp3_26+ROcp3_26*qdd[16]-qd[16]*(OMcp3_16*ROcp3_36-OMcp3_36*ROcp3_16)
    OPcp3_316 = OPcp3_36+ROcp3_36*qdd[16]+qd[16]*(OMcp3_16*ROcp3_26-OMcp3_26*ROcp3_16)
    RLcp3_117 = ROcp3_416*s.dpt[2,27]
    RLcp3_217 = ROcp3_516*s.dpt[2,27]
    RLcp3_317 = ROcp3_616*s.dpt[2,27]
    OMcp3_117 = OMcp3_116+ROcp3_16*qd[17]
    OMcp3_217 = OMcp3_216+ROcp3_26*qd[17]
    OMcp3_317 = OMcp3_316+ROcp3_36*qd[17]
    ORcp3_117 = OMcp3_216*RLcp3_317-OMcp3_316*RLcp3_217
    ORcp3_217 = -(OMcp3_116*RLcp3_317-OMcp3_316*RLcp3_117)
    ORcp3_317 = OMcp3_116*RLcp3_217-OMcp3_216*RLcp3_117
    OPcp3_117 = OPcp3_116+ROcp3_16*qdd[17]+qd[17]*(OMcp3_216*ROcp3_36-OMcp3_316*ROcp3_26)
    OPcp3_217 = OPcp3_216+ROcp3_26*qdd[17]-qd[17]*(OMcp3_116*ROcp3_36-OMcp3_316*ROcp3_16)
    OPcp3_317 = OPcp3_316+ROcp3_36*qdd[17]+qd[17]*(OMcp3_116*ROcp3_26-OMcp3_216*ROcp3_16)
    RLcp3_118 = ROcp3_16*s.dpt[1,31]
    RLcp3_218 = ROcp3_26*s.dpt[1,31]
    RLcp3_318 = ROcp3_36*s.dpt[1,31]
    POcp3_118 = RLcp3_116+RLcp3_117+RLcp3_118+q[1]
    POcp3_218 = RLcp3_216+RLcp3_217+RLcp3_218+q[2]
    POcp3_318 = RLcp3_316+RLcp3_317+RLcp3_318+q[3]
    OMcp3_118 = OMcp3_117+ROcp3_16*qd[18]
    OMcp3_218 = OMcp3_217+ROcp3_26*qd[18]
    OMcp3_318 = OMcp3_317+ROcp3_36*qd[18]
    ORcp3_118 = OMcp3_217*RLcp3_318-OMcp3_317*RLcp3_218
    ORcp3_218 = -(OMcp3_117*RLcp3_318-OMcp3_317*RLcp3_118)
    ORcp3_318 = OMcp3_117*RLcp3_218-OMcp3_217*RLcp3_118
    VIcp3_118 = ORcp3_116+ORcp3_117+ORcp3_118+qd[1]
    VIcp3_218 = ORcp3_216+ORcp3_217+ORcp3_218+qd[2]
    VIcp3_318 = ORcp3_316+ORcp3_317+ORcp3_318+qd[3]
    OPcp3_118 = OPcp3_117+ROcp3_16*qdd[18]+qd[18]*(OMcp3_217*ROcp3_36-OMcp3_317*ROcp3_26)
    OPcp3_218 = OPcp3_217+ROcp3_26*qdd[18]-qd[18]*(OMcp3_117*ROcp3_36-OMcp3_317*ROcp3_16)
    OPcp3_318 = OPcp3_317+ROcp3_36*qdd[18]+qd[18]*(OMcp3_117*ROcp3_26-OMcp3_217*ROcp3_16)
    ACcp3_118 = qdd[1]+OMcp3_216*ORcp3_317+OMcp3_217*ORcp3_318+OMcp3_26*ORcp3_316-OMcp3_316*ORcp3_217-OMcp3_317*ORcp3_218-\
   OMcp3_36*ORcp3_216+OPcp3_216*RLcp3_317+OPcp3_217*RLcp3_318+OPcp3_26*RLcp3_316-OPcp3_316*RLcp3_217-OPcp3_317*RLcp3_218-\
   OPcp3_36*RLcp3_216
    ACcp3_218 = qdd[2]-OMcp3_116*ORcp3_317-OMcp3_117*ORcp3_318-OMcp3_16*ORcp3_316+OMcp3_316*ORcp3_117+OMcp3_317*ORcp3_118+\
   OMcp3_36*ORcp3_116-OPcp3_116*RLcp3_317-OPcp3_117*RLcp3_318-OPcp3_16*RLcp3_316+OPcp3_316*RLcp3_117+OPcp3_317*RLcp3_118+\
   OPcp3_36*RLcp3_116
    ACcp3_318 = qdd[3]+OMcp3_116*ORcp3_217+OMcp3_117*ORcp3_218+OMcp3_16*ORcp3_216-OMcp3_216*ORcp3_117-OMcp3_217*ORcp3_118-\
   OMcp3_26*ORcp3_116+OPcp3_116*RLcp3_217+OPcp3_117*RLcp3_218+OPcp3_16*RLcp3_216-OPcp3_216*RLcp3_117-OPcp3_217*RLcp3_118-\
   OPcp3_26*RLcp3_116

# = = Block_1_0_0_4_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp3_118
    sens.P[2] = POcp3_218
    sens.P[3] = POcp3_318
    sens.R[1,1] = ROcp3_16
    sens.R[1,2] = ROcp3_26
    sens.R[1,3] = ROcp3_36
    sens.R[2,1] = ROcp3_418
    sens.R[2,2] = ROcp3_518
    sens.R[2,3] = ROcp3_618
    sens.R[3,1] = ROcp3_718
    sens.R[3,2] = ROcp3_818
    sens.R[3,3] = ROcp3_918
    sens.V[1] = VIcp3_118
    sens.V[2] = VIcp3_218
    sens.V[3] = VIcp3_318
    sens.OM[1] = OMcp3_118
    sens.OM[2] = OMcp3_218
    sens.OM[3] = OMcp3_318
    sens.A[1] = ACcp3_118
    sens.A[2] = ACcp3_218
    sens.A[3] = ACcp3_318
    sens.OMP[1] = OPcp3_118
    sens.OMP[2] = OPcp3_218
    sens.OMP[3] = OPcp3_318



# ====== END Task 1 ====== 

  

