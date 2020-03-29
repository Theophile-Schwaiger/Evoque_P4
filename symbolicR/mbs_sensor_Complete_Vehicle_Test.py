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
#	==> Generation Date : Thu Mar 26 17:28:13 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 18
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 2632
#
#	==> Generation Time :  0.040 seconds
#	==> Post-Processing :  0.050 seconds
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


    ROcp0_45 = -S4*C5
    ROcp0_55 = C4*C5
    ROcp0_75 = S4*S5
    ROcp0_85 = -C4*S5
    ROcp0_16 = -(ROcp0_75*S6-C4*C6)
    ROcp0_26 = -(ROcp0_85*S6-S4*C6)
    ROcp0_36 = -C5*S6
    ROcp0_76 = ROcp0_75*C6+C4*S6
    ROcp0_86 = ROcp0_85*C6+S4*S6
    ROcp0_96 = C5*C6
    OMcp0_15 = qd[5]*C4
    OMcp0_25 = qd[5]*S4
    OMcp0_16 = OMcp0_15+ROcp0_45*qd[6]
    OMcp0_26 = OMcp0_25+ROcp0_55*qd[6]
    OMcp0_36 = qd[4]+qd[6]*S5
    OPcp0_16 = ROcp0_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp0_25*S5-ROcp0_55*qd[4])
    OPcp0_26 = ROcp0_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp0_15*S5-ROcp0_45*qd[4])
    OPcp0_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_1_0_2 = = 
 
# Sensor Kinematics 


    ROcp0_47 = ROcp0_45*C7+ROcp0_76*S7
    ROcp0_57 = ROcp0_55*C7+ROcp0_86*S7
    ROcp0_67 = ROcp0_96*S7+S5*C7
    ROcp0_77 = -(ROcp0_45*S7-ROcp0_76*C7)
    ROcp0_87 = -(ROcp0_55*S7-ROcp0_86*C7)
    ROcp0_97 = ROcp0_96*C7-S5*S7
    ROcp0_18 = ROcp0_16*C8+ROcp0_47*S8
    ROcp0_28 = ROcp0_26*C8+ROcp0_57*S8
    ROcp0_38 = ROcp0_36*C8+ROcp0_67*S8
    ROcp0_48 = -(ROcp0_16*S8-ROcp0_47*C8)
    ROcp0_58 = -(ROcp0_26*S8-ROcp0_57*C8)
    ROcp0_68 = -(ROcp0_36*S8-ROcp0_67*C8)
    RLcp0_17 = ROcp0_16*s.dpt[1,1]+ROcp0_45*s.dpt[2,1]+ROcp0_76*s.dpt[3,1]
    RLcp0_27 = ROcp0_26*s.dpt[1,1]+ROcp0_55*s.dpt[2,1]+ROcp0_86*s.dpt[3,1]
    RLcp0_37 = ROcp0_36*s.dpt[1,1]+ROcp0_96*s.dpt[3,1]+s.dpt[2,1]*S5
    OMcp0_17 = OMcp0_16+ROcp0_16*qd[7]
    OMcp0_27 = OMcp0_26+ROcp0_26*qd[7]
    OMcp0_37 = OMcp0_36+ROcp0_36*qd[7]
    ORcp0_17 = OMcp0_26*RLcp0_37-OMcp0_36*RLcp0_27
    ORcp0_27 = -(OMcp0_16*RLcp0_37-OMcp0_36*RLcp0_17)
    ORcp0_37 = OMcp0_16*RLcp0_27-OMcp0_26*RLcp0_17
    OPcp0_17 = OPcp0_16+ROcp0_16*qdd[7]+qd[7]*(OMcp0_26*ROcp0_36-OMcp0_36*ROcp0_26)
    OPcp0_27 = OPcp0_26+ROcp0_26*qdd[7]-qd[7]*(OMcp0_16*ROcp0_36-OMcp0_36*ROcp0_16)
    OPcp0_37 = OPcp0_36+ROcp0_36*qdd[7]+qd[7]*(OMcp0_16*ROcp0_26-OMcp0_26*ROcp0_16)
    RLcp0_18 = ROcp0_47*s.dpt[2,14]
    RLcp0_28 = ROcp0_57*s.dpt[2,14]
    RLcp0_38 = ROcp0_67*s.dpt[2,14]
    POcp0_18 = RLcp0_17+RLcp0_18+q[1]
    POcp0_28 = RLcp0_27+RLcp0_28+q[2]
    POcp0_38 = RLcp0_37+RLcp0_38+q[3]
    JTcp0_18_4 = -(RLcp0_27+RLcp0_28)
    JTcp0_28_4 = RLcp0_17+RLcp0_18
    JTcp0_18_5 = S4*(RLcp0_37+RLcp0_38)
    JTcp0_28_5 = -C4*(RLcp0_37+RLcp0_38)
    JTcp0_38_5 = C4*(RLcp0_27+RLcp0_28)-S4*(RLcp0_17+RLcp0_18)
    JTcp0_18_6 = ROcp0_55*(RLcp0_37+RLcp0_38)-S5*(RLcp0_27+RLcp0_28)
    JTcp0_28_6 = -(ROcp0_45*(RLcp0_37+RLcp0_38)-S5*(RLcp0_17+RLcp0_18))
    JTcp0_38_6 = ROcp0_45*(RLcp0_27+RLcp0_28)-ROcp0_55*(RLcp0_17+RLcp0_18)
    JTcp0_18_7 = -(RLcp0_28*ROcp0_36-RLcp0_38*ROcp0_26)
    JTcp0_28_7 = RLcp0_18*ROcp0_36-RLcp0_38*ROcp0_16
    JTcp0_38_7 = -(RLcp0_18*ROcp0_26-RLcp0_28*ROcp0_16)
    OMcp0_18 = OMcp0_17+ROcp0_77*qd[8]
    OMcp0_28 = OMcp0_27+ROcp0_87*qd[8]
    OMcp0_38 = OMcp0_37+ROcp0_97*qd[8]
    ORcp0_18 = OMcp0_27*RLcp0_38-OMcp0_37*RLcp0_28
    ORcp0_28 = -(OMcp0_17*RLcp0_38-OMcp0_37*RLcp0_18)
    ORcp0_38 = OMcp0_17*RLcp0_28-OMcp0_27*RLcp0_18
    VIcp0_18 = ORcp0_17+ORcp0_18+qd[1]
    VIcp0_28 = ORcp0_27+ORcp0_28+qd[2]
    VIcp0_38 = ORcp0_37+ORcp0_38+qd[3]
    OPcp0_18 = OPcp0_17+ROcp0_77*qdd[8]+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)
    OPcp0_28 = OPcp0_27+ROcp0_87*qdd[8]-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)
    OPcp0_38 = OPcp0_37+ROcp0_97*qdd[8]+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)
    ACcp0_18 = qdd[1]+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_36*ORcp0_27-OMcp0_37*ORcp0_28+OPcp0_26*RLcp0_37+OPcp0_27*\
   RLcp0_38-OPcp0_36*RLcp0_27-OPcp0_37*RLcp0_28
    ACcp0_28 = qdd[2]-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_36*ORcp0_17+OMcp0_37*ORcp0_18-OPcp0_16*RLcp0_37-OPcp0_17*\
   RLcp0_38+OPcp0_36*RLcp0_17+OPcp0_37*RLcp0_18
    ACcp0_38 = qdd[3]+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_26*ORcp0_17-OMcp0_27*ORcp0_18+OPcp0_16*RLcp0_27+OPcp0_17*\
   RLcp0_28-OPcp0_26*RLcp0_17-OPcp0_27*RLcp0_18

# = = Block_1_0_0_1_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp0_18
    sens.P[2] = POcp0_28
    sens.P[3] = POcp0_38
    sens.R[1,1] = ROcp0_18
    sens.R[1,2] = ROcp0_28
    sens.R[1,3] = ROcp0_38
    sens.R[2,1] = ROcp0_48
    sens.R[2,2] = ROcp0_58
    sens.R[2,3] = ROcp0_68
    sens.R[3,1] = ROcp0_77
    sens.R[3,2] = ROcp0_87
    sens.R[3,3] = ROcp0_97
    sens.V[1] = VIcp0_18
    sens.V[2] = VIcp0_28
    sens.V[3] = VIcp0_38
    sens.OM[1] = OMcp0_18
    sens.OM[2] = OMcp0_28
    sens.OM[3] = OMcp0_38
    sens.J[1,1] = (1.0)
    sens.J[1,4] = JTcp0_18_4
    sens.J[1,5] = JTcp0_18_5
    sens.J[1,6] = JTcp0_18_6
    sens.J[1,7] = JTcp0_18_7
    sens.J[2,2] = (1.0)
    sens.J[2,4] = JTcp0_28_4
    sens.J[2,5] = JTcp0_28_5
    sens.J[2,6] = JTcp0_28_6
    sens.J[2,7] = JTcp0_28_7
    sens.J[3,3] = (1.0)
    sens.J[3,5] = JTcp0_38_5
    sens.J[3,6] = JTcp0_38_6
    sens.J[3,7] = JTcp0_38_7
    sens.J[4,5] = C4
    sens.J[4,6] = ROcp0_45
    sens.J[4,7] = ROcp0_16
    sens.J[4,8] = ROcp0_77
    sens.J[5,5] = S4
    sens.J[5,6] = ROcp0_55
    sens.J[5,7] = ROcp0_26
    sens.J[5,8] = ROcp0_87
    sens.J[6,4] = (1.0)
    sens.J[6,6] = S5
    sens.J[6,7] = ROcp0_36
    sens.J[6,8] = ROcp0_97
    sens.A[1] = ACcp0_18
    sens.A[2] = ACcp0_28
    sens.A[3] = ACcp0_38
    sens.OMP[1] = OPcp0_18
    sens.OMP[2] = OPcp0_28
    sens.OMP[3] = OPcp0_38
 
# 
  elif(isens==2): 


# = = Block_1_0_0_2_0_1 = = 
 
