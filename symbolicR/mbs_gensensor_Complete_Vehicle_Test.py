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
#	==> Flops complexity : 3030
#
#	==> Generation Time :  0.050 seconds
#	==> Post-Processing :  0.060 seconds
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


    ROcp4_45 = -S4*C5
    ROcp4_55 = C4*C5
    ROcp4_75 = S4*S5
    ROcp4_85 = -C4*S5
    OMcp4_15 = qd[5]*C4
    OMcp4_25 = qd[5]*S4
    OPcp4_15 = qdd[5]*C4-qd[4]*qd[5]*S4
    OPcp4_25 = qdd[5]*S4+qd[4]*qd[5]*C4

# = = Block_1_0_0_5_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = C4
    sens.R[1,2] = S4
    sens.R[2,1] = ROcp4_45
    sens.R[2,2] = ROcp4_55
    sens.R[2,3] = S5
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

# = = Block_1_0_0_6_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = q[1]
    sens.P[2] = q[2]
    sens.P[3] = q[3]
    sens.R[1,1] = ROcp5_16
    sens.R[1,2] = ROcp5_26
    sens.R[1,3] = ROcp5_36
    sens.R[2,1] = ROcp5_45
    sens.R[2,2] = ROcp5_55
    sens.R[2,3] = S5
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

# = = Block_1_0_0_7_0_2 = = 
 
# Sensor Kinematics 


    ROcp6_47 = ROcp6_45*C7+ROcp6_76*S7
    ROcp6_57 = ROcp6_55*C7+ROcp6_86*S7
    ROcp6_67 = ROcp6_96*S7+S5*C7
    ROcp6_77 = -(ROcp6_45*S7-ROcp6_76*C7)
    ROcp6_87 = -(ROcp6_55*S7-ROcp6_86*C7)
    ROcp6_97 = ROcp6_96*C7-S5*S7
    RLcp6_17 = ROcp6_16*s.dpt[1,1]+ROcp6_45*s.dpt[2,1]+ROcp6_76*s.dpt[3,1]
    RLcp6_27 = ROcp6_26*s.dpt[1,1]+ROcp6_55*s.dpt[2,1]+ROcp6_86*s.dpt[3,1]
    RLcp6_37 = ROcp6_36*s.dpt[1,1]+ROcp6_96*s.dpt[3,1]+s.dpt[2,1]*S5
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

# = = Block_1_0_0_8_0_2 = = 
 
# Sensor Kinematics 


    ROcp7_47 = ROcp7_45*C7+ROcp7_76*S7
    ROcp7_57 = ROcp7_55*C7+ROcp7_86*S7
    ROcp7_67 = ROcp7_96*S7+S5*C7
    ROcp7_77 = -(ROcp7_45*S7-ROcp7_76*C7)
    ROcp7_87 = -(ROcp7_55*S7-ROcp7_86*C7)
    ROcp7_97 = ROcp7_96*C7-S5*S7
    ROcp7_18 = ROcp7_16*C8+ROcp7_47*S8
    ROcp7_28 = ROcp7_26*C8+ROcp7_57*S8
    ROcp7_38 = ROcp7_36*C8+ROcp7_67*S8
    ROcp7_48 = -(ROcp7_16*S8-ROcp7_47*C8)
    ROcp7_58 = -(ROcp7_26*S8-ROcp7_57*C8)
    ROcp7_68 = -(ROcp7_36*S8-ROcp7_67*C8)
    RLcp7_17 = ROcp7_16*s.dpt[1,1]+ROcp7_45*s.dpt[2,1]+ROcp7_76*s.dpt[3,1]
    RLcp7_27 = ROcp7_26*s.dpt[1,1]+ROcp7_55*s.dpt[2,1]+ROcp7_86*s.dpt[3,1]
    RLcp7_37 = ROcp7_36*s.dpt[1,1]+ROcp7_96*s.dpt[3,1]+s.dpt[2,1]*S5
    OMcp7_17 = OMcp7_16+ROcp7_16*qd[7]
    OMcp7_27 = OMcp7_26+ROcp7_26*qd[7]
    OMcp7_37 = OMcp7_36+ROcp7_36*qd[7]
    ORcp7_17 = OMcp7_26*RLcp7_37-OMcp7_36*RLcp7_27
    ORcp7_27 = -(OMcp7_16*RLcp7_37-OMcp7_36*RLcp7_17)
    ORcp7_37 = OMcp7_16*RLcp7_27-OMcp7_26*RLcp7_17
    OPcp7_17 = OPcp7_16+ROcp7_16*qdd[7]+qd[7]*(OMcp7_26*ROcp7_36-OMcp7_36*ROcp7_26)
    OPcp7_27 = OPcp7_26+ROcp7_26*qdd[7]-qd[7]*(OMcp7_16*ROcp7_36-OMcp7_36*ROcp7_16)
    OPcp7_37 = OPcp7_36+ROcp7_36*qdd[7]+qd[7]*(OMcp7_16*ROcp7_26-OMcp7_26*ROcp7_16)
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


    ROcp8_45 = -S4*C5
    ROcp8_55 = C4*C5
    ROcp8_75 = S4*S5
    ROcp8_85 = -C4*S5
    ROcp8_16 = -(ROcp8_75*S6-C4*C6)
    ROcp8_26 = -(ROcp8_85*S6-S4*C6)
    ROcp8_36 = -C5*S6
    ROcp8_76 = ROcp8_75*C6+C4*S6
    ROcp8_86 = ROcp8_85*C6+S4*S6
    ROcp8_96 = C5*C6
    OMcp8_15 = qd[5]*C4
    OMcp8_25 = qd[5]*S4
    OMcp8_16 = OMcp8_15+ROcp8_45*qd[6]
    OMcp8_26 = OMcp8_25+ROcp8_55*qd[6]
    OMcp8_36 = qd[4]+qd[6]*S5
    OPcp8_16 = ROcp8_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp8_25*S5-ROcp8_55*qd[4])
    OPcp8_26 = ROcp8_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp8_15*S5-ROcp8_45*qd[4])
    OPcp8_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_9_0_2 = = 
 
# Sensor Kinematics 


    ROcp8_47 = ROcp8_45*C7+ROcp8_76*S7
    ROcp8_57 = ROcp8_55*C7+ROcp8_86*S7
    ROcp8_67 = ROcp8_96*S7+S5*C7
    ROcp8_77 = -(ROcp8_45*S7-ROcp8_76*C7)
    ROcp8_87 = -(ROcp8_55*S7-ROcp8_86*C7)
    ROcp8_97 = ROcp8_96*C7-S5*S7
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
    RLcp8_17 = ROcp8_16*s.dpt[1,1]+ROcp8_45*s.dpt[2,1]+ROcp8_76*s.dpt[3,1]
    RLcp8_27 = ROcp8_26*s.dpt[1,1]+ROcp8_55*s.dpt[2,1]+ROcp8_86*s.dpt[3,1]
    RLcp8_37 = ROcp8_36*s.dpt[1,1]+ROcp8_96*s.dpt[3,1]+s.dpt[2,1]*S5
    OMcp8_17 = OMcp8_16+ROcp8_16*qd[7]
    OMcp8_27 = OMcp8_26+ROcp8_26*qd[7]
    OMcp8_37 = OMcp8_36+ROcp8_36*qd[7]
    ORcp8_17 = OMcp8_26*RLcp8_37-OMcp8_36*RLcp8_27
    ORcp8_27 = -(OMcp8_16*RLcp8_37-OMcp8_36*RLcp8_17)
    ORcp8_37 = OMcp8_16*RLcp8_27-OMcp8_26*RLcp8_17
    OPcp8_17 = OPcp8_16+ROcp8_16*qdd[7]+qd[7]*(OMcp8_26*ROcp8_36-OMcp8_36*ROcp8_26)
    OPcp8_27 = OPcp8_26+ROcp8_26*qdd[7]-qd[7]*(OMcp8_16*ROcp8_36-OMcp8_36*ROcp8_16)
    OPcp8_37 = OPcp8_36+ROcp8_36*qdd[7]+qd[7]*(OMcp8_16*ROcp8_26-OMcp8_26*ROcp8_16)
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


    ROcp9_45 = -S4*C5
    ROcp9_55 = C4*C5
    ROcp9_75 = S4*S5
    ROcp9_85 = -C4*S5
    ROcp9_16 = -(ROcp9_75*S6-C4*C6)
    ROcp9_26 = -(ROcp9_85*S6-S4*C6)
    ROcp9_36 = -C5*S6
    ROcp9_76 = ROcp9_75*C6+C4*S6
    ROcp9_86 = ROcp9_85*C6+S4*S6
    ROcp9_96 = C5*C6
    OMcp9_15 = qd[5]*C4
    OMcp9_25 = qd[5]*S4
    OMcp9_16 = OMcp9_15+ROcp9_45*qd[6]
    OMcp9_26 = OMcp9_25+ROcp9_55*qd[6]
    OMcp9_36 = qd[4]+qd[6]*S5
    OPcp9_16 = ROcp9_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp9_25*S5-ROcp9_55*qd[4])
    OPcp9_26 = ROcp9_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp9_15*S5-ROcp9_45*qd[4])
    OPcp9_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_10_0_3 = = 
 
