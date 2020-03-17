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
#	==> Flops complexity : 4516
#
#	==> Generation Time :  0.120 seconds
#	==> Post-Processing :  0.080 seconds
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
    sens.R[1,1] = (1.0)
    sens.R[2,2] = C4
    sens.R[2,3] = S4
    sens.R[3,2] = -S4
    sens.R[3,3] = C4
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.V[3] = qd[3]
    sens.OM[1] = qd[4]
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
    sens.A[3] = qdd[3]
    sens.OMP[1] = qdd[4]
 
# 
  elif(isens==5): 


# = = Block_1_0_0_5_0_1 = = 
 
# Sensor Kinematics 


    ROcp4_25 = S4*S5
    ROcp4_35 = -C4*S5
    ROcp4_85 = -S4*C5
    ROcp4_95 = C4*C5
    OMcp4_25 = qd[5]*C4
    OMcp4_35 = qd[5]*S4
    OPcp4_25 = qdd[5]*C4-qd[4]*qd[5]*S4
    OPcp4_35 = qdd[5]*S4+qd[4]*qd[5]*C4

# = = Block_1_0_0_5_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = C5
    sens.R[1,2] = ROcp4_25
    sens.R[1,3] = ROcp4_35
    sens.R[2,2] = C4
    sens.R[2,3] = S4
    sens.R[3,1] = S5
    sens.R[3,2] = ROcp4_85
    sens.R[3,3] = ROcp4_95
    sens.V[1] = qd[1]
    sens.V[2] = qd[2]
    sens.V[3] = qd[3]
    sens.OM[1] = qd[4]
    sens.OM[2] = OMcp4_25
    sens.OM[3] = OMcp4_35
    sens.A[1] = qdd[1]
    sens.A[2] = qdd[2]
    sens.A[3] = qdd[3]
    sens.OMP[1] = qdd[4]
    sens.OMP[2] = OPcp4_25
    sens.OMP[3] = OPcp4_35
 
# 
  elif(isens==6): 


# = = Block_1_0_0_6_0_1 = = 
 
# Sensor Kinematics 


    ROcp5_25 = S4*S5
    ROcp5_35 = -C4*S5
    ROcp5_85 = -S4*C5
    ROcp5_95 = C4*C5
    ROcp5_16 = C5*C6
    ROcp5_26 = ROcp5_25*C6+C4*S6
    ROcp5_36 = ROcp5_35*C6+S4*S6
    ROcp5_46 = -C5*S6
    ROcp5_56 = -(ROcp5_25*S6-C4*C6)
    ROcp5_66 = -(ROcp5_35*S6-S4*C6)
    OMcp5_25 = qd[5]*C4
    OMcp5_35 = qd[5]*S4
    OMcp5_16 = qd[4]+qd[6]*S5
    OMcp5_26 = OMcp5_25+ROcp5_85*qd[6]
    OMcp5_36 = OMcp5_35+ROcp5_95*qd[6]
    OPcp5_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp5_26 = ROcp5_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp5_35*S5-ROcp5_95*qd[4])
    OPcp5_36 = ROcp5_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp5_25*S5-ROcp5_85*qd[4])

# = = Block_1_0_0_6_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = ROcp5_16
    sens.R[1,2] = ROcp5_26
    sens.R[1,3] = ROcp5_36
    sens.R[2,1] = ROcp5_46
    sens.R[2,2] = ROcp5_56
    sens.R[2,3] = ROcp5_66
    sens.R[3,1] = S5
    sens.R[3,2] = ROcp5_85
    sens.R[3,3] = ROcp5_95
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


    ROcp6_25 = S4*S5
    ROcp6_35 = -C4*S5
    ROcp6_85 = -S4*C5
    ROcp6_95 = C4*C5
    ROcp6_16 = C5*C6
    ROcp6_26 = ROcp6_25*C6+C4*S6
    ROcp6_36 = ROcp6_35*C6+S4*S6
    ROcp6_46 = -C5*S6
    ROcp6_56 = -(ROcp6_25*S6-C4*C6)
    ROcp6_66 = -(ROcp6_35*S6-S4*C6)
    OMcp6_25 = qd[5]*C4
    OMcp6_35 = qd[5]*S4
    OMcp6_16 = qd[4]+qd[6]*S5
    OMcp6_26 = OMcp6_25+ROcp6_85*qd[6]
    OMcp6_36 = OMcp6_35+ROcp6_95*qd[6]
    OPcp6_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp6_26 = ROcp6_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp6_35*S5-ROcp6_95*qd[4])
    OPcp6_36 = ROcp6_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp6_25*S5-ROcp6_85*qd[4])

# = = Block_1_0_0_7_0_2 = = 
 
# Sensor Kinematics 


    ROcp6_47 = ROcp6_46*C7+S5*S7
    ROcp6_57 = ROcp6_56*C7+ROcp6_85*S7
    ROcp6_67 = ROcp6_66*C7+ROcp6_95*S7
    ROcp6_77 = -(ROcp6_46*S7-S5*C7)
    ROcp6_87 = -(ROcp6_56*S7-ROcp6_85*C7)
    ROcp6_97 = -(ROcp6_66*S7-ROcp6_95*C7)
    RLcp6_17 = ROcp6_16*s.dpt[1,1]+ROcp6_46*s.dpt[2,1]+s.dpt[3,1]*S5
    RLcp6_27 = ROcp6_26*s.dpt[1,1]+ROcp6_56*s.dpt[2,1]+ROcp6_85*s.dpt[3,1]
    RLcp6_37 = ROcp6_36*s.dpt[1,1]+ROcp6_66*s.dpt[2,1]+ROcp6_95*s.dpt[3,1]
    POcp6_17 = RLcp6_17+q[1]
    POcp6_27 = RLcp6_27+q[2]
    POcp6_37 = RLcp6_37+q[3]
    OMcp6_17 = OMcp6_16+ROcp6_16*qd[7]
    OMcp6_27 = OMcp6_26+ROcp6_26*qd[7]
    OMcp6_37 = OMcp6_36+ROcp6_36*qd[7]
    ORcp6_17 = OMcp6_26*RLcp6_37-OMcp6_36*RLcp6_27
    ORcp6_27 = -(OMcp6_16*RLcp6_37-OMcp6_36*RLcp6_17)
    ORcp6_37 = OMcp6_16*RLcp6_27-OMcp6_26*RLcp6_17
    VIcp6_17 = ORcp6_17+qd[1]
    VIcp6_27 = ORcp6_27+qd[2]
    VIcp6_37 = ORcp6_37+qd[3]
    OPcp6_17 = OPcp6_16+ROcp6_16*qdd[7]+qd[7]*(OMcp6_26*ROcp6_36-OMcp6_36*ROcp6_26)
    OPcp6_27 = OPcp6_26+ROcp6_26*qdd[7]-qd[7]*(OMcp6_16*ROcp6_36-OMcp6_36*ROcp6_16)
    OPcp6_37 = OPcp6_36+ROcp6_36*qdd[7]+qd[7]*(OMcp6_16*ROcp6_26-OMcp6_26*ROcp6_16)
    ACcp6_17 = qdd[1]+OMcp6_26*ORcp6_37-OMcp6_36*ORcp6_27+OPcp6_26*RLcp6_37-OPcp6_36*RLcp6_27
    ACcp6_27 = qdd[2]-OMcp6_16*ORcp6_37+OMcp6_36*ORcp6_17-OPcp6_16*RLcp6_37+OPcp6_36*RLcp6_17
    ACcp6_37 = qdd[3]+OMcp6_16*ORcp6_27-OMcp6_26*ORcp6_17+OPcp6_16*RLcp6_27-OPcp6_26*RLcp6_17

# = = Block_1_0_0_7_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp6_17
    sens.P[2] = POcp6_27
    sens.P[3] = POcp6_37
    sens.R[1,1] = ROcp6_16
    sens.R[1,2] = ROcp6_26
    sens.R[1,3] = ROcp6_36
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


    ROcp7_25 = S4*S5
    ROcp7_35 = -C4*S5
    ROcp7_85 = -S4*C5
    ROcp7_95 = C4*C5
    ROcp7_16 = C5*C6
    ROcp7_26 = ROcp7_25*C6+C4*S6
    ROcp7_36 = ROcp7_35*C6+S4*S6
    ROcp7_46 = -C5*S6
    ROcp7_56 = -(ROcp7_25*S6-C4*C6)
    ROcp7_66 = -(ROcp7_35*S6-S4*C6)
    OMcp7_25 = qd[5]*C4
    OMcp7_35 = qd[5]*S4
    OMcp7_16 = qd[4]+qd[6]*S5
    OMcp7_26 = OMcp7_25+ROcp7_85*qd[6]
    OMcp7_36 = OMcp7_35+ROcp7_95*qd[6]
    OPcp7_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp7_26 = ROcp7_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp7_35*S5-ROcp7_95*qd[4])
    OPcp7_36 = ROcp7_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp7_25*S5-ROcp7_85*qd[4])

# = = Block_1_0_0_8_0_2 = = 
 
# Sensor Kinematics 


    ROcp7_47 = ROcp7_46*C7+S5*S7
    ROcp7_57 = ROcp7_56*C7+ROcp7_85*S7
    ROcp7_67 = ROcp7_66*C7+ROcp7_95*S7
    ROcp7_77 = -(ROcp7_46*S7-S5*C7)
    ROcp7_87 = -(ROcp7_56*S7-ROcp7_85*C7)
    ROcp7_97 = -(ROcp7_66*S7-ROcp7_95*C7)
    ROcp7_18 = ROcp7_16*C8+ROcp7_47*S8
    ROcp7_28 = ROcp7_26*C8+ROcp7_57*S8
    ROcp7_38 = ROcp7_36*C8+ROcp7_67*S8
    ROcp7_48 = -(ROcp7_16*S8-ROcp7_47*C8)
    ROcp7_58 = -(ROcp7_26*S8-ROcp7_57*C8)
    ROcp7_68 = -(ROcp7_36*S8-ROcp7_67*C8)
    RLcp7_17 = ROcp7_16*s.dpt[1,1]+ROcp7_46*s.dpt[2,1]+s.dpt[3,1]*S5
    RLcp7_27 = ROcp7_26*s.dpt[1,1]+ROcp7_56*s.dpt[2,1]+ROcp7_85*s.dpt[3,1]
    RLcp7_37 = ROcp7_36*s.dpt[1,1]+ROcp7_66*s.dpt[2,1]+ROcp7_95*s.dpt[3,1]
    OMcp7_17 = OMcp7_16+ROcp7_16*qd[7]
    OMcp7_27 = OMcp7_26+ROcp7_26*qd[7]
    OMcp7_37 = OMcp7_36+ROcp7_36*qd[7]
    ORcp7_17 = OMcp7_26*RLcp7_37-OMcp7_36*RLcp7_27
    ORcp7_27 = -(OMcp7_16*RLcp7_37-OMcp7_36*RLcp7_17)
    ORcp7_37 = OMcp7_16*RLcp7_27-OMcp7_26*RLcp7_17
    OPcp7_17 = OPcp7_16+ROcp7_16*qdd[7]+qd[7]*(OMcp7_26*ROcp7_36-OMcp7_36*ROcp7_26)
    OPcp7_27 = OPcp7_26+ROcp7_26*qdd[7]-qd[7]*(OMcp7_16*ROcp7_36-OMcp7_36*ROcp7_16)
    OPcp7_37 = OPcp7_36+ROcp7_36*qdd[7]+qd[7]*(OMcp7_16*ROcp7_26-OMcp7_26*ROcp7_16)
    RLcp7_18 = ROcp7_47*s.dpt[2,13]
    RLcp7_28 = ROcp7_57*s.dpt[2,13]
    RLcp7_38 = ROcp7_67*s.dpt[2,13]
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


    ROcp8_25 = S4*S5
    ROcp8_35 = -C4*S5
    ROcp8_85 = -S4*C5
    ROcp8_95 = C4*C5
    ROcp8_16 = C5*C6
    ROcp8_26 = ROcp8_25*C6+C4*S6
    ROcp8_36 = ROcp8_35*C6+S4*S6
    ROcp8_46 = -C5*S6
    ROcp8_56 = -(ROcp8_25*S6-C4*C6)
    ROcp8_66 = -(ROcp8_35*S6-S4*C6)
    OMcp8_25 = qd[5]*C4
    OMcp8_35 = qd[5]*S4
    OMcp8_16 = qd[4]+qd[6]*S5
    OMcp8_26 = OMcp8_25+ROcp8_85*qd[6]
    OMcp8_36 = OMcp8_35+ROcp8_95*qd[6]
    OPcp8_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp8_26 = ROcp8_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp8_35*S5-ROcp8_95*qd[4])
    OPcp8_36 = ROcp8_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp8_25*S5-ROcp8_85*qd[4])

# = = Block_1_0_0_9_0_2 = = 
 