# Sensor Kinematics 


    ROcp1_45 = -S4*C5
    ROcp1_55 = C4*C5
    ROcp1_75 = S4*S5
    ROcp1_85 = -C4*S5
    ROcp1_16 = -(ROcp1_75*S6-C4*C6)
    ROcp1_26 = -(ROcp1_85*S6-S4*C6)
    ROcp1_36 = -C5*S6
    ROcp1_76 = ROcp1_75*C6+C4*S6
    ROcp1_86 = ROcp1_85*C6+S4*S6
    ROcp1_96 = C5*C6
    OMcp1_15 = qd[5]*C4
    OMcp1_25 = qd[5]*S4
    OMcp1_16 = OMcp1_15+ROcp1_45*qd[6]
    OMcp1_26 = OMcp1_25+ROcp1_55*qd[6]
    OMcp1_36 = qd[4]+qd[6]*S5
    OPcp1_16 = ROcp1_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp1_25*S5-ROcp1_55*qd[4])
    OPcp1_26 = ROcp1_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp1_15*S5-ROcp1_45*qd[4])
    OPcp1_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_2_0_3 = = 
 
# Sensor Kinematics 


    ROcp1_410 = ROcp1_45*C10+ROcp1_76*S10
    ROcp1_510 = ROcp1_55*C10+ROcp1_86*S10
    ROcp1_610 = ROcp1_96*S10+C10*S5
    ROcp1_710 = -(ROcp1_45*S10-ROcp1_76*C10)
    ROcp1_810 = -(ROcp1_55*S10-ROcp1_86*C10)
    ROcp1_910 = ROcp1_96*C10-S10*S5
    ROcp1_111 = ROcp1_16*C11+ROcp1_410*S11
    ROcp1_211 = ROcp1_26*C11+ROcp1_510*S11
    ROcp1_311 = ROcp1_36*C11+ROcp1_610*S11
    ROcp1_411 = -(ROcp1_16*S11-ROcp1_410*C11)
    ROcp1_511 = -(ROcp1_26*S11-ROcp1_510*C11)
    ROcp1_611 = -(ROcp1_36*S11-ROcp1_610*C11)
    RLcp1_110 = ROcp1_16*s.dpt[1,4]+ROcp1_45*s.dpt[2,4]+ROcp1_76*s.dpt[3,4]
    RLcp1_210 = ROcp1_26*s.dpt[1,4]+ROcp1_55*s.dpt[2,4]+ROcp1_86*s.dpt[3,4]
    RLcp1_310 = ROcp1_36*s.dpt[1,4]+ROcp1_96*s.dpt[3,4]+s.dpt[2,4]*S5
    OMcp1_110 = OMcp1_16+ROcp1_16*qd[10]
    OMcp1_210 = OMcp1_26+ROcp1_26*qd[10]
    OMcp1_310 = OMcp1_36+ROcp1_36*qd[10]
    ORcp1_110 = OMcp1_26*RLcp1_310-OMcp1_36*RLcp1_210
    ORcp1_210 = -(OMcp1_16*RLcp1_310-OMcp1_36*RLcp1_110)
    ORcp1_310 = OMcp1_16*RLcp1_210-OMcp1_26*RLcp1_110
    OPcp1_110 = OPcp1_16+ROcp1_16*qdd[10]+qd[10]*(OMcp1_26*ROcp1_36-OMcp1_36*ROcp1_26)
    OPcp1_210 = OPcp1_26+ROcp1_26*qdd[10]-qd[10]*(OMcp1_16*ROcp1_36-OMcp1_36*ROcp1_16)
    OPcp1_310 = OPcp1_36+ROcp1_36*qdd[10]+qd[10]*(OMcp1_16*ROcp1_26-OMcp1_26*ROcp1_16)
    RLcp1_111 = ROcp1_410*s.dpt[2,19]
    RLcp1_211 = ROcp1_510*s.dpt[2,19]
    RLcp1_311 = ROcp1_610*s.dpt[2,19]
    POcp1_111 = RLcp1_110+RLcp1_111+q[1]
    POcp1_211 = RLcp1_210+RLcp1_211+q[2]
    POcp1_311 = RLcp1_310+RLcp1_311+q[3]
    JTcp1_111_4 = -(RLcp1_210+RLcp1_211)
    JTcp1_211_4 = RLcp1_110+RLcp1_111
    JTcp1_111_5 = S4*(RLcp1_310+RLcp1_311)
    JTcp1_211_5 = -C4*(RLcp1_310+RLcp1_311)
    JTcp1_311_5 = C4*(RLcp1_210+RLcp1_211)-S4*(RLcp1_110+RLcp1_111)
    JTcp1_111_6 = ROcp1_55*(RLcp1_310+RLcp1_311)-S5*(RLcp1_210+RLcp1_211)
    JTcp1_211_6 = -(ROcp1_45*(RLcp1_310+RLcp1_311)-S5*(RLcp1_110+RLcp1_111))
    JTcp1_311_6 = ROcp1_45*(RLcp1_210+RLcp1_211)-ROcp1_55*(RLcp1_110+RLcp1_111)
    JTcp1_111_7 = -(RLcp1_211*ROcp1_36-RLcp1_311*ROcp1_26)
    JTcp1_211_7 = RLcp1_111*ROcp1_36-RLcp1_311*ROcp1_16
    JTcp1_311_7 = -(RLcp1_111*ROcp1_26-RLcp1_211*ROcp1_16)
    OMcp1_111 = OMcp1_110+ROcp1_710*qd[11]
    OMcp1_211 = OMcp1_210+ROcp1_810*qd[11]
    OMcp1_311 = OMcp1_310+ROcp1_910*qd[11]
    ORcp1_111 = OMcp1_210*RLcp1_311-OMcp1_310*RLcp1_211
    ORcp1_211 = -(OMcp1_110*RLcp1_311-OMcp1_310*RLcp1_111)
    ORcp1_311 = OMcp1_110*RLcp1_211-OMcp1_210*RLcp1_111
    VIcp1_111 = ORcp1_110+ORcp1_111+qd[1]
    VIcp1_211 = ORcp1_210+ORcp1_211+qd[2]
    VIcp1_311 = ORcp1_310+ORcp1_311+qd[3]
    OPcp1_111 = OPcp1_110+ROcp1_710*qdd[11]+qd[11]*(OMcp1_210*ROcp1_910-OMcp1_310*ROcp1_810)
    OPcp1_211 = OPcp1_210+ROcp1_810*qdd[11]-qd[11]*(OMcp1_110*ROcp1_910-OMcp1_310*ROcp1_710)
    OPcp1_311 = OPcp1_310+ROcp1_910*qdd[11]+qd[11]*(OMcp1_110*ROcp1_810-OMcp1_210*ROcp1_710)
    ACcp1_111 = qdd[1]+OMcp1_210*ORcp1_311+OMcp1_26*ORcp1_310-OMcp1_310*ORcp1_211-OMcp1_36*ORcp1_210+OPcp1_210*RLcp1_311+\
   OPcp1_26*RLcp1_310-OPcp1_310*RLcp1_211-OPcp1_36*RLcp1_210
    ACcp1_211 = qdd[2]-OMcp1_110*ORcp1_311-OMcp1_16*ORcp1_310+OMcp1_310*ORcp1_111+OMcp1_36*ORcp1_110-OPcp1_110*RLcp1_311-\
   OPcp1_16*RLcp1_310+OPcp1_310*RLcp1_111+OPcp1_36*RLcp1_110
    ACcp1_311 = qdd[3]+OMcp1_110*ORcp1_211+OMcp1_16*ORcp1_210-OMcp1_210*ORcp1_111-OMcp1_26*ORcp1_110+OPcp1_110*RLcp1_211+\
   OPcp1_16*RLcp1_210-OPcp1_210*RLcp1_111-OPcp1_26*RLcp1_110

# = = Block_1_0_0_2_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp1_111
    sens.P[2] = POcp1_211
    sens.P[3] = POcp1_311
    sens.R[1,1] = ROcp1_111
    sens.R[1,2] = ROcp1_211
    sens.R[1,3] = ROcp1_311
    sens.R[2,1] = ROcp1_411
    sens.R[2,2] = ROcp1_511
    sens.R[2,3] = ROcp1_611
    sens.R[3,1] = ROcp1_710
    sens.R[3,2] = ROcp1_810
    sens.R[3,3] = ROcp1_910
    sens.V[1] = VIcp1_111
    sens.V[2] = VIcp1_211
    sens.V[3] = VIcp1_311
    sens.OM[1] = OMcp1_111
    sens.OM[2] = OMcp1_211
    sens.OM[3] = OMcp1_311
    sens.J[1,1] = (1.0)
    sens.J[1,4] = JTcp1_111_4
    sens.J[1,5] = JTcp1_111_5
    sens.J[1,6] = JTcp1_111_6
    sens.J[1,10] = JTcp1_111_7
    sens.J[2,2] = (1.0)
    sens.J[2,4] = JTcp1_211_4
    sens.J[2,5] = JTcp1_211_5
    sens.J[2,6] = JTcp1_211_6
    sens.J[2,10] = JTcp1_211_7
    sens.J[3,3] = (1.0)
    sens.J[3,5] = JTcp1_311_5
    sens.J[3,6] = JTcp1_311_6
    sens.J[3,10] = JTcp1_311_7
    sens.J[4,5] = C4
    sens.J[4,6] = ROcp1_45
    sens.J[4,10] = ROcp1_16
    sens.J[4,11] = ROcp1_710
    sens.J[5,5] = S4
    sens.J[5,6] = ROcp1_55
    sens.J[5,10] = ROcp1_26
    sens.J[5,11] = ROcp1_810
    sens.J[6,4] = (1.0)
    sens.J[6,6] = S5
    sens.J[6,10] = ROcp1_36
    sens.J[6,11] = ROcp1_910
    sens.A[1] = ACcp1_111
    sens.A[2] = ACcp1_211
    sens.A[3] = ACcp1_311
    sens.OMP[1] = OPcp1_111
    sens.OMP[2] = OPcp1_211
    sens.OMP[3] = OPcp1_311
 
# 
  elif(isens==3): 


# = = Block_1_0_0_3_0_1 = = 
 