# Sensor Kinematics 


    ROcp9_410 = ROcp9_45*C10+ROcp9_76*S10
    ROcp9_510 = ROcp9_55*C10+ROcp9_86*S10
    ROcp9_610 = ROcp9_96*S10+C10*S5
    ROcp9_710 = -(ROcp9_45*S10-ROcp9_76*C10)
    ROcp9_810 = -(ROcp9_55*S10-ROcp9_86*C10)
    ROcp9_910 = ROcp9_96*C10-S10*S5
    RLcp9_110 = ROcp9_16*s.dpt[1,4]+ROcp9_45*s.dpt[2,4]+ROcp9_76*s.dpt[3,4]
    RLcp9_210 = ROcp9_26*s.dpt[1,4]+ROcp9_55*s.dpt[2,4]+ROcp9_86*s.dpt[3,4]
    RLcp9_310 = ROcp9_36*s.dpt[1,4]+ROcp9_96*s.dpt[3,4]+s.dpt[2,4]*S5
    POcp9_110 = RLcp9_110+q[1]
    POcp9_210 = RLcp9_210+q[2]
    POcp9_310 = RLcp9_310+q[3]
    OMcp9_110 = OMcp9_16+ROcp9_16*qd[10]
    OMcp9_210 = OMcp9_26+ROcp9_26*qd[10]
    OMcp9_310 = OMcp9_36+ROcp9_36*qd[10]
    ORcp9_110 = OMcp9_26*RLcp9_310-OMcp9_36*RLcp9_210
    ORcp9_210 = -(OMcp9_16*RLcp9_310-OMcp9_36*RLcp9_110)
    ORcp9_310 = OMcp9_16*RLcp9_210-OMcp9_26*RLcp9_110
    VIcp9_110 = ORcp9_110+qd[1]
    VIcp9_210 = ORcp9_210+qd[2]
    VIcp9_310 = ORcp9_310+qd[3]
    OPcp9_110 = OPcp9_16+ROcp9_16*qdd[10]+qd[10]*(OMcp9_26*ROcp9_36-OMcp9_36*ROcp9_26)
    OPcp9_210 = OPcp9_26+ROcp9_26*qdd[10]-qd[10]*(OMcp9_16*ROcp9_36-OMcp9_36*ROcp9_16)
    OPcp9_310 = OPcp9_36+ROcp9_36*qdd[10]+qd[10]*(OMcp9_16*ROcp9_26-OMcp9_26*ROcp9_16)
    ACcp9_110 = qdd[1]+OMcp9_26*ORcp9_310-OMcp9_36*ORcp9_210+OPcp9_26*RLcp9_310-OPcp9_36*RLcp9_210
    ACcp9_210 = qdd[2]-OMcp9_16*ORcp9_310+OMcp9_36*ORcp9_110-OPcp9_16*RLcp9_310+OPcp9_36*RLcp9_110
    ACcp9_310 = qdd[3]+OMcp9_16*ORcp9_210-OMcp9_26*ORcp9_110+OPcp9_16*RLcp9_210-OPcp9_26*RLcp9_110

# = = Block_1_0_0_10_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp9_110
    sens.P[2] = POcp9_210
    sens.P[3] = POcp9_310
    sens.R[1,1] = ROcp9_16
    sens.R[1,2] = ROcp9_26
    sens.R[1,3] = ROcp9_36
    sens.R[2,1] = ROcp9_410
    sens.R[2,2] = ROcp9_510
    sens.R[2,3] = ROcp9_610
    sens.R[3,1] = ROcp9_710
    sens.R[3,2] = ROcp9_810
    sens.R[3,3] = ROcp9_910
    sens.V[1] = VIcp9_110
    sens.V[2] = VIcp9_210
    sens.V[3] = VIcp9_310
    sens.OM[1] = OMcp9_110
    sens.OM[2] = OMcp9_210
    sens.OM[3] = OMcp9_310
    sens.A[1] = ACcp9_110
    sens.A[2] = ACcp9_210
    sens.A[3] = ACcp9_310
    sens.OMP[1] = OPcp9_110
    sens.OMP[2] = OPcp9_210
    sens.OMP[3] = OPcp9_310
 
# 
  elif(isens==11): 


# = = Block_1_0_0_11_0_1 = = 
 
# Sensor Kinematics 


    ROcp10_45 = -S4*C5
    ROcp10_55 = C4*C5
    ROcp10_75 = S4*S5
    ROcp10_85 = -C4*S5
    ROcp10_16 = -(ROcp10_75*S6-C4*C6)
    ROcp10_26 = -(ROcp10_85*S6-S4*C6)
    ROcp10_36 = -C5*S6
    ROcp10_76 = ROcp10_75*C6+C4*S6
    ROcp10_86 = ROcp10_85*C6+S4*S6
    ROcp10_96 = C5*C6
    OMcp10_15 = qd[5]*C4
    OMcp10_25 = qd[5]*S4
    OMcp10_16 = OMcp10_15+ROcp10_45*qd[6]
    OMcp10_26 = OMcp10_25+ROcp10_55*qd[6]
    OMcp10_36 = qd[4]+qd[6]*S5
    OPcp10_16 = ROcp10_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp10_25*S5-ROcp10_55*qd[4])
    OPcp10_26 = ROcp10_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp10_15*S5-ROcp10_45*qd[4])
    OPcp10_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_11_0_3 = = 
 
# Sensor Kinematics 


    ROcp10_410 = ROcp10_45*C10+ROcp10_76*S10
    ROcp10_510 = ROcp10_55*C10+ROcp10_86*S10
    ROcp10_610 = ROcp10_96*S10+C10*S5
    ROcp10_710 = -(ROcp10_45*S10-ROcp10_76*C10)
    ROcp10_810 = -(ROcp10_55*S10-ROcp10_86*C10)
    ROcp10_910 = ROcp10_96*C10-S10*S5
    ROcp10_111 = ROcp10_16*C11+ROcp10_410*S11
    ROcp10_211 = ROcp10_26*C11+ROcp10_510*S11
    ROcp10_311 = ROcp10_36*C11+ROcp10_610*S11
    ROcp10_411 = -(ROcp10_16*S11-ROcp10_410*C11)
    ROcp10_511 = -(ROcp10_26*S11-ROcp10_510*C11)
    ROcp10_611 = -(ROcp10_36*S11-ROcp10_610*C11)
    RLcp10_110 = ROcp10_16*s.dpt[1,4]+ROcp10_45*s.dpt[2,4]+ROcp10_76*s.dpt[3,4]
    RLcp10_210 = ROcp10_26*s.dpt[1,4]+ROcp10_55*s.dpt[2,4]+ROcp10_86*s.dpt[3,4]
    RLcp10_310 = ROcp10_36*s.dpt[1,4]+ROcp10_96*s.dpt[3,4]+s.dpt[2,4]*S5
    OMcp10_110 = OMcp10_16+ROcp10_16*qd[10]
    OMcp10_210 = OMcp10_26+ROcp10_26*qd[10]
    OMcp10_310 = OMcp10_36+ROcp10_36*qd[10]
    ORcp10_110 = OMcp10_26*RLcp10_310-OMcp10_36*RLcp10_210
    ORcp10_210 = -(OMcp10_16*RLcp10_310-OMcp10_36*RLcp10_110)
    ORcp10_310 = OMcp10_16*RLcp10_210-OMcp10_26*RLcp10_110
    OPcp10_110 = OPcp10_16+ROcp10_16*qdd[10]+qd[10]*(OMcp10_26*ROcp10_36-OMcp10_36*ROcp10_26)
    OPcp10_210 = OPcp10_26+ROcp10_26*qdd[10]-qd[10]*(OMcp10_16*ROcp10_36-OMcp10_36*ROcp10_16)
    OPcp10_310 = OPcp10_36+ROcp10_36*qdd[10]+qd[10]*(OMcp10_16*ROcp10_26-OMcp10_26*ROcp10_16)
    RLcp10_111 = ROcp10_410*s.dpt[2,19]
    RLcp10_211 = ROcp10_510*s.dpt[2,19]
    RLcp10_311 = ROcp10_610*s.dpt[2,19]
    POcp10_111 = RLcp10_110+RLcp10_111+q[1]
    POcp10_211 = RLcp10_210+RLcp10_211+q[2]
    POcp10_311 = RLcp10_310+RLcp10_311+q[3]
    OMcp10_111 = OMcp10_110+ROcp10_710*qd[11]
    OMcp10_211 = OMcp10_210+ROcp10_810*qd[11]
    OMcp10_311 = OMcp10_310+ROcp10_910*qd[11]
    ORcp10_111 = OMcp10_210*RLcp10_311-OMcp10_310*RLcp10_211
    ORcp10_211 = -(OMcp10_110*RLcp10_311-OMcp10_310*RLcp10_111)
    ORcp10_311 = OMcp10_110*RLcp10_211-OMcp10_210*RLcp10_111
    VIcp10_111 = ORcp10_110+ORcp10_111+qd[1]
    VIcp10_211 = ORcp10_210+ORcp10_211+qd[2]
    VIcp10_311 = ORcp10_310+ORcp10_311+qd[3]
    OPcp10_111 = OPcp10_110+ROcp10_710*qdd[11]+qd[11]*(OMcp10_210*ROcp10_910-OMcp10_310*ROcp10_810)
    OPcp10_211 = OPcp10_210+ROcp10_810*qdd[11]-qd[11]*(OMcp10_110*ROcp10_910-OMcp10_310*ROcp10_710)
    OPcp10_311 = OPcp10_310+ROcp10_910*qdd[11]+qd[11]*(OMcp10_110*ROcp10_810-OMcp10_210*ROcp10_710)
    ACcp10_111 = qdd[1]+OMcp10_210*ORcp10_311+OMcp10_26*ORcp10_310-OMcp10_310*ORcp10_211-OMcp10_36*ORcp10_210+OPcp10_210*\
   RLcp10_311+OPcp10_26*RLcp10_310-OPcp10_310*RLcp10_211-OPcp10_36*RLcp10_210
    ACcp10_211 = qdd[2]-OMcp10_110*ORcp10_311-OMcp10_16*ORcp10_310+OMcp10_310*ORcp10_111+OMcp10_36*ORcp10_110-OPcp10_110*\
   RLcp10_311-OPcp10_16*RLcp10_310+OPcp10_310*RLcp10_111+OPcp10_36*RLcp10_110
    ACcp10_311 = qdd[3]+OMcp10_110*ORcp10_211+OMcp10_16*ORcp10_210-OMcp10_210*ORcp10_111-OMcp10_26*ORcp10_110+OPcp10_110*\
   RLcp10_211+OPcp10_16*RLcp10_210-OPcp10_210*RLcp10_111-OPcp10_26*RLcp10_110

