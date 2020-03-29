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
#	==> Function : F19 : External Forces
#	==> Flops complexity : 1440
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
  OMcp4_16 = OMcp4_15+qd[6]*ROcp4_45
  OMcp4_26 = OMcp4_25+qd[6]*ROcp4_55
  OMcp4_36 = qd[4]+qd[6]*S5
  OPcp4_16 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp4_55-OMcp4_25*S5)-qdd[5]*C4-qdd[6]*ROcp4_45)
  OPcp4_26 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp4_45-OMcp4_15*S5)+qdd[5]*S4+qdd[6]*ROcp4_55
  OPcp4_36 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5

# = = Block_0_0_1_1_0_2 = = 
 
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
  OMcp4_17 = OMcp4_16+qd[7]*ROcp4_16
  OMcp4_27 = OMcp4_26+qd[7]*ROcp4_26
  OMcp4_37 = OMcp4_36+qd[7]*ROcp4_36
  ORcp4_17 = OMcp4_26*RLcp4_37-OMcp4_36*RLcp4_27
  ORcp4_27 = -(OMcp4_16*RLcp4_37-OMcp4_36*RLcp4_17)
  ORcp4_37 = OMcp4_16*RLcp4_27-OMcp4_26*RLcp4_17
  OPcp4_17 = OPcp4_16+qd[7]*(OMcp4_26*ROcp4_36-OMcp4_36*ROcp4_26)+qdd[7]*ROcp4_16
  OPcp4_27 = OPcp4_26-qd[7]*(OMcp4_16*ROcp4_36-OMcp4_36*ROcp4_16)+qdd[7]*ROcp4_26
  OPcp4_37 = OPcp4_36+qd[7]*(OMcp4_16*ROcp4_26-OMcp4_26*ROcp4_16)+qdd[7]*ROcp4_36
  RLcp4_18 = ROcp4_47*s.dpt[2,14]
  RLcp4_28 = ROcp4_57*s.dpt[2,14]
  RLcp4_38 = ROcp4_67*s.dpt[2,14]
  OMcp4_18 = OMcp4_17+qd[8]*ROcp4_77
  OMcp4_28 = OMcp4_27+qd[8]*ROcp4_87
  OMcp4_38 = OMcp4_37+qd[8]*ROcp4_97
  ORcp4_18 = OMcp4_27*RLcp4_38-OMcp4_37*RLcp4_28
  ORcp4_28 = -(OMcp4_17*RLcp4_38-OMcp4_37*RLcp4_18)
  ORcp4_38 = OMcp4_17*RLcp4_28-OMcp4_27*RLcp4_18
  PxF1[1] = q[1]+RLcp4_17+RLcp4_18
  PxF1[2] = q[2]+RLcp4_27+RLcp4_28
  PxF1[3] = q[3]+RLcp4_37+RLcp4_38
  RxF1[1,1] = ROcp4_18
  RxF1[1,2] = ROcp4_28
  RxF1[1,3] = ROcp4_38
  RxF1[2,1] = ROcp4_49
  RxF1[2,2] = ROcp4_59
  RxF1[2,3] = ROcp4_69
  RxF1[3,1] = ROcp4_79
  RxF1[3,2] = ROcp4_89
  RxF1[3,3] = ROcp4_99
  VxF1[1] = qd[1]+ORcp4_17+ORcp4_18
  VxF1[2] = qd[2]+ORcp4_27+ORcp4_28
  VxF1[3] = qd[3]+ORcp4_37+ORcp4_38
  OMxF1[1] = OMcp4_18+qd[9]*ROcp4_18
  OMxF1[2] = OMcp4_28+qd[9]*ROcp4_28
  OMxF1[3] = OMcp4_38+qd[9]*ROcp4_38
  AxF1[1] = qdd[1]+OMcp4_26*ORcp4_37+OMcp4_27*ORcp4_38-OMcp4_36*ORcp4_27-OMcp4_37*ORcp4_28+OPcp4_26*RLcp4_37+OPcp4_27*\
   RLcp4_38-OPcp4_36*RLcp4_27-OPcp4_37*RLcp4_28
  AxF1[2] = qdd[2]-OMcp4_16*ORcp4_37-OMcp4_17*ORcp4_38+OMcp4_36*ORcp4_17+OMcp4_37*ORcp4_18-OPcp4_16*RLcp4_37-OPcp4_17*\
   RLcp4_38+OPcp4_36*RLcp4_17+OPcp4_37*RLcp4_18
  AxF1[3] = qdd[3]+OMcp4_16*ORcp4_27+OMcp4_17*ORcp4_28-OMcp4_26*ORcp4_17-OMcp4_27*ORcp4_18+OPcp4_16*RLcp4_27+OPcp4_17*\
   RLcp4_28-OPcp4_26*RLcp4_17-OPcp4_27*RLcp4_18
  OMPxF1[1] = OPcp4_17+qd[8]*(OMcp4_27*ROcp4_97-OMcp4_37*ROcp4_87)+qd[9]*(OMcp4_28*ROcp4_38-OMcp4_38*ROcp4_28)+qdd[8]*\
   ROcp4_77+qdd[9]*ROcp4_18
  OMPxF1[2] = OPcp4_27-qd[8]*(OMcp4_17*ROcp4_97-OMcp4_37*ROcp4_77)-qd[9]*(OMcp4_18*ROcp4_38-OMcp4_38*ROcp4_18)+qdd[8]*\
   ROcp4_87+qdd[9]*ROcp4_28
  OMPxF1[3] = OPcp4_37+qd[8]*(OMcp4_17*ROcp4_87-OMcp4_27*ROcp4_77)+qd[9]*(OMcp4_18*ROcp4_28-OMcp4_28*ROcp4_18)+qdd[8]*\
   ROcp4_97+qdd[9]*ROcp4_38
 
