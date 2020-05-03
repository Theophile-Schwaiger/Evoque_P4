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
#	==> Function : F19 : External Forces
#	==> Flops complexity : 2464
#
#	==> Generation Time :  0.050 seconds
#	==> Post-Processing :  0.040 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def extforces(frc,trq,s,tsim):
  
  q = s.q
  qd = s.qd
  qdd = s.qdd
  frc = s.frc
  trq = s.trq
  
  PxF1=np.zeros(4)
  RxF1=np.zeros((4,4))
  VxF1=np.zeros(4)
  OMxF1=np.zeros(4)
  AxF1=np.zeros(4)
  OMPxF1=np.zeros(4)
  PxF2=np.zeros(4)
  RxF2=np.zeros((4,4))
  VxF2=np.zeros(4)
  OMxF2=np.zeros(4)
  AxF2=np.zeros(4)
  OMPxF2=np.zeros(4)
  PxF3=np.zeros(4)
  RxF3=np.zeros((4,4))
  VxF3=np.zeros(4)
  OMxF3=np.zeros(4)
  AxF3=np.zeros(4)
  OMPxF3=np.zeros(4)
  PxF4=np.zeros(4)
  RxF4=np.zeros((4,4))
  VxF4=np.zeros(4)
  OMxF4=np.zeros(4)
  AxF4=np.zeros(4)
  OMPxF4=np.zeros(4)
  PxF5=np.zeros(4)
  RxF5=np.zeros((4,4))
  VxF5=np.zeros(4)
  OMxF5=np.zeros(4)
  AxF5=np.zeros(4)
  OMPxF5=np.zeros(4)
  PxF6=np.zeros(4)
  RxF6=np.zeros((4,4))
  VxF6=np.zeros(4)
  OMxF6=np.zeros(4)
  AxF6=np.zeros(4)
  OMPxF6=np.zeros(4)

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

# = = Block_0_0_1_1_0_1 = = 
 
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
  OMcp0_16 = OMcp0_15+qd[6]*ROcp0_15
  OMcp0_26 = OMcp0_25+qd[6]*ROcp0_25
  OMcp0_36 = qd[4]-qd[6]*S5
  OPcp0_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp0_25+OMcp0_25*S5)+qdd[5]*S4-qdd[6]*ROcp0_15)
  OPcp0_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp0_15+OMcp0_15*S5)-qdd[5]*C4-qdd[6]*ROcp0_25)
  OPcp0_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5
  RLcp0_196 = ROcp0_15*s.dpt[1,16]+ROcp0_76*s.dpt[3,16]
  RLcp0_296 = ROcp0_25*s.dpt[1,16]+ROcp0_86*s.dpt[3,16]
  RLcp0_396 = ROcp0_96*s.dpt[3,16]-s.dpt[1,16]*S5
  ORcp0_196 = OMcp0_26*RLcp0_396-OMcp0_36*RLcp0_296
  ORcp0_296 = -(OMcp0_16*RLcp0_396-OMcp0_36*RLcp0_196)
  ORcp0_396 = OMcp0_16*RLcp0_296-OMcp0_26*RLcp0_196
  PxF1[1] = q[1]+RLcp0_196
  PxF1[2] = q[2]+RLcp0_296
  PxF1[3] = q[3]+RLcp0_396
  RxF1[1,1] = ROcp0_15
  RxF1[1,2] = ROcp0_25
  RxF1[1,3] = -S5
  RxF1[2,1] = ROcp0_46
  RxF1[2,2] = ROcp0_56
  RxF1[2,3] = ROcp0_66
  RxF1[3,1] = ROcp0_76
  RxF1[3,2] = ROcp0_86
  RxF1[3,3] = ROcp0_96
  VxF1[1] = qd[1]+ORcp0_196
  VxF1[2] = qd[2]+ORcp0_296
  VxF1[3] = qd[3]+ORcp0_396
  OMxF1[1] = OMcp0_16
  OMxF1[2] = OMcp0_26
  OMxF1[3] = OMcp0_36
  AxF1[1] = qdd[1]+OMcp0_26*ORcp0_396-OMcp0_36*ORcp0_296+OPcp0_26*RLcp0_396-OPcp0_36*RLcp0_296
  AxF1[2] = qdd[2]-OMcp0_16*ORcp0_396+OMcp0_36*ORcp0_196-OPcp0_16*RLcp0_396+OPcp0_36*RLcp0_196
  AxF1[3] = qdd[3]+OMcp0_16*ORcp0_296-OMcp0_26*ORcp0_196+OPcp0_16*RLcp0_296-OPcp0_26*RLcp0_196
  OMPxF1[1] = OPcp0_16
  OMPxF1[2] = OPcp0_26
  OMPxF1[3] = OPcp0_36
 
# Sensor Forces Computation 

  SWr1 = s.user_ExtForces(PxF1,RxF1,VxF1,OMxF1,AxF1,OMPxF1,s,tsim,1)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc11 = ROcp0_15*SWr1[1]+ROcp0_25*SWr1[2]-SWr1[3]*S5
  xfrc21 = ROcp0_46*SWr1[1]+ROcp0_56*SWr1[2]+ROcp0_66*SWr1[3]
  xfrc31 = ROcp0_76*SWr1[1]+ROcp0_86*SWr1[2]+ROcp0_96*SWr1[3]
  s.frc[1,6] = s.frc[1,6]+xfrc11
  s.frc[2,6] = s.frc[2,6]+xfrc21
  s.frc[3,6] = s.frc[3,6]+xfrc31
  xtrq11 = ROcp0_15*SWr1[4]+ROcp0_25*SWr1[5]-SWr1[6]*S5
  xtrq21 = ROcp0_46*SWr1[4]+ROcp0_56*SWr1[5]+ROcp0_66*SWr1[6]
  xtrq31 = ROcp0_76*SWr1[4]+ROcp0_86*SWr1[5]+ROcp0_96*SWr1[6]
  s.trq[1,6] = s.trq[1,6]+xtrq11-xfrc21*(SWr1[9]-s.l[3,6])+xfrc31*SWr1[8]
  s.trq[2,6] = s.trq[2,6]+xtrq21+xfrc11*(SWr1[9]-s.l[3,6])-xfrc31*SWr1[7]
  s.trq[3,6] = s.trq[3,6]+xtrq31-xfrc11*SWr1[8]+xfrc21*SWr1[7]

