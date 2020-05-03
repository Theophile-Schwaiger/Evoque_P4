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
#	==> Function : F19 : External Forces
#	==> Flops complexity : 2166
#
#	==> Generation Time :  0.030 seconds
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

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C39 = np.cos(q[39])
  S39 = np.sin(q[39])
  C40 = np.cos(q[40])
  S40 = np.sin(q[40])

# = = Block_0_0_1_1_0_1 = = 
 
# Sensor Kinematics 


  ROcp0_15 = C4*C5
  ROcp0_25 = S4*C5
  ROcp0_75 = C4*S5
  ROcp0_85 = S4*S5
  ROcp0_46 = ROcp0_75*S6-S4*C6
  ROcp0_56 = ROcp0_85*S6+C4*C6
  ROcp0_76 = ROcp0_75*C6+S4*S6
  ROcp0_86 = ROcp0_85*C6-C4*S6
  OMcp0_15 = -qd[5]*S4
  OMcp0_25 = qd[5]*C4
  OMcp0_16 = OMcp0_15+qd[6]*ROcp0_15
  OMcp0_26 = OMcp0_25+qd[6]*ROcp0_25
  OMcp0_36 = qd[4]-qd[6]*S5
  OPcp0_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp0_25+OMcp0_25*S5)+qdd[5]*S4-qdd[6]*ROcp0_15)
  OPcp0_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp0_15+OMcp0_15*S5)-qdd[5]*C4-qdd[6]*ROcp0_25)
  OPcp0_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5

# = = Block_0_0_1_1_0_2 = = 
 
# Trigonometric Variables  

  S6p7 = C6*S7+S6*C7
  C6p7 = C6*C7-S6*S7
 
# Sensor Kinematics 


  ROcp0_47 = ROcp0_46*C7+ROcp0_76*S7
  ROcp0_57 = ROcp0_56*C7+ROcp0_86*S7
  ROcp0_67 = S6p7*C5
  ROcp0_77 = -(ROcp0_46*S7-ROcp0_76*C7)
  ROcp0_87 = -(ROcp0_56*S7-ROcp0_86*C7)
  ROcp0_97 = C6p7*C5
  ROcp0_18 = ROcp0_15*C8+ROcp0_47*S8
  ROcp0_28 = ROcp0_25*C8+ROcp0_57*S8
  ROcp0_38 = ROcp0_67*S8-S5*C8
  ROcp0_48 = -(ROcp0_15*S8-ROcp0_47*C8)
  ROcp0_58 = -(ROcp0_25*S8-ROcp0_57*C8)
  ROcp0_68 = ROcp0_67*C8+S5*S8
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
  RLcp0_17 = ROcp0_15*s.dpt[1,1]+ROcp0_46*s.dpt[2,1]
  RLcp0_27 = ROcp0_25*s.dpt[1,1]+ROcp0_56*s.dpt[2,1]
  RLcp0_37 = C5*S6*s.dpt[2,1]-s.dpt[1,1]*S5
  OMcp0_17 = OMcp0_16+qd[7]*ROcp0_15
  OMcp0_27 = OMcp0_26+qd[7]*ROcp0_25
  OMcp0_37 = OMcp0_36-qd[7]*S5
  ORcp0_17 = OMcp0_26*RLcp0_37-OMcp0_36*RLcp0_27
  ORcp0_27 = -(OMcp0_16*RLcp0_37-OMcp0_36*RLcp0_17)
  ORcp0_37 = OMcp0_16*RLcp0_27-OMcp0_26*RLcp0_17
  OPcp0_17 = OPcp0_16-qd[7]*(OMcp0_26*S5+OMcp0_36*ROcp0_25)+qdd[7]*ROcp0_15
  OPcp0_27 = OPcp0_26+qd[7]*(OMcp0_16*S5+OMcp0_36*ROcp0_15)+qdd[7]*ROcp0_25
  OPcp0_37 = OPcp0_36+qd[7]*(OMcp0_16*ROcp0_25-OMcp0_26*ROcp0_15)-qdd[7]*S5
  RLcp0_18 = ROcp0_47*s.dpt[2,14]
  RLcp0_28 = ROcp0_57*s.dpt[2,14]
  RLcp0_38 = ROcp0_67*s.dpt[2,14]
  OMcp0_18 = OMcp0_17+qd[8]*ROcp0_77
  OMcp0_28 = OMcp0_27+qd[8]*ROcp0_87
  OMcp0_38 = OMcp0_37+qd[8]*ROcp0_97
  ORcp0_18 = OMcp0_27*RLcp0_38-OMcp0_37*RLcp0_28
  ORcp0_28 = -(OMcp0_17*RLcp0_38-OMcp0_37*RLcp0_18)
  ORcp0_38 = OMcp0_17*RLcp0_28-OMcp0_27*RLcp0_18
  OMcp0_19 = OMcp0_18+qd[9]*ROcp0_18
  OMcp0_29 = OMcp0_28+qd[9]*ROcp0_28
  OMcp0_39 = OMcp0_38+qd[9]*ROcp0_38
  OMcp0_110 = OMcp0_19+qd[10]*ROcp0_49
  OMcp0_210 = OMcp0_29+qd[10]*ROcp0_59
  OMcp0_310 = OMcp0_39+qd[10]*ROcp0_69
  OPcp0_110 = OPcp0_17+qd[10]*(OMcp0_29*ROcp0_69-OMcp0_39*ROcp0_59)+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(\
   OMcp0_28*ROcp0_38-OMcp0_38*ROcp0_28)+qdd[10]*ROcp0_49+qdd[8]*ROcp0_77+qdd[9]*ROcp0_18
  OPcp0_210 = OPcp0_27-qd[10]*(OMcp0_19*ROcp0_69-OMcp0_39*ROcp0_49)-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(\
   OMcp0_18*ROcp0_38-OMcp0_38*ROcp0_18)+qdd[10]*ROcp0_59+qdd[8]*ROcp0_87+qdd[9]*ROcp0_28
  OPcp0_310 = OPcp0_37+qd[10]*(OMcp0_19*ROcp0_59-OMcp0_29*ROcp0_49)+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(\
   OMcp0_18*ROcp0_28-OMcp0_28*ROcp0_18)+qdd[10]*ROcp0_69+qdd[8]*ROcp0_97+qdd[9]*ROcp0_38

# = = Block_0_0_1_1_0_4 = = 
 
