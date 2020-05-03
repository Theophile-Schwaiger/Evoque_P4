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
#	==> Generation Date : Sat May  2 23:53:37 2020
#
#	==> Project name : Model_In_Wheel
#	==> using XML input file 
#
#	==> Number of joints : 65
#
#	==> Function : F19 : External Forces
#	==> Flops complexity : 2190
#
#	==> Generation Time :  0.040 seconds
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
  RLcp0_18 = ROcp0_47*s.dpt[2,16]
  RLcp0_28 = ROcp0_57*s.dpt[2,16]
  RLcp0_38 = ROcp0_67*s.dpt[2,16]
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
  RLcp0_113 = ROcp0_49*s.dpt[2,18]+ROcp0_710*s.dpt[3,18]
  RLcp0_213 = ROcp0_59*s.dpt[2,18]+ROcp0_810*s.dpt[3,18]
  RLcp0_313 = ROcp0_69*s.dpt[2,18]+ROcp0_910*s.dpt[3,18]
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
  RLcp1_116 = ROcp1_415*s.dpt[2,23]
  RLcp1_216 = ROcp1_515*s.dpt[2,23]
  RLcp1_316 = ROcp1_615*s.dpt[2,23]
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
  RLcp1_121 = ROcp1_417*s.dpt[2,25]+ROcp1_718*s.dpt[3,25]
  RLcp1_221 = ROcp1_517*s.dpt[2,25]+ROcp1_818*s.dpt[3,25]
  RLcp1_321 = ROcp1_617*s.dpt[2,25]+ROcp1_918*s.dpt[3,25]
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

# = = Block_0_0_1_3_0_11 = = 
 
# Trigonometric Variables  

  S29p6 = C29*S6+S29*C6
  C29p6 = C29*C6-S29*S6
 
