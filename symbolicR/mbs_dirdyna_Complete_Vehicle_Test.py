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
#	==> Generation Date : Sun Mar 15 20:44:09 2020
#
#	==> Project name : Complete_Vehicle_Test
#	==> using XML input file 
#
#	==> Number of joints : 18
#
#	==> Function : F 1 : Direct Dynamics (Semi-Explicit formulation) : RNEA
#	==> Flops complexity : 4527
#
#	==> Generation Time :  0.040 seconds
#	==> Post-Processing :  0.090 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def dirdyna(M, c, s,tsim):
  
  q = s.q
  qd = s.qd
  qdd = s.qdd
  frc = s.frc
  trq = s.trq

# === begin imp_aux === 

# === end imp_aux === 

# ===== BEGIN task 0 ===== 

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

# = = Block_0_0_0_0_0_3 = = 
 
# Trigonometric Variables  

  C10 = np.cos(q[10])
  S10 = np.sin(q[10])
  C11 = np.cos(q[11])
  S11 = np.sin(q[11])
  C12 = np.cos(q[12])
  S12 = np.sin(q[12])

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C13 = np.cos(q[13])
  S13 = np.sin(q[13])
  C14 = np.cos(q[14])
  S14 = np.sin(q[14])
  C15 = np.cos(q[15])
  S15 = np.sin(q[15])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C16 = np.cos(q[16])
  S16 = np.sin(q[16])
  C17 = np.cos(q[17])
  S17 = np.sin(q[17])
  C18 = np.cos(q[18])
  S18 = np.sin(q[18])

# = = Block_0_1_0_0_0_1 = = 
 
# Forward Kinematics 

  AlF24 = -s.g[3]*S4
  AlF34 = -s.g[3]*C4
  OM15 = qd[4]*C5
  OpF15 = -qd[4]*qd[5]*S5
  OpF35 = qd[4]*qd[5]*C5
  AlF15 = -AlF34*S5
  AlF35 = AlF34*C5
  AlM15_2 = S4*S5
  AlM35_2 = -S4*C5
  AlM15_3 = -C4*S5
  AlM35_3 = C4*C5
  OM16 = qd[5]*S6+OM15*C6
  OM26 = qd[5]*C6-OM15*S6
  OM36 = qd[6]+qd[4]*S5
  OpF16 = -(qd[6]*OM15*S6-C6*(OpF15+qd[5]*qd[6]))
  OpF26 = -(qd[6]*OM15*C6+S6*(OpF15+qd[5]*qd[6]))
  BS16 = -(OM26*OM26+OM36*OM36)
  BS26 = OM16*OM26
  BS36 = OM16*OM36
  BS56 = -(OM16*OM16+OM36*OM36)
  BS66 = OM26*OM36
  BS96 = -(OM16*OM16+OM26*OM26)
  BeF26 = BS26-OpF35
  BeF36 = BS36+OpF26
  BeF46 = BS26+OpF35
  BeF66 = BS66-OpF16
  BeF76 = BS36-OpF26
  BeF86 = BS66+OpF16
  AlF16 = AlF15*C6+AlF24*S6
  AlF26 = -(AlF15*S6-AlF24*C6)
  AlM16_1 = C5*C6
  AlM26_1 = -C5*S6
  AlM16_2 = AlM15_2*C6+C4*S6
  AlM26_2 = -(AlM15_2*S6-C4*C6)
  AlM16_3 = AlM15_3*C6+S4*S6
  AlM26_3 = -(AlM15_3*S6-S4*C6)
  OpM16_4 = C5*C6
  OpM26_4 = -C5*S6

# = = Block_0_1_0_1_0_2 = = 
 
# Forward Kinematics 

  OM17 = qd[7]+OM16
  OM27 = OM26*C7+OM36*S7
  OM37 = -(OM26*S7-OM36*C7)
  OpF27 = C7*(OpF26+qd[7]*OM36)+S7*(OpF35-qd[7]*OM26)
  OpF37 = C7*(OpF35-qd[7]*OM26)-S7*(OpF26+qd[7]*OM36)
  BS57 = -(OM17*OM17+OM37*OM37)
  BeF27 = OM17*OM27-OpF37
  BeF87 = OpF16+OM27*OM37
  AlF17 = AlF16+BS16*s.dpt[1,1]+BeF26*s.dpt[2,1]+BeF36*s.dpt[3,1]
  AlF27 = C7*(AlF26+BS56*s.dpt[2,1]+BeF46*s.dpt[1,1]+BeF66*s.dpt[3,1])+S7*(AlF35+BS96*s.dpt[3,1]+BeF76*s.dpt[1,1]+BeF86*\
   s.dpt[2,1])
  AlF37 = C7*(AlF35+BS96*s.dpt[3,1]+BeF76*s.dpt[1,1]+BeF86*s.dpt[2,1])-S7*(AlF26+BS56*s.dpt[2,1]+BeF46*s.dpt[1,1]+BeF66*\
   s.dpt[3,1])
  AlM27_1 = AlM26_1*C7+S5*S7
  AlM37_1 = -(AlM26_1*S7-S5*C7)
  AlM27_2 = AlM26_2*C7+AlM35_2*S7
  AlM37_2 = -(AlM26_2*S7-AlM35_2*C7)
  AlM27_3 = AlM26_3*C7+AlM35_3*S7
  AlM37_3 = -(AlM26_3*S7-AlM35_3*C7)
  OpM27_4 = OpM26_4*C7+S5*S7
  OpM37_4 = -(OpM26_4*S7-S5*C7)
  AlM17_4 = OpM26_4*s.dpt[3,1]-s.dpt[2,1]*S5
  AlM27_4 = -(C7*(OpM16_4*s.dpt[3,1]-s.dpt[1,1]*S5)-S7*(OpM16_4*s.dpt[2,1]-OpM26_4*s.dpt[1,1]))
  AlM37_4 = C7*(OpM16_4*s.dpt[2,1]-OpM26_4*s.dpt[1,1])+S7*(OpM16_4*s.dpt[3,1]-s.dpt[1,1]*S5)
  OpM27_5 = C6*C7
  OpM37_5 = -C6*S7
  AlM17_5 = s.dpt[3,1]*C6
  AlM27_5 = -(s.dpt[3,1]*S6*C7+S7*(s.dpt[1,1]*C6-s.dpt[2,1]*S6))
  AlM37_5 = s.dpt[3,1]*S6*S7-C7*(s.dpt[1,1]*C6-s.dpt[2,1]*S6)
  AlM27_6 = s.dpt[1,1]*C7
  AlM37_6 = -s.dpt[1,1]*S7
  OM18 = OM17*C8+OM27*S8
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OpF18 = C8*(OpF16+qd[8]*OM27)+S8*(OpF27-qd[8]*OM17)
  AlF18 = C8*(AlF17+BeF27*s.dpt[2,13])+S8*(AlF27+BS57*s.dpt[2,13])
  AlF28 = C8*(AlF27+BS57*s.dpt[2,13])-S8*(AlF17+BeF27*s.dpt[2,13])
  AlF38 = AlF37+BeF87*s.dpt[2,13]
  AlM18_1 = AlM16_1*C8+AlM27_1*S8
  AlM28_1 = -(AlM16_1*S8-AlM27_1*C8)
  AlM18_2 = AlM16_2*C8+AlM27_2*S8
  AlM28_2 = -(AlM16_2*S8-AlM27_2*C8)
  AlM18_3 = AlM16_3*C8+AlM27_3*S8
  AlM28_3 = -(AlM16_3*S8-AlM27_3*C8)
  OpM18_4 = OpM16_4*C8+OpM27_4*S8
  AlM18_4 = AlM27_4*S8+C8*(AlM17_4-OpM37_4*s.dpt[2,13])
  AlM28_4 = AlM27_4*C8-S8*(AlM17_4-OpM37_4*s.dpt[2,13])
  AlM38_4 = AlM37_4+OpM16_4*s.dpt[2,13]
  OpM18_5 = OpM27_5*S8+S6*C8
  AlM18_5 = AlM27_5*S8+C8*(AlM17_5-OpM37_5*s.dpt[2,13])
  AlM28_5 = AlM27_5*C8-S8*(AlM17_5-OpM37_5*s.dpt[2,13])
  AlM38_5 = AlM37_5+s.dpt[2,13]*S6
  OpM18_6 = S7*S8
  AlM18_6 = AlM27_6*S8-C8*(s.dpt[2,1]+s.dpt[2,13]*C7)
  AlM28_6 = AlM27_6*C8+S8*(s.dpt[2,1]+s.dpt[2,13]*C7)
  OM19 = qd[9]+OM18

# = = Block_0_1_0_1_0_3 = = 
 
# Forward Kinematics 

  OM110 = qd[10]+OM16
  OM210 = OM26*C10+OM36*S10
  OM310 = -(OM26*S10-OM36*C10)
  OpF210 = C10*(OpF26+qd[10]*OM36)+S10*(OpF35-qd[10]*OM26)
  OpF310 = C10*(OpF35-qd[10]*OM26)-S10*(OpF26+qd[10]*OM36)
  BS510 = -(OM110*OM110+OM310*OM310)
  BeF210 = OM110*OM210-OpF310
  BeF810 = OpF16+OM210*OM310
  AlF110 = AlF16+BS16*s.dpt[1,4]+BeF26*s.dpt[2,4]+BeF36*s.dpt[3,4]
  AlF210 = C10*(AlF26+BS56*s.dpt[2,4]+BeF46*s.dpt[1,4]+BeF66*s.dpt[3,4])+S10*(AlF35+BS96*s.dpt[3,4]+BeF76*s.dpt[1,4]+\
   BeF86*s.dpt[2,4])
  AlF310 = C10*(AlF35+BS96*s.dpt[3,4]+BeF76*s.dpt[1,4]+BeF86*s.dpt[2,4])-S10*(AlF26+BS56*s.dpt[2,4]+BeF46*s.dpt[1,4]+\
   BeF66*s.dpt[3,4])
  AlM210_1 = AlM26_1*C10+S10*S5
  AlM310_1 = -(AlM26_1*S10-C10*S5)
  AlM210_2 = AlM26_2*C10+AlM35_2*S10
  AlM310_2 = -(AlM26_2*S10-AlM35_2*C10)
  AlM210_3 = AlM26_3*C10+AlM35_3*S10
  AlM310_3 = -(AlM26_3*S10-AlM35_3*C10)
  OpM210_4 = OpM26_4*C10+S10*S5
  OpM310_4 = -(OpM26_4*S10-C10*S5)
  AlM110_4 = OpM26_4*s.dpt[3,4]-s.dpt[2,4]*S5
  AlM210_4 = -(C10*(OpM16_4*s.dpt[3,4]-s.dpt[1,4]*S5)-S10*(OpM16_4*s.dpt[2,4]-OpM26_4*s.dpt[1,4]))
  AlM310_4 = C10*(OpM16_4*s.dpt[2,4]-OpM26_4*s.dpt[1,4])+S10*(OpM16_4*s.dpt[3,4]-s.dpt[1,4]*S5)
  OpM210_5 = C10*C6
  OpM310_5 = -S10*C6
  AlM110_5 = s.dpt[3,4]*C6
  AlM210_5 = -(s.dpt[3,4]*C10*S6+S10*(s.dpt[1,4]*C6-s.dpt[2,4]*S6))
  AlM310_5 = s.dpt[3,4]*S10*S6-C10*(s.dpt[1,4]*C6-s.dpt[2,4]*S6)
  AlM210_6 = s.dpt[1,4]*C10
  AlM310_6 = -s.dpt[1,4]*S10
  OM111 = OM110*C11+OM210*S11
  OM211 = -(OM110*S11-OM210*C11)
  OM311 = qd[11]+OM310
  OpF111 = C11*(OpF16+qd[11]*OM210)+S11*(OpF210-qd[11]*OM110)
  AlF111 = C11*(AlF110+BeF210*s.dpt[2,17])+S11*(AlF210+BS510*s.dpt[2,17])
  AlF211 = C11*(AlF210+BS510*s.dpt[2,17])-S11*(AlF110+BeF210*s.dpt[2,17])
  AlF311 = AlF310+BeF810*s.dpt[2,17]
  AlM111_1 = AlM16_1*C11+AlM210_1*S11
  AlM211_1 = -(AlM16_1*S11-AlM210_1*C11)
  AlM111_2 = AlM16_2*C11+AlM210_2*S11
  AlM211_2 = -(AlM16_2*S11-AlM210_2*C11)
  AlM111_3 = AlM16_3*C11+AlM210_3*S11
  AlM211_3 = -(AlM16_3*S11-AlM210_3*C11)
  OpM111_4 = OpM16_4*C11+OpM210_4*S11
  AlM111_4 = AlM210_4*S11+C11*(AlM110_4-OpM310_4*s.dpt[2,17])
  AlM211_4 = AlM210_4*C11-S11*(AlM110_4-OpM310_4*s.dpt[2,17])
  AlM311_4 = AlM310_4+OpM16_4*s.dpt[2,17]
  OpM111_5 = OpM210_5*S11+C11*S6
  AlM111_5 = AlM210_5*S11+C11*(AlM110_5-OpM310_5*s.dpt[2,17])
  AlM211_5 = AlM210_5*C11-S11*(AlM110_5-OpM310_5*s.dpt[2,17])
  AlM311_5 = AlM310_5+s.dpt[2,17]*S6
  OpM111_6 = S10*S11
  AlM111_6 = AlM210_6*S11-C11*(s.dpt[2,4]+s.dpt[2,17]*C10)
  AlM211_6 = AlM210_6*C11+S11*(s.dpt[2,4]+s.dpt[2,17]*C10)
  OM112 = qd[12]+OM111

