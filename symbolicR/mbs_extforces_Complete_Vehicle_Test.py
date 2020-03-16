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
#	==> Generation Date : Mon Mar 16 18:21:54 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 18
#
#	==> Function : F19 : External Forces
#	==> Flops complexity : 1444
#
#	==> Generation Time :  0.020 seconds
#	==> Post-Processing :  0.030 seconds
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

# = = Block_0_0_1_1_0_1 = = 
 
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
  OMcp0_26 = OMcp0_25+qd[6]*ROcp0_85
  OMcp0_36 = OMcp0_35+qd[6]*ROcp0_95
  OPcp0_16 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5
  OPcp0_26 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp0_95-OMcp0_35*S5)-qdd[5]*C4-qdd[6]*ROcp0_85)
  OPcp0_36 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp0_85-OMcp0_25*S5)+qdd[5]*S4+qdd[6]*ROcp0_95

# = = Block_0_0_1_1_0_2 = = 
 
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
  OMcp0_17 = OMcp0_16+qd[7]*ROcp0_16
  OMcp0_27 = OMcp0_26+qd[7]*ROcp0_26
  OMcp0_37 = OMcp0_36+qd[7]*ROcp0_36
  ORcp0_17 = OMcp0_26*RLcp0_37-OMcp0_36*RLcp0_27
  ORcp0_27 = -(OMcp0_16*RLcp0_37-OMcp0_36*RLcp0_17)
  ORcp0_37 = OMcp0_16*RLcp0_27-OMcp0_26*RLcp0_17
  OPcp0_17 = OPcp0_16+qd[7]*(OMcp0_26*ROcp0_36-OMcp0_36*ROcp0_26)+qdd[7]*ROcp0_16
  OPcp0_27 = OPcp0_26-qd[7]*(OMcp0_16*ROcp0_36-OMcp0_36*ROcp0_16)+qdd[7]*ROcp0_26
  OPcp0_37 = OPcp0_36+qd[7]*(OMcp0_16*ROcp0_26-OMcp0_26*ROcp0_16)+qdd[7]*ROcp0_36
  RLcp0_18 = ROcp0_47*s.dpt[2,13]
  RLcp0_28 = ROcp0_57*s.dpt[2,13]
  RLcp0_38 = ROcp0_67*s.dpt[2,13]
  OMcp0_18 = OMcp0_17+qd[8]*ROcp0_77
  OMcp0_28 = OMcp0_27+qd[8]*ROcp0_87
  OMcp0_38 = OMcp0_37+qd[8]*ROcp0_97
  ORcp0_18 = OMcp0_27*RLcp0_38-OMcp0_37*RLcp0_28
  ORcp0_28 = -(OMcp0_17*RLcp0_38-OMcp0_37*RLcp0_18)
  ORcp0_38 = OMcp0_17*RLcp0_28-OMcp0_27*RLcp0_18
  PxF1[1] = q[1]+RLcp0_17+RLcp0_18
  PxF1[2] = q[2]+RLcp0_27+RLcp0_28
  PxF1[3] = q[3]+RLcp0_37+RLcp0_38
  RxF1[1,1] = ROcp0_18
  RxF1[1,2] = ROcp0_28
  RxF1[1,3] = ROcp0_38
  RxF1[2,1] = ROcp0_49
  RxF1[2,2] = ROcp0_59
  RxF1[2,3] = ROcp0_69
  RxF1[3,1] = ROcp0_79
  RxF1[3,2] = ROcp0_89
  RxF1[3,3] = ROcp0_99
  VxF1[1] = qd[1]+ORcp0_17+ORcp0_18
  VxF1[2] = qd[2]+ORcp0_27+ORcp0_28
  VxF1[3] = qd[3]+ORcp0_37+ORcp0_38
  OMxF1[1] = OMcp0_18+qd[9]*ROcp0_18
  OMxF1[2] = OMcp0_28+qd[9]*ROcp0_28
  OMxF1[3] = OMcp0_38+qd[9]*ROcp0_38
  AxF1[1] = qdd[1]+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_36*ORcp0_27-OMcp0_37*ORcp0_28+OPcp0_26*RLcp0_37+OPcp0_27*\
   RLcp0_38-OPcp0_36*RLcp0_27-OPcp0_37*RLcp0_28
  AxF1[2] = qdd[2]-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_36*ORcp0_17+OMcp0_37*ORcp0_18-OPcp0_16*RLcp0_37-OPcp0_17*\
   RLcp0_38+OPcp0_36*RLcp0_17+OPcp0_37*RLcp0_18
  AxF1[3] = qdd[3]+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_26*ORcp0_17-OMcp0_27*ORcp0_18+OPcp0_16*RLcp0_27+OPcp0_17*\
   RLcp0_28-OPcp0_26*RLcp0_17-OPcp0_27*RLcp0_18
  OMPxF1[1] = OPcp0_17+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(OMcp0_28*ROcp0_38-OMcp0_38*ROcp0_28)+qdd[8]*\
   ROcp0_77+qdd[9]*ROcp0_18
  OMPxF1[2] = OPcp0_27-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(OMcp0_18*ROcp0_38-OMcp0_38*ROcp0_18)+qdd[8]*\
   ROcp0_87+qdd[9]*ROcp0_28
  OMPxF1[3] = OPcp0_37+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(OMcp0_18*ROcp0_28-OMcp0_28*ROcp0_18)+qdd[8]*\
   ROcp0_97+qdd[9]*ROcp0_38
 