# Sensor Kinematics 


  ROcp0_413 = ROcp0_49*C13+ROcp0_710*S13
  ROcp0_513 = ROcp0_59*C13+ROcp0_810*S13
  ROcp0_613 = ROcp0_69*C13+ROcp0_910*S13
  ROcp0_713 = -(ROcp0_49*S13-ROcp0_710*C13)
  ROcp0_813 = -(ROcp0_59*S13-ROcp0_810*C13)
  ROcp0_913 = -(ROcp0_69*S13-ROcp0_910*C13)
  ROcp0_114 = ROcp0_110*C14-ROcp0_713*S14
  ROcp0_214 = ROcp0_210*C14-ROcp0_813*S14
  ROcp0_314 = ROcp0_310*C14-ROcp0_913*S14
  ROcp0_714 = ROcp0_110*S14+ROcp0_713*C14
  ROcp0_814 = ROcp0_210*S14+ROcp0_813*C14
  ROcp0_914 = ROcp0_310*S14+ROcp0_913*C14
  RLcp0_113 = ROcp0_710*s.dpt[3,16]
  RLcp0_213 = ROcp0_810*s.dpt[3,16]
  RLcp0_313 = ROcp0_910*s.dpt[3,16]
  OMcp0_113 = OMcp0_110+qd[13]*ROcp0_110
  OMcp0_213 = OMcp0_210+qd[13]*ROcp0_210
  OMcp0_313 = OMcp0_310+qd[13]*ROcp0_310
  ORcp0_113 = OMcp0_210*RLcp0_313-OMcp0_310*RLcp0_213
  ORcp0_213 = -(OMcp0_110*RLcp0_313-OMcp0_310*RLcp0_113)
  ORcp0_313 = OMcp0_110*RLcp0_213-OMcp0_210*RLcp0_113
  PxF1[1] = q[1]+RLcp0_113+RLcp0_17+RLcp0_18
  PxF1[2] = q[2]+RLcp0_213+RLcp0_27+RLcp0_28
  PxF1[3] = q[3]+RLcp0_313+RLcp0_37+RLcp0_38
  RxF1[1,1] = ROcp0_114
  RxF1[1,2] = ROcp0_214
  RxF1[1,3] = ROcp0_314
  RxF1[2,1] = ROcp0_413
  RxF1[2,2] = ROcp0_513
  RxF1[2,3] = ROcp0_613
  RxF1[3,1] = ROcp0_714
  RxF1[3,2] = ROcp0_814
  RxF1[3,3] = ROcp0_914
  VxF1[1] = qd[1]+ORcp0_113+ORcp0_17+ORcp0_18
  VxF1[2] = qd[2]+ORcp0_213+ORcp0_27+ORcp0_28
  VxF1[3] = qd[3]+ORcp0_313+ORcp0_37+ORcp0_38
  OMxF1[1] = OMcp0_113+qd[14]*ROcp0_413
  OMxF1[2] = OMcp0_213+qd[14]*ROcp0_513
  OMxF1[3] = OMcp0_313+qd[14]*ROcp0_613
  AxF1[1] = qdd[1]+OMcp0_210*ORcp0_313+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_310*ORcp0_213-OMcp0_36*ORcp0_27-\
   OMcp0_37*ORcp0_28+OPcp0_210*RLcp0_313+OPcp0_26*RLcp0_37+OPcp0_27*RLcp0_38-OPcp0_310*RLcp0_213-OPcp0_36*RLcp0_27-OPcp0_37*\
   RLcp0_28
  AxF1[2] = qdd[2]-OMcp0_110*ORcp0_313-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_310*ORcp0_113+OMcp0_36*ORcp0_17+\
   OMcp0_37*ORcp0_18-OPcp0_110*RLcp0_313-OPcp0_16*RLcp0_37-OPcp0_17*RLcp0_38+OPcp0_310*RLcp0_113+OPcp0_36*RLcp0_17+OPcp0_37*\
   RLcp0_18
  AxF1[3] = qdd[3]+OMcp0_110*ORcp0_213+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_210*ORcp0_113-OMcp0_26*ORcp0_17-\
   OMcp0_27*ORcp0_18+OPcp0_110*RLcp0_213+OPcp0_16*RLcp0_27+OPcp0_17*RLcp0_28-OPcp0_210*RLcp0_113-OPcp0_26*RLcp0_17-OPcp0_27*\
   RLcp0_18
  OMPxF1[1] = OPcp0_110+qd[13]*(OMcp0_210*ROcp0_310-OMcp0_310*ROcp0_210)+qd[14]*(OMcp0_213*ROcp0_613-OMcp0_313*ROcp0_513\
   )+qdd[13]*ROcp0_110+qdd[14]*ROcp0_413
  OMPxF1[2] = OPcp0_210-qd[13]*(OMcp0_110*ROcp0_310-OMcp0_310*ROcp0_110)-qd[14]*(OMcp0_113*ROcp0_613-OMcp0_313*ROcp0_413\
   )+qdd[13]*ROcp0_210+qdd[14]*ROcp0_513
  OMPxF1[3] = OPcp0_310+qd[13]*(OMcp0_110*ROcp0_210-OMcp0_210*ROcp0_110)+qd[14]*(OMcp0_113*ROcp0_513-OMcp0_213*ROcp0_413\
   )+qdd[13]*ROcp0_310+qdd[14]*ROcp0_613
 
# Sensor Forces Computation 

  SWr1 = s.user_ExtForces(PxF1,RxF1,VxF1,OMxF1,AxF1,OMPxF1,s,tsim,1)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc11 = ROcp0_114*SWr1[1]+ROcp0_214*SWr1[2]+ROcp0_314*SWr1[3]
  xfrc21 = ROcp0_413*SWr1[1]+ROcp0_513*SWr1[2]+ROcp0_613*SWr1[3]
  xfrc31 = ROcp0_714*SWr1[1]+ROcp0_814*SWr1[2]+ROcp0_914*SWr1[3]
  frc[1,14] = s.frc[1,14]+xfrc11
  frc[2,14] = s.frc[2,14]+xfrc21
  frc[3,14] = s.frc[3,14]+xfrc31
  xtrq11 = ROcp0_114*SWr1[4]+ROcp0_214*SWr1[5]+ROcp0_314*SWr1[6]
  xtrq21 = ROcp0_413*SWr1[4]+ROcp0_513*SWr1[5]+ROcp0_613*SWr1[6]
  xtrq31 = ROcp0_714*SWr1[4]+ROcp0_814*SWr1[5]+ROcp0_914*SWr1[6]
  trq[1,14] = s.trq[1,14]+xtrq11-xfrc21*SWr1[9]+xfrc31*SWr1[8]
  trq[2,14] = s.trq[2,14]+xtrq21+xfrc11*SWr1[9]-xfrc31*SWr1[7]
  trq[3,14] = s.trq[3,14]+xtrq31-xfrc11*SWr1[8]+xfrc21*SWr1[7]

# = = Block_0_0_1_2_0_1 = = 
 
# Sensor Kinematics 


  ROcp1_15 = C4*C5
  ROcp1_25 = S4*C5
  ROcp1_75 = C4*S5
  ROcp1_85 = S4*S5
  ROcp1_46 = ROcp1_75*S6-S4*C6
  ROcp1_56 = ROcp1_85*S6+C4*C6
  ROcp1_76 = ROcp1_75*C6+S4*S6
  ROcp1_86 = ROcp1_85*C6-C4*S6
  OMcp1_15 = -qd[5]*S4
  OMcp1_25 = qd[5]*C4
  OMcp1_16 = OMcp1_15+qd[6]*ROcp1_15
  OMcp1_26 = OMcp1_25+qd[6]*ROcp1_25
  OMcp1_36 = qd[4]-qd[6]*S5
  OPcp1_16 = -(qd[4]*qd[5]*C4+qd[6]*(qd[4]*ROcp1_25+OMcp1_25*S5)+qdd[5]*S4-qdd[6]*ROcp1_15)
  OPcp1_26 = -(qd[4]*qd[5]*S4-qd[6]*(qd[4]*ROcp1_15+OMcp1_15*S5)-qdd[5]*C4-qdd[6]*ROcp1_25)
  OPcp1_36 = qdd[4]-qd[5]*qd[6]*C5-qdd[6]*S5

# = = Block_0_0_1_2_0_5 = = 
 