# = = Block_1_0_0_11_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp10_111
    sens.P[2] = POcp10_211
    sens.P[3] = POcp10_311
    sens.R[1,1] = ROcp10_111
    sens.R[1,2] = ROcp10_211
    sens.R[1,3] = ROcp10_311
    sens.R[2,1] = ROcp10_411
    sens.R[2,2] = ROcp10_511
    sens.R[2,3] = ROcp10_611
    sens.R[3,1] = ROcp10_710
    sens.R[3,2] = ROcp10_810
    sens.R[3,3] = ROcp10_910
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


    ROcp11_45 = -S4*C5
    ROcp11_55 = C4*C5
    ROcp11_75 = S4*S5
    ROcp11_85 = -C4*S5
    ROcp11_16 = -(ROcp11_75*S6-C4*C6)
    ROcp11_26 = -(ROcp11_85*S6-S4*C6)
    ROcp11_36 = -C5*S6
    ROcp11_76 = ROcp11_75*C6+C4*S6
    ROcp11_86 = ROcp11_85*C6+S4*S6
    ROcp11_96 = C5*C6
    OMcp11_15 = qd[5]*C4
    OMcp11_25 = qd[5]*S4
    OMcp11_16 = OMcp11_15+ROcp11_45*qd[6]
    OMcp11_26 = OMcp11_25+ROcp11_55*qd[6]
    OMcp11_36 = qd[4]+qd[6]*S5
    OPcp11_16 = ROcp11_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp11_25*S5-ROcp11_55*qd[4])
    OPcp11_26 = ROcp11_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp11_15*S5-ROcp11_45*qd[4])
    OPcp11_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_12_0_3 = = 
 
# Sensor Kinematics 


    ROcp11_410 = ROcp11_45*C10+ROcp11_76*S10
    ROcp11_510 = ROcp11_55*C10+ROcp11_86*S10
    ROcp11_610 = ROcp11_96*S10+C10*S5
    ROcp11_710 = -(ROcp11_45*S10-ROcp11_76*C10)
    ROcp11_810 = -(ROcp11_55*S10-ROcp11_86*C10)
    ROcp11_910 = ROcp11_96*C10-S10*S5
    ROcp11_111 = ROcp11_16*C11+ROcp11_410*S11
    ROcp11_211 = ROcp11_26*C11+ROcp11_510*S11
    ROcp11_311 = ROcp11_36*C11+ROcp11_610*S11
    ROcp11_411 = -(ROcp11_16*S11-ROcp11_410*C11)
    ROcp11_511 = -(ROcp11_26*S11-ROcp11_510*C11)
    ROcp11_611 = -(ROcp11_36*S11-ROcp11_610*C11)
    ROcp11_412 = ROcp11_411*C12+ROcp11_710*S12
    ROcp11_512 = ROcp11_511*C12+ROcp11_810*S12
    ROcp11_612 = ROcp11_611*C12+ROcp11_910*S12
    ROcp11_712 = -(ROcp11_411*S12-ROcp11_710*C12)
    ROcp11_812 = -(ROcp11_511*S12-ROcp11_810*C12)
    ROcp11_912 = -(ROcp11_611*S12-ROcp11_910*C12)
    RLcp11_110 = ROcp11_16*s.dpt[1,4]+ROcp11_45*s.dpt[2,4]+ROcp11_76*s.dpt[3,4]
    RLcp11_210 = ROcp11_26*s.dpt[1,4]+ROcp11_55*s.dpt[2,4]+ROcp11_86*s.dpt[3,4]
    RLcp11_310 = ROcp11_36*s.dpt[1,4]+ROcp11_96*s.dpt[3,4]+s.dpt[2,4]*S5
    OMcp11_110 = OMcp11_16+ROcp11_16*qd[10]
    OMcp11_210 = OMcp11_26+ROcp11_26*qd[10]
    OMcp11_310 = OMcp11_36+ROcp11_36*qd[10]
    ORcp11_110 = OMcp11_26*RLcp11_310-OMcp11_36*RLcp11_210
    ORcp11_210 = -(OMcp11_16*RLcp11_310-OMcp11_36*RLcp11_110)
    ORcp11_310 = OMcp11_16*RLcp11_210-OMcp11_26*RLcp11_110
    OPcp11_110 = OPcp11_16+ROcp11_16*qdd[10]+qd[10]*(OMcp11_26*ROcp11_36-OMcp11_36*ROcp11_26)
    OPcp11_210 = OPcp11_26+ROcp11_26*qdd[10]-qd[10]*(OMcp11_16*ROcp11_36-OMcp11_36*ROcp11_16)
    OPcp11_310 = OPcp11_36+ROcp11_36*qdd[10]+qd[10]*(OMcp11_16*ROcp11_26-OMcp11_26*ROcp11_16)
    RLcp11_111 = ROcp11_410*s.dpt[2,19]
    RLcp11_211 = ROcp11_510*s.dpt[2,19]
    RLcp11_311 = ROcp11_610*s.dpt[2,19]
    POcp11_111 = RLcp11_110+RLcp11_111+q[1]
    POcp11_211 = RLcp11_210+RLcp11_211+q[2]
    POcp11_311 = RLcp11_310+RLcp11_311+q[3]
    OMcp11_111 = OMcp11_110+ROcp11_710*qd[11]
    OMcp11_211 = OMcp11_210+ROcp11_810*qd[11]
    OMcp11_311 = OMcp11_310+ROcp11_910*qd[11]
    ORcp11_111 = OMcp11_210*RLcp11_311-OMcp11_310*RLcp11_211
    ORcp11_211 = -(OMcp11_110*RLcp11_311-OMcp11_310*RLcp11_111)
    ORcp11_311 = OMcp11_110*RLcp11_211-OMcp11_210*RLcp11_111
    VIcp11_111 = ORcp11_110+ORcp11_111+qd[1]
    VIcp11_211 = ORcp11_210+ORcp11_211+qd[2]
    VIcp11_311 = ORcp11_310+ORcp11_311+qd[3]
    ACcp11_111 = qdd[1]+OMcp11_210*ORcp11_311+OMcp11_26*ORcp11_310-OMcp11_310*ORcp11_211-OMcp11_36*ORcp11_210+OPcp11_210*\
   RLcp11_311+OPcp11_26*RLcp11_310-OPcp11_310*RLcp11_211-OPcp11_36*RLcp11_210
    ACcp11_211 = qdd[2]-OMcp11_110*ORcp11_311-OMcp11_16*ORcp11_310+OMcp11_310*ORcp11_111+OMcp11_36*ORcp11_110-OPcp11_110*\
   RLcp11_311-OPcp11_16*RLcp11_310+OPcp11_310*RLcp11_111+OPcp11_36*RLcp11_110
    ACcp11_311 = qdd[3]+OMcp11_110*ORcp11_211+OMcp11_16*ORcp11_210-OMcp11_210*ORcp11_111-OMcp11_26*ORcp11_110+OPcp11_110*\
   RLcp11_211+OPcp11_16*RLcp11_210-OPcp11_210*RLcp11_111-OPcp11_26*RLcp11_110
    OMcp11_112 = OMcp11_111+ROcp11_111*qd[12]
    OMcp11_212 = OMcp11_211+ROcp11_211*qd[12]
    OMcp11_312 = OMcp11_311+ROcp11_311*qd[12]
    OPcp11_112 = OPcp11_110+ROcp11_111*qdd[12]+ROcp11_710*qdd[11]+qd[11]*(OMcp11_210*ROcp11_910-OMcp11_310*ROcp11_810)+\
   qd[12]*(OMcp11_211*ROcp11_311-OMcp11_311*ROcp11_211)
    OPcp11_212 = OPcp11_210+ROcp11_211*qdd[12]+ROcp11_810*qdd[11]-qd[11]*(OMcp11_110*ROcp11_910-OMcp11_310*ROcp11_710)-\
   qd[12]*(OMcp11_111*ROcp11_311-OMcp11_311*ROcp11_111)
    OPcp11_312 = OPcp11_310+ROcp11_311*qdd[12]+ROcp11_910*qdd[11]+qd[11]*(OMcp11_110*ROcp11_810-OMcp11_210*ROcp11_710)+\
   qd[12]*(OMcp11_111*ROcp11_211-OMcp11_211*ROcp11_111)