# = = Block_0_1_0_1_0_4 = = 
 
# Trigonometric Variables  

  C13p14 = C13*C14-S13*S14
  S13p14 = C13*S14+S13*C14
  C13p14p15 = C13p14*C15-S13p14*S15
  S13p14p15 = C13p14*S15+S13p14*C15
 
# Forward Kinematics 

  OM113 = qd[13]+OM16
  OM213 = OM26*C13+OM36*S13
  OM313 = -(OM26*S13-OM36*C13)
  OpF213 = C13*(OpF26+qd[13]*OM36)+S13*(OpF35-qd[13]*OM26)
  OpF313 = C13*(OpF35-qd[13]*OM26)-S13*(OpF26+qd[13]*OM36)
  BS513 = -(OM113*OM113+OM313*OM313)
  BeF213 = OM113*OM213-OpF313
  BeF813 = OpF16+OM213*OM313
  AlF113 = AlF16+BS16*s.dpt[1,9]+BeF26*s.dpt[2,9]+BeF36*s.dpt[3,9]
  AlF213 = C13*(AlF26+BS56*s.dpt[2,9]+BeF46*s.dpt[1,9]+BeF66*s.dpt[3,9])+S13*(AlF35+BS96*s.dpt[3,9]+BeF76*s.dpt[1,9]+\
   BeF86*s.dpt[2,9])
  AlF313 = C13*(AlF35+BS96*s.dpt[3,9]+BeF76*s.dpt[1,9]+BeF86*s.dpt[2,9])-S13*(AlF26+BS56*s.dpt[2,9]+BeF46*s.dpt[1,9]+\
   BeF66*s.dpt[3,9])
  AlM213_1 = AlM26_1*C13+S13*S5
  AlM313_1 = -(AlM26_1*S13-C13*S5)
  AlM213_2 = AlM26_2*C13+AlM35_2*S13
  AlM313_2 = -(AlM26_2*S13-AlM35_2*C13)
  AlM213_3 = AlM26_3*C13+AlM35_3*S13
  AlM313_3 = -(AlM26_3*S13-AlM35_3*C13)
  OpM213_4 = OpM26_4*C13+S13*S5
  OpM313_4 = -(OpM26_4*S13-C13*S5)
  AlM113_4 = OpM26_4*s.dpt[3,9]-s.dpt[2,9]*S5
  AlM213_4 = -(C13*(OpM16_4*s.dpt[3,9]-s.dpt[1,9]*S5)-S13*(OpM16_4*s.dpt[2,9]-OpM26_4*s.dpt[1,9]))
  AlM313_4 = C13*(OpM16_4*s.dpt[2,9]-OpM26_4*s.dpt[1,9])+S13*(OpM16_4*s.dpt[3,9]-s.dpt[1,9]*S5)
  OpM313_5 = -S13*C6
  AlM113_5 = s.dpt[3,9]*C6
  AlM213_5 = -(s.dpt[3,9]*C13*S6+S13*(s.dpt[1,9]*C6-s.dpt[2,9]*S6))
  AlM313_5 = s.dpt[3,9]*S13*S6-C13*(s.dpt[1,9]*C6-s.dpt[2,9]*S6)
  OM114 = qd[14]+OM113
  OM214 = OM213*C14+OM313*S14
  OM314 = -(OM213*S14-OM313*C14)
  BS114 = -(OM214*OM214+OM314*OM314)
  BeF414 = OM114*OM214+C14*(OpF313-qd[14]*OM213)-S14*(OpF213+qd[14]*OM313)
  BeF714 = OM114*OM314-C14*(OpF213+qd[14]*OM313)-S14*(OpF313-qd[14]*OM213)
  AlF114 = AlF113+BeF213*s.dpt[2,21]
  AlF214 = C14*(AlF213+BS513*s.dpt[2,21])+S14*(AlF313+BeF813*s.dpt[2,21])
  AlF314 = C14*(AlF313+BeF813*s.dpt[2,21])-S14*(AlF213+BS513*s.dpt[2,21])
  AlM214_1 = AlM213_1*C14+AlM313_1*S14
  AlM314_1 = -(AlM213_1*S14-AlM313_1*C14)
  AlM214_2 = AlM213_2*C14+AlM313_2*S14
  AlM314_2 = -(AlM213_2*S14-AlM313_2*C14)
  AlM214_3 = AlM213_3*C14+AlM313_3*S14
  AlM314_3 = -(AlM213_3*S14-AlM313_3*C14)
  OpM214_4 = OpM213_4*C14+OpM313_4*S14
  OpM314_4 = -(OpM213_4*S14-OpM313_4*C14)
  AlM114_4 = AlM113_4-OpM313_4*s.dpt[2,21]
  AlM214_4 = AlM213_4*C14+S14*(AlM313_4+OpM16_4*s.dpt[2,21])
  AlM314_4 = -(AlM213_4*S14-C14*(AlM313_4+OpM16_4*s.dpt[2,21]))
  OpM214_5 = C13p14*C6
  OpM314_5 = -S13p14*C6
  AlM114_5 = AlM113_5-OpM313_5*s.dpt[2,21]
  AlM214_5 = AlM213_5*C14+S14*(AlM313_5+s.dpt[2,21]*S6)
  AlM314_5 = -(AlM213_5*S14-C14*(AlM313_5+s.dpt[2,21]*S6))
  AlM114_6 = -(s.dpt[2,9]+s.dpt[2,21]*C13)
  OM115 = qd[15]+OM114

# = = Block_0_1_0_1_0_5 = = 
 
# Trigonometric Variables  

  C16p17 = C16*C17-S16*S17
  S16p17 = C16*S17+S16*C17
  C16p17p18 = C16p17*C18-S16p17*S18
  S16p17p18 = C16p17*S18+S16p17*C18
 
# Forward Kinematics 

  OM116 = qd[16]+OM16
  OM216 = OM26*C16+OM36*S16
  OM316 = -(OM26*S16-OM36*C16)
  OpF216 = C16*(OpF26+qd[16]*OM36)+S16*(OpF35-qd[16]*OM26)
  OpF316 = C16*(OpF35-qd[16]*OM26)-S16*(OpF26+qd[16]*OM36)
  BS516 = -(OM116*OM116+OM316*OM316)
  BeF216 = OM116*OM216-OpF316
  BeF816 = OpF16+OM216*OM316
  AlF116 = AlF16+BS16*s.dpt[1,11]+BeF26*s.dpt[2,11]+BeF36*s.dpt[3,11]
  AlF216 = C16*(AlF26+BS56*s.dpt[2,11]+BeF46*s.dpt[1,11]+BeF66*s.dpt[3,11])+S16*(AlF35+BS96*s.dpt[3,11]+BeF76*\
   s.dpt[1,11]+BeF86*s.dpt[2,11])
  AlF316 = C16*(AlF35+BS96*s.dpt[3,11]+BeF76*s.dpt[1,11]+BeF86*s.dpt[2,11])-S16*(AlF26+BS56*s.dpt[2,11]+BeF46*\
   s.dpt[1,11]+BeF66*s.dpt[3,11])
  AlM216_1 = AlM26_1*C16+S16*S5
  AlM316_1 = -(AlM26_1*S16-C16*S5)
  AlM216_2 = AlM26_2*C16+AlM35_2*S16
  AlM316_2 = -(AlM26_2*S16-AlM35_2*C16)
  AlM216_3 = AlM26_3*C16+AlM35_3*S16
  AlM316_3 = -(AlM26_3*S16-AlM35_3*C16)
  OpM216_4 = OpM26_4*C16+S16*S5
  OpM316_4 = -(OpM26_4*S16-C16*S5)
  AlM116_4 = OpM26_4*s.dpt[3,11]-s.dpt[2,11]*S5
  AlM216_4 = -(C16*(OpM16_4*s.dpt[3,11]-s.dpt[1,11]*S5)-S16*(OpM16_4*s.dpt[2,11]-OpM26_4*s.dpt[1,11]))
  AlM316_4 = C16*(OpM16_4*s.dpt[2,11]-OpM26_4*s.dpt[1,11])+S16*(OpM16_4*s.dpt[3,11]-s.dpt[1,11]*S5)
  OpM316_5 = -S16*C6
  AlM116_5 = s.dpt[3,11]*C6
  AlM216_5 = -(s.dpt[3,11]*C16*S6+S16*(s.dpt[1,11]*C6-s.dpt[2,11]*S6))
  AlM316_5 = s.dpt[3,11]*S16*S6-C16*(s.dpt[1,11]*C6-s.dpt[2,11]*S6)
  OM117 = qd[17]+OM116
  OM217 = OM216*C17+OM316*S17
  OM317 = -(OM216*S17-OM316*C17)
  BS117 = -(OM217*OM217+OM317*OM317)
  BeF417 = OM117*OM217+C17*(OpF316-qd[17]*OM216)-S17*(OpF216+qd[17]*OM316)
  BeF717 = OM117*OM317-C17*(OpF216+qd[17]*OM316)-S17*(OpF316-qd[17]*OM216)
  AlF117 = AlF116+BeF216*s.dpt[2,27]
  AlF217 = C17*(AlF216+BS516*s.dpt[2,27])+S17*(AlF316+BeF816*s.dpt[2,27])
  AlF317 = C17*(AlF316+BeF816*s.dpt[2,27])-S17*(AlF216+BS516*s.dpt[2,27])
  AlM217_1 = AlM216_1*C17+AlM316_1*S17
  AlM317_1 = -(AlM216_1*S17-AlM316_1*C17)
  AlM217_2 = AlM216_2*C17+AlM316_2*S17
  AlM317_2 = -(AlM216_2*S17-AlM316_2*C17)
  AlM217_3 = AlM216_3*C17+AlM316_3*S17
  AlM317_3 = -(AlM216_3*S17-AlM316_3*C17)
  OpM217_4 = OpM216_4*C17+OpM316_4*S17
  OpM317_4 = -(OpM216_4*S17-OpM316_4*C17)
  AlM117_4 = AlM116_4-OpM316_4*s.dpt[2,27]
  AlM217_4 = AlM216_4*C17+S17*(AlM316_4+OpM16_4*s.dpt[2,27])
  AlM317_4 = -(AlM216_4*S17-C17*(AlM316_4+OpM16_4*s.dpt[2,27]))
  OpM217_5 = C16p17*C6
  OpM317_5 = -S16p17*C6
  AlM117_5 = AlM116_5-OpM316_5*s.dpt[2,27]
  AlM217_5 = AlM216_5*C17+S17*(AlM316_5+s.dpt[2,27]*S6)
  AlM317_5 = -(AlM216_5*S17-C17*(AlM316_5+s.dpt[2,27]*S6))
  AlM117_6 = -(s.dpt[2,11]+s.dpt[2,27]*C16)
  OM118 = qd[18]+OM117

# = = Block_0_2_0_1_0_2 = = 
 