# Sensor Kinematics 


    ROcp2_45 = -S4*C5
    ROcp2_55 = C4*C5
    ROcp2_75 = S4*S5
    ROcp2_85 = -C4*S5
    ROcp2_16 = -(ROcp2_75*S6-C4*C6)
    ROcp2_26 = -(ROcp2_85*S6-S4*C6)
    ROcp2_36 = -C5*S6
    ROcp2_76 = ROcp2_75*C6+C4*S6
    ROcp2_86 = ROcp2_85*C6+S4*S6
    ROcp2_96 = C5*C6
    OMcp2_15 = qd[5]*C4
    OMcp2_25 = qd[5]*S4
    OMcp2_16 = OMcp2_15+ROcp2_45*qd[6]
    OMcp2_26 = OMcp2_25+ROcp2_55*qd[6]
    OMcp2_36 = qd[4]+qd[6]*S5
    OPcp2_16 = ROcp2_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp2_25*S5-ROcp2_55*qd[4])
    OPcp2_26 = ROcp2_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp2_15*S5-ROcp2_45*qd[4])
    OPcp2_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_3_0_4 = = 
 
# Sensor Kinematics 


    ROcp2_413 = ROcp2_45*C13+ROcp2_76*S13
    ROcp2_513 = ROcp2_55*C13+ROcp2_86*S13
    ROcp2_613 = ROcp2_96*S13+C13*S5
    ROcp2_713 = -(ROcp2_45*S13-ROcp2_76*C13)
    ROcp2_813 = -(ROcp2_55*S13-ROcp2_86*C13)
    ROcp2_913 = ROcp2_96*C13-S13*S5
    ROcp2_414 = ROcp2_413*C14+ROcp2_713*S14
    ROcp2_514 = ROcp2_513*C14+ROcp2_813*S14
    ROcp2_614 = ROcp2_613*C14+ROcp2_913*S14
    ROcp2_714 = -(ROcp2_413*S14-ROcp2_713*C14)
    ROcp2_814 = -(ROcp2_513*S14-ROcp2_813*C14)
    ROcp2_914 = -(ROcp2_613*S14-ROcp2_913*C14)
    RLcp2_113 = ROcp2_16*s.dpt[1,9]+ROcp2_45*s.dpt[2,9]+ROcp2_76*s.dpt[3,9]
    RLcp2_213 = ROcp2_26*s.dpt[1,9]+ROcp2_55*s.dpt[2,9]+ROcp2_86*s.dpt[3,9]
    RLcp2_313 = ROcp2_36*s.dpt[1,9]+ROcp2_96*s.dpt[3,9]+s.dpt[2,9]*S5
    OMcp2_113 = OMcp2_16+ROcp2_16*qd[13]
    OMcp2_213 = OMcp2_26+ROcp2_26*qd[13]
    OMcp2_313 = OMcp2_36+ROcp2_36*qd[13]
    ORcp2_113 = OMcp2_26*RLcp2_313-OMcp2_36*RLcp2_213
    ORcp2_213 = -(OMcp2_16*RLcp2_313-OMcp2_36*RLcp2_113)
    ORcp2_313 = OMcp2_16*RLcp2_213-OMcp2_26*RLcp2_113
    OPcp2_113 = OPcp2_16+ROcp2_16*qdd[13]+qd[13]*(OMcp2_26*ROcp2_36-OMcp2_36*ROcp2_26)
    OPcp2_213 = OPcp2_26+ROcp2_26*qdd[13]-qd[13]*(OMcp2_16*ROcp2_36-OMcp2_36*ROcp2_16)
    OPcp2_313 = OPcp2_36+ROcp2_36*qdd[13]+qd[13]*(OMcp2_16*ROcp2_26-OMcp2_26*ROcp2_16)
    RLcp2_114 = ROcp2_413*s.dpt[2,24]
    RLcp2_214 = ROcp2_513*s.dpt[2,24]
    RLcp2_314 = ROcp2_613*s.dpt[2,24]
    OMcp2_114 = OMcp2_113+ROcp2_16*qd[14]
    OMcp2_214 = OMcp2_213+ROcp2_26*qd[14]
    OMcp2_314 = OMcp2_313+ROcp2_36*qd[14]
    ORcp2_114 = OMcp2_213*RLcp2_314-OMcp2_313*RLcp2_214
    ORcp2_214 = -(OMcp2_113*RLcp2_314-OMcp2_313*RLcp2_114)
    ORcp2_314 = OMcp2_113*RLcp2_214-OMcp2_213*RLcp2_114
    OPcp2_114 = OPcp2_113+ROcp2_16*qdd[14]+qd[14]*(OMcp2_213*ROcp2_36-OMcp2_313*ROcp2_26)
    OPcp2_214 = OPcp2_213+ROcp2_26*qdd[14]-qd[14]*(OMcp2_113*ROcp2_36-OMcp2_313*ROcp2_16)
    OPcp2_314 = OPcp2_313+ROcp2_36*qdd[14]+qd[14]*(OMcp2_113*ROcp2_26-OMcp2_213*ROcp2_16)
    RLcp2_137 = ROcp2_714*s.dpt[3,27]
    RLcp2_237 = ROcp2_814*s.dpt[3,27]
    RLcp2_337 = ROcp2_914*s.dpt[3,27]
    POcp2_137 = RLcp2_113+RLcp2_114+RLcp2_137+q[1]
    POcp2_237 = RLcp2_213+RLcp2_214+RLcp2_237+q[2]
    POcp2_337 = RLcp2_313+RLcp2_314+RLcp2_337+q[3]
    JTcp2_137_4 = -(RLcp2_213+RLcp2_214+RLcp2_237)
    JTcp2_237_4 = RLcp2_113+RLcp2_114+RLcp2_137
    JTcp2_137_5 = S4*(RLcp2_313+RLcp2_314+RLcp2_337)
    JTcp2_237_5 = -C4*(RLcp2_313+RLcp2_314+RLcp2_337)
    JTcp2_337_5 = C4*(RLcp2_213+RLcp2_214)-S4*(RLcp2_113+RLcp2_114)-RLcp2_137*S4+RLcp2_237*C4
    JTcp2_137_6 = ROcp2_55*(RLcp2_313+RLcp2_314)-S5*(RLcp2_213+RLcp2_214)-RLcp2_237*S5+RLcp2_337*ROcp2_55
    JTcp2_237_6 = RLcp2_137*S5-RLcp2_337*ROcp2_45-ROcp2_45*(RLcp2_313+RLcp2_314)+S5*(RLcp2_113+RLcp2_114)
    JTcp2_337_6 = ROcp2_45*(RLcp2_213+RLcp2_214)-ROcp2_55*(RLcp2_113+RLcp2_114)-RLcp2_137*ROcp2_55+RLcp2_237*ROcp2_45
    JTcp2_137_7 = ROcp2_26*(RLcp2_314+RLcp2_337)-ROcp2_36*(RLcp2_214+RLcp2_237)
    JTcp2_237_7 = -(ROcp2_16*(RLcp2_314+RLcp2_337)-ROcp2_36*(RLcp2_114+RLcp2_137))
    JTcp2_337_7 = ROcp2_16*(RLcp2_214+RLcp2_237)-ROcp2_26*(RLcp2_114+RLcp2_137)
    JTcp2_137_8 = -(RLcp2_237*ROcp2_36-RLcp2_337*ROcp2_26)
    JTcp2_237_8 = RLcp2_137*ROcp2_36-RLcp2_337*ROcp2_16
    JTcp2_337_8 = -(RLcp2_137*ROcp2_26-RLcp2_237*ROcp2_16)
    ORcp2_137 = OMcp2_214*RLcp2_337-OMcp2_314*RLcp2_237
    ORcp2_237 = -(OMcp2_114*RLcp2_337-OMcp2_314*RLcp2_137)
    ORcp2_337 = OMcp2_114*RLcp2_237-OMcp2_214*RLcp2_137
    VIcp2_137 = ORcp2_113+ORcp2_114+ORcp2_137+qd[1]
    VIcp2_237 = ORcp2_213+ORcp2_214+ORcp2_237+qd[2]
    VIcp2_337 = ORcp2_313+ORcp2_314+ORcp2_337+qd[3]
    ACcp2_137 = qdd[1]+OMcp2_213*ORcp2_314+OMcp2_214*ORcp2_337+OMcp2_26*ORcp2_313-OMcp2_313*ORcp2_214-OMcp2_314*ORcp2_237-\
   OMcp2_36*ORcp2_213+OPcp2_213*RLcp2_314+OPcp2_214*RLcp2_337+OPcp2_26*RLcp2_313-OPcp2_313*RLcp2_214-OPcp2_314*RLcp2_237-\
   OPcp2_36*RLcp2_213
    ACcp2_237 = qdd[2]-OMcp2_113*ORcp2_314-OMcp2_114*ORcp2_337-OMcp2_16*ORcp2_313+OMcp2_313*ORcp2_114+OMcp2_314*ORcp2_137+\
   OMcp2_36*ORcp2_113-OPcp2_113*RLcp2_314-OPcp2_114*RLcp2_337-OPcp2_16*RLcp2_313+OPcp2_313*RLcp2_114+OPcp2_314*RLcp2_137+\
   OPcp2_36*RLcp2_113
    ACcp2_337 = qdd[3]+OMcp2_113*ORcp2_214+OMcp2_114*ORcp2_237+OMcp2_16*ORcp2_213-OMcp2_213*ORcp2_114-OMcp2_214*ORcp2_137-\
   OMcp2_26*ORcp2_113+OPcp2_113*RLcp2_214+OPcp2_114*RLcp2_237+OPcp2_16*RLcp2_213-OPcp2_213*RLcp2_114-OPcp2_214*RLcp2_137-\
   OPcp2_26*RLcp2_113

