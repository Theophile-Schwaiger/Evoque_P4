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
#	==> Generation Date : Sun May  3 18:39:12 2020
#
#	==> Project name : Complete_Vehicle_New_Dimensions
#	==> using XML input file 
#
#	==> Number of joints : 67
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 2264
#
#	==> Generation Time :  0.050 seconds
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

# = = Block_0_0_0_0_0_7 = = 
 
# Trigonometric Variables  

  C21 = np.cos(q[21])
  S21 = np.sin(q[21])
  C22 = np.cos(q[22])
  S22 = np.sin(q[22])

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

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C36 = np.cos(q[36])
  S36 = np.sin(q[36])
  C37 = np.cos(q[37])
  S37 = np.sin(q[37])

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

# = = Block_0_0_0_0_0_17 = = 
 
# Trigonometric Variables  

  C47 = np.cos(q[47])
  S47 = np.sin(q[47])
  C48 = np.cos(q[48])
  S48 = np.sin(q[48])

# = = Block_0_0_0_3_0_2 = = 
 
# Trigonometric Variables  

  S6p7 = C6*S7+S6*C7
  C6p7 = C6*C7-S6*S7

# = = Block_0_0_0_4_0_5 = = 
 
# Trigonometric Variables  

  S15p6 = C15*S6+S15*C6
  C15p6 = C15*C6-S15*S6

# = = Block_0_0_0_5_0_11 = = 
 
# Trigonometric Variables  

  S29p6 = C29*S6+S29*C6
  C29p6 = C29*C6-S29*S6

# = = Block_0_0_0_6_0_15 = = 
 
# Trigonometric Variables  

  S40p6 = C40*S6+S40*C6
  C40p6 = C40*C6-S40*S6

# ====== END Task 0 ====== 

# ===== BEGIN task 1 ===== 
 
# Sensor Kinematics 


 
# 
  if(isens==1): 


# = = Block_1_0_0_1_0_1 = = 
 
# Sensor Kinematics 


    ROcp0_15 = C4*C5
    ROcp0_25 = S4*C5
    ROcp0_75 = C4*S5
    ROcp0_85 = S4*S5
    ROcp0_46 = ROcp0_75*S6-S4*C6
    ROcp0_56 = ROcp0_85*S6+C4*C6
    ROcp0_66 = C5*S6
    ROcp0_76 = ROcp0_75*C6+S4*S6
    ROcp0_86 = ROcp0_85*C6-C4*S6
    ROcp0_96 = C5*C6
    OMcp0_15 = -qd[5]*S4
    OMcp0_25 = qd[5]*C4
    OMcp0_16 = OMcp0_15+ROcp0_15*qd[6]
    OMcp0_26 = OMcp0_25+ROcp0_25*qd[6]
    OMcp0_36 = qd[4]-qd[6]*S5
    OPcp0_16 = ROcp0_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp0_25*S5+ROcp0_25*qd[4])
    OPcp0_26 = ROcp0_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp0_15*S5+ROcp0_15*qd[4])
    OPcp0_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5
    RLcp0_196 = ROcp0_15*s.dpt[1,16]+ROcp0_76*s.dpt[3,16]
    RLcp0_296 = ROcp0_25*s.dpt[1,16]+ROcp0_86*s.dpt[3,16]
    RLcp0_396 = ROcp0_96*s.dpt[3,16]-s.dpt[1,16]*S5
    POcp0_196 = RLcp0_196+q[1]
    POcp0_296 = RLcp0_296+q[2]
    POcp0_396 = RLcp0_396+q[3]
    ORcp0_196 = OMcp0_26*RLcp0_396-OMcp0_36*RLcp0_296
    ORcp0_296 = -(OMcp0_16*RLcp0_396-OMcp0_36*RLcp0_196)
    ORcp0_396 = OMcp0_16*RLcp0_296-OMcp0_26*RLcp0_196
    VIcp0_196 = ORcp0_196+qd[1]
    VIcp0_296 = ORcp0_296+qd[2]
    VIcp0_396 = ORcp0_396+qd[3]
    ACcp0_196 = qdd[1]+OMcp0_26*ORcp0_396-OMcp0_36*ORcp0_296+OPcp0_26*RLcp0_396-OPcp0_36*RLcp0_296
    ACcp0_296 = qdd[2]-OMcp0_16*ORcp0_396+OMcp0_36*ORcp0_196-OPcp0_16*RLcp0_396+OPcp0_36*RLcp0_196
    ACcp0_396 = qdd[3]+OMcp0_16*ORcp0_296-OMcp0_26*ORcp0_196+OPcp0_16*RLcp0_296-OPcp0_26*RLcp0_196

# = = Block_1_0_0_1_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp0_196
    sens.P[2] = POcp0_296
    sens.P[3] = POcp0_396
    sens.R[1,1] = ROcp0_15
    sens.R[1,2] = ROcp0_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp0_46
    sens.R[2,2] = ROcp0_56
    sens.R[2,3] = ROcp0_66
    sens.R[3,1] = ROcp0_76
    sens.R[3,2] = ROcp0_86
    sens.R[3,3] = ROcp0_96
    sens.V[1] = VIcp0_196
    sens.V[2] = VIcp0_296
    sens.V[3] = VIcp0_396
    sens.OM[1] = OMcp0_16
    sens.OM[2] = OMcp0_26
    sens.OM[3] = OMcp0_36
    sens.A[1] = ACcp0_196
    sens.A[2] = ACcp0_296
    sens.A[3] = ACcp0_396
    sens.OMP[1] = OPcp0_16
    sens.OMP[2] = OPcp0_26
    sens.OMP[3] = OPcp0_36
 
# 
  elif(isens==2): 


# = = Block_1_0_0_2_0_1 = = 
 
# Sensor Kinematics 


    ROcp1_15 = C4*C5
    ROcp1_25 = S4*C5
    ROcp1_75 = C4*S5
    ROcp1_85 = S4*S5
    ROcp1_46 = ROcp1_75*S6-S4*C6
    ROcp1_56 = ROcp1_85*S6+C4*C6
    ROcp1_66 = C5*S6
    ROcp1_76 = ROcp1_75*C6+S4*S6
    ROcp1_86 = ROcp1_85*C6-C4*S6
    ROcp1_96 = C5*C6
    OMcp1_15 = -qd[5]*S4
    OMcp1_25 = qd[5]*C4
    OMcp1_16 = OMcp1_15+ROcp1_15*qd[6]
    OMcp1_26 = OMcp1_25+ROcp1_25*qd[6]
    OMcp1_36 = qd[4]-qd[6]*S5
    OPcp1_16 = ROcp1_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp1_25*S5+ROcp1_25*qd[4])
    OPcp1_26 = ROcp1_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp1_15*S5+ROcp1_15*qd[4])
    OPcp1_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5
    RLcp1_197 = ROcp1_15*s.dpt[1,17]+ROcp1_76*s.dpt[3,17]
    RLcp1_297 = ROcp1_25*s.dpt[1,17]+ROcp1_86*s.dpt[3,17]
    RLcp1_397 = ROcp1_96*s.dpt[3,17]-s.dpt[1,17]*S5
    POcp1_197 = RLcp1_197+q[1]
    POcp1_297 = RLcp1_297+q[2]
    POcp1_397 = RLcp1_397+q[3]
    ORcp1_197 = OMcp1_26*RLcp1_397-OMcp1_36*RLcp1_297
    ORcp1_297 = -(OMcp1_16*RLcp1_397-OMcp1_36*RLcp1_197)
    ORcp1_397 = OMcp1_16*RLcp1_297-OMcp1_26*RLcp1_197
    VIcp1_197 = ORcp1_197+qd[1]
    VIcp1_297 = ORcp1_297+qd[2]
    VIcp1_397 = ORcp1_397+qd[3]
    ACcp1_197 = qdd[1]+OMcp1_26*ORcp1_397-OMcp1_36*ORcp1_297+OPcp1_26*RLcp1_397-OPcp1_36*RLcp1_297
    ACcp1_297 = qdd[2]-OMcp1_16*ORcp1_397+OMcp1_36*ORcp1_197-OPcp1_16*RLcp1_397+OPcp1_36*RLcp1_197
    ACcp1_397 = qdd[3]+OMcp1_16*ORcp1_297-OMcp1_26*ORcp1_197+OPcp1_16*RLcp1_297-OPcp1_26*RLcp1_197