# Sensor Kinematics 


    ROcp8_47 = ROcp8_46*C7+S5*S7
    ROcp8_57 = ROcp8_56*C7+ROcp8_85*S7
    ROcp8_67 = ROcp8_66*C7+ROcp8_95*S7
    ROcp8_77 = -(ROcp8_46*S7-S5*C7)
    ROcp8_87 = -(ROcp8_56*S7-ROcp8_85*C7)
    ROcp8_97 = -(ROcp8_66*S7-ROcp8_95*C7)
    ROcp8_18 = ROcp8_16*C8+ROcp8_47*S8
    ROcp8_28 = ROcp8_26*C8+ROcp8_57*S8
    ROcp8_38 = ROcp8_36*C8+ROcp8_67*S8
    ROcp8_48 = -(ROcp8_16*S8-ROcp8_47*C8)
    ROcp8_58 = -(ROcp8_26*S8-ROcp8_57*C8)
    ROcp8_68 = -(ROcp8_36*S8-ROcp8_67*C8)
    ROcp8_49 = ROcp8_48*C9+ROcp8_77*S9
    ROcp8_59 = ROcp8_58*C9+ROcp8_87*S9
    ROcp8_69 = ROcp8_68*C9+ROcp8_97*S9
    ROcp8_79 = -(ROcp8_48*S9-ROcp8_77*C9)
    ROcp8_89 = -(ROcp8_58*S9-ROcp8_87*C9)
    ROcp8_99 = -(ROcp8_68*S9-ROcp8_97*C9)
    RLcp8_17 = ROcp8_16*s.dpt[1,1]+ROcp8_46*s.dpt[2,1]+s.dpt[3,1]*S5
    RLcp8_27 = ROcp8_26*s.dpt[1,1]+ROcp8_56*s.dpt[2,1]+ROcp8_85*s.dpt[3,1]
    RLcp8_37 = ROcp8_36*s.dpt[1,1]+ROcp8_66*s.dpt[2,1]+ROcp8_95*s.dpt[3,1]
    OMcp8_17 = OMcp8_16+ROcp8_16*qd[7]
    OMcp8_27 = OMcp8_26+ROcp8_26*qd[7]
    OMcp8_37 = OMcp8_36+ROcp8_36*qd[7]
    ORcp8_17 = OMcp8_26*RLcp8_37-OMcp8_36*RLcp8_27
    ORcp8_27 = -(OMcp8_16*RLcp8_37-OMcp8_36*RLcp8_17)
    ORcp8_37 = OMcp8_16*RLcp8_27-OMcp8_26*RLcp8_17
    OPcp8_17 = OPcp8_16+ROcp8_16*qdd[7]+qd[7]*(OMcp8_26*ROcp8_36-OMcp8_36*ROcp8_26)
    OPcp8_27 = OPcp8_26+ROcp8_26*qdd[7]-qd[7]*(OMcp8_16*ROcp8_36-OMcp8_36*ROcp8_16)
    OPcp8_37 = OPcp8_36+ROcp8_36*qdd[7]+qd[7]*(OMcp8_16*ROcp8_26-OMcp8_26*ROcp8_16)
    RLcp8_18 = ROcp8_47*s.dpt[2,13]
    RLcp8_28 = ROcp8_57*s.dpt[2,13]
    RLcp8_38 = ROcp8_67*s.dpt[2,13]
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


    ROcp9_25 = S4*S5
    ROcp9_35 = -C4*S5
    ROcp9_85 = -S4*C5
    ROcp9_95 = C4*C5
    ROcp9_16 = C5*C6
    ROcp9_26 = ROcp9_25*C6+C4*S6
    ROcp9_36 = ROcp9_35*C6+S4*S6
    ROcp9_46 = -C5*S6
    ROcp9_56 = -(ROcp9_25*S6-C4*C6)
    ROcp9_66 = -(ROcp9_35*S6-S4*C6)
    OMcp9_25 = qd[5]*C4
    OMcp9_35 = qd[5]*S4
    OMcp9_16 = qd[4]+qd[6]*S5
    OMcp9_26 = OMcp9_25+ROcp9_85*qd[6]
    OMcp9_36 = OMcp9_35+ROcp9_95*qd[6]
    OPcp9_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp9_26 = ROcp9_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp9_35*S5-ROcp9_95*qd[4])
    OPcp9_36 = ROcp9_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp9_25*S5-ROcp9_85*qd[4])

# = = Block_1_0_0_10_0_2 = = 
 
# Sensor Kinematics 


    ROcp9_47 = ROcp9_46*C7+S5*S7
    ROcp9_57 = ROcp9_56*C7+ROcp9_85*S7
    ROcp9_67 = ROcp9_66*C7+ROcp9_95*S7
    ROcp9_77 = -(ROcp9_46*S7-S5*C7)
    ROcp9_87 = -(ROcp9_56*S7-ROcp9_85*C7)
    ROcp9_97 = -(ROcp9_66*S7-ROcp9_95*C7)
    ROcp9_18 = ROcp9_16*C8+ROcp9_47*S8
    ROcp9_28 = ROcp9_26*C8+ROcp9_57*S8
    ROcp9_38 = ROcp9_36*C8+ROcp9_67*S8
    ROcp9_48 = -(ROcp9_16*S8-ROcp9_47*C8)
    ROcp9_58 = -(ROcp9_26*S8-ROcp9_57*C8)
    ROcp9_68 = -(ROcp9_36*S8-ROcp9_67*C8)
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
    RLcp9_17 = ROcp9_16*s.dpt[1,1]+ROcp9_46*s.dpt[2,1]+s.dpt[3,1]*S5
    RLcp9_27 = ROcp9_26*s.dpt[1,1]+ROcp9_56*s.dpt[2,1]+ROcp9_85*s.dpt[3,1]
    RLcp9_37 = ROcp9_36*s.dpt[1,1]+ROcp9_66*s.dpt[2,1]+ROcp9_95*s.dpt[3,1]
    OMcp9_17 = OMcp9_16+ROcp9_16*qd[7]
    OMcp9_27 = OMcp9_26+ROcp9_26*qd[7]
    OMcp9_37 = OMcp9_36+ROcp9_36*qd[7]
    ORcp9_17 = OMcp9_26*RLcp9_37-OMcp9_36*RLcp9_27
    ORcp9_27 = -(OMcp9_16*RLcp9_37-OMcp9_36*RLcp9_17)
    ORcp9_37 = OMcp9_16*RLcp9_27-OMcp9_26*RLcp9_17
    OPcp9_17 = OPcp9_16+ROcp9_16*qdd[7]+qd[7]*(OMcp9_26*ROcp9_36-OMcp9_36*ROcp9_26)
    OPcp9_27 = OPcp9_26+ROcp9_26*qdd[7]-qd[7]*(OMcp9_16*ROcp9_36-OMcp9_36*ROcp9_16)
    OPcp9_37 = OPcp9_36+ROcp9_36*qdd[7]+qd[7]*(OMcp9_16*ROcp9_26-OMcp9_26*ROcp9_16)
    RLcp9_18 = ROcp9_47*s.dpt[2,13]
    RLcp9_28 = ROcp9_57*s.dpt[2,13]
    RLcp9_38 = ROcp9_67*s.dpt[2,13]
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


    ROcp10_25 = S4*S5
    ROcp10_35 = -C4*S5
    ROcp10_85 = -S4*C5
    ROcp10_95 = C4*C5
    ROcp10_16 = C5*C6
    ROcp10_26 = ROcp10_25*C6+C4*S6
    ROcp10_36 = ROcp10_35*C6+S4*S6
    ROcp10_46 = -C5*S6
    ROcp10_56 = -(ROcp10_25*S6-C4*C6)
    ROcp10_66 = -(ROcp10_35*S6-S4*C6)
    OMcp10_25 = qd[5]*C4
    OMcp10_35 = qd[5]*S4
    OMcp10_16 = qd[4]+qd[6]*S5
    OMcp10_26 = OMcp10_25+ROcp10_85*qd[6]
    OMcp10_36 = OMcp10_35+ROcp10_95*qd[6]
    OPcp10_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp10_26 = ROcp10_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp10_35*S5-ROcp10_95*qd[4])
    OPcp10_36 = ROcp10_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp10_25*S5-ROcp10_85*qd[4])

# = = Block_1_0_0_11_0_3 = = 
 
# Sensor Kinematics 


    ROcp10_411 = ROcp10_46*C11+S11*S5
    ROcp10_511 = ROcp10_56*C11+ROcp10_85*S11
    ROcp10_611 = ROcp10_66*C11+ROcp10_95*S11
    ROcp10_711 = -(ROcp10_46*S11-C11*S5)
    ROcp10_811 = -(ROcp10_56*S11-ROcp10_85*C11)
    ROcp10_911 = -(ROcp10_66*S11-ROcp10_95*C11)
    RLcp10_111 = ROcp10_16*s.dpt[1,4]+ROcp10_46*s.dpt[2,4]+s.dpt[3,4]*S5
    RLcp10_211 = ROcp10_26*s.dpt[1,4]+ROcp10_56*s.dpt[2,4]+ROcp10_85*s.dpt[3,4]
    RLcp10_311 = ROcp10_36*s.dpt[1,4]+ROcp10_66*s.dpt[2,4]+ROcp10_95*s.dpt[3,4]
    POcp10_111 = RLcp10_111+q[1]
    POcp10_211 = RLcp10_211+q[2]
    POcp10_311 = RLcp10_311+q[3]
    OMcp10_111 = OMcp10_16+ROcp10_16*qd[11]
    OMcp10_211 = OMcp10_26+ROcp10_26*qd[11]
    OMcp10_311 = OMcp10_36+ROcp10_36*qd[11]
    ORcp10_111 = OMcp10_26*RLcp10_311-OMcp10_36*RLcp10_211
    ORcp10_211 = -(OMcp10_16*RLcp10_311-OMcp10_36*RLcp10_111)
    ORcp10_311 = OMcp10_16*RLcp10_211-OMcp10_26*RLcp10_111
    VIcp10_111 = ORcp10_111+qd[1]
    VIcp10_211 = ORcp10_211+qd[2]
    VIcp10_311 = ORcp10_311+qd[3]
    OPcp10_111 = OPcp10_16+ROcp10_16*qdd[11]+qd[11]*(OMcp10_26*ROcp10_36-OMcp10_36*ROcp10_26)
    OPcp10_211 = OPcp10_26+ROcp10_26*qdd[11]-qd[11]*(OMcp10_16*ROcp10_36-OMcp10_36*ROcp10_16)
    OPcp10_311 = OPcp10_36+ROcp10_36*qdd[11]+qd[11]*(OMcp10_16*ROcp10_26-OMcp10_26*ROcp10_16)
    ACcp10_111 = qdd[1]+OMcp10_26*ORcp10_311-OMcp10_36*ORcp10_211+OPcp10_26*RLcp10_311-OPcp10_36*RLcp10_211
    ACcp10_211 = qdd[2]-OMcp10_16*ORcp10_311+OMcp10_36*ORcp10_111-OPcp10_16*RLcp10_311+OPcp10_36*RLcp10_111
    ACcp10_311 = qdd[3]+OMcp10_16*ORcp10_211-OMcp10_26*ORcp10_111+OPcp10_16*RLcp10_211-OPcp10_26*RLcp10_111

# = = Block_1_0_0_11_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp10_111
    sens.P[2] = POcp10_211
    sens.P[3] = POcp10_311
    sens.R[1,1] = ROcp10_16
    sens.R[1,2] = ROcp10_26
    sens.R[1,3] = ROcp10_36
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


    ROcp11_25 = S4*S5
    ROcp11_35 = -C4*S5
    ROcp11_85 = -S4*C5
    ROcp11_95 = C4*C5
    ROcp11_16 = C5*C6
    ROcp11_26 = ROcp11_25*C6+C4*S6
    ROcp11_36 = ROcp11_35*C6+S4*S6
    ROcp11_46 = -C5*S6
    ROcp11_56 = -(ROcp11_25*S6-C4*C6)
    ROcp11_66 = -(ROcp11_35*S6-S4*C6)
    OMcp11_25 = qd[5]*C4
    OMcp11_35 = qd[5]*S4
    OMcp11_16 = qd[4]+qd[6]*S5
    OMcp11_26 = OMcp11_25+ROcp11_85*qd[6]
    OMcp11_36 = OMcp11_35+ROcp11_95*qd[6]
    OPcp11_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp11_26 = ROcp11_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp11_35*S5-ROcp11_95*qd[4])
    OPcp11_36 = ROcp11_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp11_25*S5-ROcp11_85*qd[4])

# = = Block_1_0_0_12_0_3 = = 
 
# Sensor Kinematics 


    ROcp11_411 = ROcp11_46*C11+S11*S5
    ROcp11_511 = ROcp11_56*C11+ROcp11_85*S11
    ROcp11_611 = ROcp11_66*C11+ROcp11_95*S11
    ROcp11_711 = -(ROcp11_46*S11-C11*S5)
    ROcp11_811 = -(ROcp11_56*S11-ROcp11_85*C11)
    ROcp11_911 = -(ROcp11_66*S11-ROcp11_95*C11)
    ROcp11_112 = ROcp11_16*C12+ROcp11_411*S12
    ROcp11_212 = ROcp11_26*C12+ROcp11_511*S12
    ROcp11_312 = ROcp11_36*C12+ROcp11_611*S12
    ROcp11_412 = -(ROcp11_16*S12-ROcp11_411*C12)
    ROcp11_512 = -(ROcp11_26*S12-ROcp11_511*C12)
    ROcp11_612 = -(ROcp11_36*S12-ROcp11_611*C12)
    RLcp11_111 = ROcp11_16*s.dpt[1,4]+ROcp11_46*s.dpt[2,4]+s.dpt[3,4]*S5
    RLcp11_211 = ROcp11_26*s.dpt[1,4]+ROcp11_56*s.dpt[2,4]+ROcp11_85*s.dpt[3,4]
    RLcp11_311 = ROcp11_36*s.dpt[1,4]+ROcp11_66*s.dpt[2,4]+ROcp11_95*s.dpt[3,4]
    OMcp11_111 = OMcp11_16+ROcp11_16*qd[11]
    OMcp11_211 = OMcp11_26+ROcp11_26*qd[11]
    OMcp11_311 = OMcp11_36+ROcp11_36*qd[11]
    ORcp11_111 = OMcp11_26*RLcp11_311-OMcp11_36*RLcp11_211
    ORcp11_211 = -(OMcp11_16*RLcp11_311-OMcp11_36*RLcp11_111)
    ORcp11_311 = OMcp11_16*RLcp11_211-OMcp11_26*RLcp11_111
    OPcp11_111 = OPcp11_16+ROcp11_16*qdd[11]+qd[11]*(OMcp11_26*ROcp11_36-OMcp11_36*ROcp11_26)
    OPcp11_211 = OPcp11_26+ROcp11_26*qdd[11]-qd[11]*(OMcp11_16*ROcp11_36-OMcp11_36*ROcp11_16)
    OPcp11_311 = OPcp11_36+ROcp11_36*qdd[11]+qd[11]*(OMcp11_16*ROcp11_26-OMcp11_26*ROcp11_16)
    RLcp11_112 = ROcp11_411*s.dpt[2,17]
    RLcp11_212 = ROcp11_511*s.dpt[2,17]
    RLcp11_312 = ROcp11_611*s.dpt[2,17]
    POcp11_112 = RLcp11_111+RLcp11_112+q[1]
    POcp11_212 = RLcp11_211+RLcp11_212+q[2]
    POcp11_312 = RLcp11_311+RLcp11_312+q[3]
    OMcp11_112 = OMcp11_111+ROcp11_711*qd[12]
    OMcp11_212 = OMcp11_211+ROcp11_811*qd[12]
    OMcp11_312 = OMcp11_311+ROcp11_911*qd[12]
    ORcp11_112 = OMcp11_211*RLcp11_312-OMcp11_311*RLcp11_212
    ORcp11_212 = -(OMcp11_111*RLcp11_312-OMcp11_311*RLcp11_112)
    ORcp11_312 = OMcp11_111*RLcp11_212-OMcp11_211*RLcp11_112
    VIcp11_112 = ORcp11_111+ORcp11_112+qd[1]
    VIcp11_212 = ORcp11_211+ORcp11_212+qd[2]
    VIcp11_312 = ORcp11_311+ORcp11_312+qd[3]
    OPcp11_112 = OPcp11_111+ROcp11_711*qdd[12]+qd[12]*(OMcp11_211*ROcp11_911-OMcp11_311*ROcp11_811)
    OPcp11_212 = OPcp11_211+ROcp11_811*qdd[12]-qd[12]*(OMcp11_111*ROcp11_911-OMcp11_311*ROcp11_711)
    OPcp11_312 = OPcp11_311+ROcp11_911*qdd[12]+qd[12]*(OMcp11_111*ROcp11_811-OMcp11_211*ROcp11_711)
    ACcp11_112 = qdd[1]+OMcp11_211*ORcp11_312+OMcp11_26*ORcp11_311-OMcp11_311*ORcp11_212-OMcp11_36*ORcp11_211+OPcp11_211*\
   RLcp11_312+OPcp11_26*RLcp11_311-OPcp11_311*RLcp11_212-OPcp11_36*RLcp11_211
    ACcp11_212 = qdd[2]-OMcp11_111*ORcp11_312-OMcp11_16*ORcp11_311+OMcp11_311*ORcp11_112+OMcp11_36*ORcp11_111-OPcp11_111*\
   RLcp11_312-OPcp11_16*RLcp11_311+OPcp11_311*RLcp11_112+OPcp11_36*RLcp11_111
    ACcp11_312 = qdd[3]+OMcp11_111*ORcp11_212+OMcp11_16*ORcp11_211-OMcp11_211*ORcp11_112-OMcp11_26*ORcp11_111+OPcp11_111*\
   RLcp11_212+OPcp11_16*RLcp11_211-OPcp11_211*RLcp11_112-OPcp11_26*RLcp11_111