# Sensor Forces Computation 

  SWr1 = s.user_ExtForces(PxF1,RxF1,VxF1,OMxF1,AxF1,OMPxF1,s,tsim,1)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc11 = ROcp0_18*SWr1[1]+ROcp0_28*SWr1[2]+ROcp0_38*SWr1[3]
  xfrc21 = ROcp0_49*SWr1[1]+ROcp0_59*SWr1[2]+ROcp0_69*SWr1[3]
  xfrc31 = ROcp0_79*SWr1[1]+ROcp0_89*SWr1[2]+ROcp0_99*SWr1[3]
  frc[1,9] = s.frc[1,9]+xfrc11
  frc[2,9] = s.frc[2,9]+xfrc21
  frc[3,9] = s.frc[3,9]+xfrc31
  xtrq11 = ROcp0_18*SWr1[4]+ROcp0_28*SWr1[5]+ROcp0_38*SWr1[6]
  xtrq21 = ROcp0_49*SWr1[4]+ROcp0_59*SWr1[5]+ROcp0_69*SWr1[6]
  xtrq31 = ROcp0_79*SWr1[4]+ROcp0_89*SWr1[5]+ROcp0_99*SWr1[6]
  trq[1,9] = s.trq[1,9]+xtrq11-xfrc21*SWr1[9]+xfrc31*SWr1[8]
  trq[2,9] = s.trq[2,9]+xtrq21+xfrc11*SWr1[9]-xfrc31*SWr1[7]
  trq[3,9] = s.trq[3,9]+xtrq31-xfrc11*SWr1[8]+xfrc21*SWr1[7]

# = = Block_0_0_1_2_0_1 = = 
 
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
  OMcp1_26 = OMcp1_25+qd[6]*ROcp1_85
  OMcp1_36 = OMcp1_35+qd[6]*ROcp1_95
  OPcp1_16 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5
  OPcp1_26 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp1_95-OMcp1_35*S5)-qdd[5]*C4-qdd[6]*ROcp1_85)
  OPcp1_36 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp1_85-OMcp1_25*S5)+qdd[5]*S4+qdd[6]*ROcp1_95

