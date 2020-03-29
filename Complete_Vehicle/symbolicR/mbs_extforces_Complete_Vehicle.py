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
#	==> Generation Date : Sat Mar 28 19:52:50 2020
#
#	==> Project name : Complete_Vehicle
#	==> using XML input file 
#
#	==> Number of joints : 38
#
#	==> Function : F19 : External Forces
#	==> Flops complexity : 2000
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

# = = Block_0_0_0_0_0_10 = = 
 
# Trigonometric Variables  

  C29 = np.cos(q[29])
  S29 = np.sin(q[29])
  C30 = np.cos(q[30])
  S30 = np.sin(q[30])

# = = Block_0_0_0_0_0_11 = = 
 
# Trigonometric Variables  

  C31 = np.cos(q[31])
  S31 = np.sin(q[31])
  C32 = np.cos(q[32])
  S32 = np.sin(q[32])
  C33 = np.cos(q[33])
  S33 = np.sin(q[33])
  C34 = np.cos(q[34])
  S34 = np.sin(q[34])

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C37 = np.cos(q[37])
  S37 = np.sin(q[37])
  C38 = np.cos(q[38])
  S38 = np.sin(q[38])

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
  RLcp0_17 = ROcp0_15*s.dpt[1,1]+ROcp0_46*s.dpt[2,1]+ROcp0_76*s.dpt[3,1]
  RLcp0_27 = ROcp0_25*s.dpt[1,1]+ROcp0_56*s.dpt[2,1]+ROcp0_86*s.dpt[3,1]
  RLcp0_37 = C5*C6*s.dpt[3,1]-s.dpt[1,1]*S5+s.dpt[2,1]*C5*S6
  OMcp0_17 = OMcp0_16+qd[7]*ROcp0_15
  OMcp0_27 = OMcp0_26+qd[7]*ROcp0_25
  OMcp0_37 = OMcp0_36-qd[7]*S5
  ORcp0_17 = OMcp0_26*RLcp0_37-OMcp0_36*RLcp0_27
  ORcp0_27 = -(OMcp0_16*RLcp0_37-OMcp0_36*RLcp0_17)
  ORcp0_37 = OMcp0_16*RLcp0_27-OMcp0_26*RLcp0_17
  OPcp0_17 = OPcp0_16-qd[7]*(OMcp0_26*S5+OMcp0_36*ROcp0_25)+qdd[7]*ROcp0_15
  OPcp0_27 = OPcp0_26+qd[7]*(OMcp0_16*S5+OMcp0_36*ROcp0_15)+qdd[7]*ROcp0_25
  OPcp0_37 = OPcp0_36+qd[7]*(OMcp0_16*ROcp0_25-OMcp0_26*ROcp0_15)-qdd[7]*S5
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
  OMcp0_110 = OMcp0_19+qd[10]*ROcp0_49
  OMcp0_210 = OMcp0_29+qd[10]*ROcp0_59
  OMcp0_310 = OMcp0_39+qd[10]*ROcp0_69

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
  OMcp0_113 = OMcp0_110+qd[13]*ROcp0_110
  OMcp0_213 = OMcp0_210+qd[13]*ROcp0_210
  OMcp0_313 = OMcp0_310+qd[13]*ROcp0_310
  PxF1[1] = q[1]+RLcp0_17+RLcp0_18
  PxF1[2] = q[2]+RLcp0_27+RLcp0_28
  PxF1[3] = q[3]+RLcp0_37+RLcp0_38
  RxF1[1,1] = ROcp0_114
  RxF1[1,2] = ROcp0_214
  RxF1[1,3] = ROcp0_314
  RxF1[2,1] = ROcp0_413
  RxF1[2,2] = ROcp0_513
  RxF1[2,3] = ROcp0_613
  RxF1[3,1] = ROcp0_714
  RxF1[3,2] = ROcp0_814
  RxF1[3,3] = ROcp0_914
  VxF1[1] = qd[1]+ORcp0_17+ORcp0_18
  VxF1[2] = qd[2]+ORcp0_27+ORcp0_28
  VxF1[3] = qd[3]+ORcp0_37+ORcp0_38
  OMxF1[1] = OMcp0_113+qd[14]*ROcp0_413
  OMxF1[2] = OMcp0_213+qd[14]*ROcp0_513
  OMxF1[3] = OMcp0_313+qd[14]*ROcp0_613
  AxF1[1] = qdd[1]+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_36*ORcp0_27-OMcp0_37*ORcp0_28+OPcp0_26*RLcp0_37+OPcp0_27*\
   RLcp0_38-OPcp0_36*RLcp0_27-OPcp0_37*RLcp0_28
  AxF1[2] = qdd[2]-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_36*ORcp0_17+OMcp0_37*ORcp0_18-OPcp0_16*RLcp0_37-OPcp0_17*\
   RLcp0_38+OPcp0_36*RLcp0_17+OPcp0_37*RLcp0_18
  AxF1[3] = qdd[3]+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_26*ORcp0_17-OMcp0_27*ORcp0_18+OPcp0_16*RLcp0_27+OPcp0_17*\
   RLcp0_28-OPcp0_26*RLcp0_17-OPcp0_27*RLcp0_18
  OMPxF1[1] = OPcp0_17+qd[10]*(OMcp0_29*ROcp0_69-OMcp0_39*ROcp0_59)+qd[13]*(OMcp0_210*ROcp0_310-OMcp0_310*ROcp0_210)+\
   qd[14]*(OMcp0_213*ROcp0_613-OMcp0_313*ROcp0_513)+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(OMcp0_28*ROcp0_38-\
   OMcp0_38*ROcp0_28)+qdd[10]*ROcp0_49+qdd[13]*ROcp0_110+qdd[14]*ROcp0_413+qdd[8]*ROcp0_77+qdd[9]*ROcp0_18
  OMPxF1[2] = OPcp0_27-qd[10]*(OMcp0_19*ROcp0_69-OMcp0_39*ROcp0_49)-qd[13]*(OMcp0_110*ROcp0_310-OMcp0_310*ROcp0_110)-\
   qd[14]*(OMcp0_113*ROcp0_613-OMcp0_313*ROcp0_413)-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(OMcp0_18*ROcp0_38-\
   OMcp0_38*ROcp0_18)+qdd[10]*ROcp0_59+qdd[13]*ROcp0_210+qdd[14]*ROcp0_513+qdd[8]*ROcp0_87+qdd[9]*ROcp0_28
  OMPxF1[3] = OPcp0_37+qd[10]*(OMcp0_19*ROcp0_59-OMcp0_29*ROcp0_49)+qd[13]*(OMcp0_110*ROcp0_210-OMcp0_210*ROcp0_110)+\
   qd[14]*(OMcp0_113*ROcp0_513-OMcp0_213*ROcp0_413)+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(OMcp0_18*ROcp0_28-\
   OMcp0_28*ROcp0_18)+qdd[10]*ROcp0_69+qdd[13]*ROcp0_310+qdd[14]*ROcp0_613+qdd[8]*ROcp0_97+qdd[9]*ROcp0_38
 
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
  RLcp1_115 = ROcp1_15*s.dpt[1,4]+ROcp1_46*s.dpt[2,4]+ROcp1_76*s.dpt[3,4]
  RLcp1_215 = ROcp1_25*s.dpt[1,4]+ROcp1_56*s.dpt[2,4]+ROcp1_86*s.dpt[3,4]
  RLcp1_315 = C5*C6*s.dpt[3,4]-s.dpt[1,4]*S5+s.dpt[2,4]*C5*S6
  OMcp1_115 = OMcp1_16+qd[15]*ROcp1_15
  OMcp1_215 = OMcp1_26+qd[15]*ROcp1_25
  OMcp1_315 = OMcp1_36-qd[15]*S5
  ORcp1_115 = OMcp1_26*RLcp1_315-OMcp1_36*RLcp1_215
  ORcp1_215 = -(OMcp1_16*RLcp1_315-OMcp1_36*RLcp1_115)
  ORcp1_315 = OMcp1_16*RLcp1_215-OMcp1_26*RLcp1_115
  OPcp1_115 = OPcp1_16-qd[15]*(OMcp1_26*S5+OMcp1_36*ROcp1_25)+qdd[15]*ROcp1_15
  OPcp1_215 = OPcp1_26+qd[15]*(OMcp1_16*S5+OMcp1_36*ROcp1_15)+qdd[15]*ROcp1_25
  OPcp1_315 = OPcp1_36+qd[15]*(OMcp1_16*ROcp1_25-OMcp1_26*ROcp1_15)-qdd[15]*S5
  RLcp1_116 = ROcp1_415*s.dpt[2,18]
  RLcp1_216 = ROcp1_515*s.dpt[2,18]
  RLcp1_316 = ROcp1_615*s.dpt[2,18]
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
  OMcp1_121 = OMcp1_118+qd[21]*ROcp1_118
  OMcp1_221 = OMcp1_218+qd[21]*ROcp1_218
  OMcp1_321 = OMcp1_318+qd[21]*ROcp1_318
  PxF2[1] = q[1]+RLcp1_115+RLcp1_116
  PxF2[2] = q[2]+RLcp1_215+RLcp1_216
  PxF2[3] = q[3]+RLcp1_315+RLcp1_316
  RxF2[1,1] = ROcp1_122
  RxF2[1,2] = ROcp1_222
  RxF2[1,3] = ROcp1_322
  RxF2[2,1] = ROcp1_421
  RxF2[2,2] = ROcp1_521
  RxF2[2,3] = ROcp1_621
  RxF2[3,1] = ROcp1_722
  RxF2[3,2] = ROcp1_822
  RxF2[3,3] = ROcp1_922
  VxF2[1] = qd[1]+ORcp1_115+ORcp1_116
  VxF2[2] = qd[2]+ORcp1_215+ORcp1_216
  VxF2[3] = qd[3]+ORcp1_315+ORcp1_316
  OMxF2[1] = OMcp1_121+qd[22]*ROcp1_421
  OMxF2[2] = OMcp1_221+qd[22]*ROcp1_521
  OMxF2[3] = OMcp1_321+qd[22]*ROcp1_621
  AxF2[1] = qdd[1]+OMcp1_215*ORcp1_316+OMcp1_26*ORcp1_315-OMcp1_315*ORcp1_216-OMcp1_36*ORcp1_215+OPcp1_215*RLcp1_316+\
   OPcp1_26*RLcp1_315-OPcp1_315*RLcp1_216-OPcp1_36*RLcp1_215
  AxF2[2] = qdd[2]-OMcp1_115*ORcp1_316-OMcp1_16*ORcp1_315+OMcp1_315*ORcp1_116+OMcp1_36*ORcp1_115-OPcp1_115*RLcp1_316-\
   OPcp1_16*RLcp1_315+OPcp1_315*RLcp1_116+OPcp1_36*RLcp1_115
  AxF2[3] = qdd[3]+OMcp1_115*ORcp1_216+OMcp1_16*ORcp1_215-OMcp1_215*ORcp1_116-OMcp1_26*ORcp1_115+OPcp1_115*RLcp1_216+\
   OPcp1_16*RLcp1_215-OPcp1_215*RLcp1_116-OPcp1_26*RLcp1_115
  OMPxF2[1] = OPcp1_115+qd[16]*(OMcp1_215*ROcp1_915-OMcp1_315*ROcp1_815)+qd[17]*(OMcp1_216*ROcp1_316-OMcp1_316*ROcp1_216\
   )+qd[18]*(OMcp1_217*ROcp1_617-OMcp1_317*ROcp1_517)+qd[21]*(OMcp1_218*ROcp1_318-OMcp1_318*ROcp1_218)+qd[22]*(OMcp1_221*\
   ROcp1_621-OMcp1_321*ROcp1_521)+qdd[16]*ROcp1_715+qdd[17]*ROcp1_116+qdd[18]*ROcp1_417+qdd[21]*ROcp1_118+qdd[22]*ROcp1_421
  OMPxF2[2] = OPcp1_215-qd[16]*(OMcp1_115*ROcp1_915-OMcp1_315*ROcp1_715)-qd[17]*(OMcp1_116*ROcp1_316-OMcp1_316*ROcp1_116\
   )-qd[18]*(OMcp1_117*ROcp1_617-OMcp1_317*ROcp1_417)-qd[21]*(OMcp1_118*ROcp1_318-OMcp1_318*ROcp1_118)-qd[22]*(OMcp1_121*\
   ROcp1_621-OMcp1_321*ROcp1_421)+qdd[16]*ROcp1_815+qdd[17]*ROcp1_216+qdd[18]*ROcp1_517+qdd[21]*ROcp1_218+qdd[22]*ROcp1_521
  OMPxF2[3] = OPcp1_315+qd[16]*(OMcp1_115*ROcp1_815-OMcp1_215*ROcp1_715)+qd[17]*(OMcp1_116*ROcp1_216-OMcp1_216*ROcp1_116\
   )+qd[18]*(OMcp1_117*ROcp1_517-OMcp1_217*ROcp1_417)+qd[21]*(OMcp1_118*ROcp1_218-OMcp1_218*ROcp1_118)+qd[22]*(OMcp1_121*\
   ROcp1_521-OMcp1_221*ROcp1_421)+qdd[16]*ROcp1_915+qdd[17]*ROcp1_316+qdd[18]*ROcp1_617+qdd[21]*ROcp1_318+qdd[22]*ROcp1_621
 
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
  ROcp2_126 = ROcp2_124*C26+ROcp2_425*S26
  ROcp2_226 = ROcp2_224*C26+ROcp2_525*S26
  ROcp2_326 = ROcp2_324*C26+ROcp2_625*S26
  ROcp2_426 = -(ROcp2_124*S26-ROcp2_425*C26)
  ROcp2_526 = -(ROcp2_224*S26-ROcp2_525*C26)
  ROcp2_626 = -(ROcp2_324*S26-ROcp2_625*C26)
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
  RLcp2_125 = ROcp2_424*s.dpt[2,23]
  RLcp2_225 = ROcp2_524*s.dpt[2,23]
  RLcp2_325 = ROcp2_624*s.dpt[2,23]
  OMcp2_125 = OMcp2_124+qd[25]*ROcp2_124
  OMcp2_225 = OMcp2_224+qd[25]*ROcp2_224
  OMcp2_325 = OMcp2_324+qd[25]*ROcp2_324
  ORcp2_125 = OMcp2_224*RLcp2_325-OMcp2_324*RLcp2_225
  ORcp2_225 = -(OMcp2_124*RLcp2_325-OMcp2_324*RLcp2_125)
  ORcp2_325 = OMcp2_124*RLcp2_225-OMcp2_224*RLcp2_125
  OMcp2_126 = OMcp2_125+qd[26]*ROcp2_725
  OMcp2_226 = OMcp2_225+qd[26]*ROcp2_825
  OMcp2_326 = OMcp2_325+qd[26]*ROcp2_925
  OPcp2_126 = OPcp2_124+qd[25]*(OMcp2_224*ROcp2_324-OMcp2_324*ROcp2_224)+qd[26]*(OMcp2_225*ROcp2_925-OMcp2_325*ROcp2_825\
   )+qdd[25]*ROcp2_124+qdd[26]*ROcp2_725
  OPcp2_226 = OPcp2_224-qd[25]*(OMcp2_124*ROcp2_324-OMcp2_324*ROcp2_124)-qd[26]*(OMcp2_125*ROcp2_925-OMcp2_325*ROcp2_725\
   )+qdd[25]*ROcp2_224+qdd[26]*ROcp2_825
  OPcp2_326 = OPcp2_324+qd[25]*(OMcp2_124*ROcp2_224-OMcp2_224*ROcp2_124)+qd[26]*(OMcp2_125*ROcp2_825-OMcp2_225*ROcp2_725\
   )+qdd[25]*ROcp2_324+qdd[26]*ROcp2_925