# = = Block_1_0_0_3_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp2_137
    sens.P[2] = POcp2_237
    sens.P[3] = POcp2_337
    sens.R[1,1] = ROcp2_16
    sens.R[1,2] = ROcp2_26
    sens.R[1,3] = ROcp2_36
    sens.R[2,1] = ROcp2_414
    sens.R[2,2] = ROcp2_514
    sens.R[2,3] = ROcp2_614
    sens.R[3,1] = ROcp2_714
    sens.R[3,2] = ROcp2_814
    sens.R[3,3] = ROcp2_914
    sens.V[1] = VIcp2_137
    sens.V[2] = VIcp2_237
    sens.V[3] = VIcp2_337
    sens.OM[1] = OMcp2_114
    sens.OM[2] = OMcp2_214
    sens.OM[3] = OMcp2_314
    sens.J[1,1] = (1.0)
    sens.J[1,4] = JTcp2_137_4
    sens.J[1,5] = JTcp2_137_5
    sens.J[1,6] = JTcp2_137_6
    sens.J[1,13] = JTcp2_137_7
    sens.J[1,14] = JTcp2_137_8
    sens.J[2,2] = (1.0)
    sens.J[2,4] = JTcp2_237_4
    sens.J[2,5] = JTcp2_237_5
    sens.J[2,6] = JTcp2_237_6
    sens.J[2,13] = JTcp2_237_7
    sens.J[2,14] = JTcp2_237_8
    sens.J[3,3] = (1.0)
    sens.J[3,5] = JTcp2_337_5
    sens.J[3,6] = JTcp2_337_6
    sens.J[3,13] = JTcp2_337_7
    sens.J[3,14] = JTcp2_337_8
    sens.J[4,5] = C4
    sens.J[4,6] = ROcp2_45
    sens.J[4,13] = ROcp2_16
    sens.J[4,14] = ROcp2_16
    sens.J[5,5] = S4
    sens.J[5,6] = ROcp2_55
    sens.J[5,13] = ROcp2_26
    sens.J[5,14] = ROcp2_26
    sens.J[6,4] = (1.0)
    sens.J[6,6] = S5
    sens.J[6,13] = ROcp2_36
    sens.J[6,14] = ROcp2_36
    sens.A[1] = ACcp2_137
    sens.A[2] = ACcp2_237
    sens.A[3] = ACcp2_337
    sens.OMP[1] = OPcp2_114
    sens.OMP[2] = OPcp2_214
    sens.OMP[3] = OPcp2_314
 
# 
  elif(isens==4): 


# = = Block_1_0_0_4_0_1 = = 
 
# Sensor Kinematics 


    ROcp3_45 = -S4*C5
    ROcp3_55 = C4*C5
    ROcp3_75 = S4*S5
    ROcp3_85 = -C4*S5
    ROcp3_16 = -(ROcp3_75*S6-C4*C6)
    ROcp3_26 = -(ROcp3_85*S6-S4*C6)
    ROcp3_36 = -C5*S6
    ROcp3_76 = ROcp3_75*C6+C4*S6
    ROcp3_86 = ROcp3_85*C6+S4*S6
    ROcp3_96 = C5*C6
    OMcp3_15 = qd[5]*C4
    OMcp3_25 = qd[5]*S4
    OMcp3_16 = OMcp3_15+ROcp3_45*qd[6]
    OMcp3_26 = OMcp3_25+ROcp3_55*qd[6]
    OMcp3_36 = qd[4]+qd[6]*S5
    OPcp3_16 = ROcp3_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp3_25*S5-ROcp3_55*qd[4])
    OPcp3_26 = ROcp3_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp3_15*S5-ROcp3_45*qd[4])
    OPcp3_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_4_0_5 = = 
 
# Sensor Kinematics 


    ROcp3_416 = ROcp3_45*C16+ROcp3_76*S16
    ROcp3_516 = ROcp3_55*C16+ROcp3_86*S16
    ROcp3_616 = ROcp3_96*S16+C16*S5
    ROcp3_716 = -(ROcp3_45*S16-ROcp3_76*C16)
    ROcp3_816 = -(ROcp3_55*S16-ROcp3_86*C16)
    ROcp3_916 = ROcp3_96*C16-S16*S5
    ROcp3_417 = ROcp3_416*C17+ROcp3_716*S17
    ROcp3_517 = ROcp3_516*C17+ROcp3_816*S17
    ROcp3_617 = ROcp3_616*C17+ROcp3_916*S17
    ROcp3_717 = -(ROcp3_416*S17-ROcp3_716*C17)
    ROcp3_817 = -(ROcp3_516*S17-ROcp3_816*C17)
    ROcp3_917 = -(ROcp3_616*S17-ROcp3_916*C17)
    RLcp3_116 = ROcp3_16*s.dpt[1,11]+ROcp3_45*s.dpt[2,11]+ROcp3_76*s.dpt[3,11]
    RLcp3_216 = ROcp3_26*s.dpt[1,11]+ROcp3_55*s.dpt[2,11]+ROcp3_86*s.dpt[3,11]
    RLcp3_316 = ROcp3_36*s.dpt[1,11]+ROcp3_96*s.dpt[3,11]+s.dpt[2,11]*S5
    OMcp3_116 = OMcp3_16+ROcp3_16*qd[16]
    OMcp3_216 = OMcp3_26+ROcp3_26*qd[16]
    OMcp3_316 = OMcp3_36+ROcp3_36*qd[16]
    ORcp3_116 = OMcp3_26*RLcp3_316-OMcp3_36*RLcp3_216
    ORcp3_216 = -(OMcp3_16*RLcp3_316-OMcp3_36*RLcp3_116)
    ORcp3_316 = OMcp3_16*RLcp3_216-OMcp3_26*RLcp3_116
    OPcp3_116 = OPcp3_16+ROcp3_16*qdd[16]+qd[16]*(OMcp3_26*ROcp3_36-OMcp3_36*ROcp3_26)
    OPcp3_216 = OPcp3_26+ROcp3_26*qdd[16]-qd[16]*(OMcp3_16*ROcp3_36-OMcp3_36*ROcp3_16)
    OPcp3_316 = OPcp3_36+ROcp3_36*qdd[16]+qd[16]*(OMcp3_16*ROcp3_26-OMcp3_26*ROcp3_16)
    RLcp3_117 = ROcp3_416*s.dpt[2,30]
    RLcp3_217 = ROcp3_516*s.dpt[2,30]
    RLcp3_317 = ROcp3_616*s.dpt[2,30]
    OMcp3_117 = OMcp3_116+ROcp3_16*qd[17]
    OMcp3_217 = OMcp3_216+ROcp3_26*qd[17]
    OMcp3_317 = OMcp3_316+ROcp3_36*qd[17]
    ORcp3_117 = OMcp3_216*RLcp3_317-OMcp3_316*RLcp3_217
    ORcp3_217 = -(OMcp3_116*RLcp3_317-OMcp3_316*RLcp3_117)
    ORcp3_317 = OMcp3_116*RLcp3_217-OMcp3_216*RLcp3_117
    OPcp3_117 = OPcp3_116+ROcp3_16*qdd[17]+qd[17]*(OMcp3_216*ROcp3_36-OMcp3_316*ROcp3_26)
    OPcp3_217 = OPcp3_216+ROcp3_26*qdd[17]-qd[17]*(OMcp3_116*ROcp3_36-OMcp3_316*ROcp3_16)
    OPcp3_317 = OPcp3_316+ROcp3_36*qdd[17]+qd[17]*(OMcp3_116*ROcp3_26-OMcp3_216*ROcp3_16)
    RLcp3_138 = ROcp3_717*s.dpt[3,31]
    RLcp3_238 = ROcp3_817*s.dpt[3,31]
    RLcp3_338 = ROcp3_917*s.dpt[3,31]
    POcp3_138 = RLcp3_116+RLcp3_117+RLcp3_138+q[1]
    POcp3_238 = RLcp3_216+RLcp3_217+RLcp3_238+q[2]
    POcp3_338 = RLcp3_316+RLcp3_317+RLcp3_338+q[3]
    JTcp3_138_4 = -(RLcp3_216+RLcp3_217+RLcp3_238)
    JTcp3_238_4 = RLcp3_116+RLcp3_117+RLcp3_138
    JTcp3_138_5 = S4*(RLcp3_316+RLcp3_317+RLcp3_338)
    JTcp3_238_5 = -C4*(RLcp3_316+RLcp3_317+RLcp3_338)
    JTcp3_338_5 = C4*(RLcp3_216+RLcp3_217)-S4*(RLcp3_116+RLcp3_117)-RLcp3_138*S4+RLcp3_238*C4
    JTcp3_138_6 = ROcp3_55*(RLcp3_316+RLcp3_317)-S5*(RLcp3_216+RLcp3_217)-RLcp3_238*S5+RLcp3_338*ROcp3_55
    JTcp3_238_6 = RLcp3_138*S5-RLcp3_338*ROcp3_45-ROcp3_45*(RLcp3_316+RLcp3_317)+S5*(RLcp3_116+RLcp3_117)
    JTcp3_338_6 = ROcp3_45*(RLcp3_216+RLcp3_217)-ROcp3_55*(RLcp3_116+RLcp3_117)-RLcp3_138*ROcp3_55+RLcp3_238*ROcp3_45
    JTcp3_138_7 = ROcp3_26*(RLcp3_317+RLcp3_338)-ROcp3_36*(RLcp3_217+RLcp3_238)
    JTcp3_238_7 = -(ROcp3_16*(RLcp3_317+RLcp3_338)-ROcp3_36*(RLcp3_117+RLcp3_138))
    JTcp3_338_7 = ROcp3_16*(RLcp3_217+RLcp3_238)-ROcp3_26*(RLcp3_117+RLcp3_138)
    JTcp3_138_8 = -(RLcp3_238*ROcp3_36-RLcp3_338*ROcp3_26)
    JTcp3_238_8 = RLcp3_138*ROcp3_36-RLcp3_338*ROcp3_16
    JTcp3_338_8 = -(RLcp3_138*ROcp3_26-RLcp3_238*ROcp3_16)
    ORcp3_138 = OMcp3_217*RLcp3_338-OMcp3_317*RLcp3_238
    ORcp3_238 = -(OMcp3_117*RLcp3_338-OMcp3_317*RLcp3_138)
    ORcp3_338 = OMcp3_117*RLcp3_238-OMcp3_217*RLcp3_138
    VIcp3_138 = ORcp3_116+ORcp3_117+ORcp3_138+qd[1]
    VIcp3_238 = ORcp3_216+ORcp3_217+ORcp3_238+qd[2]
    VIcp3_338 = ORcp3_316+ORcp3_317+ORcp3_338+qd[3]
    ACcp3_138 = qdd[1]+OMcp3_216*ORcp3_317+OMcp3_217*ORcp3_338+OMcp3_26*ORcp3_316-OMcp3_316*ORcp3_217-OMcp3_317*ORcp3_238-\
   OMcp3_36*ORcp3_216+OPcp3_216*RLcp3_317+OPcp3_217*RLcp3_338+OPcp3_26*RLcp3_316-OPcp3_316*RLcp3_217-OPcp3_317*RLcp3_238-\
   OPcp3_36*RLcp3_216
    ACcp3_238 = qdd[2]-OMcp3_116*ORcp3_317-OMcp3_117*ORcp3_338-OMcp3_16*ORcp3_316+OMcp3_316*ORcp3_117+OMcp3_317*ORcp3_138+\
   OMcp3_36*ORcp3_116-OPcp3_116*RLcp3_317-OPcp3_117*RLcp3_338-OPcp3_16*RLcp3_316+OPcp3_316*RLcp3_117+OPcp3_317*RLcp3_138+\
   OPcp3_36*RLcp3_116
    ACcp3_338 = qdd[3]+OMcp3_116*ORcp3_217+OMcp3_117*ORcp3_238+OMcp3_16*ORcp3_216-OMcp3_216*ORcp3_117-OMcp3_217*ORcp3_138-\
   OMcp3_26*ORcp3_116+OPcp3_116*RLcp3_217+OPcp3_117*RLcp3_238+OPcp3_16*RLcp3_216-OPcp3_216*RLcp3_117-OPcp3_217*RLcp3_138-\
   OPcp3_26*RLcp3_116