# = = Block_0_0_1_2_0_3 = = 
 
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
  OMcp1_110 = OMcp1_16+qd[10]*ROcp1_16
  OMcp1_210 = OMcp1_26+qd[10]*ROcp1_26
  OMcp1_310 = OMcp1_36+qd[10]*ROcp1_36
  ORcp1_110 = OMcp1_26*RLcp1_310-OMcp1_36*RLcp1_210
  ORcp1_210 = -(OMcp1_16*RLcp1_310-OMcp1_36*RLcp1_110)
  ORcp1_310 = OMcp1_16*RLcp1_210-OMcp1_26*RLcp1_110
  OPcp1_110 = OPcp1_16+qd[10]*(OMcp1_26*ROcp1_36-OMcp1_36*ROcp1_26)+qdd[10]*ROcp1_16
  OPcp1_210 = OPcp1_26-qd[10]*(OMcp1_16*ROcp1_36-OMcp1_36*ROcp1_16)+qdd[10]*ROcp1_26
  OPcp1_310 = OPcp1_36+qd[10]*(OMcp1_16*ROcp1_26-OMcp1_26*ROcp1_16)+qdd[10]*ROcp1_36
  RLcp1_111 = ROcp1_410*s.dpt[2,17]
  RLcp1_211 = ROcp1_510*s.dpt[2,17]
  RLcp1_311 = ROcp1_610*s.dpt[2,17]
  OMcp1_111 = OMcp1_110+qd[11]*ROcp1_710
  OMcp1_211 = OMcp1_210+qd[11]*ROcp1_810
  OMcp1_311 = OMcp1_310+qd[11]*ROcp1_910
  ORcp1_111 = OMcp1_210*RLcp1_311-OMcp1_310*RLcp1_211
  ORcp1_211 = -(OMcp1_110*RLcp1_311-OMcp1_310*RLcp1_111)
  ORcp1_311 = OMcp1_110*RLcp1_211-OMcp1_210*RLcp1_111
  PxF2[1] = q[1]+RLcp1_110+RLcp1_111
  PxF2[2] = q[2]+RLcp1_210+RLcp1_211
  PxF2[3] = q[3]+RLcp1_310+RLcp1_311
  RxF2[1,1] = ROcp1_111
  RxF2[1,2] = ROcp1_211
  RxF2[1,3] = ROcp1_311
  RxF2[2,1] = ROcp1_412
  RxF2[2,2] = ROcp1_512
  RxF2[2,3] = ROcp1_612
  RxF2[3,1] = ROcp1_712
  RxF2[3,2] = ROcp1_812
  RxF2[3,3] = ROcp1_912
  VxF2[1] = qd[1]+ORcp1_110+ORcp1_111
  VxF2[2] = qd[2]+ORcp1_210+ORcp1_211
  VxF2[3] = qd[3]+ORcp1_310+ORcp1_311
  OMxF2[1] = OMcp1_111+qd[12]*ROcp1_111
  OMxF2[2] = OMcp1_211+qd[12]*ROcp1_211
  OMxF2[3] = OMcp1_311+qd[12]*ROcp1_311
  AxF2[1] = qdd[1]+OMcp1_210*ORcp1_311+OMcp1_26*ORcp1_310-OMcp1_310*ORcp1_211-OMcp1_36*ORcp1_210+OPcp1_210*RLcp1_311+\
   OPcp1_26*RLcp1_310-OPcp1_310*RLcp1_211-OPcp1_36*RLcp1_210
  AxF2[2] = qdd[2]-OMcp1_110*ORcp1_311-OMcp1_16*ORcp1_310+OMcp1_310*ORcp1_111+OMcp1_36*ORcp1_110-OPcp1_110*RLcp1_311-\
   OPcp1_16*RLcp1_310+OPcp1_310*RLcp1_111+OPcp1_36*RLcp1_110
  AxF2[3] = qdd[3]+OMcp1_110*ORcp1_211+OMcp1_16*ORcp1_210-OMcp1_210*ORcp1_111-OMcp1_26*ORcp1_110+OPcp1_110*RLcp1_211+\
   OPcp1_16*RLcp1_210-OPcp1_210*RLcp1_111-OPcp1_26*RLcp1_110
  OMPxF2[1] = OPcp1_110+qd[11]*(OMcp1_210*ROcp1_910-OMcp1_310*ROcp1_810)+qd[12]*(OMcp1_211*ROcp1_311-OMcp1_311*ROcp1_211\
   )+qdd[11]*ROcp1_710+qdd[12]*ROcp1_111
  OMPxF2[2] = OPcp1_210-qd[11]*(OMcp1_110*ROcp1_910-OMcp1_310*ROcp1_710)-qd[12]*(OMcp1_111*ROcp1_311-OMcp1_311*ROcp1_111\
   )+qdd[11]*ROcp1_810+qdd[12]*ROcp1_211
  OMPxF2[3] = OPcp1_310+qd[11]*(OMcp1_110*ROcp1_810-OMcp1_210*ROcp1_710)+qd[12]*(OMcp1_111*ROcp1_211-OMcp1_211*ROcp1_111\
   )+qdd[11]*ROcp1_910+qdd[12]*ROcp1_311
 
