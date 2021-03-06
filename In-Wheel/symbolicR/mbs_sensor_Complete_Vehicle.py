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
#	==> Generation Date : Sun Mar 29 20:34:02 2020
#
#	==> Project name : Complete_Vehicle
#	==> using XML input file 
#
#	==> Number of joints : 38
#
#	==> Function : F 6 : Sensors Kinematical Informations (sens) 
#	==> Flops complexity : 1868
#
#	==> Generation Time :  0.030 seconds
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

# = = Block_0_0_0_1_0_2 = = 
 
# Trigonometric Variables  

  S6p7 = C6*S7+S6*C7
  C6p7 = C6*C7-S6*S7

# = = Block_0_0_0_2_0_5 = = 
 
# Trigonometric Variables  

  S15p6 = C15*S6+S15*C6
  C15p6 = C15*C6-S15*S6

# = = Block_0_0_0_3_0_8 = = 
 
# Trigonometric Variables  

  S23p6 = C23*S6+S23*C6
  C23p6 = C23*C6-S23*S6

# = = Block_0_0_0_4_0_11 = = 
 
# Trigonometric Variables  

  S31p6 = C31*S6+S31*C6
  C31p6 = C31*C6-S31*S6

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
    ROcp0_76 = ROcp0_75*C6+S4*S6
    ROcp0_86 = ROcp0_85*C6-C4*S6
    OMcp0_15 = -qd[5]*S4
    OMcp0_25 = qd[5]*C4
    OMcp0_16 = OMcp0_15+ROcp0_15*qd[6]
    OMcp0_26 = OMcp0_25+ROcp0_25*qd[6]
    OMcp0_36 = qd[4]-qd[6]*S5
    OPcp0_16 = ROcp0_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp0_25*S5+ROcp0_25*qd[4])
    OPcp0_26 = ROcp0_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp0_15*S5+ROcp0_15*qd[4])
    OPcp0_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_1_0_2 = = 
 
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
    OMcp0_17 = OMcp0_16+ROcp0_15*qd[7]
    OMcp0_27 = OMcp0_26+ROcp0_25*qd[7]
    OMcp0_37 = OMcp0_36-qd[7]*S5
    ORcp0_17 = OMcp0_26*RLcp0_37-OMcp0_36*RLcp0_27
    ORcp0_27 = -(OMcp0_16*RLcp0_37-OMcp0_36*RLcp0_17)
    ORcp0_37 = OMcp0_16*RLcp0_27-OMcp0_26*RLcp0_17
    OPcp0_17 = OPcp0_16+ROcp0_15*qdd[7]-qd[7]*(OMcp0_26*S5+OMcp0_36*ROcp0_25)
    OPcp0_27 = OPcp0_26+ROcp0_25*qdd[7]+qd[7]*(OMcp0_16*S5+OMcp0_36*ROcp0_15)
    OPcp0_37 = OPcp0_36-qdd[7]*S5+qd[7]*(OMcp0_16*ROcp0_25-OMcp0_26*ROcp0_15)
    RLcp0_18 = ROcp0_47*s.dpt[2,13]
    RLcp0_28 = ROcp0_57*s.dpt[2,13]
    RLcp0_38 = ROcp0_67*s.dpt[2,13]
    POcp0_18 = RLcp0_17+RLcp0_18+q[1]
    POcp0_28 = RLcp0_27+RLcp0_28+q[2]
    POcp0_38 = RLcp0_37+RLcp0_38+q[3]
    OMcp0_18 = OMcp0_17+ROcp0_77*qd[8]
    OMcp0_28 = OMcp0_27+ROcp0_87*qd[8]
    OMcp0_38 = OMcp0_37+ROcp0_97*qd[8]
    ORcp0_18 = OMcp0_27*RLcp0_38-OMcp0_37*RLcp0_28
    ORcp0_28 = -(OMcp0_17*RLcp0_38-OMcp0_37*RLcp0_18)
    ORcp0_38 = OMcp0_17*RLcp0_28-OMcp0_27*RLcp0_18
    VIcp0_18 = ORcp0_17+ORcp0_18+qd[1]
    VIcp0_28 = ORcp0_27+ORcp0_28+qd[2]
    VIcp0_38 = ORcp0_37+ORcp0_38+qd[3]
    ACcp0_18 = qdd[1]+OMcp0_26*ORcp0_37+OMcp0_27*ORcp0_38-OMcp0_36*ORcp0_27-OMcp0_37*ORcp0_28+OPcp0_26*RLcp0_37+OPcp0_27*\
   RLcp0_38-OPcp0_36*RLcp0_27-OPcp0_37*RLcp0_28
    ACcp0_28 = qdd[2]-OMcp0_16*ORcp0_37-OMcp0_17*ORcp0_38+OMcp0_36*ORcp0_17+OMcp0_37*ORcp0_18-OPcp0_16*RLcp0_37-OPcp0_17*\
   RLcp0_38+OPcp0_36*RLcp0_17+OPcp0_37*RLcp0_18
    ACcp0_38 = qdd[3]+OMcp0_16*ORcp0_27+OMcp0_17*ORcp0_28-OMcp0_26*ORcp0_17-OMcp0_27*ORcp0_18+OPcp0_16*RLcp0_27+OPcp0_17*\
   RLcp0_28-OPcp0_26*RLcp0_17-OPcp0_27*RLcp0_18
    OMcp0_19 = OMcp0_18+ROcp0_18*qd[9]
    OMcp0_29 = OMcp0_28+ROcp0_28*qd[9]
    OMcp0_39 = OMcp0_38+ROcp0_38*qd[9]
    OMcp0_110 = OMcp0_19+ROcp0_49*qd[10]
    OMcp0_210 = OMcp0_29+ROcp0_59*qd[10]
    OMcp0_310 = OMcp0_39+ROcp0_69*qd[10]