# = = Block_1_0_0_12_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp11_111
    sens.P[2] = POcp11_211
    sens.P[3] = POcp11_311
    sens.R[1,1] = ROcp11_111
    sens.R[1,2] = ROcp11_211
    sens.R[1,3] = ROcp11_311
    sens.R[2,1] = ROcp11_412
    sens.R[2,2] = ROcp11_512
    sens.R[2,3] = ROcp11_612
    sens.R[3,1] = ROcp11_712
    sens.R[3,2] = ROcp11_812
    sens.R[3,3] = ROcp11_912
    sens.V[1] = VIcp11_111
    sens.V[2] = VIcp11_211
    sens.V[3] = VIcp11_311
    sens.OM[1] = OMcp11_112
    sens.OM[2] = OMcp11_212
    sens.OM[3] = OMcp11_312
    sens.A[1] = ACcp11_111
    sens.A[2] = ACcp11_211
    sens.A[3] = ACcp11_311
    sens.OMP[1] = OPcp11_112
    sens.OMP[2] = OPcp11_212
    sens.OMP[3] = OPcp11_312
 
# 
  elif(isens==13): 


# = = Block_1_0_0_13_0_1 = = 
 
# Sensor Kinematics 


    ROcp12_45 = -S4*C5
    ROcp12_55 = C4*C5
    ROcp12_75 = S4*S5
    ROcp12_85 = -C4*S5
    ROcp12_16 = -(ROcp12_75*S6-C4*C6)
    ROcp12_26 = -(ROcp12_85*S6-S4*C6)
    ROcp12_36 = -C5*S6
    ROcp12_76 = ROcp12_75*C6+C4*S6
    ROcp12_86 = ROcp12_85*C6+S4*S6
    ROcp12_96 = C5*C6
    OMcp12_15 = qd[5]*C4
    OMcp12_25 = qd[5]*S4
    OMcp12_16 = OMcp12_15+ROcp12_45*qd[6]
    OMcp12_26 = OMcp12_25+ROcp12_55*qd[6]
    OMcp12_36 = qd[4]+qd[6]*S5
    OPcp12_16 = ROcp12_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp12_25*S5-ROcp12_55*qd[4])
    OPcp12_26 = ROcp12_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp12_15*S5-ROcp12_45*qd[4])
    OPcp12_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_13_0_4 = = 
 
# Sensor Kinematics 


    ROcp12_413 = ROcp12_45*C13+ROcp12_76*S13
    ROcp12_513 = ROcp12_55*C13+ROcp12_86*S13
    ROcp12_613 = ROcp12_96*S13+C13*S5
    ROcp12_713 = -(ROcp12_45*S13-ROcp12_76*C13)
    ROcp12_813 = -(ROcp12_55*S13-ROcp12_86*C13)
    ROcp12_913 = ROcp12_96*C13-S13*S5
    RLcp12_113 = ROcp12_16*s.dpt[1,9]+ROcp12_45*s.dpt[2,9]+ROcp12_76*s.dpt[3,9]
    RLcp12_213 = ROcp12_26*s.dpt[1,9]+ROcp12_55*s.dpt[2,9]+ROcp12_86*s.dpt[3,9]
    RLcp12_313 = ROcp12_36*s.dpt[1,9]+ROcp12_96*s.dpt[3,9]+s.dpt[2,9]*S5
    POcp12_113 = RLcp12_113+q[1]
    POcp12_213 = RLcp12_213+q[2]
    POcp12_313 = RLcp12_313+q[3]
    OMcp12_113 = OMcp12_16+ROcp12_16*qd[13]
    OMcp12_213 = OMcp12_26+ROcp12_26*qd[13]
    OMcp12_313 = OMcp12_36+ROcp12_36*qd[13]
    ORcp12_113 = OMcp12_26*RLcp12_313-OMcp12_36*RLcp12_213
    ORcp12_213 = -(OMcp12_16*RLcp12_313-OMcp12_36*RLcp12_113)
    ORcp12_313 = OMcp12_16*RLcp12_213-OMcp12_26*RLcp12_113
    VIcp12_113 = ORcp12_113+qd[1]
    VIcp12_213 = ORcp12_213+qd[2]
    VIcp12_313 = ORcp12_313+qd[3]
    OPcp12_113 = OPcp12_16+ROcp12_16*qdd[13]+qd[13]*(OMcp12_26*ROcp12_36-OMcp12_36*ROcp12_26)
    OPcp12_213 = OPcp12_26+ROcp12_26*qdd[13]-qd[13]*(OMcp12_16*ROcp12_36-OMcp12_36*ROcp12_16)
    OPcp12_313 = OPcp12_36+ROcp12_36*qdd[13]+qd[13]*(OMcp12_16*ROcp12_26-OMcp12_26*ROcp12_16)
    ACcp12_113 = qdd[1]+OMcp12_26*ORcp12_313-OMcp12_36*ORcp12_213+OPcp12_26*RLcp12_313-OPcp12_36*RLcp12_213
    ACcp12_213 = qdd[2]-OMcp12_16*ORcp12_313+OMcp12_36*ORcp12_113-OPcp12_16*RLcp12_313+OPcp12_36*RLcp12_113
    ACcp12_313 = qdd[3]+OMcp12_16*ORcp12_213-OMcp12_26*ORcp12_113+OPcp12_16*RLcp12_213-OPcp12_26*RLcp12_113

# = = Block_1_0_0_13_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp12_113
    sens.P[2] = POcp12_213
    sens.P[3] = POcp12_313
    sens.R[1,1] = ROcp12_16
    sens.R[1,2] = ROcp12_26
    sens.R[1,3] = ROcp12_36
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


    ROcp13_45 = -S4*C5
    ROcp13_55 = C4*C5
    ROcp13_75 = S4*S5
    ROcp13_85 = -C4*S5
    ROcp13_16 = -(ROcp13_75*S6-C4*C6)
    ROcp13_26 = -(ROcp13_85*S6-S4*C6)
    ROcp13_36 = -C5*S6
    ROcp13_76 = ROcp13_75*C6+C4*S6
    ROcp13_86 = ROcp13_85*C6+S4*S6
    ROcp13_96 = C5*C6
    OMcp13_15 = qd[5]*C4
    OMcp13_25 = qd[5]*S4
    OMcp13_16 = OMcp13_15+ROcp13_45*qd[6]
    OMcp13_26 = OMcp13_25+ROcp13_55*qd[6]
    OMcp13_36 = qd[4]+qd[6]*S5
    OPcp13_16 = ROcp13_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp13_25*S5-ROcp13_55*qd[4])
    OPcp13_26 = ROcp13_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp13_15*S5-ROcp13_45*qd[4])
    OPcp13_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_14_0_4 = = 
 