# = = Block_1_0_0_2_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp1_197
    sens.P[2] = POcp1_297
    sens.P[3] = POcp1_397
    sens.R[1,1] = ROcp1_15
    sens.R[1,2] = ROcp1_25
    sens.R[1,3] = -S5
    sens.R[2,1] = ROcp1_46
    sens.R[2,2] = ROcp1_56
    sens.R[2,3] = ROcp1_66
    sens.R[3,1] = ROcp1_76
    sens.R[3,2] = ROcp1_86
    sens.R[3,3] = ROcp1_96
    sens.V[1] = VIcp1_197
    sens.V[2] = VIcp1_297
    sens.V[3] = VIcp1_397
    sens.OM[1] = OMcp1_16
    sens.OM[2] = OMcp1_26
    sens.OM[3] = OMcp1_36
    sens.A[1] = ACcp1_197
    sens.A[2] = ACcp1_297
    sens.A[3] = ACcp1_397
    sens.OMP[1] = OPcp1_16
    sens.OMP[2] = OPcp1_26
    sens.OMP[3] = OPcp1_36
 
# 
  elif(isens==3): 


# = = Block_1_0_0_3_0_1 = = 
 
# Sensor Kinematics 


    ROcp2_15 = C4*C5
    ROcp2_25 = S4*C5
    ROcp2_75 = C4*S5
    ROcp2_85 = S4*S5
    ROcp2_46 = ROcp2_75*S6-S4*C6
    ROcp2_56 = ROcp2_85*S6+C4*C6
    ROcp2_76 = ROcp2_75*C6+S4*S6
    ROcp2_86 = ROcp2_85*C6-C4*S6
    OMcp2_15 = -qd[5]*S4
    OMcp2_25 = qd[5]*C4
    OMcp2_16 = OMcp2_15+ROcp2_15*qd[6]
    OMcp2_26 = OMcp2_25+ROcp2_25*qd[6]
    OMcp2_36 = qd[4]-qd[6]*S5
    OPcp2_16 = ROcp2_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp2_25*S5+ROcp2_25*qd[4])
    OPcp2_26 = ROcp2_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp2_15*S5+ROcp2_15*qd[4])
    OPcp2_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_3_0_2 = = 
 
# Sensor Kinematics 


    ROcp2_47 = ROcp2_46*C7+ROcp2_76*S7
    ROcp2_57 = ROcp2_56*C7+ROcp2_86*S7
    ROcp2_67 = S6p7*C5
    ROcp2_77 = -(ROcp2_46*S7-ROcp2_76*C7)
    ROcp2_87 = -(ROcp2_56*S7-ROcp2_86*C7)
    ROcp2_97 = C6p7*C5
    ROcp2_18 = ROcp2_15*C8+ROcp2_47*S8
    ROcp2_28 = ROcp2_25*C8+ROcp2_57*S8
    ROcp2_38 = ROcp2_67*S8-S5*C8
    ROcp2_48 = -(ROcp2_15*S8-ROcp2_47*C8)
    ROcp2_58 = -(ROcp2_25*S8-ROcp2_57*C8)
    ROcp2_68 = ROcp2_67*C8+S5*S8
    ROcp2_49 = ROcp2_48*C9+ROcp2_77*S9
    ROcp2_59 = ROcp2_58*C9+ROcp2_87*S9
    ROcp2_69 = ROcp2_68*C9+ROcp2_97*S9
    ROcp2_79 = -(ROcp2_48*S9-ROcp2_77*C9)
    ROcp2_89 = -(ROcp2_58*S9-ROcp2_87*C9)
    ROcp2_99 = -(ROcp2_68*S9-ROcp2_97*C9)
    ROcp2_110 = ROcp2_18*C10-ROcp2_79*S10
    ROcp2_210 = ROcp2_28*C10-ROcp2_89*S10
    ROcp2_310 = ROcp2_38*C10-ROcp2_99*S10
    ROcp2_710 = ROcp2_18*S10+ROcp2_79*C10
    ROcp2_810 = ROcp2_28*S10+ROcp2_89*C10
    ROcp2_910 = ROcp2_38*S10+ROcp2_99*C10
    RLcp2_17 = ROcp2_15*s.dpt[1,1]+ROcp2_46*s.dpt[2,1]
    RLcp2_27 = ROcp2_25*s.dpt[1,1]+ROcp2_56*s.dpt[2,1]
    RLcp2_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
    OMcp2_17 = OMcp2_16+ROcp2_15*qd[7]
    OMcp2_27 = OMcp2_26+ROcp2_25*qd[7]
    OMcp2_37 = OMcp2_36-qd[7]*S5
    ORcp2_17 = OMcp2_26*RLcp2_37-OMcp2_36*RLcp2_27
    ORcp2_27 = -(OMcp2_16*RLcp2_37-OMcp2_36*RLcp2_17)
    ORcp2_37 = OMcp2_16*RLcp2_27-OMcp2_26*RLcp2_17
    OPcp2_17 = OPcp2_16+ROcp2_15*qdd[7]-qd[7]*(OMcp2_26*S5+OMcp2_36*ROcp2_25)
    OPcp2_27 = OPcp2_26+ROcp2_25*qdd[7]+qd[7]*(OMcp2_16*S5+OMcp2_36*ROcp2_15)
    OPcp2_37 = OPcp2_36-qdd[7]*S5+qd[7]*(OMcp2_16*ROcp2_25-OMcp2_26*ROcp2_15)
    RLcp2_18 = ROcp2_47*s.dpt[2,18]
    RLcp2_28 = ROcp2_57*s.dpt[2,18]
    RLcp2_38 = ROcp2_67*s.dpt[2,18]
    OMcp2_18 = OMcp2_17+ROcp2_77*qd[8]
    OMcp2_28 = OMcp2_27+ROcp2_87*qd[8]
    OMcp2_38 = OMcp2_37+ROcp2_97*qd[8]
    ORcp2_18 = OMcp2_27*RLcp2_38-OMcp2_37*RLcp2_28
    ORcp2_28 = -(OMcp2_17*RLcp2_38-OMcp2_37*RLcp2_18)
    ORcp2_38 = OMcp2_17*RLcp2_28-OMcp2_27*RLcp2_18
    OMcp2_19 = OMcp2_18+ROcp2_18*qd[9]
    OMcp2_29 = OMcp2_28+ROcp2_28*qd[9]
    OMcp2_39 = OMcp2_38+ROcp2_38*qd[9]
    OMcp2_110 = OMcp2_19+ROcp2_49*qd[10]
    OMcp2_210 = OMcp2_29+ROcp2_59*qd[10]
    OMcp2_310 = OMcp2_39+ROcp2_69*qd[10]
    OPcp2_110 = OPcp2_17+ROcp2_18*qdd[9]+ROcp2_49*qdd[10]+ROcp2_77*qdd[8]+qd[10]*(OMcp2_29*ROcp2_69-OMcp2_39*ROcp2_59)+\
   qd[8]*(OMcp2_27*ROcp2_97-OMcp2_37*ROcp2_87)+qd[9]*(OMcp2_28*ROcp2_38-OMcp2_38*ROcp2_28)
    OPcp2_210 = OPcp2_27+ROcp2_28*qdd[9]+ROcp2_59*qdd[10]+ROcp2_87*qdd[8]-qd[10]*(OMcp2_19*ROcp2_69-OMcp2_39*ROcp2_49)-\
   qd[8]*(OMcp2_17*ROcp2_97-OMcp2_37*ROcp2_77)-qd[9]*(OMcp2_18*ROcp2_38-OMcp2_38*ROcp2_18)
    OPcp2_310 = OPcp2_37+ROcp2_38*qdd[9]+ROcp2_69*qdd[10]+ROcp2_97*qdd[8]+qd[10]*(OMcp2_19*ROcp2_59-OMcp2_29*ROcp2_49)+\
   qd[8]*(OMcp2_17*ROcp2_87-OMcp2_27*ROcp2_77)+qd[9]*(OMcp2_18*ROcp2_28-OMcp2_28*ROcp2_18)

