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
#	==> Generation Date : Mon Mar 16 18:21:54 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 18
#
#	==> Function : F18 : Constraints Quadratic Velocity Terms (Jdqd)
#	==> Flops complexity : 104
#
#	==> Generation Time :  0.000 seconds
#	==> Post-Processing :  0.010 seconds
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

  RL_1_214 = s.dpt[2,21]*C13
  RL_1_314 = s.dpt[2,21]*S13
  PO_1_214 = RL_1_214+s.dpt[2,9]
  PO_1_314 = RL_1_314+s.dpt[3,9]
  RL_1_220 = -s.dpt[3,24]*S13p14
  RL_1_320 = s.dpt[3,24]*C13p14

# = = Block_0_1_0_0_0_5 = = 
 
# Trigonometric Variables  

#
  S16p17 = C16*S17+S16*C17
  C16p17 = C16*C17-S16*S17
 
# Constraints and Constraints Jacobian 

  RL_4_217 = s.dpt[2,27]*C16
  RL_4_317 = s.dpt[2,27]*S16
  PO_4_217 = RL_4_217+s.dpt[2,11]
  PO_4_317 = RL_4_317+s.dpt[3,11]
  RL_4_223 = -s.dpt[3,28]*S16p17
  RL_4_323 = s.dpt[3,28]*C16p17

# = = Block_0_2_0_0_0_0 = = 
 
# Constraints Quadratic Terms 

#
  OM_1_114 = qd[13]+qd[14]
  OR_1_214 = -RL_1_314*qd[13]
  OR_1_314 = RL_1_214*qd[13]
  Apqp_1_214 = -OR_1_314*qd[13]
  Apqp_1_314 = OR_1_214*qd[13]
  OR_1_220 = -OM_1_114*RL_1_320
  OR_1_320 = OM_1_114*RL_1_220
  VI_1_220 = OR_1_214+OR_1_220
  VI_1_320 = OR_1_314+OR_1_320
#
  OM_4_117 = qd[16]+qd[17]
  OR_4_217 = -RL_4_317*qd[16]
  OR_4_317 = RL_4_217*qd[16]
  Apqp_4_217 = -OR_4_317*qd[16]
  Apqp_4_317 = OR_4_217*qd[16]
  OR_4_223 = -OM_4_117*RL_4_323
  OR_4_323 = OM_4_117*RL_4_223
  VI_4_223 = OR_4_217+OR_4_223
  VI_4_323 = OR_4_317+OR_4_323

# = = Block_0_2_0_0_0_1 = = 
 
# Constraints Quadratic Terms 

#
  jdqd1 = VI_1_220*VI_1_220+VI_1_320*VI_1_320+(Apqp_1_314+OM_1_114*OR_1_220)*(PO_1_314+RL_1_320)+(Apqp_1_214-OM_1_114*\
   OR_1_320)*(PO_1_214+RL_1_220-s.dpt[2,10])
#
  jdqd2 = Apqp_1_214*(PO_1_214-s.dpt[2,6])+Apqp_1_314*(PO_1_314-s.dpt[3,6])+OR_1_214*OR_1_214+OR_1_314*OR_1_314
#
  jdqd3 = VI_4_223*VI_4_223+VI_4_323*VI_4_323+(Apqp_4_317+OM_4_117*OR_4_223)*(PO_4_317+RL_4_323)+(Apqp_4_217-OM_4_117*\
   OR_4_323)*(PO_4_217+RL_4_223-s.dpt[2,12])
#
  jdqd4 = Apqp_4_217*(PO_4_217-s.dpt[2,8])+Apqp_4_317*(PO_4_317-s.dpt[3,8])+OR_4_217*OR_4_217+OR_4_317*OR_4_317

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  Jdqd[1] = jdqd1
  Jdqd[2] = jdqd2
  Jdqd[3] = jdqd3
  Jdqd[4] = jdqd4

# ====== END Task 0 ====== 

  