# Backward Dynamics 

  FA29 = -(s.frc[2,9]-s.m[9]*(AlF28*C9+AlF38*S9))
  FA39 = -(s.frc[3,9]+s.m[9]*(AlF28*S9-AlF38*C9))
  CF19 = -(s.trq[1,9]-s.In[1,9]*OpF18)
  CF29 = -(s.trq[2,9]+s.In[1,9]*OM19*(OM28*S9-OM38*C9))
  CF39 = -(s.trq[3,9]+s.In[1,9]*OM19*(OM28*C9+OM38*S9))
  FB29_1 = s.m[9]*(AlM28_1*C9+AlM37_1*S9)
  FB39_1 = -s.m[9]*(AlM28_1*S9-AlM37_1*C9)
  FB29_2 = s.m[9]*(AlM28_2*C9+AlM37_2*S9)
  FB39_2 = -s.m[9]*(AlM28_2*S9-AlM37_2*C9)
  FB29_3 = s.m[9]*(AlM28_3*C9+AlM37_3*S9)
  FB39_3 = -s.m[9]*(AlM28_3*S9-AlM37_3*C9)
  FB29_4 = s.m[9]*(AlM28_4*C9+AlM38_4*S9)
  FB39_4 = -s.m[9]*(AlM28_4*S9-AlM38_4*C9)
  CM19_4 = s.In[1,9]*OpM18_4
  FB29_5 = s.m[9]*(AlM28_5*C9+AlM38_5*S9)
  FB39_5 = -s.m[9]*(AlM28_5*S9-AlM38_5*C9)
  CM19_5 = s.In[1,9]*OpM18_5
  FB29_6 = s.m[9]*(AlM28_6*C9+AlM37_6*S9)
  FB39_6 = -s.m[9]*(AlM28_6*S9-AlM37_6*C9)
  CM19_6 = s.In[1,9]*OpM18_6
  CM19_7 = s.In[1,9]*C8
  FA18 = -(s.frc[1,8]-s.m[8]*(AlF18+s.l[3,8]*(OM18*OM38+C8*(OpF27-qd[8]*OM17)-S8*(OpF16+qd[8]*OM27))))
  FA28 = -(s.frc[2,8]-s.m[8]*(AlF28-s.l[3,8]*(OpF18-OM28*OM38)))
  FF18 = -(s.frc[1,9]-FA18-s.m[9]*AlF18)
  FF28 = FA28+FA29*C9-FA39*S9
  FF38 = -(s.frc[3,8]-s.m[8]*(AlF38-s.l[3,8]*(OM18*OM18+OM28*OM28))-FA29*S9-FA39*C9)
  CF18 = -(s.trq[1,8]-CF19-s.In[1,8]*OpF18-s.In[9,8]*OM28*OM38+FA28*s.l[3,8])
  CF28 = -(s.trq[2,8]-CF29*C9+CF39*S9-FA18*s.l[3,8]-OM18*OM38*(s.In[1,8]-s.In[9,8]))
  CF38 = -(s.trq[3,8]+s.In[1,8]*OM18*OM28-s.In[9,8]*OpF37-CF29*S9-CF39*C9)
  FB18_1 = s.m[8]*AlM18_1
  FB28_1 = s.m[8]*AlM28_1
  FM18_1 = FB18_1+s.m[9]*AlM18_1
  FM28_1 = FB28_1+FB29_1*C9-FB39_1*S9
  FM38_1 = s.m[8]*AlM37_1+FB29_1*S9+FB39_1*C9
  CM18_1 = -FB28_1*s.l[3,8]
  CM28_1 = FB18_1*s.l[3,8]
  FB18_2 = s.m[8]*AlM18_2
  FB28_2 = s.m[8]*AlM28_2
  FM18_2 = FB18_2+s.m[9]*AlM18_2
  FM28_2 = FB28_2+FB29_2*C9-FB39_2*S9
  FM38_2 = s.m[8]*AlM37_2+FB29_2*S9+FB39_2*C9
  CM18_2 = -FB28_2*s.l[3,8]
  CM28_2 = FB18_2*s.l[3,8]
  FB18_3 = s.m[8]*AlM18_3
  FB28_3 = s.m[8]*AlM28_3
  FM18_3 = FB18_3+s.m[9]*AlM18_3
  FM28_3 = FB28_3+FB29_3*C9-FB39_3*S9
  FM38_3 = s.m[8]*AlM37_3+FB29_3*S9+FB39_3*C9
  CM18_3 = -FB28_3*s.l[3,8]
  CM28_3 = FB18_3*s.l[3,8]
  FB18_4 = s.m[8]*(AlM18_4-s.l[3,8]*(OpM16_4*S8-OpM27_4*C8))
  FB28_4 = s.m[8]*(AlM28_4-OpM18_4*s.l[3,8])
  FM18_4 = FB18_4+s.m[9]*AlM18_4
  FM28_4 = FB28_4+FB29_4*C9-FB39_4*S9
  FM38_4 = s.m[8]*AlM38_4+FB29_4*S9+FB39_4*C9
  CM18_4 = CM19_4+s.In[1,8]*OpM18_4-FB28_4*s.l[3,8]
  CM28_4 = FB18_4*s.l[3,8]
  CM38_4 = s.In[9,8]*OpM37_4
  FB18_5 = s.m[8]*(AlM18_5+s.l[3,8]*(OpM27_5*C8-S6*S8))
  FB28_5 = s.m[8]*(AlM28_5-OpM18_5*s.l[3,8])
  FM18_5 = FB18_5+s.m[9]*AlM18_5
  FM28_5 = FB28_5+FB29_5*C9-FB39_5*S9
  FM38_5 = s.m[8]*AlM38_5+FB29_5*S9+FB39_5*C9
  CM18_5 = CM19_5+s.In[1,8]*OpM18_5-FB28_5*s.l[3,8]
  CM28_5 = FB18_5*s.l[3,8]
  CM38_5 = s.In[9,8]*OpM37_5
  FB18_6 = s.m[8]*(AlM18_6+s.l[3,8]*S7*C8)
  FB28_6 = s.m[8]*(AlM28_6-OpM18_6*s.l[3,8])
  FM18_6 = FB18_6+s.m[9]*AlM18_6
  FM28_6 = FB28_6+FB29_6*C9-FB39_6*S9
  FM38_6 = s.m[8]*AlM37_6+FB29_6*S9+FB39_6*C9
  CM18_6 = CM19_6+s.In[1,8]*OpM18_6-FB28_6*s.l[3,8]
  CM28_6 = FB18_6*s.l[3,8]
  CM38_6 = s.In[9,8]*C7
  FA17 = -(s.frc[1,7]-s.m[7]*(AlF17+BeF27*s.l[2,7]))
  FA37 = -(s.frc[3,7]-s.m[7]*(AlF37+BeF87*s.l[2,7]))
  FF17 = FA17+FF18*C8-FF28*S8
  FF27 = -(s.frc[2,7]-s.m[7]*(AlF27+BS57*s.l[2,7])-FF18*S8-FF28*C8)
  FF37 = FA37+FF38
  CF17 = -(s.trq[1,7]-s.In[1,7]*OpF16-CF18*C8+CF28*S8-FA37*s.l[2,7]-FF38*s.dpt[2,13])
  CF27 = -(s.trq[2,7]-s.In[1,7]*OM17*OM37-CF18*S8-CF28*C8)
  CF37 = -(s.trq[3,7]-CF38+s.In[1,7]*OM17*OM27+FA17*s.l[2,7]+s.dpt[2,13]*(FF18*C8-FF28*S8))
  FB17_1 = s.m[7]*AlM16_1
  FB37_1 = s.m[7]*AlM37_1
  FM17_1 = FB17_1+FM18_1*C8-FM28_1*S8
  FM27_1 = s.m[7]*AlM27_1+FM18_1*S8+FM28_1*C8
  FM37_1 = FB37_1+FM38_1
  CM71_28 = CM18_1*S8+CM28_1*C8
  CM17_1 = CM18_1*C8-CM28_1*S8+FB37_1*s.l[2,7]+FM38_1*s.dpt[2,13]
  CM37_1 = -(FB17_1*s.l[2,7]+s.dpt[2,13]*(FM18_1*C8-FM28_1*S8))
  FB17_2 = s.m[7]*AlM16_2
  FB37_2 = s.m[7]*AlM37_2
  FM17_2 = FB17_2+FM18_2*C8-FM28_2*S8
  FM27_2 = s.m[7]*AlM27_2+FM18_2*S8+FM28_2*C8
  FM37_2 = FB37_2+FM38_2
  CM72_28 = CM18_2*S8+CM28_2*C8
  CM17_2 = CM18_2*C8-CM28_2*S8+FB37_2*s.l[2,7]+FM38_2*s.dpt[2,13]
  CM37_2 = -(FB17_2*s.l[2,7]+s.dpt[2,13]*(FM18_2*C8-FM28_2*S8))
  FB17_3 = s.m[7]*AlM16_3
  FB37_3 = s.m[7]*AlM37_3
  FM17_3 = FB17_3+FM18_3*C8-FM28_3*S8
  FM27_3 = s.m[7]*AlM27_3+FM18_3*S8+FM28_3*C8
  FM37_3 = FB37_3+FM38_3
  CM73_28 = CM18_3*S8+CM28_3*C8
  CM17_3 = CM18_3*C8-CM28_3*S8+FB37_3*s.l[2,7]+FM38_3*s.dpt[2,13]
  CM37_3 = -(FB17_3*s.l[2,7]+s.dpt[2,13]*(FM18_3*C8-FM28_3*S8))
  FB17_4 = s.m[7]*(AlM17_4-OpM37_4*s.l[2,7])
  FB37_4 = s.m[7]*(AlM37_4+OpM16_4*s.l[2,7])
  FM17_4 = FB17_4+FM18_4*C8-FM28_4*S8
  FM27_4 = s.m[7]*AlM27_4+FM18_4*S8+FM28_4*C8
  FM37_4 = FB37_4+FM38_4
  CM74_28 = CM18_4*S8+CM28_4*C8
  CM17_4 = s.In[1,7]*OpM16_4+CM18_4*C8-CM28_4*S8+FB37_4*s.l[2,7]+FM38_4*s.dpt[2,13]
  CM37_4 = CM38_4-FB17_4*s.l[2,7]-s.dpt[2,13]*(FM18_4*C8-FM28_4*S8)
  FB17_5 = s.m[7]*(AlM17_5-OpM37_5*s.l[2,7])
  FB37_5 = s.m[7]*(AlM37_5+s.l[2,7]*S6)
  FM17_5 = FB17_5+FM18_5*C8-FM28_5*S8
  FM27_5 = s.m[7]*AlM27_5+FM18_5*S8+FM28_5*C8
  FM37_5 = FB37_5+FM38_5
  CM75_28 = CM18_5*S8+CM28_5*C8
  CM17_5 = s.In[1,7]*S6+CM18_5*C8-CM28_5*S8+FB37_5*s.l[2,7]+FM38_5*s.dpt[2,13]
  CM37_5 = CM38_5-FB17_5*s.l[2,7]-s.dpt[2,13]*(FM18_5*C8-FM28_5*S8)
  FB17_6 = -s.m[7]*(s.dpt[2,1]+s.l[2,7]*C7)
  FB37_6 = s.m[7]*AlM37_6
  CM17_6 = CM18_6*C8-CM28_6*S8+FB37_6*s.l[2,7]+FM38_6*s.dpt[2,13]
  CM17_7 = s.In[1,7]+s.m[7]*s.l[2,7]*s.l[2,7]+s.m[8]*s.l[3,8]*s.l[3,8]*S8*S8+s.dpt[2,13]*s.dpt[2,13]*(s.m[8]+s.m[9])+C8*\
   (CM19_7+s.In[1,8]*C8+s.m[8]*s.l[3,8]*s.l[3,8]*C8)

# = = Block_0_2_0_1_0_3 = = 
 