# Trigonometric Variables  

  S15p6 = C15*S6+S15*C6
  C15p6 = C15*C6-S15*S6
 
# Sensor Kinematics 


  ROcp1_415 = ROcp1_46*C15+ROcp1_76*S15
  ROcp1_515 = ROcp1_56*C15+ROcp1_86*S15
  ROcp1_615 = S15p6*C5
  ROcp1_715 = -(ROcp1_46*S15-ROcp1_76*C15)
  ROcp1_815 = -(ROcp1_56*S15-ROcp1_86*C15)
  ROcp1_915 = C15p6*C5
  ROcp1_116 = ROcp1_15*C16+ROcp1_415*S16
  ROcp1_216 = ROcp1_25*C16+ROcp1_515*S16
  ROcp1_316 = ROcp1_615*S16-C16*S5
  ROcp1_416 = -(ROcp1_15*S16-ROcp1_415*C16)
  ROcp1_516 = -(ROcp1_25*S16-ROcp1_515*C16)
  ROcp1_616 = ROcp1_615*C16+S16*S5
  ROcp1_417 = ROcp1_416*C17+ROcp1_715*S17
  ROcp1_517 = ROcp1_516*C17+ROcp1_815*S17
  ROcp1_617 = ROcp1_616*C17+ROcp1_915*S17
  ROcp1_717 = -(ROcp1_416*S17-ROcp1_715*C17)
  ROcp1_817 = -(ROcp1_516*S17-ROcp1_815*C17)
  ROcp1_917 = -(ROcp1_616*S17-ROcp1_915*C17)
  ROcp1_118 = ROcp1_116*C18-ROcp1_717*S18
  ROcp1_218 = ROcp1_216*C18-ROcp1_817*S18
  ROcp1_318 = ROcp1_316*C18-ROcp1_917*S18
  ROcp1_718 = ROcp1_116*S18+ROcp1_717*C18
  ROcp1_818 = ROcp1_216*S18+ROcp1_817*C18
  ROcp1_918 = ROcp1_316*S18+ROcp1_917*C18
  RLcp1_115 = ROcp1_15*s.dpt[1,4]+ROcp1_46*s.dpt[2,4]
  RLcp1_215 = ROcp1_25*s.dpt[1,4]+ROcp1_56*s.dpt[2,4]
  RLcp1_315 = C5*S6*s.dpt[2,4]-s.dpt[1,4]*S5
  OMcp1_115 = OMcp1_16+qd[15]*ROcp1_15
  OMcp1_215 = OMcp1_26+qd[15]*ROcp1_25
  OMcp1_315 = OMcp1_36-qd[15]*S5
  ORcp1_115 = OMcp1_26*RLcp1_315-OMcp1_36*RLcp1_215
  ORcp1_215 = -(OMcp1_16*RLcp1_315-OMcp1_36*RLcp1_115)
  ORcp1_315 = OMcp1_16*RLcp1_215-OMcp1_26*RLcp1_115
  OPcp1_115 = OPcp1_16-qd[15]*(OMcp1_26*S5+OMcp1_36*ROcp1_25)+qdd[15]*ROcp1_15
  OPcp1_215 = OPcp1_26+qd[15]*(OMcp1_16*S5+OMcp1_36*ROcp1_15)+qdd[15]*ROcp1_25
  OPcp1_315 = OPcp1_36+qd[15]*(OMcp1_16*ROcp1_25-OMcp1_26*ROcp1_15)-qdd[15]*S5
  RLcp1_116 = ROcp1_415*s.dpt[2,20]
  RLcp1_216 = ROcp1_515*s.dpt[2,20]
  RLcp1_316 = ROcp1_615*s.dpt[2,20]
  OMcp1_116 = OMcp1_115+qd[16]*ROcp1_715
  OMcp1_216 = OMcp1_215+qd[16]*ROcp1_815
  OMcp1_316 = OMcp1_315+qd[16]*ROcp1_915
  ORcp1_116 = OMcp1_215*RLcp1_316-OMcp1_315*RLcp1_216
  ORcp1_216 = -(OMcp1_115*RLcp1_316-OMcp1_315*RLcp1_116)
  ORcp1_316 = OMcp1_115*RLcp1_216-OMcp1_215*RLcp1_116
  OMcp1_117 = OMcp1_116+qd[17]*ROcp1_116
  OMcp1_217 = OMcp1_216+qd[17]*ROcp1_216
  OMcp1_317 = OMcp1_316+qd[17]*ROcp1_316
  OMcp1_118 = OMcp1_117+qd[18]*ROcp1_417
  OMcp1_218 = OMcp1_217+qd[18]*ROcp1_517
  OMcp1_318 = OMcp1_317+qd[18]*ROcp1_617
  OPcp1_118 = OPcp1_115+qd[16]*(OMcp1_215*ROcp1_915-OMcp1_315*ROcp1_815)+qd[17]*(OMcp1_216*ROcp1_316-OMcp1_316*ROcp1_216\
   )+qd[18]*(OMcp1_217*ROcp1_617-OMcp1_317*ROcp1_517)+qdd[16]*ROcp1_715+qdd[17]*ROcp1_116+qdd[18]*ROcp1_417
  OPcp1_218 = OPcp1_215-qd[16]*(OMcp1_115*ROcp1_915-OMcp1_315*ROcp1_715)-qd[17]*(OMcp1_116*ROcp1_316-OMcp1_316*ROcp1_116\
   )-qd[18]*(OMcp1_117*ROcp1_617-OMcp1_317*ROcp1_417)+qdd[16]*ROcp1_815+qdd[17]*ROcp1_216+qdd[18]*ROcp1_517
  OPcp1_318 = OPcp1_315+qd[16]*(OMcp1_115*ROcp1_815-OMcp1_215*ROcp1_715)+qd[17]*(OMcp1_116*ROcp1_216-OMcp1_216*ROcp1_116\
   )+qd[18]*(OMcp1_117*ROcp1_517-OMcp1_217*ROcp1_417)+qdd[16]*ROcp1_915+qdd[17]*ROcp1_316+qdd[18]*ROcp1_617

# = = Block_0_0_1_2_0_7 = = 
 