# = = Block_1_0_0_1_0_4 = = 
 
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
    OMcp0_113 = OMcp0_110+ROcp0_110*qd[13]
    OMcp0_213 = OMcp0_210+ROcp0_210*qd[13]
    OMcp0_313 = OMcp0_310+ROcp0_310*qd[13]
    OMcp0_114 = OMcp0_113+ROcp0_413*qd[14]
    OMcp0_214 = OMcp0_213+ROcp0_513*qd[14]
    OMcp0_314 = OMcp0_313+ROcp0_613*qd[14]
    OPcp0_114 = OPcp0_17+ROcp0_110*qdd[13]+ROcp0_18*qdd[9]+ROcp0_413*qdd[14]+ROcp0_49*qdd[10]+ROcp0_77*qdd[8]+qd[10]*(\
   OMcp0_29*ROcp0_69-OMcp0_39*ROcp0_59)+qd[13]*(OMcp0_210*ROcp0_310-OMcp0_310*ROcp0_210)+qd[14]*(OMcp0_213*ROcp0_613-OMcp0_313*\
   ROcp0_513)+qd[8]*(OMcp0_27*ROcp0_97-OMcp0_37*ROcp0_87)+qd[9]*(OMcp0_28*ROcp0_38-OMcp0_38*ROcp0_28)
    OPcp0_214 = OPcp0_27+ROcp0_210*qdd[13]+ROcp0_28*qdd[9]+ROcp0_513*qdd[14]+ROcp0_59*qdd[10]+ROcp0_87*qdd[8]-qd[10]*(\
   OMcp0_19*ROcp0_69-OMcp0_39*ROcp0_49)-qd[13]*(OMcp0_110*ROcp0_310-OMcp0_310*ROcp0_110)-qd[14]*(OMcp0_113*ROcp0_613-OMcp0_313*\
   ROcp0_413)-qd[8]*(OMcp0_17*ROcp0_97-OMcp0_37*ROcp0_77)-qd[9]*(OMcp0_18*ROcp0_38-OMcp0_38*ROcp0_18)
    OPcp0_314 = OPcp0_37+ROcp0_310*qdd[13]+ROcp0_38*qdd[9]+ROcp0_613*qdd[14]+ROcp0_69*qdd[10]+ROcp0_97*qdd[8]+qd[10]*(\
   OMcp0_19*ROcp0_59-OMcp0_29*ROcp0_49)+qd[13]*(OMcp0_110*ROcp0_210-OMcp0_210*ROcp0_110)+qd[14]*(OMcp0_113*ROcp0_513-OMcp0_213*\
   ROcp0_413)+qd[8]*(OMcp0_17*ROcp0_87-OMcp0_27*ROcp0_77)+qd[9]*(OMcp0_18*ROcp0_28-OMcp0_28*ROcp0_18)