# = = Block_1_0_0_12_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp11_112
    sens.P[2] = POcp11_212
    sens.P[3] = POcp11_312
    sens.R[1,1] = ROcp11_112
    sens.R[1,2] = ROcp11_212
    sens.R[1,3] = ROcp11_312
    sens.R[2,1] = ROcp11_412
    sens.R[2,2] = ROcp11_512
    sens.R[2,3] = ROcp11_612
    sens.R[3,1] = ROcp11_711
    sens.R[3,2] = ROcp11_811
    sens.R[3,3] = ROcp11_911
    sens.V[1] = VIcp11_112
    sens.V[2] = VIcp11_212
    sens.V[3] = VIcp11_312
    sens.OM[1] = OMcp11_112
    sens.OM[2] = OMcp11_212
    sens.OM[3] = OMcp11_312
    sens.A[1] = ACcp11_112
    sens.A[2] = ACcp11_212
    sens.A[3] = ACcp11_312
    sens.OMP[1] = OPcp11_112
    sens.OMP[2] = OPcp11_212
    sens.OMP[3] = OPcp11_312
 
# 
  elif(isens==13): 


# = = Block_1_0_0_13_0_1 = = 
 
# Sensor Kinematics 


    ROcp12_25 = S4*S5
    ROcp12_35 = -C4*S5
    ROcp12_85 = -S4*C5
    ROcp12_95 = C4*C5
    ROcp12_16 = C5*C6
    ROcp12_26 = ROcp12_25*C6+C4*S6
    ROcp12_36 = ROcp12_35*C6+S4*S6
    ROcp12_46 = -C5*S6
    ROcp12_56 = -(ROcp12_25*S6-C4*C6)
    ROcp12_66 = -(ROcp12_35*S6-S4*C6)
    OMcp12_25 = qd[5]*C4
    OMcp12_35 = qd[5]*S4
    OMcp12_16 = qd[4]+qd[6]*S5
    OMcp12_26 = OMcp12_25+ROcp12_85*qd[6]
    OMcp12_36 = OMcp12_35+ROcp12_95*qd[6]
    OPcp12_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp12_26 = ROcp12_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp12_35*S5-ROcp12_95*qd[4])
    OPcp12_36 = ROcp12_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp12_25*S5-ROcp12_85*qd[4])

# = = Block_1_0_0_13_0_3 = = 
 
# Sensor Kinematics 


    ROcp12_411 = ROcp12_46*C11+S11*S5
    ROcp12_511 = ROcp12_56*C11+ROcp12_85*S11
    ROcp12_611 = ROcp12_66*C11+ROcp12_95*S11
    ROcp12_711 = -(ROcp12_46*S11-C11*S5)
    ROcp12_811 = -(ROcp12_56*S11-ROcp12_85*C11)
    ROcp12_911 = -(ROcp12_66*S11-ROcp12_95*C11)
    ROcp12_112 = ROcp12_16*C12+ROcp12_411*S12
    ROcp12_212 = ROcp12_26*C12+ROcp12_511*S12
    ROcp12_312 = ROcp12_36*C12+ROcp12_611*S12
    ROcp12_412 = -(ROcp12_16*S12-ROcp12_411*C12)
    ROcp12_512 = -(ROcp12_26*S12-ROcp12_511*C12)
    ROcp12_612 = -(ROcp12_36*S12-ROcp12_611*C12)
    ROcp12_413 = ROcp12_412*C13+ROcp12_711*S13
    ROcp12_513 = ROcp12_512*C13+ROcp12_811*S13
    ROcp12_613 = ROcp12_612*C13+ROcp12_911*S13
    ROcp12_713 = -(ROcp12_412*S13-ROcp12_711*C13)
    ROcp12_813 = -(ROcp12_512*S13-ROcp12_811*C13)
    ROcp12_913 = -(ROcp12_612*S13-ROcp12_911*C13)
    RLcp12_111 = ROcp12_16*s.dpt[1,4]+ROcp12_46*s.dpt[2,4]+s.dpt[3,4]*S5
    RLcp12_211 = ROcp12_26*s.dpt[1,4]+ROcp12_56*s.dpt[2,4]+ROcp12_85*s.dpt[3,4]
    RLcp12_311 = ROcp12_36*s.dpt[1,4]+ROcp12_66*s.dpt[2,4]+ROcp12_95*s.dpt[3,4]
    OMcp12_111 = OMcp12_16+ROcp12_16*qd[11]
    OMcp12_211 = OMcp12_26+ROcp12_26*qd[11]
    OMcp12_311 = OMcp12_36+ROcp12_36*qd[11]
    ORcp12_111 = OMcp12_26*RLcp12_311-OMcp12_36*RLcp12_211
    ORcp12_211 = -(OMcp12_16*RLcp12_311-OMcp12_36*RLcp12_111)
    ORcp12_311 = OMcp12_16*RLcp12_211-OMcp12_26*RLcp12_111
    OPcp12_111 = OPcp12_16+ROcp12_16*qdd[11]+qd[11]*(OMcp12_26*ROcp12_36-OMcp12_36*ROcp12_26)
    OPcp12_211 = OPcp12_26+ROcp12_26*qdd[11]-qd[11]*(OMcp12_16*ROcp12_36-OMcp12_36*ROcp12_16)
    OPcp12_311 = OPcp12_36+ROcp12_36*qdd[11]+qd[11]*(OMcp12_16*ROcp12_26-OMcp12_26*ROcp12_16)
    RLcp12_112 = ROcp12_411*s.dpt[2,17]
    RLcp12_212 = ROcp12_511*s.dpt[2,17]
    RLcp12_312 = ROcp12_611*s.dpt[2,17]
    POcp12_112 = RLcp12_111+RLcp12_112+q[1]
    POcp12_212 = RLcp12_211+RLcp12_212+q[2]
    POcp12_312 = RLcp12_311+RLcp12_312+q[3]
    OMcp12_112 = OMcp12_111+ROcp12_711*qd[12]
    OMcp12_212 = OMcp12_211+ROcp12_811*qd[12]
    OMcp12_312 = OMcp12_311+ROcp12_911*qd[12]
    ORcp12_112 = OMcp12_211*RLcp12_312-OMcp12_311*RLcp12_212
    ORcp12_212 = -(OMcp12_111*RLcp12_312-OMcp12_311*RLcp12_112)
    ORcp12_312 = OMcp12_111*RLcp12_212-OMcp12_211*RLcp12_112
    VIcp12_112 = ORcp12_111+ORcp12_112+qd[1]
    VIcp12_212 = ORcp12_211+ORcp12_212+qd[2]
    VIcp12_312 = ORcp12_311+ORcp12_312+qd[3]
    ACcp12_112 = qdd[1]+OMcp12_211*ORcp12_312+OMcp12_26*ORcp12_311-OMcp12_311*ORcp12_212-OMcp12_36*ORcp12_211+OPcp12_211*\
   RLcp12_312+OPcp12_26*RLcp12_311-OPcp12_311*RLcp12_212-OPcp12_36*RLcp12_211
    ACcp12_212 = qdd[2]-OMcp12_111*ORcp12_312-OMcp12_16*ORcp12_311+OMcp12_311*ORcp12_112+OMcp12_36*ORcp12_111-OPcp12_111*\
   RLcp12_312-OPcp12_16*RLcp12_311+OPcp12_311*RLcp12_112+OPcp12_36*RLcp12_111
    ACcp12_312 = qdd[3]+OMcp12_111*ORcp12_212+OMcp12_16*ORcp12_211-OMcp12_211*ORcp12_112-OMcp12_26*ORcp12_111+OPcp12_111*\
   RLcp12_212+OPcp12_16*RLcp12_211-OPcp12_211*RLcp12_112-OPcp12_26*RLcp12_111
    OMcp12_113 = OMcp12_112+ROcp12_112*qd[13]
    OMcp12_213 = OMcp12_212+ROcp12_212*qd[13]
    OMcp12_313 = OMcp12_312+ROcp12_312*qd[13]
    OPcp12_113 = OPcp12_111+ROcp12_112*qdd[13]+ROcp12_711*qdd[12]+qd[12]*(OMcp12_211*ROcp12_911-OMcp12_311*ROcp12_811)+\
   qd[13]*(OMcp12_212*ROcp12_312-OMcp12_312*ROcp12_212)
    OPcp12_213 = OPcp12_211+ROcp12_212*qdd[13]+ROcp12_811*qdd[12]-qd[12]*(OMcp12_111*ROcp12_911-OMcp12_311*ROcp12_711)-\
   qd[13]*(OMcp12_112*ROcp12_312-OMcp12_312*ROcp12_112)
    OPcp12_313 = OPcp12_311+ROcp12_312*qdd[13]+ROcp12_911*qdd[12]+qd[12]*(OMcp12_111*ROcp12_811-OMcp12_211*ROcp12_711)+\
   qd[13]*(OMcp12_112*ROcp12_212-OMcp12_212*ROcp12_112)

# = = Block_1_0_0_13_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp12_112
    sens.P[2] = POcp12_212
    sens.P[3] = POcp12_312
    sens.R[1,1] = ROcp12_112
    sens.R[1,2] = ROcp12_212
    sens.R[1,3] = ROcp12_312
    sens.R[2,1] = ROcp12_413
    sens.R[2,2] = ROcp12_513
    sens.R[2,3] = ROcp12_613
    sens.R[3,1] = ROcp12_713
    sens.R[3,2] = ROcp12_813
    sens.R[3,3] = ROcp12_913
    sens.V[1] = VIcp12_112
    sens.V[2] = VIcp12_212
    sens.V[3] = VIcp12_312
    sens.OM[1] = OMcp12_113
    sens.OM[2] = OMcp12_213
    sens.OM[3] = OMcp12_313
    sens.A[1] = ACcp12_112
    sens.A[2] = ACcp12_212
    sens.A[3] = ACcp12_312
    sens.OMP[1] = OPcp12_113
    sens.OMP[2] = OPcp12_213
    sens.OMP[3] = OPcp12_313
 
# 
  elif(isens==14): 


# = = Block_1_0_0_14_0_1 = = 
 
# Sensor Kinematics 


    ROcp13_25 = S4*S5
    ROcp13_35 = -C4*S5
    ROcp13_85 = -S4*C5
    ROcp13_95 = C4*C5
    ROcp13_16 = C5*C6
    ROcp13_26 = ROcp13_25*C6+C4*S6
    ROcp13_36 = ROcp13_35*C6+S4*S6
    ROcp13_46 = -C5*S6
    ROcp13_56 = -(ROcp13_25*S6-C4*C6)
    ROcp13_66 = -(ROcp13_35*S6-S4*C6)
    OMcp13_25 = qd[5]*C4
    OMcp13_35 = qd[5]*S4
    OMcp13_16 = qd[4]+qd[6]*S5
    OMcp13_26 = OMcp13_25+ROcp13_85*qd[6]
    OMcp13_36 = OMcp13_35+ROcp13_95*qd[6]
    OPcp13_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp13_26 = ROcp13_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp13_35*S5-ROcp13_95*qd[4])
    OPcp13_36 = ROcp13_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp13_25*S5-ROcp13_85*qd[4])

# = = Block_1_0_0_14_0_3 = = 
 