# = = Block_0_0_1_2_0_1 = = 
 
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
  OMcp1_16 = OMcp1_15+qd[6]*ROcp1_15
  OMcp1_26 = OMcp1_25+qd[6]*ROcp1_25
  OMcp1_36 = qd[4]-qd[6]*S5
  OPcp1_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp1_25+OMcp1_25*S5)+qdd[5]*S4-qdd[6]*ROcp1_15)
  OPcp1_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp1_15+OMcp1_15*S5)-qdd[5]*C4-qdd[6]*ROcp1_25)
  OPcp1_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5
  RLcp1_197 = ROcp1_15*s.dpt[1,17]+ROcp1_76*s.dpt[3,17]
  RLcp1_297 = ROcp1_25*s.dpt[1,17]+ROcp1_86*s.dpt[3,17]
  RLcp1_397 = ROcp1_96*s.dpt[3,17]-s.dpt[1,17]*S5
  ORcp1_197 = OMcp1_26*RLcp1_397-OMcp1_36*RLcp1_297
  ORcp1_297 = -(OMcp1_16*RLcp1_397-OMcp1_36*RLcp1_197)
  ORcp1_397 = OMcp1_16*RLcp1_297-OMcp1_26*RLcp1_197
  PxF2[1] = q[1]+RLcp1_197
  PxF2[2] = q[2]+RLcp1_297
  PxF2[3] = q[3]+RLcp1_397
  RxF2[1,1] = ROcp1_15
  RxF2[1,2] = ROcp1_25
  RxF2[1,3] = -S5
  RxF2[2,1] = ROcp1_46
  RxF2[2,2] = ROcp1_56
  RxF2[2,3] = ROcp1_66
  RxF2[3,1] = ROcp1_76
  RxF2[3,2] = ROcp1_86
  RxF2[3,3] = ROcp1_96
  VxF2[1] = qd[1]+ORcp1_197
  VxF2[2] = qd[2]+ORcp1_297
  VxF2[3] = qd[3]+ORcp1_397
  OMxF2[1] = OMcp1_16
  OMxF2[2] = OMcp1_26
  OMxF2[3] = OMcp1_36
  AxF2[1] = qdd[1]+OMcp1_26*ORcp1_397-OMcp1_36*ORcp1_297+OPcp1_26*RLcp1_397-OPcp1_36*RLcp1_297
  AxF2[2] = qdd[2]-OMcp1_16*ORcp1_397+OMcp1_36*ORcp1_197-OPcp1_16*RLcp1_397+OPcp1_36*RLcp1_197
  AxF2[3] = qdd[3]+OMcp1_16*ORcp1_297-OMcp1_26*ORcp1_197+OPcp1_16*RLcp1_297-OPcp1_26*RLcp1_197
  OMPxF2[1] = OPcp1_16
  OMPxF2[2] = OPcp1_26
  OMPxF2[3] = OPcp1_36
 
# Sensor Forces Computation 

  SWr2 = s.user_ExtForces(PxF2,RxF2,VxF2,OMxF2,AxF2,OMPxF2,s,tsim,2)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc12 = ROcp1_15*SWr2[1]+ROcp1_25*SWr2[2]-SWr2[3]*S5
  xfrc22 = ROcp1_46*SWr2[1]+ROcp1_56*SWr2[2]+ROcp1_66*SWr2[3]
  xfrc32 = ROcp1_76*SWr2[1]+ROcp1_86*SWr2[2]+ROcp1_96*SWr2[3]
  frc[1,6] = s.frc[1,6]+xfrc12
  frc[2,6] = s.frc[2,6]+xfrc22
  frc[3,6] = s.frc[3,6]+xfrc32
  xtrq12 = ROcp1_15*SWr2[4]+ROcp1_25*SWr2[5]-SWr2[6]*S5
  xtrq22 = ROcp1_46*SWr2[4]+ROcp1_56*SWr2[5]+ROcp1_66*SWr2[6]
  xtrq32 = ROcp1_76*SWr2[4]+ROcp1_86*SWr2[5]+ROcp1_96*SWr2[6]
  trq[1,6] = s.trq[1,6]+xtrq12-xfrc22*(SWr2[9]-s.l[3,6])+xfrc32*SWr2[8]
  trq[2,6] = s.trq[2,6]+xtrq22+xfrc12*(SWr2[9]-s.l[3,6])-xfrc32*SWr2[7]
  trq[3,6] = s.trq[3,6]+xtrq32-xfrc12*SWr2[8]+xfrc22*SWr2[7]

# = = Block_0_0_1_3_0_1 = = 
 
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
  OMcp2_16 = OMcp2_15+qd[6]*ROcp2_15
  OMcp2_26 = OMcp2_25+qd[6]*ROcp2_25
  OMcp2_36 = qd[4]-qd[6]*S5
  OPcp2_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp2_25+OMcp2_25*S5)+qdd[5]*S4-qdd[6]*ROcp2_15)
  OPcp2_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp2_15+OMcp2_15*S5)-qdd[5]*C4-qdd[6]*ROcp2_25)
  OPcp2_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5

# = = Block_0_0_1_3_0_2 = = 
 
# Trigonometric Variables  

  S6p7 = C6*S7+S6*C7
  C6p7 = C6*C7-S6*S7
 
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
  OMcp2_17 = OMcp2_16+qd[7]*ROcp2_15
  OMcp2_27 = OMcp2_26+qd[7]*ROcp2_25
  OMcp2_37 = OMcp2_36-qd[7]*S5
  ORcp2_17 = OMcp2_26*RLcp2_37-OMcp2_36*RLcp2_27
  ORcp2_27 = -(OMcp2_16*RLcp2_37-OMcp2_36*RLcp2_17)
  ORcp2_37 = OMcp2_16*RLcp2_27-OMcp2_26*RLcp2_17
  OPcp2_17 = OPcp2_16-qd[7]*(OMcp2_26*S5+OMcp2_36*ROcp2_25)+qdd[7]*ROcp2_15
  OPcp2_27 = OPcp2_26+qd[7]*(OMcp2_16*S5+OMcp2_36*ROcp2_15)+qdd[7]*ROcp2_25
  OPcp2_37 = OPcp2_36+qd[7]*(OMcp2_16*ROcp2_25-OMcp2_26*ROcp2_15)-qdd[7]*S5
  RLcp2_18 = ROcp2_47*s.dpt[2,18]
  RLcp2_28 = ROcp2_57*s.dpt[2,18]
  RLcp2_38 = ROcp2_67*s.dpt[2,18]
  OMcp2_18 = OMcp2_17+qd[8]*ROcp2_77
  OMcp2_28 = OMcp2_27+qd[8]*ROcp2_87
  OMcp2_38 = OMcp2_37+qd[8]*ROcp2_97
  ORcp2_18 = OMcp2_27*RLcp2_38-OMcp2_37*RLcp2_28
  ORcp2_28 = -(OMcp2_17*RLcp2_38-OMcp2_37*RLcp2_18)
  ORcp2_38 = OMcp2_17*RLcp2_28-OMcp2_27*RLcp2_18
  OMcp2_19 = OMcp2_18+qd[9]*ROcp2_18
  OMcp2_29 = OMcp2_28+qd[9]*ROcp2_28
  OMcp2_39 = OMcp2_38+qd[9]*ROcp2_38
  OMcp2_110 = OMcp2_19+qd[10]*ROcp2_49
  OMcp2_210 = OMcp2_29+qd[10]*ROcp2_59
  OMcp2_310 = OMcp2_39+qd[10]*ROcp2_69
  OPcp2_110 = OPcp2_17+qd[10]*(OMcp2_29*ROcp2_69-OMcp2_39*ROcp2_59)+qd[8]*(OMcp2_27*ROcp2_97-OMcp2_37*ROcp2_87)+qd[9]*(\
   OMcp2_28*ROcp2_38-OMcp2_38*ROcp2_28)+qdd[10]*ROcp2_49+qdd[8]*ROcp2_77+qdd[9]*ROcp2_18
  OPcp2_210 = OPcp2_27-qd[10]*(OMcp2_19*ROcp2_69-OMcp2_39*ROcp2_49)-qd[8]*(OMcp2_17*ROcp2_97-OMcp2_37*ROcp2_77)-qd[9]*(\
   OMcp2_18*ROcp2_38-OMcp2_38*ROcp2_18)+qdd[10]*ROcp2_59+qdd[8]*ROcp2_87+qdd[9]*ROcp2_28
  OPcp2_310 = OPcp2_37+qd[10]*(OMcp2_19*ROcp2_59-OMcp2_29*ROcp2_49)+qd[8]*(OMcp2_17*ROcp2_87-OMcp2_27*ROcp2_77)+qd[9]*(\
   OMcp2_18*ROcp2_28-OMcp2_28*ROcp2_18)+qdd[10]*ROcp2_69+qdd[8]*ROcp2_97+qdd[9]*ROcp2_38