# = = Block_1_0_0_1_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp0_18
    sens.P[2] = POcp0_28
    sens.P[3] = POcp0_38
    sens.R[1,1] = ROcp0_114
    sens.R[1,2] = ROcp0_214
    sens.R[1,3] = ROcp0_314
    sens.R[2,1] = ROcp0_413
    sens.R[2,2] = ROcp0_513
    sens.R[2,3] = ROcp0_613
    sens.R[3,1] = ROcp0_714
    sens.R[3,2] = ROcp0_814
    sens.R[3,3] = ROcp0_914
    sens.V[1] = VIcp0_18
    sens.V[2] = VIcp0_28
    sens.V[3] = VIcp0_38
    sens.OM[1] = OMcp0_114
    sens.OM[2] = OMcp0_214
    sens.OM[3] = OMcp0_314
    sens.A[1] = ACcp0_18
    sens.A[2] = ACcp0_28
    sens.A[3] = ACcp0_38
    sens.OMP[1] = OPcp0_114
    sens.OMP[2] = OPcp0_214
    sens.OMP[3] = OPcp0_314
 
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
    ROcp1_76 = ROcp1_75*C6+S4*S6
    ROcp1_86 = ROcp1_85*C6-C4*S6
    OMcp1_15 = -qd[5]*S4
    OMcp1_25 = qd[5]*C4
    OMcp1_16 = OMcp1_15+ROcp1_15*qd[6]
    OMcp1_26 = OMcp1_25+ROcp1_25*qd[6]
    OMcp1_36 = qd[4]-qd[6]*S5
    OPcp1_16 = ROcp1_15*qdd[6]-qdd[5]*S4-qd[4]*qd[5]*C4-qd[6]*(OMcp1_25*S5+ROcp1_25*qd[4])
    OPcp1_26 = ROcp1_25*qdd[6]+qdd[5]*C4-qd[4]*qd[5]*S4+qd[6]*(OMcp1_15*S5+ROcp1_15*qd[4])
    OPcp1_36 = qdd[4]-qdd[6]*S5-qd[5]*qd[6]*C5

# = = Block_1_0_0_2_0_5 = = 
 
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
    OMcp1_115 = OMcp1_16+ROcp1_15*qd[15]
    OMcp1_215 = OMcp1_26+ROcp1_25*qd[15]
    OMcp1_315 = OMcp1_36-qd[15]*S5
    ORcp1_115 = OMcp1_26*RLcp1_315-OMcp1_36*RLcp1_215
    ORcp1_215 = -(OMcp1_16*RLcp1_315-OMcp1_36*RLcp1_115)
    ORcp1_315 = OMcp1_16*RLcp1_215-OMcp1_26*RLcp1_115
    OPcp1_115 = OPcp1_16+ROcp1_15*qdd[15]-qd[15]*(OMcp1_26*S5+OMcp1_36*ROcp1_25)
    OPcp1_215 = OPcp1_26+ROcp1_25*qdd[15]+qd[15]*(OMcp1_16*S5+OMcp1_36*ROcp1_15)
    OPcp1_315 = OPcp1_36-qdd[15]*S5+qd[15]*(OMcp1_16*ROcp1_25-OMcp1_26*ROcp1_15)
    RLcp1_116 = ROcp1_415*s.dpt[2,18]
    RLcp1_216 = ROcp1_515*s.dpt[2,18]
    RLcp1_316 = ROcp1_615*s.dpt[2,18]
    POcp1_116 = RLcp1_115+RLcp1_116+q[1]
    POcp1_216 = RLcp1_215+RLcp1_216+q[2]
    POcp1_316 = RLcp1_315+RLcp1_316+q[3]
    OMcp1_116 = OMcp1_115+ROcp1_715*qd[16]
    OMcp1_216 = OMcp1_215+ROcp1_815*qd[16]
    OMcp1_316 = OMcp1_315+ROcp1_915*qd[16]
    ORcp1_116 = OMcp1_215*RLcp1_316-OMcp1_315*RLcp1_216
    ORcp1_216 = -(OMcp1_115*RLcp1_316-OMcp1_315*RLcp1_116)
    ORcp1_316 = OMcp1_115*RLcp1_216-OMcp1_215*RLcp1_116
    VIcp1_116 = ORcp1_115+ORcp1_116+qd[1]
    VIcp1_216 = ORcp1_215+ORcp1_216+qd[2]
    VIcp1_316 = ORcp1_315+ORcp1_316+qd[3]
    ACcp1_116 = qdd[1]+OMcp1_215*ORcp1_316+OMcp1_26*ORcp1_315-OMcp1_315*ORcp1_216-OMcp1_36*ORcp1_215+OPcp1_215*RLcp1_316+\
   OPcp1_26*RLcp1_315-OPcp1_315*RLcp1_216-OPcp1_36*RLcp1_215
    ACcp1_216 = qdd[2]-OMcp1_115*ORcp1_316-OMcp1_16*ORcp1_315+OMcp1_315*ORcp1_116+OMcp1_36*ORcp1_115-OPcp1_115*RLcp1_316-\
   OPcp1_16*RLcp1_315+OPcp1_315*RLcp1_116+OPcp1_36*RLcp1_115
    ACcp1_316 = qdd[3]+OMcp1_115*ORcp1_216+OMcp1_16*ORcp1_215-OMcp1_215*ORcp1_116-OMcp1_26*ORcp1_115+OPcp1_115*RLcp1_216+\
   OPcp1_16*RLcp1_215-OPcp1_215*RLcp1_116-OPcp1_26*RLcp1_115
    OMcp1_117 = OMcp1_116+ROcp1_116*qd[17]
    OMcp1_217 = OMcp1_216+ROcp1_216*qd[17]
    OMcp1_317 = OMcp1_316+ROcp1_316*qd[17]
    OMcp1_118 = OMcp1_117+ROcp1_417*qd[18]
    OMcp1_218 = OMcp1_217+ROcp1_517*qd[18]
    OMcp1_318 = OMcp1_317+ROcp1_617*qd[18]

