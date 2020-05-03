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
#	==> Generation Date : Sat Mar 28 16:35:51 2020
#
#	==> Project name : Complete_Vehicle
#	==> using XML input file 
#
#	==> Number of joints : 30
#
#	==> Function : F 7 : Point to point Link Forces (frc,trq,Flnk) 
#	==> Flops complexity : 134
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

# = = Block_0_1_0_0_1_2 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  RLlnk0_28 = s.dpt[2,13]*C7
  RLlnk0_38 = s.dpt[2,13]*S7
  RLlnk0_243 = -s.dpt[3,14]*S7
  RLlnk0_343 = s.dpt[3,14]*C7

# = = Block_0_1_0_0_2_3 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  RLlnk2_212 = s.dpt[2,17]*C11
  RLlnk2_312 = s.dpt[2,17]*S11
  RLlnk2_245 = -s.dpt[3,18]*S11
  RLlnk2_345 = s.dpt[3,18]*C11

# = = Block_0_1_0_1_1_1 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  Plnk11 = -(s.dpt[1,1]-s.dpt[1,3])
  Plnk21 = -(RLlnk0_243+RLlnk0_28+s.dpt[2,1]-s.dpt[2,3])
  Plnk31 = -(RLlnk0_343+RLlnk0_38+s.dpt[3,1]-s.dpt[3,3])
  Z1 = np.sqrt(Plnk11*Plnk11+Plnk21*Plnk21+Plnk31*Plnk31)
  e11 = Plnk11/Z1
  e21 = Plnk21/Z1
  e31 = Plnk31/Z1
  Zd1 = qd[7]*(e21*(RLlnk0_343+RLlnk0_38)-e31*(RLlnk0_243+RLlnk0_28))
 
# Link Force Computation 

  Flink1 = s.user_LinkForces(Z1,Zd1,s,tsim,1)

# = = Block_0_1_0_1_2_1 = = 
 
# Link Kinematics: Distance Z , Relative Velocity ZD 

  Plnk12 = s.dpt[1,2]-s.dpt[1,4]
  Plnk22 = -(RLlnk2_212+RLlnk2_245-s.dpt[2,2]+s.dpt[2,4])
  Plnk32 = -(RLlnk2_312+RLlnk2_345-s.dpt[3,2]+s.dpt[3,4])
  Z2 = np.sqrt(Plnk12*Plnk12+Plnk22*Plnk22+Plnk32*Plnk32)
  e12 = Plnk12/Z2
  e22 = Plnk22/Z2
  e32 = Plnk32/Z2
  Zd2 = qd[11]*(e22*(RLlnk2_312+RLlnk2_345)-e32*(RLlnk2_212+RLlnk2_245))
 
# Link Force Computation 

  Flink2 = s.user_LinkForces(Z2,Zd2,s,tsim,2)

# = = Block_0_1_0_2_2_1 = = 
 
# Link Dynamics : Forces projection on body-fixed frames 

  fSlnk11 = Flink1*e11
  fSlnk21 = Flink1*e21
  fSlnk31 = Flink1*e31
  s.frc[1,6] = s.frc[1,6]-fSlnk11
  s.frc[2,6] = s.frc[2,6]-fSlnk21
  s.frc[3,6] = s.frc[3,6]-fSlnk31
  s.trq[1,6] = s.trq[1,6]+fSlnk21*(s.dpt[3,3]-s.l[3,6])-fSlnk31*s.dpt[2,3]
  s.trq[2,6] = s.trq[2,6]-fSlnk11*(s.dpt[3,3]-s.l[3,6])+fSlnk31*s.dpt[1,3]
  s.trq[3,6] = s.trq[3,6]+fSlnk11*s.dpt[2,3]-fSlnk21*s.dpt[1,3]

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
  frc[1,6] = -(fSlnk12-s.frc[1,6])
  frc[2,6] = -(fSlnk22-s.frc[2,6])
  frc[3,6] = -(fSlnk32-s.frc[3,6])
  trq[1,6] = s.trq[1,6]+fSlnk22*(s.dpt[3,2]-s.l[3,6])-fSlnk32*s.dpt[2,2]
  trq[2,6] = s.trq[2,6]-fSlnk12*(s.dpt[3,2]-s.l[3,6])+fSlnk32*s.dpt[1,2]
  trq[3,6] = s.trq[3,6]+fSlnk12*s.dpt[2,2]-fSlnk22*s.dpt[1,2]

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
  frc[1,16] = s.frc[1,16]
  frc[2,16] = s.frc[2,16]
  frc[3,16] = s.frc[3,16]
  frc[1,18] = s.frc[1,18]
  frc[2,18] = s.frc[2,18]
  frc[3,18] = s.frc[3,18]
  frc[1,20] = s.frc[1,20]
  frc[2,20] = s.frc[2,20]
  frc[3,20] = s.frc[3,20]
  frc[1,22] = s.frc[1,22]
  frc[2,22] = s.frc[2,22]
  frc[3,22] = s.frc[3,22]
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
  trq[1,16] = s.trq[1,16]
  trq[2,16] = s.trq[2,16]
  trq[3,16] = s.trq[3,16]
  trq[1,18] = s.trq[1,18]
  trq[2,18] = s.trq[2,18]
  trq[3,18] = s.trq[3,18]
  trq[1,20] = s.trq[1,20]
  trq[2,20] = s.trq[2,20]
  trq[3,20] = s.trq[3,20]
  trq[1,22] = s.trq[1,22]
  trq[2,22] = s.trq[2,22]
  trq[3,22] = s.trq[3,22]
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
  Flnk[1] = Flink1
  Flnk[2] = Flink2
  Z[1] = Z1
  Z[2] = Z2
  Zd[1] = Zd1
  Zd[2] = Zd2

# ====== END Task 0 ====== 

  