# = = Block_0_0_1_3_0_10 = = 
 
# Sensor Kinematics 


  ROcp2_429 = ROcp2_426*C29+ROcp2_725*S29
  ROcp2_529 = ROcp2_526*C29+ROcp2_825*S29
  ROcp2_629 = ROcp2_626*C29+ROcp2_925*S29
  ROcp2_729 = -(ROcp2_426*S29-ROcp2_725*C29)
  ROcp2_829 = -(ROcp2_526*S29-ROcp2_825*C29)
  ROcp2_929 = -(ROcp2_626*S29-ROcp2_925*C29)
  ROcp2_130 = ROcp2_126*C30-ROcp2_729*S30
  ROcp2_230 = ROcp2_226*C30-ROcp2_829*S30
  ROcp2_330 = ROcp2_326*C30-ROcp2_929*S30
  ROcp2_730 = ROcp2_126*S30+ROcp2_729*C30
  ROcp2_830 = ROcp2_226*S30+ROcp2_829*C30
  ROcp2_930 = ROcp2_326*S30+ROcp2_929*C30
  RLcp2_129 = ROcp2_725*s.dpt[3,25]
  RLcp2_229 = ROcp2_825*s.dpt[3,25]
  RLcp2_329 = ROcp2_925*s.dpt[3,25]
  OMcp2_129 = OMcp2_126+qd[29]*ROcp2_126
  OMcp2_229 = OMcp2_226+qd[29]*ROcp2_226
  OMcp2_329 = OMcp2_326+qd[29]*ROcp2_326
  ORcp2_129 = OMcp2_226*RLcp2_329-OMcp2_326*RLcp2_229
  ORcp2_229 = -(OMcp2_126*RLcp2_329-OMcp2_326*RLcp2_129)
  ORcp2_329 = OMcp2_126*RLcp2_229-OMcp2_226*RLcp2_129
  PxF3[1] = q[1]+RLcp2_123+RLcp2_125+RLcp2_129
  PxF3[2] = q[2]+RLcp2_223+RLcp2_225+RLcp2_229
  PxF3[3] = q[3]+RLcp2_323+RLcp2_325+RLcp2_329
  RxF3[1,1] = ROcp2_130
  RxF3[1,2] = ROcp2_230
  RxF3[1,3] = ROcp2_330
  RxF3[2,1] = ROcp2_429
  RxF3[2,2] = ROcp2_529
  RxF3[2,3] = ROcp2_629
  RxF3[3,1] = ROcp2_730
  RxF3[3,2] = ROcp2_830
  RxF3[3,3] = ROcp2_930
  VxF3[1] = qd[1]+ORcp2_123+ORcp2_125+ORcp2_129
  VxF3[2] = qd[2]+ORcp2_223+ORcp2_225+ORcp2_229
  VxF3[3] = qd[3]+ORcp2_323+ORcp2_325+ORcp2_329
  OMxF3[1] = OMcp2_129+qd[30]*ROcp2_429
  OMxF3[2] = OMcp2_229+qd[30]*ROcp2_529
  OMxF3[3] = OMcp2_329+qd[30]*ROcp2_629
  AxF3[1] = qdd[1]+OMcp2_224*ORcp2_325+OMcp2_226*ORcp2_329+OMcp2_26*ORcp2_323-OMcp2_324*ORcp2_225-OMcp2_326*ORcp2_229-\
   OMcp2_36*ORcp2_223+OPcp2_224*RLcp2_325+OPcp2_226*RLcp2_329+OPcp2_26*RLcp2_323-OPcp2_324*RLcp2_225-OPcp2_326*RLcp2_229-\
   OPcp2_36*RLcp2_223
  AxF3[2] = qdd[2]-OMcp2_124*ORcp2_325-OMcp2_126*ORcp2_329-OMcp2_16*ORcp2_323+OMcp2_324*ORcp2_125+OMcp2_326*ORcp2_129+\
   OMcp2_36*ORcp2_123-OPcp2_124*RLcp2_325-OPcp2_126*RLcp2_329-OPcp2_16*RLcp2_323+OPcp2_324*RLcp2_125+OPcp2_326*RLcp2_129+\
   OPcp2_36*RLcp2_123
  AxF3[3] = qdd[3]+OMcp2_124*ORcp2_225+OMcp2_126*ORcp2_229+OMcp2_16*ORcp2_223-OMcp2_224*ORcp2_125-OMcp2_226*ORcp2_129-\
   OMcp2_26*ORcp2_123+OPcp2_124*RLcp2_225+OPcp2_126*RLcp2_229+OPcp2_16*RLcp2_223-OPcp2_224*RLcp2_125-OPcp2_226*RLcp2_129-\
   OPcp2_26*RLcp2_123
  OMPxF3[1] = OPcp2_126+qd[29]*(OMcp2_226*ROcp2_326-OMcp2_326*ROcp2_226)+qd[30]*(OMcp2_229*ROcp2_629-OMcp2_329*ROcp2_529\
   )+qdd[29]*ROcp2_126+qdd[30]*ROcp2_429
  OMPxF3[2] = OPcp2_226-qd[29]*(OMcp2_126*ROcp2_326-OMcp2_326*ROcp2_126)-qd[30]*(OMcp2_129*ROcp2_629-OMcp2_329*ROcp2_429\
   )+qdd[29]*ROcp2_226+qdd[30]*ROcp2_529
  OMPxF3[3] = OPcp2_326+qd[29]*(OMcp2_126*ROcp2_226-OMcp2_226*ROcp2_126)+qd[30]*(OMcp2_129*ROcp2_529-OMcp2_229*ROcp2_429\
   )+qdd[29]*ROcp2_326+qdd[30]*ROcp2_629
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc13 = ROcp2_130*SWr3[1]+ROcp2_230*SWr3[2]+ROcp2_330*SWr3[3]
  xfrc23 = ROcp2_429*SWr3[1]+ROcp2_529*SWr3[2]+ROcp2_629*SWr3[3]
  xfrc33 = ROcp2_730*SWr3[1]+ROcp2_830*SWr3[2]+ROcp2_930*SWr3[3]
  frc[1,30] = s.frc[1,30]+xfrc13
  frc[2,30] = s.frc[2,30]+xfrc23
  frc[3,30] = s.frc[3,30]+xfrc33
  xtrq13 = ROcp2_130*SWr3[4]+ROcp2_230*SWr3[5]+ROcp2_330*SWr3[6]
  xtrq23 = ROcp2_429*SWr3[4]+ROcp2_529*SWr3[5]+ROcp2_629*SWr3[6]
  xtrq33 = ROcp2_730*SWr3[4]+ROcp2_830*SWr3[5]+ROcp2_930*SWr3[6]
  trq[1,30] = s.trq[1,30]+xtrq13-xfrc23*SWr3[9]+xfrc33*SWr3[8]
  trq[2,30] = s.trq[2,30]+xtrq23+xfrc13*SWr3[9]-xfrc33*SWr3[7]
  trq[3,30] = s.trq[3,30]+xtrq33-xfrc13*SWr3[8]+xfrc23*SWr3[7]

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

  S31p6 = C31*S6+S31*C6
  C31p6 = C31*C6-S31*S6
 
