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
#	==> Generation Date : Mon Mar 16 22:45:10 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 22
#
#	==> Function : F18 : Constraints Quadratic Velocity Terms (Jdqd)
#	==> Flops complexity : 104
#
#	==> Generation Time :  0.000 seconds
#	==> Post-Processing :  0.000 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def cons_jdqd(Jdqd,s):   
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

# = = Block_0_2_0_0_0_0 = = 
 
# Constraints Quadratic Terms 

#
  OM_1_116 = qd[15]+qd[16]
  OR_1_216 = -RL_1_316*qd[15]
  OR_1_316 = RL_1_216*qd[15]
  Apqp_1_216 = -OR_1_316*qd[15]
  Apqp_1_316 = OR_1_216*qd[15]
  OR_1_224 = -OM_1_116*RL_1_324
  OR_1_324 = OM_1_116*RL_1_224
  VI_1_224 = OR_1_216+OR_1_224
  VI_1_324 = OR_1_316+OR_1_324
#
  OM_4_120 = qd[19]+qd[20]
  OR_4_220 = -RL_4_320*qd[19]
  OR_4_320 = RL_4_220*qd[19]
  Apqp_4_220 = -OR_4_320*qd[19]
  Apqp_4_320 = OR_4_220*qd[19]
  OR_4_227 = -OM_4_120*RL_4_327
  OR_4_327 = OM_4_120*RL_4_227
  VI_4_227 = OR_4_220+OR_4_227
  VI_4_327 = OR_4_320+OR_4_327

# = = Block_0_2_0_0_0_1 = = 
 
# Constraints Quadratic Terms 

#
  jdqd1 = VI_1_224*VI_1_224+VI_1_324*VI_1_324+(Apqp_1_316+OM_1_116*OR_1_224)*(PO_1_316+RL_1_324)+(Apqp_1_216-OM_1_116*\
   OR_1_324)*(PO_1_216+RL_1_224-s.dpt[2,10])
#
  jdqd2 = Apqp_1_216*(PO_1_216-s.dpt[2,6])+Apqp_1_316*(PO_1_316-s.dpt[3,6])+OR_1_216*OR_1_216+OR_1_316*OR_1_316
#
  jdqd3 = VI_4_227*VI_4_227+VI_4_327*VI_4_327+(Apqp_4_320+OM_4_120*OR_4_227)*(PO_4_320+RL_4_327)+(Apqp_4_220-OM_4_120*\
   OR_4_327)*(PO_4_220+RL_4_227-s.dpt[2,12])
#
  jdqd4 = Apqp_4_220*(PO_4_220-s.dpt[2,8])+Apqp_4_320*(PO_4_320-s.dpt[3,8])+OR_4_220*OR_4_220+OR_4_320*OR_4_320

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  Jdqd[1] = jdqd1
  Jdqd[2] = jdqd2
  Jdqd[3] = jdqd3
  Jdqd[4] = jdqd4

# ====== END Task 0 ====== 

  