# Backward Dynamics 

  FA212 = -(s.frc[2,12]-s.m[12]*(AlF211*C12+AlF311*S12))
  FA312 = -(s.frc[3,12]+s.m[12]*(AlF211*S12-AlF311*C12))
  CF112 = -(s.trq[1,12]-s.In[1,12]*OpF111)
  CF212 = -(s.trq[2,12]+s.In[1,12]*OM112*(OM211*S12-OM311*C12))
  CF312 = -(s.trq[3,12]+s.In[1,12]*OM112*(OM211*C12+OM311*S12))
  FB212_1 = s.m[12]*(AlM211_1*C12+AlM310_1*S12)
  FB312_1 = -s.m[12]*(AlM211_1*S12-AlM310_1*C12)
  FB212_2 = s.m[12]*(AlM211_2*C12+AlM310_2*S12)
  FB312_2 = -s.m[12]*(AlM211_2*S12-AlM310_2*C12)
  FB212_3 = s.m[12]*(AlM211_3*C12+AlM310_3*S12)
  FB312_3 = -s.m[12]*(AlM211_3*S12-AlM310_3*C12)
  FB212_4 = s.m[12]*(AlM211_4*C12+AlM311_4*S12)
  FB312_4 = -s.m[12]*(AlM211_4*S12-AlM311_4*C12)
  CM112_4 = s.In[1,12]*OpM111_4
  FB212_5 = s.m[12]*(AlM211_5*C12+AlM311_5*S12)
  FB312_5 = -s.m[12]*(AlM211_5*S12-AlM311_5*C12)
  CM112_5 = s.In[1,12]*OpM111_5
  FB212_6 = s.m[12]*(AlM211_6*C12+AlM310_6*S12)
  FB312_6 = -s.m[12]*(AlM211_6*S12-AlM310_6*C12)
  CM112_6 = s.In[1,12]*OpM111_6
  CM112_10 = s.In[1,12]*C11
  FA111 = -(s.frc[1,11]-s.m[11]*(AlF111+s.l[3,11]*(OM111*OM311+C11*(OpF210-qd[11]*OM110)-S11*(OpF16+qd[11]*OM210))))
  FA211 = -(s.frc[2,11]-s.m[11]*(AlF211-s.l[3,11]*(OpF111-OM211*OM311)))
  FF111 = -(s.frc[1,12]-FA111-s.m[12]*AlF111)
  FF211 = FA211+FA212*C12-FA312*S12
  FF311 = -(s.frc[3,11]-s.m[11]*(AlF311-s.l[3,11]*(OM111*OM111+OM211*OM211))-FA212*S12-FA312*C12)
  CF111 = -(s.trq[1,11]-CF112-s.In[1,11]*OpF111-s.In[9,11]*OM211*OM311+FA211*s.l[3,11])
  CF211 = -(s.trq[2,11]-CF212*C12+CF312*S12-FA111*s.l[3,11]-OM111*OM311*(s.In[1,11]-s.In[9,11]))
  CF311 = -(s.trq[3,11]+s.In[1,11]*OM111*OM211-s.In[9,11]*OpF310-CF212*S12-CF312*C12)
  FB111_1 = s.m[11]*AlM111_1
  FB211_1 = s.m[11]*AlM211_1
  FM111_1 = FB111_1+s.m[12]*AlM111_1
  FM211_1 = FB211_1+FB212_1*C12-FB312_1*S12
  FM311_1 = s.m[11]*AlM310_1+FB212_1*S12+FB312_1*C12
  CM111_1 = -FB211_1*s.l[3,11]
  CM211_1 = FB111_1*s.l[3,11]
  FB111_2 = s.m[11]*AlM111_2
  FB211_2 = s.m[11]*AlM211_2
  FM111_2 = FB111_2+s.m[12]*AlM111_2
  FM211_2 = FB211_2+FB212_2*C12-FB312_2*S12
  FM311_2 = s.m[11]*AlM310_2+FB212_2*S12+FB312_2*C12
  CM111_2 = -FB211_2*s.l[3,11]
  CM211_2 = FB111_2*s.l[3,11]
  FB111_3 = s.m[11]*AlM111_3
  FB211_3 = s.m[11]*AlM211_3
  FM111_3 = FB111_3+s.m[12]*AlM111_3
  FM211_3 = FB211_3+FB212_3*C12-FB312_3*S12
  FM311_3 = s.m[11]*AlM310_3+FB212_3*S12+FB312_3*C12
  CM111_3 = -FB211_3*s.l[3,11]
  CM211_3 = FB111_3*s.l[3,11]
  FB111_4 = s.m[11]*(AlM111_4-s.l[3,11]*(OpM16_4*S11-OpM210_4*C11))
  FB211_4 = s.m[11]*(AlM211_4-OpM111_4*s.l[3,11])
  FM111_4 = FB111_4+s.m[12]*AlM111_4
  FM211_4 = FB211_4+FB212_4*C12-FB312_4*S12
  FM311_4 = s.m[11]*AlM311_4+FB212_4*S12+FB312_4*C12
  CM111_4 = CM112_4+s.In[1,11]*OpM111_4-FB211_4*s.l[3,11]
  CM211_4 = FB111_4*s.l[3,11]
  CM311_4 = s.In[9,11]*OpM310_4
  FB111_5 = s.m[11]*(AlM111_5+s.l[3,11]*(OpM210_5*C11-S11*S6))
  FB211_5 = s.m[11]*(AlM211_5-OpM111_5*s.l[3,11])
  FM111_5 = FB111_5+s.m[12]*AlM111_5
  FM211_5 = FB211_5+FB212_5*C12-FB312_5*S12
  FM311_5 = s.m[11]*AlM311_5+FB212_5*S12+FB312_5*C12
  CM111_5 = CM112_5+s.In[1,11]*OpM111_5-FB211_5*s.l[3,11]
  CM211_5 = FB111_5*s.l[3,11]
  CM311_5 = s.In[9,11]*OpM310_5
  FB111_6 = s.m[11]*(AlM111_6+s.l[3,11]*S10*C11)
  FB211_6 = s.m[11]*(AlM211_6-OpM111_6*s.l[3,11])
  FM111_6 = FB111_6+s.m[12]*AlM111_6
  FM211_6 = FB211_6+FB212_6*C12-FB312_6*S12
  FM311_6 = s.m[11]*AlM310_6+FB212_6*S12+FB312_6*C12
  CM111_6 = CM112_6+s.In[1,11]*OpM111_6-FB211_6*s.l[3,11]
  CM211_6 = FB111_6*s.l[3,11]
  CM311_6 = s.In[9,11]*C10
  FA110 = -(s.frc[1,10]-s.m[10]*(AlF110+BeF210*s.l[2,10]))
  FA310 = -(s.frc[3,10]-s.m[10]*(AlF310+BeF810*s.l[2,10]))
  FF110 = FA110+FF111*C11-FF211*S11
  FF210 = -(s.frc[2,10]-s.m[10]*(AlF210+BS510*s.l[2,10])-FF111*S11-FF211*C11)
  FF310 = FA310+FF311
  CF110 = -(s.trq[1,10]-s.In[1,10]*OpF16-CF111*C11+CF211*S11-FA310*s.l[2,10]-FF311*s.dpt[2,17])
  CF210 = -(s.trq[2,10]-s.In[1,10]*OM110*OM310-CF111*S11-CF211*C11)
  CF310 = -(s.trq[3,10]-CF311+s.In[1,10]*OM110*OM210+FA110*s.l[2,10]+s.dpt[2,17]*(FF111*C11-FF211*S11))
  FB110_1 = s.m[10]*AlM16_1
  FB310_1 = s.m[10]*AlM310_1
  FM110_1 = FB110_1+FM111_1*C11-FM211_1*S11
  FM210_1 = s.m[10]*AlM210_1+FM111_1*S11+FM211_1*C11
  FM310_1 = FB310_1+FM311_1
  CM101_211 = CM111_1*S11+CM211_1*C11
  CM110_1 = CM111_1*C11-CM211_1*S11+FB310_1*s.l[2,10]+FM311_1*s.dpt[2,17]
  CM310_1 = -(FB110_1*s.l[2,10]+s.dpt[2,17]*(FM111_1*C11-FM211_1*S11))
  FB110_2 = s.m[10]*AlM16_2
  FB310_2 = s.m[10]*AlM310_2
  FM110_2 = FB110_2+FM111_2*C11-FM211_2*S11
  FM210_2 = s.m[10]*AlM210_2+FM111_2*S11+FM211_2*C11
  FM310_2 = FB310_2+FM311_2
  CM102_211 = CM111_2*S11+CM211_2*C11
  CM110_2 = CM111_2*C11-CM211_2*S11+FB310_2*s.l[2,10]+FM311_2*s.dpt[2,17]
  CM310_2 = -(FB110_2*s.l[2,10]+s.dpt[2,17]*(FM111_2*C11-FM211_2*S11))
  FB110_3 = s.m[10]*AlM16_3
  FB310_3 = s.m[10]*AlM310_3
  FM110_3 = FB110_3+FM111_3*C11-FM211_3*S11
  FM210_3 = s.m[10]*AlM210_3+FM111_3*S11+FM211_3*C11
  FM310_3 = FB310_3+FM311_3
  CM103_211 = CM111_3*S11+CM211_3*C11
  CM110_3 = CM111_3*C11-CM211_3*S11+FB310_3*s.l[2,10]+FM311_3*s.dpt[2,17]
  CM310_3 = -(FB110_3*s.l[2,10]+s.dpt[2,17]*(FM111_3*C11-FM211_3*S11))
  FB110_4 = s.m[10]*(AlM110_4-OpM310_4*s.l[2,10])
  FB310_4 = s.m[10]*(AlM310_4+OpM16_4*s.l[2,10])
  FM110_4 = FB110_4+FM111_4*C11-FM211_4*S11
  FM210_4 = s.m[10]*AlM210_4+FM111_4*S11+FM211_4*C11
  FM310_4 = FB310_4+FM311_4
  CM104_211 = CM111_4*S11+CM211_4*C11
  CM110_4 = s.In[1,10]*OpM16_4+CM111_4*C11-CM211_4*S11+FB310_4*s.l[2,10]+FM311_4*s.dpt[2,17]
  CM310_4 = CM311_4-FB110_4*s.l[2,10]-s.dpt[2,17]*(FM111_4*C11-FM211_4*S11)
  FB110_5 = s.m[10]*(AlM110_5-OpM310_5*s.l[2,10])
  FB310_5 = s.m[10]*(AlM310_5+s.l[2,10]*S6)
  FM110_5 = FB110_5+FM111_5*C11-FM211_5*S11
  FM210_5 = s.m[10]*AlM210_5+FM111_5*S11+FM211_5*C11
  FM310_5 = FB310_5+FM311_5
  CM105_211 = CM111_5*S11+CM211_5*C11
  CM110_5 = s.In[1,10]*S6+CM111_5*C11-CM211_5*S11+FB310_5*s.l[2,10]+FM311_5*s.dpt[2,17]
  CM310_5 = CM311_5-FB110_5*s.l[2,10]-s.dpt[2,17]*(FM111_5*C11-FM211_5*S11)
  FB110_6 = -s.m[10]*(s.dpt[2,4]+s.l[2,10]*C10)
  FB310_6 = s.m[10]*AlM310_6
  CM110_6 = CM111_6*C11-CM211_6*S11+FB310_6*s.l[2,10]+FM311_6*s.dpt[2,17]
  CM110_10 = s.In[1,10]+s.m[10]*s.l[2,10]*s.l[2,10]+s.m[11]*s.l[3,11]*s.l[3,11]*S11*S11+s.dpt[2,17]*s.dpt[2,17]*(s.m[11]\
   +s.m[12])+C11*(CM112_10+s.In[1,11]*C11+s.m[11]*s.l[3,11]*s.l[3,11]*C11)

# = = Block_0_2_0_1_0_4 = = 
 
