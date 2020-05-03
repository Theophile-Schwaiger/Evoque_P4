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
#	==> Generation Date : Fri Apr  3 02:23:57 2020
#
#	==> Project name : Complete_Vehicle_Direction
#	==> using XML input file 
#
#	==> Number of joints : 41
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 12483
#
#	==> Generation Time :  0.190 seconds
#	==> Post-Processing :  0.260 seconds
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

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C13 = np.cos(q[13])
  S13 = np.sin(q[13])
  C14 = np.cos(q[14])
  S14 = np.sin(q[14])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C15 = np.cos(q[15])
  S15 = np.sin(q[15])
  C16 = np.cos(q[16])
  S16 = np.sin(q[16])
  C17 = np.cos(q[17])
  S17 = np.sin(q[17])
  C18 = np.cos(q[18])
  S18 = np.sin(q[18])

# = = Block_0_0_0_0_0_6 = = 
 
# Trigonometric Variables  

  C19 = np.cos(q[19])
  S19 = np.sin(q[19])

# = = Block_0_0_0_0_0_7 = = 
 
# Trigonometric Variables  

  C21 = np.cos(q[21])
  S21 = np.sin(q[21])
  C22 = np.cos(q[22])
  S22 = np.sin(q[22])

# = = Block_0_0_0_0_0_8 = = 
 
# Trigonometric Variables  

  C23 = np.cos(q[23])
  S23 = np.sin(q[23])
  C24 = np.cos(q[24])
  S24 = np.sin(q[24])
  C25 = np.cos(q[25])
  S25 = np.sin(q[25])
  C26 = np.cos(q[26])
  S26 = np.sin(q[26])
  C27 = np.cos(q[27])
  S27 = np.sin(q[27])

# = = Block_0_0_0_0_0_9 = = 
 
# Trigonometric Variables  

  C28 = np.cos(q[28])
  S28 = np.sin(q[28])

# = = Block_0_0_0_0_0_10 = = 
 
# Trigonometric Variables  

  C30 = np.cos(q[30])
  S30 = np.sin(q[30])
  C31 = np.cos(q[31])
  S31 = np.sin(q[31])

# = = Block_0_0_0_0_0_11 = = 
 
# Trigonometric Variables  

  C32 = np.cos(q[32])
  S32 = np.sin(q[32])
  C33 = np.cos(q[33])
  S33 = np.sin(q[33])
  C34 = np.cos(q[34])
  S34 = np.sin(q[34])
  C35 = np.cos(q[35])
  S35 = np.sin(q[35])
  C36 = np.cos(q[36])
  S36 = np.sin(q[36])

# = = Block_0_0_0_0_0_12 = = 
 
# Trigonometric Variables  

  C37 = np.cos(q[37])
  S37 = np.sin(q[37])

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C39 = np.cos(q[39])
  S39 = np.sin(q[39])
  C40 = np.cos(q[40])
  S40 = np.sin(q[40])

# = = Block_0_0_0_7_0_2 = = 
 
# Trigonometric Variables  

  S6p7 = C6*S7+S6*C7
  C6p7 = C6*C7-S6*S7

# = = Block_0_0_0_15_0_5 = = 
 
# Trigonometric Variables  

  S15p6 = C15*S6+S15*C6
  C15p6 = C15*C6-S15*S6

# = = Block_0_0_0_23_0_8 = = 
 
# Trigonometric Variables  

  S23p6 = C23*S6+S23*C6
  C23p6 = C23*C6-S23*S6

# = = Block_0_0_0_32_0_11 = = 
 
# Trigonometric Variables  

  S32p6 = C32*S6+S32*C6
  C32p6 = C32*C6-S32*S6

# ====== END Task 0 ====== 

# ===== BEGIN task 1 ===== 
 
# Sensor Kinematics 


 
# 
  if(isens==1): 


# = = Block_1_0_0_1_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.R[1,1] = (1.0)
    sens.R[2,2] = (1.0)
    sens.R[3,3] = (1.0)
    sens.V[1] = qd[1]
    sens.A[1] = qdd[1]
 
# 
  elif(isens==2): 


# = = Block_1_0_0_2_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.R[1,1] = (1.0)
    sens.R[2,2] = (1.0)
    sens.R[3,3] = (1.0)
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
 
# 
  elif(isens==3): 


# = = Block_1_0_0_3_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = (1.0)
    sens.R[2,2] = (1.0)
    sens.R[3,3] = (1.0)
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.V[3] = qd[3]
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
    sens.A[3] = qdd[3]
 
# 
  elif(isens==4): 


# = = Block_1_0_0_4_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = C4
    sens.R[1,2] = S4
    sens.R[2,1] = -S4
    sens.R[2,2] = C4
    sens.R[3,3] = (1.0)
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.V[3] = qd[3]
    sens.OM[3] = qd[4]
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
    sens.A[3] = qdd[3]
    sens.OMP[3] = qdd[4]
 
# 
  elif(isens==5): 


# = = Block_1_0_0_5_0_1 = = 
 
# Sensor Kinematics 


    ROcp4_15 = C4*C5
    ROcp4_25 = S4*C5
    ROcp4_75 = C4*S5
    ROcp4_85 = S4*S5
    OMcp4_15 = -qd[5]*S4
    OMcp4_25 = qd[5]*C4
    OPcp4_15 = -(qdd[5]*S4+qd[4]*qd[5]*C4)
    OPcp4_25 = qdd[5]*C4-qd[4]*qd[5]*S4

# = = Block_1_0_0_5_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = ROcp4_15
    sens.R[1,2] = ROcp4_25
    sens.R[1,3] = -S5
    sens.R[2,1] = -S4
    sens.R[2,2] = C4
    sens.R[3,1] = ROcp4_75
    sens.R[3,2] = ROcp4_85
    sens.R[3,3] = C5
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.V[3] = qd[3]
    sens.OM[1] = OMcp4_15
    sens.OM[2] = OMcp4_25
    sens.OM[3] = qd[4]
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
    sens.A[3] = qdd[3]
    sens.OMP[1] = OPcp4_15
    sens.OMP[2] = OPcp4_25
    sens.OMP[3] = qdd[4]
 
# 
  elif(isens==6): 


# = = Block_1_0_0_6_0_1 = = 
 
# Sensor Kinematics 


    ROcp5_15 = C4*C5
    ROcp5_25 = S4*C5
    ROcp5_75 = C4*S5
    ROcp5_85 = S4*S5
    ROcp5_46 = ROcp5_75*S6-S4*C6
    ROcp5_56 = ROcp5_85*S6+C4*C6
    ROcp5_66 = C5*S6
    ROcp5_76 = ROcp5_75*C6+S4*S6
    ROcp5_86 = ROcp5_85*C6-C4*S6
    ROcp5_96 = C5*C6
    OMcp5_15 = -qd[5]*S4
    OMcp5_25 = qd[5]*C4
    OMcp5_16 = OMcp5_15+ROcp5_15*qd[6]
    OMcp5_26 = OMcp5_25+ROcp5_25*qd[6]
    OMcp5_36 = qd[4]-qd[6]*S5
    OPcp5_16 = ROcp5_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp5_25*S5+ROcp5_25*qd[4])
    OPcp5_26 = ROcp5_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp5_15*S5+ROcp5_15*qd[4])
    OPcp5_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_6_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = ROcp5_15
    sens.R[1,2] = ROcp5_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp5_46
    sens.R[2,2] = ROcp5_56
    sens.R[2,3] = ROcp5_66
    sens.R[3,1] = ROcp5_76
    sens.R[3,2] = ROcp5_86
    sens.R[3,3] = ROcp5_96
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.V[3] = qd[3]
    sens.OM[1] = OMcp5_16
    sens.OM[2] = OMcp5_26
    sens.OM[3] = OMcp5_36
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
    sens.A[3] = qdd[3]
    sens.OMP[1] = OPcp5_16
    sens.OMP[2] = OPcp5_26
    sens.OMP[3] = OPcp5_36
 
# 
  elif(isens==7): 


# = = Block_1_0_0_7_0_1 = = 
 
# Sensor Kinematics 


    ROcp6_15 = C4*C5
    ROcp6_25 = S4*C5
    ROcp6_75 = C4*S5
    ROcp6_85 = S4*S5
    ROcp6_46 = ROcp6_75*S6-S4*C6
    ROcp6_56 = ROcp6_85*S6+C4*C6
    ROcp6_76 = ROcp6_75*C6+S4*S6
    ROcp6_86 = ROcp6_85*C6-C4*S6
    OMcp6_15 = -qd[5]*S4
    OMcp6_25 = qd[5]*C4
    OMcp6_16 = OMcp6_15+ROcp6_15*qd[6]
    OMcp6_26 = OMcp6_25+ROcp6_25*qd[6]
    OMcp6_36 = qd[4]-qd[6]*S5
    OPcp6_16 = ROcp6_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp6_25*S5+ROcp6_25*qd[4])
    OPcp6_26 = ROcp6_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp6_15*S5+ROcp6_15*qd[4])
    OPcp6_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_7_0_2 = = 
 
# Sensor Kinematics 


    ROcp6_47 = ROcp6_46*C7+ROcp6_76*S7
    ROcp6_57 = ROcp6_56*C7+ROcp6_86*S7
    ROcp6_67 = S6p7*C5
    ROcp6_77 = -(ROcp6_46*S7-ROcp6_76*C7)
    ROcp6_87 = -(ROcp6_56*S7-ROcp6_86*C7)
    ROcp6_97 = C6p7*C5
    RLcp6_17 = ROcp6_15*s.dpt[1,1]+ROcp6_46*s.dpt[2,1]
    RLcp6_27 = ROcp6_25*s.dpt[1,1]+ROcp6_56*s.dpt[2,1]
    RLcp6_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    POcp6_17 = RLcp6_17+q[1]
    POcp6_27 = RLcp6_27+q[2]
    POcp6_37 = RLcp6_37+q[3]
    OMcp6_17 = OMcp6_16+ROcp6_15*qd[7]
    OMcp6_27 = OMcp6_26+ROcp6_25*qd[7]
    OMcp6_37 = OMcp6_36-qd[7]*S5
    ORcp6_17 = OMcp6_26*RLcp6_37-OMcp6_36*RLcp6_27
    ORcp6_27 = -(OMcp6_16*RLcp6_37-OMcp6_36*RLcp6_17)
    ORcp6_37 = OMcp6_16*RLcp6_27-OMcp6_26*RLcp6_17
    VIcp6_17 = ORcp6_17+qd[1]
    VIcp6_27 = ORcp6_27+qd[2]
    VIcp6_37 = ORcp6_37+qd[3]
    OPcp6_17 = OPcp6_16+ROcp6_15*qdd[7]-qd[7]*(OMcp6_26*S5+OMcp6_36*ROcp6_25)
    OPcp6_27 = OPcp6_26+ROcp6_25*qdd[7]+qd[7]*(OMcp6_16*S5+OMcp6_36*ROcp6_15)
    OPcp6_37 = OPcp6_36-qdd[7]*S5+qd[7]*(OMcp6_16*ROcp6_25-OMcp6_26*ROcp6_15)
    ACcp6_17 = qdd[1]+OMcp6_26*ORcp6_37-OMcp6_36*ORcp6_27+OPcp6_26*RLcp6_37-OPcp6_36*RLcp6_27
    ACcp6_27 = qdd[2]-OMcp6_16*ORcp6_37+OMcp6_36*ORcp6_17-OPcp6_16*RLcp6_37+OPcp6_36*RLcp6_17
    ACcp6_37 = qdd[3]+OMcp6_16*ORcp6_27-OMcp6_26*ORcp6_17+OPcp6_16*RLcp6_27-OPcp6_26*RLcp6_17

# = = Block_1_0_0_7_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp6_17
    sens.P[2] = POcp6_27
    sens.P[3] = POcp6_37
    sens.R[1,1] = ROcp6_15
    sens.R[1,2] = ROcp6_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp6_47
    sens.R[2,2] = ROcp6_57
    sens.R[2,3] = ROcp6_67
    sens.R[3,1] = ROcp6_77
    sens.R[3,2] = ROcp6_87
    sens.R[3,3] = ROcp6_97
    sens.V[1] = VIcp6_17
    sens.V[2] = VIcp6_27
    sens.V[3] = VIcp6_37
    sens.OM[1] = OMcp6_17
    sens.OM[2] = OMcp6_27
    sens.OM[3] = OMcp6_37
    sens.A[1] = ACcp6_17
    sens.A[2] = ACcp6_27
    sens.A[3] = ACcp6_37
    sens.OMP[1] = OPcp6_17
    sens.OMP[2] = OPcp6_27
    sens.OMP[3] = OPcp6_37
 
# 
  elif(isens==8): 


# = = Block_1_0_0_8_0_1 = = 
 
# Sensor Kinematics 


    ROcp7_15 = C4*C5
    ROcp7_25 = S4*C5
    ROcp7_75 = C4*S5
    ROcp7_85 = S4*S5
    ROcp7_46 = ROcp7_75*S6-S4*C6
    ROcp7_56 = ROcp7_85*S6+C4*C6
    ROcp7_76 = ROcp7_75*C6+S4*S6
    ROcp7_86 = ROcp7_85*C6-C4*S6
    OMcp7_15 = -qd[5]*S4
    OMcp7_25 = qd[5]*C4
    OMcp7_16 = OMcp7_15+ROcp7_15*qd[6]
    OMcp7_26 = OMcp7_25+ROcp7_25*qd[6]
    OMcp7_36 = qd[4]-qd[6]*S5
    OPcp7_16 = ROcp7_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp7_25*S5+ROcp7_25*qd[4])
    OPcp7_26 = ROcp7_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp7_15*S5+ROcp7_15*qd[4])
    OPcp7_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_8_0_2 = = 
 
# Sensor Kinematics 


    ROcp7_47 = ROcp7_46*C7+ROcp7_76*S7
    ROcp7_57 = ROcp7_56*C7+ROcp7_86*S7
    ROcp7_67 = S6p7*C5
    ROcp7_77 = -(ROcp7_46*S7-ROcp7_76*C7)
    ROcp7_87 = -(ROcp7_56*S7-ROcp7_86*C7)
    ROcp7_97 = C6p7*C5
    ROcp7_18 = ROcp7_15*C8+ROcp7_47*S8
    ROcp7_28 = ROcp7_25*C8+ROcp7_57*S8
    ROcp7_38 = ROcp7_67*S8-S5*C8
    ROcp7_48 = -(ROcp7_15*S8-ROcp7_47*C8)
    ROcp7_58 = -(ROcp7_25*S8-ROcp7_57*C8)
    ROcp7_68 = ROcp7_67*C8+S5*S8
    RLcp7_17 = ROcp7_15*s.dpt[1,1]+ROcp7_46*s.dpt[2,1]
    RLcp7_27 = ROcp7_25*s.dpt[1,1]+ROcp7_56*s.dpt[2,1]
    RLcp7_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp7_17 = OMcp7_16+ROcp7_15*qd[7]
    OMcp7_27 = OMcp7_26+ROcp7_25*qd[7]
    OMcp7_37 = OMcp7_36-qd[7]*S5
    ORcp7_17 = OMcp7_26*RLcp7_37-OMcp7_36*RLcp7_27
    ORcp7_27 = -(OMcp7_16*RLcp7_37-OMcp7_36*RLcp7_17)
    ORcp7_37 = OMcp7_16*RLcp7_27-OMcp7_26*RLcp7_17
    OPcp7_17 = OPcp7_16+ROcp7_15*qdd[7]-qd[7]*(OMcp7_26*S5+OMcp7_36*ROcp7_25)
    OPcp7_27 = OPcp7_26+ROcp7_25*qdd[7]+qd[7]*(OMcp7_16*S5+OMcp7_36*ROcp7_15)
    OPcp7_37 = OPcp7_36-qdd[7]*S5+qd[7]*(OMcp7_16*ROcp7_25-OMcp7_26*ROcp7_15)
    RLcp7_18 = ROcp7_47*s.dpt[2,14]
    RLcp7_28 = ROcp7_57*s.dpt[2,14]
    RLcp7_38 = ROcp7_67*s.dpt[2,14]
    POcp7_18 = RLcp7_17+RLcp7_18+q[1]
    POcp7_28 = RLcp7_27+RLcp7_28+q[2]
    POcp7_38 = RLcp7_37+RLcp7_38+q[3]
    OMcp7_18 = OMcp7_17+ROcp7_77*qd[8]
    OMcp7_28 = OMcp7_27+ROcp7_87*qd[8]
    OMcp7_38 = OMcp7_37+ROcp7_97*qd[8]
    ORcp7_18 = OMcp7_27*RLcp7_38-OMcp7_37*RLcp7_28
    ORcp7_28 = -(OMcp7_17*RLcp7_38-OMcp7_37*RLcp7_18)
    ORcp7_38 = OMcp7_17*RLcp7_28-OMcp7_27*RLcp7_18
    VIcp7_18 = ORcp7_17+ORcp7_18+qd[1]
    VIcp7_28 = ORcp7_27+ORcp7_28+qd[2]
    VIcp7_38 = ORcp7_37+ORcp7_38+qd[3]
    OPcp7_18 = OPcp7_17+ROcp7_77*qdd[8]+qd[8]*(OMcp7_27*ROcp7_97-OMcp7_37*ROcp7_87)
    OPcp7_28 = OPcp7_27+ROcp7_87*qdd[8]-qd[8]*(OMcp7_17*ROcp7_97-OMcp7_37*ROcp7_77)
    OPcp7_38 = OPcp7_37+ROcp7_97*qdd[8]+qd[8]*(OMcp7_17*ROcp7_87-OMcp7_27*ROcp7_77)
    ACcp7_18 = qdd[1]+OMcp7_26*ORcp7_37+OMcp7_27*ORcp7_38-OMcp7_36*ORcp7_27-OMcp7_37*ORcp7_28+OPcp7_26*RLcp7_37+OPcp7_27*\
   RLcp7_38-OPcp7_36*RLcp7_27-OPcp7_37*RLcp7_28
    ACcp7_28 = qdd[2]-OMcp7_16*ORcp7_37-OMcp7_17*ORcp7_38+OMcp7_36*ORcp7_17+OMcp7_37*ORcp7_18-OPcp7_16*RLcp7_37-OPcp7_17*\
   RLcp7_38+OPcp7_36*RLcp7_17+OPcp7_37*RLcp7_18
    ACcp7_38 = qdd[3]+OMcp7_16*ORcp7_27+OMcp7_17*ORcp7_28-OMcp7_26*ORcp7_17-OMcp7_27*ORcp7_18+OPcp7_16*RLcp7_27+OPcp7_17*\
   RLcp7_28-OPcp7_26*RLcp7_17-OPcp7_27*RLcp7_18

# = = Block_1_0_0_8_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp7_18
    sens.P[2] = POcp7_28
    sens.P[3] = POcp7_38
    sens.R[1,1] = ROcp7_18
    sens.R[1,2] = ROcp7_28
    sens.R[1,3] = ROcp7_38
    sens.R[2,1] = ROcp7_48
    sens.R[2,2] = ROcp7_58
    sens.R[2,3] = ROcp7_68
    sens.R[3,1] = ROcp7_77
    sens.R[3,2] = ROcp7_87
    sens.R[3,3] = ROcp7_97
    sens.V[1] = VIcp7_18
    sens.V[2] = VIcp7_28
    sens.V[3] = VIcp7_38
    sens.OM[1] = OMcp7_18
    sens.OM[2] = OMcp7_28
    sens.OM[3] = OMcp7_38
    sens.A[1] = ACcp7_18
    sens.A[2] = ACcp7_28
    sens.A[3] = ACcp7_38
    sens.OMP[1] = OPcp7_18
    sens.OMP[2] = OPcp7_28
    sens.OMP[3] = OPcp7_38
 
# 
  elif(isens==9): 


# = = Block_1_0_0_9_0_1 = = 
 
# Sensor Kinematics 


    ROcp8_15 = C4*C5
    ROcp8_25 = S4*C5
    ROcp8_75 = C4*S5
    ROcp8_85 = S4*S5
    ROcp8_46 = ROcp8_75*S6-S4*C6
    ROcp8_56 = ROcp8_85*S6+C4*C6
    ROcp8_76 = ROcp8_75*C6+S4*S6
    ROcp8_86 = ROcp8_85*C6-C4*S6
    OMcp8_15 = -qd[5]*S4
    OMcp8_25 = qd[5]*C4
    OMcp8_16 = OMcp8_15+ROcp8_15*qd[6]
    OMcp8_26 = OMcp8_25+ROcp8_25*qd[6]
    OMcp8_36 = qd[4]-qd[6]*S5
    OPcp8_16 = ROcp8_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp8_25*S5+ROcp8_25*qd[4])
    OPcp8_26 = ROcp8_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp8_15*S5+ROcp8_15*qd[4])
    OPcp8_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_9_0_2 = = 
 
# Sensor Kinematics 


    ROcp8_47 = ROcp8_46*C7+ROcp8_76*S7
    ROcp8_57 = ROcp8_56*C7+ROcp8_86*S7
    ROcp8_67 = S6p7*C5
    ROcp8_77 = -(ROcp8_46*S7-ROcp8_76*C7)
    ROcp8_87 = -(ROcp8_56*S7-ROcp8_86*C7)
    ROcp8_97 = C6p7*C5
    ROcp8_18 = ROcp8_15*C8+ROcp8_47*S8
    ROcp8_28 = ROcp8_25*C8+ROcp8_57*S8
    ROcp8_38 = ROcp8_67*S8-S5*C8
    ROcp8_48 = -(ROcp8_15*S8-ROcp8_47*C8)
    ROcp8_58 = -(ROcp8_25*S8-ROcp8_57*C8)
    ROcp8_68 = ROcp8_67*C8+S5*S8
    ROcp8_49 = ROcp8_48*C9+ROcp8_77*S9
    ROcp8_59 = ROcp8_58*C9+ROcp8_87*S9
    ROcp8_69 = ROcp8_68*C9+ROcp8_97*S9
    ROcp8_79 = -(ROcp8_48*S9-ROcp8_77*C9)
    ROcp8_89 = -(ROcp8_58*S9-ROcp8_87*C9)
    ROcp8_99 = -(ROcp8_68*S9-ROcp8_97*C9)
    RLcp8_17 = ROcp8_15*s.dpt[1,1]+ROcp8_46*s.dpt[2,1]
    RLcp8_27 = ROcp8_25*s.dpt[1,1]+ROcp8_56*s.dpt[2,1]
    RLcp8_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp8_17 = OMcp8_16+ROcp8_15*qd[7]
    OMcp8_27 = OMcp8_26+ROcp8_25*qd[7]
    OMcp8_37 = OMcp8_36-qd[7]*S5
    ORcp8_17 = OMcp8_26*RLcp8_37-OMcp8_36*RLcp8_27
    ORcp8_27 = -(OMcp8_16*RLcp8_37-OMcp8_36*RLcp8_17)
    ORcp8_37 = OMcp8_16*RLcp8_27-OMcp8_26*RLcp8_17
    OPcp8_17 = OPcp8_16+ROcp8_15*qdd[7]-qd[7]*(OMcp8_26*S5+OMcp8_36*ROcp8_25)
    OPcp8_27 = OPcp8_26+ROcp8_25*qdd[7]+qd[7]*(OMcp8_16*S5+OMcp8_36*ROcp8_15)
    OPcp8_37 = OPcp8_36-qdd[7]*S5+qd[7]*(OMcp8_16*ROcp8_25-OMcp8_26*ROcp8_15)
    RLcp8_18 = ROcp8_47*s.dpt[2,14]
    RLcp8_28 = ROcp8_57*s.dpt[2,14]
    RLcp8_38 = ROcp8_67*s.dpt[2,14]
    POcp8_18 = RLcp8_17+RLcp8_18+q[1]
    POcp8_28 = RLcp8_27+RLcp8_28+q[2]
    POcp8_38 = RLcp8_37+RLcp8_38+q[3]
    OMcp8_18 = OMcp8_17+ROcp8_77*qd[8]
    OMcp8_28 = OMcp8_27+ROcp8_87*qd[8]
    OMcp8_38 = OMcp8_37+ROcp8_97*qd[8]
    ORcp8_18 = OMcp8_27*RLcp8_38-OMcp8_37*RLcp8_28
    ORcp8_28 = -(OMcp8_17*RLcp8_38-OMcp8_37*RLcp8_18)
    ORcp8_38 = OMcp8_17*RLcp8_28-OMcp8_27*RLcp8_18
    VIcp8_18 = ORcp8_17+ORcp8_18+qd[1]
    VIcp8_28 = ORcp8_27+ORcp8_28+qd[2]
    VIcp8_38 = ORcp8_37+ORcp8_38+qd[3]
    ACcp8_18 = qdd[1]+OMcp8_26*ORcp8_37+OMcp8_27*ORcp8_38-OMcp8_36*ORcp8_27-OMcp8_37*ORcp8_28+OPcp8_26*RLcp8_37+OPcp8_27*\
   RLcp8_38-OPcp8_36*RLcp8_27-OPcp8_37*RLcp8_28
    ACcp8_28 = qdd[2]-OMcp8_16*ORcp8_37-OMcp8_17*ORcp8_38+OMcp8_36*ORcp8_17+OMcp8_37*ORcp8_18-OPcp8_16*RLcp8_37-OPcp8_17*\
   RLcp8_38+OPcp8_36*RLcp8_17+OPcp8_37*RLcp8_18
    ACcp8_38 = qdd[3]+OMcp8_16*ORcp8_27+OMcp8_17*ORcp8_28-OMcp8_26*ORcp8_17-OMcp8_27*ORcp8_18+OPcp8_16*RLcp8_27+OPcp8_17*\
   RLcp8_28-OPcp8_26*RLcp8_17-OPcp8_27*RLcp8_18
    OMcp8_19 = OMcp8_18+ROcp8_18*qd[9]
    OMcp8_29 = OMcp8_28+ROcp8_28*qd[9]
    OMcp8_39 = OMcp8_38+ROcp8_38*qd[9]
    OPcp8_19 = OPcp8_17+ROcp8_18*qdd[9]+ROcp8_77*qdd[8]+qd[8]*(OMcp8_27*ROcp8_97-OMcp8_37*ROcp8_87)+qd[9]*(OMcp8_28*\
   ROcp8_38-OMcp8_38*ROcp8_28)
    OPcp8_29 = OPcp8_27+ROcp8_28*qdd[9]+ROcp8_87*qdd[8]-qd[8]*(OMcp8_17*ROcp8_97-OMcp8_37*ROcp8_77)-qd[9]*(OMcp8_18*\
   ROcp8_38-OMcp8_38*ROcp8_18)
    OPcp8_39 = OPcp8_37+ROcp8_38*qdd[9]+ROcp8_97*qdd[8]+qd[8]*(OMcp8_17*ROcp8_87-OMcp8_27*ROcp8_77)+qd[9]*(OMcp8_18*\
   ROcp8_28-OMcp8_28*ROcp8_18)

# = = Block_1_0_0_9_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp8_18
    sens.P[2] = POcp8_28
    sens.P[3] = POcp8_38
    sens.R[1,1] = ROcp8_18
    sens.R[1,2] = ROcp8_28
    sens.R[1,3] = ROcp8_38
    sens.R[2,1] = ROcp8_49
    sens.R[2,2] = ROcp8_59
    sens.R[2,3] = ROcp8_69
    sens.R[3,1] = ROcp8_79
    sens.R[3,2] = ROcp8_89
    sens.R[3,3] = ROcp8_99
    sens.V[1] = VIcp8_18
    sens.V[2] = VIcp8_28
    sens.V[3] = VIcp8_38
    sens.OM[1] = OMcp8_19
    sens.OM[2] = OMcp8_29
    sens.OM[3] = OMcp8_39
    sens.A[1] = ACcp8_18
    sens.A[2] = ACcp8_28
    sens.A[3] = ACcp8_38
    sens.OMP[1] = OPcp8_19
    sens.OMP[2] = OPcp8_29
    sens.OMP[3] = OPcp8_39
 
# 
  elif(isens==10): 


# = = Block_1_0_0_10_0_1 = = 
 
# Sensor Kinematics 


    ROcp9_15 = C4*C5
    ROcp9_25 = S4*C5
    ROcp9_75 = C4*S5
    ROcp9_85 = S4*S5
    ROcp9_46 = ROcp9_75*S6-S4*C6
    ROcp9_56 = ROcp9_85*S6+C4*C6
    ROcp9_76 = ROcp9_75*C6+S4*S6
    ROcp9_86 = ROcp9_85*C6-C4*S6
    OMcp9_15 = -qd[5]*S4
    OMcp9_25 = qd[5]*C4
    OMcp9_16 = OMcp9_15+ROcp9_15*qd[6]
    OMcp9_26 = OMcp9_25+ROcp9_25*qd[6]
    OMcp9_36 = qd[4]-qd[6]*S5
    OPcp9_16 = ROcp9_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp9_25*S5+ROcp9_25*qd[4])
    OPcp9_26 = ROcp9_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp9_15*S5+ROcp9_15*qd[4])
    OPcp9_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_10_0_2 = = 
 
# Sensor Kinematics 


    ROcp9_47 = ROcp9_46*C7+ROcp9_76*S7
    ROcp9_57 = ROcp9_56*C7+ROcp9_86*S7
    ROcp9_67 = S6p7*C5
    ROcp9_77 = -(ROcp9_46*S7-ROcp9_76*C7)
    ROcp9_87 = -(ROcp9_56*S7-ROcp9_86*C7)
    ROcp9_97 = C6p7*C5
    ROcp9_18 = ROcp9_15*C8+ROcp9_47*S8
    ROcp9_28 = ROcp9_25*C8+ROcp9_57*S8
    ROcp9_38 = ROcp9_67*S8-S5*C8
    ROcp9_48 = -(ROcp9_15*S8-ROcp9_47*C8)
    ROcp9_58 = -(ROcp9_25*S8-ROcp9_57*C8)
    ROcp9_68 = ROcp9_67*C8+S5*S8
    ROcp9_49 = ROcp9_48*C9+ROcp9_77*S9
    ROcp9_59 = ROcp9_58*C9+ROcp9_87*S9
    ROcp9_69 = ROcp9_68*C9+ROcp9_97*S9
    ROcp9_79 = -(ROcp9_48*S9-ROcp9_77*C9)
    ROcp9_89 = -(ROcp9_58*S9-ROcp9_87*C9)
    ROcp9_99 = -(ROcp9_68*S9-ROcp9_97*C9)
    ROcp9_110 = ROcp9_18*C10-ROcp9_79*S10
    ROcp9_210 = ROcp9_28*C10-ROcp9_89*S10
    ROcp9_310 = ROcp9_38*C10-ROcp9_99*S10
    ROcp9_710 = ROcp9_18*S10+ROcp9_79*C10
    ROcp9_810 = ROcp9_28*S10+ROcp9_89*C10
    ROcp9_910 = ROcp9_38*S10+ROcp9_99*C10
    RLcp9_17 = ROcp9_15*s.dpt[1,1]+ROcp9_46*s.dpt[2,1]
    RLcp9_27 = ROcp9_25*s.dpt[1,1]+ROcp9_56*s.dpt[2,1]
    RLcp9_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp9_17 = OMcp9_16+ROcp9_15*qd[7]
    OMcp9_27 = OMcp9_26+ROcp9_25*qd[7]
    OMcp9_37 = OMcp9_36-qd[7]*S5
    ORcp9_17 = OMcp9_26*RLcp9_37-OMcp9_36*RLcp9_27
    ORcp9_27 = -(OMcp9_16*RLcp9_37-OMcp9_36*RLcp9_17)
    ORcp9_37 = OMcp9_16*RLcp9_27-OMcp9_26*RLcp9_17
    OPcp9_17 = OPcp9_16+ROcp9_15*qdd[7]-qd[7]*(OMcp9_26*S5+OMcp9_36*ROcp9_25)
    OPcp9_27 = OPcp9_26+ROcp9_25*qdd[7]+qd[7]*(OMcp9_16*S5+OMcp9_36*ROcp9_15)
    OPcp9_37 = OPcp9_36-qdd[7]*S5+qd[7]*(OMcp9_16*ROcp9_25-OMcp9_26*ROcp9_15)
    RLcp9_18 = ROcp9_47*s.dpt[2,14]
    RLcp9_28 = ROcp9_57*s.dpt[2,14]
    RLcp9_38 = ROcp9_67*s.dpt[2,14]
    POcp9_18 = RLcp9_17+RLcp9_18+q[1]
    POcp9_28 = RLcp9_27+RLcp9_28+q[2]
    POcp9_38 = RLcp9_37+RLcp9_38+q[3]
    OMcp9_18 = OMcp9_17+ROcp9_77*qd[8]
    OMcp9_28 = OMcp9_27+ROcp9_87*qd[8]
    OMcp9_38 = OMcp9_37+ROcp9_97*qd[8]
    ORcp9_18 = OMcp9_27*RLcp9_38-OMcp9_37*RLcp9_28
    ORcp9_28 = -(OMcp9_17*RLcp9_38-OMcp9_37*RLcp9_18)
    ORcp9_38 = OMcp9_17*RLcp9_28-OMcp9_27*RLcp9_18
    VIcp9_18 = ORcp9_17+ORcp9_18+qd[1]
    VIcp9_28 = ORcp9_27+ORcp9_28+qd[2]
    VIcp9_38 = ORcp9_37+ORcp9_38+qd[3]
    ACcp9_18 = qdd[1]+OMcp9_26*ORcp9_37+OMcp9_27*ORcp9_38-OMcp9_36*ORcp9_27-OMcp9_37*ORcp9_28+OPcp9_26*RLcp9_37+OPcp9_27*\
   RLcp9_38-OPcp9_36*RLcp9_27-OPcp9_37*RLcp9_28
    ACcp9_28 = qdd[2]-OMcp9_16*ORcp9_37-OMcp9_17*ORcp9_38+OMcp9_36*ORcp9_17+OMcp9_37*ORcp9_18-OPcp9_16*RLcp9_37-OPcp9_17*\
   RLcp9_38+OPcp9_36*RLcp9_17+OPcp9_37*RLcp9_18
    ACcp9_38 = qdd[3]+OMcp9_16*ORcp9_27+OMcp9_17*ORcp9_28-OMcp9_26*ORcp9_17-OMcp9_27*ORcp9_18+OPcp9_16*RLcp9_27+OPcp9_17*\
   RLcp9_28-OPcp9_26*RLcp9_17-OPcp9_27*RLcp9_18
    OMcp9_19 = OMcp9_18+ROcp9_18*qd[9]
    OMcp9_29 = OMcp9_28+ROcp9_28*qd[9]
    OMcp9_39 = OMcp9_38+ROcp9_38*qd[9]
    OMcp9_110 = OMcp9_19+ROcp9_49*qd[10]
    OMcp9_210 = OMcp9_29+ROcp9_59*qd[10]
    OMcp9_310 = OMcp9_39+ROcp9_69*qd[10]
    OPcp9_110 = OPcp9_17+ROcp9_18*qdd[9]+ROcp9_49*qdd[10]+ROcp9_77*qdd[8]+qd[10]*(OMcp9_29*ROcp9_69-OMcp9_39*ROcp9_59)+\
   qd[8]*(OMcp9_27*ROcp9_97-OMcp9_37*ROcp9_87)+qd[9]*(OMcp9_28*ROcp9_38-OMcp9_38*ROcp9_28)
    OPcp9_210 = OPcp9_27+ROcp9_28*qdd[9]+ROcp9_59*qdd[10]+ROcp9_87*qdd[8]-qd[10]*(OMcp9_19*ROcp9_69-OMcp9_39*ROcp9_49)-\
   qd[8]*(OMcp9_17*ROcp9_97-OMcp9_37*ROcp9_77)-qd[9]*(OMcp9_18*ROcp9_38-OMcp9_38*ROcp9_18)
    OPcp9_310 = OPcp9_37+ROcp9_38*qdd[9]+ROcp9_69*qdd[10]+ROcp9_97*qdd[8]+qd[10]*(OMcp9_19*ROcp9_59-OMcp9_29*ROcp9_49)+\
   qd[8]*(OMcp9_17*ROcp9_87-OMcp9_27*ROcp9_77)+qd[9]*(OMcp9_18*ROcp9_28-OMcp9_28*ROcp9_18)

# = = Block_1_0_0_10_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp9_18
    sens.P[2] = POcp9_28
    sens.P[3] = POcp9_38
    sens.R[1,1] = ROcp9_110
    sens.R[1,2] = ROcp9_210
    sens.R[1,3] = ROcp9_310
    sens.R[2,1] = ROcp9_49
    sens.R[2,2] = ROcp9_59
    sens.R[2,3] = ROcp9_69
    sens.R[3,1] = ROcp9_710
    sens.R[3,2] = ROcp9_810
    sens.R[3,3] = ROcp9_910
    sens.V[1] = VIcp9_18
    sens.V[2] = VIcp9_28
    sens.V[3] = VIcp9_38
    sens.OM[1] = OMcp9_110
    sens.OM[2] = OMcp9_210
    sens.OM[3] = OMcp9_310
    sens.A[1] = ACcp9_18
    sens.A[2] = ACcp9_28
    sens.A[3] = ACcp9_38
    sens.OMP[1] = OPcp9_110
    sens.OMP[2] = OPcp9_210
    sens.OMP[3] = OPcp9_310
 
# 
  elif(isens==11): 


# = = Block_1_0_0_11_0_1 = = 
 
# Sensor Kinematics 


    ROcp10_15 = C4*C5
    ROcp10_25 = S4*C5
    ROcp10_75 = C4*S5
    ROcp10_85 = S4*S5
    ROcp10_46 = ROcp10_75*S6-S4*C6
    ROcp10_56 = ROcp10_85*S6+C4*C6
    ROcp10_76 = ROcp10_75*C6+S4*S6
    ROcp10_86 = ROcp10_85*C6-C4*S6
    OMcp10_15 = -qd[5]*S4
    OMcp10_25 = qd[5]*C4
    OMcp10_16 = OMcp10_15+ROcp10_15*qd[6]
    OMcp10_26 = OMcp10_25+ROcp10_25*qd[6]
    OMcp10_36 = qd[4]-qd[6]*S5
    OPcp10_16 = ROcp10_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp10_25*S5+ROcp10_25*qd[4])
    OPcp10_26 = ROcp10_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp10_15*S5+ROcp10_15*qd[4])
    OPcp10_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_11_0_2 = = 
 
# Sensor Kinematics 


    ROcp10_47 = ROcp10_46*C7+ROcp10_76*S7
    ROcp10_57 = ROcp10_56*C7+ROcp10_86*S7
    ROcp10_67 = S6p7*C5
    ROcp10_77 = -(ROcp10_46*S7-ROcp10_76*C7)
    ROcp10_87 = -(ROcp10_56*S7-ROcp10_86*C7)
    ROcp10_97 = C6p7*C5
    ROcp10_18 = ROcp10_15*C8+ROcp10_47*S8
    ROcp10_28 = ROcp10_25*C8+ROcp10_57*S8
    ROcp10_38 = ROcp10_67*S8-S5*C8
    ROcp10_48 = -(ROcp10_15*S8-ROcp10_47*C8)
    ROcp10_58 = -(ROcp10_25*S8-ROcp10_57*C8)
    ROcp10_68 = ROcp10_67*C8+S5*S8
    ROcp10_49 = ROcp10_48*C9+ROcp10_77*S9
    ROcp10_59 = ROcp10_58*C9+ROcp10_87*S9
    ROcp10_69 = ROcp10_68*C9+ROcp10_97*S9
    ROcp10_79 = -(ROcp10_48*S9-ROcp10_77*C9)
    ROcp10_89 = -(ROcp10_58*S9-ROcp10_87*C9)
    ROcp10_99 = -(ROcp10_68*S9-ROcp10_97*C9)
    ROcp10_110 = ROcp10_18*C10-ROcp10_79*S10
    ROcp10_210 = ROcp10_28*C10-ROcp10_89*S10
    ROcp10_310 = ROcp10_38*C10-ROcp10_99*S10
    ROcp10_710 = ROcp10_18*S10+ROcp10_79*C10
    ROcp10_810 = ROcp10_28*S10+ROcp10_89*C10
    ROcp10_910 = ROcp10_38*S10+ROcp10_99*C10
    RLcp10_17 = ROcp10_15*s.dpt[1,1]+ROcp10_46*s.dpt[2,1]
    RLcp10_27 = ROcp10_25*s.dpt[1,1]+ROcp10_56*s.dpt[2,1]
    RLcp10_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp10_17 = OMcp10_16+ROcp10_15*qd[7]
    OMcp10_27 = OMcp10_26+ROcp10_25*qd[7]
    OMcp10_37 = OMcp10_36-qd[7]*S5
    ORcp10_17 = OMcp10_26*RLcp10_37-OMcp10_36*RLcp10_27
    ORcp10_27 = -(OMcp10_16*RLcp10_37-OMcp10_36*RLcp10_17)
    ORcp10_37 = OMcp10_16*RLcp10_27-OMcp10_26*RLcp10_17
    OPcp10_17 = OPcp10_16+ROcp10_15*qdd[7]-qd[7]*(OMcp10_26*S5+OMcp10_36*ROcp10_25)
    OPcp10_27 = OPcp10_26+ROcp10_25*qdd[7]+qd[7]*(OMcp10_16*S5+OMcp10_36*ROcp10_15)
    OPcp10_37 = OPcp10_36-qdd[7]*S5+qd[7]*(OMcp10_16*ROcp10_25-OMcp10_26*ROcp10_15)
    RLcp10_18 = ROcp10_47*s.dpt[2,14]
    RLcp10_28 = ROcp10_57*s.dpt[2,14]
    RLcp10_38 = ROcp10_67*s.dpt[2,14]
    OMcp10_18 = OMcp10_17+ROcp10_77*qd[8]
    OMcp10_28 = OMcp10_27+ROcp10_87*qd[8]
    OMcp10_38 = OMcp10_37+ROcp10_97*qd[8]
    ORcp10_18 = OMcp10_27*RLcp10_38-OMcp10_37*RLcp10_28
    ORcp10_28 = -(OMcp10_17*RLcp10_38-OMcp10_37*RLcp10_18)
    ORcp10_38 = OMcp10_17*RLcp10_28-OMcp10_27*RLcp10_18
    OMcp10_19 = OMcp10_18+ROcp10_18*qd[9]
    OMcp10_29 = OMcp10_28+ROcp10_28*qd[9]
    OMcp10_39 = OMcp10_38+ROcp10_38*qd[9]
    OMcp10_110 = OMcp10_19+ROcp10_49*qd[10]
    OMcp10_210 = OMcp10_29+ROcp10_59*qd[10]
    OMcp10_310 = OMcp10_39+ROcp10_69*qd[10]
    OPcp10_110 = OPcp10_17+ROcp10_18*qdd[9]+ROcp10_49*qdd[10]+ROcp10_77*qdd[8]+qd[10]*(OMcp10_29*ROcp10_69-OMcp10_39*\
   ROcp10_59)+qd[8]*(OMcp10_27*ROcp10_97-OMcp10_37*ROcp10_87)+qd[9]*(OMcp10_28*ROcp10_38-OMcp10_38*ROcp10_28)
    OPcp10_210 = OPcp10_27+ROcp10_28*qdd[9]+ROcp10_59*qdd[10]+ROcp10_87*qdd[8]-qd[10]*(OMcp10_19*ROcp10_69-OMcp10_39*\
   ROcp10_49)-qd[8]*(OMcp10_17*ROcp10_97-OMcp10_37*ROcp10_77)-qd[9]*(OMcp10_18*ROcp10_38-OMcp10_38*ROcp10_18)
    OPcp10_310 = OPcp10_37+ROcp10_38*qdd[9]+ROcp10_69*qdd[10]+ROcp10_97*qdd[8]+qd[10]*(OMcp10_19*ROcp10_59-OMcp10_29*\
   ROcp10_49)+qd[8]*(OMcp10_17*ROcp10_87-OMcp10_27*ROcp10_77)+qd[9]*(OMcp10_18*ROcp10_28-OMcp10_28*ROcp10_18)

# = = Block_1_0_0_11_0_3 = = 
 
# Sensor Kinematics 


    ROcp10_411 = ROcp10_49*C11+ROcp10_710*S11
    ROcp10_511 = ROcp10_59*C11+ROcp10_810*S11
    ROcp10_611 = ROcp10_69*C11+ROcp10_910*S11
    ROcp10_711 = -(ROcp10_49*S11-ROcp10_710*C11)
    ROcp10_811 = -(ROcp10_59*S11-ROcp10_810*C11)
    ROcp10_911 = -(ROcp10_69*S11-ROcp10_910*C11)
    RLcp10_111 = ROcp10_710*s.dpt[3,15]
    RLcp10_211 = ROcp10_810*s.dpt[3,15]
    RLcp10_311 = ROcp10_910*s.dpt[3,15]
    POcp10_111 = RLcp10_111+RLcp10_17+RLcp10_18+q[1]
    POcp10_211 = RLcp10_211+RLcp10_27+RLcp10_28+q[2]
    POcp10_311 = RLcp10_311+RLcp10_37+RLcp10_38+q[3]
    OMcp10_111 = OMcp10_110+ROcp10_110*qd[11]
    OMcp10_211 = OMcp10_210+ROcp10_210*qd[11]
    OMcp10_311 = OMcp10_310+ROcp10_310*qd[11]
    ORcp10_111 = OMcp10_210*RLcp10_311-OMcp10_310*RLcp10_211
    ORcp10_211 = -(OMcp10_110*RLcp10_311-OMcp10_310*RLcp10_111)
    ORcp10_311 = OMcp10_110*RLcp10_211-OMcp10_210*RLcp10_111
    VIcp10_111 = ORcp10_111+ORcp10_17+ORcp10_18+qd[1]
    VIcp10_211 = ORcp10_211+ORcp10_27+ORcp10_28+qd[2]
    VIcp10_311 = ORcp10_311+ORcp10_37+ORcp10_38+qd[3]
    OPcp10_111 = OPcp10_110+ROcp10_110*qdd[11]+qd[11]*(OMcp10_210*ROcp10_310-OMcp10_310*ROcp10_210)
    OPcp10_211 = OPcp10_210+ROcp10_210*qdd[11]-qd[11]*(OMcp10_110*ROcp10_310-OMcp10_310*ROcp10_110)
    OPcp10_311 = OPcp10_310+ROcp10_310*qdd[11]+qd[11]*(OMcp10_110*ROcp10_210-OMcp10_210*ROcp10_110)
    ACcp10_111 = qdd[1]+OMcp10_210*ORcp10_311+OMcp10_26*ORcp10_37+OMcp10_27*ORcp10_38-OMcp10_310*ORcp10_211-OMcp10_36*\
   ORcp10_27-OMcp10_37*ORcp10_28+OPcp10_210*RLcp10_311+OPcp10_26*RLcp10_37+OPcp10_27*RLcp10_38-OPcp10_310*RLcp10_211-OPcp10_36*\
   RLcp10_27-OPcp10_37*RLcp10_28
    ACcp10_211 = qdd[2]-OMcp10_110*ORcp10_311-OMcp10_16*ORcp10_37-OMcp10_17*ORcp10_38+OMcp10_310*ORcp10_111+OMcp10_36*\
   ORcp10_17+OMcp10_37*ORcp10_18-OPcp10_110*RLcp10_311-OPcp10_16*RLcp10_37-OPcp10_17*RLcp10_38+OPcp10_310*RLcp10_111+OPcp10_36*\
   RLcp10_17+OPcp10_37*RLcp10_18
    ACcp10_311 = qdd[3]+OMcp10_110*ORcp10_211+OMcp10_16*ORcp10_27+OMcp10_17*ORcp10_28-OMcp10_210*ORcp10_111-OMcp10_26*\
   ORcp10_17-OMcp10_27*ORcp10_18+OPcp10_110*RLcp10_211+OPcp10_16*RLcp10_27+OPcp10_17*RLcp10_28-OPcp10_210*RLcp10_111-OPcp10_26*\
   RLcp10_17-OPcp10_27*RLcp10_18

# = = Block_1_0_0_11_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp10_111
    sens.P[2] = POcp10_211
    sens.P[3] = POcp10_311
    sens.R[1,1] = ROcp10_110
    sens.R[1,2] = ROcp10_210
    sens.R[1,3] = ROcp10_310
    sens.R[2,1] = ROcp10_411
    sens.R[2,2] = ROcp10_511
    sens.R[2,3] = ROcp10_611
    sens.R[3,1] = ROcp10_711
    sens.R[3,2] = ROcp10_811
    sens.R[3,3] = ROcp10_911
    sens.V[1] = VIcp10_111
    sens.V[2] = VIcp10_211
    sens.V[3] = VIcp10_311
    sens.OM[1] = OMcp10_111
    sens.OM[2] = OMcp10_211
    sens.OM[3] = OMcp10_311
    sens.A[1] = ACcp10_111
    sens.A[2] = ACcp10_211
    sens.A[3] = ACcp10_311
    sens.OMP[1] = OPcp10_111
    sens.OMP[2] = OPcp10_211
    sens.OMP[3] = OPcp10_311
 
# 
  elif(isens==12): 


# = = Block_1_0_0_12_0_1 = = 
 
# Sensor Kinematics 


    ROcp11_15 = C4*C5
    ROcp11_25 = S4*C5
    ROcp11_75 = C4*S5
    ROcp11_85 = S4*S5
    ROcp11_46 = ROcp11_75*S6-S4*C6
    ROcp11_56 = ROcp11_85*S6+C4*C6
    ROcp11_76 = ROcp11_75*C6+S4*S6
    ROcp11_86 = ROcp11_85*C6-C4*S6
    OMcp11_15 = -qd[5]*S4
    OMcp11_25 = qd[5]*C4
    OMcp11_16 = OMcp11_15+ROcp11_15*qd[6]
    OMcp11_26 = OMcp11_25+ROcp11_25*qd[6]
    OMcp11_36 = qd[4]-qd[6]*S5
    OPcp11_16 = ROcp11_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp11_25*S5+ROcp11_25*qd[4])
    OPcp11_26 = ROcp11_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp11_15*S5+ROcp11_15*qd[4])
    OPcp11_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_12_0_2 = = 
 
# Sensor Kinematics 


    ROcp11_47 = ROcp11_46*C7+ROcp11_76*S7
    ROcp11_57 = ROcp11_56*C7+ROcp11_86*S7
    ROcp11_67 = S6p7*C5
    ROcp11_77 = -(ROcp11_46*S7-ROcp11_76*C7)
    ROcp11_87 = -(ROcp11_56*S7-ROcp11_86*C7)
    ROcp11_97 = C6p7*C5
    ROcp11_18 = ROcp11_15*C8+ROcp11_47*S8
    ROcp11_28 = ROcp11_25*C8+ROcp11_57*S8
    ROcp11_38 = ROcp11_67*S8-S5*C8
    ROcp11_48 = -(ROcp11_15*S8-ROcp11_47*C8)
    ROcp11_58 = -(ROcp11_25*S8-ROcp11_57*C8)
    ROcp11_68 = ROcp11_67*C8+S5*S8
    ROcp11_49 = ROcp11_48*C9+ROcp11_77*S9
    ROcp11_59 = ROcp11_58*C9+ROcp11_87*S9
    ROcp11_69 = ROcp11_68*C9+ROcp11_97*S9
    ROcp11_79 = -(ROcp11_48*S9-ROcp11_77*C9)
    ROcp11_89 = -(ROcp11_58*S9-ROcp11_87*C9)
    ROcp11_99 = -(ROcp11_68*S9-ROcp11_97*C9)
    ROcp11_110 = ROcp11_18*C10-ROcp11_79*S10
    ROcp11_210 = ROcp11_28*C10-ROcp11_89*S10
    ROcp11_310 = ROcp11_38*C10-ROcp11_99*S10
    ROcp11_710 = ROcp11_18*S10+ROcp11_79*C10
    ROcp11_810 = ROcp11_28*S10+ROcp11_89*C10
    ROcp11_910 = ROcp11_38*S10+ROcp11_99*C10
    RLcp11_17 = ROcp11_15*s.dpt[1,1]+ROcp11_46*s.dpt[2,1]
    RLcp11_27 = ROcp11_25*s.dpt[1,1]+ROcp11_56*s.dpt[2,1]
    RLcp11_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp11_17 = OMcp11_16+ROcp11_15*qd[7]
    OMcp11_27 = OMcp11_26+ROcp11_25*qd[7]
    OMcp11_37 = OMcp11_36-qd[7]*S5
    ORcp11_17 = OMcp11_26*RLcp11_37-OMcp11_36*RLcp11_27
    ORcp11_27 = -(OMcp11_16*RLcp11_37-OMcp11_36*RLcp11_17)
    ORcp11_37 = OMcp11_16*RLcp11_27-OMcp11_26*RLcp11_17
    OPcp11_17 = OPcp11_16+ROcp11_15*qdd[7]-qd[7]*(OMcp11_26*S5+OMcp11_36*ROcp11_25)
    OPcp11_27 = OPcp11_26+ROcp11_25*qdd[7]+qd[7]*(OMcp11_16*S5+OMcp11_36*ROcp11_15)
    OPcp11_37 = OPcp11_36-qdd[7]*S5+qd[7]*(OMcp11_16*ROcp11_25-OMcp11_26*ROcp11_15)
    RLcp11_18 = ROcp11_47*s.dpt[2,14]
    RLcp11_28 = ROcp11_57*s.dpt[2,14]
    RLcp11_38 = ROcp11_67*s.dpt[2,14]
    OMcp11_18 = OMcp11_17+ROcp11_77*qd[8]
    OMcp11_28 = OMcp11_27+ROcp11_87*qd[8]
    OMcp11_38 = OMcp11_37+ROcp11_97*qd[8]
    ORcp11_18 = OMcp11_27*RLcp11_38-OMcp11_37*RLcp11_28
    ORcp11_28 = -(OMcp11_17*RLcp11_38-OMcp11_37*RLcp11_18)
    ORcp11_38 = OMcp11_17*RLcp11_28-OMcp11_27*RLcp11_18
    OMcp11_19 = OMcp11_18+ROcp11_18*qd[9]
    OMcp11_29 = OMcp11_28+ROcp11_28*qd[9]
    OMcp11_39 = OMcp11_38+ROcp11_38*qd[9]
    OMcp11_110 = OMcp11_19+ROcp11_49*qd[10]
    OMcp11_210 = OMcp11_29+ROcp11_59*qd[10]
    OMcp11_310 = OMcp11_39+ROcp11_69*qd[10]
    OPcp11_110 = OPcp11_17+ROcp11_18*qdd[9]+ROcp11_49*qdd[10]+ROcp11_77*qdd[8]+qd[10]*(OMcp11_29*ROcp11_69-OMcp11_39*\
   ROcp11_59)+qd[8]*(OMcp11_27*ROcp11_97-OMcp11_37*ROcp11_87)+qd[9]*(OMcp11_28*ROcp11_38-OMcp11_38*ROcp11_28)
    OPcp11_210 = OPcp11_27+ROcp11_28*qdd[9]+ROcp11_59*qdd[10]+ROcp11_87*qdd[8]-qd[10]*(OMcp11_19*ROcp11_69-OMcp11_39*\
   ROcp11_49)-qd[8]*(OMcp11_17*ROcp11_97-OMcp11_37*ROcp11_77)-qd[9]*(OMcp11_18*ROcp11_38-OMcp11_38*ROcp11_18)
    OPcp11_310 = OPcp11_37+ROcp11_38*qdd[9]+ROcp11_69*qdd[10]+ROcp11_97*qdd[8]+qd[10]*(OMcp11_19*ROcp11_59-OMcp11_29*\
   ROcp11_49)+qd[8]*(OMcp11_17*ROcp11_87-OMcp11_27*ROcp11_77)+qd[9]*(OMcp11_18*ROcp11_28-OMcp11_28*ROcp11_18)

# = = Block_1_0_0_12_0_3 = = 
 
# Sensor Kinematics 


    ROcp11_411 = ROcp11_49*C11+ROcp11_710*S11
    ROcp11_511 = ROcp11_59*C11+ROcp11_810*S11
    ROcp11_611 = ROcp11_69*C11+ROcp11_910*S11
    ROcp11_711 = -(ROcp11_49*S11-ROcp11_710*C11)
    ROcp11_811 = -(ROcp11_59*S11-ROcp11_810*C11)
    ROcp11_911 = -(ROcp11_69*S11-ROcp11_910*C11)
    RLcp11_111 = ROcp11_710*s.dpt[3,15]
    RLcp11_211 = ROcp11_810*s.dpt[3,15]
    RLcp11_311 = ROcp11_910*s.dpt[3,15]
    OMcp11_111 = OMcp11_110+ROcp11_110*qd[11]
    OMcp11_211 = OMcp11_210+ROcp11_210*qd[11]
    OMcp11_311 = OMcp11_310+ROcp11_310*qd[11]
    ORcp11_111 = OMcp11_210*RLcp11_311-OMcp11_310*RLcp11_211
    ORcp11_211 = -(OMcp11_110*RLcp11_311-OMcp11_310*RLcp11_111)
    ORcp11_311 = OMcp11_110*RLcp11_211-OMcp11_210*RLcp11_111
    OPcp11_111 = OPcp11_110+ROcp11_110*qdd[11]+qd[11]*(OMcp11_210*ROcp11_310-OMcp11_310*ROcp11_210)
    OPcp11_211 = OPcp11_210+ROcp11_210*qdd[11]-qd[11]*(OMcp11_110*ROcp11_310-OMcp11_310*ROcp11_110)
    OPcp11_311 = OPcp11_310+ROcp11_310*qdd[11]+qd[11]*(OMcp11_110*ROcp11_210-OMcp11_210*ROcp11_110)
    RLcp11_112 = ROcp11_711*q[12]
    RLcp11_212 = ROcp11_811*q[12]
    RLcp11_312 = ROcp11_911*q[12]
    POcp11_112 = RLcp11_111+RLcp11_112+RLcp11_17+RLcp11_18+q[1]
    POcp11_212 = RLcp11_211+RLcp11_212+RLcp11_27+RLcp11_28+q[2]
    POcp11_312 = RLcp11_311+RLcp11_312+RLcp11_37+RLcp11_38+q[3]
    ORcp11_112 = OMcp11_211*RLcp11_312-OMcp11_311*RLcp11_212
    ORcp11_212 = -(OMcp11_111*RLcp11_312-OMcp11_311*RLcp11_112)
    ORcp11_312 = OMcp11_111*RLcp11_212-OMcp11_211*RLcp11_112
    VIcp11_112 = ORcp11_111+ORcp11_112+ORcp11_17+ORcp11_18+qd[1]+ROcp11_711*qd[12]
    VIcp11_212 = ORcp11_211+ORcp11_212+ORcp11_27+ORcp11_28+qd[2]+ROcp11_811*qd[12]
    VIcp11_312 = ORcp11_311+ORcp11_312+ORcp11_37+ORcp11_38+qd[3]+ROcp11_911*qd[12]
    ACcp11_112 = qdd[1]+OMcp11_210*ORcp11_311+OMcp11_211*ORcp11_312+OMcp11_26*ORcp11_37+OMcp11_27*ORcp11_38-OMcp11_310*\
   ORcp11_211-OMcp11_311*ORcp11_212-OMcp11_36*ORcp11_27-OMcp11_37*ORcp11_28+OPcp11_210*RLcp11_311+OPcp11_211*RLcp11_312+\
   OPcp11_26*RLcp11_37+OPcp11_27*RLcp11_38-OPcp11_310*RLcp11_211-OPcp11_311*RLcp11_212-OPcp11_36*RLcp11_27-OPcp11_37*RLcp11_28+\
   ROcp11_711*qdd[12]+(2.0)*qd[12]*(OMcp11_211*ROcp11_911-OMcp11_311*ROcp11_811)
    ACcp11_212 = qdd[2]-OMcp11_110*ORcp11_311-OMcp11_111*ORcp11_312-OMcp11_16*ORcp11_37-OMcp11_17*ORcp11_38+OMcp11_310*\
   ORcp11_111+OMcp11_311*ORcp11_112+OMcp11_36*ORcp11_17+OMcp11_37*ORcp11_18-OPcp11_110*RLcp11_311-OPcp11_111*RLcp11_312-\
   OPcp11_16*RLcp11_37-OPcp11_17*RLcp11_38+OPcp11_310*RLcp11_111+OPcp11_311*RLcp11_112+OPcp11_36*RLcp11_17+OPcp11_37*RLcp11_18+\
   ROcp11_811*qdd[12]-(2.0)*qd[12]*(OMcp11_111*ROcp11_911-OMcp11_311*ROcp11_711)
    ACcp11_312 = qdd[3]+OMcp11_110*ORcp11_211+OMcp11_111*ORcp11_212+OMcp11_16*ORcp11_27+OMcp11_17*ORcp11_28-OMcp11_210*\
   ORcp11_111-OMcp11_211*ORcp11_112-OMcp11_26*ORcp11_17-OMcp11_27*ORcp11_18+OPcp11_110*RLcp11_211+OPcp11_111*RLcp11_212+\
   OPcp11_16*RLcp11_27+OPcp11_17*RLcp11_28-OPcp11_210*RLcp11_111-OPcp11_211*RLcp11_112-OPcp11_26*RLcp11_17-OPcp11_27*RLcp11_18+\
   ROcp11_911*qdd[12]+(2.0)*qd[12]*(OMcp11_111*ROcp11_811-OMcp11_211*ROcp11_711)

# = = Block_1_0_0_12_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp11_112
    sens.P[2] = POcp11_212
    sens.P[3] = POcp11_312
    sens.R[1,1] = ROcp11_110
    sens.R[1,2] = ROcp11_210
    sens.R[1,3] = ROcp11_310
    sens.R[2,1] = ROcp11_411
    sens.R[2,2] = ROcp11_511
    sens.R[2,3] = ROcp11_611
    sens.R[3,1] = ROcp11_711
    sens.R[3,2] = ROcp11_811
    sens.R[3,3] = ROcp11_911
    sens.V[1] = VIcp11_112
    sens.V[2] = VIcp11_212
    sens.V[3] = VIcp11_312
    sens.OM[1] = OMcp11_111
    sens.OM[2] = OMcp11_211
    sens.OM[3] = OMcp11_311
    sens.A[1] = ACcp11_112
    sens.A[2] = ACcp11_212
    sens.A[3] = ACcp11_312
    sens.OMP[1] = OPcp11_111
    sens.OMP[2] = OPcp11_211
    sens.OMP[3] = OPcp11_311
 
# 
  elif(isens==13): 


# = = Block_1_0_0_13_0_1 = = 
 
# Sensor Kinematics 


    ROcp12_15 = C4*C5
    ROcp12_25 = S4*C5
    ROcp12_75 = C4*S5
    ROcp12_85 = S4*S5
    ROcp12_46 = ROcp12_75*S6-S4*C6
    ROcp12_56 = ROcp12_85*S6+C4*C6
    ROcp12_76 = ROcp12_75*C6+S4*S6
    ROcp12_86 = ROcp12_85*C6-C4*S6
    OMcp12_15 = -qd[5]*S4
    OMcp12_25 = qd[5]*C4
    OMcp12_16 = OMcp12_15+ROcp12_15*qd[6]
    OMcp12_26 = OMcp12_25+ROcp12_25*qd[6]
    OMcp12_36 = qd[4]-qd[6]*S5
    OPcp12_16 = ROcp12_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp12_25*S5+ROcp12_25*qd[4])
    OPcp12_26 = ROcp12_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp12_15*S5+ROcp12_15*qd[4])
    OPcp12_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_13_0_2 = = 
 
# Sensor Kinematics 


    ROcp12_47 = ROcp12_46*C7+ROcp12_76*S7
    ROcp12_57 = ROcp12_56*C7+ROcp12_86*S7
    ROcp12_67 = S6p7*C5
    ROcp12_77 = -(ROcp12_46*S7-ROcp12_76*C7)
    ROcp12_87 = -(ROcp12_56*S7-ROcp12_86*C7)
    ROcp12_97 = C6p7*C5
    ROcp12_18 = ROcp12_15*C8+ROcp12_47*S8
    ROcp12_28 = ROcp12_25*C8+ROcp12_57*S8
    ROcp12_38 = ROcp12_67*S8-S5*C8
    ROcp12_48 = -(ROcp12_15*S8-ROcp12_47*C8)
    ROcp12_58 = -(ROcp12_25*S8-ROcp12_57*C8)
    ROcp12_68 = ROcp12_67*C8+S5*S8
    ROcp12_49 = ROcp12_48*C9+ROcp12_77*S9
    ROcp12_59 = ROcp12_58*C9+ROcp12_87*S9
    ROcp12_69 = ROcp12_68*C9+ROcp12_97*S9
    ROcp12_79 = -(ROcp12_48*S9-ROcp12_77*C9)
    ROcp12_89 = -(ROcp12_58*S9-ROcp12_87*C9)
    ROcp12_99 = -(ROcp12_68*S9-ROcp12_97*C9)
    ROcp12_110 = ROcp12_18*C10-ROcp12_79*S10
    ROcp12_210 = ROcp12_28*C10-ROcp12_89*S10
    ROcp12_310 = ROcp12_38*C10-ROcp12_99*S10
    ROcp12_710 = ROcp12_18*S10+ROcp12_79*C10
    ROcp12_810 = ROcp12_28*S10+ROcp12_89*C10
    ROcp12_910 = ROcp12_38*S10+ROcp12_99*C10
    RLcp12_17 = ROcp12_15*s.dpt[1,1]+ROcp12_46*s.dpt[2,1]
    RLcp12_27 = ROcp12_25*s.dpt[1,1]+ROcp12_56*s.dpt[2,1]
    RLcp12_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp12_17 = OMcp12_16+ROcp12_15*qd[7]
    OMcp12_27 = OMcp12_26+ROcp12_25*qd[7]
    OMcp12_37 = OMcp12_36-qd[7]*S5
    ORcp12_17 = OMcp12_26*RLcp12_37-OMcp12_36*RLcp12_27
    ORcp12_27 = -(OMcp12_16*RLcp12_37-OMcp12_36*RLcp12_17)
    ORcp12_37 = OMcp12_16*RLcp12_27-OMcp12_26*RLcp12_17
    OPcp12_17 = OPcp12_16+ROcp12_15*qdd[7]-qd[7]*(OMcp12_26*S5+OMcp12_36*ROcp12_25)
    OPcp12_27 = OPcp12_26+ROcp12_25*qdd[7]+qd[7]*(OMcp12_16*S5+OMcp12_36*ROcp12_15)
    OPcp12_37 = OPcp12_36-qdd[7]*S5+qd[7]*(OMcp12_16*ROcp12_25-OMcp12_26*ROcp12_15)
    RLcp12_18 = ROcp12_47*s.dpt[2,14]
    RLcp12_28 = ROcp12_57*s.dpt[2,14]
    RLcp12_38 = ROcp12_67*s.dpt[2,14]
    OMcp12_18 = OMcp12_17+ROcp12_77*qd[8]
    OMcp12_28 = OMcp12_27+ROcp12_87*qd[8]
    OMcp12_38 = OMcp12_37+ROcp12_97*qd[8]
    ORcp12_18 = OMcp12_27*RLcp12_38-OMcp12_37*RLcp12_28
    ORcp12_28 = -(OMcp12_17*RLcp12_38-OMcp12_37*RLcp12_18)
    ORcp12_38 = OMcp12_17*RLcp12_28-OMcp12_27*RLcp12_18
    OMcp12_19 = OMcp12_18+ROcp12_18*qd[9]
    OMcp12_29 = OMcp12_28+ROcp12_28*qd[9]
    OMcp12_39 = OMcp12_38+ROcp12_38*qd[9]
    OMcp12_110 = OMcp12_19+ROcp12_49*qd[10]
    OMcp12_210 = OMcp12_29+ROcp12_59*qd[10]
    OMcp12_310 = OMcp12_39+ROcp12_69*qd[10]
    OPcp12_110 = OPcp12_17+ROcp12_18*qdd[9]+ROcp12_49*qdd[10]+ROcp12_77*qdd[8]+qd[10]*(OMcp12_29*ROcp12_69-OMcp12_39*\
   ROcp12_59)+qd[8]*(OMcp12_27*ROcp12_97-OMcp12_37*ROcp12_87)+qd[9]*(OMcp12_28*ROcp12_38-OMcp12_38*ROcp12_28)
    OPcp12_210 = OPcp12_27+ROcp12_28*qdd[9]+ROcp12_59*qdd[10]+ROcp12_87*qdd[8]-qd[10]*(OMcp12_19*ROcp12_69-OMcp12_39*\
   ROcp12_49)-qd[8]*(OMcp12_17*ROcp12_97-OMcp12_37*ROcp12_77)-qd[9]*(OMcp12_18*ROcp12_38-OMcp12_38*ROcp12_18)
    OPcp12_310 = OPcp12_37+ROcp12_38*qdd[9]+ROcp12_69*qdd[10]+ROcp12_97*qdd[8]+qd[10]*(OMcp12_19*ROcp12_59-OMcp12_29*\
   ROcp12_49)+qd[8]*(OMcp12_17*ROcp12_87-OMcp12_27*ROcp12_77)+qd[9]*(OMcp12_18*ROcp12_28-OMcp12_28*ROcp12_18)

# = = Block_1_0_0_13_0_4 = = 
 
# Sensor Kinematics 


    ROcp12_413 = ROcp12_49*C13+ROcp12_710*S13
    ROcp12_513 = ROcp12_59*C13+ROcp12_810*S13
    ROcp12_613 = ROcp12_69*C13+ROcp12_910*S13
    ROcp12_713 = -(ROcp12_49*S13-ROcp12_710*C13)
    ROcp12_813 = -(ROcp12_59*S13-ROcp12_810*C13)
    ROcp12_913 = -(ROcp12_69*S13-ROcp12_910*C13)
    RLcp12_113 = ROcp12_710*s.dpt[3,16]
    RLcp12_213 = ROcp12_810*s.dpt[3,16]
    RLcp12_313 = ROcp12_910*s.dpt[3,16]
    POcp12_113 = RLcp12_113+RLcp12_17+RLcp12_18+q[1]
    POcp12_213 = RLcp12_213+RLcp12_27+RLcp12_28+q[2]
    POcp12_313 = RLcp12_313+RLcp12_37+RLcp12_38+q[3]
    OMcp12_113 = OMcp12_110+ROcp12_110*qd[13]
    OMcp12_213 = OMcp12_210+ROcp12_210*qd[13]
    OMcp12_313 = OMcp12_310+ROcp12_310*qd[13]
    ORcp12_113 = OMcp12_210*RLcp12_313-OMcp12_310*RLcp12_213
    ORcp12_213 = -(OMcp12_110*RLcp12_313-OMcp12_310*RLcp12_113)
    ORcp12_313 = OMcp12_110*RLcp12_213-OMcp12_210*RLcp12_113
    VIcp12_113 = ORcp12_113+ORcp12_17+ORcp12_18+qd[1]
    VIcp12_213 = ORcp12_213+ORcp12_27+ORcp12_28+qd[2]
    VIcp12_313 = ORcp12_313+ORcp12_37+ORcp12_38+qd[3]
    OPcp12_113 = OPcp12_110+ROcp12_110*qdd[13]+qd[13]*(OMcp12_210*ROcp12_310-OMcp12_310*ROcp12_210)
    OPcp12_213 = OPcp12_210+ROcp12_210*qdd[13]-qd[13]*(OMcp12_110*ROcp12_310-OMcp12_310*ROcp12_110)
    OPcp12_313 = OPcp12_310+ROcp12_310*qdd[13]+qd[13]*(OMcp12_110*ROcp12_210-OMcp12_210*ROcp12_110)
    ACcp12_113 = qdd[1]+OMcp12_210*ORcp12_313+OMcp12_26*ORcp12_37+OMcp12_27*ORcp12_38-OMcp12_310*ORcp12_213-OMcp12_36*\
   ORcp12_27-OMcp12_37*ORcp12_28+OPcp12_210*RLcp12_313+OPcp12_26*RLcp12_37+OPcp12_27*RLcp12_38-OPcp12_310*RLcp12_213-OPcp12_36*\
   RLcp12_27-OPcp12_37*RLcp12_28
    ACcp12_213 = qdd[2]-OMcp12_110*ORcp12_313-OMcp12_16*ORcp12_37-OMcp12_17*ORcp12_38+OMcp12_310*ORcp12_113+OMcp12_36*\
   ORcp12_17+OMcp12_37*ORcp12_18-OPcp12_110*RLcp12_313-OPcp12_16*RLcp12_37-OPcp12_17*RLcp12_38+OPcp12_310*RLcp12_113+OPcp12_36*\
   RLcp12_17+OPcp12_37*RLcp12_18
    ACcp12_313 = qdd[3]+OMcp12_110*ORcp12_213+OMcp12_16*ORcp12_27+OMcp12_17*ORcp12_28-OMcp12_210*ORcp12_113-OMcp12_26*\
   ORcp12_17-OMcp12_27*ORcp12_18+OPcp12_110*RLcp12_213+OPcp12_16*RLcp12_27+OPcp12_17*RLcp12_28-OPcp12_210*RLcp12_113-OPcp12_26*\
   RLcp12_17-OPcp12_27*RLcp12_18

# = = Block_1_0_0_13_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp12_113
    sens.P[2] = POcp12_213
    sens.P[3] = POcp12_313
    sens.R[1,1] = ROcp12_110
    sens.R[1,2] = ROcp12_210
    sens.R[1,3] = ROcp12_310
    sens.R[2,1] = ROcp12_413
    sens.R[2,2] = ROcp12_513
    sens.R[2,3] = ROcp12_613
    sens.R[3,1] = ROcp12_713
    sens.R[3,2] = ROcp12_813
    sens.R[3,3] = ROcp12_913
    sens.V[1] = VIcp12_113
    sens.V[2] = VIcp12_213
    sens.V[3] = VIcp12_313
    sens.OM[1] = OMcp12_113
    sens.OM[2] = OMcp12_213
    sens.OM[3] = OMcp12_313
    sens.A[1] = ACcp12_113
    sens.A[2] = ACcp12_213
    sens.A[3] = ACcp12_313
    sens.OMP[1] = OPcp12_113
    sens.OMP[2] = OPcp12_213
    sens.OMP[3] = OPcp12_313
 
# 
  elif(isens==14): 


# = = Block_1_0_0_14_0_1 = = 
 
# Sensor Kinematics 


    ROcp13_15 = C4*C5
    ROcp13_25 = S4*C5
    ROcp13_75 = C4*S5
    ROcp13_85 = S4*S5
    ROcp13_46 = ROcp13_75*S6-S4*C6
    ROcp13_56 = ROcp13_85*S6+C4*C6
    ROcp13_76 = ROcp13_75*C6+S4*S6
    ROcp13_86 = ROcp13_85*C6-C4*S6
    OMcp13_15 = -qd[5]*S4
    OMcp13_25 = qd[5]*C4
    OMcp13_16 = OMcp13_15+ROcp13_15*qd[6]
    OMcp13_26 = OMcp13_25+ROcp13_25*qd[6]
    OMcp13_36 = qd[4]-qd[6]*S5
    OPcp13_16 = ROcp13_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp13_25*S5+ROcp13_25*qd[4])
    OPcp13_26 = ROcp13_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp13_15*S5+ROcp13_15*qd[4])
    OPcp13_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_14_0_2 = = 
 
# Sensor Kinematics 


    ROcp13_47 = ROcp13_46*C7+ROcp13_76*S7
    ROcp13_57 = ROcp13_56*C7+ROcp13_86*S7
    ROcp13_67 = S6p7*C5
    ROcp13_77 = -(ROcp13_46*S7-ROcp13_76*C7)
    ROcp13_87 = -(ROcp13_56*S7-ROcp13_86*C7)
    ROcp13_97 = C6p7*C5
    ROcp13_18 = ROcp13_15*C8+ROcp13_47*S8
    ROcp13_28 = ROcp13_25*C8+ROcp13_57*S8
    ROcp13_38 = ROcp13_67*S8-S5*C8
    ROcp13_48 = -(ROcp13_15*S8-ROcp13_47*C8)
    ROcp13_58 = -(ROcp13_25*S8-ROcp13_57*C8)
    ROcp13_68 = ROcp13_67*C8+S5*S8
    ROcp13_49 = ROcp13_48*C9+ROcp13_77*S9
    ROcp13_59 = ROcp13_58*C9+ROcp13_87*S9
    ROcp13_69 = ROcp13_68*C9+ROcp13_97*S9
    ROcp13_79 = -(ROcp13_48*S9-ROcp13_77*C9)
    ROcp13_89 = -(ROcp13_58*S9-ROcp13_87*C9)
    ROcp13_99 = -(ROcp13_68*S9-ROcp13_97*C9)
    ROcp13_110 = ROcp13_18*C10-ROcp13_79*S10
    ROcp13_210 = ROcp13_28*C10-ROcp13_89*S10
    ROcp13_310 = ROcp13_38*C10-ROcp13_99*S10
    ROcp13_710 = ROcp13_18*S10+ROcp13_79*C10
    ROcp13_810 = ROcp13_28*S10+ROcp13_89*C10
    ROcp13_910 = ROcp13_38*S10+ROcp13_99*C10
    RLcp13_17 = ROcp13_15*s.dpt[1,1]+ROcp13_46*s.dpt[2,1]
    RLcp13_27 = ROcp13_25*s.dpt[1,1]+ROcp13_56*s.dpt[2,1]
    RLcp13_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp13_17 = OMcp13_16+ROcp13_15*qd[7]
    OMcp13_27 = OMcp13_26+ROcp13_25*qd[7]
    OMcp13_37 = OMcp13_36-qd[7]*S5
    ORcp13_17 = OMcp13_26*RLcp13_37-OMcp13_36*RLcp13_27
    ORcp13_27 = -(OMcp13_16*RLcp13_37-OMcp13_36*RLcp13_17)
    ORcp13_37 = OMcp13_16*RLcp13_27-OMcp13_26*RLcp13_17
    OPcp13_17 = OPcp13_16+ROcp13_15*qdd[7]-qd[7]*(OMcp13_26*S5+OMcp13_36*ROcp13_25)
    OPcp13_27 = OPcp13_26+ROcp13_25*qdd[7]+qd[7]*(OMcp13_16*S5+OMcp13_36*ROcp13_15)
    OPcp13_37 = OPcp13_36-qdd[7]*S5+qd[7]*(OMcp13_16*ROcp13_25-OMcp13_26*ROcp13_15)
    RLcp13_18 = ROcp13_47*s.dpt[2,14]
    RLcp13_28 = ROcp13_57*s.dpt[2,14]
    RLcp13_38 = ROcp13_67*s.dpt[2,14]
    OMcp13_18 = OMcp13_17+ROcp13_77*qd[8]
    OMcp13_28 = OMcp13_27+ROcp13_87*qd[8]
    OMcp13_38 = OMcp13_37+ROcp13_97*qd[8]
    ORcp13_18 = OMcp13_27*RLcp13_38-OMcp13_37*RLcp13_28
    ORcp13_28 = -(OMcp13_17*RLcp13_38-OMcp13_37*RLcp13_18)
    ORcp13_38 = OMcp13_17*RLcp13_28-OMcp13_27*RLcp13_18
    OMcp13_19 = OMcp13_18+ROcp13_18*qd[9]
    OMcp13_29 = OMcp13_28+ROcp13_28*qd[9]
    OMcp13_39 = OMcp13_38+ROcp13_38*qd[9]
    OMcp13_110 = OMcp13_19+ROcp13_49*qd[10]
    OMcp13_210 = OMcp13_29+ROcp13_59*qd[10]
    OMcp13_310 = OMcp13_39+ROcp13_69*qd[10]
    OPcp13_110 = OPcp13_17+ROcp13_18*qdd[9]+ROcp13_49*qdd[10]+ROcp13_77*qdd[8]+qd[10]*(OMcp13_29*ROcp13_69-OMcp13_39*\
   ROcp13_59)+qd[8]*(OMcp13_27*ROcp13_97-OMcp13_37*ROcp13_87)+qd[9]*(OMcp13_28*ROcp13_38-OMcp13_38*ROcp13_28)
    OPcp13_210 = OPcp13_27+ROcp13_28*qdd[9]+ROcp13_59*qdd[10]+ROcp13_87*qdd[8]-qd[10]*(OMcp13_19*ROcp13_69-OMcp13_39*\
   ROcp13_49)-qd[8]*(OMcp13_17*ROcp13_97-OMcp13_37*ROcp13_77)-qd[9]*(OMcp13_18*ROcp13_38-OMcp13_38*ROcp13_18)
    OPcp13_310 = OPcp13_37+ROcp13_38*qdd[9]+ROcp13_69*qdd[10]+ROcp13_97*qdd[8]+qd[10]*(OMcp13_19*ROcp13_59-OMcp13_29*\
   ROcp13_49)+qd[8]*(OMcp13_17*ROcp13_87-OMcp13_27*ROcp13_77)+qd[9]*(OMcp13_18*ROcp13_28-OMcp13_28*ROcp13_18)

# = = Block_1_0_0_14_0_4 = = 
 
# Sensor Kinematics 


    ROcp13_413 = ROcp13_49*C13+ROcp13_710*S13
    ROcp13_513 = ROcp13_59*C13+ROcp13_810*S13
    ROcp13_613 = ROcp13_69*C13+ROcp13_910*S13
    ROcp13_713 = -(ROcp13_49*S13-ROcp13_710*C13)
    ROcp13_813 = -(ROcp13_59*S13-ROcp13_810*C13)
    ROcp13_913 = -(ROcp13_69*S13-ROcp13_910*C13)
    ROcp13_114 = ROcp13_110*C14-ROcp13_713*S14
    ROcp13_214 = ROcp13_210*C14-ROcp13_813*S14
    ROcp13_314 = ROcp13_310*C14-ROcp13_913*S14
    ROcp13_714 = ROcp13_110*S14+ROcp13_713*C14
    ROcp13_814 = ROcp13_210*S14+ROcp13_813*C14
    ROcp13_914 = ROcp13_310*S14+ROcp13_913*C14
    RLcp13_113 = ROcp13_710*s.dpt[3,16]
    RLcp13_213 = ROcp13_810*s.dpt[3,16]
    RLcp13_313 = ROcp13_910*s.dpt[3,16]
    POcp13_113 = RLcp13_113+RLcp13_17+RLcp13_18+q[1]
    POcp13_213 = RLcp13_213+RLcp13_27+RLcp13_28+q[2]
    POcp13_313 = RLcp13_313+RLcp13_37+RLcp13_38+q[3]
    OMcp13_113 = OMcp13_110+ROcp13_110*qd[13]
    OMcp13_213 = OMcp13_210+ROcp13_210*qd[13]
    OMcp13_313 = OMcp13_310+ROcp13_310*qd[13]
    ORcp13_113 = OMcp13_210*RLcp13_313-OMcp13_310*RLcp13_213
    ORcp13_213 = -(OMcp13_110*RLcp13_313-OMcp13_310*RLcp13_113)
    ORcp13_313 = OMcp13_110*RLcp13_213-OMcp13_210*RLcp13_113
    VIcp13_113 = ORcp13_113+ORcp13_17+ORcp13_18+qd[1]
    VIcp13_213 = ORcp13_213+ORcp13_27+ORcp13_28+qd[2]
    VIcp13_313 = ORcp13_313+ORcp13_37+ORcp13_38+qd[3]
    ACcp13_113 = qdd[1]+OMcp13_210*ORcp13_313+OMcp13_26*ORcp13_37+OMcp13_27*ORcp13_38-OMcp13_310*ORcp13_213-OMcp13_36*\
   ORcp13_27-OMcp13_37*ORcp13_28+OPcp13_210*RLcp13_313+OPcp13_26*RLcp13_37+OPcp13_27*RLcp13_38-OPcp13_310*RLcp13_213-OPcp13_36*\
   RLcp13_27-OPcp13_37*RLcp13_28
    ACcp13_213 = qdd[2]-OMcp13_110*ORcp13_313-OMcp13_16*ORcp13_37-OMcp13_17*ORcp13_38+OMcp13_310*ORcp13_113+OMcp13_36*\
   ORcp13_17+OMcp13_37*ORcp13_18-OPcp13_110*RLcp13_313-OPcp13_16*RLcp13_37-OPcp13_17*RLcp13_38+OPcp13_310*RLcp13_113+OPcp13_36*\
   RLcp13_17+OPcp13_37*RLcp13_18
    ACcp13_313 = qdd[3]+OMcp13_110*ORcp13_213+OMcp13_16*ORcp13_27+OMcp13_17*ORcp13_28-OMcp13_210*ORcp13_113-OMcp13_26*\
   ORcp13_17-OMcp13_27*ORcp13_18+OPcp13_110*RLcp13_213+OPcp13_16*RLcp13_27+OPcp13_17*RLcp13_28-OPcp13_210*RLcp13_113-OPcp13_26*\
   RLcp13_17-OPcp13_27*RLcp13_18
    OMcp13_114 = OMcp13_113+ROcp13_413*qd[14]
    OMcp13_214 = OMcp13_213+ROcp13_513*qd[14]
    OMcp13_314 = OMcp13_313+ROcp13_613*qd[14]
    OPcp13_114 = OPcp13_110+ROcp13_110*qdd[13]+ROcp13_413*qdd[14]+qd[13]*(OMcp13_210*ROcp13_310-OMcp13_310*ROcp13_210)+\
   qd[14]*(OMcp13_213*ROcp13_613-OMcp13_313*ROcp13_513)
    OPcp13_214 = OPcp13_210+ROcp13_210*qdd[13]+ROcp13_513*qdd[14]-qd[13]*(OMcp13_110*ROcp13_310-OMcp13_310*ROcp13_110)-\
   qd[14]*(OMcp13_113*ROcp13_613-OMcp13_313*ROcp13_413)
    OPcp13_314 = OPcp13_310+ROcp13_310*qdd[13]+ROcp13_613*qdd[14]+qd[13]*(OMcp13_110*ROcp13_210-OMcp13_210*ROcp13_110)+\
   qd[14]*(OMcp13_113*ROcp13_513-OMcp13_213*ROcp13_413)

# = = Block_1_0_0_14_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp13_113
    sens.P[2] = POcp13_213
    sens.P[3] = POcp13_313
    sens.R[1,1] = ROcp13_114
    sens.R[1,2] = ROcp13_214
    sens.R[1,3] = ROcp13_314
    sens.R[2,1] = ROcp13_413
    sens.R[2,2] = ROcp13_513
    sens.R[2,3] = ROcp13_613
    sens.R[3,1] = ROcp13_714
    sens.R[3,2] = ROcp13_814
    sens.R[3,3] = ROcp13_914
    sens.V[1] = VIcp13_113
    sens.V[2] = VIcp13_213
    sens.V[3] = VIcp13_313
    sens.OM[1] = OMcp13_114
    sens.OM[2] = OMcp13_214
    sens.OM[3] = OMcp13_314
    sens.A[1] = ACcp13_113
    sens.A[2] = ACcp13_213
    sens.A[3] = ACcp13_313
    sens.OMP[1] = OPcp13_114
    sens.OMP[2] = OPcp13_214
    sens.OMP[3] = OPcp13_314
 
# 
  elif(isens==15): 


# = = Block_1_0_0_15_0_1 = = 
 
# Sensor Kinematics 


    ROcp14_15 = C4*C5
    ROcp14_25 = S4*C5
    ROcp14_75 = C4*S5
    ROcp14_85 = S4*S5
    ROcp14_46 = ROcp14_75*S6-S4*C6
    ROcp14_56 = ROcp14_85*S6+C4*C6
    ROcp14_76 = ROcp14_75*C6+S4*S6
    ROcp14_86 = ROcp14_85*C6-C4*S6
    OMcp14_15 = -qd[5]*S4
    OMcp14_25 = qd[5]*C4
    OMcp14_16 = OMcp14_15+ROcp14_15*qd[6]
    OMcp14_26 = OMcp14_25+ROcp14_25*qd[6]
    OMcp14_36 = qd[4]-qd[6]*S5
    OPcp14_16 = ROcp14_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp14_25*S5+ROcp14_25*qd[4])
    OPcp14_26 = ROcp14_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp14_15*S5+ROcp14_15*qd[4])
    OPcp14_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_15_0_5 = = 
 
# Sensor Kinematics 


    ROcp14_415 = ROcp14_46*C15+ROcp14_76*S15
    ROcp14_515 = ROcp14_56*C15+ROcp14_86*S15
    ROcp14_615 = S15p6*C5
    ROcp14_715 = -(ROcp14_46*S15-ROcp14_76*C15)
    ROcp14_815 = -(ROcp14_56*S15-ROcp14_86*C15)
    ROcp14_915 = C15p6*C5
    RLcp14_115 = ROcp14_15*s.dpt[1,4]+ROcp14_46*s.dpt[2,4]
    RLcp14_215 = ROcp14_25*s.dpt[1,4]+ROcp14_56*s.dpt[2,4]
    RLcp14_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    POcp14_115 = RLcp14_115+q[1]
    POcp14_215 = RLcp14_215+q[2]
    POcp14_315 = RLcp14_315+q[3]
    OMcp14_115 = OMcp14_16+ROcp14_15*qd[15]
    OMcp14_215 = OMcp14_26+ROcp14_25*qd[15]
    OMcp14_315 = OMcp14_36-qd[15]*S5
    ORcp14_115 = OMcp14_26*RLcp14_315-OMcp14_36*RLcp14_215
    ORcp14_215 = -(OMcp14_16*RLcp14_315-OMcp14_36*RLcp14_115)
    ORcp14_315 = OMcp14_16*RLcp14_215-OMcp14_26*RLcp14_115
    VIcp14_115 = ORcp14_115+qd[1]
    VIcp14_215 = ORcp14_215+qd[2]
    VIcp14_315 = ORcp14_315+qd[3]
    OPcp14_115 = OPcp14_16+ROcp14_15*qdd[15]-qd[15]*(OMcp14_26*S5+OMcp14_36*ROcp14_25)
    OPcp14_215 = OPcp14_26+ROcp14_25*qdd[15]+qd[15]*(OMcp14_16*S5+OMcp14_36*ROcp14_15)
    OPcp14_315 = OPcp14_36-qdd[15]*S5+qd[15]*(OMcp14_16*ROcp14_25-OMcp14_26*ROcp14_15)
    ACcp14_115 = qdd[1]+OMcp14_26*ORcp14_315-OMcp14_36*ORcp14_215+OPcp14_26*RLcp14_315-OPcp14_36*RLcp14_215
    ACcp14_215 = qdd[2]-OMcp14_16*ORcp14_315+OMcp14_36*ORcp14_115-OPcp14_16*RLcp14_315+OPcp14_36*RLcp14_115
    ACcp14_315 = qdd[3]+OMcp14_16*ORcp14_215-OMcp14_26*ORcp14_115+OPcp14_16*RLcp14_215-OPcp14_26*RLcp14_115

# = = Block_1_0_0_15_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp14_115
    sens.P[2] = POcp14_215
    sens.P[3] = POcp14_315
    sens.R[1,1] = ROcp14_15
    sens.R[1,2] = ROcp14_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp14_415
    sens.R[2,2] = ROcp14_515
    sens.R[2,3] = ROcp14_615
    sens.R[3,1] = ROcp14_715
    sens.R[3,2] = ROcp14_815
    sens.R[3,3] = ROcp14_915
    sens.V[1] = VIcp14_115
    sens.V[2] = VIcp14_215
    sens.V[3] = VIcp14_315
    sens.OM[1] = OMcp14_115
    sens.OM[2] = OMcp14_215
    sens.OM[3] = OMcp14_315
    sens.A[1] = ACcp14_115
    sens.A[2] = ACcp14_215
    sens.A[3] = ACcp14_315
    sens.OMP[1] = OPcp14_115
    sens.OMP[2] = OPcp14_215
    sens.OMP[3] = OPcp14_315
 
# 
  elif(isens==16): 


# = = Block_1_0_0_16_0_1 = = 
 
# Sensor Kinematics 


    ROcp15_15 = C4*C5
    ROcp15_25 = S4*C5
    ROcp15_75 = C4*S5
    ROcp15_85 = S4*S5
    ROcp15_46 = ROcp15_75*S6-S4*C6
    ROcp15_56 = ROcp15_85*S6+C4*C6
    ROcp15_76 = ROcp15_75*C6+S4*S6
    ROcp15_86 = ROcp15_85*C6-C4*S6
    OMcp15_15 = -qd[5]*S4
    OMcp15_25 = qd[5]*C4
    OMcp15_16 = OMcp15_15+ROcp15_15*qd[6]
    OMcp15_26 = OMcp15_25+ROcp15_25*qd[6]
    OMcp15_36 = qd[4]-qd[6]*S5
    OPcp15_16 = ROcp15_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp15_25*S5+ROcp15_25*qd[4])
    OPcp15_26 = ROcp15_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp15_15*S5+ROcp15_15*qd[4])
    OPcp15_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_16_0_5 = = 
 
# Sensor Kinematics 


    ROcp15_415 = ROcp15_46*C15+ROcp15_76*S15
    ROcp15_515 = ROcp15_56*C15+ROcp15_86*S15
    ROcp15_615 = S15p6*C5
    ROcp15_715 = -(ROcp15_46*S15-ROcp15_76*C15)
    ROcp15_815 = -(ROcp15_56*S15-ROcp15_86*C15)
    ROcp15_915 = C15p6*C5
    ROcp15_116 = ROcp15_15*C16+ROcp15_415*S16
    ROcp15_216 = ROcp15_25*C16+ROcp15_515*S16
    ROcp15_316 = ROcp15_615*S16-C16*S5
    ROcp15_416 = -(ROcp15_15*S16-ROcp15_415*C16)
    ROcp15_516 = -(ROcp15_25*S16-ROcp15_515*C16)
    ROcp15_616 = ROcp15_615*C16+S16*S5
    RLcp15_115 = ROcp15_15*s.dpt[1,4]+ROcp15_46*s.dpt[2,4]
    RLcp15_215 = ROcp15_25*s.dpt[1,4]+ROcp15_56*s.dpt[2,4]
    RLcp15_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp15_115 = OMcp15_16+ROcp15_15*qd[15]
    OMcp15_215 = OMcp15_26+ROcp15_25*qd[15]
    OMcp15_315 = OMcp15_36-qd[15]*S5
    ORcp15_115 = OMcp15_26*RLcp15_315-OMcp15_36*RLcp15_215
    ORcp15_215 = -(OMcp15_16*RLcp15_315-OMcp15_36*RLcp15_115)
    ORcp15_315 = OMcp15_16*RLcp15_215-OMcp15_26*RLcp15_115
    OPcp15_115 = OPcp15_16+ROcp15_15*qdd[15]-qd[15]*(OMcp15_26*S5+OMcp15_36*ROcp15_25)
    OPcp15_215 = OPcp15_26+ROcp15_25*qdd[15]+qd[15]*(OMcp15_16*S5+OMcp15_36*ROcp15_15)
    OPcp15_315 = OPcp15_36-qdd[15]*S5+qd[15]*(OMcp15_16*ROcp15_25-OMcp15_26*ROcp15_15)
    RLcp15_116 = ROcp15_415*s.dpt[2,20]
    RLcp15_216 = ROcp15_515*s.dpt[2,20]
    RLcp15_316 = ROcp15_615*s.dpt[2,20]
    POcp15_116 = RLcp15_115+RLcp15_116+q[1]
    POcp15_216 = RLcp15_215+RLcp15_216+q[2]
    POcp15_316 = RLcp15_315+RLcp15_316+q[3]
    OMcp15_116 = OMcp15_115+ROcp15_715*qd[16]
    OMcp15_216 = OMcp15_215+ROcp15_815*qd[16]
    OMcp15_316 = OMcp15_315+ROcp15_915*qd[16]
    ORcp15_116 = OMcp15_215*RLcp15_316-OMcp15_315*RLcp15_216
    ORcp15_216 = -(OMcp15_115*RLcp15_316-OMcp15_315*RLcp15_116)
    ORcp15_316 = OMcp15_115*RLcp15_216-OMcp15_215*RLcp15_116
    VIcp15_116 = ORcp15_115+ORcp15_116+qd[1]
    VIcp15_216 = ORcp15_215+ORcp15_216+qd[2]
    VIcp15_316 = ORcp15_315+ORcp15_316+qd[3]
    OPcp15_116 = OPcp15_115+ROcp15_715*qdd[16]+qd[16]*(OMcp15_215*ROcp15_915-OMcp15_315*ROcp15_815)
    OPcp15_216 = OPcp15_215+ROcp15_815*qdd[16]-qd[16]*(OMcp15_115*ROcp15_915-OMcp15_315*ROcp15_715)
    OPcp15_316 = OPcp15_315+ROcp15_915*qdd[16]+qd[16]*(OMcp15_115*ROcp15_815-OMcp15_215*ROcp15_715)
    ACcp15_116 = qdd[1]+OMcp15_215*ORcp15_316+OMcp15_26*ORcp15_315-OMcp15_315*ORcp15_216-OMcp15_36*ORcp15_215+OPcp15_215*\
   RLcp15_316+OPcp15_26*RLcp15_315-OPcp15_315*RLcp15_216-OPcp15_36*RLcp15_215
    ACcp15_216 = qdd[2]-OMcp15_115*ORcp15_316-OMcp15_16*ORcp15_315+OMcp15_315*ORcp15_116+OMcp15_36*ORcp15_115-OPcp15_115*\
   RLcp15_316-OPcp15_16*RLcp15_315+OPcp15_315*RLcp15_116+OPcp15_36*RLcp15_115
    ACcp15_316 = qdd[3]+OMcp15_115*ORcp15_216+OMcp15_16*ORcp15_215-OMcp15_215*ORcp15_116-OMcp15_26*ORcp15_115+OPcp15_115*\
   RLcp15_216+OPcp15_16*RLcp15_215-OPcp15_215*RLcp15_116-OPcp15_26*RLcp15_115

# = = Block_1_0_0_16_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp15_116
    sens.P[2] = POcp15_216
    sens.P[3] = POcp15_316
    sens.R[1,1] = ROcp15_116
    sens.R[1,2] = ROcp15_216
    sens.R[1,3] = ROcp15_316
    sens.R[2,1] = ROcp15_416
    sens.R[2,2] = ROcp15_516
    sens.R[2,3] = ROcp15_616
    sens.R[3,1] = ROcp15_715
    sens.R[3,2] = ROcp15_815
    sens.R[3,3] = ROcp15_915
    sens.V[1] = VIcp15_116
    sens.V[2] = VIcp15_216
    sens.V[3] = VIcp15_316
    sens.OM[1] = OMcp15_116
    sens.OM[2] = OMcp15_216
    sens.OM[3] = OMcp15_316
    sens.A[1] = ACcp15_116
    sens.A[2] = ACcp15_216
    sens.A[3] = ACcp15_316
    sens.OMP[1] = OPcp15_116
    sens.OMP[2] = OPcp15_216
    sens.OMP[3] = OPcp15_316
 
# 
  elif(isens==17): 


# = = Block_1_0_0_17_0_1 = = 
 
# Sensor Kinematics 


    ROcp16_15 = C4*C5
    ROcp16_25 = S4*C5
    ROcp16_75 = C4*S5
    ROcp16_85 = S4*S5
    ROcp16_46 = ROcp16_75*S6-S4*C6
    ROcp16_56 = ROcp16_85*S6+C4*C6
    ROcp16_76 = ROcp16_75*C6+S4*S6
    ROcp16_86 = ROcp16_85*C6-C4*S6
    OMcp16_15 = -qd[5]*S4
    OMcp16_25 = qd[5]*C4
    OMcp16_16 = OMcp16_15+ROcp16_15*qd[6]
    OMcp16_26 = OMcp16_25+ROcp16_25*qd[6]
    OMcp16_36 = qd[4]-qd[6]*S5
    OPcp16_16 = ROcp16_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp16_25*S5+ROcp16_25*qd[4])
    OPcp16_26 = ROcp16_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp16_15*S5+ROcp16_15*qd[4])
    OPcp16_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_17_0_5 = = 
 
# Sensor Kinematics 


    ROcp16_415 = ROcp16_46*C15+ROcp16_76*S15
    ROcp16_515 = ROcp16_56*C15+ROcp16_86*S15
    ROcp16_615 = S15p6*C5
    ROcp16_715 = -(ROcp16_46*S15-ROcp16_76*C15)
    ROcp16_815 = -(ROcp16_56*S15-ROcp16_86*C15)
    ROcp16_915 = C15p6*C5
    ROcp16_116 = ROcp16_15*C16+ROcp16_415*S16
    ROcp16_216 = ROcp16_25*C16+ROcp16_515*S16
    ROcp16_316 = ROcp16_615*S16-C16*S5
    ROcp16_416 = -(ROcp16_15*S16-ROcp16_415*C16)
    ROcp16_516 = -(ROcp16_25*S16-ROcp16_515*C16)
    ROcp16_616 = ROcp16_615*C16+S16*S5
    ROcp16_417 = ROcp16_416*C17+ROcp16_715*S17
    ROcp16_517 = ROcp16_516*C17+ROcp16_815*S17
    ROcp16_617 = ROcp16_616*C17+ROcp16_915*S17
    ROcp16_717 = -(ROcp16_416*S17-ROcp16_715*C17)
    ROcp16_817 = -(ROcp16_516*S17-ROcp16_815*C17)
    ROcp16_917 = -(ROcp16_616*S17-ROcp16_915*C17)
    RLcp16_115 = ROcp16_15*s.dpt[1,4]+ROcp16_46*s.dpt[2,4]
    RLcp16_215 = ROcp16_25*s.dpt[1,4]+ROcp16_56*s.dpt[2,4]
    RLcp16_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp16_115 = OMcp16_16+ROcp16_15*qd[15]
    OMcp16_215 = OMcp16_26+ROcp16_25*qd[15]
    OMcp16_315 = OMcp16_36-qd[15]*S5
    ORcp16_115 = OMcp16_26*RLcp16_315-OMcp16_36*RLcp16_215
    ORcp16_215 = -(OMcp16_16*RLcp16_315-OMcp16_36*RLcp16_115)
    ORcp16_315 = OMcp16_16*RLcp16_215-OMcp16_26*RLcp16_115
    OPcp16_115 = OPcp16_16+ROcp16_15*qdd[15]-qd[15]*(OMcp16_26*S5+OMcp16_36*ROcp16_25)
    OPcp16_215 = OPcp16_26+ROcp16_25*qdd[15]+qd[15]*(OMcp16_16*S5+OMcp16_36*ROcp16_15)
    OPcp16_315 = OPcp16_36-qdd[15]*S5+qd[15]*(OMcp16_16*ROcp16_25-OMcp16_26*ROcp16_15)
    RLcp16_116 = ROcp16_415*s.dpt[2,20]
    RLcp16_216 = ROcp16_515*s.dpt[2,20]
    RLcp16_316 = ROcp16_615*s.dpt[2,20]
    POcp16_116 = RLcp16_115+RLcp16_116+q[1]
    POcp16_216 = RLcp16_215+RLcp16_216+q[2]
    POcp16_316 = RLcp16_315+RLcp16_316+q[3]
    OMcp16_116 = OMcp16_115+ROcp16_715*qd[16]
    OMcp16_216 = OMcp16_215+ROcp16_815*qd[16]
    OMcp16_316 = OMcp16_315+ROcp16_915*qd[16]
    ORcp16_116 = OMcp16_215*RLcp16_316-OMcp16_315*RLcp16_216
    ORcp16_216 = -(OMcp16_115*RLcp16_316-OMcp16_315*RLcp16_116)
    ORcp16_316 = OMcp16_115*RLcp16_216-OMcp16_215*RLcp16_116
    VIcp16_116 = ORcp16_115+ORcp16_116+qd[1]
    VIcp16_216 = ORcp16_215+ORcp16_216+qd[2]
    VIcp16_316 = ORcp16_315+ORcp16_316+qd[3]
    ACcp16_116 = qdd[1]+OMcp16_215*ORcp16_316+OMcp16_26*ORcp16_315-OMcp16_315*ORcp16_216-OMcp16_36*ORcp16_215+OPcp16_215*\
   RLcp16_316+OPcp16_26*RLcp16_315-OPcp16_315*RLcp16_216-OPcp16_36*RLcp16_215
    ACcp16_216 = qdd[2]-OMcp16_115*ORcp16_316-OMcp16_16*ORcp16_315+OMcp16_315*ORcp16_116+OMcp16_36*ORcp16_115-OPcp16_115*\
   RLcp16_316-OPcp16_16*RLcp16_315+OPcp16_315*RLcp16_116+OPcp16_36*RLcp16_115
    ACcp16_316 = qdd[3]+OMcp16_115*ORcp16_216+OMcp16_16*ORcp16_215-OMcp16_215*ORcp16_116-OMcp16_26*ORcp16_115+OPcp16_115*\
   RLcp16_216+OPcp16_16*RLcp16_215-OPcp16_215*RLcp16_116-OPcp16_26*RLcp16_115
    OMcp16_117 = OMcp16_116+ROcp16_116*qd[17]
    OMcp16_217 = OMcp16_216+ROcp16_216*qd[17]
    OMcp16_317 = OMcp16_316+ROcp16_316*qd[17]
    OPcp16_117 = OPcp16_115+ROcp16_116*qdd[17]+ROcp16_715*qdd[16]+qd[16]*(OMcp16_215*ROcp16_915-OMcp16_315*ROcp16_815)+\
   qd[17]*(OMcp16_216*ROcp16_316-OMcp16_316*ROcp16_216)
    OPcp16_217 = OPcp16_215+ROcp16_216*qdd[17]+ROcp16_815*qdd[16]-qd[16]*(OMcp16_115*ROcp16_915-OMcp16_315*ROcp16_715)-\
   qd[17]*(OMcp16_116*ROcp16_316-OMcp16_316*ROcp16_116)
    OPcp16_317 = OPcp16_315+ROcp16_316*qdd[17]+ROcp16_915*qdd[16]+qd[16]*(OMcp16_115*ROcp16_815-OMcp16_215*ROcp16_715)+\
   qd[17]*(OMcp16_116*ROcp16_216-OMcp16_216*ROcp16_116)

# = = Block_1_0_0_17_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp16_116
    sens.P[2] = POcp16_216
    sens.P[3] = POcp16_316
    sens.R[1,1] = ROcp16_116
    sens.R[1,2] = ROcp16_216
    sens.R[1,3] = ROcp16_316
    sens.R[2,1] = ROcp16_417
    sens.R[2,2] = ROcp16_517
    sens.R[2,3] = ROcp16_617
    sens.R[3,1] = ROcp16_717
    sens.R[3,2] = ROcp16_817
    sens.R[3,3] = ROcp16_917
    sens.V[1] = VIcp16_116
    sens.V[2] = VIcp16_216
    sens.V[3] = VIcp16_316
    sens.OM[1] = OMcp16_117
    sens.OM[2] = OMcp16_217
    sens.OM[3] = OMcp16_317
    sens.A[1] = ACcp16_116
    sens.A[2] = ACcp16_216
    sens.A[3] = ACcp16_316
    sens.OMP[1] = OPcp16_117
    sens.OMP[2] = OPcp16_217
    sens.OMP[3] = OPcp16_317
 
# 
  elif(isens==18): 


# = = Block_1_0_0_18_0_1 = = 
 
# Sensor Kinematics 


    ROcp17_15 = C4*C5
    ROcp17_25 = S4*C5
    ROcp17_75 = C4*S5
    ROcp17_85 = S4*S5
    ROcp17_46 = ROcp17_75*S6-S4*C6
    ROcp17_56 = ROcp17_85*S6+C4*C6
    ROcp17_76 = ROcp17_75*C6+S4*S6
    ROcp17_86 = ROcp17_85*C6-C4*S6
    OMcp17_15 = -qd[5]*S4
    OMcp17_25 = qd[5]*C4
    OMcp17_16 = OMcp17_15+ROcp17_15*qd[6]
    OMcp17_26 = OMcp17_25+ROcp17_25*qd[6]
    OMcp17_36 = qd[4]-qd[6]*S5
    OPcp17_16 = ROcp17_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp17_25*S5+ROcp17_25*qd[4])
    OPcp17_26 = ROcp17_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp17_15*S5+ROcp17_15*qd[4])
    OPcp17_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_18_0_5 = = 
 
# Sensor Kinematics 


    ROcp17_415 = ROcp17_46*C15+ROcp17_76*S15
    ROcp17_515 = ROcp17_56*C15+ROcp17_86*S15
    ROcp17_615 = S15p6*C5
    ROcp17_715 = -(ROcp17_46*S15-ROcp17_76*C15)
    ROcp17_815 = -(ROcp17_56*S15-ROcp17_86*C15)
    ROcp17_915 = C15p6*C5
    ROcp17_116 = ROcp17_15*C16+ROcp17_415*S16
    ROcp17_216 = ROcp17_25*C16+ROcp17_515*S16
    ROcp17_316 = ROcp17_615*S16-C16*S5
    ROcp17_416 = -(ROcp17_15*S16-ROcp17_415*C16)
    ROcp17_516 = -(ROcp17_25*S16-ROcp17_515*C16)
    ROcp17_616 = ROcp17_615*C16+S16*S5
    ROcp17_417 = ROcp17_416*C17+ROcp17_715*S17
    ROcp17_517 = ROcp17_516*C17+ROcp17_815*S17
    ROcp17_617 = ROcp17_616*C17+ROcp17_915*S17
    ROcp17_717 = -(ROcp17_416*S17-ROcp17_715*C17)
    ROcp17_817 = -(ROcp17_516*S17-ROcp17_815*C17)
    ROcp17_917 = -(ROcp17_616*S17-ROcp17_915*C17)
    ROcp17_118 = ROcp17_116*C18-ROcp17_717*S18
    ROcp17_218 = ROcp17_216*C18-ROcp17_817*S18
    ROcp17_318 = ROcp17_316*C18-ROcp17_917*S18
    ROcp17_718 = ROcp17_116*S18+ROcp17_717*C18
    ROcp17_818 = ROcp17_216*S18+ROcp17_817*C18
    ROcp17_918 = ROcp17_316*S18+ROcp17_917*C18
    RLcp17_115 = ROcp17_15*s.dpt[1,4]+ROcp17_46*s.dpt[2,4]
    RLcp17_215 = ROcp17_25*s.dpt[1,4]+ROcp17_56*s.dpt[2,4]
    RLcp17_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp17_115 = OMcp17_16+ROcp17_15*qd[15]
    OMcp17_215 = OMcp17_26+ROcp17_25*qd[15]
    OMcp17_315 = OMcp17_36-qd[15]*S5
    ORcp17_115 = OMcp17_26*RLcp17_315-OMcp17_36*RLcp17_215
    ORcp17_215 = -(OMcp17_16*RLcp17_315-OMcp17_36*RLcp17_115)
    ORcp17_315 = OMcp17_16*RLcp17_215-OMcp17_26*RLcp17_115
    OPcp17_115 = OPcp17_16+ROcp17_15*qdd[15]-qd[15]*(OMcp17_26*S5+OMcp17_36*ROcp17_25)
    OPcp17_215 = OPcp17_26+ROcp17_25*qdd[15]+qd[15]*(OMcp17_16*S5+OMcp17_36*ROcp17_15)
    OPcp17_315 = OPcp17_36-qdd[15]*S5+qd[15]*(OMcp17_16*ROcp17_25-OMcp17_26*ROcp17_15)
    RLcp17_116 = ROcp17_415*s.dpt[2,20]
    RLcp17_216 = ROcp17_515*s.dpt[2,20]
    RLcp17_316 = ROcp17_615*s.dpt[2,20]
    POcp17_116 = RLcp17_115+RLcp17_116+q[1]
    POcp17_216 = RLcp17_215+RLcp17_216+q[2]
    POcp17_316 = RLcp17_315+RLcp17_316+q[3]
    OMcp17_116 = OMcp17_115+ROcp17_715*qd[16]
    OMcp17_216 = OMcp17_215+ROcp17_815*qd[16]
    OMcp17_316 = OMcp17_315+ROcp17_915*qd[16]
    ORcp17_116 = OMcp17_215*RLcp17_316-OMcp17_315*RLcp17_216
    ORcp17_216 = -(OMcp17_115*RLcp17_316-OMcp17_315*RLcp17_116)
    ORcp17_316 = OMcp17_115*RLcp17_216-OMcp17_215*RLcp17_116
    VIcp17_116 = ORcp17_115+ORcp17_116+qd[1]
    VIcp17_216 = ORcp17_215+ORcp17_216+qd[2]
    VIcp17_316 = ORcp17_315+ORcp17_316+qd[3]
    ACcp17_116 = qdd[1]+OMcp17_215*ORcp17_316+OMcp17_26*ORcp17_315-OMcp17_315*ORcp17_216-OMcp17_36*ORcp17_215+OPcp17_215*\
   RLcp17_316+OPcp17_26*RLcp17_315-OPcp17_315*RLcp17_216-OPcp17_36*RLcp17_215
    ACcp17_216 = qdd[2]-OMcp17_115*ORcp17_316-OMcp17_16*ORcp17_315+OMcp17_315*ORcp17_116+OMcp17_36*ORcp17_115-OPcp17_115*\
   RLcp17_316-OPcp17_16*RLcp17_315+OPcp17_315*RLcp17_116+OPcp17_36*RLcp17_115
    ACcp17_316 = qdd[3]+OMcp17_115*ORcp17_216+OMcp17_16*ORcp17_215-OMcp17_215*ORcp17_116-OMcp17_26*ORcp17_115+OPcp17_115*\
   RLcp17_216+OPcp17_16*RLcp17_215-OPcp17_215*RLcp17_116-OPcp17_26*RLcp17_115
    OMcp17_117 = OMcp17_116+ROcp17_116*qd[17]
    OMcp17_217 = OMcp17_216+ROcp17_216*qd[17]
    OMcp17_317 = OMcp17_316+ROcp17_316*qd[17]
    OMcp17_118 = OMcp17_117+ROcp17_417*qd[18]
    OMcp17_218 = OMcp17_217+ROcp17_517*qd[18]
    OMcp17_318 = OMcp17_317+ROcp17_617*qd[18]
    OPcp17_118 = OPcp17_115+ROcp17_116*qdd[17]+ROcp17_417*qdd[18]+ROcp17_715*qdd[16]+qd[16]*(OMcp17_215*ROcp17_915-\
   OMcp17_315*ROcp17_815)+qd[17]*(OMcp17_216*ROcp17_316-OMcp17_316*ROcp17_216)+qd[18]*(OMcp17_217*ROcp17_617-OMcp17_317*\
   ROcp17_517)
    OPcp17_218 = OPcp17_215+ROcp17_216*qdd[17]+ROcp17_517*qdd[18]+ROcp17_815*qdd[16]-qd[16]*(OMcp17_115*ROcp17_915-\
   OMcp17_315*ROcp17_715)-qd[17]*(OMcp17_116*ROcp17_316-OMcp17_316*ROcp17_116)-qd[18]*(OMcp17_117*ROcp17_617-OMcp17_317*\
   ROcp17_417)
    OPcp17_318 = OPcp17_315+ROcp17_316*qdd[17]+ROcp17_617*qdd[18]+ROcp17_915*qdd[16]+qd[16]*(OMcp17_115*ROcp17_815-\
   OMcp17_215*ROcp17_715)+qd[17]*(OMcp17_116*ROcp17_216-OMcp17_216*ROcp17_116)+qd[18]*(OMcp17_117*ROcp17_517-OMcp17_217*\
   ROcp17_417)

# = = Block_1_0_0_18_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp17_116
    sens.P[2] = POcp17_216
    sens.P[3] = POcp17_316
    sens.R[1,1] = ROcp17_118
    sens.R[1,2] = ROcp17_218
    sens.R[1,3] = ROcp17_318
    sens.R[2,1] = ROcp17_417
    sens.R[2,2] = ROcp17_517
    sens.R[2,3] = ROcp17_617
    sens.R[3,1] = ROcp17_718
    sens.R[3,2] = ROcp17_818
    sens.R[3,3] = ROcp17_918
    sens.V[1] = VIcp17_116
    sens.V[2] = VIcp17_216
    sens.V[3] = VIcp17_316
    sens.OM[1] = OMcp17_118
    sens.OM[2] = OMcp17_218
    sens.OM[3] = OMcp17_318
    sens.A[1] = ACcp17_116
    sens.A[2] = ACcp17_216
    sens.A[3] = ACcp17_316
    sens.OMP[1] = OPcp17_118
    sens.OMP[2] = OPcp17_218
    sens.OMP[3] = OPcp17_318
 
# 
  elif(isens==19): 


# = = Block_1_0_0_19_0_1 = = 
 
# Sensor Kinematics 


    ROcp18_15 = C4*C5
    ROcp18_25 = S4*C5
    ROcp18_75 = C4*S5
    ROcp18_85 = S4*S5
    ROcp18_46 = ROcp18_75*S6-S4*C6
    ROcp18_56 = ROcp18_85*S6+C4*C6
    ROcp18_76 = ROcp18_75*C6+S4*S6
    ROcp18_86 = ROcp18_85*C6-C4*S6
    OMcp18_15 = -qd[5]*S4
    OMcp18_25 = qd[5]*C4
    OMcp18_16 = OMcp18_15+ROcp18_15*qd[6]
    OMcp18_26 = OMcp18_25+ROcp18_25*qd[6]
    OMcp18_36 = qd[4]-qd[6]*S5
    OPcp18_16 = ROcp18_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp18_25*S5+ROcp18_25*qd[4])
    OPcp18_26 = ROcp18_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp18_15*S5+ROcp18_15*qd[4])
    OPcp18_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_19_0_5 = = 
 
# Sensor Kinematics 


    ROcp18_415 = ROcp18_46*C15+ROcp18_76*S15
    ROcp18_515 = ROcp18_56*C15+ROcp18_86*S15
    ROcp18_615 = S15p6*C5
    ROcp18_715 = -(ROcp18_46*S15-ROcp18_76*C15)
    ROcp18_815 = -(ROcp18_56*S15-ROcp18_86*C15)
    ROcp18_915 = C15p6*C5
    ROcp18_116 = ROcp18_15*C16+ROcp18_415*S16
    ROcp18_216 = ROcp18_25*C16+ROcp18_515*S16
    ROcp18_316 = ROcp18_615*S16-C16*S5
    ROcp18_416 = -(ROcp18_15*S16-ROcp18_415*C16)
    ROcp18_516 = -(ROcp18_25*S16-ROcp18_515*C16)
    ROcp18_616 = ROcp18_615*C16+S16*S5
    ROcp18_417 = ROcp18_416*C17+ROcp18_715*S17
    ROcp18_517 = ROcp18_516*C17+ROcp18_815*S17
    ROcp18_617 = ROcp18_616*C17+ROcp18_915*S17
    ROcp18_717 = -(ROcp18_416*S17-ROcp18_715*C17)
    ROcp18_817 = -(ROcp18_516*S17-ROcp18_815*C17)
    ROcp18_917 = -(ROcp18_616*S17-ROcp18_915*C17)
    ROcp18_118 = ROcp18_116*C18-ROcp18_717*S18
    ROcp18_218 = ROcp18_216*C18-ROcp18_817*S18
    ROcp18_318 = ROcp18_316*C18-ROcp18_917*S18
    ROcp18_718 = ROcp18_116*S18+ROcp18_717*C18
    ROcp18_818 = ROcp18_216*S18+ROcp18_817*C18
    ROcp18_918 = ROcp18_316*S18+ROcp18_917*C18
    RLcp18_115 = ROcp18_15*s.dpt[1,4]+ROcp18_46*s.dpt[2,4]
    RLcp18_215 = ROcp18_25*s.dpt[1,4]+ROcp18_56*s.dpt[2,4]
    RLcp18_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp18_115 = OMcp18_16+ROcp18_15*qd[15]
    OMcp18_215 = OMcp18_26+ROcp18_25*qd[15]
    OMcp18_315 = OMcp18_36-qd[15]*S5
    ORcp18_115 = OMcp18_26*RLcp18_315-OMcp18_36*RLcp18_215
    ORcp18_215 = -(OMcp18_16*RLcp18_315-OMcp18_36*RLcp18_115)
    ORcp18_315 = OMcp18_16*RLcp18_215-OMcp18_26*RLcp18_115
    OPcp18_115 = OPcp18_16+ROcp18_15*qdd[15]-qd[15]*(OMcp18_26*S5+OMcp18_36*ROcp18_25)
    OPcp18_215 = OPcp18_26+ROcp18_25*qdd[15]+qd[15]*(OMcp18_16*S5+OMcp18_36*ROcp18_15)
    OPcp18_315 = OPcp18_36-qdd[15]*S5+qd[15]*(OMcp18_16*ROcp18_25-OMcp18_26*ROcp18_15)
    RLcp18_116 = ROcp18_415*s.dpt[2,20]
    RLcp18_216 = ROcp18_515*s.dpt[2,20]
    RLcp18_316 = ROcp18_615*s.dpt[2,20]
    OMcp18_116 = OMcp18_115+ROcp18_715*qd[16]
    OMcp18_216 = OMcp18_215+ROcp18_815*qd[16]
    OMcp18_316 = OMcp18_315+ROcp18_915*qd[16]
    ORcp18_116 = OMcp18_215*RLcp18_316-OMcp18_315*RLcp18_216
    ORcp18_216 = -(OMcp18_115*RLcp18_316-OMcp18_315*RLcp18_116)
    ORcp18_316 = OMcp18_115*RLcp18_216-OMcp18_215*RLcp18_116
    OMcp18_117 = OMcp18_116+ROcp18_116*qd[17]
    OMcp18_217 = OMcp18_216+ROcp18_216*qd[17]
    OMcp18_317 = OMcp18_316+ROcp18_316*qd[17]
    OMcp18_118 = OMcp18_117+ROcp18_417*qd[18]
    OMcp18_218 = OMcp18_217+ROcp18_517*qd[18]
    OMcp18_318 = OMcp18_317+ROcp18_617*qd[18]
    OPcp18_118 = OPcp18_115+ROcp18_116*qdd[17]+ROcp18_417*qdd[18]+ROcp18_715*qdd[16]+qd[16]*(OMcp18_215*ROcp18_915-\
   OMcp18_315*ROcp18_815)+qd[17]*(OMcp18_216*ROcp18_316-OMcp18_316*ROcp18_216)+qd[18]*(OMcp18_217*ROcp18_617-OMcp18_317*\
   ROcp18_517)
    OPcp18_218 = OPcp18_215+ROcp18_216*qdd[17]+ROcp18_517*qdd[18]+ROcp18_815*qdd[16]-qd[16]*(OMcp18_115*ROcp18_915-\
   OMcp18_315*ROcp18_715)-qd[17]*(OMcp18_116*ROcp18_316-OMcp18_316*ROcp18_116)-qd[18]*(OMcp18_117*ROcp18_617-OMcp18_317*\
   ROcp18_417)
    OPcp18_318 = OPcp18_315+ROcp18_316*qdd[17]+ROcp18_617*qdd[18]+ROcp18_915*qdd[16]+qd[16]*(OMcp18_115*ROcp18_815-\
   OMcp18_215*ROcp18_715)+qd[17]*(OMcp18_116*ROcp18_216-OMcp18_216*ROcp18_116)+qd[18]*(OMcp18_117*ROcp18_517-OMcp18_217*\
   ROcp18_417)

# = = Block_1_0_0_19_0_6 = = 
 
# Sensor Kinematics 


    ROcp18_419 = ROcp18_417*C19+ROcp18_718*S19
    ROcp18_519 = ROcp18_517*C19+ROcp18_818*S19
    ROcp18_619 = ROcp18_617*C19+ROcp18_918*S19
    ROcp18_719 = -(ROcp18_417*S19-ROcp18_718*C19)
    ROcp18_819 = -(ROcp18_517*S19-ROcp18_818*C19)
    ROcp18_919 = -(ROcp18_617*S19-ROcp18_918*C19)
    RLcp18_119 = ROcp18_718*s.dpt[3,21]
    RLcp18_219 = ROcp18_818*s.dpt[3,21]
    RLcp18_319 = ROcp18_918*s.dpt[3,21]
    POcp18_119 = RLcp18_115+RLcp18_116+RLcp18_119+q[1]
    POcp18_219 = RLcp18_215+RLcp18_216+RLcp18_219+q[2]
    POcp18_319 = RLcp18_315+RLcp18_316+RLcp18_319+q[3]
    OMcp18_119 = OMcp18_118+ROcp18_118*qd[19]
    OMcp18_219 = OMcp18_218+ROcp18_218*qd[19]
    OMcp18_319 = OMcp18_318+ROcp18_318*qd[19]
    ORcp18_119 = OMcp18_218*RLcp18_319-OMcp18_318*RLcp18_219
    ORcp18_219 = -(OMcp18_118*RLcp18_319-OMcp18_318*RLcp18_119)
    ORcp18_319 = OMcp18_118*RLcp18_219-OMcp18_218*RLcp18_119
    VIcp18_119 = ORcp18_115+ORcp18_116+ORcp18_119+qd[1]
    VIcp18_219 = ORcp18_215+ORcp18_216+ORcp18_219+qd[2]
    VIcp18_319 = ORcp18_315+ORcp18_316+ORcp18_319+qd[3]
    OPcp18_119 = OPcp18_118+ROcp18_118*qdd[19]+qd[19]*(OMcp18_218*ROcp18_318-OMcp18_318*ROcp18_218)
    OPcp18_219 = OPcp18_218+ROcp18_218*qdd[19]-qd[19]*(OMcp18_118*ROcp18_318-OMcp18_318*ROcp18_118)
    OPcp18_319 = OPcp18_318+ROcp18_318*qdd[19]+qd[19]*(OMcp18_118*ROcp18_218-OMcp18_218*ROcp18_118)
    ACcp18_119 = qdd[1]+OMcp18_215*ORcp18_316+OMcp18_218*ORcp18_319+OMcp18_26*ORcp18_315-OMcp18_315*ORcp18_216-OMcp18_318*\
   ORcp18_219-OMcp18_36*ORcp18_215+OPcp18_215*RLcp18_316+OPcp18_218*RLcp18_319+OPcp18_26*RLcp18_315-OPcp18_315*RLcp18_216-\
   OPcp18_318*RLcp18_219-OPcp18_36*RLcp18_215
    ACcp18_219 = qdd[2]-OMcp18_115*ORcp18_316-OMcp18_118*ORcp18_319-OMcp18_16*ORcp18_315+OMcp18_315*ORcp18_116+OMcp18_318*\
   ORcp18_119+OMcp18_36*ORcp18_115-OPcp18_115*RLcp18_316-OPcp18_118*RLcp18_319-OPcp18_16*RLcp18_315+OPcp18_315*RLcp18_116+\
   OPcp18_318*RLcp18_119+OPcp18_36*RLcp18_115
    ACcp18_319 = qdd[3]+OMcp18_115*ORcp18_216+OMcp18_118*ORcp18_219+OMcp18_16*ORcp18_215-OMcp18_215*ORcp18_116-OMcp18_218*\
   ORcp18_119-OMcp18_26*ORcp18_115+OPcp18_115*RLcp18_216+OPcp18_118*RLcp18_219+OPcp18_16*RLcp18_215-OPcp18_215*RLcp18_116-\
   OPcp18_218*RLcp18_119-OPcp18_26*RLcp18_115

# = = Block_1_0_0_19_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp18_119
    sens.P[2] = POcp18_219
    sens.P[3] = POcp18_319
    sens.R[1,1] = ROcp18_118
    sens.R[1,2] = ROcp18_218
    sens.R[1,3] = ROcp18_318
    sens.R[2,1] = ROcp18_419
    sens.R[2,2] = ROcp18_519
    sens.R[2,3] = ROcp18_619
    sens.R[3,1] = ROcp18_719
    sens.R[3,2] = ROcp18_819
    sens.R[3,3] = ROcp18_919
    sens.V[1] = VIcp18_119
    sens.V[2] = VIcp18_219
    sens.V[3] = VIcp18_319
    sens.OM[1] = OMcp18_119
    sens.OM[2] = OMcp18_219
    sens.OM[3] = OMcp18_319
    sens.A[1] = ACcp18_119
    sens.A[2] = ACcp18_219
    sens.A[3] = ACcp18_319
    sens.OMP[1] = OPcp18_119
    sens.OMP[2] = OPcp18_219
    sens.OMP[3] = OPcp18_319
 
# 
  elif(isens==20): 


# = = Block_1_0_0_20_0_1 = = 
 
# Sensor Kinematics 


    ROcp19_15 = C4*C5
    ROcp19_25 = S4*C5
    ROcp19_75 = C4*S5
    ROcp19_85 = S4*S5
    ROcp19_46 = ROcp19_75*S6-S4*C6
    ROcp19_56 = ROcp19_85*S6+C4*C6
    ROcp19_76 = ROcp19_75*C6+S4*S6
    ROcp19_86 = ROcp19_85*C6-C4*S6
    OMcp19_15 = -qd[5]*S4
    OMcp19_25 = qd[5]*C4
    OMcp19_16 = OMcp19_15+ROcp19_15*qd[6]
    OMcp19_26 = OMcp19_25+ROcp19_25*qd[6]
    OMcp19_36 = qd[4]-qd[6]*S5
    OPcp19_16 = ROcp19_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp19_25*S5+ROcp19_25*qd[4])
    OPcp19_26 = ROcp19_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp19_15*S5+ROcp19_15*qd[4])
    OPcp19_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_20_0_5 = = 
 
# Sensor Kinematics 


    ROcp19_415 = ROcp19_46*C15+ROcp19_76*S15
    ROcp19_515 = ROcp19_56*C15+ROcp19_86*S15
    ROcp19_615 = S15p6*C5
    ROcp19_715 = -(ROcp19_46*S15-ROcp19_76*C15)
    ROcp19_815 = -(ROcp19_56*S15-ROcp19_86*C15)
    ROcp19_915 = C15p6*C5
    ROcp19_116 = ROcp19_15*C16+ROcp19_415*S16
    ROcp19_216 = ROcp19_25*C16+ROcp19_515*S16
    ROcp19_316 = ROcp19_615*S16-C16*S5
    ROcp19_416 = -(ROcp19_15*S16-ROcp19_415*C16)
    ROcp19_516 = -(ROcp19_25*S16-ROcp19_515*C16)
    ROcp19_616 = ROcp19_615*C16+S16*S5
    ROcp19_417 = ROcp19_416*C17+ROcp19_715*S17
    ROcp19_517 = ROcp19_516*C17+ROcp19_815*S17
    ROcp19_617 = ROcp19_616*C17+ROcp19_915*S17
    ROcp19_717 = -(ROcp19_416*S17-ROcp19_715*C17)
    ROcp19_817 = -(ROcp19_516*S17-ROcp19_815*C17)
    ROcp19_917 = -(ROcp19_616*S17-ROcp19_915*C17)
    ROcp19_118 = ROcp19_116*C18-ROcp19_717*S18
    ROcp19_218 = ROcp19_216*C18-ROcp19_817*S18
    ROcp19_318 = ROcp19_316*C18-ROcp19_917*S18
    ROcp19_718 = ROcp19_116*S18+ROcp19_717*C18
    ROcp19_818 = ROcp19_216*S18+ROcp19_817*C18
    ROcp19_918 = ROcp19_316*S18+ROcp19_917*C18
    RLcp19_115 = ROcp19_15*s.dpt[1,4]+ROcp19_46*s.dpt[2,4]
    RLcp19_215 = ROcp19_25*s.dpt[1,4]+ROcp19_56*s.dpt[2,4]
    RLcp19_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp19_115 = OMcp19_16+ROcp19_15*qd[15]
    OMcp19_215 = OMcp19_26+ROcp19_25*qd[15]
    OMcp19_315 = OMcp19_36-qd[15]*S5
    ORcp19_115 = OMcp19_26*RLcp19_315-OMcp19_36*RLcp19_215
    ORcp19_215 = -(OMcp19_16*RLcp19_315-OMcp19_36*RLcp19_115)
    ORcp19_315 = OMcp19_16*RLcp19_215-OMcp19_26*RLcp19_115
    OPcp19_115 = OPcp19_16+ROcp19_15*qdd[15]-qd[15]*(OMcp19_26*S5+OMcp19_36*ROcp19_25)
    OPcp19_215 = OPcp19_26+ROcp19_25*qdd[15]+qd[15]*(OMcp19_16*S5+OMcp19_36*ROcp19_15)
    OPcp19_315 = OPcp19_36-qdd[15]*S5+qd[15]*(OMcp19_16*ROcp19_25-OMcp19_26*ROcp19_15)
    RLcp19_116 = ROcp19_415*s.dpt[2,20]
    RLcp19_216 = ROcp19_515*s.dpt[2,20]
    RLcp19_316 = ROcp19_615*s.dpt[2,20]
    OMcp19_116 = OMcp19_115+ROcp19_715*qd[16]
    OMcp19_216 = OMcp19_215+ROcp19_815*qd[16]
    OMcp19_316 = OMcp19_315+ROcp19_915*qd[16]
    ORcp19_116 = OMcp19_215*RLcp19_316-OMcp19_315*RLcp19_216
    ORcp19_216 = -(OMcp19_115*RLcp19_316-OMcp19_315*RLcp19_116)
    ORcp19_316 = OMcp19_115*RLcp19_216-OMcp19_215*RLcp19_116
    OMcp19_117 = OMcp19_116+ROcp19_116*qd[17]
    OMcp19_217 = OMcp19_216+ROcp19_216*qd[17]
    OMcp19_317 = OMcp19_316+ROcp19_316*qd[17]
    OMcp19_118 = OMcp19_117+ROcp19_417*qd[18]
    OMcp19_218 = OMcp19_217+ROcp19_517*qd[18]
    OMcp19_318 = OMcp19_317+ROcp19_617*qd[18]
    OPcp19_118 = OPcp19_115+ROcp19_116*qdd[17]+ROcp19_417*qdd[18]+ROcp19_715*qdd[16]+qd[16]*(OMcp19_215*ROcp19_915-\
   OMcp19_315*ROcp19_815)+qd[17]*(OMcp19_216*ROcp19_316-OMcp19_316*ROcp19_216)+qd[18]*(OMcp19_217*ROcp19_617-OMcp19_317*\
   ROcp19_517)
    OPcp19_218 = OPcp19_215+ROcp19_216*qdd[17]+ROcp19_517*qdd[18]+ROcp19_815*qdd[16]-qd[16]*(OMcp19_115*ROcp19_915-\
   OMcp19_315*ROcp19_715)-qd[17]*(OMcp19_116*ROcp19_316-OMcp19_316*ROcp19_116)-qd[18]*(OMcp19_117*ROcp19_617-OMcp19_317*\
   ROcp19_417)
    OPcp19_318 = OPcp19_315+ROcp19_316*qdd[17]+ROcp19_617*qdd[18]+ROcp19_915*qdd[16]+qd[16]*(OMcp19_115*ROcp19_815-\
   OMcp19_215*ROcp19_715)+qd[17]*(OMcp19_116*ROcp19_216-OMcp19_216*ROcp19_116)+qd[18]*(OMcp19_117*ROcp19_517-OMcp19_217*\
   ROcp19_417)

# = = Block_1_0_0_20_0_6 = = 
 
# Sensor Kinematics 


    ROcp19_419 = ROcp19_417*C19+ROcp19_718*S19
    ROcp19_519 = ROcp19_517*C19+ROcp19_818*S19
    ROcp19_619 = ROcp19_617*C19+ROcp19_918*S19
    ROcp19_719 = -(ROcp19_417*S19-ROcp19_718*C19)
    ROcp19_819 = -(ROcp19_517*S19-ROcp19_818*C19)
    ROcp19_919 = -(ROcp19_617*S19-ROcp19_918*C19)
    RLcp19_119 = ROcp19_718*s.dpt[3,21]
    RLcp19_219 = ROcp19_818*s.dpt[3,21]
    RLcp19_319 = ROcp19_918*s.dpt[3,21]
    OMcp19_119 = OMcp19_118+ROcp19_118*qd[19]
    OMcp19_219 = OMcp19_218+ROcp19_218*qd[19]
    OMcp19_319 = OMcp19_318+ROcp19_318*qd[19]
    ORcp19_119 = OMcp19_218*RLcp19_319-OMcp19_318*RLcp19_219
    ORcp19_219 = -(OMcp19_118*RLcp19_319-OMcp19_318*RLcp19_119)
    ORcp19_319 = OMcp19_118*RLcp19_219-OMcp19_218*RLcp19_119
    OPcp19_119 = OPcp19_118+ROcp19_118*qdd[19]+qd[19]*(OMcp19_218*ROcp19_318-OMcp19_318*ROcp19_218)
    OPcp19_219 = OPcp19_218+ROcp19_218*qdd[19]-qd[19]*(OMcp19_118*ROcp19_318-OMcp19_318*ROcp19_118)
    OPcp19_319 = OPcp19_318+ROcp19_318*qdd[19]+qd[19]*(OMcp19_118*ROcp19_218-OMcp19_218*ROcp19_118)
    RLcp19_120 = ROcp19_719*q[20]
    RLcp19_220 = ROcp19_819*q[20]
    RLcp19_320 = ROcp19_919*q[20]
    POcp19_120 = RLcp19_115+RLcp19_116+RLcp19_119+RLcp19_120+q[1]
    POcp19_220 = RLcp19_215+RLcp19_216+RLcp19_219+RLcp19_220+q[2]
    POcp19_320 = RLcp19_315+RLcp19_316+RLcp19_319+RLcp19_320+q[3]
    ORcp19_120 = OMcp19_219*RLcp19_320-OMcp19_319*RLcp19_220
    ORcp19_220 = -(OMcp19_119*RLcp19_320-OMcp19_319*RLcp19_120)
    ORcp19_320 = OMcp19_119*RLcp19_220-OMcp19_219*RLcp19_120
    VIcp19_120 = ORcp19_115+ORcp19_116+ORcp19_119+ORcp19_120+qd[1]+ROcp19_719*qd[20]
    VIcp19_220 = ORcp19_215+ORcp19_216+ORcp19_219+ORcp19_220+qd[2]+ROcp19_819*qd[20]
    VIcp19_320 = ORcp19_315+ORcp19_316+ORcp19_319+ORcp19_320+qd[3]+ROcp19_919*qd[20]
    ACcp19_120 = qdd[1]+OMcp19_215*ORcp19_316+OMcp19_218*ORcp19_319+OMcp19_219*ORcp19_320+OMcp19_26*ORcp19_315-OMcp19_315*\
   ORcp19_216-OMcp19_318*ORcp19_219-OMcp19_319*ORcp19_220-OMcp19_36*ORcp19_215+OPcp19_215*RLcp19_316+OPcp19_218*RLcp19_319+\
   OPcp19_219*RLcp19_320+OPcp19_26*RLcp19_315-OPcp19_315*RLcp19_216-OPcp19_318*RLcp19_219-OPcp19_319*RLcp19_220-OPcp19_36*\
   RLcp19_215+ROcp19_719*qdd[20]+(2.0)*qd[20]*(OMcp19_219*ROcp19_919-OMcp19_319*ROcp19_819)
    ACcp19_220 = qdd[2]-OMcp19_115*ORcp19_316-OMcp19_118*ORcp19_319-OMcp19_119*ORcp19_320-OMcp19_16*ORcp19_315+OMcp19_315*\
   ORcp19_116+OMcp19_318*ORcp19_119+OMcp19_319*ORcp19_120+OMcp19_36*ORcp19_115-OPcp19_115*RLcp19_316-OPcp19_118*RLcp19_319-\
   OPcp19_119*RLcp19_320-OPcp19_16*RLcp19_315+OPcp19_315*RLcp19_116+OPcp19_318*RLcp19_119+OPcp19_319*RLcp19_120+OPcp19_36*\
   RLcp19_115+ROcp19_819*qdd[20]-(2.0)*qd[20]*(OMcp19_119*ROcp19_919-OMcp19_319*ROcp19_719)
    ACcp19_320 = qdd[3]+OMcp19_115*ORcp19_216+OMcp19_118*ORcp19_219+OMcp19_119*ORcp19_220+OMcp19_16*ORcp19_215-OMcp19_215*\
   ORcp19_116-OMcp19_218*ORcp19_119-OMcp19_219*ORcp19_120-OMcp19_26*ORcp19_115+OPcp19_115*RLcp19_216+OPcp19_118*RLcp19_219+\
   OPcp19_119*RLcp19_220+OPcp19_16*RLcp19_215-OPcp19_215*RLcp19_116-OPcp19_218*RLcp19_119-OPcp19_219*RLcp19_120-OPcp19_26*\
   RLcp19_115+ROcp19_919*qdd[20]+(2.0)*qd[20]*(OMcp19_119*ROcp19_819-OMcp19_219*ROcp19_719)

# = = Block_1_0_0_20_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp19_120
    sens.P[2] = POcp19_220
    sens.P[3] = POcp19_320
    sens.R[1,1] = ROcp19_118
    sens.R[1,2] = ROcp19_218
    sens.R[1,3] = ROcp19_318
    sens.R[2,1] = ROcp19_419
    sens.R[2,2] = ROcp19_519
    sens.R[2,3] = ROcp19_619
    sens.R[3,1] = ROcp19_719
    sens.R[3,2] = ROcp19_819
    sens.R[3,3] = ROcp19_919
    sens.V[1] = VIcp19_120
    sens.V[2] = VIcp19_220
    sens.V[3] = VIcp19_320
    sens.OM[1] = OMcp19_119
    sens.OM[2] = OMcp19_219
    sens.OM[3] = OMcp19_319
    sens.A[1] = ACcp19_120
    sens.A[2] = ACcp19_220
    sens.A[3] = ACcp19_320
    sens.OMP[1] = OPcp19_119
    sens.OMP[2] = OPcp19_219
    sens.OMP[3] = OPcp19_319
 
# 
  elif(isens==21): 


# = = Block_1_0_0_21_0_1 = = 
 
# Sensor Kinematics 


    ROcp20_15 = C4*C5
    ROcp20_25 = S4*C5
    ROcp20_75 = C4*S5
    ROcp20_85 = S4*S5
    ROcp20_46 = ROcp20_75*S6-S4*C6
    ROcp20_56 = ROcp20_85*S6+C4*C6
    ROcp20_76 = ROcp20_75*C6+S4*S6
    ROcp20_86 = ROcp20_85*C6-C4*S6
    OMcp20_15 = -qd[5]*S4
    OMcp20_25 = qd[5]*C4
    OMcp20_16 = OMcp20_15+ROcp20_15*qd[6]
    OMcp20_26 = OMcp20_25+ROcp20_25*qd[6]
    OMcp20_36 = qd[4]-qd[6]*S5
    OPcp20_16 = ROcp20_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp20_25*S5+ROcp20_25*qd[4])
    OPcp20_26 = ROcp20_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp20_15*S5+ROcp20_15*qd[4])
    OPcp20_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_21_0_5 = = 
 
# Sensor Kinematics 


    ROcp20_415 = ROcp20_46*C15+ROcp20_76*S15
    ROcp20_515 = ROcp20_56*C15+ROcp20_86*S15
    ROcp20_615 = S15p6*C5
    ROcp20_715 = -(ROcp20_46*S15-ROcp20_76*C15)
    ROcp20_815 = -(ROcp20_56*S15-ROcp20_86*C15)
    ROcp20_915 = C15p6*C5
    ROcp20_116 = ROcp20_15*C16+ROcp20_415*S16
    ROcp20_216 = ROcp20_25*C16+ROcp20_515*S16
    ROcp20_316 = ROcp20_615*S16-C16*S5
    ROcp20_416 = -(ROcp20_15*S16-ROcp20_415*C16)
    ROcp20_516 = -(ROcp20_25*S16-ROcp20_515*C16)
    ROcp20_616 = ROcp20_615*C16+S16*S5
    ROcp20_417 = ROcp20_416*C17+ROcp20_715*S17
    ROcp20_517 = ROcp20_516*C17+ROcp20_815*S17
    ROcp20_617 = ROcp20_616*C17+ROcp20_915*S17
    ROcp20_717 = -(ROcp20_416*S17-ROcp20_715*C17)
    ROcp20_817 = -(ROcp20_516*S17-ROcp20_815*C17)
    ROcp20_917 = -(ROcp20_616*S17-ROcp20_915*C17)
    ROcp20_118 = ROcp20_116*C18-ROcp20_717*S18
    ROcp20_218 = ROcp20_216*C18-ROcp20_817*S18
    ROcp20_318 = ROcp20_316*C18-ROcp20_917*S18
    ROcp20_718 = ROcp20_116*S18+ROcp20_717*C18
    ROcp20_818 = ROcp20_216*S18+ROcp20_817*C18
    ROcp20_918 = ROcp20_316*S18+ROcp20_917*C18
    RLcp20_115 = ROcp20_15*s.dpt[1,4]+ROcp20_46*s.dpt[2,4]
    RLcp20_215 = ROcp20_25*s.dpt[1,4]+ROcp20_56*s.dpt[2,4]
    RLcp20_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp20_115 = OMcp20_16+ROcp20_15*qd[15]
    OMcp20_215 = OMcp20_26+ROcp20_25*qd[15]
    OMcp20_315 = OMcp20_36-qd[15]*S5
    ORcp20_115 = OMcp20_26*RLcp20_315-OMcp20_36*RLcp20_215
    ORcp20_215 = -(OMcp20_16*RLcp20_315-OMcp20_36*RLcp20_115)
    ORcp20_315 = OMcp20_16*RLcp20_215-OMcp20_26*RLcp20_115
    OPcp20_115 = OPcp20_16+ROcp20_15*qdd[15]-qd[15]*(OMcp20_26*S5+OMcp20_36*ROcp20_25)
    OPcp20_215 = OPcp20_26+ROcp20_25*qdd[15]+qd[15]*(OMcp20_16*S5+OMcp20_36*ROcp20_15)
    OPcp20_315 = OPcp20_36-qdd[15]*S5+qd[15]*(OMcp20_16*ROcp20_25-OMcp20_26*ROcp20_15)
    RLcp20_116 = ROcp20_415*s.dpt[2,20]
    RLcp20_216 = ROcp20_515*s.dpt[2,20]
    RLcp20_316 = ROcp20_615*s.dpt[2,20]
    OMcp20_116 = OMcp20_115+ROcp20_715*qd[16]
    OMcp20_216 = OMcp20_215+ROcp20_815*qd[16]
    OMcp20_316 = OMcp20_315+ROcp20_915*qd[16]
    ORcp20_116 = OMcp20_215*RLcp20_316-OMcp20_315*RLcp20_216
    ORcp20_216 = -(OMcp20_115*RLcp20_316-OMcp20_315*RLcp20_116)
    ORcp20_316 = OMcp20_115*RLcp20_216-OMcp20_215*RLcp20_116
    OMcp20_117 = OMcp20_116+ROcp20_116*qd[17]
    OMcp20_217 = OMcp20_216+ROcp20_216*qd[17]
    OMcp20_317 = OMcp20_316+ROcp20_316*qd[17]
    OMcp20_118 = OMcp20_117+ROcp20_417*qd[18]
    OMcp20_218 = OMcp20_217+ROcp20_517*qd[18]
    OMcp20_318 = OMcp20_317+ROcp20_617*qd[18]
    OPcp20_118 = OPcp20_115+ROcp20_116*qdd[17]+ROcp20_417*qdd[18]+ROcp20_715*qdd[16]+qd[16]*(OMcp20_215*ROcp20_915-\
   OMcp20_315*ROcp20_815)+qd[17]*(OMcp20_216*ROcp20_316-OMcp20_316*ROcp20_216)+qd[18]*(OMcp20_217*ROcp20_617-OMcp20_317*\
   ROcp20_517)
    OPcp20_218 = OPcp20_215+ROcp20_216*qdd[17]+ROcp20_517*qdd[18]+ROcp20_815*qdd[16]-qd[16]*(OMcp20_115*ROcp20_915-\
   OMcp20_315*ROcp20_715)-qd[17]*(OMcp20_116*ROcp20_316-OMcp20_316*ROcp20_116)-qd[18]*(OMcp20_117*ROcp20_617-OMcp20_317*\
   ROcp20_417)
    OPcp20_318 = OPcp20_315+ROcp20_316*qdd[17]+ROcp20_617*qdd[18]+ROcp20_915*qdd[16]+qd[16]*(OMcp20_115*ROcp20_815-\
   OMcp20_215*ROcp20_715)+qd[17]*(OMcp20_116*ROcp20_216-OMcp20_216*ROcp20_116)+qd[18]*(OMcp20_117*ROcp20_517-OMcp20_217*\
   ROcp20_417)

# = = Block_1_0_0_21_0_7 = = 
 
# Sensor Kinematics 


    ROcp20_421 = ROcp20_417*C21+ROcp20_718*S21
    ROcp20_521 = ROcp20_517*C21+ROcp20_818*S21
    ROcp20_621 = ROcp20_617*C21+ROcp20_918*S21
    ROcp20_721 = -(ROcp20_417*S21-ROcp20_718*C21)
    ROcp20_821 = -(ROcp20_517*S21-ROcp20_818*C21)
    ROcp20_921 = -(ROcp20_617*S21-ROcp20_918*C21)
    RLcp20_121 = ROcp20_718*s.dpt[3,22]
    RLcp20_221 = ROcp20_818*s.dpt[3,22]
    RLcp20_321 = ROcp20_918*s.dpt[3,22]
    POcp20_121 = RLcp20_115+RLcp20_116+RLcp20_121+q[1]
    POcp20_221 = RLcp20_215+RLcp20_216+RLcp20_221+q[2]
    POcp20_321 = RLcp20_315+RLcp20_316+RLcp20_321+q[3]
    OMcp20_121 = OMcp20_118+ROcp20_118*qd[21]
    OMcp20_221 = OMcp20_218+ROcp20_218*qd[21]
    OMcp20_321 = OMcp20_318+ROcp20_318*qd[21]
    ORcp20_121 = OMcp20_218*RLcp20_321-OMcp20_318*RLcp20_221
    ORcp20_221 = -(OMcp20_118*RLcp20_321-OMcp20_318*RLcp20_121)
    ORcp20_321 = OMcp20_118*RLcp20_221-OMcp20_218*RLcp20_121
    VIcp20_121 = ORcp20_115+ORcp20_116+ORcp20_121+qd[1]
    VIcp20_221 = ORcp20_215+ORcp20_216+ORcp20_221+qd[2]
    VIcp20_321 = ORcp20_315+ORcp20_316+ORcp20_321+qd[3]
    OPcp20_121 = OPcp20_118+ROcp20_118*qdd[21]+qd[21]*(OMcp20_218*ROcp20_318-OMcp20_318*ROcp20_218)
    OPcp20_221 = OPcp20_218+ROcp20_218*qdd[21]-qd[21]*(OMcp20_118*ROcp20_318-OMcp20_318*ROcp20_118)
    OPcp20_321 = OPcp20_318+ROcp20_318*qdd[21]+qd[21]*(OMcp20_118*ROcp20_218-OMcp20_218*ROcp20_118)
    ACcp20_121 = qdd[1]+OMcp20_215*ORcp20_316+OMcp20_218*ORcp20_321+OMcp20_26*ORcp20_315-OMcp20_315*ORcp20_216-OMcp20_318*\
   ORcp20_221-OMcp20_36*ORcp20_215+OPcp20_215*RLcp20_316+OPcp20_218*RLcp20_321+OPcp20_26*RLcp20_315-OPcp20_315*RLcp20_216-\
   OPcp20_318*RLcp20_221-OPcp20_36*RLcp20_215
    ACcp20_221 = qdd[2]-OMcp20_115*ORcp20_316-OMcp20_118*ORcp20_321-OMcp20_16*ORcp20_315+OMcp20_315*ORcp20_116+OMcp20_318*\
   ORcp20_121+OMcp20_36*ORcp20_115-OPcp20_115*RLcp20_316-OPcp20_118*RLcp20_321-OPcp20_16*RLcp20_315+OPcp20_315*RLcp20_116+\
   OPcp20_318*RLcp20_121+OPcp20_36*RLcp20_115
    ACcp20_321 = qdd[3]+OMcp20_115*ORcp20_216+OMcp20_118*ORcp20_221+OMcp20_16*ORcp20_215-OMcp20_215*ORcp20_116-OMcp20_218*\
   ORcp20_121-OMcp20_26*ORcp20_115+OPcp20_115*RLcp20_216+OPcp20_118*RLcp20_221+OPcp20_16*RLcp20_215-OPcp20_215*RLcp20_116-\
   OPcp20_218*RLcp20_121-OPcp20_26*RLcp20_115

# = = Block_1_0_0_21_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp20_121
    sens.P[2] = POcp20_221
    sens.P[3] = POcp20_321
    sens.R[1,1] = ROcp20_118
    sens.R[1,2] = ROcp20_218
    sens.R[1,3] = ROcp20_318
    sens.R[2,1] = ROcp20_421
    sens.R[2,2] = ROcp20_521
    sens.R[2,3] = ROcp20_621
    sens.R[3,1] = ROcp20_721
    sens.R[3,2] = ROcp20_821
    sens.R[3,3] = ROcp20_921
    sens.V[1] = VIcp20_121
    sens.V[2] = VIcp20_221
    sens.V[3] = VIcp20_321
    sens.OM[1] = OMcp20_121
    sens.OM[2] = OMcp20_221
    sens.OM[3] = OMcp20_321
    sens.A[1] = ACcp20_121
    sens.A[2] = ACcp20_221
    sens.A[3] = ACcp20_321
    sens.OMP[1] = OPcp20_121
    sens.OMP[2] = OPcp20_221
    sens.OMP[3] = OPcp20_321
 
# 
  elif(isens==22): 


# = = Block_1_0_0_22_0_1 = = 
 
# Sensor Kinematics 


    ROcp21_15 = C4*C5
    ROcp21_25 = S4*C5
    ROcp21_75 = C4*S5
    ROcp21_85 = S4*S5
    ROcp21_46 = ROcp21_75*S6-S4*C6
    ROcp21_56 = ROcp21_85*S6+C4*C6
    ROcp21_76 = ROcp21_75*C6+S4*S6
    ROcp21_86 = ROcp21_85*C6-C4*S6
    OMcp21_15 = -qd[5]*S4
    OMcp21_25 = qd[5]*C4
    OMcp21_16 = OMcp21_15+ROcp21_15*qd[6]
    OMcp21_26 = OMcp21_25+ROcp21_25*qd[6]
    OMcp21_36 = qd[4]-qd[6]*S5
    OPcp21_16 = ROcp21_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp21_25*S5+ROcp21_25*qd[4])
    OPcp21_26 = ROcp21_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp21_15*S5+ROcp21_15*qd[4])
    OPcp21_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_22_0_5 = = 
 
# Sensor Kinematics 


    ROcp21_415 = ROcp21_46*C15+ROcp21_76*S15
    ROcp21_515 = ROcp21_56*C15+ROcp21_86*S15
    ROcp21_615 = S15p6*C5
    ROcp21_715 = -(ROcp21_46*S15-ROcp21_76*C15)
    ROcp21_815 = -(ROcp21_56*S15-ROcp21_86*C15)
    ROcp21_915 = C15p6*C5
    ROcp21_116 = ROcp21_15*C16+ROcp21_415*S16
    ROcp21_216 = ROcp21_25*C16+ROcp21_515*S16
    ROcp21_316 = ROcp21_615*S16-C16*S5
    ROcp21_416 = -(ROcp21_15*S16-ROcp21_415*C16)
    ROcp21_516 = -(ROcp21_25*S16-ROcp21_515*C16)
    ROcp21_616 = ROcp21_615*C16+S16*S5
    ROcp21_417 = ROcp21_416*C17+ROcp21_715*S17
    ROcp21_517 = ROcp21_516*C17+ROcp21_815*S17
    ROcp21_617 = ROcp21_616*C17+ROcp21_915*S17
    ROcp21_717 = -(ROcp21_416*S17-ROcp21_715*C17)
    ROcp21_817 = -(ROcp21_516*S17-ROcp21_815*C17)
    ROcp21_917 = -(ROcp21_616*S17-ROcp21_915*C17)
    ROcp21_118 = ROcp21_116*C18-ROcp21_717*S18
    ROcp21_218 = ROcp21_216*C18-ROcp21_817*S18
    ROcp21_318 = ROcp21_316*C18-ROcp21_917*S18
    ROcp21_718 = ROcp21_116*S18+ROcp21_717*C18
    ROcp21_818 = ROcp21_216*S18+ROcp21_817*C18
    ROcp21_918 = ROcp21_316*S18+ROcp21_917*C18
    RLcp21_115 = ROcp21_15*s.dpt[1,4]+ROcp21_46*s.dpt[2,4]
    RLcp21_215 = ROcp21_25*s.dpt[1,4]+ROcp21_56*s.dpt[2,4]
    RLcp21_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp21_115 = OMcp21_16+ROcp21_15*qd[15]
    OMcp21_215 = OMcp21_26+ROcp21_25*qd[15]
    OMcp21_315 = OMcp21_36-qd[15]*S5
    ORcp21_115 = OMcp21_26*RLcp21_315-OMcp21_36*RLcp21_215
    ORcp21_215 = -(OMcp21_16*RLcp21_315-OMcp21_36*RLcp21_115)
    ORcp21_315 = OMcp21_16*RLcp21_215-OMcp21_26*RLcp21_115
    OPcp21_115 = OPcp21_16+ROcp21_15*qdd[15]-qd[15]*(OMcp21_26*S5+OMcp21_36*ROcp21_25)
    OPcp21_215 = OPcp21_26+ROcp21_25*qdd[15]+qd[15]*(OMcp21_16*S5+OMcp21_36*ROcp21_15)
    OPcp21_315 = OPcp21_36-qdd[15]*S5+qd[15]*(OMcp21_16*ROcp21_25-OMcp21_26*ROcp21_15)
    RLcp21_116 = ROcp21_415*s.dpt[2,20]
    RLcp21_216 = ROcp21_515*s.dpt[2,20]
    RLcp21_316 = ROcp21_615*s.dpt[2,20]
    OMcp21_116 = OMcp21_115+ROcp21_715*qd[16]
    OMcp21_216 = OMcp21_215+ROcp21_815*qd[16]
    OMcp21_316 = OMcp21_315+ROcp21_915*qd[16]
    ORcp21_116 = OMcp21_215*RLcp21_316-OMcp21_315*RLcp21_216
    ORcp21_216 = -(OMcp21_115*RLcp21_316-OMcp21_315*RLcp21_116)
    ORcp21_316 = OMcp21_115*RLcp21_216-OMcp21_215*RLcp21_116
    OMcp21_117 = OMcp21_116+ROcp21_116*qd[17]
    OMcp21_217 = OMcp21_216+ROcp21_216*qd[17]
    OMcp21_317 = OMcp21_316+ROcp21_316*qd[17]
    OMcp21_118 = OMcp21_117+ROcp21_417*qd[18]
    OMcp21_218 = OMcp21_217+ROcp21_517*qd[18]
    OMcp21_318 = OMcp21_317+ROcp21_617*qd[18]
    OPcp21_118 = OPcp21_115+ROcp21_116*qdd[17]+ROcp21_417*qdd[18]+ROcp21_715*qdd[16]+qd[16]*(OMcp21_215*ROcp21_915-\
   OMcp21_315*ROcp21_815)+qd[17]*(OMcp21_216*ROcp21_316-OMcp21_316*ROcp21_216)+qd[18]*(OMcp21_217*ROcp21_617-OMcp21_317*\
   ROcp21_517)
    OPcp21_218 = OPcp21_215+ROcp21_216*qdd[17]+ROcp21_517*qdd[18]+ROcp21_815*qdd[16]-qd[16]*(OMcp21_115*ROcp21_915-\
   OMcp21_315*ROcp21_715)-qd[17]*(OMcp21_116*ROcp21_316-OMcp21_316*ROcp21_116)-qd[18]*(OMcp21_117*ROcp21_617-OMcp21_317*\
   ROcp21_417)
    OPcp21_318 = OPcp21_315+ROcp21_316*qdd[17]+ROcp21_617*qdd[18]+ROcp21_915*qdd[16]+qd[16]*(OMcp21_115*ROcp21_815-\
   OMcp21_215*ROcp21_715)+qd[17]*(OMcp21_116*ROcp21_216-OMcp21_216*ROcp21_116)+qd[18]*(OMcp21_117*ROcp21_517-OMcp21_217*\
   ROcp21_417)

# = = Block_1_0_0_22_0_7 = = 
 
# Sensor Kinematics 


    ROcp21_421 = ROcp21_417*C21+ROcp21_718*S21
    ROcp21_521 = ROcp21_517*C21+ROcp21_818*S21
    ROcp21_621 = ROcp21_617*C21+ROcp21_918*S21
    ROcp21_721 = -(ROcp21_417*S21-ROcp21_718*C21)
    ROcp21_821 = -(ROcp21_517*S21-ROcp21_818*C21)
    ROcp21_921 = -(ROcp21_617*S21-ROcp21_918*C21)
    ROcp21_122 = ROcp21_118*C22-ROcp21_721*S22
    ROcp21_222 = ROcp21_218*C22-ROcp21_821*S22
    ROcp21_322 = ROcp21_318*C22-ROcp21_921*S22
    ROcp21_722 = ROcp21_118*S22+ROcp21_721*C22
    ROcp21_822 = ROcp21_218*S22+ROcp21_821*C22
    ROcp21_922 = ROcp21_318*S22+ROcp21_921*C22
    RLcp21_121 = ROcp21_718*s.dpt[3,22]
    RLcp21_221 = ROcp21_818*s.dpt[3,22]
    RLcp21_321 = ROcp21_918*s.dpt[3,22]
    POcp21_121 = RLcp21_115+RLcp21_116+RLcp21_121+q[1]
    POcp21_221 = RLcp21_215+RLcp21_216+RLcp21_221+q[2]
    POcp21_321 = RLcp21_315+RLcp21_316+RLcp21_321+q[3]
    OMcp21_121 = OMcp21_118+ROcp21_118*qd[21]
    OMcp21_221 = OMcp21_218+ROcp21_218*qd[21]
    OMcp21_321 = OMcp21_318+ROcp21_318*qd[21]
    ORcp21_121 = OMcp21_218*RLcp21_321-OMcp21_318*RLcp21_221
    ORcp21_221 = -(OMcp21_118*RLcp21_321-OMcp21_318*RLcp21_121)
    ORcp21_321 = OMcp21_118*RLcp21_221-OMcp21_218*RLcp21_121
    VIcp21_121 = ORcp21_115+ORcp21_116+ORcp21_121+qd[1]
    VIcp21_221 = ORcp21_215+ORcp21_216+ORcp21_221+qd[2]
    VIcp21_321 = ORcp21_315+ORcp21_316+ORcp21_321+qd[3]
    ACcp21_121 = qdd[1]+OMcp21_215*ORcp21_316+OMcp21_218*ORcp21_321+OMcp21_26*ORcp21_315-OMcp21_315*ORcp21_216-OMcp21_318*\
   ORcp21_221-OMcp21_36*ORcp21_215+OPcp21_215*RLcp21_316+OPcp21_218*RLcp21_321+OPcp21_26*RLcp21_315-OPcp21_315*RLcp21_216-\
   OPcp21_318*RLcp21_221-OPcp21_36*RLcp21_215
    ACcp21_221 = qdd[2]-OMcp21_115*ORcp21_316-OMcp21_118*ORcp21_321-OMcp21_16*ORcp21_315+OMcp21_315*ORcp21_116+OMcp21_318*\
   ORcp21_121+OMcp21_36*ORcp21_115-OPcp21_115*RLcp21_316-OPcp21_118*RLcp21_321-OPcp21_16*RLcp21_315+OPcp21_315*RLcp21_116+\
   OPcp21_318*RLcp21_121+OPcp21_36*RLcp21_115
    ACcp21_321 = qdd[3]+OMcp21_115*ORcp21_216+OMcp21_118*ORcp21_221+OMcp21_16*ORcp21_215-OMcp21_215*ORcp21_116-OMcp21_218*\
   ORcp21_121-OMcp21_26*ORcp21_115+OPcp21_115*RLcp21_216+OPcp21_118*RLcp21_221+OPcp21_16*RLcp21_215-OPcp21_215*RLcp21_116-\
   OPcp21_218*RLcp21_121-OPcp21_26*RLcp21_115
    OMcp21_122 = OMcp21_121+ROcp21_421*qd[22]
    OMcp21_222 = OMcp21_221+ROcp21_521*qd[22]
    OMcp21_322 = OMcp21_321+ROcp21_621*qd[22]
    OPcp21_122 = OPcp21_118+ROcp21_118*qdd[21]+ROcp21_421*qdd[22]+qd[21]*(OMcp21_218*ROcp21_318-OMcp21_318*ROcp21_218)+\
   qd[22]*(OMcp21_221*ROcp21_621-OMcp21_321*ROcp21_521)
    OPcp21_222 = OPcp21_218+ROcp21_218*qdd[21]+ROcp21_521*qdd[22]-qd[21]*(OMcp21_118*ROcp21_318-OMcp21_318*ROcp21_118)-\
   qd[22]*(OMcp21_121*ROcp21_621-OMcp21_321*ROcp21_421)
    OPcp21_322 = OPcp21_318+ROcp21_318*qdd[21]+ROcp21_621*qdd[22]+qd[21]*(OMcp21_118*ROcp21_218-OMcp21_218*ROcp21_118)+\
   qd[22]*(OMcp21_121*ROcp21_521-OMcp21_221*ROcp21_421)

# = = Block_1_0_0_22_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp21_121
    sens.P[2] = POcp21_221
    sens.P[3] = POcp21_321
    sens.R[1,1] = ROcp21_122
    sens.R[1,2] = ROcp21_222
    sens.R[1,3] = ROcp21_322
    sens.R[2,1] = ROcp21_421
    sens.R[2,2] = ROcp21_521
    sens.R[2,3] = ROcp21_621
    sens.R[3,1] = ROcp21_722
    sens.R[3,2] = ROcp21_822
    sens.R[3,3] = ROcp21_922
    sens.V[1] = VIcp21_121
    sens.V[2] = VIcp21_221
    sens.V[3] = VIcp21_321
    sens.OM[1] = OMcp21_122
    sens.OM[2] = OMcp21_222
    sens.OM[3] = OMcp21_322
    sens.A[1] = ACcp21_121
    sens.A[2] = ACcp21_221
    sens.A[3] = ACcp21_321
    sens.OMP[1] = OPcp21_122
    sens.OMP[2] = OPcp21_222
    sens.OMP[3] = OPcp21_322
 
# 
  elif(isens==23): 


# = = Block_1_0_0_23_0_1 = = 
 
# Sensor Kinematics 


    ROcp22_15 = C4*C5
    ROcp22_25 = S4*C5
    ROcp22_75 = C4*S5
    ROcp22_85 = S4*S5
    ROcp22_46 = ROcp22_75*S6-S4*C6
    ROcp22_56 = ROcp22_85*S6+C4*C6
    ROcp22_76 = ROcp22_75*C6+S4*S6
    ROcp22_86 = ROcp22_85*C6-C4*S6
    OMcp22_15 = -qd[5]*S4
    OMcp22_25 = qd[5]*C4
    OMcp22_16 = OMcp22_15+ROcp22_15*qd[6]
    OMcp22_26 = OMcp22_25+ROcp22_25*qd[6]
    OMcp22_36 = qd[4]-qd[6]*S5
    OPcp22_16 = ROcp22_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp22_25*S5+ROcp22_25*qd[4])
    OPcp22_26 = ROcp22_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp22_15*S5+ROcp22_15*qd[4])
    OPcp22_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_23_0_8 = = 
 
# Sensor Kinematics 


    ROcp22_423 = ROcp22_46*C23+ROcp22_76*S23
    ROcp22_523 = ROcp22_56*C23+ROcp22_86*S23
    ROcp22_623 = S23p6*C5
    ROcp22_723 = -(ROcp22_46*S23-ROcp22_76*C23)
    ROcp22_823 = -(ROcp22_56*S23-ROcp22_86*C23)
    ROcp22_923 = C23p6*C5
    RLcp22_123 = ROcp22_15*s.dpt[1,10]+ROcp22_46*s.dpt[2,10]
    RLcp22_223 = ROcp22_25*s.dpt[1,10]+ROcp22_56*s.dpt[2,10]
    RLcp22_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    POcp22_123 = RLcp22_123+q[1]
    POcp22_223 = RLcp22_223+q[2]
    POcp22_323 = RLcp22_323+q[3]
    OMcp22_123 = OMcp22_16+ROcp22_15*qd[23]
    OMcp22_223 = OMcp22_26+ROcp22_25*qd[23]
    OMcp22_323 = OMcp22_36-qd[23]*S5
    ORcp22_123 = OMcp22_26*RLcp22_323-OMcp22_36*RLcp22_223
    ORcp22_223 = -(OMcp22_16*RLcp22_323-OMcp22_36*RLcp22_123)
    ORcp22_323 = OMcp22_16*RLcp22_223-OMcp22_26*RLcp22_123
    VIcp22_123 = ORcp22_123+qd[1]
    VIcp22_223 = ORcp22_223+qd[2]
    VIcp22_323 = ORcp22_323+qd[3]
    OPcp22_123 = OPcp22_16+ROcp22_15*qdd[23]-qd[23]*(OMcp22_26*S5+OMcp22_36*ROcp22_25)
    OPcp22_223 = OPcp22_26+ROcp22_25*qdd[23]+qd[23]*(OMcp22_16*S5+OMcp22_36*ROcp22_15)
    OPcp22_323 = OPcp22_36-qdd[23]*S5+qd[23]*(OMcp22_16*ROcp22_25-OMcp22_26*ROcp22_15)
    ACcp22_123 = qdd[1]+OMcp22_26*ORcp22_323-OMcp22_36*ORcp22_223+OPcp22_26*RLcp22_323-OPcp22_36*RLcp22_223
    ACcp22_223 = qdd[2]-OMcp22_16*ORcp22_323+OMcp22_36*ORcp22_123-OPcp22_16*RLcp22_323+OPcp22_36*RLcp22_123
    ACcp22_323 = qdd[3]+OMcp22_16*ORcp22_223-OMcp22_26*ORcp22_123+OPcp22_16*RLcp22_223-OPcp22_26*RLcp22_123

# = = Block_1_0_0_23_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp22_123
    sens.P[2] = POcp22_223
    sens.P[3] = POcp22_323
    sens.R[1,1] = ROcp22_15
    sens.R[1,2] = ROcp22_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp22_423
    sens.R[2,2] = ROcp22_523
    sens.R[2,3] = ROcp22_623
    sens.R[3,1] = ROcp22_723
    sens.R[3,2] = ROcp22_823
    sens.R[3,3] = ROcp22_923
    sens.V[1] = VIcp22_123
    sens.V[2] = VIcp22_223
    sens.V[3] = VIcp22_323
    sens.OM[1] = OMcp22_123
    sens.OM[2] = OMcp22_223
    sens.OM[3] = OMcp22_323
    sens.A[1] = ACcp22_123
    sens.A[2] = ACcp22_223
    sens.A[3] = ACcp22_323
    sens.OMP[1] = OPcp22_123
    sens.OMP[2] = OPcp22_223
    sens.OMP[3] = OPcp22_323
 
# 
  elif(isens==24): 


# = = Block_1_0_0_24_0_1 = = 
 
# Sensor Kinematics 


    ROcp23_15 = C4*C5
    ROcp23_25 = S4*C5
    ROcp23_75 = C4*S5
    ROcp23_85 = S4*S5
    ROcp23_46 = ROcp23_75*S6-S4*C6
    ROcp23_56 = ROcp23_85*S6+C4*C6
    ROcp23_76 = ROcp23_75*C6+S4*S6
    ROcp23_86 = ROcp23_85*C6-C4*S6
    OMcp23_15 = -qd[5]*S4
    OMcp23_25 = qd[5]*C4
    OMcp23_16 = OMcp23_15+ROcp23_15*qd[6]
    OMcp23_26 = OMcp23_25+ROcp23_25*qd[6]
    OMcp23_36 = qd[4]-qd[6]*S5
    OPcp23_16 = ROcp23_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp23_25*S5+ROcp23_25*qd[4])
    OPcp23_26 = ROcp23_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp23_15*S5+ROcp23_15*qd[4])
    OPcp23_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_24_0_8 = = 
 
# Sensor Kinematics 


    ROcp23_423 = ROcp23_46*C23+ROcp23_76*S23
    ROcp23_523 = ROcp23_56*C23+ROcp23_86*S23
    ROcp23_623 = S23p6*C5
    ROcp23_723 = -(ROcp23_46*S23-ROcp23_76*C23)
    ROcp23_823 = -(ROcp23_56*S23-ROcp23_86*C23)
    ROcp23_923 = C23p6*C5
    ROcp23_124 = ROcp23_15*C24+ROcp23_423*S24
    ROcp23_224 = ROcp23_25*C24+ROcp23_523*S24
    ROcp23_324 = ROcp23_623*S24-C24*S5
    ROcp23_424 = -(ROcp23_15*S24-ROcp23_423*C24)
    ROcp23_524 = -(ROcp23_25*S24-ROcp23_523*C24)
    ROcp23_624 = ROcp23_623*C24+S24*S5
    RLcp23_123 = ROcp23_15*s.dpt[1,10]+ROcp23_46*s.dpt[2,10]
    RLcp23_223 = ROcp23_25*s.dpt[1,10]+ROcp23_56*s.dpt[2,10]
    RLcp23_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    POcp23_123 = RLcp23_123+q[1]
    POcp23_223 = RLcp23_223+q[2]
    POcp23_323 = RLcp23_323+q[3]
    OMcp23_123 = OMcp23_16+ROcp23_15*qd[23]
    OMcp23_223 = OMcp23_26+ROcp23_25*qd[23]
    OMcp23_323 = OMcp23_36-qd[23]*S5
    ORcp23_123 = OMcp23_26*RLcp23_323-OMcp23_36*RLcp23_223
    ORcp23_223 = -(OMcp23_16*RLcp23_323-OMcp23_36*RLcp23_123)
    ORcp23_323 = OMcp23_16*RLcp23_223-OMcp23_26*RLcp23_123
    VIcp23_123 = ORcp23_123+qd[1]
    VIcp23_223 = ORcp23_223+qd[2]
    VIcp23_323 = ORcp23_323+qd[3]
    ACcp23_123 = qdd[1]+OMcp23_26*ORcp23_323-OMcp23_36*ORcp23_223+OPcp23_26*RLcp23_323-OPcp23_36*RLcp23_223
    ACcp23_223 = qdd[2]-OMcp23_16*ORcp23_323+OMcp23_36*ORcp23_123-OPcp23_16*RLcp23_323+OPcp23_36*RLcp23_123
    ACcp23_323 = qdd[3]+OMcp23_16*ORcp23_223-OMcp23_26*ORcp23_123+OPcp23_16*RLcp23_223-OPcp23_26*RLcp23_123
    OMcp23_124 = OMcp23_123+ROcp23_723*qd[24]
    OMcp23_224 = OMcp23_223+ROcp23_823*qd[24]
    OMcp23_324 = OMcp23_323+ROcp23_923*qd[24]
    OPcp23_124 = OPcp23_16+ROcp23_15*qdd[23]+ROcp23_723*qdd[24]-qd[23]*(OMcp23_26*S5+OMcp23_36*ROcp23_25)+qd[24]*(\
   OMcp23_223*ROcp23_923-OMcp23_323*ROcp23_823)
    OPcp23_224 = OPcp23_26+ROcp23_25*qdd[23]+ROcp23_823*qdd[24]+qd[23]*(OMcp23_16*S5+OMcp23_36*ROcp23_15)-qd[24]*(\
   OMcp23_123*ROcp23_923-OMcp23_323*ROcp23_723)
    OPcp23_324 = OPcp23_36+ROcp23_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp23_16*ROcp23_25-OMcp23_26*ROcp23_15)+qd[24]*(\
   OMcp23_123*ROcp23_823-OMcp23_223*ROcp23_723)

# = = Block_1_0_0_24_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp23_123
    sens.P[2] = POcp23_223
    sens.P[3] = POcp23_323
    sens.R[1,1] = ROcp23_124
    sens.R[1,2] = ROcp23_224
    sens.R[1,3] = ROcp23_324
    sens.R[2,1] = ROcp23_424
    sens.R[2,2] = ROcp23_524
    sens.R[2,3] = ROcp23_624
    sens.R[3,1] = ROcp23_723
    sens.R[3,2] = ROcp23_823
    sens.R[3,3] = ROcp23_923
    sens.V[1] = VIcp23_123
    sens.V[2] = VIcp23_223
    sens.V[3] = VIcp23_323
    sens.OM[1] = OMcp23_124
    sens.OM[2] = OMcp23_224
    sens.OM[3] = OMcp23_324
    sens.A[1] = ACcp23_123
    sens.A[2] = ACcp23_223
    sens.A[3] = ACcp23_323
    sens.OMP[1] = OPcp23_124
    sens.OMP[2] = OPcp23_224
    sens.OMP[3] = OPcp23_324
 
# 
  elif(isens==25): 


# = = Block_1_0_0_25_0_1 = = 
 
# Sensor Kinematics 


    ROcp24_15 = C4*C5
    ROcp24_25 = S4*C5
    ROcp24_75 = C4*S5
    ROcp24_85 = S4*S5
    ROcp24_46 = ROcp24_75*S6-S4*C6
    ROcp24_56 = ROcp24_85*S6+C4*C6
    ROcp24_76 = ROcp24_75*C6+S4*S6
    ROcp24_86 = ROcp24_85*C6-C4*S6
    OMcp24_15 = -qd[5]*S4
    OMcp24_25 = qd[5]*C4
    OMcp24_16 = OMcp24_15+ROcp24_15*qd[6]
    OMcp24_26 = OMcp24_25+ROcp24_25*qd[6]
    OMcp24_36 = qd[4]-qd[6]*S5
    OPcp24_16 = ROcp24_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp24_25*S5+ROcp24_25*qd[4])
    OPcp24_26 = ROcp24_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp24_15*S5+ROcp24_15*qd[4])
    OPcp24_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_25_0_8 = = 
 
# Sensor Kinematics 


    ROcp24_423 = ROcp24_46*C23+ROcp24_76*S23
    ROcp24_523 = ROcp24_56*C23+ROcp24_86*S23
    ROcp24_623 = S23p6*C5
    ROcp24_723 = -(ROcp24_46*S23-ROcp24_76*C23)
    ROcp24_823 = -(ROcp24_56*S23-ROcp24_86*C23)
    ROcp24_923 = C23p6*C5
    ROcp24_124 = ROcp24_15*C24+ROcp24_423*S24
    ROcp24_224 = ROcp24_25*C24+ROcp24_523*S24
    ROcp24_324 = ROcp24_623*S24-C24*S5
    ROcp24_424 = -(ROcp24_15*S24-ROcp24_423*C24)
    ROcp24_524 = -(ROcp24_25*S24-ROcp24_523*C24)
    ROcp24_624 = ROcp24_623*C24+S24*S5
    ROcp24_425 = ROcp24_424*C25+ROcp24_723*S25
    ROcp24_525 = ROcp24_524*C25+ROcp24_823*S25
    ROcp24_625 = ROcp24_624*C25+ROcp24_923*S25
    ROcp24_725 = -(ROcp24_424*S25-ROcp24_723*C25)
    ROcp24_825 = -(ROcp24_524*S25-ROcp24_823*C25)
    ROcp24_925 = -(ROcp24_624*S25-ROcp24_923*C25)
    RLcp24_123 = ROcp24_15*s.dpt[1,10]+ROcp24_46*s.dpt[2,10]
    RLcp24_223 = ROcp24_25*s.dpt[1,10]+ROcp24_56*s.dpt[2,10]
    RLcp24_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp24_123 = OMcp24_16+ROcp24_15*qd[23]
    OMcp24_223 = OMcp24_26+ROcp24_25*qd[23]
    OMcp24_323 = OMcp24_36-qd[23]*S5
    ORcp24_123 = OMcp24_26*RLcp24_323-OMcp24_36*RLcp24_223
    ORcp24_223 = -(OMcp24_16*RLcp24_323-OMcp24_36*RLcp24_123)
    ORcp24_323 = OMcp24_16*RLcp24_223-OMcp24_26*RLcp24_123
    OMcp24_124 = OMcp24_123+ROcp24_723*qd[24]
    OMcp24_224 = OMcp24_223+ROcp24_823*qd[24]
    OMcp24_324 = OMcp24_323+ROcp24_923*qd[24]
    OPcp24_124 = OPcp24_16+ROcp24_15*qdd[23]+ROcp24_723*qdd[24]-qd[23]*(OMcp24_26*S5+OMcp24_36*ROcp24_25)+qd[24]*(\
   OMcp24_223*ROcp24_923-OMcp24_323*ROcp24_823)
    OPcp24_224 = OPcp24_26+ROcp24_25*qdd[23]+ROcp24_823*qdd[24]+qd[23]*(OMcp24_16*S5+OMcp24_36*ROcp24_15)-qd[24]*(\
   OMcp24_123*ROcp24_923-OMcp24_323*ROcp24_723)
    OPcp24_324 = OPcp24_36+ROcp24_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp24_16*ROcp24_25-OMcp24_26*ROcp24_15)+qd[24]*(\
   OMcp24_123*ROcp24_823-OMcp24_223*ROcp24_723)
    RLcp24_125 = ROcp24_424*s.dpt[2,26]
    RLcp24_225 = ROcp24_524*s.dpt[2,26]
    RLcp24_325 = ROcp24_624*s.dpt[2,26]
    POcp24_125 = RLcp24_123+RLcp24_125+q[1]
    POcp24_225 = RLcp24_223+RLcp24_225+q[2]
    POcp24_325 = RLcp24_323+RLcp24_325+q[3]
    OMcp24_125 = OMcp24_124+ROcp24_124*qd[25]
    OMcp24_225 = OMcp24_224+ROcp24_224*qd[25]
    OMcp24_325 = OMcp24_324+ROcp24_324*qd[25]
    ORcp24_125 = OMcp24_224*RLcp24_325-OMcp24_324*RLcp24_225
    ORcp24_225 = -(OMcp24_124*RLcp24_325-OMcp24_324*RLcp24_125)
    ORcp24_325 = OMcp24_124*RLcp24_225-OMcp24_224*RLcp24_125
    VIcp24_125 = ORcp24_123+ORcp24_125+qd[1]
    VIcp24_225 = ORcp24_223+ORcp24_225+qd[2]
    VIcp24_325 = ORcp24_323+ORcp24_325+qd[3]
    OPcp24_125 = OPcp24_124+ROcp24_124*qdd[25]+qd[25]*(OMcp24_224*ROcp24_324-OMcp24_324*ROcp24_224)
    OPcp24_225 = OPcp24_224+ROcp24_224*qdd[25]-qd[25]*(OMcp24_124*ROcp24_324-OMcp24_324*ROcp24_124)
    OPcp24_325 = OPcp24_324+ROcp24_324*qdd[25]+qd[25]*(OMcp24_124*ROcp24_224-OMcp24_224*ROcp24_124)
    ACcp24_125 = qdd[1]+OMcp24_224*ORcp24_325+OMcp24_26*ORcp24_323-OMcp24_324*ORcp24_225-OMcp24_36*ORcp24_223+OPcp24_224*\
   RLcp24_325+OPcp24_26*RLcp24_323-OPcp24_324*RLcp24_225-OPcp24_36*RLcp24_223
    ACcp24_225 = qdd[2]-OMcp24_124*ORcp24_325-OMcp24_16*ORcp24_323+OMcp24_324*ORcp24_125+OMcp24_36*ORcp24_123-OPcp24_124*\
   RLcp24_325-OPcp24_16*RLcp24_323+OPcp24_324*RLcp24_125+OPcp24_36*RLcp24_123
    ACcp24_325 = qdd[3]+OMcp24_124*ORcp24_225+OMcp24_16*ORcp24_223-OMcp24_224*ORcp24_125-OMcp24_26*ORcp24_123+OPcp24_124*\
   RLcp24_225+OPcp24_16*RLcp24_223-OPcp24_224*RLcp24_125-OPcp24_26*RLcp24_123

# = = Block_1_0_0_25_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp24_125
    sens.P[2] = POcp24_225
    sens.P[3] = POcp24_325
    sens.R[1,1] = ROcp24_124
    sens.R[1,2] = ROcp24_224
    sens.R[1,3] = ROcp24_324
    sens.R[2,1] = ROcp24_425
    sens.R[2,2] = ROcp24_525
    sens.R[2,3] = ROcp24_625
    sens.R[3,1] = ROcp24_725
    sens.R[3,2] = ROcp24_825
    sens.R[3,3] = ROcp24_925
    sens.V[1] = VIcp24_125
    sens.V[2] = VIcp24_225
    sens.V[3] = VIcp24_325
    sens.OM[1] = OMcp24_125
    sens.OM[2] = OMcp24_225
    sens.OM[3] = OMcp24_325
    sens.A[1] = ACcp24_125
    sens.A[2] = ACcp24_225
    sens.A[3] = ACcp24_325
    sens.OMP[1] = OPcp24_125
    sens.OMP[2] = OPcp24_225
    sens.OMP[3] = OPcp24_325
 
# 
  elif(isens==26): 


# = = Block_1_0_0_26_0_1 = = 
 
# Sensor Kinematics 


    ROcp25_15 = C4*C5
    ROcp25_25 = S4*C5
    ROcp25_75 = C4*S5
    ROcp25_85 = S4*S5
    ROcp25_46 = ROcp25_75*S6-S4*C6
    ROcp25_56 = ROcp25_85*S6+C4*C6
    ROcp25_76 = ROcp25_75*C6+S4*S6
    ROcp25_86 = ROcp25_85*C6-C4*S6
    OMcp25_15 = -qd[5]*S4
    OMcp25_25 = qd[5]*C4
    OMcp25_16 = OMcp25_15+ROcp25_15*qd[6]
    OMcp25_26 = OMcp25_25+ROcp25_25*qd[6]
    OMcp25_36 = qd[4]-qd[6]*S5
    OPcp25_16 = ROcp25_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp25_25*S5+ROcp25_25*qd[4])
    OPcp25_26 = ROcp25_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp25_15*S5+ROcp25_15*qd[4])
    OPcp25_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_26_0_8 = = 
 
# Sensor Kinematics 


    ROcp25_423 = ROcp25_46*C23+ROcp25_76*S23
    ROcp25_523 = ROcp25_56*C23+ROcp25_86*S23
    ROcp25_623 = S23p6*C5
    ROcp25_723 = -(ROcp25_46*S23-ROcp25_76*C23)
    ROcp25_823 = -(ROcp25_56*S23-ROcp25_86*C23)
    ROcp25_923 = C23p6*C5
    ROcp25_124 = ROcp25_15*C24+ROcp25_423*S24
    ROcp25_224 = ROcp25_25*C24+ROcp25_523*S24
    ROcp25_324 = ROcp25_623*S24-C24*S5
    ROcp25_424 = -(ROcp25_15*S24-ROcp25_423*C24)
    ROcp25_524 = -(ROcp25_25*S24-ROcp25_523*C24)
    ROcp25_624 = ROcp25_623*C24+S24*S5
    ROcp25_425 = ROcp25_424*C25+ROcp25_723*S25
    ROcp25_525 = ROcp25_524*C25+ROcp25_823*S25
    ROcp25_625 = ROcp25_624*C25+ROcp25_923*S25
    ROcp25_725 = -(ROcp25_424*S25-ROcp25_723*C25)
    ROcp25_825 = -(ROcp25_524*S25-ROcp25_823*C25)
    ROcp25_925 = -(ROcp25_624*S25-ROcp25_923*C25)
    ROcp25_126 = ROcp25_124*C26-ROcp25_725*S26
    ROcp25_226 = ROcp25_224*C26-ROcp25_825*S26
    ROcp25_326 = ROcp25_324*C26-ROcp25_925*S26
    ROcp25_726 = ROcp25_124*S26+ROcp25_725*C26
    ROcp25_826 = ROcp25_224*S26+ROcp25_825*C26
    ROcp25_926 = ROcp25_324*S26+ROcp25_925*C26
    RLcp25_123 = ROcp25_15*s.dpt[1,10]+ROcp25_46*s.dpt[2,10]
    RLcp25_223 = ROcp25_25*s.dpt[1,10]+ROcp25_56*s.dpt[2,10]
    RLcp25_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp25_123 = OMcp25_16+ROcp25_15*qd[23]
    OMcp25_223 = OMcp25_26+ROcp25_25*qd[23]
    OMcp25_323 = OMcp25_36-qd[23]*S5
    ORcp25_123 = OMcp25_26*RLcp25_323-OMcp25_36*RLcp25_223
    ORcp25_223 = -(OMcp25_16*RLcp25_323-OMcp25_36*RLcp25_123)
    ORcp25_323 = OMcp25_16*RLcp25_223-OMcp25_26*RLcp25_123
    OMcp25_124 = OMcp25_123+ROcp25_723*qd[24]
    OMcp25_224 = OMcp25_223+ROcp25_823*qd[24]
    OMcp25_324 = OMcp25_323+ROcp25_923*qd[24]
    OPcp25_124 = OPcp25_16+ROcp25_15*qdd[23]+ROcp25_723*qdd[24]-qd[23]*(OMcp25_26*S5+OMcp25_36*ROcp25_25)+qd[24]*(\
   OMcp25_223*ROcp25_923-OMcp25_323*ROcp25_823)
    OPcp25_224 = OPcp25_26+ROcp25_25*qdd[23]+ROcp25_823*qdd[24]+qd[23]*(OMcp25_16*S5+OMcp25_36*ROcp25_15)-qd[24]*(\
   OMcp25_123*ROcp25_923-OMcp25_323*ROcp25_723)
    OPcp25_324 = OPcp25_36+ROcp25_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp25_16*ROcp25_25-OMcp25_26*ROcp25_15)+qd[24]*(\
   OMcp25_123*ROcp25_823-OMcp25_223*ROcp25_723)
    RLcp25_125 = ROcp25_424*s.dpt[2,26]
    RLcp25_225 = ROcp25_524*s.dpt[2,26]
    RLcp25_325 = ROcp25_624*s.dpt[2,26]
    POcp25_125 = RLcp25_123+RLcp25_125+q[1]
    POcp25_225 = RLcp25_223+RLcp25_225+q[2]
    POcp25_325 = RLcp25_323+RLcp25_325+q[3]
    OMcp25_125 = OMcp25_124+ROcp25_124*qd[25]
    OMcp25_225 = OMcp25_224+ROcp25_224*qd[25]
    OMcp25_325 = OMcp25_324+ROcp25_324*qd[25]
    ORcp25_125 = OMcp25_224*RLcp25_325-OMcp25_324*RLcp25_225
    ORcp25_225 = -(OMcp25_124*RLcp25_325-OMcp25_324*RLcp25_125)
    ORcp25_325 = OMcp25_124*RLcp25_225-OMcp25_224*RLcp25_125
    VIcp25_125 = ORcp25_123+ORcp25_125+qd[1]
    VIcp25_225 = ORcp25_223+ORcp25_225+qd[2]
    VIcp25_325 = ORcp25_323+ORcp25_325+qd[3]
    ACcp25_125 = qdd[1]+OMcp25_224*ORcp25_325+OMcp25_26*ORcp25_323-OMcp25_324*ORcp25_225-OMcp25_36*ORcp25_223+OPcp25_224*\
   RLcp25_325+OPcp25_26*RLcp25_323-OPcp25_324*RLcp25_225-OPcp25_36*RLcp25_223
    ACcp25_225 = qdd[2]-OMcp25_124*ORcp25_325-OMcp25_16*ORcp25_323+OMcp25_324*ORcp25_125+OMcp25_36*ORcp25_123-OPcp25_124*\
   RLcp25_325-OPcp25_16*RLcp25_323+OPcp25_324*RLcp25_125+OPcp25_36*RLcp25_123
    ACcp25_325 = qdd[3]+OMcp25_124*ORcp25_225+OMcp25_16*ORcp25_223-OMcp25_224*ORcp25_125-OMcp25_26*ORcp25_123+OPcp25_124*\
   RLcp25_225+OPcp25_16*RLcp25_223-OPcp25_224*RLcp25_125-OPcp25_26*RLcp25_123
    OMcp25_126 = OMcp25_125+ROcp25_425*qd[26]
    OMcp25_226 = OMcp25_225+ROcp25_525*qd[26]
    OMcp25_326 = OMcp25_325+ROcp25_625*qd[26]
    OPcp25_126 = OPcp25_124+ROcp25_124*qdd[25]+ROcp25_425*qdd[26]+qd[25]*(OMcp25_224*ROcp25_324-OMcp25_324*ROcp25_224)+\
   qd[26]*(OMcp25_225*ROcp25_625-OMcp25_325*ROcp25_525)
    OPcp25_226 = OPcp25_224+ROcp25_224*qdd[25]+ROcp25_525*qdd[26]-qd[25]*(OMcp25_124*ROcp25_324-OMcp25_324*ROcp25_124)-\
   qd[26]*(OMcp25_125*ROcp25_625-OMcp25_325*ROcp25_425)
    OPcp25_326 = OPcp25_324+ROcp25_324*qdd[25]+ROcp25_625*qdd[26]+qd[25]*(OMcp25_124*ROcp25_224-OMcp25_224*ROcp25_124)+\
   qd[26]*(OMcp25_125*ROcp25_525-OMcp25_225*ROcp25_425)

# = = Block_1_0_0_26_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp25_125
    sens.P[2] = POcp25_225
    sens.P[3] = POcp25_325
    sens.R[1,1] = ROcp25_126
    sens.R[1,2] = ROcp25_226
    sens.R[1,3] = ROcp25_326
    sens.R[2,1] = ROcp25_425
    sens.R[2,2] = ROcp25_525
    sens.R[2,3] = ROcp25_625
    sens.R[3,1] = ROcp25_726
    sens.R[3,2] = ROcp25_826
    sens.R[3,3] = ROcp25_926
    sens.V[1] = VIcp25_125
    sens.V[2] = VIcp25_225
    sens.V[3] = VIcp25_325
    sens.OM[1] = OMcp25_126
    sens.OM[2] = OMcp25_226
    sens.OM[3] = OMcp25_326
    sens.A[1] = ACcp25_125
    sens.A[2] = ACcp25_225
    sens.A[3] = ACcp25_325
    sens.OMP[1] = OPcp25_126
    sens.OMP[2] = OPcp25_226
    sens.OMP[3] = OPcp25_326
 
# 
  elif(isens==27): 


# = = Block_1_0_0_27_0_1 = = 
 
# Sensor Kinematics 


    ROcp26_15 = C4*C5
    ROcp26_25 = S4*C5
    ROcp26_75 = C4*S5
    ROcp26_85 = S4*S5
    ROcp26_46 = ROcp26_75*S6-S4*C6
    ROcp26_56 = ROcp26_85*S6+C4*C6
    ROcp26_76 = ROcp26_75*C6+S4*S6
    ROcp26_86 = ROcp26_85*C6-C4*S6
    OMcp26_15 = -qd[5]*S4
    OMcp26_25 = qd[5]*C4
    OMcp26_16 = OMcp26_15+ROcp26_15*qd[6]
    OMcp26_26 = OMcp26_25+ROcp26_25*qd[6]
    OMcp26_36 = qd[4]-qd[6]*S5
    OPcp26_16 = ROcp26_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp26_25*S5+ROcp26_25*qd[4])
    OPcp26_26 = ROcp26_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp26_15*S5+ROcp26_15*qd[4])
    OPcp26_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_27_0_8 = = 
 
# Sensor Kinematics 


    ROcp26_423 = ROcp26_46*C23+ROcp26_76*S23
    ROcp26_523 = ROcp26_56*C23+ROcp26_86*S23
    ROcp26_623 = S23p6*C5
    ROcp26_723 = -(ROcp26_46*S23-ROcp26_76*C23)
    ROcp26_823 = -(ROcp26_56*S23-ROcp26_86*C23)
    ROcp26_923 = C23p6*C5
    ROcp26_124 = ROcp26_15*C24+ROcp26_423*S24
    ROcp26_224 = ROcp26_25*C24+ROcp26_523*S24
    ROcp26_324 = ROcp26_623*S24-C24*S5
    ROcp26_424 = -(ROcp26_15*S24-ROcp26_423*C24)
    ROcp26_524 = -(ROcp26_25*S24-ROcp26_523*C24)
    ROcp26_624 = ROcp26_623*C24+S24*S5
    ROcp26_425 = ROcp26_424*C25+ROcp26_723*S25
    ROcp26_525 = ROcp26_524*C25+ROcp26_823*S25
    ROcp26_625 = ROcp26_624*C25+ROcp26_923*S25
    ROcp26_725 = -(ROcp26_424*S25-ROcp26_723*C25)
    ROcp26_825 = -(ROcp26_524*S25-ROcp26_823*C25)
    ROcp26_925 = -(ROcp26_624*S25-ROcp26_923*C25)
    ROcp26_126 = ROcp26_124*C26-ROcp26_725*S26
    ROcp26_226 = ROcp26_224*C26-ROcp26_825*S26
    ROcp26_326 = ROcp26_324*C26-ROcp26_925*S26
    ROcp26_726 = ROcp26_124*S26+ROcp26_725*C26
    ROcp26_826 = ROcp26_224*S26+ROcp26_825*C26
    ROcp26_926 = ROcp26_324*S26+ROcp26_925*C26
    ROcp26_127 = ROcp26_126*C27+ROcp26_425*S27
    ROcp26_227 = ROcp26_226*C27+ROcp26_525*S27
    ROcp26_327 = ROcp26_326*C27+ROcp26_625*S27
    ROcp26_427 = -(ROcp26_126*S27-ROcp26_425*C27)
    ROcp26_527 = -(ROcp26_226*S27-ROcp26_525*C27)
    ROcp26_627 = -(ROcp26_326*S27-ROcp26_625*C27)
    RLcp26_123 = ROcp26_15*s.dpt[1,10]+ROcp26_46*s.dpt[2,10]
    RLcp26_223 = ROcp26_25*s.dpt[1,10]+ROcp26_56*s.dpt[2,10]
    RLcp26_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp26_123 = OMcp26_16+ROcp26_15*qd[23]
    OMcp26_223 = OMcp26_26+ROcp26_25*qd[23]
    OMcp26_323 = OMcp26_36-qd[23]*S5
    ORcp26_123 = OMcp26_26*RLcp26_323-OMcp26_36*RLcp26_223
    ORcp26_223 = -(OMcp26_16*RLcp26_323-OMcp26_36*RLcp26_123)
    ORcp26_323 = OMcp26_16*RLcp26_223-OMcp26_26*RLcp26_123
    OMcp26_124 = OMcp26_123+ROcp26_723*qd[24]
    OMcp26_224 = OMcp26_223+ROcp26_823*qd[24]
    OMcp26_324 = OMcp26_323+ROcp26_923*qd[24]
    OPcp26_124 = OPcp26_16+ROcp26_15*qdd[23]+ROcp26_723*qdd[24]-qd[23]*(OMcp26_26*S5+OMcp26_36*ROcp26_25)+qd[24]*(\
   OMcp26_223*ROcp26_923-OMcp26_323*ROcp26_823)
    OPcp26_224 = OPcp26_26+ROcp26_25*qdd[23]+ROcp26_823*qdd[24]+qd[23]*(OMcp26_16*S5+OMcp26_36*ROcp26_15)-qd[24]*(\
   OMcp26_123*ROcp26_923-OMcp26_323*ROcp26_723)
    OPcp26_324 = OPcp26_36+ROcp26_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp26_16*ROcp26_25-OMcp26_26*ROcp26_15)+qd[24]*(\
   OMcp26_123*ROcp26_823-OMcp26_223*ROcp26_723)
    RLcp26_125 = ROcp26_424*s.dpt[2,26]
    RLcp26_225 = ROcp26_524*s.dpt[2,26]
    RLcp26_325 = ROcp26_624*s.dpt[2,26]
    POcp26_125 = RLcp26_123+RLcp26_125+q[1]
    POcp26_225 = RLcp26_223+RLcp26_225+q[2]
    POcp26_325 = RLcp26_323+RLcp26_325+q[3]
    OMcp26_125 = OMcp26_124+ROcp26_124*qd[25]
    OMcp26_225 = OMcp26_224+ROcp26_224*qd[25]
    OMcp26_325 = OMcp26_324+ROcp26_324*qd[25]
    ORcp26_125 = OMcp26_224*RLcp26_325-OMcp26_324*RLcp26_225
    ORcp26_225 = -(OMcp26_124*RLcp26_325-OMcp26_324*RLcp26_125)
    ORcp26_325 = OMcp26_124*RLcp26_225-OMcp26_224*RLcp26_125
    VIcp26_125 = ORcp26_123+ORcp26_125+qd[1]
    VIcp26_225 = ORcp26_223+ORcp26_225+qd[2]
    VIcp26_325 = ORcp26_323+ORcp26_325+qd[3]
    ACcp26_125 = qdd[1]+OMcp26_224*ORcp26_325+OMcp26_26*ORcp26_323-OMcp26_324*ORcp26_225-OMcp26_36*ORcp26_223+OPcp26_224*\
   RLcp26_325+OPcp26_26*RLcp26_323-OPcp26_324*RLcp26_225-OPcp26_36*RLcp26_223
    ACcp26_225 = qdd[2]-OMcp26_124*ORcp26_325-OMcp26_16*ORcp26_323+OMcp26_324*ORcp26_125+OMcp26_36*ORcp26_123-OPcp26_124*\
   RLcp26_325-OPcp26_16*RLcp26_323+OPcp26_324*RLcp26_125+OPcp26_36*RLcp26_123
    ACcp26_325 = qdd[3]+OMcp26_124*ORcp26_225+OMcp26_16*ORcp26_223-OMcp26_224*ORcp26_125-OMcp26_26*ORcp26_123+OPcp26_124*\
   RLcp26_225+OPcp26_16*RLcp26_223-OPcp26_224*RLcp26_125-OPcp26_26*RLcp26_123
    OMcp26_126 = OMcp26_125+ROcp26_425*qd[26]
    OMcp26_226 = OMcp26_225+ROcp26_525*qd[26]
    OMcp26_326 = OMcp26_325+ROcp26_625*qd[26]
    OMcp26_127 = OMcp26_126+ROcp26_726*qd[27]
    OMcp26_227 = OMcp26_226+ROcp26_826*qd[27]
    OMcp26_327 = OMcp26_326+ROcp26_926*qd[27]
    OPcp26_127 = OPcp26_124+ROcp26_124*qdd[25]+ROcp26_425*qdd[26]+ROcp26_726*qdd[27]+qd[25]*(OMcp26_224*ROcp26_324-\
   OMcp26_324*ROcp26_224)+qd[26]*(OMcp26_225*ROcp26_625-OMcp26_325*ROcp26_525)+qd[27]*(OMcp26_226*ROcp26_926-OMcp26_326*\
   ROcp26_826)
    OPcp26_227 = OPcp26_224+ROcp26_224*qdd[25]+ROcp26_525*qdd[26]+ROcp26_826*qdd[27]-qd[25]*(OMcp26_124*ROcp26_324-\
   OMcp26_324*ROcp26_124)-qd[26]*(OMcp26_125*ROcp26_625-OMcp26_325*ROcp26_425)-qd[27]*(OMcp26_126*ROcp26_926-OMcp26_326*\
   ROcp26_726)
    OPcp26_327 = OPcp26_324+ROcp26_324*qdd[25]+ROcp26_625*qdd[26]+ROcp26_926*qdd[27]+qd[25]*(OMcp26_124*ROcp26_224-\
   OMcp26_224*ROcp26_124)+qd[26]*(OMcp26_125*ROcp26_525-OMcp26_225*ROcp26_425)+qd[27]*(OMcp26_126*ROcp26_826-OMcp26_226*\
   ROcp26_726)

# = = Block_1_0_0_27_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp26_125
    sens.P[2] = POcp26_225
    sens.P[3] = POcp26_325
    sens.R[1,1] = ROcp26_127
    sens.R[1,2] = ROcp26_227
    sens.R[1,3] = ROcp26_327
    sens.R[2,1] = ROcp26_427
    sens.R[2,2] = ROcp26_527
    sens.R[2,3] = ROcp26_627
    sens.R[3,1] = ROcp26_726
    sens.R[3,2] = ROcp26_826
    sens.R[3,3] = ROcp26_926
    sens.V[1] = VIcp26_125
    sens.V[2] = VIcp26_225
    sens.V[3] = VIcp26_325
    sens.OM[1] = OMcp26_127
    sens.OM[2] = OMcp26_227
    sens.OM[3] = OMcp26_327
    sens.A[1] = ACcp26_125
    sens.A[2] = ACcp26_225
    sens.A[3] = ACcp26_325
    sens.OMP[1] = OPcp26_127
    sens.OMP[2] = OPcp26_227
    sens.OMP[3] = OPcp26_327
 
# 
  elif(isens==28): 


# = = Block_1_0_0_28_0_1 = = 
 
# Sensor Kinematics 


    ROcp27_15 = C4*C5
    ROcp27_25 = S4*C5
    ROcp27_75 = C4*S5
    ROcp27_85 = S4*S5
    ROcp27_46 = ROcp27_75*S6-S4*C6
    ROcp27_56 = ROcp27_85*S6+C4*C6
    ROcp27_76 = ROcp27_75*C6+S4*S6
    ROcp27_86 = ROcp27_85*C6-C4*S6
    OMcp27_15 = -qd[5]*S4
    OMcp27_25 = qd[5]*C4
    OMcp27_16 = OMcp27_15+ROcp27_15*qd[6]
    OMcp27_26 = OMcp27_25+ROcp27_25*qd[6]
    OMcp27_36 = qd[4]-qd[6]*S5
    OPcp27_16 = ROcp27_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp27_25*S5+ROcp27_25*qd[4])
    OPcp27_26 = ROcp27_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp27_15*S5+ROcp27_15*qd[4])
    OPcp27_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_28_0_8 = = 
 
# Sensor Kinematics 


    ROcp27_423 = ROcp27_46*C23+ROcp27_76*S23
    ROcp27_523 = ROcp27_56*C23+ROcp27_86*S23
    ROcp27_623 = S23p6*C5
    ROcp27_723 = -(ROcp27_46*S23-ROcp27_76*C23)
    ROcp27_823 = -(ROcp27_56*S23-ROcp27_86*C23)
    ROcp27_923 = C23p6*C5
    ROcp27_124 = ROcp27_15*C24+ROcp27_423*S24
    ROcp27_224 = ROcp27_25*C24+ROcp27_523*S24
    ROcp27_324 = ROcp27_623*S24-C24*S5
    ROcp27_424 = -(ROcp27_15*S24-ROcp27_423*C24)
    ROcp27_524 = -(ROcp27_25*S24-ROcp27_523*C24)
    ROcp27_624 = ROcp27_623*C24+S24*S5
    ROcp27_425 = ROcp27_424*C25+ROcp27_723*S25
    ROcp27_525 = ROcp27_524*C25+ROcp27_823*S25
    ROcp27_625 = ROcp27_624*C25+ROcp27_923*S25
    ROcp27_725 = -(ROcp27_424*S25-ROcp27_723*C25)
    ROcp27_825 = -(ROcp27_524*S25-ROcp27_823*C25)
    ROcp27_925 = -(ROcp27_624*S25-ROcp27_923*C25)
    ROcp27_126 = ROcp27_124*C26-ROcp27_725*S26
    ROcp27_226 = ROcp27_224*C26-ROcp27_825*S26
    ROcp27_326 = ROcp27_324*C26-ROcp27_925*S26
    ROcp27_726 = ROcp27_124*S26+ROcp27_725*C26
    ROcp27_826 = ROcp27_224*S26+ROcp27_825*C26
    ROcp27_926 = ROcp27_324*S26+ROcp27_925*C26
    ROcp27_127 = ROcp27_126*C27+ROcp27_425*S27
    ROcp27_227 = ROcp27_226*C27+ROcp27_525*S27
    ROcp27_327 = ROcp27_326*C27+ROcp27_625*S27
    ROcp27_427 = -(ROcp27_126*S27-ROcp27_425*C27)
    ROcp27_527 = -(ROcp27_226*S27-ROcp27_525*C27)
    ROcp27_627 = -(ROcp27_326*S27-ROcp27_625*C27)
    RLcp27_123 = ROcp27_15*s.dpt[1,10]+ROcp27_46*s.dpt[2,10]
    RLcp27_223 = ROcp27_25*s.dpt[1,10]+ROcp27_56*s.dpt[2,10]
    RLcp27_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp27_123 = OMcp27_16+ROcp27_15*qd[23]
    OMcp27_223 = OMcp27_26+ROcp27_25*qd[23]
    OMcp27_323 = OMcp27_36-qd[23]*S5
    ORcp27_123 = OMcp27_26*RLcp27_323-OMcp27_36*RLcp27_223
    ORcp27_223 = -(OMcp27_16*RLcp27_323-OMcp27_36*RLcp27_123)
    ORcp27_323 = OMcp27_16*RLcp27_223-OMcp27_26*RLcp27_123
    OMcp27_124 = OMcp27_123+ROcp27_723*qd[24]
    OMcp27_224 = OMcp27_223+ROcp27_823*qd[24]
    OMcp27_324 = OMcp27_323+ROcp27_923*qd[24]
    OPcp27_124 = OPcp27_16+ROcp27_15*qdd[23]+ROcp27_723*qdd[24]-qd[23]*(OMcp27_26*S5+OMcp27_36*ROcp27_25)+qd[24]*(\
   OMcp27_223*ROcp27_923-OMcp27_323*ROcp27_823)
    OPcp27_224 = OPcp27_26+ROcp27_25*qdd[23]+ROcp27_823*qdd[24]+qd[23]*(OMcp27_16*S5+OMcp27_36*ROcp27_15)-qd[24]*(\
   OMcp27_123*ROcp27_923-OMcp27_323*ROcp27_723)
    OPcp27_324 = OPcp27_36+ROcp27_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp27_16*ROcp27_25-OMcp27_26*ROcp27_15)+qd[24]*(\
   OMcp27_123*ROcp27_823-OMcp27_223*ROcp27_723)
    RLcp27_125 = ROcp27_424*s.dpt[2,26]
    RLcp27_225 = ROcp27_524*s.dpt[2,26]
    RLcp27_325 = ROcp27_624*s.dpt[2,26]
    OMcp27_125 = OMcp27_124+ROcp27_124*qd[25]
    OMcp27_225 = OMcp27_224+ROcp27_224*qd[25]
    OMcp27_325 = OMcp27_324+ROcp27_324*qd[25]
    ORcp27_125 = OMcp27_224*RLcp27_325-OMcp27_324*RLcp27_225
    ORcp27_225 = -(OMcp27_124*RLcp27_325-OMcp27_324*RLcp27_125)
    ORcp27_325 = OMcp27_124*RLcp27_225-OMcp27_224*RLcp27_125
    OMcp27_126 = OMcp27_125+ROcp27_425*qd[26]
    OMcp27_226 = OMcp27_225+ROcp27_525*qd[26]
    OMcp27_326 = OMcp27_325+ROcp27_625*qd[26]
    OMcp27_127 = OMcp27_126+ROcp27_726*qd[27]
    OMcp27_227 = OMcp27_226+ROcp27_826*qd[27]
    OMcp27_327 = OMcp27_326+ROcp27_926*qd[27]
    OPcp27_127 = OPcp27_124+ROcp27_124*qdd[25]+ROcp27_425*qdd[26]+ROcp27_726*qdd[27]+qd[25]*(OMcp27_224*ROcp27_324-\
   OMcp27_324*ROcp27_224)+qd[26]*(OMcp27_225*ROcp27_625-OMcp27_325*ROcp27_525)+qd[27]*(OMcp27_226*ROcp27_926-OMcp27_326*\
   ROcp27_826)
    OPcp27_227 = OPcp27_224+ROcp27_224*qdd[25]+ROcp27_525*qdd[26]+ROcp27_826*qdd[27]-qd[25]*(OMcp27_124*ROcp27_324-\
   OMcp27_324*ROcp27_124)-qd[26]*(OMcp27_125*ROcp27_625-OMcp27_325*ROcp27_425)-qd[27]*(OMcp27_126*ROcp27_926-OMcp27_326*\
   ROcp27_726)
    OPcp27_327 = OPcp27_324+ROcp27_324*qdd[25]+ROcp27_625*qdd[26]+ROcp27_926*qdd[27]+qd[25]*(OMcp27_124*ROcp27_224-\
   OMcp27_224*ROcp27_124)+qd[26]*(OMcp27_125*ROcp27_525-OMcp27_225*ROcp27_425)+qd[27]*(OMcp27_126*ROcp27_826-OMcp27_226*\
   ROcp27_726)

# = = Block_1_0_0_28_0_9 = = 
 
# Sensor Kinematics 


    ROcp27_428 = ROcp27_427*C28+ROcp27_726*S28
    ROcp27_528 = ROcp27_527*C28+ROcp27_826*S28
    ROcp27_628 = ROcp27_627*C28+ROcp27_926*S28
    ROcp27_728 = -(ROcp27_427*S28-ROcp27_726*C28)
    ROcp27_828 = -(ROcp27_527*S28-ROcp27_826*C28)
    ROcp27_928 = -(ROcp27_627*S28-ROcp27_926*C28)
    RLcp27_128 = ROcp27_726*s.dpt[3,27]
    RLcp27_228 = ROcp27_826*s.dpt[3,27]
    RLcp27_328 = ROcp27_926*s.dpt[3,27]
    POcp27_128 = RLcp27_123+RLcp27_125+RLcp27_128+q[1]
    POcp27_228 = RLcp27_223+RLcp27_225+RLcp27_228+q[2]
    POcp27_328 = RLcp27_323+RLcp27_325+RLcp27_328+q[3]
    OMcp27_128 = OMcp27_127+ROcp27_127*qd[28]
    OMcp27_228 = OMcp27_227+ROcp27_227*qd[28]
    OMcp27_328 = OMcp27_327+ROcp27_327*qd[28]
    ORcp27_128 = OMcp27_227*RLcp27_328-OMcp27_327*RLcp27_228
    ORcp27_228 = -(OMcp27_127*RLcp27_328-OMcp27_327*RLcp27_128)
    ORcp27_328 = OMcp27_127*RLcp27_228-OMcp27_227*RLcp27_128
    VIcp27_128 = ORcp27_123+ORcp27_125+ORcp27_128+qd[1]
    VIcp27_228 = ORcp27_223+ORcp27_225+ORcp27_228+qd[2]
    VIcp27_328 = ORcp27_323+ORcp27_325+ORcp27_328+qd[3]
    OPcp27_128 = OPcp27_127+ROcp27_127*qdd[28]+qd[28]*(OMcp27_227*ROcp27_327-OMcp27_327*ROcp27_227)
    OPcp27_228 = OPcp27_227+ROcp27_227*qdd[28]-qd[28]*(OMcp27_127*ROcp27_327-OMcp27_327*ROcp27_127)
    OPcp27_328 = OPcp27_327+ROcp27_327*qdd[28]+qd[28]*(OMcp27_127*ROcp27_227-OMcp27_227*ROcp27_127)
    ACcp27_128 = qdd[1]+OMcp27_224*ORcp27_325+OMcp27_227*ORcp27_328+OMcp27_26*ORcp27_323-OMcp27_324*ORcp27_225-OMcp27_327*\
   ORcp27_228-OMcp27_36*ORcp27_223+OPcp27_224*RLcp27_325+OPcp27_227*RLcp27_328+OPcp27_26*RLcp27_323-OPcp27_324*RLcp27_225-\
   OPcp27_327*RLcp27_228-OPcp27_36*RLcp27_223
    ACcp27_228 = qdd[2]-OMcp27_124*ORcp27_325-OMcp27_127*ORcp27_328-OMcp27_16*ORcp27_323+OMcp27_324*ORcp27_125+OMcp27_327*\
   ORcp27_128+OMcp27_36*ORcp27_123-OPcp27_124*RLcp27_325-OPcp27_127*RLcp27_328-OPcp27_16*RLcp27_323+OPcp27_324*RLcp27_125+\
   OPcp27_327*RLcp27_128+OPcp27_36*RLcp27_123
    ACcp27_328 = qdd[3]+OMcp27_124*ORcp27_225+OMcp27_127*ORcp27_228+OMcp27_16*ORcp27_223-OMcp27_224*ORcp27_125-OMcp27_227*\
   ORcp27_128-OMcp27_26*ORcp27_123+OPcp27_124*RLcp27_225+OPcp27_127*RLcp27_228+OPcp27_16*RLcp27_223-OPcp27_224*RLcp27_125-\
   OPcp27_227*RLcp27_128-OPcp27_26*RLcp27_123

# = = Block_1_0_0_28_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp27_128
    sens.P[2] = POcp27_228
    sens.P[3] = POcp27_328
    sens.R[1,1] = ROcp27_127
    sens.R[1,2] = ROcp27_227
    sens.R[1,3] = ROcp27_327
    sens.R[2,1] = ROcp27_428
    sens.R[2,2] = ROcp27_528
    sens.R[2,3] = ROcp27_628
    sens.R[3,1] = ROcp27_728
    sens.R[3,2] = ROcp27_828
    sens.R[3,3] = ROcp27_928
    sens.V[1] = VIcp27_128
    sens.V[2] = VIcp27_228
    sens.V[3] = VIcp27_328
    sens.OM[1] = OMcp27_128
    sens.OM[2] = OMcp27_228
    sens.OM[3] = OMcp27_328
    sens.A[1] = ACcp27_128
    sens.A[2] = ACcp27_228
    sens.A[3] = ACcp27_328
    sens.OMP[1] = OPcp27_128
    sens.OMP[2] = OPcp27_228
    sens.OMP[3] = OPcp27_328
 
# 
  elif(isens==29): 


# = = Block_1_0_0_29_0_1 = = 
 
# Sensor Kinematics 


    ROcp28_15 = C4*C5
    ROcp28_25 = S4*C5
    ROcp28_75 = C4*S5
    ROcp28_85 = S4*S5
    ROcp28_46 = ROcp28_75*S6-S4*C6
    ROcp28_56 = ROcp28_85*S6+C4*C6
    ROcp28_76 = ROcp28_75*C6+S4*S6
    ROcp28_86 = ROcp28_85*C6-C4*S6
    OMcp28_15 = -qd[5]*S4
    OMcp28_25 = qd[5]*C4
    OMcp28_16 = OMcp28_15+ROcp28_15*qd[6]
    OMcp28_26 = OMcp28_25+ROcp28_25*qd[6]
    OMcp28_36 = qd[4]-qd[6]*S5
    OPcp28_16 = ROcp28_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp28_25*S5+ROcp28_25*qd[4])
    OPcp28_26 = ROcp28_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp28_15*S5+ROcp28_15*qd[4])
    OPcp28_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_29_0_8 = = 
 
# Sensor Kinematics 


    ROcp28_423 = ROcp28_46*C23+ROcp28_76*S23
    ROcp28_523 = ROcp28_56*C23+ROcp28_86*S23
    ROcp28_623 = S23p6*C5
    ROcp28_723 = -(ROcp28_46*S23-ROcp28_76*C23)
    ROcp28_823 = -(ROcp28_56*S23-ROcp28_86*C23)
    ROcp28_923 = C23p6*C5
    ROcp28_124 = ROcp28_15*C24+ROcp28_423*S24
    ROcp28_224 = ROcp28_25*C24+ROcp28_523*S24
    ROcp28_324 = ROcp28_623*S24-C24*S5
    ROcp28_424 = -(ROcp28_15*S24-ROcp28_423*C24)
    ROcp28_524 = -(ROcp28_25*S24-ROcp28_523*C24)
    ROcp28_624 = ROcp28_623*C24+S24*S5
    ROcp28_425 = ROcp28_424*C25+ROcp28_723*S25
    ROcp28_525 = ROcp28_524*C25+ROcp28_823*S25
    ROcp28_625 = ROcp28_624*C25+ROcp28_923*S25
    ROcp28_725 = -(ROcp28_424*S25-ROcp28_723*C25)
    ROcp28_825 = -(ROcp28_524*S25-ROcp28_823*C25)
    ROcp28_925 = -(ROcp28_624*S25-ROcp28_923*C25)
    ROcp28_126 = ROcp28_124*C26-ROcp28_725*S26
    ROcp28_226 = ROcp28_224*C26-ROcp28_825*S26
    ROcp28_326 = ROcp28_324*C26-ROcp28_925*S26
    ROcp28_726 = ROcp28_124*S26+ROcp28_725*C26
    ROcp28_826 = ROcp28_224*S26+ROcp28_825*C26
    ROcp28_926 = ROcp28_324*S26+ROcp28_925*C26
    ROcp28_127 = ROcp28_126*C27+ROcp28_425*S27
    ROcp28_227 = ROcp28_226*C27+ROcp28_525*S27
    ROcp28_327 = ROcp28_326*C27+ROcp28_625*S27
    ROcp28_427 = -(ROcp28_126*S27-ROcp28_425*C27)
    ROcp28_527 = -(ROcp28_226*S27-ROcp28_525*C27)
    ROcp28_627 = -(ROcp28_326*S27-ROcp28_625*C27)
    RLcp28_123 = ROcp28_15*s.dpt[1,10]+ROcp28_46*s.dpt[2,10]
    RLcp28_223 = ROcp28_25*s.dpt[1,10]+ROcp28_56*s.dpt[2,10]
    RLcp28_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp28_123 = OMcp28_16+ROcp28_15*qd[23]
    OMcp28_223 = OMcp28_26+ROcp28_25*qd[23]
    OMcp28_323 = OMcp28_36-qd[23]*S5
    ORcp28_123 = OMcp28_26*RLcp28_323-OMcp28_36*RLcp28_223
    ORcp28_223 = -(OMcp28_16*RLcp28_323-OMcp28_36*RLcp28_123)
    ORcp28_323 = OMcp28_16*RLcp28_223-OMcp28_26*RLcp28_123
    OMcp28_124 = OMcp28_123+ROcp28_723*qd[24]
    OMcp28_224 = OMcp28_223+ROcp28_823*qd[24]
    OMcp28_324 = OMcp28_323+ROcp28_923*qd[24]
    OPcp28_124 = OPcp28_16+ROcp28_15*qdd[23]+ROcp28_723*qdd[24]-qd[23]*(OMcp28_26*S5+OMcp28_36*ROcp28_25)+qd[24]*(\
   OMcp28_223*ROcp28_923-OMcp28_323*ROcp28_823)
    OPcp28_224 = OPcp28_26+ROcp28_25*qdd[23]+ROcp28_823*qdd[24]+qd[23]*(OMcp28_16*S5+OMcp28_36*ROcp28_15)-qd[24]*(\
   OMcp28_123*ROcp28_923-OMcp28_323*ROcp28_723)
    OPcp28_324 = OPcp28_36+ROcp28_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp28_16*ROcp28_25-OMcp28_26*ROcp28_15)+qd[24]*(\
   OMcp28_123*ROcp28_823-OMcp28_223*ROcp28_723)
    RLcp28_125 = ROcp28_424*s.dpt[2,26]
    RLcp28_225 = ROcp28_524*s.dpt[2,26]
    RLcp28_325 = ROcp28_624*s.dpt[2,26]
    OMcp28_125 = OMcp28_124+ROcp28_124*qd[25]
    OMcp28_225 = OMcp28_224+ROcp28_224*qd[25]
    OMcp28_325 = OMcp28_324+ROcp28_324*qd[25]
    ORcp28_125 = OMcp28_224*RLcp28_325-OMcp28_324*RLcp28_225
    ORcp28_225 = -(OMcp28_124*RLcp28_325-OMcp28_324*RLcp28_125)
    ORcp28_325 = OMcp28_124*RLcp28_225-OMcp28_224*RLcp28_125
    OMcp28_126 = OMcp28_125+ROcp28_425*qd[26]
    OMcp28_226 = OMcp28_225+ROcp28_525*qd[26]
    OMcp28_326 = OMcp28_325+ROcp28_625*qd[26]
    OMcp28_127 = OMcp28_126+ROcp28_726*qd[27]
    OMcp28_227 = OMcp28_226+ROcp28_826*qd[27]
    OMcp28_327 = OMcp28_326+ROcp28_926*qd[27]
    OPcp28_127 = OPcp28_124+ROcp28_124*qdd[25]+ROcp28_425*qdd[26]+ROcp28_726*qdd[27]+qd[25]*(OMcp28_224*ROcp28_324-\
   OMcp28_324*ROcp28_224)+qd[26]*(OMcp28_225*ROcp28_625-OMcp28_325*ROcp28_525)+qd[27]*(OMcp28_226*ROcp28_926-OMcp28_326*\
   ROcp28_826)
    OPcp28_227 = OPcp28_224+ROcp28_224*qdd[25]+ROcp28_525*qdd[26]+ROcp28_826*qdd[27]-qd[25]*(OMcp28_124*ROcp28_324-\
   OMcp28_324*ROcp28_124)-qd[26]*(OMcp28_125*ROcp28_625-OMcp28_325*ROcp28_425)-qd[27]*(OMcp28_126*ROcp28_926-OMcp28_326*\
   ROcp28_726)
    OPcp28_327 = OPcp28_324+ROcp28_324*qdd[25]+ROcp28_625*qdd[26]+ROcp28_926*qdd[27]+qd[25]*(OMcp28_124*ROcp28_224-\
   OMcp28_224*ROcp28_124)+qd[26]*(OMcp28_125*ROcp28_525-OMcp28_225*ROcp28_425)+qd[27]*(OMcp28_126*ROcp28_826-OMcp28_226*\
   ROcp28_726)

# = = Block_1_0_0_29_0_9 = = 
 
# Sensor Kinematics 


    ROcp28_428 = ROcp28_427*C28+ROcp28_726*S28
    ROcp28_528 = ROcp28_527*C28+ROcp28_826*S28
    ROcp28_628 = ROcp28_627*C28+ROcp28_926*S28
    ROcp28_728 = -(ROcp28_427*S28-ROcp28_726*C28)
    ROcp28_828 = -(ROcp28_527*S28-ROcp28_826*C28)
    ROcp28_928 = -(ROcp28_627*S28-ROcp28_926*C28)
    RLcp28_128 = ROcp28_726*s.dpt[3,27]
    RLcp28_228 = ROcp28_826*s.dpt[3,27]
    RLcp28_328 = ROcp28_926*s.dpt[3,27]
    OMcp28_128 = OMcp28_127+ROcp28_127*qd[28]
    OMcp28_228 = OMcp28_227+ROcp28_227*qd[28]
    OMcp28_328 = OMcp28_327+ROcp28_327*qd[28]
    ORcp28_128 = OMcp28_227*RLcp28_328-OMcp28_327*RLcp28_228
    ORcp28_228 = -(OMcp28_127*RLcp28_328-OMcp28_327*RLcp28_128)
    ORcp28_328 = OMcp28_127*RLcp28_228-OMcp28_227*RLcp28_128
    OPcp28_128 = OPcp28_127+ROcp28_127*qdd[28]+qd[28]*(OMcp28_227*ROcp28_327-OMcp28_327*ROcp28_227)
    OPcp28_228 = OPcp28_227+ROcp28_227*qdd[28]-qd[28]*(OMcp28_127*ROcp28_327-OMcp28_327*ROcp28_127)
    OPcp28_328 = OPcp28_327+ROcp28_327*qdd[28]+qd[28]*(OMcp28_127*ROcp28_227-OMcp28_227*ROcp28_127)
    RLcp28_129 = ROcp28_728*q[29]
    RLcp28_229 = ROcp28_828*q[29]
    RLcp28_329 = ROcp28_928*q[29]
    POcp28_129 = RLcp28_123+RLcp28_125+RLcp28_128+RLcp28_129+q[1]
    POcp28_229 = RLcp28_223+RLcp28_225+RLcp28_228+RLcp28_229+q[2]
    POcp28_329 = RLcp28_323+RLcp28_325+RLcp28_328+RLcp28_329+q[3]
    ORcp28_129 = OMcp28_228*RLcp28_329-OMcp28_328*RLcp28_229
    ORcp28_229 = -(OMcp28_128*RLcp28_329-OMcp28_328*RLcp28_129)
    ORcp28_329 = OMcp28_128*RLcp28_229-OMcp28_228*RLcp28_129
    VIcp28_129 = ORcp28_123+ORcp28_125+ORcp28_128+ORcp28_129+qd[1]+ROcp28_728*qd[29]
    VIcp28_229 = ORcp28_223+ORcp28_225+ORcp28_228+ORcp28_229+qd[2]+ROcp28_828*qd[29]
    VIcp28_329 = ORcp28_323+ORcp28_325+ORcp28_328+ORcp28_329+qd[3]+ROcp28_928*qd[29]
    ACcp28_129 = qdd[1]+OMcp28_224*ORcp28_325+OMcp28_227*ORcp28_328+OMcp28_228*ORcp28_329+OMcp28_26*ORcp28_323-OMcp28_324*\
   ORcp28_225-OMcp28_327*ORcp28_228-OMcp28_328*ORcp28_229-OMcp28_36*ORcp28_223+OPcp28_224*RLcp28_325+OPcp28_227*RLcp28_328+\
   OPcp28_228*RLcp28_329+OPcp28_26*RLcp28_323-OPcp28_324*RLcp28_225-OPcp28_327*RLcp28_228-OPcp28_328*RLcp28_229-OPcp28_36*\
   RLcp28_223+ROcp28_728*qdd[29]+(2.0)*qd[29]*(OMcp28_228*ROcp28_928-OMcp28_328*ROcp28_828)
    ACcp28_229 = qdd[2]-OMcp28_124*ORcp28_325-OMcp28_127*ORcp28_328-OMcp28_128*ORcp28_329-OMcp28_16*ORcp28_323+OMcp28_324*\
   ORcp28_125+OMcp28_327*ORcp28_128+OMcp28_328*ORcp28_129+OMcp28_36*ORcp28_123-OPcp28_124*RLcp28_325-OPcp28_127*RLcp28_328-\
   OPcp28_128*RLcp28_329-OPcp28_16*RLcp28_323+OPcp28_324*RLcp28_125+OPcp28_327*RLcp28_128+OPcp28_328*RLcp28_129+OPcp28_36*\
   RLcp28_123+ROcp28_828*qdd[29]-(2.0)*qd[29]*(OMcp28_128*ROcp28_928-OMcp28_328*ROcp28_728)
    ACcp28_329 = qdd[3]+OMcp28_124*ORcp28_225+OMcp28_127*ORcp28_228+OMcp28_128*ORcp28_229+OMcp28_16*ORcp28_223-OMcp28_224*\
   ORcp28_125-OMcp28_227*ORcp28_128-OMcp28_228*ORcp28_129-OMcp28_26*ORcp28_123+OPcp28_124*RLcp28_225+OPcp28_127*RLcp28_228+\
   OPcp28_128*RLcp28_229+OPcp28_16*RLcp28_223-OPcp28_224*RLcp28_125-OPcp28_227*RLcp28_128-OPcp28_228*RLcp28_129-OPcp28_26*\
   RLcp28_123+ROcp28_928*qdd[29]+(2.0)*qd[29]*(OMcp28_128*ROcp28_828-OMcp28_228*ROcp28_728)

# = = Block_1_0_0_29_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp28_129
    sens.P[2] = POcp28_229
    sens.P[3] = POcp28_329
    sens.R[1,1] = ROcp28_127
    sens.R[1,2] = ROcp28_227
    sens.R[1,3] = ROcp28_327
    sens.R[2,1] = ROcp28_428
    sens.R[2,2] = ROcp28_528
    sens.R[2,3] = ROcp28_628
    sens.R[3,1] = ROcp28_728
    sens.R[3,2] = ROcp28_828
    sens.R[3,3] = ROcp28_928
    sens.V[1] = VIcp28_129
    sens.V[2] = VIcp28_229
    sens.V[3] = VIcp28_329
    sens.OM[1] = OMcp28_128
    sens.OM[2] = OMcp28_228
    sens.OM[3] = OMcp28_328
    sens.A[1] = ACcp28_129
    sens.A[2] = ACcp28_229
    sens.A[3] = ACcp28_329
    sens.OMP[1] = OPcp28_128
    sens.OMP[2] = OPcp28_228
    sens.OMP[3] = OPcp28_328
 
# 
  elif(isens==30): 


# = = Block_1_0_0_30_0_1 = = 
 
# Sensor Kinematics 


    ROcp29_15 = C4*C5
    ROcp29_25 = S4*C5
    ROcp29_75 = C4*S5
    ROcp29_85 = S4*S5
    ROcp29_46 = ROcp29_75*S6-S4*C6
    ROcp29_56 = ROcp29_85*S6+C4*C6
    ROcp29_76 = ROcp29_75*C6+S4*S6
    ROcp29_86 = ROcp29_85*C6-C4*S6
    OMcp29_15 = -qd[5]*S4
    OMcp29_25 = qd[5]*C4
    OMcp29_16 = OMcp29_15+ROcp29_15*qd[6]
    OMcp29_26 = OMcp29_25+ROcp29_25*qd[6]
    OMcp29_36 = qd[4]-qd[6]*S5
    OPcp29_16 = ROcp29_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp29_25*S5+ROcp29_25*qd[4])
    OPcp29_26 = ROcp29_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp29_15*S5+ROcp29_15*qd[4])
    OPcp29_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_30_0_8 = = 
 
# Sensor Kinematics 


    ROcp29_423 = ROcp29_46*C23+ROcp29_76*S23
    ROcp29_523 = ROcp29_56*C23+ROcp29_86*S23
    ROcp29_623 = S23p6*C5
    ROcp29_723 = -(ROcp29_46*S23-ROcp29_76*C23)
    ROcp29_823 = -(ROcp29_56*S23-ROcp29_86*C23)
    ROcp29_923 = C23p6*C5
    ROcp29_124 = ROcp29_15*C24+ROcp29_423*S24
    ROcp29_224 = ROcp29_25*C24+ROcp29_523*S24
    ROcp29_324 = ROcp29_623*S24-C24*S5
    ROcp29_424 = -(ROcp29_15*S24-ROcp29_423*C24)
    ROcp29_524 = -(ROcp29_25*S24-ROcp29_523*C24)
    ROcp29_624 = ROcp29_623*C24+S24*S5
    ROcp29_425 = ROcp29_424*C25+ROcp29_723*S25
    ROcp29_525 = ROcp29_524*C25+ROcp29_823*S25
    ROcp29_625 = ROcp29_624*C25+ROcp29_923*S25
    ROcp29_725 = -(ROcp29_424*S25-ROcp29_723*C25)
    ROcp29_825 = -(ROcp29_524*S25-ROcp29_823*C25)
    ROcp29_925 = -(ROcp29_624*S25-ROcp29_923*C25)
    ROcp29_126 = ROcp29_124*C26-ROcp29_725*S26
    ROcp29_226 = ROcp29_224*C26-ROcp29_825*S26
    ROcp29_326 = ROcp29_324*C26-ROcp29_925*S26
    ROcp29_726 = ROcp29_124*S26+ROcp29_725*C26
    ROcp29_826 = ROcp29_224*S26+ROcp29_825*C26
    ROcp29_926 = ROcp29_324*S26+ROcp29_925*C26
    ROcp29_127 = ROcp29_126*C27+ROcp29_425*S27
    ROcp29_227 = ROcp29_226*C27+ROcp29_525*S27
    ROcp29_327 = ROcp29_326*C27+ROcp29_625*S27
    ROcp29_427 = -(ROcp29_126*S27-ROcp29_425*C27)
    ROcp29_527 = -(ROcp29_226*S27-ROcp29_525*C27)
    ROcp29_627 = -(ROcp29_326*S27-ROcp29_625*C27)
    RLcp29_123 = ROcp29_15*s.dpt[1,10]+ROcp29_46*s.dpt[2,10]
    RLcp29_223 = ROcp29_25*s.dpt[1,10]+ROcp29_56*s.dpt[2,10]
    RLcp29_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp29_123 = OMcp29_16+ROcp29_15*qd[23]
    OMcp29_223 = OMcp29_26+ROcp29_25*qd[23]
    OMcp29_323 = OMcp29_36-qd[23]*S5
    ORcp29_123 = OMcp29_26*RLcp29_323-OMcp29_36*RLcp29_223
    ORcp29_223 = -(OMcp29_16*RLcp29_323-OMcp29_36*RLcp29_123)
    ORcp29_323 = OMcp29_16*RLcp29_223-OMcp29_26*RLcp29_123
    OMcp29_124 = OMcp29_123+ROcp29_723*qd[24]
    OMcp29_224 = OMcp29_223+ROcp29_823*qd[24]
    OMcp29_324 = OMcp29_323+ROcp29_923*qd[24]
    OPcp29_124 = OPcp29_16+ROcp29_15*qdd[23]+ROcp29_723*qdd[24]-qd[23]*(OMcp29_26*S5+OMcp29_36*ROcp29_25)+qd[24]*(\
   OMcp29_223*ROcp29_923-OMcp29_323*ROcp29_823)
    OPcp29_224 = OPcp29_26+ROcp29_25*qdd[23]+ROcp29_823*qdd[24]+qd[23]*(OMcp29_16*S5+OMcp29_36*ROcp29_15)-qd[24]*(\
   OMcp29_123*ROcp29_923-OMcp29_323*ROcp29_723)
    OPcp29_324 = OPcp29_36+ROcp29_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp29_16*ROcp29_25-OMcp29_26*ROcp29_15)+qd[24]*(\
   OMcp29_123*ROcp29_823-OMcp29_223*ROcp29_723)
    RLcp29_125 = ROcp29_424*s.dpt[2,26]
    RLcp29_225 = ROcp29_524*s.dpt[2,26]
    RLcp29_325 = ROcp29_624*s.dpt[2,26]
    OMcp29_125 = OMcp29_124+ROcp29_124*qd[25]
    OMcp29_225 = OMcp29_224+ROcp29_224*qd[25]
    OMcp29_325 = OMcp29_324+ROcp29_324*qd[25]
    ORcp29_125 = OMcp29_224*RLcp29_325-OMcp29_324*RLcp29_225
    ORcp29_225 = -(OMcp29_124*RLcp29_325-OMcp29_324*RLcp29_125)
    ORcp29_325 = OMcp29_124*RLcp29_225-OMcp29_224*RLcp29_125
    OMcp29_126 = OMcp29_125+ROcp29_425*qd[26]
    OMcp29_226 = OMcp29_225+ROcp29_525*qd[26]
    OMcp29_326 = OMcp29_325+ROcp29_625*qd[26]
    OMcp29_127 = OMcp29_126+ROcp29_726*qd[27]
    OMcp29_227 = OMcp29_226+ROcp29_826*qd[27]
    OMcp29_327 = OMcp29_326+ROcp29_926*qd[27]
    OPcp29_127 = OPcp29_124+ROcp29_124*qdd[25]+ROcp29_425*qdd[26]+ROcp29_726*qdd[27]+qd[25]*(OMcp29_224*ROcp29_324-\
   OMcp29_324*ROcp29_224)+qd[26]*(OMcp29_225*ROcp29_625-OMcp29_325*ROcp29_525)+qd[27]*(OMcp29_226*ROcp29_926-OMcp29_326*\
   ROcp29_826)
    OPcp29_227 = OPcp29_224+ROcp29_224*qdd[25]+ROcp29_525*qdd[26]+ROcp29_826*qdd[27]-qd[25]*(OMcp29_124*ROcp29_324-\
   OMcp29_324*ROcp29_124)-qd[26]*(OMcp29_125*ROcp29_625-OMcp29_325*ROcp29_425)-qd[27]*(OMcp29_126*ROcp29_926-OMcp29_326*\
   ROcp29_726)
    OPcp29_327 = OPcp29_324+ROcp29_324*qdd[25]+ROcp29_625*qdd[26]+ROcp29_926*qdd[27]+qd[25]*(OMcp29_124*ROcp29_224-\
   OMcp29_224*ROcp29_124)+qd[26]*(OMcp29_125*ROcp29_525-OMcp29_225*ROcp29_425)+qd[27]*(OMcp29_126*ROcp29_826-OMcp29_226*\
   ROcp29_726)

# = = Block_1_0_0_30_0_10 = = 
 
# Sensor Kinematics 


    ROcp29_430 = ROcp29_427*C30+ROcp29_726*S30
    ROcp29_530 = ROcp29_527*C30+ROcp29_826*S30
    ROcp29_630 = ROcp29_627*C30+ROcp29_926*S30
    ROcp29_730 = -(ROcp29_427*S30-ROcp29_726*C30)
    ROcp29_830 = -(ROcp29_527*S30-ROcp29_826*C30)
    ROcp29_930 = -(ROcp29_627*S30-ROcp29_926*C30)
    RLcp29_130 = ROcp29_726*s.dpt[3,28]
    RLcp29_230 = ROcp29_826*s.dpt[3,28]
    RLcp29_330 = ROcp29_926*s.dpt[3,28]
    POcp29_130 = RLcp29_123+RLcp29_125+RLcp29_130+q[1]
    POcp29_230 = RLcp29_223+RLcp29_225+RLcp29_230+q[2]
    POcp29_330 = RLcp29_323+RLcp29_325+RLcp29_330+q[3]
    OMcp29_130 = OMcp29_127+ROcp29_127*qd[30]
    OMcp29_230 = OMcp29_227+ROcp29_227*qd[30]
    OMcp29_330 = OMcp29_327+ROcp29_327*qd[30]
    ORcp29_130 = OMcp29_227*RLcp29_330-OMcp29_327*RLcp29_230
    ORcp29_230 = -(OMcp29_127*RLcp29_330-OMcp29_327*RLcp29_130)
    ORcp29_330 = OMcp29_127*RLcp29_230-OMcp29_227*RLcp29_130
    VIcp29_130 = ORcp29_123+ORcp29_125+ORcp29_130+qd[1]
    VIcp29_230 = ORcp29_223+ORcp29_225+ORcp29_230+qd[2]
    VIcp29_330 = ORcp29_323+ORcp29_325+ORcp29_330+qd[3]
    OPcp29_130 = OPcp29_127+ROcp29_127*qdd[30]+qd[30]*(OMcp29_227*ROcp29_327-OMcp29_327*ROcp29_227)
    OPcp29_230 = OPcp29_227+ROcp29_227*qdd[30]-qd[30]*(OMcp29_127*ROcp29_327-OMcp29_327*ROcp29_127)
    OPcp29_330 = OPcp29_327+ROcp29_327*qdd[30]+qd[30]*(OMcp29_127*ROcp29_227-OMcp29_227*ROcp29_127)
    ACcp29_130 = qdd[1]+OMcp29_224*ORcp29_325+OMcp29_227*ORcp29_330+OMcp29_26*ORcp29_323-OMcp29_324*ORcp29_225-OMcp29_327*\
   ORcp29_230-OMcp29_36*ORcp29_223+OPcp29_224*RLcp29_325+OPcp29_227*RLcp29_330+OPcp29_26*RLcp29_323-OPcp29_324*RLcp29_225-\
   OPcp29_327*RLcp29_230-OPcp29_36*RLcp29_223
    ACcp29_230 = qdd[2]-OMcp29_124*ORcp29_325-OMcp29_127*ORcp29_330-OMcp29_16*ORcp29_323+OMcp29_324*ORcp29_125+OMcp29_327*\
   ORcp29_130+OMcp29_36*ORcp29_123-OPcp29_124*RLcp29_325-OPcp29_127*RLcp29_330-OPcp29_16*RLcp29_323+OPcp29_324*RLcp29_125+\
   OPcp29_327*RLcp29_130+OPcp29_36*RLcp29_123
    ACcp29_330 = qdd[3]+OMcp29_124*ORcp29_225+OMcp29_127*ORcp29_230+OMcp29_16*ORcp29_223-OMcp29_224*ORcp29_125-OMcp29_227*\
   ORcp29_130-OMcp29_26*ORcp29_123+OPcp29_124*RLcp29_225+OPcp29_127*RLcp29_230+OPcp29_16*RLcp29_223-OPcp29_224*RLcp29_125-\
   OPcp29_227*RLcp29_130-OPcp29_26*RLcp29_123

# = = Block_1_0_0_30_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp29_130
    sens.P[2] = POcp29_230
    sens.P[3] = POcp29_330
    sens.R[1,1] = ROcp29_127
    sens.R[1,2] = ROcp29_227
    sens.R[1,3] = ROcp29_327
    sens.R[2,1] = ROcp29_430
    sens.R[2,2] = ROcp29_530
    sens.R[2,3] = ROcp29_630
    sens.R[3,1] = ROcp29_730
    sens.R[3,2] = ROcp29_830
    sens.R[3,3] = ROcp29_930
    sens.V[1] = VIcp29_130
    sens.V[2] = VIcp29_230
    sens.V[3] = VIcp29_330
    sens.OM[1] = OMcp29_130
    sens.OM[2] = OMcp29_230
    sens.OM[3] = OMcp29_330
    sens.A[1] = ACcp29_130
    sens.A[2] = ACcp29_230
    sens.A[3] = ACcp29_330
    sens.OMP[1] = OPcp29_130
    sens.OMP[2] = OPcp29_230
    sens.OMP[3] = OPcp29_330
 
# 
  elif(isens==31): 


# = = Block_1_0_0_31_0_1 = = 
 
# Sensor Kinematics 


    ROcp30_15 = C4*C5
    ROcp30_25 = S4*C5
    ROcp30_75 = C4*S5
    ROcp30_85 = S4*S5
    ROcp30_46 = ROcp30_75*S6-S4*C6
    ROcp30_56 = ROcp30_85*S6+C4*C6
    ROcp30_76 = ROcp30_75*C6+S4*S6
    ROcp30_86 = ROcp30_85*C6-C4*S6
    OMcp30_15 = -qd[5]*S4
    OMcp30_25 = qd[5]*C4
    OMcp30_16 = OMcp30_15+ROcp30_15*qd[6]
    OMcp30_26 = OMcp30_25+ROcp30_25*qd[6]
    OMcp30_36 = qd[4]-qd[6]*S5
    OPcp30_16 = ROcp30_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp30_25*S5+ROcp30_25*qd[4])
    OPcp30_26 = ROcp30_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp30_15*S5+ROcp30_15*qd[4])
    OPcp30_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_31_0_8 = = 
 
# Sensor Kinematics 


    ROcp30_423 = ROcp30_46*C23+ROcp30_76*S23
    ROcp30_523 = ROcp30_56*C23+ROcp30_86*S23
    ROcp30_623 = S23p6*C5
    ROcp30_723 = -(ROcp30_46*S23-ROcp30_76*C23)
    ROcp30_823 = -(ROcp30_56*S23-ROcp30_86*C23)
    ROcp30_923 = C23p6*C5
    ROcp30_124 = ROcp30_15*C24+ROcp30_423*S24
    ROcp30_224 = ROcp30_25*C24+ROcp30_523*S24
    ROcp30_324 = ROcp30_623*S24-C24*S5
    ROcp30_424 = -(ROcp30_15*S24-ROcp30_423*C24)
    ROcp30_524 = -(ROcp30_25*S24-ROcp30_523*C24)
    ROcp30_624 = ROcp30_623*C24+S24*S5
    ROcp30_425 = ROcp30_424*C25+ROcp30_723*S25
    ROcp30_525 = ROcp30_524*C25+ROcp30_823*S25
    ROcp30_625 = ROcp30_624*C25+ROcp30_923*S25
    ROcp30_725 = -(ROcp30_424*S25-ROcp30_723*C25)
    ROcp30_825 = -(ROcp30_524*S25-ROcp30_823*C25)
    ROcp30_925 = -(ROcp30_624*S25-ROcp30_923*C25)
    ROcp30_126 = ROcp30_124*C26-ROcp30_725*S26
    ROcp30_226 = ROcp30_224*C26-ROcp30_825*S26
    ROcp30_326 = ROcp30_324*C26-ROcp30_925*S26
    ROcp30_726 = ROcp30_124*S26+ROcp30_725*C26
    ROcp30_826 = ROcp30_224*S26+ROcp30_825*C26
    ROcp30_926 = ROcp30_324*S26+ROcp30_925*C26
    ROcp30_127 = ROcp30_126*C27+ROcp30_425*S27
    ROcp30_227 = ROcp30_226*C27+ROcp30_525*S27
    ROcp30_327 = ROcp30_326*C27+ROcp30_625*S27
    ROcp30_427 = -(ROcp30_126*S27-ROcp30_425*C27)
    ROcp30_527 = -(ROcp30_226*S27-ROcp30_525*C27)
    ROcp30_627 = -(ROcp30_326*S27-ROcp30_625*C27)
    RLcp30_123 = ROcp30_15*s.dpt[1,10]+ROcp30_46*s.dpt[2,10]
    RLcp30_223 = ROcp30_25*s.dpt[1,10]+ROcp30_56*s.dpt[2,10]
    RLcp30_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp30_123 = OMcp30_16+ROcp30_15*qd[23]
    OMcp30_223 = OMcp30_26+ROcp30_25*qd[23]
    OMcp30_323 = OMcp30_36-qd[23]*S5
    ORcp30_123 = OMcp30_26*RLcp30_323-OMcp30_36*RLcp30_223
    ORcp30_223 = -(OMcp30_16*RLcp30_323-OMcp30_36*RLcp30_123)
    ORcp30_323 = OMcp30_16*RLcp30_223-OMcp30_26*RLcp30_123
    OMcp30_124 = OMcp30_123+ROcp30_723*qd[24]
    OMcp30_224 = OMcp30_223+ROcp30_823*qd[24]
    OMcp30_324 = OMcp30_323+ROcp30_923*qd[24]
    OPcp30_124 = OPcp30_16+ROcp30_15*qdd[23]+ROcp30_723*qdd[24]-qd[23]*(OMcp30_26*S5+OMcp30_36*ROcp30_25)+qd[24]*(\
   OMcp30_223*ROcp30_923-OMcp30_323*ROcp30_823)
    OPcp30_224 = OPcp30_26+ROcp30_25*qdd[23]+ROcp30_823*qdd[24]+qd[23]*(OMcp30_16*S5+OMcp30_36*ROcp30_15)-qd[24]*(\
   OMcp30_123*ROcp30_923-OMcp30_323*ROcp30_723)
    OPcp30_324 = OPcp30_36+ROcp30_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp30_16*ROcp30_25-OMcp30_26*ROcp30_15)+qd[24]*(\
   OMcp30_123*ROcp30_823-OMcp30_223*ROcp30_723)
    RLcp30_125 = ROcp30_424*s.dpt[2,26]
    RLcp30_225 = ROcp30_524*s.dpt[2,26]
    RLcp30_325 = ROcp30_624*s.dpt[2,26]
    OMcp30_125 = OMcp30_124+ROcp30_124*qd[25]
    OMcp30_225 = OMcp30_224+ROcp30_224*qd[25]
    OMcp30_325 = OMcp30_324+ROcp30_324*qd[25]
    ORcp30_125 = OMcp30_224*RLcp30_325-OMcp30_324*RLcp30_225
    ORcp30_225 = -(OMcp30_124*RLcp30_325-OMcp30_324*RLcp30_125)
    ORcp30_325 = OMcp30_124*RLcp30_225-OMcp30_224*RLcp30_125
    OMcp30_126 = OMcp30_125+ROcp30_425*qd[26]
    OMcp30_226 = OMcp30_225+ROcp30_525*qd[26]
    OMcp30_326 = OMcp30_325+ROcp30_625*qd[26]
    OMcp30_127 = OMcp30_126+ROcp30_726*qd[27]
    OMcp30_227 = OMcp30_226+ROcp30_826*qd[27]
    OMcp30_327 = OMcp30_326+ROcp30_926*qd[27]
    OPcp30_127 = OPcp30_124+ROcp30_124*qdd[25]+ROcp30_425*qdd[26]+ROcp30_726*qdd[27]+qd[25]*(OMcp30_224*ROcp30_324-\
   OMcp30_324*ROcp30_224)+qd[26]*(OMcp30_225*ROcp30_625-OMcp30_325*ROcp30_525)+qd[27]*(OMcp30_226*ROcp30_926-OMcp30_326*\
   ROcp30_826)
    OPcp30_227 = OPcp30_224+ROcp30_224*qdd[25]+ROcp30_525*qdd[26]+ROcp30_826*qdd[27]-qd[25]*(OMcp30_124*ROcp30_324-\
   OMcp30_324*ROcp30_124)-qd[26]*(OMcp30_125*ROcp30_625-OMcp30_325*ROcp30_425)-qd[27]*(OMcp30_126*ROcp30_926-OMcp30_326*\
   ROcp30_726)
    OPcp30_327 = OPcp30_324+ROcp30_324*qdd[25]+ROcp30_625*qdd[26]+ROcp30_926*qdd[27]+qd[25]*(OMcp30_124*ROcp30_224-\
   OMcp30_224*ROcp30_124)+qd[26]*(OMcp30_125*ROcp30_525-OMcp30_225*ROcp30_425)+qd[27]*(OMcp30_126*ROcp30_826-OMcp30_226*\
   ROcp30_726)

# = = Block_1_0_0_31_0_10 = = 
 
# Sensor Kinematics 


    ROcp30_430 = ROcp30_427*C30+ROcp30_726*S30
    ROcp30_530 = ROcp30_527*C30+ROcp30_826*S30
    ROcp30_630 = ROcp30_627*C30+ROcp30_926*S30
    ROcp30_730 = -(ROcp30_427*S30-ROcp30_726*C30)
    ROcp30_830 = -(ROcp30_527*S30-ROcp30_826*C30)
    ROcp30_930 = -(ROcp30_627*S30-ROcp30_926*C30)
    ROcp30_131 = ROcp30_127*C31-ROcp30_730*S31
    ROcp30_231 = ROcp30_227*C31-ROcp30_830*S31
    ROcp30_331 = ROcp30_327*C31-ROcp30_930*S31
    ROcp30_731 = ROcp30_127*S31+ROcp30_730*C31
    ROcp30_831 = ROcp30_227*S31+ROcp30_830*C31
    ROcp30_931 = ROcp30_327*S31+ROcp30_930*C31
    RLcp30_130 = ROcp30_726*s.dpt[3,28]
    RLcp30_230 = ROcp30_826*s.dpt[3,28]
    RLcp30_330 = ROcp30_926*s.dpt[3,28]
    POcp30_130 = RLcp30_123+RLcp30_125+RLcp30_130+q[1]
    POcp30_230 = RLcp30_223+RLcp30_225+RLcp30_230+q[2]
    POcp30_330 = RLcp30_323+RLcp30_325+RLcp30_330+q[3]
    OMcp30_130 = OMcp30_127+ROcp30_127*qd[30]
    OMcp30_230 = OMcp30_227+ROcp30_227*qd[30]
    OMcp30_330 = OMcp30_327+ROcp30_327*qd[30]
    ORcp30_130 = OMcp30_227*RLcp30_330-OMcp30_327*RLcp30_230
    ORcp30_230 = -(OMcp30_127*RLcp30_330-OMcp30_327*RLcp30_130)
    ORcp30_330 = OMcp30_127*RLcp30_230-OMcp30_227*RLcp30_130
    VIcp30_130 = ORcp30_123+ORcp30_125+ORcp30_130+qd[1]
    VIcp30_230 = ORcp30_223+ORcp30_225+ORcp30_230+qd[2]
    VIcp30_330 = ORcp30_323+ORcp30_325+ORcp30_330+qd[3]
    ACcp30_130 = qdd[1]+OMcp30_224*ORcp30_325+OMcp30_227*ORcp30_330+OMcp30_26*ORcp30_323-OMcp30_324*ORcp30_225-OMcp30_327*\
   ORcp30_230-OMcp30_36*ORcp30_223+OPcp30_224*RLcp30_325+OPcp30_227*RLcp30_330+OPcp30_26*RLcp30_323-OPcp30_324*RLcp30_225-\
   OPcp30_327*RLcp30_230-OPcp30_36*RLcp30_223
    ACcp30_230 = qdd[2]-OMcp30_124*ORcp30_325-OMcp30_127*ORcp30_330-OMcp30_16*ORcp30_323+OMcp30_324*ORcp30_125+OMcp30_327*\
   ORcp30_130+OMcp30_36*ORcp30_123-OPcp30_124*RLcp30_325-OPcp30_127*RLcp30_330-OPcp30_16*RLcp30_323+OPcp30_324*RLcp30_125+\
   OPcp30_327*RLcp30_130+OPcp30_36*RLcp30_123
    ACcp30_330 = qdd[3]+OMcp30_124*ORcp30_225+OMcp30_127*ORcp30_230+OMcp30_16*ORcp30_223-OMcp30_224*ORcp30_125-OMcp30_227*\
   ORcp30_130-OMcp30_26*ORcp30_123+OPcp30_124*RLcp30_225+OPcp30_127*RLcp30_230+OPcp30_16*RLcp30_223-OPcp30_224*RLcp30_125-\
   OPcp30_227*RLcp30_130-OPcp30_26*RLcp30_123
    OMcp30_131 = OMcp30_130+ROcp30_430*qd[31]
    OMcp30_231 = OMcp30_230+ROcp30_530*qd[31]
    OMcp30_331 = OMcp30_330+ROcp30_630*qd[31]
    OPcp30_131 = OPcp30_127+ROcp30_127*qdd[30]+ROcp30_430*qdd[31]+qd[30]*(OMcp30_227*ROcp30_327-OMcp30_327*ROcp30_227)+\
   qd[31]*(OMcp30_230*ROcp30_630-OMcp30_330*ROcp30_530)
    OPcp30_231 = OPcp30_227+ROcp30_227*qdd[30]+ROcp30_530*qdd[31]-qd[30]*(OMcp30_127*ROcp30_327-OMcp30_327*ROcp30_127)-\
   qd[31]*(OMcp30_130*ROcp30_630-OMcp30_330*ROcp30_430)
    OPcp30_331 = OPcp30_327+ROcp30_327*qdd[30]+ROcp30_630*qdd[31]+qd[30]*(OMcp30_127*ROcp30_227-OMcp30_227*ROcp30_127)+\
   qd[31]*(OMcp30_130*ROcp30_530-OMcp30_230*ROcp30_430)

# = = Block_1_0_0_31_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp30_130
    sens.P[2] = POcp30_230
    sens.P[3] = POcp30_330
    sens.R[1,1] = ROcp30_131
    sens.R[1,2] = ROcp30_231
    sens.R[1,3] = ROcp30_331
    sens.R[2,1] = ROcp30_430
    sens.R[2,2] = ROcp30_530
    sens.R[2,3] = ROcp30_630
    sens.R[3,1] = ROcp30_731
    sens.R[3,2] = ROcp30_831
    sens.R[3,3] = ROcp30_931
    sens.V[1] = VIcp30_130
    sens.V[2] = VIcp30_230
    sens.V[3] = VIcp30_330
    sens.OM[1] = OMcp30_131
    sens.OM[2] = OMcp30_231
    sens.OM[3] = OMcp30_331
    sens.A[1] = ACcp30_130
    sens.A[2] = ACcp30_230
    sens.A[3] = ACcp30_330
    sens.OMP[1] = OPcp30_131
    sens.OMP[2] = OPcp30_231
    sens.OMP[3] = OPcp30_331
 
# 
  elif(isens==32): 


# = = Block_1_0_0_32_0_1 = = 
 
# Sensor Kinematics 


    ROcp31_15 = C4*C5
    ROcp31_25 = S4*C5
    ROcp31_75 = C4*S5
    ROcp31_85 = S4*S5
    ROcp31_46 = ROcp31_75*S6-S4*C6
    ROcp31_56 = ROcp31_85*S6+C4*C6
    ROcp31_76 = ROcp31_75*C6+S4*S6
    ROcp31_86 = ROcp31_85*C6-C4*S6
    OMcp31_15 = -qd[5]*S4
    OMcp31_25 = qd[5]*C4
    OMcp31_16 = OMcp31_15+ROcp31_15*qd[6]
    OMcp31_26 = OMcp31_25+ROcp31_25*qd[6]
    OMcp31_36 = qd[4]-qd[6]*S5
    OPcp31_16 = ROcp31_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp31_25*S5+ROcp31_25*qd[4])
    OPcp31_26 = ROcp31_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp31_15*S5+ROcp31_15*qd[4])
    OPcp31_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_32_0_11 = = 
 
# Sensor Kinematics 


    ROcp31_432 = ROcp31_46*C32+ROcp31_76*S32
    ROcp31_532 = ROcp31_56*C32+ROcp31_86*S32
    ROcp31_632 = S32p6*C5
    ROcp31_732 = -(ROcp31_46*S32-ROcp31_76*C32)
    ROcp31_832 = -(ROcp31_56*S32-ROcp31_86*C32)
    ROcp31_932 = C32p6*C5
    RLcp31_132 = ROcp31_15*s.dpt[1,12]+ROcp31_46*s.dpt[2,12]
    RLcp31_232 = ROcp31_25*s.dpt[1,12]+ROcp31_56*s.dpt[2,12]
    RLcp31_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    POcp31_132 = RLcp31_132+q[1]
    POcp31_232 = RLcp31_232+q[2]
    POcp31_332 = RLcp31_332+q[3]
    OMcp31_132 = OMcp31_16+ROcp31_15*qd[32]
    OMcp31_232 = OMcp31_26+ROcp31_25*qd[32]
    OMcp31_332 = OMcp31_36-qd[32]*S5
    ORcp31_132 = OMcp31_26*RLcp31_332-OMcp31_36*RLcp31_232
    ORcp31_232 = -(OMcp31_16*RLcp31_332-OMcp31_36*RLcp31_132)
    ORcp31_332 = OMcp31_16*RLcp31_232-OMcp31_26*RLcp31_132
    VIcp31_132 = ORcp31_132+qd[1]
    VIcp31_232 = ORcp31_232+qd[2]
    VIcp31_332 = ORcp31_332+qd[3]
    OPcp31_132 = OPcp31_16+ROcp31_15*qdd[32]-qd[32]*(OMcp31_26*S5+OMcp31_36*ROcp31_25)
    OPcp31_232 = OPcp31_26+ROcp31_25*qdd[32]+qd[32]*(OMcp31_16*S5+OMcp31_36*ROcp31_15)
    OPcp31_332 = OPcp31_36-qdd[32]*S5+qd[32]*(OMcp31_16*ROcp31_25-OMcp31_26*ROcp31_15)
    ACcp31_132 = qdd[1]+OMcp31_26*ORcp31_332-OMcp31_36*ORcp31_232+OPcp31_26*RLcp31_332-OPcp31_36*RLcp31_232
    ACcp31_232 = qdd[2]-OMcp31_16*ORcp31_332+OMcp31_36*ORcp31_132-OPcp31_16*RLcp31_332+OPcp31_36*RLcp31_132
    ACcp31_332 = qdd[3]+OMcp31_16*ORcp31_232-OMcp31_26*ORcp31_132+OPcp31_16*RLcp31_232-OPcp31_26*RLcp31_132

# = = Block_1_0_0_32_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp31_132
    sens.P[2] = POcp31_232
    sens.P[3] = POcp31_332
    sens.R[1,1] = ROcp31_15
    sens.R[1,2] = ROcp31_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp31_432
    sens.R[2,2] = ROcp31_532
    sens.R[2,3] = ROcp31_632
    sens.R[3,1] = ROcp31_732
    sens.R[3,2] = ROcp31_832
    sens.R[3,3] = ROcp31_932
    sens.V[1] = VIcp31_132
    sens.V[2] = VIcp31_232
    sens.V[3] = VIcp31_332
    sens.OM[1] = OMcp31_132
    sens.OM[2] = OMcp31_232
    sens.OM[3] = OMcp31_332
    sens.A[1] = ACcp31_132
    sens.A[2] = ACcp31_232
    sens.A[3] = ACcp31_332
    sens.OMP[1] = OPcp31_132
    sens.OMP[2] = OPcp31_232
    sens.OMP[3] = OPcp31_332
 
# 
  elif(isens==33): 


# = = Block_1_0_0_33_0_1 = = 
 
# Sensor Kinematics 


    ROcp32_15 = C4*C5
    ROcp32_25 = S4*C5
    ROcp32_75 = C4*S5
    ROcp32_85 = S4*S5
    ROcp32_46 = ROcp32_75*S6-S4*C6
    ROcp32_56 = ROcp32_85*S6+C4*C6
    ROcp32_76 = ROcp32_75*C6+S4*S6
    ROcp32_86 = ROcp32_85*C6-C4*S6
    OMcp32_15 = -qd[5]*S4
    OMcp32_25 = qd[5]*C4
    OMcp32_16 = OMcp32_15+ROcp32_15*qd[6]
    OMcp32_26 = OMcp32_25+ROcp32_25*qd[6]
    OMcp32_36 = qd[4]-qd[6]*S5
    OPcp32_16 = ROcp32_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp32_25*S5+ROcp32_25*qd[4])
    OPcp32_26 = ROcp32_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp32_15*S5+ROcp32_15*qd[4])
    OPcp32_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_33_0_11 = = 
 
# Sensor Kinematics 


    ROcp32_432 = ROcp32_46*C32+ROcp32_76*S32
    ROcp32_532 = ROcp32_56*C32+ROcp32_86*S32
    ROcp32_632 = S32p6*C5
    ROcp32_732 = -(ROcp32_46*S32-ROcp32_76*C32)
    ROcp32_832 = -(ROcp32_56*S32-ROcp32_86*C32)
    ROcp32_932 = C32p6*C5
    ROcp32_133 = ROcp32_15*C33+ROcp32_432*S33
    ROcp32_233 = ROcp32_25*C33+ROcp32_532*S33
    ROcp32_333 = ROcp32_632*S33-C33*S5
    ROcp32_433 = -(ROcp32_15*S33-ROcp32_432*C33)
    ROcp32_533 = -(ROcp32_25*S33-ROcp32_532*C33)
    ROcp32_633 = ROcp32_632*C33+S33*S5
    RLcp32_132 = ROcp32_15*s.dpt[1,12]+ROcp32_46*s.dpt[2,12]
    RLcp32_232 = ROcp32_25*s.dpt[1,12]+ROcp32_56*s.dpt[2,12]
    RLcp32_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    POcp32_132 = RLcp32_132+q[1]
    POcp32_232 = RLcp32_232+q[2]
    POcp32_332 = RLcp32_332+q[3]
    OMcp32_132 = OMcp32_16+ROcp32_15*qd[32]
    OMcp32_232 = OMcp32_26+ROcp32_25*qd[32]
    OMcp32_332 = OMcp32_36-qd[32]*S5
    ORcp32_132 = OMcp32_26*RLcp32_332-OMcp32_36*RLcp32_232
    ORcp32_232 = -(OMcp32_16*RLcp32_332-OMcp32_36*RLcp32_132)
    ORcp32_332 = OMcp32_16*RLcp32_232-OMcp32_26*RLcp32_132
    VIcp32_132 = ORcp32_132+qd[1]
    VIcp32_232 = ORcp32_232+qd[2]
    VIcp32_332 = ORcp32_332+qd[3]
    ACcp32_132 = qdd[1]+OMcp32_26*ORcp32_332-OMcp32_36*ORcp32_232+OPcp32_26*RLcp32_332-OPcp32_36*RLcp32_232
    ACcp32_232 = qdd[2]-OMcp32_16*ORcp32_332+OMcp32_36*ORcp32_132-OPcp32_16*RLcp32_332+OPcp32_36*RLcp32_132
    ACcp32_332 = qdd[3]+OMcp32_16*ORcp32_232-OMcp32_26*ORcp32_132+OPcp32_16*RLcp32_232-OPcp32_26*RLcp32_132
    OMcp32_133 = OMcp32_132+ROcp32_732*qd[33]
    OMcp32_233 = OMcp32_232+ROcp32_832*qd[33]
    OMcp32_333 = OMcp32_332+ROcp32_932*qd[33]
    OPcp32_133 = OPcp32_16+ROcp32_15*qdd[32]+ROcp32_732*qdd[33]-qd[32]*(OMcp32_26*S5+OMcp32_36*ROcp32_25)+qd[33]*(\
   OMcp32_232*ROcp32_932-OMcp32_332*ROcp32_832)
    OPcp32_233 = OPcp32_26+ROcp32_25*qdd[32]+ROcp32_832*qdd[33]+qd[32]*(OMcp32_16*S5+OMcp32_36*ROcp32_15)-qd[33]*(\
   OMcp32_132*ROcp32_932-OMcp32_332*ROcp32_732)
    OPcp32_333 = OPcp32_36+ROcp32_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp32_16*ROcp32_25-OMcp32_26*ROcp32_15)+qd[33]*(\
   OMcp32_132*ROcp32_832-OMcp32_232*ROcp32_732)

# = = Block_1_0_0_33_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp32_132
    sens.P[2] = POcp32_232
    sens.P[3] = POcp32_332
    sens.R[1,1] = ROcp32_133
    sens.R[1,2] = ROcp32_233
    sens.R[1,3] = ROcp32_333
    sens.R[2,1] = ROcp32_433
    sens.R[2,2] = ROcp32_533
    sens.R[2,3] = ROcp32_633
    sens.R[3,1] = ROcp32_732
    sens.R[3,2] = ROcp32_832
    sens.R[3,3] = ROcp32_932
    sens.V[1] = VIcp32_132
    sens.V[2] = VIcp32_232
    sens.V[3] = VIcp32_332
    sens.OM[1] = OMcp32_133
    sens.OM[2] = OMcp32_233
    sens.OM[3] = OMcp32_333
    sens.A[1] = ACcp32_132
    sens.A[2] = ACcp32_232
    sens.A[3] = ACcp32_332
    sens.OMP[1] = OPcp32_133
    sens.OMP[2] = OPcp32_233
    sens.OMP[3] = OPcp32_333
 
# 
  elif(isens==34): 


# = = Block_1_0_0_34_0_1 = = 
 
# Sensor Kinematics 


    ROcp33_15 = C4*C5
    ROcp33_25 = S4*C5
    ROcp33_75 = C4*S5
    ROcp33_85 = S4*S5
    ROcp33_46 = ROcp33_75*S6-S4*C6
    ROcp33_56 = ROcp33_85*S6+C4*C6
    ROcp33_76 = ROcp33_75*C6+S4*S6
    ROcp33_86 = ROcp33_85*C6-C4*S6
    OMcp33_15 = -qd[5]*S4
    OMcp33_25 = qd[5]*C4
    OMcp33_16 = OMcp33_15+ROcp33_15*qd[6]
    OMcp33_26 = OMcp33_25+ROcp33_25*qd[6]
    OMcp33_36 = qd[4]-qd[6]*S5
    OPcp33_16 = ROcp33_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp33_25*S5+ROcp33_25*qd[4])
    OPcp33_26 = ROcp33_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp33_15*S5+ROcp33_15*qd[4])
    OPcp33_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_34_0_11 = = 
 
# Sensor Kinematics 


    ROcp33_432 = ROcp33_46*C32+ROcp33_76*S32
    ROcp33_532 = ROcp33_56*C32+ROcp33_86*S32
    ROcp33_632 = S32p6*C5
    ROcp33_732 = -(ROcp33_46*S32-ROcp33_76*C32)
    ROcp33_832 = -(ROcp33_56*S32-ROcp33_86*C32)
    ROcp33_932 = C32p6*C5
    ROcp33_133 = ROcp33_15*C33+ROcp33_432*S33
    ROcp33_233 = ROcp33_25*C33+ROcp33_532*S33
    ROcp33_333 = ROcp33_632*S33-C33*S5
    ROcp33_433 = -(ROcp33_15*S33-ROcp33_432*C33)
    ROcp33_533 = -(ROcp33_25*S33-ROcp33_532*C33)
    ROcp33_633 = ROcp33_632*C33+S33*S5
    ROcp33_434 = ROcp33_433*C34+ROcp33_732*S34
    ROcp33_534 = ROcp33_533*C34+ROcp33_832*S34
    ROcp33_634 = ROcp33_633*C34+ROcp33_932*S34
    ROcp33_734 = -(ROcp33_433*S34-ROcp33_732*C34)
    ROcp33_834 = -(ROcp33_533*S34-ROcp33_832*C34)
    ROcp33_934 = -(ROcp33_633*S34-ROcp33_932*C34)
    RLcp33_132 = ROcp33_15*s.dpt[1,12]+ROcp33_46*s.dpt[2,12]
    RLcp33_232 = ROcp33_25*s.dpt[1,12]+ROcp33_56*s.dpt[2,12]
    RLcp33_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp33_132 = OMcp33_16+ROcp33_15*qd[32]
    OMcp33_232 = OMcp33_26+ROcp33_25*qd[32]
    OMcp33_332 = OMcp33_36-qd[32]*S5
    ORcp33_132 = OMcp33_26*RLcp33_332-OMcp33_36*RLcp33_232
    ORcp33_232 = -(OMcp33_16*RLcp33_332-OMcp33_36*RLcp33_132)
    ORcp33_332 = OMcp33_16*RLcp33_232-OMcp33_26*RLcp33_132
    OMcp33_133 = OMcp33_132+ROcp33_732*qd[33]
    OMcp33_233 = OMcp33_232+ROcp33_832*qd[33]
    OMcp33_333 = OMcp33_332+ROcp33_932*qd[33]
    OPcp33_133 = OPcp33_16+ROcp33_15*qdd[32]+ROcp33_732*qdd[33]-qd[32]*(OMcp33_26*S5+OMcp33_36*ROcp33_25)+qd[33]*(\
   OMcp33_232*ROcp33_932-OMcp33_332*ROcp33_832)
    OPcp33_233 = OPcp33_26+ROcp33_25*qdd[32]+ROcp33_832*qdd[33]+qd[32]*(OMcp33_16*S5+OMcp33_36*ROcp33_15)-qd[33]*(\
   OMcp33_132*ROcp33_932-OMcp33_332*ROcp33_732)
    OPcp33_333 = OPcp33_36+ROcp33_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp33_16*ROcp33_25-OMcp33_26*ROcp33_15)+qd[33]*(\
   OMcp33_132*ROcp33_832-OMcp33_232*ROcp33_732)
    RLcp33_134 = ROcp33_433*s.dpt[2,33]
    RLcp33_234 = ROcp33_533*s.dpt[2,33]
    RLcp33_334 = ROcp33_633*s.dpt[2,33]
    POcp33_134 = RLcp33_132+RLcp33_134+q[1]
    POcp33_234 = RLcp33_232+RLcp33_234+q[2]
    POcp33_334 = RLcp33_332+RLcp33_334+q[3]
    OMcp33_134 = OMcp33_133+ROcp33_133*qd[34]
    OMcp33_234 = OMcp33_233+ROcp33_233*qd[34]
    OMcp33_334 = OMcp33_333+ROcp33_333*qd[34]
    ORcp33_134 = OMcp33_233*RLcp33_334-OMcp33_333*RLcp33_234
    ORcp33_234 = -(OMcp33_133*RLcp33_334-OMcp33_333*RLcp33_134)
    ORcp33_334 = OMcp33_133*RLcp33_234-OMcp33_233*RLcp33_134
    VIcp33_134 = ORcp33_132+ORcp33_134+qd[1]
    VIcp33_234 = ORcp33_232+ORcp33_234+qd[2]
    VIcp33_334 = ORcp33_332+ORcp33_334+qd[3]
    OPcp33_134 = OPcp33_133+ROcp33_133*qdd[34]+qd[34]*(OMcp33_233*ROcp33_333-OMcp33_333*ROcp33_233)
    OPcp33_234 = OPcp33_233+ROcp33_233*qdd[34]-qd[34]*(OMcp33_133*ROcp33_333-OMcp33_333*ROcp33_133)
    OPcp33_334 = OPcp33_333+ROcp33_333*qdd[34]+qd[34]*(OMcp33_133*ROcp33_233-OMcp33_233*ROcp33_133)
    ACcp33_134 = qdd[1]+OMcp33_233*ORcp33_334+OMcp33_26*ORcp33_332-OMcp33_333*ORcp33_234-OMcp33_36*ORcp33_232+OPcp33_233*\
   RLcp33_334+OPcp33_26*RLcp33_332-OPcp33_333*RLcp33_234-OPcp33_36*RLcp33_232
    ACcp33_234 = qdd[2]-OMcp33_133*ORcp33_334-OMcp33_16*ORcp33_332+OMcp33_333*ORcp33_134+OMcp33_36*ORcp33_132-OPcp33_133*\
   RLcp33_334-OPcp33_16*RLcp33_332+OPcp33_333*RLcp33_134+OPcp33_36*RLcp33_132
    ACcp33_334 = qdd[3]+OMcp33_133*ORcp33_234+OMcp33_16*ORcp33_232-OMcp33_233*ORcp33_134-OMcp33_26*ORcp33_132+OPcp33_133*\
   RLcp33_234+OPcp33_16*RLcp33_232-OPcp33_233*RLcp33_134-OPcp33_26*RLcp33_132

# = = Block_1_0_0_34_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp33_134
    sens.P[2] = POcp33_234
    sens.P[3] = POcp33_334
    sens.R[1,1] = ROcp33_133
    sens.R[1,2] = ROcp33_233
    sens.R[1,3] = ROcp33_333
    sens.R[2,1] = ROcp33_434
    sens.R[2,2] = ROcp33_534
    sens.R[2,3] = ROcp33_634
    sens.R[3,1] = ROcp33_734
    sens.R[3,2] = ROcp33_834
    sens.R[3,3] = ROcp33_934
    sens.V[1] = VIcp33_134
    sens.V[2] = VIcp33_234
    sens.V[3] = VIcp33_334
    sens.OM[1] = OMcp33_134
    sens.OM[2] = OMcp33_234
    sens.OM[3] = OMcp33_334
    sens.A[1] = ACcp33_134
    sens.A[2] = ACcp33_234
    sens.A[3] = ACcp33_334
    sens.OMP[1] = OPcp33_134
    sens.OMP[2] = OPcp33_234
    sens.OMP[3] = OPcp33_334
 
# 
  elif(isens==35): 


# = = Block_1_0_0_35_0_1 = = 
 
# Sensor Kinematics 


    ROcp34_15 = C4*C5
    ROcp34_25 = S4*C5
    ROcp34_75 = C4*S5
    ROcp34_85 = S4*S5
    ROcp34_46 = ROcp34_75*S6-S4*C6
    ROcp34_56 = ROcp34_85*S6+C4*C6
    ROcp34_76 = ROcp34_75*C6+S4*S6
    ROcp34_86 = ROcp34_85*C6-C4*S6
    OMcp34_15 = -qd[5]*S4
    OMcp34_25 = qd[5]*C4
    OMcp34_16 = OMcp34_15+ROcp34_15*qd[6]
    OMcp34_26 = OMcp34_25+ROcp34_25*qd[6]
    OMcp34_36 = qd[4]-qd[6]*S5
    OPcp34_16 = ROcp34_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp34_25*S5+ROcp34_25*qd[4])
    OPcp34_26 = ROcp34_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp34_15*S5+ROcp34_15*qd[4])
    OPcp34_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_35_0_11 = = 
 
# Sensor Kinematics 


    ROcp34_432 = ROcp34_46*C32+ROcp34_76*S32
    ROcp34_532 = ROcp34_56*C32+ROcp34_86*S32
    ROcp34_632 = S32p6*C5
    ROcp34_732 = -(ROcp34_46*S32-ROcp34_76*C32)
    ROcp34_832 = -(ROcp34_56*S32-ROcp34_86*C32)
    ROcp34_932 = C32p6*C5
    ROcp34_133 = ROcp34_15*C33+ROcp34_432*S33
    ROcp34_233 = ROcp34_25*C33+ROcp34_532*S33
    ROcp34_333 = ROcp34_632*S33-C33*S5
    ROcp34_433 = -(ROcp34_15*S33-ROcp34_432*C33)
    ROcp34_533 = -(ROcp34_25*S33-ROcp34_532*C33)
    ROcp34_633 = ROcp34_632*C33+S33*S5
    ROcp34_434 = ROcp34_433*C34+ROcp34_732*S34
    ROcp34_534 = ROcp34_533*C34+ROcp34_832*S34
    ROcp34_634 = ROcp34_633*C34+ROcp34_932*S34
    ROcp34_734 = -(ROcp34_433*S34-ROcp34_732*C34)
    ROcp34_834 = -(ROcp34_533*S34-ROcp34_832*C34)
    ROcp34_934 = -(ROcp34_633*S34-ROcp34_932*C34)
    ROcp34_135 = ROcp34_133*C35-ROcp34_734*S35
    ROcp34_235 = ROcp34_233*C35-ROcp34_834*S35
    ROcp34_335 = ROcp34_333*C35-ROcp34_934*S35
    ROcp34_735 = ROcp34_133*S35+ROcp34_734*C35
    ROcp34_835 = ROcp34_233*S35+ROcp34_834*C35
    ROcp34_935 = ROcp34_333*S35+ROcp34_934*C35
    RLcp34_132 = ROcp34_15*s.dpt[1,12]+ROcp34_46*s.dpt[2,12]
    RLcp34_232 = ROcp34_25*s.dpt[1,12]+ROcp34_56*s.dpt[2,12]
    RLcp34_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp34_132 = OMcp34_16+ROcp34_15*qd[32]
    OMcp34_232 = OMcp34_26+ROcp34_25*qd[32]
    OMcp34_332 = OMcp34_36-qd[32]*S5
    ORcp34_132 = OMcp34_26*RLcp34_332-OMcp34_36*RLcp34_232
    ORcp34_232 = -(OMcp34_16*RLcp34_332-OMcp34_36*RLcp34_132)
    ORcp34_332 = OMcp34_16*RLcp34_232-OMcp34_26*RLcp34_132
    OMcp34_133 = OMcp34_132+ROcp34_732*qd[33]
    OMcp34_233 = OMcp34_232+ROcp34_832*qd[33]
    OMcp34_333 = OMcp34_332+ROcp34_932*qd[33]
    OPcp34_133 = OPcp34_16+ROcp34_15*qdd[32]+ROcp34_732*qdd[33]-qd[32]*(OMcp34_26*S5+OMcp34_36*ROcp34_25)+qd[33]*(\
   OMcp34_232*ROcp34_932-OMcp34_332*ROcp34_832)
    OPcp34_233 = OPcp34_26+ROcp34_25*qdd[32]+ROcp34_832*qdd[33]+qd[32]*(OMcp34_16*S5+OMcp34_36*ROcp34_15)-qd[33]*(\
   OMcp34_132*ROcp34_932-OMcp34_332*ROcp34_732)
    OPcp34_333 = OPcp34_36+ROcp34_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp34_16*ROcp34_25-OMcp34_26*ROcp34_15)+qd[33]*(\
   OMcp34_132*ROcp34_832-OMcp34_232*ROcp34_732)
    RLcp34_134 = ROcp34_433*s.dpt[2,33]
    RLcp34_234 = ROcp34_533*s.dpt[2,33]
    RLcp34_334 = ROcp34_633*s.dpt[2,33]
    POcp34_134 = RLcp34_132+RLcp34_134+q[1]
    POcp34_234 = RLcp34_232+RLcp34_234+q[2]
    POcp34_334 = RLcp34_332+RLcp34_334+q[3]
    OMcp34_134 = OMcp34_133+ROcp34_133*qd[34]
    OMcp34_234 = OMcp34_233+ROcp34_233*qd[34]
    OMcp34_334 = OMcp34_333+ROcp34_333*qd[34]
    ORcp34_134 = OMcp34_233*RLcp34_334-OMcp34_333*RLcp34_234
    ORcp34_234 = -(OMcp34_133*RLcp34_334-OMcp34_333*RLcp34_134)
    ORcp34_334 = OMcp34_133*RLcp34_234-OMcp34_233*RLcp34_134
    VIcp34_134 = ORcp34_132+ORcp34_134+qd[1]
    VIcp34_234 = ORcp34_232+ORcp34_234+qd[2]
    VIcp34_334 = ORcp34_332+ORcp34_334+qd[3]
    ACcp34_134 = qdd[1]+OMcp34_233*ORcp34_334+OMcp34_26*ORcp34_332-OMcp34_333*ORcp34_234-OMcp34_36*ORcp34_232+OPcp34_233*\
   RLcp34_334+OPcp34_26*RLcp34_332-OPcp34_333*RLcp34_234-OPcp34_36*RLcp34_232
    ACcp34_234 = qdd[2]-OMcp34_133*ORcp34_334-OMcp34_16*ORcp34_332+OMcp34_333*ORcp34_134+OMcp34_36*ORcp34_132-OPcp34_133*\
   RLcp34_334-OPcp34_16*RLcp34_332+OPcp34_333*RLcp34_134+OPcp34_36*RLcp34_132
    ACcp34_334 = qdd[3]+OMcp34_133*ORcp34_234+OMcp34_16*ORcp34_232-OMcp34_233*ORcp34_134-OMcp34_26*ORcp34_132+OPcp34_133*\
   RLcp34_234+OPcp34_16*RLcp34_232-OPcp34_233*RLcp34_134-OPcp34_26*RLcp34_132
    OMcp34_135 = OMcp34_134+ROcp34_434*qd[35]
    OMcp34_235 = OMcp34_234+ROcp34_534*qd[35]
    OMcp34_335 = OMcp34_334+ROcp34_634*qd[35]
    OPcp34_135 = OPcp34_133+ROcp34_133*qdd[34]+ROcp34_434*qdd[35]+qd[34]*(OMcp34_233*ROcp34_333-OMcp34_333*ROcp34_233)+\
   qd[35]*(OMcp34_234*ROcp34_634-OMcp34_334*ROcp34_534)
    OPcp34_235 = OPcp34_233+ROcp34_233*qdd[34]+ROcp34_534*qdd[35]-qd[34]*(OMcp34_133*ROcp34_333-OMcp34_333*ROcp34_133)-\
   qd[35]*(OMcp34_134*ROcp34_634-OMcp34_334*ROcp34_434)
    OPcp34_335 = OPcp34_333+ROcp34_333*qdd[34]+ROcp34_634*qdd[35]+qd[34]*(OMcp34_133*ROcp34_233-OMcp34_233*ROcp34_133)+\
   qd[35]*(OMcp34_134*ROcp34_534-OMcp34_234*ROcp34_434)

# = = Block_1_0_0_35_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp34_134
    sens.P[2] = POcp34_234
    sens.P[3] = POcp34_334
    sens.R[1,1] = ROcp34_135
    sens.R[1,2] = ROcp34_235
    sens.R[1,3] = ROcp34_335
    sens.R[2,1] = ROcp34_434
    sens.R[2,2] = ROcp34_534
    sens.R[2,3] = ROcp34_634
    sens.R[3,1] = ROcp34_735
    sens.R[3,2] = ROcp34_835
    sens.R[3,3] = ROcp34_935
    sens.V[1] = VIcp34_134
    sens.V[2] = VIcp34_234
    sens.V[3] = VIcp34_334
    sens.OM[1] = OMcp34_135
    sens.OM[2] = OMcp34_235
    sens.OM[3] = OMcp34_335
    sens.A[1] = ACcp34_134
    sens.A[2] = ACcp34_234
    sens.A[3] = ACcp34_334
    sens.OMP[1] = OPcp34_135
    sens.OMP[2] = OPcp34_235
    sens.OMP[3] = OPcp34_335
 
# 
  elif(isens==36): 


# = = Block_1_0_0_36_0_1 = = 
 
# Sensor Kinematics 


    ROcp35_15 = C4*C5
    ROcp35_25 = S4*C5
    ROcp35_75 = C4*S5
    ROcp35_85 = S4*S5
    ROcp35_46 = ROcp35_75*S6-S4*C6
    ROcp35_56 = ROcp35_85*S6+C4*C6
    ROcp35_76 = ROcp35_75*C6+S4*S6
    ROcp35_86 = ROcp35_85*C6-C4*S6
    OMcp35_15 = -qd[5]*S4
    OMcp35_25 = qd[5]*C4
    OMcp35_16 = OMcp35_15+ROcp35_15*qd[6]
    OMcp35_26 = OMcp35_25+ROcp35_25*qd[6]
    OMcp35_36 = qd[4]-qd[6]*S5
    OPcp35_16 = ROcp35_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp35_25*S5+ROcp35_25*qd[4])
    OPcp35_26 = ROcp35_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp35_15*S5+ROcp35_15*qd[4])
    OPcp35_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_36_0_11 = = 
 
# Sensor Kinematics 


    ROcp35_432 = ROcp35_46*C32+ROcp35_76*S32
    ROcp35_532 = ROcp35_56*C32+ROcp35_86*S32
    ROcp35_632 = S32p6*C5
    ROcp35_732 = -(ROcp35_46*S32-ROcp35_76*C32)
    ROcp35_832 = -(ROcp35_56*S32-ROcp35_86*C32)
    ROcp35_932 = C32p6*C5
    ROcp35_133 = ROcp35_15*C33+ROcp35_432*S33
    ROcp35_233 = ROcp35_25*C33+ROcp35_532*S33
    ROcp35_333 = ROcp35_632*S33-C33*S5
    ROcp35_433 = -(ROcp35_15*S33-ROcp35_432*C33)
    ROcp35_533 = -(ROcp35_25*S33-ROcp35_532*C33)
    ROcp35_633 = ROcp35_632*C33+S33*S5
    ROcp35_434 = ROcp35_433*C34+ROcp35_732*S34
    ROcp35_534 = ROcp35_533*C34+ROcp35_832*S34
    ROcp35_634 = ROcp35_633*C34+ROcp35_932*S34
    ROcp35_734 = -(ROcp35_433*S34-ROcp35_732*C34)
    ROcp35_834 = -(ROcp35_533*S34-ROcp35_832*C34)
    ROcp35_934 = -(ROcp35_633*S34-ROcp35_932*C34)
    ROcp35_135 = ROcp35_133*C35-ROcp35_734*S35
    ROcp35_235 = ROcp35_233*C35-ROcp35_834*S35
    ROcp35_335 = ROcp35_333*C35-ROcp35_934*S35
    ROcp35_735 = ROcp35_133*S35+ROcp35_734*C35
    ROcp35_835 = ROcp35_233*S35+ROcp35_834*C35
    ROcp35_935 = ROcp35_333*S35+ROcp35_934*C35
    ROcp35_136 = ROcp35_135*C36+ROcp35_434*S36
    ROcp35_236 = ROcp35_235*C36+ROcp35_534*S36
    ROcp35_336 = ROcp35_335*C36+ROcp35_634*S36
    ROcp35_436 = -(ROcp35_135*S36-ROcp35_434*C36)
    ROcp35_536 = -(ROcp35_235*S36-ROcp35_534*C36)
    ROcp35_636 = -(ROcp35_335*S36-ROcp35_634*C36)
    RLcp35_132 = ROcp35_15*s.dpt[1,12]+ROcp35_46*s.dpt[2,12]
    RLcp35_232 = ROcp35_25*s.dpt[1,12]+ROcp35_56*s.dpt[2,12]
    RLcp35_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp35_132 = OMcp35_16+ROcp35_15*qd[32]
    OMcp35_232 = OMcp35_26+ROcp35_25*qd[32]
    OMcp35_332 = OMcp35_36-qd[32]*S5
    ORcp35_132 = OMcp35_26*RLcp35_332-OMcp35_36*RLcp35_232
    ORcp35_232 = -(OMcp35_16*RLcp35_332-OMcp35_36*RLcp35_132)
    ORcp35_332 = OMcp35_16*RLcp35_232-OMcp35_26*RLcp35_132
    OMcp35_133 = OMcp35_132+ROcp35_732*qd[33]
    OMcp35_233 = OMcp35_232+ROcp35_832*qd[33]
    OMcp35_333 = OMcp35_332+ROcp35_932*qd[33]
    OPcp35_133 = OPcp35_16+ROcp35_15*qdd[32]+ROcp35_732*qdd[33]-qd[32]*(OMcp35_26*S5+OMcp35_36*ROcp35_25)+qd[33]*(\
   OMcp35_232*ROcp35_932-OMcp35_332*ROcp35_832)
    OPcp35_233 = OPcp35_26+ROcp35_25*qdd[32]+ROcp35_832*qdd[33]+qd[32]*(OMcp35_16*S5+OMcp35_36*ROcp35_15)-qd[33]*(\
   OMcp35_132*ROcp35_932-OMcp35_332*ROcp35_732)
    OPcp35_333 = OPcp35_36+ROcp35_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp35_16*ROcp35_25-OMcp35_26*ROcp35_15)+qd[33]*(\
   OMcp35_132*ROcp35_832-OMcp35_232*ROcp35_732)
    RLcp35_134 = ROcp35_433*s.dpt[2,33]
    RLcp35_234 = ROcp35_533*s.dpt[2,33]
    RLcp35_334 = ROcp35_633*s.dpt[2,33]
    POcp35_134 = RLcp35_132+RLcp35_134+q[1]
    POcp35_234 = RLcp35_232+RLcp35_234+q[2]
    POcp35_334 = RLcp35_332+RLcp35_334+q[3]
    OMcp35_134 = OMcp35_133+ROcp35_133*qd[34]
    OMcp35_234 = OMcp35_233+ROcp35_233*qd[34]
    OMcp35_334 = OMcp35_333+ROcp35_333*qd[34]
    ORcp35_134 = OMcp35_233*RLcp35_334-OMcp35_333*RLcp35_234
    ORcp35_234 = -(OMcp35_133*RLcp35_334-OMcp35_333*RLcp35_134)
    ORcp35_334 = OMcp35_133*RLcp35_234-OMcp35_233*RLcp35_134
    VIcp35_134 = ORcp35_132+ORcp35_134+qd[1]
    VIcp35_234 = ORcp35_232+ORcp35_234+qd[2]
    VIcp35_334 = ORcp35_332+ORcp35_334+qd[3]
    ACcp35_134 = qdd[1]+OMcp35_233*ORcp35_334+OMcp35_26*ORcp35_332-OMcp35_333*ORcp35_234-OMcp35_36*ORcp35_232+OPcp35_233*\
   RLcp35_334+OPcp35_26*RLcp35_332-OPcp35_333*RLcp35_234-OPcp35_36*RLcp35_232
    ACcp35_234 = qdd[2]-OMcp35_133*ORcp35_334-OMcp35_16*ORcp35_332+OMcp35_333*ORcp35_134+OMcp35_36*ORcp35_132-OPcp35_133*\
   RLcp35_334-OPcp35_16*RLcp35_332+OPcp35_333*RLcp35_134+OPcp35_36*RLcp35_132
    ACcp35_334 = qdd[3]+OMcp35_133*ORcp35_234+OMcp35_16*ORcp35_232-OMcp35_233*ORcp35_134-OMcp35_26*ORcp35_132+OPcp35_133*\
   RLcp35_234+OPcp35_16*RLcp35_232-OPcp35_233*RLcp35_134-OPcp35_26*RLcp35_132
    OMcp35_135 = OMcp35_134+ROcp35_434*qd[35]
    OMcp35_235 = OMcp35_234+ROcp35_534*qd[35]
    OMcp35_335 = OMcp35_334+ROcp35_634*qd[35]
    OMcp35_136 = OMcp35_135+ROcp35_735*qd[36]
    OMcp35_236 = OMcp35_235+ROcp35_835*qd[36]
    OMcp35_336 = OMcp35_335+ROcp35_935*qd[36]
    OPcp35_136 = OPcp35_133+ROcp35_133*qdd[34]+ROcp35_434*qdd[35]+ROcp35_735*qdd[36]+qd[34]*(OMcp35_233*ROcp35_333-\
   OMcp35_333*ROcp35_233)+qd[35]*(OMcp35_234*ROcp35_634-OMcp35_334*ROcp35_534)+qd[36]*(OMcp35_235*ROcp35_935-OMcp35_335*\
   ROcp35_835)
    OPcp35_236 = OPcp35_233+ROcp35_233*qdd[34]+ROcp35_534*qdd[35]+ROcp35_835*qdd[36]-qd[34]*(OMcp35_133*ROcp35_333-\
   OMcp35_333*ROcp35_133)-qd[35]*(OMcp35_134*ROcp35_634-OMcp35_334*ROcp35_434)-qd[36]*(OMcp35_135*ROcp35_935-OMcp35_335*\
   ROcp35_735)
    OPcp35_336 = OPcp35_333+ROcp35_333*qdd[34]+ROcp35_634*qdd[35]+ROcp35_935*qdd[36]+qd[34]*(OMcp35_133*ROcp35_233-\
   OMcp35_233*ROcp35_133)+qd[35]*(OMcp35_134*ROcp35_534-OMcp35_234*ROcp35_434)+qd[36]*(OMcp35_135*ROcp35_835-OMcp35_235*\
   ROcp35_735)

# = = Block_1_0_0_36_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp35_134
    sens.P[2] = POcp35_234
    sens.P[3] = POcp35_334
    sens.R[1,1] = ROcp35_136
    sens.R[1,2] = ROcp35_236
    sens.R[1,3] = ROcp35_336
    sens.R[2,1] = ROcp35_436
    sens.R[2,2] = ROcp35_536
    sens.R[2,3] = ROcp35_636
    sens.R[3,1] = ROcp35_735
    sens.R[3,2] = ROcp35_835
    sens.R[3,3] = ROcp35_935
    sens.V[1] = VIcp35_134
    sens.V[2] = VIcp35_234
    sens.V[3] = VIcp35_334
    sens.OM[1] = OMcp35_136
    sens.OM[2] = OMcp35_236
    sens.OM[3] = OMcp35_336
    sens.A[1] = ACcp35_134
    sens.A[2] = ACcp35_234
    sens.A[3] = ACcp35_334
    sens.OMP[1] = OPcp35_136
    sens.OMP[2] = OPcp35_236
    sens.OMP[3] = OPcp35_336
 
# 
  elif(isens==37): 


# = = Block_1_0_0_37_0_1 = = 
 
# Sensor Kinematics 


    ROcp36_15 = C4*C5
    ROcp36_25 = S4*C5
    ROcp36_75 = C4*S5
    ROcp36_85 = S4*S5
    ROcp36_46 = ROcp36_75*S6-S4*C6
    ROcp36_56 = ROcp36_85*S6+C4*C6
    ROcp36_76 = ROcp36_75*C6+S4*S6
    ROcp36_86 = ROcp36_85*C6-C4*S6
    OMcp36_15 = -qd[5]*S4
    OMcp36_25 = qd[5]*C4
    OMcp36_16 = OMcp36_15+ROcp36_15*qd[6]
    OMcp36_26 = OMcp36_25+ROcp36_25*qd[6]
    OMcp36_36 = qd[4]-qd[6]*S5
    OPcp36_16 = ROcp36_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp36_25*S5+ROcp36_25*qd[4])
    OPcp36_26 = ROcp36_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp36_15*S5+ROcp36_15*qd[4])
    OPcp36_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_37_0_11 = = 
 
# Sensor Kinematics 


    ROcp36_432 = ROcp36_46*C32+ROcp36_76*S32
    ROcp36_532 = ROcp36_56*C32+ROcp36_86*S32
    ROcp36_632 = S32p6*C5
    ROcp36_732 = -(ROcp36_46*S32-ROcp36_76*C32)
    ROcp36_832 = -(ROcp36_56*S32-ROcp36_86*C32)
    ROcp36_932 = C32p6*C5
    ROcp36_133 = ROcp36_15*C33+ROcp36_432*S33
    ROcp36_233 = ROcp36_25*C33+ROcp36_532*S33
    ROcp36_333 = ROcp36_632*S33-C33*S5
    ROcp36_433 = -(ROcp36_15*S33-ROcp36_432*C33)
    ROcp36_533 = -(ROcp36_25*S33-ROcp36_532*C33)
    ROcp36_633 = ROcp36_632*C33+S33*S5
    ROcp36_434 = ROcp36_433*C34+ROcp36_732*S34
    ROcp36_534 = ROcp36_533*C34+ROcp36_832*S34
    ROcp36_634 = ROcp36_633*C34+ROcp36_932*S34
    ROcp36_734 = -(ROcp36_433*S34-ROcp36_732*C34)
    ROcp36_834 = -(ROcp36_533*S34-ROcp36_832*C34)
    ROcp36_934 = -(ROcp36_633*S34-ROcp36_932*C34)
    ROcp36_135 = ROcp36_133*C35-ROcp36_734*S35
    ROcp36_235 = ROcp36_233*C35-ROcp36_834*S35
    ROcp36_335 = ROcp36_333*C35-ROcp36_934*S35
    ROcp36_735 = ROcp36_133*S35+ROcp36_734*C35
    ROcp36_835 = ROcp36_233*S35+ROcp36_834*C35
    ROcp36_935 = ROcp36_333*S35+ROcp36_934*C35
    ROcp36_136 = ROcp36_135*C36+ROcp36_434*S36
    ROcp36_236 = ROcp36_235*C36+ROcp36_534*S36
    ROcp36_336 = ROcp36_335*C36+ROcp36_634*S36
    ROcp36_436 = -(ROcp36_135*S36-ROcp36_434*C36)
    ROcp36_536 = -(ROcp36_235*S36-ROcp36_534*C36)
    ROcp36_636 = -(ROcp36_335*S36-ROcp36_634*C36)
    RLcp36_132 = ROcp36_15*s.dpt[1,12]+ROcp36_46*s.dpt[2,12]
    RLcp36_232 = ROcp36_25*s.dpt[1,12]+ROcp36_56*s.dpt[2,12]
    RLcp36_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp36_132 = OMcp36_16+ROcp36_15*qd[32]
    OMcp36_232 = OMcp36_26+ROcp36_25*qd[32]
    OMcp36_332 = OMcp36_36-qd[32]*S5
    ORcp36_132 = OMcp36_26*RLcp36_332-OMcp36_36*RLcp36_232
    ORcp36_232 = -(OMcp36_16*RLcp36_332-OMcp36_36*RLcp36_132)
    ORcp36_332 = OMcp36_16*RLcp36_232-OMcp36_26*RLcp36_132
    OMcp36_133 = OMcp36_132+ROcp36_732*qd[33]
    OMcp36_233 = OMcp36_232+ROcp36_832*qd[33]
    OMcp36_333 = OMcp36_332+ROcp36_932*qd[33]
    OPcp36_133 = OPcp36_16+ROcp36_15*qdd[32]+ROcp36_732*qdd[33]-qd[32]*(OMcp36_26*S5+OMcp36_36*ROcp36_25)+qd[33]*(\
   OMcp36_232*ROcp36_932-OMcp36_332*ROcp36_832)
    OPcp36_233 = OPcp36_26+ROcp36_25*qdd[32]+ROcp36_832*qdd[33]+qd[32]*(OMcp36_16*S5+OMcp36_36*ROcp36_15)-qd[33]*(\
   OMcp36_132*ROcp36_932-OMcp36_332*ROcp36_732)
    OPcp36_333 = OPcp36_36+ROcp36_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp36_16*ROcp36_25-OMcp36_26*ROcp36_15)+qd[33]*(\
   OMcp36_132*ROcp36_832-OMcp36_232*ROcp36_732)
    RLcp36_134 = ROcp36_433*s.dpt[2,33]
    RLcp36_234 = ROcp36_533*s.dpt[2,33]
    RLcp36_334 = ROcp36_633*s.dpt[2,33]
    OMcp36_134 = OMcp36_133+ROcp36_133*qd[34]
    OMcp36_234 = OMcp36_233+ROcp36_233*qd[34]
    OMcp36_334 = OMcp36_333+ROcp36_333*qd[34]
    ORcp36_134 = OMcp36_233*RLcp36_334-OMcp36_333*RLcp36_234
    ORcp36_234 = -(OMcp36_133*RLcp36_334-OMcp36_333*RLcp36_134)
    ORcp36_334 = OMcp36_133*RLcp36_234-OMcp36_233*RLcp36_134
    OMcp36_135 = OMcp36_134+ROcp36_434*qd[35]
    OMcp36_235 = OMcp36_234+ROcp36_534*qd[35]
    OMcp36_335 = OMcp36_334+ROcp36_634*qd[35]
    OMcp36_136 = OMcp36_135+ROcp36_735*qd[36]
    OMcp36_236 = OMcp36_235+ROcp36_835*qd[36]
    OMcp36_336 = OMcp36_335+ROcp36_935*qd[36]
    OPcp36_136 = OPcp36_133+ROcp36_133*qdd[34]+ROcp36_434*qdd[35]+ROcp36_735*qdd[36]+qd[34]*(OMcp36_233*ROcp36_333-\
   OMcp36_333*ROcp36_233)+qd[35]*(OMcp36_234*ROcp36_634-OMcp36_334*ROcp36_534)+qd[36]*(OMcp36_235*ROcp36_935-OMcp36_335*\
   ROcp36_835)
    OPcp36_236 = OPcp36_233+ROcp36_233*qdd[34]+ROcp36_534*qdd[35]+ROcp36_835*qdd[36]-qd[34]*(OMcp36_133*ROcp36_333-\
   OMcp36_333*ROcp36_133)-qd[35]*(OMcp36_134*ROcp36_634-OMcp36_334*ROcp36_434)-qd[36]*(OMcp36_135*ROcp36_935-OMcp36_335*\
   ROcp36_735)
    OPcp36_336 = OPcp36_333+ROcp36_333*qdd[34]+ROcp36_634*qdd[35]+ROcp36_935*qdd[36]+qd[34]*(OMcp36_133*ROcp36_233-\
   OMcp36_233*ROcp36_133)+qd[35]*(OMcp36_134*ROcp36_534-OMcp36_234*ROcp36_434)+qd[36]*(OMcp36_135*ROcp36_835-OMcp36_235*\
   ROcp36_735)

# = = Block_1_0_0_37_0_12 = = 
 
# Sensor Kinematics 


    ROcp36_437 = ROcp36_436*C37+ROcp36_735*S37
    ROcp36_537 = ROcp36_536*C37+ROcp36_835*S37
    ROcp36_637 = ROcp36_636*C37+ROcp36_935*S37
    ROcp36_737 = -(ROcp36_436*S37-ROcp36_735*C37)
    ROcp36_837 = -(ROcp36_536*S37-ROcp36_835*C37)
    ROcp36_937 = -(ROcp36_636*S37-ROcp36_935*C37)
    RLcp36_137 = ROcp36_735*s.dpt[3,36]
    RLcp36_237 = ROcp36_835*s.dpt[3,36]
    RLcp36_337 = ROcp36_935*s.dpt[3,36]
    POcp36_137 = RLcp36_132+RLcp36_134+RLcp36_137+q[1]
    POcp36_237 = RLcp36_232+RLcp36_234+RLcp36_237+q[2]
    POcp36_337 = RLcp36_332+RLcp36_334+RLcp36_337+q[3]
    OMcp36_137 = OMcp36_136+ROcp36_136*qd[37]
    OMcp36_237 = OMcp36_236+ROcp36_236*qd[37]
    OMcp36_337 = OMcp36_336+ROcp36_336*qd[37]
    ORcp36_137 = OMcp36_236*RLcp36_337-OMcp36_336*RLcp36_237
    ORcp36_237 = -(OMcp36_136*RLcp36_337-OMcp36_336*RLcp36_137)
    ORcp36_337 = OMcp36_136*RLcp36_237-OMcp36_236*RLcp36_137
    VIcp36_137 = ORcp36_132+ORcp36_134+ORcp36_137+qd[1]
    VIcp36_237 = ORcp36_232+ORcp36_234+ORcp36_237+qd[2]
    VIcp36_337 = ORcp36_332+ORcp36_334+ORcp36_337+qd[3]
    OPcp36_137 = OPcp36_136+ROcp36_136*qdd[37]+qd[37]*(OMcp36_236*ROcp36_336-OMcp36_336*ROcp36_236)
    OPcp36_237 = OPcp36_236+ROcp36_236*qdd[37]-qd[37]*(OMcp36_136*ROcp36_336-OMcp36_336*ROcp36_136)
    OPcp36_337 = OPcp36_336+ROcp36_336*qdd[37]+qd[37]*(OMcp36_136*ROcp36_236-OMcp36_236*ROcp36_136)
    ACcp36_137 = qdd[1]+OMcp36_233*ORcp36_334+OMcp36_236*ORcp36_337+OMcp36_26*ORcp36_332-OMcp36_333*ORcp36_234-OMcp36_336*\
   ORcp36_237-OMcp36_36*ORcp36_232+OPcp36_233*RLcp36_334+OPcp36_236*RLcp36_337+OPcp36_26*RLcp36_332-OPcp36_333*RLcp36_234-\
   OPcp36_336*RLcp36_237-OPcp36_36*RLcp36_232
    ACcp36_237 = qdd[2]-OMcp36_133*ORcp36_334-OMcp36_136*ORcp36_337-OMcp36_16*ORcp36_332+OMcp36_333*ORcp36_134+OMcp36_336*\
   ORcp36_137+OMcp36_36*ORcp36_132-OPcp36_133*RLcp36_334-OPcp36_136*RLcp36_337-OPcp36_16*RLcp36_332+OPcp36_333*RLcp36_134+\
   OPcp36_336*RLcp36_137+OPcp36_36*RLcp36_132
    ACcp36_337 = qdd[3]+OMcp36_133*ORcp36_234+OMcp36_136*ORcp36_237+OMcp36_16*ORcp36_232-OMcp36_233*ORcp36_134-OMcp36_236*\
   ORcp36_137-OMcp36_26*ORcp36_132+OPcp36_133*RLcp36_234+OPcp36_136*RLcp36_237+OPcp36_16*RLcp36_232-OPcp36_233*RLcp36_134-\
   OPcp36_236*RLcp36_137-OPcp36_26*RLcp36_132

# = = Block_1_0_0_37_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp36_137
    sens.P[2] = POcp36_237
    sens.P[3] = POcp36_337
    sens.R[1,1] = ROcp36_136
    sens.R[1,2] = ROcp36_236
    sens.R[1,3] = ROcp36_336
    sens.R[2,1] = ROcp36_437
    sens.R[2,2] = ROcp36_537
    sens.R[2,3] = ROcp36_637
    sens.R[3,1] = ROcp36_737
    sens.R[3,2] = ROcp36_837
    sens.R[3,3] = ROcp36_937
    sens.V[1] = VIcp36_137
    sens.V[2] = VIcp36_237
    sens.V[3] = VIcp36_337
    sens.OM[1] = OMcp36_137
    sens.OM[2] = OMcp36_237
    sens.OM[3] = OMcp36_337
    sens.A[1] = ACcp36_137
    sens.A[2] = ACcp36_237
    sens.A[3] = ACcp36_337
    sens.OMP[1] = OPcp36_137
    sens.OMP[2] = OPcp36_237
    sens.OMP[3] = OPcp36_337
 
# 
  elif(isens==38): 


# = = Block_1_0_0_38_0_1 = = 
 
# Sensor Kinematics 


    ROcp37_15 = C4*C5
    ROcp37_25 = S4*C5
    ROcp37_75 = C4*S5
    ROcp37_85 = S4*S5
    ROcp37_46 = ROcp37_75*S6-S4*C6
    ROcp37_56 = ROcp37_85*S6+C4*C6
    ROcp37_76 = ROcp37_75*C6+S4*S6
    ROcp37_86 = ROcp37_85*C6-C4*S6
    OMcp37_15 = -qd[5]*S4
    OMcp37_25 = qd[5]*C4
    OMcp37_16 = OMcp37_15+ROcp37_15*qd[6]
    OMcp37_26 = OMcp37_25+ROcp37_25*qd[6]
    OMcp37_36 = qd[4]-qd[6]*S5
    OPcp37_16 = ROcp37_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp37_25*S5+ROcp37_25*qd[4])
    OPcp37_26 = ROcp37_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp37_15*S5+ROcp37_15*qd[4])
    OPcp37_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_38_0_11 = = 
 
# Sensor Kinematics 


    ROcp37_432 = ROcp37_46*C32+ROcp37_76*S32
    ROcp37_532 = ROcp37_56*C32+ROcp37_86*S32
    ROcp37_632 = S32p6*C5
    ROcp37_732 = -(ROcp37_46*S32-ROcp37_76*C32)
    ROcp37_832 = -(ROcp37_56*S32-ROcp37_86*C32)
    ROcp37_932 = C32p6*C5
    ROcp37_133 = ROcp37_15*C33+ROcp37_432*S33
    ROcp37_233 = ROcp37_25*C33+ROcp37_532*S33
    ROcp37_333 = ROcp37_632*S33-C33*S5
    ROcp37_433 = -(ROcp37_15*S33-ROcp37_432*C33)
    ROcp37_533 = -(ROcp37_25*S33-ROcp37_532*C33)
    ROcp37_633 = ROcp37_632*C33+S33*S5
    ROcp37_434 = ROcp37_433*C34+ROcp37_732*S34
    ROcp37_534 = ROcp37_533*C34+ROcp37_832*S34
    ROcp37_634 = ROcp37_633*C34+ROcp37_932*S34
    ROcp37_734 = -(ROcp37_433*S34-ROcp37_732*C34)
    ROcp37_834 = -(ROcp37_533*S34-ROcp37_832*C34)
    ROcp37_934 = -(ROcp37_633*S34-ROcp37_932*C34)
    ROcp37_135 = ROcp37_133*C35-ROcp37_734*S35
    ROcp37_235 = ROcp37_233*C35-ROcp37_834*S35
    ROcp37_335 = ROcp37_333*C35-ROcp37_934*S35
    ROcp37_735 = ROcp37_133*S35+ROcp37_734*C35
    ROcp37_835 = ROcp37_233*S35+ROcp37_834*C35
    ROcp37_935 = ROcp37_333*S35+ROcp37_934*C35
    ROcp37_136 = ROcp37_135*C36+ROcp37_434*S36
    ROcp37_236 = ROcp37_235*C36+ROcp37_534*S36
    ROcp37_336 = ROcp37_335*C36+ROcp37_634*S36
    ROcp37_436 = -(ROcp37_135*S36-ROcp37_434*C36)
    ROcp37_536 = -(ROcp37_235*S36-ROcp37_534*C36)
    ROcp37_636 = -(ROcp37_335*S36-ROcp37_634*C36)
    RLcp37_132 = ROcp37_15*s.dpt[1,12]+ROcp37_46*s.dpt[2,12]
    RLcp37_232 = ROcp37_25*s.dpt[1,12]+ROcp37_56*s.dpt[2,12]
    RLcp37_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp37_132 = OMcp37_16+ROcp37_15*qd[32]
    OMcp37_232 = OMcp37_26+ROcp37_25*qd[32]
    OMcp37_332 = OMcp37_36-qd[32]*S5
    ORcp37_132 = OMcp37_26*RLcp37_332-OMcp37_36*RLcp37_232
    ORcp37_232 = -(OMcp37_16*RLcp37_332-OMcp37_36*RLcp37_132)
    ORcp37_332 = OMcp37_16*RLcp37_232-OMcp37_26*RLcp37_132
    OMcp37_133 = OMcp37_132+ROcp37_732*qd[33]
    OMcp37_233 = OMcp37_232+ROcp37_832*qd[33]
    OMcp37_333 = OMcp37_332+ROcp37_932*qd[33]
    OPcp37_133 = OPcp37_16+ROcp37_15*qdd[32]+ROcp37_732*qdd[33]-qd[32]*(OMcp37_26*S5+OMcp37_36*ROcp37_25)+qd[33]*(\
   OMcp37_232*ROcp37_932-OMcp37_332*ROcp37_832)
    OPcp37_233 = OPcp37_26+ROcp37_25*qdd[32]+ROcp37_832*qdd[33]+qd[32]*(OMcp37_16*S5+OMcp37_36*ROcp37_15)-qd[33]*(\
   OMcp37_132*ROcp37_932-OMcp37_332*ROcp37_732)
    OPcp37_333 = OPcp37_36+ROcp37_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp37_16*ROcp37_25-OMcp37_26*ROcp37_15)+qd[33]*(\
   OMcp37_132*ROcp37_832-OMcp37_232*ROcp37_732)
    RLcp37_134 = ROcp37_433*s.dpt[2,33]
    RLcp37_234 = ROcp37_533*s.dpt[2,33]
    RLcp37_334 = ROcp37_633*s.dpt[2,33]
    OMcp37_134 = OMcp37_133+ROcp37_133*qd[34]
    OMcp37_234 = OMcp37_233+ROcp37_233*qd[34]
    OMcp37_334 = OMcp37_333+ROcp37_333*qd[34]
    ORcp37_134 = OMcp37_233*RLcp37_334-OMcp37_333*RLcp37_234
    ORcp37_234 = -(OMcp37_133*RLcp37_334-OMcp37_333*RLcp37_134)
    ORcp37_334 = OMcp37_133*RLcp37_234-OMcp37_233*RLcp37_134
    OMcp37_135 = OMcp37_134+ROcp37_434*qd[35]
    OMcp37_235 = OMcp37_234+ROcp37_534*qd[35]
    OMcp37_335 = OMcp37_334+ROcp37_634*qd[35]
    OMcp37_136 = OMcp37_135+ROcp37_735*qd[36]
    OMcp37_236 = OMcp37_235+ROcp37_835*qd[36]
    OMcp37_336 = OMcp37_335+ROcp37_935*qd[36]
    OPcp37_136 = OPcp37_133+ROcp37_133*qdd[34]+ROcp37_434*qdd[35]+ROcp37_735*qdd[36]+qd[34]*(OMcp37_233*ROcp37_333-\
   OMcp37_333*ROcp37_233)+qd[35]*(OMcp37_234*ROcp37_634-OMcp37_334*ROcp37_534)+qd[36]*(OMcp37_235*ROcp37_935-OMcp37_335*\
   ROcp37_835)
    OPcp37_236 = OPcp37_233+ROcp37_233*qdd[34]+ROcp37_534*qdd[35]+ROcp37_835*qdd[36]-qd[34]*(OMcp37_133*ROcp37_333-\
   OMcp37_333*ROcp37_133)-qd[35]*(OMcp37_134*ROcp37_634-OMcp37_334*ROcp37_434)-qd[36]*(OMcp37_135*ROcp37_935-OMcp37_335*\
   ROcp37_735)
    OPcp37_336 = OPcp37_333+ROcp37_333*qdd[34]+ROcp37_634*qdd[35]+ROcp37_935*qdd[36]+qd[34]*(OMcp37_133*ROcp37_233-\
   OMcp37_233*ROcp37_133)+qd[35]*(OMcp37_134*ROcp37_534-OMcp37_234*ROcp37_434)+qd[36]*(OMcp37_135*ROcp37_835-OMcp37_235*\
   ROcp37_735)

# = = Block_1_0_0_38_0_12 = = 
 
# Sensor Kinematics 


    ROcp37_437 = ROcp37_436*C37+ROcp37_735*S37
    ROcp37_537 = ROcp37_536*C37+ROcp37_835*S37
    ROcp37_637 = ROcp37_636*C37+ROcp37_935*S37
    ROcp37_737 = -(ROcp37_436*S37-ROcp37_735*C37)
    ROcp37_837 = -(ROcp37_536*S37-ROcp37_835*C37)
    ROcp37_937 = -(ROcp37_636*S37-ROcp37_935*C37)
    RLcp37_137 = ROcp37_735*s.dpt[3,36]
    RLcp37_237 = ROcp37_835*s.dpt[3,36]
    RLcp37_337 = ROcp37_935*s.dpt[3,36]
    OMcp37_137 = OMcp37_136+ROcp37_136*qd[37]
    OMcp37_237 = OMcp37_236+ROcp37_236*qd[37]
    OMcp37_337 = OMcp37_336+ROcp37_336*qd[37]
    ORcp37_137 = OMcp37_236*RLcp37_337-OMcp37_336*RLcp37_237
    ORcp37_237 = -(OMcp37_136*RLcp37_337-OMcp37_336*RLcp37_137)
    ORcp37_337 = OMcp37_136*RLcp37_237-OMcp37_236*RLcp37_137
    OPcp37_137 = OPcp37_136+ROcp37_136*qdd[37]+qd[37]*(OMcp37_236*ROcp37_336-OMcp37_336*ROcp37_236)
    OPcp37_237 = OPcp37_236+ROcp37_236*qdd[37]-qd[37]*(OMcp37_136*ROcp37_336-OMcp37_336*ROcp37_136)
    OPcp37_337 = OPcp37_336+ROcp37_336*qdd[37]+qd[37]*(OMcp37_136*ROcp37_236-OMcp37_236*ROcp37_136)
    RLcp37_138 = ROcp37_737*q[38]
    RLcp37_238 = ROcp37_837*q[38]
    RLcp37_338 = ROcp37_937*q[38]
    POcp37_138 = RLcp37_132+RLcp37_134+RLcp37_137+RLcp37_138+q[1]
    POcp37_238 = RLcp37_232+RLcp37_234+RLcp37_237+RLcp37_238+q[2]
    POcp37_338 = RLcp37_332+RLcp37_334+RLcp37_337+RLcp37_338+q[3]
    ORcp37_138 = OMcp37_237*RLcp37_338-OMcp37_337*RLcp37_238
    ORcp37_238 = -(OMcp37_137*RLcp37_338-OMcp37_337*RLcp37_138)
    ORcp37_338 = OMcp37_137*RLcp37_238-OMcp37_237*RLcp37_138
    VIcp37_138 = ORcp37_132+ORcp37_134+ORcp37_137+ORcp37_138+qd[1]+ROcp37_737*qd[38]
    VIcp37_238 = ORcp37_232+ORcp37_234+ORcp37_237+ORcp37_238+qd[2]+ROcp37_837*qd[38]
    VIcp37_338 = ORcp37_332+ORcp37_334+ORcp37_337+ORcp37_338+qd[3]+ROcp37_937*qd[38]
    ACcp37_138 = qdd[1]+OMcp37_233*ORcp37_334+OMcp37_236*ORcp37_337+OMcp37_237*ORcp37_338+OMcp37_26*ORcp37_332-OMcp37_333*\
   ORcp37_234-OMcp37_336*ORcp37_237-OMcp37_337*ORcp37_238-OMcp37_36*ORcp37_232+OPcp37_233*RLcp37_334+OPcp37_236*RLcp37_337+\
   OPcp37_237*RLcp37_338+OPcp37_26*RLcp37_332-OPcp37_333*RLcp37_234-OPcp37_336*RLcp37_237-OPcp37_337*RLcp37_238-OPcp37_36*\
   RLcp37_232+ROcp37_737*qdd[38]+(2.0)*qd[38]*(OMcp37_237*ROcp37_937-OMcp37_337*ROcp37_837)
    ACcp37_238 = qdd[2]-OMcp37_133*ORcp37_334-OMcp37_136*ORcp37_337-OMcp37_137*ORcp37_338-OMcp37_16*ORcp37_332+OMcp37_333*\
   ORcp37_134+OMcp37_336*ORcp37_137+OMcp37_337*ORcp37_138+OMcp37_36*ORcp37_132-OPcp37_133*RLcp37_334-OPcp37_136*RLcp37_337-\
   OPcp37_137*RLcp37_338-OPcp37_16*RLcp37_332+OPcp37_333*RLcp37_134+OPcp37_336*RLcp37_137+OPcp37_337*RLcp37_138+OPcp37_36*\
   RLcp37_132+ROcp37_837*qdd[38]-(2.0)*qd[38]*(OMcp37_137*ROcp37_937-OMcp37_337*ROcp37_737)
    ACcp37_338 = qdd[3]+OMcp37_133*ORcp37_234+OMcp37_136*ORcp37_237+OMcp37_137*ORcp37_238+OMcp37_16*ORcp37_232-OMcp37_233*\
   ORcp37_134-OMcp37_236*ORcp37_137-OMcp37_237*ORcp37_138-OMcp37_26*ORcp37_132+OPcp37_133*RLcp37_234+OPcp37_136*RLcp37_237+\
   OPcp37_137*RLcp37_238+OPcp37_16*RLcp37_232-OPcp37_233*RLcp37_134-OPcp37_236*RLcp37_137-OPcp37_237*RLcp37_138-OPcp37_26*\
   RLcp37_132+ROcp37_937*qdd[38]+(2.0)*qd[38]*(OMcp37_137*ROcp37_837-OMcp37_237*ROcp37_737)

# = = Block_1_0_0_38_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp37_138
    sens.P[2] = POcp37_238
    sens.P[3] = POcp37_338
    sens.R[1,1] = ROcp37_136
    sens.R[1,2] = ROcp37_236
    sens.R[1,3] = ROcp37_336
    sens.R[2,1] = ROcp37_437
    sens.R[2,2] = ROcp37_537
    sens.R[2,3] = ROcp37_637
    sens.R[3,1] = ROcp37_737
    sens.R[3,2] = ROcp37_837
    sens.R[3,3] = ROcp37_937
    sens.V[1] = VIcp37_138
    sens.V[2] = VIcp37_238
    sens.V[3] = VIcp37_338
    sens.OM[1] = OMcp37_137
    sens.OM[2] = OMcp37_237
    sens.OM[3] = OMcp37_337
    sens.A[1] = ACcp37_138
    sens.A[2] = ACcp37_238
    sens.A[3] = ACcp37_338
    sens.OMP[1] = OPcp37_137
    sens.OMP[2] = OPcp37_237
    sens.OMP[3] = OPcp37_337
 
# 
  elif(isens==39): 


# = = Block_1_0_0_39_0_1 = = 
 
# Sensor Kinematics 


    ROcp38_15 = C4*C5
    ROcp38_25 = S4*C5
    ROcp38_75 = C4*S5
    ROcp38_85 = S4*S5
    ROcp38_46 = ROcp38_75*S6-S4*C6
    ROcp38_56 = ROcp38_85*S6+C4*C6
    ROcp38_76 = ROcp38_75*C6+S4*S6
    ROcp38_86 = ROcp38_85*C6-C4*S6
    OMcp38_15 = -qd[5]*S4
    OMcp38_25 = qd[5]*C4
    OMcp38_16 = OMcp38_15+ROcp38_15*qd[6]
    OMcp38_26 = OMcp38_25+ROcp38_25*qd[6]
    OMcp38_36 = qd[4]-qd[6]*S5
    OPcp38_16 = ROcp38_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp38_25*S5+ROcp38_25*qd[4])
    OPcp38_26 = ROcp38_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp38_15*S5+ROcp38_15*qd[4])
    OPcp38_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_39_0_11 = = 
 
# Sensor Kinematics 


    ROcp38_432 = ROcp38_46*C32+ROcp38_76*S32
    ROcp38_532 = ROcp38_56*C32+ROcp38_86*S32
    ROcp38_632 = S32p6*C5
    ROcp38_732 = -(ROcp38_46*S32-ROcp38_76*C32)
    ROcp38_832 = -(ROcp38_56*S32-ROcp38_86*C32)
    ROcp38_932 = C32p6*C5
    ROcp38_133 = ROcp38_15*C33+ROcp38_432*S33
    ROcp38_233 = ROcp38_25*C33+ROcp38_532*S33
    ROcp38_333 = ROcp38_632*S33-C33*S5
    ROcp38_433 = -(ROcp38_15*S33-ROcp38_432*C33)
    ROcp38_533 = -(ROcp38_25*S33-ROcp38_532*C33)
    ROcp38_633 = ROcp38_632*C33+S33*S5
    ROcp38_434 = ROcp38_433*C34+ROcp38_732*S34
    ROcp38_534 = ROcp38_533*C34+ROcp38_832*S34
    ROcp38_634 = ROcp38_633*C34+ROcp38_932*S34
    ROcp38_734 = -(ROcp38_433*S34-ROcp38_732*C34)
    ROcp38_834 = -(ROcp38_533*S34-ROcp38_832*C34)
    ROcp38_934 = -(ROcp38_633*S34-ROcp38_932*C34)
    ROcp38_135 = ROcp38_133*C35-ROcp38_734*S35
    ROcp38_235 = ROcp38_233*C35-ROcp38_834*S35
    ROcp38_335 = ROcp38_333*C35-ROcp38_934*S35
    ROcp38_735 = ROcp38_133*S35+ROcp38_734*C35
    ROcp38_835 = ROcp38_233*S35+ROcp38_834*C35
    ROcp38_935 = ROcp38_333*S35+ROcp38_934*C35
    ROcp38_136 = ROcp38_135*C36+ROcp38_434*S36
    ROcp38_236 = ROcp38_235*C36+ROcp38_534*S36
    ROcp38_336 = ROcp38_335*C36+ROcp38_634*S36
    ROcp38_436 = -(ROcp38_135*S36-ROcp38_434*C36)
    ROcp38_536 = -(ROcp38_235*S36-ROcp38_534*C36)
    ROcp38_636 = -(ROcp38_335*S36-ROcp38_634*C36)
    RLcp38_132 = ROcp38_15*s.dpt[1,12]+ROcp38_46*s.dpt[2,12]
    RLcp38_232 = ROcp38_25*s.dpt[1,12]+ROcp38_56*s.dpt[2,12]
    RLcp38_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp38_132 = OMcp38_16+ROcp38_15*qd[32]
    OMcp38_232 = OMcp38_26+ROcp38_25*qd[32]
    OMcp38_332 = OMcp38_36-qd[32]*S5
    ORcp38_132 = OMcp38_26*RLcp38_332-OMcp38_36*RLcp38_232
    ORcp38_232 = -(OMcp38_16*RLcp38_332-OMcp38_36*RLcp38_132)
    ORcp38_332 = OMcp38_16*RLcp38_232-OMcp38_26*RLcp38_132
    OMcp38_133 = OMcp38_132+ROcp38_732*qd[33]
    OMcp38_233 = OMcp38_232+ROcp38_832*qd[33]
    OMcp38_333 = OMcp38_332+ROcp38_932*qd[33]
    OPcp38_133 = OPcp38_16+ROcp38_15*qdd[32]+ROcp38_732*qdd[33]-qd[32]*(OMcp38_26*S5+OMcp38_36*ROcp38_25)+qd[33]*(\
   OMcp38_232*ROcp38_932-OMcp38_332*ROcp38_832)
    OPcp38_233 = OPcp38_26+ROcp38_25*qdd[32]+ROcp38_832*qdd[33]+qd[32]*(OMcp38_16*S5+OMcp38_36*ROcp38_15)-qd[33]*(\
   OMcp38_132*ROcp38_932-OMcp38_332*ROcp38_732)
    OPcp38_333 = OPcp38_36+ROcp38_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp38_16*ROcp38_25-OMcp38_26*ROcp38_15)+qd[33]*(\
   OMcp38_132*ROcp38_832-OMcp38_232*ROcp38_732)
    RLcp38_134 = ROcp38_433*s.dpt[2,33]
    RLcp38_234 = ROcp38_533*s.dpt[2,33]
    RLcp38_334 = ROcp38_633*s.dpt[2,33]
    OMcp38_134 = OMcp38_133+ROcp38_133*qd[34]
    OMcp38_234 = OMcp38_233+ROcp38_233*qd[34]
    OMcp38_334 = OMcp38_333+ROcp38_333*qd[34]
    ORcp38_134 = OMcp38_233*RLcp38_334-OMcp38_333*RLcp38_234
    ORcp38_234 = -(OMcp38_133*RLcp38_334-OMcp38_333*RLcp38_134)
    ORcp38_334 = OMcp38_133*RLcp38_234-OMcp38_233*RLcp38_134
    OMcp38_135 = OMcp38_134+ROcp38_434*qd[35]
    OMcp38_235 = OMcp38_234+ROcp38_534*qd[35]
    OMcp38_335 = OMcp38_334+ROcp38_634*qd[35]
    OMcp38_136 = OMcp38_135+ROcp38_735*qd[36]
    OMcp38_236 = OMcp38_235+ROcp38_835*qd[36]
    OMcp38_336 = OMcp38_335+ROcp38_935*qd[36]
    OPcp38_136 = OPcp38_133+ROcp38_133*qdd[34]+ROcp38_434*qdd[35]+ROcp38_735*qdd[36]+qd[34]*(OMcp38_233*ROcp38_333-\
   OMcp38_333*ROcp38_233)+qd[35]*(OMcp38_234*ROcp38_634-OMcp38_334*ROcp38_534)+qd[36]*(OMcp38_235*ROcp38_935-OMcp38_335*\
   ROcp38_835)
    OPcp38_236 = OPcp38_233+ROcp38_233*qdd[34]+ROcp38_534*qdd[35]+ROcp38_835*qdd[36]-qd[34]*(OMcp38_133*ROcp38_333-\
   OMcp38_333*ROcp38_133)-qd[35]*(OMcp38_134*ROcp38_634-OMcp38_334*ROcp38_434)-qd[36]*(OMcp38_135*ROcp38_935-OMcp38_335*\
   ROcp38_735)
    OPcp38_336 = OPcp38_333+ROcp38_333*qdd[34]+ROcp38_634*qdd[35]+ROcp38_935*qdd[36]+qd[34]*(OMcp38_133*ROcp38_233-\
   OMcp38_233*ROcp38_133)+qd[35]*(OMcp38_134*ROcp38_534-OMcp38_234*ROcp38_434)+qd[36]*(OMcp38_135*ROcp38_835-OMcp38_235*\
   ROcp38_735)

# = = Block_1_0_0_39_0_13 = = 
 
# Sensor Kinematics 


    ROcp38_439 = ROcp38_436*C39+ROcp38_735*S39
    ROcp38_539 = ROcp38_536*C39+ROcp38_835*S39
    ROcp38_639 = ROcp38_636*C39+ROcp38_935*S39
    ROcp38_739 = -(ROcp38_436*S39-ROcp38_735*C39)
    ROcp38_839 = -(ROcp38_536*S39-ROcp38_835*C39)
    ROcp38_939 = -(ROcp38_636*S39-ROcp38_935*C39)
    RLcp38_139 = ROcp38_735*s.dpt[3,37]
    RLcp38_239 = ROcp38_835*s.dpt[3,37]
    RLcp38_339 = ROcp38_935*s.dpt[3,37]
    POcp38_139 = RLcp38_132+RLcp38_134+RLcp38_139+q[1]
    POcp38_239 = RLcp38_232+RLcp38_234+RLcp38_239+q[2]
    POcp38_339 = RLcp38_332+RLcp38_334+RLcp38_339+q[3]
    OMcp38_139 = OMcp38_136+ROcp38_136*qd[39]
    OMcp38_239 = OMcp38_236+ROcp38_236*qd[39]
    OMcp38_339 = OMcp38_336+ROcp38_336*qd[39]
    ORcp38_139 = OMcp38_236*RLcp38_339-OMcp38_336*RLcp38_239
    ORcp38_239 = -(OMcp38_136*RLcp38_339-OMcp38_336*RLcp38_139)
    ORcp38_339 = OMcp38_136*RLcp38_239-OMcp38_236*RLcp38_139
    VIcp38_139 = ORcp38_132+ORcp38_134+ORcp38_139+qd[1]
    VIcp38_239 = ORcp38_232+ORcp38_234+ORcp38_239+qd[2]
    VIcp38_339 = ORcp38_332+ORcp38_334+ORcp38_339+qd[3]
    OPcp38_139 = OPcp38_136+ROcp38_136*qdd[39]+qd[39]*(OMcp38_236*ROcp38_336-OMcp38_336*ROcp38_236)
    OPcp38_239 = OPcp38_236+ROcp38_236*qdd[39]-qd[39]*(OMcp38_136*ROcp38_336-OMcp38_336*ROcp38_136)
    OPcp38_339 = OPcp38_336+ROcp38_336*qdd[39]+qd[39]*(OMcp38_136*ROcp38_236-OMcp38_236*ROcp38_136)
    ACcp38_139 = qdd[1]+OMcp38_233*ORcp38_334+OMcp38_236*ORcp38_339+OMcp38_26*ORcp38_332-OMcp38_333*ORcp38_234-OMcp38_336*\
   ORcp38_239-OMcp38_36*ORcp38_232+OPcp38_233*RLcp38_334+OPcp38_236*RLcp38_339+OPcp38_26*RLcp38_332-OPcp38_333*RLcp38_234-\
   OPcp38_336*RLcp38_239-OPcp38_36*RLcp38_232
    ACcp38_239 = qdd[2]-OMcp38_133*ORcp38_334-OMcp38_136*ORcp38_339-OMcp38_16*ORcp38_332+OMcp38_333*ORcp38_134+OMcp38_336*\
   ORcp38_139+OMcp38_36*ORcp38_132-OPcp38_133*RLcp38_334-OPcp38_136*RLcp38_339-OPcp38_16*RLcp38_332+OPcp38_333*RLcp38_134+\
   OPcp38_336*RLcp38_139+OPcp38_36*RLcp38_132
    ACcp38_339 = qdd[3]+OMcp38_133*ORcp38_234+OMcp38_136*ORcp38_239+OMcp38_16*ORcp38_232-OMcp38_233*ORcp38_134-OMcp38_236*\
   ORcp38_139-OMcp38_26*ORcp38_132+OPcp38_133*RLcp38_234+OPcp38_136*RLcp38_239+OPcp38_16*RLcp38_232-OPcp38_233*RLcp38_134-\
   OPcp38_236*RLcp38_139-OPcp38_26*RLcp38_132

# = = Block_1_0_0_39_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp38_139
    sens.P[2] = POcp38_239
    sens.P[3] = POcp38_339
    sens.R[1,1] = ROcp38_136
    sens.R[1,2] = ROcp38_236
    sens.R[1,3] = ROcp38_336
    sens.R[2,1] = ROcp38_439
    sens.R[2,2] = ROcp38_539
    sens.R[2,3] = ROcp38_639
    sens.R[3,1] = ROcp38_739
    sens.R[3,2] = ROcp38_839
    sens.R[3,3] = ROcp38_939
    sens.V[1] = VIcp38_139
    sens.V[2] = VIcp38_239
    sens.V[3] = VIcp38_339
    sens.OM[1] = OMcp38_139
    sens.OM[2] = OMcp38_239
    sens.OM[3] = OMcp38_339
    sens.A[1] = ACcp38_139
    sens.A[2] = ACcp38_239
    sens.A[3] = ACcp38_339
    sens.OMP[1] = OPcp38_139
    sens.OMP[2] = OPcp38_239
    sens.OMP[3] = OPcp38_339
 
# 
  elif(isens==40): 


# = = Block_1_0_0_40_0_1 = = 
 
# Sensor Kinematics 


    ROcp39_15 = C4*C5
    ROcp39_25 = S4*C5
    ROcp39_75 = C4*S5
    ROcp39_85 = S4*S5
    ROcp39_46 = ROcp39_75*S6-S4*C6
    ROcp39_56 = ROcp39_85*S6+C4*C6
    ROcp39_76 = ROcp39_75*C6+S4*S6
    ROcp39_86 = ROcp39_85*C6-C4*S6
    OMcp39_15 = -qd[5]*S4
    OMcp39_25 = qd[5]*C4
    OMcp39_16 = OMcp39_15+ROcp39_15*qd[6]
    OMcp39_26 = OMcp39_25+ROcp39_25*qd[6]
    OMcp39_36 = qd[4]-qd[6]*S5
    OPcp39_16 = ROcp39_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp39_25*S5+ROcp39_25*qd[4])
    OPcp39_26 = ROcp39_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp39_15*S5+ROcp39_15*qd[4])
    OPcp39_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_40_0_11 = = 
 
# Sensor Kinematics 


    ROcp39_432 = ROcp39_46*C32+ROcp39_76*S32
    ROcp39_532 = ROcp39_56*C32+ROcp39_86*S32
    ROcp39_632 = S32p6*C5
    ROcp39_732 = -(ROcp39_46*S32-ROcp39_76*C32)
    ROcp39_832 = -(ROcp39_56*S32-ROcp39_86*C32)
    ROcp39_932 = C32p6*C5
    ROcp39_133 = ROcp39_15*C33+ROcp39_432*S33
    ROcp39_233 = ROcp39_25*C33+ROcp39_532*S33
    ROcp39_333 = ROcp39_632*S33-C33*S5
    ROcp39_433 = -(ROcp39_15*S33-ROcp39_432*C33)
    ROcp39_533 = -(ROcp39_25*S33-ROcp39_532*C33)
    ROcp39_633 = ROcp39_632*C33+S33*S5
    ROcp39_434 = ROcp39_433*C34+ROcp39_732*S34
    ROcp39_534 = ROcp39_533*C34+ROcp39_832*S34
    ROcp39_634 = ROcp39_633*C34+ROcp39_932*S34
    ROcp39_734 = -(ROcp39_433*S34-ROcp39_732*C34)
    ROcp39_834 = -(ROcp39_533*S34-ROcp39_832*C34)
    ROcp39_934 = -(ROcp39_633*S34-ROcp39_932*C34)
    ROcp39_135 = ROcp39_133*C35-ROcp39_734*S35
    ROcp39_235 = ROcp39_233*C35-ROcp39_834*S35
    ROcp39_335 = ROcp39_333*C35-ROcp39_934*S35
    ROcp39_735 = ROcp39_133*S35+ROcp39_734*C35
    ROcp39_835 = ROcp39_233*S35+ROcp39_834*C35
    ROcp39_935 = ROcp39_333*S35+ROcp39_934*C35
    ROcp39_136 = ROcp39_135*C36+ROcp39_434*S36
    ROcp39_236 = ROcp39_235*C36+ROcp39_534*S36
    ROcp39_336 = ROcp39_335*C36+ROcp39_634*S36
    ROcp39_436 = -(ROcp39_135*S36-ROcp39_434*C36)
    ROcp39_536 = -(ROcp39_235*S36-ROcp39_534*C36)
    ROcp39_636 = -(ROcp39_335*S36-ROcp39_634*C36)
    RLcp39_132 = ROcp39_15*s.dpt[1,12]+ROcp39_46*s.dpt[2,12]
    RLcp39_232 = ROcp39_25*s.dpt[1,12]+ROcp39_56*s.dpt[2,12]
    RLcp39_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp39_132 = OMcp39_16+ROcp39_15*qd[32]
    OMcp39_232 = OMcp39_26+ROcp39_25*qd[32]
    OMcp39_332 = OMcp39_36-qd[32]*S5
    ORcp39_132 = OMcp39_26*RLcp39_332-OMcp39_36*RLcp39_232
    ORcp39_232 = -(OMcp39_16*RLcp39_332-OMcp39_36*RLcp39_132)
    ORcp39_332 = OMcp39_16*RLcp39_232-OMcp39_26*RLcp39_132
    OMcp39_133 = OMcp39_132+ROcp39_732*qd[33]
    OMcp39_233 = OMcp39_232+ROcp39_832*qd[33]
    OMcp39_333 = OMcp39_332+ROcp39_932*qd[33]
    OPcp39_133 = OPcp39_16+ROcp39_15*qdd[32]+ROcp39_732*qdd[33]-qd[32]*(OMcp39_26*S5+OMcp39_36*ROcp39_25)+qd[33]*(\
   OMcp39_232*ROcp39_932-OMcp39_332*ROcp39_832)
    OPcp39_233 = OPcp39_26+ROcp39_25*qdd[32]+ROcp39_832*qdd[33]+qd[32]*(OMcp39_16*S5+OMcp39_36*ROcp39_15)-qd[33]*(\
   OMcp39_132*ROcp39_932-OMcp39_332*ROcp39_732)
    OPcp39_333 = OPcp39_36+ROcp39_932*qdd[33]-qdd[32]*S5+qd[32]*(OMcp39_16*ROcp39_25-OMcp39_26*ROcp39_15)+qd[33]*(\
   OMcp39_132*ROcp39_832-OMcp39_232*ROcp39_732)
    RLcp39_134 = ROcp39_433*s.dpt[2,33]
    RLcp39_234 = ROcp39_533*s.dpt[2,33]
    RLcp39_334 = ROcp39_633*s.dpt[2,33]
    OMcp39_134 = OMcp39_133+ROcp39_133*qd[34]
    OMcp39_234 = OMcp39_233+ROcp39_233*qd[34]
    OMcp39_334 = OMcp39_333+ROcp39_333*qd[34]
    ORcp39_134 = OMcp39_233*RLcp39_334-OMcp39_333*RLcp39_234
    ORcp39_234 = -(OMcp39_133*RLcp39_334-OMcp39_333*RLcp39_134)
    ORcp39_334 = OMcp39_133*RLcp39_234-OMcp39_233*RLcp39_134
    OMcp39_135 = OMcp39_134+ROcp39_434*qd[35]
    OMcp39_235 = OMcp39_234+ROcp39_534*qd[35]
    OMcp39_335 = OMcp39_334+ROcp39_634*qd[35]
    OMcp39_136 = OMcp39_135+ROcp39_735*qd[36]
    OMcp39_236 = OMcp39_235+ROcp39_835*qd[36]
    OMcp39_336 = OMcp39_335+ROcp39_935*qd[36]
    OPcp39_136 = OPcp39_133+ROcp39_133*qdd[34]+ROcp39_434*qdd[35]+ROcp39_735*qdd[36]+qd[34]*(OMcp39_233*ROcp39_333-\
   OMcp39_333*ROcp39_233)+qd[35]*(OMcp39_234*ROcp39_634-OMcp39_334*ROcp39_534)+qd[36]*(OMcp39_235*ROcp39_935-OMcp39_335*\
   ROcp39_835)
    OPcp39_236 = OPcp39_233+ROcp39_233*qdd[34]+ROcp39_534*qdd[35]+ROcp39_835*qdd[36]-qd[34]*(OMcp39_133*ROcp39_333-\
   OMcp39_333*ROcp39_133)-qd[35]*(OMcp39_134*ROcp39_634-OMcp39_334*ROcp39_434)-qd[36]*(OMcp39_135*ROcp39_935-OMcp39_335*\
   ROcp39_735)
    OPcp39_336 = OPcp39_333+ROcp39_333*qdd[34]+ROcp39_634*qdd[35]+ROcp39_935*qdd[36]+qd[34]*(OMcp39_133*ROcp39_233-\
   OMcp39_233*ROcp39_133)+qd[35]*(OMcp39_134*ROcp39_534-OMcp39_234*ROcp39_434)+qd[36]*(OMcp39_135*ROcp39_835-OMcp39_235*\
   ROcp39_735)

# = = Block_1_0_0_40_0_13 = = 
 
# Sensor Kinematics 


    ROcp39_439 = ROcp39_436*C39+ROcp39_735*S39
    ROcp39_539 = ROcp39_536*C39+ROcp39_835*S39
    ROcp39_639 = ROcp39_636*C39+ROcp39_935*S39
    ROcp39_739 = -(ROcp39_436*S39-ROcp39_735*C39)
    ROcp39_839 = -(ROcp39_536*S39-ROcp39_835*C39)
    ROcp39_939 = -(ROcp39_636*S39-ROcp39_935*C39)
    ROcp39_140 = ROcp39_136*C40-ROcp39_739*S40
    ROcp39_240 = ROcp39_236*C40-ROcp39_839*S40
    ROcp39_340 = ROcp39_336*C40-ROcp39_939*S40
    ROcp39_740 = ROcp39_136*S40+ROcp39_739*C40
    ROcp39_840 = ROcp39_236*S40+ROcp39_839*C40
    ROcp39_940 = ROcp39_336*S40+ROcp39_939*C40
    RLcp39_139 = ROcp39_735*s.dpt[3,37]
    RLcp39_239 = ROcp39_835*s.dpt[3,37]
    RLcp39_339 = ROcp39_935*s.dpt[3,37]
    POcp39_139 = RLcp39_132+RLcp39_134+RLcp39_139+q[1]
    POcp39_239 = RLcp39_232+RLcp39_234+RLcp39_239+q[2]
    POcp39_339 = RLcp39_332+RLcp39_334+RLcp39_339+q[3]
    OMcp39_139 = OMcp39_136+ROcp39_136*qd[39]
    OMcp39_239 = OMcp39_236+ROcp39_236*qd[39]
    OMcp39_339 = OMcp39_336+ROcp39_336*qd[39]
    ORcp39_139 = OMcp39_236*RLcp39_339-OMcp39_336*RLcp39_239
    ORcp39_239 = -(OMcp39_136*RLcp39_339-OMcp39_336*RLcp39_139)
    ORcp39_339 = OMcp39_136*RLcp39_239-OMcp39_236*RLcp39_139
    VIcp39_139 = ORcp39_132+ORcp39_134+ORcp39_139+qd[1]
    VIcp39_239 = ORcp39_232+ORcp39_234+ORcp39_239+qd[2]
    VIcp39_339 = ORcp39_332+ORcp39_334+ORcp39_339+qd[3]
    ACcp39_139 = qdd[1]+OMcp39_233*ORcp39_334+OMcp39_236*ORcp39_339+OMcp39_26*ORcp39_332-OMcp39_333*ORcp39_234-OMcp39_336*\
   ORcp39_239-OMcp39_36*ORcp39_232+OPcp39_233*RLcp39_334+OPcp39_236*RLcp39_339+OPcp39_26*RLcp39_332-OPcp39_333*RLcp39_234-\
   OPcp39_336*RLcp39_239-OPcp39_36*RLcp39_232
    ACcp39_239 = qdd[2]-OMcp39_133*ORcp39_334-OMcp39_136*ORcp39_339-OMcp39_16*ORcp39_332+OMcp39_333*ORcp39_134+OMcp39_336*\
   ORcp39_139+OMcp39_36*ORcp39_132-OPcp39_133*RLcp39_334-OPcp39_136*RLcp39_339-OPcp39_16*RLcp39_332+OPcp39_333*RLcp39_134+\
   OPcp39_336*RLcp39_139+OPcp39_36*RLcp39_132
    ACcp39_339 = qdd[3]+OMcp39_133*ORcp39_234+OMcp39_136*ORcp39_239+OMcp39_16*ORcp39_232-OMcp39_233*ORcp39_134-OMcp39_236*\
   ORcp39_139-OMcp39_26*ORcp39_132+OPcp39_133*RLcp39_234+OPcp39_136*RLcp39_239+OPcp39_16*RLcp39_232-OPcp39_233*RLcp39_134-\
   OPcp39_236*RLcp39_139-OPcp39_26*RLcp39_132
    OMcp39_140 = OMcp39_139+ROcp39_439*qd[40]
    OMcp39_240 = OMcp39_239+ROcp39_539*qd[40]
    OMcp39_340 = OMcp39_339+ROcp39_639*qd[40]
    OPcp39_140 = OPcp39_136+ROcp39_136*qdd[39]+ROcp39_439*qdd[40]+qd[39]*(OMcp39_236*ROcp39_336-OMcp39_336*ROcp39_236)+\
   qd[40]*(OMcp39_239*ROcp39_639-OMcp39_339*ROcp39_539)
    OPcp39_240 = OPcp39_236+ROcp39_236*qdd[39]+ROcp39_539*qdd[40]-qd[39]*(OMcp39_136*ROcp39_336-OMcp39_336*ROcp39_136)-\
   qd[40]*(OMcp39_139*ROcp39_639-OMcp39_339*ROcp39_439)
    OPcp39_340 = OPcp39_336+ROcp39_336*qdd[39]+ROcp39_639*qdd[40]+qd[39]*(OMcp39_136*ROcp39_236-OMcp39_236*ROcp39_136)+\
   qd[40]*(OMcp39_139*ROcp39_539-OMcp39_239*ROcp39_439)

# = = Block_1_0_0_40_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp39_139
    sens.P[2] = POcp39_239
    sens.P[3] = POcp39_339
    sens.R[1,1] = ROcp39_140
    sens.R[1,2] = ROcp39_240
    sens.R[1,3] = ROcp39_340
    sens.R[2,1] = ROcp39_439
    sens.R[2,2] = ROcp39_539
    sens.R[2,3] = ROcp39_639
    sens.R[3,1] = ROcp39_740
    sens.R[3,2] = ROcp39_840
    sens.R[3,3] = ROcp39_940
    sens.V[1] = VIcp39_139
    sens.V[2] = VIcp39_239
    sens.V[3] = VIcp39_339
    sens.OM[1] = OMcp39_140
    sens.OM[2] = OMcp39_240
    sens.OM[3] = OMcp39_340
    sens.A[1] = ACcp39_139
    sens.A[2] = ACcp39_239
    sens.A[3] = ACcp39_339
    sens.OMP[1] = OPcp39_140
    sens.OMP[2] = OPcp39_240
    sens.OMP[3] = OPcp39_340
 
# 
  elif(isens==41): 


# = = Block_1_0_0_41_0_1 = = 
 
# Sensor Kinematics 


    ROcp40_15 = C4*C5
    ROcp40_25 = S4*C5
    ROcp40_75 = C4*S5
    ROcp40_85 = S4*S5
    ROcp40_46 = ROcp40_75*S6-S4*C6
    ROcp40_56 = ROcp40_85*S6+C4*C6
    ROcp40_66 = C5*S6
    ROcp40_76 = ROcp40_75*C6+S4*S6
    ROcp40_86 = ROcp40_85*C6-C4*S6
    ROcp40_96 = C5*C6
    OMcp40_15 = -qd[5]*S4
    OMcp40_25 = qd[5]*C4
    OMcp40_16 = OMcp40_15+ROcp40_15*qd[6]
    OMcp40_26 = OMcp40_25+ROcp40_25*qd[6]
    OMcp40_36 = qd[4]-qd[6]*S5
    OPcp40_16 = ROcp40_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp40_25*S5+ROcp40_25*qd[4])
    OPcp40_26 = ROcp40_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp40_15*S5+ROcp40_15*qd[4])
    OPcp40_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_41_0_14 = = 
 
# Sensor Kinematics 


    RLcp40_141 = ROcp40_15*s.dpt[1,13]+ROcp40_46*q[41]
    RLcp40_241 = ROcp40_25*s.dpt[1,13]+ROcp40_56*q[41]
    RLcp40_341 = ROcp40_66*q[41]-s.dpt[1,13]*S5
    POcp40_141 = RLcp40_141+q[1]
    POcp40_241 = RLcp40_241+q[2]
    POcp40_341 = RLcp40_341+q[3]
    ORcp40_141 = OMcp40_26*RLcp40_341-OMcp40_36*RLcp40_241
    ORcp40_241 = -(OMcp40_16*RLcp40_341-OMcp40_36*RLcp40_141)
    ORcp40_341 = OMcp40_16*RLcp40_241-OMcp40_26*RLcp40_141
    VIcp40_141 = ORcp40_141+qd[1]+ROcp40_46*qd[41]
    VIcp40_241 = ORcp40_241+qd[2]+ROcp40_56*qd[41]
    VIcp40_341 = ORcp40_341+qd[3]+ROcp40_66*qd[41]
    ACcp40_141 = qdd[1]+OMcp40_26*ORcp40_341-OMcp40_36*ORcp40_241+OPcp40_26*RLcp40_341-OPcp40_36*RLcp40_241+ROcp40_46*\
   qdd[41]+(2.0)*qd[41]*(OMcp40_26*ROcp40_66-OMcp40_36*ROcp40_56)
    ACcp40_241 = qdd[2]-OMcp40_16*ORcp40_341+OMcp40_36*ORcp40_141-OPcp40_16*RLcp40_341+OPcp40_36*RLcp40_141+ROcp40_56*\
   qdd[41]-(2.0)*qd[41]*(OMcp40_16*ROcp40_66-OMcp40_36*ROcp40_46)
    ACcp40_341 = qdd[3]+OMcp40_16*ORcp40_241-OMcp40_26*ORcp40_141+OPcp40_16*RLcp40_241-OPcp40_26*RLcp40_141+ROcp40_66*\
   qdd[41]+(2.0)*qd[41]*(OMcp40_16*ROcp40_56-OMcp40_26*ROcp40_46)

# = = Block_1_0_0_41_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp40_141
    sens.P[2] = POcp40_241
    sens.P[3] = POcp40_341
    sens.R[1,1] = ROcp40_15
    sens.R[1,2] = ROcp40_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp40_46
    sens.R[2,2] = ROcp40_56
    sens.R[2,3] = ROcp40_66
    sens.R[3,1] = ROcp40_76
    sens.R[3,2] = ROcp40_86
    sens.R[3,3] = ROcp40_96
    sens.V[1] = VIcp40_141
    sens.V[2] = VIcp40_241
    sens.V[3] = VIcp40_341
    sens.OM[1] = OMcp40_16
    sens.OM[2] = OMcp40_26
    sens.OM[3] = OMcp40_36
    sens.A[1] = ACcp40_141
    sens.A[2] = ACcp40_241
    sens.A[3] = ACcp40_341
    sens.OMP[1] = OPcp40_16
    sens.OMP[2] = OPcp40_26
    sens.OMP[3] = OPcp40_36



# ====== END Task 1 ====== 

  

