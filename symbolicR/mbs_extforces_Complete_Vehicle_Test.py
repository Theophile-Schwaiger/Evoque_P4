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
#	==> Function : F19 : External Forces
#	==> Flops complexity : 1632
#
#	==> Generation Time :  0.020 seconds
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
  ROcp0_110 = ROcp0_18*C10-ROcp0_79*S10
  ROcp0_210 = ROcp0_28*C10-ROcp0_89*S10
  ROcp0_310 = ROcp0_38*C10-ROcp0_99*S10
  ROcp0_710 = ROcp0_18*S10+ROcp0_79*C10
  ROcp0_810 = ROcp0_28*S10+ROcp0_89*C10
  ROcp0_910 = ROcp0_38*S10+ROcp0_99*C10
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
  OMcp0_19 = OMcp0_18+qd[9]*ROcp0_18
  OMcp0_29 = OMcp0_28+qd[9]*ROcp0_28
  OMcp0_39 = OMcp0_38+qd[9]*ROcp0_38
  PxF1[1] = q[1]+RLcp0_17+RLcp0_18
  PxF1[2] = q[2]+RLcp0_27+RLcp0_28
  PxF1[3] = q[3]+RLcp0_37+RLcp0_38
  RxF1[1,1] = ROcp0_110
  RxF1[1,2] = ROcp0_210
  RxF1[1,3] = ROcp0_310
  RxF1[2,1] = ROcp0_49
  RxF1[2,2] = ROcp0_59
  RxF1[2,3] = ROcp0_69
  RxF1[3,1] = ROcp0_710
  RxF1[3,2] = ROcp0_810
  RxF1[3,3] = ROcp0_910
  VxF1[1] = qd[1]+ORcp0_17+ORcp0_18
  VxF1[2] = qd[2]+ORcp0_27+ORcp0_28
  VxF1[3] = qd[3]+ORcp0_37+ORcp0_38
  OMxF1[1] = OMcp0_19+qd[10]*ROcp0_49
  OMxF1[2] = OMcp0_29+qd[10]*ROcp0_59
  OMxF1[3] = OMcp0_39+qd[10]*ROcp0_69
  AxF1[1] = qdd[1]+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_36*ORcp0_27-OMcp0_37*ORcp0_28+OPcp0_26*RLcp0_37+OPcp0_27*\
   RLcp0_38-OPcp0_36*RLcp0_27-OPcp0_37*RLcp0_28
  AxF1[2] = qdd[2]-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_36*ORcp0_17+OMcp0_37*ORcp0_18-OPcp0_16*RLcp0_37-OPcp0_17*\
   RLcp0_38+OPcp0_36*RLcp0_17+OPcp0_37*RLcp0_18
  AxF1[3] = qdd[3]+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_26*ORcp0_17-OMcp0_27*ORcp0_18+OPcp0_16*RLcp0_27+OPcp0_17*\
   RLcp0_28-OPcp0_26*RLcp0_17-OPcp0_27*RLcp0_18
  OMPxF1[1] = OPcp0_17+qd[10]*(OMcp0_29*ROcp0_69-OMcp0_39*ROcp0_59)+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(\
   OMcp0_28*ROcp0_38-OMcp0_38*ROcp0_28)+qdd[10]*ROcp0_49+qdd[8]*ROcp0_77+qdd[9]*ROcp0_18
  OMPxF1[2] = OPcp0_27-qd[10]*(OMcp0_19*ROcp0_69-OMcp0_39*ROcp0_49)-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(\
   OMcp0_18*ROcp0_38-OMcp0_38*ROcp0_18)+qdd[10]*ROcp0_59+qdd[8]*ROcp0_87+qdd[9]*ROcp0_28
  OMPxF1[3] = OPcp0_37+qd[10]*(OMcp0_19*ROcp0_59-OMcp0_29*ROcp0_49)+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(\
   OMcp0_18*ROcp0_28-OMcp0_28*ROcp0_18)+qdd[10]*ROcp0_69+qdd[8]*ROcp0_97+qdd[9]*ROcp0_38
 