# Sensor Kinematics 


  ROcp3_431 = ROcp3_46*C31+ROcp3_76*S31
  ROcp3_531 = ROcp3_56*C31+ROcp3_86*S31
  ROcp3_631 = S31p6*C5
  ROcp3_731 = -(ROcp3_46*S31-ROcp3_76*C31)
  ROcp3_831 = -(ROcp3_56*S31-ROcp3_86*C31)
  ROcp3_931 = C31p6*C5
  ROcp3_132 = ROcp3_15*C32+ROcp3_431*S32
  ROcp3_232 = ROcp3_25*C32+ROcp3_531*S32
  ROcp3_332 = ROcp3_631*S32-C32*S5
  ROcp3_432 = -(ROcp3_15*S32-ROcp3_431*C32)
  ROcp3_532 = -(ROcp3_25*S32-ROcp3_531*C32)
  ROcp3_632 = ROcp3_631*C32+S32*S5
  ROcp3_433 = ROcp3_432*C33+ROcp3_731*S33
  ROcp3_533 = ROcp3_532*C33+ROcp3_831*S33
  ROcp3_633 = ROcp3_632*C33+ROcp3_931*S33
  ROcp3_733 = -(ROcp3_432*S33-ROcp3_731*C33)
  ROcp3_833 = -(ROcp3_532*S33-ROcp3_831*C33)
  ROcp3_933 = -(ROcp3_632*S33-ROcp3_931*C33)
  ROcp3_134 = ROcp3_132*C34+ROcp3_433*S34
  ROcp3_234 = ROcp3_232*C34+ROcp3_533*S34
  ROcp3_334 = ROcp3_332*C34+ROcp3_633*S34
  ROcp3_434 = -(ROcp3_132*S34-ROcp3_433*C34)
  ROcp3_534 = -(ROcp3_232*S34-ROcp3_533*C34)
  ROcp3_634 = -(ROcp3_332*S34-ROcp3_633*C34)
  RLcp3_131 = ROcp3_15*s.dpt[1,12]+ROcp3_46*s.dpt[2,12]
  RLcp3_231 = ROcp3_25*s.dpt[1,12]+ROcp3_56*s.dpt[2,12]
  RLcp3_331 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
  OMcp3_131 = OMcp3_16+qd[31]*ROcp3_15
  OMcp3_231 = OMcp3_26+qd[31]*ROcp3_25
  OMcp3_331 = OMcp3_36-qd[31]*S5
  ORcp3_131 = OMcp3_26*RLcp3_331-OMcp3_36*RLcp3_231
  ORcp3_231 = -(OMcp3_16*RLcp3_331-OMcp3_36*RLcp3_131)
  ORcp3_331 = OMcp3_16*RLcp3_231-OMcp3_26*RLcp3_131
  OMcp3_132 = OMcp3_131+qd[32]*ROcp3_731
  OMcp3_232 = OMcp3_231+qd[32]*ROcp3_831
  OMcp3_332 = OMcp3_331+qd[32]*ROcp3_931
  OPcp3_132 = OPcp3_16-qd[31]*(OMcp3_26*S5+OMcp3_36*ROcp3_25)+qd[32]*(OMcp3_231*ROcp3_931-OMcp3_331*ROcp3_831)+qdd[31]*\
   ROcp3_15+qdd[32]*ROcp3_731
  OPcp3_232 = OPcp3_26+qd[31]*(OMcp3_16*S5+OMcp3_36*ROcp3_15)-qd[32]*(OMcp3_131*ROcp3_931-OMcp3_331*ROcp3_731)+qdd[31]*\
   ROcp3_25+qdd[32]*ROcp3_831
  OPcp3_332 = OPcp3_36+qd[31]*(OMcp3_16*ROcp3_25-OMcp3_26*ROcp3_15)+qd[32]*(OMcp3_131*ROcp3_831-OMcp3_231*ROcp3_731)-\
   qdd[31]*S5+qdd[32]*ROcp3_931
  RLcp3_133 = ROcp3_432*s.dpt[2,30]
  RLcp3_233 = ROcp3_532*s.dpt[2,30]
  RLcp3_333 = ROcp3_632*s.dpt[2,30]
  OMcp3_133 = OMcp3_132+qd[33]*ROcp3_132
  OMcp3_233 = OMcp3_232+qd[33]*ROcp3_232
  OMcp3_333 = OMcp3_332+qd[33]*ROcp3_332
  ORcp3_133 = OMcp3_232*RLcp3_333-OMcp3_332*RLcp3_233
  ORcp3_233 = -(OMcp3_132*RLcp3_333-OMcp3_332*RLcp3_133)
  ORcp3_333 = OMcp3_132*RLcp3_233-OMcp3_232*RLcp3_133
  OMcp3_134 = OMcp3_133+qd[34]*ROcp3_733
  OMcp3_234 = OMcp3_233+qd[34]*ROcp3_833
  OMcp3_334 = OMcp3_333+qd[34]*ROcp3_933
  OPcp3_134 = OPcp3_132+qd[33]*(OMcp3_232*ROcp3_332-OMcp3_332*ROcp3_232)+qd[34]*(OMcp3_233*ROcp3_933-OMcp3_333*ROcp3_833\
   )+qdd[33]*ROcp3_132+qdd[34]*ROcp3_733
  OPcp3_234 = OPcp3_232-qd[33]*(OMcp3_132*ROcp3_332-OMcp3_332*ROcp3_132)-qd[34]*(OMcp3_133*ROcp3_933-OMcp3_333*ROcp3_733\
   )+qdd[33]*ROcp3_232+qdd[34]*ROcp3_833
  OPcp3_334 = OPcp3_332+qd[33]*(OMcp3_132*ROcp3_232-OMcp3_232*ROcp3_132)+qd[34]*(OMcp3_133*ROcp3_833-OMcp3_233*ROcp3_733\
   )+qdd[33]*ROcp3_332+qdd[34]*ROcp3_933