# = = Block_1_0_0_2_0_7 = = 
 
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
    OMcp1_121 = OMcp1_118+ROcp1_118*qd[21]
    OMcp1_221 = OMcp1_218+ROcp1_218*qd[21]
    OMcp1_321 = OMcp1_318+ROcp1_318*qd[21]
    OMcp1_122 = OMcp1_121+ROcp1_421*qd[22]
    OMcp1_222 = OMcp1_221+ROcp1_521*qd[22]
    OMcp1_322 = OMcp1_321+ROcp1_621*qd[22]
    OPcp1_122 = OPcp1_115+ROcp1_116*qdd[17]+ROcp1_118*qdd[21]+ROcp1_417*qdd[18]+ROcp1_421*qdd[22]+ROcp1_715*qdd[16]+qd[16]\
   *(OMcp1_215*ROcp1_915-OMcp1_315*ROcp1_815)+qd[17]*(OMcp1_216*ROcp1_316-OMcp1_316*ROcp1_216)+qd[18]*(OMcp1_217*ROcp1_617-\
   OMcp1_317*ROcp1_517)+qd[21]*(OMcp1_218*ROcp1_318-OMcp1_318*ROcp1_218)+qd[22]*(OMcp1_221*ROcp1_621-OMcp1_321*ROcp1_521)
    OPcp1_222 = OPcp1_215+ROcp1_216*qdd[17]+ROcp1_218*qdd[21]+ROcp1_517*qdd[18]+ROcp1_521*qdd[22]+ROcp1_815*qdd[16]-qd[16]\
   *(OMcp1_115*ROcp1_915-OMcp1_315*ROcp1_715)-qd[17]*(OMcp1_116*ROcp1_316-OMcp1_316*ROcp1_116)-qd[18]*(OMcp1_117*ROcp1_617-\
   OMcp1_317*ROcp1_417)-qd[21]*(OMcp1_118*ROcp1_318-OMcp1_318*ROcp1_118)-qd[22]*(OMcp1_121*ROcp1_621-OMcp1_321*ROcp1_421)
    OPcp1_322 = OPcp1_315+ROcp1_316*qdd[17]+ROcp1_318*qdd[21]+ROcp1_617*qdd[18]+ROcp1_621*qdd[22]+ROcp1_915*qdd[16]+qd[16]\
   *(OMcp1_115*ROcp1_815-OMcp1_215*ROcp1_715)+qd[17]*(OMcp1_116*ROcp1_216-OMcp1_216*ROcp1_116)+qd[18]*(OMcp1_117*ROcp1_517-\
   OMcp1_217*ROcp1_417)+qd[21]*(OMcp1_118*ROcp1_218-OMcp1_218*ROcp1_118)+qd[22]*(OMcp1_121*ROcp1_521-OMcp1_221*ROcp1_421)

# = = Block_1_0_0_2_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp1_116
    sens.P[2] = POcp1_216
    sens.P[3] = POcp1_316
    sens.R[1,1] = ROcp1_122
    sens.R[1,2] = ROcp1_222
    sens.R[1,3] = ROcp1_322
    sens.R[2,1] = ROcp1_421
    sens.R[2,2] = ROcp1_521
    sens.R[2,3] = ROcp1_621
    sens.R[3,1] = ROcp1_722
    sens.R[3,2] = ROcp1_822
    sens.R[3,3] = ROcp1_922
    sens.V[1] = VIcp1_116
    sens.V[2] = VIcp1_216
    sens.V[3] = VIcp1_316
    sens.OM[1] = OMcp1_122
    sens.OM[2] = OMcp1_222
    sens.OM[3] = OMcp1_322
    sens.A[1] = ACcp1_116
    sens.A[2] = ACcp1_216
    sens.A[3] = ACcp1_316
    sens.OMP[1] = OPcp1_122
    sens.OMP[2] = OPcp1_222
    sens.OMP[3] = OPcp1_322
 
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