# = = Block_1_0_0_3_0_4 = = 
 
# Sensor Kinematics 


    ROcp2_413 = ROcp2_49*C13+ROcp2_710*S13
    ROcp2_513 = ROcp2_59*C13+ROcp2_810*S13
    ROcp2_613 = ROcp2_69*C13+ROcp2_910*S13
    ROcp2_713 = -(ROcp2_49*S13-ROcp2_710*C13)
    ROcp2_813 = -(ROcp2_59*S13-ROcp2_810*C13)
    ROcp2_913 = -(ROcp2_69*S13-ROcp2_910*C13)
    ROcp2_114 = ROcp2_110*C14-ROcp2_713*S14
    ROcp2_214 = ROcp2_210*C14-ROcp2_813*S14
    ROcp2_314 = ROcp2_310*C14-ROcp2_913*S14
    ROcp2_714 = ROcp2_110*S14+ROcp2_713*C14
    ROcp2_814 = ROcp2_210*S14+ROcp2_813*C14
    ROcp2_914 = ROcp2_310*S14+ROcp2_913*C14
    RLcp2_113 = ROcp2_49*s.dpt[2,20]+ROcp2_710*s.dpt[3,20]
    RLcp2_213 = ROcp2_59*s.dpt[2,20]+ROcp2_810*s.dpt[3,20]
    RLcp2_313 = ROcp2_69*s.dpt[2,20]+ROcp2_910*s.dpt[3,20]
    POcp2_113 = RLcp2_113+RLcp2_17+RLcp2_18+q[1]
    POcp2_213 = RLcp2_213+RLcp2_27+RLcp2_28+q[2]
    POcp2_313 = RLcp2_313+RLcp2_37+RLcp2_38+q[3]
    OMcp2_113 = OMcp2_110+ROcp2_110*qd[13]
    OMcp2_213 = OMcp2_210+ROcp2_210*qd[13]
    OMcp2_313 = OMcp2_310+ROcp2_310*qd[13]
    ORcp2_113 = OMcp2_210*RLcp2_313-OMcp2_310*RLcp2_213
    ORcp2_213 = -(OMcp2_110*RLcp2_313-OMcp2_310*RLcp2_113)
    ORcp2_313 = OMcp2_110*RLcp2_213-OMcp2_210*RLcp2_113
    VIcp2_113 = ORcp2_113+ORcp2_17+ORcp2_18+qd[1]
    VIcp2_213 = ORcp2_213+ORcp2_27+ORcp2_28+qd[2]
    VIcp2_313 = ORcp2_313+ORcp2_37+ORcp2_38+qd[3]
    ACcp2_113 = qdd[1]+OMcp2_210*ORcp2_313+OMcp2_26*ORcp2_37+OMcp2_27*ORcp2_38-OMcp2_310*ORcp2_213-OMcp2_36*ORcp2_27-\
   OMcp2_37*ORcp2_28+OPcp2_210*RLcp2_313+OPcp2_26*RLcp2_37+OPcp2_27*RLcp2_38-OPcp2_310*RLcp2_213-OPcp2_36*RLcp2_27-OPcp2_37*\
   RLcp2_28
    ACcp2_213 = qdd[2]-OMcp2_110*ORcp2_313-OMcp2_16*ORcp2_37-OMcp2_17*ORcp2_38+OMcp2_310*ORcp2_113+OMcp2_36*ORcp2_17+\
   OMcp2_37*ORcp2_18-OPcp2_110*RLcp2_313-OPcp2_16*RLcp2_37-OPcp2_17*RLcp2_38+OPcp2_310*RLcp2_113+OPcp2_36*RLcp2_17+OPcp2_37*\
   RLcp2_18
    ACcp2_313 = qdd[3]+OMcp2_110*ORcp2_213+OMcp2_16*ORcp2_27+OMcp2_17*ORcp2_28-OMcp2_210*ORcp2_113-OMcp2_26*ORcp2_17-\
   OMcp2_27*ORcp2_18+OPcp2_110*RLcp2_213+OPcp2_16*RLcp2_27+OPcp2_17*RLcp2_28-OPcp2_210*RLcp2_113-OPcp2_26*RLcp2_17-OPcp2_27*\
   RLcp2_18
    OMcp2_114 = OMcp2_113+ROcp2_413*qd[14]
    OMcp2_214 = OMcp2_213+ROcp2_513*qd[14]
    OMcp2_314 = OMcp2_313+ROcp2_613*qd[14]
    OPcp2_114 = OPcp2_110+ROcp2_110*qdd[13]+ROcp2_413*qdd[14]+qd[13]*(OMcp2_210*ROcp2_310-OMcp2_310*ROcp2_210)+qd[14]*(\
   OMcp2_213*ROcp2_613-OMcp2_313*ROcp2_513)
    OPcp2_214 = OPcp2_210+ROcp2_210*qdd[13]+ROcp2_513*qdd[14]-qd[13]*(OMcp2_110*ROcp2_310-OMcp2_310*ROcp2_110)-qd[14]*(\
   OMcp2_113*ROcp2_613-OMcp2_313*ROcp2_413)
    OPcp2_314 = OPcp2_310+ROcp2_310*qdd[13]+ROcp2_613*qdd[14]+qd[13]*(OMcp2_110*ROcp2_210-OMcp2_210*ROcp2_110)+qd[14]*(\
   OMcp2_113*ROcp2_513-OMcp2_213*ROcp2_413)

# = = Block_1_0_0_3_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp2_113
    sens.P[2] = POcp2_213
    sens.P[3] = POcp2_313
    sens.R[1,1] = ROcp2_114
    sens.R[1,2] = ROcp2_214
    sens.R[1,3] = ROcp2_314
    sens.R[2,1] = ROcp2_413
    sens.R[2,2] = ROcp2_513
    sens.R[2,3] = ROcp2_613
    sens.R[3,1] = ROcp2_714
    sens.R[3,2] = ROcp2_814
    sens.R[3,3] = ROcp2_914
    sens.V[1] = VIcp2_113
    sens.V[2] = VIcp2_213
    sens.V[3] = VIcp2_313
    sens.OM[1] = OMcp2_114
    sens.OM[2] = OMcp2_214
    sens.OM[3] = OMcp2_314
    sens.A[1] = ACcp2_113
    sens.A[2] = ACcp2_213
    sens.A[3] = ACcp2_313
    sens.OMP[1] = OPcp2_114
    sens.OMP[2] = OPcp2_214
    sens.OMP[3] = OPcp2_314
 
# 
  elif(isens==4): 


# = = Block_1_0_0_4_0_1 = = 
 
# Sensor Kinematics 


    ROcp3_15 = C4*C5
    ROcp3_25 = S4*C5
    ROcp3_75 = C4*S5
    ROcp3_85 = S4*S5
    ROcp3_46 = ROcp3_75*S6-S4*C6
    ROcp3_56 = ROcp3_85*S6+C4*C6
    ROcp3_76 = ROcp3_75*C6+S4*S6
    ROcp3_86 = ROcp3_85*C6-C4*S6
    OMcp3_15 = -qd[5]*S4
    OMcp3_25 = qd[5]*C4
    OMcp3_16 = OMcp3_15+ROcp3_15*qd[6]
    OMcp3_26 = OMcp3_25+ROcp3_25*qd[6]
    OMcp3_36 = qd[4]-qd[6]*S5
    OPcp3_16 = ROcp3_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp3_25*S5+ROcp3_25*qd[4])
    OPcp3_26 = ROcp3_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp3_15*S5+ROcp3_15*qd[4])
    OPcp3_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_4_0_5 = = 
 