# = = Block_0_0_1_3_0_4 = = 
 
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
  OMcp2_113 = OMcp2_110+qd[13]*ROcp2_110
  OMcp2_213 = OMcp2_210+qd[13]*ROcp2_210
  OMcp2_313 = OMcp2_310+qd[13]*ROcp2_310
  ORcp2_113 = OMcp2_210*RLcp2_313-OMcp2_310*RLcp2_213
  ORcp2_213 = -(OMcp2_110*RLcp2_313-OMcp2_310*RLcp2_113)
  ORcp2_313 = OMcp2_110*RLcp2_213-OMcp2_210*RLcp2_113
  PxF3[1] = q[1]+RLcp2_113+RLcp2_17+RLcp2_18
  PxF3[2] = q[2]+RLcp2_213+RLcp2_27+RLcp2_28
  PxF3[3] = q[3]+RLcp2_313+RLcp2_37+RLcp2_38
  RxF3[1,1] = ROcp2_114
  RxF3[1,2] = ROcp2_214
  RxF3[1,3] = ROcp2_314
  RxF3[2,1] = ROcp2_413
  RxF3[2,2] = ROcp2_513
  RxF3[2,3] = ROcp2_613
  RxF3[3,1] = ROcp2_714
  RxF3[3,2] = ROcp2_814
  RxF3[3,3] = ROcp2_914
  VxF3[1] = qd[1]+ORcp2_113+ORcp2_17+ORcp2_18
  VxF3[2] = qd[2]+ORcp2_213+ORcp2_27+ORcp2_28
  VxF3[3] = qd[3]+ORcp2_313+ORcp2_37+ORcp2_38
  OMxF3[1] = OMcp2_113+qd[14]*ROcp2_413
  OMxF3[2] = OMcp2_213+qd[14]*ROcp2_513
  OMxF3[3] = OMcp2_313+qd[14]*ROcp2_613
  AxF3[1] = qdd[1]+OMcp2_210*ORcp2_313+OMcp2_26*ORcp2_37+OMcp2_27*ORcp2_38-OMcp2_310*ORcp2_213-OMcp2_36*ORcp2_27-\
   OMcp2_37*ORcp2_28+OPcp2_210*RLcp2_313+OPcp2_26*RLcp2_37+OPcp2_27*RLcp2_38-OPcp2_310*RLcp2_213-OPcp2_36*RLcp2_27-OPcp2_37*\
   RLcp2_28
  AxF3[2] = qdd[2]-OMcp2_110*ORcp2_313-OMcp2_16*ORcp2_37-OMcp2_17*ORcp2_38+OMcp2_310*ORcp2_113+OMcp2_36*ORcp2_17+\
   OMcp2_37*ORcp2_18-OPcp2_110*RLcp2_313-OPcp2_16*RLcp2_37-OPcp2_17*RLcp2_38+OPcp2_310*RLcp2_113+OPcp2_36*RLcp2_17+OPcp2_37*\
   RLcp2_18
  AxF3[3] = qdd[3]+OMcp2_110*ORcp2_213+OMcp2_16*ORcp2_27+OMcp2_17*ORcp2_28-OMcp2_210*ORcp2_113-OMcp2_26*ORcp2_17-\
   OMcp2_27*ORcp2_18+OPcp2_110*RLcp2_213+OPcp2_16*RLcp2_27+OPcp2_17*RLcp2_28-OPcp2_210*RLcp2_113-OPcp2_26*RLcp2_17-OPcp2_27*\
   RLcp2_18
  OMPxF3[1] = OPcp2_110+qd[13]*(OMcp2_210*ROcp2_310-OMcp2_310*ROcp2_210)+qd[14]*(OMcp2_213*ROcp2_613-OMcp2_313*ROcp2_513\
   )+qdd[13]*ROcp2_110+qdd[14]*ROcp2_413
  OMPxF3[2] = OPcp2_210-qd[13]*(OMcp2_110*ROcp2_310-OMcp2_310*ROcp2_110)-qd[14]*(OMcp2_113*ROcp2_613-OMcp2_313*ROcp2_413\
   )+qdd[13]*ROcp2_210+qdd[14]*ROcp2_513
  OMPxF3[3] = OPcp2_310+qd[13]*(OMcp2_110*ROcp2_210-OMcp2_210*ROcp2_110)+qd[14]*(OMcp2_113*ROcp2_513-OMcp2_213*ROcp2_413\
   )+qdd[13]*ROcp2_310+qdd[14]*ROcp2_613
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc13 = ROcp2_114*SWr3[1]+ROcp2_214*SWr3[2]+ROcp2_314*SWr3[3]
  xfrc23 = ROcp2_413*SWr3[1]+ROcp2_513*SWr3[2]+ROcp2_613*SWr3[3]
  xfrc33 = ROcp2_714*SWr3[1]+ROcp2_814*SWr3[2]+ROcp2_914*SWr3[3]
  frc[1,14] = s.frc[1,14]+xfrc13
  frc[2,14] = s.frc[2,14]+xfrc23
  frc[3,14] = s.frc[3,14]+xfrc33
  xtrq13 = ROcp2_114*SWr3[4]+ROcp2_214*SWr3[5]+ROcp2_314*SWr3[6]
  xtrq23 = ROcp2_413*SWr3[4]+ROcp2_513*SWr3[5]+ROcp2_613*SWr3[6]
  xtrq33 = ROcp2_714*SWr3[4]+ROcp2_814*SWr3[5]+ROcp2_914*SWr3[6]
  trq[1,14] = s.trq[1,14]+xtrq13-xfrc23*SWr3[9]+xfrc33*SWr3[8]
  trq[2,14] = s.trq[2,14]+xtrq23+xfrc13*SWr3[9]-xfrc33*SWr3[7]
  trq[3,14] = s.trq[3,14]+xtrq33-xfrc13*SWr3[8]+xfrc23*SWr3[7]

# = = Block_0_0_1_4_0_1 = = 
 
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
  OMcp3_16 = OMcp3_15+qd[6]*ROcp3_15
  OMcp3_26 = OMcp3_25+qd[6]*ROcp3_25
  OMcp3_36 = qd[4]-qd[6]*S5
  OPcp3_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp3_25+OMcp3_25*S5)+qdd[5]*S4-qdd[6]*ROcp3_15)
  OPcp3_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp3_15+OMcp3_15*S5)-qdd[5]*C4-qdd[6]*ROcp3_25)
  OPcp3_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5

# = = Block_0_0_1_4_0_5 = = 
 