# Sensor Kinematics 


  ROcp2_429 = ROcp2_46*C29+ROcp2_76*S29
  ROcp2_529 = ROcp2_56*C29+ROcp2_86*S29
  ROcp2_629 = S29p6*C5
  ROcp2_729 = -(ROcp2_46*S29-ROcp2_76*C29)
  ROcp2_829 = -(ROcp2_56*S29-ROcp2_86*C29)
  ROcp2_929 = C29p6*C5
  ROcp2_130 = ROcp2_15*C30+ROcp2_429*S30
  ROcp2_230 = ROcp2_25*C30+ROcp2_529*S30
  ROcp2_330 = ROcp2_629*S30-C30*S5
  ROcp2_430 = -(ROcp2_15*S30-ROcp2_429*C30)
  ROcp2_530 = -(ROcp2_25*S30-ROcp2_529*C30)
  ROcp2_630 = ROcp2_629*C30+S30*S5
  ROcp2_431 = ROcp2_430*C31+ROcp2_729*S31
  ROcp2_531 = ROcp2_530*C31+ROcp2_829*S31
  ROcp2_631 = ROcp2_630*C31+ROcp2_929*S31
  ROcp2_731 = -(ROcp2_430*S31-ROcp2_729*C31)
  ROcp2_831 = -(ROcp2_530*S31-ROcp2_829*C31)
  ROcp2_931 = -(ROcp2_630*S31-ROcp2_929*C31)
  ROcp2_132 = ROcp2_130*C32-ROcp2_731*S32
  ROcp2_232 = ROcp2_230*C32-ROcp2_831*S32
  ROcp2_332 = ROcp2_330*C32-ROcp2_931*S32
  ROcp2_732 = ROcp2_130*S32+ROcp2_731*C32
  ROcp2_832 = ROcp2_230*S32+ROcp2_831*C32
  ROcp2_932 = ROcp2_330*S32+ROcp2_931*C32
  ROcp2_133 = ROcp2_132*C33+ROcp2_431*S33
  ROcp2_233 = ROcp2_232*C33+ROcp2_531*S33
  ROcp2_333 = ROcp2_332*C33+ROcp2_631*S33
  ROcp2_433 = -(ROcp2_132*S33-ROcp2_431*C33)
  ROcp2_533 = -(ROcp2_232*S33-ROcp2_531*C33)
  ROcp2_633 = -(ROcp2_332*S33-ROcp2_631*C33)
  RLcp2_129 = ROcp2_15*s.dpt[1,10]+ROcp2_46*s.dpt[2,10]
  RLcp2_229 = ROcp2_25*s.dpt[1,10]+ROcp2_56*s.dpt[2,10]
  RLcp2_329 = C5*S6*s.dpt[2,10]-s.dpt[1,10]*S5
  OMcp2_129 = OMcp2_16+qd[29]*ROcp2_15
  OMcp2_229 = OMcp2_26+qd[29]*ROcp2_25
  OMcp2_329 = OMcp2_36-qd[29]*S5
  ORcp2_129 = OMcp2_26*RLcp2_329-OMcp2_36*RLcp2_229
  ORcp2_229 = -(OMcp2_16*RLcp2_329-OMcp2_36*RLcp2_129)
  ORcp2_329 = OMcp2_16*RLcp2_229-OMcp2_26*RLcp2_129
  OMcp2_130 = OMcp2_129+qd[30]*ROcp2_729
  OMcp2_230 = OMcp2_229+qd[30]*ROcp2_829
  OMcp2_330 = OMcp2_329+qd[30]*ROcp2_929
  OPcp2_130 = OPcp2_16-qd[29]*(OMcp2_26*S5+OMcp2_36*ROcp2_25)+qd[30]*(OMcp2_229*ROcp2_929-OMcp2_329*ROcp2_829)+qdd[29]*\
   ROcp2_15+qdd[30]*ROcp2_729
  OPcp2_230 = OPcp2_26+qd[29]*(OMcp2_16*S5+OMcp2_36*ROcp2_15)-qd[30]*(OMcp2_129*ROcp2_929-OMcp2_329*ROcp2_729)+qdd[29]*\
   ROcp2_25+qdd[30]*ROcp2_829
  OPcp2_330 = OPcp2_36+qd[29]*(OMcp2_16*ROcp2_25-OMcp2_26*ROcp2_15)+qd[30]*(OMcp2_129*ROcp2_829-OMcp2_229*ROcp2_729)-\
   qdd[29]*S5+qdd[30]*ROcp2_929
  RLcp2_131 = ROcp2_430*s.dpt[2,33]
  RLcp2_231 = ROcp2_530*s.dpt[2,33]
  RLcp2_331 = ROcp2_630*s.dpt[2,33]
  OMcp2_131 = OMcp2_130+qd[31]*ROcp2_130
  OMcp2_231 = OMcp2_230+qd[31]*ROcp2_230
  OMcp2_331 = OMcp2_330+qd[31]*ROcp2_330
  ORcp2_131 = OMcp2_230*RLcp2_331-OMcp2_330*RLcp2_231
  ORcp2_231 = -(OMcp2_130*RLcp2_331-OMcp2_330*RLcp2_131)
  ORcp2_331 = OMcp2_130*RLcp2_231-OMcp2_230*RLcp2_131
  OMcp2_132 = OMcp2_131+qd[32]*ROcp2_431
  OMcp2_232 = OMcp2_231+qd[32]*ROcp2_531
  OMcp2_332 = OMcp2_331+qd[32]*ROcp2_631
  OMcp2_133 = OMcp2_132+qd[33]*ROcp2_732
  OMcp2_233 = OMcp2_232+qd[33]*ROcp2_832
  OMcp2_333 = OMcp2_332+qd[33]*ROcp2_932
  OPcp2_133 = OPcp2_130+qd[31]*(OMcp2_230*ROcp2_330-OMcp2_330*ROcp2_230)+qd[32]*(OMcp2_231*ROcp2_631-OMcp2_331*ROcp2_531\
   )+qd[33]*(OMcp2_232*ROcp2_932-OMcp2_332*ROcp2_832)+qdd[31]*ROcp2_130+qdd[32]*ROcp2_431+qdd[33]*ROcp2_732
  OPcp2_233 = OPcp2_230-qd[31]*(OMcp2_130*ROcp2_330-OMcp2_330*ROcp2_130)-qd[32]*(OMcp2_131*ROcp2_631-OMcp2_331*ROcp2_431\
   )-qd[33]*(OMcp2_132*ROcp2_932-OMcp2_332*ROcp2_732)+qdd[31]*ROcp2_230+qdd[32]*ROcp2_531+qdd[33]*ROcp2_832
  OPcp2_333 = OPcp2_330+qd[31]*(OMcp2_130*ROcp2_230-OMcp2_230*ROcp2_130)+qd[32]*(OMcp2_131*ROcp2_531-OMcp2_231*ROcp2_431\
   )+qd[33]*(OMcp2_132*ROcp2_832-OMcp2_232*ROcp2_732)+qdd[31]*ROcp2_330+qdd[32]*ROcp2_631+qdd[33]*ROcp2_932