# Sensor Kinematics 


    ROcp3_415 = ROcp3_46*C15+ROcp3_76*S15
    ROcp3_515 = ROcp3_56*C15+ROcp3_86*S15
    ROcp3_615 = S15p6*C5
    ROcp3_715 = -(ROcp3_46*S15-ROcp3_76*C15)
    ROcp3_815 = -(ROcp3_56*S15-ROcp3_86*C15)
    ROcp3_915 = C15p6*C5
    ROcp3_116 = ROcp3_15*C16+ROcp3_415*S16
    ROcp3_216 = ROcp3_25*C16+ROcp3_515*S16
    ROcp3_316 = ROcp3_615*S16-C16*S5
    ROcp3_416 = -(ROcp3_15*S16-ROcp3_415*C16)
    ROcp3_516 = -(ROcp3_25*S16-ROcp3_515*C16)
    ROcp3_616 = ROcp3_615*C16+S16*S5
    ROcp3_417 = ROcp3_416*C17+ROcp3_715*S17
    ROcp3_517 = ROcp3_516*C17+ROcp3_815*S17
    ROcp3_617 = ROcp3_616*C17+ROcp3_915*S17
    ROcp3_717 = -(ROcp3_416*S17-ROcp3_715*C17)
    ROcp3_817 = -(ROcp3_516*S17-ROcp3_815*C17)
    ROcp3_917 = -(ROcp3_616*S17-ROcp3_915*C17)
    ROcp3_118 = ROcp3_116*C18-ROcp3_717*S18
    ROcp3_218 = ROcp3_216*C18-ROcp3_817*S18
    ROcp3_318 = ROcp3_316*C18-ROcp3_917*S18
    ROcp3_718 = ROcp3_116*S18+ROcp3_717*C18
    ROcp3_818 = ROcp3_216*S18+ROcp3_817*C18
    ROcp3_918 = ROcp3_316*S18+ROcp3_917*C18
    RLcp3_115 = ROcp3_15*s.dpt[1,4]+ROcp3_46*s.dpt[2,4]
    RLcp3_215 = ROcp3_25*s.dpt[1,4]+ROcp3_56*s.dpt[2,4]
    RLcp3_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
    OMcp3_115 = OMcp3_16+ROcp3_15*qd[15]
    OMcp3_215 = OMcp3_26+ROcp3_25*qd[15]
    OMcp3_315 = OMcp3_36-qd[15]*S5
    ORcp3_115 = OMcp3_26*RLcp3_315-OMcp3_36*RLcp3_215
    ORcp3_215 = -(OMcp3_16*RLcp3_315-OMcp3_36*RLcp3_115)
    ORcp3_315 = OMcp3_16*RLcp3_215-OMcp3_26*RLcp3_115
    OPcp3_115 = OPcp3_16+ROcp3_15*qdd[15]-qd[15]*(OMcp3_26*S5+OMcp3_36*ROcp3_25)
    OPcp3_215 = OPcp3_26+ROcp3_25*qdd[15]+qd[15]*(OMcp3_16*S5+OMcp3_36*ROcp3_15)
    OPcp3_315 = OPcp3_36-qdd[15]*S5+qd[15]*(OMcp3_16*ROcp3_25-OMcp3_26*ROcp3_15)
    RLcp3_116 = ROcp3_415*s.dpt[2,25]
    RLcp3_216 = ROcp3_515*s.dpt[2,25]
    RLcp3_316 = ROcp3_615*s.dpt[2,25]
    OMcp3_116 = OMcp3_115+ROcp3_715*qd[16]
    OMcp3_216 = OMcp3_215+ROcp3_815*qd[16]
    OMcp3_316 = OMcp3_315+ROcp3_915*qd[16]
    ORcp3_116 = OMcp3_215*RLcp3_316-OMcp3_315*RLcp3_216
    ORcp3_216 = -(OMcp3_115*RLcp3_316-OMcp3_315*RLcp3_116)
    ORcp3_316 = OMcp3_115*RLcp3_216-OMcp3_215*RLcp3_116
    OMcp3_117 = OMcp3_116+ROcp3_116*qd[17]
    OMcp3_217 = OMcp3_216+ROcp3_216*qd[17]
    OMcp3_317 = OMcp3_316+ROcp3_316*qd[17]
    OMcp3_118 = OMcp3_117+ROcp3_417*qd[18]
    OMcp3_218 = OMcp3_217+ROcp3_517*qd[18]
    OMcp3_318 = OMcp3_317+ROcp3_617*qd[18]
    OPcp3_118 = OPcp3_115+ROcp3_116*qdd[17]+ROcp3_417*qdd[18]+ROcp3_715*qdd[16]+qd[16]*(OMcp3_215*ROcp3_915-OMcp3_315*\
   ROcp3_815)+qd[17]*(OMcp3_216*ROcp3_316-OMcp3_316*ROcp3_216)+qd[18]*(OMcp3_217*ROcp3_617-OMcp3_317*ROcp3_517)
    OPcp3_218 = OPcp3_215+ROcp3_216*qdd[17]+ROcp3_517*qdd[18]+ROcp3_815*qdd[16]-qd[16]*(OMcp3_115*ROcp3_915-OMcp3_315*\
   ROcp3_715)-qd[17]*(OMcp3_116*ROcp3_316-OMcp3_316*ROcp3_116)-qd[18]*(OMcp3_117*ROcp3_617-OMcp3_317*ROcp3_417)
    OPcp3_318 = OPcp3_315+ROcp3_316*qdd[17]+ROcp3_617*qdd[18]+ROcp3_915*qdd[16]+qd[16]*(OMcp3_115*ROcp3_815-OMcp3_215*\
   ROcp3_715)+qd[17]*(OMcp3_116*ROcp3_216-OMcp3_216*ROcp3_116)+qd[18]*(OMcp3_117*ROcp3_517-OMcp3_217*ROcp3_417)

# = = Block_1_0_0_4_0_7 = = 
 