# Backward Dynamics 

  FA215 = -(s.frc[2,15]-s.m[15]*(C15*(AlF214+BeF414*s.dpt[1,23])+S15*(AlF314+BeF714*s.dpt[1,23])))
  FA315 = -(s.frc[3,15]-s.m[15]*(C15*(AlF314+BeF714*s.dpt[1,23])-S15*(AlF214+BeF414*s.dpt[1,23])))
  CF115 = -(s.trq[1,15]-s.In[1,15]*OpF16)
  CF215 = -(s.trq[2,15]+s.In[1,15]*OM115*(OM214*S15-OM314*C15))
  CF315 = -(s.trq[3,15]+s.In[1,15]*OM115*(OM214*C15+OM314*S15))
  FB215_1 = s.m[15]*(AlM214_1*C15+AlM314_1*S15)
  FB315_1 = -s.m[15]*(AlM214_1*S15-AlM314_1*C15)
  FB215_2 = s.m[15]*(AlM214_2*C15+AlM314_2*S15)
  FB315_2 = -s.m[15]*(AlM214_2*S15-AlM314_2*C15)
  FB215_3 = s.m[15]*(AlM214_3*C15+AlM314_3*S15)
  FB315_3 = -s.m[15]*(AlM214_3*S15-AlM314_3*C15)
  FB215_4 = s.m[15]*(C15*(AlM214_4+OpM314_4*s.dpt[1,23])+S15*(AlM314_4-OpM214_4*s.dpt[1,23]))
  FB315_4 = s.m[15]*(C15*(AlM314_4-OpM214_4*s.dpt[1,23])-S15*(AlM214_4+OpM314_4*s.dpt[1,23]))
  CM115_4 = s.In[1,15]*OpM16_4
  FB215_5 = s.m[15]*(C15*(AlM214_5+OpM314_5*s.dpt[1,23])+S15*(AlM314_5-OpM214_5*s.dpt[1,23]))
  FB315_5 = s.m[15]*(C15*(AlM314_5-OpM214_5*s.dpt[1,23])-S15*(AlM214_5+OpM314_5*s.dpt[1,23]))
  CM115_5 = s.In[1,15]*S6
  FA214 = -(s.frc[2,14]-s.m[14]*(AlF214+BeF414*s.l[1,14]))
  FA314 = -(s.frc[3,14]-s.m[14]*(AlF314+BeF714*s.l[1,14]))
  FF114 = -(s.frc[1,14]+s.frc[1,15]-s.m[14]*(AlF114+BS114*s.l[1,14])-s.m[15]*(AlF114+BS114*s.dpt[1,23]))
  FF214 = FA214+FA215*C15-FA315*S15
  FF314 = FA314+FA215*S15+FA315*C15
  CF114 = -(s.trq[1,14]-CF115-s.In[1,14]*OpF16)
  CF214 = -(s.trq[2,14]-s.In[1,14]*OM114*OM314-CF215*C15+CF315*S15+FA314*s.l[1,14]+s.dpt[1,23]*(FA215*S15+FA315*C15))
  CF314 = -(s.trq[3,14]+s.In[1,14]*OM114*OM214-CF215*S15-CF315*C15-FA214*s.l[1,14]-s.dpt[1,23]*(FA215*C15-FA315*S15))
  FB214_1 = s.m[14]*AlM214_1
  FB314_1 = s.m[14]*AlM314_1
  FM114_1 = AlM16_1*(s.m[14]+s.m[15])
  FM214_1 = FB214_1+FB215_1*C15-FB315_1*S15
  FM314_1 = FB314_1+FB215_1*S15+FB315_1*C15
  CM214_1 = -(FB314_1*s.l[1,14]+s.dpt[1,23]*(FB215_1*S15+FB315_1*C15))
  CM314_1 = FB214_1*s.l[1,14]+s.dpt[1,23]*(FB215_1*C15-FB315_1*S15)
  FB214_2 = s.m[14]*AlM214_2
  FB314_2 = s.m[14]*AlM314_2
  FM114_2 = AlM16_2*(s.m[14]+s.m[15])
  FM214_2 = FB214_2+FB215_2*C15-FB315_2*S15
  FM314_2 = FB314_2+FB215_2*S15+FB315_2*C15
  CM214_2 = -(FB314_2*s.l[1,14]+s.dpt[1,23]*(FB215_2*S15+FB315_2*C15))
  CM314_2 = FB214_2*s.l[1,14]+s.dpt[1,23]*(FB215_2*C15-FB315_2*S15)
  FB214_3 = s.m[14]*AlM214_3
  FB314_3 = s.m[14]*AlM314_3
  FM114_3 = AlM16_3*(s.m[14]+s.m[15])
  FM214_3 = FB214_3+FB215_3*C15-FB315_3*S15
  FM314_3 = FB314_3+FB215_3*S15+FB315_3*C15
  CM214_3 = -(FB314_3*s.l[1,14]+s.dpt[1,23]*(FB215_3*S15+FB315_3*C15))
  CM314_3 = FB214_3*s.l[1,14]+s.dpt[1,23]*(FB215_3*C15-FB315_3*S15)
  FB214_4 = s.m[14]*(AlM214_4+OpM314_4*s.l[1,14])
  FB314_4 = s.m[14]*(AlM314_4-OpM214_4*s.l[1,14])
  FM114_4 = AlM114_4*(s.m[14]+s.m[15])
  FM214_4 = FB214_4+FB215_4*C15-FB315_4*S15
  FM314_4 = FB314_4+FB215_4*S15+FB315_4*C15
  CM114_4 = CM115_4+s.In[1,14]*OpM16_4
  CM214_4 = -(FB314_4*s.l[1,14]+s.dpt[1,23]*(FB215_4*S15+FB315_4*C15))
  CM314_4 = FB214_4*s.l[1,14]+s.dpt[1,23]*(FB215_4*C15-FB315_4*S15)
  FB214_5 = s.m[14]*(AlM214_5+OpM314_5*s.l[1,14])
  FB314_5 = s.m[14]*(AlM314_5-OpM214_5*s.l[1,14])
  FM114_5 = AlM114_5*(s.m[14]+s.m[15])
  FM214_5 = FB214_5+FB215_5*C15-FB315_5*S15
  FM314_5 = FB314_5+FB215_5*S15+FB315_5*C15
  CM114_5 = S6*(s.In[1,14]+s.In[1,15])
  CM214_5 = -(FB314_5*s.l[1,14]+s.dpt[1,23]*(FB215_5*S15+FB315_5*C15))
  CM314_5 = FB214_5*s.l[1,14]+s.dpt[1,23]*(FB215_5*C15-FB315_5*S15)
  FB214_6 = s.m[14]*C13p14*(s.dpt[1,9]+s.l[1,14])
  FB314_6 = -s.m[14]*S13p14*(s.dpt[1,9]+s.l[1,14])
  FM114_6 = AlM114_6*(s.m[14]+s.m[15])
  FM214_6 = FB214_6+s.m[15]*C13p14*(s.dpt[1,23]+s.dpt[1,9])
  FM314_6 = FB314_6-s.m[15]*S13p14*(s.dpt[1,23]+s.dpt[1,9])
  CM214_6 = s.m[15]*s.dpt[1,23]*S13p14*(s.dpt[1,23]+s.dpt[1,9])-FB314_6*s.l[1,14]
  CM314_6 = s.m[15]*s.dpt[1,23]*C13p14*(s.dpt[1,23]+s.dpt[1,9])+FB214_6*s.l[1,14]
  CM114_13 = s.In[1,14]+s.In[1,15]
  CM114_14 = s.In[1,14]+s.In[1,15]
  FA113 = -(s.frc[1,13]-s.m[13]*(AlF113+BeF213*s.l[2,13]))
  FA313 = -(s.frc[3,13]-s.m[13]*(AlF313+BeF813*s.l[2,13]))
  FF113 = FA113+FF114
  FF213 = -(s.frc[2,13]-s.m[13]*(AlF213+BS513*s.l[2,13])-FF214*C14+FF314*S14)
  FF313 = FA313+FF214*S14+FF314*C14
  CF113 = -(s.trq[1,13]-CF114-s.In[1,13]*OpF16-s.In[9,13]*OM213*OM313-FA313*s.l[2,13]-s.dpt[2,21]*(FF214*S14+FF314*C14))
  CF213 = -(s.trq[2,13]-CF214*C14+CF314*S14-OM113*OM313*(s.In[1,13]-s.In[9,13]))
  CF313 = -(s.trq[3,13]+s.In[1,13]*OM113*OM213-s.In[9,13]*OpF313-CF214*S14-CF314*C14+FA113*s.l[2,13]+FF114*s.dpt[2,21])
  FB113_1 = s.m[13]*AlM16_1
  FB313_1 = s.m[13]*AlM313_1
  FM113_1 = FB113_1+FM114_1
  FM213_1 = s.m[13]*AlM213_1+FM214_1*C14-FM314_1*S14
  FM313_1 = FB313_1+FM214_1*S14+FM314_1*C14
  CM131_214 = CM214_1*C14-CM314_1*S14
  CM113_1 = FB313_1*s.l[2,13]+s.dpt[2,21]*(FM214_1*S14+FM314_1*C14)
  CM313_1 = CM214_1*S14+CM314_1*C14-FB113_1*s.l[2,13]-FM114_1*s.dpt[2,21]
  FB113_2 = s.m[13]*AlM16_2
  FB313_2 = s.m[13]*AlM313_2
  FM113_2 = FB113_2+FM114_2
  FM213_2 = s.m[13]*AlM213_2+FM214_2*C14-FM314_2*S14
  FM313_2 = FB313_2+FM214_2*S14+FM314_2*C14
  CM132_214 = CM214_2*C14-CM314_2*S14
  CM113_2 = FB313_2*s.l[2,13]+s.dpt[2,21]*(FM214_2*S14+FM314_2*C14)
  CM313_2 = CM214_2*S14+CM314_2*C14-FB113_2*s.l[2,13]-FM114_2*s.dpt[2,21]
  FB113_3 = s.m[13]*AlM16_3
  FB313_3 = s.m[13]*AlM313_3
  FM113_3 = FB113_3+FM114_3
  FM213_3 = s.m[13]*AlM213_3+FM214_3*C14-FM314_3*S14
  FM313_3 = FB313_3+FM214_3*S14+FM314_3*C14
  CM133_214 = CM214_3*C14-CM314_3*S14
  CM113_3 = FB313_3*s.l[2,13]+s.dpt[2,21]*(FM214_3*S14+FM314_3*C14)
  CM313_3 = CM214_3*S14+CM314_3*C14-FB113_3*s.l[2,13]-FM114_3*s.dpt[2,21]
  FB113_4 = s.m[13]*(AlM113_4-OpM313_4*s.l[2,13])
  FB313_4 = s.m[13]*(AlM313_4+OpM16_4*s.l[2,13])
  FM113_4 = FB113_4+FM114_4
  FM213_4 = s.m[13]*AlM213_4+FM214_4*C14-FM314_4*S14
  FM313_4 = FB313_4+FM214_4*S14+FM314_4*C14
  CM134_214 = CM214_4*C14-CM314_4*S14
  CM113_4 = CM114_4+s.In[1,13]*OpM16_4+FB313_4*s.l[2,13]+s.dpt[2,21]*(FM214_4*S14+FM314_4*C14)
  CM313_4 = s.In[9,13]*OpM313_4+CM214_4*S14+CM314_4*C14-FB113_4*s.l[2,13]-FM114_4*s.dpt[2,21]
  FB113_5 = s.m[13]*(AlM113_5-OpM313_5*s.l[2,13])
  FB313_5 = s.m[13]*(AlM313_5+s.l[2,13]*S6)
  FM113_5 = FB113_5+FM114_5
  FM213_5 = s.m[13]*AlM213_5+FM214_5*C14-FM314_5*S14
  FM313_5 = FB313_5+FM214_5*S14+FM314_5*C14
  CM135_214 = CM214_5*C14-CM314_5*S14
  CM113_5 = CM114_5+s.In[1,13]*S6+FB313_5*s.l[2,13]+s.dpt[2,21]*(FM214_5*S14+FM314_5*C14)
  CM313_5 = s.In[9,13]*OpM313_5+CM214_5*S14+CM314_5*C14-FB113_5*s.l[2,13]-FM114_5*s.dpt[2,21]
  FB113_6 = -s.m[13]*(s.dpt[2,9]+s.l[2,13]*C13)
  FB313_6 = -s.m[13]*s.dpt[1,9]*S13
  CM113_6 = FB313_6*s.l[2,13]+s.dpt[2,21]*(FM214_6*S14+FM314_6*C14)
  CM113_13 = s.In[1,13]+CM114_13+s.m[13]*s.l[2,13]*s.l[2,13]+s.dpt[2,21]*s.dpt[2,21]*(s.m[14]+s.m[15])

# = = Block_0_2_0_1_0_5 = = 
 