# Sensor Kinematics 


    ROcp13_411 = ROcp13_46*C11+S11*S5
    ROcp13_511 = ROcp13_56*C11+ROcp13_85*S11
    ROcp13_611 = ROcp13_66*C11+ROcp13_95*S11
    ROcp13_711 = -(ROcp13_46*S11-C11*S5)
    ROcp13_811 = -(ROcp13_56*S11-ROcp13_85*C11)
    ROcp13_911 = -(ROcp13_66*S11-ROcp13_95*C11)
    ROcp13_112 = ROcp13_16*C12+ROcp13_411*S12
    ROcp13_212 = ROcp13_26*C12+ROcp13_511*S12
    ROcp13_312 = ROcp13_36*C12+ROcp13_611*S12
    ROcp13_412 = -(ROcp13_16*S12-ROcp13_411*C12)
    ROcp13_512 = -(ROcp13_26*S12-ROcp13_511*C12)
    ROcp13_612 = -(ROcp13_36*S12-ROcp13_611*C12)
    ROcp13_413 = ROcp13_412*C13+ROcp13_711*S13
    ROcp13_513 = ROcp13_512*C13+ROcp13_811*S13
    ROcp13_613 = ROcp13_612*C13+ROcp13_911*S13
    ROcp13_713 = -(ROcp13_412*S13-ROcp13_711*C13)
    ROcp13_813 = -(ROcp13_512*S13-ROcp13_811*C13)
    ROcp13_913 = -(ROcp13_612*S13-ROcp13_911*C13)
    ROcp13_114 = ROcp13_112*C14-ROcp13_713*S14
    ROcp13_214 = ROcp13_212*C14-ROcp13_813*S14
    ROcp13_314 = ROcp13_312*C14-ROcp13_913*S14
    ROcp13_714 = ROcp13_112*S14+ROcp13_713*C14
    ROcp13_814 = ROcp13_212*S14+ROcp13_813*C14
    ROcp13_914 = ROcp13_312*S14+ROcp13_913*C14
    RLcp13_111 = ROcp13_16*s.dpt[1,4]+ROcp13_46*s.dpt[2,4]+s.dpt[3,4]*S5
    RLcp13_211 = ROcp13_26*s.dpt[1,4]+ROcp13_56*s.dpt[2,4]+ROcp13_85*s.dpt[3,4]
    RLcp13_311 = ROcp13_36*s.dpt[1,4]+ROcp13_66*s.dpt[2,4]+ROcp13_95*s.dpt[3,4]
    OMcp13_111 = OMcp13_16+ROcp13_16*qd[11]
    OMcp13_211 = OMcp13_26+ROcp13_26*qd[11]
    OMcp13_311 = OMcp13_36+ROcp13_36*qd[11]
    ORcp13_111 = OMcp13_26*RLcp13_311-OMcp13_36*RLcp13_211
    ORcp13_211 = -(OMcp13_16*RLcp13_311-OMcp13_36*RLcp13_111)
    ORcp13_311 = OMcp13_16*RLcp13_211-OMcp13_26*RLcp13_111
    OPcp13_111 = OPcp13_16+ROcp13_16*qdd[11]+qd[11]*(OMcp13_26*ROcp13_36-OMcp13_36*ROcp13_26)
    OPcp13_211 = OPcp13_26+ROcp13_26*qdd[11]-qd[11]*(OMcp13_16*ROcp13_36-OMcp13_36*ROcp13_16)
    OPcp13_311 = OPcp13_36+ROcp13_36*qdd[11]+qd[11]*(OMcp13_16*ROcp13_26-OMcp13_26*ROcp13_16)
    RLcp13_112 = ROcp13_411*s.dpt[2,17]
    RLcp13_212 = ROcp13_511*s.dpt[2,17]
    RLcp13_312 = ROcp13_611*s.dpt[2,17]
    POcp13_112 = RLcp13_111+RLcp13_112+q[1]
    POcp13_212 = RLcp13_211+RLcp13_212+q[2]
    POcp13_312 = RLcp13_311+RLcp13_312+q[3]
    OMcp13_112 = OMcp13_111+ROcp13_711*qd[12]
    OMcp13_212 = OMcp13_211+ROcp13_811*qd[12]
    OMcp13_312 = OMcp13_311+ROcp13_911*qd[12]
    ORcp13_112 = OMcp13_211*RLcp13_312-OMcp13_311*RLcp13_212
    ORcp13_212 = -(OMcp13_111*RLcp13_312-OMcp13_311*RLcp13_112)
    ORcp13_312 = OMcp13_111*RLcp13_212-OMcp13_211*RLcp13_112
    VIcp13_112 = ORcp13_111+ORcp13_112+qd[1]
    VIcp13_212 = ORcp13_211+ORcp13_212+qd[2]
    VIcp13_312 = ORcp13_311+ORcp13_312+qd[3]
    ACcp13_112 = qdd[1]+OMcp13_211*ORcp13_312+OMcp13_26*ORcp13_311-OMcp13_311*ORcp13_212-OMcp13_36*ORcp13_211+OPcp13_211*\
   RLcp13_312+OPcp13_26*RLcp13_311-OPcp13_311*RLcp13_212-OPcp13_36*RLcp13_211
    ACcp13_212 = qdd[2]-OMcp13_111*ORcp13_312-OMcp13_16*ORcp13_311+OMcp13_311*ORcp13_112+OMcp13_36*ORcp13_111-OPcp13_111*\
   RLcp13_312-OPcp13_16*RLcp13_311+OPcp13_311*RLcp13_112+OPcp13_36*RLcp13_111
    ACcp13_312 = qdd[3]+OMcp13_111*ORcp13_212+OMcp13_16*ORcp13_211-OMcp13_211*ORcp13_112-OMcp13_26*ORcp13_111+OPcp13_111*\
   RLcp13_212+OPcp13_16*RLcp13_211-OPcp13_211*RLcp13_112-OPcp13_26*RLcp13_111
    OMcp13_113 = OMcp13_112+ROcp13_112*qd[13]
    OMcp13_213 = OMcp13_212+ROcp13_212*qd[13]
    OMcp13_313 = OMcp13_312+ROcp13_312*qd[13]
    OMcp13_114 = OMcp13_113+ROcp13_413*qd[14]
    OMcp13_214 = OMcp13_213+ROcp13_513*qd[14]
    OMcp13_314 = OMcp13_313+ROcp13_613*qd[14]
    OPcp13_114 = OPcp13_111+ROcp13_112*qdd[13]+ROcp13_413*qdd[14]+ROcp13_711*qdd[12]+qd[12]*(OMcp13_211*ROcp13_911-\
   OMcp13_311*ROcp13_811)+qd[13]*(OMcp13_212*ROcp13_312-OMcp13_312*ROcp13_212)+qd[14]*(OMcp13_213*ROcp13_613-OMcp13_313*\
   ROcp13_513)
    OPcp13_214 = OPcp13_211+ROcp13_212*qdd[13]+ROcp13_513*qdd[14]+ROcp13_811*qdd[12]-qd[12]*(OMcp13_111*ROcp13_911-\
   OMcp13_311*ROcp13_711)-qd[13]*(OMcp13_112*ROcp13_312-OMcp13_312*ROcp13_112)-qd[14]*(OMcp13_113*ROcp13_613-OMcp13_313*\
   ROcp13_413)
    OPcp13_314 = OPcp13_311+ROcp13_312*qdd[13]+ROcp13_613*qdd[14]+ROcp13_911*qdd[12]+qd[12]*(OMcp13_111*ROcp13_811-\
   OMcp13_211*ROcp13_711)+qd[13]*(OMcp13_112*ROcp13_212-OMcp13_212*ROcp13_112)+qd[14]*(OMcp13_113*ROcp13_513-OMcp13_213*\
   ROcp13_413)

# = = Block_1_0_0_14_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp13_112
    sens.P[2] = POcp13_212
    sens.P[3] = POcp13_312
    sens.R[1,1] = ROcp13_114
    sens.R[1,2] = ROcp13_214
    sens.R[1,3] = ROcp13_314
    sens.R[2,1] = ROcp13_413
    sens.R[2,2] = ROcp13_513
    sens.R[2,3] = ROcp13_613
    sens.R[3,1] = ROcp13_714
    sens.R[3,2] = ROcp13_814
    sens.R[3,3] = ROcp13_914
    sens.V[1] = VIcp13_112
    sens.V[2] = VIcp13_212
    sens.V[3] = VIcp13_312
    sens.OM[1] = OMcp13_114
    sens.OM[2] = OMcp13_214
    sens.OM[3] = OMcp13_314
    sens.A[1] = ACcp13_112
    sens.A[2] = ACcp13_212
    sens.A[3] = ACcp13_312
    sens.OMP[1] = OPcp13_114
    sens.OMP[2] = OPcp13_214
    sens.OMP[3] = OPcp13_314
 
# 
  elif(isens==15): 


# = = Block_1_0_0_15_0_1 = = 
 
# Sensor Kinematics 


    ROcp14_25 = S4*S5
    ROcp14_35 = -C4*S5
    ROcp14_85 = -S4*C5
    ROcp14_95 = C4*C5
    ROcp14_16 = C5*C6
    ROcp14_26 = ROcp14_25*C6+C4*S6
    ROcp14_36 = ROcp14_35*C6+S4*S6
    ROcp14_46 = -C5*S6
    ROcp14_56 = -(ROcp14_25*S6-C4*C6)
    ROcp14_66 = -(ROcp14_35*S6-S4*C6)
    OMcp14_25 = qd[5]*C4
    OMcp14_35 = qd[5]*S4
    OMcp14_16 = qd[4]+qd[6]*S5
    OMcp14_26 = OMcp14_25+ROcp14_85*qd[6]
    OMcp14_36 = OMcp14_35+ROcp14_95*qd[6]
    OPcp14_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp14_26 = ROcp14_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp14_35*S5-ROcp14_95*qd[4])
    OPcp14_36 = ROcp14_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp14_25*S5-ROcp14_85*qd[4])

# = = Block_1_0_0_15_0_4 = = 
 
# Sensor Kinematics 


    ROcp14_415 = ROcp14_46*C15+S15*S5
    ROcp14_515 = ROcp14_56*C15+ROcp14_85*S15
    ROcp14_615 = ROcp14_66*C15+ROcp14_95*S15
    ROcp14_715 = -(ROcp14_46*S15-C15*S5)
    ROcp14_815 = -(ROcp14_56*S15-ROcp14_85*C15)
    ROcp14_915 = -(ROcp14_66*S15-ROcp14_95*C15)
    RLcp14_115 = ROcp14_16*s.dpt[1,9]+ROcp14_46*s.dpt[2,9]+s.dpt[3,9]*S5
    RLcp14_215 = ROcp14_26*s.dpt[1,9]+ROcp14_56*s.dpt[2,9]+ROcp14_85*s.dpt[3,9]
    RLcp14_315 = ROcp14_36*s.dpt[1,9]+ROcp14_66*s.dpt[2,9]+ROcp14_95*s.dpt[3,9]
    POcp14_115 = RLcp14_115+q[1]
    POcp14_215 = RLcp14_215+q[2]
    POcp14_315 = RLcp14_315+q[3]
    OMcp14_115 = OMcp14_16+ROcp14_16*qd[15]
    OMcp14_215 = OMcp14_26+ROcp14_26*qd[15]
    OMcp14_315 = OMcp14_36+ROcp14_36*qd[15]
    ORcp14_115 = OMcp14_26*RLcp14_315-OMcp14_36*RLcp14_215
    ORcp14_215 = -(OMcp14_16*RLcp14_315-OMcp14_36*RLcp14_115)
    ORcp14_315 = OMcp14_16*RLcp14_215-OMcp14_26*RLcp14_115
    VIcp14_115 = ORcp14_115+qd[1]
    VIcp14_215 = ORcp14_215+qd[2]
    VIcp14_315 = ORcp14_315+qd[3]
    OPcp14_115 = OPcp14_16+ROcp14_16*qdd[15]+qd[15]*(OMcp14_26*ROcp14_36-OMcp14_36*ROcp14_26)
    OPcp14_215 = OPcp14_26+ROcp14_26*qdd[15]-qd[15]*(OMcp14_16*ROcp14_36-OMcp14_36*ROcp14_16)
    OPcp14_315 = OPcp14_36+ROcp14_36*qdd[15]+qd[15]*(OMcp14_16*ROcp14_26-OMcp14_26*ROcp14_16)
    ACcp14_115 = qdd[1]+OMcp14_26*ORcp14_315-OMcp14_36*ORcp14_215+OPcp14_26*RLcp14_315-OPcp14_36*RLcp14_215
    ACcp14_215 = qdd[2]-OMcp14_16*ORcp14_315+OMcp14_36*ORcp14_115-OPcp14_16*RLcp14_315+OPcp14_36*RLcp14_115
    ACcp14_315 = qdd[3]+OMcp14_16*ORcp14_215-OMcp14_26*ORcp14_115+OPcp14_16*RLcp14_215-OPcp14_26*RLcp14_115

# = = Block_1_0_0_15_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp14_115
    sens.P[2] = POcp14_215
    sens.P[3] = POcp14_315
    sens.R[1,1] = ROcp14_16
    sens.R[1,2] = ROcp14_26
    sens.R[1,3] = ROcp14_36
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


    ROcp15_25 = S4*S5
    ROcp15_35 = -C4*S5
    ROcp15_85 = -S4*C5
    ROcp15_95 = C4*C5
    ROcp15_16 = C5*C6
    ROcp15_26 = ROcp15_25*C6+C4*S6
    ROcp15_36 = ROcp15_35*C6+S4*S6
    ROcp15_46 = -C5*S6
    ROcp15_56 = -(ROcp15_25*S6-C4*C6)
    ROcp15_66 = -(ROcp15_35*S6-S4*C6)
    OMcp15_25 = qd[5]*C4
    OMcp15_35 = qd[5]*S4
    OMcp15_16 = qd[4]+qd[6]*S5
    OMcp15_26 = OMcp15_25+ROcp15_85*qd[6]
    OMcp15_36 = OMcp15_35+ROcp15_95*qd[6]
    OPcp15_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp15_26 = ROcp15_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp15_35*S5-ROcp15_95*qd[4])
    OPcp15_36 = ROcp15_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp15_25*S5-ROcp15_85*qd[4])

# = = Block_1_0_0_16_0_4 = = 
 