# Sensor Kinematics 


  ROcp1_421 = ROcp1_417*C21+ROcp1_718*S21
  ROcp1_521 = ROcp1_517*C21+ROcp1_818*S21
  ROcp1_621 = ROcp1_617*C21+ROcp1_918*S21
  ROcp1_721 = -(ROcp1_417*S21-ROcp1_718*C21)
  ROcp1_821 = -(ROcp1_517*S21-ROcp1_818*C21)
  ROcp1_921 = -(ROcp1_617*S21-ROcp1_918*C21)
  ROcp1_122 = ROcp1_118*C22-ROcp1_721*S22
  ROcp1_222 = ROcp1_218*C22-ROcp1_821*S22
  ROcp1_322 = ROcp1_318*C22-ROcp1_921*S22
  ROcp1_722 = ROcp1_118*S22+ROcp1_721*C22
  ROcp1_822 = ROcp1_218*S22+ROcp1_821*C22
  ROcp1_922 = ROcp1_318*S22+ROcp1_921*C22
  RLcp1_121 = ROcp1_718*s.dpt[3,22]
  RLcp1_221 = ROcp1_818*s.dpt[3,22]
  RLcp1_321 = ROcp1_918*s.dpt[3,22]
  OMcp1_121 = OMcp1_118+qd[21]*ROcp1_118
  OMcp1_221 = OMcp1_218+qd[21]*ROcp1_218
  OMcp1_321 = OMcp1_318+qd[21]*ROcp1_318
  ORcp1_121 = OMcp1_218*RLcp1_321-OMcp1_318*RLcp1_221
  ORcp1_221 = -(OMcp1_118*RLcp1_321-OMcp1_318*RLcp1_121)
  ORcp1_321 = OMcp1_118*RLcp1_221-OMcp1_218*RLcp1_121
  PxF2[1] = q[1]+RLcp1_115+RLcp1_116+RLcp1_121
  PxF2[2] = q[2]+RLcp1_215+RLcp1_216+RLcp1_221
  PxF2[3] = q[3]+RLcp1_315+RLcp1_316+RLcp1_321
  RxF2[1,1] = ROcp1_122
  RxF2[1,2] = ROcp1_222
  RxF2[1,3] = ROcp1_322
  RxF2[2,1] = ROcp1_421
  RxF2[2,2] = ROcp1_521
  RxF2[2,3] = ROcp1_621
  RxF2[3,1] = ROcp1_722
  RxF2[3,2] = ROcp1_822
  RxF2[3,3] = ROcp1_922
  VxF2[1] = qd[1]+ORcp1_115+ORcp1_116+ORcp1_121
  VxF2[2] = qd[2]+ORcp1_215+ORcp1_216+ORcp1_221
  VxF2[3] = qd[3]+ORcp1_315+ORcp1_316+ORcp1_321
  OMxF2[1] = OMcp1_121+qd[22]*ROcp1_421
  OMxF2[2] = OMcp1_221+qd[22]*ROcp1_521
  OMxF2[3] = OMcp1_321+qd[22]*ROcp1_621
  AxF2[1] = qdd[1]+OMcp1_215*ORcp1_316+OMcp1_218*ORcp1_321+OMcp1_26*ORcp1_315-OMcp1_315*ORcp1_216-OMcp1_318*ORcp1_221-\
   OMcp1_36*ORcp1_215+OPcp1_215*RLcp1_316+OPcp1_218*RLcp1_321+OPcp1_26*RLcp1_315-OPcp1_315*RLcp1_216-OPcp1_318*RLcp1_221-\
   OPcp1_36*RLcp1_215
  AxF2[2] = qdd[2]-OMcp1_115*ORcp1_316-OMcp1_118*ORcp1_321-OMcp1_16*ORcp1_315+OMcp1_315*ORcp1_116+OMcp1_318*ORcp1_121+\
   OMcp1_36*ORcp1_115-OPcp1_115*RLcp1_316-OPcp1_118*RLcp1_321-OPcp1_16*RLcp1_315+OPcp1_315*RLcp1_116+OPcp1_318*RLcp1_121+\
   OPcp1_36*RLcp1_115
  AxF2[3] = qdd[3]+OMcp1_115*ORcp1_216+OMcp1_118*ORcp1_221+OMcp1_16*ORcp1_215-OMcp1_215*ORcp1_116-OMcp1_218*ORcp1_121-\
   OMcp1_26*ORcp1_115+OPcp1_115*RLcp1_216+OPcp1_118*RLcp1_221+OPcp1_16*RLcp1_215-OPcp1_215*RLcp1_116-OPcp1_218*RLcp1_121-\
   OPcp1_26*RLcp1_115
  OMPxF2[1] = OPcp1_118+qd[21]*(OMcp1_218*ROcp1_318-OMcp1_318*ROcp1_218)+qd[22]*(OMcp1_221*ROcp1_621-OMcp1_321*ROcp1_521\
   )+qdd[21]*ROcp1_118+qdd[22]*ROcp1_421
  OMPxF2[2] = OPcp1_218-qd[21]*(OMcp1_118*ROcp1_318-OMcp1_318*ROcp1_118)-qd[22]*(OMcp1_121*ROcp1_621-OMcp1_321*ROcp1_421\
   )+qdd[21]*ROcp1_218+qdd[22]*ROcp1_521
  OMPxF2[3] = OPcp1_318+qd[21]*(OMcp1_118*ROcp1_218-OMcp1_218*ROcp1_118)+qd[22]*(OMcp1_121*ROcp1_521-OMcp1_221*ROcp1_421\
   )+qdd[21]*ROcp1_318+qdd[22]*ROcp1_621
 
# Sensor Forces Computation 

  SWr2 = s.user_ExtForces(PxF2,RxF2,VxF2,OMxF2,AxF2,OMPxF2,s,tsim,2)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc12 = ROcp1_122*SWr2[1]+ROcp1_222*SWr2[2]+ROcp1_322*SWr2[3]
  xfrc22 = ROcp1_421*SWr2[1]+ROcp1_521*SWr2[2]+ROcp1_621*SWr2[3]
  xfrc32 = ROcp1_722*SWr2[1]+ROcp1_822*SWr2[2]+ROcp1_922*SWr2[3]
  frc[1,22] = s.frc[1,22]+xfrc12
  frc[2,22] = s.frc[2,22]+xfrc22
  frc[3,22] = s.frc[3,22]+xfrc32
  xtrq12 = ROcp1_122*SWr2[4]+ROcp1_222*SWr2[5]+ROcp1_322*SWr2[6]
  xtrq22 = ROcp1_421*SWr2[4]+ROcp1_521*SWr2[5]+ROcp1_621*SWr2[6]
  xtrq32 = ROcp1_722*SWr2[4]+ROcp1_822*SWr2[5]+ROcp1_922*SWr2[6]
  trq[1,22] = s.trq[1,22]+xtrq12-xfrc22*SWr2[9]+xfrc32*SWr2[8]
  trq[2,22] = s.trq[2,22]+xtrq22+xfrc12*SWr2[9]-xfrc32*SWr2[7]
  trq[3,22] = s.trq[3,22]+xtrq32-xfrc12*SWr2[8]+xfrc22*SWr2[7]

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

# = = Block_0_0_1_3_0_8 = = 
 
# Trigonometric Variables  

  S23p6 = C23*S6+S23*C6
  C23p6 = C23*C6-S23*S6
 