# Sensor Kinematics 


    ROcp3_421 = ROcp3_417*C21+ROcp3_718*S21
    ROcp3_521 = ROcp3_517*C21+ROcp3_818*S21
    ROcp3_621 = ROcp3_617*C21+ROcp3_918*S21
    ROcp3_721 = -(ROcp3_417*S21-ROcp3_718*C21)
    ROcp3_821 = -(ROcp3_517*S21-ROcp3_818*C21)
    ROcp3_921 = -(ROcp3_617*S21-ROcp3_918*C21)
    ROcp3_122 = ROcp3_118*C22-ROcp3_721*S22
    ROcp3_222 = ROcp3_218*C22-ROcp3_821*S22
    ROcp3_322 = ROcp3_318*C22-ROcp3_921*S22
    ROcp3_722 = ROcp3_118*S22+ROcp3_721*C22
    ROcp3_822 = ROcp3_218*S22+ROcp3_821*C22
    ROcp3_922 = ROcp3_318*S22+ROcp3_921*C22
    RLcp3_121 = ROcp3_417*s.dpt[2,27]+ROcp3_718*s.dpt[3,27]
    RLcp3_221 = ROcp3_517*s.dpt[2,27]+ROcp3_818*s.dpt[3,27]
    RLcp3_321 = ROcp3_617*s.dpt[2,27]+ROcp3_918*s.dpt[3,27]
    POcp3_121 = RLcp3_115+RLcp3_116+RLcp3_121+q[1]
    POcp3_221 = RLcp3_215+RLcp3_216+RLcp3_221+q[2]
    POcp3_321 = RLcp3_315+RLcp3_316+RLcp3_321+q[3]
    OMcp3_121 = OMcp3_118+ROcp3_118*qd[21]
    OMcp3_221 = OMcp3_218+ROcp3_218*qd[21]
    OMcp3_321 = OMcp3_318+ROcp3_318*qd[21]
    ORcp3_121 = OMcp3_218*RLcp3_321-OMcp3_318*RLcp3_221
    ORcp3_221 = -(OMcp3_118*RLcp3_321-OMcp3_318*RLcp3_121)
    ORcp3_321 = OMcp3_118*RLcp3_221-OMcp3_218*RLcp3_121
    VIcp3_121 = ORcp3_115+ORcp3_116+ORcp3_121+qd[1]
    VIcp3_221 = ORcp3_215+ORcp3_216+ORcp3_221+qd[2]
    VIcp3_321 = ORcp3_315+ORcp3_316+ORcp3_321+qd[3]
    ACcp3_121 = qdd[1]+OMcp3_215*ORcp3_316+OMcp3_218*ORcp3_321+OMcp3_26*ORcp3_315-OMcp3_315*ORcp3_216-OMcp3_318*ORcp3_221-\
   OMcp3_36*ORcp3_215+OPcp3_215*RLcp3_316+OPcp3_218*RLcp3_321+OPcp3_26*RLcp3_315-OPcp3_315*RLcp3_216-OPcp3_318*RLcp3_221-\
   OPcp3_36*RLcp3_215
    ACcp3_221 = qdd[2]-OMcp3_115*ORcp3_316-OMcp3_118*ORcp3_321-OMcp3_16*ORcp3_315+OMcp3_315*ORcp3_116+OMcp3_318*ORcp3_121+\
   OMcp3_36*ORcp3_115-OPcp3_115*RLcp3_316-OPcp3_118*RLcp3_321-OPcp3_16*RLcp3_315+OPcp3_315*RLcp3_116+OPcp3_318*RLcp3_121+\
   OPcp3_36*RLcp3_115
    ACcp3_321 = qdd[3]+OMcp3_115*ORcp3_216+OMcp3_118*ORcp3_221+OMcp3_16*ORcp3_215-OMcp3_215*ORcp3_116-OMcp3_218*ORcp3_121-\
   OMcp3_26*ORcp3_115+OPcp3_115*RLcp3_216+OPcp3_118*RLcp3_221+OPcp3_16*RLcp3_215-OPcp3_215*RLcp3_116-OPcp3_218*RLcp3_121-\
   OPcp3_26*RLcp3_115
    OMcp3_122 = OMcp3_121+ROcp3_421*qd[22]
    OMcp3_222 = OMcp3_221+ROcp3_521*qd[22]
    OMcp3_322 = OMcp3_321+ROcp3_621*qd[22]
    OPcp3_122 = OPcp3_118+ROcp3_118*qdd[21]+ROcp3_421*qdd[22]+qd[21]*(OMcp3_218*ROcp3_318-OMcp3_318*ROcp3_218)+qd[22]*(\
   OMcp3_221*ROcp3_621-OMcp3_321*ROcp3_521)
    OPcp3_222 = OPcp3_218+ROcp3_218*qdd[21]+ROcp3_521*qdd[22]-qd[21]*(OMcp3_118*ROcp3_318-OMcp3_318*ROcp3_118)-qd[22]*(\
   OMcp3_121*ROcp3_621-OMcp3_321*ROcp3_421)
    OPcp3_322 = OPcp3_318+ROcp3_318*qdd[21]+ROcp3_621*qdd[22]+qd[21]*(OMcp3_118*ROcp3_218-OMcp3_218*ROcp3_118)+qd[22]*(\
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
 
# 
  elif(isens==5): 


# = = Block_1_0_0_5_0_1 = = 
 
# Sensor Kinematics 


    ROcp4_15 = C4*C5
    ROcp4_25 = S4*C5
    ROcp4_75 = C4*S5
    ROcp4_85 = S4*S5
    ROcp4_46 = ROcp4_75*S6-S4*C6
    ROcp4_56 = ROcp4_85*S6+C4*C6
    ROcp4_76 = ROcp4_75*C6+S4*S6
    ROcp4_86 = ROcp4_85*C6-C4*S6
    OMcp4_15 = -qd[5]*S4
    OMcp4_25 = qd[5]*C4
    OMcp4_16 = OMcp4_15+ROcp4_15*qd[6]
    OMcp4_26 = OMcp4_25+ROcp4_25*qd[6]
    OMcp4_36 = qd[4]-qd[6]*S5
    OPcp4_16 = ROcp4_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp4_25*S5+ROcp4_25*qd[4])
    OPcp4_26 = ROcp4_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp4_15*S5+ROcp4_15*qd[4])
    OPcp4_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_5_0_11 = = 
 
# Sensor Kinematics 


    ROcp4_429 = ROcp4_46*C29+ROcp4_76*S29
    ROcp4_529 = ROcp4_56*C29+ROcp4_86*S29
    ROcp4_629 = S29p6*C5
    ROcp4_729 = -(ROcp4_46*S29-ROcp4_76*C29)
    ROcp4_829 = -(ROcp4_56*S29-ROcp4_86*C29)
    ROcp4_929 = C29p6*C5
    ROcp4_130 = ROcp4_15*C30+ROcp4_429*S30
    ROcp4_230 = ROcp4_25*C30+ROcp4_529*S30
    ROcp4_330 = ROcp4_629*S30-C30*S5
    ROcp4_430 = -(ROcp4_15*S30-ROcp4_429*C30)
    ROcp4_530 = -(ROcp4_25*S30-ROcp4_529*C30)
    ROcp4_630 = ROcp4_629*C30+S30*S5
    ROcp4_431 = ROcp4_430*C31+ROcp4_729*S31
    ROcp4_531 = ROcp4_530*C31+ROcp4_829*S31
    ROcp4_631 = ROcp4_630*C31+ROcp4_929*S31
    ROcp4_731 = -(ROcp4_430*S31-ROcp4_729*C31)
    ROcp4_831 = -(ROcp4_530*S31-ROcp4_829*C31)
    ROcp4_931 = -(ROcp4_630*S31-ROcp4_929*C31)
    ROcp4_132 = ROcp4_130*C32-ROcp4_731*S32
    ROcp4_232 = ROcp4_230*C32-ROcp4_831*S32
    ROcp4_332 = ROcp4_330*C32-ROcp4_931*S32
    ROcp4_732 = ROcp4_130*S32+ROcp4_731*C32
    ROcp4_832 = ROcp4_230*S32+ROcp4_831*C32
    ROcp4_932 = ROcp4_330*S32+ROcp4_931*C32
    ROcp4_133 = ROcp4_132*C33+ROcp4_431*S33
    ROcp4_233 = ROcp4_232*C33+ROcp4_531*S33
    ROcp4_333 = ROcp4_332*C33+ROcp4_631*S33
    ROcp4_433 = -(ROcp4_132*S33-ROcp4_431*C33)
    ROcp4_533 = -(ROcp4_232*S33-ROcp4_531*C33)
    ROcp4_633 = -(ROcp4_332*S33-ROcp4_631*C33)
    RLcp4_129 = ROcp4_15*s.dpt[1,10]+ROcp4_46*s.dpt[2,10]
    RLcp4_229 = ROcp4_25*s.dpt[1,10]+ROcp4_56*s.dpt[2,10]
    RLcp4_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
    OMcp4_129 = OMcp4_16+ROcp4_15*qd[29]
    OMcp4_229 = OMcp4_26+ROcp4_25*qd[29]
    OMcp4_329 = OMcp4_36-qd[29]*S5
    ORcp4_129 = OMcp4_26*RLcp4_329-OMcp4_36*RLcp4_229
    ORcp4_229 = -(OMcp4_16*RLcp4_329-OMcp4_36*RLcp4_129)
    ORcp4_329 = OMcp4_16*RLcp4_229-OMcp4_26*RLcp4_129
    OMcp4_130 = OMcp4_129+ROcp4_729*qd[30]
    OMcp4_230 = OMcp4_229+ROcp4_829*qd[30]
    OMcp4_330 = OMcp4_329+ROcp4_929*qd[30]
    OPcp4_130 = OPcp4_16+ROcp4_15*qdd[29]+ROcp4_729*qdd[30]-qd[29]*(OMcp4_26*S5+OMcp4_36*ROcp4_25)+qd[30]*(OMcp4_229*\
   ROcp4_929-OMcp4_329*ROcp4_829)
    OPcp4_230 = OPcp4_26+ROcp4_25*qdd[29]+ROcp4_829*qdd[30]+qd[29]*(OMcp4_16*S5+OMcp4_36*ROcp4_15)-qd[30]*(OMcp4_129*\
   ROcp4_929-OMcp4_329*ROcp4_729)
    OPcp4_330 = OPcp4_36+ROcp4_929*qdd[30]-qdd[29]*S5+qd[29]*(OMcp4_16*ROcp4_25-OMcp4_26*ROcp4_15)+qd[30]*(OMcp4_129*\
   ROcp4_829-OMcp4_229*ROcp4_729)
    RLcp4_131 = ROcp4_430*s.dpt[2,35]
    RLcp4_231 = ROcp4_530*s.dpt[2,35]
    RLcp4_331 = ROcp4_630*s.dpt[2,35]
    OMcp4_131 = OMcp4_130+ROcp4_130*qd[31]
    OMcp4_231 = OMcp4_230+ROcp4_230*qd[31]
    OMcp4_331 = OMcp4_330+ROcp4_330*qd[31]
    ORcp4_131 = OMcp4_230*RLcp4_331-OMcp4_330*RLcp4_231
    ORcp4_231 = -(OMcp4_130*RLcp4_331-OMcp4_330*RLcp4_131)
    ORcp4_331 = OMcp4_130*RLcp4_231-OMcp4_230*RLcp4_131
    OMcp4_132 = OMcp4_131+ROcp4_431*qd[32]
    OMcp4_232 = OMcp4_231+ROcp4_531*qd[32]
    OMcp4_332 = OMcp4_331+ROcp4_631*qd[32]
    OMcp4_133 = OMcp4_132+ROcp4_732*qd[33]
    OMcp4_233 = OMcp4_232+ROcp4_832*qd[33]
    OMcp4_333 = OMcp4_332+ROcp4_932*qd[33]
    OPcp4_133 = OPcp4_130+ROcp4_130*qdd[31]+ROcp4_431*qdd[32]+ROcp4_732*qdd[33]+qd[31]*(OMcp4_230*ROcp4_330-OMcp4_330*\
   ROcp4_230)+qd[32]*(OMcp4_231*ROcp4_631-OMcp4_331*ROcp4_531)+qd[33]*(OMcp4_232*ROcp4_932-OMcp4_332*ROcp4_832)
    OPcp4_233 = OPcp4_230+ROcp4_230*qdd[31]+ROcp4_531*qdd[32]+ROcp4_832*qdd[33]-qd[31]*(OMcp4_130*ROcp4_330-OMcp4_330*\
   ROcp4_130)-qd[32]*(OMcp4_131*ROcp4_631-OMcp4_331*ROcp4_431)-qd[33]*(OMcp4_132*ROcp4_932-OMcp4_332*ROcp4_732)
    OPcp4_333 = OPcp4_330+ROcp4_330*qdd[31]+ROcp4_631*qdd[32]+ROcp4_932*qdd[33]+qd[31]*(OMcp4_130*ROcp4_230-OMcp4_230*\
   ROcp4_130)+qd[32]*(OMcp4_131*ROcp4_531-OMcp4_231*ROcp4_431)+qd[33]*(OMcp4_132*ROcp4_832-OMcp4_232*ROcp4_732)