# Sensor Forces Computation 

  SWr2 = s.user_ExtForces(PxF2,RxF2,VxF2,OMxF2,AxF2,OMPxF2,s,tsim,2)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc12 = ROcp1_111*SWr2[1]+ROcp1_211*SWr2[2]+ROcp1_311*SWr2[3]
  xfrc22 = ROcp1_412*SWr2[1]+ROcp1_512*SWr2[2]+ROcp1_612*SWr2[3]
  xfrc32 = ROcp1_712*SWr2[1]+ROcp1_812*SWr2[2]+ROcp1_912*SWr2[3]
  frc[1,12] = s.frc[1,12]+xfrc12
  frc[2,12] = s.frc[2,12]+xfrc22
  frc[3,12] = s.frc[3,12]+xfrc32
  xtrq12 = ROcp1_111*SWr2[4]+ROcp1_211*SWr2[5]+ROcp1_311*SWr2[6]
  xtrq22 = ROcp1_412*SWr2[4]+ROcp1_512*SWr2[5]+ROcp1_612*SWr2[6]
  xtrq32 = ROcp1_712*SWr2[4]+ROcp1_812*SWr2[5]+ROcp1_912*SWr2[6]
  trq[1,12] = s.trq[1,12]+xtrq12-xfrc22*SWr2[9]+xfrc32*SWr2[8]
  trq[2,12] = s.trq[2,12]+xtrq22+xfrc12*SWr2[9]-xfrc32*SWr2[7]
  trq[3,12] = s.trq[3,12]+xtrq32-xfrc12*SWr2[8]+xfrc22*SWr2[7]

# = = Block_0_0_1_3_0_1 = = 
 
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
  OMcp2_26 = OMcp2_25+qd[6]*ROcp2_85
  OMcp2_36 = OMcp2_35+qd[6]*ROcp2_95
  OPcp2_16 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5
  OPcp2_26 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp2_95-OMcp2_35*S5)-qdd[5]*C4-qdd[6]*ROcp2_85)
  OPcp2_36 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp2_85-OMcp2_25*S5)+qdd[5]*S4+qdd[6]*ROcp2_95