# Trigonometric Variables  

  S15p6 = C15*S6+S15*C6
  C15p6 = C15*C6-S15*S6
 
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
  OMcp3_115 = OMcp3_16+qd[15]*ROcp3_15
  OMcp3_215 = OMcp3_26+qd[15]*ROcp3_25
  OMcp3_315 = OMcp3_36-qd[15]*S5
  ORcp3_115 = OMcp3_26*RLcp3_315-OMcp3_36*RLcp3_215
  ORcp3_215 = -(OMcp3_16*RLcp3_315-OMcp3_36*RLcp3_115)
  ORcp3_315 = OMcp3_16*RLcp3_215-OMcp3_26*RLcp3_115
  OPcp3_115 = OPcp3_16-qd[15]*(OMcp3_26*S5+OMcp3_36*ROcp3_25)+qdd[15]*ROcp3_15
  OPcp3_215 = OPcp3_26+qd[15]*(OMcp3_16*S5+OMcp3_36*ROcp3_15)+qdd[15]*ROcp3_25
  OPcp3_315 = OPcp3_36+qd[15]*(OMcp3_16*ROcp3_25-OMcp3_26*ROcp3_15)-qdd[15]*S5
  RLcp3_116 = ROcp3_415*s.dpt[2,25]
  RLcp3_216 = ROcp3_515*s.dpt[2,25]
  RLcp3_316 = ROcp3_615*s.dpt[2,25]
  OMcp3_116 = OMcp3_115+qd[16]*ROcp3_715
  OMcp3_216 = OMcp3_215+qd[16]*ROcp3_815
  OMcp3_316 = OMcp3_315+qd[16]*ROcp3_915
  ORcp3_116 = OMcp3_215*RLcp3_316-OMcp3_315*RLcp3_216
  ORcp3_216 = -(OMcp3_115*RLcp3_316-OMcp3_315*RLcp3_116)
  ORcp3_316 = OMcp3_115*RLcp3_216-OMcp3_215*RLcp3_116
  OMcp3_117 = OMcp3_116+qd[17]*ROcp3_116
  OMcp3_217 = OMcp3_216+qd[17]*ROcp3_216
  OMcp3_317 = OMcp3_316+qd[17]*ROcp3_316
  OMcp3_118 = OMcp3_117+qd[18]*ROcp3_417
  OMcp3_218 = OMcp3_217+qd[18]*ROcp3_517
  OMcp3_318 = OMcp3_317+qd[18]*ROcp3_617
  OPcp3_118 = OPcp3_115+qd[16]*(OMcp3_215*ROcp3_915-OMcp3_315*ROcp3_815)+qd[17]*(OMcp3_216*ROcp3_316-OMcp3_316*ROcp3_216\
   )+qd[18]*(OMcp3_217*ROcp3_617-OMcp3_317*ROcp3_517)+qdd[16]*ROcp3_715+qdd[17]*ROcp3_116+qdd[18]*ROcp3_417
  OPcp3_218 = OPcp3_215-qd[16]*(OMcp3_115*ROcp3_915-OMcp3_315*ROcp3_715)-qd[17]*(OMcp3_116*ROcp3_316-OMcp3_316*ROcp3_116\
   )-qd[18]*(OMcp3_117*ROcp3_617-OMcp3_317*ROcp3_417)+qdd[16]*ROcp3_815+qdd[17]*ROcp3_216+qdd[18]*ROcp3_517
  OPcp3_318 = OPcp3_315+qd[16]*(OMcp3_115*ROcp3_815-OMcp3_215*ROcp3_715)+qd[17]*(OMcp3_116*ROcp3_216-OMcp3_216*ROcp3_116\
   )+qd[18]*(OMcp3_117*ROcp3_517-OMcp3_217*ROcp3_417)+qdd[16]*ROcp3_915+qdd[17]*ROcp3_316+qdd[18]*ROcp3_617

# = = Block_0_0_1_4_0_7 = = 
 
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
  OMcp3_121 = OMcp3_118+qd[21]*ROcp3_118
  OMcp3_221 = OMcp3_218+qd[21]*ROcp3_218
  OMcp3_321 = OMcp3_318+qd[21]*ROcp3_318
  ORcp3_121 = OMcp3_218*RLcp3_321-OMcp3_318*RLcp3_221
  ORcp3_221 = -(OMcp3_118*RLcp3_321-OMcp3_318*RLcp3_121)
  ORcp3_321 = OMcp3_118*RLcp3_221-OMcp3_218*RLcp3_121
  PxF4[1] = q[1]+RLcp3_115+RLcp3_116+RLcp3_121
  PxF4[2] = q[2]+RLcp3_215+RLcp3_216+RLcp3_221
  PxF4[3] = q[3]+RLcp3_315+RLcp3_316+RLcp3_321
  RxF4[1,1] = ROcp3_122
  RxF4[1,2] = ROcp3_222
  RxF4[1,3] = ROcp3_322
  RxF4[2,1] = ROcp3_421
  RxF4[2,2] = ROcp3_521
  RxF4[2,3] = ROcp3_621
  RxF4[3,1] = ROcp3_722
  RxF4[3,2] = ROcp3_822
  RxF4[3,3] = ROcp3_922
  VxF4[1] = qd[1]+ORcp3_115+ORcp3_116+ORcp3_121
  VxF4[2] = qd[2]+ORcp3_215+ORcp3_216+ORcp3_221
  VxF4[3] = qd[3]+ORcp3_315+ORcp3_316+ORcp3_321
  OMxF4[1] = OMcp3_121+qd[22]*ROcp3_421
  OMxF4[2] = OMcp3_221+qd[22]*ROcp3_521
  OMxF4[3] = OMcp3_321+qd[22]*ROcp3_621
  AxF4[1] = qdd[1]+OMcp3_215*ORcp3_316+OMcp3_218*ORcp3_321+OMcp3_26*ORcp3_315-OMcp3_315*ORcp3_216-OMcp3_318*ORcp3_221-\
   OMcp3_36*ORcp3_215+OPcp3_215*RLcp3_316+OPcp3_218*RLcp3_321+OPcp3_26*RLcp3_315-OPcp3_315*RLcp3_216-OPcp3_318*RLcp3_221-\
   OPcp3_36*RLcp3_215
  AxF4[2] = qdd[2]-OMcp3_115*ORcp3_316-OMcp3_118*ORcp3_321-OMcp3_16*ORcp3_315+OMcp3_315*ORcp3_116+OMcp3_318*ORcp3_121+\
   OMcp3_36*ORcp3_115-OPcp3_115*RLcp3_316-OPcp3_118*RLcp3_321-OPcp3_16*RLcp3_315+OPcp3_315*RLcp3_116+OPcp3_318*RLcp3_121+\
   OPcp3_36*RLcp3_115
  AxF4[3] = qdd[3]+OMcp3_115*ORcp3_216+OMcp3_118*ORcp3_221+OMcp3_16*ORcp3_215-OMcp3_215*ORcp3_116-OMcp3_218*ORcp3_121-\
   OMcp3_26*ORcp3_115+OPcp3_115*RLcp3_216+OPcp3_118*RLcp3_221+OPcp3_16*RLcp3_215-OPcp3_215*RLcp3_116-OPcp3_218*RLcp3_121-\
   OPcp3_26*RLcp3_115
  OMPxF4[1] = OPcp3_118+qd[21]*(OMcp3_218*ROcp3_318-OMcp3_318*ROcp3_218)+qd[22]*(OMcp3_221*ROcp3_621-OMcp3_321*ROcp3_521\
   )+qdd[21]*ROcp3_118+qdd[22]*ROcp3_421
  OMPxF4[2] = OPcp3_218-qd[21]*(OMcp3_118*ROcp3_318-OMcp3_318*ROcp3_118)-qd[22]*(OMcp3_121*ROcp3_621-OMcp3_321*ROcp3_421\
   )+qdd[21]*ROcp3_218+qdd[22]*ROcp3_521
  OMPxF4[3] = OPcp3_318+qd[21]*(OMcp3_118*ROcp3_218-OMcp3_218*ROcp3_118)+qd[22]*(OMcp3_121*ROcp3_521-OMcp3_221*ROcp3_421\
   )+qdd[21]*ROcp3_318+qdd[22]*ROcp3_621
 
# Sensor Forces Computation 

  SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc14 = ROcp3_122*SWr4[1]+ROcp3_222*SWr4[2]+ROcp3_322*SWr4[3]
  xfrc24 = ROcp3_421*SWr4[1]+ROcp3_521*SWr4[2]+ROcp3_621*SWr4[3]
  xfrc34 = ROcp3_722*SWr4[1]+ROcp3_822*SWr4[2]+ROcp3_922*SWr4[3]
  frc[1,22] = s.frc[1,22]+xfrc14
  frc[2,22] = s.frc[2,22]+xfrc24
  frc[3,22] = s.frc[3,22]+xfrc34
  xtrq14 = ROcp3_122*SWr4[4]+ROcp3_222*SWr4[5]+ROcp3_322*SWr4[6]
  xtrq24 = ROcp3_421*SWr4[4]+ROcp3_521*SWr4[5]+ROcp3_621*SWr4[6]
  xtrq34 = ROcp3_722*SWr4[4]+ROcp3_822*SWr4[5]+ROcp3_922*SWr4[6]
  trq[1,22] = s.trq[1,22]+xtrq14-xfrc24*SWr4[9]+xfrc34*SWr4[8]
  trq[2,22] = s.trq[2,22]+xtrq24+xfrc14*SWr4[9]-xfrc34*SWr4[7]
  trq[3,22] = s.trq[3,22]+xtrq34-xfrc14*SWr4[8]+xfrc24*SWr4[7]