# = = Block_1_0_0_4_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp3_138
    sens.P[2] = POcp3_238
    sens.P[3] = POcp3_338
    sens.R[1,1] = ROcp3_16
    sens.R[1,2] = ROcp3_26
    sens.R[1,3] = ROcp3_36
    sens.R[2,1] = ROcp3_417
    sens.R[2,2] = ROcp3_517
    sens.R[2,3] = ROcp3_617
    sens.R[3,1] = ROcp3_717
    sens.R[3,2] = ROcp3_817
    sens.R[3,3] = ROcp3_917
    sens.V[1] = VIcp3_138
    sens.V[2] = VIcp3_238
    sens.V[3] = VIcp3_338
    sens.OM[1] = OMcp3_117
    sens.OM[2] = OMcp3_217
    sens.OM[3] = OMcp3_317
    sens.J[1,1] = (1.0)
    sens.J[1,4] = JTcp3_138_4
    sens.J[1,5] = JTcp3_138_5
    sens.J[1,6] = JTcp3_138_6
    sens.J[1,16] = JTcp3_138_7
    sens.J[1,17] = JTcp3_138_8
    sens.J[2,2] = (1.0)
    sens.J[2,4] = JTcp3_238_4
    sens.J[2,5] = JTcp3_238_5
    sens.J[2,6] = JTcp3_238_6
    sens.J[2,16] = JTcp3_238_7
    sens.J[2,17] = JTcp3_238_8
    sens.J[3,3] = (1.0)
    sens.J[3,5] = JTcp3_338_5
    sens.J[3,6] = JTcp3_338_6
    sens.J[3,16] = JTcp3_338_7
    sens.J[3,17] = JTcp3_338_8
    sens.J[4,5] = C4
    sens.J[4,6] = ROcp3_45
    sens.J[4,16] = ROcp3_16
    sens.J[4,17] = ROcp3_16
    sens.J[5,5] = S4
    sens.J[5,6] = ROcp3_55
    sens.J[5,16] = ROcp3_26
    sens.J[5,17] = ROcp3_26
    sens.J[6,4] = (1.0)
    sens.J[6,6] = S5
    sens.J[6,16] = ROcp3_36
    sens.J[6,17] = ROcp3_36
    sens.A[1] = ACcp3_138
    sens.A[2] = ACcp3_238
    sens.A[3] = ACcp3_338
    sens.OMP[1] = OPcp3_117
    sens.OMP[2] = OPcp3_217
    sens.OMP[3] = OPcp3_317
 
# 
  elif(isens==5): 


# = = Block_1_0_0_5_0_1 = = 
 
# Sensor Kinematics 


    ROcp4_45 = -S4*C5
    ROcp4_55 = C4*C5
    ROcp4_75 = S4*S5
    ROcp4_85 = -C4*S5
    ROcp4_16 = -(ROcp4_75*S6-C4*C6)
    ROcp4_26 = -(ROcp4_85*S6-S4*C6)
    ROcp4_36 = -C5*S6
    ROcp4_76 = ROcp4_75*C6+C4*S6
    ROcp4_86 = ROcp4_85*C6+S4*S6
    ROcp4_96 = C5*C6
    OMcp4_15 = qd[5]*C4
    OMcp4_25 = qd[5]*S4
    OMcp4_16 = OMcp4_15+ROcp4_45*qd[6]
    OMcp4_26 = OMcp4_25+ROcp4_55*qd[6]
    OMcp4_36 = qd[4]+qd[6]*S5
    OPcp4_16 = ROcp4_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp4_25*S5-ROcp4_55*qd[4])
    OPcp4_26 = ROcp4_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp4_15*S5-ROcp4_45*qd[4])
    OPcp4_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_5_0_2 = = 
 
# Sensor Kinematics 


    ROcp4_47 = ROcp4_45*C7+ROcp4_76*S7
    ROcp4_57 = ROcp4_55*C7+ROcp4_86*S7
    ROcp4_67 = ROcp4_96*S7+S5*C7
    ROcp4_77 = -(ROcp4_45*S7-ROcp4_76*C7)
    ROcp4_87 = -(ROcp4_55*S7-ROcp4_86*C7)
    ROcp4_97 = ROcp4_96*C7-S5*S7
    ROcp4_18 = ROcp4_16*C8+ROcp4_47*S8
    ROcp4_28 = ROcp4_26*C8+ROcp4_57*S8
    ROcp4_38 = ROcp4_36*C8+ROcp4_67*S8
    ROcp4_48 = -(ROcp4_16*S8-ROcp4_47*C8)
    ROcp4_58 = -(ROcp4_26*S8-ROcp4_57*C8)
    ROcp4_68 = -(ROcp4_36*S8-ROcp4_67*C8)
    ROcp4_49 = ROcp4_48*C9+ROcp4_77*S9
    ROcp4_59 = ROcp4_58*C9+ROcp4_87*S9
    ROcp4_69 = ROcp4_68*C9+ROcp4_97*S9
    ROcp4_79 = -(ROcp4_48*S9-ROcp4_77*C9)
    ROcp4_89 = -(ROcp4_58*S9-ROcp4_87*C9)
    ROcp4_99 = -(ROcp4_68*S9-ROcp4_97*C9)
    RLcp4_17 = ROcp4_16*s.dpt[1,1]+ROcp4_45*s.dpt[2,1]+ROcp4_76*s.dpt[3,1]
    RLcp4_27 = ROcp4_26*s.dpt[1,1]+ROcp4_55*s.dpt[2,1]+ROcp4_86*s.dpt[3,1]
    RLcp4_37 = ROcp4_36*s.dpt[1,1]+ROcp4_96*s.dpt[3,1]+s.dpt[2,1]*S5
    OMcp4_17 = OMcp4_16+ROcp4_16*qd[7]
    OMcp4_27 = OMcp4_26+ROcp4_26*qd[7]
    OMcp4_37 = OMcp4_36+ROcp4_36*qd[7]
    ORcp4_17 = OMcp4_26*RLcp4_37-OMcp4_36*RLcp4_27
    ORcp4_27 = -(OMcp4_16*RLcp4_37-OMcp4_36*RLcp4_17)
    ORcp4_37 = OMcp4_16*RLcp4_27-OMcp4_26*RLcp4_17
    OPcp4_17 = OPcp4_16+ROcp4_16*qdd[7]+qd[7]*(OMcp4_26*ROcp4_36-OMcp4_36*ROcp4_26)
    OPcp4_27 = OPcp4_26+ROcp4_26*qdd[7]-qd[7]*(OMcp4_16*ROcp4_36-OMcp4_36*ROcp4_16)
    OPcp4_37 = OPcp4_36+ROcp4_36*qdd[7]+qd[7]*(OMcp4_16*ROcp4_26-OMcp4_26*ROcp4_16)
    RLcp4_18 = ROcp4_47*s.dpt[2,14]
    RLcp4_28 = ROcp4_57*s.dpt[2,14]
    RLcp4_38 = ROcp4_67*s.dpt[2,14]
    POcp4_18 = RLcp4_17+RLcp4_18+q[1]
    POcp4_28 = RLcp4_27+RLcp4_28+q[2]
    POcp4_38 = RLcp4_37+RLcp4_38+q[3]
    OMcp4_18 = OMcp4_17+ROcp4_77*qd[8]
    OMcp4_28 = OMcp4_27+ROcp4_87*qd[8]
    OMcp4_38 = OMcp4_37+ROcp4_97*qd[8]
    ORcp4_18 = OMcp4_27*RLcp4_38-OMcp4_37*RLcp4_28
    ORcp4_28 = -(OMcp4_17*RLcp4_38-OMcp4_37*RLcp4_18)
    ORcp4_38 = OMcp4_17*RLcp4_28-OMcp4_27*RLcp4_18
    VIcp4_18 = ORcp4_17+ORcp4_18+qd[1]
    VIcp4_28 = ORcp4_27+ORcp4_28+qd[2]
    VIcp4_38 = ORcp4_37+ORcp4_38+qd[3]
    ACcp4_18 = qdd[1]+OMcp4_26*ORcp4_37+OMcp4_27*ORcp4_38-OMcp4_36*ORcp4_27-OMcp4_37*ORcp4_28+OPcp4_26*RLcp4_37+OPcp4_27*\
   RLcp4_38-OPcp4_36*RLcp4_27-OPcp4_37*RLcp4_28
    ACcp4_28 = qdd[2]-OMcp4_16*ORcp4_37-OMcp4_17*ORcp4_38+OMcp4_36*ORcp4_17+OMcp4_37*ORcp4_18-OPcp4_16*RLcp4_37-OPcp4_17*\
   RLcp4_38+OPcp4_36*RLcp4_17+OPcp4_37*RLcp4_18
    ACcp4_38 = qdd[3]+OMcp4_16*ORcp4_27+OMcp4_17*ORcp4_28-OMcp4_26*ORcp4_17-OMcp4_27*ORcp4_18+OPcp4_16*RLcp4_27+OPcp4_17*\
   RLcp4_28-OPcp4_26*RLcp4_17-OPcp4_27*RLcp4_18
    OMcp4_19 = OMcp4_18+ROcp4_18*qd[9]
    OMcp4_29 = OMcp4_28+ROcp4_28*qd[9]
    OMcp4_39 = OMcp4_38+ROcp4_38*qd[9]
    OPcp4_19 = OPcp4_17+ROcp4_18*qdd[9]+ROcp4_77*qdd[8]+qd[8]*(OMcp4_27*ROcp4_97-OMcp4_37*ROcp4_87)+qd[9]*(OMcp4_28*\
   ROcp4_38-OMcp4_38*ROcp4_28)
    OPcp4_29 = OPcp4_27+ROcp4_28*qdd[9]+ROcp4_87*qdd[8]-qd[8]*(OMcp4_17*ROcp4_97-OMcp4_37*ROcp4_77)-qd[9]*(OMcp4_18*\
   ROcp4_38-OMcp4_38*ROcp4_18)
    OPcp4_39 = OPcp4_37+ROcp4_38*qdd[9]+ROcp4_97*qdd[8]+qd[8]*(OMcp4_17*ROcp4_87-OMcp4_27*ROcp4_77)+qd[9]*(OMcp4_18*\
   ROcp4_28-OMcp4_28*ROcp4_18)

