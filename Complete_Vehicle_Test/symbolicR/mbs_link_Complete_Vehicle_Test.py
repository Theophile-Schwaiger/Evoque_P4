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
#	==> Generation Date : Mon Mar 16 22:45:11 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 22
#
#	==> Function : F 7 : Point to point Link Forces (frc,trq,Flnk) 
#	==> Flops complexity : 283
#
#	==> Generation Time :  0.000 seconds
#	==> Post-Processing :  0.010 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def link(frc, trq, Flnk, Z, Zd, s, tsim):   
  q = s.q
  qd = s.qd
  qdd = s.qdd
  frc = s.frc
  trq = s.trq

# === begin imp_aux === 

# === end imp_aux === 

# ===== BEGIN task 0 ===== 

# = = Block_0_0_0_0_0_2 = = 
 
# Trigonometric Variables  

  C7 = np.cos(q[7])
  S7 = np.sin(q[7])
  C8 = np.cos(q[8])
  S8 = np.sin(q[8])

# = = Block_0_0_0_0_0_3 = = 
 
# Trigonometric Variables  

  C11 = np.cos(q[11])
  S11 = np.sin(q[11])
  C12 = np.cos(q[12])
  S12 = np.sin(q[12])

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C15 = np.cos(q[15])
  S15 = np.sin(q[15])
  C16 = np.cos(q[16])
  S16 = np.sin(q[16])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C19 = np.cos(q[19])
  S19 = np.sin(q[19])
  C20 = np.cos(q[20])
  S20 = np.sin(q[20])

# = = Block_0_1_0_0_1_2 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  RLlnk0_28 = s.dpt[2,13]*C7
  RLlnk0_38 = s.dpt[2,13]*S7
  RLlnk0_231 = -s.dpt[3,14]*S7
  RLlnk0_331 = s.dpt[3,14]*C7

# = = Block_0_1_0_0_2_3 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  RLlnk2_212 = s.dpt[2,17]*C11
  RLlnk2_312 = s.dpt[2,17]*S11
  RLlnk2_233 = -s.dpt[3,18]*S11
  RLlnk2_333 = s.dpt[3,18]*C11

# = = Block_0_1_0_0_3_4 = = 
 
# Trigonometric Variables  

  S15p16 = C15*S16+S15*C16
  C15p16 = C15*C16-S15*S16
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  RLlnk5_216 = s.dpt[2,21]*C15
  RLlnk5_316 = s.dpt[2,21]*S15
  OMlnk5_116 = qd[15]+qd[16]
  RLlnk5_236 = -s.dpt[3,22]*S15p16
  RLlnk5_336 = s.dpt[3,22]*C15p16

# = = Block_0_1_0_0_4_5 = = 
 
# Trigonometric Variables  

  S19p20 = C19*S20+S19*C20
  C19p20 = C19*C20-S19*S20
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  RLlnk6_220 = s.dpt[2,27]*C19
  RLlnk6_320 = s.dpt[2,27]*S19
  OMlnk6_120 = qd[19]+qd[20]
  RLlnk6_237 = -s.dpt[3,30]*S19p20
  RLlnk6_337 = s.dpt[3,30]*C19p20

# = = Block_0_1_0_1_1_1 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  Plnk11 = -(s.dpt[1,1]-s.dpt[1,3])
  Plnk21 = -(RLlnk0_231+RLlnk0_28+s.dpt[2,1]-s.dpt[2,3])
  Plnk31 = -(RLlnk0_331+RLlnk0_38+s.dpt[3,1]-s.dpt[3,3])
  Z1 = np.sqrt(Plnk11*Plnk11+Plnk21*Plnk21+Plnk31*Plnk31)
  e11 = Plnk11/Z1
  e21 = Plnk21/Z1
  e31 = Plnk31/Z1
  Zd1 = qd[7]*(e21*(RLlnk0_331+RLlnk0_38)-e31*(RLlnk0_231+RLlnk0_28))
 