# Sensor Kinematics 


    ROcp13_413 = ROcp13_45*C13+ROcp13_76*S13
    ROcp13_513 = ROcp13_55*C13+ROcp13_86*S13
    ROcp13_613 = ROcp13_96*S13+C13*S5
    ROcp13_713 = -(ROcp13_45*S13-ROcp13_76*C13)
    ROcp13_813 = -(ROcp13_55*S13-ROcp13_86*C13)
    ROcp13_913 = ROcp13_96*C13-S13*S5
    ROcp13_414 = ROcp13_413*C14+ROcp13_713*S14
    ROcp13_514 = ROcp13_513*C14+ROcp13_813*S14
    ROcp13_614 = ROcp13_613*C14+ROcp13_913*S14
    ROcp13_714 = -(ROcp13_413*S14-ROcp13_713*C14)
    ROcp13_814 = -(ROcp13_513*S14-ROcp13_813*C14)
    ROcp13_914 = -(ROcp13_613*S14-ROcp13_913*C14)
    RLcp13_113 = ROcp13_16*s.dpt[1,9]+ROcp13_45*s.dpt[2,9]+ROcp13_76*s.dpt[3,9]
    RLcp13_213 = ROcp13_26*s.dpt[1,9]+ROcp13_55*s.dpt[2,9]+ROcp13_86*s.dpt[3,9]
    RLcp13_313 = ROcp13_36*s.dpt[1,9]+ROcp13_96*s.dpt[3,9]+s.dpt[2,9]*S5
    OMcp13_113 = OMcp13_16+ROcp13_16*qd[13]
    OMcp13_213 = OMcp13_26+ROcp13_26*qd[13]
    OMcp13_313 = OMcp13_36+ROcp13_36*qd[13]
    ORcp13_113 = OMcp13_26*RLcp13_313-OMcp13_36*RLcp13_213
    ORcp13_213 = -(OMcp13_16*RLcp13_313-OMcp13_36*RLcp13_113)
    ORcp13_313 = OMcp13_16*RLcp13_213-OMcp13_26*RLcp13_113
    OPcp13_113 = OPcp13_16+ROcp13_16*qdd[13]+qd[13]*(OMcp13_26*ROcp13_36-OMcp13_36*ROcp13_26)
    OPcp13_213 = OPcp13_26+ROcp13_26*qdd[13]-qd[13]*(OMcp13_16*ROcp13_36-OMcp13_36*ROcp13_16)
    OPcp13_313 = OPcp13_36+ROcp13_36*qdd[13]+qd[13]*(OMcp13_16*ROcp13_26-OMcp13_26*ROcp13_16)
    RLcp13_114 = ROcp13_413*s.dpt[2,24]
    RLcp13_214 = ROcp13_513*s.dpt[2,24]
    RLcp13_314 = ROcp13_613*s.dpt[2,24]
    POcp13_114 = RLcp13_113+RLcp13_114+q[1]
    POcp13_214 = RLcp13_213+RLcp13_214+q[2]
    POcp13_314 = RLcp13_313+RLcp13_314+q[3]
    OMcp13_114 = OMcp13_113+ROcp13_16*qd[14]
    OMcp13_214 = OMcp13_213+ROcp13_26*qd[14]
    OMcp13_314 = OMcp13_313+ROcp13_36*qd[14]
    ORcp13_114 = OMcp13_213*RLcp13_314-OMcp13_313*RLcp13_214
    ORcp13_214 = -(OMcp13_113*RLcp13_314-OMcp13_313*RLcp13_114)
    ORcp13_314 = OMcp13_113*RLcp13_214-OMcp13_213*RLcp13_114
    VIcp13_114 = ORcp13_113+ORcp13_114+qd[1]
    VIcp13_214 = ORcp13_213+ORcp13_214+qd[2]
    VIcp13_314 = ORcp13_313+ORcp13_314+qd[3]
    OPcp13_114 = OPcp13_113+ROcp13_16*qdd[14]+qd[14]*(OMcp13_213*ROcp13_36-OMcp13_313*ROcp13_26)
    OPcp13_214 = OPcp13_213+ROcp13_26*qdd[14]-qd[14]*(OMcp13_113*ROcp13_36-OMcp13_313*ROcp13_16)
    OPcp13_314 = OPcp13_313+ROcp13_36*qdd[14]+qd[14]*(OMcp13_113*ROcp13_26-OMcp13_213*ROcp13_16)
    ACcp13_114 = qdd[1]+OMcp13_213*ORcp13_314+OMcp13_26*ORcp13_313-OMcp13_313*ORcp13_214-OMcp13_36*ORcp13_213+OPcp13_213*\
   RLcp13_314+OPcp13_26*RLcp13_313-OPcp13_313*RLcp13_214-OPcp13_36*RLcp13_213
    ACcp13_214 = qdd[2]-OMcp13_113*ORcp13_314-OMcp13_16*ORcp13_313+OMcp13_313*ORcp13_114+OMcp13_36*ORcp13_113-OPcp13_113*\
   RLcp13_314-OPcp13_16*RLcp13_313+OPcp13_313*RLcp13_114+OPcp13_36*RLcp13_113
    ACcp13_314 = qdd[3]+OMcp13_113*ORcp13_214+OMcp13_16*ORcp13_213-OMcp13_213*ORcp13_114-OMcp13_26*ORcp13_113+OPcp13_113*\
   RLcp13_214+OPcp13_16*RLcp13_213-OPcp13_213*RLcp13_114-OPcp13_26*RLcp13_113

# = = Block_1_0_0_14_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp13_114
    sens.P[2] = POcp13_214
    sens.P[3] = POcp13_314
    sens.R[1,1] = ROcp13_16
    sens.R[1,2] = ROcp13_26
    sens.R[1,3] = ROcp13_36
    sens.R[2,1] = ROcp13_414
    sens.R[2,2] = ROcp13_514
    sens.R[2,3] = ROcp13_614
    sens.R[3,1] = ROcp13_714
    sens.R[3,2] = ROcp13_814
    sens.R[3,3] = ROcp13_914
    sens.V[1] = VIcp13_114
    sens.V[2] = VIcp13_214
    sens.V[3] = VIcp13_314
    sens.OM[1] = OMcp13_114
    sens.OM[2] = OMcp13_214
    sens.OM[3] = OMcp13_314
    sens.A[1] = ACcp13_114
    sens.A[2] = ACcp13_214
    sens.A[3] = ACcp13_314
    sens.OMP[1] = OPcp13_114
    sens.OMP[2] = OPcp13_214
    sens.OMP[3] = OPcp13_314
 
# 
  elif(isens==15): 


# = = Block_1_0_0_15_0_1 = = 
 
# Sensor Kinematics 


    ROcp14_45 = -S4*C5
    ROcp14_55 = C4*C5
    ROcp14_75 = S4*S5
    ROcp14_85 = -C4*S5
    ROcp14_16 = -(ROcp14_75*S6-C4*C6)
    ROcp14_26 = -(ROcp14_85*S6-S4*C6)
    ROcp14_36 = -C5*S6
    ROcp14_76 = ROcp14_75*C6+C4*S6
    ROcp14_86 = ROcp14_85*C6+S4*S6
    ROcp14_96 = C5*C6
    OMcp14_15 = qd[5]*C4
    OMcp14_25 = qd[5]*S4
    OMcp14_16 = OMcp14_15+ROcp14_45*qd[6]
    OMcp14_26 = OMcp14_25+ROcp14_55*qd[6]
    OMcp14_36 = qd[4]+qd[6]*S5
    OPcp14_16 = ROcp14_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp14_25*S5-ROcp14_55*qd[4])
    OPcp14_26 = ROcp14_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp14_15*S5-ROcp14_45*qd[4])
    OPcp14_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_15_0_4 = = 
 