# = = Block_1_0_0_3_0_8 = = 
 
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
    OMcp2_123 = OMcp2_16+ROcp2_15*qd[23]
    OMcp2_223 = OMcp2_26+ROcp2_25*qd[23]
    OMcp2_323 = OMcp2_36-qd[23]*S5
    ORcp2_123 = OMcp2_26*RLcp2_323-OMcp2_36*RLcp2_223
    ORcp2_223 = -(OMcp2_16*RLcp2_323-OMcp2_36*RLcp2_123)
    ORcp2_323 = OMcp2_16*RLcp2_223-OMcp2_26*RLcp2_123
    OMcp2_124 = OMcp2_123+ROcp2_723*qd[24]
    OMcp2_224 = OMcp2_223+ROcp2_823*qd[24]
    OMcp2_324 = OMcp2_323+ROcp2_923*qd[24]
    OPcp2_124 = OPcp2_16+ROcp2_15*qdd[23]+ROcp2_723*qdd[24]-qd[23]*(OMcp2_26*S5+OMcp2_36*ROcp2_25)+qd[24]*(OMcp2_223*\
   ROcp2_923-OMcp2_323*ROcp2_823)
    OPcp2_224 = OPcp2_26+ROcp2_25*qdd[23]+ROcp2_823*qdd[24]+qd[23]*(OMcp2_16*S5+OMcp2_36*ROcp2_15)-qd[24]*(OMcp2_123*\
   ROcp2_923-OMcp2_323*ROcp2_723)
    OPcp2_324 = OPcp2_36+ROcp2_923*qdd[24]-qdd[23]*S5+qd[23]*(OMcp2_16*ROcp2_25-OMcp2_26*ROcp2_15)+qd[24]*(OMcp2_123*\
   ROcp2_823-OMcp2_223*ROcp2_723)
    RLcp2_125 = ROcp2_424*s.dpt[2,23]
    RLcp2_225 = ROcp2_524*s.dpt[2,23]
    RLcp2_325 = ROcp2_624*s.dpt[2,23]
    OMcp2_125 = OMcp2_124+ROcp2_124*qd[25]
    OMcp2_225 = OMcp2_224+ROcp2_224*qd[25]
    OMcp2_325 = OMcp2_324+ROcp2_324*qd[25]
    ORcp2_125 = OMcp2_224*RLcp2_325-OMcp2_324*RLcp2_225
    ORcp2_225 = -(OMcp2_124*RLcp2_325-OMcp2_324*RLcp2_125)
    ORcp2_325 = OMcp2_124*RLcp2_225-OMcp2_224*RLcp2_125
    OMcp2_126 = OMcp2_125+ROcp2_725*qd[26]
    OMcp2_226 = OMcp2_225+ROcp2_825*qd[26]
    OMcp2_326 = OMcp2_325+ROcp2_925*qd[26]
    OPcp2_126 = OPcp2_124+ROcp2_124*qdd[25]+ROcp2_725*qdd[26]+qd[25]*(OMcp2_224*ROcp2_324-OMcp2_324*ROcp2_224)+qd[26]*(\
   OMcp2_225*ROcp2_925-OMcp2_325*ROcp2_825)
    OPcp2_226 = OPcp2_224+ROcp2_224*qdd[25]+ROcp2_825*qdd[26]-qd[25]*(OMcp2_124*ROcp2_324-OMcp2_324*ROcp2_124)-qd[26]*(\
   OMcp2_125*ROcp2_925-OMcp2_325*ROcp2_725)
    OPcp2_326 = OPcp2_324+ROcp2_324*qdd[25]+ROcp2_925*qdd[26]+qd[25]*(OMcp2_124*ROcp2_224-OMcp2_224*ROcp2_124)+qd[26]*(\
   OMcp2_125*ROcp2_825-OMcp2_225*ROcp2_725)