# Sensor Kinematics 


  ROcp2_423 = ROcp2_46*C23+ROcp2_76*S23
  ROcp2_523 = ROcp2_56*C23+ROcp2_86*S23
  ROcp2_623 = S23p6*C5
  ROcp2_723 = -(ROcp2_46*S23-ROcp2_76*C23)
  ROcp2_823 = -(ROcp2_56*S23-ROcp2_86*C23)
  ROcp2_923 = C23p6*C5
  ROcp2_124 = ROcp2_15*C24+ROcp2_423*S24
  ROcp2_224 = ROcp2_25*C24+ROcp2_523*S24
  ROcp2_324 = ROcp2_623*S24-C24*S5
  ROcp2_424 = -(ROcp2_15*S24-ROcp2_423*C24)
  ROcp2_524 = -(ROcp2_25*S24-ROcp2_523*C24)
  ROcp2_624 = ROcp2_623*C24+S24*S5
  ROcp2_425 = ROcp2_424*C25+ROcp2_723*S25
  ROcp2_525 = ROcp2_524*C25+ROcp2_823*S25
  ROcp2_625 = ROcp2_624*C25+ROcp2_923*S25
  ROcp2_725 = -(ROcp2_424*S25-ROcp2_723*C25)
  ROcp2_825 = -(ROcp2_524*S25-ROcp2_823*C25)
  ROcp2_925 = -(ROcp2_624*S25-ROcp2_923*C25)
  ROcp2_126 = ROcp2_124*C26-ROcp2_725*S26
  ROcp2_226 = ROcp2_224*C26-ROcp2_825*S26
  ROcp2_326 = ROcp2_324*C26-ROcp2_925*S26
  ROcp2_726 = ROcp2_124*S26+ROcp2_725*C26
  ROcp2_826 = ROcp2_224*S26+ROcp2_825*C26
  ROcp2_926 = ROcp2_324*S26+ROcp2_925*C26
  ROcp2_127 = ROcp2_126*C27+ROcp2_425*S27
  ROcp2_227 = ROcp2_226*C27+ROcp2_525*S27
  ROcp2_327 = ROcp2_326*C27+ROcp2_625*S27
  ROcp2_427 = -(ROcp2_126*S27-ROcp2_425*C27)
  ROcp2_527 = -(ROcp2_226*S27-ROcp2_525*C27)
  ROcp2_627 = -(ROcp2_326*S27-ROcp2_625*C27)
  RLcp2_123 = ROcp2_15*s.dpt[1,10]+ROcp2_46*s.dpt[2,10]
  RLcp2_223 = ROcp2_25*s.dpt[1,10]+ROcp2_56*s.dpt[2,10]
  RLcp2_323 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
  OMcp2_123 = OMcp2_16+qd[23]*ROcp2_15
  OMcp2_223 = OMcp2_26+qd[23]*ROcp2_25
  OMcp2_323 = OMcp2_36-qd[23]*S5
  ORcp2_123 = OMcp2_26*RLcp2_323-OMcp2_36*RLcp2_223
  ORcp2_223 = -(OMcp2_16*RLcp2_323-OMcp2_36*RLcp2_123)
  ORcp2_323 = OMcp2_16*RLcp2_223-OMcp2_26*RLcp2_123
  OMcp2_124 = OMcp2_123+qd[24]*ROcp2_723
  OMcp2_224 = OMcp2_223+qd[24]*ROcp2_823
  OMcp2_324 = OMcp2_323+qd[24]*ROcp2_923
  OPcp2_124 = OPcp2_16-qd[23]*(OMcp2_26*S5+OMcp2_36*ROcp2_25)+qd[24]*(OMcp2_223*ROcp2_923-OMcp2_323*ROcp2_823)+qdd[23]*\
   ROcp2_15+qdd[24]*ROcp2_723
  OPcp2_224 = OPcp2_26+qd[23]*(OMcp2_16*S5+OMcp2_36*ROcp2_15)-qd[24]*(OMcp2_123*ROcp2_923-OMcp2_323*ROcp2_723)+qdd[23]*\
   ROcp2_25+qdd[24]*ROcp2_823
  OPcp2_324 = OPcp2_36+qd[23]*(OMcp2_16*ROcp2_25-OMcp2_26*ROcp2_15)+qd[24]*(OMcp2_123*ROcp2_823-OMcp2_223*ROcp2_723)-\
   qdd[23]*S5+qdd[24]*ROcp2_923
  RLcp2_125 = ROcp2_424*s.dpt[2,26]
  RLcp2_225 = ROcp2_524*s.dpt[2,26]
  RLcp2_325 = ROcp2_624*s.dpt[2,26]
  OMcp2_125 = OMcp2_124+qd[25]*ROcp2_124
  OMcp2_225 = OMcp2_224+qd[25]*ROcp2_224
  OMcp2_325 = OMcp2_324+qd[25]*ROcp2_324
  ORcp2_125 = OMcp2_224*RLcp2_325-OMcp2_324*RLcp2_225
  ORcp2_225 = -(OMcp2_124*RLcp2_325-OMcp2_324*RLcp2_125)
  ORcp2_325 = OMcp2_124*RLcp2_225-OMcp2_224*RLcp2_125
  OMcp2_126 = OMcp2_125+qd[26]*ROcp2_425
  OMcp2_226 = OMcp2_225+qd[26]*ROcp2_525
  OMcp2_326 = OMcp2_325+qd[26]*ROcp2_625
  OMcp2_127 = OMcp2_126+qd[27]*ROcp2_726
  OMcp2_227 = OMcp2_226+qd[27]*ROcp2_826
  OMcp2_327 = OMcp2_326+qd[27]*ROcp2_926
  OPcp2_127 = OPcp2_124+qd[25]*(OMcp2_224*ROcp2_324-OMcp2_324*ROcp2_224)+qd[26]*(OMcp2_225*ROcp2_625-OMcp2_325*ROcp2_525\
   )+qd[27]*(OMcp2_226*ROcp2_926-OMcp2_326*ROcp2_826)+qdd[25]*ROcp2_124+qdd[26]*ROcp2_425+qdd[27]*ROcp2_726
  OPcp2_227 = OPcp2_224-qd[25]*(OMcp2_124*ROcp2_324-OMcp2_324*ROcp2_124)-qd[26]*(OMcp2_125*ROcp2_625-OMcp2_325*ROcp2_425\
   )-qd[27]*(OMcp2_126*ROcp2_926-OMcp2_326*ROcp2_726)+qdd[25]*ROcp2_224+qdd[26]*ROcp2_525+qdd[27]*ROcp2_826
  OPcp2_327 = OPcp2_324+qd[25]*(OMcp2_124*ROcp2_224-OMcp2_224*ROcp2_124)+qd[26]*(OMcp2_125*ROcp2_525-OMcp2_225*ROcp2_425\
   )+qd[27]*(OMcp2_126*ROcp2_826-OMcp2_226*ROcp2_726)+qdd[25]*ROcp2_324+qdd[26]*ROcp2_625+qdd[27]*ROcp2_926

# = = Block_0_0_1_3_0_10 = = 
 