# = = Block_0_0_1_3_0_4 = = 
 
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
  OMcp2_113 = OMcp2_16+qd[13]*ROcp2_16
  OMcp2_213 = OMcp2_26+qd[13]*ROcp2_26
  OMcp2_313 = OMcp2_36+qd[13]*ROcp2_36
  ORcp2_113 = OMcp2_26*RLcp2_313-OMcp2_36*RLcp2_213
  ORcp2_213 = -(OMcp2_16*RLcp2_313-OMcp2_36*RLcp2_113)
  ORcp2_313 = OMcp2_16*RLcp2_213-OMcp2_26*RLcp2_113
  OPcp2_113 = OPcp2_16+qd[13]*(OMcp2_26*ROcp2_36-OMcp2_36*ROcp2_26)+qdd[13]*ROcp2_16
  OPcp2_213 = OPcp2_26-qd[13]*(OMcp2_16*ROcp2_36-OMcp2_36*ROcp2_16)+qdd[13]*ROcp2_26
  OPcp2_313 = OPcp2_36+qd[13]*(OMcp2_16*ROcp2_26-OMcp2_26*ROcp2_16)+qdd[13]*ROcp2_36
  RLcp2_114 = ROcp2_413*s.dpt[2,21]
  RLcp2_214 = ROcp2_513*s.dpt[2,21]
  RLcp2_314 = ROcp2_613*s.dpt[2,21]
  OMcp2_114 = OMcp2_113+qd[14]*ROcp2_16
  OMcp2_214 = OMcp2_213+qd[14]*ROcp2_26
  OMcp2_314 = OMcp2_313+qd[14]*ROcp2_36
  ORcp2_114 = OMcp2_213*RLcp2_314-OMcp2_313*RLcp2_214
  ORcp2_214 = -(OMcp2_113*RLcp2_314-OMcp2_313*RLcp2_114)
  ORcp2_314 = OMcp2_113*RLcp2_214-OMcp2_213*RLcp2_114
  OPcp2_114 = OPcp2_113+qd[14]*(OMcp2_213*ROcp2_36-OMcp2_313*ROcp2_26)+qdd[14]*ROcp2_16
  OPcp2_214 = OPcp2_213-qd[14]*(OMcp2_113*ROcp2_36-OMcp2_313*ROcp2_16)+qdd[14]*ROcp2_26
  OPcp2_314 = OPcp2_313+qd[14]*(OMcp2_113*ROcp2_26-OMcp2_213*ROcp2_16)+qdd[14]*ROcp2_36
  RLcp2_115 = ROcp2_16*s.dpt[1,23]
  RLcp2_215 = ROcp2_26*s.dpt[1,23]
  RLcp2_315 = ROcp2_36*s.dpt[1,23]
  ORcp2_115 = OMcp2_214*RLcp2_315-OMcp2_314*RLcp2_215
  ORcp2_215 = -(OMcp2_114*RLcp2_315-OMcp2_314*RLcp2_115)
  ORcp2_315 = OMcp2_114*RLcp2_215-OMcp2_214*RLcp2_115
  PxF3[1] = q[1]+RLcp2_113+RLcp2_114+RLcp2_115
  PxF3[2] = q[2]+RLcp2_213+RLcp2_214+RLcp2_215
  PxF3[3] = q[3]+RLcp2_313+RLcp2_314+RLcp2_315
  RxF3[1,1] = ROcp2_16
  RxF3[1,2] = ROcp2_26
  RxF3[1,3] = ROcp2_36
  RxF3[2,1] = ROcp2_415
  RxF3[2,2] = ROcp2_515
  RxF3[2,3] = ROcp2_615
  RxF3[3,1] = ROcp2_715
  RxF3[3,2] = ROcp2_815
  RxF3[3,3] = ROcp2_915
  VxF3[1] = qd[1]+ORcp2_113+ORcp2_114+ORcp2_115
  VxF3[2] = qd[2]+ORcp2_213+ORcp2_214+ORcp2_215
  VxF3[3] = qd[3]+ORcp2_313+ORcp2_314+ORcp2_315
  OMxF3[1] = OMcp2_114+qd[15]*ROcp2_16
  OMxF3[2] = OMcp2_214+qd[15]*ROcp2_26
  OMxF3[3] = OMcp2_314+qd[15]*ROcp2_36
  AxF3[1] = qdd[1]+OMcp2_213*ORcp2_314+OMcp2_214*ORcp2_315+OMcp2_26*ORcp2_313-OMcp2_313*ORcp2_214-OMcp2_314*ORcp2_215-\
   OMcp2_36*ORcp2_213+OPcp2_213*RLcp2_314+OPcp2_214*RLcp2_315+OPcp2_26*RLcp2_313-OPcp2_313*RLcp2_214-OPcp2_314*RLcp2_215-\
   OPcp2_36*RLcp2_213
  AxF3[2] = qdd[2]-OMcp2_113*ORcp2_314-OMcp2_114*ORcp2_315-OMcp2_16*ORcp2_313+OMcp2_313*ORcp2_114+OMcp2_314*ORcp2_115+\
   OMcp2_36*ORcp2_113-OPcp2_113*RLcp2_314-OPcp2_114*RLcp2_315-OPcp2_16*RLcp2_313+OPcp2_313*RLcp2_114+OPcp2_314*RLcp2_115+\
   OPcp2_36*RLcp2_113
  AxF3[3] = qdd[3]+OMcp2_113*ORcp2_214+OMcp2_114*ORcp2_215+OMcp2_16*ORcp2_213-OMcp2_213*ORcp2_114-OMcp2_214*ORcp2_115-\
   OMcp2_26*ORcp2_113+OPcp2_113*RLcp2_214+OPcp2_114*RLcp2_215+OPcp2_16*RLcp2_213-OPcp2_213*RLcp2_114-OPcp2_214*RLcp2_115-\
   OPcp2_26*RLcp2_113
  OMPxF3[1] = OPcp2_114+qd[15]*(OMcp2_214*ROcp2_36-OMcp2_314*ROcp2_26)+qdd[15]*ROcp2_16
  OMPxF3[2] = OPcp2_214-qd[15]*(OMcp2_114*ROcp2_36-OMcp2_314*ROcp2_16)+qdd[15]*ROcp2_26
  OMPxF3[3] = OPcp2_314+qd[15]*(OMcp2_114*ROcp2_26-OMcp2_214*ROcp2_16)+qdd[15]*ROcp2_36
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc13 = ROcp2_16*SWr3[1]+ROcp2_26*SWr3[2]+ROcp2_36*SWr3[3]
  xfrc23 = ROcp2_415*SWr3[1]+ROcp2_515*SWr3[2]+ROcp2_615*SWr3[3]
  xfrc33 = ROcp2_715*SWr3[1]+ROcp2_815*SWr3[2]+ROcp2_915*SWr3[3]
  frc[1,15] = s.frc[1,15]+xfrc13
  frc[2,15] = s.frc[2,15]+xfrc23
  frc[3,15] = s.frc[3,15]+xfrc33
  xtrq13 = ROcp2_16*SWr3[4]+ROcp2_26*SWr3[5]+ROcp2_36*SWr3[6]
  xtrq23 = ROcp2_415*SWr3[4]+ROcp2_515*SWr3[5]+ROcp2_615*SWr3[6]
  xtrq33 = ROcp2_715*SWr3[4]+ROcp2_815*SWr3[5]+ROcp2_915*SWr3[6]
  trq[1,15] = s.trq[1,15]+xtrq13-xfrc23*SWr3[9]+xfrc33*SWr3[8]
  trq[2,15] = s.trq[2,15]+xtrq23+xfrc13*SWr3[9]-xfrc33*SWr3[7]
  trq[3,15] = s.trq[3,15]+xtrq33-xfrc13*SWr3[8]+xfrc23*SWr3[7]