# Sensor Kinematics 


    ROcp15_415 = ROcp15_46*C15+S15*S5
    ROcp15_515 = ROcp15_56*C15+ROcp15_85*S15
    ROcp15_615 = ROcp15_66*C15+ROcp15_95*S15
    ROcp15_715 = -(ROcp15_46*S15-C15*S5)
    ROcp15_815 = -(ROcp15_56*S15-ROcp15_85*C15)
    ROcp15_915 = -(ROcp15_66*S15-ROcp15_95*C15)
    ROcp15_416 = ROcp15_415*C16+ROcp15_715*S16
    ROcp15_516 = ROcp15_515*C16+ROcp15_815*S16
    ROcp15_616 = ROcp15_615*C16+ROcp15_915*S16
    ROcp15_716 = -(ROcp15_415*S16-ROcp15_715*C16)
    ROcp15_816 = -(ROcp15_515*S16-ROcp15_815*C16)
    ROcp15_916 = -(ROcp15_615*S16-ROcp15_915*C16)
    RLcp15_115 = ROcp15_16*s.dpt[1,9]+ROcp15_46*s.dpt[2,9]+s.dpt[3,9]*S5
    RLcp15_215 = ROcp15_26*s.dpt[1,9]+ROcp15_56*s.dpt[2,9]+ROcp15_85*s.dpt[3,9]
    RLcp15_315 = ROcp15_36*s.dpt[1,9]+ROcp15_66*s.dpt[2,9]+ROcp15_95*s.dpt[3,9]
    OMcp15_115 = OMcp15_16+ROcp15_16*qd[15]
    OMcp15_215 = OMcp15_26+ROcp15_26*qd[15]
    OMcp15_315 = OMcp15_36+ROcp15_36*qd[15]
    ORcp15_115 = OMcp15_26*RLcp15_315-OMcp15_36*RLcp15_215
    ORcp15_215 = -(OMcp15_16*RLcp15_315-OMcp15_36*RLcp15_115)
    ORcp15_315 = OMcp15_16*RLcp15_215-OMcp15_26*RLcp15_115
    OPcp15_115 = OPcp15_16+ROcp15_16*qdd[15]+qd[15]*(OMcp15_26*ROcp15_36-OMcp15_36*ROcp15_26)
    OPcp15_215 = OPcp15_26+ROcp15_26*qdd[15]-qd[15]*(OMcp15_16*ROcp15_36-OMcp15_36*ROcp15_16)
    OPcp15_315 = OPcp15_36+ROcp15_36*qdd[15]+qd[15]*(OMcp15_16*ROcp15_26-OMcp15_26*ROcp15_16)
    RLcp15_116 = ROcp15_415*s.dpt[2,21]
    RLcp15_216 = ROcp15_515*s.dpt[2,21]
    RLcp15_316 = ROcp15_615*s.dpt[2,21]
    POcp15_116 = RLcp15_115+RLcp15_116+q[1]
    POcp15_216 = RLcp15_215+RLcp15_216+q[2]
    POcp15_316 = RLcp15_315+RLcp15_316+q[3]
    OMcp15_116 = OMcp15_115+ROcp15_16*qd[16]
    OMcp15_216 = OMcp15_215+ROcp15_26*qd[16]
    OMcp15_316 = OMcp15_315+ROcp15_36*qd[16]
    ORcp15_116 = OMcp15_215*RLcp15_316-OMcp15_315*RLcp15_216
    ORcp15_216 = -(OMcp15_115*RLcp15_316-OMcp15_315*RLcp15_116)
    ORcp15_316 = OMcp15_115*RLcp15_216-OMcp15_215*RLcp15_116
    VIcp15_116 = ORcp15_115+ORcp15_116+qd[1]
    VIcp15_216 = ORcp15_215+ORcp15_216+qd[2]
    VIcp15_316 = ORcp15_315+ORcp15_316+qd[3]
    OPcp15_116 = OPcp15_115+ROcp15_16*qdd[16]+qd[16]*(OMcp15_215*ROcp15_36-OMcp15_315*ROcp15_26)
    OPcp15_216 = OPcp15_215+ROcp15_26*qdd[16]-qd[16]*(OMcp15_115*ROcp15_36-OMcp15_315*ROcp15_16)
    OPcp15_316 = OPcp15_315+ROcp15_36*qdd[16]+qd[16]*(OMcp15_115*ROcp15_26-OMcp15_215*ROcp15_16)
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
    sens.R[1,1] = ROcp15_16
    sens.R[1,2] = ROcp15_26
    sens.R[1,3] = ROcp15_36
    sens.R[2,1] = ROcp15_416
    sens.R[2,2] = ROcp15_516
    sens.R[2,3] = ROcp15_616
    sens.R[3,1] = ROcp15_716
    sens.R[3,2] = ROcp15_816
    sens.R[3,3] = ROcp15_916
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


    ROcp16_25 = S4*S5
    ROcp16_35 = -C4*S5
    ROcp16_85 = -S4*C5
    ROcp16_95 = C4*C5
    ROcp16_16 = C5*C6
    ROcp16_26 = ROcp16_25*C6+C4*S6
    ROcp16_36 = ROcp16_35*C6+S4*S6
    ROcp16_46 = -C5*S6
    ROcp16_56 = -(ROcp16_25*S6-C4*C6)
    ROcp16_66 = -(ROcp16_35*S6-S4*C6)
    OMcp16_25 = qd[5]*C4
    OMcp16_35 = qd[5]*S4
    OMcp16_16 = qd[4]+qd[6]*S5
    OMcp16_26 = OMcp16_25+ROcp16_85*qd[6]
    OMcp16_36 = OMcp16_35+ROcp16_95*qd[6]
    OPcp16_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp16_26 = ROcp16_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp16_35*S5-ROcp16_95*qd[4])
    OPcp16_36 = ROcp16_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp16_25*S5-ROcp16_85*qd[4])

# = = Block_1_0_0_17_0_4 = = 
 
# Sensor Kinematics 


    ROcp16_415 = ROcp16_46*C15+S15*S5
    ROcp16_515 = ROcp16_56*C15+ROcp16_85*S15
    ROcp16_615 = ROcp16_66*C15+ROcp16_95*S15
    ROcp16_715 = -(ROcp16_46*S15-C15*S5)
    ROcp16_815 = -(ROcp16_56*S15-ROcp16_85*C15)
    ROcp16_915 = -(ROcp16_66*S15-ROcp16_95*C15)
    ROcp16_416 = ROcp16_415*C16+ROcp16_715*S16
    ROcp16_516 = ROcp16_515*C16+ROcp16_815*S16
    ROcp16_616 = ROcp16_615*C16+ROcp16_915*S16
    ROcp16_716 = -(ROcp16_415*S16-ROcp16_715*C16)
    ROcp16_816 = -(ROcp16_515*S16-ROcp16_815*C16)
    ROcp16_916 = -(ROcp16_615*S16-ROcp16_915*C16)
    ROcp16_417 = ROcp16_416*C17+ROcp16_716*S17
    ROcp16_517 = ROcp16_516*C17+ROcp16_816*S17
    ROcp16_617 = ROcp16_616*C17+ROcp16_916*S17
    ROcp16_717 = -(ROcp16_416*S17-ROcp16_716*C17)
    ROcp16_817 = -(ROcp16_516*S17-ROcp16_816*C17)
    ROcp16_917 = -(ROcp16_616*S17-ROcp16_916*C17)
    RLcp16_115 = ROcp16_16*s.dpt[1,9]+ROcp16_46*s.dpt[2,9]+s.dpt[3,9]*S5
    RLcp16_215 = ROcp16_26*s.dpt[1,9]+ROcp16_56*s.dpt[2,9]+ROcp16_85*s.dpt[3,9]
    RLcp16_315 = ROcp16_36*s.dpt[1,9]+ROcp16_66*s.dpt[2,9]+ROcp16_95*s.dpt[3,9]
    OMcp16_115 = OMcp16_16+ROcp16_16*qd[15]
    OMcp16_215 = OMcp16_26+ROcp16_26*qd[15]
    OMcp16_315 = OMcp16_36+ROcp16_36*qd[15]
    ORcp16_115 = OMcp16_26*RLcp16_315-OMcp16_36*RLcp16_215
    ORcp16_215 = -(OMcp16_16*RLcp16_315-OMcp16_36*RLcp16_115)
    ORcp16_315 = OMcp16_16*RLcp16_215-OMcp16_26*RLcp16_115
    OPcp16_115 = OPcp16_16+ROcp16_16*qdd[15]+qd[15]*(OMcp16_26*ROcp16_36-OMcp16_36*ROcp16_26)
    OPcp16_215 = OPcp16_26+ROcp16_26*qdd[15]-qd[15]*(OMcp16_16*ROcp16_36-OMcp16_36*ROcp16_16)
    OPcp16_315 = OPcp16_36+ROcp16_36*qdd[15]+qd[15]*(OMcp16_16*ROcp16_26-OMcp16_26*ROcp16_16)
    RLcp16_116 = ROcp16_415*s.dpt[2,21]
    RLcp16_216 = ROcp16_515*s.dpt[2,21]
    RLcp16_316 = ROcp16_615*s.dpt[2,21]
    OMcp16_116 = OMcp16_115+ROcp16_16*qd[16]
    OMcp16_216 = OMcp16_215+ROcp16_26*qd[16]
    OMcp16_316 = OMcp16_315+ROcp16_36*qd[16]
    ORcp16_116 = OMcp16_215*RLcp16_316-OMcp16_315*RLcp16_216
    ORcp16_216 = -(OMcp16_115*RLcp16_316-OMcp16_315*RLcp16_116)
    ORcp16_316 = OMcp16_115*RLcp16_216-OMcp16_215*RLcp16_116
    OPcp16_116 = OPcp16_115+ROcp16_16*qdd[16]+qd[16]*(OMcp16_215*ROcp16_36-OMcp16_315*ROcp16_26)
    OPcp16_216 = OPcp16_215+ROcp16_26*qdd[16]-qd[16]*(OMcp16_115*ROcp16_36-OMcp16_315*ROcp16_16)
    OPcp16_316 = OPcp16_315+ROcp16_36*qdd[16]+qd[16]*(OMcp16_115*ROcp16_26-OMcp16_215*ROcp16_16)
    RLcp16_117 = ROcp16_16*s.dpt[1,23]
    RLcp16_217 = ROcp16_26*s.dpt[1,23]
    RLcp16_317 = ROcp16_36*s.dpt[1,23]
    POcp16_117 = RLcp16_115+RLcp16_116+RLcp16_117+q[1]
    POcp16_217 = RLcp16_215+RLcp16_216+RLcp16_217+q[2]
    POcp16_317 = RLcp16_315+RLcp16_316+RLcp16_317+q[3]
    OMcp16_117 = OMcp16_116+ROcp16_16*qd[17]
    OMcp16_217 = OMcp16_216+ROcp16_26*qd[17]
    OMcp16_317 = OMcp16_316+ROcp16_36*qd[17]
    ORcp16_117 = OMcp16_216*RLcp16_317-OMcp16_316*RLcp16_217
    ORcp16_217 = -(OMcp16_116*RLcp16_317-OMcp16_316*RLcp16_117)
    ORcp16_317 = OMcp16_116*RLcp16_217-OMcp16_216*RLcp16_117
    VIcp16_117 = ORcp16_115+ORcp16_116+ORcp16_117+qd[1]
    VIcp16_217 = ORcp16_215+ORcp16_216+ORcp16_217+qd[2]
    VIcp16_317 = ORcp16_315+ORcp16_316+ORcp16_317+qd[3]
    OPcp16_117 = OPcp16_116+ROcp16_16*qdd[17]+qd[17]*(OMcp16_216*ROcp16_36-OMcp16_316*ROcp16_26)
    OPcp16_217 = OPcp16_216+ROcp16_26*qdd[17]-qd[17]*(OMcp16_116*ROcp16_36-OMcp16_316*ROcp16_16)
    OPcp16_317 = OPcp16_316+ROcp16_36*qdd[17]+qd[17]*(OMcp16_116*ROcp16_26-OMcp16_216*ROcp16_16)
    ACcp16_117 = qdd[1]+OMcp16_215*ORcp16_316+OMcp16_216*ORcp16_317+OMcp16_26*ORcp16_315-OMcp16_315*ORcp16_216-OMcp16_316*\
   ORcp16_217-OMcp16_36*ORcp16_215+OPcp16_215*RLcp16_316+OPcp16_216*RLcp16_317+OPcp16_26*RLcp16_315-OPcp16_315*RLcp16_216-\
   OPcp16_316*RLcp16_217-OPcp16_36*RLcp16_215
    ACcp16_217 = qdd[2]-OMcp16_115*ORcp16_316-OMcp16_116*ORcp16_317-OMcp16_16*ORcp16_315+OMcp16_315*ORcp16_116+OMcp16_316*\
   ORcp16_117+OMcp16_36*ORcp16_115-OPcp16_115*RLcp16_316-OPcp16_116*RLcp16_317-OPcp16_16*RLcp16_315+OPcp16_315*RLcp16_116+\
   OPcp16_316*RLcp16_117+OPcp16_36*RLcp16_115
    ACcp16_317 = qdd[3]+OMcp16_115*ORcp16_216+OMcp16_116*ORcp16_217+OMcp16_16*ORcp16_215-OMcp16_215*ORcp16_116-OMcp16_216*\
   ORcp16_117-OMcp16_26*ORcp16_115+OPcp16_115*RLcp16_216+OPcp16_116*RLcp16_217+OPcp16_16*RLcp16_215-OPcp16_215*RLcp16_116-\
   OPcp16_216*RLcp16_117-OPcp16_26*RLcp16_115

# = = Block_1_0_0_17_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp16_117
    sens.P[2] = POcp16_217
    sens.P[3] = POcp16_317
    sens.R[1,1] = ROcp16_16
    sens.R[1,2] = ROcp16_26
    sens.R[1,3] = ROcp16_36
    sens.R[2,1] = ROcp16_417
    sens.R[2,2] = ROcp16_517
    sens.R[2,3] = ROcp16_617
    sens.R[3,1] = ROcp16_717
    sens.R[3,2] = ROcp16_817
    sens.R[3,3] = ROcp16_917
    sens.V[1] = VIcp16_117
    sens.V[2] = VIcp16_217
    sens.V[3] = VIcp16_317
    sens.OM[1] = OMcp16_117
    sens.OM[2] = OMcp16_217
    sens.OM[3] = OMcp16_317
    sens.A[1] = ACcp16_117
    sens.A[2] = ACcp16_217
    sens.A[3] = ACcp16_317
    sens.OMP[1] = OPcp16_117
    sens.OMP[2] = OPcp16_217
    sens.OMP[3] = OPcp16_317
 
# 
  elif(isens==18): 