# Link Force Computation 

  Flink1 = s.user_LinkForces(Z1,Zd1,s,tsim,1)

# = = Block_0_1_0_1_2_1 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  Plnk12 = s.dpt[1,2]-s.dpt[1,4]
  Plnk22 = -(RLlnk2_212+RLlnk2_233-s.dpt[2,2]+s.dpt[2,4])
  Plnk32 = -(RLlnk2_312+RLlnk2_333-s.dpt[3,2]+s.dpt[3,4])
  Z2 = np.sqrt(Plnk12*Plnk12+Plnk22*Plnk22+Plnk32*Plnk32)
  e12 = Plnk12/Z2
  e22 = Plnk22/Z2
  e32 = Plnk32/Z2
  Zd2 = qd[11]*(e22*(RLlnk2_312+RLlnk2_333)-e32*(RLlnk2_212+RLlnk2_233))
 
# Link Force Computation 

  Flink2 = s.user_LinkForces(Z2,Zd2,s,tsim,2)

# = = Block_0_1_0_1_3_4 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  Plnk13 = s.dpt[1,22]-s.dpt[1,5]+s.dpt[1,9]
  Plnk23 = RLlnk5_216+RLlnk5_236-s.dpt[2,5]+s.dpt[2,9]
  Plnk33 = RLlnk5_316+RLlnk5_336-s.dpt[3,5]+s.dpt[3,9]
  Z3 = np.sqrt(Plnk13*Plnk13+Plnk23*Plnk23+Plnk33*Plnk33)
  e13 = Plnk13/Z3
  e23 = Plnk23/Z3
  e33 = Plnk33/Z3
  Zd3 = (qd[15]*RLlnk5_216+OMlnk5_116*RLlnk5_236)*e33-e23*(qd[15]*RLlnk5_316+OMlnk5_116*RLlnk5_336)
 
# Link Force Computation 

  Flink3 = s.user_LinkForces(Z3,Zd3,s,tsim,3)

# = = Block_0_1_0_1_4_1 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  Plnk14 = -(s.dpt[1,11]+s.dpt[1,30]-s.dpt[1,7])
  Plnk24 = -(RLlnk6_220+RLlnk6_237+s.dpt[2,11]-s.dpt[2,7])
  Plnk34 = -(RLlnk6_320+RLlnk6_337+s.dpt[3,11]-s.dpt[3,7])
  Z4 = np.sqrt(Plnk14*Plnk14+Plnk24*Plnk24+Plnk34*Plnk34)
  e14 = Plnk14/Z4
  e24 = Plnk24/Z4
  e34 = Plnk34/Z4
  Zd4 = e24*(qd[19]*RLlnk6_320+OMlnk6_120*RLlnk6_337)-e34*(qd[19]*RLlnk6_220+OMlnk6_120*RLlnk6_237)
 
# Link Force Computation 

  Flink4 = s.user_LinkForces(Z4,Zd4,s,tsim,4)

# = = Block_0_1_0_2_2_1 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fSlnk11 = Flink1*e11
  fSlnk21 = Flink1*e21
  fSlnk31 = Flink1*e31

# = = Block_0_1_0_2_2_2 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fPlnk11 = Flink1*(e11*C8+e21*C7*S8+e31*S7*S8)
  fPlnk21 = Flink1*(S7*C8*e31-e11*S8+e21*C7*C8)
  fPlnk31 = -Flink1*(e21*S7-e31*C7)
  frc[1,8] = s.frc[1,8]+fPlnk11
  frc[2,8] = s.frc[2,8]+fPlnk21
  frc[3,8] = s.frc[3,8]+fPlnk31
  trq[1,8] = s.trq[1,8]-fPlnk21*(s.dpt[3,14]-s.l[3,8])
  trq[2,8] = s.trq[2,8]+fPlnk11*(s.dpt[3,14]-s.l[3,8])