# = = Block_0_0_1_5_0_1 = = 
 
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
  OMcp4_16 = OMcp4_15+qd[6]*ROcp4_15
  OMcp4_26 = OMcp4_25+qd[6]*ROcp4_25
  OMcp4_36 = qd[4]-qd[6]*S5
  OPcp4_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp4_25+OMcp4_25*S5)+qdd[5]*S4-qdd[6]*ROcp4_15)
  OPcp4_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp4_15+OMcp4_15*S5)-qdd[5]*C4-qdd[6]*ROcp4_25)
  OPcp4_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5

# = = Block_0_0_1_5_0_11 = = 
 
# Trigonometric Variables  

  S29p6 = C29*S6+S29*C6
  C29p6 = C29*C6-S29*S6
 
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
  OMcp4_129 = OMcp4_16+qd[29]*ROcp4_15
  OMcp4_229 = OMcp4_26+qd[29]*ROcp4_25
  OMcp4_329 = OMcp4_36-qd[29]*S5
  ORcp4_129 = OMcp4_26*RLcp4_329-OMcp4_36*RLcp4_229
  ORcp4_229 = -(OMcp4_16*RLcp4_329-OMcp4_36*RLcp4_129)
  ORcp4_329 = OMcp4_16*RLcp4_229-OMcp4_26*RLcp4_129
  OMcp4_130 = OMcp4_129+qd[30]*ROcp4_729
  OMcp4_230 = OMcp4_229+qd[30]*ROcp4_829
  OMcp4_330 = OMcp4_329+qd[30]*ROcp4_929
  OPcp4_130 = OPcp4_16-qd[29]*(OMcp4_26*S5+OMcp4_36*ROcp4_25)+qd[30]*(OMcp4_229*ROcp4_929-OMcp4_329*ROcp4_829)+qdd[29]*\
   ROcp4_15+qdd[30]*ROcp4_729
  OPcp4_230 = OPcp4_26+qd[29]*(OMcp4_16*S5+OMcp4_36*ROcp4_15)-qd[30]*(OMcp4_129*ROcp4_929-OMcp4_329*ROcp4_729)+qdd[29]*\
   ROcp4_25+qdd[30]*ROcp4_829
  OPcp4_330 = OPcp4_36+qd[29]*(OMcp4_16*ROcp4_25-OMcp4_26*ROcp4_15)+qd[30]*(OMcp4_129*ROcp4_829-OMcp4_229*ROcp4_729)-\
   qdd[29]*S5+qdd[30]*ROcp4_929
  RLcp4_131 = ROcp4_430*s.dpt[2,35]
  RLcp4_231 = ROcp4_530*s.dpt[2,35]
  RLcp4_331 = ROcp4_630*s.dpt[2,35]
  OMcp4_131 = OMcp4_130+qd[31]*ROcp4_130
  OMcp4_231 = OMcp4_230+qd[31]*ROcp4_230
  OMcp4_331 = OMcp4_330+qd[31]*ROcp4_330
  ORcp4_131 = OMcp4_230*RLcp4_331-OMcp4_330*RLcp4_231
  ORcp4_231 = -(OMcp4_130*RLcp4_331-OMcp4_330*RLcp4_131)
  ORcp4_331 = OMcp4_130*RLcp4_231-OMcp4_230*RLcp4_131
  OMcp4_132 = OMcp4_131+qd[32]*ROcp4_431
  OMcp4_232 = OMcp4_231+qd[32]*ROcp4_531
  OMcp4_332 = OMcp4_331+qd[32]*ROcp4_631
  OMcp4_133 = OMcp4_132+qd[33]*ROcp4_732
  OMcp4_233 = OMcp4_232+qd[33]*ROcp4_832
  OMcp4_333 = OMcp4_332+qd[33]*ROcp4_932
  OPcp4_133 = OPcp4_130+qd[31]*(OMcp4_230*ROcp4_330-OMcp4_330*ROcp4_230)+qd[32]*(OMcp4_231*ROcp4_631-OMcp4_331*ROcp4_531\
   )+qd[33]*(OMcp4_232*ROcp4_932-OMcp4_332*ROcp4_832)+qdd[31]*ROcp4_130+qdd[32]*ROcp4_431+qdd[33]*ROcp4_732
  OPcp4_233 = OPcp4_230-qd[31]*(OMcp4_130*ROcp4_330-OMcp4_330*ROcp4_130)-qd[32]*(OMcp4_131*ROcp4_631-OMcp4_331*ROcp4_431\
   )-qd[33]*(OMcp4_132*ROcp4_932-OMcp4_332*ROcp4_732)+qdd[31]*ROcp4_230+qdd[32]*ROcp4_531+qdd[33]*ROcp4_832
  OPcp4_333 = OPcp4_330+qd[31]*(OMcp4_130*ROcp4_230-OMcp4_230*ROcp4_130)+qd[32]*(OMcp4_131*ROcp4_531-OMcp4_231*ROcp4_431\
   )+qd[33]*(OMcp4_132*ROcp4_832-OMcp4_232*ROcp4_732)+qdd[31]*ROcp4_330+qdd[32]*ROcp4_631+qdd[33]*ROcp4_932

# = = Block_0_0_1_5_0_13 = = 
 
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
  OMcp4_136 = OMcp4_133+qd[36]*ROcp4_133
  OMcp4_236 = OMcp4_233+qd[36]*ROcp4_233
  OMcp4_336 = OMcp4_333+qd[36]*ROcp4_333
  ORcp4_136 = OMcp4_233*RLcp4_336-OMcp4_333*RLcp4_236
  ORcp4_236 = -(OMcp4_133*RLcp4_336-OMcp4_333*RLcp4_136)
  ORcp4_336 = OMcp4_133*RLcp4_236-OMcp4_233*RLcp4_136
  PxF5[1] = q[1]+RLcp4_129+RLcp4_131+RLcp4_136
  PxF5[2] = q[2]+RLcp4_229+RLcp4_231+RLcp4_236
  PxF5[3] = q[3]+RLcp4_329+RLcp4_331+RLcp4_336
  RxF5[1,1] = ROcp4_137
  RxF5[1,2] = ROcp4_237
  RxF5[1,3] = ROcp4_337
  RxF5[2,1] = ROcp4_436
  RxF5[2,2] = ROcp4_536
  RxF5[2,3] = ROcp4_636
  RxF5[3,1] = ROcp4_737
  RxF5[3,2] = ROcp4_837
  RxF5[3,3] = ROcp4_937
  VxF5[1] = qd[1]+ORcp4_129+ORcp4_131+ORcp4_136
  VxF5[2] = qd[2]+ORcp4_229+ORcp4_231+ORcp4_236
  VxF5[3] = qd[3]+ORcp4_329+ORcp4_331+ORcp4_336
  OMxF5[1] = OMcp4_136+qd[37]*ROcp4_436
  OMxF5[2] = OMcp4_236+qd[37]*ROcp4_536
  OMxF5[3] = OMcp4_336+qd[37]*ROcp4_636
  AxF5[1] = qdd[1]+OMcp4_230*ORcp4_331+OMcp4_233*ORcp4_336+OMcp4_26*ORcp4_329-OMcp4_330*ORcp4_231-OMcp4_333*ORcp4_236-\
   OMcp4_36*ORcp4_229+OPcp4_230*RLcp4_331+OPcp4_233*RLcp4_336+OPcp4_26*RLcp4_329-OPcp4_330*RLcp4_231-OPcp4_333*RLcp4_236-\
   OPcp4_36*RLcp4_229
  AxF5[2] = qdd[2]-OMcp4_130*ORcp4_331-OMcp4_133*ORcp4_336-OMcp4_16*ORcp4_329+OMcp4_330*ORcp4_131+OMcp4_333*ORcp4_136+\
   OMcp4_36*ORcp4_129-OPcp4_130*RLcp4_331-OPcp4_133*RLcp4_336-OPcp4_16*RLcp4_329+OPcp4_330*RLcp4_131+OPcp4_333*RLcp4_136+\
   OPcp4_36*RLcp4_129
  AxF5[3] = qdd[3]+OMcp4_130*ORcp4_231+OMcp4_133*ORcp4_236+OMcp4_16*ORcp4_229-OMcp4_230*ORcp4_131-OMcp4_233*ORcp4_136-\
   OMcp4_26*ORcp4_129+OPcp4_130*RLcp4_231+OPcp4_133*RLcp4_236+OPcp4_16*RLcp4_229-OPcp4_230*RLcp4_131-OPcp4_233*RLcp4_136-\
   OPcp4_26*RLcp4_129
  OMPxF5[1] = OPcp4_133+qd[36]*(OMcp4_233*ROcp4_333-OMcp4_333*ROcp4_233)+qd[37]*(OMcp4_236*ROcp4_636-OMcp4_336*ROcp4_536\
   )+qdd[36]*ROcp4_133+qdd[37]*ROcp4_436
  OMPxF5[2] = OPcp4_233-qd[36]*(OMcp4_133*ROcp4_333-OMcp4_333*ROcp4_133)-qd[37]*(OMcp4_136*ROcp4_636-OMcp4_336*ROcp4_436\
   )+qdd[36]*ROcp4_233+qdd[37]*ROcp4_536
  OMPxF5[3] = OPcp4_333+qd[36]*(OMcp4_133*ROcp4_233-OMcp4_233*ROcp4_133)+qd[37]*(OMcp4_136*ROcp4_536-OMcp4_236*ROcp4_436\
   )+qdd[36]*ROcp4_333+qdd[37]*ROcp4_636
 