# = = Block_0_0_1_4_0_1 = = 
 
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
  OMcp3_26 = OMcp3_25+qd[6]*ROcp3_85
  OMcp3_36 = OMcp3_35+qd[6]*ROcp3_95
  OPcp3_16 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5
  OPcp3_26 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp3_95-OMcp3_35*S5)-qdd[5]*C4-qdd[6]*ROcp3_85)
  OPcp3_36 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp3_85-OMcp3_25*S5)+qdd[5]*S4+qdd[6]*ROcp3_95

# = = Block_0_0_1_4_0_5 = = 
 
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
  OMcp3_116 = OMcp3_16+qd[16]*ROcp3_16
  OMcp3_216 = OMcp3_26+qd[16]*ROcp3_26
  OMcp3_316 = OMcp3_36+qd[16]*ROcp3_36
  ORcp3_116 = OMcp3_26*RLcp3_316-OMcp3_36*RLcp3_216
  ORcp3_216 = -(OMcp3_16*RLcp3_316-OMcp3_36*RLcp3_116)
  ORcp3_316 = OMcp3_16*RLcp3_216-OMcp3_26*RLcp3_116
  OPcp3_116 = OPcp3_16+qd[16]*(OMcp3_26*ROcp3_36-OMcp3_36*ROcp3_26)+qdd[16]*ROcp3_16
  OPcp3_216 = OPcp3_26-qd[16]*(OMcp3_16*ROcp3_36-OMcp3_36*ROcp3_16)+qdd[16]*ROcp3_26
  OPcp3_316 = OPcp3_36+qd[16]*(OMcp3_16*ROcp3_26-OMcp3_26*ROcp3_16)+qdd[16]*ROcp3_36
  RLcp3_117 = ROcp3_416*s.dpt[2,27]
  RLcp3_217 = ROcp3_516*s.dpt[2,27]
  RLcp3_317 = ROcp3_616*s.dpt[2,27]
  OMcp3_117 = OMcp3_116+qd[17]*ROcp3_16
  OMcp3_217 = OMcp3_216+qd[17]*ROcp3_26
  OMcp3_317 = OMcp3_316+qd[17]*ROcp3_36
  ORcp3_117 = OMcp3_216*RLcp3_317-OMcp3_316*RLcp3_217
  ORcp3_217 = -(OMcp3_116*RLcp3_317-OMcp3_316*RLcp3_117)
  ORcp3_317 = OMcp3_116*RLcp3_217-OMcp3_216*RLcp3_117
  OPcp3_117 = OPcp3_116+qd[17]*(OMcp3_216*ROcp3_36-OMcp3_316*ROcp3_26)+qdd[17]*ROcp3_16
  OPcp3_217 = OPcp3_216-qd[17]*(OMcp3_116*ROcp3_36-OMcp3_316*ROcp3_16)+qdd[17]*ROcp3_26
  OPcp3_317 = OPcp3_316+qd[17]*(OMcp3_116*ROcp3_26-OMcp3_216*ROcp3_16)+qdd[17]*ROcp3_36
  RLcp3_118 = ROcp3_16*s.dpt[1,31]
  RLcp3_218 = ROcp3_26*s.dpt[1,31]
  RLcp3_318 = ROcp3_36*s.dpt[1,31]
  ORcp3_118 = OMcp3_217*RLcp3_318-OMcp3_317*RLcp3_218
  ORcp3_218 = -(OMcp3_117*RLcp3_318-OMcp3_317*RLcp3_118)
  ORcp3_318 = OMcp3_117*RLcp3_218-OMcp3_217*RLcp3_118
  PxF4[1] = q[1]+RLcp3_116+RLcp3_117+RLcp3_118
  PxF4[2] = q[2]+RLcp3_216+RLcp3_217+RLcp3_218
  PxF4[3] = q[3]+RLcp3_316+RLcp3_317+RLcp3_318
  RxF4[1,1] = ROcp3_16
  RxF4[1,2] = ROcp3_26
  RxF4[1,3] = ROcp3_36
  RxF4[2,1] = ROcp3_418
  RxF4[2,2] = ROcp3_518
  RxF4[2,3] = ROcp3_618
  RxF4[3,1] = ROcp3_718
  RxF4[3,2] = ROcp3_818
  RxF4[3,3] = ROcp3_918
  VxF4[1] = qd[1]+ORcp3_116+ORcp3_117+ORcp3_118
  VxF4[2] = qd[2]+ORcp3_216+ORcp3_217+ORcp3_218
  VxF4[3] = qd[3]+ORcp3_316+ORcp3_317+ORcp3_318
  OMxF4[1] = OMcp3_117+qd[18]*ROcp3_16
  OMxF4[2] = OMcp3_217+qd[18]*ROcp3_26
  OMxF4[3] = OMcp3_317+qd[18]*ROcp3_36
  AxF4[1] = qdd[1]+OMcp3_216*ORcp3_317+OMcp3_217*ORcp3_318+OMcp3_26*ORcp3_316-OMcp3_316*ORcp3_217-OMcp3_317*ORcp3_218-\
   OMcp3_36*ORcp3_216+OPcp3_216*RLcp3_317+OPcp3_217*RLcp3_318+OPcp3_26*RLcp3_316-OPcp3_316*RLcp3_217-OPcp3_317*RLcp3_218-\
   OPcp3_36*RLcp3_216
  AxF4[2] = qdd[2]-OMcp3_116*ORcp3_317-OMcp3_117*ORcp3_318-OMcp3_16*ORcp3_316+OMcp3_316*ORcp3_117+OMcp3_317*ORcp3_118+\
   OMcp3_36*ORcp3_116-OPcp3_116*RLcp3_317-OPcp3_117*RLcp3_318-OPcp3_16*RLcp3_316+OPcp3_316*RLcp3_117+OPcp3_317*RLcp3_118+\
   OPcp3_36*RLcp3_116
  AxF4[3] = qdd[3]+OMcp3_116*ORcp3_217+OMcp3_117*ORcp3_218+OMcp3_16*ORcp3_216-OMcp3_216*ORcp3_117-OMcp3_217*ORcp3_118-\
   OMcp3_26*ORcp3_116+OPcp3_116*RLcp3_217+OPcp3_117*RLcp3_218+OPcp3_16*RLcp3_216-OPcp3_216*RLcp3_117-OPcp3_217*RLcp3_118-\
   OPcp3_26*RLcp3_116
  OMPxF4[1] = OPcp3_117+qd[18]*(OMcp3_217*ROcp3_36-OMcp3_317*ROcp3_26)+qdd[18]*ROcp3_16
  OMPxF4[2] = OPcp3_217-qd[18]*(OMcp3_117*ROcp3_36-OMcp3_317*ROcp3_16)+qdd[18]*ROcp3_26
  OMPxF4[3] = OPcp3_317+qd[18]*(OMcp3_117*ROcp3_26-OMcp3_217*ROcp3_16)+qdd[18]*ROcp3_36
 