# = = Block_1_0_0_5_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp4_18
    sens.P[2] = POcp4_28
    sens.P[3] = POcp4_38
    sens.R[1,1] = ROcp4_18
    sens.R[1,2] = ROcp4_28
    sens.R[1,3] = ROcp4_38
    sens.R[2,1] = ROcp4_49
    sens.R[2,2] = ROcp4_59
    sens.R[2,3] = ROcp4_69
    sens.R[3,1] = ROcp4_79
    sens.R[3,2] = ROcp4_89
    sens.R[3,3] = ROcp4_99
    sens.V[1] = VIcp4_18
    sens.V[2] = VIcp4_28
    sens.V[3] = VIcp4_38
    sens.OM[1] = OMcp4_19
    sens.OM[2] = OMcp4_29
    sens.OM[3] = OMcp4_39
    sens.A[1] = ACcp4_18
    sens.A[2] = ACcp4_28
    sens.A[3] = ACcp4_38
    sens.OMP[1] = OPcp4_19
    sens.OMP[2] = OPcp4_29
    sens.OMP[3] = OPcp4_39
 
# 
  elif(isens==6): 


# = = Block_1_0_0_6_0_1 = = 
 
# Sensor Kinematics 


    ROcp5_45 = -S4*C5
    ROcp5_55 = C4*C5
    ROcp5_75 = S4*S5
    ROcp5_85 = -C4*S5
    ROcp5_16 = -(ROcp5_75*S6-C4*C6)
    ROcp5_26 = -(ROcp5_85*S6-S4*C6)
    ROcp5_36 = -C5*S6
    ROcp5_76 = ROcp5_75*C6+C4*S6
    ROcp5_86 = ROcp5_85*C6+S4*S6
    ROcp5_96 = C5*C6
    OMcp5_15 = qd[5]*C4
    OMcp5_25 = qd[5]*S4
    OMcp5_16 = OMcp5_15+ROcp5_45*qd[6]
    OMcp5_26 = OMcp5_25+ROcp5_55*qd[6]
    OMcp5_36 = qd[4]+qd[6]*S5
    OPcp5_16 = ROcp5_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp5_25*S5-ROcp5_55*qd[4])
    OPcp5_26 = ROcp5_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp5_15*S5-ROcp5_45*qd[4])
    OPcp5_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_6_0_3 = = 
 
# Sensor Kinematics 


    ROcp5_410 = ROcp5_45*C10+ROcp5_76*S10
    ROcp5_510 = ROcp5_55*C10+ROcp5_86*S10
    ROcp5_610 = ROcp5_96*S10+C10*S5
    ROcp5_710 = -(ROcp5_45*S10-ROcp5_76*C10)
    ROcp5_810 = -(ROcp5_55*S10-ROcp5_86*C10)
    ROcp5_910 = ROcp5_96*C10-S10*S5
    ROcp5_111 = ROcp5_16*C11+ROcp5_410*S11
    ROcp5_211 = ROcp5_26*C11+ROcp5_510*S11
    ROcp5_311 = ROcp5_36*C11+ROcp5_610*S11
    ROcp5_411 = -(ROcp5_16*S11-ROcp5_410*C11)
    ROcp5_511 = -(ROcp5_26*S11-ROcp5_510*C11)
    ROcp5_611 = -(ROcp5_36*S11-ROcp5_610*C11)
    ROcp5_412 = ROcp5_411*C12+ROcp5_710*S12
    ROcp5_512 = ROcp5_511*C12+ROcp5_810*S12
    ROcp5_612 = ROcp5_611*C12+ROcp5_910*S12
    ROcp5_712 = -(ROcp5_411*S12-ROcp5_710*C12)
    ROcp5_812 = -(ROcp5_511*S12-ROcp5_810*C12)
    ROcp5_912 = -(ROcp5_611*S12-ROcp5_910*C12)
    RLcp5_110 = ROcp5_16*s.dpt[1,4]+ROcp5_45*s.dpt[2,4]+ROcp5_76*s.dpt[3,4]
    RLcp5_210 = ROcp5_26*s.dpt[1,4]+ROcp5_55*s.dpt[2,4]+ROcp5_86*s.dpt[3,4]
    RLcp5_310 = ROcp5_36*s.dpt[1,4]+ROcp5_96*s.dpt[3,4]+s.dpt[2,4]*S5
    OMcp5_110 = OMcp5_16+ROcp5_16*qd[10]
    OMcp5_210 = OMcp5_26+ROcp5_26*qd[10]
    OMcp5_310 = OMcp5_36+ROcp5_36*qd[10]
    ORcp5_110 = OMcp5_26*RLcp5_310-OMcp5_36*RLcp5_210
    ORcp5_210 = -(OMcp5_16*RLcp5_310-OMcp5_36*RLcp5_110)
    ORcp5_310 = OMcp5_16*RLcp5_210-OMcp5_26*RLcp5_110
    OPcp5_110 = OPcp5_16+ROcp5_16*qdd[10]+qd[10]*(OMcp5_26*ROcp5_36-OMcp5_36*ROcp5_26)
    OPcp5_210 = OPcp5_26+ROcp5_26*qdd[10]-qd[10]*(OMcp5_16*ROcp5_36-OMcp5_36*ROcp5_16)
    OPcp5_310 = OPcp5_36+ROcp5_36*qdd[10]+qd[10]*(OMcp5_16*ROcp5_26-OMcp5_26*ROcp5_16)
    RLcp5_111 = ROcp5_410*s.dpt[2,19]
    RLcp5_211 = ROcp5_510*s.dpt[2,19]
    RLcp5_311 = ROcp5_610*s.dpt[2,19]
    POcp5_111 = RLcp5_110+RLcp5_111+q[1]
    POcp5_211 = RLcp5_210+RLcp5_211+q[2]
    POcp5_311 = RLcp5_310+RLcp5_311+q[3]
    OMcp5_111 = OMcp5_110+ROcp5_710*qd[11]
    OMcp5_211 = OMcp5_210+ROcp5_810*qd[11]
    OMcp5_311 = OMcp5_310+ROcp5_910*qd[11]
    ORcp5_111 = OMcp5_210*RLcp5_311-OMcp5_310*RLcp5_211
    ORcp5_211 = -(OMcp5_110*RLcp5_311-OMcp5_310*RLcp5_111)
    ORcp5_311 = OMcp5_110*RLcp5_211-OMcp5_210*RLcp5_111
    VIcp5_111 = ORcp5_110+ORcp5_111+qd[1]
    VIcp5_211 = ORcp5_210+ORcp5_211+qd[2]
    VIcp5_311 = ORcp5_310+ORcp5_311+qd[3]
    ACcp5_111 = qdd[1]+OMcp5_210*ORcp5_311+OMcp5_26*ORcp5_310-OMcp5_310*ORcp5_211-OMcp5_36*ORcp5_210+OPcp5_210*RLcp5_311+\
   OPcp5_26*RLcp5_310-OPcp5_310*RLcp5_211-OPcp5_36*RLcp5_210
    ACcp5_211 = qdd[2]-OMcp5_110*ORcp5_311-OMcp5_16*ORcp5_310+OMcp5_310*ORcp5_111+OMcp5_36*ORcp5_110-OPcp5_110*RLcp5_311-\
   OPcp5_16*RLcp5_310+OPcp5_310*RLcp5_111+OPcp5_36*RLcp5_110
    ACcp5_311 = qdd[3]+OMcp5_110*ORcp5_211+OMcp5_16*ORcp5_210-OMcp5_210*ORcp5_111-OMcp5_26*ORcp5_110+OPcp5_110*RLcp5_211+\
   OPcp5_16*RLcp5_210-OPcp5_210*RLcp5_111-OPcp5_26*RLcp5_110
    OMcp5_112 = OMcp5_111+ROcp5_111*qd[12]
    OMcp5_212 = OMcp5_211+ROcp5_211*qd[12]
    OMcp5_312 = OMcp5_311+ROcp5_311*qd[12]
    OPcp5_112 = OPcp5_110+ROcp5_111*qdd[12]+ROcp5_710*qdd[11]+qd[11]*(OMcp5_210*ROcp5_910-OMcp5_310*ROcp5_810)+qd[12]*(\
   OMcp5_211*ROcp5_311-OMcp5_311*ROcp5_211)
    OPcp5_212 = OPcp5_210+ROcp5_211*qdd[12]+ROcp5_810*qdd[11]-qd[11]*(OMcp5_110*ROcp5_910-OMcp5_310*ROcp5_710)-qd[12]*(\
   OMcp5_111*ROcp5_311-OMcp5_311*ROcp5_111)
    OPcp5_312 = OPcp5_310+ROcp5_311*qdd[12]+ROcp5_910*qdd[11]+qd[11]*(OMcp5_110*ROcp5_810-OMcp5_210*ROcp5_710)+qd[12]*(\
   OMcp5_111*ROcp5_211-OMcp5_211*ROcp5_111)

# = = Block_1_0_0_6_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp5_111
    sens.P[2] = POcp5_211
    sens.P[3] = POcp5_311
    sens.R[1,1] = ROcp5_111
    sens.R[1,2] = ROcp5_211
    sens.R[1,3] = ROcp5_311
    sens.R[2,1] = ROcp5_412
    sens.R[2,2] = ROcp5_512
    sens.R[2,3] = ROcp5_612
    sens.R[3,1] = ROcp5_712
    sens.R[3,2] = ROcp5_812
    sens.R[3,3] = ROcp5_912
    sens.V[1] = VIcp5_111
    sens.V[2] = VIcp5_211
    sens.V[3] = VIcp5_311
    sens.OM[1] = OMcp5_112
    sens.OM[2] = OMcp5_212
    sens.OM[3] = OMcp5_312
    sens.A[1] = ACcp5_111
    sens.A[2] = ACcp5_211
    sens.A[3] = ACcp5_311
    sens.OMP[1] = OPcp5_112
    sens.OMP[2] = OPcp5_212
    sens.OMP[3] = OPcp5_312
 