# = = Block_1_0_0_5_0_13 = = 
 
# Sensor Kinematics 


    ROcp4_436 = ROcp4_433*C36+ROcp4_732*S36
    ROcp4_536 = ROcp4_533*C36+ROcp4_832*S36
    ROcp4_636 = ROcp4_633*C36+ROcp4_932*S36
    ROcp4_736 = -(ROcp4_433*S36-ROcp4_732*C36)
    ROcp4_836 = -(ROcp4_533*S36-ROcp4_832*C36)
    ROcp4_936 = -(ROcp4_633*S36-ROcp4_932*C36)
    ROcp4_137 = ROcp4_133*C37-ROcp4_736*S37
    ROcp4_237 = ROcp4_233*C37-ROcp4_836*S37
    ROcp4_337 = ROcp4_333*C37-ROcp4_936*S37
    ROcp4_737 = ROcp4_133*S37+ROcp4_736*C37
    ROcp4_837 = ROcp4_233*S37+ROcp4_836*C37
    ROcp4_937 = ROcp4_333*S37+ROcp4_936*C37
    RLcp4_136 = ROcp4_433*s.dpt[2,37]+ROcp4_732*s.dpt[3,37]
    RLcp4_236 = ROcp4_533*s.dpt[2,37]+ROcp4_832*s.dpt[3,37]
    RLcp4_336 = ROcp4_633*s.dpt[2,37]+ROcp4_932*s.dpt[3,37]
    POcp4_136 = RLcp4_129+RLcp4_131+RLcp4_136+q[1]
    POcp4_236 = RLcp4_229+RLcp4_231+RLcp4_236+q[2]
    POcp4_336 = RLcp4_329+RLcp4_331+RLcp4_336+q[3]
    OMcp4_136 = OMcp4_133+ROcp4_133*qd[36]
    OMcp4_236 = OMcp4_233+ROcp4_233*qd[36]
    OMcp4_336 = OMcp4_333+ROcp4_333*qd[36]
    ORcp4_136 = OMcp4_233*RLcp4_336-OMcp4_333*RLcp4_236
    ORcp4_236 = -(OMcp4_133*RLcp4_336-OMcp4_333*RLcp4_136)
    ORcp4_336 = OMcp4_133*RLcp4_236-OMcp4_233*RLcp4_136
    VIcp4_136 = ORcp4_129+ORcp4_131+ORcp4_136+qd[1]
    VIcp4_236 = ORcp4_229+ORcp4_231+ORcp4_236+qd[2]
    VIcp4_336 = ORcp4_329+ORcp4_331+ORcp4_336+qd[3]
    ACcp4_136 = qdd[1]+OMcp4_230*ORcp4_331+OMcp4_233*ORcp4_336+OMcp4_26*ORcp4_329-OMcp4_330*ORcp4_231-OMcp4_333*ORcp4_236-\
   OMcp4_36*ORcp4_229+OPcp4_230*RLcp4_331+OPcp4_233*RLcp4_336+OPcp4_26*RLcp4_329-OPcp4_330*RLcp4_231-OPcp4_333*RLcp4_236-\
   OPcp4_36*RLcp4_229
    ACcp4_236 = qdd[2]-OMcp4_130*ORcp4_331-OMcp4_133*ORcp4_336-OMcp4_16*ORcp4_329+OMcp4_330*ORcp4_131+OMcp4_333*ORcp4_136+\
   OMcp4_36*ORcp4_129-OPcp4_130*RLcp4_331-OPcp4_133*RLcp4_336-OPcp4_16*RLcp4_329+OPcp4_330*RLcp4_131+OPcp4_333*RLcp4_136+\
   OPcp4_36*RLcp4_129
    ACcp4_336 = qdd[3]+OMcp4_130*ORcp4_231+OMcp4_133*ORcp4_236+OMcp4_16*ORcp4_229-OMcp4_230*ORcp4_131-OMcp4_233*ORcp4_136-\
   OMcp4_26*ORcp4_129+OPcp4_130*RLcp4_231+OPcp4_133*RLcp4_236+OPcp4_16*RLcp4_229-OPcp4_230*RLcp4_131-OPcp4_233*RLcp4_136-\
   OPcp4_26*RLcp4_129
    OMcp4_137 = OMcp4_136+ROcp4_436*qd[37]
    OMcp4_237 = OMcp4_236+ROcp4_536*qd[37]
    OMcp4_337 = OMcp4_336+ROcp4_636*qd[37]
    OPcp4_137 = OPcp4_133+ROcp4_133*qdd[36]+ROcp4_436*qdd[37]+qd[36]*(OMcp4_233*ROcp4_333-OMcp4_333*ROcp4_233)+qd[37]*(\
   OMcp4_236*ROcp4_636-OMcp4_336*ROcp4_536)
    OPcp4_237 = OPcp4_233+ROcp4_233*qdd[36]+ROcp4_536*qdd[37]-qd[36]*(OMcp4_133*ROcp4_333-OMcp4_333*ROcp4_133)-qd[37]*(\
   OMcp4_136*ROcp4_636-OMcp4_336*ROcp4_436)
    OPcp4_337 = OPcp4_333+ROcp4_333*qdd[36]+ROcp4_636*qdd[37]+qd[36]*(OMcp4_133*ROcp4_233-OMcp4_233*ROcp4_133)+qd[37]*(\
   OMcp4_136*ROcp4_536-OMcp4_236*ROcp4_436)