# Sensor Kinematics 


  ROcp2_430 = ROcp2_427*C30+ROcp2_726*S30
  ROcp2_530 = ROcp2_527*C30+ROcp2_826*S30
  ROcp2_630 = ROcp2_627*C30+ROcp2_926*S30
  ROcp2_730 = -(ROcp2_427*S30-ROcp2_726*C30)
  ROcp2_830 = -(ROcp2_527*S30-ROcp2_826*C30)
  ROcp2_930 = -(ROcp2_627*S30-ROcp2_926*C30)
  ROcp2_131 = ROcp2_127*C31-ROcp2_730*S31
  ROcp2_231 = ROcp2_227*C31-ROcp2_830*S31
  ROcp2_331 = ROcp2_327*C31-ROcp2_930*S31
  ROcp2_731 = ROcp2_127*S31+ROcp2_730*C31
  ROcp2_831 = ROcp2_227*S31+ROcp2_830*C31
  ROcp2_931 = ROcp2_327*S31+ROcp2_930*C31
  RLcp2_130 = ROcp2_726*s.dpt[3,28]
  RLcp2_230 = ROcp2_826*s.dpt[3,28]
  RLcp2_330 = ROcp2_926*s.dpt[3,28]
  OMcp2_130 = OMcp2_127+qd[30]*ROcp2_127
  OMcp2_230 = OMcp2_227+qd[30]*ROcp2_227
  OMcp2_330 = OMcp2_327+qd[30]*ROcp2_327
  ORcp2_130 = OMcp2_227*RLcp2_330-OMcp2_327*RLcp2_230
  ORcp2_230 = -(OMcp2_127*RLcp2_330-OMcp2_327*RLcp2_130)
  ORcp2_330 = OMcp2_127*RLcp2_230-OMcp2_227*RLcp2_130
  PxF3[1] = q[1]+RLcp2_123+RLcp2_125+RLcp2_130
  PxF3[2] = q[2]+RLcp2_223+RLcp2_225+RLcp2_230
  PxF3[3] = q[3]+RLcp2_323+RLcp2_325+RLcp2_330
  RxF3[1,1] = ROcp2_131
  RxF3[1,2] = ROcp2_231
  RxF3[1,3] = ROcp2_331
  RxF3[2,1] = ROcp2_430
  RxF3[2,2] = ROcp2_530
  RxF3[2,3] = ROcp2_630
  RxF3[3,1] = ROcp2_731
  RxF3[3,2] = ROcp2_831
  RxF3[3,3] = ROcp2_931
  VxF3[1] = qd[1]+ORcp2_123+ORcp2_125+ORcp2_130
  VxF3[2] = qd[2]+ORcp2_223+ORcp2_225+ORcp2_230
  VxF3[3] = qd[3]+ORcp2_323+ORcp2_325+ORcp2_330
  OMxF3[1] = OMcp2_130+qd[31]*ROcp2_430
  OMxF3[2] = OMcp2_230+qd[31]*ROcp2_530
  OMxF3[3] = OMcp2_330+qd[31]*ROcp2_630
  AxF3[1] = qdd[1]+OMcp2_224*ORcp2_325+OMcp2_227*ORcp2_330+OMcp2_26*ORcp2_323-OMcp2_324*ORcp2_225-OMcp2_327*ORcp2_230-\
   OMcp2_36*ORcp2_223+OPcp2_224*RLcp2_325+OPcp2_227*RLcp2_330+OPcp2_26*RLcp2_323-OPcp2_324*RLcp2_225-OPcp2_327*RLcp2_230-\
   OPcp2_36*RLcp2_223
  AxF3[2] = qdd[2]-OMcp2_124*ORcp2_325-OMcp2_127*ORcp2_330-OMcp2_16*ORcp2_323+OMcp2_324*ORcp2_125+OMcp2_327*ORcp2_130+\
   OMcp2_36*ORcp2_123-OPcp2_124*RLcp2_325-OPcp2_127*RLcp2_330-OPcp2_16*RLcp2_323+OPcp2_324*RLcp2_125+OPcp2_327*RLcp2_130+\
   OPcp2_36*RLcp2_123
  AxF3[3] = qdd[3]+OMcp2_124*ORcp2_225+OMcp2_127*ORcp2_230+OMcp2_16*ORcp2_223-OMcp2_224*ORcp2_125-OMcp2_227*ORcp2_130-\
   OMcp2_26*ORcp2_123+OPcp2_124*RLcp2_225+OPcp2_127*RLcp2_230+OPcp2_16*RLcp2_223-OPcp2_224*RLcp2_125-OPcp2_227*RLcp2_130-\
   OPcp2_26*RLcp2_123
  OMPxF3[1] = OPcp2_127+qd[30]*(OMcp2_227*ROcp2_327-OMcp2_327*ROcp2_227)+qd[31]*(OMcp2_230*ROcp2_630-OMcp2_330*ROcp2_530\
   )+qdd[30]*ROcp2_127+qdd[31]*ROcp2_430
  OMPxF3[2] = OPcp2_227-qd[30]*(OMcp2_127*ROcp2_327-OMcp2_327*ROcp2_127)-qd[31]*(OMcp2_130*ROcp2_630-OMcp2_330*ROcp2_430\
   )+qdd[30]*ROcp2_227+qdd[31]*ROcp2_530
  OMPxF3[3] = OPcp2_327+qd[30]*(OMcp2_127*ROcp2_227-OMcp2_227*ROcp2_127)+qd[31]*(OMcp2_130*ROcp2_530-OMcp2_230*ROcp2_430\
   )+qdd[30]*ROcp2_327+qdd[31]*ROcp2_630
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc13 = ROcp2_131*SWr3[1]+ROcp2_231*SWr3[2]+ROcp2_331*SWr3[3]
  xfrc23 = ROcp2_430*SWr3[1]+ROcp2_530*SWr3[2]+ROcp2_630*SWr3[3]
  xfrc33 = ROcp2_731*SWr3[1]+ROcp2_831*SWr3[2]+ROcp2_931*SWr3[3]
  frc[1,31] = s.frc[1,31]+xfrc13
  frc[2,31] = s.frc[2,31]+xfrc23
  frc[3,31] = s.frc[3,31]+xfrc33
  xtrq13 = ROcp2_131*SWr3[4]+ROcp2_231*SWr3[5]+ROcp2_331*SWr3[6]
  xtrq23 = ROcp2_430*SWr3[4]+ROcp2_530*SWr3[5]+ROcp2_630*SWr3[6]
  xtrq33 = ROcp2_731*SWr3[4]+ROcp2_831*SWr3[5]+ROcp2_931*SWr3[6]
  trq[1,31] = s.trq[1,31]+xtrq13-xfrc23*SWr3[9]+xfrc33*SWr3[8]
  trq[2,31] = s.trq[2,31]+xtrq23+xfrc13*SWr3[9]-xfrc33*SWr3[7]
  trq[3,31] = s.trq[3,31]+xtrq33-xfrc13*SWr3[8]+xfrc23*SWr3[7]

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

# = = Block_0_0_1_4_0_11 = = 
 
# Trigonometric Variables  

  S32p6 = C32*S6+S32*C6
  C32p6 = C32*C6-S32*S6
 