# = = Block_1_0_0_18_0_1 = = 
 
# Sensor Kinematics 


    ROcp17_25 = S4*S5
    ROcp17_35 = -C4*S5
    ROcp17_85 = -S4*C5
    ROcp17_95 = C4*C5
    ROcp17_16 = C5*C6
    ROcp17_26 = ROcp17_25*C6+C4*S6
    ROcp17_36 = ROcp17_35*C6+S4*S6
    ROcp17_46 = -C5*S6
    ROcp17_56 = -(ROcp17_25*S6-C4*C6)
    ROcp17_66 = -(ROcp17_35*S6-S4*C6)
    OMcp17_25 = qd[5]*C4
    OMcp17_35 = qd[5]*S4
    OMcp17_16 = qd[4]+qd[6]*S5
    OMcp17_26 = OMcp17_25+ROcp17_85*qd[6]
    OMcp17_36 = OMcp17_35+ROcp17_95*qd[6]
    OPcp17_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp17_26 = ROcp17_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp17_35*S5-ROcp17_95*qd[4])
    OPcp17_36 = ROcp17_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp17_25*S5-ROcp17_85*qd[4])

# = = Block_1_0_0_18_0_4 = = 
 
# Sensor Kinematics 


    ROcp17_415 = ROcp17_46*C15+S15*S5
    ROcp17_515 = ROcp17_56*C15+ROcp17_85*S15
    ROcp17_615 = ROcp17_66*C15+ROcp17_95*S15
    ROcp17_715 = -(ROcp17_46*S15-C15*S5)
    ROcp17_815 = -(ROcp17_56*S15-ROcp17_85*C15)
    ROcp17_915 = -(ROcp17_66*S15-ROcp17_95*C15)
    ROcp17_416 = ROcp17_415*C16+ROcp17_715*S16
    ROcp17_516 = ROcp17_515*C16+ROcp17_815*S16
    ROcp17_616 = ROcp17_615*C16+ROcp17_915*S16
    ROcp17_716 = -(ROcp17_415*S16-ROcp17_715*C16)
    ROcp17_816 = -(ROcp17_515*S16-ROcp17_815*C16)
    ROcp17_916 = -(ROcp17_615*S16-ROcp17_915*C16)
    ROcp17_417 = ROcp17_416*C17+ROcp17_716*S17
    ROcp17_517 = ROcp17_516*C17+ROcp17_816*S17
    ROcp17_617 = ROcp17_616*C17+ROcp17_916*S17
    ROcp17_717 = -(ROcp17_416*S17-ROcp17_716*C17)
    ROcp17_817 = -(ROcp17_516*S17-ROcp17_816*C17)
    ROcp17_917 = -(ROcp17_616*S17-ROcp17_916*C17)
    ROcp17_118 = ROcp17_16*C18-ROcp17_717*S18
    ROcp17_218 = ROcp17_26*C18-ROcp17_817*S18
    ROcp17_318 = ROcp17_36*C18-ROcp17_917*S18
    ROcp17_718 = ROcp17_16*S18+ROcp17_717*C18
    ROcp17_818 = ROcp17_26*S18+ROcp17_817*C18
    ROcp17_918 = ROcp17_36*S18+ROcp17_917*C18
    RLcp17_115 = ROcp17_16*s.dpt[1,9]+ROcp17_46*s.dpt[2,9]+s.dpt[3,9]*S5
    RLcp17_215 = ROcp17_26*s.dpt[1,9]+ROcp17_56*s.dpt[2,9]+ROcp17_85*s.dpt[3,9]
    RLcp17_315 = ROcp17_36*s.dpt[1,9]+ROcp17_66*s.dpt[2,9]+ROcp17_95*s.dpt[3,9]
    OMcp17_115 = OMcp17_16+ROcp17_16*qd[15]
    OMcp17_215 = OMcp17_26+ROcp17_26*qd[15]
    OMcp17_315 = OMcp17_36+ROcp17_36*qd[15]
    ORcp17_115 = OMcp17_26*RLcp17_315-OMcp17_36*RLcp17_215
    ORcp17_215 = -(OMcp17_16*RLcp17_315-OMcp17_36*RLcp17_115)
    ORcp17_315 = OMcp17_16*RLcp17_215-OMcp17_26*RLcp17_115
    OPcp17_115 = OPcp17_16+ROcp17_16*qdd[15]+qd[15]*(OMcp17_26*ROcp17_36-OMcp17_36*ROcp17_26)
    OPcp17_215 = OPcp17_26+ROcp17_26*qdd[15]-qd[15]*(OMcp17_16*ROcp17_36-OMcp17_36*ROcp17_16)
    OPcp17_315 = OPcp17_36+ROcp17_36*qdd[15]+qd[15]*(OMcp17_16*ROcp17_26-OMcp17_26*ROcp17_16)
    RLcp17_116 = ROcp17_415*s.dpt[2,21]
    RLcp17_216 = ROcp17_515*s.dpt[2,21]
    RLcp17_316 = ROcp17_615*s.dpt[2,21]
    OMcp17_116 = OMcp17_115+ROcp17_16*qd[16]
    OMcp17_216 = OMcp17_215+ROcp17_26*qd[16]
    OMcp17_316 = OMcp17_315+ROcp17_36*qd[16]
    ORcp17_116 = OMcp17_215*RLcp17_316-OMcp17_315*RLcp17_216
    ORcp17_216 = -(OMcp17_115*RLcp17_316-OMcp17_315*RLcp17_116)
    ORcp17_316 = OMcp17_115*RLcp17_216-OMcp17_215*RLcp17_116
    OPcp17_116 = OPcp17_115+ROcp17_16*qdd[16]+qd[16]*(OMcp17_215*ROcp17_36-OMcp17_315*ROcp17_26)
    OPcp17_216 = OPcp17_215+ROcp17_26*qdd[16]-qd[16]*(OMcp17_115*ROcp17_36-OMcp17_315*ROcp17_16)
    OPcp17_316 = OPcp17_315+ROcp17_36*qdd[16]+qd[16]*(OMcp17_115*ROcp17_26-OMcp17_215*ROcp17_16)
    RLcp17_117 = ROcp17_16*s.dpt[1,23]
    RLcp17_217 = ROcp17_26*s.dpt[1,23]
    RLcp17_317 = ROcp17_36*s.dpt[1,23]
    POcp17_117 = RLcp17_115+RLcp17_116+RLcp17_117+q[1]
    POcp17_217 = RLcp17_215+RLcp17_216+RLcp17_217+q[2]
    POcp17_317 = RLcp17_315+RLcp17_316+RLcp17_317+q[3]
    OMcp17_117 = OMcp17_116+ROcp17_16*qd[17]
    OMcp17_217 = OMcp17_216+ROcp17_26*qd[17]
    OMcp17_317 = OMcp17_316+ROcp17_36*qd[17]
    ORcp17_117 = OMcp17_216*RLcp17_317-OMcp17_316*RLcp17_217
    ORcp17_217 = -(OMcp17_116*RLcp17_317-OMcp17_316*RLcp17_117)
    ORcp17_317 = OMcp17_116*RLcp17_217-OMcp17_216*RLcp17_117
    VIcp17_117 = ORcp17_115+ORcp17_116+ORcp17_117+qd[1]
    VIcp17_217 = ORcp17_215+ORcp17_216+ORcp17_217+qd[2]
    VIcp17_317 = ORcp17_315+ORcp17_316+ORcp17_317+qd[3]
    ACcp17_117 = qdd[1]+OMcp17_215*ORcp17_316+OMcp17_216*ORcp17_317+OMcp17_26*ORcp17_315-OMcp17_315*ORcp17_216-OMcp17_316*\
   ORcp17_217-OMcp17_36*ORcp17_215+OPcp17_215*RLcp17_316+OPcp17_216*RLcp17_317+OPcp17_26*RLcp17_315-OPcp17_315*RLcp17_216-\
   OPcp17_316*RLcp17_217-OPcp17_36*RLcp17_215
    ACcp17_217 = qdd[2]-OMcp17_115*ORcp17_316-OMcp17_116*ORcp17_317-OMcp17_16*ORcp17_315+OMcp17_315*ORcp17_116+OMcp17_316*\
   ORcp17_117+OMcp17_36*ORcp17_115-OPcp17_115*RLcp17_316-OPcp17_116*RLcp17_317-OPcp17_16*RLcp17_315+OPcp17_315*RLcp17_116+\
   OPcp17_316*RLcp17_117+OPcp17_36*RLcp17_115
    ACcp17_317 = qdd[3]+OMcp17_115*ORcp17_216+OMcp17_116*ORcp17_217+OMcp17_16*ORcp17_215-OMcp17_215*ORcp17_116-OMcp17_216*\
   ORcp17_117-OMcp17_26*ORcp17_115+OPcp17_115*RLcp17_216+OPcp17_116*RLcp17_217+OPcp17_16*RLcp17_215-OPcp17_215*RLcp17_116-\
   OPcp17_216*RLcp17_117-OPcp17_26*RLcp17_115
    OMcp17_118 = OMcp17_117+ROcp17_417*qd[18]
    OMcp17_218 = OMcp17_217+ROcp17_517*qd[18]
    OMcp17_318 = OMcp17_317+ROcp17_617*qd[18]
    OPcp17_118 = OPcp17_116+ROcp17_16*qdd[17]+ROcp17_417*qdd[18]+qd[17]*(OMcp17_216*ROcp17_36-OMcp17_316*ROcp17_26)+qd[18]\
   *(OMcp17_217*ROcp17_617-OMcp17_317*ROcp17_517)
    OPcp17_218 = OPcp17_216+ROcp17_26*qdd[17]+ROcp17_517*qdd[18]-qd[17]*(OMcp17_116*ROcp17_36-OMcp17_316*ROcp17_16)-qd[18]\
   *(OMcp17_117*ROcp17_617-OMcp17_317*ROcp17_417)
    OPcp17_318 = OPcp17_316+ROcp17_36*qdd[17]+ROcp17_617*qdd[18]+qd[17]*(OMcp17_116*ROcp17_26-OMcp17_216*ROcp17_16)+qd[18]\
   *(OMcp17_117*ROcp17_517-OMcp17_217*ROcp17_417)

# = = Block_1_0_0_18_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp17_117
    sens.P[2] = POcp17_217
    sens.P[3] = POcp17_317
    sens.R[1,1] = ROcp17_118
    sens.R[1,2] = ROcp17_218
    sens.R[1,3] = ROcp17_318
    sens.R[2,1] = ROcp17_417
    sens.R[2,2] = ROcp17_517
    sens.R[2,3] = ROcp17_617
    sens.R[3,1] = ROcp17_718
    sens.R[3,2] = ROcp17_818
    sens.R[3,3] = ROcp17_918
    sens.V[1] = VIcp17_117
    sens.V[2] = VIcp17_217
    sens.V[3] = VIcp17_317
    sens.OM[1] = OMcp17_118
    sens.OM[2] = OMcp17_218
    sens.OM[3] = OMcp17_318
    sens.A[1] = ACcp17_117
    sens.A[2] = ACcp17_217
    sens.A[3] = ACcp17_317
    sens.OMP[1] = OPcp17_118
    sens.OMP[2] = OPcp17_218
    sens.OMP[3] = OPcp17_318
 
# 
  elif(isens==19): 


# = = Block_1_0_0_19_0_1 = = 
 
# Sensor Kinematics 


    ROcp18_25 = S4*S5
    ROcp18_35 = -C4*S5
    ROcp18_85 = -S4*C5
    ROcp18_95 = C4*C5
    ROcp18_16 = C5*C6
    ROcp18_26 = ROcp18_25*C6+C4*S6
    ROcp18_36 = ROcp18_35*C6+S4*S6
    ROcp18_46 = -C5*S6
    ROcp18_56 = -(ROcp18_25*S6-C4*C6)
    ROcp18_66 = -(ROcp18_35*S6-S4*C6)
    OMcp18_25 = qd[5]*C4
    OMcp18_35 = qd[5]*S4
    OMcp18_16 = qd[4]+qd[6]*S5
    OMcp18_26 = OMcp18_25+ROcp18_85*qd[6]
    OMcp18_36 = OMcp18_35+ROcp18_95*qd[6]
    OPcp18_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp18_26 = ROcp18_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp18_35*S5-ROcp18_95*qd[4])
    OPcp18_36 = ROcp18_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp18_25*S5-ROcp18_85*qd[4])

# = = Block_1_0_0_19_0_5 = = 
 
# Sensor Kinematics 


    ROcp18_419 = ROcp18_46*C19+S19*S5
    ROcp18_519 = ROcp18_56*C19+ROcp18_85*S19
    ROcp18_619 = ROcp18_66*C19+ROcp18_95*S19
    ROcp18_719 = -(ROcp18_46*S19-C19*S5)
    ROcp18_819 = -(ROcp18_56*S19-ROcp18_85*C19)
    ROcp18_919 = -(ROcp18_66*S19-ROcp18_95*C19)
    RLcp18_119 = ROcp18_16*s.dpt[1,11]+ROcp18_46*s.dpt[2,11]+s.dpt[3,11]*S5
    RLcp18_219 = ROcp18_26*s.dpt[1,11]+ROcp18_56*s.dpt[2,11]+ROcp18_85*s.dpt[3,11]
    RLcp18_319 = ROcp18_36*s.dpt[1,11]+ROcp18_66*s.dpt[2,11]+ROcp18_95*s.dpt[3,11]
    POcp18_119 = RLcp18_119+q[1]
    POcp18_219 = RLcp18_219+q[2]
    POcp18_319 = RLcp18_319+q[3]
    OMcp18_119 = OMcp18_16+ROcp18_16*qd[19]
    OMcp18_219 = OMcp18_26+ROcp18_26*qd[19]
    OMcp18_319 = OMcp18_36+ROcp18_36*qd[19]
    ORcp18_119 = OMcp18_26*RLcp18_319-OMcp18_36*RLcp18_219
    ORcp18_219 = -(OMcp18_16*RLcp18_319-OMcp18_36*RLcp18_119)
    ORcp18_319 = OMcp18_16*RLcp18_219-OMcp18_26*RLcp18_119
    VIcp18_119 = ORcp18_119+qd[1]
    VIcp18_219 = ORcp18_219+qd[2]
    VIcp18_319 = ORcp18_319+qd[3]
    OPcp18_119 = OPcp18_16+ROcp18_16*qdd[19]+qd[19]*(OMcp18_26*ROcp18_36-OMcp18_36*ROcp18_26)
    OPcp18_219 = OPcp18_26+ROcp18_26*qdd[19]-qd[19]*(OMcp18_16*ROcp18_36-OMcp18_36*ROcp18_16)
    OPcp18_319 = OPcp18_36+ROcp18_36*qdd[19]+qd[19]*(OMcp18_16*ROcp18_26-OMcp18_26*ROcp18_16)
    ACcp18_119 = qdd[1]+OMcp18_26*ORcp18_319-OMcp18_36*ORcp18_219+OPcp18_26*RLcp18_319-OPcp18_36*RLcp18_219
    ACcp18_219 = qdd[2]-OMcp18_16*ORcp18_319+OMcp18_36*ORcp18_119-OPcp18_16*RLcp18_319+OPcp18_36*RLcp18_119
    ACcp18_319 = qdd[3]+OMcp18_16*ORcp18_219-OMcp18_26*ORcp18_119+OPcp18_16*RLcp18_219-OPcp18_26*RLcp18_119