# = = Block_1_0_0_5_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp4_136
    sens.P[2] = POcp4_236
    sens.P[3] = POcp4_336
    sens.R[1,1] = ROcp4_137
    sens.R[1,2] = ROcp4_237
    sens.R[1,3] = ROcp4_337
    sens.R[2,1] = ROcp4_436
    sens.R[2,2] = ROcp4_536
    sens.R[2,3] = ROcp4_636
    sens.R[3,1] = ROcp4_737
    sens.R[3,2] = ROcp4_837
    sens.R[3,3] = ROcp4_937
    sens.V[1] = VIcp4_136
    sens.V[2] = VIcp4_236
    sens.V[3] = VIcp4_336
    sens.OM[1] = OMcp4_137
    sens.OM[2] = OMcp4_237
    sens.OM[3] = OMcp4_337
    sens.A[1] = ACcp4_136
    sens.A[2] = ACcp4_236
    sens.A[3] = ACcp4_336
    sens.OMP[1] = OPcp4_137
    sens.OMP[2] = OPcp4_237
    sens.OMP[3] = OPcp4_337
 
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
    ROcp5_76 = ROcp5_75*C6+S4*S6
    ROcp5_86 = ROcp5_85*C6-C4*S6
    OMcp5_15 = -qd[5]*S4
    OMcp5_25 = qd[5]*C4
    OMcp5_16 = OMcp5_15+ROcp5_15*qd[6]
    OMcp5_26 = OMcp5_25+ROcp5_25*qd[6]
    OMcp5_36 = qd[4]-qd[6]*S5
    OPcp5_16 = ROcp5_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp5_25*S5+ROcp5_25*qd[4])
    OPcp5_26 = ROcp5_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp5_15*S5+ROcp5_15*qd[4])
    OPcp5_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_6_0_15 = = 
 
# Sensor Kinematics 


    ROcp5_440 = ROcp5_46*C40+ROcp5_76*S40
    ROcp5_540 = ROcp5_56*C40+ROcp5_86*S40
    ROcp5_640 = S40p6*C5
    ROcp5_740 = -(ROcp5_46*S40-ROcp5_76*C40)
    ROcp5_840 = -(ROcp5_56*S40-ROcp5_86*C40)
    ROcp5_940 = C40p6*C5
    ROcp5_141 = ROcp5_15*C41+ROcp5_440*S41
    ROcp5_241 = ROcp5_25*C41+ROcp5_540*S41
    ROcp5_341 = ROcp5_640*S41-C41*S5
    ROcp5_441 = -(ROcp5_15*S41-ROcp5_440*C41)
    ROcp5_541 = -(ROcp5_25*S41-ROcp5_540*C41)
    ROcp5_641 = ROcp5_640*C41+S41*S5
    ROcp5_442 = ROcp5_441*C42+ROcp5_740*S42
    ROcp5_542 = ROcp5_541*C42+ROcp5_840*S42
    ROcp5_642 = ROcp5_641*C42+ROcp5_940*S42
    ROcp5_742 = -(ROcp5_441*S42-ROcp5_740*C42)
    ROcp5_842 = -(ROcp5_541*S42-ROcp5_840*C42)
    ROcp5_942 = -(ROcp5_641*S42-ROcp5_940*C42)
    ROcp5_143 = ROcp5_141*C43-ROcp5_742*S43
    ROcp5_243 = ROcp5_241*C43-ROcp5_842*S43
    ROcp5_343 = ROcp5_341*C43-ROcp5_942*S43
    ROcp5_743 = ROcp5_141*S43+ROcp5_742*C43
    ROcp5_843 = ROcp5_241*S43+ROcp5_842*C43
    ROcp5_943 = ROcp5_341*S43+ROcp5_942*C43
    ROcp5_144 = ROcp5_143*C44+ROcp5_442*S44
    ROcp5_244 = ROcp5_243*C44+ROcp5_542*S44
    ROcp5_344 = ROcp5_343*C44+ROcp5_642*S44
    ROcp5_444 = -(ROcp5_143*S44-ROcp5_442*C44)
    ROcp5_544 = -(ROcp5_243*S44-ROcp5_542*C44)
    ROcp5_644 = -(ROcp5_343*S44-ROcp5_642*C44)
    RLcp5_140 = ROcp5_15*s.dpt[1,12]+ROcp5_46*s.dpt[2,12]
    RLcp5_240 = ROcp5_25*s.dpt[1,12]+ROcp5_56*s.dpt[2,12]
    RLcp5_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
    OMcp5_140 = OMcp5_16+ROcp5_15*qd[40]
    OMcp5_240 = OMcp5_26+ROcp5_25*qd[40]
    OMcp5_340 = OMcp5_36-qd[40]*S5
    ORcp5_140 = OMcp5_26*RLcp5_340-OMcp5_36*RLcp5_240
    ORcp5_240 = -(OMcp5_16*RLcp5_340-OMcp5_36*RLcp5_140)
    ORcp5_340 = OMcp5_16*RLcp5_240-OMcp5_26*RLcp5_140
    OMcp5_141 = OMcp5_140+ROcp5_740*qd[41]
    OMcp5_241 = OMcp5_240+ROcp5_840*qd[41]
    OMcp5_341 = OMcp5_340+ROcp5_940*qd[41]
    OPcp5_141 = OPcp5_16+ROcp5_15*qdd[40]+ROcp5_740*qdd[41]-qd[40]*(OMcp5_26*S5+OMcp5_36*ROcp5_25)+qd[41]*(OMcp5_240*\
   ROcp5_940-OMcp5_340*ROcp5_840)
    OPcp5_241 = OPcp5_26+ROcp5_25*qdd[40]+ROcp5_840*qdd[41]+qd[40]*(OMcp5_16*S5+OMcp5_36*ROcp5_15)-qd[41]*(OMcp5_140*\
   ROcp5_940-OMcp5_340*ROcp5_740)
    OPcp5_341 = OPcp5_36+ROcp5_940*qdd[41]-qdd[40]*S5+qd[40]*(OMcp5_16*ROcp5_25-OMcp5_26*ROcp5_15)+qd[41]*(OMcp5_140*\
   ROcp5_840-OMcp5_240*ROcp5_740)
    RLcp5_142 = ROcp5_441*s.dpt[2,44]
    RLcp5_242 = ROcp5_541*s.dpt[2,44]
    RLcp5_342 = ROcp5_641*s.dpt[2,44]
    OMcp5_142 = OMcp5_141+ROcp5_141*qd[42]
    OMcp5_242 = OMcp5_241+ROcp5_241*qd[42]
    OMcp5_342 = OMcp5_341+ROcp5_341*qd[42]
    ORcp5_142 = OMcp5_241*RLcp5_342-OMcp5_341*RLcp5_242
    ORcp5_242 = -(OMcp5_141*RLcp5_342-OMcp5_341*RLcp5_142)
    ORcp5_342 = OMcp5_141*RLcp5_242-OMcp5_241*RLcp5_142
    OMcp5_143 = OMcp5_142+ROcp5_442*qd[43]
    OMcp5_243 = OMcp5_242+ROcp5_542*qd[43]
    OMcp5_343 = OMcp5_342+ROcp5_642*qd[43]
    OMcp5_144 = OMcp5_143+ROcp5_743*qd[44]
    OMcp5_244 = OMcp5_243+ROcp5_843*qd[44]
    OMcp5_344 = OMcp5_343+ROcp5_943*qd[44]
    OPcp5_144 = OPcp5_141+ROcp5_141*qdd[42]+ROcp5_442*qdd[43]+ROcp5_743*qdd[44]+qd[42]*(OMcp5_241*ROcp5_341-OMcp5_341*\
   ROcp5_241)+qd[43]*(OMcp5_242*ROcp5_642-OMcp5_342*ROcp5_542)+qd[44]*(OMcp5_243*ROcp5_943-OMcp5_343*ROcp5_843)
    OPcp5_244 = OPcp5_241+ROcp5_241*qdd[42]+ROcp5_542*qdd[43]+ROcp5_843*qdd[44]-qd[42]*(OMcp5_141*ROcp5_341-OMcp5_341*\
   ROcp5_141)-qd[43]*(OMcp5_142*ROcp5_642-OMcp5_342*ROcp5_442)-qd[44]*(OMcp5_143*ROcp5_943-OMcp5_343*ROcp5_743)
    OPcp5_344 = OPcp5_341+ROcp5_341*qdd[42]+ROcp5_642*qdd[43]+ROcp5_943*qdd[44]+qd[42]*(OMcp5_141*ROcp5_241-OMcp5_241*\
   ROcp5_141)+qd[43]*(OMcp5_142*ROcp5_542-OMcp5_242*ROcp5_442)+qd[44]*(OMcp5_143*ROcp5_843-OMcp5_243*ROcp5_743)