# Sensor Kinematics 


  ROcp3_432 = ROcp3_46*C32+ROcp3_76*S32
  ROcp3_532 = ROcp3_56*C32+ROcp3_86*S32
  ROcp3_632 = S32p6*C5
  ROcp3_732 = -(ROcp3_46*S32-ROcp3_76*C32)
  ROcp3_832 = -(ROcp3_56*S32-ROcp3_86*C32)
  ROcp3_932 = C32p6*C5
  ROcp3_133 = ROcp3_15*C33+ROcp3_432*S33
  ROcp3_233 = ROcp3_25*C33+ROcp3_532*S33
  ROcp3_333 = ROcp3_632*S33-C33*S5
  ROcp3_433 = -(ROcp3_15*S33-ROcp3_432*C33)
  ROcp3_533 = -(ROcp3_25*S33-ROcp3_532*C33)
  ROcp3_633 = ROcp3_632*C33+S33*S5
  ROcp3_434 = ROcp3_433*C34+ROcp3_732*S34
  ROcp3_534 = ROcp3_533*C34+ROcp3_832*S34
  ROcp3_634 = ROcp3_633*C34+ROcp3_932*S34
  ROcp3_734 = -(ROcp3_433*S34-ROcp3_732*C34)
  ROcp3_834 = -(ROcp3_533*S34-ROcp3_832*C34)
  ROcp3_934 = -(ROcp3_633*S34-ROcp3_932*C34)
  ROcp3_135 = ROcp3_133*C35-ROcp3_734*S35
  ROcp3_235 = ROcp3_233*C35-ROcp3_834*S35
  ROcp3_335 = ROcp3_333*C35-ROcp3_934*S35
  ROcp3_735 = ROcp3_133*S35+ROcp3_734*C35
  ROcp3_835 = ROcp3_233*S35+ROcp3_834*C35
  ROcp3_935 = ROcp3_333*S35+ROcp3_934*C35
  ROcp3_136 = ROcp3_135*C36+ROcp3_434*S36
  ROcp3_236 = ROcp3_235*C36+ROcp3_534*S36
  ROcp3_336 = ROcp3_335*C36+ROcp3_634*S36
  ROcp3_436 = -(ROcp3_135*S36-ROcp3_434*C36)
  ROcp3_536 = -(ROcp3_235*S36-ROcp3_534*C36)
  ROcp3_636 = -(ROcp3_335*S36-ROcp3_634*C36)
  RLcp3_132 = ROcp3_15*s.dpt[1,12]+ROcp3_46*s.dpt[2,12]
  RLcp3_232 = ROcp3_25*s.dpt[1,12]+ROcp3_56*s.dpt[2,12]
  RLcp3_332 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
  OMcp3_132 = OMcp3_16+qd[32]*ROcp3_15
  OMcp3_232 = OMcp3_26+qd[32]*ROcp3_25
  OMcp3_332 = OMcp3_36-qd[32]*S5
  ORcp3_132 = OMcp3_26*RLcp3_332-OMcp3_36*RLcp3_232
  ORcp3_232 = -(OMcp3_16*RLcp3_332-OMcp3_36*RLcp3_132)
  ORcp3_332 = OMcp3_16*RLcp3_232-OMcp3_26*RLcp3_132
  OMcp3_133 = OMcp3_132+qd[33]*ROcp3_732
  OMcp3_233 = OMcp3_232+qd[33]*ROcp3_832
  OMcp3_333 = OMcp3_332+qd[33]*ROcp3_932
  OPcp3_133 = OPcp3_16-qd[32]*(OMcp3_26*S5+OMcp3_36*ROcp3_25)+qd[33]*(OMcp3_232*ROcp3_932-OMcp3_332*ROcp3_832)+qdd[32]*\
   ROcp3_15+qdd[33]*ROcp3_732
  OPcp3_233 = OPcp3_26+qd[32]*(OMcp3_16*S5+OMcp3_36*ROcp3_15)-qd[33]*(OMcp3_132*ROcp3_932-OMcp3_332*ROcp3_732)+qdd[32]*\
   ROcp3_25+qdd[33]*ROcp3_832
  OPcp3_333 = OPcp3_36+qd[32]*(OMcp3_16*ROcp3_25-OMcp3_26*ROcp3_15)+qd[33]*(OMcp3_132*ROcp3_832-OMcp3_232*ROcp3_732)-\
   qdd[32]*S5+qdd[33]*ROcp3_932
  RLcp3_134 = ROcp3_433*s.dpt[2,33]
  RLcp3_234 = ROcp3_533*s.dpt[2,33]
  RLcp3_334 = ROcp3_633*s.dpt[2,33]
  OMcp3_134 = OMcp3_133+qd[34]*ROcp3_133
  OMcp3_234 = OMcp3_233+qd[34]*ROcp3_233
  OMcp3_334 = OMcp3_333+qd[34]*ROcp3_333
  ORcp3_134 = OMcp3_233*RLcp3_334-OMcp3_333*RLcp3_234
  ORcp3_234 = -(OMcp3_133*RLcp3_334-OMcp3_333*RLcp3_134)
  ORcp3_334 = OMcp3_133*RLcp3_234-OMcp3_233*RLcp3_134
  OMcp3_135 = OMcp3_134+qd[35]*ROcp3_434
  OMcp3_235 = OMcp3_234+qd[35]*ROcp3_534
  OMcp3_335 = OMcp3_334+qd[35]*ROcp3_634
  OMcp3_136 = OMcp3_135+qd[36]*ROcp3_735
  OMcp3_236 = OMcp3_235+qd[36]*ROcp3_835
  OMcp3_336 = OMcp3_335+qd[36]*ROcp3_935
  OPcp3_136 = OPcp3_133+qd[34]*(OMcp3_233*ROcp3_333-OMcp3_333*ROcp3_233)+qd[35]*(OMcp3_234*ROcp3_634-OMcp3_334*ROcp3_534\
   )+qd[36]*(OMcp3_235*ROcp3_935-OMcp3_335*ROcp3_835)+qdd[34]*ROcp3_133+qdd[35]*ROcp3_434+qdd[36]*ROcp3_735
  OPcp3_236 = OPcp3_233-qd[34]*(OMcp3_133*ROcp3_333-OMcp3_333*ROcp3_133)-qd[35]*(OMcp3_134*ROcp3_634-OMcp3_334*ROcp3_434\
   )-qd[36]*(OMcp3_135*ROcp3_935-OMcp3_335*ROcp3_735)+qdd[34]*ROcp3_233+qdd[35]*ROcp3_534+qdd[36]*ROcp3_835
  OPcp3_336 = OPcp3_333+qd[34]*(OMcp3_133*ROcp3_233-OMcp3_233*ROcp3_133)+qd[35]*(OMcp3_134*ROcp3_534-OMcp3_234*ROcp3_434\
   )+qd[36]*(OMcp3_135*ROcp3_835-OMcp3_235*ROcp3_735)+qdd[34]*ROcp3_333+qdd[35]*ROcp3_634+qdd[36]*ROcp3_935

# = = Block_0_0_1_4_0_13 = = 
 