# Sensor Forces Computation 

  SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc14 = ROcp3_16*SWr4[1]+ROcp3_26*SWr4[2]+ROcp3_36*SWr4[3]
  xfrc24 = ROcp3_418*SWr4[1]+ROcp3_518*SWr4[2]+ROcp3_618*SWr4[3]
  xfrc34 = ROcp3_718*SWr4[1]+ROcp3_818*SWr4[2]+ROcp3_918*SWr4[3]
  frc[1,18] = s.frc[1,18]+xfrc14
  frc[2,18] = s.frc[2,18]+xfrc24
  frc[3,18] = s.frc[3,18]+xfrc34
  xtrq14 = ROcp3_16*SWr4[4]+ROcp3_26*SWr4[5]+ROcp3_36*SWr4[6]
  xtrq24 = ROcp3_418*SWr4[4]+ROcp3_518*SWr4[5]+ROcp3_618*SWr4[6]
  xtrq34 = ROcp3_718*SWr4[4]+ROcp3_818*SWr4[5]+ROcp3_918*SWr4[6]
  trq[1,18] = s.trq[1,18]+xtrq14-xfrc24*SWr4[9]+xfrc34*SWr4[8]
  trq[2,18] = s.trq[2,18]+xtrq24+xfrc14*SWr4[9]-xfrc34*SWr4[7]
  trq[3,18] = s.trq[3,18]+xtrq34-xfrc14*SWr4[8]+xfrc24*SWr4[7]