# Sensor Forces Computation 

  SWr1 = s.user_ExtForces(PxF1,RxF1,VxF1,OMxF1,AxF1,OMPxF1,s,tsim,1)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc11 = ROcp0_110*SWr1[1]+ROcp0_210*SWr1[2]+ROcp0_310*SWr1[3]
  xfrc21 = ROcp0_49*SWr1[1]+ROcp0_59*SWr1[2]+ROcp0_69*SWr1[3]
  xfrc31 = ROcp0_710*SWr1[1]+ROcp0_810*SWr1[2]+ROcp0_910*SWr1[3]
  frc[1,10] = s.frc[1,10]+xfrc11
  frc[2,10] = s.frc[2,10]+xfrc21
  frc[3,10] = s.frc[3,10]+xfrc31
  xtrq11 = ROcp0_110*SWr1[4]+ROcp0_210*SWr1[5]+ROcp0_310*SWr1[6]
  xtrq21 = ROcp0_49*SWr1[4]+ROcp0_59*SWr1[5]+ROcp0_69*SWr1[6]
  xtrq31 = ROcp0_710*SWr1[4]+ROcp0_810*SWr1[5]+ROcp0_910*SWr1[6]
  trq[1,10] = s.trq[1,10]+xtrq11-xfrc21*SWr1[9]+xfrc31*SWr1[8]
  trq[2,10] = s.trq[2,10]+xtrq21+xfrc11*SWr1[9]-xfrc31*SWr1[7]
  trq[3,10] = s.trq[3,10]+xtrq31-xfrc11*SWr1[8]+xfrc21*SWr1[7]

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


  ROcp1_411 = ROcp1_46*C11+S11*S5
  ROcp1_511 = ROcp1_56*C11+ROcp1_85*S11
  ROcp1_611 = ROcp1_66*C11+ROcp1_95*S11
  ROcp1_711 = -(ROcp1_46*S11-C11*S5)
  ROcp1_811 = -(ROcp1_56*S11-ROcp1_85*C11)
  ROcp1_911 = -(ROcp1_66*S11-ROcp1_95*C11)
  ROcp1_112 = ROcp1_16*C12+ROcp1_411*S12
  ROcp1_212 = ROcp1_26*C12+ROcp1_511*S12
  ROcp1_312 = ROcp1_36*C12+ROcp1_611*S12
  ROcp1_412 = -(ROcp1_16*S12-ROcp1_411*C12)
  ROcp1_512 = -(ROcp1_26*S12-ROcp1_511*C12)
  ROcp1_612 = -(ROcp1_36*S12-ROcp1_611*C12)
  ROcp1_413 = ROcp1_412*C13+ROcp1_711*S13
  ROcp1_513 = ROcp1_512*C13+ROcp1_811*S13
  ROcp1_613 = ROcp1_612*C13+ROcp1_911*S13
  ROcp1_713 = -(ROcp1_412*S13-ROcp1_711*C13)
  ROcp1_813 = -(ROcp1_512*S13-ROcp1_811*C13)
  ROcp1_913 = -(ROcp1_612*S13-ROcp1_911*C13)
  ROcp1_114 = ROcp1_112*C14-ROcp1_713*S14
  ROcp1_214 = ROcp1_212*C14-ROcp1_813*S14
  ROcp1_314 = ROcp1_312*C14-ROcp1_913*S14
  ROcp1_714 = ROcp1_112*S14+ROcp1_713*C14
  ROcp1_814 = ROcp1_212*S14+ROcp1_813*C14
  ROcp1_914 = ROcp1_312*S14+ROcp1_913*C14
  RLcp1_111 = ROcp1_16*s.dpt[1,4]+ROcp1_46*s.dpt[2,4]+s.dpt[3,4]*S5
  RLcp1_211 = ROcp1_26*s.dpt[1,4]+ROcp1_56*s.dpt[2,4]+ROcp1_85*s.dpt[3,4]
  RLcp1_311 = ROcp1_36*s.dpt[1,4]+ROcp1_66*s.dpt[2,4]+ROcp1_95*s.dpt[3,4]
  OMcp1_111 = OMcp1_16+qd[11]*ROcp1_16
  OMcp1_211 = OMcp1_26+qd[11]*ROcp1_26
  OMcp1_311 = OMcp1_36+qd[11]*ROcp1_36
  ORcp1_111 = OMcp1_26*RLcp1_311-OMcp1_36*RLcp1_211
  ORcp1_211 = -(OMcp1_16*RLcp1_311-OMcp1_36*RLcp1_111)
  ORcp1_311 = OMcp1_16*RLcp1_211-OMcp1_26*RLcp1_111
  OPcp1_111 = OPcp1_16+qd[11]*(OMcp1_26*ROcp1_36-OMcp1_36*ROcp1_26)+qdd[11]*ROcp1_16
  OPcp1_211 = OPcp1_26-qd[11]*(OMcp1_16*ROcp1_36-OMcp1_36*ROcp1_16)+qdd[11]*ROcp1_26
  OPcp1_311 = OPcp1_36+qd[11]*(OMcp1_16*ROcp1_26-OMcp1_26*ROcp1_16)+qdd[11]*ROcp1_36
  RLcp1_112 = ROcp1_411*s.dpt[2,17]
  RLcp1_212 = ROcp1_511*s.dpt[2,17]
  RLcp1_312 = ROcp1_611*s.dpt[2,17]
  OMcp1_112 = OMcp1_111+qd[12]*ROcp1_711
  OMcp1_212 = OMcp1_211+qd[12]*ROcp1_811
  OMcp1_312 = OMcp1_311+qd[12]*ROcp1_911
  ORcp1_112 = OMcp1_211*RLcp1_312-OMcp1_311*RLcp1_212
  ORcp1_212 = -(OMcp1_111*RLcp1_312-OMcp1_311*RLcp1_112)
  ORcp1_312 = OMcp1_111*RLcp1_212-OMcp1_211*RLcp1_112
  OMcp1_113 = OMcp1_112+qd[13]*ROcp1_112
  OMcp1_213 = OMcp1_212+qd[13]*ROcp1_212
  OMcp1_313 = OMcp1_312+qd[13]*ROcp1_312
  PxF2[1] = q[1]+RLcp1_111+RLcp1_112
  PxF2[2] = q[2]+RLcp1_211+RLcp1_212
  PxF2[3] = q[3]+RLcp1_311+RLcp1_312
  RxF2[1,1] = ROcp1_114
  RxF2[1,2] = ROcp1_214
  RxF2[1,3] = ROcp1_314
  RxF2[2,1] = ROcp1_413
  RxF2[2,2] = ROcp1_513
  RxF2[2,3] = ROcp1_613
  RxF2[3,1] = ROcp1_714
  RxF2[3,2] = ROcp1_814
  RxF2[3,3] = ROcp1_914
  VxF2[1] = qd[1]+ORcp1_111+ORcp1_112
  VxF2[2] = qd[2]+ORcp1_211+ORcp1_212
  VxF2[3] = qd[3]+ORcp1_311+ORcp1_312
  OMxF2[1] = OMcp1_113+qd[14]*ROcp1_413
  OMxF2[2] = OMcp1_213+qd[14]*ROcp1_513
  OMxF2[3] = OMcp1_313+qd[14]*ROcp1_613
  AxF2[1] = qdd[1]+OMcp1_211*ORcp1_312+OMcp1_26*ORcp1_311-OMcp1_311*ORcp1_212-OMcp1_36*ORcp1_211+OPcp1_211*RLcp1_312+\
   OPcp1_26*RLcp1_311-OPcp1_311*RLcp1_212-OPcp1_36*RLcp1_211
  AxF2[2] = qdd[2]-OMcp1_111*ORcp1_312-OMcp1_16*ORcp1_311+OMcp1_311*ORcp1_112+OMcp1_36*ORcp1_111-OPcp1_111*RLcp1_312-\
   OPcp1_16*RLcp1_311+OPcp1_311*RLcp1_112+OPcp1_36*RLcp1_111
  AxF2[3] = qdd[3]+OMcp1_111*ORcp1_212+OMcp1_16*ORcp1_211-OMcp1_211*ORcp1_112-OMcp1_26*ORcp1_111+OPcp1_111*RLcp1_212+\
   OPcp1_16*RLcp1_211-OPcp1_211*RLcp1_112-OPcp1_26*RLcp1_111
  OMPxF2[1] = OPcp1_111+qd[12]*(OMcp1_211*ROcp1_911-OMcp1_311*ROcp1_811)+qd[13]*(OMcp1_212*ROcp1_312-OMcp1_312*ROcp1_212\
   )+qd[14]*(OMcp1_213*ROcp1_613-OMcp1_313*ROcp1_513)+qdd[12]*ROcp1_711+qdd[13]*ROcp1_112+qdd[14]*ROcp1_413
  OMPxF2[2] = OPcp1_211-qd[12]*(OMcp1_111*ROcp1_911-OMcp1_311*ROcp1_711)-qd[13]*(OMcp1_112*ROcp1_312-OMcp1_312*ROcp1_112\
   )-qd[14]*(OMcp1_113*ROcp1_613-OMcp1_313*ROcp1_413)+qdd[12]*ROcp1_811+qdd[13]*ROcp1_212+qdd[14]*ROcp1_513
  OMPxF2[3] = OPcp1_311+qd[12]*(OMcp1_111*ROcp1_811-OMcp1_211*ROcp1_711)+qd[13]*(OMcp1_112*ROcp1_212-OMcp1_212*ROcp1_112\
   )+qd[14]*(OMcp1_113*ROcp1_513-OMcp1_213*ROcp1_413)+qdd[12]*ROcp1_911+qdd[13]*ROcp1_312+qdd[14]*ROcp1_613
 