# Sensor Forces Computation 

  SWr5 = s.user_ExtForces(PxF5,RxF5,VxF5,OMxF5,AxF5,OMPxF5,s,tsim,5)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc15 = ROcp4_137*SWr5[1]+ROcp4_237*SWr5[2]+ROcp4_337*SWr5[3]
  xfrc25 = ROcp4_436*SWr5[1]+ROcp4_536*SWr5[2]+ROcp4_636*SWr5[3]
  xfrc35 = ROcp4_737*SWr5[1]+ROcp4_837*SWr5[2]+ROcp4_937*SWr5[3]
  frc[1,37] = s.frc[1,37]+xfrc15
  frc[2,37] = s.frc[2,37]+xfrc25
  frc[3,37] = s.frc[3,37]+xfrc35
  xtrq15 = ROcp4_137*SWr5[4]+ROcp4_237*SWr5[5]+ROcp4_337*SWr5[6]
  xtrq25 = ROcp4_436*SWr5[4]+ROcp4_536*SWr5[5]+ROcp4_636*SWr5[6]
  xtrq35 = ROcp4_737*SWr5[4]+ROcp4_837*SWr5[5]+ROcp4_937*SWr5[6]
  trq[1,37] = s.trq[1,37]+xtrq15-xfrc25*SWr5[9]+xfrc35*SWr5[8]
  trq[2,37] = s.trq[2,37]+xtrq25+xfrc15*SWr5[9]-xfrc35*SWr5[7]
  trq[3,37] = s.trq[3,37]+xtrq35-xfrc15*SWr5[8]+xfrc25*SWr5[7]

# = = Block_0_0_1_6_0_1 = = 
 
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
  OMcp5_16 = OMcp5_15+qd[6]*ROcp5_15
  OMcp5_26 = OMcp5_25+qd[6]*ROcp5_25
  OMcp5_36 = qd[4]-qd[6]*S5
  OPcp5_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp5_25+OMcp5_25*S5)+qdd[5]*S4-qdd[6]*ROcp5_15)
  OPcp5_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp5_15+OMcp5_15*S5)-qdd[5]*C4-qdd[6]*ROcp5_25)
  OPcp5_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5

# = = Block_0_0_1_6_0_15 = = 
 
# Trigonometric Variables  

  S40p6 = C40*S6+S40*C6
  C40p6 = C40*C6-S40*S6
 
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
  OMcp5_140 = OMcp5_16+qd[40]*ROcp5_15
  OMcp5_240 = OMcp5_26+qd[40]*ROcp5_25
  OMcp5_340 = OMcp5_36-qd[40]*S5
  ORcp5_140 = OMcp5_26*RLcp5_340-OMcp5_36*RLcp5_240
  ORcp5_240 = -(OMcp5_16*RLcp5_340-OMcp5_36*RLcp5_140)
  ORcp5_340 = OMcp5_16*RLcp5_240-OMcp5_26*RLcp5_140
  OMcp5_141 = OMcp5_140+qd[41]*ROcp5_740
  OMcp5_241 = OMcp5_240+qd[41]*ROcp5_840
  OMcp5_341 = OMcp5_340+qd[41]*ROcp5_940
  OPcp5_141 = OPcp5_16-qd[40]*(OMcp5_26*S5+OMcp5_36*ROcp5_25)+qd[41]*(OMcp5_240*ROcp5_940-OMcp5_340*ROcp5_840)+qdd[40]*\
   ROcp5_15+qdd[41]*ROcp5_740
  OPcp5_241 = OPcp5_26+qd[40]*(OMcp5_16*S5+OMcp5_36*ROcp5_15)-qd[41]*(OMcp5_140*ROcp5_940-OMcp5_340*ROcp5_740)+qdd[40]*\
   ROcp5_25+qdd[41]*ROcp5_840
  OPcp5_341 = OPcp5_36+qd[40]*(OMcp5_16*ROcp5_25-OMcp5_26*ROcp5_15)+qd[41]*(OMcp5_140*ROcp5_840-OMcp5_240*ROcp5_740)-\
   qdd[40]*S5+qdd[41]*ROcp5_940
  RLcp5_142 = ROcp5_441*s.dpt[2,44]
  RLcp5_242 = ROcp5_541*s.dpt[2,44]
  RLcp5_342 = ROcp5_641*s.dpt[2,44]
  OMcp5_142 = OMcp5_141+qd[42]*ROcp5_141
  OMcp5_242 = OMcp5_241+qd[42]*ROcp5_241
  OMcp5_342 = OMcp5_341+qd[42]*ROcp5_341
  ORcp5_142 = OMcp5_241*RLcp5_342-OMcp5_341*RLcp5_242
  ORcp5_242 = -(OMcp5_141*RLcp5_342-OMcp5_341*RLcp5_142)
  ORcp5_342 = OMcp5_141*RLcp5_242-OMcp5_241*RLcp5_142
  OMcp5_143 = OMcp5_142+qd[43]*ROcp5_442
  OMcp5_243 = OMcp5_242+qd[43]*ROcp5_542
  OMcp5_343 = OMcp5_342+qd[43]*ROcp5_642
  OMcp5_144 = OMcp5_143+qd[44]*ROcp5_743
  OMcp5_244 = OMcp5_243+qd[44]*ROcp5_843
  OMcp5_344 = OMcp5_343+qd[44]*ROcp5_943
  OPcp5_144 = OPcp5_141+qd[42]*(OMcp5_241*ROcp5_341-OMcp5_341*ROcp5_241)+qd[43]*(OMcp5_242*ROcp5_642-OMcp5_342*ROcp5_542\
   )+qd[44]*(OMcp5_243*ROcp5_943-OMcp5_343*ROcp5_843)+qdd[42]*ROcp5_141+qdd[43]*ROcp5_442+qdd[44]*ROcp5_743
  OPcp5_244 = OPcp5_241-qd[42]*(OMcp5_141*ROcp5_341-OMcp5_341*ROcp5_141)-qd[43]*(OMcp5_142*ROcp5_642-OMcp5_342*ROcp5_442\
   )-qd[44]*(OMcp5_143*ROcp5_943-OMcp5_343*ROcp5_743)+qdd[42]*ROcp5_241+qdd[43]*ROcp5_542+qdd[44]*ROcp5_843
  OPcp5_344 = OPcp5_341+qd[42]*(OMcp5_141*ROcp5_241-OMcp5_241*ROcp5_141)+qd[43]*(OMcp5_142*ROcp5_542-OMcp5_242*ROcp5_442\
   )+qd[44]*(OMcp5_143*ROcp5_843-OMcp5_243*ROcp5_743)+qdd[42]*ROcp5_341+qdd[43]*ROcp5_642+qdd[44]*ROcp5_943