# Sensor Forces Computation 

  SWr1 = s.user_ExtForces(PxF1,RxF1,VxF1,OMxF1,AxF1,OMPxF1,s,tsim,1)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc15 = ROcp4_18*SWr1[1]+ROcp4_28*SWr1[2]+ROcp4_38*SWr1[3]
  xfrc25 = ROcp4_49*SWr1[1]+ROcp4_59*SWr1[2]+ROcp4_69*SWr1[3]
  xfrc35 = ROcp4_79*SWr1[1]+ROcp4_89*SWr1[2]+ROcp4_99*SWr1[3]
  frc[1,9] = s.frc[1,9]+xfrc15
  frc[2,9] = s.frc[2,9]+xfrc25
  frc[3,9] = s.frc[3,9]+xfrc35
  xtrq15 = ROcp4_18*SWr1[4]+ROcp4_28*SWr1[5]+ROcp4_38*SWr1[6]
  xtrq25 = ROcp4_49*SWr1[4]+ROcp4_59*SWr1[5]+ROcp4_69*SWr1[6]
  xtrq35 = ROcp4_79*SWr1[4]+ROcp4_89*SWr1[5]+ROcp4_99*SWr1[6]
  trq[1,9] = s.trq[1,9]+xtrq15-xfrc25*SWr1[9]+xfrc35*SWr1[8]
  trq[2,9] = s.trq[2,9]+xtrq25+xfrc15*SWr1[9]-xfrc35*SWr1[7]
  trq[3,9] = s.trq[3,9]+xtrq35-xfrc15*SWr1[8]+xfrc25*SWr1[7]

# = = Block_0_0_1_2_0_1 = = 
 
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
  OMcp5_16 = OMcp5_15+qd[6]*ROcp5_45
  OMcp5_26 = OMcp5_25+qd[6]*ROcp5_55
  OMcp5_36 = qd[4]+qd[6]*S5
  OPcp5_16 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp5_55-OMcp5_25*S5)-qdd[5]*C4-qdd[6]*ROcp5_45)
  OPcp5_26 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp5_45-OMcp5_15*S5)+qdd[5]*S4+qdd[6]*ROcp5_55
  OPcp5_36 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5