# = = Block_0_1_0_2_3_1 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fSlnk12 = Flink2*e12
  fSlnk22 = Flink2*e22
  fSlnk32 = Flink2*e32

# = = Block_0_1_0_2_3_3 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fPlnk12 = Flink2*(e12*C12+e22*C11*S12+e32*S11*S12)
  fPlnk22 = Flink2*(S11*C12*e32-e12*S12+e22*C11*C12)
  fPlnk32 = -Flink2*(e22*S11-e32*C11)
  frc[1,12] = s.frc[1,12]+fPlnk12
  frc[2,12] = s.frc[2,12]+fPlnk22
  frc[3,12] = s.frc[3,12]+fPlnk32
  trq[1,12] = s.trq[1,12]-fPlnk22*(s.dpt[3,18]-s.l[3,12])
  trq[2,12] = s.trq[2,12]+fPlnk12*(s.dpt[3,18]-s.l[3,12])

# = = Block_0_1_0_2_4_1 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fPlnk13 = Flink3*e13
  fPlnk23 = Flink3*e23
  fPlnk33 = Flink3*e33
  s.frc[1,6] = s.frc[1,6]+fPlnk13-fSlnk11-fSlnk12
  s.frc[2,6] = s.frc[2,6]+fPlnk23-fSlnk21-fSlnk22
  s.frc[3,6] = s.frc[3,6]+fPlnk33-fSlnk31-fSlnk32
  s.trq[1,6] = s.trq[1,6]-fPlnk23*(s.dpt[3,5]-s.l[3,6])+fPlnk33*s.dpt[2,5]+fSlnk21*(s.dpt[3,3]-s.l[3,6])+fSlnk22*(\
   s.dpt[3,2]-s.l[3,6])-fSlnk31*s.dpt[2,3]-fSlnk32*s.dpt[2,2]
  s.trq[2,6] = s.trq[2,6]+fPlnk13*(s.dpt[3,5]-s.l[3,6])-fPlnk33*s.dpt[1,5]-fSlnk11*(s.dpt[3,3]-s.l[3,6])-fSlnk12*(\
   s.dpt[3,2]-s.l[3,6])+fSlnk31*s.dpt[1,3]+fSlnk32*s.dpt[1,2]
  s.trq[3,6] = s.trq[3,6]-fPlnk13*s.dpt[2,5]+fPlnk23*s.dpt[1,5]+fSlnk11*s.dpt[2,3]+fSlnk12*s.dpt[2,2]-fSlnk21*s.dpt[1,3]\
   -fSlnk22*s.dpt[1,2]

# = = Block_0_1_0_2_4_4 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fSlnk13 = Flink3*e13
  fSlnk23 = Flink3*(e23*C15p16+e33*S15p16)
  fSlnk33 = -Flink3*(e23*S15p16-e33*C15p16)
  frc[1,16] = s.frc[1,16]-fSlnk13
  frc[2,16] = s.frc[2,16]-fSlnk23
  frc[3,16] = s.frc[3,16]-fSlnk33
  trq[1,16] = s.trq[1,16]+fSlnk23*s.dpt[3,22]
  trq[2,16] = s.trq[2,16]-fSlnk13*s.dpt[3,22]+fSlnk33*(s.dpt[1,22]-s.l[1,16])
  trq[3,16] = s.trq[3,16]-fSlnk23*(s.dpt[1,22]-s.l[1,16])

# = = Block_0_1_0_2_5_1 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fSlnk14 = Flink4*e14
  fSlnk24 = Flink4*e24
  fSlnk34 = Flink4*e34
  frc[1,6] = -(fSlnk14-s.frc[1,6])
  frc[2,6] = -(fSlnk24-s.frc[2,6])
  frc[3,6] = -(fSlnk34-s.frc[3,6])
  trq[1,6] = s.trq[1,6]+fSlnk24*(s.dpt[3,7]-s.l[3,6])-fSlnk34*s.dpt[2,7]
  trq[2,6] = s.trq[2,6]-fSlnk14*(s.dpt[3,7]-s.l[3,6])+fSlnk34*s.dpt[1,7]
  trq[3,6] = s.trq[3,6]+fSlnk14*s.dpt[2,7]-fSlnk24*s.dpt[1,7]