# = = Block_0_0_1_3_0_13 = = 
 
# Sensor Kinematics 


  ROcp2_436 = ROcp2_433*C36+ROcp2_732*S36
  ROcp2_536 = ROcp2_533*C36+ROcp2_832*S36
  ROcp2_636 = ROcp2_633*C36+ROcp2_932*S36
  ROcp2_736 = -(ROcp2_433*S36-ROcp2_732*C36)
  ROcp2_836 = -(ROcp2_533*S36-ROcp2_832*C36)
  ROcp2_936 = -(ROcp2_633*S36-ROcp2_932*C36)
  ROcp2_137 = ROcp2_133*C37-ROcp2_736*S37
  ROcp2_237 = ROcp2_233*C37-ROcp2_836*S37
  ROcp2_337 = ROcp2_333*C37-ROcp2_936*S37
  ROcp2_737 = ROcp2_133*S37+ROcp2_736*C37
  ROcp2_837 = ROcp2_233*S37+ROcp2_836*C37
  ROcp2_937 = ROcp2_333*S37+ROcp2_936*C37
  RLcp2_136 = ROcp2_433*s.dpt[2,35]+ROcp2_732*s.dpt[3,35]
  RLcp2_236 = ROcp2_533*s.dpt[2,35]+ROcp2_832*s.dpt[3,35]
  RLcp2_336 = ROcp2_633*s.dpt[2,35]+ROcp2_932*s.dpt[3,35]
  OMcp2_136 = OMcp2_133+qd[36]*ROcp2_133
  OMcp2_236 = OMcp2_233+qd[36]*ROcp2_233
  OMcp2_336 = OMcp2_333+qd[36]*ROcp2_333
  ORcp2_136 = OMcp2_233*RLcp2_336-OMcp2_333*RLcp2_236
  ORcp2_236 = -(OMcp2_133*RLcp2_336-OMcp2_333*RLcp2_136)
  ORcp2_336 = OMcp2_133*RLcp2_236-OMcp2_233*RLcp2_136
  PxF3[1] = q[1]+RLcp2_129+RLcp2_131+RLcp2_136
  PxF3[2] = q[2]+RLcp2_229+RLcp2_231+RLcp2_236
  PxF3[3] = q[3]+RLcp2_329+RLcp2_331+RLcp2_336
  RxF3[1,1] = ROcp2_137
  RxF3[1,2] = ROcp2_237
  RxF3[1,3] = ROcp2_337
  RxF3[2,1] = ROcp2_436
  RxF3[2,2] = ROcp2_536
  RxF3[2,3] = ROcp2_636
  RxF3[3,1] = ROcp2_737
  RxF3[3,2] = ROcp2_837
  RxF3[3,3] = ROcp2_937
  VxF3[1] = qd[1]+ORcp2_129+ORcp2_131+ORcp2_136
  VxF3[2] = qd[2]+ORcp2_229+ORcp2_231+ORcp2_236
  VxF3[3] = qd[3]+ORcp2_329+ORcp2_331+ORcp2_336
  OMxF3[1] = OMcp2_136+qd[37]*ROcp2_436
  OMxF3[2] = OMcp2_236+qd[37]*ROcp2_536
  OMxF3[3] = OMcp2_336+qd[37]*ROcp2_636
  AxF3[1] = qdd[1]+OMcp2_230*ORcp2_331+OMcp2_233*ORcp2_336+OMcp2_26*ORcp2_329-OMcp2_330*ORcp2_231-OMcp2_333*ORcp2_236-\
   OMcp2_36*ORcp2_229+OPcp2_230*RLcp2_331+OPcp2_233*RLcp2_336+OPcp2_26*RLcp2_329-OPcp2_330*RLcp2_231-OPcp2_333*RLcp2_236-\
   OPcp2_36*RLcp2_229
  AxF3[2] = qdd[2]-OMcp2_130*ORcp2_331-OMcp2_133*ORcp2_336-OMcp2_16*ORcp2_329+OMcp2_330*ORcp2_131+OMcp2_333*ORcp2_136+\
   OMcp2_36*ORcp2_129-OPcp2_130*RLcp2_331-OPcp2_133*RLcp2_336-OPcp2_16*RLcp2_329+OPcp2_330*RLcp2_131+OPcp2_333*RLcp2_136+\
   OPcp2_36*RLcp2_129
  AxF3[3] = qdd[3]+OMcp2_130*ORcp2_231+OMcp2_133*ORcp2_236+OMcp2_16*ORcp2_229-OMcp2_230*ORcp2_131-OMcp2_233*ORcp2_136-\
   OMcp2_26*ORcp2_129+OPcp2_130*RLcp2_231+OPcp2_133*RLcp2_236+OPcp2_16*RLcp2_229-OPcp2_230*RLcp2_131-OPcp2_233*RLcp2_136-\
   OPcp2_26*RLcp2_129
  OMPxF3[1] = OPcp2_133+qd[36]*(OMcp2_233*ROcp2_333-OMcp2_333*ROcp2_233)+qd[37]*(OMcp2_236*ROcp2_636-OMcp2_336*ROcp2_536\
   )+qdd[36]*ROcp2_133+qdd[37]*ROcp2_436
  OMPxF3[2] = OPcp2_233-qd[36]*(OMcp2_133*ROcp2_333-OMcp2_333*ROcp2_133)-qd[37]*(OMcp2_136*ROcp2_636-OMcp2_336*ROcp2_436\
   )+qdd[36]*ROcp2_233+qdd[37]*ROcp2_536
  OMPxF3[3] = OPcp2_333+qd[36]*(OMcp2_133*ROcp2_233-OMcp2_233*ROcp2_133)+qd[37]*(OMcp2_136*ROcp2_536-OMcp2_236*ROcp2_436\
   )+qdd[36]*ROcp2_333+qdd[37]*ROcp2_636
 