# = = Block_1_0_0_3_0_10 = = 
 
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
    POcp2_129 = RLcp2_123+RLcp2_125+RLcp2_129+q[1]
    POcp2_229 = RLcp2_223+RLcp2_225+RLcp2_229+q[2]
    POcp2_329 = RLcp2_323+RLcp2_325+RLcp2_329+q[3]
    OMcp2_129 = OMcp2_126+ROcp2_126*qd[29]
    OMcp2_229 = OMcp2_226+ROcp2_226*qd[29]
    OMcp2_329 = OMcp2_326+ROcp2_326*qd[29]
    ORcp2_129 = OMcp2_226*RLcp2_329-OMcp2_326*RLcp2_229
    ORcp2_229 = -(OMcp2_126*RLcp2_329-OMcp2_326*RLcp2_129)
    ORcp2_329 = OMcp2_126*RLcp2_229-OMcp2_226*RLcp2_129
    VIcp2_129 = ORcp2_123+ORcp2_125+ORcp2_129+qd[1]
    VIcp2_229 = ORcp2_223+ORcp2_225+ORcp2_229+qd[2]
    VIcp2_329 = ORcp2_323+ORcp2_325+ORcp2_329+qd[3]
    ACcp2_129 = qdd[1]+OMcp2_224*ORcp2_325+OMcp2_226*ORcp2_329+OMcp2_26*ORcp2_323-OMcp2_324*ORcp2_225-OMcp2_326*ORcp2_229-\
   OMcp2_36*ORcp2_223+OPcp2_224*RLcp2_325+OPcp2_226*RLcp2_329+OPcp2_26*RLcp2_323-OPcp2_324*RLcp2_225-OPcp2_326*RLcp2_229-\
   OPcp2_36*RLcp2_223
    ACcp2_229 = qdd[2]-OMcp2_124*ORcp2_325-OMcp2_126*ORcp2_329-OMcp2_16*ORcp2_323+OMcp2_324*ORcp2_125+OMcp2_326*ORcp2_129+\
   OMcp2_36*ORcp2_123-OPcp2_124*RLcp2_325-OPcp2_126*RLcp2_329-OPcp2_16*RLcp2_323+OPcp2_324*RLcp2_125+OPcp2_326*RLcp2_129+\
   OPcp2_36*RLcp2_123
    ACcp2_329 = qdd[3]+OMcp2_124*ORcp2_225+OMcp2_126*ORcp2_229+OMcp2_16*ORcp2_223-OMcp2_224*ORcp2_125-OMcp2_226*ORcp2_129-\
   OMcp2_26*ORcp2_123+OPcp2_124*RLcp2_225+OPcp2_126*RLcp2_229+OPcp2_16*RLcp2_223-OPcp2_224*RLcp2_125-OPcp2_226*RLcp2_129-\
   OPcp2_26*RLcp2_123
    OMcp2_130 = OMcp2_129+ROcp2_429*qd[30]
    OMcp2_230 = OMcp2_229+ROcp2_529*qd[30]
    OMcp2_330 = OMcp2_329+ROcp2_629*qd[30]
    OPcp2_130 = OPcp2_126+ROcp2_126*qdd[29]+ROcp2_429*qdd[30]+qd[29]*(OMcp2_226*ROcp2_326-OMcp2_326*ROcp2_226)+qd[30]*(\
   OMcp2_229*ROcp2_629-OMcp2_329*ROcp2_529)
    OPcp2_230 = OPcp2_226+ROcp2_226*qdd[29]+ROcp2_529*qdd[30]-qd[29]*(OMcp2_126*ROcp2_326-OMcp2_326*ROcp2_126)-qd[30]*(\
   OMcp2_129*ROcp2_629-OMcp2_329*ROcp2_429)
    OPcp2_330 = OPcp2_326+ROcp2_326*qdd[29]+ROcp2_629*qdd[30]+qd[29]*(OMcp2_126*ROcp2_226-OMcp2_226*ROcp2_126)+qd[30]*(\
   OMcp2_129*ROcp2_529-OMcp2_229*ROcp2_429)

# = = Block_1_0_0_3_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp2_129
    sens.P[2] = POcp2_229
    sens.P[3] = POcp2_329
    sens.R[1,1] = ROcp2_130
    sens.R[1,2] = ROcp2_230
    sens.R[1,3] = ROcp2_330
    sens.R[2,1] = ROcp2_429
    sens.R[2,2] = ROcp2_529
    sens.R[2,3] = ROcp2_629
    sens.R[3,1] = ROcp2_730
    sens.R[3,2] = ROcp2_830
    sens.R[3,3] = ROcp2_930
    sens.V[1] = VIcp2_129
    sens.V[2] = VIcp2_229
    sens.V[3] = VIcp2_329
    sens.OM[1] = OMcp2_130
    sens.OM[2] = OMcp2_230
    sens.OM[3] = OMcp2_330
    sens.A[1] = ACcp2_129
    sens.A[2] = ACcp2_229
    sens.A[3] = ACcp2_329
    sens.OMP[1] = OPcp2_130
    sens.OMP[2] = OPcp2_230
    sens.OMP[3] = OPcp2_330
 
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