# = = Block_0_0_1_2_0_3 = = 
 
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
  OMcp5_110 = OMcp5_16+qd[10]*ROcp5_16
  OMcp5_210 = OMcp5_26+qd[10]*ROcp5_26
  OMcp5_310 = OMcp5_36+qd[10]*ROcp5_36
  ORcp5_110 = OMcp5_26*RLcp5_310-OMcp5_36*RLcp5_210
  ORcp5_210 = -(OMcp5_16*RLcp5_310-OMcp5_36*RLcp5_110)
  ORcp5_310 = OMcp5_16*RLcp5_210-OMcp5_26*RLcp5_110
  OPcp5_110 = OPcp5_16+qd[10]*(OMcp5_26*ROcp5_36-OMcp5_36*ROcp5_26)+qdd[10]*ROcp5_16
  OPcp5_210 = OPcp5_26-qd[10]*(OMcp5_16*ROcp5_36-OMcp5_36*ROcp5_16)+qdd[10]*ROcp5_26
  OPcp5_310 = OPcp5_36+qd[10]*(OMcp5_16*ROcp5_26-OMcp5_26*ROcp5_16)+qdd[10]*ROcp5_36
  RLcp5_111 = ROcp5_410*s.dpt[2,19]
  RLcp5_211 = ROcp5_510*s.dpt[2,19]
  RLcp5_311 = ROcp5_610*s.dpt[2,19]
  OMcp5_111 = OMcp5_110+qd[11]*ROcp5_710
  OMcp5_211 = OMcp5_210+qd[11]*ROcp5_810
  OMcp5_311 = OMcp5_310+qd[11]*ROcp5_910
  ORcp5_111 = OMcp5_210*RLcp5_311-OMcp5_310*RLcp5_211
  ORcp5_211 = -(OMcp5_110*RLcp5_311-OMcp5_310*RLcp5_111)
  ORcp5_311 = OMcp5_110*RLcp5_211-OMcp5_210*RLcp5_111
  PxF2[1] = q[1]+RLcp5_110+RLcp5_111
  PxF2[2] = q[2]+RLcp5_210+RLcp5_211
  PxF2[3] = q[3]+RLcp5_310+RLcp5_311
  RxF2[1,1] = ROcp5_111
  RxF2[1,2] = ROcp5_211
  RxF2[1,3] = ROcp5_311
  RxF2[2,1] = ROcp5_412
  RxF2[2,2] = ROcp5_512
  RxF2[2,3] = ROcp5_612
  RxF2[3,1] = ROcp5_712
  RxF2[3,2] = ROcp5_812
  RxF2[3,3] = ROcp5_912
  VxF2[1] = qd[1]+ORcp5_110+ORcp5_111
  VxF2[2] = qd[2]+ORcp5_210+ORcp5_211
  VxF2[3] = qd[3]+ORcp5_310+ORcp5_311
  OMxF2[1] = OMcp5_111+qd[12]*ROcp5_111
  OMxF2[2] = OMcp5_211+qd[12]*ROcp5_211
  OMxF2[3] = OMcp5_311+qd[12]*ROcp5_311
  AxF2[1] = qdd[1]+OMcp5_210*ORcp5_311+OMcp5_26*ORcp5_310-OMcp5_310*ORcp5_211-OMcp5_36*ORcp5_210+OPcp5_210*RLcp5_311+\
   OPcp5_26*RLcp5_310-OPcp5_310*RLcp5_211-OPcp5_36*RLcp5_210
  AxF2[2] = qdd[2]-OMcp5_110*ORcp5_311-OMcp5_16*ORcp5_310+OMcp5_310*ORcp5_111+OMcp5_36*ORcp5_110-OPcp5_110*RLcp5_311-\
   OPcp5_16*RLcp5_310+OPcp5_310*RLcp5_111+OPcp5_36*RLcp5_110
  AxF2[3] = qdd[3]+OMcp5_110*ORcp5_211+OMcp5_16*ORcp5_210-OMcp5_210*ORcp5_111-OMcp5_26*ORcp5_110+OPcp5_110*RLcp5_211+\
   OPcp5_16*RLcp5_210-OPcp5_210*RLcp5_111-OPcp5_26*RLcp5_110
  OMPxF2[1] = OPcp5_110+qd[11]*(OMcp5_210*ROcp5_910-OMcp5_310*ROcp5_810)+qd[12]*(OMcp5_211*ROcp5_311-OMcp5_311*ROcp5_211\
   )+qdd[11]*ROcp5_710+qdd[12]*ROcp5_111
  OMPxF2[2] = OPcp5_210-qd[11]*(OMcp5_110*ROcp5_910-OMcp5_310*ROcp5_710)-qd[12]*(OMcp5_111*ROcp5_311-OMcp5_311*ROcp5_111\
   )+qdd[11]*ROcp5_810+qdd[12]*ROcp5_211
  OMPxF2[3] = OPcp5_310+qd[11]*(OMcp5_110*ROcp5_810-OMcp5_210*ROcp5_710)+qd[12]*(OMcp5_111*ROcp5_211-OMcp5_211*ROcp5_111\
   )+qdd[11]*ROcp5_910+qdd[12]*ROcp5_311
 