# Sensor Kinematics 


  ROcp3_439 = ROcp3_436*C39+ROcp3_735*S39
  ROcp3_539 = ROcp3_536*C39+ROcp3_835*S39
  ROcp3_639 = ROcp3_636*C39+ROcp3_935*S39
  ROcp3_739 = -(ROcp3_436*S39-ROcp3_735*C39)
  ROcp3_839 = -(ROcp3_536*S39-ROcp3_835*C39)
  ROcp3_939 = -(ROcp3_636*S39-ROcp3_935*C39)
  ROcp3_140 = ROcp3_136*C40-ROcp3_739*S40
  ROcp3_240 = ROcp3_236*C40-ROcp3_839*S40
  ROcp3_340 = ROcp3_336*C40-ROcp3_939*S40
  ROcp3_740 = ROcp3_136*S40+ROcp3_739*C40
  ROcp3_840 = ROcp3_236*S40+ROcp3_839*C40
  ROcp3_940 = ROcp3_336*S40+ROcp3_939*C40
  RLcp3_139 = ROcp3_735*s.dpt[3,37]
  RLcp3_239 = ROcp3_835*s.dpt[3,37]
  RLcp3_339 = ROcp3_935*s.dpt[3,37]
  OMcp3_139 = OMcp3_136+qd[39]*ROcp3_136
  OMcp3_239 = OMcp3_236+qd[39]*ROcp3_236
  OMcp3_339 = OMcp3_336+qd[39]*ROcp3_336
  ORcp3_139 = OMcp3_236*RLcp3_339-OMcp3_336*RLcp3_239
  ORcp3_239 = -(OMcp3_136*RLcp3_339-OMcp3_336*RLcp3_139)
  ORcp3_339 = OMcp3_136*RLcp3_239-OMcp3_236*RLcp3_139
  PxF4[1] = q[1]+RLcp3_132+RLcp3_134+RLcp3_139
  PxF4[2] = q[2]+RLcp3_232+RLcp3_234+RLcp3_239
  PxF4[3] = q[3]+RLcp3_332+RLcp3_334+RLcp3_339
  RxF4[1,1] = ROcp3_140
  RxF4[1,2] = ROcp3_240
  RxF4[1,3] = ROcp3_340
  RxF4[2,1] = ROcp3_439
  RxF4[2,2] = ROcp3_539
  RxF4[2,3] = ROcp3_639
  RxF4[3,1] = ROcp3_740
  RxF4[3,2] = ROcp3_840
  RxF4[3,3] = ROcp3_940
  VxF4[1] = qd[1]+ORcp3_132+ORcp3_134+ORcp3_139
  VxF4[2] = qd[2]+ORcp3_232+ORcp3_234+ORcp3_239
  VxF4[3] = qd[3]+ORcp3_332+ORcp3_334+ORcp3_339
  OMxF4[1] = OMcp3_139+qd[40]*ROcp3_439
  OMxF4[2] = OMcp3_239+qd[40]*ROcp3_539
  OMxF4[3] = OMcp3_339+qd[40]*ROcp3_639
  AxF4[1] = qdd[1]+OMcp3_233*ORcp3_334+OMcp3_236*ORcp3_339+OMcp3_26*ORcp3_332-OMcp3_333*ORcp3_234-OMcp3_336*ORcp3_239-\
   OMcp3_36*ORcp3_232+OPcp3_233*RLcp3_334+OPcp3_236*RLcp3_339+OPcp3_26*RLcp3_332-OPcp3_333*RLcp3_234-OPcp3_336*RLcp3_239-\
   OPcp3_36*RLcp3_232
  AxF4[2] = qdd[2]-OMcp3_133*ORcp3_334-OMcp3_136*ORcp3_339-OMcp3_16*ORcp3_332+OMcp3_333*ORcp3_134+OMcp3_336*ORcp3_139+\
   OMcp3_36*ORcp3_132-OPcp3_133*RLcp3_334-OPcp3_136*RLcp3_339-OPcp3_16*RLcp3_332+OPcp3_333*RLcp3_134+OPcp3_336*RLcp3_139+\
   OPcp3_36*RLcp3_132
  AxF4[3] = qdd[3]+OMcp3_133*ORcp3_234+OMcp3_136*ORcp3_239+OMcp3_16*ORcp3_232-OMcp3_233*ORcp3_134-OMcp3_236*ORcp3_139-\
   OMcp3_26*ORcp3_132+OPcp3_133*RLcp3_234+OPcp3_136*RLcp3_239+OPcp3_16*RLcp3_232-OPcp3_233*RLcp3_134-OPcp3_236*RLcp3_139-\
   OPcp3_26*RLcp3_132
  OMPxF4[1] = OPcp3_136+qd[39]*(OMcp3_236*ROcp3_336-OMcp3_336*ROcp3_236)+qd[40]*(OMcp3_239*ROcp3_639-OMcp3_339*ROcp3_539\
   )+qdd[39]*ROcp3_136+qdd[40]*ROcp3_439
  OMPxF4[2] = OPcp3_236-qd[39]*(OMcp3_136*ROcp3_336-OMcp3_336*ROcp3_136)-qd[40]*(OMcp3_139*ROcp3_639-OMcp3_339*ROcp3_439\
   )+qdd[39]*ROcp3_236+qdd[40]*ROcp3_539
  OMPxF4[3] = OPcp3_336+qd[39]*(OMcp3_136*ROcp3_236-OMcp3_236*ROcp3_136)+qd[40]*(OMcp3_139*ROcp3_539-OMcp3_239*ROcp3_439\
   )+qdd[39]*ROcp3_336+qdd[40]*ROcp3_639
 
# Sensor Forces Computation 

  SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc14 = ROcp3_140*SWr4[1]+ROcp3_240*SWr4[2]+ROcp3_340*SWr4[3]
  xfrc24 = ROcp3_439*SWr4[1]+ROcp3_539*SWr4[2]+ROcp3_639*SWr4[3]
  xfrc34 = ROcp3_740*SWr4[1]+ROcp3_840*SWr4[2]+ROcp3_940*SWr4[3]
  frc[1,40] = s.frc[1,40]+xfrc14
  frc[2,40] = s.frc[2,40]+xfrc24
  frc[3,40] = s.frc[3,40]+xfrc34
  xtrq14 = ROcp3_140*SWr4[4]+ROcp3_240*SWr4[5]+ROcp3_340*SWr4[6]
  xtrq24 = ROcp3_439*SWr4[4]+ROcp3_539*SWr4[5]+ROcp3_639*SWr4[6]
  xtrq34 = ROcp3_740*SWr4[4]+ROcp3_840*SWr4[5]+ROcp3_940*SWr4[6]
  trq[1,40] = s.trq[1,40]+xtrq14-xfrc24*SWr4[9]+xfrc34*SWr4[8]
  trq[2,40] = s.trq[2,40]+xtrq24+xfrc14*SWr4[9]-xfrc34*SWr4[7]
  trq[3,40] = s.trq[3,40]+xtrq34-xfrc14*SWr4[8]+xfrc24*SWr4[7]

# = = Block_0_0_1_4_1_0 = = 
 
# Symbolic Outputs  

  frc[1,6] = s.frc[1,6]
  frc[2,6] = s.frc[2,6]
  frc[3,6] = s.frc[3,6]
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
  frc[1,27] = s.frc[1,27]
  frc[2,27] = s.frc[2,27]
  frc[3,27] = s.frc[3,27]
  frc[1,29] = s.frc[1,29]
  frc[2,29] = s.frc[2,29]
  frc[3,29] = s.frc[3,29]
  frc[1,33] = s.frc[1,33]
  frc[2,33] = s.frc[2,33]
  frc[3,33] = s.frc[3,33]
  frc[1,36] = s.frc[1,36]
  frc[2,36] = s.frc[2,36]
  frc[3,36] = s.frc[3,36]
  frc[1,38] = s.frc[1,38]
  frc[2,38] = s.frc[2,38]
  frc[3,38] = s.frc[3,38]
  frc[1,41] = s.frc[1,41]
  frc[2,41] = s.frc[2,41]
  frc[3,41] = s.frc[3,41]
  trq[1,6] = s.trq[1,6]
  trq[2,6] = s.trq[2,6]
  trq[3,6] = s.trq[3,6]
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
  trq[1,27] = s.trq[1,27]
  trq[2,27] = s.trq[2,27]
  trq[3,27] = s.trq[3,27]
  trq[1,29] = s.trq[1,29]
  trq[2,29] = s.trq[2,29]
  trq[3,29] = s.trq[3,29]
  trq[1,33] = s.trq[1,33]
  trq[2,33] = s.trq[2,33]
  trq[3,33] = s.trq[3,33]
  trq[1,36] = s.trq[1,36]
  trq[2,36] = s.trq[2,36]
  trq[3,36] = s.trq[3,36]
  trq[1,38] = s.trq[1,38]
  trq[2,38] = s.trq[2,38]
  trq[3,38] = s.trq[3,38]
  trq[1,41] = s.trq[1,41]
  trq[2,41] = s.trq[2,41]
  trq[3,41] = s.trq[3,41]

# ====== END Task 0 ====== 

  

