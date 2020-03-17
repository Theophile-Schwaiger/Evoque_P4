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
#	==> Function : F 8 : Constraints Vector (h) and Jacobian Matrix (Jac) 
#	==> Flops complexity : 109
#
#	==> Generation Time :  0.000 seconds
#	==> Post-Processing :  0.000 seconds
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

# = = Block_0_1_0_0_0_4 = = 
 
# Trigonometric Variables  

#
  S15p16 = C15*S16+S15*C16
  C15p16 = C15*C16-S15*S16
 
# Constraints and Constraints Jacobian 

  RL_1_216 = s.dpt[2,21]*C15
  RL_1_316 = s.dpt[2,21]*S15
  PO_1_216 = RL_1_216+s.dpt[2,9]
  PO_1_316 = RL_1_316+s.dpt[3,9]
  RL_1_224 = -s.dpt[3,24]*S15p16
  RL_1_324 = s.dpt[3,24]*C15p16
  PO_1_324 = PO_1_316+RL_1_324

# = = Block_0_1_0_0_0_5 = = 
 
# Trigonometric Variables  

#
  S19p20 = C19*S20+S19*C20
  C19p20 = C19*C20-S19*S20
 
# Constraints and Constraints Jacobian 

  RL_4_220 = s.dpt[2,27]*C19
  RL_4_320 = s.dpt[2,27]*S19
  PO_4_220 = RL_4_220+s.dpt[2,11]
  PO_4_320 = RL_4_320+s.dpt[3,11]
  RL_4_227 = -s.dpt[3,28]*S19p20
  RL_4_327 = s.dpt[3,28]*C19p20
  PO_4_327 = PO_4_320+RL_4_327

# = = Block_0_1_0_0_1_0 = = 
 
# Constraints and Constraints Jacobian 

#
  Plp11 = s.dpt[1,10]-s.dpt[1,9]
  Plp21 = -(PO_1_216+RL_1_224-s.dpt[2,10])
  h_1 = (0.50)*(PO_1_324*PO_1_324+Plp11*Plp11+Plp21*Plp21-s.lrod[1]*s.lrod[1])
#
  Jacu_1_15 = PO_1_324*(RL_1_216+RL_1_224)+Plp21*(RL_1_316+RL_1_324)
  Jac_1_16 = PO_1_324*RL_1_224+Plp21*RL_1_324
#
  Plp12 = -(s.dpt[1,25]-s.dpt[1,6]+s.dpt[1,9])
  Plp22 = -(PO_1_216-s.dpt[2,6])
  Plp32 = -(PO_1_316-s.dpt[3,6])
  h_2 = (0.50)*(Plp12*Plp12+Plp22*Plp22+Plp32*Plp32-s.lrod[2]*s.lrod[2])
#
  Jacu_2_15 = Plp22*RL_1_316-Plp32*RL_1_216
#
  Plp13 = s.dpt[1,11]-s.dpt[1,12]
  Plp23 = PO_4_220+RL_4_227-s.dpt[2,12]
  h_3 = (0.50)*(PO_4_327*PO_4_327+Plp13*Plp13+Plp23*Plp23-s.lrod[3]*s.lrod[3])
#
  Jacu_3_19 = PO_4_327*(RL_4_220+RL_4_227)-Plp23*(RL_4_320+RL_4_327)
  Jac_3_20 = PO_4_327*RL_4_227-Plp23*RL_4_327
#
  Plp14 = s.dpt[1,11]+s.dpt[1,29]-s.dpt[1,8]
  Plp24 = PO_4_220-s.dpt[2,8]
  Plp34 = PO_4_320-s.dpt[3,8]
  h_4 = (0.50)*(Plp14*Plp14+Plp24*Plp24+Plp34*Plp34-s.lrod[4]*s.lrod[4])
#
  Jacu_4_19 = -(Plp24*RL_4_320-Plp34*RL_4_220)

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  h[1] = h_1
  h[2] = h_2
  h[3] = h_3
  h[4] = h_4
  Jac[1,15] = Jacu_1_15
  Jac[1,16] = Jac_1_16
  Jac[2,15] = Jacu_2_15
  Jac[3,19] = Jacu_3_19
  Jac[3,20] = Jac_3_20
  Jac[4,19] = Jacu_4_19

# ====== END Task 0 ====== 

  