# Sensor Kinematics 


    ROcp14_413 = ROcp14_45*C13+ROcp14_76*S13
    ROcp14_513 = ROcp14_55*C13+ROcp14_86*S13
    ROcp14_613 = ROcp14_96*S13+C13*S5
    ROcp14_713 = -(ROcp14_45*S13-ROcp14_76*C13)
    ROcp14_813 = -(ROcp14_55*S13-ROcp14_86*C13)
    ROcp14_913 = ROcp14_96*C13-S13*S5
    ROcp14_414 = ROcp14_413*C14+ROcp14_713*S14
    ROcp14_514 = ROcp14_513*C14+ROcp14_813*S14
    ROcp14_614 = ROcp14_613*C14+ROcp14_913*S14
    ROcp14_714 = -(ROcp14_413*S14-ROcp14_713*C14)
    ROcp14_814 = -(ROcp14_513*S14-ROcp14_813*C14)
    ROcp14_914 = -(ROcp14_613*S14-ROcp14_913*C14)
    ROcp14_415 = ROcp14_414*C15+ROcp14_714*S15
    ROcp14_515 = ROcp14_514*C15+ROcp14_814*S15
    ROcp14_615 = ROcp14_614*C15+ROcp14_914*S15
    ROcp14_715 = -(ROcp14_414*S15-ROcp14_714*C15)
    ROcp14_815 = -(ROcp14_514*S15-ROcp14_814*C15)
    ROcp14_915 = -(ROcp14_614*S15-ROcp14_914*C15)
    RLcp14_113 = ROcp14_16*s.dpt[1,9]+ROcp14_45*s.dpt[2,9]+ROcp14_76*s.dpt[3,9]
    RLcp14_213 = ROcp14_26*s.dpt[1,9]+ROcp14_55*s.dpt[2,9]+ROcp14_86*s.dpt[3,9]
    RLcp14_313 = ROcp14_36*s.dpt[1,9]+ROcp14_96*s.dpt[3,9]+s.dpt[2,9]*S5
    OMcp14_113 = OMcp14_16+ROcp14_16*qd[13]
    OMcp14_213 = OMcp14_26+ROcp14_26*qd[13]
    OMcp14_313 = OMcp14_36+ROcp14_36*qd[13]
    ORcp14_113 = OMcp14_26*RLcp14_313-OMcp14_36*RLcp14_213
    ORcp14_213 = -(OMcp14_16*RLcp14_313-OMcp14_36*RLcp14_113)
    ORcp14_313 = OMcp14_16*RLcp14_213-OMcp14_26*RLcp14_113
    OPcp14_113 = OPcp14_16+ROcp14_16*qdd[13]+qd[13]*(OMcp14_26*ROcp14_36-OMcp14_36*ROcp14_26)
    OPcp14_213 = OPcp14_26+ROcp14_26*qdd[13]-qd[13]*(OMcp14_16*ROcp14_36-OMcp14_36*ROcp14_16)
    OPcp14_313 = OPcp14_36+ROcp14_36*qdd[13]+qd[13]*(OMcp14_16*ROcp14_26-OMcp14_26*ROcp14_16)
    RLcp14_114 = ROcp14_413*s.dpt[2,24]
    RLcp14_214 = ROcp14_513*s.dpt[2,24]
    RLcp14_314 = ROcp14_613*s.dpt[2,24]
    OMcp14_114 = OMcp14_113+ROcp14_16*qd[14]
    OMcp14_214 = OMcp14_213+ROcp14_26*qd[14]
    OMcp14_314 = OMcp14_313+ROcp14_36*qd[14]
    ORcp14_114 = OMcp14_213*RLcp14_314-OMcp14_313*RLcp14_214
    ORcp14_214 = -(OMcp14_113*RLcp14_314-OMcp14_313*RLcp14_114)
    ORcp14_314 = OMcp14_113*RLcp14_214-OMcp14_213*RLcp14_114
    OPcp14_114 = OPcp14_113+ROcp14_16*qdd[14]+qd[14]*(OMcp14_213*ROcp14_36-OMcp14_313*ROcp14_26)
    OPcp14_214 = OPcp14_213+ROcp14_26*qdd[14]-qd[14]*(OMcp14_113*ROcp14_36-OMcp14_313*ROcp14_16)
    OPcp14_314 = OPcp14_313+ROcp14_36*qdd[14]+qd[14]*(OMcp14_113*ROcp14_26-OMcp14_213*ROcp14_16)
    RLcp14_115 = ROcp14_16*s.dpt[1,26]
    RLcp14_215 = ROcp14_26*s.dpt[1,26]
    RLcp14_315 = ROcp14_36*s.dpt[1,26]
    POcp14_115 = RLcp14_113+RLcp14_114+RLcp14_115+q[1]
    POcp14_215 = RLcp14_213+RLcp14_214+RLcp14_215+q[2]
    POcp14_315 = RLcp14_313+RLcp14_314+RLcp14_315+q[3]
    OMcp14_115 = OMcp14_114+ROcp14_16*qd[15]
    OMcp14_215 = OMcp14_214+ROcp14_26*qd[15]
    OMcp14_315 = OMcp14_314+ROcp14_36*qd[15]
    ORcp14_115 = OMcp14_214*RLcp14_315-OMcp14_314*RLcp14_215
    ORcp14_215 = -(OMcp14_114*RLcp14_315-OMcp14_314*RLcp14_115)
    ORcp14_315 = OMcp14_114*RLcp14_215-OMcp14_214*RLcp14_115
    VIcp14_115 = ORcp14_113+ORcp14_114+ORcp14_115+qd[1]
    VIcp14_215 = ORcp14_213+ORcp14_214+ORcp14_215+qd[2]
    VIcp14_315 = ORcp14_313+ORcp14_314+ORcp14_315+qd[3]
    OPcp14_115 = OPcp14_114+ROcp14_16*qdd[15]+qd[15]*(OMcp14_214*ROcp14_36-OMcp14_314*ROcp14_26)
    OPcp14_215 = OPcp14_214+ROcp14_26*qdd[15]-qd[15]*(OMcp14_114*ROcp14_36-OMcp14_314*ROcp14_16)
    OPcp14_315 = OPcp14_314+ROcp14_36*qdd[15]+qd[15]*(OMcp14_114*ROcp14_26-OMcp14_214*ROcp14_16)
    ACcp14_115 = qdd[1]+OMcp14_213*ORcp14_314+OMcp14_214*ORcp14_315+OMcp14_26*ORcp14_313-OMcp14_313*ORcp14_214-OMcp14_314*\
   ORcp14_215-OMcp14_36*ORcp14_213+OPcp14_213*RLcp14_314+OPcp14_214*RLcp14_315+OPcp14_26*RLcp14_313-OPcp14_313*RLcp14_214-\
   OPcp14_314*RLcp14_215-OPcp14_36*RLcp14_213
    ACcp14_215 = qdd[2]-OMcp14_113*ORcp14_314-OMcp14_114*ORcp14_315-OMcp14_16*ORcp14_313+OMcp14_313*ORcp14_114+OMcp14_314*\
   ORcp14_115+OMcp14_36*ORcp14_113-OPcp14_113*RLcp14_314-OPcp14_114*RLcp14_315-OPcp14_16*RLcp14_313+OPcp14_313*RLcp14_114+\
   OPcp14_314*RLcp14_115+OPcp14_36*RLcp14_113
    ACcp14_315 = qdd[3]+OMcp14_113*ORcp14_214+OMcp14_114*ORcp14_215+OMcp14_16*ORcp14_213-OMcp14_213*ORcp14_114-OMcp14_214*\
   ORcp14_115-OMcp14_26*ORcp14_113+OPcp14_113*RLcp14_214+OPcp14_114*RLcp14_215+OPcp14_16*RLcp14_213-OPcp14_213*RLcp14_114-\
   OPcp14_214*RLcp14_115-OPcp14_26*RLcp14_113

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


    ROcp15_45 = -S4*C5
    ROcp15_55 = C4*C5
    ROcp15_75 = S4*S5
    ROcp15_85 = -C4*S5
    ROcp15_16 = -(ROcp15_75*S6-C4*C6)
    ROcp15_26 = -(ROcp15_85*S6-S4*C6)
    ROcp15_36 = -C5*S6
    ROcp15_76 = ROcp15_75*C6+C4*S6
    ROcp15_86 = ROcp15_85*C6+S4*S6
    ROcp15_96 = C5*C6
    OMcp15_15 = qd[5]*C4
    OMcp15_25 = qd[5]*S4
    OMcp15_16 = OMcp15_15+ROcp15_45*qd[6]
    OMcp15_26 = OMcp15_25+ROcp15_55*qd[6]
    OMcp15_36 = qd[4]+qd[6]*S5
    OPcp15_16 = ROcp15_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp15_25*S5-ROcp15_55*qd[4])
    OPcp15_26 = ROcp15_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp15_15*S5-ROcp15_45*qd[4])
    OPcp15_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_16_0_5 = = 
 