# 
  elif(isens==7): 


# = = Block_1_0_0_7_0_1 = = 
 
# Sensor Kinematics 


    ROcp6_45 = -S4*C5
    ROcp6_55 = C4*C5
    ROcp6_75 = S4*S5
    ROcp6_85 = -C4*S5
    ROcp6_16 = -(ROcp6_75*S6-C4*C6)
    ROcp6_26 = -(ROcp6_85*S6-S4*C6)
    ROcp6_36 = -C5*S6
    ROcp6_76 = ROcp6_75*C6+C4*S6
    ROcp6_86 = ROcp6_85*C6+S4*S6
    ROcp6_96 = C5*C6
    OMcp6_15 = qd[5]*C4
    OMcp6_25 = qd[5]*S4
    OMcp6_16 = OMcp6_15+ROcp6_45*qd[6]
    OMcp6_26 = OMcp6_25+ROcp6_55*qd[6]
    OMcp6_36 = qd[4]+qd[6]*S5
    OPcp6_16 = ROcp6_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp6_25*S5-ROcp6_55*qd[4])
    OPcp6_26 = ROcp6_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp6_15*S5-ROcp6_45*qd[4])
    OPcp6_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_7_0_4 = = 
 
# Sensor Kinematics 


    ROcp6_413 = ROcp6_45*C13+ROcp6_76*S13
    ROcp6_513 = ROcp6_55*C13+ROcp6_86*S13
    ROcp6_613 = ROcp6_96*S13+C13*S5
    ROcp6_713 = -(ROcp6_45*S13-ROcp6_76*C13)
    ROcp6_813 = -(ROcp6_55*S13-ROcp6_86*C13)
    ROcp6_913 = ROcp6_96*C13-S13*S5
    ROcp6_414 = ROcp6_413*C14+ROcp6_713*S14
    ROcp6_514 = ROcp6_513*C14+ROcp6_813*S14
    ROcp6_614 = ROcp6_613*C14+ROcp6_913*S14
    ROcp6_714 = -(ROcp6_413*S14-ROcp6_713*C14)
    ROcp6_814 = -(ROcp6_513*S14-ROcp6_813*C14)
    ROcp6_914 = -(ROcp6_613*S14-ROcp6_913*C14)
    ROcp6_415 = ROcp6_414*C15+ROcp6_714*S15
    ROcp6_515 = ROcp6_514*C15+ROcp6_814*S15
    ROcp6_615 = ROcp6_614*C15+ROcp6_914*S15
    ROcp6_715 = -(ROcp6_414*S15-ROcp6_714*C15)
    ROcp6_815 = -(ROcp6_514*S15-ROcp6_814*C15)
    ROcp6_915 = -(ROcp6_614*S15-ROcp6_914*C15)
    RLcp6_113 = ROcp6_16*s.dpt[1,9]+ROcp6_45*s.dpt[2,9]+ROcp6_76*s.dpt[3,9]
    RLcp6_213 = ROcp6_26*s.dpt[1,9]+ROcp6_55*s.dpt[2,9]+ROcp6_86*s.dpt[3,9]
    RLcp6_313 = ROcp6_36*s.dpt[1,9]+ROcp6_96*s.dpt[3,9]+s.dpt[2,9]*S5
    OMcp6_113 = OMcp6_16+ROcp6_16*qd[13]
    OMcp6_213 = OMcp6_26+ROcp6_26*qd[13]
    OMcp6_313 = OMcp6_36+ROcp6_36*qd[13]
    ORcp6_113 = OMcp6_26*RLcp6_313-OMcp6_36*RLcp6_213
    ORcp6_213 = -(OMcp6_16*RLcp6_313-OMcp6_36*RLcp6_113)
    ORcp6_313 = OMcp6_16*RLcp6_213-OMcp6_26*RLcp6_113
    OPcp6_113 = OPcp6_16+ROcp6_16*qdd[13]+qd[13]*(OMcp6_26*ROcp6_36-OMcp6_36*ROcp6_26)
    OPcp6_213 = OPcp6_26+ROcp6_26*qdd[13]-qd[13]*(OMcp6_16*ROcp6_36-OMcp6_36*ROcp6_16)
    OPcp6_313 = OPcp6_36+ROcp6_36*qdd[13]+qd[13]*(OMcp6_16*ROcp6_26-OMcp6_26*ROcp6_16)
    RLcp6_114 = ROcp6_413*s.dpt[2,24]
    RLcp6_214 = ROcp6_513*s.dpt[2,24]
    RLcp6_314 = ROcp6_613*s.dpt[2,24]
    OMcp6_114 = OMcp6_113+ROcp6_16*qd[14]
    OMcp6_214 = OMcp6_213+ROcp6_26*qd[14]
    OMcp6_314 = OMcp6_313+ROcp6_36*qd[14]
    ORcp6_114 = OMcp6_213*RLcp6_314-OMcp6_313*RLcp6_214
    ORcp6_214 = -(OMcp6_113*RLcp6_314-OMcp6_313*RLcp6_114)
    ORcp6_314 = OMcp6_113*RLcp6_214-OMcp6_213*RLcp6_114
    OPcp6_114 = OPcp6_113+ROcp6_16*qdd[14]+qd[14]*(OMcp6_213*ROcp6_36-OMcp6_313*ROcp6_26)
    OPcp6_214 = OPcp6_213+ROcp6_26*qdd[14]-qd[14]*(OMcp6_113*ROcp6_36-OMcp6_313*ROcp6_16)
    OPcp6_314 = OPcp6_313+ROcp6_36*qdd[14]+qd[14]*(OMcp6_113*ROcp6_26-OMcp6_213*ROcp6_16)
    RLcp6_115 = ROcp6_16*s.dpt[1,26]
    RLcp6_215 = ROcp6_26*s.dpt[1,26]
    RLcp6_315 = ROcp6_36*s.dpt[1,26]
    POcp6_115 = RLcp6_113+RLcp6_114+RLcp6_115+q[1]
    POcp6_215 = RLcp6_213+RLcp6_214+RLcp6_215+q[2]
    POcp6_315 = RLcp6_313+RLcp6_314+RLcp6_315+q[3]
    OMcp6_115 = OMcp6_114+ROcp6_16*qd[15]
    OMcp6_215 = OMcp6_214+ROcp6_26*qd[15]
    OMcp6_315 = OMcp6_314+ROcp6_36*qd[15]
    ORcp6_115 = OMcp6_214*RLcp6_315-OMcp6_314*RLcp6_215
    ORcp6_215 = -(OMcp6_114*RLcp6_315-OMcp6_314*RLcp6_115)
    ORcp6_315 = OMcp6_114*RLcp6_215-OMcp6_214*RLcp6_115
    VIcp6_115 = ORcp6_113+ORcp6_114+ORcp6_115+qd[1]
    VIcp6_215 = ORcp6_213+ORcp6_214+ORcp6_215+qd[2]
    VIcp6_315 = ORcp6_313+ORcp6_314+ORcp6_315+qd[3]
    OPcp6_115 = OPcp6_114+ROcp6_16*qdd[15]+qd[15]*(OMcp6_214*ROcp6_36-OMcp6_314*ROcp6_26)
    OPcp6_215 = OPcp6_214+ROcp6_26*qdd[15]-qd[15]*(OMcp6_114*ROcp6_36-OMcp6_314*ROcp6_16)
    OPcp6_315 = OPcp6_314+ROcp6_36*qdd[15]+qd[15]*(OMcp6_114*ROcp6_26-OMcp6_214*ROcp6_16)
    ACcp6_115 = qdd[1]+OMcp6_213*ORcp6_314+OMcp6_214*ORcp6_315+OMcp6_26*ORcp6_313-OMcp6_313*ORcp6_214-OMcp6_314*ORcp6_215-\
   OMcp6_36*ORcp6_213+OPcp6_213*RLcp6_314+OPcp6_214*RLcp6_315+OPcp6_26*RLcp6_313-OPcp6_313*RLcp6_214-OPcp6_314*RLcp6_215-\
   OPcp6_36*RLcp6_213
    ACcp6_215 = qdd[2]-OMcp6_113*ORcp6_314-OMcp6_114*ORcp6_315-OMcp6_16*ORcp6_313+OMcp6_313*ORcp6_114+OMcp6_314*ORcp6_115+\
   OMcp6_36*ORcp6_113-OPcp6_113*RLcp6_314-OPcp6_114*RLcp6_315-OPcp6_16*RLcp6_313+OPcp6_313*RLcp6_114+OPcp6_314*RLcp6_115+\
   OPcp6_36*RLcp6_113
    ACcp6_315 = qdd[3]+OMcp6_113*ORcp6_214+OMcp6_114*ORcp6_215+OMcp6_16*ORcp6_213-OMcp6_213*ORcp6_114-OMcp6_214*ORcp6_115-\
   OMcp6_26*ORcp6_113+OPcp6_113*RLcp6_214+OPcp6_114*RLcp6_215+OPcp6_16*RLcp6_213-OPcp6_213*RLcp6_114-OPcp6_214*RLcp6_115-\
   OPcp6_26*RLcp6_113

# = = Block_1_0_0_7_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp6_115
    sens.P[2] = POcp6_215
    sens.P[3] = POcp6_315
    sens.R[1,1] = ROcp6_16
    sens.R[1,2] = ROcp6_26
    sens.R[1,3] = ROcp6_36
    sens.R[2,1] = ROcp6_415
    sens.R[2,2] = ROcp6_515
    sens.R[2,3] = ROcp6_615
    sens.R[3,1] = ROcp6_715
    sens.R[3,2] = ROcp6_815
    sens.R[3,3] = ROcp6_915
    sens.V[1] = VIcp6_115
    sens.V[2] = VIcp6_215
    sens.V[3] = VIcp6_315
    sens.OM[1] = OMcp6_115
    sens.OM[2] = OMcp6_215
    sens.OM[3] = OMcp6_315
    sens.A[1] = ACcp6_115
    sens.A[2] = ACcp6_215
    sens.A[3] = ACcp6_315
    sens.OMP[1] = OPcp6_115
    sens.OMP[2] = OPcp6_215
    sens.OMP[3] = OPcp6_315
 