# = = Block_0_0_1_6_0_17 = = 
 
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
  OMcp5_147 = OMcp5_144+qd[47]*ROcp5_144
  OMcp5_247 = OMcp5_244+qd[47]*ROcp5_244
  OMcp5_347 = OMcp5_344+qd[47]*ROcp5_344
  ORcp5_147 = OMcp5_244*RLcp5_347-OMcp5_344*RLcp5_247
  ORcp5_247 = -(OMcp5_144*RLcp5_347-OMcp5_344*RLcp5_147)
  ORcp5_347 = OMcp5_144*RLcp5_247-OMcp5_244*RLcp5_147
  PxF6[1] = q[1]+RLcp5_140+RLcp5_142+RLcp5_147
  PxF6[2] = q[2]+RLcp5_240+RLcp5_242+RLcp5_247
  PxF6[3] = q[3]+RLcp5_340+RLcp5_342+RLcp5_347
  RxF6[1,1] = ROcp5_148
  RxF6[1,2] = ROcp5_248
  RxF6[1,3] = ROcp5_348
  RxF6[2,1] = ROcp5_447
  RxF6[2,2] = ROcp5_547
  RxF6[2,3] = ROcp5_647
  RxF6[3,1] = ROcp5_748
  RxF6[3,2] = ROcp5_848
  RxF6[3,3] = ROcp5_948
  VxF6[1] = qd[1]+ORcp5_140+ORcp5_142+ORcp5_147
  VxF6[2] = qd[2]+ORcp5_240+ORcp5_242+ORcp5_247
  VxF6[3] = qd[3]+ORcp5_340+ORcp5_342+ORcp5_347
  OMxF6[1] = OMcp5_147+qd[48]*ROcp5_447
  OMxF6[2] = OMcp5_247+qd[48]*ROcp5_547
  OMxF6[3] = OMcp5_347+qd[48]*ROcp5_647
  AxF6[1] = qdd[1]+OMcp5_241*ORcp5_342+OMcp5_244*ORcp5_347+OMcp5_26*ORcp5_340-OMcp5_341*ORcp5_242-OMcp5_344*ORcp5_247-\
   OMcp5_36*ORcp5_240+OPcp5_241*RLcp5_342+OPcp5_244*RLcp5_347+OPcp5_26*RLcp5_340-OPcp5_341*RLcp5_242-OPcp5_344*RLcp5_247-\
   OPcp5_36*RLcp5_240
  AxF6[2] = qdd[2]-OMcp5_141*ORcp5_342-OMcp5_144*ORcp5_347-OMcp5_16*ORcp5_340+OMcp5_341*ORcp5_142+OMcp5_344*ORcp5_147+\
   OMcp5_36*ORcp5_140-OPcp5_141*RLcp5_342-OPcp5_144*RLcp5_347-OPcp5_16*RLcp5_340+OPcp5_341*RLcp5_142+OPcp5_344*RLcp5_147+\
   OPcp5_36*RLcp5_140
  AxF6[3] = qdd[3]+OMcp5_141*ORcp5_242+OMcp5_144*ORcp5_247+OMcp5_16*ORcp5_240-OMcp5_241*ORcp5_142-OMcp5_244*ORcp5_147-\
   OMcp5_26*ORcp5_140+OPcp5_141*RLcp5_242+OPcp5_144*RLcp5_247+OPcp5_16*RLcp5_240-OPcp5_241*RLcp5_142-OPcp5_244*RLcp5_147-\
   OPcp5_26*RLcp5_140
  OMPxF6[1] = OPcp5_144+qd[47]*(OMcp5_244*ROcp5_344-OMcp5_344*ROcp5_244)+qd[48]*(OMcp5_247*ROcp5_647-OMcp5_347*ROcp5_547\
   )+qdd[47]*ROcp5_144+qdd[48]*ROcp5_447
  OMPxF6[2] = OPcp5_244-qd[47]*(OMcp5_144*ROcp5_344-OMcp5_344*ROcp5_144)-qd[48]*(OMcp5_147*ROcp5_647-OMcp5_347*ROcp5_447\
   )+qdd[47]*ROcp5_244+qdd[48]*ROcp5_547
  OMPxF6[3] = OPcp5_344+qd[47]*(OMcp5_144*ROcp5_244-OMcp5_244*ROcp5_144)+qd[48]*(OMcp5_147*ROcp5_547-OMcp5_247*ROcp5_447\
   )+qdd[47]*ROcp5_344+qdd[48]*ROcp5_647
 
# Sensor Forces Computation 

  SWr6 = s.user_ExtForces(PxF6,RxF6,VxF6,OMxF6,AxF6,OMPxF6,s,tsim,6)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc16 = ROcp5_148*SWr6[1]+ROcp5_248*SWr6[2]+ROcp5_348*SWr6[3]
  xfrc26 = ROcp5_447*SWr6[1]+ROcp5_547*SWr6[2]+ROcp5_647*SWr6[3]
  xfrc36 = ROcp5_748*SWr6[1]+ROcp5_848*SWr6[2]+ROcp5_948*SWr6[3]
  frc[1,48] = s.frc[1,48]+xfrc16
  frc[2,48] = s.frc[2,48]+xfrc26
  frc[3,48] = s.frc[3,48]+xfrc36
  xtrq16 = ROcp5_148*SWr6[4]+ROcp5_248*SWr6[5]+ROcp5_348*SWr6[6]
  xtrq26 = ROcp5_447*SWr6[4]+ROcp5_547*SWr6[5]+ROcp5_647*SWr6[6]
  xtrq36 = ROcp5_748*SWr6[4]+ROcp5_848*SWr6[5]+ROcp5_948*SWr6[6]
  trq[1,48] = s.trq[1,48]+xtrq16-xfrc26*SWr6[9]+xfrc36*SWr6[8]
  trq[2,48] = s.trq[2,48]+xtrq26+xfrc16*SWr6[9]-xfrc36*SWr6[7]
  trq[3,48] = s.trq[3,48]+xtrq36-xfrc16*SWr6[8]+xfrc26*SWr6[7]

# = = Block_0_0_1_6_1_0 = = 
 