# = = Block_0_0_1_4_0_13 = = 
 
# Sensor Kinematics 


  ROcp3_437 = ROcp3_434*C37+ROcp3_733*S37
  ROcp3_537 = ROcp3_534*C37+ROcp3_833*S37
  ROcp3_637 = ROcp3_634*C37+ROcp3_933*S37
  ROcp3_737 = -(ROcp3_434*S37-ROcp3_733*C37)
  ROcp3_837 = -(ROcp3_534*S37-ROcp3_833*C37)
  ROcp3_937 = -(ROcp3_634*S37-ROcp3_933*C37)
  ROcp3_138 = ROcp3_134*C38-ROcp3_737*S38
  ROcp3_238 = ROcp3_234*C38-ROcp3_837*S38
  ROcp3_338 = ROcp3_334*C38-ROcp3_937*S38
  ROcp3_738 = ROcp3_134*S38+ROcp3_737*C38
  ROcp3_838 = ROcp3_234*S38+ROcp3_837*C38
  ROcp3_938 = ROcp3_334*S38+ROcp3_937*C38
  RLcp3_137 = ROcp3_733*s.dpt[3,34]
  RLcp3_237 = ROcp3_833*s.dpt[3,34]
  RLcp3_337 = ROcp3_933*s.dpt[3,34]
  OMcp3_137 = OMcp3_134+qd[37]*ROcp3_134
  OMcp3_237 = OMcp3_234+qd[37]*ROcp3_234
  OMcp3_337 = OMcp3_334+qd[37]*ROcp3_334
  ORcp3_137 = OMcp3_234*RLcp3_337-OMcp3_334*RLcp3_237
  ORcp3_237 = -(OMcp3_134*RLcp3_337-OMcp3_334*RLcp3_137)
  ORcp3_337 = OMcp3_134*RLcp3_237-OMcp3_234*RLcp3_137
  PxF4[1] = q[1]+RLcp3_131+RLcp3_133+RLcp3_137
  PxF4[2] = q[2]+RLcp3_231+RLcp3_233+RLcp3_237
  PxF4[3] = q[3]+RLcp3_331+RLcp3_333+RLcp3_337
  RxF4[1,1] = ROcp3_138
  RxF4[1,2] = ROcp3_238
  RxF4[1,3] = ROcp3_338
  RxF4[2,1] = ROcp3_437
  RxF4[2,2] = ROcp3_537
  RxF4[2,3] = ROcp3_637
  RxF4[3,1] = ROcp3_738
  RxF4[3,2] = ROcp3_838
  RxF4[3,3] = ROcp3_938
  VxF4[1] = qd[1]+ORcp3_131+ORcp3_133+ORcp3_137
  VxF4[2] = qd[2]+ORcp3_231+ORcp3_233+ORcp3_237
  VxF4[3] = qd[3]+ORcp3_331+ORcp3_333+ORcp3_337
  OMxF4[1] = OMcp3_137+qd[38]*ROcp3_437
  OMxF4[2] = OMcp3_237+qd[38]*ROcp3_537
  OMxF4[3] = OMcp3_337+qd[38]*ROcp3_637
  AxF4[1] = qdd[1]+OMcp3_232*ORcp3_333+OMcp3_234*ORcp3_337+OMcp3_26*ORcp3_331-OMcp3_332*ORcp3_233-OMcp3_334*ORcp3_237-\
   OMcp3_36*ORcp3_231+OPcp3_232*RLcp3_333+OPcp3_234*RLcp3_337+OPcp3_26*RLcp3_331-OPcp3_332*RLcp3_233-OPcp3_334*RLcp3_237-\
   OPcp3_36*RLcp3_231
  AxF4[2] = qdd[2]-OMcp3_132*ORcp3_333-OMcp3_134*ORcp3_337-OMcp3_16*ORcp3_331+OMcp3_332*ORcp3_133+OMcp3_334*ORcp3_137+\
   OMcp3_36*ORcp3_131-OPcp3_132*RLcp3_333-OPcp3_134*RLcp3_337-OPcp3_16*RLcp3_331+OPcp3_332*RLcp3_133+OPcp3_334*RLcp3_137+\
   OPcp3_36*RLcp3_131
  AxF4[3] = qdd[3]+OMcp3_132*ORcp3_233+OMcp3_134*ORcp3_237+OMcp3_16*ORcp3_231-OMcp3_232*ORcp3_133-OMcp3_234*ORcp3_137-\
   OMcp3_26*ORcp3_131+OPcp3_132*RLcp3_233+OPcp3_134*RLcp3_237+OPcp3_16*RLcp3_231-OPcp3_232*RLcp3_133-OPcp3_234*RLcp3_137-\
   OPcp3_26*RLcp3_131
  OMPxF4[1] = OPcp3_134+qd[37]*(OMcp3_234*ROcp3_334-OMcp3_334*ROcp3_234)+qd[38]*(OMcp3_237*ROcp3_637-OMcp3_337*ROcp3_537\
   )+qdd[37]*ROcp3_134+qdd[38]*ROcp3_437
  OMPxF4[2] = OPcp3_234-qd[37]*(OMcp3_134*ROcp3_334-OMcp3_334*ROcp3_134)-qd[38]*(OMcp3_137*ROcp3_637-OMcp3_337*ROcp3_437\
   )+qdd[37]*ROcp3_234+qdd[38]*ROcp3_537
  OMPxF4[3] = OPcp3_334+qd[37]*(OMcp3_134*ROcp3_234-OMcp3_234*ROcp3_134)+qd[38]*(OMcp3_137*ROcp3_537-OMcp3_237*ROcp3_437\
   )+qdd[37]*ROcp3_334+qdd[38]*ROcp3_637
 