# Sensor Forces Computation 

  SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc13 = ROcp2_137*SWr3[1]+ROcp2_237*SWr3[2]+ROcp2_337*SWr3[3]
  xfrc23 = ROcp2_436*SWr3[1]+ROcp2_536*SWr3[2]+ROcp2_636*SWr3[3]
  xfrc33 = ROcp2_737*SWr3[1]+ROcp2_837*SWr3[2]+ROcp2_937*SWr3[3]
  frc[1,37] = s.frc[1,37]+xfrc13
  frc[2,37] = s.frc[2,37]+xfrc23
  frc[3,37] = s.frc[3,37]+xfrc33
  xtrq13 = ROcp2_137*SWr3[4]+ROcp2_237*SWr3[5]+ROcp2_337*SWr3[6]
  xtrq23 = ROcp2_436*SWr3[4]+ROcp2_536*SWr3[5]+ROcp2_636*SWr3[6]
  xtrq33 = ROcp2_737*SWr3[4]+ROcp2_837*SWr3[5]+ROcp2_937*SWr3[6]
  trq[1,37] = s.trq[1,37]+xtrq13-xfrc23*SWr3[9]+xfrc33*SWr3[8]
  trq[2,37] = s.trq[2,37]+xtrq23+xfrc13*SWr3[9]-xfrc33*SWr3[7]
  trq[3,37] = s.trq[3,37]+xtrq33-xfrc13*SWr3[8]+xfrc23*SWr3[7]

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