# = = Block_0_0_1_4_1_0 = = 
 
# Symbolic Outputs  

  frc[1,6] = s.frc[1,6]
  frc[2,6] = s.frc[2,6]
  frc[3,6] = s.frc[3,6]
  frc[1,7] = s.frc[1,7]
  frc[2,7] = s.frc[2,7]
  frc[3,7] = s.frc[3,7]
  frc[1,8] = s.frc[1,8]
  frc[2,8] = s.frc[2,8]
  frc[3,8] = s.frc[3,8]
  frc[1,10] = s.frc[1,10]
  frc[2,10] = s.frc[2,10]
  frc[3,10] = s.frc[3,10]
  frc[1,11] = s.frc[1,11]
  frc[2,11] = s.frc[2,11]
  frc[3,11] = s.frc[3,11]
  frc[1,13] = s.frc[1,13]
  frc[2,13] = s.frc[2,13]
  frc[3,13] = s.frc[3,13]
  frc[1,14] = s.frc[1,14]
  frc[2,14] = s.frc[2,14]
  frc[3,14] = s.frc[3,14]
  frc[1,16] = s.frc[1,16]
  frc[2,16] = s.frc[2,16]
  frc[3,16] = s.frc[3,16]
  frc[1,17] = s.frc[1,17]
  frc[2,17] = s.frc[2,17]
  frc[3,17] = s.frc[3,17]
  trq[1,6] = s.trq[1,6]
  trq[2,6] = s.trq[2,6]
  trq[3,6] = s.trq[3,6]
  trq[1,7] = s.trq[1,7]
  trq[2,7] = s.trq[2,7]
  trq[3,7] = s.trq[3,7]
  trq[1,8] = s.trq[1,8]
  trq[2,8] = s.trq[2,8]
  trq[3,8] = s.trq[3,8]
  trq[1,10] = s.trq[1,10]
  trq[2,10] = s.trq[2,10]
  trq[3,10] = s.trq[3,10]
  trq[1,11] = s.trq[1,11]
  trq[2,11] = s.trq[2,11]
  trq[3,11] = s.trq[3,11]
  trq[1,13] = s.trq[1,13]
  trq[2,13] = s.trq[2,13]
  trq[3,13] = s.trq[3,13]
  trq[1,14] = s.trq[1,14]
  trq[2,14] = s.trq[2,14]
  trq[3,14] = s.trq[3,14]
  trq[1,16] = s.trq[1,16]
  trq[2,16] = s.trq[2,16]
  trq[3,16] = s.trq[3,16]
  trq[1,17] = s.trq[1,17]
  trq[2,17] = s.trq[2,17]
  trq[3,17] = s.trq[3,17]

# ====== END Task 0 ====== 

  