# Sensor Forces Computation 

  SWr2 = s.user_ExtForces(PxF2,RxF2,VxF2,OMxF2,AxF2,OMPxF2,s,tsim,2)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc16 = ROcp5_111*SWr2[1]+ROcp5_211*SWr2[2]+ROcp5_311*SWr2[3]
  xfrc26 = ROcp5_412*SWr2[1]+ROcp5_512*SWr2[2]+ROcp5_612*SWr2[3]
  xfrc36 = ROcp5_712*SWr2[1]+ROcp5_812*SWr2[2]+ROcp5_912*SWr2[3]
  frc[1,12] = s.frc[1,12]+xfrc16
  frc[2,12] = s.frc[2,12]+xfrc26
  frc[3,12] = s.frc[3,12]+xfrc36
  xtrq16 = ROcp5_111*SWr2[4]+ROcp5_211*SWr2[5]+ROcp5_311*SWr2[6]
  xtrq26 = ROcp5_412*SWr2[4]+ROcp5_512*SWr2[5]+ROcp5_612*SWr2[6]
  xtrq36 = ROcp5_712*SWr2[4]+ROcp5_812*SWr2[5]+ROcp5_912*SWr2[6]
  trq[1,12] = s.trq[1,12]+xtrq16-xfrc26*SWr2[9]+xfrc36*SWr2[8]
  trq[2,12] = s.trq[2,12]+xtrq26+xfrc16*SWr2[9]-xfrc36*SWr2[7]
  trq[3,12] = s.trq[3,12]+xtrq36-xfrc16*SWr2[8]+xfrc26*SWr2[7]

# = = Block_0_0_1_3_0_1 = = 
 
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
  OMcp6_16 = OMcp6_15+qd[6]*ROcp6_45
  OMcp6_26 = OMcp6_25+qd[6]*ROcp6_55
  OMcp6_36 = qd[4]+qd[6]*S5
  OPcp6_16 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp6_55-OMcp6_25*S5)-qdd[5]*C4-qdd[6]*ROcp6_45)
  OPcp6_26 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp6_45-OMcp6_15*S5)+qdd[5]*S4+qdd[6]*ROcp6_55
  OPcp6_36 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5