# Sensor Forces Computation 

  SWr2 = s.user_ExtForces(PxF2,RxF2,VxF2,OMxF2,AxF2,OMPxF2,s,tsim,2)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc12 = ROcp1_114*SWr2[1]+ROcp1_214*SWr2[2]+ROcp1_314*SWr2[3]
  xfrc22 = ROcp1_413*SWr2[1]+ROcp1_513*SWr2[2]+ROcp1_613*SWr2[3]
  xfrc32 = ROcp1_714*SWr2[1]+ROcp1_814*SWr2[2]+ROcp1_914*SWr2[3]
  frc[1,14] = s.frc[1,14]+xfrc12
  frc[2,14] = s.frc[2,14]+xfrc22
  frc[3,14] = s.frc[3,14]+xfrc32
  xtrq12 = ROcp1_114*SWr2[4]+ROcp1_214*SWr2[5]+ROcp1_314*SWr2[6]
  xtrq22 = ROcp1_413*SWr2[4]+ROcp1_513*SWr2[5]+ROcp1_613*SWr2[6]
  xtrq32 = ROcp1_714*SWr2[4]+ROcp1_814*SWr2[5]+ROcp1_914*SWr2[6]
  trq[1,14] = s.trq[1,14]+xtrq12-xfrc22*SWr2[9]+xfrc32*SWr2[8]
  trq[2,14] = s.trq[2,14]+xtrq22+xfrc12*SWr2[9]-xfrc32*SWr2[7]
  trq[3,14] = s.trq[3,14]+xtrq32-xfrc12*SWr2[8]+xfrc22*SWr2[7]

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


  ROcp2_415 = ROcp2_46*C15+S15*S5
  ROcp2_515 = ROcp2_56*C15+ROcp2_85*S15
  ROcp2_615 = ROcp2_66*C15+ROcp2_95*S15
  ROcp2_715 = -(ROcp2_46*S15-C15*S5)
  ROcp2_815 = -(ROcp2_56*S15-ROcp2_85*C15)
  ROcp2_915 = -(ROcp2_66*S15-ROcp2_95*C15)
  ROcp2_416 = ROcp2_415*C16+ROcp2_715*S16
  ROcp2_516 = ROcp2_515*C16+ROcp2_815*S16
  ROcp2_616 = ROcp2_615*C16+ROcp2_915*S16
  ROcp2_716 = -(ROcp2_415*S16-ROcp2_715*C16)
  ROcp2_816 = -(ROcp2_515*S16-ROcp2_815*C16)
  ROcp2_916 = -(ROcp2_615*S16-ROcp2_915*C16)
  ROcp2_417 = ROcp2_416*C17+ROcp2_716*S17
  ROcp2_517 = ROcp2_516*C17+ROcp2_816*S17
  ROcp2_617 = ROcp2_616*C17+ROcp2_916*S17
  ROcp2_717 = -(ROcp2_416*S17-ROcp2_716*C17)
  ROcp2_817 = -(ROcp2_516*S17-ROcp2_816*C17)
  ROcp2_917 = -(ROcp2_616*S17-ROcp2_916*C17)
  ROcp2_118 = ROcp2_16*C18-ROcp2_717*S18
  ROcp2_218 = ROcp2_26*C18-ROcp2_817*S18
  ROcp2_318 = ROcp2_36*C18-ROcp2_917*S18
  ROcp2_718 = ROcp2_16*S18+ROcp2_717*C18
  ROcp2_818 = ROcp2_26*S18+ROcp2_817*C18
  ROcp2_918 = ROcp2_36*S18+ROcp2_917*C18
  RLcp2_115 = ROcp2_16*s.dpt[1,9]+ROcp2_46*s.dpt[2,9]+s.dpt[3,9]*S5
  RLcp2_215 = ROcp2_26*s.dpt[1,9]+ROcp2_56*s.dpt[2,9]+ROcp2_85*s.dpt[3,9]
  RLcp2_315 = ROcp2_36*s.dpt[1,9]+ROcp2_66*s.dpt[2,9]+ROcp2_95*s.dpt[3,9]
  OMcp2_115 = OMcp2_16+qd[15]*ROcp2_16
  OMcp2_215 = OMcp2_26+qd[15]*ROcp2_26
  OMcp2_315 = OMcp2_36+qd[15]*ROcp2_36
  ORcp2_115 = OMcp2_26*RLcp2_315-OMcp2_36*RLcp2_215
  ORcp2_215 = -(OMcp2_16*RLcp2_315-OMcp2_36*RLcp2_115)
  ORcp2_315 = OMcp2_16*RLcp2_215-OMcp2_26*RLcp2_115
  OPcp2_115 = OPcp2_16+qd[15]*(OMcp2_26*ROcp2_36-OMcp2_36*ROcp2_26)+qdd[15]*ROcp2_16
  OPcp2_215 = OPcp2_26-qd[15]*(OMcp2_16*ROcp2_36-OMcp2_36*ROcp2_16)+qdd[15]*ROcp2_26
  OPcp2_315 = OPcp2_36+qd[15]*(OMcp2_16*ROcp2_26-OMcp2_26*ROcp2_16)+qdd[15]*ROcp2_36
  RLcp2_116 = ROcp2_415*s.dpt[2,21]
  RLcp2_216 = ROcp2_515*s.dpt[2,21]
  RLcp2_316 = ROcp2_615*s.dpt[2,21]
  OMcp2_116 = OMcp2_115+qd[16]*ROcp2_16
  OMcp2_216 = OMcp2_215+qd[16]*ROcp2_26
  OMcp2_316 = OMcp2_315+qd[16]*ROcp2_36
  ORcp2_116 = OMcp2_215*RLcp2_316-OMcp2_315*RLcp2_216
  ORcp2_216 = -(OMcp2_115*RLcp2_316-OMcp2_315*RLcp2_116)
  ORcp2_316 = OMcp2_115*RLcp2_216-OMcp2_215*RLcp2_116
  OPcp2_116 = OPcp2_115+qd[16]*(OMcp2_215*ROcp2_36-OMcp2_315*ROcp2_26)+qdd[16]*ROcp2_16
  OPcp2_216 = OPcp2_215-qd[16]*(OMcp2_115*ROcp2_36-OMcp2_315*ROcp2_16)+qdd[16]*ROcp2_26
  OPcp2_316 = OPcp2_315+qd[16]*(OMcp2_115*ROcp2_26-OMcp2_215*ROcp2_16)+qdd[16]*ROcp2_36
  RLcp2_117 = ROcp2_16*s.dpt[1,23]
  RLcp2_217 = ROcp2_26*s.dpt[1,23]
  RLcp2_317 = ROcp2_36*s.dpt[1,23]
  OMcp2_117 = OMcp2_116+qd[17]*ROcp2_16
  OMcp2_217 = OMcp2_216+qd[17]*ROcp2_26
  OMcp2_317 = OMcp2_316+qd[17]*ROcp2_36
  ORcp2_117 = OMcp2_216*RLcp2_317-OMcp2_316*RLcp2_217
  ORcp2_217 = -(OMcp2_116*RLcp2_317-OMcp2_316*RLcp2_117)
  ORcp2_317 = OMcp2_116*RLcp2_217-OMcp2_216*RLcp2_117
  PxF3[1] = q[1]+RLcp2_115+RLcp2_116+RLcp2_117
  PxF3[2] = q[2]+RLcp2_215+RLcp2_216+RLcp2_217
  PxF3[3] = q[3]+RLcp2_315+RLcp2_316+RLcp2_317
  RxF3[1,1] = ROcp2_118
  RxF3[1,2] = ROcp2_218
  RxF3[1,3] = ROcp2_318
  RxF3[2,1] = ROcp2_417
  RxF3[2,2] = ROcp2_517
  RxF3[2,3] = ROcp2_617
  RxF3[3,1] = ROcp2_718
  RxF3[3,2] = ROcp2_818
  RxF3[3,3] = ROcp2_918
  VxF3[1] = qd[1]+ORcp2_115+ORcp2_116+ORcp2_117
  VxF3[2] = qd[2]+ORcp2_215+ORcp2_216+ORcp2_217
  VxF3[3] = qd[3]+ORcp2_315+ORcp2_316+ORcp2_317
  OMxF3[1] = OMcp2_117+qd[18]*ROcp2_417
  OMxF3[2] = OMcp2_217+qd[18]*ROcp2_517
  OMxF3[3] = OMcp2_317+qd[18]*ROcp2_617
  AxF3[1] = qdd[1]+OMcp2_215*ORcp2_316+OMcp2_216*ORcp2_317+OMcp2_26*ORcp2_315-OMcp2_315*ORcp2_216-OMcp2_316*ORcp2_217-\
   OMcp2_36*ORcp2_215+OPcp2_215*RLcp2_316+OPcp2_216*RLcp2_317+OPcp2_26*RLcp2_315-OPcp2_315*RLcp2_216-OPcp2_316*RLcp2_217-\
   OPcp2_36*RLcp2_215
  AxF3[2] = qdd[2]-OMcp2_115*ORcp2_316-OMcp2_116*ORcp2_317-OMcp2_16*ORcp2_315+OMcp2_315*ORcp2_116+OMcp2_316*ORcp2_117+\
   OMcp2_36*ORcp2_115-OPcp2_115*RLcp2_316-OPcp2_116*RLcp2_317-OPcp2_16*RLcp2_315+OPcp2_315*RLcp2_116+OPcp2_316*RLcp2_117+\
   OPcp2_36*RLcp2_115
  AxF3[3] = qdd[3]+OMcp2_115*ORcp2_216+OMcp2_116*ORcp2_217+OMcp2_16*ORcp2_215-OMcp2_215*ORcp2_116-OMcp2_216*ORcp2_117-\
   OMcp2_26*ORcp2_115+OPcp2_115*RLcp2_216+OPcp2_116*RLcp2_217+OPcp2_16*RLcp2_215-OPcp2_215*RLcp2_116-OPcp2_216*RLcp2_117-\
   OPcp2_26*RLcp2_115
  OMPxF3[1] = OPcp2_116+qd[17]*(OMcp2_216*ROcp2_36-OMcp2_316*ROcp2_26)+qd[18]*(OMcp2_217*ROcp2_617-OMcp2_317*ROcp2_517)+\
   qdd[17]*ROcp2_16+qdd[18]*ROcp2_417
  OMPxF3[2] = OPcp2_216-qd[17]*(OMcp2_116*ROcp2_36-OMcp2_316*ROcp2_16)-qd[18]*(OMcp2_117*ROcp2_617-OMcp2_317*ROcp2_417)+\
   qdd[17]*ROcp2_26+qdd[18]*ROcp2_517
  OMPxF3[3] = OPcp2_316+qd[17]*(OMcp2_116*ROcp2_26-OMcp2_216*ROcp2_16)+qd[18]*(OMcp2_117*ROcp2_517-OMcp2_217*ROcp2_417)+\
   qdd[17]*ROcp2_36+qdd[18]*ROcp2_617
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc13 = ROcp2_118*SWr3[1]+ROcp2_218*SWr3[2]+ROcp2_318*SWr3[3]
  xfrc23 = ROcp2_417*SWr3[1]+ROcp2_517*SWr3[2]+ROcp2_617*SWr3[3]
  xfrc33 = ROcp2_718*SWr3[1]+ROcp2_818*SWr3[2]+ROcp2_918*SWr3[3]
  frc[1,18] = s.frc[1,18]+xfrc13
  frc[2,18] = s.frc[2,18]+xfrc23
  frc[3,18] = s.frc[3,18]+xfrc33
  xtrq13 = ROcp2_118*SWr3[4]+ROcp2_218*SWr3[5]+ROcp2_318*SWr3[6]
  xtrq23 = ROcp2_417*SWr3[4]+ROcp2_517*SWr3[5]+ROcp2_617*SWr3[6]
  xtrq33 = ROcp2_718*SWr3[4]+ROcp2_818*SWr3[5]+ROcp2_918*SWr3[6]
  trq[1,18] = s.trq[1,18]+xtrq13-xfrc23*SWr3[9]+xfrc33*SWr3[8]
  trq[2,18] = s.trq[2,18]+xtrq23+xfrc13*SWr3[9]-xfrc33*SWr3[7]
  trq[3,18] = s.trq[3,18]+xtrq33-xfrc13*SWr3[8]+xfrc23*SWr3[7]

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


  ROcp3_419 = ROcp3_46*C19+S19*S5
  ROcp3_519 = ROcp3_56*C19+ROcp3_85*S19
  ROcp3_619 = ROcp3_66*C19+ROcp3_95*S19
  ROcp3_719 = -(ROcp3_46*S19-C19*S5)
  ROcp3_819 = -(ROcp3_56*S19-ROcp3_85*C19)
  ROcp3_919 = -(ROcp3_66*S19-ROcp3_95*C19)
  ROcp3_420 = ROcp3_419*C20+ROcp3_719*S20
  ROcp3_520 = ROcp3_519*C20+ROcp3_819*S20
  ROcp3_620 = ROcp3_619*C20+ROcp3_919*S20
  ROcp3_720 = -(ROcp3_419*S20-ROcp3_719*C20)
  ROcp3_820 = -(ROcp3_519*S20-ROcp3_819*C20)
  ROcp3_920 = -(ROcp3_619*S20-ROcp3_919*C20)
  ROcp3_421 = ROcp3_420*C21+ROcp3_720*S21
  ROcp3_521 = ROcp3_520*C21+ROcp3_820*S21
  ROcp3_621 = ROcp3_620*C21+ROcp3_920*S21
  ROcp3_721 = -(ROcp3_420*S21-ROcp3_720*C21)
  ROcp3_821 = -(ROcp3_520*S21-ROcp3_820*C21)
  ROcp3_921 = -(ROcp3_620*S21-ROcp3_920*C21)
  ROcp3_122 = ROcp3_16*C22-ROcp3_721*S22
  ROcp3_222 = ROcp3_26*C22-ROcp3_821*S22
  ROcp3_322 = ROcp3_36*C22-ROcp3_921*S22
  ROcp3_722 = ROcp3_16*S22+ROcp3_721*C22
  ROcp3_822 = ROcp3_26*S22+ROcp3_821*C22
  ROcp3_922 = ROcp3_36*S22+ROcp3_921*C22
  RLcp3_119 = ROcp3_16*s.dpt[1,11]+ROcp3_46*s.dpt[2,11]+s.dpt[3,11]*S5
  RLcp3_219 = ROcp3_26*s.dpt[1,11]+ROcp3_56*s.dpt[2,11]+ROcp3_85*s.dpt[3,11]
  RLcp3_319 = ROcp3_36*s.dpt[1,11]+ROcp3_66*s.dpt[2,11]+ROcp3_95*s.dpt[3,11]
  OMcp3_119 = OMcp3_16+qd[19]*ROcp3_16
  OMcp3_219 = OMcp3_26+qd[19]*ROcp3_26
  OMcp3_319 = OMcp3_36+qd[19]*ROcp3_36
  ORcp3_119 = OMcp3_26*RLcp3_319-OMcp3_36*RLcp3_219
  ORcp3_219 = -(OMcp3_16*RLcp3_319-OMcp3_36*RLcp3_119)
  ORcp3_319 = OMcp3_16*RLcp3_219-OMcp3_26*RLcp3_119
  OPcp3_119 = OPcp3_16+qd[19]*(OMcp3_26*ROcp3_36-OMcp3_36*ROcp3_26)+qdd[19]*ROcp3_16
  OPcp3_219 = OPcp3_26-qd[19]*(OMcp3_16*ROcp3_36-OMcp3_36*ROcp3_16)+qdd[19]*ROcp3_26
  OPcp3_319 = OPcp3_36+qd[19]*(OMcp3_16*ROcp3_26-OMcp3_26*ROcp3_16)+qdd[19]*ROcp3_36
  RLcp3_120 = ROcp3_419*s.dpt[2,27]
  RLcp3_220 = ROcp3_519*s.dpt[2,27]
  RLcp3_320 = ROcp3_619*s.dpt[2,27]
  OMcp3_120 = OMcp3_119+qd[20]*ROcp3_16
  OMcp3_220 = OMcp3_219+qd[20]*ROcp3_26
  OMcp3_320 = OMcp3_319+qd[20]*ROcp3_36
  ORcp3_120 = OMcp3_219*RLcp3_320-OMcp3_319*RLcp3_220
  ORcp3_220 = -(OMcp3_119*RLcp3_320-OMcp3_319*RLcp3_120)
  ORcp3_320 = OMcp3_119*RLcp3_220-OMcp3_219*RLcp3_120
  OPcp3_120 = OPcp3_119+qd[20]*(OMcp3_219*ROcp3_36-OMcp3_319*ROcp3_26)+qdd[20]*ROcp3_16
  OPcp3_220 = OPcp3_219-qd[20]*(OMcp3_119*ROcp3_36-OMcp3_319*ROcp3_16)+qdd[20]*ROcp3_26
  OPcp3_320 = OPcp3_319+qd[20]*(OMcp3_119*ROcp3_26-OMcp3_219*ROcp3_16)+qdd[20]*ROcp3_36
  RLcp3_121 = ROcp3_16*s.dpt[1,31]
  RLcp3_221 = ROcp3_26*s.dpt[1,31]
  RLcp3_321 = ROcp3_36*s.dpt[1,31]
  OMcp3_121 = OMcp3_120+qd[21]*ROcp3_16
  OMcp3_221 = OMcp3_220+qd[21]*ROcp3_26
  OMcp3_321 = OMcp3_320+qd[21]*ROcp3_36
  ORcp3_121 = OMcp3_220*RLcp3_321-OMcp3_320*RLcp3_221
  ORcp3_221 = -(OMcp3_120*RLcp3_321-OMcp3_320*RLcp3_121)
  ORcp3_321 = OMcp3_120*RLcp3_221-OMcp3_220*RLcp3_121
  PxF4[1] = q[1]+RLcp3_119+RLcp3_120+RLcp3_121
  PxF4[2] = q[2]+RLcp3_219+RLcp3_220+RLcp3_221
  PxF4[3] = q[3]+RLcp3_319+RLcp3_320+RLcp3_321
  RxF4[1,1] = ROcp3_122
  RxF4[1,2] = ROcp3_222
  RxF4[1,3] = ROcp3_322
  RxF4[2,1] = ROcp3_421
  RxF4[2,2] = ROcp3_521
  RxF4[2,3] = ROcp3_621
  RxF4[3,1] = ROcp3_722
  RxF4[3,2] = ROcp3_822
  RxF4[3,3] = ROcp3_922
  VxF4[1] = qd[1]+ORcp3_119+ORcp3_120+ORcp3_121
  VxF4[2] = qd[2]+ORcp3_219+ORcp3_220+ORcp3_221
  VxF4[3] = qd[3]+ORcp3_319+ORcp3_320+ORcp3_321
  OMxF4[1] = OMcp3_121+qd[22]*ROcp3_421
  OMxF4[2] = OMcp3_221+qd[22]*ROcp3_521
  OMxF4[3] = OMcp3_321+qd[22]*ROcp3_621
  AxF4[1] = qdd[1]+OMcp3_219*ORcp3_320+OMcp3_220*ORcp3_321+OMcp3_26*ORcp3_319-OMcp3_319*ORcp3_220-OMcp3_320*ORcp3_221-\
   OMcp3_36*ORcp3_219+OPcp3_219*RLcp3_320+OPcp3_220*RLcp3_321+OPcp3_26*RLcp3_319-OPcp3_319*RLcp3_220-OPcp3_320*RLcp3_221-\
   OPcp3_36*RLcp3_219
  AxF4[2] = qdd[2]-OMcp3_119*ORcp3_320-OMcp3_120*ORcp3_321-OMcp3_16*ORcp3_319+OMcp3_319*ORcp3_120+OMcp3_320*ORcp3_121+\
   OMcp3_36*ORcp3_119-OPcp3_119*RLcp3_320-OPcp3_120*RLcp3_321-OPcp3_16*RLcp3_319+OPcp3_319*RLcp3_120+OPcp3_320*RLcp3_121+\
   OPcp3_36*RLcp3_119
  AxF4[3] = qdd[3]+OMcp3_119*ORcp3_220+OMcp3_120*ORcp3_221+OMcp3_16*ORcp3_219-OMcp3_219*ORcp3_120-OMcp3_220*ORcp3_121-\
   OMcp3_26*ORcp3_119+OPcp3_119*RLcp3_220+OPcp3_120*RLcp3_221+OPcp3_16*RLcp3_219-OPcp3_219*RLcp3_120-OPcp3_220*RLcp3_121-\
   OPcp3_26*RLcp3_119
  OMPxF4[1] = OPcp3_120+qd[21]*(OMcp3_220*ROcp3_36-OMcp3_320*ROcp3_26)+qd[22]*(OMcp3_221*ROcp3_621-OMcp3_321*ROcp3_521)+\
   qdd[21]*ROcp3_16+qdd[22]*ROcp3_421
  OMPxF4[2] = OPcp3_220-qd[21]*(OMcp3_120*ROcp3_36-OMcp3_320*ROcp3_16)-qd[22]*(OMcp3_121*ROcp3_621-OMcp3_321*ROcp3_421)+\
   qdd[21]*ROcp3_26+qdd[22]*ROcp3_521
  OMPxF4[3] = OPcp3_320+qd[21]*(OMcp3_120*ROcp3_26-OMcp3_220*ROcp3_16)+qd[22]*(OMcp3_121*ROcp3_521-OMcp3_221*ROcp3_421)+\
   qdd[21]*ROcp3_36+qdd[22]*ROcp3_621
 
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
  frc[1,11] = s.frc[1,11]
  frc[2,11] = s.frc[2,11]
  frc[3,11] = s.frc[3,11]
  frc[1,12] = s.frc[1,12]
  frc[2,12] = s.frc[2,12]
  frc[3,12] = s.frc[3,12]
  frc[1,15] = s.frc[1,15]
  frc[2,15] = s.frc[2,15]
  frc[3,15] = s.frc[3,15]
  frc[1,16] = s.frc[1,16]
  frc[2,16] = s.frc[2,16]
  frc[3,16] = s.frc[3,16]
  frc[1,19] = s.frc[1,19]
  frc[2,19] = s.frc[2,19]
  frc[3,19] = s.frc[3,19]
  frc[1,20] = s.frc[1,20]
  frc[2,20] = s.frc[2,20]
  frc[3,20] = s.frc[3,20]
  trq[1,6] = s.trq[1,6]
  trq[2,6] = s.trq[2,6]
  trq[3,6] = s.trq[3,6]
  trq[1,7] = s.trq[1,7]
  trq[2,7] = s.trq[2,7]
  trq[3,7] = s.trq[3,7]
  trq[1,8] = s.trq[1,8]
  trq[2,8] = s.trq[2,8]
  trq[3,8] = s.trq[3,8]
  trq[1,11] = s.trq[1,11]
  trq[2,11] = s.trq[2,11]
  trq[3,11] = s.trq[3,11]
  trq[1,12] = s.trq[1,12]
  trq[2,12] = s.trq[2,12]
  trq[3,12] = s.trq[3,12]
  trq[1,15] = s.trq[1,15]
  trq[2,15] = s.trq[2,15]
  trq[3,15] = s.trq[3,15]
  trq[1,16] = s.trq[1,16]
  trq[2,16] = s.trq[2,16]
  trq[3,16] = s.trq[3,16]
  trq[1,19] = s.trq[1,19]
  trq[2,19] = s.trq[2,19]
  trq[3,19] = s.trq[3,19]
  trq[1,20] = s.trq[1,20]
  trq[2,20] = s.trq[2,20]
  trq[3,20] = s.trq[3,20]

# ====== END Task 0 ====== 

  