# Backward Dynamics 

  FA218 = -(s.frc[2,18]-s.m[18]*(C18*(AlF217+BeF417*s.dpt[1,31])+S18*(AlF317+BeF717*s.dpt[1,31])))
  FA318 = -(s.frc[3,18]-s.m[18]*(C18*(AlF317+BeF717*s.dpt[1,31])-S18*(AlF217+BeF417*s.dpt[1,31])))
  CF118 = -(s.trq[1,18]-s.In[1,18]*OpF16)
  CF218 = -(s.trq[2,18]+s.In[1,18]*OM118*(OM217*S18-OM317*C18))
  CF318 = -(s.trq[3,18]+s.In[1,18]*OM118*(OM217*C18+OM317*S18))
  FB218_1 = s.m[18]*(AlM217_1*C18+AlM317_1*S18)
  FB318_1 = -s.m[18]*(AlM217_1*S18-AlM317_1*C18)
  FB218_2 = s.m[18]*(AlM217_2*C18+AlM317_2*S18)
  FB318_2 = -s.m[18]*(AlM217_2*S18-AlM317_2*C18)
  FB218_3 = s.m[18]*(AlM217_3*C18+AlM317_3*S18)
  FB318_3 = -s.m[18]*(AlM217_3*S18-AlM317_3*C18)
  FB218_4 = s.m[18]*(C18*(AlM217_4+OpM317_4*s.dpt[1,31])+S18*(AlM317_4-OpM217_4*s.dpt[1,31]))
  FB318_4 = s.m[18]*(C18*(AlM317_4-OpM217_4*s.dpt[1,31])-S18*(AlM217_4+OpM317_4*s.dpt[1,31]))
  CM118_4 = s.In[1,18]*OpM16_4
  FB218_5 = s.m[18]*(C18*(AlM217_5+OpM317_5*s.dpt[1,31])+S18*(AlM317_5-OpM217_5*s.dpt[1,31]))
  FB318_5 = s.m[18]*(C18*(AlM317_5-OpM217_5*s.dpt[1,31])-S18*(AlM217_5+OpM317_5*s.dpt[1,31]))
  CM118_5 = s.In[1,18]*S6
  FA217 = -(s.frc[2,17]-s.m[17]*(AlF217+BeF417*s.l[1,17]))
  FA317 = -(s.frc[3,17]-s.m[17]*(AlF317+BeF717*s.l[1,17]))
  FF117 = -(s.frc[1,17]+s.frc[1,18]-s.m[17]*(AlF117+BS117*s.l[1,17])-s.m[18]*(AlF117+BS117*s.dpt[1,31]))
  FF217 = FA217+FA218*C18-FA318*S18
  FF317 = FA317+FA218*S18+FA318*C18
  CF117 = -(s.trq[1,17]-CF118-s.In[1,17]*OpF16)
  CF217 = -(s.trq[2,17]-s.In[1,17]*OM117*OM317-CF218*C18+CF318*S18+FA317*s.l[1,17]+s.dpt[1,31]*(FA218*S18+FA318*C18))
  CF317 = -(s.trq[3,17]+s.In[1,17]*OM117*OM217-CF218*S18-CF318*C18-FA217*s.l[1,17]-s.dpt[1,31]*(FA218*C18-FA318*S18))
  FB217_1 = s.m[17]*AlM217_1
  FB317_1 = s.m[17]*AlM317_1
  FM117_1 = AlM16_1*(s.m[17]+s.m[18])
  FM217_1 = FB217_1+FB218_1*C18-FB318_1*S18
  FM317_1 = FB317_1+FB218_1*S18+FB318_1*C18
  CM217_1 = -(FB317_1*s.l[1,17]+s.dpt[1,31]*(FB218_1*S18+FB318_1*C18))
  CM317_1 = FB217_1*s.l[1,17]+s.dpt[1,31]*(FB218_1*C18-FB318_1*S18)
  FB217_2 = s.m[17]*AlM217_2
  FB317_2 = s.m[17]*AlM317_2
  FM117_2 = AlM16_2*(s.m[17]+s.m[18])
  FM217_2 = FB217_2+FB218_2*C18-FB318_2*S18
  FM317_2 = FB317_2+FB218_2*S18+FB318_2*C18
  CM217_2 = -(FB317_2*s.l[1,17]+s.dpt[1,31]*(FB218_2*S18+FB318_2*C18))
  CM317_2 = FB217_2*s.l[1,17]+s.dpt[1,31]*(FB218_2*C18-FB318_2*S18)
  FB217_3 = s.m[17]*AlM217_3
  FB317_3 = s.m[17]*AlM317_3
  FM117_3 = AlM16_3*(s.m[17]+s.m[18])
  FM217_3 = FB217_3+FB218_3*C18-FB318_3*S18
  FM317_3 = FB317_3+FB218_3*S18+FB318_3*C18
  CM217_3 = -(FB317_3*s.l[1,17]+s.dpt[1,31]*(FB218_3*S18+FB318_3*C18))
  CM317_3 = FB217_3*s.l[1,17]+s.dpt[1,31]*(FB218_3*C18-FB318_3*S18)
  FB217_4 = s.m[17]*(AlM217_4+OpM317_4*s.l[1,17])
  FB317_4 = s.m[17]*(AlM317_4-OpM217_4*s.l[1,17])
  FM117_4 = AlM117_4*(s.m[17]+s.m[18])
  FM217_4 = FB217_4+FB218_4*C18-FB318_4*S18
  FM317_4 = FB317_4+FB218_4*S18+FB318_4*C18
  CM117_4 = CM118_4+s.In[1,17]*OpM16_4
  CM217_4 = -(FB317_4*s.l[1,17]+s.dpt[1,31]*(FB218_4*S18+FB318_4*C18))
  CM317_4 = FB217_4*s.l[1,17]+s.dpt[1,31]*(FB218_4*C18-FB318_4*S18)
  FB217_5 = s.m[17]*(AlM217_5+OpM317_5*s.l[1,17])
  FB317_5 = s.m[17]*(AlM317_5-OpM217_5*s.l[1,17])
  FM117_5 = AlM117_5*(s.m[17]+s.m[18])
  FM217_5 = FB217_5+FB218_5*C18-FB318_5*S18
  FM317_5 = FB317_5+FB218_5*S18+FB318_5*C18
  CM117_5 = S6*(s.In[1,17]+s.In[1,18])
  CM217_5 = -(FB317_5*s.l[1,17]+s.dpt[1,31]*(FB218_5*S18+FB318_5*C18))
  CM317_5 = FB217_5*s.l[1,17]+s.dpt[1,31]*(FB218_5*C18-FB318_5*S18)
  FB217_6 = s.m[17]*C16p17*(s.dpt[1,11]+s.l[1,17])
  FB317_6 = -s.m[17]*S16p17*(s.dpt[1,11]+s.l[1,17])
  FM117_6 = AlM117_6*(s.m[17]+s.m[18])
  FM217_6 = FB217_6+s.m[18]*C16p17*(s.dpt[1,11]+s.dpt[1,31])
  FM317_6 = FB317_6-s.m[18]*S16p17*(s.dpt[1,11]+s.dpt[1,31])
  CM217_6 = s.m[18]*s.dpt[1,31]*S16p17*(s.dpt[1,11]+s.dpt[1,31])-FB317_6*s.l[1,17]
  CM317_6 = s.m[18]*s.dpt[1,31]*C16p17*(s.dpt[1,11]+s.dpt[1,31])+FB217_6*s.l[1,17]
  CM117_16 = s.In[1,17]+s.In[1,18]
  CM117_17 = s.In[1,17]+s.In[1,18]
  FA116 = -(s.frc[1,16]-s.m[16]*(AlF116+BeF216*s.l[2,16]))
  FA316 = -(s.frc[3,16]-s.m[16]*(AlF316+BeF816*s.l[2,16]))
  FF116 = FA116+FF117
  FF216 = -(s.frc[2,16]-s.m[16]*(AlF216+BS516*s.l[2,16])-FF217*C17+FF317*S17)
  FF316 = FA316+FF217*S17+FF317*C17
  CF116 = -(s.trq[1,16]-CF117-s.In[1,16]*OpF16-s.In[9,16]*OM216*OM316-FA316*s.l[2,16]-s.dpt[2,27]*(FF217*S17+FF317*C17))
  CF216 = -(s.trq[2,16]-CF217*C17+CF317*S17-OM116*OM316*(s.In[1,16]-s.In[9,16]))
  CF316 = -(s.trq[3,16]+s.In[1,16]*OM116*OM216-s.In[9,16]*OpF316-CF217*S17-CF317*C17+FA116*s.l[2,16]+FF117*s.dpt[2,27])
  FB116_1 = s.m[16]*AlM16_1
  FB316_1 = s.m[16]*AlM316_1
  FM116_1 = FB116_1+FM117_1
  FM216_1 = s.m[16]*AlM216_1+FM217_1*C17-FM317_1*S17
  FM316_1 = FB316_1+FM217_1*S17+FM317_1*C17
  CM161_217 = CM217_1*C17-CM317_1*S17
  CM116_1 = FB316_1*s.l[2,16]+s.dpt[2,27]*(FM217_1*S17+FM317_1*C17)
  CM316_1 = CM217_1*S17+CM317_1*C17-FB116_1*s.l[2,16]-FM117_1*s.dpt[2,27]
  FB116_2 = s.m[16]*AlM16_2
  FB316_2 = s.m[16]*AlM316_2
  FM116_2 = FB116_2+FM117_2
  FM216_2 = s.m[16]*AlM216_2+FM217_2*C17-FM317_2*S17
  FM316_2 = FB316_2+FM217_2*S17+FM317_2*C17
  CM162_217 = CM217_2*C17-CM317_2*S17
  CM116_2 = FB316_2*s.l[2,16]+s.dpt[2,27]*(FM217_2*S17+FM317_2*C17)
  CM316_2 = CM217_2*S17+CM317_2*C17-FB116_2*s.l[2,16]-FM117_2*s.dpt[2,27]
  FB116_3 = s.m[16]*AlM16_3
  FB316_3 = s.m[16]*AlM316_3
  FM116_3 = FB116_3+FM117_3
  FM216_3 = s.m[16]*AlM216_3+FM217_3*C17-FM317_3*S17
  FM316_3 = FB316_3+FM217_3*S17+FM317_3*C17
  CM163_217 = CM217_3*C17-CM317_3*S17
  CM116_3 = FB316_3*s.l[2,16]+s.dpt[2,27]*(FM217_3*S17+FM317_3*C17)
  CM316_3 = CM217_3*S17+CM317_3*C17-FB116_3*s.l[2,16]-FM117_3*s.dpt[2,27]
  FB116_4 = s.m[16]*(AlM116_4-OpM316_4*s.l[2,16])
  FB316_4 = s.m[16]*(AlM316_4+OpM16_4*s.l[2,16])
  FM116_4 = FB116_4+FM117_4
  FM216_4 = s.m[16]*AlM216_4+FM217_4*C17-FM317_4*S17
  FM316_4 = FB316_4+FM217_4*S17+FM317_4*C17
  CM164_217 = CM217_4*C17-CM317_4*S17
  CM116_4 = CM117_4+s.In[1,16]*OpM16_4+FB316_4*s.l[2,16]+s.dpt[2,27]*(FM217_4*S17+FM317_4*C17)
  CM316_4 = s.In[9,16]*OpM316_4+CM217_4*S17+CM317_4*C17-FB116_4*s.l[2,16]-FM117_4*s.dpt[2,27]
  FB116_5 = s.m[16]*(AlM116_5-OpM316_5*s.l[2,16])
  FB316_5 = s.m[16]*(AlM316_5+s.l[2,16]*S6)
  FM116_5 = FB116_5+FM117_5
  FM216_5 = s.m[16]*AlM216_5+FM217_5*C17-FM317_5*S17
  FM316_5 = FB316_5+FM217_5*S17+FM317_5*C17
  CM165_217 = CM217_5*C17-CM317_5*S17
  CM116_5 = CM117_5+s.In[1,16]*S6+FB316_5*s.l[2,16]+s.dpt[2,27]*(FM217_5*S17+FM317_5*C17)
  CM316_5 = s.In[9,16]*OpM316_5+CM217_5*S17+CM317_5*C17-FB116_5*s.l[2,16]-FM117_5*s.dpt[2,27]
  FB116_6 = -s.m[16]*(s.dpt[2,11]+s.l[2,16]*C16)
  FB316_6 = -s.m[16]*s.dpt[1,11]*S16
  CM116_6 = FB316_6*s.l[2,16]+s.dpt[2,27]*(FM217_6*S17+FM317_6*C17)
  CM116_16 = s.In[1,16]+CM117_16+s.m[16]*s.l[2,16]*s.l[2,16]+s.dpt[2,27]*s.dpt[2,27]*(s.m[17]+s.m[18])

# = = Block_0_2_0_2_0_1 = = 
 