# = = Block_1_0_0_6_0_17 = = 
 
# Sensor Kinematics 


    ROcp5_447 = ROcp5_444*C47+ROcp5_743*S47
    ROcp5_547 = ROcp5_544*C47+ROcp5_843*S47
    ROcp5_647 = ROcp5_644*C47+ROcp5_943*S47
    ROcp5_747 = -(ROcp5_444*S47-ROcp5_743*C47)
    ROcp5_847 = -(ROcp5_544*S47-ROcp5_843*C47)
    ROcp5_947 = -(ROcp5_644*S47-ROcp5_943*C47)
    ROcp5_148 = ROcp5_144*C48-ROcp5_747*S48
    ROcp5_248 = ROcp5_244*C48-ROcp5_847*S48
    ROcp5_348 = ROcp5_344*C48-ROcp5_947*S48
    ROcp5_748 = ROcp5_144*S48+ROcp5_747*C48
    ROcp5_848 = ROcp5_244*S48+ROcp5_847*C48
    ROcp5_948 = ROcp5_344*S48+ROcp5_947*C48
    RLcp5_147 = ROcp5_444*s.dpt[2,48]+ROcp5_743*s.dpt[3,48]
    RLcp5_247 = ROcp5_544*s.dpt[2,48]+ROcp5_843*s.dpt[3,48]
    RLcp5_347 = ROcp5_644*s.dpt[2,48]+ROcp5_943*s.dpt[3,48]
    POcp5_147 = RLcp5_140+RLcp5_142+RLcp5_147+q[1]
    POcp5_247 = RLcp5_240+RLcp5_242+RLcp5_247+q[2]
    POcp5_347 = RLcp5_340+RLcp5_342+RLcp5_347+q[3]
    OMcp5_147 = OMcp5_144+ROcp5_144*qd[47]
    OMcp5_247 = OMcp5_244+ROcp5_244*qd[47]
    OMcp5_347 = OMcp5_344+ROcp5_344*qd[47]
    ORcp5_147 = OMcp5_244*RLcp5_347-OMcp5_344*RLcp5_247
    ORcp5_247 = -(OMcp5_144*RLcp5_347-OMcp5_344*RLcp5_147)
    ORcp5_347 = OMcp5_144*RLcp5_247-OMcp5_244*RLcp5_147
    VIcp5_147 = ORcp5_140+ORcp5_142+ORcp5_147+qd[1]
    VIcp5_247 = ORcp5_240+ORcp5_242+ORcp5_247+qd[2]
    VIcp5_347 = ORcp5_340+ORcp5_342+ORcp5_347+qd[3]
    ACcp5_147 = qdd[1]+OMcp5_241*ORcp5_342+OMcp5_244*ORcp5_347+OMcp5_26*ORcp5_340-OMcp5_341*ORcp5_242-OMcp5_344*ORcp5_247-\
   OMcp5_36*ORcp5_240+OPcp5_241*RLcp5_342+OPcp5_244*RLcp5_347+OPcp5_26*RLcp5_340-OPcp5_341*RLcp5_242-OPcp5_344*RLcp5_247-\
   OPcp5_36*RLcp5_240
    ACcp5_247 = qdd[2]-OMcp5_141*ORcp5_342-OMcp5_144*ORcp5_347-OMcp5_16*ORcp5_340+OMcp5_341*ORcp5_142+OMcp5_344*ORcp5_147+\
   OMcp5_36*ORcp5_140-OPcp5_141*RLcp5_342-OPcp5_144*RLcp5_347-OPcp5_16*RLcp5_340+OPcp5_341*RLcp5_142+OPcp5_344*RLcp5_147+\
   OPcp5_36*RLcp5_140
    ACcp5_347 = qdd[3]+OMcp5_141*ORcp5_242+OMcp5_144*ORcp5_247+OMcp5_16*ORcp5_240-OMcp5_241*ORcp5_142-OMcp5_244*ORcp5_147-\
   OMcp5_26*ORcp5_140+OPcp5_141*RLcp5_242+OPcp5_144*RLcp5_247+OPcp5_16*RLcp5_240-OPcp5_241*RLcp5_142-OPcp5_244*RLcp5_147-\
   OPcp5_26*RLcp5_140
    OMcp5_148 = OMcp5_147+ROcp5_447*qd[48]
    OMcp5_248 = OMcp5_247+ROcp5_547*qd[48]
    OMcp5_348 = OMcp5_347+ROcp5_647*qd[48]
    OPcp5_148 = OPcp5_144+ROcp5_144*qdd[47]+ROcp5_447*qdd[48]+qd[47]*(OMcp5_244*ROcp5_344-OMcp5_344*ROcp5_244)+qd[48]*(\
   OMcp5_247*ROcp5_647-OMcp5_347*ROcp5_547)
    OPcp5_248 = OPcp5_244+ROcp5_244*qdd[47]+ROcp5_547*qdd[48]-qd[47]*(OMcp5_144*ROcp5_344-OMcp5_344*ROcp5_144)-qd[48]*(\
   OMcp5_147*ROcp5_647-OMcp5_347*ROcp5_447)
    OPcp5_348 = OPcp5_344+ROcp5_344*qdd[47]+ROcp5_647*qdd[48]+qd[47]*(OMcp5_144*ROcp5_244-OMcp5_244*ROcp5_144)+qd[48]*(\
   OMcp5_147*ROcp5_547-OMcp5_247*ROcp5_447)

# = = Block_1_0_0_6_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp5_147
    sens.P[2] = POcp5_247
    sens.P[3] = POcp5_347
    sens.R[1,1] = ROcp5_148
    sens.R[1,2] = ROcp5_248
    sens.R[1,3] = ROcp5_348
    sens.R[2,1] = ROcp5_447
    sens.R[2,2] = ROcp5_547
    sens.R[2,3] = ROcp5_647
    sens.R[3,1] = ROcp5_748
    sens.R[3,2] = ROcp5_848
    sens.R[3,3] = ROcp5_948
    sens.V[1] = VIcp5_147
    sens.V[2] = VIcp5_247
    sens.V[3] = VIcp5_347
    sens.OM[1] = OMcp5_148
    sens.OM[2] = OMcp5_248
    sens.OM[3] = OMcp5_348
    sens.A[1] = ACcp5_147
    sens.A[2] = ACcp5_247
    sens.A[3] = ACcp5_347
    sens.OMP[1] = OPcp5_148
    sens.OMP[2] = OPcp5_248
    sens.OMP[3] = OPcp5_348



# ====== END Task 1 ====== 

  