# Sensor Forces Computation 

  SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc14 = ROcp3_138*SWr4[1]+ROcp3_238*SWr4[2]+ROcp3_338*SWr4[3]
  xfrc24 = ROcp3_437*SWr4[1]+ROcp3_537*SWr4[2]+ROcp3_637*SWr4[3]
  xfrc34 = ROcp3_738*SWr4[1]+ROcp3_838*SWr4[2]+ROcp3_938*SWr4[3]
  frc[1,38] = s.frc[1,38]+xfrc14
  frc[2,38] = s.frc[2,38]+xfrc24
  frc[3,38] = s.frc[3,38]+xfrc34
  xtrq14 = ROcp3_138*SWr4[4]+ROcp3_238*SWr4[5]+ROcp3_338*SWr4[6]
  xtrq24 = ROcp3_437*SWr4[4]+ROcp3_537*SWr4[5]+ROcp3_637*SWr4[6]
  xtrq34 = ROcp3_738*SWr4[4]+ROcp3_838*SWr4[5]+ROcp3_938*SWr4[6]
  trq[1,38] = s.trq[1,38]+xtrq14-xfrc24*SWr4[9]+xfrc34*SWr4[8]
  trq[2,38] = s.trq[2,38]+xtrq24+xfrc14*SWr4[9]-xfrc34*SWr4[7]
  trq[3,38] = s.trq[3,38]+xtrq34-xfrc14*SWr4[8]+xfrc24*SWr4[7]

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
  frc[1,26] = s.frc[1,26]
  frc[2,26] = s.frc[2,26]
  frc[3,26] = s.frc[3,26]
  frc[1,28] = s.frc[1,28]
  frc[2,28] = s.frc[2,28]
  frc[3,28] = s.frc[3,28]
  frc[1,32] = s.frc[1,32]
  frc[2,32] = s.frc[2,32]
  frc[3,32] = s.frc[3,32]
  frc[1,34] = s.frc[1,34]
  frc[2,34] = s.frc[2,34]
  frc[3,34] = s.frc[3,34]
  frc[1,36] = s.frc[1,36]
  frc[2,36] = s.frc[2,36]
  frc[3,36] = s.frc[3,36]
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
  trq[1,26] = s.trq[1,26]
  trq[2,26] = s.trq[2,26]
  trq[3,26] = s.trq[3,26]
  trq[1,28] = s.trq[1,28]
  trq[2,28] = s.trq[2,28]
  trq[3,28] = s.trq[3,28]
  trq[1,32] = s.trq[1,32]
  trq[2,32] = s.trq[2,32]
  trq[3,32] = s.trq[3,32]
  trq[1,34] = s.trq[1,34]
  trq[2,34] = s.trq[2,34]
  trq[3,34] = s.trq[3,34]
  trq[1,36] = s.trq[1,36]
  trq[2,36] = s.trq[2,36]
  trq[3,36] = s.trq[3,36]

# ====== END Task 0 ====== 

  