# = = Block_0_0_1_4_0_15 = = 
 
# Trigonometric Variables  

  S40p6 = C40*S6+S40*C6
  C40p6 = C40*C6-S40*S6
 
# Sensor Kinematics 


  ROcp3_440 = ROcp3_46*C40+ROcp3_76*S40
  ROcp3_540 = ROcp3_56*C40+ROcp3_86*S40
  ROcp3_640 = S40p6*C5
  ROcp3_740 = -(ROcp3_46*S40-ROcp3_76*C40)
  ROcp3_840 = -(ROcp3_56*S40-ROcp3_86*C40)
  ROcp3_940 = C40p6*C5
  ROcp3_141 = ROcp3_15*C41+ROcp3_440*S41
  ROcp3_241 = ROcp3_25*C41+ROcp3_540*S41
  ROcp3_341 = ROcp3_640*S41-C41*S5
  ROcp3_441 = -(ROcp3_15*S41-ROcp3_440*C41)
  ROcp3_541 = -(ROcp3_25*S41-ROcp3_540*C41)
  ROcp3_641 = ROcp3_640*C41+S41*S5
  ROcp3_442 = ROcp3_441*C42+ROcp3_740*S42
  ROcp3_542 = ROcp3_541*C42+ROcp3_840*S42
  ROcp3_642 = ROcp3_641*C42+ROcp3_940*S42
  ROcp3_742 = -(ROcp3_441*S42-ROcp3_740*C42)
  ROcp3_842 = -(ROcp3_541*S42-ROcp3_840*C42)
  ROcp3_942 = -(ROcp3_641*S42-ROcp3_940*C42)
  ROcp3_143 = ROcp3_141*C43-ROcp3_742*S43
  ROcp3_243 = ROcp3_241*C43-ROcp3_842*S43
  ROcp3_343 = ROcp3_341*C43-ROcp3_942*S43
  ROcp3_743 = ROcp3_141*S43+ROcp3_742*C43
  ROcp3_843 = ROcp3_241*S43+ROcp3_842*C43
  ROcp3_943 = ROcp3_341*S43+ROcp3_942*C43
  ROcp3_144 = ROcp3_143*C44+ROcp3_442*S44
  ROcp3_244 = ROcp3_243*C44+ROcp3_542*S44
  ROcp3_344 = ROcp3_343*C44+ROcp3_642*S44
  ROcp3_444 = -(ROcp3_143*S44-ROcp3_442*C44)
  ROcp3_544 = -(ROcp3_243*S44-ROcp3_542*C44)
  ROcp3_644 = -(ROcp3_343*S44-ROcp3_642*C44)
  RLcp3_140 = ROcp3_15*s.dpt[1,12]+ROcp3_46*s.dpt[2,12]
  RLcp3_240 = ROcp3_25*s.dpt[1,12]+ROcp3_56*s.dpt[2,12]
  RLcp3_340 = C5*S6*s.dpt[2,12]-s.dpt[1,12]*S5
  OMcp3_140 = OMcp3_16+qd[40]*ROcp3_15
  OMcp3_240 = OMcp3_26+qd[40]*ROcp3_25
  OMcp3_340 = OMcp3_36-qd[40]*S5
  ORcp3_140 = OMcp3_26*RLcp3_340-OMcp3_36*RLcp3_240
  ORcp3_240 = -(OMcp3_16*RLcp3_340-OMcp3_36*RLcp3_140)
  ORcp3_340 = OMcp3_16*RLcp3_240-OMcp3_26*RLcp3_140
  OMcp3_141 = OMcp3_140+qd[41]*ROcp3_740
  OMcp3_241 = OMcp3_240+qd[41]*ROcp3_840
  OMcp3_341 = OMcp3_340+qd[41]*ROcp3_940
  OPcp3_141 = OPcp3_16-qd[40]*(OMcp3_26*S5+OMcp3_36*ROcp3_25)+qd[41]*(OMcp3_240*ROcp3_940-OMcp3_340*ROcp3_840)+qdd[40]*\
   ROcp3_15+qdd[41]*ROcp3_740
  OPcp3_241 = OPcp3_26+qd[40]*(OMcp3_16*S5+OMcp3_36*ROcp3_15)-qd[41]*(OMcp3_140*ROcp3_940-OMcp3_340*ROcp3_740)+qdd[40]*\
   ROcp3_25+qdd[41]*ROcp3_840
  OPcp3_341 = OPcp3_36+qd[40]*(OMcp3_16*ROcp3_25-OMcp3_26*ROcp3_15)+qd[41]*(OMcp3_140*ROcp3_840-OMcp3_240*ROcp3_740)-\
   qdd[40]*S5+qdd[41]*ROcp3_940
  RLcp3_142 = ROcp3_441*s.dpt[2,42]
  RLcp3_242 = ROcp3_541*s.dpt[2,42]
  RLcp3_342 = ROcp3_641*s.dpt[2,42]
  OMcp3_142 = OMcp3_141+qd[42]*ROcp3_141
  OMcp3_242 = OMcp3_241+qd[42]*ROcp3_241
  OMcp3_342 = OMcp3_341+qd[42]*ROcp3_341
  ORcp3_142 = OMcp3_241*RLcp3_342-OMcp3_341*RLcp3_242
  ORcp3_242 = -(OMcp3_141*RLcp3_342-OMcp3_341*RLcp3_142)
  ORcp3_342 = OMcp3_141*RLcp3_242-OMcp3_241*RLcp3_142
  OMcp3_143 = OMcp3_142+qd[43]*ROcp3_442
  OMcp3_243 = OMcp3_242+qd[43]*ROcp3_542
  OMcp3_343 = OMcp3_342+qd[43]*ROcp3_642
  OMcp3_144 = OMcp3_143+qd[44]*ROcp3_743
  OMcp3_244 = OMcp3_243+qd[44]*ROcp3_843
  OMcp3_344 = OMcp3_343+qd[44]*ROcp3_943
  OPcp3_144 = OPcp3_141+qd[42]*(OMcp3_241*ROcp3_341-OMcp3_341*ROcp3_241)+qd[43]*(OMcp3_242*ROcp3_642-OMcp3_342*ROcp3_542\
   )+qd[44]*(OMcp3_243*ROcp3_943-OMcp3_343*ROcp3_843)+qdd[42]*ROcp3_141+qdd[43]*ROcp3_442+qdd[44]*ROcp3_743
  OPcp3_244 = OPcp3_241-qd[42]*(OMcp3_141*ROcp3_341-OMcp3_341*ROcp3_141)-qd[43]*(OMcp3_142*ROcp3_642-OMcp3_342*ROcp3_442\
   )-qd[44]*(OMcp3_143*ROcp3_943-OMcp3_343*ROcp3_743)+qdd[42]*ROcp3_241+qdd[43]*ROcp3_542+qdd[44]*ROcp3_843
  OPcp3_344 = OPcp3_341+qd[42]*(OMcp3_141*ROcp3_241-OMcp3_241*ROcp3_141)+qd[43]*(OMcp3_142*ROcp3_542-OMcp3_242*ROcp3_442\
   )+qd[44]*(OMcp3_143*ROcp3_843-OMcp3_243*ROcp3_743)+qdd[42]*ROcp3_341+qdd[43]*ROcp3_642+qdd[44]*ROcp3_943