# = = Block_1_0_0_19_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp18_119
    sens.P[2] = POcp18_219
    sens.P[3] = POcp18_319
    sens.R[1,1] = ROcp18_16
    sens.R[1,2] = ROcp18_26
    sens.R[1,3] = ROcp18_36
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


    ROcp19_25 = S4*S5
    ROcp19_35 = -C4*S5
    ROcp19_85 = -S4*C5
    ROcp19_95 = C4*C5
    ROcp19_16 = C5*C6
    ROcp19_26 = ROcp19_25*C6+C4*S6
    ROcp19_36 = ROcp19_35*C6+S4*S6
    ROcp19_46 = -C5*S6
    ROcp19_56 = -(ROcp19_25*S6-C4*C6)
    ROcp19_66 = -(ROcp19_35*S6-S4*C6)
    OMcp19_25 = qd[5]*C4
    OMcp19_35 = qd[5]*S4
    OMcp19_16 = qd[4]+qd[6]*S5
    OMcp19_26 = OMcp19_25+ROcp19_85*qd[6]
    OMcp19_36 = OMcp19_35+ROcp19_95*qd[6]
    OPcp19_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp19_26 = ROcp19_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp19_35*S5-ROcp19_95*qd[4])
    OPcp19_36 = ROcp19_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp19_25*S5-ROcp19_85*qd[4])

# = = Block_1_0_0_20_0_5 = = 
 
# Sensor Kinematics 


    ROcp19_419 = ROcp19_46*C19+S19*S5
    ROcp19_519 = ROcp19_56*C19+ROcp19_85*S19
    ROcp19_619 = ROcp19_66*C19+ROcp19_95*S19
    ROcp19_719 = -(ROcp19_46*S19-C19*S5)
    ROcp19_819 = -(ROcp19_56*S19-ROcp19_85*C19)
    ROcp19_919 = -(ROcp19_66*S19-ROcp19_95*C19)
    ROcp19_420 = ROcp19_419*C20+ROcp19_719*S20
    ROcp19_520 = ROcp19_519*C20+ROcp19_819*S20
    ROcp19_620 = ROcp19_619*C20+ROcp19_919*S20
    ROcp19_720 = -(ROcp19_419*S20-ROcp19_719*C20)
    ROcp19_820 = -(ROcp19_519*S20-ROcp19_819*C20)
    ROcp19_920 = -(ROcp19_619*S20-ROcp19_919*C20)
    RLcp19_119 = ROcp19_16*s.dpt[1,11]+ROcp19_46*s.dpt[2,11]+s.dpt[3,11]*S5
    RLcp19_219 = ROcp19_26*s.dpt[1,11]+ROcp19_56*s.dpt[2,11]+ROcp19_85*s.dpt[3,11]
    RLcp19_319 = ROcp19_36*s.dpt[1,11]+ROcp19_66*s.dpt[2,11]+ROcp19_95*s.dpt[3,11]
    OMcp19_119 = OMcp19_16+ROcp19_16*qd[19]
    OMcp19_219 = OMcp19_26+ROcp19_26*qd[19]
    OMcp19_319 = OMcp19_36+ROcp19_36*qd[19]
    ORcp19_119 = OMcp19_26*RLcp19_319-OMcp19_36*RLcp19_219
    ORcp19_219 = -(OMcp19_16*RLcp19_319-OMcp19_36*RLcp19_119)
    ORcp19_319 = OMcp19_16*RLcp19_219-OMcp19_26*RLcp19_119
    OPcp19_119 = OPcp19_16+ROcp19_16*qdd[19]+qd[19]*(OMcp19_26*ROcp19_36-OMcp19_36*ROcp19_26)
    OPcp19_219 = OPcp19_26+ROcp19_26*qdd[19]-qd[19]*(OMcp19_16*ROcp19_36-OMcp19_36*ROcp19_16)
    OPcp19_319 = OPcp19_36+ROcp19_36*qdd[19]+qd[19]*(OMcp19_16*ROcp19_26-OMcp19_26*ROcp19_16)
    RLcp19_120 = ROcp19_419*s.dpt[2,27]
    RLcp19_220 = ROcp19_519*s.dpt[2,27]
    RLcp19_320 = ROcp19_619*s.dpt[2,27]
    POcp19_120 = RLcp19_119+RLcp19_120+q[1]
    POcp19_220 = RLcp19_219+RLcp19_220+q[2]
    POcp19_320 = RLcp19_319+RLcp19_320+q[3]
    OMcp19_120 = OMcp19_119+ROcp19_16*qd[20]
    OMcp19_220 = OMcp19_219+ROcp19_26*qd[20]
    OMcp19_320 = OMcp19_319+ROcp19_36*qd[20]
    ORcp19_120 = OMcp19_219*RLcp19_320-OMcp19_319*RLcp19_220
    ORcp19_220 = -(OMcp19_119*RLcp19_320-OMcp19_319*RLcp19_120)
    ORcp19_320 = OMcp19_119*RLcp19_220-OMcp19_219*RLcp19_120
    VIcp19_120 = ORcp19_119+ORcp19_120+qd[1]
    VIcp19_220 = ORcp19_219+ORcp19_220+qd[2]
    VIcp19_320 = ORcp19_319+ORcp19_320+qd[3]
    OPcp19_120 = OPcp19_119+ROcp19_16*qdd[20]+qd[20]*(OMcp19_219*ROcp19_36-OMcp19_319*ROcp19_26)
    OPcp19_220 = OPcp19_219+ROcp19_26*qdd[20]-qd[20]*(OMcp19_119*ROcp19_36-OMcp19_319*ROcp19_16)
    OPcp19_320 = OPcp19_319+ROcp19_36*qdd[20]+qd[20]*(OMcp19_119*ROcp19_26-OMcp19_219*ROcp19_16)
    ACcp19_120 = qdd[1]+OMcp19_219*ORcp19_320+OMcp19_26*ORcp19_319-OMcp19_319*ORcp19_220-OMcp19_36*ORcp19_219+OPcp19_219*\
   RLcp19_320+OPcp19_26*RLcp19_319-OPcp19_319*RLcp19_220-OPcp19_36*RLcp19_219
    ACcp19_220 = qdd[2]-OMcp19_119*ORcp19_320-OMcp19_16*ORcp19_319+OMcp19_319*ORcp19_120+OMcp19_36*ORcp19_119-OPcp19_119*\
   RLcp19_320-OPcp19_16*RLcp19_319+OPcp19_319*RLcp19_120+OPcp19_36*RLcp19_119
    ACcp19_320 = qdd[3]+OMcp19_119*ORcp19_220+OMcp19_16*ORcp19_219-OMcp19_219*ORcp19_120-OMcp19_26*ORcp19_119+OPcp19_119*\
   RLcp19_220+OPcp19_16*RLcp19_219-OPcp19_219*RLcp19_120-OPcp19_26*RLcp19_119

# = = Block_1_0_0_20_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp19_120
    sens.P[2] = POcp19_220
    sens.P[3] = POcp19_320
    sens.R[1,1] = ROcp19_16
    sens.R[1,2] = ROcp19_26
    sens.R[1,3] = ROcp19_36
    sens.R[2,1] = ROcp19_420
    sens.R[2,2] = ROcp19_520
    sens.R[2,3] = ROcp19_620
    sens.R[3,1] = ROcp19_720
    sens.R[3,2] = ROcp19_820
    sens.R[3,3] = ROcp19_920
    sens.V[1] = VIcp19_120
    sens.V[2] = VIcp19_220
    sens.V[3] = VIcp19_320
    sens.OM[1] = OMcp19_120
    sens.OM[2] = OMcp19_220
    sens.OM[3] = OMcp19_320
    sens.A[1] = ACcp19_120
    sens.A[2] = ACcp19_220
    sens.A[3] = ACcp19_320
    sens.OMP[1] = OPcp19_120
    sens.OMP[2] = OPcp19_220
    sens.OMP[3] = OPcp19_320
 
# 
  elif(isens==21): 


# = = Block_1_0_0_21_0_1 = = 
 
# Sensor Kinematics 


    ROcp20_25 = S4*S5
    ROcp20_35 = -C4*S5
    ROcp20_85 = -S4*C5
    ROcp20_95 = C4*C5
    ROcp20_16 = C5*C6
    ROcp20_26 = ROcp20_25*C6+C4*S6
    ROcp20_36 = ROcp20_35*C6+S4*S6
    ROcp20_46 = -C5*S6
    ROcp20_56 = -(ROcp20_25*S6-C4*C6)
    ROcp20_66 = -(ROcp20_35*S6-S4*C6)
    OMcp20_25 = qd[5]*C4
    OMcp20_35 = qd[5]*S4
    OMcp20_16 = qd[4]+qd[6]*S5
    OMcp20_26 = OMcp20_25+ROcp20_85*qd[6]
    OMcp20_36 = OMcp20_35+ROcp20_95*qd[6]
    OPcp20_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp20_26 = ROcp20_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp20_35*S5-ROcp20_95*qd[4])
    OPcp20_36 = ROcp20_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp20_25*S5-ROcp20_85*qd[4])

# = = Block_1_0_0_21_0_5 = = 
 
# Sensor Kinematics 


    ROcp20_419 = ROcp20_46*C19+S19*S5
    ROcp20_519 = ROcp20_56*C19+ROcp20_85*S19
    ROcp20_619 = ROcp20_66*C19+ROcp20_95*S19
    ROcp20_719 = -(ROcp20_46*S19-C19*S5)
    ROcp20_819 = -(ROcp20_56*S19-ROcp20_85*C19)
    ROcp20_919 = -(ROcp20_66*S19-ROcp20_95*C19)
    ROcp20_420 = ROcp20_419*C20+ROcp20_719*S20
    ROcp20_520 = ROcp20_519*C20+ROcp20_819*S20
    ROcp20_620 = ROcp20_619*C20+ROcp20_919*S20
    ROcp20_720 = -(ROcp20_419*S20-ROcp20_719*C20)
    ROcp20_820 = -(ROcp20_519*S20-ROcp20_819*C20)
    ROcp20_920 = -(ROcp20_619*S20-ROcp20_919*C20)
    ROcp20_421 = ROcp20_420*C21+ROcp20_720*S21
    ROcp20_521 = ROcp20_520*C21+ROcp20_820*S21
    ROcp20_621 = ROcp20_620*C21+ROcp20_920*S21
    ROcp20_721 = -(ROcp20_420*S21-ROcp20_720*C21)
    ROcp20_821 = -(ROcp20_520*S21-ROcp20_820*C21)
    ROcp20_921 = -(ROcp20_620*S21-ROcp20_920*C21)
    RLcp20_119 = ROcp20_16*s.dpt[1,11]+ROcp20_46*s.dpt[2,11]+s.dpt[3,11]*S5
    RLcp20_219 = ROcp20_26*s.dpt[1,11]+ROcp20_56*s.dpt[2,11]+ROcp20_85*s.dpt[3,11]
    RLcp20_319 = ROcp20_36*s.dpt[1,11]+ROcp20_66*s.dpt[2,11]+ROcp20_95*s.dpt[3,11]
    OMcp20_119 = OMcp20_16+ROcp20_16*qd[19]
    OMcp20_219 = OMcp20_26+ROcp20_26*qd[19]
    OMcp20_319 = OMcp20_36+ROcp20_36*qd[19]
    ORcp20_119 = OMcp20_26*RLcp20_319-OMcp20_36*RLcp20_219
    ORcp20_219 = -(OMcp20_16*RLcp20_319-OMcp20_36*RLcp20_119)
    ORcp20_319 = OMcp20_16*RLcp20_219-OMcp20_26*RLcp20_119
    OPcp20_119 = OPcp20_16+ROcp20_16*qdd[19]+qd[19]*(OMcp20_26*ROcp20_36-OMcp20_36*ROcp20_26)
    OPcp20_219 = OPcp20_26+ROcp20_26*qdd[19]-qd[19]*(OMcp20_16*ROcp20_36-OMcp20_36*ROcp20_16)
    OPcp20_319 = OPcp20_36+ROcp20_36*qdd[19]+qd[19]*(OMcp20_16*ROcp20_26-OMcp20_26*ROcp20_16)
    RLcp20_120 = ROcp20_419*s.dpt[2,27]
    RLcp20_220 = ROcp20_519*s.dpt[2,27]
    RLcp20_320 = ROcp20_619*s.dpt[2,27]
    OMcp20_120 = OMcp20_119+ROcp20_16*qd[20]
    OMcp20_220 = OMcp20_219+ROcp20_26*qd[20]
    OMcp20_320 = OMcp20_319+ROcp20_36*qd[20]
    ORcp20_120 = OMcp20_219*RLcp20_320-OMcp20_319*RLcp20_220
    ORcp20_220 = -(OMcp20_119*RLcp20_320-OMcp20_319*RLcp20_120)
    ORcp20_320 = OMcp20_119*RLcp20_220-OMcp20_219*RLcp20_120
    OPcp20_120 = OPcp20_119+ROcp20_16*qdd[20]+qd[20]*(OMcp20_219*ROcp20_36-OMcp20_319*ROcp20_26)
    OPcp20_220 = OPcp20_219+ROcp20_26*qdd[20]-qd[20]*(OMcp20_119*ROcp20_36-OMcp20_319*ROcp20_16)
    OPcp20_320 = OPcp20_319+ROcp20_36*qdd[20]+qd[20]*(OMcp20_119*ROcp20_26-OMcp20_219*ROcp20_16)
    RLcp20_121 = ROcp20_16*s.dpt[1,31]
    RLcp20_221 = ROcp20_26*s.dpt[1,31]
    RLcp20_321 = ROcp20_36*s.dpt[1,31]
    POcp20_121 = RLcp20_119+RLcp20_120+RLcp20_121+q[1]
    POcp20_221 = RLcp20_219+RLcp20_220+RLcp20_221+q[2]
    POcp20_321 = RLcp20_319+RLcp20_320+RLcp20_321+q[3]
    OMcp20_121 = OMcp20_120+ROcp20_16*qd[21]
    OMcp20_221 = OMcp20_220+ROcp20_26*qd[21]
    OMcp20_321 = OMcp20_320+ROcp20_36*qd[21]
    ORcp20_121 = OMcp20_220*RLcp20_321-OMcp20_320*RLcp20_221
    ORcp20_221 = -(OMcp20_120*RLcp20_321-OMcp20_320*RLcp20_121)
    ORcp20_321 = OMcp20_120*RLcp20_221-OMcp20_220*RLcp20_121
    VIcp20_121 = ORcp20_119+ORcp20_120+ORcp20_121+qd[1]
    VIcp20_221 = ORcp20_219+ORcp20_220+ORcp20_221+qd[2]
    VIcp20_321 = ORcp20_319+ORcp20_320+ORcp20_321+qd[3]
    OPcp20_121 = OPcp20_120+ROcp20_16*qdd[21]+qd[21]*(OMcp20_220*ROcp20_36-OMcp20_320*ROcp20_26)
    OPcp20_221 = OPcp20_220+ROcp20_26*qdd[21]-qd[21]*(OMcp20_120*ROcp20_36-OMcp20_320*ROcp20_16)
    OPcp20_321 = OPcp20_320+ROcp20_36*qdd[21]+qd[21]*(OMcp20_120*ROcp20_26-OMcp20_220*ROcp20_16)
    ACcp20_121 = qdd[1]+OMcp20_219*ORcp20_320+OMcp20_220*ORcp20_321+OMcp20_26*ORcp20_319-OMcp20_319*ORcp20_220-OMcp20_320*\
   ORcp20_221-OMcp20_36*ORcp20_219+OPcp20_219*RLcp20_320+OPcp20_220*RLcp20_321+OPcp20_26*RLcp20_319-OPcp20_319*RLcp20_220-\
   OPcp20_320*RLcp20_221-OPcp20_36*RLcp20_219
    ACcp20_221 = qdd[2]-OMcp20_119*ORcp20_320-OMcp20_120*ORcp20_321-OMcp20_16*ORcp20_319+OMcp20_319*ORcp20_120+OMcp20_320*\
   ORcp20_121+OMcp20_36*ORcp20_119-OPcp20_119*RLcp20_320-OPcp20_120*RLcp20_321-OPcp20_16*RLcp20_319+OPcp20_319*RLcp20_120+\
   OPcp20_320*RLcp20_121+OPcp20_36*RLcp20_119
    ACcp20_321 = qdd[3]+OMcp20_119*ORcp20_220+OMcp20_120*ORcp20_221+OMcp20_16*ORcp20_219-OMcp20_219*ORcp20_120-OMcp20_220*\
   ORcp20_121-OMcp20_26*ORcp20_119+OPcp20_119*RLcp20_220+OPcp20_120*RLcp20_221+OPcp20_16*RLcp20_219-OPcp20_219*RLcp20_120-\
   OPcp20_220*RLcp20_121-OPcp20_26*RLcp20_119