# Sensor Kinematics 


    ROcp15_416 = ROcp15_45*C16+ROcp15_76*S16
    ROcp15_516 = ROcp15_55*C16+ROcp15_86*S16
    ROcp15_616 = ROcp15_96*S16+C16*S5
    ROcp15_716 = -(ROcp15_45*S16-ROcp15_76*C16)
    ROcp15_816 = -(ROcp15_55*S16-ROcp15_86*C16)
    ROcp15_916 = ROcp15_96*C16-S16*S5
    RLcp15_116 = ROcp15_16*s.dpt[1,11]+ROcp15_45*s.dpt[2,11]+ROcp15_76*s.dpt[3,11]
    RLcp15_216 = ROcp15_26*s.dpt[1,11]+ROcp15_55*s.dpt[2,11]+ROcp15_86*s.dpt[3,11]
    RLcp15_316 = ROcp15_36*s.dpt[1,11]+ROcp15_96*s.dpt[3,11]+s.dpt[2,11]*S5
    POcp15_116 = RLcp15_116+q[1]
    POcp15_216 = RLcp15_216+q[2]
    POcp15_316 = RLcp15_316+q[3]
    OMcp15_116 = OMcp15_16+ROcp15_16*qd[16]
    OMcp15_216 = OMcp15_26+ROcp15_26*qd[16]
    OMcp15_316 = OMcp15_36+ROcp15_36*qd[16]
    ORcp15_116 = OMcp15_26*RLcp15_316-OMcp15_36*RLcp15_216
    ORcp15_216 = -(OMcp15_16*RLcp15_316-OMcp15_36*RLcp15_116)
    ORcp15_316 = OMcp15_16*RLcp15_216-OMcp15_26*RLcp15_116
    VIcp15_116 = ORcp15_116+qd[1]
    VIcp15_216 = ORcp15_216+qd[2]
    VIcp15_316 = ORcp15_316+qd[3]
    OPcp15_116 = OPcp15_16+ROcp15_16*qdd[16]+qd[16]*(OMcp15_26*ROcp15_36-OMcp15_36*ROcp15_26)
    OPcp15_216 = OPcp15_26+ROcp15_26*qdd[16]-qd[16]*(OMcp15_16*ROcp15_36-OMcp15_36*ROcp15_16)
    OPcp15_316 = OPcp15_36+ROcp15_36*qdd[16]+qd[16]*(OMcp15_16*ROcp15_26-OMcp15_26*ROcp15_16)
    ACcp15_116 = qdd[1]+OMcp15_26*ORcp15_316-OMcp15_36*ORcp15_216+OPcp15_26*RLcp15_316-OPcp15_36*RLcp15_216
    ACcp15_216 = qdd[2]-OMcp15_16*ORcp15_316+OMcp15_36*ORcp15_116-OPcp15_16*RLcp15_316+OPcp15_36*RLcp15_116
    ACcp15_316 = qdd[3]+OMcp15_16*ORcp15_216-OMcp15_26*ORcp15_116+OPcp15_16*RLcp15_216-OPcp15_26*RLcp15_116

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


    ROcp16_45 = -S4*C5
    ROcp16_55 = C4*C5
    ROcp16_75 = S4*S5
    ROcp16_85 = -C4*S5
    ROcp16_16 = -(ROcp16_75*S6-C4*C6)
    ROcp16_26 = -(ROcp16_85*S6-S4*C6)
    ROcp16_36 = -C5*S6
    ROcp16_76 = ROcp16_75*C6+C4*S6
    ROcp16_86 = ROcp16_85*C6+S4*S6
    ROcp16_96 = C5*C6
    OMcp16_15 = qd[5]*C4
    OMcp16_25 = qd[5]*S4
    OMcp16_16 = OMcp16_15+ROcp16_45*qd[6]
    OMcp16_26 = OMcp16_25+ROcp16_55*qd[6]
    OMcp16_36 = qd[4]+qd[6]*S5
    OPcp16_16 = ROcp16_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp16_25*S5-ROcp16_55*qd[4])
    OPcp16_26 = ROcp16_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp16_15*S5-ROcp16_45*qd[4])
    OPcp16_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_17_0_5 = = 
 
# Sensor Kinematics 


    ROcp16_416 = ROcp16_45*C16+ROcp16_76*S16
    ROcp16_516 = ROcp16_55*C16+ROcp16_86*S16
    ROcp16_616 = ROcp16_96*S16+C16*S5
    ROcp16_716 = -(ROcp16_45*S16-ROcp16_76*C16)
    ROcp16_816 = -(ROcp16_55*S16-ROcp16_86*C16)
    ROcp16_916 = ROcp16_96*C16-S16*S5
    ROcp16_417 = ROcp16_416*C17+ROcp16_716*S17
    ROcp16_517 = ROcp16_516*C17+ROcp16_816*S17
    ROcp16_617 = ROcp16_616*C17+ROcp16_916*S17
    ROcp16_717 = -(ROcp16_416*S17-ROcp16_716*C17)
    ROcp16_817 = -(ROcp16_516*S17-ROcp16_816*C17)
    ROcp16_917 = -(ROcp16_616*S17-ROcp16_916*C17)
    RLcp16_116 = ROcp16_16*s.dpt[1,11]+ROcp16_45*s.dpt[2,11]+ROcp16_76*s.dpt[3,11]
    RLcp16_216 = ROcp16_26*s.dpt[1,11]+ROcp16_55*s.dpt[2,11]+ROcp16_86*s.dpt[3,11]
    RLcp16_316 = ROcp16_36*s.dpt[1,11]+ROcp16_96*s.dpt[3,11]+s.dpt[2,11]*S5
    OMcp16_116 = OMcp16_16+ROcp16_16*qd[16]
    OMcp16_216 = OMcp16_26+ROcp16_26*qd[16]
    OMcp16_316 = OMcp16_36+ROcp16_36*qd[16]
    ORcp16_116 = OMcp16_26*RLcp16_316-OMcp16_36*RLcp16_216
    ORcp16_216 = -(OMcp16_16*RLcp16_316-OMcp16_36*RLcp16_116)
    ORcp16_316 = OMcp16_16*RLcp16_216-OMcp16_26*RLcp16_116
    OPcp16_116 = OPcp16_16+ROcp16_16*qdd[16]+qd[16]*(OMcp16_26*ROcp16_36-OMcp16_36*ROcp16_26)
    OPcp16_216 = OPcp16_26+ROcp16_26*qdd[16]-qd[16]*(OMcp16_16*ROcp16_36-OMcp16_36*ROcp16_16)
    OPcp16_316 = OPcp16_36+ROcp16_36*qdd[16]+qd[16]*(OMcp16_16*ROcp16_26-OMcp16_26*ROcp16_16)
    RLcp16_117 = ROcp16_416*s.dpt[2,30]
    RLcp16_217 = ROcp16_516*s.dpt[2,30]
    RLcp16_317 = ROcp16_616*s.dpt[2,30]
    POcp16_117 = RLcp16_116+RLcp16_117+q[1]
    POcp16_217 = RLcp16_216+RLcp16_217+q[2]
    POcp16_317 = RLcp16_316+RLcp16_317+q[3]
    OMcp16_117 = OMcp16_116+ROcp16_16*qd[17]
    OMcp16_217 = OMcp16_216+ROcp16_26*qd[17]
    OMcp16_317 = OMcp16_316+ROcp16_36*qd[17]
    ORcp16_117 = OMcp16_216*RLcp16_317-OMcp16_316*RLcp16_217
    ORcp16_217 = -(OMcp16_116*RLcp16_317-OMcp16_316*RLcp16_117)
    ORcp16_317 = OMcp16_116*RLcp16_217-OMcp16_216*RLcp16_117
    VIcp16_117 = ORcp16_116+ORcp16_117+qd[1]
    VIcp16_217 = ORcp16_216+ORcp16_217+qd[2]
    VIcp16_317 = ORcp16_316+ORcp16_317+qd[3]
    OPcp16_117 = OPcp16_116+ROcp16_16*qdd[17]+qd[17]*(OMcp16_216*ROcp16_36-OMcp16_316*ROcp16_26)
    OPcp16_217 = OPcp16_216+ROcp16_26*qdd[17]-qd[17]*(OMcp16_116*ROcp16_36-OMcp16_316*ROcp16_16)
    OPcp16_317 = OPcp16_316+ROcp16_36*qdd[17]+qd[17]*(OMcp16_116*ROcp16_26-OMcp16_216*ROcp16_16)
    ACcp16_117 = qdd[1]+OMcp16_216*ORcp16_317+OMcp16_26*ORcp16_316-OMcp16_316*ORcp16_217-OMcp16_36*ORcp16_216+OPcp16_216*\
   RLcp16_317+OPcp16_26*RLcp16_316-OPcp16_316*RLcp16_217-OPcp16_36*RLcp16_216
    ACcp16_217 = qdd[2]-OMcp16_116*ORcp16_317-OMcp16_16*ORcp16_316+OMcp16_316*ORcp16_117+OMcp16_36*ORcp16_116-OPcp16_116*\
   RLcp16_317-OPcp16_16*RLcp16_316+OPcp16_316*RLcp16_117+OPcp16_36*RLcp16_116
    ACcp16_317 = qdd[3]+OMcp16_116*ORcp16_217+OMcp16_16*ORcp16_216-OMcp16_216*ORcp16_117-OMcp16_26*ORcp16_116+OPcp16_116*\
   RLcp16_217+OPcp16_16*RLcp16_216-OPcp16_216*RLcp16_117-OPcp16_26*RLcp16_116

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


    ROcp17_45 = -S4*C5
    ROcp17_55 = C4*C5
    ROcp17_75 = S4*S5
    ROcp17_85 = -C4*S5
    ROcp17_16 = -(ROcp17_75*S6-C4*C6)
    ROcp17_26 = -(ROcp17_85*S6-S4*C6)
    ROcp17_36 = -C5*S6
    ROcp17_76 = ROcp17_75*C6+C4*S6
    ROcp17_86 = ROcp17_85*C6+S4*S6
    ROcp17_96 = C5*C6
    OMcp17_15 = qd[5]*C4
    OMcp17_25 = qd[5]*S4
    OMcp17_16 = OMcp17_15+ROcp17_45*qd[6]
    OMcp17_26 = OMcp17_25+ROcp17_55*qd[6]
    OMcp17_36 = qd[4]+qd[6]*S5
    OPcp17_16 = ROcp17_45*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp17_25*S5-ROcp17_55*qd[4])
    OPcp17_26 = ROcp17_55*qdd[6]+qdd[5]*S4+qd[4]*qd[5]*C4-qd[6]*(OMcp17_15*S5-ROcp17_45*qd[4])
    OPcp17_36 = qdd[4]+qdd[6]*S5+qd[5]*qd[6]*C5

# = = Block_1_0_0_18_0_5 = = 
 