# = = Block_1_0_0_4_0_11 = = 
 
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
    OMcp3_131 = OMcp3_16+ROcp3_15*qd[31]
    OMcp3_231 = OMcp3_26+ROcp3_25*qd[31]
    OMcp3_331 = OMcp3_36-qd[31]*S5
    ORcp3_131 = OMcp3_26*RLcp3_331-OMcp3_36*RLcp3_231
    ORcp3_231 = -(OMcp3_16*RLcp3_331-OMcp3_36*RLcp3_131)
    ORcp3_331 = OMcp3_16*RLcp3_231-OMcp3_26*RLcp3_131
    OMcp3_132 = OMcp3_131+ROcp3_731*qd[32]
    OMcp3_232 = OMcp3_231+ROcp3_831*qd[32]
    OMcp3_332 = OMcp3_331+ROcp3_931*qd[32]
    OPcp3_132 = OPcp3_16+ROcp3_15*qdd[31]+ROcp3_731*qdd[32]-qd[31]*(OMcp3_26*S5+OMcp3_36*ROcp3_25)+qd[32]*(OMcp3_231*\
   ROcp3_931-OMcp3_331*ROcp3_831)
    OPcp3_232 = OPcp3_26+ROcp3_25*qdd[31]+ROcp3_831*qdd[32]+qd[31]*(OMcp3_16*S5+OMcp3_36*ROcp3_15)-qd[32]*(OMcp3_131*\
   ROcp3_931-OMcp3_331*ROcp3_731)
    OPcp3_332 = OPcp3_36+ROcp3_931*qdd[32]-qdd[31]*S5+qd[31]*(OMcp3_16*ROcp3_25-OMcp3_26*ROcp3_15)+qd[32]*(OMcp3_131*\
   ROcp3_831-OMcp3_231*ROcp3_731)
    RLcp3_133 = ROcp3_432*s.dpt[2,30]
    RLcp3_233 = ROcp3_532*s.dpt[2,30]
    RLcp3_333 = ROcp3_632*s.dpt[2,30]
    OMcp3_133 = OMcp3_132+ROcp3_132*qd[33]
    OMcp3_233 = OMcp3_232+ROcp3_232*qd[33]
    OMcp3_333 = OMcp3_332+ROcp3_332*qd[33]
    ORcp3_133 = OMcp3_232*RLcp3_333-OMcp3_332*RLcp3_233
    ORcp3_233 = -(OMcp3_132*RLcp3_333-OMcp3_332*RLcp3_133)
    ORcp3_333 = OMcp3_132*RLcp3_233-OMcp3_232*RLcp3_133
    OMcp3_134 = OMcp3_133+ROcp3_733*qd[34]
    OMcp3_234 = OMcp3_233+ROcp3_833*qd[34]
    OMcp3_334 = OMcp3_333+ROcp3_933*qd[34]
    OPcp3_134 = OPcp3_132+ROcp3_132*qdd[33]+ROcp3_733*qdd[34]+qd[33]*(OMcp3_232*ROcp3_332-OMcp3_332*ROcp3_232)+qd[34]*(\
   OMcp3_233*ROcp3_933-OMcp3_333*ROcp3_833)
    OPcp3_234 = OPcp3_232+ROcp3_232*qdd[33]+ROcp3_833*qdd[34]-qd[33]*(OMcp3_132*ROcp3_332-OMcp3_332*ROcp3_132)-qd[34]*(\
   OMcp3_133*ROcp3_933-OMcp3_333*ROcp3_733)
    OPcp3_334 = OPcp3_332+ROcp3_332*qdd[33]+ROcp3_933*qdd[34]+qd[33]*(OMcp3_132*ROcp3_232-OMcp3_232*ROcp3_132)+qd[34]*(\
   OMcp3_133*ROcp3_833-OMcp3_233*ROcp3_733)