# = = Block_0_0_1_3_0_4 = = 
 
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
  OMcp6_113 = OMcp6_16+qd[13]*ROcp6_16
  OMcp6_213 = OMcp6_26+qd[13]*ROcp6_26
  OMcp6_313 = OMcp6_36+qd[13]*ROcp6_36
  ORcp6_113 = OMcp6_26*RLcp6_313-OMcp6_36*RLcp6_213
  ORcp6_213 = -(OMcp6_16*RLcp6_313-OMcp6_36*RLcp6_113)
  ORcp6_313 = OMcp6_16*RLcp6_213-OMcp6_26*RLcp6_113
  OPcp6_113 = OPcp6_16+qd[13]*(OMcp6_26*ROcp6_36-OMcp6_36*ROcp6_26)+qdd[13]*ROcp6_16
  OPcp6_213 = OPcp6_26-qd[13]*(OMcp6_16*ROcp6_36-OMcp6_36*ROcp6_16)+qdd[13]*ROcp6_26
  OPcp6_313 = OPcp6_36+qd[13]*(OMcp6_16*ROcp6_26-OMcp6_26*ROcp6_16)+qdd[13]*ROcp6_36
  RLcp6_114 = ROcp6_413*s.dpt[2,24]
  RLcp6_214 = ROcp6_513*s.dpt[2,24]
  RLcp6_314 = ROcp6_613*s.dpt[2,24]
  OMcp6_114 = OMcp6_113+qd[14]*ROcp6_16
  OMcp6_214 = OMcp6_213+qd[14]*ROcp6_26
  OMcp6_314 = OMcp6_313+qd[14]*ROcp6_36
  ORcp6_114 = OMcp6_213*RLcp6_314-OMcp6_313*RLcp6_214
  ORcp6_214 = -(OMcp6_113*RLcp6_314-OMcp6_313*RLcp6_114)
  ORcp6_314 = OMcp6_113*RLcp6_214-OMcp6_213*RLcp6_114
  OPcp6_114 = OPcp6_113+qd[14]*(OMcp6_213*ROcp6_36-OMcp6_313*ROcp6_26)+qdd[14]*ROcp6_16
  OPcp6_214 = OPcp6_213-qd[14]*(OMcp6_113*ROcp6_36-OMcp6_313*ROcp6_16)+qdd[14]*ROcp6_26
  OPcp6_314 = OPcp6_313+qd[14]*(OMcp6_113*ROcp6_26-OMcp6_213*ROcp6_16)+qdd[14]*ROcp6_36
  RLcp6_115 = ROcp6_16*s.dpt[1,26]
  RLcp6_215 = ROcp6_26*s.dpt[1,26]
  RLcp6_315 = ROcp6_36*s.dpt[1,26]
  ORcp6_115 = OMcp6_214*RLcp6_315-OMcp6_314*RLcp6_215
  ORcp6_215 = -(OMcp6_114*RLcp6_315-OMcp6_314*RLcp6_115)
  ORcp6_315 = OMcp6_114*RLcp6_215-OMcp6_214*RLcp6_115
  PxF3[1] = q[1]+RLcp6_113+RLcp6_114+RLcp6_115
  PxF3[2] = q[2]+RLcp6_213+RLcp6_214+RLcp6_215
  PxF3[3] = q[3]+RLcp6_313+RLcp6_314+RLcp6_315
  RxF3[1,1] = ROcp6_16
  RxF3[1,2] = ROcp6_26
  RxF3[1,3] = ROcp6_36
  RxF3[2,1] = ROcp6_415
  RxF3[2,2] = ROcp6_515
  RxF3[2,3] = ROcp6_615
  RxF3[3,1] = ROcp6_715
  RxF3[3,2] = ROcp6_815
  RxF3[3,3] = ROcp6_915
  VxF3[1] = qd[1]+ORcp6_113+ORcp6_114+ORcp6_115
  VxF3[2] = qd[2]+ORcp6_213+ORcp6_214+ORcp6_215
  VxF3[3] = qd[3]+ORcp6_313+ORcp6_314+ORcp6_315
  OMxF3[1] = OMcp6_114+qd[15]*ROcp6_16
  OMxF3[2] = OMcp6_214+qd[15]*ROcp6_26
  OMxF3[3] = OMcp6_314+qd[15]*ROcp6_36
  AxF3[1] = qdd[1]+OMcp6_213*ORcp6_314+OMcp6_214*ORcp6_315+OMcp6_26*ORcp6_313-OMcp6_313*ORcp6_214-OMcp6_314*ORcp6_215-\
   OMcp6_36*ORcp6_213+OPcp6_213*RLcp6_314+OPcp6_214*RLcp6_315+OPcp6_26*RLcp6_313-OPcp6_313*RLcp6_214-OPcp6_314*RLcp6_215-\
   OPcp6_36*RLcp6_213
  AxF3[2] = qdd[2]-OMcp6_113*ORcp6_314-OMcp6_114*ORcp6_315-OMcp6_16*ORcp6_313+OMcp6_313*ORcp6_114+OMcp6_314*ORcp6_115+\
   OMcp6_36*ORcp6_113-OPcp6_113*RLcp6_314-OPcp6_114*RLcp6_315-OPcp6_16*RLcp6_313+OPcp6_313*RLcp6_114+OPcp6_314*RLcp6_115+\
   OPcp6_36*RLcp6_113
  AxF3[3] = qdd[3]+OMcp6_113*ORcp6_214+OMcp6_114*ORcp6_215+OMcp6_16*ORcp6_213-OMcp6_213*ORcp6_114-OMcp6_214*ORcp6_115-\
   OMcp6_26*ORcp6_113+OPcp6_113*RLcp6_214+OPcp6_114*RLcp6_215+OPcp6_16*RLcp6_213-OPcp6_213*RLcp6_114-OPcp6_214*RLcp6_115-\
   OPcp6_26*RLcp6_113
  OMPxF3[1] = OPcp6_114+qd[15]*(OMcp6_214*ROcp6_36-OMcp6_314*ROcp6_26)+qdd[15]*ROcp6_16
  OMPxF3[2] = OPcp6_214-qd[15]*(OMcp6_114*ROcp6_36-OMcp6_314*ROcp6_16)+qdd[15]*ROcp6_26
  OMPxF3[3] = OPcp6_314+qd[15]*(OMcp6_114*ROcp6_26-OMcp6_214*ROcp6_16)+qdd[15]*ROcp6_36
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc17 = ROcp6_16*SWr3[1]+ROcp6_26*SWr3[2]+ROcp6_36*SWr3[3]
  xfrc27 = ROcp6_415*SWr3[1]+ROcp6_515*SWr3[2]+ROcp6_615*SWr3[3]
  xfrc37 = ROcp6_715*SWr3[1]+ROcp6_815*SWr3[2]+ROcp6_915*SWr3[3]
  frc[1,15] = s.frc[1,15]+xfrc17
  frc[2,15] = s.frc[2,15]+xfrc27
  frc[3,15] = s.frc[3,15]+xfrc37
  xtrq17 = ROcp6_16*SWr3[4]+ROcp6_26*SWr3[5]+ROcp6_36*SWr3[6]
  xtrq27 = ROcp6_415*SWr3[4]+ROcp6_515*SWr3[5]+ROcp6_615*SWr3[6]
  xtrq37 = ROcp6_715*SWr3[4]+ROcp6_815*SWr3[5]+ROcp6_915*SWr3[6]
  trq[1,15] = s.trq[1,15]+xtrq17-xfrc27*SWr3[9]+xfrc37*SWr3[8]
  trq[2,15] = s.trq[2,15]+xtrq27+xfrc17*SWr3[9]-xfrc37*SWr3[7]
  trq[3,15] = s.trq[3,15]+xtrq37-xfrc17*SWr3[8]+xfrc27*SWr3[7]