# = = Block_1_0_0_21_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp20_121
    sens.P[2] = POcp20_221
    sens.P[3] = POcp20_321
    sens.R[1,1] = ROcp20_16
    sens.R[1,2] = ROcp20_26
    sens.R[1,3] = ROcp20_36
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


    ROcp21_25 = S4*S5
    ROcp21_35 = -C4*S5
    ROcp21_85 = -S4*C5
    ROcp21_95 = C4*C5
    ROcp21_16 = C5*C6
    ROcp21_26 = ROcp21_25*C6+C4*S6
    ROcp21_36 = ROcp21_35*C6+S4*S6
    ROcp21_46 = -C5*S6
    ROcp21_56 = -(ROcp21_25*S6-C4*C6)
    ROcp21_66 = -(ROcp21_35*S6-S4*C6)
    OMcp21_25 = qd[5]*C4
    OMcp21_35 = qd[5]*S4
    OMcp21_16 = qd[4]+qd[6]*S5
    OMcp21_26 = OMcp21_25+ROcp21_85*qd[6]
    OMcp21_36 = OMcp21_35+ROcp21_95*qd[6]
    OPcp21_16 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5
    OPcp21_26 = ROcp21_85*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp21_35*S5-ROcp21_95*qd[4])
    OPcp21_36 = ROcp21_95*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp21_25*S5-ROcp21_85*qd[4])

# = = Block_1_0_0_22_0_5 = = 
 
# Sensor Kinematics 


    ROcp21_419 = ROcp21_46*C19+S19*S5
    ROcp21_519 = ROcp21_56*C19+ROcp21_85*S19
    ROcp21_619 = ROcp21_66*C19+ROcp21_95*S19
    ROcp21_719 = -(ROcp21_46*S19-C19*S5)
    ROcp21_819 = -(ROcp21_56*S19-ROcp21_85*C19)
    ROcp21_919 = -(ROcp21_66*S19-ROcp21_95*C19)
    ROcp21_420 = ROcp21_419*C20+ROcp21_719*S20
    ROcp21_520 = ROcp21_519*C20+ROcp21_819*S20
    ROcp21_620 = ROcp21_619*C20+ROcp21_919*S20
    ROcp21_720 = -(ROcp21_419*S20-ROcp21_719*C20)
    ROcp21_820 = -(ROcp21_519*S20-ROcp21_819*C20)
    ROcp21_920 = -(ROcp21_619*S20-ROcp21_919*C20)
    ROcp21_421 = ROcp21_420*C21+ROcp21_720*S21
    ROcp21_521 = ROcp21_520*C21+ROcp21_820*S21
    ROcp21_621 = ROcp21_620*C21+ROcp21_920*S21
    ROcp21_721 = -(ROcp21_420*S21-ROcp21_720*C21)
    ROcp21_821 = -(ROcp21_520*S21-ROcp21_820*C21)
    ROcp21_921 = -(ROcp21_620*S21-ROcp21_920*C21)
    ROcp21_122 = ROcp21_16*C22-ROcp21_721*S22
    ROcp21_222 = ROcp21_26*C22-ROcp21_821*S22
    ROcp21_322 = ROcp21_36*C22-ROcp21_921*S22
    ROcp21_722 = ROcp21_16*S22+ROcp21_721*C22
    ROcp21_822 = ROcp21_26*S22+ROcp21_821*C22
    ROcp21_922 = ROcp21_36*S22+ROcp21_921*C22
    RLcp21_119 = ROcp21_16*s.dpt[1,11]+ROcp21_46*s.dpt[2,11]+s.dpt[3,11]*S5
    RLcp21_219 = ROcp21_26*s.dpt[1,11]+ROcp21_56*s.dpt[2,11]+ROcp21_85*s.dpt[3,11]
    RLcp21_319 = ROcp21_36*s.dpt[1,11]+ROcp21_66*s.dpt[2,11]+ROcp21_95*s.dpt[3,11]
    OMcp21_119 = OMcp21_16+ROcp21_16*qd[19]
    OMcp21_219 = OMcp21_26+ROcp21_26*qd[19]
    OMcp21_319 = OMcp21_36+ROcp21_36*qd[19]
    ORcp21_119 = OMcp21_26*RLcp21_319-OMcp21_36*RLcp21_219
    ORcp21_219 = -(OMcp21_16*RLcp21_319-OMcp21_36*RLcp21_119)
    ORcp21_319 = OMcp21_16*RLcp21_219-OMcp21_26*RLcp21_119
    OPcp21_119 = OPcp21_16+ROcp21_16*qdd[19]+qd[19]*(OMcp21_26*ROcp21_36-OMcp21_36*ROcp21_26)
    OPcp21_219 = OPcp21_26+ROcp21_26*qdd[19]-qd[19]*(OMcp21_16*ROcp21_36-OMcp21_36*ROcp21_16)
    OPcp21_319 = OPcp21_36+ROcp21_36*qdd[19]+qd[19]*(OMcp21_16*ROcp21_26-OMcp21_26*ROcp21_16)
    RLcp21_120 = ROcp21_419*s.dpt[2,27]
    RLcp21_220 = ROcp21_519*s.dpt[2,27]
    RLcp21_320 = ROcp21_619*s.dpt[2,27]
    OMcp21_120 = OMcp21_119+ROcp21_16*qd[20]
    OMcp21_220 = OMcp21_219+ROcp21_26*qd[20]
    OMcp21_320 = OMcp21_319+ROcp21_36*qd[20]
    ORcp21_120 = OMcp21_219*RLcp21_320-OMcp21_319*RLcp21_220
    ORcp21_220 = -(OMcp21_119*RLcp21_320-OMcp21_319*RLcp21_120)
    ORcp21_320 = OMcp21_119*RLcp21_220-OMcp21_219*RLcp21_120
    OPcp21_120 = OPcp21_119+ROcp21_16*qdd[20]+qd[20]*(OMcp21_219*ROcp21_36-OMcp21_319*ROcp21_26)
    OPcp21_220 = OPcp21_219+ROcp21_26*qdd[20]-qd[20]*(OMcp21_119*ROcp21_36-OMcp21_319*ROcp21_16)
    OPcp21_320 = OPcp21_319+ROcp21_36*qdd[20]+qd[20]*(OMcp21_119*ROcp21_26-OMcp21_219*ROcp21_16)
    RLcp21_121 = ROcp21_16*s.dpt[1,31]
    RLcp21_221 = ROcp21_26*s.dpt[1,31]
    RLcp21_321 = ROcp21_36*s.dpt[1,31]
    POcp21_121 = RLcp21_119+RLcp21_120+RLcp21_121+q[1]
    POcp21_221 = RLcp21_219+RLcp21_220+RLcp21_221+q[2]
    POcp21_321 = RLcp21_319+RLcp21_320+RLcp21_321+q[3]
    OMcp21_121 = OMcp21_120+ROcp21_16*qd[21]
    OMcp21_221 = OMcp21_220+ROcp21_26*qd[21]
    OMcp21_321 = OMcp21_320+ROcp21_36*qd[21]
    ORcp21_121 = OMcp21_220*RLcp21_321-OMcp21_320*RLcp21_221
    ORcp21_221 = -(OMcp21_120*RLcp21_321-OMcp21_320*RLcp21_121)
    ORcp21_321 = OMcp21_120*RLcp21_221-OMcp21_220*RLcp21_121
    VIcp21_121 = ORcp21_119+ORcp21_120+ORcp21_121+qd[1]
    VIcp21_221 = ORcp21_219+ORcp21_220+ORcp21_221+qd[2]
    VIcp21_321 = ORcp21_319+ORcp21_320+ORcp21_321+qd[3]
    ACcp21_121 = qdd[1]+OMcp21_219*ORcp21_320+OMcp21_220*ORcp21_321+OMcp21_26*ORcp21_319-OMcp21_319*ORcp21_220-OMcp21_320*\
   ORcp21_221-OMcp21_36*ORcp21_219+OPcp21_219*RLcp21_320+OPcp21_220*RLcp21_321+OPcp21_26*RLcp21_319-OPcp21_319*RLcp21_220-\
   OPcp21_320*RLcp21_221-OPcp21_36*RLcp21_219
    ACcp21_221 = qdd[2]-OMcp21_119*ORcp21_320-OMcp21_120*ORcp21_321-OMcp21_16*ORcp21_319+OMcp21_319*ORcp21_120+OMcp21_320*\
   ORcp21_121+OMcp21_36*ORcp21_119-OPcp21_119*RLcp21_320-OPcp21_120*RLcp21_321-OPcp21_16*RLcp21_319+OPcp21_319*RLcp21_120+\
   OPcp21_320*RLcp21_121+OPcp21_36*RLcp21_119
    ACcp21_321 = qdd[3]+OMcp21_119*ORcp21_220+OMcp21_120*ORcp21_221+OMcp21_16*ORcp21_219-OMcp21_219*ORcp21_120-OMcp21_220*\
   ORcp21_121-OMcp21_26*ORcp21_119+OPcp21_119*RLcp21_220+OPcp21_120*RLcp21_221+OPcp21_16*RLcp21_219-OPcp21_219*RLcp21_120-\
   OPcp21_220*RLcp21_121-OPcp21_26*RLcp21_119
    OMcp21_122 = OMcp21_121+ROcp21_421*qd[22]
    OMcp21_222 = OMcp21_221+ROcp21_521*qd[22]
    OMcp21_322 = OMcp21_321+ROcp21_621*qd[22]
    OPcp21_122 = OPcp21_120+ROcp21_16*qdd[21]+ROcp21_421*qdd[22]+qd[21]*(OMcp21_220*ROcp21_36-OMcp21_320*ROcp21_26)+qd[22]\
   *(OMcp21_221*ROcp21_621-OMcp21_321*ROcp21_521)
    OPcp21_222 = OPcp21_220+ROcp21_26*qdd[21]+ROcp21_521*qdd[22]-qd[21]*(OMcp21_120*ROcp21_36-OMcp21_320*ROcp21_16)-qd[22]\
   *(OMcp21_121*ROcp21_621-OMcp21_321*ROcp21_421)
    OPcp21_322 = OPcp21_320+ROcp21_36*qdd[21]+ROcp21_621*qdd[22]+qd[21]*(OMcp21_120*ROcp21_26-OMcp21_220*ROcp21_16)+qd[22]\
   *(OMcp21_121*ROcp21_521-OMcp21_221*ROcp21_421)

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



# ====== END Task 1 ====== 

  