# Backward Dynamics 

  FA16 = -(s.frc[1,6]-s.m[6]*(AlF16+BeF36*s.l[3,6]))
  FA26 = -(s.frc[2,6]-s.m[6]*(AlF26+BeF66*s.l[3,6]))
  FF16 = FA16+FF110+FF113+FF116+FF17
  FF26 = FA26+FF210*C10+FF213*C13+FF216*C16+FF27*C7-FF310*S10-FF313*S13-FF316*S16-FF37*S7
  FF36 = -(s.frc[3,6]-s.m[6]*(AlF35+BS96*s.l[3,6])-FF210*S10-FF213*S13-FF216*S16-FF27*S7-FF310*C10-FF313*C13-FF316*C16-\
   FF37*C7)
  CF16 = -(s.trq[1,6]-CF110-CF113-CF116-CF17-s.In[1,6]*OpF16+FA26*s.l[3,6]+OM26*OM36*(s.In[5,6]-s.In[9,6])-s.dpt[2,11]*(\
   FF216*S16+FF316*C16)-s.dpt[2,1]*(FF27*S7+FF37*C7)-s.dpt[2,4]*(FF210*S10+FF310*C10)-s.dpt[2,9]*(FF213*S13+FF313*C13)+\
   s.dpt[3,11]*(FF216*C16-FF316*S16)+s.dpt[3,1]*(FF27*C7-FF37*S7)+s.dpt[3,4]*(FF210*C10-FF310*S10)+s.dpt[3,9]*(FF213*C13-FF313*\
   S13))
  CF26 = -(s.trq[2,6]-s.In[5,6]*OpF26-CF210*C10-CF213*C13-CF216*C16-CF27*C7+CF310*S10+CF313*S13+CF316*S16+CF37*S7-FA16*\
   s.l[3,6]-FF110*s.dpt[3,4]-FF113*s.dpt[3,9]-FF116*s.dpt[3,11]-FF17*s.dpt[3,1]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,11]*(\
   FF216*S16+FF316*C16)+s.dpt[1,1]*(FF27*S7+FF37*C7)+s.dpt[1,4]*(FF210*S10+FF310*C10)+s.dpt[1,9]*(FF213*S13+FF313*C13))
  CF36 = -(s.trq[3,6]-s.In[9,6]*OpF35-CF210*S10-CF213*S13-CF216*S16-CF27*S7-CF310*C10-CF313*C13-CF316*C16-CF37*C7+FF110*\
   s.dpt[2,4]+FF113*s.dpt[2,9]+FF116*s.dpt[2,11]+FF17*s.dpt[2,1]+OM16*OM26*(s.In[1,6]-s.In[5,6])-s.dpt[1,11]*(FF216*C16-FF316*\
   S16)-s.dpt[1,1]*(FF27*C7-FF37*S7)-s.dpt[1,4]*(FF210*C10-FF310*S10)-s.dpt[1,9]*(FF213*C13-FF313*S13))
  FB16_1 = s.m[6]*AlM16_1
  FB26_1 = s.m[6]*AlM26_1
  FM16_1 = FB16_1+FM110_1+FM113_1+FM116_1+FM17_1
  FM26_1 = FB26_1+FM210_1*C10+FM213_1*C13+FM216_1*C16+FM27_1*C7-FM310_1*S10-FM313_1*S13-FM316_1*S16-FM37_1*S7
  FM36_1 = s.m[6]*S5+FM210_1*S10+FM213_1*S13+FM216_1*S16+FM27_1*S7+FM310_1*C10+FM313_1*C13+FM316_1*C16+FM37_1*C7
  CM16_1 = CM110_1+CM113_1+CM116_1+CM17_1-FB26_1*s.l[3,6]+s.dpt[2,11]*(FM216_1*S16+FM316_1*C16)+s.dpt[2,1]*(FM27_1*S7+\
   FM37_1*C7)+s.dpt[2,4]*(FM210_1*S10+FM310_1*C10)+s.dpt[2,9]*(FM213_1*S13+FM313_1*C13)-s.dpt[3,11]*(FM216_1*C16-FM316_1*S16)-\
   s.dpt[3,1]*(FM27_1*C7-FM37_1*S7)-s.dpt[3,4]*(FM210_1*C10-FM310_1*S10)-s.dpt[3,9]*(FM213_1*C13-FM313_1*S13)
  CM26_1 = CM101_211*C10+CM131_214*C13+CM161_217*C16-CM310_1*S10-CM313_1*S13-CM316_1*S16-CM37_1*S7+CM71_28*C7+FB16_1*\
   s.l[3,6]+FM110_1*s.dpt[3,4]+FM113_1*s.dpt[3,9]+FM116_1*s.dpt[3,11]+FM17_1*s.dpt[3,1]-s.dpt[1,11]*(FM216_1*S16+FM316_1*C16)-\
   s.dpt[1,1]*(FM27_1*S7+FM37_1*C7)-s.dpt[1,4]*(FM210_1*S10+FM310_1*C10)-s.dpt[1,9]*(FM213_1*S13+FM313_1*C13)
  CM36_1 = CM101_211*S10+CM131_214*S13+CM161_217*S16+CM310_1*C10+CM313_1*C13+CM316_1*C16+CM37_1*C7+CM71_28*S7-FM110_1*\
   s.dpt[2,4]-FM113_1*s.dpt[2,9]-FM116_1*s.dpt[2,11]-FM17_1*s.dpt[2,1]+s.dpt[1,11]*(FM216_1*C16-FM316_1*S16)+s.dpt[1,1]*(FM27_1\
   *C7-FM37_1*S7)+s.dpt[1,4]*(FM210_1*C10-FM310_1*S10)+s.dpt[1,9]*(FM213_1*C13-FM313_1*S13)
  FB16_2 = s.m[6]*AlM16_2
  FB26_2 = s.m[6]*AlM26_2
  FM16_2 = FB16_2+FM110_2+FM113_2+FM116_2+FM17_2
  FM26_2 = FB26_2+FM210_2*C10+FM213_2*C13+FM216_2*C16+FM27_2*C7-FM310_2*S10-FM313_2*S13-FM316_2*S16-FM37_2*S7
  CM16_2 = CM110_2+CM113_2+CM116_2+CM17_2-FB26_2*s.l[3,6]+s.dpt[2,11]*(FM216_2*S16+FM316_2*C16)+s.dpt[2,1]*(FM27_2*S7+\
   FM37_2*C7)+s.dpt[2,4]*(FM210_2*S10+FM310_2*C10)+s.dpt[2,9]*(FM213_2*S13+FM313_2*C13)-s.dpt[3,11]*(FM216_2*C16-FM316_2*S16)-\
   s.dpt[3,1]*(FM27_2*C7-FM37_2*S7)-s.dpt[3,4]*(FM210_2*C10-FM310_2*S10)-s.dpt[3,9]*(FM213_2*C13-FM313_2*S13)
  CM26_2 = CM102_211*C10+CM132_214*C13+CM162_217*C16-CM310_2*S10-CM313_2*S13-CM316_2*S16-CM37_2*S7+CM72_28*C7+FB16_2*\
   s.l[3,6]+FM110_2*s.dpt[3,4]+FM113_2*s.dpt[3,9]+FM116_2*s.dpt[3,11]+FM17_2*s.dpt[3,1]-s.dpt[1,11]*(FM216_2*S16+FM316_2*C16)-\
   s.dpt[1,1]*(FM27_2*S7+FM37_2*C7)-s.dpt[1,4]*(FM210_2*S10+FM310_2*C10)-s.dpt[1,9]*(FM213_2*S13+FM313_2*C13)
  CM36_2 = CM102_211*S10+CM132_214*S13+CM162_217*S16+CM310_2*C10+CM313_2*C13+CM316_2*C16+CM37_2*C7+CM72_28*S7-FM110_2*\
   s.dpt[2,4]-FM113_2*s.dpt[2,9]-FM116_2*s.dpt[2,11]-FM17_2*s.dpt[2,1]+s.dpt[1,11]*(FM216_2*C16-FM316_2*S16)+s.dpt[1,1]*(FM27_2\
   *C7-FM37_2*S7)+s.dpt[1,4]*(FM210_2*C10-FM310_2*S10)+s.dpt[1,9]*(FM213_2*C13-FM313_2*S13)
  FB16_3 = s.m[6]*AlM16_3
  FB26_3 = s.m[6]*AlM26_3
  FM16_3 = FB16_3+FM110_3+FM113_3+FM116_3+FM17_3
  FM26_3 = FB26_3+FM210_3*C10+FM213_3*C13+FM216_3*C16+FM27_3*C7-FM310_3*S10-FM313_3*S13-FM316_3*S16-FM37_3*S7
  CM16_3 = CM110_3+CM113_3+CM116_3+CM17_3-FB26_3*s.l[3,6]+s.dpt[2,11]*(FM216_3*S16+FM316_3*C16)+s.dpt[2,1]*(FM27_3*S7+\
   FM37_3*C7)+s.dpt[2,4]*(FM210_3*S10+FM310_3*C10)+s.dpt[2,9]*(FM213_3*S13+FM313_3*C13)-s.dpt[3,11]*(FM216_3*C16-FM316_3*S16)-\
   s.dpt[3,1]*(FM27_3*C7-FM37_3*S7)-s.dpt[3,4]*(FM210_3*C10-FM310_3*S10)-s.dpt[3,9]*(FM213_3*C13-FM313_3*S13)
  CM26_3 = CM103_211*C10+CM133_214*C13+CM163_217*C16-CM310_3*S10-CM313_3*S13-CM316_3*S16-CM37_3*S7+CM73_28*C7+FB16_3*\
   s.l[3,6]+FM110_3*s.dpt[3,4]+FM113_3*s.dpt[3,9]+FM116_3*s.dpt[3,11]+FM17_3*s.dpt[3,1]-s.dpt[1,11]*(FM216_3*S16+FM316_3*C16)-\
   s.dpt[1,1]*(FM27_3*S7+FM37_3*C7)-s.dpt[1,4]*(FM210_3*S10+FM310_3*C10)-s.dpt[1,9]*(FM213_3*S13+FM313_3*C13)
  CM36_3 = CM103_211*S10+CM133_214*S13+CM163_217*S16+CM310_3*C10+CM313_3*C13+CM316_3*C16+CM37_3*C7+CM73_28*S7-FM110_3*\
   s.dpt[2,4]-FM113_3*s.dpt[2,9]-FM116_3*s.dpt[2,11]-FM17_3*s.dpt[2,1]+s.dpt[1,11]*(FM216_3*C16-FM316_3*S16)+s.dpt[1,1]*(FM27_3\
   *C7-FM37_3*S7)+s.dpt[1,4]*(FM210_3*C10-FM310_3*S10)+s.dpt[1,9]*(FM213_3*C13-FM313_3*S13)
  CM16_4 = CM110_4+CM113_4+CM116_4+CM17_4+s.In[1,6]*OpM16_4+s.m[6]*OpM16_4*s.l[3,6]*s.l[3,6]+s.dpt[2,11]*(FM216_4*S16+\
   FM316_4*C16)+s.dpt[2,1]*(FM27_4*S7+FM37_4*C7)+s.dpt[2,4]*(FM210_4*S10+FM310_4*C10)+s.dpt[2,9]*(FM213_4*S13+FM313_4*C13)-\
   s.dpt[3,11]*(FM216_4*C16-FM316_4*S16)-s.dpt[3,1]*(FM27_4*C7-FM37_4*S7)-s.dpt[3,4]*(FM210_4*C10-FM310_4*S10)-s.dpt[3,9]*(\
   FM213_4*C13-FM313_4*S13)
  CM26_4 = CM104_211*C10+CM134_214*C13+CM164_217*C16-CM310_4*S10-CM313_4*S13-CM316_4*S16-CM37_4*S7+CM74_28*C7+FM110_4*\
   s.dpt[3,4]+FM113_4*s.dpt[3,9]+FM116_4*s.dpt[3,11]+FM17_4*s.dpt[3,1]+OpM26_4*(s.In[5,6]+s.m[6]*s.l[3,6]*s.l[3,6])-s.dpt[1,11]\
   *(FM216_4*S16+FM316_4*C16)-s.dpt[1,1]*(FM27_4*S7+FM37_4*C7)-s.dpt[1,4]*(FM210_4*S10+FM310_4*C10)-s.dpt[1,9]*(FM213_4*S13+\
   FM313_4*C13)
  CM36_4 = s.In[9,6]*S5+CM104_211*S10+CM134_214*S13+CM164_217*S16+CM310_4*C10+CM313_4*C13+CM316_4*C16+CM37_4*C7+CM74_28*\
   S7-FM110_4*s.dpt[2,4]-FM113_4*s.dpt[2,9]-FM116_4*s.dpt[2,11]-FM17_4*s.dpt[2,1]+s.dpt[1,11]*(FM216_4*C16-FM316_4*S16)+\
   s.dpt[1,1]*(FM27_4*C7-FM37_4*S7)+s.dpt[1,4]*(FM210_4*C10-FM310_4*S10)+s.dpt[1,9]*(FM213_4*C13-FM313_4*S13)
  CM36_5 = CM105_211*S10+CM135_214*S13+CM165_217*S16+CM310_5*C10+CM313_5*C13+CM316_5*C16+CM37_5*C7+CM75_28*S7-FM110_5*\
   s.dpt[2,4]-FM113_5*s.dpt[2,9]-FM116_5*s.dpt[2,11]-FM17_5*s.dpt[2,1]+s.dpt[1,11]*(FM216_5*C16-FM316_5*S16)+s.dpt[1,1]*(FM27_5\
   *C7-FM37_5*S7)+s.dpt[1,4]*(FM210_5*C10-FM310_5*S10)+s.dpt[1,9]*(FM213_5*C13-FM313_5*S13)
  CM36_6 = s.In[9,6]+s.dpt[1,11]*(C16*(s.m[16]*s.dpt[1,11]*C16+FM217_6*C17-FM317_6*S17)-S16*(FB316_6+FM217_6*S17+FM317_6\
   *C17))+s.dpt[1,1]*(C7*(s.m[7]*AlM27_6+FM18_6*S8+FM28_6*C8)-S7*(FB37_6+FM38_6))+s.dpt[1,4]*(C10*(s.m[10]*AlM210_6+FM111_6*S11\
   +FM211_6*C11)-S10*(FB310_6+FM311_6))+s.dpt[1,9]*(C13*(s.m[13]*s.dpt[1,9]*C13+FM214_6*C14-FM314_6*S14)-S13*(FB313_6+FM214_6*\
   S14+FM314_6*C14))-s.dpt[2,11]*(FB116_6+FM117_6)-s.dpt[2,1]*(FB17_6+FM18_6*C8-FM28_6*S8)-s.dpt[2,4]*(FB110_6+FM111_6*C11-\
   FM211_6*S11)-s.dpt[2,9]*(FB113_6+FM114_6)+C10*(CM311_6-FB110_6*s.l[2,10]-s.dpt[2,17]*(FM111_6*C11-FM211_6*S11))+S10*(CM111_6\
   *S11+CM211_6*C11)+C13*(s.In[9,13]*C13+CM214_6*S14+CM314_6*C14-FB113_6*s.l[2,13]-FM114_6*s.dpt[2,21])+S13*(CM214_6*C14-\
   CM314_6*S14)+C16*(s.In[9,16]*C16+CM217_6*S17+CM317_6*C17-FB116_6*s.l[2,16]-FM117_6*s.dpt[2,27])+S16*(CM217_6*C17-CM317_6*S17\
   )+C7*(CM38_6-FB17_6*s.l[2,7]-s.dpt[2,13]*(FM18_6*C8-FM28_6*S8))+S7*(CM18_6*S8+CM28_6*C8)
  FF5_16 = FF16*C6-FF26*S6
  FF5_26 = FF16*S6+FF26*C6
  CF5_26 = CF16*S6+CF26*C6
  FM51_16 = FM16_1*C6-FM26_1*S6
  FM51_26 = FM16_1*S6+FM26_1*C6
  CM51_26 = CM16_1*S6+CM26_1*C6
  FM52_26 = FM16_2*S6+FM26_2*C6
  CM52_26 = CM16_2*S6+CM26_2*C6
  CM53_26 = CM16_3*S6+CM26_3*C6
  CM54_26 = CM16_4*S6+CM26_4*C6
  CM55_26 = C6*(CM105_211*C10+CM135_214*C13+CM165_217*C16-CM310_5*S10-CM313_5*S13-CM316_5*S16-CM37_5*S7+CM75_28*C7+\
   FM110_5*s.dpt[3,4]+FM113_5*s.dpt[3,9]+FM116_5*s.dpt[3,11]+FM17_5*s.dpt[3,1]-s.dpt[1,11]*(FM216_5*S16+FM316_5*C16)-s.dpt[1,1]\
   *(FM27_5*S7+FM37_5*C7)-s.dpt[1,4]*(FM210_5*S10+FM310_5*C10)-s.dpt[1,9]*(FM213_5*S13+FM313_5*C13)+C6*(s.In[5,6]+s.m[6]*\
   s.l[3,6]*s.l[3,6]))+S6*(CM110_5+CM113_5+CM116_5+CM17_5+s.In[1,6]*S6+s.m[6]*s.l[3,6]*s.l[3,6]*S6+s.dpt[2,11]*(FM216_5*S16+\
   FM316_5*C16)+s.dpt[2,1]*(FM27_5*S7+FM37_5*C7)+s.dpt[2,4]*(FM210_5*S10+FM310_5*C10)+s.dpt[2,9]*(FM213_5*S13+FM313_5*C13)-\
   s.dpt[3,11]*(FM216_5*C16-FM316_5*S16)-s.dpt[3,1]*(FM27_5*C7-FM37_5*S7)-s.dpt[3,4]*(FM210_5*C10-FM310_5*S10)-s.dpt[3,9]*(\
   FM213_5*C13-FM313_5*S13))
  FF4_15 = FF36*S5+FF5_16*C5
  FF4_35 = FF36*C5-FF5_16*S5
  CF4_15 = CF36*S5+C5*(CF16*C6-CF26*S6)
  FM41_15 = FM36_1*S5+FM51_16*C5
  FM41_35 = FM36_1*C5-FM51_16*S5
  CM41_15 = CM36_1*S5+C5*(CM16_1*C6-CM26_1*S6)
  FM42_35 = C5*(s.m[6]*AlM35_2+FM210_2*S10+FM213_2*S13+FM216_2*S16+FM27_2*S7+FM310_2*C10+FM313_2*C13+FM316_2*C16+FM37_2*\
   C7)-S5*(FM16_2*C6-FM26_2*S6)
  CM42_15 = CM36_2*S5+C5*(CM16_2*C6-CM26_2*S6)
  CM43_15 = CM36_3*S5+C5*(CM16_3*C6-CM26_3*S6)
  CM44_15 = CM36_4*S5+C5*(CM16_4*C6-CM26_4*S6)
  FF3_24 = -(FF4_35*S4-FF5_26*C4)
  FF3_34 = FF4_35*C4+FF5_26*S4
  FM31_24 = -(FM41_35*S4-FM51_26*C4)
  FM31_34 = FM41_35*C4+FM51_26*S4
  FM32_24 = -(FM42_35*S4-FM52_26*C4)
  FM32_34 = FM42_35*C4+FM52_26*S4
  FM33_34 = C4*(C5*(s.m[6]*AlM35_3+FM210_3*S10+FM213_3*S13+FM216_3*S16+FM27_3*S7+FM310_3*C10+FM313_3*C13+FM316_3*C16+\
   FM37_3*C7)-S5*(FM16_3*C6-FM26_3*S6))+S4*(FM16_3*S6+FM26_3*C6)

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  M[1,1] = FM41_15
  M[1,2] = FM31_24
  M[1,3] = FM31_34
  M[1,4] = CM41_15
  M[1,5] = CM51_26
  M[1,6] = CM36_1
  M[1,7] = CM17_1
  M[1,10] = CM110_1
  M[1,13] = CM113_1
  M[1,16] = CM116_1
  M[2,1] = FM31_24
  M[2,2] = FM32_24
  M[2,3] = FM32_34
  M[2,4] = CM42_15
  M[2,5] = CM52_26
  M[2,6] = CM36_2
  M[2,7] = CM17_2
  M[2,10] = CM110_2
  M[2,13] = CM113_2
  M[2,16] = CM116_2
  M[3,1] = FM31_34
  M[3,2] = FM32_34
  M[3,3] = FM33_34
  M[3,4] = CM43_15
  M[3,5] = CM53_26
  M[3,6] = CM36_3
  M[3,7] = CM17_3
  M[3,10] = CM110_3
  M[3,13] = CM113_3
  M[3,16] = CM116_3
  M[4,1] = CM41_15
  M[4,2] = CM42_15
  M[4,3] = CM43_15
  M[4,4] = CM44_15
  M[4,5] = CM54_26
  M[4,6] = CM36_4
  M[4,7] = CM17_4
  M[4,8] = CM38_4
  M[4,9] = CM19_4
  M[4,10] = CM110_4
  M[4,11] = CM311_4
  M[4,12] = CM112_4
  M[4,13] = CM113_4
  M[4,14] = CM114_4
  M[4,15] = CM115_4
  M[4,16] = CM116_4
  M[4,17] = CM117_4
  M[4,18] = CM118_4
  M[5,1] = CM51_26
  M[5,2] = CM52_26
  M[5,3] = CM53_26
  M[5,4] = CM54_26
  M[5,5] = CM55_26
  M[5,6] = CM36_5
  M[5,7] = CM17_5
  M[5,8] = CM38_5
  M[5,9] = CM19_5
  M[5,10] = CM110_5
  M[5,11] = CM311_5
  M[5,12] = CM112_5
  M[5,13] = CM113_5
  M[5,14] = CM114_5
  M[5,15] = CM115_5
  M[5,16] = CM116_5
  M[5,17] = CM117_5
  M[5,18] = CM118_5
  M[6,1] = CM36_1
  M[6,2] = CM36_2
  M[6,3] = CM36_3
  M[6,4] = CM36_4
  M[6,5] = CM36_5
  M[6,6] = CM36_6
  M[6,7] = CM17_6
  M[6,8] = CM38_6
  M[6,9] = CM19_6
  M[6,10] = CM110_6
  M[6,11] = CM311_6
  M[6,12] = CM112_6
  M[6,13] = CM113_6
  M[6,16] = CM116_6
  M[7,1] = CM17_1
  M[7,2] = CM17_2
  M[7,3] = CM17_3
  M[7,4] = CM17_4
  M[7,5] = CM17_5
  M[7,6] = CM17_6
  M[7,7] = CM17_7
  M[7,9] = CM19_7
  M[8,4] = CM38_4
  M[8,5] = CM38_5
  M[8,6] = CM38_6
  M[8,8] = s.In[9,8]
  M[9,4] = CM19_4
  M[9,5] = CM19_5
  M[9,6] = CM19_6
  M[9,7] = CM19_7
  M[9,9] = s.In[1,9]
  M[10,1] = CM110_1
  M[10,2] = CM110_2
  M[10,3] = CM110_3
  M[10,4] = CM110_4
  M[10,5] = CM110_5
  M[10,6] = CM110_6
  M[10,10] = CM110_10
  M[10,12] = CM112_10
  M[11,4] = CM311_4
  M[11,5] = CM311_5
  M[11,6] = CM311_6
  M[11,11] = s.In[9,11]
  M[12,4] = CM112_4
  M[12,5] = CM112_5
  M[12,6] = CM112_6
  M[12,10] = CM112_10
  M[12,12] = s.In[1,12]
  M[13,1] = CM113_1
  M[13,2] = CM113_2
  M[13,3] = CM113_3
  M[13,4] = CM113_4
  M[13,5] = CM113_5
  M[13,6] = CM113_6
  M[13,13] = CM113_13
  M[13,14] = CM114_13
  M[13,15] = s.In[1,15]
  M[14,4] = CM114_4
  M[14,5] = CM114_5
  M[14,13] = CM114_13
  M[14,14] = CM114_14
  M[14,15] = s.In[1,15]
  M[15,4] = CM115_4
  M[15,5] = CM115_5
  M[15,13] = s.In[1,15]
  M[15,14] = s.In[1,15]
  M[15,15] = s.In[1,15]
  M[16,1] = CM116_1
  M[16,2] = CM116_2
  M[16,3] = CM116_3
  M[16,4] = CM116_4
  M[16,5] = CM116_5
  M[16,6] = CM116_6
  M[16,16] = CM116_16
  M[16,17] = CM117_16
  M[16,18] = s.In[1,18]
  M[17,4] = CM117_4
  M[17,5] = CM117_5
  M[17,16] = CM117_16
  M[17,17] = CM117_17
  M[17,18] = s.In[1,18]
  M[18,4] = CM118_4
  M[18,5] = CM118_5
  M[18,16] = s.In[1,18]
  M[18,17] = s.In[1,18]
  M[18,18] = s.In[1,18]
  c[1] = FF4_15
  c[2] = FF3_24
  c[3] = FF3_34
  c[4] = CF4_15
  c[5] = CF5_26
  c[6] = CF36
  c[7] = CF17
  c[8] = CF38
  c[9] = CF19
  c[10] = CF110
  c[11] = CF311
  c[12] = CF112
  c[13] = CF113
  c[14] = CF114
  c[15] = CF115
  c[16] = CF116
  c[17] = CF117
  c[18] = CF118

# ====== END Task 0 ====== 

  