# 
  elif(isens==8): 


# = = Block_1_0_0_8_0_1 = = 
 
# Sensor Kinematics 


    ROcp7_45 = -S4*C5
    ROcp7_55 = C4*C5
    ROcp7_75 = S4*S5
    ROcp7_85 = -C4*S5
    ROcp7_16 = -(ROcp7_75*S6-C4*C6)
    ROcp7_26 = -(ROcp7_85*S6-S4*C6)
    ROcp7_36 = -C5*S6
    ROcp7_76 = ROcp7_75*C6+C4*S6
    ROcp7_86 = ROcp7_85*C6+S4*S6
    ROcp7_96 = C5*C6
    OMcp7_15 = qd[5]*C4
    OMcp7_25 = qd[5]*S4
    OMcp7_16 = OMcp7_15+ROcp7_45*qd[6]
    OMcp7_26 = OMcp7_25+ROcp7_55*qd[6]
    OMcp7_36 = qd[4]+qd[6]*S5
    OPcp7_16 = ROcp7_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp7_25*S5-ROcp7_55*qd[4])
    OPcp7_26 = ROcp7_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp7_15*S5-ROcp7_45*qd[4])
    OPcp7_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_8_0_5 = = 
 
# Sensor Kinematics 


    ROcp7_416 = ROcp7_45*C16+ROcp7_76*S16
    ROcp7_516 = ROcp7_55*C16+ROcp7_86*S16
    ROcp7_616 = ROcp7_96*S16+C16*S5
    ROcp7_716 = -(ROcp7_45*S16-ROcp7_76*C16)
    ROcp7_816 = -(ROcp7_55*S16-ROcp7_86*C16)
    ROcp7_916 = ROcp7_96*C16-S16*S5
    ROcp7_417 = ROcp7_416*C17+ROcp7_716*S17
    ROcp7_517 = ROcp7_516*C17+ROcp7_816*S17
    ROcp7_617 = ROcp7_616*C17+ROcp7_916*S17
    ROcp7_717 = -(ROcp7_416*S17-ROcp7_716*C17)
    ROcp7_817 = -(ROcp7_516*S17-ROcp7_816*C17)
    ROcp7_917 = -(ROcp7_616*S17-ROcp7_916*C17)
    ROcp7_418 = ROcp7_417*C18+ROcp7_717*S18
    ROcp7_518 = ROcp7_517*C18+ROcp7_817*S18
    ROcp7_618 = ROcp7_617*C18+ROcp7_917*S18
    ROcp7_718 = -(ROcp7_417*S18-ROcp7_717*C18)
    ROcp7_818 = -(ROcp7_517*S18-ROcp7_817*C18)
    ROcp7_918 = -(ROcp7_617*S18-ROcp7_917*C18)
    RLcp7_116 = ROcp7_16*s.dpt[1,11]+ROcp7_45*s.dpt[2,11]+ROcp7_76*s.dpt[3,11]
    RLcp7_216 = ROcp7_26*s.dpt[1,11]+ROcp7_55*s.dpt[2,11]+ROcp7_86*s.dpt[3,11]
    RLcp7_316 = ROcp7_36*s.dpt[1,11]+ROcp7_96*s.dpt[3,11]+s.dpt[2,11]*S5
    OMcp7_116 = OMcp7_16+ROcp7_16*qd[16]
    OMcp7_216 = OMcp7_26+ROcp7_26*qd[16]
    OMcp7_316 = OMcp7_36+ROcp7_36*qd[16]
    ORcp7_116 = OMcp7_26*RLcp7_316-OMcp7_36*RLcp7_216
    ORcp7_216 = -(OMcp7_16*RLcp7_316-OMcp7_36*RLcp7_116)
    ORcp7_316 = OMcp7_16*RLcp7_216-OMcp7_26*RLcp7_116
    OPcp7_116 = OPcp7_16+ROcp7_16*qdd[16]+qd[16]*(OMcp7_26*ROcp7_36-OMcp7_36*ROcp7_26)
    OPcp7_216 = OPcp7_26+ROcp7_26*qdd[16]-qd[16]*(OMcp7_16*ROcp7_36-OMcp7_36*ROcp7_16)
    OPcp7_316 = OPcp7_36+ROcp7_36*qdd[16]+qd[16]*(OMcp7_16*ROcp7_26-OMcp7_26*ROcp7_16)
    RLcp7_117 = ROcp7_416*s.dpt[2,30]
    RLcp7_217 = ROcp7_516*s.dpt[2,30]
    RLcp7_317 = ROcp7_616*s.dpt[2,30]
    OMcp7_117 = OMcp7_116+ROcp7_16*qd[17]
    OMcp7_217 = OMcp7_216+ROcp7_26*qd[17]
    OMcp7_317 = OMcp7_316+ROcp7_36*qd[17]
    ORcp7_117 = OMcp7_216*RLcp7_317-OMcp7_316*RLcp7_217
    ORcp7_217 = -(OMcp7_116*RLcp7_317-OMcp7_316*RLcp7_117)
    ORcp7_317 = OMcp7_116*RLcp7_217-OMcp7_216*RLcp7_117
    OPcp7_117 = OPcp7_116+ROcp7_16*qdd[17]+qd[17]*(OMcp7_216*ROcp7_36-OMcp7_316*ROcp7_26)
    OPcp7_217 = OPcp7_216+ROcp7_26*qdd[17]-qd[17]*(OMcp7_116*ROcp7_36-OMcp7_316*ROcp7_16)
    OPcp7_317 = OPcp7_316+ROcp7_36*qdd[17]+qd[17]*(OMcp7_116*ROcp7_26-OMcp7_216*ROcp7_16)
    RLcp7_118 = ROcp7_16*s.dpt[1,34]
    RLcp7_218 = ROcp7_26*s.dpt[1,34]
    RLcp7_318 = ROcp7_36*s.dpt[1,34]
    POcp7_118 = RLcp7_116+RLcp7_117+RLcp7_118+q[1]
    POcp7_218 = RLcp7_216+RLcp7_217+RLcp7_218+q[2]
    POcp7_318 = RLcp7_316+RLcp7_317+RLcp7_318+q[3]
    OMcp7_118 = OMcp7_117+ROcp7_16*qd[18]
    OMcp7_218 = OMcp7_217+ROcp7_26*qd[18]
    OMcp7_318 = OMcp7_317+ROcp7_36*qd[18]
    ORcp7_118 = OMcp7_217*RLcp7_318-OMcp7_317*RLcp7_218
    ORcp7_218 = -(OMcp7_117*RLcp7_318-OMcp7_317*RLcp7_118)
    ORcp7_318 = OMcp7_117*RLcp7_218-OMcp7_217*RLcp7_118
    VIcp7_118 = ORcp7_116+ORcp7_117+ORcp7_118+qd[1]
    VIcp7_218 = ORcp7_216+ORcp7_217+ORcp7_218+qd[2]
    VIcp7_318 = ORcp7_316+ORcp7_317+ORcp7_318+qd[3]
    OPcp7_118 = OPcp7_117+ROcp7_16*qdd[18]+qd[18]*(OMcp7_217*ROcp7_36-OMcp7_317*ROcp7_26)
    OPcp7_218 = OPcp7_217+ROcp7_26*qdd[18]-qd[18]*(OMcp7_117*ROcp7_36-OMcp7_317*ROcp7_16)
    OPcp7_318 = OPcp7_317+ROcp7_36*qdd[18]+qd[18]*(OMcp7_117*ROcp7_26-OMcp7_217*ROcp7_16)
    ACcp7_118 = qdd[1]+OMcp7_216*ORcp7_317+OMcp7_217*ORcp7_318+OMcp7_26*ORcp7_316-OMcp7_316*ORcp7_217-OMcp7_317*ORcp7_218-\
   OMcp7_36*ORcp7_216+OPcp7_216*RLcp7_317+OPcp7_217*RLcp7_318+OPcp7_26*RLcp7_316-OPcp7_316*RLcp7_217-OPcp7_317*RLcp7_218-\
   OPcp7_36*RLcp7_216
    ACcp7_218 = qdd[2]-OMcp7_116*ORcp7_317-OMcp7_117*ORcp7_318-OMcp7_16*ORcp7_316+OMcp7_316*ORcp7_117+OMcp7_317*ORcp7_118+\
   OMcp7_36*ORcp7_116-OPcp7_116*RLcp7_317-OPcp7_117*RLcp7_318-OPcp7_16*RLcp7_316+OPcp7_316*RLcp7_117+OPcp7_317*RLcp7_118+\
   OPcp7_36*RLcp7_116
    ACcp7_318 = qdd[3]+OMcp7_116*ORcp7_217+OMcp7_117*ORcp7_218+OMcp7_16*ORcp7_216-OMcp7_216*ORcp7_117-OMcp7_217*ORcp7_118-\
   OMcp7_26*ORcp7_116+OPcp7_116*RLcp7_217+OPcp7_117*RLcp7_218+OPcp7_16*RLcp7_216-OPcp7_216*RLcp7_117-OPcp7_217*RLcp7_118-\
   OPcp7_26*RLcp7_116

# = = Block_1_0_0_8_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp7_118
    sens.P[2] = POcp7_218
    sens.P[3] = POcp7_318
    sens.R[1,1] = ROcp7_16
    sens.R[1,2] = ROcp7_26
    sens.R[1,3] = ROcp7_36
    sens.R[2,1] = ROcp7_418
    sens.R[2,2] = ROcp7_518
    sens.R[2,3] = ROcp7_618
    sens.R[3,1] = ROcp7_718
    sens.R[3,2] = ROcp7_818
    sens.R[3,3] = ROcp7_918
    sens.V[1] = VIcp7_118
    sens.V[2] = VIcp7_218
    sens.V[3] = VIcp7_318
    sens.OM[1] = OMcp7_118
    sens.OM[2] = OMcp7_218
    sens.OM[3] = OMcp7_318
    sens.A[1] = ACcp7_118
    sens.A[2] = ACcp7_218
    sens.A[3] = ACcp7_318
    sens.OMP[1] = OPcp7_118
    sens.OMP[2] = OPcp7_218
    sens.OMP[3] = OPcp7_318



# ====== END Task 1 ====== 

  