# = = Block_0_0_1_4_0_1 = = 
 
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
  OMcp7_16 = OMcp7_15+qd[6]*ROcp7_45
  OMcp7_26 = OMcp7_25+qd[6]*ROcp7_55
  OMcp7_36 = qd[4]+qd[6]*S5
  OPcp7_16 = -(qd[4]*qd[5]*S4+qd[6]*(qd[4]*ROcp7_55-OMcp7_25*S5)-qdd[5]*C4-qdd[6]*ROcp7_45)
  OPcp7_26 = qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp7_45-OMcp7_15*S5)+qdd[5]*S4+qdd[6]*ROcp7_55
  OPcp7_36 = qdd[4]+qd[5]*qd[6]*C5+qdd[6]*S5

# = = Block_0_0_1_4_0_5 = = 
 
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
  OMcp7_116 = OMcp7_16+qd[16]*ROcp7_16
  OMcp7_216 = OMcp7_26+qd[16]*ROcp7_26
  OMcp7_316 = OMcp7_36+qd[16]*ROcp7_36
  ORcp7_116 = OMcp7_26*RLcp7_316-OMcp7_36*RLcp7_216
  ORcp7_216 = -(OMcp7_16*RLcp7_316-OMcp7_36*RLcp7_116)
  ORcp7_316 = OMcp7_16*RLcp7_216-OMcp7_26*RLcp7_116
  OPcp7_116 = OPcp7_16+qd[16]*(OMcp7_26*ROcp7_36-OMcp7_36*ROcp7_26)+qdd[16]*ROcp7_16
  OPcp7_216 = OPcp7_26-qd[16]*(OMcp7_16*ROcp7_36-OMcp7_36*ROcp7_16)+qdd[16]*ROcp7_26
  OPcp7_316 = OPcp7_36+qd[16]*(OMcp7_16*ROcp7_26-OMcp7_26*ROcp7_16)+qdd[16]*ROcp7_36
  RLcp7_117 = ROcp7_416*s.dpt[2,30]
  RLcp7_217 = ROcp7_516*s.dpt[2,30]
  RLcp7_317 = ROcp7_616*s.dpt[2,30]
  OMcp7_117 = OMcp7_116+qd[17]*ROcp7_16
  OMcp7_217 = OMcp7_216+qd[17]*ROcp7_26
  OMcp7_317 = OMcp7_316+qd[17]*ROcp7_36
  ORcp7_117 = OMcp7_216*RLcp7_317-OMcp7_316*RLcp7_217
  ORcp7_217 = -(OMcp7_116*RLcp7_317-OMcp7_316*RLcp7_117)
  ORcp7_317 = OMcp7_116*RLcp7_217-OMcp7_216*RLcp7_117
  OPcp7_117 = OPcp7_116+qd[17]*(OMcp7_216*ROcp7_36-OMcp7_316*ROcp7_26)+qdd[17]*ROcp7_16
  OPcp7_217 = OPcp7_216-qd[17]*(OMcp7_116*ROcp7_36-OMcp7_316*ROcp7_16)+qdd[17]*ROcp7_26
  OPcp7_317 = OPcp7_316+qd[17]*(OMcp7_116*ROcp7_26-OMcp7_216*ROcp7_16)+qdd[17]*ROcp7_36
  RLcp7_118 = ROcp7_16*s.dpt[1,34]
  RLcp7_218 = ROcp7_26*s.dpt[1,34]
  RLcp7_318 = ROcp7_36*s.dpt[1,34]
  ORcp7_118 = OMcp7_217*RLcp7_318-OMcp7_317*RLcp7_218
  ORcp7_218 = -(OMcp7_117*RLcp7_318-OMcp7_317*RLcp7_118)
  ORcp7_318 = OMcp7_117*RLcp7_218-OMcp7_217*RLcp7_118
  PxF4[1] = q[1]+RLcp7_116+RLcp7_117+RLcp7_118
  PxF4[2] = q[2]+RLcp7_216+RLcp7_217+RLcp7_218
  PxF4[3] = q[3]+RLcp7_316+RLcp7_317+RLcp7_318
  RxF4[1,1] = ROcp7_16
  RxF4[1,2] = ROcp7_26
  RxF4[1,3] = ROcp7_36
  RxF4[2,1] = ROcp7_418
  RxF4[2,2] = ROcp7_518
  RxF4[2,3] = ROcp7_618
  RxF4[3,1] = ROcp7_718
  RxF4[3,2] = ROcp7_818
  RxF4[3,3] = ROcp7_918
  VxF4[1] = qd[1]+ORcp7_116+ORcp7_117+ORcp7_118
  VxF4[2] = qd[2]+ORcp7_216+ORcp7_217+ORcp7_218
  VxF4[3] = qd[3]+ORcp7_316+ORcp7_317+ORcp7_318
  OMxF4[1] = OMcp7_117+qd[18]*ROcp7_16
  OMxF4[2] = OMcp7_217+qd[18]*ROcp7_26
  OMxF4[3] = OMcp7_317+qd[18]*ROcp7_36
  AxF4[1] = qdd[1]+OMcp7_216*ORcp7_317+OMcp7_217*ORcp7_318+OMcp7_26*ORcp7_316-OMcp7_316*ORcp7_217-OMcp7_317*ORcp7_218-\
   OMcp7_36*ORcp7_216+OPcp7_216*RLcp7_317+OPcp7_217*RLcp7_318+OPcp7_26*RLcp7_316-OPcp7_316*RLcp7_217-OPcp7_317*RLcp7_218-\
   OPcp7_36*RLcp7_216
  AxF4[2] = qdd[2]-OMcp7_116*ORcp7_317-OMcp7_117*ORcp7_318-OMcp7_16*ORcp7_316+OMcp7_316*ORcp7_117+OMcp7_317*ORcp7_118+\
   OMcp7_36*ORcp7_116-OPcp7_116*RLcp7_317-OPcp7_117*RLcp7_318-OPcp7_16*RLcp7_316+OPcp7_316*RLcp7_117+OPcp7_317*RLcp7_118+\
   OPcp7_36*RLcp7_116
  AxF4[3] = qdd[3]+OMcp7_116*ORcp7_217+OMcp7_117*ORcp7_218+OMcp7_16*ORcp7_216-OMcp7_216*ORcp7_117-OMcp7_217*ORcp7_118-\
   OMcp7_26*ORcp7_116+OPcp7_116*RLcp7_217+OPcp7_117*RLcp7_218+OPcp7_16*RLcp7_216-OPcp7_216*RLcp7_117-OPcp7_217*RLcp7_118-\
   OPcp7_26*RLcp7_116
  OMPxF4[1] = OPcp7_117+qd[18]*(OMcp7_217*ROcp7_36-OMcp7_317*ROcp7_26)+qdd[18]*ROcp7_16
  OMPxF4[2] = OPcp7_217-qd[18]*(OMcp7_117*ROcp7_36-OMcp7_317*ROcp7_16)+qdd[18]*ROcp7_26
  OMPxF4[3] = OPcp7_317+qd[18]*(OMcp7_117*ROcp7_26-OMcp7_217*ROcp7_16)+qdd[18]*ROcp7_36
 