# Symbolic Outputs  

  frc[1,7] = s.frc[1,7]
  frc[2,7] = s.frc[2,7]
  frc[3,7] = s.frc[3,7]
  frc[1,10] = s.frc[1,10]
  frc[2,10] = s.frc[2,10]
  frc[3,10] = s.frc[3,10]
  frc[1,12] = s.frc[1,12]
  frc[2,12] = s.frc[2,12]
  frc[3,12] = s.frc[3,12]
  frc[1,15] = s.frc[1,15]
  frc[2,15] = s.frc[2,15]
  frc[3,15] = s.frc[3,15]
  frc[1,18] = s.frc[1,18]
  frc[2,18] = s.frc[2,18]
  frc[3,18] = s.frc[3,18]
  frc[1,20] = s.frc[1,20]
  frc[2,20] = s.frc[2,20]
  frc[3,20] = s.frc[3,20]
  frc[1,24] = s.frc[1,24]
  frc[2,24] = s.frc[2,24]
  frc[3,24] = s.frc[3,24]
  frc[1,26] = s.frc[1,26]
  frc[2,26] = s.frc[2,26]
  frc[3,26] = s.frc[3,26]
  frc[1,28] = s.frc[1,28]
  frc[2,28] = s.frc[2,28]
  frc[3,28] = s.frc[3,28]
  frc[1,30] = s.frc[1,30]
  frc[2,30] = s.frc[2,30]
  frc[3,30] = s.frc[3,30]
  frc[1,33] = s.frc[1,33]
  frc[2,33] = s.frc[2,33]
  frc[3,33] = s.frc[3,33]
  frc[1,35] = s.frc[1,35]
  frc[2,35] = s.frc[2,35]
  frc[3,35] = s.frc[3,35]
  frc[1,39] = s.frc[1,39]
  frc[2,39] = s.frc[2,39]
  frc[3,39] = s.frc[3,39]
  frc[1,41] = s.frc[1,41]
  frc[2,41] = s.frc[2,41]
  frc[3,41] = s.frc[3,41]
  frc[1,44] = s.frc[1,44]
  frc[2,44] = s.frc[2,44]
  frc[3,44] = s.frc[3,44]
  frc[1,46] = s.frc[1,46]
  frc[2,46] = s.frc[2,46]
  frc[3,46] = s.frc[3,46]
  frc[1,49] = s.frc[1,49]
  frc[2,49] = s.frc[2,49]
  frc[3,49] = s.frc[3,49]
  frc[1,51] = s.frc[1,51]
  frc[2,51] = s.frc[2,51]
  frc[3,51] = s.frc[3,51]
  frc[1,53] = s.frc[1,53]
  frc[2,53] = s.frc[2,53]
  frc[3,53] = s.frc[3,53]
  frc[1,54] = s.frc[1,54]
  frc[2,54] = s.frc[2,54]
  frc[3,54] = s.frc[3,54]
  frc[1,55] = s.frc[1,55]
  frc[2,55] = s.frc[2,55]
  frc[3,55] = s.frc[3,55]
  frc[1,57] = s.frc[1,57]
  frc[2,57] = s.frc[2,57]
  frc[3,57] = s.frc[3,57]
  frc[1,59] = s.frc[1,59]
  frc[2,59] = s.frc[2,59]
  frc[3,59] = s.frc[3,59]
  frc[1,60] = s.frc[1,60]
  frc[2,60] = s.frc[2,60]
  frc[3,60] = s.frc[3,60]
  frc[1,61] = s.frc[1,61]
  frc[2,61] = s.frc[2,61]
  frc[3,61] = s.frc[3,61]
  frc[1,63] = s.frc[1,63]
  frc[2,63] = s.frc[2,63]
  frc[3,63] = s.frc[3,63]
  frc[1,65] = s.frc[1,65]
  frc[2,65] = s.frc[2,65]
  frc[3,65] = s.frc[3,65]
  frc[1,66] = s.frc[1,66]
  frc[2,66] = s.frc[2,66]
  frc[3,66] = s.frc[3,66]
  frc[1,67] = s.frc[1,67]
  frc[2,67] = s.frc[2,67]
  frc[3,67] = s.frc[3,67]
  trq[1,7] = s.trq[1,7]
  trq[2,7] = s.trq[2,7]
  trq[3,7] = s.trq[3,7]
  trq[1,10] = s.trq[1,10]
  trq[2,10] = s.trq[2,10]
  trq[3,10] = s.trq[3,10]
  trq[1,12] = s.trq[1,12]
  trq[2,12] = s.trq[2,12]
  trq[3,12] = s.trq[3,12]
  trq[1,15] = s.trq[1,15]
  trq[2,15] = s.trq[2,15]
  trq[3,15] = s.trq[3,15]
  trq[1,18] = s.trq[1,18]
  trq[2,18] = s.trq[2,18]
  trq[3,18] = s.trq[3,18]
  trq[1,20] = s.trq[1,20]
  trq[2,20] = s.trq[2,20]
  trq[3,20] = s.trq[3,20]
  trq[1,24] = s.trq[1,24]
  trq[2,24] = s.trq[2,24]
  trq[3,24] = s.trq[3,24]
  trq[1,26] = s.trq[1,26]
  trq[2,26] = s.trq[2,26]
  trq[3,26] = s.trq[3,26]
  trq[1,28] = s.trq[1,28]
  trq[2,28] = s.trq[2,28]
  trq[3,28] = s.trq[3,28]
  trq[1,30] = s.trq[1,30]
  trq[2,30] = s.trq[2,30]
  trq[3,30] = s.trq[3,30]
  trq[1,33] = s.trq[1,33]
  trq[2,33] = s.trq[2,33]
  trq[3,33] = s.trq[3,33]
  trq[1,35] = s.trq[1,35]
  trq[2,35] = s.trq[2,35]
  trq[3,35] = s.trq[3,35]
  trq[1,39] = s.trq[1,39]
  trq[2,39] = s.trq[2,39]
  trq[3,39] = s.trq[3,39]
  trq[1,41] = s.trq[1,41]
  trq[2,41] = s.trq[2,41]
  trq[3,41] = s.trq[3,41]
  trq[1,44] = s.trq[1,44]
  trq[2,44] = s.trq[2,44]
  trq[3,44] = s.trq[3,44]
  trq[1,46] = s.trq[1,46]
  trq[2,46] = s.trq[2,46]
  trq[3,46] = s.trq[3,46]
  trq[1,49] = s.trq[1,49]
  trq[2,49] = s.trq[2,49]
  trq[3,49] = s.trq[3,49]
  trq[1,51] = s.trq[1,51]
  trq[2,51] = s.trq[2,51]
  trq[3,51] = s.trq[3,51]
  trq[1,53] = s.trq[1,53]
  trq[2,53] = s.trq[2,53]
  trq[3,53] = s.trq[3,53]
  trq[1,54] = s.trq[1,54]
  trq[2,54] = s.trq[2,54]
  trq[3,54] = s.trq[3,54]
  trq[1,55] = s.trq[1,55]
  trq[2,55] = s.trq[2,55]
  trq[3,55] = s.trq[3,55]
  trq[1,57] = s.trq[1,57]
  trq[2,57] = s.trq[2,57]
  trq[3,57] = s.trq[3,57]
  trq[1,59] = s.trq[1,59]
  trq[2,59] = s.trq[2,59]
  trq[3,59] = s.trq[3,59]
  trq[1,60] = s.trq[1,60]
  trq[2,60] = s.trq[2,60]
  trq[3,60] = s.trq[3,60]
  trq[1,61] = s.trq[1,61]
  trq[2,61] = s.trq[2,61]
  trq[3,61] = s.trq[3,61]
  trq[1,63] = s.trq[1,63]
  trq[2,63] = s.trq[2,63]
  trq[3,63] = s.trq[3,63]
  trq[1,65] = s.trq[1,65]
  trq[2,65] = s.trq[2,65]
  trq[3,65] = s.trq[3,65]
  trq[1,66] = s.trq[1,66]
  trq[2,66] = s.trq[2,66]
  trq[3,66] = s.trq[3,66]
  trq[1,67] = s.trq[1,67]
  trq[2,67] = s.trq[2,67]
  trq[3,67] = s.trq[3,67]

# ====== END Task 0 ====== 

  