# = = Block_0_0_1_4_0_17 = = 
 
# Sensor Kinematics 


  ROcp3_447 = ROcp3_444*C47+ROcp3_743*S47
  ROcp3_547 = ROcp3_544*C47+ROcp3_843*S47
  ROcp3_647 = ROcp3_644*C47+ROcp3_943*S47
  ROcp3_747 = -(ROcp3_444*S47-ROcp3_743*C47)
  ROcp3_847 = -(ROcp3_544*S47-ROcp3_843*C47)
  ROcp3_947 = -(ROcp3_644*S47-ROcp3_943*C47)
  ROcp3_148 = ROcp3_144*C48-ROcp3_747*S48
  ROcp3_248 = ROcp3_244*C48-ROcp3_847*S48
  ROcp3_348 = ROcp3_344*C48-ROcp3_947*S48
  ROcp3_748 = ROcp3_144*S48+ROcp3_747*C48
  ROcp3_848 = ROcp3_244*S48+ROcp3_847*C48
  ROcp3_948 = ROcp3_344*S48+ROcp3_947*C48
  RLcp3_147 = ROcp3_444*s.dpt[2,46]+ROcp3_743*s.dpt[3,46]
  RLcp3_247 = ROcp3_544*s.dpt[2,46]+ROcp3_843*s.dpt[3,46]
  RLcp3_347 = ROcp3_644*s.dpt[2,46]+ROcp3_943*s.dpt[3,46]
  OMcp3_147 = OMcp3_144+qd[47]*ROcp3_144
  OMcp3_247 = OMcp3_244+qd[47]*ROcp3_244
  OMcp3_347 = OMcp3_344+qd[47]*ROcp3_344
  ORcp3_147 = OMcp3_244*RLcp3_347-OMcp3_344*RLcp3_247
  ORcp3_247 = -(OMcp3_144*RLcp3_347-OMcp3_344*RLcp3_147)
  ORcp3_347 = OMcp3_144*RLcp3_247-OMcp3_244*RLcp3_147
  PxF4[1] = q[1]+RLcp3_140+RLcp3_142+RLcp3_147
  PxF4[2] = q[2]+RLcp3_240+RLcp3_242+RLcp3_247
  PxF4[3] = q[3]+RLcp3_340+RLcp3_342+RLcp3_347
  RxF4[1,1] = ROcp3_148
  RxF4[1,2] = ROcp3_248
  RxF4[1,3] = ROcp3_348
  RxF4[2,1] = ROcp3_447
  RxF4[2,2] = ROcp3_547
  RxF4[2,3] = ROcp3_647
  RxF4[3,1] = ROcp3_748
  RxF4[3,2] = ROcp3_848
  RxF4[3,3] = ROcp3_948
  VxF4[1] = qd[1]+ORcp3_140+ORcp3_142+ORcp3_147
  VxF4[2] = qd[2]+ORcp3_240+ORcp3_242+ORcp3_247
  VxF4[3] = qd[3]+ORcp3_340+ORcp3_342+ORcp3_347
  OMxF4[1] = OMcp3_147+qd[48]*ROcp3_447
  OMxF4[2] = OMcp3_247+qd[48]*ROcp3_547
  OMxF4[3] = OMcp3_347+qd[48]*ROcp3_647
  AxF4[1] = qdd[1]+OMcp3_241*ORcp3_342+OMcp3_244*ORcp3_347+OMcp3_26*ORcp3_340-OMcp3_341*ORcp3_242-OMcp3_344*ORcp3_247-\
   OMcp3_36*ORcp3_240+OPcp3_241*RLcp3_342+OPcp3_244*RLcp3_347+OPcp3_26*RLcp3_340-OPcp3_341*RLcp3_242-OPcp3_344*RLcp3_247-\
   OPcp3_36*RLcp3_240
  AxF4[2] = qdd[2]-OMcp3_141*ORcp3_342-OMcp3_144*ORcp3_347-OMcp3_16*ORcp3_340+OMcp3_341*ORcp3_142+OMcp3_344*ORcp3_147+\
   OMcp3_36*ORcp3_140-OPcp3_141*RLcp3_342-OPcp3_144*RLcp3_347-OPcp3_16*RLcp3_340+OPcp3_341*RLcp3_142+OPcp3_344*RLcp3_147+\
   OPcp3_36*RLcp3_140
  AxF4[3] = qdd[3]+OMcp3_141*ORcp3_242+OMcp3_144*ORcp3_247+OMcp3_16*ORcp3_240-OMcp3_241*ORcp3_142-OMcp3_244*ORcp3_147-\
   OMcp3_26*ORcp3_140+OPcp3_141*RLcp3_242+OPcp3_144*RLcp3_247+OPcp3_16*RLcp3_240-OPcp3_241*RLcp3_142-OPcp3_244*RLcp3_147-\
   OPcp3_26*RLcp3_140
  OMPxF4[1] = OPcp3_144+qd[47]*(OMcp3_244*ROcp3_344-OMcp3_344*ROcp3_244)+qd[48]*(OMcp3_247*ROcp3_647-OMcp3_347*ROcp3_547\
   )+qdd[47]*ROcp3_144+qdd[48]*ROcp3_447
  OMPxF4[2] = OPcp3_244-qd[47]*(OMcp3_144*ROcp3_344-OMcp3_344*ROcp3_144)-qd[48]*(OMcp3_147*ROcp3_647-OMcp3_347*ROcp3_447\
   )+qdd[47]*ROcp3_244+qdd[48]*ROcp3_547
  OMPxF4[3] = OPcp3_344+qd[47]*(OMcp3_144*ROcp3_244-OMcp3_244*ROcp3_144)+qd[48]*(OMcp3_147*ROcp3_547-OMcp3_247*ROcp3_447\
   )+qdd[47]*ROcp3_344+qdd[48]*ROcp3_647
 