# Sensor Forces Computation 

  SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc18 = ROcp7_16*SWr4[1]+ROcp7_26*SWr4[2]+ROcp7_36*SWr4[3]
  xfrc28 = ROcp7_418*SWr4[1]+ROcp7_518*SWr4[2]+ROcp7_618*SWr4[3]
  xfrc38 = ROcp7_718*SWr4[1]+ROcp7_818*SWr4[2]+ROcp7_918*SWr4[3]
  frc[1,18] = s.frc[1,18]+xfrc18
  frc[2,18] = s.frc[2,18]+xfrc28
  frc[3,18] = s.frc[3,18]+xfrc38
  xtrq18 = ROcp7_16*SWr4[4]+ROcp7_26*SWr4[5]+ROcp7_36*SWr4[6]
  xtrq28 = ROcp7_418*SWr4[4]+ROcp7_518*SWr4[5]+ROcp7_618*SWr4[6]
  xtrq38 = ROcp7_718*SWr4[4]+ROcp7_818*SWr4[5]+ROcp7_918*SWr4[6]
  trq[1,18] = s.trq[1,18]+xtrq18-xfrc28*SWr4[9]+xfrc38*SWr4[8]
  trq[2,18] = s.trq[2,18]+xtrq28+xfrc18*SWr4[9]-xfrc38*SWr4[7]
  trq[3,18] = s.trq[3,18]+xtrq38-xfrc18*SWr4[8]+xfrc28*SWr4[7]

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

  