# = = Block_0_1_0_2_5_5 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fPlnk14 = Flink4*e14
  fPlnk24 = Flink4*(e24*C19p20+e34*S19p20)
  fPlnk34 = -Flink4*(e24*S19p20-e34*C19p20)
  frc[1,20] = s.frc[1,20]+fPlnk14
  frc[2,20] = s.frc[2,20]+fPlnk24
  frc[3,20] = s.frc[3,20]+fPlnk34
  trq[1,20] = s.trq[1,20]-fPlnk24*s.dpt[3,30]
  trq[2,20] = s.trq[2,20]+fPlnk14*s.dpt[3,30]-fPlnk34*(s.dpt[1,30]-s.l[1,20])
  trq[3,20] = s.trq[3,20]+fPlnk24*(s.dpt[1,30]-s.l[1,20])

# = = Block_0_2_0_0_0_0 = = 
 
# Symbolic Outputs  

  frc[1,7] = s.frc[1,7]
  frc[2,7] = s.frc[2,7]
  frc[3,7] = s.frc[3,7]
  frc[1,10] = s.frc[1,10]
  frc[2,10] = s.frc[2,10]
  frc[3,10] = s.frc[3,10]
  frc[1,11] = s.frc[1,11]
  frc[2,11] = s.frc[2,11]
  frc[3,11] = s.frc[3,11]
  frc[1,14] = s.frc[1,14]
  frc[2,14] = s.frc[2,14]
  frc[3,14] = s.frc[3,14]
  frc[1,15] = s.frc[1,15]
  frc[2,15] = s.frc[2,15]
  frc[3,15] = s.frc[3,15]
  frc[1,18] = s.frc[1,18]
  frc[2,18] = s.frc[2,18]
  frc[3,18] = s.frc[3,18]
  frc[1,19] = s.frc[1,19]
  frc[2,19] = s.frc[2,19]
  frc[3,19] = s.frc[3,19]
  frc[1,22] = s.frc[1,22]
  frc[2,22] = s.frc[2,22]
  frc[3,22] = s.frc[3,22]
  trq[1,7] = s.trq[1,7]
  trq[2,7] = s.trq[2,7]
  trq[3,7] = s.trq[3,7]
  trq[3,8] = s.trq[3,8]
  trq[1,10] = s.trq[1,10]
  trq[2,10] = s.trq[2,10]
  trq[3,10] = s.trq[3,10]
  trq[1,11] = s.trq[1,11]
  trq[2,11] = s.trq[2,11]
  trq[3,11] = s.trq[3,11]
  trq[3,12] = s.trq[3,12]
  trq[1,14] = s.trq[1,14]
  trq[2,14] = s.trq[2,14]
  trq[3,14] = s.trq[3,14]
  trq[1,15] = s.trq[1,15]
  trq[2,15] = s.trq[2,15]
  trq[3,15] = s.trq[3,15]
  trq[1,18] = s.trq[1,18]
  trq[2,18] = s.trq[2,18]
  trq[3,18] = s.trq[3,18]
  trq[1,19] = s.trq[1,19]
  trq[2,19] = s.trq[2,19]
  trq[3,19] = s.trq[3,19]
  trq[1,22] = s.trq[1,22]
  trq[2,22] = s.trq[2,22]
  trq[3,22] = s.trq[3,22]
  Flnk[1] = Flink1
  Flnk[2] = Flink2
  Flnk[3] = Flink3
  Flnk[4] = Flink4
  Z[1] = Z1
  Z[2] = Z2
  Z[3] = Z3
  Z[4] = Z4
  Zd[1] = Zd1
  Zd[2] = Zd2
  Zd[3] = Zd3
  Zd[4] = Zd4

# ====== END Task 0 ====== 

  
