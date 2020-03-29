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
#	==> Function : F 8 : Constraints Vector (h) and Jacobian Matrix (Jac) 
#	==> Flops complexity : 109
#
#	==> Generation Time :  0.000 seconds
#	==> Post-Processing :  0.010 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def cons_hJ(h,Jac,s):   
  q = s.q
  qd = s.qd
  qdd = s.qdd

# === begin imp_aux === 

# === end imp_aux === 

# ===== BEGIN task 0 ===== 

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C13 = np.cos(q[13])
  S13 = np.sin(q[13])
  C14 = np.cos(q[14])
  S14 = np.sin(q[14])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C16 = np.cos(q[16])
  S16 = np.sin(q[16])
  C17 = np.cos(q[17])
  S17 = np.sin(q[17])

# = = Block_0_1_0_0_0_4 = = 
 
# Trigonometric Variables  

#
  S13p14 = C13*S14+S13*C14
  C13p14 = C13*C14-S13*S14
 
# Constraints and Constraints Jacobian 

  RL_1_214 = s.dpt[2,24]*C13
  RL_1_314 = s.dpt[2,24]*S13
  PO_1_214 = RL_1_214+s.dpt[2,9]
  PO_1_314 = RL_1_314+s.dpt[3,9]
  RL_1_220 = -s.dpt[3,27]*S13p14
  RL_1_320 = s.dpt[3,27]*C13p14
  PO_1_320 = PO_1_314+RL_1_320

# = = Block_0_1_0_0_0_5 = = 
 
# Trigonometric Variables  

#
  S16p17 = C16*S17+S16*C17
  C16p17 = C16*C17-S16*S17
 
# Constraints and Constraints Jacobian 

  RL_4_217 = s.dpt[2,30]*C16
  RL_4_317 = s.dpt[2,30]*S16
  PO_4_217 = RL_4_217+s.dpt[2,11]
  PO_4_317 = RL_4_317+s.dpt[3,11]
  RL_4_223 = -s.dpt[3,31]*S16p17
  RL_4_323 = s.dpt[3,31]*C16p17
  PO_4_323 = PO_4_317+RL_4_323

# = = Block_0_1_0_0_1_0 = = 
 
# Constraints and Constraints Jacobian 

#
  Plp11 = s.dpt[1,10]-s.dpt[1,9]
  Plp21 = -(PO_1_214+RL_1_220-s.dpt[2,10])
  h_1 = (0.50)*(PO_1_320*PO_1_320+Plp11*Plp11+Plp21*Plp21-s.lrod[1]*s.lrod[1])
#
  Jacu_1_13 = PO_1_320*(RL_1_214+RL_1_220)+Plp21*(RL_1_314+RL_1_320)
  Jac_1_14 = PO_1_320*RL_1_220+Plp21*RL_1_320
#
  Plp12 = -(s.dpt[1,28]-s.dpt[1,6]+s.dpt[1,9])
  Plp22 = -(PO_1_214-s.dpt[2,6])
  Plp32 = -(PO_1_314-s.dpt[3,6])
  h_2 = (0.50)*(Plp12*Plp12+Plp22*Plp22+Plp32*Plp32-s.lrod[2]*s.lrod[2])
#
  Jacu_2_13 = Plp22*RL_1_314-Plp32*RL_1_214
#
  Plp13 = s.dpt[1,11]-s.dpt[1,12]
  Plp23 = PO_4_217+RL_4_223-s.dpt[2,12]
  h_3 = (0.50)*(PO_4_323*PO_4_323+Plp13*Plp13+Plp23*Plp23-s.lrod[3]*s.lrod[3])
#
  Jacu_3_16 = PO_4_323*(RL_4_217+RL_4_223)-Plp23*(RL_4_317+RL_4_323)
  Jac_3_17 = PO_4_323*RL_4_223-Plp23*RL_4_323
#
  Plp14 = s.dpt[1,11]+s.dpt[1,32]-s.dpt[1,8]
  Plp24 = PO_4_217-s.dpt[2,8]
  Plp34 = PO_4_317-s.dpt[3,8]
  h_4 = (0.50)*(Plp14*Plp14+Plp24*Plp24+Plp34*Plp34-s.lrod[4]*s.lrod[4])
#
  Jacu_4_16 = -(Plp24*RL_4_317-Plp34*RL_4_217)

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  h[1] = h_1
  h[2] = h_2
  h[3] = h_3
  h[4] = h_4
  Jac[1,13] = Jacu_1_13
  Jac[1,14] = Jac_1_14
  Jac[2,13] = Jacu_2_13
  Jac[3,16] = Jacu_3_16
  Jac[3,17] = Jac_3_17
  Jac[4,16] = Jacu_4_16

# ====== END Task 0 ====== 

  