# Sensor Forces Computation 

  SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
 
# Sensor Dynamics : Forces projection on body-fixed frames 

  xfrc14 = ROcp3_148*SWr4[1]+ROcp3_248*SWr4[2]+ROcp3_348*SWr4[3]
  xfrc24 = ROcp3_447*SWr4[1]+ROcp3_547*SWr4[2]+ROcp3_647*SWr4[3]
  xfrc34 = ROcp3_748*SWr4[1]+ROcp3_848*SWr4[2]+ROcp3_948*SWr4[3]
  frc[1,48] = s.frc[1,48]+xfrc14
  frc[2,48] = s.frc[2,48]+xfrc24
  frc[3,48] = s.frc[3,48]+xfrc34
  xtrq14 = ROcp3_148*SWr4[4]+ROcp3_248*SWr4[5]+ROcp3_348*SWr4[6]
  xtrq24 = ROcp3_447*SWr4[4]+ROcp3_547*SWr4[5]+ROcp3_647*SWr4[6]
  xtrq34 = ROcp3_748*SWr4[4]+ROcp3_848*SWr4[5]+ROcp3_948*SWr4[6]
  trq[1,48] = s.trq[1,48]+xtrq14-xfrc24*SWr4[9]+xfrc34*SWr4[8]
  trq[2,48] = s.trq[2,48]+xtrq24+xfrc14*SWr4[9]-xfrc34*SWr4[7]
  trq[3,48] = s.trq[3,48]+xtrq34-xfrc14*SWr4[8]+xfrc24*SWr4[7]

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

# ====== END Task 0 ====== 

  