# = = Block_1_0_0_4_0_13 = = 
 
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
    POcp3_137 = RLcp3_131+RLcp3_133+RLcp3_137+q[1]
    POcp3_237 = RLcp3_231+RLcp3_233+RLcp3_237+q[2]
    POcp3_337 = RLcp3_331+RLcp3_333+RLcp3_337+q[3]
    OMcp3_137 = OMcp3_134+ROcp3_134*qd[37]
    OMcp3_237 = OMcp3_234+ROcp3_234*qd[37]
    OMcp3_337 = OMcp3_334+ROcp3_334*qd[37]
    ORcp3_137 = OMcp3_234*RLcp3_337-OMcp3_334*RLcp3_237
    ORcp3_237 = -(OMcp3_134*RLcp3_337-OMcp3_334*RLcp3_137)
    ORcp3_337 = OMcp3_134*RLcp3_237-OMcp3_234*RLcp3_137
    VIcp3_137 = ORcp3_131+ORcp3_133+ORcp3_137+qd[1]
    VIcp3_237 = ORcp3_231+ORcp3_233+ORcp3_237+qd[2]
    VIcp3_337 = ORcp3_331+ORcp3_333+ORcp3_337+qd[3]
    ACcp3_137 = qdd[1]+OMcp3_232*ORcp3_333+OMcp3_234*ORcp3_337+OMcp3_26*ORcp3_331-OMcp3_332*ORcp3_233-OMcp3_334*ORcp3_237-\
   OMcp3_36*ORcp3_231+OPcp3_232*RLcp3_333+OPcp3_234*RLcp3_337+OPcp3_26*RLcp3_331-OPcp3_332*RLcp3_233-OPcp3_334*RLcp3_237-\
   OPcp3_36*RLcp3_231
    ACcp3_237 = qdd[2]-OMcp3_132*ORcp3_333-OMcp3_134*ORcp3_337-OMcp3_16*ORcp3_331+OMcp3_332*ORcp3_133+OMcp3_334*ORcp3_137+\
   OMcp3_36*ORcp3_131-OPcp3_132*RLcp3_333-OPcp3_134*RLcp3_337-OPcp3_16*RLcp3_331+OPcp3_332*RLcp3_133+OPcp3_334*RLcp3_137+\
   OPcp3_36*RLcp3_131
    ACcp3_337 = qdd[3]+OMcp3_132*ORcp3_233+OMcp3_134*ORcp3_237+OMcp3_16*ORcp3_231-OMcp3_232*ORcp3_133-OMcp3_234*ORcp3_137-\
   OMcp3_26*ORcp3_131+OPcp3_132*RLcp3_233+OPcp3_134*RLcp3_237+OPcp3_16*RLcp3_231-OPcp3_232*RLcp3_133-OPcp3_234*RLcp3_137-\
   OPcp3_26*RLcp3_131
    OMcp3_138 = OMcp3_137+ROcp3_437*qd[38]
    OMcp3_238 = OMcp3_237+ROcp3_537*qd[38]
    OMcp3_338 = OMcp3_337+ROcp3_637*qd[38]
    OPcp3_138 = OPcp3_134+ROcp3_134*qdd[37]+ROcp3_437*qdd[38]+qd[37]*(OMcp3_234*ROcp3_334-OMcp3_334*ROcp3_234)+qd[38]*(\
   OMcp3_237*ROcp3_637-OMcp3_337*ROcp3_537)
    OPcp3_238 = OPcp3_234+ROcp3_234*qdd[37]+ROcp3_537*qdd[38]-qd[37]*(OMcp3_134*ROcp3_334-OMcp3_334*ROcp3_134)-qd[38]*(\
   OMcp3_137*ROcp3_637-OMcp3_337*ROcp3_437)
    OPcp3_338 = OPcp3_334+ROcp3_334*qdd[37]+ROcp3_637*qdd[38]+qd[37]*(OMcp3_134*ROcp3_234-OMcp3_234*ROcp3_134)+qd[38]*(\
   OMcp3_137*ROcp3_537-OMcp3_237*ROcp3_437)

# = = Block_1_0_0_4_1_0 = = 
 
# Symbolic Outputs  

    sens.P[1] = POcp3_137
    sens.P[2] = POcp3_237
    sens.P[3] = POcp3_337
    sens.R[1,1] = ROcp3_138
    sens.R[1,2] = ROcp3_238
    sens.R[1,3] = ROcp3_338
    sens.R[2,1] = ROcp3_437
    sens.R[2,2] = ROcp3_537
    sens.R[2,3] = ROcp3_637
    sens.R[3,1] = ROcp3_738
    sens.R[3,2] = ROcp3_838
    sens.R[3,3] = ROcp3_938
    sens.V[1] = VIcp3_137
    sens.V[2] = VIcp3_237
    sens.V[3] = VIcp3_337
    sens.OM[1] = OMcp3_138
    sens.OM[2] = OMcp3_238
    sens.OM[3] = OMcp3_338
    sens.A[1] = ACcp3_137
    sens.A[2] = ACcp3_237
    sens.A[3] = ACcp3_337
    sens.OMP[1] = OPcp3_138
    sens.OMP[2] = OPcp3_238
    sens.OMP[3] = OPcp3_338



# ====== END Task 1 ====== 

  

