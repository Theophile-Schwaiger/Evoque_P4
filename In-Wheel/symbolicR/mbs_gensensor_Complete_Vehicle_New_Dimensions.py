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
#	==> Generation Date : Sat May  2 22:51:37 2020
#
#	==> Project name : Complete_Vehicle_New_Dimensions
#	==> using XML input file 
#
#	==> Number of joints : 65
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 18045
#
#	==> Generation Time :  0.290 seconds
#	==> Post-Processing :  0.390 seconds
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

# = = Block_0_0_0_0_0_9 = = 
 
# Trigonometric Variables  

  C25 = np.cos(q[25])
  S25 = np.sin(q[25])
  C26 = np.cos(q[26])
  S26 = np.sin(q[26])

# = = Block_0_0_0_0_0_10 = = 
 
# Trigonometric Variables  

  C27 = np.cos(q[27])
  S27 = np.sin(q[27])
  C28 = np.cos(q[28])
  S28 = np.sin(q[28])

# = = Block_0_0_0_0_0_11 = = 
 
# Trigonometric Variables  

  C29 = np.cos(q[29])
  S29 = np.sin(q[29])
  C30 = np.cos(q[30])
  S30 = np.sin(q[30])
  C31 = np.cos(q[31])
  S31 = np.sin(q[31])
  C32 = np.cos(q[32])
  S32 = np.sin(q[32])
  C33 = np.cos(q[33])
  S33 = np.sin(q[33])

# = = Block_0_0_0_0_0_12 = = 
 
# Trigonometric Variables  

  C34 = np.cos(q[34])
  S34 = np.sin(q[34])

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C36 = np.cos(q[36])
  S36 = np.sin(q[36])
  C37 = np.cos(q[37])
  S37 = np.sin(q[37])

# = = Block_0_0_0_0_0_14 = = 
 
# Trigonometric Variables  

  C38 = np.cos(q[38])
  S38 = np.sin(q[38])
  C39 = np.cos(q[39])
  S39 = np.sin(q[39])

# = = Block_0_0_0_0_0_15 = = 
 
# Trigonometric Variables  

  C40 = np.cos(q[40])
  S40 = np.sin(q[40])
  C41 = np.cos(q[41])
  S41 = np.sin(q[41])
  C42 = np.cos(q[42])
  S42 = np.sin(q[42])
  C43 = np.cos(q[43])
  S43 = np.sin(q[43])
  C44 = np.cos(q[44])
  S44 = np.sin(q[44])

# = = Block_0_0_0_0_0_16 = = 
 
# Trigonometric Variables  

  C45 = np.cos(q[45])
  S45 = np.sin(q[45])

# = = Block_0_0_0_0_0_17 = = 
 
# Trigonometric Variables  

  C47 = np.cos(q[47])
  S47 = np.sin(q[47])
  C48 = np.cos(q[48])
  S48 = np.sin(q[48])

# = = Block_0_0_0_0_0_19 = = 
 
# Trigonometric Variables  

  C50 = np.cos(q[50])
  S50 = np.sin(q[50])
  C51 = np.cos(q[51])
  S51 = np.sin(q[51])

# = = Block_0_0_0_0_0_20 = = 
 
# Trigonometric Variables  

  C52 = np.cos(q[52])
  S52 = np.sin(q[52])
  C53 = np.cos(q[53])
  S53 = np.sin(q[53])

# = = Block_0_0_0_0_0_21 = = 
 
# Trigonometric Variables  

  C54 = np.cos(q[54])
  S54 = np.sin(q[54])

# = = Block_0_0_0_0_0_22 = = 
 
# Trigonometric Variables  

  C55 = np.cos(q[55])
  S55 = np.sin(q[55])
  C56 = np.cos(q[56])
  S56 = np.sin(q[56])
  C57 = np.cos(q[57])
  S57 = np.sin(q[57])

# = = Block_0_0_0_0_0_23 = = 
 
# Trigonometric Variables  

  C58 = np.cos(q[58])
  S58 = np.sin(q[58])
  C59 = np.cos(q[59])
  S59 = np.sin(q[59])

# = = Block_0_0_0_0_0_24 = = 
 
# Trigonometric Variables  

  C60 = np.cos(q[60])
  S60 = np.sin(q[60])

# = = Block_0_0_0_0_0_25 = = 
 
# Trigonometric Variables  

  C61 = np.cos(q[61])
  S61 = np.sin(q[61])
  C62 = np.cos(q[62])
  S62 = np.sin(q[62])
  C63 = np.cos(q[63])
  S63 = np.sin(q[63])

# = = Block_0_0_0_0_0_26 = = 
 
# Trigonometric Variables  

  C64 = np.cos(q[64])
  S64 = np.sin(q[64])
  C65 = np.cos(q[65])
  S65 = np.sin(q[65])

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

# = = Block_0_0_0_25_0_9 = = 
 
# Trigonometric Variables  

  S25p6 = C25*S6+S25*C6
  C25p6 = C25*C6-S25*S6

# = = Block_0_0_0_27_0_10 = = 
 
# Trigonometric Variables  

  S27p6 = C27*S6+S27*C6
  C27p6 = C27*C6-S27*S6

# = = Block_0_0_0_29_0_11 = = 
 
# Trigonometric Variables  

  S29p6 = C29*S6+S29*C6
  C29p6 = C29*C6-S29*S6

# = = Block_0_0_0_38_0_14 = = 
 
# Trigonometric Variables  

  S38p6 = C38*S6+S38*C6
  C38p6 = C38*C6-S38*S6

# = = Block_0_0_0_40_0_15 = = 
 
# Trigonometric Variables  

  S40p6 = C40*S6+S40*C6
  C40p6 = C40*C6-S40*S6

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
    RLcp7_18 = ROcp7_47*s.dpt[2,16]
    RLcp7_28 = ROcp7_57*s.dpt[2,16]
    RLcp7_38 = ROcp7_67*s.dpt[2,16]
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
    RLcp8_18 = ROcp8_47*s.dpt[2,16]
    RLcp8_28 = ROcp8_57*s.dpt[2,16]
    RLcp8_38 = ROcp8_67*s.dpt[2,16]
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
    RLcp9_18 = ROcp9_47*s.dpt[2,16]
    RLcp9_28 = ROcp9_57*s.dpt[2,16]
    RLcp9_38 = ROcp9_67*s.dpt[2,16]
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
    RLcp10_18 = ROcp10_47*s.dpt[2,16]
    RLcp10_28 = ROcp10_57*s.dpt[2,16]
    RLcp10_38 = ROcp10_67*s.dpt[2,16]
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
    RLcp10_111 = ROcp10_49*s.dpt[2,17]+ROcp10_710*s.dpt[3,17]
    RLcp10_211 = ROcp10_59*s.dpt[2,17]+ROcp10_810*s.dpt[3,17]
    RLcp10_311 = ROcp10_69*s.dpt[2,17]+ROcp10_910*s.dpt[3,17]
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
    RLcp11_18 = ROcp11_47*s.dpt[2,16]
    RLcp11_28 = ROcp11_57*s.dpt[2,16]
    RLcp11_38 = ROcp11_67*s.dpt[2,16]
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
    RLcp11_111 = ROcp11_49*s.dpt[2,17]+ROcp11_710*s.dpt[3,17]
    RLcp11_211 = ROcp11_59*s.dpt[2,17]+ROcp11_810*s.dpt[3,17]
    RLcp11_311 = ROcp11_69*s.dpt[2,17]+ROcp11_910*s.dpt[3,17]
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
    RLcp12_18 = ROcp12_47*s.dpt[2,16]
    RLcp12_28 = ROcp12_57*s.dpt[2,16]
    RLcp12_38 = ROcp12_67*s.dpt[2,16]
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
    RLcp12_113 = ROcp12_49*s.dpt[2,18]+ROcp12_710*s.dpt[3,18]
    RLcp12_213 = ROcp12_59*s.dpt[2,18]+ROcp12_810*s.dpt[3,18]
    RLcp12_313 = ROcp12_69*s.dpt[2,18]+ROcp12_910*s.dpt[3,18]
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
    RLcp13_18 = ROcp13_47*s.dpt[2,16]
    RLcp13_28 = ROcp13_57*s.dpt[2,16]
    RLcp13_38 = ROcp13_67*s.dpt[2,16]
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
    RLcp13_113 = ROcp13_49*s.dpt[2,18]+ROcp13_710*s.dpt[3,18]
    RLcp13_213 = ROcp13_59*s.dpt[2,18]+ROcp13_810*s.dpt[3,18]
    RLcp13_313 = ROcp13_69*s.dpt[2,18]+ROcp13_910*s.dpt[3,18]
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
    RLcp15_116 = ROcp15_415*s.dpt[2,23]
    RLcp15_216 = ROcp15_515*s.dpt[2,23]
    RLcp15_316 = ROcp15_615*s.dpt[2,23]
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
    RLcp16_116 = ROcp16_415*s.dpt[2,23]
    RLcp16_216 = ROcp16_515*s.dpt[2,23]
    RLcp16_316 = ROcp16_615*s.dpt[2,23]
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
    RLcp17_116 = ROcp17_415*s.dpt[2,23]
    RLcp17_216 = ROcp17_515*s.dpt[2,23]
    RLcp17_316 = ROcp17_615*s.dpt[2,23]
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
    RLcp18_116 = ROcp18_415*s.dpt[2,23]
    RLcp18_216 = ROcp18_515*s.dpt[2,23]
    RLcp18_316 = ROcp18_615*s.dpt[2,23]
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
    RLcp18_119 = ROcp18_417*s.dpt[2,24]+ROcp18_718*s.dpt[3,24]
    RLcp18_219 = ROcp18_517*s.dpt[2,24]+ROcp18_818*s.dpt[3,24]
    RLcp18_319 = ROcp18_617*s.dpt[2,24]+ROcp18_918*s.dpt[3,24]
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
    RLcp19_116 = ROcp19_415*s.dpt[2,23]
    RLcp19_216 = ROcp19_515*s.dpt[2,23]
    RLcp19_316 = ROcp19_615*s.dpt[2,23]
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
    RLcp19_119 = ROcp19_417*s.dpt[2,24]+ROcp19_718*s.dpt[3,24]
    RLcp19_219 = ROcp19_517*s.dpt[2,24]+ROcp19_818*s.dpt[3,24]
    RLcp19_319 = ROcp19_617*s.dpt[2,24]+ROcp19_918*s.dpt[3,24]
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
    RLcp20_116 = ROcp20_415*s.dpt[2,23]
    RLcp20_216 = ROcp20_515*s.dpt[2,23]
    RLcp20_316 = ROcp20_615*s.dpt[2,23]
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
    RLcp20_121 = ROcp20_417*s.dpt[2,25]+ROcp20_718*s.dpt[3,25]
    RLcp20_221 = ROcp20_517*s.dpt[2,25]+ROcp20_818*s.dpt[3,25]
    RLcp20_321 = ROcp20_617*s.dpt[2,25]+ROcp20_918*s.dpt[3,25]
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
    RLcp21_116 = ROcp21_415*s.dpt[2,23]
    RLcp21_216 = ROcp21_515*s.dpt[2,23]
    RLcp21_316 = ROcp21_615*s.dpt[2,23]
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
    RLcp21_121 = ROcp21_417*s.dpt[2,25]+ROcp21_718*s.dpt[3,25]
    RLcp21_221 = ROcp21_517*s.dpt[2,25]+ROcp21_818*s.dpt[3,25]
    RLcp21_321 = ROcp21_617*s.dpt[2,25]+ROcp21_918*s.dpt[3,25]
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
    RLcp22_123 = ROcp22_15*s.dpt[1,6]+ROcp22_46*s.dpt[2,6]+ROcp22_76*s.dpt[3,6]
    RLcp22_223 = ROcp22_25*s.dpt[1,6]+ROcp22_56*s.dpt[2,6]+ROcp22_86*s.dpt[3,6]
    RLcp22_323 = C5*C6*s.dpt[3,6]-s.dpt[1,6]*S5+s.dpt[2,6]*C5*S6
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
    RLcp23_123 = ROcp23_15*s.dpt[1,6]+ROcp23_46*s.dpt[2,6]+ROcp23_76*s.dpt[3,6]
    RLcp23_223 = ROcp23_25*s.dpt[1,6]+ROcp23_56*s.dpt[2,6]+ROcp23_86*s.dpt[3,6]
    RLcp23_323 = C5*C6*s.dpt[3,6]-s.dpt[1,6]*S5+s.dpt[2,6]*C5*S6
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

# = = Block_1_0_0_25_0_9 = = 
 
# Sensor Kinematics 


    ROcp24_425 = ROcp24_46*C25+ROcp24_76*S25
    ROcp24_525 = ROcp24_56*C25+ROcp24_86*S25
    ROcp24_625 = S25p6*C5
    ROcp24_725 = -(ROcp24_46*S25-ROcp24_76*C25)
    ROcp24_825 = -(ROcp24_56*S25-ROcp24_86*C25)
    ROcp24_925 = C25p6*C5
    RLcp24_125 = ROcp24_15*s.dpt[1,8]+ROcp24_46*s.dpt[2,8]+ROcp24_76*s.dpt[3,8]
    RLcp24_225 = ROcp24_25*s.dpt[1,8]+ROcp24_56*s.dpt[2,8]+ROcp24_86*s.dpt[3,8]
    RLcp24_325 = C5*C6*s.dpt[3,8]-s.dpt[1,8]*S5+s.dpt[2,8]*C5*S6
    POcp24_125 = RLcp24_125+q[1]
    POcp24_225 = RLcp24_225+q[2]
    POcp24_325 = RLcp24_325+q[3]
    OMcp24_125 = OMcp24_16+ROcp24_15*qd[25]
    OMcp24_225 = OMcp24_26+ROcp24_25*qd[25]
    OMcp24_325 = OMcp24_36-qd[25]*S5
    ORcp24_125 = OMcp24_26*RLcp24_325-OMcp24_36*RLcp24_225
    ORcp24_225 = -(OMcp24_16*RLcp24_325-OMcp24_36*RLcp24_125)
    ORcp24_325 = OMcp24_16*RLcp24_225-OMcp24_26*RLcp24_125
    VIcp24_125 = ORcp24_125+qd[1]
    VIcp24_225 = ORcp24_225+qd[2]
    VIcp24_325 = ORcp24_325+qd[3]
    OPcp24_125 = OPcp24_16+ROcp24_15*qdd[25]-qd[25]*(OMcp24_26*S5+OMcp24_36*ROcp24_25)
    OPcp24_225 = OPcp24_26+ROcp24_25*qdd[25]+qd[25]*(OMcp24_16*S5+OMcp24_36*ROcp24_15)
    OPcp24_325 = OPcp24_36-qdd[25]*S5+qd[25]*(OMcp24_16*ROcp24_25-OMcp24_26*ROcp24_15)
    ACcp24_125 = qdd[1]+OMcp24_26*ORcp24_325-OMcp24_36*ORcp24_225+OPcp24_26*RLcp24_325-OPcp24_36*RLcp24_225
    ACcp24_225 = qdd[2]-OMcp24_16*ORcp24_325+OMcp24_36*ORcp24_125-OPcp24_16*RLcp24_325+OPcp24_36*RLcp24_125
    ACcp24_325 = qdd[3]+OMcp24_16*ORcp24_225-OMcp24_26*ORcp24_125+OPcp24_16*RLcp24_225-OPcp24_26*RLcp24_125

# = = Block_1_0_0_25_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp24_125
    sens.P[2] = POcp24_225
    sens.P[3] = POcp24_325
    sens.R[1,1] = ROcp24_15
    sens.R[1,2] = ROcp24_25
    sens.R[1,3] = -S5
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

# = = Block_1_0_0_26_0_9 = = 
 
# Sensor Kinematics 


    ROcp25_425 = ROcp25_46*C25+ROcp25_76*S25
    ROcp25_525 = ROcp25_56*C25+ROcp25_86*S25
    ROcp25_625 = S25p6*C5
    ROcp25_725 = -(ROcp25_46*S25-ROcp25_76*C25)
    ROcp25_825 = -(ROcp25_56*S25-ROcp25_86*C25)
    ROcp25_925 = C25p6*C5
    ROcp25_126 = ROcp25_15*C26+ROcp25_425*S26
    ROcp25_226 = ROcp25_25*C26+ROcp25_525*S26
    ROcp25_326 = ROcp25_625*S26-C26*S5
    ROcp25_426 = -(ROcp25_15*S26-ROcp25_425*C26)
    ROcp25_526 = -(ROcp25_25*S26-ROcp25_525*C26)
    ROcp25_626 = ROcp25_625*C26+S26*S5
    RLcp25_125 = ROcp25_15*s.dpt[1,8]+ROcp25_46*s.dpt[2,8]+ROcp25_76*s.dpt[3,8]
    RLcp25_225 = ROcp25_25*s.dpt[1,8]+ROcp25_56*s.dpt[2,8]+ROcp25_86*s.dpt[3,8]
    RLcp25_325 = C5*C6*s.dpt[3,8]-s.dpt[1,8]*S5+s.dpt[2,8]*C5*S6
    POcp25_125 = RLcp25_125+q[1]
    POcp25_225 = RLcp25_225+q[2]
    POcp25_325 = RLcp25_325+q[3]
    OMcp25_125 = OMcp25_16+ROcp25_15*qd[25]
    OMcp25_225 = OMcp25_26+ROcp25_25*qd[25]
    OMcp25_325 = OMcp25_36-qd[25]*S5
    ORcp25_125 = OMcp25_26*RLcp25_325-OMcp25_36*RLcp25_225
    ORcp25_225 = -(OMcp25_16*RLcp25_325-OMcp25_36*RLcp25_125)
    ORcp25_325 = OMcp25_16*RLcp25_225-OMcp25_26*RLcp25_125
    VIcp25_125 = ORcp25_125+qd[1]
    VIcp25_225 = ORcp25_225+qd[2]
    VIcp25_325 = ORcp25_325+qd[3]
    ACcp25_125 = qdd[1]+OMcp25_26*ORcp25_325-OMcp25_36*ORcp25_225+OPcp25_26*RLcp25_325-OPcp25_36*RLcp25_225
    ACcp25_225 = qdd[2]-OMcp25_16*ORcp25_325+OMcp25_36*ORcp25_125-OPcp25_16*RLcp25_325+OPcp25_36*RLcp25_125
    ACcp25_325 = qdd[3]+OMcp25_16*ORcp25_225-OMcp25_26*ORcp25_125+OPcp25_16*RLcp25_225-OPcp25_26*RLcp25_125
    OMcp25_126 = OMcp25_125+ROcp25_725*qd[26]
    OMcp25_226 = OMcp25_225+ROcp25_825*qd[26]
    OMcp25_326 = OMcp25_325+ROcp25_925*qd[26]
    OPcp25_126 = OPcp25_16+ROcp25_15*qdd[25]+ROcp25_725*qdd[26]-qd[25]*(OMcp25_26*S5+OMcp25_36*ROcp25_25)+qd[26]*(\
   OMcp25_225*ROcp25_925-OMcp25_325*ROcp25_825)
    OPcp25_226 = OPcp25_26+ROcp25_25*qdd[25]+ROcp25_825*qdd[26]+qd[25]*(OMcp25_16*S5+OMcp25_36*ROcp25_15)-qd[26]*(\
   OMcp25_125*ROcp25_925-OMcp25_325*ROcp25_725)
    OPcp25_326 = OPcp25_36+ROcp25_925*qdd[26]-qdd[25]*S5+qd[25]*(OMcp25_16*ROcp25_25-OMcp25_26*ROcp25_15)+qd[26]*(\
   OMcp25_125*ROcp25_825-OMcp25_225*ROcp25_725)

# = = Block_1_0_0_26_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp25_125
    sens.P[2] = POcp25_225
    sens.P[3] = POcp25_325
    sens.R[1,1] = ROcp25_126
    sens.R[1,2] = ROcp25_226
    sens.R[1,3] = ROcp25_326
    sens.R[2,1] = ROcp25_426
    sens.R[2,2] = ROcp25_526
    sens.R[2,3] = ROcp25_626
    sens.R[3,1] = ROcp25_725
    sens.R[3,2] = ROcp25_825
    sens.R[3,3] = ROcp25_925
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

# = = Block_1_0_0_27_0_10 = = 
 
# Sensor Kinematics 


    ROcp26_427 = ROcp26_46*C27+ROcp26_76*S27
    ROcp26_527 = ROcp26_56*C27+ROcp26_86*S27
    ROcp26_627 = S27p6*C5
    ROcp26_727 = -(ROcp26_46*S27-ROcp26_76*C27)
    ROcp26_827 = -(ROcp26_56*S27-ROcp26_86*C27)
    ROcp26_927 = C27p6*C5
    RLcp26_127 = ROcp26_15*s.dpt[1,9]+ROcp26_46*s.dpt[2,9]+ROcp26_76*s.dpt[3,9]
    RLcp26_227 = ROcp26_25*s.dpt[1,9]+ROcp26_56*s.dpt[2,9]+ROcp26_86*s.dpt[3,9]
    RLcp26_327 = C5*C6*s.dpt[3,9]-s.dpt[1,9]*S5+s.dpt[2,9]*C5*S6
    POcp26_127 = RLcp26_127+q[1]
    POcp26_227 = RLcp26_227+q[2]
    POcp26_327 = RLcp26_327+q[3]
    OMcp26_127 = OMcp26_16+ROcp26_15*qd[27]
    OMcp26_227 = OMcp26_26+ROcp26_25*qd[27]
    OMcp26_327 = OMcp26_36-qd[27]*S5
    ORcp26_127 = OMcp26_26*RLcp26_327-OMcp26_36*RLcp26_227
    ORcp26_227 = -(OMcp26_16*RLcp26_327-OMcp26_36*RLcp26_127)
    ORcp26_327 = OMcp26_16*RLcp26_227-OMcp26_26*RLcp26_127
    VIcp26_127 = ORcp26_127+qd[1]
    VIcp26_227 = ORcp26_227+qd[2]
    VIcp26_327 = ORcp26_327+qd[3]
    OPcp26_127 = OPcp26_16+ROcp26_15*qdd[27]-qd[27]*(OMcp26_26*S5+OMcp26_36*ROcp26_25)
    OPcp26_227 = OPcp26_26+ROcp26_25*qdd[27]+qd[27]*(OMcp26_16*S5+OMcp26_36*ROcp26_15)
    OPcp26_327 = OPcp26_36-qdd[27]*S5+qd[27]*(OMcp26_16*ROcp26_25-OMcp26_26*ROcp26_15)
    ACcp26_127 = qdd[1]+OMcp26_26*ORcp26_327-OMcp26_36*ORcp26_227+OPcp26_26*RLcp26_327-OPcp26_36*RLcp26_227
    ACcp26_227 = qdd[2]-OMcp26_16*ORcp26_327+OMcp26_36*ORcp26_127-OPcp26_16*RLcp26_327+OPcp26_36*RLcp26_127
    ACcp26_327 = qdd[3]+OMcp26_16*ORcp26_227-OMcp26_26*ORcp26_127+OPcp26_16*RLcp26_227-OPcp26_26*RLcp26_127

# = = Block_1_0_0_27_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp26_127
    sens.P[2] = POcp26_227
    sens.P[3] = POcp26_327
    sens.R[1,1] = ROcp26_15
    sens.R[1,2] = ROcp26_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp26_427
    sens.R[2,2] = ROcp26_527
    sens.R[2,3] = ROcp26_627
    sens.R[3,1] = ROcp26_727
    sens.R[3,2] = ROcp26_827
    sens.R[3,3] = ROcp26_927
    sens.V[1] = VIcp26_127
    sens.V[2] = VIcp26_227
    sens.V[3] = VIcp26_327
    sens.OM[1] = OMcp26_127
    sens.OM[2] = OMcp26_227
    sens.OM[3] = OMcp26_327
    sens.A[1] = ACcp26_127
    sens.A[2] = ACcp26_227
    sens.A[3] = ACcp26_327
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

# = = Block_1_0_0_28_0_10 = = 
 
# Sensor Kinematics 


    ROcp27_427 = ROcp27_46*C27+ROcp27_76*S27
    ROcp27_527 = ROcp27_56*C27+ROcp27_86*S27
    ROcp27_627 = S27p6*C5
    ROcp27_727 = -(ROcp27_46*S27-ROcp27_76*C27)
    ROcp27_827 = -(ROcp27_56*S27-ROcp27_86*C27)
    ROcp27_927 = C27p6*C5
    ROcp27_128 = ROcp27_15*C28+ROcp27_427*S28
    ROcp27_228 = ROcp27_25*C28+ROcp27_527*S28
    ROcp27_328 = ROcp27_627*S28-C28*S5
    ROcp27_428 = -(ROcp27_15*S28-ROcp27_427*C28)
    ROcp27_528 = -(ROcp27_25*S28-ROcp27_527*C28)
    ROcp27_628 = ROcp27_627*C28+S28*S5
    RLcp27_127 = ROcp27_15*s.dpt[1,9]+ROcp27_46*s.dpt[2,9]+ROcp27_76*s.dpt[3,9]
    RLcp27_227 = ROcp27_25*s.dpt[1,9]+ROcp27_56*s.dpt[2,9]+ROcp27_86*s.dpt[3,9]
    RLcp27_327 = C5*C6*s.dpt[3,9]-s.dpt[1,9]*S5+s.dpt[2,9]*C5*S6
    POcp27_127 = RLcp27_127+q[1]
    POcp27_227 = RLcp27_227+q[2]
    POcp27_327 = RLcp27_327+q[3]
    OMcp27_127 = OMcp27_16+ROcp27_15*qd[27]
    OMcp27_227 = OMcp27_26+ROcp27_25*qd[27]
    OMcp27_327 = OMcp27_36-qd[27]*S5
    ORcp27_127 = OMcp27_26*RLcp27_327-OMcp27_36*RLcp27_227
    ORcp27_227 = -(OMcp27_16*RLcp27_327-OMcp27_36*RLcp27_127)
    ORcp27_327 = OMcp27_16*RLcp27_227-OMcp27_26*RLcp27_127
    VIcp27_127 = ORcp27_127+qd[1]
    VIcp27_227 = ORcp27_227+qd[2]
    VIcp27_327 = ORcp27_327+qd[3]
    ACcp27_127 = qdd[1]+OMcp27_26*ORcp27_327-OMcp27_36*ORcp27_227+OPcp27_26*RLcp27_327-OPcp27_36*RLcp27_227
    ACcp27_227 = qdd[2]-OMcp27_16*ORcp27_327+OMcp27_36*ORcp27_127-OPcp27_16*RLcp27_327+OPcp27_36*RLcp27_127
    ACcp27_327 = qdd[3]+OMcp27_16*ORcp27_227-OMcp27_26*ORcp27_127+OPcp27_16*RLcp27_227-OPcp27_26*RLcp27_127
    OMcp27_128 = OMcp27_127+ROcp27_727*qd[28]
    OMcp27_228 = OMcp27_227+ROcp27_827*qd[28]
    OMcp27_328 = OMcp27_327+ROcp27_927*qd[28]
    OPcp27_128 = OPcp27_16+ROcp27_15*qdd[27]+ROcp27_727*qdd[28]-qd[27]*(OMcp27_26*S5+OMcp27_36*ROcp27_25)+qd[28]*(\
   OMcp27_227*ROcp27_927-OMcp27_327*ROcp27_827)
    OPcp27_228 = OPcp27_26+ROcp27_25*qdd[27]+ROcp27_827*qdd[28]+qd[27]*(OMcp27_16*S5+OMcp27_36*ROcp27_15)-qd[28]*(\
   OMcp27_127*ROcp27_927-OMcp27_327*ROcp27_727)
    OPcp27_328 = OPcp27_36+ROcp27_927*qdd[28]-qdd[27]*S5+qd[27]*(OMcp27_16*ROcp27_25-OMcp27_26*ROcp27_15)+qd[28]*(\
   OMcp27_127*ROcp27_827-OMcp27_227*ROcp27_727)

# = = Block_1_0_0_28_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp27_127
    sens.P[2] = POcp27_227
    sens.P[3] = POcp27_327
    sens.R[1,1] = ROcp27_128
    sens.R[1,2] = ROcp27_228
    sens.R[1,3] = ROcp27_328
    sens.R[2,1] = ROcp27_428
    sens.R[2,2] = ROcp27_528
    sens.R[2,3] = ROcp27_628
    sens.R[3,1] = ROcp27_727
    sens.R[3,2] = ROcp27_827
    sens.R[3,3] = ROcp27_927
    sens.V[1] = VIcp27_127
    sens.V[2] = VIcp27_227
    sens.V[3] = VIcp27_327
    sens.OM[1] = OMcp27_128
    sens.OM[2] = OMcp27_228
    sens.OM[3] = OMcp27_328
    sens.A[1] = ACcp27_127
    sens.A[2] = ACcp27_227
    sens.A[3] = ACcp27_327
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

# = = Block_1_0_0_29_0_11 = = 
 
# Sensor Kinematics 


    ROcp28_429 = ROcp28_46*C29+ROcp28_76*S29
    ROcp28_529 = ROcp28_56*C29+ROcp28_86*S29
    ROcp28_629 = S29p6*C5
    ROcp28_729 = -(ROcp28_46*S29-ROcp28_76*C29)
    ROcp28_829 = -(ROcp28_56*S29-ROcp28_86*C29)
    ROcp28_929 = C29p6*C5
    RLcp28_129 = ROcp28_15*s.dpt[1,10]+ROcp28_46*s.dpt[2,10]
    RLcp28_229 = ROcp28_25*s.dpt[1,10]+ROcp28_56*s.dpt[2,10]
    RLcp28_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    POcp28_129 = RLcp28_129+q[1]
    POcp28_229 = RLcp28_229+q[2]
    POcp28_329 = RLcp28_329+q[3]
    OMcp28_129 = OMcp28_16+ROcp28_15*qd[29]
    OMcp28_229 = OMcp28_26+ROcp28_25*qd[29]
    OMcp28_329 = OMcp28_36-qd[29]*S5
    ORcp28_129 = OMcp28_26*RLcp28_329-OMcp28_36*RLcp28_229
    ORcp28_229 = -(OMcp28_16*RLcp28_329-OMcp28_36*RLcp28_129)
    ORcp28_329 = OMcp28_16*RLcp28_229-OMcp28_26*RLcp28_129
    VIcp28_129 = ORcp28_129+qd[1]
    VIcp28_229 = ORcp28_229+qd[2]
    VIcp28_329 = ORcp28_329+qd[3]
    OPcp28_129 = OPcp28_16+ROcp28_15*qdd[29]-qd[29]*(OMcp28_26*S5+OMcp28_36*ROcp28_25)
    OPcp28_229 = OPcp28_26+ROcp28_25*qdd[29]+qd[29]*(OMcp28_16*S5+OMcp28_36*ROcp28_15)
    OPcp28_329 = OPcp28_36-qdd[29]*S5+qd[29]*(OMcp28_16*ROcp28_25-OMcp28_26*ROcp28_15)
    ACcp28_129 = qdd[1]+OMcp28_26*ORcp28_329-OMcp28_36*ORcp28_229+OPcp28_26*RLcp28_329-OPcp28_36*RLcp28_229
    ACcp28_229 = qdd[2]-OMcp28_16*ORcp28_329+OMcp28_36*ORcp28_129-OPcp28_16*RLcp28_329+OPcp28_36*RLcp28_129
    ACcp28_329 = qdd[3]+OMcp28_16*ORcp28_229-OMcp28_26*ORcp28_129+OPcp28_16*RLcp28_229-OPcp28_26*RLcp28_129

# = = Block_1_0_0_29_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp28_129
    sens.P[2] = POcp28_229
    sens.P[3] = POcp28_329
    sens.R[1,1] = ROcp28_15
    sens.R[1,2] = ROcp28_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp28_429
    sens.R[2,2] = ROcp28_529
    sens.R[2,3] = ROcp28_629
    sens.R[3,1] = ROcp28_729
    sens.R[3,2] = ROcp28_829
    sens.R[3,3] = ROcp28_929
    sens.V[1] = VIcp28_129
    sens.V[2] = VIcp28_229
    sens.V[3] = VIcp28_329
    sens.OM[1] = OMcp28_129
    sens.OM[2] = OMcp28_229
    sens.OM[3] = OMcp28_329
    sens.A[1] = ACcp28_129
    sens.A[2] = ACcp28_229
    sens.A[3] = ACcp28_329
    sens.OMP[1] = OPcp28_129
    sens.OMP[2] = OPcp28_229
    sens.OMP[3] = OPcp28_329
 
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

# = = Block_1_0_0_30_0_11 = = 
 
# Sensor Kinematics 


    ROcp29_429 = ROcp29_46*C29+ROcp29_76*S29
    ROcp29_529 = ROcp29_56*C29+ROcp29_86*S29
    ROcp29_629 = S29p6*C5
    ROcp29_729 = -(ROcp29_46*S29-ROcp29_76*C29)
    ROcp29_829 = -(ROcp29_56*S29-ROcp29_86*C29)
    ROcp29_929 = C29p6*C5
    ROcp29_130 = ROcp29_15*C30+ROcp29_429*S30
    ROcp29_230 = ROcp29_25*C30+ROcp29_529*S30
    ROcp29_330 = ROcp29_629*S30-C30*S5
    ROcp29_430 = -(ROcp29_15*S30-ROcp29_429*C30)
    ROcp29_530 = -(ROcp29_25*S30-ROcp29_529*C30)
    ROcp29_630 = ROcp29_629*C30+S30*S5
    RLcp29_129 = ROcp29_15*s.dpt[1,10]+ROcp29_46*s.dpt[2,10]
    RLcp29_229 = ROcp29_25*s.dpt[1,10]+ROcp29_56*s.dpt[2,10]
    RLcp29_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    POcp29_129 = RLcp29_129+q[1]
    POcp29_229 = RLcp29_229+q[2]
    POcp29_329 = RLcp29_329+q[3]
    OMcp29_129 = OMcp29_16+ROcp29_15*qd[29]
    OMcp29_229 = OMcp29_26+ROcp29_25*qd[29]
    OMcp29_329 = OMcp29_36-qd[29]*S5
    ORcp29_129 = OMcp29_26*RLcp29_329-OMcp29_36*RLcp29_229
    ORcp29_229 = -(OMcp29_16*RLcp29_329-OMcp29_36*RLcp29_129)
    ORcp29_329 = OMcp29_16*RLcp29_229-OMcp29_26*RLcp29_129
    VIcp29_129 = ORcp29_129+qd[1]
    VIcp29_229 = ORcp29_229+qd[2]
    VIcp29_329 = ORcp29_329+qd[3]
    ACcp29_129 = qdd[1]+OMcp29_26*ORcp29_329-OMcp29_36*ORcp29_229+OPcp29_26*RLcp29_329-OPcp29_36*RLcp29_229
    ACcp29_229 = qdd[2]-OMcp29_16*ORcp29_329+OMcp29_36*ORcp29_129-OPcp29_16*RLcp29_329+OPcp29_36*RLcp29_129
    ACcp29_329 = qdd[3]+OMcp29_16*ORcp29_229-OMcp29_26*ORcp29_129+OPcp29_16*RLcp29_229-OPcp29_26*RLcp29_129
    OMcp29_130 = OMcp29_129+ROcp29_729*qd[30]
    OMcp29_230 = OMcp29_229+ROcp29_829*qd[30]
    OMcp29_330 = OMcp29_329+ROcp29_929*qd[30]
    OPcp29_130 = OPcp29_16+ROcp29_15*qdd[29]+ROcp29_729*qdd[30]-qd[29]*(OMcp29_26*S5+OMcp29_36*ROcp29_25)+qd[30]*(\
   OMcp29_229*ROcp29_929-OMcp29_329*ROcp29_829)
    OPcp29_230 = OPcp29_26+ROcp29_25*qdd[29]+ROcp29_829*qdd[30]+qd[29]*(OMcp29_16*S5+OMcp29_36*ROcp29_15)-qd[30]*(\
   OMcp29_129*ROcp29_929-OMcp29_329*ROcp29_729)
    OPcp29_330 = OPcp29_36+ROcp29_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp29_16*ROcp29_25-OMcp29_26*ROcp29_15)+qd[30]*(\
   OMcp29_129*ROcp29_829-OMcp29_229*ROcp29_729)

# = = Block_1_0_0_30_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp29_129
    sens.P[2] = POcp29_229
    sens.P[3] = POcp29_329
    sens.R[1,1] = ROcp29_130
    sens.R[1,2] = ROcp29_230
    sens.R[1,3] = ROcp29_330
    sens.R[2,1] = ROcp29_430
    sens.R[2,2] = ROcp29_530
    sens.R[2,3] = ROcp29_630
    sens.R[3,1] = ROcp29_729
    sens.R[3,2] = ROcp29_829
    sens.R[3,3] = ROcp29_929
    sens.V[1] = VIcp29_129
    sens.V[2] = VIcp29_229
    sens.V[3] = VIcp29_329
    sens.OM[1] = OMcp29_130
    sens.OM[2] = OMcp29_230
    sens.OM[3] = OMcp29_330
    sens.A[1] = ACcp29_129
    sens.A[2] = ACcp29_229
    sens.A[3] = ACcp29_329
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

# = = Block_1_0_0_31_0_11 = = 
 
# Sensor Kinematics 


    ROcp30_429 = ROcp30_46*C29+ROcp30_76*S29
    ROcp30_529 = ROcp30_56*C29+ROcp30_86*S29
    ROcp30_629 = S29p6*C5
    ROcp30_729 = -(ROcp30_46*S29-ROcp30_76*C29)
    ROcp30_829 = -(ROcp30_56*S29-ROcp30_86*C29)
    ROcp30_929 = C29p6*C5
    ROcp30_130 = ROcp30_15*C30+ROcp30_429*S30
    ROcp30_230 = ROcp30_25*C30+ROcp30_529*S30
    ROcp30_330 = ROcp30_629*S30-C30*S5
    ROcp30_430 = -(ROcp30_15*S30-ROcp30_429*C30)
    ROcp30_530 = -(ROcp30_25*S30-ROcp30_529*C30)
    ROcp30_630 = ROcp30_629*C30+S30*S5
    ROcp30_431 = ROcp30_430*C31+ROcp30_729*S31
    ROcp30_531 = ROcp30_530*C31+ROcp30_829*S31
    ROcp30_631 = ROcp30_630*C31+ROcp30_929*S31
    ROcp30_731 = -(ROcp30_430*S31-ROcp30_729*C31)
    ROcp30_831 = -(ROcp30_530*S31-ROcp30_829*C31)
    ROcp30_931 = -(ROcp30_630*S31-ROcp30_929*C31)
    RLcp30_129 = ROcp30_15*s.dpt[1,10]+ROcp30_46*s.dpt[2,10]
    RLcp30_229 = ROcp30_25*s.dpt[1,10]+ROcp30_56*s.dpt[2,10]
    RLcp30_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp30_129 = OMcp30_16+ROcp30_15*qd[29]
    OMcp30_229 = OMcp30_26+ROcp30_25*qd[29]
    OMcp30_329 = OMcp30_36-qd[29]*S5
    ORcp30_129 = OMcp30_26*RLcp30_329-OMcp30_36*RLcp30_229
    ORcp30_229 = -(OMcp30_16*RLcp30_329-OMcp30_36*RLcp30_129)
    ORcp30_329 = OMcp30_16*RLcp30_229-OMcp30_26*RLcp30_129
    OMcp30_130 = OMcp30_129+ROcp30_729*qd[30]
    OMcp30_230 = OMcp30_229+ROcp30_829*qd[30]
    OMcp30_330 = OMcp30_329+ROcp30_929*qd[30]
    OPcp30_130 = OPcp30_16+ROcp30_15*qdd[29]+ROcp30_729*qdd[30]-qd[29]*(OMcp30_26*S5+OMcp30_36*ROcp30_25)+qd[30]*(\
   OMcp30_229*ROcp30_929-OMcp30_329*ROcp30_829)
    OPcp30_230 = OPcp30_26+ROcp30_25*qdd[29]+ROcp30_829*qdd[30]+qd[29]*(OMcp30_16*S5+OMcp30_36*ROcp30_15)-qd[30]*(\
   OMcp30_129*ROcp30_929-OMcp30_329*ROcp30_729)
    OPcp30_330 = OPcp30_36+ROcp30_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp30_16*ROcp30_25-OMcp30_26*ROcp30_15)+qd[30]*(\
   OMcp30_129*ROcp30_829-OMcp30_229*ROcp30_729)
    RLcp30_131 = ROcp30_430*s.dpt[2,33]
    RLcp30_231 = ROcp30_530*s.dpt[2,33]
    RLcp30_331 = ROcp30_630*s.dpt[2,33]
    POcp30_131 = RLcp30_129+RLcp30_131+q[1]
    POcp30_231 = RLcp30_229+RLcp30_231+q[2]
    POcp30_331 = RLcp30_329+RLcp30_331+q[3]
    OMcp30_131 = OMcp30_130+ROcp30_130*qd[31]
    OMcp30_231 = OMcp30_230+ROcp30_230*qd[31]
    OMcp30_331 = OMcp30_330+ROcp30_330*qd[31]
    ORcp30_131 = OMcp30_230*RLcp30_331-OMcp30_330*RLcp30_231
    ORcp30_231 = -(OMcp30_130*RLcp30_331-OMcp30_330*RLcp30_131)
    ORcp30_331 = OMcp30_130*RLcp30_231-OMcp30_230*RLcp30_131
    VIcp30_131 = ORcp30_129+ORcp30_131+qd[1]
    VIcp30_231 = ORcp30_229+ORcp30_231+qd[2]
    VIcp30_331 = ORcp30_329+ORcp30_331+qd[3]
    OPcp30_131 = OPcp30_130+ROcp30_130*qdd[31]+qd[31]*(OMcp30_230*ROcp30_330-OMcp30_330*ROcp30_230)
    OPcp30_231 = OPcp30_230+ROcp30_230*qdd[31]-qd[31]*(OMcp30_130*ROcp30_330-OMcp30_330*ROcp30_130)
    OPcp30_331 = OPcp30_330+ROcp30_330*qdd[31]+qd[31]*(OMcp30_130*ROcp30_230-OMcp30_230*ROcp30_130)
    ACcp30_131 = qdd[1]+OMcp30_230*ORcp30_331+OMcp30_26*ORcp30_329-OMcp30_330*ORcp30_231-OMcp30_36*ORcp30_229+OPcp30_230*\
   RLcp30_331+OPcp30_26*RLcp30_329-OPcp30_330*RLcp30_231-OPcp30_36*RLcp30_229
    ACcp30_231 = qdd[2]-OMcp30_130*ORcp30_331-OMcp30_16*ORcp30_329+OMcp30_330*ORcp30_131+OMcp30_36*ORcp30_129-OPcp30_130*\
   RLcp30_331-OPcp30_16*RLcp30_329+OPcp30_330*RLcp30_131+OPcp30_36*RLcp30_129
    ACcp30_331 = qdd[3]+OMcp30_130*ORcp30_231+OMcp30_16*ORcp30_229-OMcp30_230*ORcp30_131-OMcp30_26*ORcp30_129+OPcp30_130*\
   RLcp30_231+OPcp30_16*RLcp30_229-OPcp30_230*RLcp30_131-OPcp30_26*RLcp30_129

# = = Block_1_0_0_31_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp30_131
    sens.P[2] = POcp30_231
    sens.P[3] = POcp30_331
    sens.R[1,1] = ROcp30_130
    sens.R[1,2] = ROcp30_230
    sens.R[1,3] = ROcp30_330
    sens.R[2,1] = ROcp30_431
    sens.R[2,2] = ROcp30_531
    sens.R[2,3] = ROcp30_631
    sens.R[3,1] = ROcp30_731
    sens.R[3,2] = ROcp30_831
    sens.R[3,3] = ROcp30_931
    sens.V[1] = VIcp30_131
    sens.V[2] = VIcp30_231
    sens.V[3] = VIcp30_331
    sens.OM[1] = OMcp30_131
    sens.OM[2] = OMcp30_231
    sens.OM[3] = OMcp30_331
    sens.A[1] = ACcp30_131
    sens.A[2] = ACcp30_231
    sens.A[3] = ACcp30_331
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


    ROcp31_429 = ROcp31_46*C29+ROcp31_76*S29
    ROcp31_529 = ROcp31_56*C29+ROcp31_86*S29
    ROcp31_629 = S29p6*C5
    ROcp31_729 = -(ROcp31_46*S29-ROcp31_76*C29)
    ROcp31_829 = -(ROcp31_56*S29-ROcp31_86*C29)
    ROcp31_929 = C29p6*C5
    ROcp31_130 = ROcp31_15*C30+ROcp31_429*S30
    ROcp31_230 = ROcp31_25*C30+ROcp31_529*S30
    ROcp31_330 = ROcp31_629*S30-C30*S5
    ROcp31_430 = -(ROcp31_15*S30-ROcp31_429*C30)
    ROcp31_530 = -(ROcp31_25*S30-ROcp31_529*C30)
    ROcp31_630 = ROcp31_629*C30+S30*S5
    ROcp31_431 = ROcp31_430*C31+ROcp31_729*S31
    ROcp31_531 = ROcp31_530*C31+ROcp31_829*S31
    ROcp31_631 = ROcp31_630*C31+ROcp31_929*S31
    ROcp31_731 = -(ROcp31_430*S31-ROcp31_729*C31)
    ROcp31_831 = -(ROcp31_530*S31-ROcp31_829*C31)
    ROcp31_931 = -(ROcp31_630*S31-ROcp31_929*C31)
    ROcp31_132 = ROcp31_130*C32-ROcp31_731*S32
    ROcp31_232 = ROcp31_230*C32-ROcp31_831*S32
    ROcp31_332 = ROcp31_330*C32-ROcp31_931*S32
    ROcp31_732 = ROcp31_130*S32+ROcp31_731*C32
    ROcp31_832 = ROcp31_230*S32+ROcp31_831*C32
    ROcp31_932 = ROcp31_330*S32+ROcp31_931*C32
    RLcp31_129 = ROcp31_15*s.dpt[1,10]+ROcp31_46*s.dpt[2,10]
    RLcp31_229 = ROcp31_25*s.dpt[1,10]+ROcp31_56*s.dpt[2,10]
    RLcp31_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp31_129 = OMcp31_16+ROcp31_15*qd[29]
    OMcp31_229 = OMcp31_26+ROcp31_25*qd[29]
    OMcp31_329 = OMcp31_36-qd[29]*S5
    ORcp31_129 = OMcp31_26*RLcp31_329-OMcp31_36*RLcp31_229
    ORcp31_229 = -(OMcp31_16*RLcp31_329-OMcp31_36*RLcp31_129)
    ORcp31_329 = OMcp31_16*RLcp31_229-OMcp31_26*RLcp31_129
    OMcp31_130 = OMcp31_129+ROcp31_729*qd[30]
    OMcp31_230 = OMcp31_229+ROcp31_829*qd[30]
    OMcp31_330 = OMcp31_329+ROcp31_929*qd[30]
    OPcp31_130 = OPcp31_16+ROcp31_15*qdd[29]+ROcp31_729*qdd[30]-qd[29]*(OMcp31_26*S5+OMcp31_36*ROcp31_25)+qd[30]*(\
   OMcp31_229*ROcp31_929-OMcp31_329*ROcp31_829)
    OPcp31_230 = OPcp31_26+ROcp31_25*qdd[29]+ROcp31_829*qdd[30]+qd[29]*(OMcp31_16*S5+OMcp31_36*ROcp31_15)-qd[30]*(\
   OMcp31_129*ROcp31_929-OMcp31_329*ROcp31_729)
    OPcp31_330 = OPcp31_36+ROcp31_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp31_16*ROcp31_25-OMcp31_26*ROcp31_15)+qd[30]*(\
   OMcp31_129*ROcp31_829-OMcp31_229*ROcp31_729)
    RLcp31_131 = ROcp31_430*s.dpt[2,33]
    RLcp31_231 = ROcp31_530*s.dpt[2,33]
    RLcp31_331 = ROcp31_630*s.dpt[2,33]
    POcp31_131 = RLcp31_129+RLcp31_131+q[1]
    POcp31_231 = RLcp31_229+RLcp31_231+q[2]
    POcp31_331 = RLcp31_329+RLcp31_331+q[3]
    OMcp31_131 = OMcp31_130+ROcp31_130*qd[31]
    OMcp31_231 = OMcp31_230+ROcp31_230*qd[31]
    OMcp31_331 = OMcp31_330+ROcp31_330*qd[31]
    ORcp31_131 = OMcp31_230*RLcp31_331-OMcp31_330*RLcp31_231
    ORcp31_231 = -(OMcp31_130*RLcp31_331-OMcp31_330*RLcp31_131)
    ORcp31_331 = OMcp31_130*RLcp31_231-OMcp31_230*RLcp31_131
    VIcp31_131 = ORcp31_129+ORcp31_131+qd[1]
    VIcp31_231 = ORcp31_229+ORcp31_231+qd[2]
    VIcp31_331 = ORcp31_329+ORcp31_331+qd[3]
    ACcp31_131 = qdd[1]+OMcp31_230*ORcp31_331+OMcp31_26*ORcp31_329-OMcp31_330*ORcp31_231-OMcp31_36*ORcp31_229+OPcp31_230*\
   RLcp31_331+OPcp31_26*RLcp31_329-OPcp31_330*RLcp31_231-OPcp31_36*RLcp31_229
    ACcp31_231 = qdd[2]-OMcp31_130*ORcp31_331-OMcp31_16*ORcp31_329+OMcp31_330*ORcp31_131+OMcp31_36*ORcp31_129-OPcp31_130*\
   RLcp31_331-OPcp31_16*RLcp31_329+OPcp31_330*RLcp31_131+OPcp31_36*RLcp31_129
    ACcp31_331 = qdd[3]+OMcp31_130*ORcp31_231+OMcp31_16*ORcp31_229-OMcp31_230*ORcp31_131-OMcp31_26*ORcp31_129+OPcp31_130*\
   RLcp31_231+OPcp31_16*RLcp31_229-OPcp31_230*RLcp31_131-OPcp31_26*RLcp31_129
    OMcp31_132 = OMcp31_131+ROcp31_431*qd[32]
    OMcp31_232 = OMcp31_231+ROcp31_531*qd[32]
    OMcp31_332 = OMcp31_331+ROcp31_631*qd[32]
    OPcp31_132 = OPcp31_130+ROcp31_130*qdd[31]+ROcp31_431*qdd[32]+qd[31]*(OMcp31_230*ROcp31_330-OMcp31_330*ROcp31_230)+\
   qd[32]*(OMcp31_231*ROcp31_631-OMcp31_331*ROcp31_531)
    OPcp31_232 = OPcp31_230+ROcp31_230*qdd[31]+ROcp31_531*qdd[32]-qd[31]*(OMcp31_130*ROcp31_330-OMcp31_330*ROcp31_130)-\
   qd[32]*(OMcp31_131*ROcp31_631-OMcp31_331*ROcp31_431)
    OPcp31_332 = OPcp31_330+ROcp31_330*qdd[31]+ROcp31_631*qdd[32]+qd[31]*(OMcp31_130*ROcp31_230-OMcp31_230*ROcp31_130)+\
   qd[32]*(OMcp31_131*ROcp31_531-OMcp31_231*ROcp31_431)

# = = Block_1_0_0_32_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp31_131
    sens.P[2] = POcp31_231
    sens.P[3] = POcp31_331
    sens.R[1,1] = ROcp31_132
    sens.R[1,2] = ROcp31_232
    sens.R[1,3] = ROcp31_332
    sens.R[2,1] = ROcp31_431
    sens.R[2,2] = ROcp31_531
    sens.R[2,3] = ROcp31_631
    sens.R[3,1] = ROcp31_732
    sens.R[3,2] = ROcp31_832
    sens.R[3,3] = ROcp31_932
    sens.V[1] = VIcp31_131
    sens.V[2] = VIcp31_231
    sens.V[3] = VIcp31_331
    sens.OM[1] = OMcp31_132
    sens.OM[2] = OMcp31_232
    sens.OM[3] = OMcp31_332
    sens.A[1] = ACcp31_131
    sens.A[2] = ACcp31_231
    sens.A[3] = ACcp31_331
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


    ROcp32_429 = ROcp32_46*C29+ROcp32_76*S29
    ROcp32_529 = ROcp32_56*C29+ROcp32_86*S29
    ROcp32_629 = S29p6*C5
    ROcp32_729 = -(ROcp32_46*S29-ROcp32_76*C29)
    ROcp32_829 = -(ROcp32_56*S29-ROcp32_86*C29)
    ROcp32_929 = C29p6*C5
    ROcp32_130 = ROcp32_15*C30+ROcp32_429*S30
    ROcp32_230 = ROcp32_25*C30+ROcp32_529*S30
    ROcp32_330 = ROcp32_629*S30-C30*S5
    ROcp32_430 = -(ROcp32_15*S30-ROcp32_429*C30)
    ROcp32_530 = -(ROcp32_25*S30-ROcp32_529*C30)
    ROcp32_630 = ROcp32_629*C30+S30*S5
    ROcp32_431 = ROcp32_430*C31+ROcp32_729*S31
    ROcp32_531 = ROcp32_530*C31+ROcp32_829*S31
    ROcp32_631 = ROcp32_630*C31+ROcp32_929*S31
    ROcp32_731 = -(ROcp32_430*S31-ROcp32_729*C31)
    ROcp32_831 = -(ROcp32_530*S31-ROcp32_829*C31)
    ROcp32_931 = -(ROcp32_630*S31-ROcp32_929*C31)
    ROcp32_132 = ROcp32_130*C32-ROcp32_731*S32
    ROcp32_232 = ROcp32_230*C32-ROcp32_831*S32
    ROcp32_332 = ROcp32_330*C32-ROcp32_931*S32
    ROcp32_732 = ROcp32_130*S32+ROcp32_731*C32
    ROcp32_832 = ROcp32_230*S32+ROcp32_831*C32
    ROcp32_932 = ROcp32_330*S32+ROcp32_931*C32
    ROcp32_133 = ROcp32_132*C33+ROcp32_431*S33
    ROcp32_233 = ROcp32_232*C33+ROcp32_531*S33
    ROcp32_333 = ROcp32_332*C33+ROcp32_631*S33
    ROcp32_433 = -(ROcp32_132*S33-ROcp32_431*C33)
    ROcp32_533 = -(ROcp32_232*S33-ROcp32_531*C33)
    ROcp32_633 = -(ROcp32_332*S33-ROcp32_631*C33)
    RLcp32_129 = ROcp32_15*s.dpt[1,10]+ROcp32_46*s.dpt[2,10]
    RLcp32_229 = ROcp32_25*s.dpt[1,10]+ROcp32_56*s.dpt[2,10]
    RLcp32_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp32_129 = OMcp32_16+ROcp32_15*qd[29]
    OMcp32_229 = OMcp32_26+ROcp32_25*qd[29]
    OMcp32_329 = OMcp32_36-qd[29]*S5
    ORcp32_129 = OMcp32_26*RLcp32_329-OMcp32_36*RLcp32_229
    ORcp32_229 = -(OMcp32_16*RLcp32_329-OMcp32_36*RLcp32_129)
    ORcp32_329 = OMcp32_16*RLcp32_229-OMcp32_26*RLcp32_129
    OMcp32_130 = OMcp32_129+ROcp32_729*qd[30]
    OMcp32_230 = OMcp32_229+ROcp32_829*qd[30]
    OMcp32_330 = OMcp32_329+ROcp32_929*qd[30]
    OPcp32_130 = OPcp32_16+ROcp32_15*qdd[29]+ROcp32_729*qdd[30]-qd[29]*(OMcp32_26*S5+OMcp32_36*ROcp32_25)+qd[30]*(\
   OMcp32_229*ROcp32_929-OMcp32_329*ROcp32_829)
    OPcp32_230 = OPcp32_26+ROcp32_25*qdd[29]+ROcp32_829*qdd[30]+qd[29]*(OMcp32_16*S5+OMcp32_36*ROcp32_15)-qd[30]*(\
   OMcp32_129*ROcp32_929-OMcp32_329*ROcp32_729)
    OPcp32_330 = OPcp32_36+ROcp32_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp32_16*ROcp32_25-OMcp32_26*ROcp32_15)+qd[30]*(\
   OMcp32_129*ROcp32_829-OMcp32_229*ROcp32_729)
    RLcp32_131 = ROcp32_430*s.dpt[2,33]
    RLcp32_231 = ROcp32_530*s.dpt[2,33]
    RLcp32_331 = ROcp32_630*s.dpt[2,33]
    POcp32_131 = RLcp32_129+RLcp32_131+q[1]
    POcp32_231 = RLcp32_229+RLcp32_231+q[2]
    POcp32_331 = RLcp32_329+RLcp32_331+q[3]
    OMcp32_131 = OMcp32_130+ROcp32_130*qd[31]
    OMcp32_231 = OMcp32_230+ROcp32_230*qd[31]
    OMcp32_331 = OMcp32_330+ROcp32_330*qd[31]
    ORcp32_131 = OMcp32_230*RLcp32_331-OMcp32_330*RLcp32_231
    ORcp32_231 = -(OMcp32_130*RLcp32_331-OMcp32_330*RLcp32_131)
    ORcp32_331 = OMcp32_130*RLcp32_231-OMcp32_230*RLcp32_131
    VIcp32_131 = ORcp32_129+ORcp32_131+qd[1]
    VIcp32_231 = ORcp32_229+ORcp32_231+qd[2]
    VIcp32_331 = ORcp32_329+ORcp32_331+qd[3]
    ACcp32_131 = qdd[1]+OMcp32_230*ORcp32_331+OMcp32_26*ORcp32_329-OMcp32_330*ORcp32_231-OMcp32_36*ORcp32_229+OPcp32_230*\
   RLcp32_331+OPcp32_26*RLcp32_329-OPcp32_330*RLcp32_231-OPcp32_36*RLcp32_229
    ACcp32_231 = qdd[2]-OMcp32_130*ORcp32_331-OMcp32_16*ORcp32_329+OMcp32_330*ORcp32_131+OMcp32_36*ORcp32_129-OPcp32_130*\
   RLcp32_331-OPcp32_16*RLcp32_329+OPcp32_330*RLcp32_131+OPcp32_36*RLcp32_129
    ACcp32_331 = qdd[3]+OMcp32_130*ORcp32_231+OMcp32_16*ORcp32_229-OMcp32_230*ORcp32_131-OMcp32_26*ORcp32_129+OPcp32_130*\
   RLcp32_231+OPcp32_16*RLcp32_229-OPcp32_230*RLcp32_131-OPcp32_26*RLcp32_129
    OMcp32_132 = OMcp32_131+ROcp32_431*qd[32]
    OMcp32_232 = OMcp32_231+ROcp32_531*qd[32]
    OMcp32_332 = OMcp32_331+ROcp32_631*qd[32]
    OMcp32_133 = OMcp32_132+ROcp32_732*qd[33]
    OMcp32_233 = OMcp32_232+ROcp32_832*qd[33]
    OMcp32_333 = OMcp32_332+ROcp32_932*qd[33]
    OPcp32_133 = OPcp32_130+ROcp32_130*qdd[31]+ROcp32_431*qdd[32]+ROcp32_732*qdd[33]+qd[31]*(OMcp32_230*ROcp32_330-\
   OMcp32_330*ROcp32_230)+qd[32]*(OMcp32_231*ROcp32_631-OMcp32_331*ROcp32_531)+qd[33]*(OMcp32_232*ROcp32_932-OMcp32_332*\
   ROcp32_832)
    OPcp32_233 = OPcp32_230+ROcp32_230*qdd[31]+ROcp32_531*qdd[32]+ROcp32_832*qdd[33]-qd[31]*(OMcp32_130*ROcp32_330-\
   OMcp32_330*ROcp32_130)-qd[32]*(OMcp32_131*ROcp32_631-OMcp32_331*ROcp32_431)-qd[33]*(OMcp32_132*ROcp32_932-OMcp32_332*\
   ROcp32_732)
    OPcp32_333 = OPcp32_330+ROcp32_330*qdd[31]+ROcp32_631*qdd[32]+ROcp32_932*qdd[33]+qd[31]*(OMcp32_130*ROcp32_230-\
   OMcp32_230*ROcp32_130)+qd[32]*(OMcp32_131*ROcp32_531-OMcp32_231*ROcp32_431)+qd[33]*(OMcp32_132*ROcp32_832-OMcp32_232*\
   ROcp32_732)

# = = Block_1_0_0_33_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp32_131
    sens.P[2] = POcp32_231
    sens.P[3] = POcp32_331
    sens.R[1,1] = ROcp32_133
    sens.R[1,2] = ROcp32_233
    sens.R[1,3] = ROcp32_333
    sens.R[2,1] = ROcp32_433
    sens.R[2,2] = ROcp32_533
    sens.R[2,3] = ROcp32_633
    sens.R[3,1] = ROcp32_732
    sens.R[3,2] = ROcp32_832
    sens.R[3,3] = ROcp32_932
    sens.V[1] = VIcp32_131
    sens.V[2] = VIcp32_231
    sens.V[3] = VIcp32_331
    sens.OM[1] = OMcp32_133
    sens.OM[2] = OMcp32_233
    sens.OM[3] = OMcp32_333
    sens.A[1] = ACcp32_131
    sens.A[2] = ACcp32_231
    sens.A[3] = ACcp32_331
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


    ROcp33_429 = ROcp33_46*C29+ROcp33_76*S29
    ROcp33_529 = ROcp33_56*C29+ROcp33_86*S29
    ROcp33_629 = S29p6*C5
    ROcp33_729 = -(ROcp33_46*S29-ROcp33_76*C29)
    ROcp33_829 = -(ROcp33_56*S29-ROcp33_86*C29)
    ROcp33_929 = C29p6*C5
    ROcp33_130 = ROcp33_15*C30+ROcp33_429*S30
    ROcp33_230 = ROcp33_25*C30+ROcp33_529*S30
    ROcp33_330 = ROcp33_629*S30-C30*S5
    ROcp33_430 = -(ROcp33_15*S30-ROcp33_429*C30)
    ROcp33_530 = -(ROcp33_25*S30-ROcp33_529*C30)
    ROcp33_630 = ROcp33_629*C30+S30*S5
    ROcp33_431 = ROcp33_430*C31+ROcp33_729*S31
    ROcp33_531 = ROcp33_530*C31+ROcp33_829*S31
    ROcp33_631 = ROcp33_630*C31+ROcp33_929*S31
    ROcp33_731 = -(ROcp33_430*S31-ROcp33_729*C31)
    ROcp33_831 = -(ROcp33_530*S31-ROcp33_829*C31)
    ROcp33_931 = -(ROcp33_630*S31-ROcp33_929*C31)
    ROcp33_132 = ROcp33_130*C32-ROcp33_731*S32
    ROcp33_232 = ROcp33_230*C32-ROcp33_831*S32
    ROcp33_332 = ROcp33_330*C32-ROcp33_931*S32
    ROcp33_732 = ROcp33_130*S32+ROcp33_731*C32
    ROcp33_832 = ROcp33_230*S32+ROcp33_831*C32
    ROcp33_932 = ROcp33_330*S32+ROcp33_931*C32
    ROcp33_133 = ROcp33_132*C33+ROcp33_431*S33
    ROcp33_233 = ROcp33_232*C33+ROcp33_531*S33
    ROcp33_333 = ROcp33_332*C33+ROcp33_631*S33
    ROcp33_433 = -(ROcp33_132*S33-ROcp33_431*C33)
    ROcp33_533 = -(ROcp33_232*S33-ROcp33_531*C33)
    ROcp33_633 = -(ROcp33_332*S33-ROcp33_631*C33)
    RLcp33_129 = ROcp33_15*s.dpt[1,10]+ROcp33_46*s.dpt[2,10]
    RLcp33_229 = ROcp33_25*s.dpt[1,10]+ROcp33_56*s.dpt[2,10]
    RLcp33_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp33_129 = OMcp33_16+ROcp33_15*qd[29]
    OMcp33_229 = OMcp33_26+ROcp33_25*qd[29]
    OMcp33_329 = OMcp33_36-qd[29]*S5
    ORcp33_129 = OMcp33_26*RLcp33_329-OMcp33_36*RLcp33_229
    ORcp33_229 = -(OMcp33_16*RLcp33_329-OMcp33_36*RLcp33_129)
    ORcp33_329 = OMcp33_16*RLcp33_229-OMcp33_26*RLcp33_129
    OMcp33_130 = OMcp33_129+ROcp33_729*qd[30]
    OMcp33_230 = OMcp33_229+ROcp33_829*qd[30]
    OMcp33_330 = OMcp33_329+ROcp33_929*qd[30]
    OPcp33_130 = OPcp33_16+ROcp33_15*qdd[29]+ROcp33_729*qdd[30]-qd[29]*(OMcp33_26*S5+OMcp33_36*ROcp33_25)+qd[30]*(\
   OMcp33_229*ROcp33_929-OMcp33_329*ROcp33_829)
    OPcp33_230 = OPcp33_26+ROcp33_25*qdd[29]+ROcp33_829*qdd[30]+qd[29]*(OMcp33_16*S5+OMcp33_36*ROcp33_15)-qd[30]*(\
   OMcp33_129*ROcp33_929-OMcp33_329*ROcp33_729)
    OPcp33_330 = OPcp33_36+ROcp33_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp33_16*ROcp33_25-OMcp33_26*ROcp33_15)+qd[30]*(\
   OMcp33_129*ROcp33_829-OMcp33_229*ROcp33_729)
    RLcp33_131 = ROcp33_430*s.dpt[2,33]
    RLcp33_231 = ROcp33_530*s.dpt[2,33]
    RLcp33_331 = ROcp33_630*s.dpt[2,33]
    OMcp33_131 = OMcp33_130+ROcp33_130*qd[31]
    OMcp33_231 = OMcp33_230+ROcp33_230*qd[31]
    OMcp33_331 = OMcp33_330+ROcp33_330*qd[31]
    ORcp33_131 = OMcp33_230*RLcp33_331-OMcp33_330*RLcp33_231
    ORcp33_231 = -(OMcp33_130*RLcp33_331-OMcp33_330*RLcp33_131)
    ORcp33_331 = OMcp33_130*RLcp33_231-OMcp33_230*RLcp33_131
    OMcp33_132 = OMcp33_131+ROcp33_431*qd[32]
    OMcp33_232 = OMcp33_231+ROcp33_531*qd[32]
    OMcp33_332 = OMcp33_331+ROcp33_631*qd[32]
    OMcp33_133 = OMcp33_132+ROcp33_732*qd[33]
    OMcp33_233 = OMcp33_232+ROcp33_832*qd[33]
    OMcp33_333 = OMcp33_332+ROcp33_932*qd[33]
    OPcp33_133 = OPcp33_130+ROcp33_130*qdd[31]+ROcp33_431*qdd[32]+ROcp33_732*qdd[33]+qd[31]*(OMcp33_230*ROcp33_330-\
   OMcp33_330*ROcp33_230)+qd[32]*(OMcp33_231*ROcp33_631-OMcp33_331*ROcp33_531)+qd[33]*(OMcp33_232*ROcp33_932-OMcp33_332*\
   ROcp33_832)
    OPcp33_233 = OPcp33_230+ROcp33_230*qdd[31]+ROcp33_531*qdd[32]+ROcp33_832*qdd[33]-qd[31]*(OMcp33_130*ROcp33_330-\
   OMcp33_330*ROcp33_130)-qd[32]*(OMcp33_131*ROcp33_631-OMcp33_331*ROcp33_431)-qd[33]*(OMcp33_132*ROcp33_932-OMcp33_332*\
   ROcp33_732)
    OPcp33_333 = OPcp33_330+ROcp33_330*qdd[31]+ROcp33_631*qdd[32]+ROcp33_932*qdd[33]+qd[31]*(OMcp33_130*ROcp33_230-\
   OMcp33_230*ROcp33_130)+qd[32]*(OMcp33_131*ROcp33_531-OMcp33_231*ROcp33_431)+qd[33]*(OMcp33_132*ROcp33_832-OMcp33_232*\
   ROcp33_732)

# = = Block_1_0_0_34_0_12 = = 
 
# Sensor Kinematics 


    ROcp33_434 = ROcp33_433*C34+ROcp33_732*S34
    ROcp33_534 = ROcp33_533*C34+ROcp33_832*S34
    ROcp33_634 = ROcp33_633*C34+ROcp33_932*S34
    ROcp33_734 = -(ROcp33_433*S34-ROcp33_732*C34)
    ROcp33_834 = -(ROcp33_533*S34-ROcp33_832*C34)
    ROcp33_934 = -(ROcp33_633*S34-ROcp33_932*C34)
    RLcp33_134 = ROcp33_433*s.dpt[2,34]+ROcp33_732*s.dpt[3,34]
    RLcp33_234 = ROcp33_533*s.dpt[2,34]+ROcp33_832*s.dpt[3,34]
    RLcp33_334 = ROcp33_633*s.dpt[2,34]+ROcp33_932*s.dpt[3,34]
    POcp33_134 = RLcp33_129+RLcp33_131+RLcp33_134+q[1]
    POcp33_234 = RLcp33_229+RLcp33_231+RLcp33_234+q[2]
    POcp33_334 = RLcp33_329+RLcp33_331+RLcp33_334+q[3]
    OMcp33_134 = OMcp33_133+ROcp33_133*qd[34]
    OMcp33_234 = OMcp33_233+ROcp33_233*qd[34]
    OMcp33_334 = OMcp33_333+ROcp33_333*qd[34]
    ORcp33_134 = OMcp33_233*RLcp33_334-OMcp33_333*RLcp33_234
    ORcp33_234 = -(OMcp33_133*RLcp33_334-OMcp33_333*RLcp33_134)
    ORcp33_334 = OMcp33_133*RLcp33_234-OMcp33_233*RLcp33_134
    VIcp33_134 = ORcp33_129+ORcp33_131+ORcp33_134+qd[1]
    VIcp33_234 = ORcp33_229+ORcp33_231+ORcp33_234+qd[2]
    VIcp33_334 = ORcp33_329+ORcp33_331+ORcp33_334+qd[3]
    OPcp33_134 = OPcp33_133+ROcp33_133*qdd[34]+qd[34]*(OMcp33_233*ROcp33_333-OMcp33_333*ROcp33_233)
    OPcp33_234 = OPcp33_233+ROcp33_233*qdd[34]-qd[34]*(OMcp33_133*ROcp33_333-OMcp33_333*ROcp33_133)
    OPcp33_334 = OPcp33_333+ROcp33_333*qdd[34]+qd[34]*(OMcp33_133*ROcp33_233-OMcp33_233*ROcp33_133)
    ACcp33_134 = qdd[1]+OMcp33_230*ORcp33_331+OMcp33_233*ORcp33_334+OMcp33_26*ORcp33_329-OMcp33_330*ORcp33_231-OMcp33_333*\
   ORcp33_234-OMcp33_36*ORcp33_229+OPcp33_230*RLcp33_331+OPcp33_233*RLcp33_334+OPcp33_26*RLcp33_329-OPcp33_330*RLcp33_231-\
   OPcp33_333*RLcp33_234-OPcp33_36*RLcp33_229
    ACcp33_234 = qdd[2]-OMcp33_130*ORcp33_331-OMcp33_133*ORcp33_334-OMcp33_16*ORcp33_329+OMcp33_330*ORcp33_131+OMcp33_333*\
   ORcp33_134+OMcp33_36*ORcp33_129-OPcp33_130*RLcp33_331-OPcp33_133*RLcp33_334-OPcp33_16*RLcp33_329+OPcp33_330*RLcp33_131+\
   OPcp33_333*RLcp33_134+OPcp33_36*RLcp33_129
    ACcp33_334 = qdd[3]+OMcp33_130*ORcp33_231+OMcp33_133*ORcp33_234+OMcp33_16*ORcp33_229-OMcp33_230*ORcp33_131-OMcp33_233*\
   ORcp33_134-OMcp33_26*ORcp33_129+OPcp33_130*RLcp33_231+OPcp33_133*RLcp33_234+OPcp33_16*RLcp33_229-OPcp33_230*RLcp33_131-\
   OPcp33_233*RLcp33_134-OPcp33_26*RLcp33_129

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


    ROcp34_429 = ROcp34_46*C29+ROcp34_76*S29
    ROcp34_529 = ROcp34_56*C29+ROcp34_86*S29
    ROcp34_629 = S29p6*C5
    ROcp34_729 = -(ROcp34_46*S29-ROcp34_76*C29)
    ROcp34_829 = -(ROcp34_56*S29-ROcp34_86*C29)
    ROcp34_929 = C29p6*C5
    ROcp34_130 = ROcp34_15*C30+ROcp34_429*S30
    ROcp34_230 = ROcp34_25*C30+ROcp34_529*S30
    ROcp34_330 = ROcp34_629*S30-C30*S5
    ROcp34_430 = -(ROcp34_15*S30-ROcp34_429*C30)
    ROcp34_530 = -(ROcp34_25*S30-ROcp34_529*C30)
    ROcp34_630 = ROcp34_629*C30+S30*S5
    ROcp34_431 = ROcp34_430*C31+ROcp34_729*S31
    ROcp34_531 = ROcp34_530*C31+ROcp34_829*S31
    ROcp34_631 = ROcp34_630*C31+ROcp34_929*S31
    ROcp34_731 = -(ROcp34_430*S31-ROcp34_729*C31)
    ROcp34_831 = -(ROcp34_530*S31-ROcp34_829*C31)
    ROcp34_931 = -(ROcp34_630*S31-ROcp34_929*C31)
    ROcp34_132 = ROcp34_130*C32-ROcp34_731*S32
    ROcp34_232 = ROcp34_230*C32-ROcp34_831*S32
    ROcp34_332 = ROcp34_330*C32-ROcp34_931*S32
    ROcp34_732 = ROcp34_130*S32+ROcp34_731*C32
    ROcp34_832 = ROcp34_230*S32+ROcp34_831*C32
    ROcp34_932 = ROcp34_330*S32+ROcp34_931*C32
    ROcp34_133 = ROcp34_132*C33+ROcp34_431*S33
    ROcp34_233 = ROcp34_232*C33+ROcp34_531*S33
    ROcp34_333 = ROcp34_332*C33+ROcp34_631*S33
    ROcp34_433 = -(ROcp34_132*S33-ROcp34_431*C33)
    ROcp34_533 = -(ROcp34_232*S33-ROcp34_531*C33)
    ROcp34_633 = -(ROcp34_332*S33-ROcp34_631*C33)
    RLcp34_129 = ROcp34_15*s.dpt[1,10]+ROcp34_46*s.dpt[2,10]
    RLcp34_229 = ROcp34_25*s.dpt[1,10]+ROcp34_56*s.dpt[2,10]
    RLcp34_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp34_129 = OMcp34_16+ROcp34_15*qd[29]
    OMcp34_229 = OMcp34_26+ROcp34_25*qd[29]
    OMcp34_329 = OMcp34_36-qd[29]*S5
    ORcp34_129 = OMcp34_26*RLcp34_329-OMcp34_36*RLcp34_229
    ORcp34_229 = -(OMcp34_16*RLcp34_329-OMcp34_36*RLcp34_129)
    ORcp34_329 = OMcp34_16*RLcp34_229-OMcp34_26*RLcp34_129
    OMcp34_130 = OMcp34_129+ROcp34_729*qd[30]
    OMcp34_230 = OMcp34_229+ROcp34_829*qd[30]
    OMcp34_330 = OMcp34_329+ROcp34_929*qd[30]
    OPcp34_130 = OPcp34_16+ROcp34_15*qdd[29]+ROcp34_729*qdd[30]-qd[29]*(OMcp34_26*S5+OMcp34_36*ROcp34_25)+qd[30]*(\
   OMcp34_229*ROcp34_929-OMcp34_329*ROcp34_829)
    OPcp34_230 = OPcp34_26+ROcp34_25*qdd[29]+ROcp34_829*qdd[30]+qd[29]*(OMcp34_16*S5+OMcp34_36*ROcp34_15)-qd[30]*(\
   OMcp34_129*ROcp34_929-OMcp34_329*ROcp34_729)
    OPcp34_330 = OPcp34_36+ROcp34_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp34_16*ROcp34_25-OMcp34_26*ROcp34_15)+qd[30]*(\
   OMcp34_129*ROcp34_829-OMcp34_229*ROcp34_729)
    RLcp34_131 = ROcp34_430*s.dpt[2,33]
    RLcp34_231 = ROcp34_530*s.dpt[2,33]
    RLcp34_331 = ROcp34_630*s.dpt[2,33]
    OMcp34_131 = OMcp34_130+ROcp34_130*qd[31]
    OMcp34_231 = OMcp34_230+ROcp34_230*qd[31]
    OMcp34_331 = OMcp34_330+ROcp34_330*qd[31]
    ORcp34_131 = OMcp34_230*RLcp34_331-OMcp34_330*RLcp34_231
    ORcp34_231 = -(OMcp34_130*RLcp34_331-OMcp34_330*RLcp34_131)
    ORcp34_331 = OMcp34_130*RLcp34_231-OMcp34_230*RLcp34_131
    OMcp34_132 = OMcp34_131+ROcp34_431*qd[32]
    OMcp34_232 = OMcp34_231+ROcp34_531*qd[32]
    OMcp34_332 = OMcp34_331+ROcp34_631*qd[32]
    OMcp34_133 = OMcp34_132+ROcp34_732*qd[33]
    OMcp34_233 = OMcp34_232+ROcp34_832*qd[33]
    OMcp34_333 = OMcp34_332+ROcp34_932*qd[33]
    OPcp34_133 = OPcp34_130+ROcp34_130*qdd[31]+ROcp34_431*qdd[32]+ROcp34_732*qdd[33]+qd[31]*(OMcp34_230*ROcp34_330-\
   OMcp34_330*ROcp34_230)+qd[32]*(OMcp34_231*ROcp34_631-OMcp34_331*ROcp34_531)+qd[33]*(OMcp34_232*ROcp34_932-OMcp34_332*\
   ROcp34_832)
    OPcp34_233 = OPcp34_230+ROcp34_230*qdd[31]+ROcp34_531*qdd[32]+ROcp34_832*qdd[33]-qd[31]*(OMcp34_130*ROcp34_330-\
   OMcp34_330*ROcp34_130)-qd[32]*(OMcp34_131*ROcp34_631-OMcp34_331*ROcp34_431)-qd[33]*(OMcp34_132*ROcp34_932-OMcp34_332*\
   ROcp34_732)
    OPcp34_333 = OPcp34_330+ROcp34_330*qdd[31]+ROcp34_631*qdd[32]+ROcp34_932*qdd[33]+qd[31]*(OMcp34_130*ROcp34_230-\
   OMcp34_230*ROcp34_130)+qd[32]*(OMcp34_131*ROcp34_531-OMcp34_231*ROcp34_431)+qd[33]*(OMcp34_132*ROcp34_832-OMcp34_232*\
   ROcp34_732)

# = = Block_1_0_0_35_0_12 = = 
 
# Sensor Kinematics 


    ROcp34_434 = ROcp34_433*C34+ROcp34_732*S34
    ROcp34_534 = ROcp34_533*C34+ROcp34_832*S34
    ROcp34_634 = ROcp34_633*C34+ROcp34_932*S34
    ROcp34_734 = -(ROcp34_433*S34-ROcp34_732*C34)
    ROcp34_834 = -(ROcp34_533*S34-ROcp34_832*C34)
    ROcp34_934 = -(ROcp34_633*S34-ROcp34_932*C34)
    RLcp34_134 = ROcp34_433*s.dpt[2,34]+ROcp34_732*s.dpt[3,34]
    RLcp34_234 = ROcp34_533*s.dpt[2,34]+ROcp34_832*s.dpt[3,34]
    RLcp34_334 = ROcp34_633*s.dpt[2,34]+ROcp34_932*s.dpt[3,34]
    OMcp34_134 = OMcp34_133+ROcp34_133*qd[34]
    OMcp34_234 = OMcp34_233+ROcp34_233*qd[34]
    OMcp34_334 = OMcp34_333+ROcp34_333*qd[34]
    ORcp34_134 = OMcp34_233*RLcp34_334-OMcp34_333*RLcp34_234
    ORcp34_234 = -(OMcp34_133*RLcp34_334-OMcp34_333*RLcp34_134)
    ORcp34_334 = OMcp34_133*RLcp34_234-OMcp34_233*RLcp34_134
    OPcp34_134 = OPcp34_133+ROcp34_133*qdd[34]+qd[34]*(OMcp34_233*ROcp34_333-OMcp34_333*ROcp34_233)
    OPcp34_234 = OPcp34_233+ROcp34_233*qdd[34]-qd[34]*(OMcp34_133*ROcp34_333-OMcp34_333*ROcp34_133)
    OPcp34_334 = OPcp34_333+ROcp34_333*qdd[34]+qd[34]*(OMcp34_133*ROcp34_233-OMcp34_233*ROcp34_133)
    RLcp34_135 = ROcp34_734*q[35]
    RLcp34_235 = ROcp34_834*q[35]
    RLcp34_335 = ROcp34_934*q[35]
    POcp34_135 = RLcp34_129+RLcp34_131+RLcp34_134+RLcp34_135+q[1]
    POcp34_235 = RLcp34_229+RLcp34_231+RLcp34_234+RLcp34_235+q[2]
    POcp34_335 = RLcp34_329+RLcp34_331+RLcp34_334+RLcp34_335+q[3]
    ORcp34_135 = OMcp34_234*RLcp34_335-OMcp34_334*RLcp34_235
    ORcp34_235 = -(OMcp34_134*RLcp34_335-OMcp34_334*RLcp34_135)
    ORcp34_335 = OMcp34_134*RLcp34_235-OMcp34_234*RLcp34_135
    VIcp34_135 = ORcp34_129+ORcp34_131+ORcp34_134+ORcp34_135+qd[1]+ROcp34_734*qd[35]
    VIcp34_235 = ORcp34_229+ORcp34_231+ORcp34_234+ORcp34_235+qd[2]+ROcp34_834*qd[35]
    VIcp34_335 = ORcp34_329+ORcp34_331+ORcp34_334+ORcp34_335+qd[3]+ROcp34_934*qd[35]
    ACcp34_135 = qdd[1]+OMcp34_230*ORcp34_331+OMcp34_233*ORcp34_334+OMcp34_234*ORcp34_335+OMcp34_26*ORcp34_329-OMcp34_330*\
   ORcp34_231-OMcp34_333*ORcp34_234-OMcp34_334*ORcp34_235-OMcp34_36*ORcp34_229+OPcp34_230*RLcp34_331+OPcp34_233*RLcp34_334+\
   OPcp34_234*RLcp34_335+OPcp34_26*RLcp34_329-OPcp34_330*RLcp34_231-OPcp34_333*RLcp34_234-OPcp34_334*RLcp34_235-OPcp34_36*\
   RLcp34_229+ROcp34_734*qdd[35]+(2.0)*qd[35]*(OMcp34_234*ROcp34_934-OMcp34_334*ROcp34_834)
    ACcp34_235 = qdd[2]-OMcp34_130*ORcp34_331-OMcp34_133*ORcp34_334-OMcp34_134*ORcp34_335-OMcp34_16*ORcp34_329+OMcp34_330*\
   ORcp34_131+OMcp34_333*ORcp34_134+OMcp34_334*ORcp34_135+OMcp34_36*ORcp34_129-OPcp34_130*RLcp34_331-OPcp34_133*RLcp34_334-\
   OPcp34_134*RLcp34_335-OPcp34_16*RLcp34_329+OPcp34_330*RLcp34_131+OPcp34_333*RLcp34_134+OPcp34_334*RLcp34_135+OPcp34_36*\
   RLcp34_129+ROcp34_834*qdd[35]-(2.0)*qd[35]*(OMcp34_134*ROcp34_934-OMcp34_334*ROcp34_734)
    ACcp34_335 = qdd[3]+OMcp34_130*ORcp34_231+OMcp34_133*ORcp34_234+OMcp34_134*ORcp34_235+OMcp34_16*ORcp34_229-OMcp34_230*\
   ORcp34_131-OMcp34_233*ORcp34_134-OMcp34_234*ORcp34_135-OMcp34_26*ORcp34_129+OPcp34_130*RLcp34_231+OPcp34_133*RLcp34_234+\
   OPcp34_134*RLcp34_235+OPcp34_16*RLcp34_229-OPcp34_230*RLcp34_131-OPcp34_233*RLcp34_134-OPcp34_234*RLcp34_135-OPcp34_26*\
   RLcp34_129+ROcp34_934*qdd[35]+(2.0)*qd[35]*(OMcp34_134*ROcp34_834-OMcp34_234*ROcp34_734)

# = = Block_1_0_0_35_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp34_135
    sens.P[2] = POcp34_235
    sens.P[3] = POcp34_335
    sens.R[1,1] = ROcp34_133
    sens.R[1,2] = ROcp34_233
    sens.R[1,3] = ROcp34_333
    sens.R[2,1] = ROcp34_434
    sens.R[2,2] = ROcp34_534
    sens.R[2,3] = ROcp34_634
    sens.R[3,1] = ROcp34_734
    sens.R[3,2] = ROcp34_834
    sens.R[3,3] = ROcp34_934
    sens.V[1] = VIcp34_135
    sens.V[2] = VIcp34_235
    sens.V[3] = VIcp34_335
    sens.OM[1] = OMcp34_134
    sens.OM[2] = OMcp34_234
    sens.OM[3] = OMcp34_334
    sens.A[1] = ACcp34_135
    sens.A[2] = ACcp34_235
    sens.A[3] = ACcp34_335
    sens.OMP[1] = OPcp34_134
    sens.OMP[2] = OPcp34_234
    sens.OMP[3] = OPcp34_334
 
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


    ROcp35_429 = ROcp35_46*C29+ROcp35_76*S29
    ROcp35_529 = ROcp35_56*C29+ROcp35_86*S29
    ROcp35_629 = S29p6*C5
    ROcp35_729 = -(ROcp35_46*S29-ROcp35_76*C29)
    ROcp35_829 = -(ROcp35_56*S29-ROcp35_86*C29)
    ROcp35_929 = C29p6*C5
    ROcp35_130 = ROcp35_15*C30+ROcp35_429*S30
    ROcp35_230 = ROcp35_25*C30+ROcp35_529*S30
    ROcp35_330 = ROcp35_629*S30-C30*S5
    ROcp35_430 = -(ROcp35_15*S30-ROcp35_429*C30)
    ROcp35_530 = -(ROcp35_25*S30-ROcp35_529*C30)
    ROcp35_630 = ROcp35_629*C30+S30*S5
    ROcp35_431 = ROcp35_430*C31+ROcp35_729*S31
    ROcp35_531 = ROcp35_530*C31+ROcp35_829*S31
    ROcp35_631 = ROcp35_630*C31+ROcp35_929*S31
    ROcp35_731 = -(ROcp35_430*S31-ROcp35_729*C31)
    ROcp35_831 = -(ROcp35_530*S31-ROcp35_829*C31)
    ROcp35_931 = -(ROcp35_630*S31-ROcp35_929*C31)
    ROcp35_132 = ROcp35_130*C32-ROcp35_731*S32
    ROcp35_232 = ROcp35_230*C32-ROcp35_831*S32
    ROcp35_332 = ROcp35_330*C32-ROcp35_931*S32
    ROcp35_732 = ROcp35_130*S32+ROcp35_731*C32
    ROcp35_832 = ROcp35_230*S32+ROcp35_831*C32
    ROcp35_932 = ROcp35_330*S32+ROcp35_931*C32
    ROcp35_133 = ROcp35_132*C33+ROcp35_431*S33
    ROcp35_233 = ROcp35_232*C33+ROcp35_531*S33
    ROcp35_333 = ROcp35_332*C33+ROcp35_631*S33
    ROcp35_433 = -(ROcp35_132*S33-ROcp35_431*C33)
    ROcp35_533 = -(ROcp35_232*S33-ROcp35_531*C33)
    ROcp35_633 = -(ROcp35_332*S33-ROcp35_631*C33)
    RLcp35_129 = ROcp35_15*s.dpt[1,10]+ROcp35_46*s.dpt[2,10]
    RLcp35_229 = ROcp35_25*s.dpt[1,10]+ROcp35_56*s.dpt[2,10]
    RLcp35_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp35_129 = OMcp35_16+ROcp35_15*qd[29]
    OMcp35_229 = OMcp35_26+ROcp35_25*qd[29]
    OMcp35_329 = OMcp35_36-qd[29]*S5
    ORcp35_129 = OMcp35_26*RLcp35_329-OMcp35_36*RLcp35_229
    ORcp35_229 = -(OMcp35_16*RLcp35_329-OMcp35_36*RLcp35_129)
    ORcp35_329 = OMcp35_16*RLcp35_229-OMcp35_26*RLcp35_129
    OMcp35_130 = OMcp35_129+ROcp35_729*qd[30]
    OMcp35_230 = OMcp35_229+ROcp35_829*qd[30]
    OMcp35_330 = OMcp35_329+ROcp35_929*qd[30]
    OPcp35_130 = OPcp35_16+ROcp35_15*qdd[29]+ROcp35_729*qdd[30]-qd[29]*(OMcp35_26*S5+OMcp35_36*ROcp35_25)+qd[30]*(\
   OMcp35_229*ROcp35_929-OMcp35_329*ROcp35_829)
    OPcp35_230 = OPcp35_26+ROcp35_25*qdd[29]+ROcp35_829*qdd[30]+qd[29]*(OMcp35_16*S5+OMcp35_36*ROcp35_15)-qd[30]*(\
   OMcp35_129*ROcp35_929-OMcp35_329*ROcp35_729)
    OPcp35_330 = OPcp35_36+ROcp35_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp35_16*ROcp35_25-OMcp35_26*ROcp35_15)+qd[30]*(\
   OMcp35_129*ROcp35_829-OMcp35_229*ROcp35_729)
    RLcp35_131 = ROcp35_430*s.dpt[2,33]
    RLcp35_231 = ROcp35_530*s.dpt[2,33]
    RLcp35_331 = ROcp35_630*s.dpt[2,33]
    OMcp35_131 = OMcp35_130+ROcp35_130*qd[31]
    OMcp35_231 = OMcp35_230+ROcp35_230*qd[31]
    OMcp35_331 = OMcp35_330+ROcp35_330*qd[31]
    ORcp35_131 = OMcp35_230*RLcp35_331-OMcp35_330*RLcp35_231
    ORcp35_231 = -(OMcp35_130*RLcp35_331-OMcp35_330*RLcp35_131)
    ORcp35_331 = OMcp35_130*RLcp35_231-OMcp35_230*RLcp35_131
    OMcp35_132 = OMcp35_131+ROcp35_431*qd[32]
    OMcp35_232 = OMcp35_231+ROcp35_531*qd[32]
    OMcp35_332 = OMcp35_331+ROcp35_631*qd[32]
    OMcp35_133 = OMcp35_132+ROcp35_732*qd[33]
    OMcp35_233 = OMcp35_232+ROcp35_832*qd[33]
    OMcp35_333 = OMcp35_332+ROcp35_932*qd[33]
    OPcp35_133 = OPcp35_130+ROcp35_130*qdd[31]+ROcp35_431*qdd[32]+ROcp35_732*qdd[33]+qd[31]*(OMcp35_230*ROcp35_330-\
   OMcp35_330*ROcp35_230)+qd[32]*(OMcp35_231*ROcp35_631-OMcp35_331*ROcp35_531)+qd[33]*(OMcp35_232*ROcp35_932-OMcp35_332*\
   ROcp35_832)
    OPcp35_233 = OPcp35_230+ROcp35_230*qdd[31]+ROcp35_531*qdd[32]+ROcp35_832*qdd[33]-qd[31]*(OMcp35_130*ROcp35_330-\
   OMcp35_330*ROcp35_130)-qd[32]*(OMcp35_131*ROcp35_631-OMcp35_331*ROcp35_431)-qd[33]*(OMcp35_132*ROcp35_932-OMcp35_332*\
   ROcp35_732)
    OPcp35_333 = OPcp35_330+ROcp35_330*qdd[31]+ROcp35_631*qdd[32]+ROcp35_932*qdd[33]+qd[31]*(OMcp35_130*ROcp35_230-\
   OMcp35_230*ROcp35_130)+qd[32]*(OMcp35_131*ROcp35_531-OMcp35_231*ROcp35_431)+qd[33]*(OMcp35_132*ROcp35_832-OMcp35_232*\
   ROcp35_732)

# = = Block_1_0_0_36_0_13 = = 
 
# Sensor Kinematics 


    ROcp35_436 = ROcp35_433*C36+ROcp35_732*S36
    ROcp35_536 = ROcp35_533*C36+ROcp35_832*S36
    ROcp35_636 = ROcp35_633*C36+ROcp35_932*S36
    ROcp35_736 = -(ROcp35_433*S36-ROcp35_732*C36)
    ROcp35_836 = -(ROcp35_533*S36-ROcp35_832*C36)
    ROcp35_936 = -(ROcp35_633*S36-ROcp35_932*C36)
    RLcp35_136 = ROcp35_433*s.dpt[2,35]+ROcp35_732*s.dpt[3,35]
    RLcp35_236 = ROcp35_533*s.dpt[2,35]+ROcp35_832*s.dpt[3,35]
    RLcp35_336 = ROcp35_633*s.dpt[2,35]+ROcp35_932*s.dpt[3,35]
    POcp35_136 = RLcp35_129+RLcp35_131+RLcp35_136+q[1]
    POcp35_236 = RLcp35_229+RLcp35_231+RLcp35_236+q[2]
    POcp35_336 = RLcp35_329+RLcp35_331+RLcp35_336+q[3]
    OMcp35_136 = OMcp35_133+ROcp35_133*qd[36]
    OMcp35_236 = OMcp35_233+ROcp35_233*qd[36]
    OMcp35_336 = OMcp35_333+ROcp35_333*qd[36]
    ORcp35_136 = OMcp35_233*RLcp35_336-OMcp35_333*RLcp35_236
    ORcp35_236 = -(OMcp35_133*RLcp35_336-OMcp35_333*RLcp35_136)
    ORcp35_336 = OMcp35_133*RLcp35_236-OMcp35_233*RLcp35_136
    VIcp35_136 = ORcp35_129+ORcp35_131+ORcp35_136+qd[1]
    VIcp35_236 = ORcp35_229+ORcp35_231+ORcp35_236+qd[2]
    VIcp35_336 = ORcp35_329+ORcp35_331+ORcp35_336+qd[3]
    OPcp35_136 = OPcp35_133+ROcp35_133*qdd[36]+qd[36]*(OMcp35_233*ROcp35_333-OMcp35_333*ROcp35_233)
    OPcp35_236 = OPcp35_233+ROcp35_233*qdd[36]-qd[36]*(OMcp35_133*ROcp35_333-OMcp35_333*ROcp35_133)
    OPcp35_336 = OPcp35_333+ROcp35_333*qdd[36]+qd[36]*(OMcp35_133*ROcp35_233-OMcp35_233*ROcp35_133)
    ACcp35_136 = qdd[1]+OMcp35_230*ORcp35_331+OMcp35_233*ORcp35_336+OMcp35_26*ORcp35_329-OMcp35_330*ORcp35_231-OMcp35_333*\
   ORcp35_236-OMcp35_36*ORcp35_229+OPcp35_230*RLcp35_331+OPcp35_233*RLcp35_336+OPcp35_26*RLcp35_329-OPcp35_330*RLcp35_231-\
   OPcp35_333*RLcp35_236-OPcp35_36*RLcp35_229
    ACcp35_236 = qdd[2]-OMcp35_130*ORcp35_331-OMcp35_133*ORcp35_336-OMcp35_16*ORcp35_329+OMcp35_330*ORcp35_131+OMcp35_333*\
   ORcp35_136+OMcp35_36*ORcp35_129-OPcp35_130*RLcp35_331-OPcp35_133*RLcp35_336-OPcp35_16*RLcp35_329+OPcp35_330*RLcp35_131+\
   OPcp35_333*RLcp35_136+OPcp35_36*RLcp35_129
    ACcp35_336 = qdd[3]+OMcp35_130*ORcp35_231+OMcp35_133*ORcp35_236+OMcp35_16*ORcp35_229-OMcp35_230*ORcp35_131-OMcp35_233*\
   ORcp35_136-OMcp35_26*ORcp35_129+OPcp35_130*RLcp35_231+OPcp35_133*RLcp35_236+OPcp35_16*RLcp35_229-OPcp35_230*RLcp35_131-\
   OPcp35_233*RLcp35_136-OPcp35_26*RLcp35_129

# = = Block_1_0_0_36_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp35_136
    sens.P[2] = POcp35_236
    sens.P[3] = POcp35_336
    sens.R[1,1] = ROcp35_133
    sens.R[1,2] = ROcp35_233
    sens.R[1,3] = ROcp35_333
    sens.R[2,1] = ROcp35_436
    sens.R[2,2] = ROcp35_536
    sens.R[2,3] = ROcp35_636
    sens.R[3,1] = ROcp35_736
    sens.R[3,2] = ROcp35_836
    sens.R[3,3] = ROcp35_936
    sens.V[1] = VIcp35_136
    sens.V[2] = VIcp35_236
    sens.V[3] = VIcp35_336
    sens.OM[1] = OMcp35_136
    sens.OM[2] = OMcp35_236
    sens.OM[3] = OMcp35_336
    sens.A[1] = ACcp35_136
    sens.A[2] = ACcp35_236
    sens.A[3] = ACcp35_336
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


    ROcp36_429 = ROcp36_46*C29+ROcp36_76*S29
    ROcp36_529 = ROcp36_56*C29+ROcp36_86*S29
    ROcp36_629 = S29p6*C5
    ROcp36_729 = -(ROcp36_46*S29-ROcp36_76*C29)
    ROcp36_829 = -(ROcp36_56*S29-ROcp36_86*C29)
    ROcp36_929 = C29p6*C5
    ROcp36_130 = ROcp36_15*C30+ROcp36_429*S30
    ROcp36_230 = ROcp36_25*C30+ROcp36_529*S30
    ROcp36_330 = ROcp36_629*S30-C30*S5
    ROcp36_430 = -(ROcp36_15*S30-ROcp36_429*C30)
    ROcp36_530 = -(ROcp36_25*S30-ROcp36_529*C30)
    ROcp36_630 = ROcp36_629*C30+S30*S5
    ROcp36_431 = ROcp36_430*C31+ROcp36_729*S31
    ROcp36_531 = ROcp36_530*C31+ROcp36_829*S31
    ROcp36_631 = ROcp36_630*C31+ROcp36_929*S31
    ROcp36_731 = -(ROcp36_430*S31-ROcp36_729*C31)
    ROcp36_831 = -(ROcp36_530*S31-ROcp36_829*C31)
    ROcp36_931 = -(ROcp36_630*S31-ROcp36_929*C31)
    ROcp36_132 = ROcp36_130*C32-ROcp36_731*S32
    ROcp36_232 = ROcp36_230*C32-ROcp36_831*S32
    ROcp36_332 = ROcp36_330*C32-ROcp36_931*S32
    ROcp36_732 = ROcp36_130*S32+ROcp36_731*C32
    ROcp36_832 = ROcp36_230*S32+ROcp36_831*C32
    ROcp36_932 = ROcp36_330*S32+ROcp36_931*C32
    ROcp36_133 = ROcp36_132*C33+ROcp36_431*S33
    ROcp36_233 = ROcp36_232*C33+ROcp36_531*S33
    ROcp36_333 = ROcp36_332*C33+ROcp36_631*S33
    ROcp36_433 = -(ROcp36_132*S33-ROcp36_431*C33)
    ROcp36_533 = -(ROcp36_232*S33-ROcp36_531*C33)
    ROcp36_633 = -(ROcp36_332*S33-ROcp36_631*C33)
    RLcp36_129 = ROcp36_15*s.dpt[1,10]+ROcp36_46*s.dpt[2,10]
    RLcp36_229 = ROcp36_25*s.dpt[1,10]+ROcp36_56*s.dpt[2,10]
    RLcp36_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp36_129 = OMcp36_16+ROcp36_15*qd[29]
    OMcp36_229 = OMcp36_26+ROcp36_25*qd[29]
    OMcp36_329 = OMcp36_36-qd[29]*S5
    ORcp36_129 = OMcp36_26*RLcp36_329-OMcp36_36*RLcp36_229
    ORcp36_229 = -(OMcp36_16*RLcp36_329-OMcp36_36*RLcp36_129)
    ORcp36_329 = OMcp36_16*RLcp36_229-OMcp36_26*RLcp36_129
    OMcp36_130 = OMcp36_129+ROcp36_729*qd[30]
    OMcp36_230 = OMcp36_229+ROcp36_829*qd[30]
    OMcp36_330 = OMcp36_329+ROcp36_929*qd[30]
    OPcp36_130 = OPcp36_16+ROcp36_15*qdd[29]+ROcp36_729*qdd[30]-qd[29]*(OMcp36_26*S5+OMcp36_36*ROcp36_25)+qd[30]*(\
   OMcp36_229*ROcp36_929-OMcp36_329*ROcp36_829)
    OPcp36_230 = OPcp36_26+ROcp36_25*qdd[29]+ROcp36_829*qdd[30]+qd[29]*(OMcp36_16*S5+OMcp36_36*ROcp36_15)-qd[30]*(\
   OMcp36_129*ROcp36_929-OMcp36_329*ROcp36_729)
    OPcp36_330 = OPcp36_36+ROcp36_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp36_16*ROcp36_25-OMcp36_26*ROcp36_15)+qd[30]*(\
   OMcp36_129*ROcp36_829-OMcp36_229*ROcp36_729)
    RLcp36_131 = ROcp36_430*s.dpt[2,33]
    RLcp36_231 = ROcp36_530*s.dpt[2,33]
    RLcp36_331 = ROcp36_630*s.dpt[2,33]
    OMcp36_131 = OMcp36_130+ROcp36_130*qd[31]
    OMcp36_231 = OMcp36_230+ROcp36_230*qd[31]
    OMcp36_331 = OMcp36_330+ROcp36_330*qd[31]
    ORcp36_131 = OMcp36_230*RLcp36_331-OMcp36_330*RLcp36_231
    ORcp36_231 = -(OMcp36_130*RLcp36_331-OMcp36_330*RLcp36_131)
    ORcp36_331 = OMcp36_130*RLcp36_231-OMcp36_230*RLcp36_131
    OMcp36_132 = OMcp36_131+ROcp36_431*qd[32]
    OMcp36_232 = OMcp36_231+ROcp36_531*qd[32]
    OMcp36_332 = OMcp36_331+ROcp36_631*qd[32]
    OMcp36_133 = OMcp36_132+ROcp36_732*qd[33]
    OMcp36_233 = OMcp36_232+ROcp36_832*qd[33]
    OMcp36_333 = OMcp36_332+ROcp36_932*qd[33]
    OPcp36_133 = OPcp36_130+ROcp36_130*qdd[31]+ROcp36_431*qdd[32]+ROcp36_732*qdd[33]+qd[31]*(OMcp36_230*ROcp36_330-\
   OMcp36_330*ROcp36_230)+qd[32]*(OMcp36_231*ROcp36_631-OMcp36_331*ROcp36_531)+qd[33]*(OMcp36_232*ROcp36_932-OMcp36_332*\
   ROcp36_832)
    OPcp36_233 = OPcp36_230+ROcp36_230*qdd[31]+ROcp36_531*qdd[32]+ROcp36_832*qdd[33]-qd[31]*(OMcp36_130*ROcp36_330-\
   OMcp36_330*ROcp36_130)-qd[32]*(OMcp36_131*ROcp36_631-OMcp36_331*ROcp36_431)-qd[33]*(OMcp36_132*ROcp36_932-OMcp36_332*\
   ROcp36_732)
    OPcp36_333 = OPcp36_330+ROcp36_330*qdd[31]+ROcp36_631*qdd[32]+ROcp36_932*qdd[33]+qd[31]*(OMcp36_130*ROcp36_230-\
   OMcp36_230*ROcp36_130)+qd[32]*(OMcp36_131*ROcp36_531-OMcp36_231*ROcp36_431)+qd[33]*(OMcp36_132*ROcp36_832-OMcp36_232*\
   ROcp36_732)

# = = Block_1_0_0_37_0_13 = = 
 
# Sensor Kinematics 


    ROcp36_436 = ROcp36_433*C36+ROcp36_732*S36
    ROcp36_536 = ROcp36_533*C36+ROcp36_832*S36
    ROcp36_636 = ROcp36_633*C36+ROcp36_932*S36
    ROcp36_736 = -(ROcp36_433*S36-ROcp36_732*C36)
    ROcp36_836 = -(ROcp36_533*S36-ROcp36_832*C36)
    ROcp36_936 = -(ROcp36_633*S36-ROcp36_932*C36)
    ROcp36_137 = ROcp36_133*C37-ROcp36_736*S37
    ROcp36_237 = ROcp36_233*C37-ROcp36_836*S37
    ROcp36_337 = ROcp36_333*C37-ROcp36_936*S37
    ROcp36_737 = ROcp36_133*S37+ROcp36_736*C37
    ROcp36_837 = ROcp36_233*S37+ROcp36_836*C37
    ROcp36_937 = ROcp36_333*S37+ROcp36_936*C37
    RLcp36_136 = ROcp36_433*s.dpt[2,35]+ROcp36_732*s.dpt[3,35]
    RLcp36_236 = ROcp36_533*s.dpt[2,35]+ROcp36_832*s.dpt[3,35]
    RLcp36_336 = ROcp36_633*s.dpt[2,35]+ROcp36_932*s.dpt[3,35]
    POcp36_136 = RLcp36_129+RLcp36_131+RLcp36_136+q[1]
    POcp36_236 = RLcp36_229+RLcp36_231+RLcp36_236+q[2]
    POcp36_336 = RLcp36_329+RLcp36_331+RLcp36_336+q[3]
    OMcp36_136 = OMcp36_133+ROcp36_133*qd[36]
    OMcp36_236 = OMcp36_233+ROcp36_233*qd[36]
    OMcp36_336 = OMcp36_333+ROcp36_333*qd[36]
    ORcp36_136 = OMcp36_233*RLcp36_336-OMcp36_333*RLcp36_236
    ORcp36_236 = -(OMcp36_133*RLcp36_336-OMcp36_333*RLcp36_136)
    ORcp36_336 = OMcp36_133*RLcp36_236-OMcp36_233*RLcp36_136
    VIcp36_136 = ORcp36_129+ORcp36_131+ORcp36_136+qd[1]
    VIcp36_236 = ORcp36_229+ORcp36_231+ORcp36_236+qd[2]
    VIcp36_336 = ORcp36_329+ORcp36_331+ORcp36_336+qd[3]
    ACcp36_136 = qdd[1]+OMcp36_230*ORcp36_331+OMcp36_233*ORcp36_336+OMcp36_26*ORcp36_329-OMcp36_330*ORcp36_231-OMcp36_333*\
   ORcp36_236-OMcp36_36*ORcp36_229+OPcp36_230*RLcp36_331+OPcp36_233*RLcp36_336+OPcp36_26*RLcp36_329-OPcp36_330*RLcp36_231-\
   OPcp36_333*RLcp36_236-OPcp36_36*RLcp36_229
    ACcp36_236 = qdd[2]-OMcp36_130*ORcp36_331-OMcp36_133*ORcp36_336-OMcp36_16*ORcp36_329+OMcp36_330*ORcp36_131+OMcp36_333*\
   ORcp36_136+OMcp36_36*ORcp36_129-OPcp36_130*RLcp36_331-OPcp36_133*RLcp36_336-OPcp36_16*RLcp36_329+OPcp36_330*RLcp36_131+\
   OPcp36_333*RLcp36_136+OPcp36_36*RLcp36_129
    ACcp36_336 = qdd[3]+OMcp36_130*ORcp36_231+OMcp36_133*ORcp36_236+OMcp36_16*ORcp36_229-OMcp36_230*ORcp36_131-OMcp36_233*\
   ORcp36_136-OMcp36_26*ORcp36_129+OPcp36_130*RLcp36_231+OPcp36_133*RLcp36_236+OPcp36_16*RLcp36_229-OPcp36_230*RLcp36_131-\
   OPcp36_233*RLcp36_136-OPcp36_26*RLcp36_129
    OMcp36_137 = OMcp36_136+ROcp36_436*qd[37]
    OMcp36_237 = OMcp36_236+ROcp36_536*qd[37]
    OMcp36_337 = OMcp36_336+ROcp36_636*qd[37]
    OPcp36_137 = OPcp36_133+ROcp36_133*qdd[36]+ROcp36_436*qdd[37]+qd[36]*(OMcp36_233*ROcp36_333-OMcp36_333*ROcp36_233)+\
   qd[37]*(OMcp36_236*ROcp36_636-OMcp36_336*ROcp36_536)
    OPcp36_237 = OPcp36_233+ROcp36_233*qdd[36]+ROcp36_536*qdd[37]-qd[36]*(OMcp36_133*ROcp36_333-OMcp36_333*ROcp36_133)-\
   qd[37]*(OMcp36_136*ROcp36_636-OMcp36_336*ROcp36_436)
    OPcp36_337 = OPcp36_333+ROcp36_333*qdd[36]+ROcp36_636*qdd[37]+qd[36]*(OMcp36_133*ROcp36_233-OMcp36_233*ROcp36_133)+\
   qd[37]*(OMcp36_136*ROcp36_536-OMcp36_236*ROcp36_436)

# = = Block_1_0_0_37_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp36_136
    sens.P[2] = POcp36_236
    sens.P[3] = POcp36_336
    sens.R[1,1] = ROcp36_137
    sens.R[1,2] = ROcp36_237
    sens.R[1,3] = ROcp36_337
    sens.R[2,1] = ROcp36_436
    sens.R[2,2] = ROcp36_536
    sens.R[2,3] = ROcp36_636
    sens.R[3,1] = ROcp36_737
    sens.R[3,2] = ROcp36_837
    sens.R[3,3] = ROcp36_937
    sens.V[1] = VIcp36_136
    sens.V[2] = VIcp36_236
    sens.V[3] = VIcp36_336
    sens.OM[1] = OMcp36_137
    sens.OM[2] = OMcp36_237
    sens.OM[3] = OMcp36_337
    sens.A[1] = ACcp36_136
    sens.A[2] = ACcp36_236
    sens.A[3] = ACcp36_336
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

# = = Block_1_0_0_38_0_14 = = 
 
# Sensor Kinematics 


    ROcp37_438 = ROcp37_46*C38+ROcp37_76*S38
    ROcp37_538 = ROcp37_56*C38+ROcp37_86*S38
    ROcp37_638 = S38p6*C5
    ROcp37_738 = -(ROcp37_46*S38-ROcp37_76*C38)
    ROcp37_838 = -(ROcp37_56*S38-ROcp37_86*C38)
    ROcp37_938 = C38p6*C5
    RLcp37_138 = ROcp37_15*s.dpt[1,11]+ROcp37_46*s.dpt[2,11]+ROcp37_76*s.dpt[3,11]
    RLcp37_238 = ROcp37_25*s.dpt[1,11]+ROcp37_56*s.dpt[2,11]+ROcp37_86*s.dpt[3,11]
    RLcp37_338 = C5*C6*s.dpt[3,11]-s.dpt[1,11]*S5+s.dpt[2,11]*C5*S6
    POcp37_138 = RLcp37_138+q[1]
    POcp37_238 = RLcp37_238+q[2]
    POcp37_338 = RLcp37_338+q[3]
    OMcp37_138 = OMcp37_16+ROcp37_15*qd[38]
    OMcp37_238 = OMcp37_26+ROcp37_25*qd[38]
    OMcp37_338 = OMcp37_36-qd[38]*S5
    ORcp37_138 = OMcp37_26*RLcp37_338-OMcp37_36*RLcp37_238
    ORcp37_238 = -(OMcp37_16*RLcp37_338-OMcp37_36*RLcp37_138)
    ORcp37_338 = OMcp37_16*RLcp37_238-OMcp37_26*RLcp37_138
    VIcp37_138 = ORcp37_138+qd[1]
    VIcp37_238 = ORcp37_238+qd[2]
    VIcp37_338 = ORcp37_338+qd[3]
    OPcp37_138 = OPcp37_16+ROcp37_15*qdd[38]-qd[38]*(OMcp37_26*S5+OMcp37_36*ROcp37_25)
    OPcp37_238 = OPcp37_26+ROcp37_25*qdd[38]+qd[38]*(OMcp37_16*S5+OMcp37_36*ROcp37_15)
    OPcp37_338 = OPcp37_36-qdd[38]*S5+qd[38]*(OMcp37_16*ROcp37_25-OMcp37_26*ROcp37_15)
    ACcp37_138 = qdd[1]+OMcp37_26*ORcp37_338-OMcp37_36*ORcp37_238+OPcp37_26*RLcp37_338-OPcp37_36*RLcp37_238
    ACcp37_238 = qdd[2]-OMcp37_16*ORcp37_338+OMcp37_36*ORcp37_138-OPcp37_16*RLcp37_338+OPcp37_36*RLcp37_138
    ACcp37_338 = qdd[3]+OMcp37_16*ORcp37_238-OMcp37_26*ORcp37_138+OPcp37_16*RLcp37_238-OPcp37_26*RLcp37_138

# = = Block_1_0_0_38_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp37_138
    sens.P[2] = POcp37_238
    sens.P[3] = POcp37_338
    sens.R[1,1] = ROcp37_15
    sens.R[1,2] = ROcp37_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp37_438
    sens.R[2,2] = ROcp37_538
    sens.R[2,3] = ROcp37_638
    sens.R[3,1] = ROcp37_738
    sens.R[3,2] = ROcp37_838
    sens.R[3,3] = ROcp37_938
    sens.V[1] = VIcp37_138
    sens.V[2] = VIcp37_238
    sens.V[3] = VIcp37_338
    sens.OM[1] = OMcp37_138
    sens.OM[2] = OMcp37_238
    sens.OM[3] = OMcp37_338
    sens.A[1] = ACcp37_138
    sens.A[2] = ACcp37_238
    sens.A[3] = ACcp37_338
    sens.OMP[1] = OPcp37_138
    sens.OMP[2] = OPcp37_238
    sens.OMP[3] = OPcp37_338
 
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

# = = Block_1_0_0_39_0_14 = = 
 
# Sensor Kinematics 


    ROcp38_438 = ROcp38_46*C38+ROcp38_76*S38
    ROcp38_538 = ROcp38_56*C38+ROcp38_86*S38
    ROcp38_638 = S38p6*C5
    ROcp38_738 = -(ROcp38_46*S38-ROcp38_76*C38)
    ROcp38_838 = -(ROcp38_56*S38-ROcp38_86*C38)
    ROcp38_938 = C38p6*C5
    ROcp38_139 = ROcp38_15*C39+ROcp38_438*S39
    ROcp38_239 = ROcp38_25*C39+ROcp38_538*S39
    ROcp38_339 = ROcp38_638*S39-C39*S5
    ROcp38_439 = -(ROcp38_15*S39-ROcp38_438*C39)
    ROcp38_539 = -(ROcp38_25*S39-ROcp38_538*C39)
    ROcp38_639 = ROcp38_638*C39+S39*S5
    RLcp38_138 = ROcp38_15*s.dpt[1,11]+ROcp38_46*s.dpt[2,11]+ROcp38_76*s.dpt[3,11]
    RLcp38_238 = ROcp38_25*s.dpt[1,11]+ROcp38_56*s.dpt[2,11]+ROcp38_86*s.dpt[3,11]
    RLcp38_338 = C5*C6*s.dpt[3,11]-s.dpt[1,11]*S5+s.dpt[2,11]*C5*S6
    POcp38_138 = RLcp38_138+q[1]
    POcp38_238 = RLcp38_238+q[2]
    POcp38_338 = RLcp38_338+q[3]
    OMcp38_138 = OMcp38_16+ROcp38_15*qd[38]
    OMcp38_238 = OMcp38_26+ROcp38_25*qd[38]
    OMcp38_338 = OMcp38_36-qd[38]*S5
    ORcp38_138 = OMcp38_26*RLcp38_338-OMcp38_36*RLcp38_238
    ORcp38_238 = -(OMcp38_16*RLcp38_338-OMcp38_36*RLcp38_138)
    ORcp38_338 = OMcp38_16*RLcp38_238-OMcp38_26*RLcp38_138
    VIcp38_138 = ORcp38_138+qd[1]
    VIcp38_238 = ORcp38_238+qd[2]
    VIcp38_338 = ORcp38_338+qd[3]
    ACcp38_138 = qdd[1]+OMcp38_26*ORcp38_338-OMcp38_36*ORcp38_238+OPcp38_26*RLcp38_338-OPcp38_36*RLcp38_238
    ACcp38_238 = qdd[2]-OMcp38_16*ORcp38_338+OMcp38_36*ORcp38_138-OPcp38_16*RLcp38_338+OPcp38_36*RLcp38_138
    ACcp38_338 = qdd[3]+OMcp38_16*ORcp38_238-OMcp38_26*ORcp38_138+OPcp38_16*RLcp38_238-OPcp38_26*RLcp38_138
    OMcp38_139 = OMcp38_138+ROcp38_738*qd[39]
    OMcp38_239 = OMcp38_238+ROcp38_838*qd[39]
    OMcp38_339 = OMcp38_338+ROcp38_938*qd[39]
    OPcp38_139 = OPcp38_16+ROcp38_15*qdd[38]+ROcp38_738*qdd[39]-qd[38]*(OMcp38_26*S5+OMcp38_36*ROcp38_25)+qd[39]*(\
   OMcp38_238*ROcp38_938-OMcp38_338*ROcp38_838)
    OPcp38_239 = OPcp38_26+ROcp38_25*qdd[38]+ROcp38_838*qdd[39]+qd[38]*(OMcp38_16*S5+OMcp38_36*ROcp38_15)-qd[39]*(\
   OMcp38_138*ROcp38_938-OMcp38_338*ROcp38_738)
    OPcp38_339 = OPcp38_36+ROcp38_938*qdd[39]-qdd[38]*S5+qd[38]*(OMcp38_16*ROcp38_25-OMcp38_26*ROcp38_15)+qd[39]*(\
   OMcp38_138*ROcp38_838-OMcp38_238*ROcp38_738)

# = = Block_1_0_0_39_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp38_138
    sens.P[2] = POcp38_238
    sens.P[3] = POcp38_338
    sens.R[1,1] = ROcp38_139
    sens.R[1,2] = ROcp38_239
    sens.R[1,3] = ROcp38_339
    sens.R[2,1] = ROcp38_439
    sens.R[2,2] = ROcp38_539
    sens.R[2,3] = ROcp38_639
    sens.R[3,1] = ROcp38_738
    sens.R[3,2] = ROcp38_838
    sens.R[3,3] = ROcp38_938
    sens.V[1] = VIcp38_138
    sens.V[2] = VIcp38_238
    sens.V[3] = VIcp38_338
    sens.OM[1] = OMcp38_139
    sens.OM[2] = OMcp38_239
    sens.OM[3] = OMcp38_339
    sens.A[1] = ACcp38_138
    sens.A[2] = ACcp38_238
    sens.A[3] = ACcp38_338
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

# = = Block_1_0_0_40_0_15 = = 
 
# Sensor Kinematics 


    ROcp39_440 = ROcp39_46*C40+ROcp39_76*S40
    ROcp39_540 = ROcp39_56*C40+ROcp39_86*S40
    ROcp39_640 = S40p6*C5
    ROcp39_740 = -(ROcp39_46*S40-ROcp39_76*C40)
    ROcp39_840 = -(ROcp39_56*S40-ROcp39_86*C40)
    ROcp39_940 = C40p6*C5
    RLcp39_140 = ROcp39_15*s.dpt[1,12]+ROcp39_46*s.dpt[2,12]
    RLcp39_240 = ROcp39_25*s.dpt[1,12]+ROcp39_56*s.dpt[2,12]
    RLcp39_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    POcp39_140 = RLcp39_140+q[1]
    POcp39_240 = RLcp39_240+q[2]
    POcp39_340 = RLcp39_340+q[3]
    OMcp39_140 = OMcp39_16+ROcp39_15*qd[40]
    OMcp39_240 = OMcp39_26+ROcp39_25*qd[40]
    OMcp39_340 = OMcp39_36-qd[40]*S5
    ORcp39_140 = OMcp39_26*RLcp39_340-OMcp39_36*RLcp39_240
    ORcp39_240 = -(OMcp39_16*RLcp39_340-OMcp39_36*RLcp39_140)
    ORcp39_340 = OMcp39_16*RLcp39_240-OMcp39_26*RLcp39_140
    VIcp39_140 = ORcp39_140+qd[1]
    VIcp39_240 = ORcp39_240+qd[2]
    VIcp39_340 = ORcp39_340+qd[3]
    OPcp39_140 = OPcp39_16+ROcp39_15*qdd[40]-qd[40]*(OMcp39_26*S5+OMcp39_36*ROcp39_25)
    OPcp39_240 = OPcp39_26+ROcp39_25*qdd[40]+qd[40]*(OMcp39_16*S5+OMcp39_36*ROcp39_15)
    OPcp39_340 = OPcp39_36-qdd[40]*S5+qd[40]*(OMcp39_16*ROcp39_25-OMcp39_26*ROcp39_15)
    ACcp39_140 = qdd[1]+OMcp39_26*ORcp39_340-OMcp39_36*ORcp39_240+OPcp39_26*RLcp39_340-OPcp39_36*RLcp39_240
    ACcp39_240 = qdd[2]-OMcp39_16*ORcp39_340+OMcp39_36*ORcp39_140-OPcp39_16*RLcp39_340+OPcp39_36*RLcp39_140
    ACcp39_340 = qdd[3]+OMcp39_16*ORcp39_240-OMcp39_26*ORcp39_140+OPcp39_16*RLcp39_240-OPcp39_26*RLcp39_140

# = = Block_1_0_0_40_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp39_140
    sens.P[2] = POcp39_240
    sens.P[3] = POcp39_340
    sens.R[1,1] = ROcp39_15
    sens.R[1,2] = ROcp39_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp39_440
    sens.R[2,2] = ROcp39_540
    sens.R[2,3] = ROcp39_640
    sens.R[3,1] = ROcp39_740
    sens.R[3,2] = ROcp39_840
    sens.R[3,3] = ROcp39_940
    sens.V[1] = VIcp39_140
    sens.V[2] = VIcp39_240
    sens.V[3] = VIcp39_340
    sens.OM[1] = OMcp39_140
    sens.OM[2] = OMcp39_240
    sens.OM[3] = OMcp39_340
    sens.A[1] = ACcp39_140
    sens.A[2] = ACcp39_240
    sens.A[3] = ACcp39_340
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
    ROcp40_76 = ROcp40_75*C6+S4*S6
    ROcp40_86 = ROcp40_85*C6-C4*S6
    OMcp40_15 = -qd[5]*S4
    OMcp40_25 = qd[5]*C4
    OMcp40_16 = OMcp40_15+ROcp40_15*qd[6]
    OMcp40_26 = OMcp40_25+ROcp40_25*qd[6]
    OMcp40_36 = qd[4]-qd[6]*S5
    OPcp40_16 = ROcp40_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp40_25*S5+ROcp40_25*qd[4])
    OPcp40_26 = ROcp40_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp40_15*S5+ROcp40_15*qd[4])
    OPcp40_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_41_0_15 = = 
 
# Sensor Kinematics 


    ROcp40_440 = ROcp40_46*C40+ROcp40_76*S40
    ROcp40_540 = ROcp40_56*C40+ROcp40_86*S40
    ROcp40_640 = S40p6*C5
    ROcp40_740 = -(ROcp40_46*S40-ROcp40_76*C40)
    ROcp40_840 = -(ROcp40_56*S40-ROcp40_86*C40)
    ROcp40_940 = C40p6*C5
    ROcp40_141 = ROcp40_15*C41+ROcp40_440*S41
    ROcp40_241 = ROcp40_25*C41+ROcp40_540*S41
    ROcp40_341 = ROcp40_640*S41-C41*S5
    ROcp40_441 = -(ROcp40_15*S41-ROcp40_440*C41)
    ROcp40_541 = -(ROcp40_25*S41-ROcp40_540*C41)
    ROcp40_641 = ROcp40_640*C41+S41*S5
    RLcp40_140 = ROcp40_15*s.dpt[1,12]+ROcp40_46*s.dpt[2,12]
    RLcp40_240 = ROcp40_25*s.dpt[1,12]+ROcp40_56*s.dpt[2,12]
    RLcp40_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    POcp40_140 = RLcp40_140+q[1]
    POcp40_240 = RLcp40_240+q[2]
    POcp40_340 = RLcp40_340+q[3]
    OMcp40_140 = OMcp40_16+ROcp40_15*qd[40]
    OMcp40_240 = OMcp40_26+ROcp40_25*qd[40]
    OMcp40_340 = OMcp40_36-qd[40]*S5
    ORcp40_140 = OMcp40_26*RLcp40_340-OMcp40_36*RLcp40_240
    ORcp40_240 = -(OMcp40_16*RLcp40_340-OMcp40_36*RLcp40_140)
    ORcp40_340 = OMcp40_16*RLcp40_240-OMcp40_26*RLcp40_140
    VIcp40_140 = ORcp40_140+qd[1]
    VIcp40_240 = ORcp40_240+qd[2]
    VIcp40_340 = ORcp40_340+qd[3]
    ACcp40_140 = qdd[1]+OMcp40_26*ORcp40_340-OMcp40_36*ORcp40_240+OPcp40_26*RLcp40_340-OPcp40_36*RLcp40_240
    ACcp40_240 = qdd[2]-OMcp40_16*ORcp40_340+OMcp40_36*ORcp40_140-OPcp40_16*RLcp40_340+OPcp40_36*RLcp40_140
    ACcp40_340 = qdd[3]+OMcp40_16*ORcp40_240-OMcp40_26*ORcp40_140+OPcp40_16*RLcp40_240-OPcp40_26*RLcp40_140
    OMcp40_141 = OMcp40_140+ROcp40_740*qd[41]
    OMcp40_241 = OMcp40_240+ROcp40_840*qd[41]
    OMcp40_341 = OMcp40_340+ROcp40_940*qd[41]
    OPcp40_141 = OPcp40_16+ROcp40_15*qdd[40]+ROcp40_740*qdd[41]-qd[40]*(OMcp40_26*S5+OMcp40_36*ROcp40_25)+qd[41]*(\
   OMcp40_240*ROcp40_940-OMcp40_340*ROcp40_840)
    OPcp40_241 = OPcp40_26+ROcp40_25*qdd[40]+ROcp40_840*qdd[41]+qd[40]*(OMcp40_16*S5+OMcp40_36*ROcp40_15)-qd[41]*(\
   OMcp40_140*ROcp40_940-OMcp40_340*ROcp40_740)
    OPcp40_341 = OPcp40_36+ROcp40_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp40_16*ROcp40_25-OMcp40_26*ROcp40_15)+qd[41]*(\
   OMcp40_140*ROcp40_840-OMcp40_240*ROcp40_740)

# = = Block_1_0_0_41_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp40_140
    sens.P[2] = POcp40_240
    sens.P[3] = POcp40_340
    sens.R[1,1] = ROcp40_141
    sens.R[1,2] = ROcp40_241
    sens.R[1,3] = ROcp40_341
    sens.R[2,1] = ROcp40_441
    sens.R[2,2] = ROcp40_541
    sens.R[2,3] = ROcp40_641
    sens.R[3,1] = ROcp40_740
    sens.R[3,2] = ROcp40_840
    sens.R[3,3] = ROcp40_940
    sens.V[1] = VIcp40_140
    sens.V[2] = VIcp40_240
    sens.V[3] = VIcp40_340
    sens.OM[1] = OMcp40_141
    sens.OM[2] = OMcp40_241
    sens.OM[3] = OMcp40_341
    sens.A[1] = ACcp40_140
    sens.A[2] = ACcp40_240
    sens.A[3] = ACcp40_340
    sens.OMP[1] = OPcp40_141
    sens.OMP[2] = OPcp40_241
    sens.OMP[3] = OPcp40_341
 
# 
  elif(isens==42): 


# = = Block_1_0_0_42_0_1 = = 
 
# Sensor Kinematics 


    ROcp41_15 = C4*C5
    ROcp41_25 = S4*C5
    ROcp41_75 = C4*S5
    ROcp41_85 = S4*S5
    ROcp41_46 = ROcp41_75*S6-S4*C6
    ROcp41_56 = ROcp41_85*S6+C4*C6
    ROcp41_76 = ROcp41_75*C6+S4*S6
    ROcp41_86 = ROcp41_85*C6-C4*S6
    OMcp41_15 = -qd[5]*S4
    OMcp41_25 = qd[5]*C4
    OMcp41_16 = OMcp41_15+ROcp41_15*qd[6]
    OMcp41_26 = OMcp41_25+ROcp41_25*qd[6]
    OMcp41_36 = qd[4]-qd[6]*S5
    OPcp41_16 = ROcp41_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp41_25*S5+ROcp41_25*qd[4])
    OPcp41_26 = ROcp41_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp41_15*S5+ROcp41_15*qd[4])
    OPcp41_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_42_0_15 = = 
 
# Sensor Kinematics 


    ROcp41_440 = ROcp41_46*C40+ROcp41_76*S40
    ROcp41_540 = ROcp41_56*C40+ROcp41_86*S40
    ROcp41_640 = S40p6*C5
    ROcp41_740 = -(ROcp41_46*S40-ROcp41_76*C40)
    ROcp41_840 = -(ROcp41_56*S40-ROcp41_86*C40)
    ROcp41_940 = C40p6*C5
    ROcp41_141 = ROcp41_15*C41+ROcp41_440*S41
    ROcp41_241 = ROcp41_25*C41+ROcp41_540*S41
    ROcp41_341 = ROcp41_640*S41-C41*S5
    ROcp41_441 = -(ROcp41_15*S41-ROcp41_440*C41)
    ROcp41_541 = -(ROcp41_25*S41-ROcp41_540*C41)
    ROcp41_641 = ROcp41_640*C41+S41*S5
    ROcp41_442 = ROcp41_441*C42+ROcp41_740*S42
    ROcp41_542 = ROcp41_541*C42+ROcp41_840*S42
    ROcp41_642 = ROcp41_641*C42+ROcp41_940*S42
    ROcp41_742 = -(ROcp41_441*S42-ROcp41_740*C42)
    ROcp41_842 = -(ROcp41_541*S42-ROcp41_840*C42)
    ROcp41_942 = -(ROcp41_641*S42-ROcp41_940*C42)
    RLcp41_140 = ROcp41_15*s.dpt[1,12]+ROcp41_46*s.dpt[2,12]
    RLcp41_240 = ROcp41_25*s.dpt[1,12]+ROcp41_56*s.dpt[2,12]
    RLcp41_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp41_140 = OMcp41_16+ROcp41_15*qd[40]
    OMcp41_240 = OMcp41_26+ROcp41_25*qd[40]
    OMcp41_340 = OMcp41_36-qd[40]*S5
    ORcp41_140 = OMcp41_26*RLcp41_340-OMcp41_36*RLcp41_240
    ORcp41_240 = -(OMcp41_16*RLcp41_340-OMcp41_36*RLcp41_140)
    ORcp41_340 = OMcp41_16*RLcp41_240-OMcp41_26*RLcp41_140
    OMcp41_141 = OMcp41_140+ROcp41_740*qd[41]
    OMcp41_241 = OMcp41_240+ROcp41_840*qd[41]
    OMcp41_341 = OMcp41_340+ROcp41_940*qd[41]
    OPcp41_141 = OPcp41_16+ROcp41_15*qdd[40]+ROcp41_740*qdd[41]-qd[40]*(OMcp41_26*S5+OMcp41_36*ROcp41_25)+qd[41]*(\
   OMcp41_240*ROcp41_940-OMcp41_340*ROcp41_840)
    OPcp41_241 = OPcp41_26+ROcp41_25*qdd[40]+ROcp41_840*qdd[41]+qd[40]*(OMcp41_16*S5+OMcp41_36*ROcp41_15)-qd[41]*(\
   OMcp41_140*ROcp41_940-OMcp41_340*ROcp41_740)
    OPcp41_341 = OPcp41_36+ROcp41_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp41_16*ROcp41_25-OMcp41_26*ROcp41_15)+qd[41]*(\
   OMcp41_140*ROcp41_840-OMcp41_240*ROcp41_740)
    RLcp41_142 = ROcp41_441*s.dpt[2,42]
    RLcp41_242 = ROcp41_541*s.dpt[2,42]
    RLcp41_342 = ROcp41_641*s.dpt[2,42]
    POcp41_142 = RLcp41_140+RLcp41_142+q[1]
    POcp41_242 = RLcp41_240+RLcp41_242+q[2]
    POcp41_342 = RLcp41_340+RLcp41_342+q[3]
    OMcp41_142 = OMcp41_141+ROcp41_141*qd[42]
    OMcp41_242 = OMcp41_241+ROcp41_241*qd[42]
    OMcp41_342 = OMcp41_341+ROcp41_341*qd[42]
    ORcp41_142 = OMcp41_241*RLcp41_342-OMcp41_341*RLcp41_242
    ORcp41_242 = -(OMcp41_141*RLcp41_342-OMcp41_341*RLcp41_142)
    ORcp41_342 = OMcp41_141*RLcp41_242-OMcp41_241*RLcp41_142
    VIcp41_142 = ORcp41_140+ORcp41_142+qd[1]
    VIcp41_242 = ORcp41_240+ORcp41_242+qd[2]
    VIcp41_342 = ORcp41_340+ORcp41_342+qd[3]
    OPcp41_142 = OPcp41_141+ROcp41_141*qdd[42]+qd[42]*(OMcp41_241*ROcp41_341-OMcp41_341*ROcp41_241)
    OPcp41_242 = OPcp41_241+ROcp41_241*qdd[42]-qd[42]*(OMcp41_141*ROcp41_341-OMcp41_341*ROcp41_141)
    OPcp41_342 = OPcp41_341+ROcp41_341*qdd[42]+qd[42]*(OMcp41_141*ROcp41_241-OMcp41_241*ROcp41_141)
    ACcp41_142 = qdd[1]+OMcp41_241*ORcp41_342+OMcp41_26*ORcp41_340-OMcp41_341*ORcp41_242-OMcp41_36*ORcp41_240+OPcp41_241*\
   RLcp41_342+OPcp41_26*RLcp41_340-OPcp41_341*RLcp41_242-OPcp41_36*RLcp41_240
    ACcp41_242 = qdd[2]-OMcp41_141*ORcp41_342-OMcp41_16*ORcp41_340+OMcp41_341*ORcp41_142+OMcp41_36*ORcp41_140-OPcp41_141*\
   RLcp41_342-OPcp41_16*RLcp41_340+OPcp41_341*RLcp41_142+OPcp41_36*RLcp41_140
    ACcp41_342 = qdd[3]+OMcp41_141*ORcp41_242+OMcp41_16*ORcp41_240-OMcp41_241*ORcp41_142-OMcp41_26*ORcp41_140+OPcp41_141*\
   RLcp41_242+OPcp41_16*RLcp41_240-OPcp41_241*RLcp41_142-OPcp41_26*RLcp41_140

# = = Block_1_0_0_42_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp41_142
    sens.P[2] = POcp41_242
    sens.P[3] = POcp41_342
    sens.R[1,1] = ROcp41_141
    sens.R[1,2] = ROcp41_241
    sens.R[1,3] = ROcp41_341
    sens.R[2,1] = ROcp41_442
    sens.R[2,2] = ROcp41_542
    sens.R[2,3] = ROcp41_642
    sens.R[3,1] = ROcp41_742
    sens.R[3,2] = ROcp41_842
    sens.R[3,3] = ROcp41_942
    sens.V[1] = VIcp41_142
    sens.V[2] = VIcp41_242
    sens.V[3] = VIcp41_342
    sens.OM[1] = OMcp41_142
    sens.OM[2] = OMcp41_242
    sens.OM[3] = OMcp41_342
    sens.A[1] = ACcp41_142
    sens.A[2] = ACcp41_242
    sens.A[3] = ACcp41_342
    sens.OMP[1] = OPcp41_142
    sens.OMP[2] = OPcp41_242
    sens.OMP[3] = OPcp41_342
 
# 
  elif(isens==43): 


# = = Block_1_0_0_43_0_1 = = 
 
# Sensor Kinematics 


    ROcp42_15 = C4*C5
    ROcp42_25 = S4*C5
    ROcp42_75 = C4*S5
    ROcp42_85 = S4*S5
    ROcp42_46 = ROcp42_75*S6-S4*C6
    ROcp42_56 = ROcp42_85*S6+C4*C6
    ROcp42_76 = ROcp42_75*C6+S4*S6
    ROcp42_86 = ROcp42_85*C6-C4*S6
    OMcp42_15 = -qd[5]*S4
    OMcp42_25 = qd[5]*C4
    OMcp42_16 = OMcp42_15+ROcp42_15*qd[6]
    OMcp42_26 = OMcp42_25+ROcp42_25*qd[6]
    OMcp42_36 = qd[4]-qd[6]*S5
    OPcp42_16 = ROcp42_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp42_25*S5+ROcp42_25*qd[4])
    OPcp42_26 = ROcp42_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp42_15*S5+ROcp42_15*qd[4])
    OPcp42_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_43_0_15 = = 
 
# Sensor Kinematics 


    ROcp42_440 = ROcp42_46*C40+ROcp42_76*S40
    ROcp42_540 = ROcp42_56*C40+ROcp42_86*S40
    ROcp42_640 = S40p6*C5
    ROcp42_740 = -(ROcp42_46*S40-ROcp42_76*C40)
    ROcp42_840 = -(ROcp42_56*S40-ROcp42_86*C40)
    ROcp42_940 = C40p6*C5
    ROcp42_141 = ROcp42_15*C41+ROcp42_440*S41
    ROcp42_241 = ROcp42_25*C41+ROcp42_540*S41
    ROcp42_341 = ROcp42_640*S41-C41*S5
    ROcp42_441 = -(ROcp42_15*S41-ROcp42_440*C41)
    ROcp42_541 = -(ROcp42_25*S41-ROcp42_540*C41)
    ROcp42_641 = ROcp42_640*C41+S41*S5
    ROcp42_442 = ROcp42_441*C42+ROcp42_740*S42
    ROcp42_542 = ROcp42_541*C42+ROcp42_840*S42
    ROcp42_642 = ROcp42_641*C42+ROcp42_940*S42
    ROcp42_742 = -(ROcp42_441*S42-ROcp42_740*C42)
    ROcp42_842 = -(ROcp42_541*S42-ROcp42_840*C42)
    ROcp42_942 = -(ROcp42_641*S42-ROcp42_940*C42)
    ROcp42_143 = ROcp42_141*C43-ROcp42_742*S43
    ROcp42_243 = ROcp42_241*C43-ROcp42_842*S43
    ROcp42_343 = ROcp42_341*C43-ROcp42_942*S43
    ROcp42_743 = ROcp42_141*S43+ROcp42_742*C43
    ROcp42_843 = ROcp42_241*S43+ROcp42_842*C43
    ROcp42_943 = ROcp42_341*S43+ROcp42_942*C43
    RLcp42_140 = ROcp42_15*s.dpt[1,12]+ROcp42_46*s.dpt[2,12]
    RLcp42_240 = ROcp42_25*s.dpt[1,12]+ROcp42_56*s.dpt[2,12]
    RLcp42_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp42_140 = OMcp42_16+ROcp42_15*qd[40]
    OMcp42_240 = OMcp42_26+ROcp42_25*qd[40]
    OMcp42_340 = OMcp42_36-qd[40]*S5
    ORcp42_140 = OMcp42_26*RLcp42_340-OMcp42_36*RLcp42_240
    ORcp42_240 = -(OMcp42_16*RLcp42_340-OMcp42_36*RLcp42_140)
    ORcp42_340 = OMcp42_16*RLcp42_240-OMcp42_26*RLcp42_140
    OMcp42_141 = OMcp42_140+ROcp42_740*qd[41]
    OMcp42_241 = OMcp42_240+ROcp42_840*qd[41]
    OMcp42_341 = OMcp42_340+ROcp42_940*qd[41]
    OPcp42_141 = OPcp42_16+ROcp42_15*qdd[40]+ROcp42_740*qdd[41]-qd[40]*(OMcp42_26*S5+OMcp42_36*ROcp42_25)+qd[41]*(\
   OMcp42_240*ROcp42_940-OMcp42_340*ROcp42_840)
    OPcp42_241 = OPcp42_26+ROcp42_25*qdd[40]+ROcp42_840*qdd[41]+qd[40]*(OMcp42_16*S5+OMcp42_36*ROcp42_15)-qd[41]*(\
   OMcp42_140*ROcp42_940-OMcp42_340*ROcp42_740)
    OPcp42_341 = OPcp42_36+ROcp42_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp42_16*ROcp42_25-OMcp42_26*ROcp42_15)+qd[41]*(\
   OMcp42_140*ROcp42_840-OMcp42_240*ROcp42_740)
    RLcp42_142 = ROcp42_441*s.dpt[2,42]
    RLcp42_242 = ROcp42_541*s.dpt[2,42]
    RLcp42_342 = ROcp42_641*s.dpt[2,42]
    POcp42_142 = RLcp42_140+RLcp42_142+q[1]
    POcp42_242 = RLcp42_240+RLcp42_242+q[2]
    POcp42_342 = RLcp42_340+RLcp42_342+q[3]
    OMcp42_142 = OMcp42_141+ROcp42_141*qd[42]
    OMcp42_242 = OMcp42_241+ROcp42_241*qd[42]
    OMcp42_342 = OMcp42_341+ROcp42_341*qd[42]
    ORcp42_142 = OMcp42_241*RLcp42_342-OMcp42_341*RLcp42_242
    ORcp42_242 = -(OMcp42_141*RLcp42_342-OMcp42_341*RLcp42_142)
    ORcp42_342 = OMcp42_141*RLcp42_242-OMcp42_241*RLcp42_142
    VIcp42_142 = ORcp42_140+ORcp42_142+qd[1]
    VIcp42_242 = ORcp42_240+ORcp42_242+qd[2]
    VIcp42_342 = ORcp42_340+ORcp42_342+qd[3]
    ACcp42_142 = qdd[1]+OMcp42_241*ORcp42_342+OMcp42_26*ORcp42_340-OMcp42_341*ORcp42_242-OMcp42_36*ORcp42_240+OPcp42_241*\
   RLcp42_342+OPcp42_26*RLcp42_340-OPcp42_341*RLcp42_242-OPcp42_36*RLcp42_240
    ACcp42_242 = qdd[2]-OMcp42_141*ORcp42_342-OMcp42_16*ORcp42_340+OMcp42_341*ORcp42_142+OMcp42_36*ORcp42_140-OPcp42_141*\
   RLcp42_342-OPcp42_16*RLcp42_340+OPcp42_341*RLcp42_142+OPcp42_36*RLcp42_140
    ACcp42_342 = qdd[3]+OMcp42_141*ORcp42_242+OMcp42_16*ORcp42_240-OMcp42_241*ORcp42_142-OMcp42_26*ORcp42_140+OPcp42_141*\
   RLcp42_242+OPcp42_16*RLcp42_240-OPcp42_241*RLcp42_142-OPcp42_26*RLcp42_140
    OMcp42_143 = OMcp42_142+ROcp42_442*qd[43]
    OMcp42_243 = OMcp42_242+ROcp42_542*qd[43]
    OMcp42_343 = OMcp42_342+ROcp42_642*qd[43]
    OPcp42_143 = OPcp42_141+ROcp42_141*qdd[42]+ROcp42_442*qdd[43]+qd[42]*(OMcp42_241*ROcp42_341-OMcp42_341*ROcp42_241)+\
   qd[43]*(OMcp42_242*ROcp42_642-OMcp42_342*ROcp42_542)
    OPcp42_243 = OPcp42_241+ROcp42_241*qdd[42]+ROcp42_542*qdd[43]-qd[42]*(OMcp42_141*ROcp42_341-OMcp42_341*ROcp42_141)-\
   qd[43]*(OMcp42_142*ROcp42_642-OMcp42_342*ROcp42_442)
    OPcp42_343 = OPcp42_341+ROcp42_341*qdd[42]+ROcp42_642*qdd[43]+qd[42]*(OMcp42_141*ROcp42_241-OMcp42_241*ROcp42_141)+\
   qd[43]*(OMcp42_142*ROcp42_542-OMcp42_242*ROcp42_442)

# = = Block_1_0_0_43_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp42_142
    sens.P[2] = POcp42_242
    sens.P[3] = POcp42_342
    sens.R[1,1] = ROcp42_143
    sens.R[1,2] = ROcp42_243
    sens.R[1,3] = ROcp42_343
    sens.R[2,1] = ROcp42_442
    sens.R[2,2] = ROcp42_542
    sens.R[2,3] = ROcp42_642
    sens.R[3,1] = ROcp42_743
    sens.R[3,2] = ROcp42_843
    sens.R[3,3] = ROcp42_943
    sens.V[1] = VIcp42_142
    sens.V[2] = VIcp42_242
    sens.V[3] = VIcp42_342
    sens.OM[1] = OMcp42_143
    sens.OM[2] = OMcp42_243
    sens.OM[3] = OMcp42_343
    sens.A[1] = ACcp42_142
    sens.A[2] = ACcp42_242
    sens.A[3] = ACcp42_342
    sens.OMP[1] = OPcp42_143
    sens.OMP[2] = OPcp42_243
    sens.OMP[3] = OPcp42_343
 
# 
  elif(isens==44): 


# = = Block_1_0_0_44_0_1 = = 
 
# Sensor Kinematics 


    ROcp43_15 = C4*C5
    ROcp43_25 = S4*C5
    ROcp43_75 = C4*S5
    ROcp43_85 = S4*S5
    ROcp43_46 = ROcp43_75*S6-S4*C6
    ROcp43_56 = ROcp43_85*S6+C4*C6
    ROcp43_76 = ROcp43_75*C6+S4*S6
    ROcp43_86 = ROcp43_85*C6-C4*S6
    OMcp43_15 = -qd[5]*S4
    OMcp43_25 = qd[5]*C4
    OMcp43_16 = OMcp43_15+ROcp43_15*qd[6]
    OMcp43_26 = OMcp43_25+ROcp43_25*qd[6]
    OMcp43_36 = qd[4]-qd[6]*S5
    OPcp43_16 = ROcp43_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp43_25*S5+ROcp43_25*qd[4])
    OPcp43_26 = ROcp43_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp43_15*S5+ROcp43_15*qd[4])
    OPcp43_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_44_0_15 = = 
 
# Sensor Kinematics 


    ROcp43_440 = ROcp43_46*C40+ROcp43_76*S40
    ROcp43_540 = ROcp43_56*C40+ROcp43_86*S40
    ROcp43_640 = S40p6*C5
    ROcp43_740 = -(ROcp43_46*S40-ROcp43_76*C40)
    ROcp43_840 = -(ROcp43_56*S40-ROcp43_86*C40)
    ROcp43_940 = C40p6*C5
    ROcp43_141 = ROcp43_15*C41+ROcp43_440*S41
    ROcp43_241 = ROcp43_25*C41+ROcp43_540*S41
    ROcp43_341 = ROcp43_640*S41-C41*S5
    ROcp43_441 = -(ROcp43_15*S41-ROcp43_440*C41)
    ROcp43_541 = -(ROcp43_25*S41-ROcp43_540*C41)
    ROcp43_641 = ROcp43_640*C41+S41*S5
    ROcp43_442 = ROcp43_441*C42+ROcp43_740*S42
    ROcp43_542 = ROcp43_541*C42+ROcp43_840*S42
    ROcp43_642 = ROcp43_641*C42+ROcp43_940*S42
    ROcp43_742 = -(ROcp43_441*S42-ROcp43_740*C42)
    ROcp43_842 = -(ROcp43_541*S42-ROcp43_840*C42)
    ROcp43_942 = -(ROcp43_641*S42-ROcp43_940*C42)
    ROcp43_143 = ROcp43_141*C43-ROcp43_742*S43
    ROcp43_243 = ROcp43_241*C43-ROcp43_842*S43
    ROcp43_343 = ROcp43_341*C43-ROcp43_942*S43
    ROcp43_743 = ROcp43_141*S43+ROcp43_742*C43
    ROcp43_843 = ROcp43_241*S43+ROcp43_842*C43
    ROcp43_943 = ROcp43_341*S43+ROcp43_942*C43
    ROcp43_144 = ROcp43_143*C44+ROcp43_442*S44
    ROcp43_244 = ROcp43_243*C44+ROcp43_542*S44
    ROcp43_344 = ROcp43_343*C44+ROcp43_642*S44
    ROcp43_444 = -(ROcp43_143*S44-ROcp43_442*C44)
    ROcp43_544 = -(ROcp43_243*S44-ROcp43_542*C44)
    ROcp43_644 = -(ROcp43_343*S44-ROcp43_642*C44)
    RLcp43_140 = ROcp43_15*s.dpt[1,12]+ROcp43_46*s.dpt[2,12]
    RLcp43_240 = ROcp43_25*s.dpt[1,12]+ROcp43_56*s.dpt[2,12]
    RLcp43_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp43_140 = OMcp43_16+ROcp43_15*qd[40]
    OMcp43_240 = OMcp43_26+ROcp43_25*qd[40]
    OMcp43_340 = OMcp43_36-qd[40]*S5
    ORcp43_140 = OMcp43_26*RLcp43_340-OMcp43_36*RLcp43_240
    ORcp43_240 = -(OMcp43_16*RLcp43_340-OMcp43_36*RLcp43_140)
    ORcp43_340 = OMcp43_16*RLcp43_240-OMcp43_26*RLcp43_140
    OMcp43_141 = OMcp43_140+ROcp43_740*qd[41]
    OMcp43_241 = OMcp43_240+ROcp43_840*qd[41]
    OMcp43_341 = OMcp43_340+ROcp43_940*qd[41]
    OPcp43_141 = OPcp43_16+ROcp43_15*qdd[40]+ROcp43_740*qdd[41]-qd[40]*(OMcp43_26*S5+OMcp43_36*ROcp43_25)+qd[41]*(\
   OMcp43_240*ROcp43_940-OMcp43_340*ROcp43_840)
    OPcp43_241 = OPcp43_26+ROcp43_25*qdd[40]+ROcp43_840*qdd[41]+qd[40]*(OMcp43_16*S5+OMcp43_36*ROcp43_15)-qd[41]*(\
   OMcp43_140*ROcp43_940-OMcp43_340*ROcp43_740)
    OPcp43_341 = OPcp43_36+ROcp43_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp43_16*ROcp43_25-OMcp43_26*ROcp43_15)+qd[41]*(\
   OMcp43_140*ROcp43_840-OMcp43_240*ROcp43_740)
    RLcp43_142 = ROcp43_441*s.dpt[2,42]
    RLcp43_242 = ROcp43_541*s.dpt[2,42]
    RLcp43_342 = ROcp43_641*s.dpt[2,42]
    POcp43_142 = RLcp43_140+RLcp43_142+q[1]
    POcp43_242 = RLcp43_240+RLcp43_242+q[2]
    POcp43_342 = RLcp43_340+RLcp43_342+q[3]
    OMcp43_142 = OMcp43_141+ROcp43_141*qd[42]
    OMcp43_242 = OMcp43_241+ROcp43_241*qd[42]
    OMcp43_342 = OMcp43_341+ROcp43_341*qd[42]
    ORcp43_142 = OMcp43_241*RLcp43_342-OMcp43_341*RLcp43_242
    ORcp43_242 = -(OMcp43_141*RLcp43_342-OMcp43_341*RLcp43_142)
    ORcp43_342 = OMcp43_141*RLcp43_242-OMcp43_241*RLcp43_142
    VIcp43_142 = ORcp43_140+ORcp43_142+qd[1]
    VIcp43_242 = ORcp43_240+ORcp43_242+qd[2]
    VIcp43_342 = ORcp43_340+ORcp43_342+qd[3]
    ACcp43_142 = qdd[1]+OMcp43_241*ORcp43_342+OMcp43_26*ORcp43_340-OMcp43_341*ORcp43_242-OMcp43_36*ORcp43_240+OPcp43_241*\
   RLcp43_342+OPcp43_26*RLcp43_340-OPcp43_341*RLcp43_242-OPcp43_36*RLcp43_240
    ACcp43_242 = qdd[2]-OMcp43_141*ORcp43_342-OMcp43_16*ORcp43_340+OMcp43_341*ORcp43_142+OMcp43_36*ORcp43_140-OPcp43_141*\
   RLcp43_342-OPcp43_16*RLcp43_340+OPcp43_341*RLcp43_142+OPcp43_36*RLcp43_140
    ACcp43_342 = qdd[3]+OMcp43_141*ORcp43_242+OMcp43_16*ORcp43_240-OMcp43_241*ORcp43_142-OMcp43_26*ORcp43_140+OPcp43_141*\
   RLcp43_242+OPcp43_16*RLcp43_240-OPcp43_241*RLcp43_142-OPcp43_26*RLcp43_140
    OMcp43_143 = OMcp43_142+ROcp43_442*qd[43]
    OMcp43_243 = OMcp43_242+ROcp43_542*qd[43]
    OMcp43_343 = OMcp43_342+ROcp43_642*qd[43]
    OMcp43_144 = OMcp43_143+ROcp43_743*qd[44]
    OMcp43_244 = OMcp43_243+ROcp43_843*qd[44]
    OMcp43_344 = OMcp43_343+ROcp43_943*qd[44]
    OPcp43_144 = OPcp43_141+ROcp43_141*qdd[42]+ROcp43_442*qdd[43]+ROcp43_743*qdd[44]+qd[42]*(OMcp43_241*ROcp43_341-\
   OMcp43_341*ROcp43_241)+qd[43]*(OMcp43_242*ROcp43_642-OMcp43_342*ROcp43_542)+qd[44]*(OMcp43_243*ROcp43_943-OMcp43_343*\
   ROcp43_843)
    OPcp43_244 = OPcp43_241+ROcp43_241*qdd[42]+ROcp43_542*qdd[43]+ROcp43_843*qdd[44]-qd[42]*(OMcp43_141*ROcp43_341-\
   OMcp43_341*ROcp43_141)-qd[43]*(OMcp43_142*ROcp43_642-OMcp43_342*ROcp43_442)-qd[44]*(OMcp43_143*ROcp43_943-OMcp43_343*\
   ROcp43_743)
    OPcp43_344 = OPcp43_341+ROcp43_341*qdd[42]+ROcp43_642*qdd[43]+ROcp43_943*qdd[44]+qd[42]*(OMcp43_141*ROcp43_241-\
   OMcp43_241*ROcp43_141)+qd[43]*(OMcp43_142*ROcp43_542-OMcp43_242*ROcp43_442)+qd[44]*(OMcp43_143*ROcp43_843-OMcp43_243*\
   ROcp43_743)

# = = Block_1_0_0_44_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp43_142
    sens.P[2] = POcp43_242
    sens.P[3] = POcp43_342
    sens.R[1,1] = ROcp43_144
    sens.R[1,2] = ROcp43_244
    sens.R[1,3] = ROcp43_344
    sens.R[2,1] = ROcp43_444
    sens.R[2,2] = ROcp43_544
    sens.R[2,3] = ROcp43_644
    sens.R[3,1] = ROcp43_743
    sens.R[3,2] = ROcp43_843
    sens.R[3,3] = ROcp43_943
    sens.V[1] = VIcp43_142
    sens.V[2] = VIcp43_242
    sens.V[3] = VIcp43_342
    sens.OM[1] = OMcp43_144
    sens.OM[2] = OMcp43_244
    sens.OM[3] = OMcp43_344
    sens.A[1] = ACcp43_142
    sens.A[2] = ACcp43_242
    sens.A[3] = ACcp43_342
    sens.OMP[1] = OPcp43_144
    sens.OMP[2] = OPcp43_244
    sens.OMP[3] = OPcp43_344
 
# 
  elif(isens==45): 


# = = Block_1_0_0_45_0_1 = = 
 
# Sensor Kinematics 


    ROcp44_15 = C4*C5
    ROcp44_25 = S4*C5
    ROcp44_75 = C4*S5
    ROcp44_85 = S4*S5
    ROcp44_46 = ROcp44_75*S6-S4*C6
    ROcp44_56 = ROcp44_85*S6+C4*C6
    ROcp44_76 = ROcp44_75*C6+S4*S6
    ROcp44_86 = ROcp44_85*C6-C4*S6
    OMcp44_15 = -qd[5]*S4
    OMcp44_25 = qd[5]*C4
    OMcp44_16 = OMcp44_15+ROcp44_15*qd[6]
    OMcp44_26 = OMcp44_25+ROcp44_25*qd[6]
    OMcp44_36 = qd[4]-qd[6]*S5
    OPcp44_16 = ROcp44_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp44_25*S5+ROcp44_25*qd[4])
    OPcp44_26 = ROcp44_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp44_15*S5+ROcp44_15*qd[4])
    OPcp44_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_45_0_15 = = 
 
# Sensor Kinematics 


    ROcp44_440 = ROcp44_46*C40+ROcp44_76*S40
    ROcp44_540 = ROcp44_56*C40+ROcp44_86*S40
    ROcp44_640 = S40p6*C5
    ROcp44_740 = -(ROcp44_46*S40-ROcp44_76*C40)
    ROcp44_840 = -(ROcp44_56*S40-ROcp44_86*C40)
    ROcp44_940 = C40p6*C5
    ROcp44_141 = ROcp44_15*C41+ROcp44_440*S41
    ROcp44_241 = ROcp44_25*C41+ROcp44_540*S41
    ROcp44_341 = ROcp44_640*S41-C41*S5
    ROcp44_441 = -(ROcp44_15*S41-ROcp44_440*C41)
    ROcp44_541 = -(ROcp44_25*S41-ROcp44_540*C41)
    ROcp44_641 = ROcp44_640*C41+S41*S5
    ROcp44_442 = ROcp44_441*C42+ROcp44_740*S42
    ROcp44_542 = ROcp44_541*C42+ROcp44_840*S42
    ROcp44_642 = ROcp44_641*C42+ROcp44_940*S42
    ROcp44_742 = -(ROcp44_441*S42-ROcp44_740*C42)
    ROcp44_842 = -(ROcp44_541*S42-ROcp44_840*C42)
    ROcp44_942 = -(ROcp44_641*S42-ROcp44_940*C42)
    ROcp44_143 = ROcp44_141*C43-ROcp44_742*S43
    ROcp44_243 = ROcp44_241*C43-ROcp44_842*S43
    ROcp44_343 = ROcp44_341*C43-ROcp44_942*S43
    ROcp44_743 = ROcp44_141*S43+ROcp44_742*C43
    ROcp44_843 = ROcp44_241*S43+ROcp44_842*C43
    ROcp44_943 = ROcp44_341*S43+ROcp44_942*C43
    ROcp44_144 = ROcp44_143*C44+ROcp44_442*S44
    ROcp44_244 = ROcp44_243*C44+ROcp44_542*S44
    ROcp44_344 = ROcp44_343*C44+ROcp44_642*S44
    ROcp44_444 = -(ROcp44_143*S44-ROcp44_442*C44)
    ROcp44_544 = -(ROcp44_243*S44-ROcp44_542*C44)
    ROcp44_644 = -(ROcp44_343*S44-ROcp44_642*C44)
    RLcp44_140 = ROcp44_15*s.dpt[1,12]+ROcp44_46*s.dpt[2,12]
    RLcp44_240 = ROcp44_25*s.dpt[1,12]+ROcp44_56*s.dpt[2,12]
    RLcp44_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp44_140 = OMcp44_16+ROcp44_15*qd[40]
    OMcp44_240 = OMcp44_26+ROcp44_25*qd[40]
    OMcp44_340 = OMcp44_36-qd[40]*S5
    ORcp44_140 = OMcp44_26*RLcp44_340-OMcp44_36*RLcp44_240
    ORcp44_240 = -(OMcp44_16*RLcp44_340-OMcp44_36*RLcp44_140)
    ORcp44_340 = OMcp44_16*RLcp44_240-OMcp44_26*RLcp44_140
    OMcp44_141 = OMcp44_140+ROcp44_740*qd[41]
    OMcp44_241 = OMcp44_240+ROcp44_840*qd[41]
    OMcp44_341 = OMcp44_340+ROcp44_940*qd[41]
    OPcp44_141 = OPcp44_16+ROcp44_15*qdd[40]+ROcp44_740*qdd[41]-qd[40]*(OMcp44_26*S5+OMcp44_36*ROcp44_25)+qd[41]*(\
   OMcp44_240*ROcp44_940-OMcp44_340*ROcp44_840)
    OPcp44_241 = OPcp44_26+ROcp44_25*qdd[40]+ROcp44_840*qdd[41]+qd[40]*(OMcp44_16*S5+OMcp44_36*ROcp44_15)-qd[41]*(\
   OMcp44_140*ROcp44_940-OMcp44_340*ROcp44_740)
    OPcp44_341 = OPcp44_36+ROcp44_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp44_16*ROcp44_25-OMcp44_26*ROcp44_15)+qd[41]*(\
   OMcp44_140*ROcp44_840-OMcp44_240*ROcp44_740)
    RLcp44_142 = ROcp44_441*s.dpt[2,42]
    RLcp44_242 = ROcp44_541*s.dpt[2,42]
    RLcp44_342 = ROcp44_641*s.dpt[2,42]
    OMcp44_142 = OMcp44_141+ROcp44_141*qd[42]
    OMcp44_242 = OMcp44_241+ROcp44_241*qd[42]
    OMcp44_342 = OMcp44_341+ROcp44_341*qd[42]
    ORcp44_142 = OMcp44_241*RLcp44_342-OMcp44_341*RLcp44_242
    ORcp44_242 = -(OMcp44_141*RLcp44_342-OMcp44_341*RLcp44_142)
    ORcp44_342 = OMcp44_141*RLcp44_242-OMcp44_241*RLcp44_142
    OMcp44_143 = OMcp44_142+ROcp44_442*qd[43]
    OMcp44_243 = OMcp44_242+ROcp44_542*qd[43]
    OMcp44_343 = OMcp44_342+ROcp44_642*qd[43]
    OMcp44_144 = OMcp44_143+ROcp44_743*qd[44]
    OMcp44_244 = OMcp44_243+ROcp44_843*qd[44]
    OMcp44_344 = OMcp44_343+ROcp44_943*qd[44]
    OPcp44_144 = OPcp44_141+ROcp44_141*qdd[42]+ROcp44_442*qdd[43]+ROcp44_743*qdd[44]+qd[42]*(OMcp44_241*ROcp44_341-\
   OMcp44_341*ROcp44_241)+qd[43]*(OMcp44_242*ROcp44_642-OMcp44_342*ROcp44_542)+qd[44]*(OMcp44_243*ROcp44_943-OMcp44_343*\
   ROcp44_843)
    OPcp44_244 = OPcp44_241+ROcp44_241*qdd[42]+ROcp44_542*qdd[43]+ROcp44_843*qdd[44]-qd[42]*(OMcp44_141*ROcp44_341-\
   OMcp44_341*ROcp44_141)-qd[43]*(OMcp44_142*ROcp44_642-OMcp44_342*ROcp44_442)-qd[44]*(OMcp44_143*ROcp44_943-OMcp44_343*\
   ROcp44_743)
    OPcp44_344 = OPcp44_341+ROcp44_341*qdd[42]+ROcp44_642*qdd[43]+ROcp44_943*qdd[44]+qd[42]*(OMcp44_141*ROcp44_241-\
   OMcp44_241*ROcp44_141)+qd[43]*(OMcp44_142*ROcp44_542-OMcp44_242*ROcp44_442)+qd[44]*(OMcp44_143*ROcp44_843-OMcp44_243*\
   ROcp44_743)

# = = Block_1_0_0_45_0_16 = = 
 
# Sensor Kinematics 


    ROcp44_445 = ROcp44_444*C45+ROcp44_743*S45
    ROcp44_545 = ROcp44_544*C45+ROcp44_843*S45
    ROcp44_645 = ROcp44_644*C45+ROcp44_943*S45
    ROcp44_745 = -(ROcp44_444*S45-ROcp44_743*C45)
    ROcp44_845 = -(ROcp44_544*S45-ROcp44_843*C45)
    ROcp44_945 = -(ROcp44_644*S45-ROcp44_943*C45)
    RLcp44_145 = ROcp44_444*s.dpt[2,45]+ROcp44_743*s.dpt[3,45]
    RLcp44_245 = ROcp44_544*s.dpt[2,45]+ROcp44_843*s.dpt[3,45]
    RLcp44_345 = ROcp44_644*s.dpt[2,45]+ROcp44_943*s.dpt[3,45]
    POcp44_145 = RLcp44_140+RLcp44_142+RLcp44_145+q[1]
    POcp44_245 = RLcp44_240+RLcp44_242+RLcp44_245+q[2]
    POcp44_345 = RLcp44_340+RLcp44_342+RLcp44_345+q[3]
    OMcp44_145 = OMcp44_144+ROcp44_144*qd[45]
    OMcp44_245 = OMcp44_244+ROcp44_244*qd[45]
    OMcp44_345 = OMcp44_344+ROcp44_344*qd[45]
    ORcp44_145 = OMcp44_244*RLcp44_345-OMcp44_344*RLcp44_245
    ORcp44_245 = -(OMcp44_144*RLcp44_345-OMcp44_344*RLcp44_145)
    ORcp44_345 = OMcp44_144*RLcp44_245-OMcp44_244*RLcp44_145
    VIcp44_145 = ORcp44_140+ORcp44_142+ORcp44_145+qd[1]
    VIcp44_245 = ORcp44_240+ORcp44_242+ORcp44_245+qd[2]
    VIcp44_345 = ORcp44_340+ORcp44_342+ORcp44_345+qd[3]
    OPcp44_145 = OPcp44_144+ROcp44_144*qdd[45]+qd[45]*(OMcp44_244*ROcp44_344-OMcp44_344*ROcp44_244)
    OPcp44_245 = OPcp44_244+ROcp44_244*qdd[45]-qd[45]*(OMcp44_144*ROcp44_344-OMcp44_344*ROcp44_144)
    OPcp44_345 = OPcp44_344+ROcp44_344*qdd[45]+qd[45]*(OMcp44_144*ROcp44_244-OMcp44_244*ROcp44_144)
    ACcp44_145 = qdd[1]+OMcp44_241*ORcp44_342+OMcp44_244*ORcp44_345+OMcp44_26*ORcp44_340-OMcp44_341*ORcp44_242-OMcp44_344*\
   ORcp44_245-OMcp44_36*ORcp44_240+OPcp44_241*RLcp44_342+OPcp44_244*RLcp44_345+OPcp44_26*RLcp44_340-OPcp44_341*RLcp44_242-\
   OPcp44_344*RLcp44_245-OPcp44_36*RLcp44_240
    ACcp44_245 = qdd[2]-OMcp44_141*ORcp44_342-OMcp44_144*ORcp44_345-OMcp44_16*ORcp44_340+OMcp44_341*ORcp44_142+OMcp44_344*\
   ORcp44_145+OMcp44_36*ORcp44_140-OPcp44_141*RLcp44_342-OPcp44_144*RLcp44_345-OPcp44_16*RLcp44_340+OPcp44_341*RLcp44_142+\
   OPcp44_344*RLcp44_145+OPcp44_36*RLcp44_140
    ACcp44_345 = qdd[3]+OMcp44_141*ORcp44_242+OMcp44_144*ORcp44_245+OMcp44_16*ORcp44_240-OMcp44_241*ORcp44_142-OMcp44_244*\
   ORcp44_145-OMcp44_26*ORcp44_140+OPcp44_141*RLcp44_242+OPcp44_144*RLcp44_245+OPcp44_16*RLcp44_240-OPcp44_241*RLcp44_142-\
   OPcp44_244*RLcp44_145-OPcp44_26*RLcp44_140

# = = Block_1_0_0_45_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp44_145
    sens.P[2] = POcp44_245
    sens.P[3] = POcp44_345
    sens.R[1,1] = ROcp44_144
    sens.R[1,2] = ROcp44_244
    sens.R[1,3] = ROcp44_344
    sens.R[2,1] = ROcp44_445
    sens.R[2,2] = ROcp44_545
    sens.R[2,3] = ROcp44_645
    sens.R[3,1] = ROcp44_745
    sens.R[3,2] = ROcp44_845
    sens.R[3,3] = ROcp44_945
    sens.V[1] = VIcp44_145
    sens.V[2] = VIcp44_245
    sens.V[3] = VIcp44_345
    sens.OM[1] = OMcp44_145
    sens.OM[2] = OMcp44_245
    sens.OM[3] = OMcp44_345
    sens.A[1] = ACcp44_145
    sens.A[2] = ACcp44_245
    sens.A[3] = ACcp44_345
    sens.OMP[1] = OPcp44_145
    sens.OMP[2] = OPcp44_245
    sens.OMP[3] = OPcp44_345
 
# 
  elif(isens==46): 


# = = Block_1_0_0_46_0_1 = = 
 
# Sensor Kinematics 


    ROcp45_15 = C4*C5
    ROcp45_25 = S4*C5
    ROcp45_75 = C4*S5
    ROcp45_85 = S4*S5
    ROcp45_46 = ROcp45_75*S6-S4*C6
    ROcp45_56 = ROcp45_85*S6+C4*C6
    ROcp45_76 = ROcp45_75*C6+S4*S6
    ROcp45_86 = ROcp45_85*C6-C4*S6
    OMcp45_15 = -qd[5]*S4
    OMcp45_25 = qd[5]*C4
    OMcp45_16 = OMcp45_15+ROcp45_15*qd[6]
    OMcp45_26 = OMcp45_25+ROcp45_25*qd[6]
    OMcp45_36 = qd[4]-qd[6]*S5
    OPcp45_16 = ROcp45_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp45_25*S5+ROcp45_25*qd[4])
    OPcp45_26 = ROcp45_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp45_15*S5+ROcp45_15*qd[4])
    OPcp45_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_46_0_15 = = 
 
# Sensor Kinematics 


    ROcp45_440 = ROcp45_46*C40+ROcp45_76*S40
    ROcp45_540 = ROcp45_56*C40+ROcp45_86*S40
    ROcp45_640 = S40p6*C5
    ROcp45_740 = -(ROcp45_46*S40-ROcp45_76*C40)
    ROcp45_840 = -(ROcp45_56*S40-ROcp45_86*C40)
    ROcp45_940 = C40p6*C5
    ROcp45_141 = ROcp45_15*C41+ROcp45_440*S41
    ROcp45_241 = ROcp45_25*C41+ROcp45_540*S41
    ROcp45_341 = ROcp45_640*S41-C41*S5
    ROcp45_441 = -(ROcp45_15*S41-ROcp45_440*C41)
    ROcp45_541 = -(ROcp45_25*S41-ROcp45_540*C41)
    ROcp45_641 = ROcp45_640*C41+S41*S5
    ROcp45_442 = ROcp45_441*C42+ROcp45_740*S42
    ROcp45_542 = ROcp45_541*C42+ROcp45_840*S42
    ROcp45_642 = ROcp45_641*C42+ROcp45_940*S42
    ROcp45_742 = -(ROcp45_441*S42-ROcp45_740*C42)
    ROcp45_842 = -(ROcp45_541*S42-ROcp45_840*C42)
    ROcp45_942 = -(ROcp45_641*S42-ROcp45_940*C42)
    ROcp45_143 = ROcp45_141*C43-ROcp45_742*S43
    ROcp45_243 = ROcp45_241*C43-ROcp45_842*S43
    ROcp45_343 = ROcp45_341*C43-ROcp45_942*S43
    ROcp45_743 = ROcp45_141*S43+ROcp45_742*C43
    ROcp45_843 = ROcp45_241*S43+ROcp45_842*C43
    ROcp45_943 = ROcp45_341*S43+ROcp45_942*C43
    ROcp45_144 = ROcp45_143*C44+ROcp45_442*S44
    ROcp45_244 = ROcp45_243*C44+ROcp45_542*S44
    ROcp45_344 = ROcp45_343*C44+ROcp45_642*S44
    ROcp45_444 = -(ROcp45_143*S44-ROcp45_442*C44)
    ROcp45_544 = -(ROcp45_243*S44-ROcp45_542*C44)
    ROcp45_644 = -(ROcp45_343*S44-ROcp45_642*C44)
    RLcp45_140 = ROcp45_15*s.dpt[1,12]+ROcp45_46*s.dpt[2,12]
    RLcp45_240 = ROcp45_25*s.dpt[1,12]+ROcp45_56*s.dpt[2,12]
    RLcp45_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp45_140 = OMcp45_16+ROcp45_15*qd[40]
    OMcp45_240 = OMcp45_26+ROcp45_25*qd[40]
    OMcp45_340 = OMcp45_36-qd[40]*S5
    ORcp45_140 = OMcp45_26*RLcp45_340-OMcp45_36*RLcp45_240
    ORcp45_240 = -(OMcp45_16*RLcp45_340-OMcp45_36*RLcp45_140)
    ORcp45_340 = OMcp45_16*RLcp45_240-OMcp45_26*RLcp45_140
    OMcp45_141 = OMcp45_140+ROcp45_740*qd[41]
    OMcp45_241 = OMcp45_240+ROcp45_840*qd[41]
    OMcp45_341 = OMcp45_340+ROcp45_940*qd[41]
    OPcp45_141 = OPcp45_16+ROcp45_15*qdd[40]+ROcp45_740*qdd[41]-qd[40]*(OMcp45_26*S5+OMcp45_36*ROcp45_25)+qd[41]*(\
   OMcp45_240*ROcp45_940-OMcp45_340*ROcp45_840)
    OPcp45_241 = OPcp45_26+ROcp45_25*qdd[40]+ROcp45_840*qdd[41]+qd[40]*(OMcp45_16*S5+OMcp45_36*ROcp45_15)-qd[41]*(\
   OMcp45_140*ROcp45_940-OMcp45_340*ROcp45_740)
    OPcp45_341 = OPcp45_36+ROcp45_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp45_16*ROcp45_25-OMcp45_26*ROcp45_15)+qd[41]*(\
   OMcp45_140*ROcp45_840-OMcp45_240*ROcp45_740)
    RLcp45_142 = ROcp45_441*s.dpt[2,42]
    RLcp45_242 = ROcp45_541*s.dpt[2,42]
    RLcp45_342 = ROcp45_641*s.dpt[2,42]
    OMcp45_142 = OMcp45_141+ROcp45_141*qd[42]
    OMcp45_242 = OMcp45_241+ROcp45_241*qd[42]
    OMcp45_342 = OMcp45_341+ROcp45_341*qd[42]
    ORcp45_142 = OMcp45_241*RLcp45_342-OMcp45_341*RLcp45_242
    ORcp45_242 = -(OMcp45_141*RLcp45_342-OMcp45_341*RLcp45_142)
    ORcp45_342 = OMcp45_141*RLcp45_242-OMcp45_241*RLcp45_142
    OMcp45_143 = OMcp45_142+ROcp45_442*qd[43]
    OMcp45_243 = OMcp45_242+ROcp45_542*qd[43]
    OMcp45_343 = OMcp45_342+ROcp45_642*qd[43]
    OMcp45_144 = OMcp45_143+ROcp45_743*qd[44]
    OMcp45_244 = OMcp45_243+ROcp45_843*qd[44]
    OMcp45_344 = OMcp45_343+ROcp45_943*qd[44]
    OPcp45_144 = OPcp45_141+ROcp45_141*qdd[42]+ROcp45_442*qdd[43]+ROcp45_743*qdd[44]+qd[42]*(OMcp45_241*ROcp45_341-\
   OMcp45_341*ROcp45_241)+qd[43]*(OMcp45_242*ROcp45_642-OMcp45_342*ROcp45_542)+qd[44]*(OMcp45_243*ROcp45_943-OMcp45_343*\
   ROcp45_843)
    OPcp45_244 = OPcp45_241+ROcp45_241*qdd[42]+ROcp45_542*qdd[43]+ROcp45_843*qdd[44]-qd[42]*(OMcp45_141*ROcp45_341-\
   OMcp45_341*ROcp45_141)-qd[43]*(OMcp45_142*ROcp45_642-OMcp45_342*ROcp45_442)-qd[44]*(OMcp45_143*ROcp45_943-OMcp45_343*\
   ROcp45_743)
    OPcp45_344 = OPcp45_341+ROcp45_341*qdd[42]+ROcp45_642*qdd[43]+ROcp45_943*qdd[44]+qd[42]*(OMcp45_141*ROcp45_241-\
   OMcp45_241*ROcp45_141)+qd[43]*(OMcp45_142*ROcp45_542-OMcp45_242*ROcp45_442)+qd[44]*(OMcp45_143*ROcp45_843-OMcp45_243*\
   ROcp45_743)

# = = Block_1_0_0_46_0_16 = = 
 
# Sensor Kinematics 


    ROcp45_445 = ROcp45_444*C45+ROcp45_743*S45
    ROcp45_545 = ROcp45_544*C45+ROcp45_843*S45
    ROcp45_645 = ROcp45_644*C45+ROcp45_943*S45
    ROcp45_745 = -(ROcp45_444*S45-ROcp45_743*C45)
    ROcp45_845 = -(ROcp45_544*S45-ROcp45_843*C45)
    ROcp45_945 = -(ROcp45_644*S45-ROcp45_943*C45)
    RLcp45_145 = ROcp45_444*s.dpt[2,45]+ROcp45_743*s.dpt[3,45]
    RLcp45_245 = ROcp45_544*s.dpt[2,45]+ROcp45_843*s.dpt[3,45]
    RLcp45_345 = ROcp45_644*s.dpt[2,45]+ROcp45_943*s.dpt[3,45]
    OMcp45_145 = OMcp45_144+ROcp45_144*qd[45]
    OMcp45_245 = OMcp45_244+ROcp45_244*qd[45]
    OMcp45_345 = OMcp45_344+ROcp45_344*qd[45]
    ORcp45_145 = OMcp45_244*RLcp45_345-OMcp45_344*RLcp45_245
    ORcp45_245 = -(OMcp45_144*RLcp45_345-OMcp45_344*RLcp45_145)
    ORcp45_345 = OMcp45_144*RLcp45_245-OMcp45_244*RLcp45_145
    OPcp45_145 = OPcp45_144+ROcp45_144*qdd[45]+qd[45]*(OMcp45_244*ROcp45_344-OMcp45_344*ROcp45_244)
    OPcp45_245 = OPcp45_244+ROcp45_244*qdd[45]-qd[45]*(OMcp45_144*ROcp45_344-OMcp45_344*ROcp45_144)
    OPcp45_345 = OPcp45_344+ROcp45_344*qdd[45]+qd[45]*(OMcp45_144*ROcp45_244-OMcp45_244*ROcp45_144)
    RLcp45_146 = ROcp45_745*q[46]
    RLcp45_246 = ROcp45_845*q[46]
    RLcp45_346 = ROcp45_945*q[46]
    POcp45_146 = RLcp45_140+RLcp45_142+RLcp45_145+RLcp45_146+q[1]
    POcp45_246 = RLcp45_240+RLcp45_242+RLcp45_245+RLcp45_246+q[2]
    POcp45_346 = RLcp45_340+RLcp45_342+RLcp45_345+RLcp45_346+q[3]
    ORcp45_146 = OMcp45_245*RLcp45_346-OMcp45_345*RLcp45_246
    ORcp45_246 = -(OMcp45_145*RLcp45_346-OMcp45_345*RLcp45_146)
    ORcp45_346 = OMcp45_145*RLcp45_246-OMcp45_245*RLcp45_146
    VIcp45_146 = ORcp45_140+ORcp45_142+ORcp45_145+ORcp45_146+qd[1]+ROcp45_745*qd[46]
    VIcp45_246 = ORcp45_240+ORcp45_242+ORcp45_245+ORcp45_246+qd[2]+ROcp45_845*qd[46]
    VIcp45_346 = ORcp45_340+ORcp45_342+ORcp45_345+ORcp45_346+qd[3]+ROcp45_945*qd[46]
    ACcp45_146 = qdd[1]+OMcp45_241*ORcp45_342+OMcp45_244*ORcp45_345+OMcp45_245*ORcp45_346+OMcp45_26*ORcp45_340-OMcp45_341*\
   ORcp45_242-OMcp45_344*ORcp45_245-OMcp45_345*ORcp45_246-OMcp45_36*ORcp45_240+OPcp45_241*RLcp45_342+OPcp45_244*RLcp45_345+\
   OPcp45_245*RLcp45_346+OPcp45_26*RLcp45_340-OPcp45_341*RLcp45_242-OPcp45_344*RLcp45_245-OPcp45_345*RLcp45_246-OPcp45_36*\
   RLcp45_240+ROcp45_745*qdd[46]+(2.0)*qd[46]*(OMcp45_245*ROcp45_945-OMcp45_345*ROcp45_845)
    ACcp45_246 = qdd[2]-OMcp45_141*ORcp45_342-OMcp45_144*ORcp45_345-OMcp45_145*ORcp45_346-OMcp45_16*ORcp45_340+OMcp45_341*\
   ORcp45_142+OMcp45_344*ORcp45_145+OMcp45_345*ORcp45_146+OMcp45_36*ORcp45_140-OPcp45_141*RLcp45_342-OPcp45_144*RLcp45_345-\
   OPcp45_145*RLcp45_346-OPcp45_16*RLcp45_340+OPcp45_341*RLcp45_142+OPcp45_344*RLcp45_145+OPcp45_345*RLcp45_146+OPcp45_36*\
   RLcp45_140+ROcp45_845*qdd[46]-(2.0)*qd[46]*(OMcp45_145*ROcp45_945-OMcp45_345*ROcp45_745)
    ACcp45_346 = qdd[3]+OMcp45_141*ORcp45_242+OMcp45_144*ORcp45_245+OMcp45_145*ORcp45_246+OMcp45_16*ORcp45_240-OMcp45_241*\
   ORcp45_142-OMcp45_244*ORcp45_145-OMcp45_245*ORcp45_146-OMcp45_26*ORcp45_140+OPcp45_141*RLcp45_242+OPcp45_144*RLcp45_245+\
   OPcp45_145*RLcp45_246+OPcp45_16*RLcp45_240-OPcp45_241*RLcp45_142-OPcp45_244*RLcp45_145-OPcp45_245*RLcp45_146-OPcp45_26*\
   RLcp45_140+ROcp45_945*qdd[46]+(2.0)*qd[46]*(OMcp45_145*ROcp45_845-OMcp45_245*ROcp45_745)

# = = Block_1_0_0_46_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp45_146
    sens.P[2] = POcp45_246
    sens.P[3] = POcp45_346
    sens.R[1,1] = ROcp45_144
    sens.R[1,2] = ROcp45_244
    sens.R[1,3] = ROcp45_344
    sens.R[2,1] = ROcp45_445
    sens.R[2,2] = ROcp45_545
    sens.R[2,3] = ROcp45_645
    sens.R[3,1] = ROcp45_745
    sens.R[3,2] = ROcp45_845
    sens.R[3,3] = ROcp45_945
    sens.V[1] = VIcp45_146
    sens.V[2] = VIcp45_246
    sens.V[3] = VIcp45_346
    sens.OM[1] = OMcp45_145
    sens.OM[2] = OMcp45_245
    sens.OM[3] = OMcp45_345
    sens.A[1] = ACcp45_146
    sens.A[2] = ACcp45_246
    sens.A[3] = ACcp45_346
    sens.OMP[1] = OPcp45_145
    sens.OMP[2] = OPcp45_245
    sens.OMP[3] = OPcp45_345
 
# 
  elif(isens==47): 


# = = Block_1_0_0_47_0_1 = = 
 
# Sensor Kinematics 


    ROcp46_15 = C4*C5
    ROcp46_25 = S4*C5
    ROcp46_75 = C4*S5
    ROcp46_85 = S4*S5
    ROcp46_46 = ROcp46_75*S6-S4*C6
    ROcp46_56 = ROcp46_85*S6+C4*C6
    ROcp46_76 = ROcp46_75*C6+S4*S6
    ROcp46_86 = ROcp46_85*C6-C4*S6
    OMcp46_15 = -qd[5]*S4
    OMcp46_25 = qd[5]*C4
    OMcp46_16 = OMcp46_15+ROcp46_15*qd[6]
    OMcp46_26 = OMcp46_25+ROcp46_25*qd[6]
    OMcp46_36 = qd[4]-qd[6]*S5
    OPcp46_16 = ROcp46_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp46_25*S5+ROcp46_25*qd[4])
    OPcp46_26 = ROcp46_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp46_15*S5+ROcp46_15*qd[4])
    OPcp46_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_47_0_15 = = 
 
# Sensor Kinematics 


    ROcp46_440 = ROcp46_46*C40+ROcp46_76*S40
    ROcp46_540 = ROcp46_56*C40+ROcp46_86*S40
    ROcp46_640 = S40p6*C5
    ROcp46_740 = -(ROcp46_46*S40-ROcp46_76*C40)
    ROcp46_840 = -(ROcp46_56*S40-ROcp46_86*C40)
    ROcp46_940 = C40p6*C5
    ROcp46_141 = ROcp46_15*C41+ROcp46_440*S41
    ROcp46_241 = ROcp46_25*C41+ROcp46_540*S41
    ROcp46_341 = ROcp46_640*S41-C41*S5
    ROcp46_441 = -(ROcp46_15*S41-ROcp46_440*C41)
    ROcp46_541 = -(ROcp46_25*S41-ROcp46_540*C41)
    ROcp46_641 = ROcp46_640*C41+S41*S5
    ROcp46_442 = ROcp46_441*C42+ROcp46_740*S42
    ROcp46_542 = ROcp46_541*C42+ROcp46_840*S42
    ROcp46_642 = ROcp46_641*C42+ROcp46_940*S42
    ROcp46_742 = -(ROcp46_441*S42-ROcp46_740*C42)
    ROcp46_842 = -(ROcp46_541*S42-ROcp46_840*C42)
    ROcp46_942 = -(ROcp46_641*S42-ROcp46_940*C42)
    ROcp46_143 = ROcp46_141*C43-ROcp46_742*S43
    ROcp46_243 = ROcp46_241*C43-ROcp46_842*S43
    ROcp46_343 = ROcp46_341*C43-ROcp46_942*S43
    ROcp46_743 = ROcp46_141*S43+ROcp46_742*C43
    ROcp46_843 = ROcp46_241*S43+ROcp46_842*C43
    ROcp46_943 = ROcp46_341*S43+ROcp46_942*C43
    ROcp46_144 = ROcp46_143*C44+ROcp46_442*S44
    ROcp46_244 = ROcp46_243*C44+ROcp46_542*S44
    ROcp46_344 = ROcp46_343*C44+ROcp46_642*S44
    ROcp46_444 = -(ROcp46_143*S44-ROcp46_442*C44)
    ROcp46_544 = -(ROcp46_243*S44-ROcp46_542*C44)
    ROcp46_644 = -(ROcp46_343*S44-ROcp46_642*C44)
    RLcp46_140 = ROcp46_15*s.dpt[1,12]+ROcp46_46*s.dpt[2,12]
    RLcp46_240 = ROcp46_25*s.dpt[1,12]+ROcp46_56*s.dpt[2,12]
    RLcp46_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp46_140 = OMcp46_16+ROcp46_15*qd[40]
    OMcp46_240 = OMcp46_26+ROcp46_25*qd[40]
    OMcp46_340 = OMcp46_36-qd[40]*S5
    ORcp46_140 = OMcp46_26*RLcp46_340-OMcp46_36*RLcp46_240
    ORcp46_240 = -(OMcp46_16*RLcp46_340-OMcp46_36*RLcp46_140)
    ORcp46_340 = OMcp46_16*RLcp46_240-OMcp46_26*RLcp46_140
    OMcp46_141 = OMcp46_140+ROcp46_740*qd[41]
    OMcp46_241 = OMcp46_240+ROcp46_840*qd[41]
    OMcp46_341 = OMcp46_340+ROcp46_940*qd[41]
    OPcp46_141 = OPcp46_16+ROcp46_15*qdd[40]+ROcp46_740*qdd[41]-qd[40]*(OMcp46_26*S5+OMcp46_36*ROcp46_25)+qd[41]*(\
   OMcp46_240*ROcp46_940-OMcp46_340*ROcp46_840)
    OPcp46_241 = OPcp46_26+ROcp46_25*qdd[40]+ROcp46_840*qdd[41]+qd[40]*(OMcp46_16*S5+OMcp46_36*ROcp46_15)-qd[41]*(\
   OMcp46_140*ROcp46_940-OMcp46_340*ROcp46_740)
    OPcp46_341 = OPcp46_36+ROcp46_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp46_16*ROcp46_25-OMcp46_26*ROcp46_15)+qd[41]*(\
   OMcp46_140*ROcp46_840-OMcp46_240*ROcp46_740)
    RLcp46_142 = ROcp46_441*s.dpt[2,42]
    RLcp46_242 = ROcp46_541*s.dpt[2,42]
    RLcp46_342 = ROcp46_641*s.dpt[2,42]
    OMcp46_142 = OMcp46_141+ROcp46_141*qd[42]
    OMcp46_242 = OMcp46_241+ROcp46_241*qd[42]
    OMcp46_342 = OMcp46_341+ROcp46_341*qd[42]
    ORcp46_142 = OMcp46_241*RLcp46_342-OMcp46_341*RLcp46_242
    ORcp46_242 = -(OMcp46_141*RLcp46_342-OMcp46_341*RLcp46_142)
    ORcp46_342 = OMcp46_141*RLcp46_242-OMcp46_241*RLcp46_142
    OMcp46_143 = OMcp46_142+ROcp46_442*qd[43]
    OMcp46_243 = OMcp46_242+ROcp46_542*qd[43]
    OMcp46_343 = OMcp46_342+ROcp46_642*qd[43]
    OMcp46_144 = OMcp46_143+ROcp46_743*qd[44]
    OMcp46_244 = OMcp46_243+ROcp46_843*qd[44]
    OMcp46_344 = OMcp46_343+ROcp46_943*qd[44]
    OPcp46_144 = OPcp46_141+ROcp46_141*qdd[42]+ROcp46_442*qdd[43]+ROcp46_743*qdd[44]+qd[42]*(OMcp46_241*ROcp46_341-\
   OMcp46_341*ROcp46_241)+qd[43]*(OMcp46_242*ROcp46_642-OMcp46_342*ROcp46_542)+qd[44]*(OMcp46_243*ROcp46_943-OMcp46_343*\
   ROcp46_843)
    OPcp46_244 = OPcp46_241+ROcp46_241*qdd[42]+ROcp46_542*qdd[43]+ROcp46_843*qdd[44]-qd[42]*(OMcp46_141*ROcp46_341-\
   OMcp46_341*ROcp46_141)-qd[43]*(OMcp46_142*ROcp46_642-OMcp46_342*ROcp46_442)-qd[44]*(OMcp46_143*ROcp46_943-OMcp46_343*\
   ROcp46_743)
    OPcp46_344 = OPcp46_341+ROcp46_341*qdd[42]+ROcp46_642*qdd[43]+ROcp46_943*qdd[44]+qd[42]*(OMcp46_141*ROcp46_241-\
   OMcp46_241*ROcp46_141)+qd[43]*(OMcp46_142*ROcp46_542-OMcp46_242*ROcp46_442)+qd[44]*(OMcp46_143*ROcp46_843-OMcp46_243*\
   ROcp46_743)

# = = Block_1_0_0_47_0_17 = = 
 
# Sensor Kinematics 


    ROcp46_447 = ROcp46_444*C47+ROcp46_743*S47
    ROcp46_547 = ROcp46_544*C47+ROcp46_843*S47
    ROcp46_647 = ROcp46_644*C47+ROcp46_943*S47
    ROcp46_747 = -(ROcp46_444*S47-ROcp46_743*C47)
    ROcp46_847 = -(ROcp46_544*S47-ROcp46_843*C47)
    ROcp46_947 = -(ROcp46_644*S47-ROcp46_943*C47)
    RLcp46_147 = ROcp46_444*s.dpt[2,46]+ROcp46_743*s.dpt[3,46]
    RLcp46_247 = ROcp46_544*s.dpt[2,46]+ROcp46_843*s.dpt[3,46]
    RLcp46_347 = ROcp46_644*s.dpt[2,46]+ROcp46_943*s.dpt[3,46]
    POcp46_147 = RLcp46_140+RLcp46_142+RLcp46_147+q[1]
    POcp46_247 = RLcp46_240+RLcp46_242+RLcp46_247+q[2]
    POcp46_347 = RLcp46_340+RLcp46_342+RLcp46_347+q[3]
    OMcp46_147 = OMcp46_144+ROcp46_144*qd[47]
    OMcp46_247 = OMcp46_244+ROcp46_244*qd[47]
    OMcp46_347 = OMcp46_344+ROcp46_344*qd[47]
    ORcp46_147 = OMcp46_244*RLcp46_347-OMcp46_344*RLcp46_247
    ORcp46_247 = -(OMcp46_144*RLcp46_347-OMcp46_344*RLcp46_147)
    ORcp46_347 = OMcp46_144*RLcp46_247-OMcp46_244*RLcp46_147
    VIcp46_147 = ORcp46_140+ORcp46_142+ORcp46_147+qd[1]
    VIcp46_247 = ORcp46_240+ORcp46_242+ORcp46_247+qd[2]
    VIcp46_347 = ORcp46_340+ORcp46_342+ORcp46_347+qd[3]
    OPcp46_147 = OPcp46_144+ROcp46_144*qdd[47]+qd[47]*(OMcp46_244*ROcp46_344-OMcp46_344*ROcp46_244)
    OPcp46_247 = OPcp46_244+ROcp46_244*qdd[47]-qd[47]*(OMcp46_144*ROcp46_344-OMcp46_344*ROcp46_144)
    OPcp46_347 = OPcp46_344+ROcp46_344*qdd[47]+qd[47]*(OMcp46_144*ROcp46_244-OMcp46_244*ROcp46_144)
    ACcp46_147 = qdd[1]+OMcp46_241*ORcp46_342+OMcp46_244*ORcp46_347+OMcp46_26*ORcp46_340-OMcp46_341*ORcp46_242-OMcp46_344*\
   ORcp46_247-OMcp46_36*ORcp46_240+OPcp46_241*RLcp46_342+OPcp46_244*RLcp46_347+OPcp46_26*RLcp46_340-OPcp46_341*RLcp46_242-\
   OPcp46_344*RLcp46_247-OPcp46_36*RLcp46_240
    ACcp46_247 = qdd[2]-OMcp46_141*ORcp46_342-OMcp46_144*ORcp46_347-OMcp46_16*ORcp46_340+OMcp46_341*ORcp46_142+OMcp46_344*\
   ORcp46_147+OMcp46_36*ORcp46_140-OPcp46_141*RLcp46_342-OPcp46_144*RLcp46_347-OPcp46_16*RLcp46_340+OPcp46_341*RLcp46_142+\
   OPcp46_344*RLcp46_147+OPcp46_36*RLcp46_140
    ACcp46_347 = qdd[3]+OMcp46_141*ORcp46_242+OMcp46_144*ORcp46_247+OMcp46_16*ORcp46_240-OMcp46_241*ORcp46_142-OMcp46_244*\
   ORcp46_147-OMcp46_26*ORcp46_140+OPcp46_141*RLcp46_242+OPcp46_144*RLcp46_247+OPcp46_16*RLcp46_240-OPcp46_241*RLcp46_142-\
   OPcp46_244*RLcp46_147-OPcp46_26*RLcp46_140

# = = Block_1_0_0_47_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp46_147
    sens.P[2] = POcp46_247
    sens.P[3] = POcp46_347
    sens.R[1,1] = ROcp46_144
    sens.R[1,2] = ROcp46_244
    sens.R[1,3] = ROcp46_344
    sens.R[2,1] = ROcp46_447
    sens.R[2,2] = ROcp46_547
    sens.R[2,3] = ROcp46_647
    sens.R[3,1] = ROcp46_747
    sens.R[3,2] = ROcp46_847
    sens.R[3,3] = ROcp46_947
    sens.V[1] = VIcp46_147
    sens.V[2] = VIcp46_247
    sens.V[3] = VIcp46_347
    sens.OM[1] = OMcp46_147
    sens.OM[2] = OMcp46_247
    sens.OM[3] = OMcp46_347
    sens.A[1] = ACcp46_147
    sens.A[2] = ACcp46_247
    sens.A[3] = ACcp46_347
    sens.OMP[1] = OPcp46_147
    sens.OMP[2] = OPcp46_247
    sens.OMP[3] = OPcp46_347
 
# 
  elif(isens==48): 


# = = Block_1_0_0_48_0_1 = = 
 
# Sensor Kinematics 


    ROcp47_15 = C4*C5
    ROcp47_25 = S4*C5
    ROcp47_75 = C4*S5
    ROcp47_85 = S4*S5
    ROcp47_46 = ROcp47_75*S6-S4*C6
    ROcp47_56 = ROcp47_85*S6+C4*C6
    ROcp47_76 = ROcp47_75*C6+S4*S6
    ROcp47_86 = ROcp47_85*C6-C4*S6
    OMcp47_15 = -qd[5]*S4
    OMcp47_25 = qd[5]*C4
    OMcp47_16 = OMcp47_15+ROcp47_15*qd[6]
    OMcp47_26 = OMcp47_25+ROcp47_25*qd[6]
    OMcp47_36 = qd[4]-qd[6]*S5
    OPcp47_16 = ROcp47_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp47_25*S5+ROcp47_25*qd[4])
    OPcp47_26 = ROcp47_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp47_15*S5+ROcp47_15*qd[4])
    OPcp47_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_48_0_15 = = 
 
# Sensor Kinematics 


    ROcp47_440 = ROcp47_46*C40+ROcp47_76*S40
    ROcp47_540 = ROcp47_56*C40+ROcp47_86*S40
    ROcp47_640 = S40p6*C5
    ROcp47_740 = -(ROcp47_46*S40-ROcp47_76*C40)
    ROcp47_840 = -(ROcp47_56*S40-ROcp47_86*C40)
    ROcp47_940 = C40p6*C5
    ROcp47_141 = ROcp47_15*C41+ROcp47_440*S41
    ROcp47_241 = ROcp47_25*C41+ROcp47_540*S41
    ROcp47_341 = ROcp47_640*S41-C41*S5
    ROcp47_441 = -(ROcp47_15*S41-ROcp47_440*C41)
    ROcp47_541 = -(ROcp47_25*S41-ROcp47_540*C41)
    ROcp47_641 = ROcp47_640*C41+S41*S5
    ROcp47_442 = ROcp47_441*C42+ROcp47_740*S42
    ROcp47_542 = ROcp47_541*C42+ROcp47_840*S42
    ROcp47_642 = ROcp47_641*C42+ROcp47_940*S42
    ROcp47_742 = -(ROcp47_441*S42-ROcp47_740*C42)
    ROcp47_842 = -(ROcp47_541*S42-ROcp47_840*C42)
    ROcp47_942 = -(ROcp47_641*S42-ROcp47_940*C42)
    ROcp47_143 = ROcp47_141*C43-ROcp47_742*S43
    ROcp47_243 = ROcp47_241*C43-ROcp47_842*S43
    ROcp47_343 = ROcp47_341*C43-ROcp47_942*S43
    ROcp47_743 = ROcp47_141*S43+ROcp47_742*C43
    ROcp47_843 = ROcp47_241*S43+ROcp47_842*C43
    ROcp47_943 = ROcp47_341*S43+ROcp47_942*C43
    ROcp47_144 = ROcp47_143*C44+ROcp47_442*S44
    ROcp47_244 = ROcp47_243*C44+ROcp47_542*S44
    ROcp47_344 = ROcp47_343*C44+ROcp47_642*S44
    ROcp47_444 = -(ROcp47_143*S44-ROcp47_442*C44)
    ROcp47_544 = -(ROcp47_243*S44-ROcp47_542*C44)
    ROcp47_644 = -(ROcp47_343*S44-ROcp47_642*C44)
    RLcp47_140 = ROcp47_15*s.dpt[1,12]+ROcp47_46*s.dpt[2,12]
    RLcp47_240 = ROcp47_25*s.dpt[1,12]+ROcp47_56*s.dpt[2,12]
    RLcp47_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp47_140 = OMcp47_16+ROcp47_15*qd[40]
    OMcp47_240 = OMcp47_26+ROcp47_25*qd[40]
    OMcp47_340 = OMcp47_36-qd[40]*S5
    ORcp47_140 = OMcp47_26*RLcp47_340-OMcp47_36*RLcp47_240
    ORcp47_240 = -(OMcp47_16*RLcp47_340-OMcp47_36*RLcp47_140)
    ORcp47_340 = OMcp47_16*RLcp47_240-OMcp47_26*RLcp47_140
    OMcp47_141 = OMcp47_140+ROcp47_740*qd[41]
    OMcp47_241 = OMcp47_240+ROcp47_840*qd[41]
    OMcp47_341 = OMcp47_340+ROcp47_940*qd[41]
    OPcp47_141 = OPcp47_16+ROcp47_15*qdd[40]+ROcp47_740*qdd[41]-qd[40]*(OMcp47_26*S5+OMcp47_36*ROcp47_25)+qd[41]*(\
   OMcp47_240*ROcp47_940-OMcp47_340*ROcp47_840)
    OPcp47_241 = OPcp47_26+ROcp47_25*qdd[40]+ROcp47_840*qdd[41]+qd[40]*(OMcp47_16*S5+OMcp47_36*ROcp47_15)-qd[41]*(\
   OMcp47_140*ROcp47_940-OMcp47_340*ROcp47_740)
    OPcp47_341 = OPcp47_36+ROcp47_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp47_16*ROcp47_25-OMcp47_26*ROcp47_15)+qd[41]*(\
   OMcp47_140*ROcp47_840-OMcp47_240*ROcp47_740)
    RLcp47_142 = ROcp47_441*s.dpt[2,42]
    RLcp47_242 = ROcp47_541*s.dpt[2,42]
    RLcp47_342 = ROcp47_641*s.dpt[2,42]
    OMcp47_142 = OMcp47_141+ROcp47_141*qd[42]
    OMcp47_242 = OMcp47_241+ROcp47_241*qd[42]
    OMcp47_342 = OMcp47_341+ROcp47_341*qd[42]
    ORcp47_142 = OMcp47_241*RLcp47_342-OMcp47_341*RLcp47_242
    ORcp47_242 = -(OMcp47_141*RLcp47_342-OMcp47_341*RLcp47_142)
    ORcp47_342 = OMcp47_141*RLcp47_242-OMcp47_241*RLcp47_142
    OMcp47_143 = OMcp47_142+ROcp47_442*qd[43]
    OMcp47_243 = OMcp47_242+ROcp47_542*qd[43]
    OMcp47_343 = OMcp47_342+ROcp47_642*qd[43]
    OMcp47_144 = OMcp47_143+ROcp47_743*qd[44]
    OMcp47_244 = OMcp47_243+ROcp47_843*qd[44]
    OMcp47_344 = OMcp47_343+ROcp47_943*qd[44]
    OPcp47_144 = OPcp47_141+ROcp47_141*qdd[42]+ROcp47_442*qdd[43]+ROcp47_743*qdd[44]+qd[42]*(OMcp47_241*ROcp47_341-\
   OMcp47_341*ROcp47_241)+qd[43]*(OMcp47_242*ROcp47_642-OMcp47_342*ROcp47_542)+qd[44]*(OMcp47_243*ROcp47_943-OMcp47_343*\
   ROcp47_843)
    OPcp47_244 = OPcp47_241+ROcp47_241*qdd[42]+ROcp47_542*qdd[43]+ROcp47_843*qdd[44]-qd[42]*(OMcp47_141*ROcp47_341-\
   OMcp47_341*ROcp47_141)-qd[43]*(OMcp47_142*ROcp47_642-OMcp47_342*ROcp47_442)-qd[44]*(OMcp47_143*ROcp47_943-OMcp47_343*\
   ROcp47_743)
    OPcp47_344 = OPcp47_341+ROcp47_341*qdd[42]+ROcp47_642*qdd[43]+ROcp47_943*qdd[44]+qd[42]*(OMcp47_141*ROcp47_241-\
   OMcp47_241*ROcp47_141)+qd[43]*(OMcp47_142*ROcp47_542-OMcp47_242*ROcp47_442)+qd[44]*(OMcp47_143*ROcp47_843-OMcp47_243*\
   ROcp47_743)

# = = Block_1_0_0_48_0_17 = = 
 
# Sensor Kinematics 


    ROcp47_447 = ROcp47_444*C47+ROcp47_743*S47
    ROcp47_547 = ROcp47_544*C47+ROcp47_843*S47
    ROcp47_647 = ROcp47_644*C47+ROcp47_943*S47
    ROcp47_747 = -(ROcp47_444*S47-ROcp47_743*C47)
    ROcp47_847 = -(ROcp47_544*S47-ROcp47_843*C47)
    ROcp47_947 = -(ROcp47_644*S47-ROcp47_943*C47)
    ROcp47_148 = ROcp47_144*C48-ROcp47_747*S48
    ROcp47_248 = ROcp47_244*C48-ROcp47_847*S48
    ROcp47_348 = ROcp47_344*C48-ROcp47_947*S48
    ROcp47_748 = ROcp47_144*S48+ROcp47_747*C48
    ROcp47_848 = ROcp47_244*S48+ROcp47_847*C48
    ROcp47_948 = ROcp47_344*S48+ROcp47_947*C48
    RLcp47_147 = ROcp47_444*s.dpt[2,46]+ROcp47_743*s.dpt[3,46]
    RLcp47_247 = ROcp47_544*s.dpt[2,46]+ROcp47_843*s.dpt[3,46]
    RLcp47_347 = ROcp47_644*s.dpt[2,46]+ROcp47_943*s.dpt[3,46]
    POcp47_147 = RLcp47_140+RLcp47_142+RLcp47_147+q[1]
    POcp47_247 = RLcp47_240+RLcp47_242+RLcp47_247+q[2]
    POcp47_347 = RLcp47_340+RLcp47_342+RLcp47_347+q[3]
    OMcp47_147 = OMcp47_144+ROcp47_144*qd[47]
    OMcp47_247 = OMcp47_244+ROcp47_244*qd[47]
    OMcp47_347 = OMcp47_344+ROcp47_344*qd[47]
    ORcp47_147 = OMcp47_244*RLcp47_347-OMcp47_344*RLcp47_247
    ORcp47_247 = -(OMcp47_144*RLcp47_347-OMcp47_344*RLcp47_147)
    ORcp47_347 = OMcp47_144*RLcp47_247-OMcp47_244*RLcp47_147
    VIcp47_147 = ORcp47_140+ORcp47_142+ORcp47_147+qd[1]
    VIcp47_247 = ORcp47_240+ORcp47_242+ORcp47_247+qd[2]
    VIcp47_347 = ORcp47_340+ORcp47_342+ORcp47_347+qd[3]
    ACcp47_147 = qdd[1]+OMcp47_241*ORcp47_342+OMcp47_244*ORcp47_347+OMcp47_26*ORcp47_340-OMcp47_341*ORcp47_242-OMcp47_344*\
   ORcp47_247-OMcp47_36*ORcp47_240+OPcp47_241*RLcp47_342+OPcp47_244*RLcp47_347+OPcp47_26*RLcp47_340-OPcp47_341*RLcp47_242-\
   OPcp47_344*RLcp47_247-OPcp47_36*RLcp47_240
    ACcp47_247 = qdd[2]-OMcp47_141*ORcp47_342-OMcp47_144*ORcp47_347-OMcp47_16*ORcp47_340+OMcp47_341*ORcp47_142+OMcp47_344*\
   ORcp47_147+OMcp47_36*ORcp47_140-OPcp47_141*RLcp47_342-OPcp47_144*RLcp47_347-OPcp47_16*RLcp47_340+OPcp47_341*RLcp47_142+\
   OPcp47_344*RLcp47_147+OPcp47_36*RLcp47_140
    ACcp47_347 = qdd[3]+OMcp47_141*ORcp47_242+OMcp47_144*ORcp47_247+OMcp47_16*ORcp47_240-OMcp47_241*ORcp47_142-OMcp47_244*\
   ORcp47_147-OMcp47_26*ORcp47_140+OPcp47_141*RLcp47_242+OPcp47_144*RLcp47_247+OPcp47_16*RLcp47_240-OPcp47_241*RLcp47_142-\
   OPcp47_244*RLcp47_147-OPcp47_26*RLcp47_140
    OMcp47_148 = OMcp47_147+ROcp47_447*qd[48]
    OMcp47_248 = OMcp47_247+ROcp47_547*qd[48]
    OMcp47_348 = OMcp47_347+ROcp47_647*qd[48]
    OPcp47_148 = OPcp47_144+ROcp47_144*qdd[47]+ROcp47_447*qdd[48]+qd[47]*(OMcp47_244*ROcp47_344-OMcp47_344*ROcp47_244)+\
   qd[48]*(OMcp47_247*ROcp47_647-OMcp47_347*ROcp47_547)
    OPcp47_248 = OPcp47_244+ROcp47_244*qdd[47]+ROcp47_547*qdd[48]-qd[47]*(OMcp47_144*ROcp47_344-OMcp47_344*ROcp47_144)-\
   qd[48]*(OMcp47_147*ROcp47_647-OMcp47_347*ROcp47_447)
    OPcp47_348 = OPcp47_344+ROcp47_344*qdd[47]+ROcp47_647*qdd[48]+qd[47]*(OMcp47_144*ROcp47_244-OMcp47_244*ROcp47_144)+\
   qd[48]*(OMcp47_147*ROcp47_547-OMcp47_247*ROcp47_447)

# = = Block_1_0_0_48_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp47_147
    sens.P[2] = POcp47_247
    sens.P[3] = POcp47_347
    sens.R[1,1] = ROcp47_148
    sens.R[1,2] = ROcp47_248
    sens.R[1,3] = ROcp47_348
    sens.R[2,1] = ROcp47_447
    sens.R[2,2] = ROcp47_547
    sens.R[2,3] = ROcp47_647
    sens.R[3,1] = ROcp47_748
    sens.R[3,2] = ROcp47_848
    sens.R[3,3] = ROcp47_948
    sens.V[1] = VIcp47_147
    sens.V[2] = VIcp47_247
    sens.V[3] = VIcp47_347
    sens.OM[1] = OMcp47_148
    sens.OM[2] = OMcp47_248
    sens.OM[3] = OMcp47_348
    sens.A[1] = ACcp47_147
    sens.A[2] = ACcp47_247
    sens.A[3] = ACcp47_347
    sens.OMP[1] = OPcp47_148
    sens.OMP[2] = OPcp47_248
    sens.OMP[3] = OPcp47_348
 
# 
  elif(isens==49): 


# = = Block_1_0_0_49_0_1 = = 
 
# Sensor Kinematics 


    ROcp48_15 = C4*C5
    ROcp48_25 = S4*C5
    ROcp48_75 = C4*S5
    ROcp48_85 = S4*S5
    ROcp48_46 = ROcp48_75*S6-S4*C6
    ROcp48_56 = ROcp48_85*S6+C4*C6
    ROcp48_66 = C5*S6
    ROcp48_76 = ROcp48_75*C6+S4*S6
    ROcp48_86 = ROcp48_85*C6-C4*S6
    ROcp48_96 = C5*C6
    OMcp48_15 = -qd[5]*S4
    OMcp48_25 = qd[5]*C4
    OMcp48_16 = OMcp48_15+ROcp48_15*qd[6]
    OMcp48_26 = OMcp48_25+ROcp48_25*qd[6]
    OMcp48_36 = qd[4]-qd[6]*S5
    OPcp48_16 = ROcp48_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp48_25*S5+ROcp48_25*qd[4])
    OPcp48_26 = ROcp48_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp48_15*S5+ROcp48_15*qd[4])
    OPcp48_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_49_0_18 = = 
 
# Sensor Kinematics 


    RLcp48_149 = ROcp48_15*s.dpt[1,13]+ROcp48_46*q[49]
    RLcp48_249 = ROcp48_25*s.dpt[1,13]+ROcp48_56*q[49]
    RLcp48_349 = ROcp48_66*q[49]-s.dpt[1,13]*S5
    POcp48_149 = RLcp48_149+q[1]
    POcp48_249 = RLcp48_249+q[2]
    POcp48_349 = RLcp48_349+q[3]
    ORcp48_149 = OMcp48_26*RLcp48_349-OMcp48_36*RLcp48_249
    ORcp48_249 = -(OMcp48_16*RLcp48_349-OMcp48_36*RLcp48_149)
    ORcp48_349 = OMcp48_16*RLcp48_249-OMcp48_26*RLcp48_149
    VIcp48_149 = ORcp48_149+qd[1]+ROcp48_46*qd[49]
    VIcp48_249 = ORcp48_249+qd[2]+ROcp48_56*qd[49]
    VIcp48_349 = ORcp48_349+qd[3]+ROcp48_66*qd[49]
    ACcp48_149 = qdd[1]+OMcp48_26*ORcp48_349-OMcp48_36*ORcp48_249+OPcp48_26*RLcp48_349-OPcp48_36*RLcp48_249+ROcp48_46*\
   qdd[49]+(2.0)*qd[49]*(OMcp48_26*ROcp48_66-OMcp48_36*ROcp48_56)
    ACcp48_249 = qdd[2]-OMcp48_16*ORcp48_349+OMcp48_36*ORcp48_149-OPcp48_16*RLcp48_349+OPcp48_36*RLcp48_149+ROcp48_56*\
   qdd[49]-(2.0)*qd[49]*(OMcp48_16*ROcp48_66-OMcp48_36*ROcp48_46)
    ACcp48_349 = qdd[3]+OMcp48_16*ORcp48_249-OMcp48_26*ORcp48_149+OPcp48_16*RLcp48_249-OPcp48_26*RLcp48_149+ROcp48_66*\
   qdd[49]+(2.0)*qd[49]*(OMcp48_16*ROcp48_56-OMcp48_26*ROcp48_46)

# = = Block_1_0_0_49_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp48_149
    sens.P[2] = POcp48_249
    sens.P[3] = POcp48_349
    sens.R[1,1] = ROcp48_15
    sens.R[1,2] = ROcp48_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp48_46
    sens.R[2,2] = ROcp48_56
    sens.R[2,3] = ROcp48_66
    sens.R[3,1] = ROcp48_76
    sens.R[3,2] = ROcp48_86
    sens.R[3,3] = ROcp48_96
    sens.V[1] = VIcp48_149
    sens.V[2] = VIcp48_249
    sens.V[3] = VIcp48_349
    sens.OM[1] = OMcp48_16
    sens.OM[2] = OMcp48_26
    sens.OM[3] = OMcp48_36
    sens.A[1] = ACcp48_149
    sens.A[2] = ACcp48_249
    sens.A[3] = ACcp48_349
    sens.OMP[1] = OPcp48_16
    sens.OMP[2] = OPcp48_26
    sens.OMP[3] = OPcp48_36
 
# 
  elif(isens==50): 


# = = Block_1_0_0_50_0_1 = = 
 
# Sensor Kinematics 


    ROcp49_15 = C4*C5
    ROcp49_25 = S4*C5
    ROcp49_75 = C4*S5
    ROcp49_85 = S4*S5
    ROcp49_46 = ROcp49_75*S6-S4*C6
    ROcp49_56 = ROcp49_85*S6+C4*C6
    ROcp49_66 = C5*S6
    ROcp49_76 = ROcp49_75*C6+S4*S6
    ROcp49_86 = ROcp49_85*C6-C4*S6
    ROcp49_96 = C5*C6
    OMcp49_15 = -qd[5]*S4
    OMcp49_25 = qd[5]*C4
    OMcp49_16 = OMcp49_15+ROcp49_15*qd[6]
    OMcp49_26 = OMcp49_25+ROcp49_25*qd[6]
    OMcp49_36 = qd[4]-qd[6]*S5
    OPcp49_16 = ROcp49_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp49_25*S5+ROcp49_25*qd[4])
    OPcp49_26 = ROcp49_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp49_15*S5+ROcp49_15*qd[4])
    OPcp49_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_50_0_18 = = 
 
# Sensor Kinematics 


    RLcp49_149 = ROcp49_15*s.dpt[1,13]+ROcp49_46*q[49]
    RLcp49_249 = ROcp49_25*s.dpt[1,13]+ROcp49_56*q[49]
    RLcp49_349 = ROcp49_66*q[49]-s.dpt[1,13]*S5
    ORcp49_149 = OMcp49_26*RLcp49_349-OMcp49_36*RLcp49_249
    ORcp49_249 = -(OMcp49_16*RLcp49_349-OMcp49_36*RLcp49_149)
    ORcp49_349 = OMcp49_16*RLcp49_249-OMcp49_26*RLcp49_149

# = = Block_1_0_0_50_0_19 = = 
 
# Sensor Kinematics 


    ROcp49_150 = ROcp49_15*C50+ROcp49_46*S50
    ROcp49_250 = ROcp49_25*C50+ROcp49_56*S50
    ROcp49_350 = ROcp49_66*S50-C50*S5
    ROcp49_450 = -(ROcp49_15*S50-ROcp49_46*C50)
    ROcp49_550 = -(ROcp49_25*S50-ROcp49_56*C50)
    ROcp49_650 = ROcp49_66*C50+S50*S5
    RLcp49_150 = ROcp49_46*s.dpt[2,50]
    RLcp49_250 = ROcp49_56*s.dpt[2,50]
    RLcp49_350 = ROcp49_66*s.dpt[2,50]
    POcp49_150 = RLcp49_149+RLcp49_150+q[1]
    POcp49_250 = RLcp49_249+RLcp49_250+q[2]
    POcp49_350 = RLcp49_349+RLcp49_350+q[3]
    OMcp49_150 = OMcp49_16+ROcp49_76*qd[50]
    OMcp49_250 = OMcp49_26+ROcp49_86*qd[50]
    OMcp49_350 = OMcp49_36+ROcp49_96*qd[50]
    ORcp49_150 = OMcp49_26*RLcp49_350-OMcp49_36*RLcp49_250
    ORcp49_250 = -(OMcp49_16*RLcp49_350-OMcp49_36*RLcp49_150)
    ORcp49_350 = OMcp49_16*RLcp49_250-OMcp49_26*RLcp49_150
    VIcp49_150 = ORcp49_149+ORcp49_150+qd[1]+ROcp49_46*qd[49]
    VIcp49_250 = ORcp49_249+ORcp49_250+qd[2]+ROcp49_56*qd[49]
    VIcp49_350 = ORcp49_349+ORcp49_350+qd[3]+ROcp49_66*qd[49]
    OPcp49_150 = OPcp49_16+ROcp49_76*qdd[50]+qd[50]*(OMcp49_26*ROcp49_96-OMcp49_36*ROcp49_86)
    OPcp49_250 = OPcp49_26+ROcp49_86*qdd[50]-qd[50]*(OMcp49_16*ROcp49_96-OMcp49_36*ROcp49_76)
    OPcp49_350 = OPcp49_36+ROcp49_96*qdd[50]+qd[50]*(OMcp49_16*ROcp49_86-OMcp49_26*ROcp49_76)
    ACcp49_150 = qdd[1]+OMcp49_26*ORcp49_349+OMcp49_26*ORcp49_350-OMcp49_36*ORcp49_249-OMcp49_36*ORcp49_250+OPcp49_26*\
   RLcp49_349+OPcp49_26*RLcp49_350-OPcp49_36*RLcp49_249-OPcp49_36*RLcp49_250+ROcp49_46*qdd[49]+(2.0)*qd[49]*(OMcp49_26*ROcp49_66-\
   OMcp49_36*ROcp49_56)
    ACcp49_250 = qdd[2]-OMcp49_16*ORcp49_349-OMcp49_16*ORcp49_350+OMcp49_36*ORcp49_149+OMcp49_36*ORcp49_150-OPcp49_16*\
   RLcp49_349-OPcp49_16*RLcp49_350+OPcp49_36*RLcp49_149+OPcp49_36*RLcp49_150+ROcp49_56*qdd[49]-(2.0)*qd[49]*(OMcp49_16*ROcp49_66-\
   OMcp49_36*ROcp49_46)
    ACcp49_350 = qdd[3]+OMcp49_16*ORcp49_249+OMcp49_16*ORcp49_250-OMcp49_26*ORcp49_149-OMcp49_26*ORcp49_150+OPcp49_16*\
   RLcp49_249+OPcp49_16*RLcp49_250-OPcp49_26*RLcp49_149-OPcp49_26*RLcp49_150+ROcp49_66*qdd[49]+(2.0)*qd[49]*(OMcp49_16*ROcp49_56-\
   OMcp49_26*ROcp49_46)

# = = Block_1_0_0_50_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp49_150
    sens.P[2] = POcp49_250
    sens.P[3] = POcp49_350
    sens.R[1,1] = ROcp49_150
    sens.R[1,2] = ROcp49_250
    sens.R[1,3] = ROcp49_350
    sens.R[2,1] = ROcp49_450
    sens.R[2,2] = ROcp49_550
    sens.R[2,3] = ROcp49_650
    sens.R[3,1] = ROcp49_76
    sens.R[3,2] = ROcp49_86
    sens.R[3,3] = ROcp49_96
    sens.V[1] = VIcp49_150
    sens.V[2] = VIcp49_250
    sens.V[3] = VIcp49_350
    sens.OM[1] = OMcp49_150
    sens.OM[2] = OMcp49_250
    sens.OM[3] = OMcp49_350
    sens.A[1] = ACcp49_150
    sens.A[2] = ACcp49_250
    sens.A[3] = ACcp49_350
    sens.OMP[1] = OPcp49_150
    sens.OMP[2] = OPcp49_250
    sens.OMP[3] = OPcp49_350
 
# 
  elif(isens==51): 


# = = Block_1_0_0_51_0_1 = = 
 
# Sensor Kinematics 


    ROcp50_15 = C4*C5
    ROcp50_25 = S4*C5
    ROcp50_75 = C4*S5
    ROcp50_85 = S4*S5
    ROcp50_46 = ROcp50_75*S6-S4*C6
    ROcp50_56 = ROcp50_85*S6+C4*C6
    ROcp50_66 = C5*S6
    ROcp50_76 = ROcp50_75*C6+S4*S6
    ROcp50_86 = ROcp50_85*C6-C4*S6
    ROcp50_96 = C5*C6
    OMcp50_15 = -qd[5]*S4
    OMcp50_25 = qd[5]*C4
    OMcp50_16 = OMcp50_15+ROcp50_15*qd[6]
    OMcp50_26 = OMcp50_25+ROcp50_25*qd[6]
    OMcp50_36 = qd[4]-qd[6]*S5
    OPcp50_16 = ROcp50_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp50_25*S5+ROcp50_25*qd[4])
    OPcp50_26 = ROcp50_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp50_15*S5+ROcp50_15*qd[4])
    OPcp50_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_51_0_18 = = 
 
# Sensor Kinematics 


    RLcp50_149 = ROcp50_15*s.dpt[1,13]+ROcp50_46*q[49]
    RLcp50_249 = ROcp50_25*s.dpt[1,13]+ROcp50_56*q[49]
    RLcp50_349 = ROcp50_66*q[49]-s.dpt[1,13]*S5
    ORcp50_149 = OMcp50_26*RLcp50_349-OMcp50_36*RLcp50_249
    ORcp50_249 = -(OMcp50_16*RLcp50_349-OMcp50_36*RLcp50_149)
    ORcp50_349 = OMcp50_16*RLcp50_249-OMcp50_26*RLcp50_149

# = = Block_1_0_0_51_0_19 = = 
 
# Sensor Kinematics 


    ROcp50_150 = ROcp50_15*C50+ROcp50_46*S50
    ROcp50_250 = ROcp50_25*C50+ROcp50_56*S50
    ROcp50_350 = ROcp50_66*S50-C50*S5
    ROcp50_450 = -(ROcp50_15*S50-ROcp50_46*C50)
    ROcp50_550 = -(ROcp50_25*S50-ROcp50_56*C50)
    ROcp50_650 = ROcp50_66*C50+S50*S5
    ROcp50_451 = ROcp50_450*C51+ROcp50_76*S51
    ROcp50_551 = ROcp50_550*C51+ROcp50_86*S51
    ROcp50_651 = ROcp50_650*C51+ROcp50_96*S51
    ROcp50_751 = -(ROcp50_450*S51-ROcp50_76*C51)
    ROcp50_851 = -(ROcp50_550*S51-ROcp50_86*C51)
    ROcp50_951 = -(ROcp50_650*S51-ROcp50_96*C51)
    RLcp50_150 = ROcp50_46*s.dpt[2,50]
    RLcp50_250 = ROcp50_56*s.dpt[2,50]
    RLcp50_350 = ROcp50_66*s.dpt[2,50]
    POcp50_150 = RLcp50_149+RLcp50_150+q[1]
    POcp50_250 = RLcp50_249+RLcp50_250+q[2]
    POcp50_350 = RLcp50_349+RLcp50_350+q[3]
    OMcp50_150 = OMcp50_16+ROcp50_76*qd[50]
    OMcp50_250 = OMcp50_26+ROcp50_86*qd[50]
    OMcp50_350 = OMcp50_36+ROcp50_96*qd[50]
    ORcp50_150 = OMcp50_26*RLcp50_350-OMcp50_36*RLcp50_250
    ORcp50_250 = -(OMcp50_16*RLcp50_350-OMcp50_36*RLcp50_150)
    ORcp50_350 = OMcp50_16*RLcp50_250-OMcp50_26*RLcp50_150
    VIcp50_150 = ORcp50_149+ORcp50_150+qd[1]+ROcp50_46*qd[49]
    VIcp50_250 = ORcp50_249+ORcp50_250+qd[2]+ROcp50_56*qd[49]
    VIcp50_350 = ORcp50_349+ORcp50_350+qd[3]+ROcp50_66*qd[49]
    ACcp50_150 = qdd[1]+OMcp50_26*ORcp50_349+OMcp50_26*ORcp50_350-OMcp50_36*ORcp50_249-OMcp50_36*ORcp50_250+OPcp50_26*\
   RLcp50_349+OPcp50_26*RLcp50_350-OPcp50_36*RLcp50_249-OPcp50_36*RLcp50_250+ROcp50_46*qdd[49]+(2.0)*qd[49]*(OMcp50_26*ROcp50_66-\
   OMcp50_36*ROcp50_56)
    ACcp50_250 = qdd[2]-OMcp50_16*ORcp50_349-OMcp50_16*ORcp50_350+OMcp50_36*ORcp50_149+OMcp50_36*ORcp50_150-OPcp50_16*\
   RLcp50_349-OPcp50_16*RLcp50_350+OPcp50_36*RLcp50_149+OPcp50_36*RLcp50_150+ROcp50_56*qdd[49]-(2.0)*qd[49]*(OMcp50_16*ROcp50_66-\
   OMcp50_36*ROcp50_46)
    ACcp50_350 = qdd[3]+OMcp50_16*ORcp50_249+OMcp50_16*ORcp50_250-OMcp50_26*ORcp50_149-OMcp50_26*ORcp50_150+OPcp50_16*\
   RLcp50_249+OPcp50_16*RLcp50_250-OPcp50_26*RLcp50_149-OPcp50_26*RLcp50_150+ROcp50_66*qdd[49]+(2.0)*qd[49]*(OMcp50_16*ROcp50_56-\
   OMcp50_26*ROcp50_46)
    OMcp50_151 = OMcp50_150+ROcp50_150*qd[51]
    OMcp50_251 = OMcp50_250+ROcp50_250*qd[51]
    OMcp50_351 = OMcp50_350+ROcp50_350*qd[51]
    OPcp50_151 = OPcp50_16+ROcp50_150*qdd[51]+ROcp50_76*qdd[50]+qd[50]*(OMcp50_26*ROcp50_96-OMcp50_36*ROcp50_86)+qd[51]*(\
   OMcp50_250*ROcp50_350-OMcp50_350*ROcp50_250)
    OPcp50_251 = OPcp50_26+ROcp50_250*qdd[51]+ROcp50_86*qdd[50]-qd[50]*(OMcp50_16*ROcp50_96-OMcp50_36*ROcp50_76)-qd[51]*(\
   OMcp50_150*ROcp50_350-OMcp50_350*ROcp50_150)
    OPcp50_351 = OPcp50_36+ROcp50_350*qdd[51]+ROcp50_96*qdd[50]+qd[50]*(OMcp50_16*ROcp50_86-OMcp50_26*ROcp50_76)+qd[51]*(\
   OMcp50_150*ROcp50_250-OMcp50_250*ROcp50_150)

# = = Block_1_0_0_51_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp50_150
    sens.P[2] = POcp50_250
    sens.P[3] = POcp50_350
    sens.R[1,1] = ROcp50_150
    sens.R[1,2] = ROcp50_250
    sens.R[1,3] = ROcp50_350
    sens.R[2,1] = ROcp50_451
    sens.R[2,2] = ROcp50_551
    sens.R[2,3] = ROcp50_651
    sens.R[3,1] = ROcp50_751
    sens.R[3,2] = ROcp50_851
    sens.R[3,3] = ROcp50_951
    sens.V[1] = VIcp50_150
    sens.V[2] = VIcp50_250
    sens.V[3] = VIcp50_350
    sens.OM[1] = OMcp50_151
    sens.OM[2] = OMcp50_251
    sens.OM[3] = OMcp50_351
    sens.A[1] = ACcp50_150
    sens.A[2] = ACcp50_250
    sens.A[3] = ACcp50_350
    sens.OMP[1] = OPcp50_151
    sens.OMP[2] = OPcp50_251
    sens.OMP[3] = OPcp50_351
 
# 
  elif(isens==52): 


# = = Block_1_0_0_52_0_1 = = 
 
# Sensor Kinematics 


    ROcp51_15 = C4*C5
    ROcp51_25 = S4*C5
    ROcp51_75 = C4*S5
    ROcp51_85 = S4*S5
    ROcp51_46 = ROcp51_75*S6-S4*C6
    ROcp51_56 = ROcp51_85*S6+C4*C6
    ROcp51_66 = C5*S6
    ROcp51_76 = ROcp51_75*C6+S4*S6
    ROcp51_86 = ROcp51_85*C6-C4*S6
    ROcp51_96 = C5*C6
    OMcp51_15 = -qd[5]*S4
    OMcp51_25 = qd[5]*C4
    OMcp51_16 = OMcp51_15+ROcp51_15*qd[6]
    OMcp51_26 = OMcp51_25+ROcp51_25*qd[6]
    OMcp51_36 = qd[4]-qd[6]*S5
    OPcp51_16 = ROcp51_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp51_25*S5+ROcp51_25*qd[4])
    OPcp51_26 = ROcp51_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp51_15*S5+ROcp51_15*qd[4])
    OPcp51_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_52_0_18 = = 
 
# Sensor Kinematics 


    RLcp51_149 = ROcp51_15*s.dpt[1,13]+ROcp51_46*q[49]
    RLcp51_249 = ROcp51_25*s.dpt[1,13]+ROcp51_56*q[49]
    RLcp51_349 = ROcp51_66*q[49]-s.dpt[1,13]*S5
    ORcp51_149 = OMcp51_26*RLcp51_349-OMcp51_36*RLcp51_249
    ORcp51_249 = -(OMcp51_16*RLcp51_349-OMcp51_36*RLcp51_149)
    ORcp51_349 = OMcp51_16*RLcp51_249-OMcp51_26*RLcp51_149

# = = Block_1_0_0_52_0_20 = = 
 
# Sensor Kinematics 


    ROcp51_152 = ROcp51_15*C52+ROcp51_46*S52
    ROcp51_252 = ROcp51_25*C52+ROcp51_56*S52
    ROcp51_352 = ROcp51_66*S52-C52*S5
    ROcp51_452 = -(ROcp51_15*S52-ROcp51_46*C52)
    ROcp51_552 = -(ROcp51_25*S52-ROcp51_56*C52)
    ROcp51_652 = ROcp51_66*C52+S52*S5
    RLcp51_152 = ROcp51_46*s.dpt[2,51]
    RLcp51_252 = ROcp51_56*s.dpt[2,51]
    RLcp51_352 = ROcp51_66*s.dpt[2,51]
    POcp51_152 = RLcp51_149+RLcp51_152+q[1]
    POcp51_252 = RLcp51_249+RLcp51_252+q[2]
    POcp51_352 = RLcp51_349+RLcp51_352+q[3]
    OMcp51_152 = OMcp51_16+ROcp51_76*qd[52]
    OMcp51_252 = OMcp51_26+ROcp51_86*qd[52]
    OMcp51_352 = OMcp51_36+ROcp51_96*qd[52]
    ORcp51_152 = OMcp51_26*RLcp51_352-OMcp51_36*RLcp51_252
    ORcp51_252 = -(OMcp51_16*RLcp51_352-OMcp51_36*RLcp51_152)
    ORcp51_352 = OMcp51_16*RLcp51_252-OMcp51_26*RLcp51_152
    VIcp51_152 = ORcp51_149+ORcp51_152+qd[1]+ROcp51_46*qd[49]
    VIcp51_252 = ORcp51_249+ORcp51_252+qd[2]+ROcp51_56*qd[49]
    VIcp51_352 = ORcp51_349+ORcp51_352+qd[3]+ROcp51_66*qd[49]
    OPcp51_152 = OPcp51_16+ROcp51_76*qdd[52]+qd[52]*(OMcp51_26*ROcp51_96-OMcp51_36*ROcp51_86)
    OPcp51_252 = OPcp51_26+ROcp51_86*qdd[52]-qd[52]*(OMcp51_16*ROcp51_96-OMcp51_36*ROcp51_76)
    OPcp51_352 = OPcp51_36+ROcp51_96*qdd[52]+qd[52]*(OMcp51_16*ROcp51_86-OMcp51_26*ROcp51_76)
    ACcp51_152 = qdd[1]+OMcp51_26*ORcp51_349+OMcp51_26*ORcp51_352-OMcp51_36*ORcp51_249-OMcp51_36*ORcp51_252+OPcp51_26*\
   RLcp51_349+OPcp51_26*RLcp51_352-OPcp51_36*RLcp51_249-OPcp51_36*RLcp51_252+ROcp51_46*qdd[49]+(2.0)*qd[49]*(OMcp51_26*ROcp51_66-\
   OMcp51_36*ROcp51_56)
    ACcp51_252 = qdd[2]-OMcp51_16*ORcp51_349-OMcp51_16*ORcp51_352+OMcp51_36*ORcp51_149+OMcp51_36*ORcp51_152-OPcp51_16*\
   RLcp51_349-OPcp51_16*RLcp51_352+OPcp51_36*RLcp51_149+OPcp51_36*RLcp51_152+ROcp51_56*qdd[49]-(2.0)*qd[49]*(OMcp51_16*ROcp51_66-\
   OMcp51_36*ROcp51_46)
    ACcp51_352 = qdd[3]+OMcp51_16*ORcp51_249+OMcp51_16*ORcp51_252-OMcp51_26*ORcp51_149-OMcp51_26*ORcp51_152+OPcp51_16*\
   RLcp51_249+OPcp51_16*RLcp51_252-OPcp51_26*RLcp51_149-OPcp51_26*RLcp51_152+ROcp51_66*qdd[49]+(2.0)*qd[49]*(OMcp51_16*ROcp51_56-\
   OMcp51_26*ROcp51_46)

# = = Block_1_0_0_52_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp51_152
    sens.P[2] = POcp51_252
    sens.P[3] = POcp51_352
    sens.R[1,1] = ROcp51_152
    sens.R[1,2] = ROcp51_252
    sens.R[1,3] = ROcp51_352
    sens.R[2,1] = ROcp51_452
    sens.R[2,2] = ROcp51_552
    sens.R[2,3] = ROcp51_652
    sens.R[3,1] = ROcp51_76
    sens.R[3,2] = ROcp51_86
    sens.R[3,3] = ROcp51_96
    sens.V[1] = VIcp51_152
    sens.V[2] = VIcp51_252
    sens.V[3] = VIcp51_352
    sens.OM[1] = OMcp51_152
    sens.OM[2] = OMcp51_252
    sens.OM[3] = OMcp51_352
    sens.A[1] = ACcp51_152
    sens.A[2] = ACcp51_252
    sens.A[3] = ACcp51_352
    sens.OMP[1] = OPcp51_152
    sens.OMP[2] = OPcp51_252
    sens.OMP[3] = OPcp51_352
 
# 
  elif(isens==53): 


# = = Block_1_0_0_53_0_1 = = 
 
# Sensor Kinematics 


    ROcp52_15 = C4*C5
    ROcp52_25 = S4*C5
    ROcp52_75 = C4*S5
    ROcp52_85 = S4*S5
    ROcp52_46 = ROcp52_75*S6-S4*C6
    ROcp52_56 = ROcp52_85*S6+C4*C6
    ROcp52_66 = C5*S6
    ROcp52_76 = ROcp52_75*C6+S4*S6
    ROcp52_86 = ROcp52_85*C6-C4*S6
    ROcp52_96 = C5*C6
    OMcp52_15 = -qd[5]*S4
    OMcp52_25 = qd[5]*C4
    OMcp52_16 = OMcp52_15+ROcp52_15*qd[6]
    OMcp52_26 = OMcp52_25+ROcp52_25*qd[6]
    OMcp52_36 = qd[4]-qd[6]*S5
    OPcp52_16 = ROcp52_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp52_25*S5+ROcp52_25*qd[4])
    OPcp52_26 = ROcp52_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp52_15*S5+ROcp52_15*qd[4])
    OPcp52_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_53_0_18 = = 
 
# Sensor Kinematics 


    RLcp52_149 = ROcp52_15*s.dpt[1,13]+ROcp52_46*q[49]
    RLcp52_249 = ROcp52_25*s.dpt[1,13]+ROcp52_56*q[49]
    RLcp52_349 = ROcp52_66*q[49]-s.dpt[1,13]*S5
    ORcp52_149 = OMcp52_26*RLcp52_349-OMcp52_36*RLcp52_249
    ORcp52_249 = -(OMcp52_16*RLcp52_349-OMcp52_36*RLcp52_149)
    ORcp52_349 = OMcp52_16*RLcp52_249-OMcp52_26*RLcp52_149

# = = Block_1_0_0_53_0_20 = = 
 
# Sensor Kinematics 


    ROcp52_152 = ROcp52_15*C52+ROcp52_46*S52
    ROcp52_252 = ROcp52_25*C52+ROcp52_56*S52
    ROcp52_352 = ROcp52_66*S52-C52*S5
    ROcp52_452 = -(ROcp52_15*S52-ROcp52_46*C52)
    ROcp52_552 = -(ROcp52_25*S52-ROcp52_56*C52)
    ROcp52_652 = ROcp52_66*C52+S52*S5
    ROcp52_453 = ROcp52_452*C53+ROcp52_76*S53
    ROcp52_553 = ROcp52_552*C53+ROcp52_86*S53
    ROcp52_653 = ROcp52_652*C53+ROcp52_96*S53
    ROcp52_753 = -(ROcp52_452*S53-ROcp52_76*C53)
    ROcp52_853 = -(ROcp52_552*S53-ROcp52_86*C53)
    ROcp52_953 = -(ROcp52_652*S53-ROcp52_96*C53)
    RLcp52_152 = ROcp52_46*s.dpt[2,51]
    RLcp52_252 = ROcp52_56*s.dpt[2,51]
    RLcp52_352 = ROcp52_66*s.dpt[2,51]
    POcp52_152 = RLcp52_149+RLcp52_152+q[1]
    POcp52_252 = RLcp52_249+RLcp52_252+q[2]
    POcp52_352 = RLcp52_349+RLcp52_352+q[3]
    OMcp52_152 = OMcp52_16+ROcp52_76*qd[52]
    OMcp52_252 = OMcp52_26+ROcp52_86*qd[52]
    OMcp52_352 = OMcp52_36+ROcp52_96*qd[52]
    ORcp52_152 = OMcp52_26*RLcp52_352-OMcp52_36*RLcp52_252
    ORcp52_252 = -(OMcp52_16*RLcp52_352-OMcp52_36*RLcp52_152)
    ORcp52_352 = OMcp52_16*RLcp52_252-OMcp52_26*RLcp52_152
    VIcp52_152 = ORcp52_149+ORcp52_152+qd[1]+ROcp52_46*qd[49]
    VIcp52_252 = ORcp52_249+ORcp52_252+qd[2]+ROcp52_56*qd[49]
    VIcp52_352 = ORcp52_349+ORcp52_352+qd[3]+ROcp52_66*qd[49]
    ACcp52_152 = qdd[1]+OMcp52_26*ORcp52_349+OMcp52_26*ORcp52_352-OMcp52_36*ORcp52_249-OMcp52_36*ORcp52_252+OPcp52_26*\
   RLcp52_349+OPcp52_26*RLcp52_352-OPcp52_36*RLcp52_249-OPcp52_36*RLcp52_252+ROcp52_46*qdd[49]+(2.0)*qd[49]*(OMcp52_26*ROcp52_66-\
   OMcp52_36*ROcp52_56)
    ACcp52_252 = qdd[2]-OMcp52_16*ORcp52_349-OMcp52_16*ORcp52_352+OMcp52_36*ORcp52_149+OMcp52_36*ORcp52_152-OPcp52_16*\
   RLcp52_349-OPcp52_16*RLcp52_352+OPcp52_36*RLcp52_149+OPcp52_36*RLcp52_152+ROcp52_56*qdd[49]-(2.0)*qd[49]*(OMcp52_16*ROcp52_66-\
   OMcp52_36*ROcp52_46)
    ACcp52_352 = qdd[3]+OMcp52_16*ORcp52_249+OMcp52_16*ORcp52_252-OMcp52_26*ORcp52_149-OMcp52_26*ORcp52_152+OPcp52_16*\
   RLcp52_249+OPcp52_16*RLcp52_252-OPcp52_26*RLcp52_149-OPcp52_26*RLcp52_152+ROcp52_66*qdd[49]+(2.0)*qd[49]*(OMcp52_16*ROcp52_56-\
   OMcp52_26*ROcp52_46)
    OMcp52_153 = OMcp52_152+ROcp52_152*qd[53]
    OMcp52_253 = OMcp52_252+ROcp52_252*qd[53]
    OMcp52_353 = OMcp52_352+ROcp52_352*qd[53]
    OPcp52_153 = OPcp52_16+ROcp52_152*qdd[53]+ROcp52_76*qdd[52]+qd[52]*(OMcp52_26*ROcp52_96-OMcp52_36*ROcp52_86)+qd[53]*(\
   OMcp52_252*ROcp52_352-OMcp52_352*ROcp52_252)
    OPcp52_253 = OPcp52_26+ROcp52_252*qdd[53]+ROcp52_86*qdd[52]-qd[52]*(OMcp52_16*ROcp52_96-OMcp52_36*ROcp52_76)-qd[53]*(\
   OMcp52_152*ROcp52_352-OMcp52_352*ROcp52_152)
    OPcp52_353 = OPcp52_36+ROcp52_352*qdd[53]+ROcp52_96*qdd[52]+qd[52]*(OMcp52_16*ROcp52_86-OMcp52_26*ROcp52_76)+qd[53]*(\
   OMcp52_152*ROcp52_252-OMcp52_252*ROcp52_152)

# = = Block_1_0_0_53_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp52_152
    sens.P[2] = POcp52_252
    sens.P[3] = POcp52_352
    sens.R[1,1] = ROcp52_152
    sens.R[1,2] = ROcp52_252
    sens.R[1,3] = ROcp52_352
    sens.R[2,1] = ROcp52_453
    sens.R[2,2] = ROcp52_553
    sens.R[2,3] = ROcp52_653
    sens.R[3,1] = ROcp52_753
    sens.R[3,2] = ROcp52_853
    sens.R[3,3] = ROcp52_953
    sens.V[1] = VIcp52_152
    sens.V[2] = VIcp52_252
    sens.V[3] = VIcp52_352
    sens.OM[1] = OMcp52_153
    sens.OM[2] = OMcp52_253
    sens.OM[3] = OMcp52_353
    sens.A[1] = ACcp52_152
    sens.A[2] = ACcp52_252
    sens.A[3] = ACcp52_352
    sens.OMP[1] = OPcp52_153
    sens.OMP[2] = OPcp52_253
    sens.OMP[3] = OPcp52_353
 
# 
  elif(isens==54): 


# = = Block_1_0_0_54_0_1 = = 
 
# Sensor Kinematics 


    ROcp53_15 = C4*C5
    ROcp53_25 = S4*C5
    ROcp53_75 = C4*S5
    ROcp53_85 = S4*S5
    ROcp53_46 = ROcp53_75*S6-S4*C6
    ROcp53_56 = ROcp53_85*S6+C4*C6
    ROcp53_66 = C5*S6
    ROcp53_76 = ROcp53_75*C6+S4*S6
    ROcp53_86 = ROcp53_85*C6-C4*S6
    ROcp53_96 = C5*C6
    OMcp53_15 = -qd[5]*S4
    OMcp53_25 = qd[5]*C4
    OMcp53_16 = OMcp53_15+ROcp53_15*qd[6]
    OMcp53_26 = OMcp53_25+ROcp53_25*qd[6]
    OMcp53_36 = qd[4]-qd[6]*S5
    OPcp53_16 = ROcp53_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp53_25*S5+ROcp53_25*qd[4])
    OPcp53_26 = ROcp53_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp53_15*S5+ROcp53_15*qd[4])
    OPcp53_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_54_0_21 = = 
 
# Sensor Kinematics 


    ROcp53_154 = ROcp53_15*C54-ROcp53_76*S54
    ROcp53_254 = ROcp53_25*C54-ROcp53_86*S54
    ROcp53_354 = -(ROcp53_96*S54+C54*S5)
    ROcp53_754 = ROcp53_15*S54+ROcp53_76*C54
    ROcp53_854 = ROcp53_25*S54+ROcp53_86*C54
    ROcp53_954 = ROcp53_96*C54-S54*S5
    RLcp53_154 = ROcp53_15*s.dpt[1,14]+ROcp53_76*s.dpt[3,14]
    RLcp53_254 = ROcp53_25*s.dpt[1,14]+ROcp53_86*s.dpt[3,14]
    RLcp53_354 = ROcp53_96*s.dpt[3,14]-s.dpt[1,14]*S5
    POcp53_154 = RLcp53_154+q[1]
    POcp53_254 = RLcp53_254+q[2]
    POcp53_354 = RLcp53_354+q[3]
    OMcp53_154 = OMcp53_16+ROcp53_46*qd[54]
    OMcp53_254 = OMcp53_26+ROcp53_56*qd[54]
    OMcp53_354 = OMcp53_36+ROcp53_66*qd[54]
    ORcp53_154 = OMcp53_26*RLcp53_354-OMcp53_36*RLcp53_254
    ORcp53_254 = -(OMcp53_16*RLcp53_354-OMcp53_36*RLcp53_154)
    ORcp53_354 = OMcp53_16*RLcp53_254-OMcp53_26*RLcp53_154
    VIcp53_154 = ORcp53_154+qd[1]
    VIcp53_254 = ORcp53_254+qd[2]
    VIcp53_354 = ORcp53_354+qd[3]
    OPcp53_154 = OPcp53_16+ROcp53_46*qdd[54]+qd[54]*(OMcp53_26*ROcp53_66-OMcp53_36*ROcp53_56)
    OPcp53_254 = OPcp53_26+ROcp53_56*qdd[54]-qd[54]*(OMcp53_16*ROcp53_66-OMcp53_36*ROcp53_46)
    OPcp53_354 = OPcp53_36+ROcp53_66*qdd[54]+qd[54]*(OMcp53_16*ROcp53_56-OMcp53_26*ROcp53_46)
    ACcp53_154 = qdd[1]+OMcp53_26*ORcp53_354-OMcp53_36*ORcp53_254+OPcp53_26*RLcp53_354-OPcp53_36*RLcp53_254
    ACcp53_254 = qdd[2]-OMcp53_16*ORcp53_354+OMcp53_36*ORcp53_154-OPcp53_16*RLcp53_354+OPcp53_36*RLcp53_154
    ACcp53_354 = qdd[3]+OMcp53_16*ORcp53_254-OMcp53_26*ORcp53_154+OPcp53_16*RLcp53_254-OPcp53_26*RLcp53_154

# = = Block_1_0_0_54_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp53_154
    sens.P[2] = POcp53_254
    sens.P[3] = POcp53_354
    sens.R[1,1] = ROcp53_154
    sens.R[1,2] = ROcp53_254
    sens.R[1,3] = ROcp53_354
    sens.R[2,1] = ROcp53_46
    sens.R[2,2] = ROcp53_56
    sens.R[2,3] = ROcp53_66
    sens.R[3,1] = ROcp53_754
    sens.R[3,2] = ROcp53_854
    sens.R[3,3] = ROcp53_954
    sens.V[1] = VIcp53_154
    sens.V[2] = VIcp53_254
    sens.V[3] = VIcp53_354
    sens.OM[1] = OMcp53_154
    sens.OM[2] = OMcp53_254
    sens.OM[3] = OMcp53_354
    sens.A[1] = ACcp53_154
    sens.A[2] = ACcp53_254
    sens.A[3] = ACcp53_354
    sens.OMP[1] = OPcp53_154
    sens.OMP[2] = OPcp53_254
    sens.OMP[3] = OPcp53_354
 
# 
  elif(isens==55): 


# = = Block_1_0_0_55_0_1 = = 
 
# Sensor Kinematics 


    ROcp54_15 = C4*C5
    ROcp54_25 = S4*C5
    ROcp54_75 = C4*S5
    ROcp54_85 = S4*S5
    ROcp54_46 = ROcp54_75*S6-S4*C6
    ROcp54_56 = ROcp54_85*S6+C4*C6
    ROcp54_66 = C5*S6
    ROcp54_76 = ROcp54_75*C6+S4*S6
    ROcp54_86 = ROcp54_85*C6-C4*S6
    ROcp54_96 = C5*C6
    OMcp54_15 = -qd[5]*S4
    OMcp54_25 = qd[5]*C4
    OMcp54_16 = OMcp54_15+ROcp54_15*qd[6]
    OMcp54_26 = OMcp54_25+ROcp54_25*qd[6]
    OMcp54_36 = qd[4]-qd[6]*S5
    OPcp54_16 = ROcp54_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp54_25*S5+ROcp54_25*qd[4])
    OPcp54_26 = ROcp54_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp54_15*S5+ROcp54_15*qd[4])
    OPcp54_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_55_0_21 = = 
 
# Sensor Kinematics 


    ROcp54_154 = ROcp54_15*C54-ROcp54_76*S54
    ROcp54_254 = ROcp54_25*C54-ROcp54_86*S54
    ROcp54_354 = -(ROcp54_96*S54+C54*S5)
    ROcp54_754 = ROcp54_15*S54+ROcp54_76*C54
    ROcp54_854 = ROcp54_25*S54+ROcp54_86*C54
    ROcp54_954 = ROcp54_96*C54-S54*S5
    RLcp54_154 = ROcp54_15*s.dpt[1,14]+ROcp54_76*s.dpt[3,14]
    RLcp54_254 = ROcp54_25*s.dpt[1,14]+ROcp54_86*s.dpt[3,14]
    RLcp54_354 = ROcp54_96*s.dpt[3,14]-s.dpt[1,14]*S5
    POcp54_154 = RLcp54_154+q[1]
    POcp54_254 = RLcp54_254+q[2]
    POcp54_354 = RLcp54_354+q[3]
    OMcp54_154 = OMcp54_16+ROcp54_46*qd[54]
    OMcp54_254 = OMcp54_26+ROcp54_56*qd[54]
    OMcp54_354 = OMcp54_36+ROcp54_66*qd[54]
    ORcp54_154 = OMcp54_26*RLcp54_354-OMcp54_36*RLcp54_254
    ORcp54_254 = -(OMcp54_16*RLcp54_354-OMcp54_36*RLcp54_154)
    ORcp54_354 = OMcp54_16*RLcp54_254-OMcp54_26*RLcp54_154
    VIcp54_154 = ORcp54_154+qd[1]
    VIcp54_254 = ORcp54_254+qd[2]
    VIcp54_354 = ORcp54_354+qd[3]
    ACcp54_154 = qdd[1]+OMcp54_26*ORcp54_354-OMcp54_36*ORcp54_254+OPcp54_26*RLcp54_354-OPcp54_36*RLcp54_254
    ACcp54_254 = qdd[2]-OMcp54_16*ORcp54_354+OMcp54_36*ORcp54_154-OPcp54_16*RLcp54_354+OPcp54_36*RLcp54_154
    ACcp54_354 = qdd[3]+OMcp54_16*ORcp54_254-OMcp54_26*ORcp54_154+OPcp54_16*RLcp54_254-OPcp54_26*RLcp54_154

# = = Block_1_0_0_55_0_22 = = 
 
# Sensor Kinematics 


    ROcp54_155 = ROcp54_154*C55-ROcp54_754*S55
    ROcp54_255 = ROcp54_254*C55-ROcp54_854*S55
    ROcp54_355 = ROcp54_354*C55-ROcp54_954*S55
    ROcp54_755 = ROcp54_154*S55+ROcp54_754*C55
    ROcp54_855 = ROcp54_254*S55+ROcp54_854*C55
    ROcp54_955 = ROcp54_354*S55+ROcp54_954*C55
    OMcp54_155 = OMcp54_154+ROcp54_46*qd[55]
    OMcp54_255 = OMcp54_254+ROcp54_56*qd[55]
    OMcp54_355 = OMcp54_354+ROcp54_66*qd[55]
    OPcp54_155 = OPcp54_16+ROcp54_46*qdd[54]+ROcp54_46*qdd[55]+qd[54]*(OMcp54_26*ROcp54_66-OMcp54_36*ROcp54_56)+qd[55]*(\
   OMcp54_254*ROcp54_66-OMcp54_354*ROcp54_56)
    OPcp54_255 = OPcp54_26+ROcp54_56*qdd[54]+ROcp54_56*qdd[55]-qd[54]*(OMcp54_16*ROcp54_66-OMcp54_36*ROcp54_46)-qd[55]*(\
   OMcp54_154*ROcp54_66-OMcp54_354*ROcp54_46)
    OPcp54_355 = OPcp54_36+ROcp54_66*qdd[54]+ROcp54_66*qdd[55]+qd[54]*(OMcp54_16*ROcp54_56-OMcp54_26*ROcp54_46)+qd[55]*(\
   OMcp54_154*ROcp54_56-OMcp54_254*ROcp54_46)

# = = Block_1_0_0_55_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp54_154
    sens.P[2] = POcp54_254
    sens.P[3] = POcp54_354
    sens.R[1,1] = ROcp54_155
    sens.R[1,2] = ROcp54_255
    sens.R[1,3] = ROcp54_355
    sens.R[2,1] = ROcp54_46
    sens.R[2,2] = ROcp54_56
    sens.R[2,3] = ROcp54_66
    sens.R[3,1] = ROcp54_755
    sens.R[3,2] = ROcp54_855
    sens.R[3,3] = ROcp54_955
    sens.V[1] = VIcp54_154
    sens.V[2] = VIcp54_254
    sens.V[3] = VIcp54_354
    sens.OM[1] = OMcp54_155
    sens.OM[2] = OMcp54_255
    sens.OM[3] = OMcp54_355
    sens.A[1] = ACcp54_154
    sens.A[2] = ACcp54_254
    sens.A[3] = ACcp54_354
    sens.OMP[1] = OPcp54_155
    sens.OMP[2] = OPcp54_255
    sens.OMP[3] = OPcp54_355
 
# 
  elif(isens==56): 


# = = Block_1_0_0_56_0_1 = = 
 
# Sensor Kinematics 


    ROcp55_15 = C4*C5
    ROcp55_25 = S4*C5
    ROcp55_75 = C4*S5
    ROcp55_85 = S4*S5
    ROcp55_46 = ROcp55_75*S6-S4*C6
    ROcp55_56 = ROcp55_85*S6+C4*C6
    ROcp55_66 = C5*S6
    ROcp55_76 = ROcp55_75*C6+S4*S6
    ROcp55_86 = ROcp55_85*C6-C4*S6
    ROcp55_96 = C5*C6
    OMcp55_15 = -qd[5]*S4
    OMcp55_25 = qd[5]*C4
    OMcp55_16 = OMcp55_15+ROcp55_15*qd[6]
    OMcp55_26 = OMcp55_25+ROcp55_25*qd[6]
    OMcp55_36 = qd[4]-qd[6]*S5
    OPcp55_16 = ROcp55_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp55_25*S5+ROcp55_25*qd[4])
    OPcp55_26 = ROcp55_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp55_15*S5+ROcp55_15*qd[4])
    OPcp55_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_56_0_21 = = 
 
# Sensor Kinematics 


    ROcp55_154 = ROcp55_15*C54-ROcp55_76*S54
    ROcp55_254 = ROcp55_25*C54-ROcp55_86*S54
    ROcp55_354 = -(ROcp55_96*S54+C54*S5)
    ROcp55_754 = ROcp55_15*S54+ROcp55_76*C54
    ROcp55_854 = ROcp55_25*S54+ROcp55_86*C54
    ROcp55_954 = ROcp55_96*C54-S54*S5
    RLcp55_154 = ROcp55_15*s.dpt[1,14]+ROcp55_76*s.dpt[3,14]
    RLcp55_254 = ROcp55_25*s.dpt[1,14]+ROcp55_86*s.dpt[3,14]
    RLcp55_354 = ROcp55_96*s.dpt[3,14]-s.dpt[1,14]*S5
    OMcp55_154 = OMcp55_16+ROcp55_46*qd[54]
    OMcp55_254 = OMcp55_26+ROcp55_56*qd[54]
    OMcp55_354 = OMcp55_36+ROcp55_66*qd[54]
    ORcp55_154 = OMcp55_26*RLcp55_354-OMcp55_36*RLcp55_254
    ORcp55_254 = -(OMcp55_16*RLcp55_354-OMcp55_36*RLcp55_154)
    ORcp55_354 = OMcp55_16*RLcp55_254-OMcp55_26*RLcp55_154

# = = Block_1_0_0_56_0_22 = = 
 
# Sensor Kinematics 


    ROcp55_155 = ROcp55_154*C55-ROcp55_754*S55
    ROcp55_255 = ROcp55_254*C55-ROcp55_854*S55
    ROcp55_355 = ROcp55_354*C55-ROcp55_954*S55
    ROcp55_755 = ROcp55_154*S55+ROcp55_754*C55
    ROcp55_855 = ROcp55_254*S55+ROcp55_854*C55
    ROcp55_955 = ROcp55_354*S55+ROcp55_954*C55
    ROcp55_156 = ROcp55_155*C56-ROcp55_755*S56
    ROcp55_256 = ROcp55_255*C56-ROcp55_855*S56
    ROcp55_356 = ROcp55_355*C56-ROcp55_955*S56
    ROcp55_756 = ROcp55_155*S56+ROcp55_755*C56
    ROcp55_856 = ROcp55_255*S56+ROcp55_855*C56
    ROcp55_956 = ROcp55_355*S56+ROcp55_955*C56
    OMcp55_155 = OMcp55_154+ROcp55_46*qd[55]
    OMcp55_255 = OMcp55_254+ROcp55_56*qd[55]
    OMcp55_355 = OMcp55_354+ROcp55_66*qd[55]
    OPcp55_155 = OPcp55_16+ROcp55_46*qdd[54]+ROcp55_46*qdd[55]+qd[54]*(OMcp55_26*ROcp55_66-OMcp55_36*ROcp55_56)+qd[55]*(\
   OMcp55_254*ROcp55_66-OMcp55_354*ROcp55_56)
    OPcp55_255 = OPcp55_26+ROcp55_56*qdd[54]+ROcp55_56*qdd[55]-qd[54]*(OMcp55_16*ROcp55_66-OMcp55_36*ROcp55_46)-qd[55]*(\
   OMcp55_154*ROcp55_66-OMcp55_354*ROcp55_46)
    OPcp55_355 = OPcp55_36+ROcp55_66*qdd[54]+ROcp55_66*qdd[55]+qd[54]*(OMcp55_16*ROcp55_56-OMcp55_26*ROcp55_46)+qd[55]*(\
   OMcp55_154*ROcp55_56-OMcp55_254*ROcp55_46)
    RLcp55_156 = ROcp55_155*s.dpt[1,55]+ROcp55_46*s.dpt[2,55]
    RLcp55_256 = ROcp55_255*s.dpt[1,55]+ROcp55_56*s.dpt[2,55]
    RLcp55_356 = ROcp55_355*s.dpt[1,55]+ROcp55_66*s.dpt[2,55]
    POcp55_156 = RLcp55_154+RLcp55_156+q[1]
    POcp55_256 = RLcp55_254+RLcp55_256+q[2]
    POcp55_356 = RLcp55_354+RLcp55_356+q[3]
    OMcp55_156 = OMcp55_155+ROcp55_46*qd[56]
    OMcp55_256 = OMcp55_255+ROcp55_56*qd[56]
    OMcp55_356 = OMcp55_355+ROcp55_66*qd[56]
    ORcp55_156 = OMcp55_255*RLcp55_356-OMcp55_355*RLcp55_256
    ORcp55_256 = -(OMcp55_155*RLcp55_356-OMcp55_355*RLcp55_156)
    ORcp55_356 = OMcp55_155*RLcp55_256-OMcp55_255*RLcp55_156
    VIcp55_156 = ORcp55_154+ORcp55_156+qd[1]
    VIcp55_256 = ORcp55_254+ORcp55_256+qd[2]
    VIcp55_356 = ORcp55_354+ORcp55_356+qd[3]
    OPcp55_156 = OPcp55_155+ROcp55_46*qdd[56]+qd[56]*(OMcp55_255*ROcp55_66-OMcp55_355*ROcp55_56)
    OPcp55_256 = OPcp55_255+ROcp55_56*qdd[56]-qd[56]*(OMcp55_155*ROcp55_66-OMcp55_355*ROcp55_46)
    OPcp55_356 = OPcp55_355+ROcp55_66*qdd[56]+qd[56]*(OMcp55_155*ROcp55_56-OMcp55_255*ROcp55_46)
    ACcp55_156 = qdd[1]+OMcp55_255*ORcp55_356+OMcp55_26*ORcp55_354-OMcp55_355*ORcp55_256-OMcp55_36*ORcp55_254+OPcp55_255*\
   RLcp55_356+OPcp55_26*RLcp55_354-OPcp55_355*RLcp55_256-OPcp55_36*RLcp55_254
    ACcp55_256 = qdd[2]-OMcp55_155*ORcp55_356-OMcp55_16*ORcp55_354+OMcp55_355*ORcp55_156+OMcp55_36*ORcp55_154-OPcp55_155*\
   RLcp55_356-OPcp55_16*RLcp55_354+OPcp55_355*RLcp55_156+OPcp55_36*RLcp55_154
    ACcp55_356 = qdd[3]+OMcp55_155*ORcp55_256+OMcp55_16*ORcp55_254-OMcp55_255*ORcp55_156-OMcp55_26*ORcp55_154+OPcp55_155*\
   RLcp55_256+OPcp55_16*RLcp55_254-OPcp55_255*RLcp55_156-OPcp55_26*RLcp55_154

# = = Block_1_0_0_56_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp55_156
    sens.P[2] = POcp55_256
    sens.P[3] = POcp55_356
    sens.R[1,1] = ROcp55_156
    sens.R[1,2] = ROcp55_256
    sens.R[1,3] = ROcp55_356
    sens.R[2,1] = ROcp55_46
    sens.R[2,2] = ROcp55_56
    sens.R[2,3] = ROcp55_66
    sens.R[3,1] = ROcp55_756
    sens.R[3,2] = ROcp55_856
    sens.R[3,3] = ROcp55_956
    sens.V[1] = VIcp55_156
    sens.V[2] = VIcp55_256
    sens.V[3] = VIcp55_356
    sens.OM[1] = OMcp55_156
    sens.OM[2] = OMcp55_256
    sens.OM[3] = OMcp55_356
    sens.A[1] = ACcp55_156
    sens.A[2] = ACcp55_256
    sens.A[3] = ACcp55_356
    sens.OMP[1] = OPcp55_156
    sens.OMP[2] = OPcp55_256
    sens.OMP[3] = OPcp55_356
 
# 
  elif(isens==57): 


# = = Block_1_0_0_57_0_1 = = 
 
# Sensor Kinematics 


    ROcp56_15 = C4*C5
    ROcp56_25 = S4*C5
    ROcp56_75 = C4*S5
    ROcp56_85 = S4*S5
    ROcp56_46 = ROcp56_75*S6-S4*C6
    ROcp56_56 = ROcp56_85*S6+C4*C6
    ROcp56_66 = C5*S6
    ROcp56_76 = ROcp56_75*C6+S4*S6
    ROcp56_86 = ROcp56_85*C6-C4*S6
    ROcp56_96 = C5*C6
    OMcp56_15 = -qd[5]*S4
    OMcp56_25 = qd[5]*C4
    OMcp56_16 = OMcp56_15+ROcp56_15*qd[6]
    OMcp56_26 = OMcp56_25+ROcp56_25*qd[6]
    OMcp56_36 = qd[4]-qd[6]*S5
    OPcp56_16 = ROcp56_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp56_25*S5+ROcp56_25*qd[4])
    OPcp56_26 = ROcp56_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp56_15*S5+ROcp56_15*qd[4])
    OPcp56_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_57_0_21 = = 
 
# Sensor Kinematics 


    ROcp56_154 = ROcp56_15*C54-ROcp56_76*S54
    ROcp56_254 = ROcp56_25*C54-ROcp56_86*S54
    ROcp56_354 = -(ROcp56_96*S54+C54*S5)
    ROcp56_754 = ROcp56_15*S54+ROcp56_76*C54
    ROcp56_854 = ROcp56_25*S54+ROcp56_86*C54
    ROcp56_954 = ROcp56_96*C54-S54*S5
    RLcp56_154 = ROcp56_15*s.dpt[1,14]+ROcp56_76*s.dpt[3,14]
    RLcp56_254 = ROcp56_25*s.dpt[1,14]+ROcp56_86*s.dpt[3,14]
    RLcp56_354 = ROcp56_96*s.dpt[3,14]-s.dpt[1,14]*S5
    OMcp56_154 = OMcp56_16+ROcp56_46*qd[54]
    OMcp56_254 = OMcp56_26+ROcp56_56*qd[54]
    OMcp56_354 = OMcp56_36+ROcp56_66*qd[54]
    ORcp56_154 = OMcp56_26*RLcp56_354-OMcp56_36*RLcp56_254
    ORcp56_254 = -(OMcp56_16*RLcp56_354-OMcp56_36*RLcp56_154)
    ORcp56_354 = OMcp56_16*RLcp56_254-OMcp56_26*RLcp56_154

# = = Block_1_0_0_57_0_22 = = 
 
# Sensor Kinematics 


    ROcp56_155 = ROcp56_154*C55-ROcp56_754*S55
    ROcp56_255 = ROcp56_254*C55-ROcp56_854*S55
    ROcp56_355 = ROcp56_354*C55-ROcp56_954*S55
    ROcp56_755 = ROcp56_154*S55+ROcp56_754*C55
    ROcp56_855 = ROcp56_254*S55+ROcp56_854*C55
    ROcp56_955 = ROcp56_354*S55+ROcp56_954*C55
    ROcp56_156 = ROcp56_155*C56-ROcp56_755*S56
    ROcp56_256 = ROcp56_255*C56-ROcp56_855*S56
    ROcp56_356 = ROcp56_355*C56-ROcp56_955*S56
    ROcp56_756 = ROcp56_155*S56+ROcp56_755*C56
    ROcp56_856 = ROcp56_255*S56+ROcp56_855*C56
    ROcp56_956 = ROcp56_355*S56+ROcp56_955*C56
    ROcp56_457 = ROcp56_46*C57+ROcp56_756*S57
    ROcp56_557 = ROcp56_56*C57+ROcp56_856*S57
    ROcp56_657 = ROcp56_66*C57+ROcp56_956*S57
    ROcp56_757 = -(ROcp56_46*S57-ROcp56_756*C57)
    ROcp56_857 = -(ROcp56_56*S57-ROcp56_856*C57)
    ROcp56_957 = -(ROcp56_66*S57-ROcp56_956*C57)
    OMcp56_155 = OMcp56_154+ROcp56_46*qd[55]
    OMcp56_255 = OMcp56_254+ROcp56_56*qd[55]
    OMcp56_355 = OMcp56_354+ROcp56_66*qd[55]
    OPcp56_155 = OPcp56_16+ROcp56_46*qdd[54]+ROcp56_46*qdd[55]+qd[54]*(OMcp56_26*ROcp56_66-OMcp56_36*ROcp56_56)+qd[55]*(\
   OMcp56_254*ROcp56_66-OMcp56_354*ROcp56_56)
    OPcp56_255 = OPcp56_26+ROcp56_56*qdd[54]+ROcp56_56*qdd[55]-qd[54]*(OMcp56_16*ROcp56_66-OMcp56_36*ROcp56_46)-qd[55]*(\
   OMcp56_154*ROcp56_66-OMcp56_354*ROcp56_46)
    OPcp56_355 = OPcp56_36+ROcp56_66*qdd[54]+ROcp56_66*qdd[55]+qd[54]*(OMcp56_16*ROcp56_56-OMcp56_26*ROcp56_46)+qd[55]*(\
   OMcp56_154*ROcp56_56-OMcp56_254*ROcp56_46)
    RLcp56_156 = ROcp56_155*s.dpt[1,55]+ROcp56_46*s.dpt[2,55]
    RLcp56_256 = ROcp56_255*s.dpt[1,55]+ROcp56_56*s.dpt[2,55]
    RLcp56_356 = ROcp56_355*s.dpt[1,55]+ROcp56_66*s.dpt[2,55]
    POcp56_156 = RLcp56_154+RLcp56_156+q[1]
    POcp56_256 = RLcp56_254+RLcp56_256+q[2]
    POcp56_356 = RLcp56_354+RLcp56_356+q[3]
    OMcp56_156 = OMcp56_155+ROcp56_46*qd[56]
    OMcp56_256 = OMcp56_255+ROcp56_56*qd[56]
    OMcp56_356 = OMcp56_355+ROcp56_66*qd[56]
    ORcp56_156 = OMcp56_255*RLcp56_356-OMcp56_355*RLcp56_256
    ORcp56_256 = -(OMcp56_155*RLcp56_356-OMcp56_355*RLcp56_156)
    ORcp56_356 = OMcp56_155*RLcp56_256-OMcp56_255*RLcp56_156
    VIcp56_156 = ORcp56_154+ORcp56_156+qd[1]
    VIcp56_256 = ORcp56_254+ORcp56_256+qd[2]
    VIcp56_356 = ORcp56_354+ORcp56_356+qd[3]
    ACcp56_156 = qdd[1]+OMcp56_255*ORcp56_356+OMcp56_26*ORcp56_354-OMcp56_355*ORcp56_256-OMcp56_36*ORcp56_254+OPcp56_255*\
   RLcp56_356+OPcp56_26*RLcp56_354-OPcp56_355*RLcp56_256-OPcp56_36*RLcp56_254
    ACcp56_256 = qdd[2]-OMcp56_155*ORcp56_356-OMcp56_16*ORcp56_354+OMcp56_355*ORcp56_156+OMcp56_36*ORcp56_154-OPcp56_155*\
   RLcp56_356-OPcp56_16*RLcp56_354+OPcp56_355*RLcp56_156+OPcp56_36*RLcp56_154
    ACcp56_356 = qdd[3]+OMcp56_155*ORcp56_256+OMcp56_16*ORcp56_254-OMcp56_255*ORcp56_156-OMcp56_26*ORcp56_154+OPcp56_155*\
   RLcp56_256+OPcp56_16*RLcp56_254-OPcp56_255*RLcp56_156-OPcp56_26*RLcp56_154
    OMcp56_157 = OMcp56_156+ROcp56_156*qd[57]
    OMcp56_257 = OMcp56_256+ROcp56_256*qd[57]
    OMcp56_357 = OMcp56_356+ROcp56_356*qd[57]
    OPcp56_157 = OPcp56_155+ROcp56_156*qdd[57]+ROcp56_46*qdd[56]+qd[56]*(OMcp56_255*ROcp56_66-OMcp56_355*ROcp56_56)+qd[57]\
   *(OMcp56_256*ROcp56_356-OMcp56_356*ROcp56_256)
    OPcp56_257 = OPcp56_255+ROcp56_256*qdd[57]+ROcp56_56*qdd[56]-qd[56]*(OMcp56_155*ROcp56_66-OMcp56_355*ROcp56_46)-qd[57]\
   *(OMcp56_156*ROcp56_356-OMcp56_356*ROcp56_156)
    OPcp56_357 = OPcp56_355+ROcp56_356*qdd[57]+ROcp56_66*qdd[56]+qd[56]*(OMcp56_155*ROcp56_56-OMcp56_255*ROcp56_46)+qd[57]\
   *(OMcp56_156*ROcp56_256-OMcp56_256*ROcp56_156)

# = = Block_1_0_0_57_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp56_156
    sens.P[2] = POcp56_256
    sens.P[3] = POcp56_356
    sens.R[1,1] = ROcp56_156
    sens.R[1,2] = ROcp56_256
    sens.R[1,3] = ROcp56_356
    sens.R[2,1] = ROcp56_457
    sens.R[2,2] = ROcp56_557
    sens.R[2,3] = ROcp56_657
    sens.R[3,1] = ROcp56_757
    sens.R[3,2] = ROcp56_857
    sens.R[3,3] = ROcp56_957
    sens.V[1] = VIcp56_156
    sens.V[2] = VIcp56_256
    sens.V[3] = VIcp56_356
    sens.OM[1] = OMcp56_157
    sens.OM[2] = OMcp56_257
    sens.OM[3] = OMcp56_357
    sens.A[1] = ACcp56_156
    sens.A[2] = ACcp56_256
    sens.A[3] = ACcp56_356
    sens.OMP[1] = OPcp56_157
    sens.OMP[2] = OPcp56_257
    sens.OMP[3] = OPcp56_357
 
# 
  elif(isens==58): 


# = = Block_1_0_0_58_0_1 = = 
 
# Sensor Kinematics 


    ROcp57_15 = C4*C5
    ROcp57_25 = S4*C5
    ROcp57_75 = C4*S5
    ROcp57_85 = S4*S5
    ROcp57_46 = ROcp57_75*S6-S4*C6
    ROcp57_56 = ROcp57_85*S6+C4*C6
    ROcp57_66 = C5*S6
    ROcp57_76 = ROcp57_75*C6+S4*S6
    ROcp57_86 = ROcp57_85*C6-C4*S6
    ROcp57_96 = C5*C6
    OMcp57_15 = -qd[5]*S4
    OMcp57_25 = qd[5]*C4
    OMcp57_16 = OMcp57_15+ROcp57_15*qd[6]
    OMcp57_26 = OMcp57_25+ROcp57_25*qd[6]
    OMcp57_36 = qd[4]-qd[6]*S5
    OPcp57_16 = ROcp57_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp57_25*S5+ROcp57_25*qd[4])
    OPcp57_26 = ROcp57_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp57_15*S5+ROcp57_15*qd[4])
    OPcp57_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_58_0_21 = = 
 
# Sensor Kinematics 


    ROcp57_154 = ROcp57_15*C54-ROcp57_76*S54
    ROcp57_254 = ROcp57_25*C54-ROcp57_86*S54
    ROcp57_354 = -(ROcp57_96*S54+C54*S5)
    ROcp57_754 = ROcp57_15*S54+ROcp57_76*C54
    ROcp57_854 = ROcp57_25*S54+ROcp57_86*C54
    ROcp57_954 = ROcp57_96*C54-S54*S5
    RLcp57_154 = ROcp57_15*s.dpt[1,14]+ROcp57_76*s.dpt[3,14]
    RLcp57_254 = ROcp57_25*s.dpt[1,14]+ROcp57_86*s.dpt[3,14]
    RLcp57_354 = ROcp57_96*s.dpt[3,14]-s.dpt[1,14]*S5
    OMcp57_154 = OMcp57_16+ROcp57_46*qd[54]
    OMcp57_254 = OMcp57_26+ROcp57_56*qd[54]
    OMcp57_354 = OMcp57_36+ROcp57_66*qd[54]
    ORcp57_154 = OMcp57_26*RLcp57_354-OMcp57_36*RLcp57_254
    ORcp57_254 = -(OMcp57_16*RLcp57_354-OMcp57_36*RLcp57_154)
    ORcp57_354 = OMcp57_16*RLcp57_254-OMcp57_26*RLcp57_154
    OPcp57_154 = OPcp57_16+ROcp57_46*qdd[54]+qd[54]*(OMcp57_26*ROcp57_66-OMcp57_36*ROcp57_56)
    OPcp57_254 = OPcp57_26+ROcp57_56*qdd[54]-qd[54]*(OMcp57_16*ROcp57_66-OMcp57_36*ROcp57_46)
    OPcp57_354 = OPcp57_36+ROcp57_66*qdd[54]+qd[54]*(OMcp57_16*ROcp57_56-OMcp57_26*ROcp57_46)

# = = Block_1_0_0_58_0_23 = = 
 
# Sensor Kinematics 


    ROcp57_158 = ROcp57_154*C58-ROcp57_754*S58
    ROcp57_258 = ROcp57_254*C58-ROcp57_854*S58
    ROcp57_358 = ROcp57_354*C58-ROcp57_954*S58
    ROcp57_758 = ROcp57_154*S58+ROcp57_754*C58
    ROcp57_858 = ROcp57_254*S58+ROcp57_854*C58
    ROcp57_958 = ROcp57_354*S58+ROcp57_954*C58
    RLcp57_158 = ROcp57_154*s.dpt[1,54]+ROcp57_46*s.dpt[2,54]
    RLcp57_258 = ROcp57_254*s.dpt[1,54]+ROcp57_56*s.dpt[2,54]
    RLcp57_358 = ROcp57_354*s.dpt[1,54]+ROcp57_66*s.dpt[2,54]
    POcp57_158 = RLcp57_154+RLcp57_158+q[1]
    POcp57_258 = RLcp57_254+RLcp57_258+q[2]
    POcp57_358 = RLcp57_354+RLcp57_358+q[3]
    OMcp57_158 = OMcp57_154+ROcp57_46*qd[58]
    OMcp57_258 = OMcp57_254+ROcp57_56*qd[58]
    OMcp57_358 = OMcp57_354+ROcp57_66*qd[58]
    ORcp57_158 = OMcp57_254*RLcp57_358-OMcp57_354*RLcp57_258
    ORcp57_258 = -(OMcp57_154*RLcp57_358-OMcp57_354*RLcp57_158)
    ORcp57_358 = OMcp57_154*RLcp57_258-OMcp57_254*RLcp57_158
    VIcp57_158 = ORcp57_154+ORcp57_158+qd[1]
    VIcp57_258 = ORcp57_254+ORcp57_258+qd[2]
    VIcp57_358 = ORcp57_354+ORcp57_358+qd[3]
    OPcp57_158 = OPcp57_154+ROcp57_46*qdd[58]+qd[58]*(OMcp57_254*ROcp57_66-OMcp57_354*ROcp57_56)
    OPcp57_258 = OPcp57_254+ROcp57_56*qdd[58]-qd[58]*(OMcp57_154*ROcp57_66-OMcp57_354*ROcp57_46)
    OPcp57_358 = OPcp57_354+ROcp57_66*qdd[58]+qd[58]*(OMcp57_154*ROcp57_56-OMcp57_254*ROcp57_46)
    ACcp57_158 = qdd[1]+OMcp57_254*ORcp57_358+OMcp57_26*ORcp57_354-OMcp57_354*ORcp57_258-OMcp57_36*ORcp57_254+OPcp57_254*\
   RLcp57_358+OPcp57_26*RLcp57_354-OPcp57_354*RLcp57_258-OPcp57_36*RLcp57_254
    ACcp57_258 = qdd[2]-OMcp57_154*ORcp57_358-OMcp57_16*ORcp57_354+OMcp57_354*ORcp57_158+OMcp57_36*ORcp57_154-OPcp57_154*\
   RLcp57_358-OPcp57_16*RLcp57_354+OPcp57_354*RLcp57_158+OPcp57_36*RLcp57_154
    ACcp57_358 = qdd[3]+OMcp57_154*ORcp57_258+OMcp57_16*ORcp57_254-OMcp57_254*ORcp57_158-OMcp57_26*ORcp57_154+OPcp57_154*\
   RLcp57_258+OPcp57_16*RLcp57_254-OPcp57_254*RLcp57_158-OPcp57_26*RLcp57_154

# = = Block_1_0_0_58_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp57_158
    sens.P[2] = POcp57_258
    sens.P[3] = POcp57_358
    sens.R[1,1] = ROcp57_158
    sens.R[1,2] = ROcp57_258
    sens.R[1,3] = ROcp57_358
    sens.R[2,1] = ROcp57_46
    sens.R[2,2] = ROcp57_56
    sens.R[2,3] = ROcp57_66
    sens.R[3,1] = ROcp57_758
    sens.R[3,2] = ROcp57_858
    sens.R[3,3] = ROcp57_958
    sens.V[1] = VIcp57_158
    sens.V[2] = VIcp57_258
    sens.V[3] = VIcp57_358
    sens.OM[1] = OMcp57_158
    sens.OM[2] = OMcp57_258
    sens.OM[3] = OMcp57_358
    sens.A[1] = ACcp57_158
    sens.A[2] = ACcp57_258
    sens.A[3] = ACcp57_358
    sens.OMP[1] = OPcp57_158
    sens.OMP[2] = OPcp57_258
    sens.OMP[3] = OPcp57_358
 
# 
  elif(isens==59): 


# = = Block_1_0_0_59_0_1 = = 
 
# Sensor Kinematics 


    ROcp58_15 = C4*C5
    ROcp58_25 = S4*C5
    ROcp58_75 = C4*S5
    ROcp58_85 = S4*S5
    ROcp58_46 = ROcp58_75*S6-S4*C6
    ROcp58_56 = ROcp58_85*S6+C4*C6
    ROcp58_66 = C5*S6
    ROcp58_76 = ROcp58_75*C6+S4*S6
    ROcp58_86 = ROcp58_85*C6-C4*S6
    ROcp58_96 = C5*C6
    OMcp58_15 = -qd[5]*S4
    OMcp58_25 = qd[5]*C4
    OMcp58_16 = OMcp58_15+ROcp58_15*qd[6]
    OMcp58_26 = OMcp58_25+ROcp58_25*qd[6]
    OMcp58_36 = qd[4]-qd[6]*S5
    OPcp58_16 = ROcp58_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp58_25*S5+ROcp58_25*qd[4])
    OPcp58_26 = ROcp58_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp58_15*S5+ROcp58_15*qd[4])
    OPcp58_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_59_0_21 = = 
 
# Sensor Kinematics 


    ROcp58_154 = ROcp58_15*C54-ROcp58_76*S54
    ROcp58_254 = ROcp58_25*C54-ROcp58_86*S54
    ROcp58_354 = -(ROcp58_96*S54+C54*S5)
    ROcp58_754 = ROcp58_15*S54+ROcp58_76*C54
    ROcp58_854 = ROcp58_25*S54+ROcp58_86*C54
    ROcp58_954 = ROcp58_96*C54-S54*S5
    RLcp58_154 = ROcp58_15*s.dpt[1,14]+ROcp58_76*s.dpt[3,14]
    RLcp58_254 = ROcp58_25*s.dpt[1,14]+ROcp58_86*s.dpt[3,14]
    RLcp58_354 = ROcp58_96*s.dpt[3,14]-s.dpt[1,14]*S5
    OMcp58_154 = OMcp58_16+ROcp58_46*qd[54]
    OMcp58_254 = OMcp58_26+ROcp58_56*qd[54]
    OMcp58_354 = OMcp58_36+ROcp58_66*qd[54]
    ORcp58_154 = OMcp58_26*RLcp58_354-OMcp58_36*RLcp58_254
    ORcp58_254 = -(OMcp58_16*RLcp58_354-OMcp58_36*RLcp58_154)
    ORcp58_354 = OMcp58_16*RLcp58_254-OMcp58_26*RLcp58_154
    OPcp58_154 = OPcp58_16+ROcp58_46*qdd[54]+qd[54]*(OMcp58_26*ROcp58_66-OMcp58_36*ROcp58_56)
    OPcp58_254 = OPcp58_26+ROcp58_56*qdd[54]-qd[54]*(OMcp58_16*ROcp58_66-OMcp58_36*ROcp58_46)
    OPcp58_354 = OPcp58_36+ROcp58_66*qdd[54]+qd[54]*(OMcp58_16*ROcp58_56-OMcp58_26*ROcp58_46)

# = = Block_1_0_0_59_0_23 = = 
 
# Sensor Kinematics 


    ROcp58_158 = ROcp58_154*C58-ROcp58_754*S58
    ROcp58_258 = ROcp58_254*C58-ROcp58_854*S58
    ROcp58_358 = ROcp58_354*C58-ROcp58_954*S58
    ROcp58_758 = ROcp58_154*S58+ROcp58_754*C58
    ROcp58_858 = ROcp58_254*S58+ROcp58_854*C58
    ROcp58_958 = ROcp58_354*S58+ROcp58_954*C58
    ROcp58_459 = ROcp58_46*C59+ROcp58_758*S59
    ROcp58_559 = ROcp58_56*C59+ROcp58_858*S59
    ROcp58_659 = ROcp58_66*C59+ROcp58_958*S59
    ROcp58_759 = -(ROcp58_46*S59-ROcp58_758*C59)
    ROcp58_859 = -(ROcp58_56*S59-ROcp58_858*C59)
    ROcp58_959 = -(ROcp58_66*S59-ROcp58_958*C59)
    RLcp58_158 = ROcp58_154*s.dpt[1,54]+ROcp58_46*s.dpt[2,54]
    RLcp58_258 = ROcp58_254*s.dpt[1,54]+ROcp58_56*s.dpt[2,54]
    RLcp58_358 = ROcp58_354*s.dpt[1,54]+ROcp58_66*s.dpt[2,54]
    POcp58_158 = RLcp58_154+RLcp58_158+q[1]
    POcp58_258 = RLcp58_254+RLcp58_258+q[2]
    POcp58_358 = RLcp58_354+RLcp58_358+q[3]
    OMcp58_158 = OMcp58_154+ROcp58_46*qd[58]
    OMcp58_258 = OMcp58_254+ROcp58_56*qd[58]
    OMcp58_358 = OMcp58_354+ROcp58_66*qd[58]
    ORcp58_158 = OMcp58_254*RLcp58_358-OMcp58_354*RLcp58_258
    ORcp58_258 = -(OMcp58_154*RLcp58_358-OMcp58_354*RLcp58_158)
    ORcp58_358 = OMcp58_154*RLcp58_258-OMcp58_254*RLcp58_158
    VIcp58_158 = ORcp58_154+ORcp58_158+qd[1]
    VIcp58_258 = ORcp58_254+ORcp58_258+qd[2]
    VIcp58_358 = ORcp58_354+ORcp58_358+qd[3]
    ACcp58_158 = qdd[1]+OMcp58_254*ORcp58_358+OMcp58_26*ORcp58_354-OMcp58_354*ORcp58_258-OMcp58_36*ORcp58_254+OPcp58_254*\
   RLcp58_358+OPcp58_26*RLcp58_354-OPcp58_354*RLcp58_258-OPcp58_36*RLcp58_254
    ACcp58_258 = qdd[2]-OMcp58_154*ORcp58_358-OMcp58_16*ORcp58_354+OMcp58_354*ORcp58_158+OMcp58_36*ORcp58_154-OPcp58_154*\
   RLcp58_358-OPcp58_16*RLcp58_354+OPcp58_354*RLcp58_158+OPcp58_36*RLcp58_154
    ACcp58_358 = qdd[3]+OMcp58_154*ORcp58_258+OMcp58_16*ORcp58_254-OMcp58_254*ORcp58_158-OMcp58_26*ORcp58_154+OPcp58_154*\
   RLcp58_258+OPcp58_16*RLcp58_254-OPcp58_254*RLcp58_158-OPcp58_26*RLcp58_154
    OMcp58_159 = OMcp58_158+ROcp58_158*qd[59]
    OMcp58_259 = OMcp58_258+ROcp58_258*qd[59]
    OMcp58_359 = OMcp58_358+ROcp58_358*qd[59]
    OPcp58_159 = OPcp58_154+ROcp58_158*qdd[59]+ROcp58_46*qdd[58]+qd[58]*(OMcp58_254*ROcp58_66-OMcp58_354*ROcp58_56)+qd[59]\
   *(OMcp58_258*ROcp58_358-OMcp58_358*ROcp58_258)
    OPcp58_259 = OPcp58_254+ROcp58_258*qdd[59]+ROcp58_56*qdd[58]-qd[58]*(OMcp58_154*ROcp58_66-OMcp58_354*ROcp58_46)-qd[59]\
   *(OMcp58_158*ROcp58_358-OMcp58_358*ROcp58_158)
    OPcp58_359 = OPcp58_354+ROcp58_358*qdd[59]+ROcp58_66*qdd[58]+qd[58]*(OMcp58_154*ROcp58_56-OMcp58_254*ROcp58_46)+qd[59]\
   *(OMcp58_158*ROcp58_258-OMcp58_258*ROcp58_158)

# = = Block_1_0_0_59_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp58_158
    sens.P[2] = POcp58_258
    sens.P[3] = POcp58_358
    sens.R[1,1] = ROcp58_158
    sens.R[1,2] = ROcp58_258
    sens.R[1,3] = ROcp58_358
    sens.R[2,1] = ROcp58_459
    sens.R[2,2] = ROcp58_559
    sens.R[2,3] = ROcp58_659
    sens.R[3,1] = ROcp58_759
    sens.R[3,2] = ROcp58_859
    sens.R[3,3] = ROcp58_959
    sens.V[1] = VIcp58_158
    sens.V[2] = VIcp58_258
    sens.V[3] = VIcp58_358
    sens.OM[1] = OMcp58_159
    sens.OM[2] = OMcp58_259
    sens.OM[3] = OMcp58_359
    sens.A[1] = ACcp58_158
    sens.A[2] = ACcp58_258
    sens.A[3] = ACcp58_358
    sens.OMP[1] = OPcp58_159
    sens.OMP[2] = OPcp58_259
    sens.OMP[3] = OPcp58_359
 
# 
  elif(isens==60): 


# = = Block_1_0_0_60_0_1 = = 
 
# Sensor Kinematics 


    ROcp59_15 = C4*C5
    ROcp59_25 = S4*C5
    ROcp59_75 = C4*S5
    ROcp59_85 = S4*S5
    ROcp59_46 = ROcp59_75*S6-S4*C6
    ROcp59_56 = ROcp59_85*S6+C4*C6
    ROcp59_66 = C5*S6
    ROcp59_76 = ROcp59_75*C6+S4*S6
    ROcp59_86 = ROcp59_85*C6-C4*S6
    ROcp59_96 = C5*C6
    OMcp59_15 = -qd[5]*S4
    OMcp59_25 = qd[5]*C4
    OMcp59_16 = OMcp59_15+ROcp59_15*qd[6]
    OMcp59_26 = OMcp59_25+ROcp59_25*qd[6]
    OMcp59_36 = qd[4]-qd[6]*S5
    OPcp59_16 = ROcp59_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp59_25*S5+ROcp59_25*qd[4])
    OPcp59_26 = ROcp59_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp59_15*S5+ROcp59_15*qd[4])
    OPcp59_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_60_0_24 = = 
 
# Sensor Kinematics 


    ROcp59_160 = ROcp59_15*C60-ROcp59_76*S60
    ROcp59_260 = ROcp59_25*C60-ROcp59_86*S60
    ROcp59_360 = -(ROcp59_96*S60+S5*C60)
    ROcp59_760 = ROcp59_15*S60+ROcp59_76*C60
    ROcp59_860 = ROcp59_25*S60+ROcp59_86*C60
    ROcp59_960 = ROcp59_96*C60-S5*S60
    RLcp59_160 = ROcp59_15*s.dpt[1,15]+ROcp59_76*s.dpt[3,15]
    RLcp59_260 = ROcp59_25*s.dpt[1,15]+ROcp59_86*s.dpt[3,15]
    RLcp59_360 = ROcp59_96*s.dpt[3,15]-s.dpt[1,15]*S5
    POcp59_160 = RLcp59_160+q[1]
    POcp59_260 = RLcp59_260+q[2]
    POcp59_360 = RLcp59_360+q[3]
    OMcp59_160 = OMcp59_16+ROcp59_46*qd[60]
    OMcp59_260 = OMcp59_26+ROcp59_56*qd[60]
    OMcp59_360 = OMcp59_36+ROcp59_66*qd[60]
    ORcp59_160 = OMcp59_26*RLcp59_360-OMcp59_36*RLcp59_260
    ORcp59_260 = -(OMcp59_16*RLcp59_360-OMcp59_36*RLcp59_160)
    ORcp59_360 = OMcp59_16*RLcp59_260-OMcp59_26*RLcp59_160
    VIcp59_160 = ORcp59_160+qd[1]
    VIcp59_260 = ORcp59_260+qd[2]
    VIcp59_360 = ORcp59_360+qd[3]
    OPcp59_160 = OPcp59_16+ROcp59_46*qdd[60]+qd[60]*(OMcp59_26*ROcp59_66-OMcp59_36*ROcp59_56)
    OPcp59_260 = OPcp59_26+ROcp59_56*qdd[60]-qd[60]*(OMcp59_16*ROcp59_66-OMcp59_36*ROcp59_46)
    OPcp59_360 = OPcp59_36+ROcp59_66*qdd[60]+qd[60]*(OMcp59_16*ROcp59_56-OMcp59_26*ROcp59_46)
    ACcp59_160 = qdd[1]+OMcp59_26*ORcp59_360-OMcp59_36*ORcp59_260+OPcp59_26*RLcp59_360-OPcp59_36*RLcp59_260
    ACcp59_260 = qdd[2]-OMcp59_16*ORcp59_360+OMcp59_36*ORcp59_160-OPcp59_16*RLcp59_360+OPcp59_36*RLcp59_160
    ACcp59_360 = qdd[3]+OMcp59_16*ORcp59_260-OMcp59_26*ORcp59_160+OPcp59_16*RLcp59_260-OPcp59_26*RLcp59_160

# = = Block_1_0_0_60_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp59_160
    sens.P[2] = POcp59_260
    sens.P[3] = POcp59_360
    sens.R[1,1] = ROcp59_160
    sens.R[1,2] = ROcp59_260
    sens.R[1,3] = ROcp59_360
    sens.R[2,1] = ROcp59_46
    sens.R[2,2] = ROcp59_56
    sens.R[2,3] = ROcp59_66
    sens.R[3,1] = ROcp59_760
    sens.R[3,2] = ROcp59_860
    sens.R[3,3] = ROcp59_960
    sens.V[1] = VIcp59_160
    sens.V[2] = VIcp59_260
    sens.V[3] = VIcp59_360
    sens.OM[1] = OMcp59_160
    sens.OM[2] = OMcp59_260
    sens.OM[3] = OMcp59_360
    sens.A[1] = ACcp59_160
    sens.A[2] = ACcp59_260
    sens.A[3] = ACcp59_360
    sens.OMP[1] = OPcp59_160
    sens.OMP[2] = OPcp59_260
    sens.OMP[3] = OPcp59_360
 
# 
  elif(isens==61): 


# = = Block_1_0_0_61_0_1 = = 
 
# Sensor Kinematics 


    ROcp60_15 = C4*C5
    ROcp60_25 = S4*C5
    ROcp60_75 = C4*S5
    ROcp60_85 = S4*S5
    ROcp60_46 = ROcp60_75*S6-S4*C6
    ROcp60_56 = ROcp60_85*S6+C4*C6
    ROcp60_66 = C5*S6
    ROcp60_76 = ROcp60_75*C6+S4*S6
    ROcp60_86 = ROcp60_85*C6-C4*S6
    ROcp60_96 = C5*C6
    OMcp60_15 = -qd[5]*S4
    OMcp60_25 = qd[5]*C4
    OMcp60_16 = OMcp60_15+ROcp60_15*qd[6]
    OMcp60_26 = OMcp60_25+ROcp60_25*qd[6]
    OMcp60_36 = qd[4]-qd[6]*S5
    OPcp60_16 = ROcp60_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp60_25*S5+ROcp60_25*qd[4])
    OPcp60_26 = ROcp60_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp60_15*S5+ROcp60_15*qd[4])
    OPcp60_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_61_0_24 = = 
 
# Sensor Kinematics 


    ROcp60_160 = ROcp60_15*C60-ROcp60_76*S60
    ROcp60_260 = ROcp60_25*C60-ROcp60_86*S60
    ROcp60_360 = -(ROcp60_96*S60+S5*C60)
    ROcp60_760 = ROcp60_15*S60+ROcp60_76*C60
    ROcp60_860 = ROcp60_25*S60+ROcp60_86*C60
    ROcp60_960 = ROcp60_96*C60-S5*S60
    RLcp60_160 = ROcp60_15*s.dpt[1,15]+ROcp60_76*s.dpt[3,15]
    RLcp60_260 = ROcp60_25*s.dpt[1,15]+ROcp60_86*s.dpt[3,15]
    RLcp60_360 = ROcp60_96*s.dpt[3,15]-s.dpt[1,15]*S5
    POcp60_160 = RLcp60_160+q[1]
    POcp60_260 = RLcp60_260+q[2]
    POcp60_360 = RLcp60_360+q[3]
    OMcp60_160 = OMcp60_16+ROcp60_46*qd[60]
    OMcp60_260 = OMcp60_26+ROcp60_56*qd[60]
    OMcp60_360 = OMcp60_36+ROcp60_66*qd[60]
    ORcp60_160 = OMcp60_26*RLcp60_360-OMcp60_36*RLcp60_260
    ORcp60_260 = -(OMcp60_16*RLcp60_360-OMcp60_36*RLcp60_160)
    ORcp60_360 = OMcp60_16*RLcp60_260-OMcp60_26*RLcp60_160
    VIcp60_160 = ORcp60_160+qd[1]
    VIcp60_260 = ORcp60_260+qd[2]
    VIcp60_360 = ORcp60_360+qd[3]
    ACcp60_160 = qdd[1]+OMcp60_26*ORcp60_360-OMcp60_36*ORcp60_260+OPcp60_26*RLcp60_360-OPcp60_36*RLcp60_260
    ACcp60_260 = qdd[2]-OMcp60_16*ORcp60_360+OMcp60_36*ORcp60_160-OPcp60_16*RLcp60_360+OPcp60_36*RLcp60_160
    ACcp60_360 = qdd[3]+OMcp60_16*ORcp60_260-OMcp60_26*ORcp60_160+OPcp60_16*RLcp60_260-OPcp60_26*RLcp60_160

# = = Block_1_0_0_61_0_25 = = 
 
# Sensor Kinematics 


    ROcp60_161 = ROcp60_160*C61-ROcp60_760*S61
    ROcp60_261 = ROcp60_260*C61-ROcp60_860*S61
    ROcp60_361 = ROcp60_360*C61-ROcp60_960*S61
    ROcp60_761 = ROcp60_160*S61+ROcp60_760*C61
    ROcp60_861 = ROcp60_260*S61+ROcp60_860*C61
    ROcp60_961 = ROcp60_360*S61+ROcp60_960*C61
    OMcp60_161 = OMcp60_160+ROcp60_46*qd[61]
    OMcp60_261 = OMcp60_260+ROcp60_56*qd[61]
    OMcp60_361 = OMcp60_360+ROcp60_66*qd[61]
    OPcp60_161 = OPcp60_16+ROcp60_46*qdd[60]+ROcp60_46*qdd[61]+qd[60]*(OMcp60_26*ROcp60_66-OMcp60_36*ROcp60_56)+qd[61]*(\
   OMcp60_260*ROcp60_66-OMcp60_360*ROcp60_56)
    OPcp60_261 = OPcp60_26+ROcp60_56*qdd[60]+ROcp60_56*qdd[61]-qd[60]*(OMcp60_16*ROcp60_66-OMcp60_36*ROcp60_46)-qd[61]*(\
   OMcp60_160*ROcp60_66-OMcp60_360*ROcp60_46)
    OPcp60_361 = OPcp60_36+ROcp60_66*qdd[60]+ROcp60_66*qdd[61]+qd[60]*(OMcp60_16*ROcp60_56-OMcp60_26*ROcp60_46)+qd[61]*(\
   OMcp60_160*ROcp60_56-OMcp60_260*ROcp60_46)

# = = Block_1_0_0_61_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp60_160
    sens.P[2] = POcp60_260
    sens.P[3] = POcp60_360
    sens.R[1,1] = ROcp60_161
    sens.R[1,2] = ROcp60_261
    sens.R[1,3] = ROcp60_361
    sens.R[2,1] = ROcp60_46
    sens.R[2,2] = ROcp60_56
    sens.R[2,3] = ROcp60_66
    sens.R[3,1] = ROcp60_761
    sens.R[3,2] = ROcp60_861
    sens.R[3,3] = ROcp60_961
    sens.V[1] = VIcp60_160
    sens.V[2] = VIcp60_260
    sens.V[3] = VIcp60_360
    sens.OM[1] = OMcp60_161
    sens.OM[2] = OMcp60_261
    sens.OM[3] = OMcp60_361
    sens.A[1] = ACcp60_160
    sens.A[2] = ACcp60_260
    sens.A[3] = ACcp60_360
    sens.OMP[1] = OPcp60_161
    sens.OMP[2] = OPcp60_261
    sens.OMP[3] = OPcp60_361
 
# 
  elif(isens==62): 


# = = Block_1_0_0_62_0_1 = = 
 
# Sensor Kinematics 


    ROcp61_15 = C4*C5
    ROcp61_25 = S4*C5
    ROcp61_75 = C4*S5
    ROcp61_85 = S4*S5
    ROcp61_46 = ROcp61_75*S6-S4*C6
    ROcp61_56 = ROcp61_85*S6+C4*C6
    ROcp61_66 = C5*S6
    ROcp61_76 = ROcp61_75*C6+S4*S6
    ROcp61_86 = ROcp61_85*C6-C4*S6
    ROcp61_96 = C5*C6
    OMcp61_15 = -qd[5]*S4
    OMcp61_25 = qd[5]*C4
    OMcp61_16 = OMcp61_15+ROcp61_15*qd[6]
    OMcp61_26 = OMcp61_25+ROcp61_25*qd[6]
    OMcp61_36 = qd[4]-qd[6]*S5
    OPcp61_16 = ROcp61_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp61_25*S5+ROcp61_25*qd[4])
    OPcp61_26 = ROcp61_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp61_15*S5+ROcp61_15*qd[4])
    OPcp61_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_62_0_24 = = 
 
# Sensor Kinematics 


    ROcp61_160 = ROcp61_15*C60-ROcp61_76*S60
    ROcp61_260 = ROcp61_25*C60-ROcp61_86*S60
    ROcp61_360 = -(ROcp61_96*S60+S5*C60)
    ROcp61_760 = ROcp61_15*S60+ROcp61_76*C60
    ROcp61_860 = ROcp61_25*S60+ROcp61_86*C60
    ROcp61_960 = ROcp61_96*C60-S5*S60
    RLcp61_160 = ROcp61_15*s.dpt[1,15]+ROcp61_76*s.dpt[3,15]
    RLcp61_260 = ROcp61_25*s.dpt[1,15]+ROcp61_86*s.dpt[3,15]
    RLcp61_360 = ROcp61_96*s.dpt[3,15]-s.dpt[1,15]*S5
    OMcp61_160 = OMcp61_16+ROcp61_46*qd[60]
    OMcp61_260 = OMcp61_26+ROcp61_56*qd[60]
    OMcp61_360 = OMcp61_36+ROcp61_66*qd[60]
    ORcp61_160 = OMcp61_26*RLcp61_360-OMcp61_36*RLcp61_260
    ORcp61_260 = -(OMcp61_16*RLcp61_360-OMcp61_36*RLcp61_160)
    ORcp61_360 = OMcp61_16*RLcp61_260-OMcp61_26*RLcp61_160

# = = Block_1_0_0_62_0_25 = = 
 
# Sensor Kinematics 


    ROcp61_161 = ROcp61_160*C61-ROcp61_760*S61
    ROcp61_261 = ROcp61_260*C61-ROcp61_860*S61
    ROcp61_361 = ROcp61_360*C61-ROcp61_960*S61
    ROcp61_761 = ROcp61_160*S61+ROcp61_760*C61
    ROcp61_861 = ROcp61_260*S61+ROcp61_860*C61
    ROcp61_961 = ROcp61_360*S61+ROcp61_960*C61
    ROcp61_162 = ROcp61_161*C62-ROcp61_761*S62
    ROcp61_262 = ROcp61_261*C62-ROcp61_861*S62
    ROcp61_362 = ROcp61_361*C62-ROcp61_961*S62
    ROcp61_762 = ROcp61_161*S62+ROcp61_761*C62
    ROcp61_862 = ROcp61_261*S62+ROcp61_861*C62
    ROcp61_962 = ROcp61_361*S62+ROcp61_961*C62
    OMcp61_161 = OMcp61_160+ROcp61_46*qd[61]
    OMcp61_261 = OMcp61_260+ROcp61_56*qd[61]
    OMcp61_361 = OMcp61_360+ROcp61_66*qd[61]
    OPcp61_161 = OPcp61_16+ROcp61_46*qdd[60]+ROcp61_46*qdd[61]+qd[60]*(OMcp61_26*ROcp61_66-OMcp61_36*ROcp61_56)+qd[61]*(\
   OMcp61_260*ROcp61_66-OMcp61_360*ROcp61_56)
    OPcp61_261 = OPcp61_26+ROcp61_56*qdd[60]+ROcp61_56*qdd[61]-qd[60]*(OMcp61_16*ROcp61_66-OMcp61_36*ROcp61_46)-qd[61]*(\
   OMcp61_160*ROcp61_66-OMcp61_360*ROcp61_46)
    OPcp61_361 = OPcp61_36+ROcp61_66*qdd[60]+ROcp61_66*qdd[61]+qd[60]*(OMcp61_16*ROcp61_56-OMcp61_26*ROcp61_46)+qd[61]*(\
   OMcp61_160*ROcp61_56-OMcp61_260*ROcp61_46)
    RLcp61_162 = ROcp61_161*s.dpt[1,59]+ROcp61_46*s.dpt[2,59]
    RLcp61_262 = ROcp61_261*s.dpt[1,59]+ROcp61_56*s.dpt[2,59]
    RLcp61_362 = ROcp61_361*s.dpt[1,59]+ROcp61_66*s.dpt[2,59]
    POcp61_162 = RLcp61_160+RLcp61_162+q[1]
    POcp61_262 = RLcp61_260+RLcp61_262+q[2]
    POcp61_362 = RLcp61_360+RLcp61_362+q[3]
    OMcp61_162 = OMcp61_161+ROcp61_46*qd[62]
    OMcp61_262 = OMcp61_261+ROcp61_56*qd[62]
    OMcp61_362 = OMcp61_361+ROcp61_66*qd[62]
    ORcp61_162 = OMcp61_261*RLcp61_362-OMcp61_361*RLcp61_262
    ORcp61_262 = -(OMcp61_161*RLcp61_362-OMcp61_361*RLcp61_162)
    ORcp61_362 = OMcp61_161*RLcp61_262-OMcp61_261*RLcp61_162
    VIcp61_162 = ORcp61_160+ORcp61_162+qd[1]
    VIcp61_262 = ORcp61_260+ORcp61_262+qd[2]
    VIcp61_362 = ORcp61_360+ORcp61_362+qd[3]
    OPcp61_162 = OPcp61_161+ROcp61_46*qdd[62]+qd[62]*(OMcp61_261*ROcp61_66-OMcp61_361*ROcp61_56)
    OPcp61_262 = OPcp61_261+ROcp61_56*qdd[62]-qd[62]*(OMcp61_161*ROcp61_66-OMcp61_361*ROcp61_46)
    OPcp61_362 = OPcp61_361+ROcp61_66*qdd[62]+qd[62]*(OMcp61_161*ROcp61_56-OMcp61_261*ROcp61_46)
    ACcp61_162 = qdd[1]+OMcp61_26*ORcp61_360+OMcp61_261*ORcp61_362-OMcp61_36*ORcp61_260-OMcp61_361*ORcp61_262+OPcp61_26*\
   RLcp61_360+OPcp61_261*RLcp61_362-OPcp61_36*RLcp61_260-OPcp61_361*RLcp61_262
    ACcp61_262 = qdd[2]-OMcp61_16*ORcp61_360-OMcp61_161*ORcp61_362+OMcp61_36*ORcp61_160+OMcp61_361*ORcp61_162-OPcp61_16*\
   RLcp61_360-OPcp61_161*RLcp61_362+OPcp61_36*RLcp61_160+OPcp61_361*RLcp61_162
    ACcp61_362 = qdd[3]+OMcp61_16*ORcp61_260+OMcp61_161*ORcp61_262-OMcp61_26*ORcp61_160-OMcp61_261*ORcp61_162+OPcp61_16*\
   RLcp61_260+OPcp61_161*RLcp61_262-OPcp61_26*RLcp61_160-OPcp61_261*RLcp61_162

# = = Block_1_0_0_62_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp61_162
    sens.P[2] = POcp61_262
    sens.P[3] = POcp61_362
    sens.R[1,1] = ROcp61_162
    sens.R[1,2] = ROcp61_262
    sens.R[1,3] = ROcp61_362
    sens.R[2,1] = ROcp61_46
    sens.R[2,2] = ROcp61_56
    sens.R[2,3] = ROcp61_66
    sens.R[3,1] = ROcp61_762
    sens.R[3,2] = ROcp61_862
    sens.R[3,3] = ROcp61_962
    sens.V[1] = VIcp61_162
    sens.V[2] = VIcp61_262
    sens.V[3] = VIcp61_362
    sens.OM[1] = OMcp61_162
    sens.OM[2] = OMcp61_262
    sens.OM[3] = OMcp61_362
    sens.A[1] = ACcp61_162
    sens.A[2] = ACcp61_262
    sens.A[3] = ACcp61_362
    sens.OMP[1] = OPcp61_162
    sens.OMP[2] = OPcp61_262
    sens.OMP[3] = OPcp61_362
 
# 
  elif(isens==63): 


# = = Block_1_0_0_63_0_1 = = 
 
# Sensor Kinematics 


    ROcp62_15 = C4*C5
    ROcp62_25 = S4*C5
    ROcp62_75 = C4*S5
    ROcp62_85 = S4*S5
    ROcp62_46 = ROcp62_75*S6-S4*C6
    ROcp62_56 = ROcp62_85*S6+C4*C6
    ROcp62_66 = C5*S6
    ROcp62_76 = ROcp62_75*C6+S4*S6
    ROcp62_86 = ROcp62_85*C6-C4*S6
    ROcp62_96 = C5*C6
    OMcp62_15 = -qd[5]*S4
    OMcp62_25 = qd[5]*C4
    OMcp62_16 = OMcp62_15+ROcp62_15*qd[6]
    OMcp62_26 = OMcp62_25+ROcp62_25*qd[6]
    OMcp62_36 = qd[4]-qd[6]*S5
    OPcp62_16 = ROcp62_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp62_25*S5+ROcp62_25*qd[4])
    OPcp62_26 = ROcp62_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp62_15*S5+ROcp62_15*qd[4])
    OPcp62_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_63_0_24 = = 
 
# Sensor Kinematics 


    ROcp62_160 = ROcp62_15*C60-ROcp62_76*S60
    ROcp62_260 = ROcp62_25*C60-ROcp62_86*S60
    ROcp62_360 = -(ROcp62_96*S60+S5*C60)
    ROcp62_760 = ROcp62_15*S60+ROcp62_76*C60
    ROcp62_860 = ROcp62_25*S60+ROcp62_86*C60
    ROcp62_960 = ROcp62_96*C60-S5*S60
    RLcp62_160 = ROcp62_15*s.dpt[1,15]+ROcp62_76*s.dpt[3,15]
    RLcp62_260 = ROcp62_25*s.dpt[1,15]+ROcp62_86*s.dpt[3,15]
    RLcp62_360 = ROcp62_96*s.dpt[3,15]-s.dpt[1,15]*S5
    OMcp62_160 = OMcp62_16+ROcp62_46*qd[60]
    OMcp62_260 = OMcp62_26+ROcp62_56*qd[60]
    OMcp62_360 = OMcp62_36+ROcp62_66*qd[60]
    ORcp62_160 = OMcp62_26*RLcp62_360-OMcp62_36*RLcp62_260
    ORcp62_260 = -(OMcp62_16*RLcp62_360-OMcp62_36*RLcp62_160)
    ORcp62_360 = OMcp62_16*RLcp62_260-OMcp62_26*RLcp62_160

# = = Block_1_0_0_63_0_25 = = 
 
# Sensor Kinematics 


    ROcp62_161 = ROcp62_160*C61-ROcp62_760*S61
    ROcp62_261 = ROcp62_260*C61-ROcp62_860*S61
    ROcp62_361 = ROcp62_360*C61-ROcp62_960*S61
    ROcp62_761 = ROcp62_160*S61+ROcp62_760*C61
    ROcp62_861 = ROcp62_260*S61+ROcp62_860*C61
    ROcp62_961 = ROcp62_360*S61+ROcp62_960*C61
    ROcp62_162 = ROcp62_161*C62-ROcp62_761*S62
    ROcp62_262 = ROcp62_261*C62-ROcp62_861*S62
    ROcp62_362 = ROcp62_361*C62-ROcp62_961*S62
    ROcp62_762 = ROcp62_161*S62+ROcp62_761*C62
    ROcp62_862 = ROcp62_261*S62+ROcp62_861*C62
    ROcp62_962 = ROcp62_361*S62+ROcp62_961*C62
    ROcp62_463 = ROcp62_46*C63+ROcp62_762*S63
    ROcp62_563 = ROcp62_56*C63+ROcp62_862*S63
    ROcp62_663 = ROcp62_66*C63+ROcp62_962*S63
    ROcp62_763 = -(ROcp62_46*S63-ROcp62_762*C63)
    ROcp62_863 = -(ROcp62_56*S63-ROcp62_862*C63)
    ROcp62_963 = -(ROcp62_66*S63-ROcp62_962*C63)
    OMcp62_161 = OMcp62_160+ROcp62_46*qd[61]
    OMcp62_261 = OMcp62_260+ROcp62_56*qd[61]
    OMcp62_361 = OMcp62_360+ROcp62_66*qd[61]
    OPcp62_161 = OPcp62_16+ROcp62_46*qdd[60]+ROcp62_46*qdd[61]+qd[60]*(OMcp62_26*ROcp62_66-OMcp62_36*ROcp62_56)+qd[61]*(\
   OMcp62_260*ROcp62_66-OMcp62_360*ROcp62_56)
    OPcp62_261 = OPcp62_26+ROcp62_56*qdd[60]+ROcp62_56*qdd[61]-qd[60]*(OMcp62_16*ROcp62_66-OMcp62_36*ROcp62_46)-qd[61]*(\
   OMcp62_160*ROcp62_66-OMcp62_360*ROcp62_46)
    OPcp62_361 = OPcp62_36+ROcp62_66*qdd[60]+ROcp62_66*qdd[61]+qd[60]*(OMcp62_16*ROcp62_56-OMcp62_26*ROcp62_46)+qd[61]*(\
   OMcp62_160*ROcp62_56-OMcp62_260*ROcp62_46)
    RLcp62_162 = ROcp62_161*s.dpt[1,59]+ROcp62_46*s.dpt[2,59]
    RLcp62_262 = ROcp62_261*s.dpt[1,59]+ROcp62_56*s.dpt[2,59]
    RLcp62_362 = ROcp62_361*s.dpt[1,59]+ROcp62_66*s.dpt[2,59]
    POcp62_162 = RLcp62_160+RLcp62_162+q[1]
    POcp62_262 = RLcp62_260+RLcp62_262+q[2]
    POcp62_362 = RLcp62_360+RLcp62_362+q[3]
    OMcp62_162 = OMcp62_161+ROcp62_46*qd[62]
    OMcp62_262 = OMcp62_261+ROcp62_56*qd[62]
    OMcp62_362 = OMcp62_361+ROcp62_66*qd[62]
    ORcp62_162 = OMcp62_261*RLcp62_362-OMcp62_361*RLcp62_262
    ORcp62_262 = -(OMcp62_161*RLcp62_362-OMcp62_361*RLcp62_162)
    ORcp62_362 = OMcp62_161*RLcp62_262-OMcp62_261*RLcp62_162
    VIcp62_162 = ORcp62_160+ORcp62_162+qd[1]
    VIcp62_262 = ORcp62_260+ORcp62_262+qd[2]
    VIcp62_362 = ORcp62_360+ORcp62_362+qd[3]
    ACcp62_162 = qdd[1]+OMcp62_26*ORcp62_360+OMcp62_261*ORcp62_362-OMcp62_36*ORcp62_260-OMcp62_361*ORcp62_262+OPcp62_26*\
   RLcp62_360+OPcp62_261*RLcp62_362-OPcp62_36*RLcp62_260-OPcp62_361*RLcp62_262
    ACcp62_262 = qdd[2]-OMcp62_16*ORcp62_360-OMcp62_161*ORcp62_362+OMcp62_36*ORcp62_160+OMcp62_361*ORcp62_162-OPcp62_16*\
   RLcp62_360-OPcp62_161*RLcp62_362+OPcp62_36*RLcp62_160+OPcp62_361*RLcp62_162
    ACcp62_362 = qdd[3]+OMcp62_16*ORcp62_260+OMcp62_161*ORcp62_262-OMcp62_26*ORcp62_160-OMcp62_261*ORcp62_162+OPcp62_16*\
   RLcp62_260+OPcp62_161*RLcp62_262-OPcp62_26*RLcp62_160-OPcp62_261*RLcp62_162
    OMcp62_163 = OMcp62_162+ROcp62_162*qd[63]
    OMcp62_263 = OMcp62_262+ROcp62_262*qd[63]
    OMcp62_363 = OMcp62_362+ROcp62_362*qd[63]
    OPcp62_163 = OPcp62_161+ROcp62_162*qdd[63]+ROcp62_46*qdd[62]+qd[62]*(OMcp62_261*ROcp62_66-OMcp62_361*ROcp62_56)+qd[63]\
   *(OMcp62_262*ROcp62_362-OMcp62_362*ROcp62_262)
    OPcp62_263 = OPcp62_261+ROcp62_262*qdd[63]+ROcp62_56*qdd[62]-qd[62]*(OMcp62_161*ROcp62_66-OMcp62_361*ROcp62_46)-qd[63]\
   *(OMcp62_162*ROcp62_362-OMcp62_362*ROcp62_162)
    OPcp62_363 = OPcp62_361+ROcp62_362*qdd[63]+ROcp62_66*qdd[62]+qd[62]*(OMcp62_161*ROcp62_56-OMcp62_261*ROcp62_46)+qd[63]\
   *(OMcp62_162*ROcp62_262-OMcp62_262*ROcp62_162)

# = = Block_1_0_0_63_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp62_162
    sens.P[2] = POcp62_262
    sens.P[3] = POcp62_362
    sens.R[1,1] = ROcp62_162
    sens.R[1,2] = ROcp62_262
    sens.R[1,3] = ROcp62_362
    sens.R[2,1] = ROcp62_463
    sens.R[2,2] = ROcp62_563
    sens.R[2,3] = ROcp62_663
    sens.R[3,1] = ROcp62_763
    sens.R[3,2] = ROcp62_863
    sens.R[3,3] = ROcp62_963
    sens.V[1] = VIcp62_162
    sens.V[2] = VIcp62_262
    sens.V[3] = VIcp62_362
    sens.OM[1] = OMcp62_163
    sens.OM[2] = OMcp62_263
    sens.OM[3] = OMcp62_363
    sens.A[1] = ACcp62_162
    sens.A[2] = ACcp62_262
    sens.A[3] = ACcp62_362
    sens.OMP[1] = OPcp62_163
    sens.OMP[2] = OPcp62_263
    sens.OMP[3] = OPcp62_363
 
# 
  elif(isens==64): 


# = = Block_1_0_0_64_0_1 = = 
 
# Sensor Kinematics 


    ROcp63_15 = C4*C5
    ROcp63_25 = S4*C5
    ROcp63_75 = C4*S5
    ROcp63_85 = S4*S5
    ROcp63_46 = ROcp63_75*S6-S4*C6
    ROcp63_56 = ROcp63_85*S6+C4*C6
    ROcp63_66 = C5*S6
    ROcp63_76 = ROcp63_75*C6+S4*S6
    ROcp63_86 = ROcp63_85*C6-C4*S6
    ROcp63_96 = C5*C6
    OMcp63_15 = -qd[5]*S4
    OMcp63_25 = qd[5]*C4
    OMcp63_16 = OMcp63_15+ROcp63_15*qd[6]
    OMcp63_26 = OMcp63_25+ROcp63_25*qd[6]
    OMcp63_36 = qd[4]-qd[6]*S5
    OPcp63_16 = ROcp63_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp63_25*S5+ROcp63_25*qd[4])
    OPcp63_26 = ROcp63_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp63_15*S5+ROcp63_15*qd[4])
    OPcp63_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_64_0_24 = = 
 
# Sensor Kinematics 


    ROcp63_160 = ROcp63_15*C60-ROcp63_76*S60
    ROcp63_260 = ROcp63_25*C60-ROcp63_86*S60
    ROcp63_360 = -(ROcp63_96*S60+S5*C60)
    ROcp63_760 = ROcp63_15*S60+ROcp63_76*C60
    ROcp63_860 = ROcp63_25*S60+ROcp63_86*C60
    ROcp63_960 = ROcp63_96*C60-S5*S60
    RLcp63_160 = ROcp63_15*s.dpt[1,15]+ROcp63_76*s.dpt[3,15]
    RLcp63_260 = ROcp63_25*s.dpt[1,15]+ROcp63_86*s.dpt[3,15]
    RLcp63_360 = ROcp63_96*s.dpt[3,15]-s.dpt[1,15]*S5
    OMcp63_160 = OMcp63_16+ROcp63_46*qd[60]
    OMcp63_260 = OMcp63_26+ROcp63_56*qd[60]
    OMcp63_360 = OMcp63_36+ROcp63_66*qd[60]
    ORcp63_160 = OMcp63_26*RLcp63_360-OMcp63_36*RLcp63_260
    ORcp63_260 = -(OMcp63_16*RLcp63_360-OMcp63_36*RLcp63_160)
    ORcp63_360 = OMcp63_16*RLcp63_260-OMcp63_26*RLcp63_160
    OPcp63_160 = OPcp63_16+ROcp63_46*qdd[60]+qd[60]*(OMcp63_26*ROcp63_66-OMcp63_36*ROcp63_56)
    OPcp63_260 = OPcp63_26+ROcp63_56*qdd[60]-qd[60]*(OMcp63_16*ROcp63_66-OMcp63_36*ROcp63_46)
    OPcp63_360 = OPcp63_36+ROcp63_66*qdd[60]+qd[60]*(OMcp63_16*ROcp63_56-OMcp63_26*ROcp63_46)

# = = Block_1_0_0_64_0_26 = = 
 
# Sensor Kinematics 


    ROcp63_164 = ROcp63_160*C64-ROcp63_760*S64
    ROcp63_264 = ROcp63_260*C64-ROcp63_860*S64
    ROcp63_364 = ROcp63_360*C64-ROcp63_960*S64
    ROcp63_764 = ROcp63_160*S64+ROcp63_760*C64
    ROcp63_864 = ROcp63_260*S64+ROcp63_860*C64
    ROcp63_964 = ROcp63_360*S64+ROcp63_960*C64
    RLcp63_164 = ROcp63_160*s.dpt[1,58]+ROcp63_46*s.dpt[2,58]
    RLcp63_264 = ROcp63_260*s.dpt[1,58]+ROcp63_56*s.dpt[2,58]
    RLcp63_364 = ROcp63_360*s.dpt[1,58]+ROcp63_66*s.dpt[2,58]
    POcp63_164 = RLcp63_160+RLcp63_164+q[1]
    POcp63_264 = RLcp63_260+RLcp63_264+q[2]
    POcp63_364 = RLcp63_360+RLcp63_364+q[3]
    OMcp63_164 = OMcp63_160+ROcp63_46*qd[64]
    OMcp63_264 = OMcp63_260+ROcp63_56*qd[64]
    OMcp63_364 = OMcp63_360+ROcp63_66*qd[64]
    ORcp63_164 = OMcp63_260*RLcp63_364-OMcp63_360*RLcp63_264
    ORcp63_264 = -(OMcp63_160*RLcp63_364-OMcp63_360*RLcp63_164)
    ORcp63_364 = OMcp63_160*RLcp63_264-OMcp63_260*RLcp63_164
    VIcp63_164 = ORcp63_160+ORcp63_164+qd[1]
    VIcp63_264 = ORcp63_260+ORcp63_264+qd[2]
    VIcp63_364 = ORcp63_360+ORcp63_364+qd[3]
    OPcp63_164 = OPcp63_160+ROcp63_46*qdd[64]+qd[64]*(OMcp63_260*ROcp63_66-OMcp63_360*ROcp63_56)
    OPcp63_264 = OPcp63_260+ROcp63_56*qdd[64]-qd[64]*(OMcp63_160*ROcp63_66-OMcp63_360*ROcp63_46)
    OPcp63_364 = OPcp63_360+ROcp63_66*qdd[64]+qd[64]*(OMcp63_160*ROcp63_56-OMcp63_260*ROcp63_46)
    ACcp63_164 = qdd[1]+OMcp63_26*ORcp63_360+OMcp63_260*ORcp63_364-OMcp63_36*ORcp63_260-OMcp63_360*ORcp63_264+OPcp63_26*\
   RLcp63_360+OPcp63_260*RLcp63_364-OPcp63_36*RLcp63_260-OPcp63_360*RLcp63_264
    ACcp63_264 = qdd[2]-OMcp63_16*ORcp63_360-OMcp63_160*ORcp63_364+OMcp63_36*ORcp63_160+OMcp63_360*ORcp63_164-OPcp63_16*\
   RLcp63_360-OPcp63_160*RLcp63_364+OPcp63_36*RLcp63_160+OPcp63_360*RLcp63_164
    ACcp63_364 = qdd[3]+OMcp63_16*ORcp63_260+OMcp63_160*ORcp63_264-OMcp63_26*ORcp63_160-OMcp63_260*ORcp63_164+OPcp63_16*\
   RLcp63_260+OPcp63_160*RLcp63_264-OPcp63_26*RLcp63_160-OPcp63_260*RLcp63_164

# = = Block_1_0_0_64_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp63_164
    sens.P[2] = POcp63_264
    sens.P[3] = POcp63_364
    sens.R[1,1] = ROcp63_164
    sens.R[1,2] = ROcp63_264
    sens.R[1,3] = ROcp63_364
    sens.R[2,1] = ROcp63_46
    sens.R[2,2] = ROcp63_56
    sens.R[2,3] = ROcp63_66
    sens.R[3,1] = ROcp63_764
    sens.R[3,2] = ROcp63_864
    sens.R[3,3] = ROcp63_964
    sens.V[1] = VIcp63_164
    sens.V[2] = VIcp63_264
    sens.V[3] = VIcp63_364
    sens.OM[1] = OMcp63_164
    sens.OM[2] = OMcp63_264
    sens.OM[3] = OMcp63_364
    sens.A[1] = ACcp63_164
    sens.A[2] = ACcp63_264
    sens.A[3] = ACcp63_364
    sens.OMP[1] = OPcp63_164
    sens.OMP[2] = OPcp63_264
    sens.OMP[3] = OPcp63_364
 
# 
  elif(isens==65): 


# = = Block_1_0_0_65_0_1 = = 
 
# Sensor Kinematics 


    ROcp64_15 = C4*C5
    ROcp64_25 = S4*C5
    ROcp64_75 = C4*S5
    ROcp64_85 = S4*S5
    ROcp64_46 = ROcp64_75*S6-S4*C6
    ROcp64_56 = ROcp64_85*S6+C4*C6
    ROcp64_66 = C5*S6
    ROcp64_76 = ROcp64_75*C6+S4*S6
    ROcp64_86 = ROcp64_85*C6-C4*S6
    ROcp64_96 = C5*C6
    OMcp64_15 = -qd[5]*S4
    OMcp64_25 = qd[5]*C4
    OMcp64_16 = OMcp64_15+ROcp64_15*qd[6]
    OMcp64_26 = OMcp64_25+ROcp64_25*qd[6]
    OMcp64_36 = qd[4]-qd[6]*S5
    OPcp64_16 = ROcp64_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp64_25*S5+ROcp64_25*qd[4])
    OPcp64_26 = ROcp64_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp64_15*S5+ROcp64_15*qd[4])
    OPcp64_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_65_0_24 = = 
 
# Sensor Kinematics 


    ROcp64_160 = ROcp64_15*C60-ROcp64_76*S60
    ROcp64_260 = ROcp64_25*C60-ROcp64_86*S60
    ROcp64_360 = -(ROcp64_96*S60+S5*C60)
    ROcp64_760 = ROcp64_15*S60+ROcp64_76*C60
    ROcp64_860 = ROcp64_25*S60+ROcp64_86*C60
    ROcp64_960 = ROcp64_96*C60-S5*S60
    RLcp64_160 = ROcp64_15*s.dpt[1,15]+ROcp64_76*s.dpt[3,15]
    RLcp64_260 = ROcp64_25*s.dpt[1,15]+ROcp64_86*s.dpt[3,15]
    RLcp64_360 = ROcp64_96*s.dpt[3,15]-s.dpt[1,15]*S5
    OMcp64_160 = OMcp64_16+ROcp64_46*qd[60]
    OMcp64_260 = OMcp64_26+ROcp64_56*qd[60]
    OMcp64_360 = OMcp64_36+ROcp64_66*qd[60]
    ORcp64_160 = OMcp64_26*RLcp64_360-OMcp64_36*RLcp64_260
    ORcp64_260 = -(OMcp64_16*RLcp64_360-OMcp64_36*RLcp64_160)
    ORcp64_360 = OMcp64_16*RLcp64_260-OMcp64_26*RLcp64_160
    OPcp64_160 = OPcp64_16+ROcp64_46*qdd[60]+qd[60]*(OMcp64_26*ROcp64_66-OMcp64_36*ROcp64_56)
    OPcp64_260 = OPcp64_26+ROcp64_56*qdd[60]-qd[60]*(OMcp64_16*ROcp64_66-OMcp64_36*ROcp64_46)
    OPcp64_360 = OPcp64_36+ROcp64_66*qdd[60]+qd[60]*(OMcp64_16*ROcp64_56-OMcp64_26*ROcp64_46)

# = = Block_1_0_0_65_0_26 = = 
 
# Sensor Kinematics 


    ROcp64_164 = ROcp64_160*C64-ROcp64_760*S64
    ROcp64_264 = ROcp64_260*C64-ROcp64_860*S64
    ROcp64_364 = ROcp64_360*C64-ROcp64_960*S64
    ROcp64_764 = ROcp64_160*S64+ROcp64_760*C64
    ROcp64_864 = ROcp64_260*S64+ROcp64_860*C64
    ROcp64_964 = ROcp64_360*S64+ROcp64_960*C64
    ROcp64_465 = ROcp64_46*C65+ROcp64_764*S65
    ROcp64_565 = ROcp64_56*C65+ROcp64_864*S65
    ROcp64_665 = ROcp64_66*C65+ROcp64_964*S65
    ROcp64_765 = -(ROcp64_46*S65-ROcp64_764*C65)
    ROcp64_865 = -(ROcp64_56*S65-ROcp64_864*C65)
    ROcp64_965 = -(ROcp64_66*S65-ROcp64_964*C65)
    RLcp64_164 = ROcp64_160*s.dpt[1,58]+ROcp64_46*s.dpt[2,58]
    RLcp64_264 = ROcp64_260*s.dpt[1,58]+ROcp64_56*s.dpt[2,58]
    RLcp64_364 = ROcp64_360*s.dpt[1,58]+ROcp64_66*s.dpt[2,58]
    POcp64_164 = RLcp64_160+RLcp64_164+q[1]
    POcp64_264 = RLcp64_260+RLcp64_264+q[2]
    POcp64_364 = RLcp64_360+RLcp64_364+q[3]
    OMcp64_164 = OMcp64_160+ROcp64_46*qd[64]
    OMcp64_264 = OMcp64_260+ROcp64_56*qd[64]
    OMcp64_364 = OMcp64_360+ROcp64_66*qd[64]
    ORcp64_164 = OMcp64_260*RLcp64_364-OMcp64_360*RLcp64_264
    ORcp64_264 = -(OMcp64_160*RLcp64_364-OMcp64_360*RLcp64_164)
    ORcp64_364 = OMcp64_160*RLcp64_264-OMcp64_260*RLcp64_164
    VIcp64_164 = ORcp64_160+ORcp64_164+qd[1]
    VIcp64_264 = ORcp64_260+ORcp64_264+qd[2]
    VIcp64_364 = ORcp64_360+ORcp64_364+qd[3]
    ACcp64_164 = qdd[1]+OMcp64_26*ORcp64_360+OMcp64_260*ORcp64_364-OMcp64_36*ORcp64_260-OMcp64_360*ORcp64_264+OPcp64_26*\
   RLcp64_360+OPcp64_260*RLcp64_364-OPcp64_36*RLcp64_260-OPcp64_360*RLcp64_264
    ACcp64_264 = qdd[2]-OMcp64_16*ORcp64_360-OMcp64_160*ORcp64_364+OMcp64_36*ORcp64_160+OMcp64_360*ORcp64_164-OPcp64_16*\
   RLcp64_360-OPcp64_160*RLcp64_364+OPcp64_36*RLcp64_160+OPcp64_360*RLcp64_164
    ACcp64_364 = qdd[3]+OMcp64_16*ORcp64_260+OMcp64_160*ORcp64_264-OMcp64_26*ORcp64_160-OMcp64_260*ORcp64_164+OPcp64_16*\
   RLcp64_260+OPcp64_160*RLcp64_264-OPcp64_26*RLcp64_160-OPcp64_260*RLcp64_164
    OMcp64_165 = OMcp64_164+ROcp64_164*qd[65]
    OMcp64_265 = OMcp64_264+ROcp64_264*qd[65]
    OMcp64_365 = OMcp64_364+ROcp64_364*qd[65]
    OPcp64_165 = OPcp64_160+ROcp64_164*qdd[65]+ROcp64_46*qdd[64]+qd[64]*(OMcp64_260*ROcp64_66-OMcp64_360*ROcp64_56)+qd[65]\
   *(OMcp64_264*ROcp64_364-OMcp64_364*ROcp64_264)
    OPcp64_265 = OPcp64_260+ROcp64_264*qdd[65]+ROcp64_56*qdd[64]-qd[64]*(OMcp64_160*ROcp64_66-OMcp64_360*ROcp64_46)-qd[65]\
   *(OMcp64_164*ROcp64_364-OMcp64_364*ROcp64_164)
    OPcp64_365 = OPcp64_360+ROcp64_364*qdd[65]+ROcp64_66*qdd[64]+qd[64]*(OMcp64_160*ROcp64_56-OMcp64_260*ROcp64_46)+qd[65]\
   *(OMcp64_164*ROcp64_264-OMcp64_264*ROcp64_164)

# = = Block_1_0_0_65_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp64_164
    sens.P[2] = POcp64_264
    sens.P[3] = POcp64_364
    sens.R[1,1] = ROcp64_164
    sens.R[1,2] = ROcp64_264
    sens.R[1,3] = ROcp64_364
    sens.R[2,1] = ROcp64_465
    sens.R[2,2] = ROcp64_565
    sens.R[2,3] = ROcp64_665
    sens.R[3,1] = ROcp64_765
    sens.R[3,2] = ROcp64_865
    sens.R[3,3] = ROcp64_965
    sens.V[1] = VIcp64_164
    sens.V[2] = VIcp64_264
    sens.V[3] = VIcp64_364
    sens.OM[1] = OMcp64_165
    sens.OM[2] = OMcp64_265
    sens.OM[3] = OMcp64_365
    sens.A[1] = ACcp64_164
    sens.A[2] = ACcp64_264
    sens.A[3] = ACcp64_364
    sens.OMP[1] = OPcp64_165
    sens.OMP[2] = OPcp64_265
    sens.OMP[3] = OPcp64_365



# ====== END Task 1 ====== 

  