# Sensor Kinematics 


    ROcp17_416 = ROcp17_45*C16+ROcp17_76*S16
    ROcp17_516 = ROcp17_55*C16+ROcp17_86*S16
    ROcp17_616 = ROcp17_96*S16+C16*S5
    ROcp17_716 = -(ROcp17_45*S16-ROcp17_76*C16)
    ROcp17_816 = -(ROcp17_55*S16-ROcp17_86*C16)
    ROcp17_916 = ROcp17_96*C16-S16*S5
    ROcp17_417 = ROcp17_416*C17+ROcp17_716*S17
    ROcp17_517 = ROcp17_516*C17+ROcp17_816*S17
    ROcp17_617 = ROcp17_616*C17+ROcp17_916*S17
    ROcp17_717 = -(ROcp17_416*S17-ROcp17_716*C17)
    ROcp17_817 = -(ROcp17_516*S17-ROcp17_816*C17)
    ROcp17_917 = -(ROcp17_616*S17-ROcp17_916*C17)
    ROcp17_418 = ROcp17_417*C18+ROcp17_717*S18
    ROcp17_518 = ROcp17_517*C18+ROcp17_817*S18
    ROcp17_618 = ROcp17_617*C18+ROcp17_917*S18
    ROcp17_718 = -(ROcp17_417*S18-ROcp17_717*C18)
    ROcp17_818 = -(ROcp17_517*S18-ROcp17_817*C18)
    ROcp17_918 = -(ROcp17_617*S18-ROcp17_917*C18)
    RLcp17_116 = ROcp17_16*s.dpt[1,11]+ROcp17_45*s.dpt[2,11]+ROcp17_76*s.dpt[3,11]
    RLcp17_216 = ROcp17_26*s.dpt[1,11]+ROcp17_55*s.dpt[2,11]+ROcp17_86*s.dpt[3,11]
    RLcp17_316 = ROcp17_36*s.dpt[1,11]+ROcp17_96*s.dpt[3,11]+s.dpt[2,11]*S5
    OMcp17_116 = OMcp17_16+ROcp17_16*qd[16]
    OMcp17_216 = OMcp17_26+ROcp17_26*qd[16]
    OMcp17_316 = OMcp17_36+ROcp17_36*qd[16]
    ORcp17_116 = OMcp17_26*RLcp17_316-OMcp17_36*RLcp17_216
    ORcp17_216 = -(OMcp17_16*RLcp17_316-OMcp17_36*RLcp17_116)
    ORcp17_316 = OMcp17_16*RLcp17_216-OMcp17_26*RLcp17_116
    OPcp17_116 = OPcp17_16+ROcp17_16*qdd[16]+qd[16]*(OMcp17_26*ROcp17_36-OMcp17_36*ROcp17_26)
    OPcp17_216 = OPcp17_26+ROcp17_26*qdd[16]-qd[16]*(OMcp17_16*ROcp17_36-OMcp17_36*ROcp17_16)
    OPcp17_316 = OPcp17_36+ROcp17_36*qdd[16]+qd[16]*(OMcp17_16*ROcp17_26-OMcp17_26*ROcp17_16)
    RLcp17_117 = ROcp17_416*s.dpt[2,30]
    RLcp17_217 = ROcp17_516*s.dpt[2,30]
    RLcp17_317 = ROcp17_616*s.dpt[2,30]
    OMcp17_117 = OMcp17_116+ROcp17_16*qd[17]
    OMcp17_217 = OMcp17_216+ROcp17_26*qd[17]
    OMcp17_317 = OMcp17_316+ROcp17_36*qd[17]
    ORcp17_117 = OMcp17_216*RLcp17_317-OMcp17_316*RLcp17_217
    ORcp17_217 = -(OMcp17_116*RLcp17_317-OMcp17_316*RLcp17_117)
    ORcp17_317 = OMcp17_116*RLcp17_217-OMcp17_216*RLcp17_117
    OPcp17_117 = OPcp17_116+ROcp17_16*qdd[17]+qd[17]*(OMcp17_216*ROcp17_36-OMcp17_316*ROcp17_26)
    OPcp17_217 = OPcp17_216+ROcp17_26*qdd[17]-qd[17]*(OMcp17_116*ROcp17_36-OMcp17_316*ROcp17_16)
    OPcp17_317 = OPcp17_316+ROcp17_36*qdd[17]+qd[17]*(OMcp17_116*ROcp17_26-OMcp17_216*ROcp17_16)
    RLcp17_118 = ROcp17_16*s.dpt[1,34]
    RLcp17_218 = ROcp17_26*s.dpt[1,34]
    RLcp17_318 = ROcp17_36*s.dpt[1,34]
    POcp17_118 = RLcp17_116+RLcp17_117+RLcp17_118+q[1]
    POcp17_218 = RLcp17_216+RLcp17_217+RLcp17_218+q[2]
    POcp17_318 = RLcp17_316+RLcp17_317+RLcp17_318+q[3]
    OMcp17_118 = OMcp17_117+ROcp17_16*qd[18]
    OMcp17_218 = OMcp17_217+ROcp17_26*qd[18]
    OMcp17_318 = OMcp17_317+ROcp17_36*qd[18]
    ORcp17_118 = OMcp17_217*RLcp17_318-OMcp17_317*RLcp17_218
    ORcp17_218 = -(OMcp17_117*RLcp17_318-OMcp17_317*RLcp17_118)
    ORcp17_318 = OMcp17_117*RLcp17_218-OMcp17_217*RLcp17_118
    VIcp17_118 = ORcp17_116+ORcp17_117+ORcp17_118+qd[1]
    VIcp17_218 = ORcp17_216+ORcp17_217+ORcp17_218+qd[2]
    VIcp17_318 = ORcp17_316+ORcp17_317+ORcp17_318+qd[3]
    OPcp17_118 = OPcp17_117+ROcp17_16*qdd[18]+qd[18]*(OMcp17_217*ROcp17_36-OMcp17_317*ROcp17_26)
    OPcp17_218 = OPcp17_217+ROcp17_26*qdd[18]-qd[18]*(OMcp17_117*ROcp17_36-OMcp17_317*ROcp17_16)
    OPcp17_318 = OPcp17_317+ROcp17_36*qdd[18]+qd[18]*(OMcp17_117*ROcp17_26-OMcp17_217*ROcp17_16)
    ACcp17_118 = qdd[1]+OMcp17_216*ORcp17_317+OMcp17_217*ORcp17_318+OMcp17_26*ORcp17_316-OMcp17_316*ORcp17_217-OMcp17_317*\
   ORcp17_218-OMcp17_36*ORcp17_216+OPcp17_216*RLcp17_317+OPcp17_217*RLcp17_318+OPcp17_26*RLcp17_316-OPcp17_316*RLcp17_217-\
   OPcp17_317*RLcp17_218-OPcp17_36*RLcp17_216
    ACcp17_218 = qdd[2]-OMcp17_116*ORcp17_317-OMcp17_117*ORcp17_318-OMcp17_16*ORcp17_316+OMcp17_316*ORcp17_117+OMcp17_317*\
   ORcp17_118+OMcp17_36*ORcp17_116-OPcp17_116*RLcp17_317-OPcp17_117*RLcp17_318-OPcp17_16*RLcp17_316+OPcp17_316*RLcp17_117+\
   OPcp17_317*RLcp17_118+OPcp17_36*RLcp17_116
    ACcp17_318 = qdd[3]+OMcp17_116*ORcp17_217+OMcp17_117*ORcp17_218+OMcp17_16*ORcp17_216-OMcp17_216*ORcp17_117-OMcp17_217*\
   ORcp17_118-OMcp17_26*ORcp17_116+OPcp17_116*RLcp17_217+OPcp17_117*RLcp17_218+OPcp17_16*RLcp17_216-OPcp17_216*RLcp17_117-\
   OPcp17_217*RLcp17_118-OPcp17_26*RLcp17_116

# = = Block_1_0_0_18_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp17_118
    sens.P[2] = POcp17_218
    sens.P[3] = POcp17_318
    sens.R[1,1] = ROcp17_16
    sens.R[1,2] = ROcp17_26
    sens.R[1,3] = ROcp17_36
    sens.R[2,1] = ROcp17_418
    sens.R[2,2] = ROcp17_518
    sens.R[2,3] = ROcp17_618
    sens.R[3,1] = ROcp17_718
    sens.R[3,2] = ROcp17_818
    sens.R[3,3] = ROcp17_918
    sens.V[1] = VIcp17_118
    sens.V[2] = VIcp17_218
    sens.V[3] = VIcp17_318
    sens.OM[1] = OMcp17_118
    sens.OM[2] = OMcp17_218
    sens.OM[3] = OMcp17_318
    sens.A[1] = ACcp17_118
    sens.A[2] = ACcp17_218
    sens.A[3] = ACcp17_318
    sens.OMP[1] = OPcp17_118
    sens.OMP[2] = OPcp17_218
    sens.OMP[3] = OPcp17_318



# ====== END Task 1 ====== 

  

