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
#	==> Function : F 1 : Direct Dynamics (Semi-Explicit formulation) : RNEA
#	==> Flops complexity : 10205
#
#	==> Generation Time :  0.110 seconds
#	==> Post-Processing :  0.180 seconds
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
  C10 = np.cos(q[10])
  S10 = np.sin(q[10])

# = = Block_0_0_0_0_0_3 = = 
 
# Trigonometric Variables  

  C11 = np.cos(q[11])
  S11 = np.sin(q[11])

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

# = = Block_0_0_0_0_0_6 = = 
 
# Trigonometric Variables  

  C19 = np.cos(q[19])
  S19 = np.sin(q[19])

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

# = = Block_0_0_0_0_0_9 = = 
 
# Trigonometric Variables  

  C27 = np.cos(q[27])
  S27 = np.sin(q[27])

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

# = = Block_0_0_0_0_0_12 = = 
 
# Trigonometric Variables  

  C35 = np.cos(q[35])
  S35 = np.sin(q[35])

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C37 = np.cos(q[37])
  S37 = np.sin(q[37])
  C38 = np.cos(q[38])
  S38 = np.sin(q[38])

# = = Block_0_1_0_0_0_1 = = 
 
# Forward Kinematics 

  OM35 = qd[4]*C5
  OpF15 = -qd[4]*qd[5]*C5
  OpF35 = -qd[4]*qd[5]*S5
  AlF15 = s.g[3]*S5
  AlF35 = -s.g[3]*C5
  AlM15_1 = C4*C5
  AlM35_1 = C4*S5
  AlM15_2 = S4*C5
  AlM35_2 = S4*S5
  OM16 = qd[6]-qd[4]*S5
  OM26 = qd[5]*C6+OM35*S6
  OM36 = -(qd[5]*S6-OM35*C6)
  OpF26 = qd[6]*OM35*C6+S6*(OpF35-qd[5]*qd[6])
  OpF36 = -(qd[6]*OM35*S6-C6*(OpF35-qd[5]*qd[6]))
  BS16 = -(OM26*OM26+OM36*OM36)
  BS26 = OM16*OM26
  BS36 = OM16*OM36
  BS56 = -(OM16*OM16+OM36*OM36)
  BS66 = OM26*OM36
  BS96 = -(OM16*OM16+OM26*OM26)
  BeF26 = BS26-OpF36
  BeF36 = BS36+OpF26
  BeF46 = BS26+OpF36
  BeF66 = BS66-OpF15
  BeF76 = BS36-OpF26
  BeF86 = BS66+OpF15
  AlF26 = AlF35*S6
  AlF36 = AlF35*C6
  AlM26_1 = AlM35_1*S6-S4*C6
  AlM36_1 = AlM35_1*C6+S4*S6
  AlM26_2 = AlM35_2*S6+C4*C6
  AlM36_2 = AlM35_2*C6-C4*S6
  OpM26_4 = C5*S6
  OpM36_4 = C5*C6

# = = Block_0_1_0_1_0_2 = = 
 
# Trigonometric Variables  

  S6p7 = C6*S7+S6*C7
  C6p7 = C6*C7-S6*S7
 
# Forward Kinematics 

  OM17 = qd[7]+OM16
  OM27 = OM26*C7+OM36*S7
  OM37 = -(OM26*S7-OM36*C7)
  OpF27 = C7*(OpF26+qd[7]*OM36)+S7*(OpF36-qd[7]*OM26)
  OpF37 = C7*(OpF36-qd[7]*OM26)-S7*(OpF26+qd[7]*OM36)
  BS57 = -(OM17*OM17+OM37*OM37)
  BeF27 = OM17*OM27-OpF37
  BeF87 = OpF15+OM27*OM37
  AlF17 = AlF15+BS16*s.dpt[1,1]+BeF26*s.dpt[2,1]+BeF36*s.dpt[3,1]
  AlF27 = C7*(AlF26+BS56*s.dpt[2,1]+BeF46*s.dpt[1,1]+BeF66*s.dpt[3,1])+S7*(AlF36+BS96*s.dpt[3,1]+BeF76*s.dpt[1,1]+BeF86*\
   s.dpt[2,1])
  AlF37 = C7*(AlF36+BS96*s.dpt[3,1]+BeF76*s.dpt[1,1]+BeF86*s.dpt[2,1])-S7*(AlF26+BS56*s.dpt[2,1]+BeF46*s.dpt[1,1]+BeF66*\
   s.dpt[3,1])
  AlM27_1 = AlM26_1*C7+AlM36_1*S7
  AlM37_1 = -(AlM26_1*S7-AlM36_1*C7)
  AlM27_2 = AlM26_2*C7+AlM36_2*S7
  AlM37_2 = -(AlM26_2*S7-AlM36_2*C7)
  AlM27_3 = S6p7*C5
  AlM37_3 = C6p7*C5
  OpM27_4 = S6p7*C5
  OpM37_4 = C6p7*C5
  AlM17_4 = OpM26_4*s.dpt[3,1]-OpM36_4*s.dpt[2,1]
  AlM27_4 = C7*(OpM36_4*s.dpt[1,1]+s.dpt[3,1]*S5)-S7*(OpM26_4*s.dpt[1,1]+s.dpt[2,1]*S5)
  AlM37_4 = -(C7*(OpM26_4*s.dpt[1,1]+s.dpt[2,1]*S5)+S7*(OpM36_4*s.dpt[1,1]+s.dpt[3,1]*S5))
  AlM17_5 = s.dpt[2,1]*S6+s.dpt[3,1]*C6
  AlM27_5 = -s.dpt[1,1]*S6p7
  AlM37_5 = -s.dpt[1,1]*C6p7
  AlM27_6 = s.dpt[2,1]*S7-s.dpt[3,1]*C7
  AlM37_6 = s.dpt[2,1]*C7+s.dpt[3,1]*S7
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OpF18 = C8*(OpF15+qd[8]*OM27)+S8*(OpF27-qd[8]*OM17)
  OpF28 = C8*(OpF27-qd[8]*OM17)-S8*(OpF15+qd[8]*OM27)
  AlF18 = C8*(AlF17+BeF27*s.dpt[2,13])+S8*(AlF27+BS57*s.dpt[2,13])
  AlF28 = C8*(AlF27+BS57*s.dpt[2,13])-S8*(AlF17+BeF27*s.dpt[2,13])
  AlF38 = AlF37+BeF87*s.dpt[2,13]
  AlM18_1 = AlM15_1*C8+AlM27_1*S8
  AlM28_1 = -(AlM15_1*S8-AlM27_1*C8)
  AlM18_2 = AlM15_2*C8+AlM27_2*S8
  AlM28_2 = -(AlM15_2*S8-AlM27_2*C8)
  AlM18_3 = AlM27_3*S8-S5*C8
  AlM28_3 = AlM27_3*C8+S5*S8
  OpM18_4 = OpM27_4*S8-S5*C8
  OpM28_4 = OpM27_4*C8+S5*S8
  AlM18_4 = AlM27_4*S8+C8*(AlM17_4-OpM37_4*s.dpt[2,13])
  AlM28_4 = AlM27_4*C8-S8*(AlM17_4-OpM37_4*s.dpt[2,13])
  AlM38_4 = AlM37_4-s.dpt[2,13]*S5
  OpM18_5 = C6p7*S8
  OpM28_5 = C6p7*C8
  AlM18_5 = AlM27_5*S8+C8*(AlM17_5+s.dpt[2,13]*S6p7)
  AlM28_5 = AlM27_5*C8-S8*(AlM17_5+s.dpt[2,13]*S6p7)
  AlM18_6 = AlM27_6*S8
  AlM28_6 = AlM27_6*C8
  AlM38_6 = AlM37_6+s.dpt[2,13]
  OM19 = qd[9]+OM17*C8+OM27*S8
  OM39 = -(OM28*S9-OM38*C9)
  OpF29 = C9*(OpF28+qd[9]*OM38)+S9*(OpF37-qd[9]*OM28)
  OpF39 = C9*(OpF37-qd[9]*OM28)-S9*(OpF28+qd[9]*OM38)
  AlF29 = AlF28*C9+AlF38*S9
  AlF39 = -(AlF28*S9-AlF38*C9)
  AlM29_1 = AlM28_1*C9+AlM37_1*S9
  AlM39_1 = -(AlM28_1*S9-AlM37_1*C9)
  AlM29_2 = AlM28_2*C9+AlM37_2*S9
  AlM39_2 = -(AlM28_2*S9-AlM37_2*C9)
  AlM29_3 = AlM28_3*C9+AlM37_3*S9
  AlM39_3 = -(AlM28_3*S9-AlM37_3*C9)
  OpM29_4 = OpM28_4*C9+OpM37_4*S9
  OpM39_4 = -(OpM28_4*S9-OpM37_4*C9)
  AlM29_4 = AlM28_4*C9+AlM38_4*S9
  AlM39_4 = -(AlM28_4*S9-AlM38_4*C9)
  OpM29_5 = OpM28_5*C9-S6p7*S9
  OpM39_5 = -(OpM28_5*S9+S6p7*C9)
  AlM29_5 = AlM28_5*C9+AlM37_5*S9
  AlM39_5 = -(AlM28_5*S9-AlM37_5*C9)
  OpM29_6 = -S8*C9
  OpM39_6 = S8*S9
  AlM29_6 = AlM28_6*C9+AlM38_6*S9
  AlM39_6 = -(AlM28_6*S9-AlM38_6*C9)
  OpM29_7 = -S8*C9
  OpM39_7 = S8*S9
  AlM29_7 = s.dpt[2,13]*S9
  AlM39_7 = s.dpt[2,13]*C9
  OM110 = OM19*C10-OM39*S10
  OM210 = qd[10]+OM28*C9+OM38*S9
  OM310 = OM19*S10+OM39*C10
  OpF110 = C10*(OpF18-qd[10]*OM39)-S10*(OpF39+qd[10]*OM19)
  OpF310 = C10*(OpF39+qd[10]*OM19)+S10*(OpF18-qd[10]*OM39)
  BS910 = -(OM110*OM110+OM210*OM210)
  BeF310 = OpF29+OM110*OM310
  BeF610 = OM210*OM310-OpF110
  AlF110 = AlF18*C10-AlF39*S10
  AlF310 = AlF18*S10+AlF39*C10
  AlM110_1 = AlM18_1*C10-AlM39_1*S10
  AlM310_1 = AlM18_1*S10+AlM39_1*C10
  AlM110_2 = AlM18_2*C10-AlM39_2*S10
  AlM310_2 = AlM18_2*S10+AlM39_2*C10
  AlM110_3 = AlM18_3*C10-AlM39_3*S10
  AlM310_3 = AlM18_3*S10+AlM39_3*C10
  OpM110_4 = OpM18_4*C10-OpM39_4*S10
  OpM310_4 = OpM18_4*S10+OpM39_4*C10
  AlM110_4 = AlM18_4*C10-AlM39_4*S10
  AlM310_4 = AlM18_4*S10+AlM39_4*C10
  OpM110_5 = OpM18_5*C10-OpM39_5*S10
  OpM310_5 = OpM18_5*S10+OpM39_5*C10
  AlM110_5 = AlM18_5*C10-AlM39_5*S10
  AlM310_5 = AlM18_5*S10+AlM39_5*C10
  OpM110_6 = -(OpM39_6*S10-C10*C8)
  OpM310_6 = OpM39_6*C10+S10*C8
  AlM110_6 = AlM18_6*C10-AlM39_6*S10
  AlM310_6 = AlM18_6*S10+AlM39_6*C10
  OpM110_7 = -(OpM39_7*S10-C10*C8)
  OpM310_7 = OpM39_7*C10+S10*C8
  AlM110_7 = -AlM39_7*S10
  AlM310_7 = AlM39_7*C10
  OpM110_8 = -S10*C9
  OpM310_8 = C10*C9

# = = Block_0_1_0_1_0_5 = = 
 
# Trigonometric Variables  

  S15p6 = C15*S6+S15*C6
  C15p6 = C15*C6-S15*S6
 
# Forward Kinematics 

  OM115 = qd[15]+OM16
  OM215 = OM26*C15+OM36*S15
  OM315 = -(OM26*S15-OM36*C15)
  OpF215 = C15*(OpF26+qd[15]*OM36)+S15*(OpF36-qd[15]*OM26)
  OpF315 = C15*(OpF36-qd[15]*OM26)-S15*(OpF26+qd[15]*OM36)
  BS515 = -(OM115*OM115+OM315*OM315)
  BeF215 = OM115*OM215-OpF315
  BeF815 = OpF15+OM215*OM315
  AlF115 = AlF15+BS16*s.dpt[1,4]+BeF26*s.dpt[2,4]+BeF36*s.dpt[3,4]
  AlF215 = C15*(AlF26+BS56*s.dpt[2,4]+BeF46*s.dpt[1,4]+BeF66*s.dpt[3,4])+S15*(AlF36+BS96*s.dpt[3,4]+BeF76*s.dpt[1,4]+\
   BeF86*s.dpt[2,4])
  AlF315 = C15*(AlF36+BS96*s.dpt[3,4]+BeF76*s.dpt[1,4]+BeF86*s.dpt[2,4])-S15*(AlF26+BS56*s.dpt[2,4]+BeF46*s.dpt[1,4]+\
   BeF66*s.dpt[3,4])
  AlM215_1 = AlM26_1*C15+AlM36_1*S15
  AlM315_1 = -(AlM26_1*S15-AlM36_1*C15)
  AlM215_2 = AlM26_2*C15+AlM36_2*S15
  AlM315_2 = -(AlM26_2*S15-AlM36_2*C15)
  AlM215_3 = S15p6*C5
  AlM315_3 = C15p6*C5
  OpM215_4 = S15p6*C5
  OpM315_4 = C15p6*C5
  AlM115_4 = OpM26_4*s.dpt[3,4]-OpM36_4*s.dpt[2,4]
  AlM215_4 = C15*(OpM36_4*s.dpt[1,4]+s.dpt[3,4]*S5)-S15*(OpM26_4*s.dpt[1,4]+s.dpt[2,4]*S5)
  AlM315_4 = -(C15*(OpM26_4*s.dpt[1,4]+s.dpt[2,4]*S5)+S15*(OpM36_4*s.dpt[1,4]+s.dpt[3,4]*S5))
  AlM115_5 = s.dpt[2,4]*S6+s.dpt[3,4]*C6
  AlM215_5 = -s.dpt[1,4]*S15p6
  AlM315_5 = -s.dpt[1,4]*C15p6
  AlM215_6 = s.dpt[2,4]*S15-s.dpt[3,4]*C15
  AlM315_6 = s.dpt[2,4]*C15+s.dpt[3,4]*S15
  OM216 = -(OM115*S16-OM215*C16)
  OM316 = qd[16]+OM315
  OpF116 = C16*(OpF15+qd[16]*OM215)+S16*(OpF215-qd[16]*OM115)
  OpF216 = C16*(OpF215-qd[16]*OM115)-S16*(OpF15+qd[16]*OM215)
  AlF116 = C16*(AlF115+BeF215*s.dpt[2,18])+S16*(AlF215+BS515*s.dpt[2,18])
  AlF216 = C16*(AlF215+BS515*s.dpt[2,18])-S16*(AlF115+BeF215*s.dpt[2,18])
  AlF316 = AlF315+BeF815*s.dpt[2,18]
  AlM116_1 = AlM15_1*C16+AlM215_1*S16
  AlM216_1 = -(AlM15_1*S16-AlM215_1*C16)
  AlM116_2 = AlM15_2*C16+AlM215_2*S16
  AlM216_2 = -(AlM15_2*S16-AlM215_2*C16)
  AlM116_3 = AlM215_3*S16-C16*S5
  AlM216_3 = AlM215_3*C16+S16*S5
  OpM116_4 = OpM215_4*S16-C16*S5
  OpM216_4 = OpM215_4*C16+S16*S5
  AlM116_4 = AlM215_4*S16+C16*(AlM115_4-OpM315_4*s.dpt[2,18])
  AlM216_4 = AlM215_4*C16-S16*(AlM115_4-OpM315_4*s.dpt[2,18])
  AlM316_4 = AlM315_4-s.dpt[2,18]*S5
  OpM116_5 = C15p6*S16
  OpM216_5 = C15p6*C16
  AlM116_5 = AlM215_5*S16+C16*(AlM115_5+s.dpt[2,18]*S15p6)
  AlM216_5 = AlM215_5*C16-S16*(AlM115_5+s.dpt[2,18]*S15p6)
  AlM116_6 = AlM215_6*S16
  AlM216_6 = AlM215_6*C16
  AlM316_6 = AlM315_6+s.dpt[2,18]
  OM117 = qd[17]+OM115*C16+OM215*S16
  OM317 = -(OM216*S17-OM316*C17)
  OpF217 = C17*(OpF216+qd[17]*OM316)+S17*(OpF315-qd[17]*OM216)
  OpF317 = C17*(OpF315-qd[17]*OM216)-S17*(OpF216+qd[17]*OM316)
  AlF217 = AlF216*C17+AlF316*S17
  AlF317 = -(AlF216*S17-AlF316*C17)
  AlM217_1 = AlM216_1*C17+AlM315_1*S17
  AlM317_1 = -(AlM216_1*S17-AlM315_1*C17)
  AlM217_2 = AlM216_2*C17+AlM315_2*S17
  AlM317_2 = -(AlM216_2*S17-AlM315_2*C17)
  AlM217_3 = AlM216_3*C17+AlM315_3*S17
  AlM317_3 = -(AlM216_3*S17-AlM315_3*C17)
  OpM217_4 = OpM216_4*C17+OpM315_4*S17
  OpM317_4 = -(OpM216_4*S17-OpM315_4*C17)
  AlM217_4 = AlM216_4*C17+AlM316_4*S17
  AlM317_4 = -(AlM216_4*S17-AlM316_4*C17)
  OpM217_5 = OpM216_5*C17-S15p6*S17
  OpM317_5 = -(OpM216_5*S17+S15p6*C17)
  AlM217_5 = AlM216_5*C17+AlM315_5*S17
  AlM317_5 = -(AlM216_5*S17-AlM315_5*C17)
  OpM217_6 = -S16*C17
  OpM317_6 = S16*S17
  AlM217_6 = AlM216_6*C17+AlM316_6*S17
  AlM317_6 = -(AlM216_6*S17-AlM316_6*C17)
  OpM217_15 = -S16*C17
  OpM317_15 = S16*S17
  AlM217_15 = s.dpt[2,18]*S17
  AlM317_15 = s.dpt[2,18]*C17
  OM118 = OM117*C18-OM317*S18
  OM218 = qd[18]+OM216*C17+OM316*S17
  OM318 = OM117*S18+OM317*C18
  OpF118 = C18*(OpF116-qd[18]*OM317)-S18*(OpF317+qd[18]*OM117)
  OpF318 = C18*(OpF317+qd[18]*OM117)+S18*(OpF116-qd[18]*OM317)
  BS918 = -(OM118*OM118+OM218*OM218)
  BeF318 = OpF217+OM118*OM318
  BeF618 = OM218*OM318-OpF118
  AlF118 = AlF116*C18-AlF317*S18
  AlF318 = AlF116*S18+AlF317*C18
  AlM118_1 = AlM116_1*C18-AlM317_1*S18
  AlM318_1 = AlM116_1*S18+AlM317_1*C18
  AlM118_2 = AlM116_2*C18-AlM317_2*S18
  AlM318_2 = AlM116_2*S18+AlM317_2*C18
  AlM118_3 = AlM116_3*C18-AlM317_3*S18
  AlM318_3 = AlM116_3*S18+AlM317_3*C18
  OpM118_4 = OpM116_4*C18-OpM317_4*S18
  OpM318_4 = OpM116_4*S18+OpM317_4*C18
  AlM118_4 = AlM116_4*C18-AlM317_4*S18
  AlM318_4 = AlM116_4*S18+AlM317_4*C18
  OpM118_5 = OpM116_5*C18-OpM317_5*S18
  OpM318_5 = OpM116_5*S18+OpM317_5*C18
  AlM118_5 = AlM116_5*C18-AlM317_5*S18
  AlM318_5 = AlM116_5*S18+AlM317_5*C18
  OpM118_6 = -(OpM317_6*S18-C16*C18)
  OpM318_6 = OpM317_6*C18+C16*S18
  AlM118_6 = AlM116_6*C18-AlM317_6*S18
  AlM318_6 = AlM116_6*S18+AlM317_6*C18
  OpM118_15 = -(OpM317_15*S18-C16*C18)
  OpM318_15 = OpM317_15*C18+C16*S18
  AlM118_15 = -AlM317_15*S18
  AlM318_15 = AlM317_15*C18
  OpM118_16 = -C17*S18
  OpM318_16 = C17*C18

# = = Block_0_1_0_1_0_8 = = 
 
# Trigonometric Variables  

  S23p6 = C23*S6+S23*C6
  C23p6 = C23*C6-S23*S6
 
# Forward Kinematics 

  OM123 = qd[23]+OM16
  OM223 = OM26*C23+OM36*S23
  OpF223 = C23*(OpF26+qd[23]*OM36)+S23*(OpF36-qd[23]*OM26)
  OpF323 = C23*(OpF36-qd[23]*OM26)-S23*(OpF26+qd[23]*OM36)
  AlF123 = AlF15+BS16*s.dpt[1,10]+BeF26*s.dpt[2,10]
  AlF223 = C23*(AlF26+BS56*s.dpt[2,10]+BeF46*s.dpt[1,10])+S23*(AlF36+BeF76*s.dpt[1,10]+BeF86*s.dpt[2,10])
  AlF323 = C23*(AlF36+BeF76*s.dpt[1,10]+BeF86*s.dpt[2,10])-S23*(AlF26+BS56*s.dpt[2,10]+BeF46*s.dpt[1,10])
  AlM223_1 = AlM26_1*C23+AlM36_1*S23
  AlM323_1 = -(AlM26_1*S23-AlM36_1*C23)
  AlM223_2 = AlM26_2*C23+AlM36_2*S23
  AlM323_2 = -(AlM26_2*S23-AlM36_2*C23)
  AlM223_3 = S23p6*C5
  AlM323_3 = C23p6*C5
  OpM223_4 = S23p6*C5
  OpM323_4 = C23p6*C5
  AlM123_4 = -OpM36_4*s.dpt[2,10]
  AlM223_4 = OpM36_4*s.dpt[1,10]*C23-S23*(OpM26_4*s.dpt[1,10]+s.dpt[2,10]*S5)
  AlM323_4 = -(OpM36_4*s.dpt[1,10]*S23+C23*(OpM26_4*s.dpt[1,10]+s.dpt[2,10]*S5))
  AlM123_5 = s.dpt[2,10]*S6
  AlM223_5 = -s.dpt[1,10]*S23p6
  AlM323_5 = -s.dpt[1,10]*C23p6
  AlM223_6 = s.dpt[2,10]*S23
  AlM323_6 = s.dpt[2,10]*C23
  OM124 = OM123*C24+OM223*S24
  OM224 = -(OM123*S24-OM223*C24)
  OM324 = qd[24]-OM26*S23+OM36*C23
  OpF124 = C24*(OpF15+qd[24]*OM223)+S24*(OpF223-qd[24]*OM123)
  OpF224 = C24*(OpF223-qd[24]*OM123)-S24*(OpF15+qd[24]*OM223)
  BS524 = -(OM124*OM124+OM324*OM324)
  BeF224 = OM124*OM224-OpF323
  BeF824 = OpF124+OM224*OM324
  AlF124 = AlF123*C24+AlF223*S24
  AlF224 = -(AlF123*S24-AlF223*C24)
  AlM124_1 = AlM15_1*C24+AlM223_1*S24
  AlM224_1 = -(AlM15_1*S24-AlM223_1*C24)
  AlM124_2 = AlM15_2*C24+AlM223_2*S24
  AlM224_2 = -(AlM15_2*S24-AlM223_2*C24)
  AlM124_3 = AlM223_3*S24-C24*S5
  AlM224_3 = AlM223_3*C24+S24*S5
  OpM124_4 = OpM223_4*S24-C24*S5
  OpM224_4 = OpM223_4*C24+S24*S5
  AlM124_4 = AlM123_4*C24+AlM223_4*S24
  AlM224_4 = -(AlM123_4*S24-AlM223_4*C24)
  OpM124_5 = C23p6*S24
  OpM224_5 = C23p6*C24
  AlM124_5 = AlM123_5*C24+AlM223_5*S24
  AlM224_5 = -(AlM123_5*S24-AlM223_5*C24)
  AlM124_6 = AlM223_6*S24
  AlM224_6 = AlM223_6*C24
  OM125 = qd[25]+OM124
  OM225 = OM224*C25+OM324*S25
  OpF225 = C25*(OpF224+qd[25]*OM324)+S25*(OpF323-qd[25]*OM224)
  OpF325 = C25*(OpF323-qd[25]*OM224)-S25*(OpF224+qd[25]*OM324)
  AlF125 = AlF124+BeF224*s.dpt[2,23]
  AlF225 = C25*(AlF224+BS524*s.dpt[2,23])+S25*(AlF323+BeF824*s.dpt[2,23])
  AlF325 = C25*(AlF323+BeF824*s.dpt[2,23])-S25*(AlF224+BS524*s.dpt[2,23])
  AlM225_1 = AlM224_1*C25+AlM323_1*S25
  AlM325_1 = -(AlM224_1*S25-AlM323_1*C25)
  AlM225_2 = AlM224_2*C25+AlM323_2*S25
  AlM325_2 = -(AlM224_2*S25-AlM323_2*C25)
  AlM225_3 = AlM224_3*C25+AlM323_3*S25
  AlM325_3 = -(AlM224_3*S25-AlM323_3*C25)
  OpM225_4 = OpM224_4*C25+OpM323_4*S25
  OpM325_4 = -(OpM224_4*S25-OpM323_4*C25)
  AlM125_4 = AlM124_4-OpM323_4*s.dpt[2,23]
  AlM225_4 = AlM224_4*C25+S25*(AlM323_4+OpM124_4*s.dpt[2,23])
  AlM325_4 = -(AlM224_4*S25-C25*(AlM323_4+OpM124_4*s.dpt[2,23]))
  OpM225_5 = OpM224_5*C25-S23p6*S25
  OpM325_5 = -(OpM224_5*S25+S23p6*C25)
  AlM125_5 = AlM124_5+s.dpt[2,23]*S23p6
  AlM225_5 = AlM224_5*C25+S25*(AlM323_5+OpM124_5*s.dpt[2,23])
  AlM325_5 = -(AlM224_5*S25-C25*(AlM323_5+OpM124_5*s.dpt[2,23]))
  OpM225_6 = -S24*C25
  OpM325_6 = S24*S25
  AlM225_6 = AlM224_6*C25+S25*(AlM323_6+s.dpt[2,23]*C24)
  AlM325_6 = -(AlM224_6*S25-C25*(AlM323_6+s.dpt[2,23]*C24))
  OpM225_23 = -S24*C25
  OpM325_23 = S24*S25
  AlM225_23 = s.dpt[2,23]*C24*S25
  AlM325_23 = s.dpt[2,23]*C24*C25
  OM126 = OM125*C26+OM225*S26
  OM226 = -(OM125*S26-OM225*C26)
  OM326 = qd[26]-OM224*S25+OM324*C25
  OpF126 = C26*(OpF124+qd[26]*OM225)+S26*(OpF225-qd[26]*OM125)
  OpF226 = C26*(OpF225-qd[26]*OM125)-S26*(OpF124+qd[26]*OM225)
  BS926 = -(OM126*OM126+OM226*OM226)
  BeF326 = OpF226+OM126*OM326
  BeF626 = OM226*OM326-OpF126
  AlF126 = AlF125*C26+AlF225*S26
  AlF226 = -(AlF125*S26-AlF225*C26)
  AlM126_1 = AlM124_1*C26+AlM225_1*S26
  AlM226_1 = -(AlM124_1*S26-AlM225_1*C26)
  AlM126_2 = AlM124_2*C26+AlM225_2*S26
  AlM226_2 = -(AlM124_2*S26-AlM225_2*C26)
  AlM126_3 = AlM124_3*C26+AlM225_3*S26
  AlM226_3 = -(AlM124_3*S26-AlM225_3*C26)
  OpM126_4 = OpM124_4*C26+OpM225_4*S26
  OpM226_4 = -(OpM124_4*S26-OpM225_4*C26)
  AlM126_4 = AlM125_4*C26+AlM225_4*S26
  AlM226_4 = -(AlM125_4*S26-AlM225_4*C26)
  OpM126_5 = OpM124_5*C26+OpM225_5*S26
  OpM226_5 = -(OpM124_5*S26-OpM225_5*C26)
  AlM126_5 = AlM125_5*C26+AlM225_5*S26
  AlM226_5 = -(AlM125_5*S26-AlM225_5*C26)
  OpM126_6 = OpM225_6*S26+C24*C26
  OpM226_6 = OpM225_6*C26-C24*S26
  AlM126_6 = AlM124_6*C26+AlM225_6*S26
  AlM226_6 = -(AlM124_6*S26-AlM225_6*C26)
  OpM126_23 = OpM225_23*S26+C24*C26
  OpM226_23 = OpM225_23*C26-C24*S26
  AlM126_23 = AlM225_23*S26
  AlM226_23 = AlM225_23*C26
  OpM126_24 = S25*S26
  OpM226_24 = S25*C26
  AlM126_24 = -s.dpt[2,23]*C26
  AlM226_24 = s.dpt[2,23]*S26

# = = Block_0_1_0_1_0_11 = = 
 
# Trigonometric Variables  

  S31p6 = C31*S6+S31*C6
  C31p6 = C31*C6-S31*S6
 
# Forward Kinematics 

  OM131 = qd[31]+OM16
  OM231 = OM26*C31+OM36*S31
  OpF231 = C31*(OpF26+qd[31]*OM36)+S31*(OpF36-qd[31]*OM26)
  OpF331 = C31*(OpF36-qd[31]*OM26)-S31*(OpF26+qd[31]*OM36)
  AlF131 = AlF15+BS16*s.dpt[1,12]+BeF26*s.dpt[2,12]
  AlF231 = C31*(AlF26+BS56*s.dpt[2,12]+BeF46*s.dpt[1,12])+S31*(AlF36+BeF76*s.dpt[1,12]+BeF86*s.dpt[2,12])
  AlF331 = C31*(AlF36+BeF76*s.dpt[1,12]+BeF86*s.dpt[2,12])-S31*(AlF26+BS56*s.dpt[2,12]+BeF46*s.dpt[1,12])
  AlM231_1 = AlM26_1*C31+AlM36_1*S31
  AlM331_1 = -(AlM26_1*S31-AlM36_1*C31)
  AlM231_2 = AlM26_2*C31+AlM36_2*S31
  AlM331_2 = -(AlM26_2*S31-AlM36_2*C31)
  AlM231_3 = S31p6*C5
  AlM331_3 = C31p6*C5
  OpM231_4 = S31p6*C5
  OpM331_4 = C31p6*C5
  AlM131_4 = -OpM36_4*s.dpt[2,12]
  AlM231_4 = OpM36_4*s.dpt[1,12]*C31-S31*(OpM26_4*s.dpt[1,12]+s.dpt[2,12]*S5)
  AlM331_4 = -(OpM36_4*s.dpt[1,12]*S31+C31*(OpM26_4*s.dpt[1,12]+s.dpt[2,12]*S5))
  AlM131_5 = s.dpt[2,12]*S6
  AlM231_5 = -s.dpt[1,12]*S31p6
  AlM331_5 = -s.dpt[1,12]*C31p6
  AlM231_6 = s.dpt[2,12]*S31
  AlM331_6 = s.dpt[2,12]*C31
  OM132 = OM131*C32+OM231*S32
  OM232 = -(OM131*S32-OM231*C32)
  OM332 = qd[32]-OM26*S31+OM36*C31
  OpF132 = C32*(OpF15+qd[32]*OM231)+S32*(OpF231-qd[32]*OM131)
  OpF232 = C32*(OpF231-qd[32]*OM131)-S32*(OpF15+qd[32]*OM231)
  BS532 = -(OM132*OM132+OM332*OM332)
  BeF232 = OM132*OM232-OpF331
  BeF832 = OpF132+OM232*OM332
  AlF132 = AlF131*C32+AlF231*S32
  AlF232 = -(AlF131*S32-AlF231*C32)
  AlM132_1 = AlM15_1*C32+AlM231_1*S32
  AlM232_1 = -(AlM15_1*S32-AlM231_1*C32)
  AlM132_2 = AlM15_2*C32+AlM231_2*S32
  AlM232_2 = -(AlM15_2*S32-AlM231_2*C32)
  AlM132_3 = AlM231_3*S32-C32*S5
  AlM232_3 = AlM231_3*C32+S32*S5
  OpM132_4 = OpM231_4*S32-C32*S5
  OpM232_4 = OpM231_4*C32+S32*S5
  AlM132_4 = AlM131_4*C32+AlM231_4*S32
  AlM232_4 = -(AlM131_4*S32-AlM231_4*C32)
  OpM132_5 = C31p6*S32
  OpM232_5 = C31p6*C32
  AlM132_5 = AlM131_5*C32+AlM231_5*S32
  AlM232_5 = -(AlM131_5*S32-AlM231_5*C32)
  AlM132_6 = AlM231_6*S32
  AlM232_6 = AlM231_6*C32
  OM133 = qd[33]+OM132
  OM233 = OM232*C33+OM332*S33
  OpF233 = C33*(OpF232+qd[33]*OM332)+S33*(OpF331-qd[33]*OM232)
  OpF333 = C33*(OpF331-qd[33]*OM232)-S33*(OpF232+qd[33]*OM332)
  AlF133 = AlF132+BeF232*s.dpt[2,30]
  AlF233 = C33*(AlF232+BS532*s.dpt[2,30])+S33*(AlF331+BeF832*s.dpt[2,30])
  AlF333 = C33*(AlF331+BeF832*s.dpt[2,30])-S33*(AlF232+BS532*s.dpt[2,30])
  AlM233_1 = AlM232_1*C33+AlM331_1*S33
  AlM333_1 = -(AlM232_1*S33-AlM331_1*C33)
  AlM233_2 = AlM232_2*C33+AlM331_2*S33
  AlM333_2 = -(AlM232_2*S33-AlM331_2*C33)
  AlM233_3 = AlM232_3*C33+AlM331_3*S33
  AlM333_3 = -(AlM232_3*S33-AlM331_3*C33)
  OpM233_4 = OpM232_4*C33+OpM331_4*S33
  OpM333_4 = -(OpM232_4*S33-OpM331_4*C33)
  AlM133_4 = AlM132_4-OpM331_4*s.dpt[2,30]
  AlM233_4 = AlM232_4*C33+S33*(AlM331_4+OpM132_4*s.dpt[2,30])
  AlM333_4 = -(AlM232_4*S33-C33*(AlM331_4+OpM132_4*s.dpt[2,30]))
  OpM233_5 = OpM232_5*C33-S31p6*S33
  OpM333_5 = -(OpM232_5*S33+S31p6*C33)
  AlM133_5 = AlM132_5+s.dpt[2,30]*S31p6
  AlM233_5 = AlM232_5*C33+S33*(AlM331_5+OpM132_5*s.dpt[2,30])
  AlM333_5 = -(AlM232_5*S33-C33*(AlM331_5+OpM132_5*s.dpt[2,30]))
  OpM233_6 = -S32*C33
  OpM333_6 = S32*S33
  AlM233_6 = AlM232_6*C33+S33*(AlM331_6+s.dpt[2,30]*C32)
  AlM333_6 = -(AlM232_6*S33-C33*(AlM331_6+s.dpt[2,30]*C32))
  OpM233_31 = -S32*C33
  OpM333_31 = S32*S33
  AlM233_31 = s.dpt[2,30]*C32*S33
  AlM333_31 = s.dpt[2,30]*C32*C33
  OM134 = OM133*C34+OM233*S34
  OM234 = -(OM133*S34-OM233*C34)
  OM334 = qd[34]-OM232*S33+OM332*C33
  OpF134 = C34*(OpF132+qd[34]*OM233)+S34*(OpF233-qd[34]*OM133)
  OpF234 = C34*(OpF233-qd[34]*OM133)-S34*(OpF132+qd[34]*OM233)
  BS934 = -(OM134*OM134+OM234*OM234)
  BeF334 = OpF234+OM134*OM334
  BeF634 = OM234*OM334-OpF134
  AlF134 = AlF133*C34+AlF233*S34
  AlF234 = -(AlF133*S34-AlF233*C34)
  AlM134_1 = AlM132_1*C34+AlM233_1*S34
  AlM234_1 = -(AlM132_1*S34-AlM233_1*C34)
  AlM134_2 = AlM132_2*C34+AlM233_2*S34
  AlM234_2 = -(AlM132_2*S34-AlM233_2*C34)
  AlM134_3 = AlM132_3*C34+AlM233_3*S34
  AlM234_3 = -(AlM132_3*S34-AlM233_3*C34)
  OpM134_4 = OpM132_4*C34+OpM233_4*S34
  OpM234_4 = -(OpM132_4*S34-OpM233_4*C34)
  AlM134_4 = AlM133_4*C34+AlM233_4*S34
  AlM234_4 = -(AlM133_4*S34-AlM233_4*C34)
  OpM134_5 = OpM132_5*C34+OpM233_5*S34
  OpM234_5 = -(OpM132_5*S34-OpM233_5*C34)
  AlM134_5 = AlM133_5*C34+AlM233_5*S34
  AlM234_5 = -(AlM133_5*S34-AlM233_5*C34)
  OpM134_6 = OpM233_6*S34+C32*C34
  OpM234_6 = OpM233_6*C34-C32*S34
  AlM134_6 = AlM132_6*C34+AlM233_6*S34
  AlM234_6 = -(AlM132_6*S34-AlM233_6*C34)
  OpM134_31 = OpM233_31*S34+C32*C34
  OpM234_31 = OpM233_31*C34-C32*S34
  AlM134_31 = AlM233_31*S34
  AlM234_31 = AlM233_31*C34
  OpM134_32 = S33*S34
  OpM234_32 = S33*C34
  AlM134_32 = -s.dpt[2,30]*C34
  AlM234_32 = s.dpt[2,30]*S34

# = = Block_0_1_0_2_0_3 = = 
 
# Forward Kinematics 

  OM111 = qd[11]+OM110
  OM211 = OM210*C11+OM310*S11
  OM311 = -(OM210*S11-OM310*C11)
  OpF211 = C11*(OpF29+qd[11]*OM310)+S11*(OpF310-qd[11]*OM210)
  OpM211_4 = OpM29_4*C11+OpM310_4*S11
  OpM211_5 = OpM29_5*C11+OpM310_5*S11
  OpM211_6 = OpM29_6*C11+OpM310_6*S11
  OpM211_7 = OpM29_7*C11+OpM310_7*S11
  OpM211_8 = OpM310_8*S11+C11*S9
  OpM211_9 = S10*S11

# = = Block_0_1_0_2_0_4 = = 
 
# Forward Kinematics 

  OM113 = qd[13]+OM110
  OM313 = -(OM210*S13-OM310*C13)
  OpF313 = C13*(OpF310-qd[13]*OM210)-S13*(OpF29+qd[13]*OM310)
  AlF313 = -(AlF29*S13-AlF310*C13)
  AlM313_1 = -(AlM29_1*S13-AlM310_1*C13)
  AlM313_2 = -(AlM29_2*S13-AlM310_2*C13)
  AlM313_3 = -(AlM29_3*S13-AlM310_3*C13)
  OpM313_4 = -(OpM29_4*S13-OpM310_4*C13)
  AlM313_4 = -(AlM29_4*S13-AlM310_4*C13)
  OpM313_5 = -(OpM29_5*S13-OpM310_5*C13)
  AlM313_5 = -(AlM29_5*S13-AlM310_5*C13)
  OpM313_6 = -(OpM29_6*S13-OpM310_6*C13)
  AlM313_6 = -(AlM29_6*S13-AlM310_6*C13)
  OpM313_7 = -(OpM29_7*S13-OpM310_7*C13)
  AlM313_7 = -(AlM29_7*S13-AlM310_7*C13)
  OpM313_8 = OpM310_8*C13-S13*S9
  OpM313_9 = S10*C13
  OM114 = OM113*C14-OM313*S14
  OM214 = qd[14]+OM210*C13+OM310*S13
  OM314 = OM113*S14+OM313*C14

# = = Block_0_1_0_2_0_6 = = 
 
# Forward Kinematics 

  OM119 = qd[19]+OM118
  OM219 = OM218*C19+OM318*S19
  OM319 = -(OM218*S19-OM318*C19)
  OpF219 = C19*(OpF217+qd[19]*OM318)+S19*(OpF318-qd[19]*OM218)
  OpM219_4 = OpM217_4*C19+OpM318_4*S19
  OpM219_5 = OpM217_5*C19+OpM318_5*S19
  OpM219_6 = OpM217_6*C19+OpM318_6*S19
  OpM219_15 = OpM217_15*C19+OpM318_15*S19
  OpM219_16 = OpM318_16*S19+S17*C19
  OpM219_17 = S18*S19

# = = Block_0_1_0_2_0_7 = = 
 
# Forward Kinematics 

  OM121 = qd[21]+OM118
  OM321 = -(OM218*S21-OM318*C21)
  OpF321 = C21*(OpF318-qd[21]*OM218)-S21*(OpF217+qd[21]*OM318)
  AlF321 = -(AlF217*S21-AlF318*C21)
  AlM321_1 = -(AlM217_1*S21-AlM318_1*C21)
  AlM321_2 = -(AlM217_2*S21-AlM318_2*C21)
  AlM321_3 = -(AlM217_3*S21-AlM318_3*C21)
  OpM321_4 = -(OpM217_4*S21-OpM318_4*C21)
  AlM321_4 = -(AlM217_4*S21-AlM318_4*C21)
  OpM321_5 = -(OpM217_5*S21-OpM318_5*C21)
  AlM321_5 = -(AlM217_5*S21-AlM318_5*C21)
  OpM321_6 = -(OpM217_6*S21-OpM318_6*C21)
  AlM321_6 = -(AlM217_6*S21-AlM318_6*C21)
  OpM321_15 = -(OpM217_15*S21-OpM318_15*C21)
  AlM321_15 = -(AlM217_15*S21-AlM318_15*C21)
  OpM321_16 = OpM318_16*C21-S17*S21
  OpM321_17 = S18*C21
  OM122 = OM121*C22-OM321*S22
  OM222 = qd[22]+OM218*C21+OM318*S21
  OM322 = OM121*S22+OM321*C22

# = = Block_0_1_0_2_0_9 = = 
 
# Forward Kinematics 

  OM127 = qd[27]+OM126
  OM227 = OM226*C27+OM326*S27
  OM327 = -(OM226*S27-OM326*C27)
  OpF227 = C27*(OpF226+qd[27]*OM326)+S27*(OpF325-qd[27]*OM226)
  OpM227_4 = OpM226_4*C27+OpM325_4*S27
  OpM227_5 = OpM226_5*C27+OpM325_5*S27
  OpM227_6 = OpM226_6*C27+OpM325_6*S27
  OpM227_23 = OpM226_23*C27+OpM325_23*S27
  OpM227_24 = OpM226_24*C27+C25*S27
  OpM227_25 = -S26*C27

# = = Block_0_1_0_2_0_10 = = 
 
# Forward Kinematics 

  OM129 = qd[29]+OM126
  OM329 = -(OM226*S29-OM326*C29)
  OpF329 = C29*(OpF325-qd[29]*OM226)-S29*(OpF226+qd[29]*OM326)
  AlF129 = AlF126+BeF326*s.dpt[3,25]
  AlF329 = C29*(AlF325+BS926*s.dpt[3,25])-S29*(AlF226+BeF626*s.dpt[3,25])
  AlM329_1 = -(AlM226_1*S29-AlM325_1*C29)
  AlM329_2 = -(AlM226_2*S29-AlM325_2*C29)
  AlM329_3 = -(AlM226_3*S29-AlM325_3*C29)
  OpM329_4 = -(OpM226_4*S29-OpM325_4*C29)
  AlM129_4 = AlM126_4+OpM226_4*s.dpt[3,25]
  AlM329_4 = AlM325_4*C29-S29*(AlM226_4-OpM126_4*s.dpt[3,25])
  OpM329_5 = -(OpM226_5*S29-OpM325_5*C29)
  AlM129_5 = AlM126_5+OpM226_5*s.dpt[3,25]
  AlM329_5 = AlM325_5*C29-S29*(AlM226_5-OpM126_5*s.dpt[3,25])
  OpM329_6 = -(OpM226_6*S29-OpM325_6*C29)
  AlM129_6 = AlM126_6+OpM226_6*s.dpt[3,25]
  AlM329_6 = AlM325_6*C29-S29*(AlM226_6-OpM126_6*s.dpt[3,25])
  OpM329_23 = -(OpM226_23*S29-OpM325_23*C29)
  AlM129_23 = AlM126_23+OpM226_23*s.dpt[3,25]
  AlM329_23 = AlM325_23*C29-S29*(AlM226_23-OpM126_23*s.dpt[3,25])
  OpM329_24 = -(OpM226_24*S29-C25*C29)
  AlM129_24 = AlM126_24+OpM226_24*s.dpt[3,25]
  AlM329_24 = -S29*(AlM226_24-OpM126_24*s.dpt[3,25])
  OpM329_25 = S26*S29
  AlM129_25 = -s.dpt[3,25]*S26
  AlM329_25 = s.dpt[3,25]*C26*S29
  OM130 = OM129*C30-OM329*S30
  OM230 = qd[30]+OM226*C29+OM326*S29
  OM330 = OM129*S30+OM329*C30

# = = Block_0_1_0_2_0_12 = = 
 
# Forward Kinematics 

  OM135 = qd[35]+OM134
  OM235 = OM234*C35+OM334*S35
  OM335 = -(OM234*S35-OM334*C35)
  OpF235 = C35*(OpF234+qd[35]*OM334)+S35*(OpF333-qd[35]*OM234)
  OpM235_4 = OpM234_4*C35+OpM333_4*S35
  OpM235_5 = OpM234_5*C35+OpM333_5*S35
  OpM235_6 = OpM234_6*C35+OpM333_6*S35
  OpM235_31 = OpM234_31*C35+OpM333_31*S35
  OpM235_32 = OpM234_32*C35+C33*S35
  OpM235_33 = -S34*C35

# = = Block_0_1_0_2_0_13 = = 
 
# Forward Kinematics 

  OM137 = qd[37]+OM134
  OM337 = -(OM234*S37-OM334*C37)
  OpF337 = C37*(OpF333-qd[37]*OM234)-S37*(OpF234+qd[37]*OM334)
  AlF137 = AlF134+BeF334*s.dpt[3,34]
  AlF337 = C37*(AlF333+BS934*s.dpt[3,34])-S37*(AlF234+BeF634*s.dpt[3,34])
  AlM337_1 = -(AlM234_1*S37-AlM333_1*C37)
  AlM337_2 = -(AlM234_2*S37-AlM333_2*C37)
  AlM337_3 = -(AlM234_3*S37-AlM333_3*C37)
  OpM337_4 = -(OpM234_4*S37-OpM333_4*C37)
  AlM137_4 = AlM134_4+OpM234_4*s.dpt[3,34]
  AlM337_4 = AlM333_4*C37-S37*(AlM234_4-OpM134_4*s.dpt[3,34])
  OpM337_5 = -(OpM234_5*S37-OpM333_5*C37)
  AlM137_5 = AlM134_5+OpM234_5*s.dpt[3,34]
  AlM337_5 = AlM333_5*C37-S37*(AlM234_5-OpM134_5*s.dpt[3,34])
  OpM337_6 = -(OpM234_6*S37-OpM333_6*C37)
  AlM137_6 = AlM134_6+OpM234_6*s.dpt[3,34]
  AlM337_6 = AlM333_6*C37-S37*(AlM234_6-OpM134_6*s.dpt[3,34])
  OpM337_31 = -(OpM234_31*S37-OpM333_31*C37)
  AlM137_31 = AlM134_31+OpM234_31*s.dpt[3,34]
  AlM337_31 = AlM333_31*C37-S37*(AlM234_31-OpM134_31*s.dpt[3,34])
  OpM337_32 = -(OpM234_32*S37-C33*C37)
  AlM137_32 = AlM134_32+OpM234_32*s.dpt[3,34]
  AlM337_32 = -S37*(AlM234_32-OpM134_32*s.dpt[3,34])
  OpM337_33 = S34*S37
  AlM137_33 = -s.dpt[3,34]*S34
  AlM337_33 = s.dpt[3,34]*C34*S37
  OM138 = OM137*C38-OM337*S38
  OM238 = qd[38]+OM234*C37+OM334*S37
  OM338 = OM137*S38+OM337*C38

# = = Block_0_2_0_1_0_3 = = 
 
# Backward Dynamics 

  FA112 = -(s.frc[1,12]-s.m[12]*(AlF110+q[12]*(OpF211+OM111*OM311)+(2.0)*qd[12]*OM211+BeF310*s.dpt[3,14]+s.l[3,12]*(OpF211+\
   OM111*OM311)))
  FA212 = -(s.frc[2,12]+s.m[12]*(q[12]*(OpF110-OM211*OM311)+(2.0)*qd[12]*OM111+s.l[3,12]*(OpF110-OM211*OM311)-C11*(AlF29+\
   BeF610*s.dpt[3,14])-S11*(AlF310+BS910*s.dpt[3,14])))
  FA312 = -(s.frc[3,12]-s.m[12]*(C11*(AlF310+BS910*s.dpt[3,14])-S11*(AlF29+BeF610*s.dpt[3,14])-(q[12]+s.l[3,12])*(OM111*\
   OM111+OM211*OM211)))
  CF312 = -(s.trq[3,12]-s.In[9,12]*(C11*(OpF310-qd[11]*OM210)-S11*(OpF29+qd[11]*OM310))+OM111*OM211*(s.In[1,12]-\
   s.In[5,12]))
  FB112_1 = s.m[12]*AlM110_1
  FB212_1 = s.m[12]*(AlM29_1*C11+AlM310_1*S11)
  FB312_1 = -s.m[12]*(AlM29_1*S11-AlM310_1*C11)
  FB112_2 = s.m[12]*AlM110_2
  FB212_2 = s.m[12]*(AlM29_2*C11+AlM310_2*S11)
  FB312_2 = -s.m[12]*(AlM29_2*S11-AlM310_2*C11)
  FB112_3 = s.m[12]*AlM110_3
  FB212_3 = s.m[12]*(AlM29_3*C11+AlM310_3*S11)
  FB312_3 = -s.m[12]*(AlM29_3*S11-AlM310_3*C11)
  FB112_4 = s.m[12]*(AlM110_4+q[12]*OpM211_4+OpM211_4*s.l[3,12]+OpM29_4*s.dpt[3,14])
  FB212_4 = s.m[12]*(AlM310_4*S11+C11*(AlM29_4-OpM110_4*s.dpt[3,14])-q[12]*OpM110_4-OpM110_4*s.l[3,12])
  FB312_4 = s.m[12]*(AlM310_4*C11-S11*(AlM29_4-OpM110_4*s.dpt[3,14]))
  CM312_4 = -s.In[9,12]*(OpM29_4*S11-OpM310_4*C11)
  FB112_5 = s.m[12]*(AlM110_5+q[12]*OpM211_5+OpM211_5*s.l[3,12]+OpM29_5*s.dpt[3,14])
  FB212_5 = s.m[12]*(AlM310_5*S11+C11*(AlM29_5-OpM110_5*s.dpt[3,14])-q[12]*OpM110_5-OpM110_5*s.l[3,12])
  FB312_5 = s.m[12]*(AlM310_5*C11-S11*(AlM29_5-OpM110_5*s.dpt[3,14]))
  CM312_5 = -s.In[9,12]*(OpM29_5*S11-OpM310_5*C11)
  FB112_6 = s.m[12]*(AlM110_6+q[12]*OpM211_6+OpM211_6*s.l[3,12]+OpM29_6*s.dpt[3,14])
  FB212_6 = s.m[12]*(AlM310_6*S11+C11*(AlM29_6-OpM110_6*s.dpt[3,14])-q[12]*OpM110_6-OpM110_6*s.l[3,12])
  FB312_6 = s.m[12]*(AlM310_6*C11-S11*(AlM29_6-OpM110_6*s.dpt[3,14]))
  CM312_6 = -s.In[9,12]*(OpM29_6*S11-OpM310_6*C11)
  FB112_7 = s.m[12]*(AlM110_7+q[12]*OpM211_7+OpM211_7*s.l[3,12]+OpM29_7*s.dpt[3,14])
  FB212_7 = s.m[12]*(AlM310_7*S11+C11*(AlM29_7-OpM110_7*s.dpt[3,14])-q[12]*OpM110_7-OpM110_7*s.l[3,12])
  FB312_7 = s.m[12]*(AlM310_7*C11-S11*(AlM29_7-OpM110_7*s.dpt[3,14]))
  CM312_7 = -s.In[9,12]*(OpM29_7*S11-OpM310_7*C11)
  FB112_8 = s.m[12]*(OpM211_8*(q[12]+s.l[3,12])+s.dpt[3,14]*S9)
  FB212_8 = -s.m[12]*OpM110_8*(q[12]+s.l[3,12]+s.dpt[3,14]*C11)
  FB312_8 = s.m[12]*OpM110_8*s.dpt[3,14]*S11
  CM312_8 = s.In[9,12]*(OpM310_8*C11-S11*S9)
  FB112_9 = s.m[12]*OpM211_9*(q[12]+s.l[3,12])
  FB212_9 = -s.m[12]*C10*(q[12]+s.l[3,12]+s.dpt[3,14]*C11)
  FB312_9 = s.m[12]*s.dpt[3,14]*C10*S11
  CM312_9 = s.In[9,12]*S10*C11
  FB112_10 = s.m[12]*(s.dpt[3,14]+q[12]*C11+s.l[3,12]*C11)
  FB212_11 = -s.m[12]*(q[12]+s.l[3,12])
  CF11_112 = -(s.trq[1,12]+q[12]*FA212-s.In[1,12]*OpF110+FA212*s.l[3,12]+OM211*OM311*(s.In[5,12]-s.In[9,12]))
  CF11_212 = -(s.trq[2,12]-q[12]*FA112-s.In[5,12]*OpF211-FA112*s.l[3,12]-OM111*OM311*(s.In[1,12]-s.In[9,12]))
  CM111_112 = -FB212_1*(q[12]+s.l[3,12])
  CM111_212 = FB112_1*(q[12]+s.l[3,12])
  CM112_112 = -FB212_2*(q[12]+s.l[3,12])
  CM112_212 = FB112_2*(q[12]+s.l[3,12])
  CM113_112 = -FB212_3*(q[12]+s.l[3,12])
  CM113_212 = FB112_3*(q[12]+s.l[3,12])
  CM114_112 = s.In[1,12]*OpM110_4-FB212_4*s.l[3,12]-q[12]*FB212_4
  CM114_212 = q[12]*FB112_4+s.In[5,12]*OpM211_4+FB112_4*s.l[3,12]
  CM115_112 = s.In[1,12]*OpM110_5-FB212_5*s.l[3,12]-q[12]*FB212_5
  CM115_212 = q[12]*FB112_5+s.In[5,12]*OpM211_5+FB112_5*s.l[3,12]
  CM116_112 = s.In[1,12]*OpM110_6-FB212_6*s.l[3,12]-q[12]*FB212_6
  CM116_212 = q[12]*FB112_6+s.In[5,12]*OpM211_6+FB112_6*s.l[3,12]
  CM117_112 = s.In[1,12]*OpM110_7-FB212_7*s.l[3,12]-q[12]*FB212_7
  CM117_212 = q[12]*FB112_7+s.In[5,12]*OpM211_7+FB112_7*s.l[3,12]
  CM118_112 = s.In[1,12]*OpM110_8-FB212_8*s.l[3,12]-q[12]*FB212_8
  CM118_212 = q[12]*FB112_8+s.In[5,12]*OpM211_8+FB112_8*s.l[3,12]
  CM119_112 = s.In[1,12]*C10-FB212_9*s.l[3,12]-q[12]*FB212_9
  CM119_212 = q[12]*FB112_9+s.In[5,12]*OpM211_9+FB112_9*s.l[3,12]
  CM1111_112 = s.In[1,12]-q[12]*FB212_11-FB212_11*s.l[3,12]
  CM101_311 = CM111_212*S11
  CM102_311 = CM112_212*S11
  CM103_311 = CM113_212*S11

# = = Block_0_2_0_1_0_4 = = 
 
# Backward Dynamics 

  FA114 = -(s.frc[1,14]-s.m[14]*(AlF110*C14-AlF313*S14))
  FA214 = -(s.frc[2,14]-s.m[14]*(AlF29*C13+AlF310*S13))
  FA314 = -(s.frc[3,14]-s.m[14]*(AlF110*S14+AlF313*C14))
  CF114 = -(s.trq[1,14]-s.In[1,14]*(C14*(OpF110-qd[14]*OM313)-S14*(OpF313+qd[14]*OM113))+OM214*OM314*(s.In[5,14]-\
   s.In[9,14]))
  CF214 = -(s.trq[2,14]-s.In[5,14]*(C13*(OpF29+qd[13]*OM310)+S13*(OpF310-qd[13]*OM210))-OM114*OM314*(s.In[1,14]-\
   s.In[9,14]))
  CF314 = -(s.trq[3,14]-s.In[9,14]*(C14*(OpF313+qd[14]*OM113)+S14*(OpF110-qd[14]*OM313))+OM114*OM214*(s.In[1,14]-\
   s.In[5,14]))
  FB114_1 = s.m[14]*(AlM110_1*C14-AlM313_1*S14)
  FB214_1 = s.m[14]*(AlM29_1*C13+AlM310_1*S13)
  FB314_1 = s.m[14]*(AlM110_1*S14+AlM313_1*C14)
  FB114_2 = s.m[14]*(AlM110_2*C14-AlM313_2*S14)
  FB214_2 = s.m[14]*(AlM29_2*C13+AlM310_2*S13)
  FB314_2 = s.m[14]*(AlM110_2*S14+AlM313_2*C14)
  FB114_3 = s.m[14]*(AlM110_3*C14-AlM313_3*S14)
  FB214_3 = s.m[14]*(AlM29_3*C13+AlM310_3*S13)
  FB314_3 = s.m[14]*(AlM110_3*S14+AlM313_3*C14)
  FB114_4 = s.m[14]*(AlM110_4*C14-AlM313_4*S14)
  FB214_4 = s.m[14]*(AlM29_4*C13+AlM310_4*S13)
  FB314_4 = s.m[14]*(AlM110_4*S14+AlM313_4*C14)
  CM114_4 = s.In[1,14]*(OpM110_4*C14-OpM313_4*S14)
  CM214_4 = s.In[5,14]*(OpM29_4*C13+OpM310_4*S13)
  CM314_4 = s.In[9,14]*(OpM110_4*S14+OpM313_4*C14)
  FB114_5 = s.m[14]*(AlM110_5*C14-AlM313_5*S14)
  FB214_5 = s.m[14]*(AlM29_5*C13+AlM310_5*S13)
  FB314_5 = s.m[14]*(AlM110_5*S14+AlM313_5*C14)
  CM114_5 = s.In[1,14]*(OpM110_5*C14-OpM313_5*S14)
  CM214_5 = s.In[5,14]*(OpM29_5*C13+OpM310_5*S13)
  CM314_5 = s.In[9,14]*(OpM110_5*S14+OpM313_5*C14)
  FB114_6 = s.m[14]*(AlM110_6*C14-AlM313_6*S14)
  FB214_6 = s.m[14]*(AlM29_6*C13+AlM310_6*S13)
  FB314_6 = s.m[14]*(AlM110_6*S14+AlM313_6*C14)
  CM114_6 = s.In[1,14]*(OpM110_6*C14-OpM313_6*S14)
  CM214_6 = s.In[5,14]*(OpM29_6*C13+OpM310_6*S13)
  CM314_6 = s.In[9,14]*(OpM110_6*S14+OpM313_6*C14)
  FB114_7 = s.m[14]*(AlM110_7*C14-AlM313_7*S14)
  FB214_7 = s.m[14]*(AlM29_7*C13+AlM310_7*S13)
  FB314_7 = s.m[14]*(AlM110_7*S14+AlM313_7*C14)
  CM114_7 = s.In[1,14]*(OpM110_7*C14-OpM313_7*S14)
  CM214_7 = s.In[5,14]*(OpM29_7*C13+OpM310_7*S13)
  CM314_7 = s.In[9,14]*(OpM110_7*S14+OpM313_7*C14)
  CM114_8 = s.In[1,14]*(OpM110_8*C14-OpM313_8*S14)
  CM214_8 = s.In[5,14]*(OpM310_8*S13+C13*S9)
  CM314_8 = s.In[9,14]*(OpM110_8*S14+OpM313_8*C14)
  CM114_9 = -s.In[1,14]*(OpM313_9*S14-C10*C14)
  CM214_9 = s.In[5,14]*S10*S13
  CM314_9 = s.In[9,14]*(OpM313_9*C14+C10*S14)
  CM114_10 = s.In[1,14]*S13*S14
  CM214_10 = s.In[5,14]*C13
  CM314_10 = -s.In[9,14]*S13*C14
  FF13_314 = -(FA114*S14-FA314*C14)
  CF13_114 = CF114*C14+CF314*S14
  CF13_314 = -(CF114*S14-CF314*C14)
  FM131_314 = -(FB114_1*S14-FB314_1*C14)
  FM132_314 = -(FB114_2*S14-FB314_2*C14)
  FM133_314 = -(FB114_3*S14-FB314_3*C14)
  FM134_314 = -(FB114_4*S14-FB314_4*C14)
  CM134_114 = CM114_4*C14+CM314_4*S14
  CM134_314 = -(CM114_4*S14-CM314_4*C14)
  FM135_314 = -(FB114_5*S14-FB314_5*C14)
  CM135_114 = CM114_5*C14+CM314_5*S14
  CM135_314 = -(CM114_5*S14-CM314_5*C14)
  FM136_314 = -(FB114_6*S14-FB314_6*C14)
  CM136_114 = CM114_6*C14+CM314_6*S14
  CM136_314 = -(CM114_6*S14-CM314_6*C14)
  FM137_314 = -(FB114_7*S14-FB314_7*C14)
  CM137_114 = CM114_7*C14+CM314_7*S14
  CM137_314 = -(CM114_7*S14-CM314_7*C14)
  CM138_114 = CM114_8*C14+CM314_8*S14
  CM138_314 = -(CM114_8*S14-CM314_8*C14)
  CM139_114 = CM114_9*C14+CM314_9*S14
  CM139_314 = -(CM114_9*S14-CM314_9*C14)
  CM1310_114 = CM114_10*C14+CM314_10*S14
  CM1313_114 = s.In[1,14]*C14*C14+s.In[9,14]*S14*S14

# = = Block_0_2_0_1_0_6 = = 
 
# Backward Dynamics 

  FA120 = -(s.frc[1,20]-s.m[20]*(AlF118+q[20]*(OpF219+OM119*OM319)+(2.0)*qd[20]*OM219+BeF318*s.dpt[3,19]+s.l[3,20]*(OpF219+\
   OM119*OM319)))
  FA220 = -(s.frc[2,20]+s.m[20]*(q[20]*(OpF118-OM219*OM319)+(2.0)*qd[20]*OM119+s.l[3,20]*(OpF118-OM219*OM319)-C19*(AlF217+\
   BeF618*s.dpt[3,19])-S19*(AlF318+BS918*s.dpt[3,19])))
  FA320 = -(s.frc[3,20]-s.m[20]*(C19*(AlF318+BS918*s.dpt[3,19])-S19*(AlF217+BeF618*s.dpt[3,19])-(q[20]+s.l[3,20])*(OM119\
   *OM119+OM219*OM219)))
  CF320 = -(s.trq[3,20]-s.In[9,20]*(C19*(OpF318-qd[19]*OM218)-S19*(OpF217+qd[19]*OM318))+OM119*OM219*(s.In[1,20]-\
   s.In[5,20]))
  FB120_1 = s.m[20]*AlM118_1
  FB220_1 = s.m[20]*(AlM217_1*C19+AlM318_1*S19)
  FB320_1 = -s.m[20]*(AlM217_1*S19-AlM318_1*C19)
  FB120_2 = s.m[20]*AlM118_2
  FB220_2 = s.m[20]*(AlM217_2*C19+AlM318_2*S19)
  FB320_2 = -s.m[20]*(AlM217_2*S19-AlM318_2*C19)
  FB120_3 = s.m[20]*AlM118_3
  FB220_3 = s.m[20]*(AlM217_3*C19+AlM318_3*S19)
  FB320_3 = -s.m[20]*(AlM217_3*S19-AlM318_3*C19)
  FB120_4 = s.m[20]*(AlM118_4+q[20]*OpM219_4+OpM217_4*s.dpt[3,19]+OpM219_4*s.l[3,20])
  FB220_4 = s.m[20]*(AlM318_4*S19+C19*(AlM217_4-OpM118_4*s.dpt[3,19])-q[20]*OpM118_4-OpM118_4*s.l[3,20])
  FB320_4 = s.m[20]*(AlM318_4*C19-S19*(AlM217_4-OpM118_4*s.dpt[3,19]))
  CM320_4 = -s.In[9,20]*(OpM217_4*S19-OpM318_4*C19)
  FB120_5 = s.m[20]*(AlM118_5+q[20]*OpM219_5+OpM217_5*s.dpt[3,19]+OpM219_5*s.l[3,20])
  FB220_5 = s.m[20]*(AlM318_5*S19+C19*(AlM217_5-OpM118_5*s.dpt[3,19])-q[20]*OpM118_5-OpM118_5*s.l[3,20])
  FB320_5 = s.m[20]*(AlM318_5*C19-S19*(AlM217_5-OpM118_5*s.dpt[3,19]))
  CM320_5 = -s.In[9,20]*(OpM217_5*S19-OpM318_5*C19)
  FB120_6 = s.m[20]*(AlM118_6+q[20]*OpM219_6+OpM217_6*s.dpt[3,19]+OpM219_6*s.l[3,20])
  FB220_6 = s.m[20]*(AlM318_6*S19+C19*(AlM217_6-OpM118_6*s.dpt[3,19])-q[20]*OpM118_6-OpM118_6*s.l[3,20])
  FB320_6 = s.m[20]*(AlM318_6*C19-S19*(AlM217_6-OpM118_6*s.dpt[3,19]))
  CM320_6 = -s.In[9,20]*(OpM217_6*S19-OpM318_6*C19)
  FB120_15 = s.m[20]*(AlM118_15+q[20]*OpM219_15+OpM217_15*s.dpt[3,19]+OpM219_15*s.l[3,20])
  FB220_15 = s.m[20]*(AlM318_15*S19+C19*(AlM217_15-OpM118_15*s.dpt[3,19])-q[20]*OpM118_15-OpM118_15*s.l[3,20])
  FB320_15 = s.m[20]*(AlM318_15*C19-S19*(AlM217_15-OpM118_15*s.dpt[3,19]))
  CM320_15 = -s.In[9,20]*(OpM217_15*S19-OpM318_15*C19)
  FB120_16 = s.m[20]*(OpM219_16*(q[20]+s.l[3,20])+s.dpt[3,19]*S17)
  FB220_16 = -s.m[20]*OpM118_16*(q[20]+s.l[3,20]+s.dpt[3,19]*C19)
  FB320_16 = s.m[20]*OpM118_16*s.dpt[3,19]*S19
  CM320_16 = s.In[9,20]*(OpM318_16*C19-S17*S19)
  FB120_17 = s.m[20]*OpM219_17*(q[20]+s.l[3,20])
  FB220_17 = -s.m[20]*C18*(q[20]+s.l[3,20]+s.dpt[3,19]*C19)
  FB320_17 = s.m[20]*s.dpt[3,19]*C18*S19
  CM320_17 = s.In[9,20]*S18*C19
  FB120_18 = s.m[20]*(s.dpt[3,19]+q[20]*C19+s.l[3,20]*C19)
  FB220_19 = -s.m[20]*(q[20]+s.l[3,20])
  CF19_120 = -(s.trq[1,20]+q[20]*FA220-s.In[1,20]*OpF118+FA220*s.l[3,20]+OM219*OM319*(s.In[5,20]-s.In[9,20]))
  CF19_220 = -(s.trq[2,20]-q[20]*FA120-s.In[5,20]*OpF219-FA120*s.l[3,20]-OM119*OM319*(s.In[1,20]-s.In[9,20]))
  CM191_120 = -FB220_1*(q[20]+s.l[3,20])
  CM191_220 = FB120_1*(q[20]+s.l[3,20])
  CM192_120 = -FB220_2*(q[20]+s.l[3,20])
  CM192_220 = FB120_2*(q[20]+s.l[3,20])
  CM193_120 = -FB220_3*(q[20]+s.l[3,20])
  CM193_220 = FB120_3*(q[20]+s.l[3,20])
  CM194_120 = s.In[1,20]*OpM118_4-FB220_4*s.l[3,20]-q[20]*FB220_4
  CM194_220 = q[20]*FB120_4+s.In[5,20]*OpM219_4+FB120_4*s.l[3,20]
  CM195_120 = s.In[1,20]*OpM118_5-FB220_5*s.l[3,20]-q[20]*FB220_5
  CM195_220 = q[20]*FB120_5+s.In[5,20]*OpM219_5+FB120_5*s.l[3,20]
  CM196_120 = s.In[1,20]*OpM118_6-FB220_6*s.l[3,20]-q[20]*FB220_6
  CM196_220 = q[20]*FB120_6+s.In[5,20]*OpM219_6+FB120_6*s.l[3,20]
  CM1915_120 = s.In[1,20]*OpM118_15-FB220_15*s.l[3,20]-q[20]*FB220_15
  CM1915_220 = q[20]*FB120_15+s.In[5,20]*OpM219_15+FB120_15*s.l[3,20]
  CM1916_120 = s.In[1,20]*OpM118_16-FB220_16*s.l[3,20]-q[20]*FB220_16
  CM1916_220 = q[20]*FB120_16+s.In[5,20]*OpM219_16+FB120_16*s.l[3,20]
  CM1917_120 = s.In[1,20]*C18-FB220_17*s.l[3,20]-q[20]*FB220_17
  CM1917_220 = q[20]*FB120_17+s.In[5,20]*OpM219_17+FB120_17*s.l[3,20]
  CM1919_120 = s.In[1,20]-q[20]*FB220_19-FB220_19*s.l[3,20]
  CM181_319 = CM191_220*S19
  CM182_319 = CM192_220*S19
  CM183_319 = CM193_220*S19

# = = Block_0_2_0_1_0_7 = = 
 
# Backward Dynamics 

  FA122 = -(s.frc[1,22]-s.m[22]*(AlF118*C22-AlF321*S22))
  FA222 = -(s.frc[2,22]-s.m[22]*(AlF217*C21+AlF318*S21))
  FA322 = -(s.frc[3,22]-s.m[22]*(AlF118*S22+AlF321*C22))
  CF122 = -(s.trq[1,22]-s.In[1,22]*(C22*(OpF118-qd[22]*OM321)-S22*(OpF321+qd[22]*OM121))+OM222*OM322*(s.In[5,22]-\
   s.In[9,22]))
  CF222 = -(s.trq[2,22]-s.In[5,22]*(C21*(OpF217+qd[21]*OM318)+S21*(OpF318-qd[21]*OM218))-OM122*OM322*(s.In[1,22]-\
   s.In[9,22]))
  CF322 = -(s.trq[3,22]-s.In[9,22]*(C22*(OpF321+qd[22]*OM121)+S22*(OpF118-qd[22]*OM321))+OM122*OM222*(s.In[1,22]-\
   s.In[5,22]))
  FB122_1 = s.m[22]*(AlM118_1*C22-AlM321_1*S22)
  FB222_1 = s.m[22]*(AlM217_1*C21+AlM318_1*S21)
  FB322_1 = s.m[22]*(AlM118_1*S22+AlM321_1*C22)
  FB122_2 = s.m[22]*(AlM118_2*C22-AlM321_2*S22)
  FB222_2 = s.m[22]*(AlM217_2*C21+AlM318_2*S21)
  FB322_2 = s.m[22]*(AlM118_2*S22+AlM321_2*C22)
  FB122_3 = s.m[22]*(AlM118_3*C22-AlM321_3*S22)
  FB222_3 = s.m[22]*(AlM217_3*C21+AlM318_3*S21)
  FB322_3 = s.m[22]*(AlM118_3*S22+AlM321_3*C22)
  FB122_4 = s.m[22]*(AlM118_4*C22-AlM321_4*S22)
  FB222_4 = s.m[22]*(AlM217_4*C21+AlM318_4*S21)
  FB322_4 = s.m[22]*(AlM118_4*S22+AlM321_4*C22)
  CM122_4 = s.In[1,22]*(OpM118_4*C22-OpM321_4*S22)
  CM222_4 = s.In[5,22]*(OpM217_4*C21+OpM318_4*S21)
  CM322_4 = s.In[9,22]*(OpM118_4*S22+OpM321_4*C22)
  FB122_5 = s.m[22]*(AlM118_5*C22-AlM321_5*S22)
  FB222_5 = s.m[22]*(AlM217_5*C21+AlM318_5*S21)
  FB322_5 = s.m[22]*(AlM118_5*S22+AlM321_5*C22)
  CM122_5 = s.In[1,22]*(OpM118_5*C22-OpM321_5*S22)
  CM222_5 = s.In[5,22]*(OpM217_5*C21+OpM318_5*S21)
  CM322_5 = s.In[9,22]*(OpM118_5*S22+OpM321_5*C22)
  FB122_6 = s.m[22]*(AlM118_6*C22-AlM321_6*S22)
  FB222_6 = s.m[22]*(AlM217_6*C21+AlM318_6*S21)
  FB322_6 = s.m[22]*(AlM118_6*S22+AlM321_6*C22)
  CM122_6 = s.In[1,22]*(OpM118_6*C22-OpM321_6*S22)
  CM222_6 = s.In[5,22]*(OpM217_6*C21+OpM318_6*S21)
  CM322_6 = s.In[9,22]*(OpM118_6*S22+OpM321_6*C22)
  FB122_15 = s.m[22]*(AlM118_15*C22-AlM321_15*S22)
  FB222_15 = s.m[22]*(AlM217_15*C21+AlM318_15*S21)
  FB322_15 = s.m[22]*(AlM118_15*S22+AlM321_15*C22)
  CM122_15 = s.In[1,22]*(OpM118_15*C22-OpM321_15*S22)
  CM222_15 = s.In[5,22]*(OpM217_15*C21+OpM318_15*S21)
  CM322_15 = s.In[9,22]*(OpM118_15*S22+OpM321_15*C22)
  CM122_16 = s.In[1,22]*(OpM118_16*C22-OpM321_16*S22)
  CM222_16 = s.In[5,22]*(OpM318_16*S21+S17*C21)
  CM322_16 = s.In[9,22]*(OpM118_16*S22+OpM321_16*C22)
  CM122_17 = -s.In[1,22]*(OpM321_17*S22-C18*C22)
  CM222_17 = s.In[5,22]*S18*S21
  CM322_17 = s.In[9,22]*(OpM321_17*C22+C18*S22)
  CM122_18 = s.In[1,22]*S21*S22
  CM222_18 = s.In[5,22]*C21
  CM322_18 = -s.In[9,22]*S21*C22
  FF21_322 = -(FA122*S22-FA322*C22)
  CF21_122 = CF122*C22+CF322*S22
  CF21_322 = -(CF122*S22-CF322*C22)
  FM211_322 = -(FB122_1*S22-FB322_1*C22)
  FM212_322 = -(FB122_2*S22-FB322_2*C22)
  FM213_322 = -(FB122_3*S22-FB322_3*C22)
  FM214_322 = -(FB122_4*S22-FB322_4*C22)
  CM214_122 = CM122_4*C22+CM322_4*S22
  CM214_322 = -(CM122_4*S22-CM322_4*C22)
  FM215_322 = -(FB122_5*S22-FB322_5*C22)
  CM215_122 = CM122_5*C22+CM322_5*S22
  CM215_322 = -(CM122_5*S22-CM322_5*C22)
  FM216_322 = -(FB122_6*S22-FB322_6*C22)
  CM216_122 = CM122_6*C22+CM322_6*S22
  CM216_322 = -(CM122_6*S22-CM322_6*C22)
  FM2115_322 = -(FB122_15*S22-FB322_15*C22)
  CM2115_122 = CM122_15*C22+CM322_15*S22
  CM2115_322 = -(CM122_15*S22-CM322_15*C22)
  CM2116_122 = CM122_16*C22+CM322_16*S22
  CM2116_322 = -(CM122_16*S22-CM322_16*C22)
  CM2117_122 = CM122_17*C22+CM322_17*S22
  CM2117_322 = -(CM122_17*S22-CM322_17*C22)
  CM2118_122 = CM122_18*C22+CM322_18*S22
  CM2121_122 = s.In[1,22]*C22*C22+s.In[9,22]*S22*S22

# = = Block_0_2_0_1_0_9 = = 
 
# Backward Dynamics 

  FA128 = -(s.frc[1,28]-s.m[28]*(AlF126+q[28]*(OpF227+OM127*OM327)+(2.0)*qd[28]*OM227+BeF326*s.dpt[3,24]+s.l[3,28]*(OpF227+\
   OM127*OM327)))
  FA228 = -(s.frc[2,28]+s.m[28]*(q[28]*(OpF126-OM227*OM327)+(2.0)*qd[28]*OM127+s.l[3,28]*(OpF126-OM227*OM327)-C27*(AlF226+\
   BeF626*s.dpt[3,24])-S27*(AlF325+BS926*s.dpt[3,24])))
  FA328 = -(s.frc[3,28]-s.m[28]*(C27*(AlF325+BS926*s.dpt[3,24])-S27*(AlF226+BeF626*s.dpt[3,24])-(q[28]+s.l[3,28])*(OM127\
   *OM127+OM227*OM227)))
  CF328 = -(s.trq[3,28]-s.In[9,28]*(C27*(OpF325-qd[27]*OM226)-S27*(OpF226+qd[27]*OM326))+OM127*OM227*(s.In[1,28]-\
   s.In[5,28]))
  FB128_1 = s.m[28]*AlM126_1
  FB228_1 = s.m[28]*(AlM226_1*C27+AlM325_1*S27)
  FB328_1 = -s.m[28]*(AlM226_1*S27-AlM325_1*C27)
  FB128_2 = s.m[28]*AlM126_2
  FB228_2 = s.m[28]*(AlM226_2*C27+AlM325_2*S27)
  FB328_2 = -s.m[28]*(AlM226_2*S27-AlM325_2*C27)
  FB128_3 = s.m[28]*AlM126_3
  FB228_3 = s.m[28]*(AlM226_3*C27+AlM325_3*S27)
  FB328_3 = -s.m[28]*(AlM226_3*S27-AlM325_3*C27)
  FB128_4 = s.m[28]*(AlM126_4+q[28]*OpM227_4+OpM226_4*s.dpt[3,24]+OpM227_4*s.l[3,28])
  FB228_4 = s.m[28]*(AlM325_4*S27+C27*(AlM226_4-OpM126_4*s.dpt[3,24])-q[28]*OpM126_4-OpM126_4*s.l[3,28])
  FB328_4 = s.m[28]*(AlM325_4*C27-S27*(AlM226_4-OpM126_4*s.dpt[3,24]))
  CM328_4 = -s.In[9,28]*(OpM226_4*S27-OpM325_4*C27)
  FB128_5 = s.m[28]*(AlM126_5+q[28]*OpM227_5+OpM226_5*s.dpt[3,24]+OpM227_5*s.l[3,28])
  FB228_5 = s.m[28]*(AlM325_5*S27+C27*(AlM226_5-OpM126_5*s.dpt[3,24])-q[28]*OpM126_5-OpM126_5*s.l[3,28])
  FB328_5 = s.m[28]*(AlM325_5*C27-S27*(AlM226_5-OpM126_5*s.dpt[3,24]))
  CM328_5 = -s.In[9,28]*(OpM226_5*S27-OpM325_5*C27)
  FB128_6 = s.m[28]*(AlM126_6+q[28]*OpM227_6+OpM226_6*s.dpt[3,24]+OpM227_6*s.l[3,28])
  FB228_6 = s.m[28]*(AlM325_6*S27+C27*(AlM226_6-OpM126_6*s.dpt[3,24])-q[28]*OpM126_6-OpM126_6*s.l[3,28])
  FB328_6 = s.m[28]*(AlM325_6*C27-S27*(AlM226_6-OpM126_6*s.dpt[3,24]))
  CM328_6 = -s.In[9,28]*(OpM226_6*S27-OpM325_6*C27)
  FB128_23 = s.m[28]*(AlM126_23+q[28]*OpM227_23+OpM226_23*s.dpt[3,24]+OpM227_23*s.l[3,28])
  FB228_23 = s.m[28]*(AlM325_23*S27+C27*(AlM226_23-OpM126_23*s.dpt[3,24])-q[28]*OpM126_23-OpM126_23*s.l[3,28])
  FB328_23 = s.m[28]*(AlM325_23*C27-S27*(AlM226_23-OpM126_23*s.dpt[3,24]))
  CM328_23 = -s.In[9,28]*(OpM226_23*S27-OpM325_23*C27)
  FB128_24 = s.m[28]*(AlM126_24+q[28]*OpM227_24+OpM226_24*s.dpt[3,24]+OpM227_24*s.l[3,28])
  FB228_24 = -s.m[28]*(OpM126_24*(q[28]+s.l[3,28])-C27*(AlM226_24-OpM126_24*s.dpt[3,24]))
  FB328_24 = -s.m[28]*S27*(AlM226_24-OpM126_24*s.dpt[3,24])
  CM328_24 = -s.In[9,28]*(OpM226_24*S27-C25*C27)
  FB128_25 = s.m[28]*(OpM227_25*(q[28]+s.l[3,28])-s.dpt[3,24]*S26)
  FB228_25 = -s.m[28]*C26*(q[28]+s.l[3,28]+s.dpt[3,24]*C27)
  FB328_25 = s.m[28]*s.dpt[3,24]*C26*S27
  CM328_25 = s.In[9,28]*S26*S27
  FB128_26 = s.m[28]*S27*(q[28]+s.l[3,28])
  FB228_27 = -s.m[28]*(q[28]+s.l[3,28])
  CF27_128 = -(s.trq[1,28]+q[28]*FA228-s.In[1,28]*OpF126+FA228*s.l[3,28]+OM227*OM327*(s.In[5,28]-s.In[9,28]))
  CF27_228 = -(s.trq[2,28]-q[28]*FA128-s.In[5,28]*OpF227-FA128*s.l[3,28]-OM127*OM327*(s.In[1,28]-s.In[9,28]))
  CM271_128 = -FB228_1*(q[28]+s.l[3,28])
  CM271_228 = FB128_1*(q[28]+s.l[3,28])
  CM272_128 = -FB228_2*(q[28]+s.l[3,28])
  CM272_228 = FB128_2*(q[28]+s.l[3,28])
  CM273_128 = -FB228_3*(q[28]+s.l[3,28])
  CM273_228 = FB128_3*(q[28]+s.l[3,28])
  CM274_128 = s.In[1,28]*OpM126_4-FB228_4*s.l[3,28]-q[28]*FB228_4
  CM274_228 = q[28]*FB128_4+s.In[5,28]*OpM227_4+FB128_4*s.l[3,28]
  CM275_128 = s.In[1,28]*OpM126_5-FB228_5*s.l[3,28]-q[28]*FB228_5
  CM275_228 = q[28]*FB128_5+s.In[5,28]*OpM227_5+FB128_5*s.l[3,28]
  CM276_128 = s.In[1,28]*OpM126_6-FB228_6*s.l[3,28]-q[28]*FB228_6
  CM276_228 = q[28]*FB128_6+s.In[5,28]*OpM227_6+FB128_6*s.l[3,28]
  CM2723_128 = s.In[1,28]*OpM126_23-FB228_23*s.l[3,28]-q[28]*FB228_23
  CM2723_228 = q[28]*FB128_23+s.In[5,28]*OpM227_23+FB128_23*s.l[3,28]
  CM2724_128 = s.In[1,28]*OpM126_24-FB228_24*s.l[3,28]-q[28]*FB228_24
  CM2724_228 = q[28]*FB128_24+s.In[5,28]*OpM227_24+FB128_24*s.l[3,28]
  CM2725_128 = s.In[1,28]*C26-FB228_25*s.l[3,28]-q[28]*FB228_25
  CM2725_228 = q[28]*FB128_25+s.In[5,28]*OpM227_25+FB128_25*s.l[3,28]
  CM2727_128 = s.In[1,28]-q[28]*FB228_27-FB228_27*s.l[3,28]
  CM261_327 = CM271_228*S27
  CM262_327 = CM272_228*S27
  CM263_327 = CM273_228*S27

# = = Block_0_2_0_1_0_10 = = 
 
# Backward Dynamics 

  FA130 = -(s.frc[1,30]-s.m[30]*(AlF129*C30-AlF329*S30))
  FA230 = -(s.frc[2,30]-s.m[30]*(C29*(AlF226+BeF626*s.dpt[3,25])+S29*(AlF325+BS926*s.dpt[3,25])))
  FA330 = -(s.frc[3,30]-s.m[30]*(AlF129*S30+AlF329*C30))
  CF130 = -(s.trq[1,30]-s.In[1,30]*(C30*(OpF126-qd[30]*OM329)-S30*(OpF329+qd[30]*OM129))+OM230*OM330*(s.In[5,30]-\
   s.In[9,30]))
  CF230 = -(s.trq[2,30]-s.In[5,30]*(C29*(OpF226+qd[29]*OM326)+S29*(OpF325-qd[29]*OM226))-OM130*OM330*(s.In[1,30]-\
   s.In[9,30]))
  CF330 = -(s.trq[3,30]-s.In[9,30]*(C30*(OpF329+qd[30]*OM129)+S30*(OpF126-qd[30]*OM329))+OM130*OM230*(s.In[1,30]-\
   s.In[5,30]))
  FB130_1 = s.m[30]*(AlM126_1*C30-AlM329_1*S30)
  FB230_1 = s.m[30]*(AlM226_1*C29+AlM325_1*S29)
  FB330_1 = s.m[30]*(AlM126_1*S30+AlM329_1*C30)
  FB130_2 = s.m[30]*(AlM126_2*C30-AlM329_2*S30)
  FB230_2 = s.m[30]*(AlM226_2*C29+AlM325_2*S29)
  FB330_2 = s.m[30]*(AlM126_2*S30+AlM329_2*C30)
  FB130_3 = s.m[30]*(AlM126_3*C30-AlM329_3*S30)
  FB230_3 = s.m[30]*(AlM226_3*C29+AlM325_3*S29)
  FB330_3 = s.m[30]*(AlM126_3*S30+AlM329_3*C30)
  FB130_4 = s.m[30]*(AlM129_4*C30-AlM329_4*S30)
  FB230_4 = s.m[30]*(AlM325_4*S29+C29*(AlM226_4-OpM126_4*s.dpt[3,25]))
  FB330_4 = s.m[30]*(AlM129_4*S30+AlM329_4*C30)
  CM130_4 = s.In[1,30]*(OpM126_4*C30-OpM329_4*S30)
  CM230_4 = s.In[5,30]*(OpM226_4*C29+OpM325_4*S29)
  CM330_4 = s.In[9,30]*(OpM126_4*S30+OpM329_4*C30)
  FB130_5 = s.m[30]*(AlM129_5*C30-AlM329_5*S30)
  FB230_5 = s.m[30]*(AlM325_5*S29+C29*(AlM226_5-OpM126_5*s.dpt[3,25]))
  FB330_5 = s.m[30]*(AlM129_5*S30+AlM329_5*C30)
  CM130_5 = s.In[1,30]*(OpM126_5*C30-OpM329_5*S30)
  CM230_5 = s.In[5,30]*(OpM226_5*C29+OpM325_5*S29)
  CM330_5 = s.In[9,30]*(OpM126_5*S30+OpM329_5*C30)
  FB130_6 = s.m[30]*(AlM129_6*C30-AlM329_6*S30)
  FB230_6 = s.m[30]*(AlM325_6*S29+C29*(AlM226_6-OpM126_6*s.dpt[3,25]))
  FB330_6 = s.m[30]*(AlM129_6*S30+AlM329_6*C30)
  CM130_6 = s.In[1,30]*(OpM126_6*C30-OpM329_6*S30)
  CM230_6 = s.In[5,30]*(OpM226_6*C29+OpM325_6*S29)
  CM330_6 = s.In[9,30]*(OpM126_6*S30+OpM329_6*C30)
  FB130_23 = s.m[30]*(AlM129_23*C30-AlM329_23*S30)
  FB230_23 = s.m[30]*(AlM325_23*S29+C29*(AlM226_23-OpM126_23*s.dpt[3,25]))
  FB330_23 = s.m[30]*(AlM129_23*S30+AlM329_23*C30)
  CM130_23 = s.In[1,30]*(OpM126_23*C30-OpM329_23*S30)
  CM230_23 = s.In[5,30]*(OpM226_23*C29+OpM325_23*S29)
  CM330_23 = s.In[9,30]*(OpM126_23*S30+OpM329_23*C30)
  FB130_24 = s.m[30]*(AlM129_24*C30-AlM329_24*S30)
  FB230_24 = s.m[30]*C29*(AlM226_24-OpM126_24*s.dpt[3,25])
  FB330_24 = s.m[30]*(AlM129_24*S30+AlM329_24*C30)
  CM130_24 = s.In[1,30]*(OpM126_24*C30-OpM329_24*S30)
  CM230_24 = s.In[5,30]*(OpM226_24*C29+C25*S29)
  CM330_24 = s.In[9,30]*(OpM126_24*S30+OpM329_24*C30)
  FB130_25 = s.m[30]*(AlM129_25*C30-AlM329_25*S30)
  FB330_25 = s.m[30]*(AlM129_25*S30+AlM329_25*C30)
  CM130_25 = -s.In[1,30]*(OpM329_25*S30-C26*C30)
  CM230_25 = -s.In[5,30]*S26*C29
  CM330_25 = s.In[9,30]*(OpM329_25*C30+C26*S30)
  CM130_26 = -s.In[1,30]*C29*S30
  CM230_26 = s.In[5,30]*S29
  CM330_26 = s.In[9,30]*C29*C30
  FF29_130 = FA130*C30+FA330*S30
  FF29_330 = -(FA130*S30-FA330*C30)
  CF29_130 = CF130*C30+CF330*S30
  CF29_330 = -(CF130*S30-CF330*C30)
  FM291_130 = FB130_1*C30+FB330_1*S30
  FM291_330 = -(FB130_1*S30-FB330_1*C30)
  FM292_130 = FB130_2*C30+FB330_2*S30
  FM292_330 = -(FB130_2*S30-FB330_2*C30)
  FM293_130 = FB130_3*C30+FB330_3*S30
  FM293_330 = -(FB130_3*S30-FB330_3*C30)
  FM294_130 = FB130_4*C30+FB330_4*S30
  FM294_330 = -(FB130_4*S30-FB330_4*C30)
  CM294_130 = CM130_4*C30+CM330_4*S30
  CM294_330 = -(CM130_4*S30-CM330_4*C30)
  FM295_130 = FB130_5*C30+FB330_5*S30
  FM295_330 = -(FB130_5*S30-FB330_5*C30)
  CM295_130 = CM130_5*C30+CM330_5*S30
  CM295_330 = -(CM130_5*S30-CM330_5*C30)
  FM296_130 = FB130_6*C30+FB330_6*S30
  FM296_330 = -(FB130_6*S30-FB330_6*C30)
  CM296_130 = CM130_6*C30+CM330_6*S30
  CM296_330 = -(CM130_6*S30-CM330_6*C30)
  FM2923_130 = FB130_23*C30+FB330_23*S30
  FM2923_330 = -(FB130_23*S30-FB330_23*C30)
  CM2923_130 = CM130_23*C30+CM330_23*S30
  CM2923_330 = -(CM130_23*S30-CM330_23*C30)
  FM2924_130 = FB130_24*C30+FB330_24*S30
  FM2924_330 = -(FB130_24*S30-FB330_24*C30)
  CM2924_130 = CM130_24*C30+CM330_24*S30
  CM2924_330 = -(CM130_24*S30-CM330_24*C30)
  CM2925_130 = CM130_25*C30+CM330_25*S30
  CM2925_330 = -(CM130_25*S30-CM330_25*C30)
  CM2926_130 = CM130_26*C30+CM330_26*S30
  CM2929_130 = s.In[1,30]*C30*C30+s.In[9,30]*S30*S30

# = = Block_0_2_0_1_0_12 = = 
 
# Backward Dynamics 

  FA136 = -(s.frc[1,36]-s.m[36]*(AlF134+q[36]*(OpF235+OM135*OM335)+(2.0)*qd[36]*OM235+BeF334*s.dpt[3,33]+s.l[3,36]*(OpF235+\
   OM135*OM335)))
  FA236 = -(s.frc[2,36]+s.m[36]*(q[36]*(OpF134-OM235*OM335)+(2.0)*qd[36]*OM135+s.l[3,36]*(OpF134-OM235*OM335)-C35*(AlF234+\
   BeF634*s.dpt[3,33])-S35*(AlF333+BS934*s.dpt[3,33])))
  FA336 = -(s.frc[3,36]-s.m[36]*(C35*(AlF333+BS934*s.dpt[3,33])-S35*(AlF234+BeF634*s.dpt[3,33])-(q[36]+s.l[3,36])*(OM135\
   *OM135+OM235*OM235)))
  CF336 = -(s.trq[3,36]-s.In[9,36]*(C35*(OpF333-qd[35]*OM234)-S35*(OpF234+qd[35]*OM334))+OM135*OM235*(s.In[1,36]-\
   s.In[5,36]))
  FB136_1 = s.m[36]*AlM134_1
  FB236_1 = s.m[36]*(AlM234_1*C35+AlM333_1*S35)
  FB336_1 = -s.m[36]*(AlM234_1*S35-AlM333_1*C35)
  FB136_2 = s.m[36]*AlM134_2
  FB236_2 = s.m[36]*(AlM234_2*C35+AlM333_2*S35)
  FB336_2 = -s.m[36]*(AlM234_2*S35-AlM333_2*C35)
  FB136_3 = s.m[36]*AlM134_3
  FB236_3 = s.m[36]*(AlM234_3*C35+AlM333_3*S35)
  FB336_3 = -s.m[36]*(AlM234_3*S35-AlM333_3*C35)
  FB136_4 = s.m[36]*(AlM134_4+q[36]*OpM235_4+OpM234_4*s.dpt[3,33]+OpM235_4*s.l[3,36])
  FB236_4 = s.m[36]*(AlM333_4*S35+C35*(AlM234_4-OpM134_4*s.dpt[3,33])-q[36]*OpM134_4-OpM134_4*s.l[3,36])
  FB336_4 = s.m[36]*(AlM333_4*C35-S35*(AlM234_4-OpM134_4*s.dpt[3,33]))
  CM336_4 = -s.In[9,36]*(OpM234_4*S35-OpM333_4*C35)
  FB136_5 = s.m[36]*(AlM134_5+q[36]*OpM235_5+OpM234_5*s.dpt[3,33]+OpM235_5*s.l[3,36])
  FB236_5 = s.m[36]*(AlM333_5*S35+C35*(AlM234_5-OpM134_5*s.dpt[3,33])-q[36]*OpM134_5-OpM134_5*s.l[3,36])
  FB336_5 = s.m[36]*(AlM333_5*C35-S35*(AlM234_5-OpM134_5*s.dpt[3,33]))
  CM336_5 = -s.In[9,36]*(OpM234_5*S35-OpM333_5*C35)
  FB136_6 = s.m[36]*(AlM134_6+q[36]*OpM235_6+OpM234_6*s.dpt[3,33]+OpM235_6*s.l[3,36])
  FB236_6 = s.m[36]*(AlM333_6*S35+C35*(AlM234_6-OpM134_6*s.dpt[3,33])-q[36]*OpM134_6-OpM134_6*s.l[3,36])
  FB336_6 = s.m[36]*(AlM333_6*C35-S35*(AlM234_6-OpM134_6*s.dpt[3,33]))
  CM336_6 = -s.In[9,36]*(OpM234_6*S35-OpM333_6*C35)
  FB136_31 = s.m[36]*(AlM134_31+q[36]*OpM235_31+OpM234_31*s.dpt[3,33]+OpM235_31*s.l[3,36])
  FB236_31 = s.m[36]*(AlM333_31*S35+C35*(AlM234_31-OpM134_31*s.dpt[3,33])-q[36]*OpM134_31-OpM134_31*s.l[3,36])
  FB336_31 = s.m[36]*(AlM333_31*C35-S35*(AlM234_31-OpM134_31*s.dpt[3,33]))
  CM336_31 = -s.In[9,36]*(OpM234_31*S35-OpM333_31*C35)
  FB136_32 = s.m[36]*(AlM134_32+q[36]*OpM235_32+OpM234_32*s.dpt[3,33]+OpM235_32*s.l[3,36])
  FB236_32 = -s.m[36]*(OpM134_32*(q[36]+s.l[3,36])-C35*(AlM234_32-OpM134_32*s.dpt[3,33]))
  FB336_32 = -s.m[36]*S35*(AlM234_32-OpM134_32*s.dpt[3,33])
  CM336_32 = -s.In[9,36]*(OpM234_32*S35-C33*C35)
  FB136_33 = s.m[36]*(OpM235_33*(q[36]+s.l[3,36])-s.dpt[3,33]*S34)
  FB236_33 = -s.m[36]*C34*(q[36]+s.l[3,36]+s.dpt[3,33]*C35)
  FB336_33 = s.m[36]*s.dpt[3,33]*C34*S35
  CM336_33 = s.In[9,36]*S34*S35
  FB136_34 = s.m[36]*S35*(q[36]+s.l[3,36])
  FB236_35 = -s.m[36]*(q[36]+s.l[3,36])
  CF35_136 = -(s.trq[1,36]+q[36]*FA236-s.In[1,36]*OpF134+FA236*s.l[3,36]+OM235*OM335*(s.In[5,36]-s.In[9,36]))
  CF35_236 = -(s.trq[2,36]-q[36]*FA136-s.In[5,36]*OpF235-FA136*s.l[3,36]-OM135*OM335*(s.In[1,36]-s.In[9,36]))
  CM351_136 = -FB236_1*(q[36]+s.l[3,36])
  CM351_236 = FB136_1*(q[36]+s.l[3,36])
  CM352_136 = -FB236_2*(q[36]+s.l[3,36])
  CM352_236 = FB136_2*(q[36]+s.l[3,36])
  CM353_136 = -FB236_3*(q[36]+s.l[3,36])
  CM353_236 = FB136_3*(q[36]+s.l[3,36])
  CM354_136 = s.In[1,36]*OpM134_4-FB236_4*s.l[3,36]-q[36]*FB236_4
  CM354_236 = q[36]*FB136_4+s.In[5,36]*OpM235_4+FB136_4*s.l[3,36]
  CM355_136 = s.In[1,36]*OpM134_5-FB236_5*s.l[3,36]-q[36]*FB236_5
  CM355_236 = q[36]*FB136_5+s.In[5,36]*OpM235_5+FB136_5*s.l[3,36]
  CM356_136 = s.In[1,36]*OpM134_6-FB236_6*s.l[3,36]-q[36]*FB236_6
  CM356_236 = q[36]*FB136_6+s.In[5,36]*OpM235_6+FB136_6*s.l[3,36]
  CM3531_136 = s.In[1,36]*OpM134_31-FB236_31*s.l[3,36]-q[36]*FB236_31
  CM3531_236 = q[36]*FB136_31+s.In[5,36]*OpM235_31+FB136_31*s.l[3,36]
  CM3532_136 = s.In[1,36]*OpM134_32-FB236_32*s.l[3,36]-q[36]*FB236_32
  CM3532_236 = q[36]*FB136_32+s.In[5,36]*OpM235_32+FB136_32*s.l[3,36]
  CM3533_136 = s.In[1,36]*C34-FB236_33*s.l[3,36]-q[36]*FB236_33
  CM3533_236 = q[36]*FB136_33+s.In[5,36]*OpM235_33+FB136_33*s.l[3,36]
  CM3535_136 = s.In[1,36]-q[36]*FB236_35-FB236_35*s.l[3,36]
  CM341_335 = CM351_236*S35
  CM342_335 = CM352_236*S35
  CM343_335 = CM353_236*S35

# = = Block_0_2_0_1_0_13 = = 
 
# Backward Dynamics 

  FA138 = -(s.frc[1,38]-s.m[38]*(AlF137*C38-AlF337*S38))
  FA238 = -(s.frc[2,38]-s.m[38]*(C37*(AlF234+BeF634*s.dpt[3,34])+S37*(AlF333+BS934*s.dpt[3,34])))
  FA338 = -(s.frc[3,38]-s.m[38]*(AlF137*S38+AlF337*C38))
  CF138 = -(s.trq[1,38]-s.In[1,38]*(C38*(OpF134-qd[38]*OM337)-S38*(OpF337+qd[38]*OM137))+OM238*OM338*(s.In[5,38]-\
   s.In[9,38]))
  CF238 = -(s.trq[2,38]-s.In[5,38]*(C37*(OpF234+qd[37]*OM334)+S37*(OpF333-qd[37]*OM234))-OM138*OM338*(s.In[1,38]-\
   s.In[9,38]))
  CF338 = -(s.trq[3,38]-s.In[9,38]*(C38*(OpF337+qd[38]*OM137)+S38*(OpF134-qd[38]*OM337))+OM138*OM238*(s.In[1,38]-\
   s.In[5,38]))
  FB138_1 = s.m[38]*(AlM134_1*C38-AlM337_1*S38)
  FB238_1 = s.m[38]*(AlM234_1*C37+AlM333_1*S37)
  FB338_1 = s.m[38]*(AlM134_1*S38+AlM337_1*C38)
  FB138_2 = s.m[38]*(AlM134_2*C38-AlM337_2*S38)
  FB238_2 = s.m[38]*(AlM234_2*C37+AlM333_2*S37)
  FB338_2 = s.m[38]*(AlM134_2*S38+AlM337_2*C38)
  FB138_3 = s.m[38]*(AlM134_3*C38-AlM337_3*S38)
  FB238_3 = s.m[38]*(AlM234_3*C37+AlM333_3*S37)
  FB338_3 = s.m[38]*(AlM134_3*S38+AlM337_3*C38)
  FB138_4 = s.m[38]*(AlM137_4*C38-AlM337_4*S38)
  FB238_4 = s.m[38]*(AlM333_4*S37+C37*(AlM234_4-OpM134_4*s.dpt[3,34]))
  FB338_4 = s.m[38]*(AlM137_4*S38+AlM337_4*C38)
  CM138_4 = s.In[1,38]*(OpM134_4*C38-OpM337_4*S38)
  CM238_4 = s.In[5,38]*(OpM234_4*C37+OpM333_4*S37)
  CM338_4 = s.In[9,38]*(OpM134_4*S38+OpM337_4*C38)
  FB138_5 = s.m[38]*(AlM137_5*C38-AlM337_5*S38)
  FB238_5 = s.m[38]*(AlM333_5*S37+C37*(AlM234_5-OpM134_5*s.dpt[3,34]))
  FB338_5 = s.m[38]*(AlM137_5*S38+AlM337_5*C38)
  CM138_5 = s.In[1,38]*(OpM134_5*C38-OpM337_5*S38)
  CM238_5 = s.In[5,38]*(OpM234_5*C37+OpM333_5*S37)
  CM338_5 = s.In[9,38]*(OpM134_5*S38+OpM337_5*C38)
  FB138_6 = s.m[38]*(AlM137_6*C38-AlM337_6*S38)
  FB238_6 = s.m[38]*(AlM333_6*S37+C37*(AlM234_6-OpM134_6*s.dpt[3,34]))
  FB338_6 = s.m[38]*(AlM137_6*S38+AlM337_6*C38)
  CM138_6 = s.In[1,38]*(OpM134_6*C38-OpM337_6*S38)
  CM238_6 = s.In[5,38]*(OpM234_6*C37+OpM333_6*S37)
  CM338_6 = s.In[9,38]*(OpM134_6*S38+OpM337_6*C38)
  FB138_31 = s.m[38]*(AlM137_31*C38-AlM337_31*S38)
  FB238_31 = s.m[38]*(AlM333_31*S37+C37*(AlM234_31-OpM134_31*s.dpt[3,34]))
  FB338_31 = s.m[38]*(AlM137_31*S38+AlM337_31*C38)
  CM138_31 = s.In[1,38]*(OpM134_31*C38-OpM337_31*S38)
  CM238_31 = s.In[5,38]*(OpM234_31*C37+OpM333_31*S37)
  CM338_31 = s.In[9,38]*(OpM134_31*S38+OpM337_31*C38)
  FB138_32 = s.m[38]*(AlM137_32*C38-AlM337_32*S38)
  FB238_32 = s.m[38]*C37*(AlM234_32-OpM134_32*s.dpt[3,34])
  FB338_32 = s.m[38]*(AlM137_32*S38+AlM337_32*C38)
  CM138_32 = s.In[1,38]*(OpM134_32*C38-OpM337_32*S38)
  CM238_32 = s.In[5,38]*(OpM234_32*C37+C33*S37)
  CM338_32 = s.In[9,38]*(OpM134_32*S38+OpM337_32*C38)
  FB138_33 = s.m[38]*(AlM137_33*C38-AlM337_33*S38)
  FB338_33 = s.m[38]*(AlM137_33*S38+AlM337_33*C38)
  CM138_33 = -s.In[1,38]*(OpM337_33*S38-C34*C38)
  CM238_33 = -s.In[5,38]*S34*C37
  CM338_33 = s.In[9,38]*(OpM337_33*C38+C34*S38)
  CM138_34 = -s.In[1,38]*C37*S38
  CM238_34 = s.In[5,38]*S37
  CM338_34 = s.In[9,38]*C37*C38
  FF37_138 = FA138*C38+FA338*S38
  FF37_338 = -(FA138*S38-FA338*C38)
  CF37_138 = CF138*C38+CF338*S38
  CF37_338 = -(CF138*S38-CF338*C38)
  FM371_138 = FB138_1*C38+FB338_1*S38
  FM371_338 = -(FB138_1*S38-FB338_1*C38)
  FM372_138 = FB138_2*C38+FB338_2*S38
  FM372_338 = -(FB138_2*S38-FB338_2*C38)
  FM373_138 = FB138_3*C38+FB338_3*S38
  FM373_338 = -(FB138_3*S38-FB338_3*C38)
  FM374_138 = FB138_4*C38+FB338_4*S38
  FM374_338 = -(FB138_4*S38-FB338_4*C38)
  CM374_138 = CM138_4*C38+CM338_4*S38
  CM374_338 = -(CM138_4*S38-CM338_4*C38)
  FM375_138 = FB138_5*C38+FB338_5*S38
  FM375_338 = -(FB138_5*S38-FB338_5*C38)
  CM375_138 = CM138_5*C38+CM338_5*S38
  CM375_338 = -(CM138_5*S38-CM338_5*C38)
  FM376_138 = FB138_6*C38+FB338_6*S38
  FM376_338 = -(FB138_6*S38-FB338_6*C38)
  CM376_138 = CM138_6*C38+CM338_6*S38
  CM376_338 = -(CM138_6*S38-CM338_6*C38)
  FM3731_138 = FB138_31*C38+FB338_31*S38
  FM3731_338 = -(FB138_31*S38-FB338_31*C38)
  CM3731_138 = CM138_31*C38+CM338_31*S38
  CM3731_338 = -(CM138_31*S38-CM338_31*C38)
  FM3732_138 = FB138_32*C38+FB338_32*S38
  FM3732_338 = -(FB138_32*S38-FB338_32*C38)
  CM3732_138 = CM138_32*C38+CM338_32*S38
  CM3732_338 = -(CM138_32*S38-CM338_32*C38)
  CM3733_138 = CM138_33*C38+CM338_33*S38
  CM3733_338 = -(CM138_33*S38-CM338_33*C38)
  CM3734_138 = CM138_34*C38+CM338_34*S38
  CM3737_138 = s.In[1,38]*C38*C38+s.In[9,38]*S38*S38

# = = Block_0_2_0_2_0_2 = = 
 
# Backward Dynamics 

  FA110 = -(s.frc[1,10]-s.m[10]*(AlF110+BeF310*s.l[3,10]))
  FA210 = -(s.frc[2,10]-s.m[10]*(AlF29+BeF610*s.l[3,10]))
  FF110 = FA110+FA112+FA114*C14+FA314*S14
  FF210 = FA210+FA212*C11+FA214*C13-FA312*S11-FF13_314*S13
  FF310 = -(s.frc[3,10]-s.m[10]*(AlF310+BS910*s.l[3,10])-FA212*S11-FA214*S13-FA312*C11-FF13_314*C13)
  CF110 = -(s.trq[1,10]-CF11_112-CF13_114-s.In[1,10]*OpF110-s.In[9,10]*OM210*OM310+FA210*s.l[3,10]+s.dpt[3,14]*(FA212*\
   C11-FA312*S11))
  CF210 = -(s.trq[2,10]-CF11_212*C11+CF13_314*S13-CF214*C13+CF312*S11-FA110*s.l[3,10]-FA112*s.dpt[3,14]-OM110*OM310*(\
   s.In[1,10]-s.In[9,10]))
  CF310 = -(s.trq[3,10]+s.In[1,10]*OM110*OM210-s.In[9,10]*OpF310-CF11_212*S11-CF13_314*C13-CF214*S13-CF312*C11)
  FB110_1 = s.m[10]*AlM110_1
  FB210_1 = s.m[10]*AlM29_1
  FM110_1 = FB110_1+FB112_1+FB114_1*C14+FB314_1*S14
  FM210_1 = FB210_1+FB212_1*C11+FB214_1*C13-FB312_1*S11-FM131_314*S13
  FM310_1 = s.m[10]*AlM310_1+FB212_1*S11+FB214_1*S13+FB312_1*C11+FM131_314*C13
  CM110_1 = CM111_112-FB210_1*s.l[3,10]-s.dpt[3,14]*(FB212_1*C11-FB312_1*S11)
  CM210_1 = CM111_212*C11+FB110_1*s.l[3,10]+FB112_1*s.dpt[3,14]
  FB110_2 = s.m[10]*AlM110_2
  FB210_2 = s.m[10]*AlM29_2
  FM110_2 = FB110_2+FB112_2+FB114_2*C14+FB314_2*S14
  FM210_2 = FB210_2+FB212_2*C11+FB214_2*C13-FB312_2*S11-FM132_314*S13
  FM310_2 = s.m[10]*AlM310_2+FB212_2*S11+FB214_2*S13+FB312_2*C11+FM132_314*C13
  CM110_2 = CM112_112-FB210_2*s.l[3,10]-s.dpt[3,14]*(FB212_2*C11-FB312_2*S11)
  CM210_2 = CM112_212*C11+FB110_2*s.l[3,10]+FB112_2*s.dpt[3,14]
  FB110_3 = s.m[10]*AlM110_3
  FB210_3 = s.m[10]*AlM29_3
  FM110_3 = FB110_3+FB112_3+FB114_3*C14+FB314_3*S14
  FM210_3 = FB210_3+FB212_3*C11+FB214_3*C13-FB312_3*S11-FM133_314*S13
  FM310_3 = s.m[10]*AlM310_3+FB212_3*S11+FB214_3*S13+FB312_3*C11+FM133_314*C13
  CM110_3 = CM113_112-FB210_3*s.l[3,10]-s.dpt[3,14]*(FB212_3*C11-FB312_3*S11)
  CM210_3 = CM113_212*C11+FB110_3*s.l[3,10]+FB112_3*s.dpt[3,14]
  FB110_4 = s.m[10]*(AlM110_4+OpM29_4*s.l[3,10])
  FB210_4 = s.m[10]*(AlM29_4-OpM110_4*s.l[3,10])
  FM110_4 = FB110_4+FB112_4+FB114_4*C14+FB314_4*S14
  FM210_4 = FB210_4+FB212_4*C11+FB214_4*C13-FB312_4*S11-FM134_314*S13
  FM310_4 = s.m[10]*AlM310_4+FB212_4*S11+FB214_4*S13+FB312_4*C11+FM134_314*C13
  CM110_4 = CM114_112+CM134_114+s.In[1,10]*OpM110_4-FB210_4*s.l[3,10]-s.dpt[3,14]*(FB212_4*C11-FB312_4*S11)
  CM210_4 = CM114_212*C11-CM134_314*S13+CM214_4*C13-CM312_4*S11+FB110_4*s.l[3,10]+FB112_4*s.dpt[3,14]
  CM310_4 = s.In[9,10]*OpM310_4+CM114_212*S11+CM134_314*C13+CM214_4*S13+CM312_4*C11
  FB110_5 = s.m[10]*(AlM110_5+OpM29_5*s.l[3,10])
  FB210_5 = s.m[10]*(AlM29_5-OpM110_5*s.l[3,10])
  FM110_5 = FB110_5+FB112_5+FB114_5*C14+FB314_5*S14
  FM210_5 = FB210_5+FB212_5*C11+FB214_5*C13-FB312_5*S11-FM135_314*S13
  FM310_5 = s.m[10]*AlM310_5+FB212_5*S11+FB214_5*S13+FB312_5*C11+FM135_314*C13
  CM110_5 = CM115_112+CM135_114+s.In[1,10]*OpM110_5-FB210_5*s.l[3,10]-s.dpt[3,14]*(FB212_5*C11-FB312_5*S11)
  CM210_5 = CM115_212*C11-CM135_314*S13+CM214_5*C13-CM312_5*S11+FB110_5*s.l[3,10]+FB112_5*s.dpt[3,14]
  CM310_5 = s.In[9,10]*OpM310_5+CM115_212*S11+CM135_314*C13+CM214_5*S13+CM312_5*C11
  FB110_6 = s.m[10]*(AlM110_6+OpM29_6*s.l[3,10])
  FB210_6 = s.m[10]*(AlM29_6-OpM110_6*s.l[3,10])
  FM110_6 = FB110_6+FB112_6+FB114_6*C14+FB314_6*S14
  FM210_6 = FB210_6+FB212_6*C11+FB214_6*C13-FB312_6*S11-FM136_314*S13
  FM310_6 = s.m[10]*AlM310_6+FB212_6*S11+FB214_6*S13+FB312_6*C11+FM136_314*C13
  CM110_6 = CM116_112+CM136_114+s.In[1,10]*OpM110_6-FB210_6*s.l[3,10]-s.dpt[3,14]*(FB212_6*C11-FB312_6*S11)
  CM210_6 = CM116_212*C11-CM136_314*S13+CM214_6*C13-CM312_6*S11+FB110_6*s.l[3,10]+FB112_6*s.dpt[3,14]
  CM310_6 = s.In[9,10]*OpM310_6+CM116_212*S11+CM136_314*C13+CM214_6*S13+CM312_6*C11
  FB110_7 = s.m[10]*(AlM110_7+OpM29_7*s.l[3,10])
  FB210_7 = s.m[10]*(AlM29_7-OpM110_7*s.l[3,10])
  CM110_7 = CM117_112+CM137_114+s.In[1,10]*OpM110_7-FB210_7*s.l[3,10]-s.dpt[3,14]*(FB212_7*C11-FB312_7*S11)
  CM210_7 = CM117_212*C11-CM137_314*S13+CM214_7*C13-CM312_7*S11+FB110_7*s.l[3,10]+FB112_7*s.dpt[3,14]
  CM310_7 = s.In[9,10]*OpM310_7+CM117_212*S11+CM137_314*C13+CM214_7*S13+CM312_7*C11
  CM110_8 = CM118_112+CM138_114+s.In[1,10]*OpM110_8+s.m[10]*OpM110_8*s.l[3,10]*s.l[3,10]-s.dpt[3,14]*(FB212_8*C11-\
   FB312_8*S11)
  CM210_8 = s.m[10]*s.l[3,10]*s.l[3,10]*S9+CM118_212*C11-CM138_314*S13+CM214_8*C13-CM312_8*S11+FB112_8*s.dpt[3,14]
  CM310_8 = s.In[9,10]*OpM310_8+CM118_212*S11+CM138_314*C13+CM214_8*S13+CM312_8*C11
  CM210_9 = CM119_212*C11-CM139_314*S13+CM214_9*C13-CM312_9*S11+FB112_9*s.dpt[3,14]
  CM210_10 = s.In[9,12]*S11*S11+s.m[10]*s.l[3,10]*s.l[3,10]+CM214_10*C13+FB112_10*s.dpt[3,14]+C11*(q[12]*FB112_10+\
   s.In[5,12]*C11+FB112_10*s.l[3,12])+S13*(CM114_10*S14-CM314_10*C14)
  FF9_110 = FF110*C10+FF310*S10
  FF9_310 = -(FF110*S10-FF310*C10)
  CF9_110 = CF110*C10+CF310*S10
  CF9_310 = -(CF110*S10-CF310*C10)
  FM91_110 = FM110_1*C10+FM310_1*S10
  FM91_310 = -(FM110_1*S10-FM310_1*C10)
  CM91_110 = CM101_311*S10+CM110_1*C10
  CM91_310 = CM101_311*C10-CM110_1*S10
  FM92_110 = FM110_2*C10+FM310_2*S10
  FM92_310 = -(FM110_2*S10-FM310_2*C10)
  CM92_110 = CM102_311*S10+CM110_2*C10
  CM92_310 = CM102_311*C10-CM110_2*S10
  FM93_110 = FM110_3*C10+FM310_3*S10
  FM93_310 = -(FM110_3*S10-FM310_3*C10)
  CM93_110 = CM103_311*S10+CM110_3*C10
  CM93_310 = CM103_311*C10-CM110_3*S10
  FM94_110 = FM110_4*C10+FM310_4*S10
  FM94_310 = -(FM110_4*S10-FM310_4*C10)
  CM94_110 = CM110_4*C10+CM310_4*S10
  CM94_310 = -(CM110_4*S10-CM310_4*C10)
  FM95_110 = FM110_5*C10+FM310_5*S10
  FM95_310 = -(FM110_5*S10-FM310_5*C10)
  CM95_110 = CM110_5*C10+CM310_5*S10
  CM95_310 = -(CM110_5*S10-CM310_5*C10)
  FM96_310 = -(FM110_6*S10-FM310_6*C10)
  CM96_110 = CM110_6*C10+CM310_6*S10
  CM96_310 = -(CM110_6*S10-CM310_6*C10)
  CM97_110 = CM110_7*C10+CM310_7*S10
  CM97_310 = -(CM110_7*S10-CM310_7*C10)
  CM98_110 = CM110_8*C10+CM310_8*S10
  CM99_110 = C10*(CM119_112+CM139_114+s.In[1,10]*C10+s.m[10]*s.l[3,10]*s.l[3,10]*C10-s.dpt[3,14]*(FB212_9*C11-FB312_9*\
   S11))+S10*(s.In[9,10]*S10+CM119_212*S11+CM139_314*C13+CM214_9*S13+CM312_9*C11)
  FF8_29 = FF210*C9-FF9_310*S9
  FF8_39 = FF210*S9+FF9_310*C9
  CF8_29 = CF210*C9-CF9_310*S9
  CF8_39 = CF210*S9+CF9_310*C9
  FM81_29 = FM210_1*C9-FM91_310*S9
  FM81_39 = FM210_1*S9+FM91_310*C9
  CM81_29 = CM210_1*C9-CM91_310*S9
  CM81_39 = CM210_1*S9+CM91_310*C9
  FM82_29 = FM210_2*C9-FM92_310*S9
  FM82_39 = FM210_2*S9+FM92_310*C9
  CM82_29 = CM210_2*C9-CM92_310*S9
  CM82_39 = CM210_2*S9+CM92_310*C9
  FM83_29 = FM210_3*C9-FM93_310*S9
  FM83_39 = FM210_3*S9+FM93_310*C9
  CM83_29 = CM210_3*C9-CM93_310*S9
  CM83_39 = CM210_3*S9+CM93_310*C9
  FM84_29 = FM210_4*C9-FM94_310*S9
  FM84_39 = FM210_4*S9+FM94_310*C9
  CM84_29 = CM210_4*C9-CM94_310*S9
  CM84_39 = CM210_4*S9+CM94_310*C9
  FM85_29 = FM210_5*C9-FM95_310*S9
  FM85_39 = FM210_5*S9+FM95_310*C9
  CM85_29 = CM210_5*C9-CM95_310*S9
  CM85_39 = CM210_5*S9+CM95_310*C9
  FM86_39 = FM210_6*S9+FM96_310*C9
  CM86_39 = CM210_6*S9+CM96_310*C9
  CM87_39 = CM210_7*S9+CM97_310*C9
  CM88_39 = CM210_8*S9-C9*(CM110_8*S10-CM310_8*C10)
  FA17 = -(s.frc[1,7]-s.m[7]*(AlF17+BeF27*s.l[2,7]))
  FA37 = -(s.frc[3,7]-s.m[7]*(AlF37+BeF87*s.l[2,7]))
  FF17 = FA17-FF8_29*S8+FF9_110*C8
  FF27 = -(s.frc[2,7]-s.m[7]*(AlF27+BS57*s.l[2,7])-FF8_29*C8-FF9_110*S8)
  FF37 = FA37+FF8_39
  CF17 = -(s.trq[1,7]-s.In[1,7]*OpF15-s.In[9,7]*OM27*OM37+CF8_29*S8-CF9_110*C8-FA37*s.l[2,7]-FF8_39*s.dpt[2,13])
  CF27 = -(s.trq[2,7]-CF8_29*C8-CF9_110*S8-OM17*OM37*(s.In[1,7]-s.In[9,7]))
  CF37 = -(s.trq[3,7]-CF8_39+s.In[1,7]*OM17*OM27-s.In[9,7]*OpF37+FA17*s.l[2,7]-s.dpt[2,13]*(FF8_29*S8-FF9_110*C8))
  FB17_1 = s.m[7]*AlM15_1
  FB37_1 = s.m[7]*AlM37_1
  FM17_1 = FB17_1-FM81_29*S8+FM91_110*C8
  FM27_1 = s.m[7]*AlM27_1+FM81_29*C8+FM91_110*S8
  FM37_1 = FB37_1+FM81_39
  CM71_28 = CM81_29*C8+CM91_110*S8
  CM17_1 = -(CM81_29*S8-CM91_110*C8-FB37_1*s.l[2,7]-FM81_39*s.dpt[2,13])
  CM37_1 = CM81_39-FB17_1*s.l[2,7]+s.dpt[2,13]*(FM81_29*S8-FM91_110*C8)
  FB17_2 = s.m[7]*AlM15_2
  FB37_2 = s.m[7]*AlM37_2
  FM17_2 = FB17_2-FM82_29*S8+FM92_110*C8
  FM27_2 = s.m[7]*AlM27_2+FM82_29*C8+FM92_110*S8
  FM37_2 = FB37_2+FM82_39
  CM72_28 = CM82_29*C8+CM92_110*S8
  CM17_2 = -(CM82_29*S8-CM92_110*C8-FB37_2*s.l[2,7]-FM82_39*s.dpt[2,13])
  CM37_2 = CM82_39-FB17_2*s.l[2,7]+s.dpt[2,13]*(FM82_29*S8-FM92_110*C8)
  FB17_3 = -s.m[7]*S5
  FB37_3 = s.m[7]*AlM37_3
  FM17_3 = FB17_3-FM83_29*S8+FM93_110*C8
  FM27_3 = s.m[7]*AlM27_3+FM83_29*C8+FM93_110*S8
  FM37_3 = FB37_3+FM83_39
  CM73_28 = CM83_29*C8+CM93_110*S8
  CM17_3 = -(CM83_29*S8-CM93_110*C8-FB37_3*s.l[2,7]-FM83_39*s.dpt[2,13])
  CM37_3 = CM83_39-FB17_3*s.l[2,7]+s.dpt[2,13]*(FM83_29*S8-FM93_110*C8)
  FB17_4 = s.m[7]*(AlM17_4-OpM37_4*s.l[2,7])
  FB37_4 = s.m[7]*(AlM37_4-s.l[2,7]*S5)
  FM17_4 = FB17_4-FM84_29*S8+FM94_110*C8
  FM27_4 = s.m[7]*AlM27_4+FM84_29*C8+FM94_110*S8
  FM37_4 = FB37_4+FM84_39
  CM74_28 = CM84_29*C8+CM94_110*S8
  CM17_4 = -(s.In[1,7]*S5+CM84_29*S8-CM94_110*C8-FB37_4*s.l[2,7]-FM84_39*s.dpt[2,13])
  CM37_4 = CM84_39+s.In[9,7]*OpM37_4-FB17_4*s.l[2,7]+s.dpt[2,13]*(FM84_29*S8-FM94_110*C8)
  FB17_5 = s.m[7]*(AlM17_5+s.l[2,7]*S6p7)
  FB37_5 = s.m[7]*AlM37_5
  FM17_5 = FB17_5-FM85_29*S8+FM95_110*C8
  FM27_5 = s.m[7]*AlM27_5+FM85_29*C8+FM95_110*S8
  FM37_5 = FB37_5+FM85_39
  CM75_28 = CM85_29*C8+CM95_110*S8
  CM17_5 = -(CM85_29*S8-CM95_110*C8-FB37_5*s.l[2,7]-FM85_39*s.dpt[2,13])
  CM37_5 = CM85_39-s.In[9,7]*S6p7-FB17_5*s.l[2,7]+s.dpt[2,13]*(FM85_29*S8-FM95_110*C8)
  FB37_6 = s.m[7]*(AlM37_6+s.l[2,7])
  FM27_6 = s.m[7]*AlM27_6+C8*(FM210_6*C9-FM96_310*S9)+S8*(FM110_6*C10+FM310_6*S10)
  FM37_6 = FB37_6+FM86_39
  CM17_6 = s.In[1,7]+CM96_110*C8+FB37_6*s.l[2,7]+FM86_39*s.dpt[2,13]-S8*(CM210_6*C9-CM96_310*S9)
  CM17_7 = s.In[1,7]+s.m[7]*s.l[2,7]*s.l[2,7]+CM97_110*C8+s.dpt[2,13]*(C9*(C10*(s.m[10]*AlM310_7+FB212_7*S11+FB214_7*S13\
   +FB312_7*C11+FM137_314*C13)-S10*(FB110_7+FB112_7+FB114_7*C14+FB314_7*S14))+S9*(FB210_7+FB212_7*C11+FB214_7*C13-FB312_7*S11-\
   FM137_314*S13))-S8*(CM210_7*C9-CM97_310*S9)

# = = Block_0_2_0_2_0_5 = = 
 
# Backward Dynamics 

  FA118 = -(s.frc[1,18]-s.m[18]*(AlF118+BeF318*s.l[3,18]))
  FA218 = -(s.frc[2,18]-s.m[18]*(AlF217+BeF618*s.l[3,18]))
  FF118 = FA118+FA120+FA122*C22+FA322*S22
  FF218 = FA218+FA220*C19+FA222*C21-FA320*S19-FF21_322*S21
  FF318 = -(s.frc[3,18]-s.m[18]*(AlF318+BS918*s.l[3,18])-FA220*S19-FA222*S21-FA320*C19-FF21_322*C21)
  CF118 = -(s.trq[1,18]-CF19_120-CF21_122-s.In[1,18]*OpF118-s.In[9,18]*OM218*OM318+FA218*s.l[3,18]+s.dpt[3,19]*(FA220*\
   C19-FA320*S19))
  CF218 = -(s.trq[2,18]-CF19_220*C19+CF21_322*S21-CF222*C21+CF320*S19-FA118*s.l[3,18]-FA120*s.dpt[3,19]-OM118*OM318*(\
   s.In[1,18]-s.In[9,18]))
  CF318 = -(s.trq[3,18]+s.In[1,18]*OM118*OM218-s.In[9,18]*OpF318-CF19_220*S19-CF21_322*C21-CF222*S21-CF320*C19)
  FB118_1 = s.m[18]*AlM118_1
  FB218_1 = s.m[18]*AlM217_1
  FM118_1 = FB118_1+FB120_1+FB122_1*C22+FB322_1*S22
  FM218_1 = FB218_1+FB220_1*C19+FB222_1*C21-FB320_1*S19-FM211_322*S21
  FM318_1 = s.m[18]*AlM318_1+FB220_1*S19+FB222_1*S21+FB320_1*C19+FM211_322*C21
  CM118_1 = CM191_120-FB218_1*s.l[3,18]-s.dpt[3,19]*(FB220_1*C19-FB320_1*S19)
  CM218_1 = CM191_220*C19+FB118_1*s.l[3,18]+FB120_1*s.dpt[3,19]
  FB118_2 = s.m[18]*AlM118_2
  FB218_2 = s.m[18]*AlM217_2
  FM118_2 = FB118_2+FB120_2+FB122_2*C22+FB322_2*S22
  FM218_2 = FB218_2+FB220_2*C19+FB222_2*C21-FB320_2*S19-FM212_322*S21
  FM318_2 = s.m[18]*AlM318_2+FB220_2*S19+FB222_2*S21+FB320_2*C19+FM212_322*C21
  CM118_2 = CM192_120-FB218_2*s.l[3,18]-s.dpt[3,19]*(FB220_2*C19-FB320_2*S19)
  CM218_2 = CM192_220*C19+FB118_2*s.l[3,18]+FB120_2*s.dpt[3,19]
  FB118_3 = s.m[18]*AlM118_3
  FB218_3 = s.m[18]*AlM217_3
  FM118_3 = FB118_3+FB120_3+FB122_3*C22+FB322_3*S22
  FM218_3 = FB218_3+FB220_3*C19+FB222_3*C21-FB320_3*S19-FM213_322*S21
  FM318_3 = s.m[18]*AlM318_3+FB220_3*S19+FB222_3*S21+FB320_3*C19+FM213_322*C21
  CM118_3 = CM193_120-FB218_3*s.l[3,18]-s.dpt[3,19]*(FB220_3*C19-FB320_3*S19)
  CM218_3 = CM193_220*C19+FB118_3*s.l[3,18]+FB120_3*s.dpt[3,19]
  FB118_4 = s.m[18]*(AlM118_4+OpM217_4*s.l[3,18])
  FB218_4 = s.m[18]*(AlM217_4-OpM118_4*s.l[3,18])
  FM118_4 = FB118_4+FB120_4+FB122_4*C22+FB322_4*S22
  FM218_4 = FB218_4+FB220_4*C19+FB222_4*C21-FB320_4*S19-FM214_322*S21
  FM318_4 = s.m[18]*AlM318_4+FB220_4*S19+FB222_4*S21+FB320_4*C19+FM214_322*C21
  CM118_4 = CM194_120+CM214_122+s.In[1,18]*OpM118_4-FB218_4*s.l[3,18]-s.dpt[3,19]*(FB220_4*C19-FB320_4*S19)
  CM218_4 = CM194_220*C19-CM214_322*S21+CM222_4*C21-CM320_4*S19+FB118_4*s.l[3,18]+FB120_4*s.dpt[3,19]
  CM318_4 = s.In[9,18]*OpM318_4+CM194_220*S19+CM214_322*C21+CM222_4*S21+CM320_4*C19
  FB118_5 = s.m[18]*(AlM118_5+OpM217_5*s.l[3,18])
  FB218_5 = s.m[18]*(AlM217_5-OpM118_5*s.l[3,18])
  FM118_5 = FB118_5+FB120_5+FB122_5*C22+FB322_5*S22
  FM218_5 = FB218_5+FB220_5*C19+FB222_5*C21-FB320_5*S19-FM215_322*S21
  FM318_5 = s.m[18]*AlM318_5+FB220_5*S19+FB222_5*S21+FB320_5*C19+FM215_322*C21
  CM118_5 = CM195_120+CM215_122+s.In[1,18]*OpM118_5-FB218_5*s.l[3,18]-s.dpt[3,19]*(FB220_5*C19-FB320_5*S19)
  CM218_5 = CM195_220*C19-CM215_322*S21+CM222_5*C21-CM320_5*S19+FB118_5*s.l[3,18]+FB120_5*s.dpt[3,19]
  CM318_5 = s.In[9,18]*OpM318_5+CM195_220*S19+CM215_322*C21+CM222_5*S21+CM320_5*C19
  FB118_6 = s.m[18]*(AlM118_6+OpM217_6*s.l[3,18])
  FB218_6 = s.m[18]*(AlM217_6-OpM118_6*s.l[3,18])
  FM118_6 = FB118_6+FB120_6+FB122_6*C22+FB322_6*S22
  FM218_6 = FB218_6+FB220_6*C19+FB222_6*C21-FB320_6*S19-FM216_322*S21
  FM318_6 = s.m[18]*AlM318_6+FB220_6*S19+FB222_6*S21+FB320_6*C19+FM216_322*C21
  CM118_6 = CM196_120+CM216_122+s.In[1,18]*OpM118_6-FB218_6*s.l[3,18]-s.dpt[3,19]*(FB220_6*C19-FB320_6*S19)
  CM218_6 = CM196_220*C19-CM216_322*S21+CM222_6*C21-CM320_6*S19+FB118_6*s.l[3,18]+FB120_6*s.dpt[3,19]
  CM318_6 = s.In[9,18]*OpM318_6+CM196_220*S19+CM216_322*C21+CM222_6*S21+CM320_6*C19
  FB118_15 = s.m[18]*(AlM118_15+OpM217_15*s.l[3,18])
  FB218_15 = s.m[18]*(AlM217_15-OpM118_15*s.l[3,18])
  CM118_15 = CM1915_120+CM2115_122+s.In[1,18]*OpM118_15-FB218_15*s.l[3,18]-s.dpt[3,19]*(FB220_15*C19-FB320_15*S19)
  CM218_15 = CM1915_220*C19-CM2115_322*S21+CM222_15*C21-CM320_15*S19+FB118_15*s.l[3,18]+FB120_15*s.dpt[3,19]
  CM318_15 = s.In[9,18]*OpM318_15+CM1915_220*S19+CM2115_322*C21+CM222_15*S21+CM320_15*C19
  CM118_16 = CM1916_120+CM2116_122+s.In[1,18]*OpM118_16+s.m[18]*OpM118_16*s.l[3,18]*s.l[3,18]-s.dpt[3,19]*(FB220_16*C19-\
   FB320_16*S19)
  CM218_16 = s.m[18]*s.l[3,18]*s.l[3,18]*S17+CM1916_220*C19-CM2116_322*S21+CM222_16*C21-CM320_16*S19+FB120_16*\
   s.dpt[3,19]
  CM318_16 = s.In[9,18]*OpM318_16+CM1916_220*S19+CM2116_322*C21+CM222_16*S21+CM320_16*C19
  CM218_17 = CM1917_220*C19-CM2117_322*S21+CM222_17*C21-CM320_17*S19+FB120_17*s.dpt[3,19]
  CM218_18 = s.In[9,20]*S19*S19+s.m[18]*s.l[3,18]*s.l[3,18]+CM222_18*C21+FB120_18*s.dpt[3,19]+C19*(q[20]*FB120_18+\
   s.In[5,20]*C19+FB120_18*s.l[3,20])+S21*(CM122_18*S22-CM322_18*C22)
  FF17_118 = FF118*C18+FF318*S18
  FF17_318 = -(FF118*S18-FF318*C18)
  CF17_118 = CF118*C18+CF318*S18
  CF17_318 = -(CF118*S18-CF318*C18)
  FM171_118 = FM118_1*C18+FM318_1*S18
  FM171_318 = -(FM118_1*S18-FM318_1*C18)
  CM171_118 = CM118_1*C18+CM181_319*S18
  CM171_318 = -(CM118_1*S18-CM181_319*C18)
  FM172_118 = FM118_2*C18+FM318_2*S18
  FM172_318 = -(FM118_2*S18-FM318_2*C18)
  CM172_118 = CM118_2*C18+CM182_319*S18
  CM172_318 = -(CM118_2*S18-CM182_319*C18)
  FM173_118 = FM118_3*C18+FM318_3*S18
  FM173_318 = -(FM118_3*S18-FM318_3*C18)
  CM173_118 = CM118_3*C18+CM183_319*S18
  CM173_318 = -(CM118_3*S18-CM183_319*C18)
  FM174_118 = FM118_4*C18+FM318_4*S18
  FM174_318 = -(FM118_4*S18-FM318_4*C18)
  CM174_118 = CM118_4*C18+CM318_4*S18
  CM174_318 = -(CM118_4*S18-CM318_4*C18)
  FM175_118 = FM118_5*C18+FM318_5*S18
  FM175_318 = -(FM118_5*S18-FM318_5*C18)
  CM175_118 = CM118_5*C18+CM318_5*S18
  CM175_318 = -(CM118_5*S18-CM318_5*C18)
  FM176_318 = -(FM118_6*S18-FM318_6*C18)
  CM176_118 = CM118_6*C18+CM318_6*S18
  CM176_318 = -(CM118_6*S18-CM318_6*C18)
  CM1715_118 = CM118_15*C18+CM318_15*S18
  CM1715_318 = -(CM118_15*S18-CM318_15*C18)
  CM1716_118 = CM118_16*C18+CM318_16*S18
  CM1717_118 = C18*(CM1917_120+CM2117_122+s.In[1,18]*C18+s.m[18]*s.l[3,18]*s.l[3,18]*C18-s.dpt[3,19]*(FB220_17*C19-\
   FB320_17*S19))+S18*(s.In[9,18]*S18+CM1917_220*S19+CM2117_322*C21+CM222_17*S21+CM320_17*C19)
  FF16_217 = -(FF17_318*S17-FF218*C17)
  FF16_317 = FF17_318*C17+FF218*S17
  CF16_217 = -(CF17_318*S17-CF218*C17)
  CF16_317 = CF17_318*C17+CF218*S17
  FM161_217 = -(FM171_318*S17-FM218_1*C17)
  FM161_317 = FM171_318*C17+FM218_1*S17
  CM161_217 = -(CM171_318*S17-CM218_1*C17)
  CM161_317 = CM171_318*C17+CM218_1*S17
  FM162_217 = -(FM172_318*S17-FM218_2*C17)
  FM162_317 = FM172_318*C17+FM218_2*S17
  CM162_217 = -(CM172_318*S17-CM218_2*C17)
  CM162_317 = CM172_318*C17+CM218_2*S17
  FM163_217 = -(FM173_318*S17-FM218_3*C17)
  FM163_317 = FM173_318*C17+FM218_3*S17
  CM163_217 = -(CM173_318*S17-CM218_3*C17)
  CM163_317 = CM173_318*C17+CM218_3*S17
  FM164_217 = -(FM174_318*S17-FM218_4*C17)
  FM164_317 = FM174_318*C17+FM218_4*S17
  CM164_217 = -(CM174_318*S17-CM218_4*C17)
  CM164_317 = CM174_318*C17+CM218_4*S17
  FM165_217 = -(FM175_318*S17-FM218_5*C17)
  FM165_317 = FM175_318*C17+FM218_5*S17
  CM165_217 = -(CM175_318*S17-CM218_5*C17)
  CM165_317 = CM175_318*C17+CM218_5*S17
  FM166_317 = FM176_318*C17+FM218_6*S17
  CM166_317 = CM176_318*C17+CM218_6*S17
  CM1615_317 = CM1715_318*C17+CM218_15*S17
  CM1616_317 = CM218_16*S17-C17*(CM118_16*S18-CM318_16*C18)
  FA115 = -(s.frc[1,15]-s.m[15]*(AlF115+BeF215*s.l[2,15]))
  FA315 = -(s.frc[3,15]-s.m[15]*(AlF315+BeF815*s.l[2,15]))
  FF115 = FA115-FF16_217*S16+FF17_118*C16
  FF215 = -(s.frc[2,15]-s.m[15]*(AlF215+BS515*s.l[2,15])-FF16_217*C16-FF17_118*S16)
  FF315 = FA315+FF16_317
  CF115 = -(s.trq[1,15]-s.In[1,15]*OpF15-s.In[9,15]*OM215*OM315+CF16_217*S16-CF17_118*C16-FA315*s.l[2,15]-FF16_317*\
   s.dpt[2,18])
  CF215 = -(s.trq[2,15]-CF16_217*C16-CF17_118*S16-OM115*OM315*(s.In[1,15]-s.In[9,15]))
  CF315 = -(s.trq[3,15]-CF16_317+s.In[1,15]*OM115*OM215-s.In[9,15]*OpF315+FA115*s.l[2,15]-s.dpt[2,18]*(FF16_217*S16-\
   FF17_118*C16))
  FB115_1 = s.m[15]*AlM15_1
  FB315_1 = s.m[15]*AlM315_1
  FM115_1 = FB115_1-FM161_217*S16+FM171_118*C16
  FM215_1 = s.m[15]*AlM215_1+FM161_217*C16+FM171_118*S16
  FM315_1 = FB315_1+FM161_317
  CM151_216 = CM161_217*C16+CM171_118*S16
  CM115_1 = -(CM161_217*S16-CM171_118*C16-FB315_1*s.l[2,15]-FM161_317*s.dpt[2,18])
  CM315_1 = CM161_317-FB115_1*s.l[2,15]+s.dpt[2,18]*(FM161_217*S16-FM171_118*C16)
  FB115_2 = s.m[15]*AlM15_2
  FB315_2 = s.m[15]*AlM315_2
  FM115_2 = FB115_2-FM162_217*S16+FM172_118*C16
  FM215_2 = s.m[15]*AlM215_2+FM162_217*C16+FM172_118*S16
  FM315_2 = FB315_2+FM162_317
  CM152_216 = CM162_217*C16+CM172_118*S16
  CM115_2 = -(CM162_217*S16-CM172_118*C16-FB315_2*s.l[2,15]-FM162_317*s.dpt[2,18])
  CM315_2 = CM162_317-FB115_2*s.l[2,15]+s.dpt[2,18]*(FM162_217*S16-FM172_118*C16)
  FB115_3 = -s.m[15]*S5
  FB315_3 = s.m[15]*AlM315_3
  FM115_3 = FB115_3-FM163_217*S16+FM173_118*C16
  FM215_3 = s.m[15]*AlM215_3+FM163_217*C16+FM173_118*S16
  FM315_3 = FB315_3+FM163_317
  CM153_216 = CM163_217*C16+CM173_118*S16
  CM115_3 = -(CM163_217*S16-CM173_118*C16-FB315_3*s.l[2,15]-FM163_317*s.dpt[2,18])
  CM315_3 = CM163_317-FB115_3*s.l[2,15]+s.dpt[2,18]*(FM163_217*S16-FM173_118*C16)
  FB115_4 = s.m[15]*(AlM115_4-OpM315_4*s.l[2,15])
  FB315_4 = s.m[15]*(AlM315_4-s.l[2,15]*S5)
  FM115_4 = FB115_4-FM164_217*S16+FM174_118*C16
  FM215_4 = s.m[15]*AlM215_4+FM164_217*C16+FM174_118*S16
  FM315_4 = FB315_4+FM164_317
  CM154_216 = CM164_217*C16+CM174_118*S16
  CM115_4 = -(s.In[1,15]*S5+CM164_217*S16-CM174_118*C16-FB315_4*s.l[2,15]-FM164_317*s.dpt[2,18])
  CM315_4 = CM164_317+s.In[9,15]*OpM315_4-FB115_4*s.l[2,15]+s.dpt[2,18]*(FM164_217*S16-FM174_118*C16)
  FB115_5 = s.m[15]*(AlM115_5+s.l[2,15]*S15p6)
  FB315_5 = s.m[15]*AlM315_5
  FM115_5 = FB115_5-FM165_217*S16+FM175_118*C16
  FM215_5 = s.m[15]*AlM215_5+FM165_217*C16+FM175_118*S16
  FM315_5 = FB315_5+FM165_317
  CM155_216 = CM165_217*C16+CM175_118*S16
  CM115_5 = -(CM165_217*S16-CM175_118*C16-FB315_5*s.l[2,15]-FM165_317*s.dpt[2,18])
  CM315_5 = CM165_317-s.In[9,15]*S15p6-FB115_5*s.l[2,15]+s.dpt[2,18]*(FM165_217*S16-FM175_118*C16)
  FB315_6 = s.m[15]*(AlM315_6+s.l[2,15])
  FM215_6 = s.m[15]*AlM215_6-C16*(FM176_318*S17-FM218_6*C17)+S16*(FM118_6*C18+FM318_6*S18)
  FM315_6 = FB315_6+FM166_317
  CM115_6 = s.In[1,15]+CM176_118*C16+FB315_6*s.l[2,15]+FM166_317*s.dpt[2,18]+S16*(CM176_318*S17-CM218_6*C17)
  CM115_15 = s.In[1,15]+s.m[15]*s.l[2,15]*s.l[2,15]+CM1715_118*C16+s.dpt[2,18]*(C17*(C18*(s.m[18]*AlM318_15+FB220_15*S19\
   +FB222_15*S21+FB320_15*C19+FM2115_322*C21)-S18*(FB118_15+FB120_15+FB122_15*C22+FB322_15*S22))+S17*(FB218_15+FB220_15*C19+\
   FB222_15*C21-FB320_15*S19-FM2115_322*S21))+S16*(CM1715_318*S17-CM218_15*C17)

# = = Block_0_2_0_2_0_8 = = 
 
# Backward Dynamics 

  FA126 = -(s.frc[1,26]-s.m[26]*(AlF126+BeF326*s.l[3,26]))
  FA226 = -(s.frc[2,26]-s.m[26]*(AlF226+BeF626*s.l[3,26]))
  FF126 = FA126+FA128+FF29_130
  FF226 = FA226+FA228*C27+FA230*C29-FA328*S27-FF29_330*S29
  FF326 = -(s.frc[3,26]-s.m[26]*(AlF325+BS926*s.l[3,26])-FA228*S27-FA230*S29-FA328*C27-FF29_330*C29)
  CF126 = -(s.trq[1,26]-CF27_128-CF29_130-s.In[1,26]*OpF126+FA226*s.l[3,26]+OM226*OM326*(s.In[5,26]-s.In[9,26])+\
   s.dpt[3,24]*(FA228*C27-FA328*S27)+s.dpt[3,25]*(FA230*C29-FF29_330*S29))
  CF226 = -(s.trq[2,26]-s.In[5,26]*OpF226-CF230*C29-CF27_228*C27+CF29_330*S29+CF328*S27-FA126*s.l[3,26]-FA128*\
   s.dpt[3,24]-FF29_130*s.dpt[3,25]-OM126*OM326*(s.In[1,26]-s.In[9,26]))
  CF326 = -(s.trq[3,26]-s.In[9,26]*OpF325-CF230*S29-CF27_228*S27-CF29_330*C29-CF328*C27+OM126*OM226*(s.In[1,26]-\
   s.In[5,26]))
  FB126_1 = s.m[26]*AlM126_1
  FB226_1 = s.m[26]*AlM226_1
  FM126_1 = FB126_1+FB128_1+FM291_130
  FM226_1 = FB226_1+FB228_1*C27+FB230_1*C29-FB328_1*S27-FM291_330*S29
  FM326_1 = s.m[26]*AlM325_1+FB228_1*S27+FB230_1*S29+FB328_1*C27+FM291_330*C29
  CM126_1 = CM271_128-FB226_1*s.l[3,26]-s.dpt[3,24]*(FB228_1*C27-FB328_1*S27)-s.dpt[3,25]*(FB230_1*C29-FM291_330*S29)
  CM226_1 = CM271_228*C27+FB126_1*s.l[3,26]+FB128_1*s.dpt[3,24]+FM291_130*s.dpt[3,25]
  FB126_2 = s.m[26]*AlM126_2
  FB226_2 = s.m[26]*AlM226_2
  FM126_2 = FB126_2+FB128_2+FM292_130
  FM226_2 = FB226_2+FB228_2*C27+FB230_2*C29-FB328_2*S27-FM292_330*S29
  FM326_2 = s.m[26]*AlM325_2+FB228_2*S27+FB230_2*S29+FB328_2*C27+FM292_330*C29
  CM126_2 = CM272_128-FB226_2*s.l[3,26]-s.dpt[3,24]*(FB228_2*C27-FB328_2*S27)-s.dpt[3,25]*(FB230_2*C29-FM292_330*S29)
  CM226_2 = CM272_228*C27+FB126_2*s.l[3,26]+FB128_2*s.dpt[3,24]+FM292_130*s.dpt[3,25]
  FB126_3 = s.m[26]*AlM126_3
  FB226_3 = s.m[26]*AlM226_3
  FM126_3 = FB126_3+FB128_3+FM293_130
  FM226_3 = FB226_3+FB228_3*C27+FB230_3*C29-FB328_3*S27-FM293_330*S29
  FM326_3 = s.m[26]*AlM325_3+FB228_3*S27+FB230_3*S29+FB328_3*C27+FM293_330*C29
  CM126_3 = CM273_128-FB226_3*s.l[3,26]-s.dpt[3,24]*(FB228_3*C27-FB328_3*S27)-s.dpt[3,25]*(FB230_3*C29-FM293_330*S29)
  CM226_3 = CM273_228*C27+FB126_3*s.l[3,26]+FB128_3*s.dpt[3,24]+FM293_130*s.dpt[3,25]
  FB126_4 = s.m[26]*(AlM126_4+OpM226_4*s.l[3,26])
  FB226_4 = s.m[26]*(AlM226_4-OpM126_4*s.l[3,26])
  FM126_4 = FB126_4+FB128_4+FM294_130
  FM226_4 = FB226_4+FB228_4*C27+FB230_4*C29-FB328_4*S27-FM294_330*S29
  FM326_4 = s.m[26]*AlM325_4+FB228_4*S27+FB230_4*S29+FB328_4*C27+FM294_330*C29
  CM126_4 = CM274_128+CM294_130+s.In[1,26]*OpM126_4-FB226_4*s.l[3,26]-s.dpt[3,24]*(FB228_4*C27-FB328_4*S27)-s.dpt[3,25]*\
   (FB230_4*C29-FM294_330*S29)
  CM226_4 = s.In[5,26]*OpM226_4+CM230_4*C29+CM274_228*C27-CM294_330*S29-CM328_4*S27+FB126_4*s.l[3,26]+FB128_4*\
   s.dpt[3,24]+FM294_130*s.dpt[3,25]
  CM326_4 = s.In[9,26]*OpM325_4+CM230_4*S29+CM274_228*S27+CM294_330*C29+CM328_4*C27
  FB126_5 = s.m[26]*(AlM126_5+OpM226_5*s.l[3,26])
  FB226_5 = s.m[26]*(AlM226_5-OpM126_5*s.l[3,26])
  FM126_5 = FB126_5+FB128_5+FM295_130
  FM226_5 = FB226_5+FB228_5*C27+FB230_5*C29-FB328_5*S27-FM295_330*S29
  FM326_5 = s.m[26]*AlM325_5+FB228_5*S27+FB230_5*S29+FB328_5*C27+FM295_330*C29
  CM126_5 = CM275_128+CM295_130+s.In[1,26]*OpM126_5-FB226_5*s.l[3,26]-s.dpt[3,24]*(FB228_5*C27-FB328_5*S27)-s.dpt[3,25]*\
   (FB230_5*C29-FM295_330*S29)
  CM226_5 = s.In[5,26]*OpM226_5+CM230_5*C29+CM275_228*C27-CM295_330*S29-CM328_5*S27+FB126_5*s.l[3,26]+FB128_5*\
   s.dpt[3,24]+FM295_130*s.dpt[3,25]
  CM326_5 = s.In[9,26]*OpM325_5+CM230_5*S29+CM275_228*S27+CM295_330*C29+CM328_5*C27
  FB126_6 = s.m[26]*(AlM126_6+OpM226_6*s.l[3,26])
  FB226_6 = s.m[26]*(AlM226_6-OpM126_6*s.l[3,26])
  FM126_6 = FB126_6+FB128_6+FM296_130
  FM226_6 = FB226_6+FB228_6*C27+FB230_6*C29-FB328_6*S27-FM296_330*S29
  FM326_6 = s.m[26]*AlM325_6+FB228_6*S27+FB230_6*S29+FB328_6*C27+FM296_330*C29
  CM126_6 = CM276_128+CM296_130+s.In[1,26]*OpM126_6-FB226_6*s.l[3,26]-s.dpt[3,24]*(FB228_6*C27-FB328_6*S27)-s.dpt[3,25]*\
   (FB230_6*C29-FM296_330*S29)
  CM226_6 = s.In[5,26]*OpM226_6+CM230_6*C29+CM276_228*C27-CM296_330*S29-CM328_6*S27+FB126_6*s.l[3,26]+FB128_6*\
   s.dpt[3,24]+FM296_130*s.dpt[3,25]
  CM326_6 = s.In[9,26]*OpM325_6+CM230_6*S29+CM276_228*S27+CM296_330*C29+CM328_6*C27
  FB126_23 = s.m[26]*(AlM126_23+OpM226_23*s.l[3,26])
  FB226_23 = s.m[26]*(AlM226_23-OpM126_23*s.l[3,26])
  FM126_23 = FB126_23+FB128_23+FM2923_130
  FM226_23 = FB226_23+FB228_23*C27+FB230_23*C29-FB328_23*S27-FM2923_330*S29
  CM126_23 = CM2723_128+CM2923_130+s.In[1,26]*OpM126_23-FB226_23*s.l[3,26]-s.dpt[3,24]*(FB228_23*C27-FB328_23*S27)-\
   s.dpt[3,25]*(FB230_23*C29-FM2923_330*S29)
  CM226_23 = s.In[5,26]*OpM226_23+CM230_23*C29+CM2723_228*C27-CM2923_330*S29-CM328_23*S27+FB126_23*s.l[3,26]+FB128_23*\
   s.dpt[3,24]+FM2923_130*s.dpt[3,25]
  CM326_23 = s.In[9,26]*OpM325_23+CM230_23*S29+CM2723_228*S27+CM2923_330*C29+CM328_23*C27
  FB126_24 = s.m[26]*(AlM126_24+OpM226_24*s.l[3,26])
  FB226_24 = s.m[26]*(AlM226_24-OpM126_24*s.l[3,26])
  CM126_24 = CM2724_128+CM2924_130+s.In[1,26]*OpM126_24-FB226_24*s.l[3,26]-s.dpt[3,24]*(FB228_24*C27-FB328_24*S27)-\
   s.dpt[3,25]*(FB230_24*C29-FM2924_330*S29)
  CM226_24 = s.In[5,26]*OpM226_24+CM230_24*C29+CM2724_228*C27-CM2924_330*S29-CM328_24*S27+FB126_24*s.l[3,26]+FB128_24*\
   s.dpt[3,24]+FM2924_130*s.dpt[3,25]
  CM326_24 = s.In[9,26]*C25+CM230_24*S29+CM2724_228*S27+CM2924_330*C29+CM328_24*C27
  CM326_25 = CM230_25*S29+CM2725_228*S27+CM2925_330*C29+CM328_25*C27
  CM326_26 = s.In[9,26]+s.In[9,28]*C27*C27+CM230_26*S29+S27*(q[28]*FB128_26+s.In[5,28]*S27+FB128_26*s.l[3,28])-C29*(\
   CM130_26*S30-CM330_26*C30)
  FF25_126 = FF126*C26-FF226*S26
  FF25_226 = FF126*S26+FF226*C26
  CF25_126 = CF126*C26-CF226*S26
  CF25_226 = CF126*S26+CF226*C26
  FM251_126 = FM126_1*C26-FM226_1*S26
  FM251_226 = FM126_1*S26+FM226_1*C26
  CM251_126 = CM126_1*C26-CM226_1*S26
  CM251_226 = CM126_1*S26+CM226_1*C26
  FM252_126 = FM126_2*C26-FM226_2*S26
  FM252_226 = FM126_2*S26+FM226_2*C26
  CM252_126 = CM126_2*C26-CM226_2*S26
  CM252_226 = CM126_2*S26+CM226_2*C26
  FM253_126 = FM126_3*C26-FM226_3*S26
  FM253_226 = FM126_3*S26+FM226_3*C26
  CM253_126 = CM126_3*C26-CM226_3*S26
  CM253_226 = CM126_3*S26+CM226_3*C26
  FM254_126 = FM126_4*C26-FM226_4*S26
  FM254_226 = FM126_4*S26+FM226_4*C26
  CM254_126 = CM126_4*C26-CM226_4*S26
  CM254_226 = CM126_4*S26+CM226_4*C26
  FM255_126 = FM126_5*C26-FM226_5*S26
  FM255_226 = FM126_5*S26+FM226_5*C26
  CM255_126 = CM126_5*C26-CM226_5*S26
  CM255_226 = CM126_5*S26+CM226_5*C26
  FM256_126 = FM126_6*C26-FM226_6*S26
  FM256_226 = FM126_6*S26+FM226_6*C26
  CM256_126 = CM126_6*C26-CM226_6*S26
  CM256_226 = CM126_6*S26+CM226_6*C26
  CM2523_126 = CM126_23*C26-CM226_23*S26
  CM2523_226 = CM126_23*S26+CM226_23*C26
  CM2524_126 = CM126_24*C26-CM226_24*S26
  CM2525_126 = C26*(CM2725_128+CM2925_130+s.In[1,26]*C26+s.m[26]*s.l[3,26]*s.l[3,26]*C26-s.dpt[3,24]*(FB228_25*C27-\
   FB328_25*S27)+s.dpt[3,25]*(s.m[30]*s.dpt[3,25]*C26*C29*C29-S29*(FB130_25*S30-FB330_25*C30)))-S26*(CM230_25*C29+CM2725_228*\
   C27-CM2925_330*S29-CM328_25*S27+FB128_25*s.dpt[3,24]+s.dpt[3,25]*(FB130_25*C30+FB330_25*S30)-S26*(s.In[5,26]+s.m[26]*\
   s.l[3,26]*s.l[3,26]))
  FA124 = -(s.frc[1,24]-s.m[24]*(AlF124+BeF224*s.l[2,24]))
  FA324 = -(s.frc[3,24]-s.m[24]*(AlF323+BeF824*s.l[2,24]))
  FF124 = FA124+FF25_126
  FF224 = -(s.frc[2,24]-s.m[24]*(AlF224+BS524*s.l[2,24])-FF25_226*C25+FF326*S25)
  FF324 = FA324+FF25_226*S25+FF326*C25
  CF124 = -(s.trq[1,24]-CF25_126-s.In[1,24]*OpF124-FA324*s.l[2,24]+OM224*OM324*(s.In[5,24]-s.In[9,24])-s.dpt[2,23]*(\
   FF25_226*S25+FF326*C25))
  CF224 = -(s.trq[2,24]-s.In[5,24]*OpF224-CF25_226*C25+CF326*S25-OM124*OM324*(s.In[1,24]-s.In[9,24]))
  CF324 = -(s.trq[3,24]-s.In[9,24]*OpF323-CF25_226*S25-CF326*C25+FA124*s.l[2,24]+FF25_126*s.dpt[2,23]+OM124*OM224*(\
   s.In[1,24]-s.In[5,24]))
  FB124_1 = s.m[24]*AlM124_1
  FB324_1 = s.m[24]*AlM323_1
  FM124_1 = FB124_1+FM251_126
  FM224_1 = s.m[24]*AlM224_1+FM251_226*C25-FM326_1*S25
  FM324_1 = FB324_1+FM251_226*S25+FM326_1*C25
  CM241_225 = CM251_226*C25-CM261_327*S25
  CM124_1 = CM251_126+FB324_1*s.l[2,24]+s.dpt[2,23]*(FM251_226*S25+FM326_1*C25)
  CM324_1 = CM251_226*S25+CM261_327*C25-FB124_1*s.l[2,24]-FM251_126*s.dpt[2,23]
  FB124_2 = s.m[24]*AlM124_2
  FB324_2 = s.m[24]*AlM323_2
  FM124_2 = FB124_2+FM252_126
  FM224_2 = s.m[24]*AlM224_2+FM252_226*C25-FM326_2*S25
  FM324_2 = FB324_2+FM252_226*S25+FM326_2*C25
  CM242_225 = CM252_226*C25-CM262_327*S25
  CM124_2 = CM252_126+FB324_2*s.l[2,24]+s.dpt[2,23]*(FM252_226*S25+FM326_2*C25)
  CM324_2 = CM252_226*S25+CM262_327*C25-FB124_2*s.l[2,24]-FM252_126*s.dpt[2,23]
  FB124_3 = s.m[24]*AlM124_3
  FB324_3 = s.m[24]*AlM323_3
  FM124_3 = FB124_3+FM253_126
  FM224_3 = s.m[24]*AlM224_3+FM253_226*C25-FM326_3*S25
  FM324_3 = FB324_3+FM253_226*S25+FM326_3*C25
  CM243_225 = CM253_226*C25-CM263_327*S25
  CM124_3 = CM253_126+FB324_3*s.l[2,24]+s.dpt[2,23]*(FM253_226*S25+FM326_3*C25)
  CM324_3 = CM253_226*S25+CM263_327*C25-FB124_3*s.l[2,24]-FM253_126*s.dpt[2,23]
  FB124_4 = s.m[24]*(AlM124_4-OpM323_4*s.l[2,24])
  FB324_4 = s.m[24]*(AlM323_4+OpM124_4*s.l[2,24])
  FM124_4 = FB124_4+FM254_126
  FM224_4 = s.m[24]*AlM224_4+FM254_226*C25-FM326_4*S25
  FM324_4 = FB324_4+FM254_226*S25+FM326_4*C25
  CM124_4 = CM254_126+s.In[1,24]*OpM124_4+FB324_4*s.l[2,24]+s.dpt[2,23]*(FM254_226*S25+FM326_4*C25)
  CM224_4 = s.In[5,24]*OpM224_4+CM254_226*C25-CM326_4*S25
  CM324_4 = s.In[9,24]*OpM323_4+CM254_226*S25+CM326_4*C25-FB124_4*s.l[2,24]-FM254_126*s.dpt[2,23]
  FB124_5 = s.m[24]*(AlM124_5+s.l[2,24]*S23p6)
  FB324_5 = s.m[24]*(AlM323_5+OpM124_5*s.l[2,24])
  FM124_5 = FB124_5+FM255_126
  FM224_5 = s.m[24]*AlM224_5+FM255_226*C25-FM326_5*S25
  FM324_5 = FB324_5+FM255_226*S25+FM326_5*C25
  CM124_5 = CM255_126+s.In[1,24]*OpM124_5+FB324_5*s.l[2,24]+s.dpt[2,23]*(FM255_226*S25+FM326_5*C25)
  CM224_5 = s.In[5,24]*OpM224_5+CM255_226*C25-CM326_5*S25
  CM324_5 = CM255_226*S25+CM326_5*C25-FM255_126*s.dpt[2,23]-s.In[9,24]*S23p6-FB124_5*s.l[2,24]
  FB124_6 = s.m[24]*AlM124_6
  FB324_6 = s.m[24]*(AlM323_6+s.l[2,24]*C24)
  CM324_6 = CM256_226*S25+CM326_6*C25-FB124_6*s.l[2,24]-FM256_126*s.dpt[2,23]
  CM2423_325 = CM2523_226*S25+CM326_23*C25-s.dpt[2,23]*(FM126_23*C26-FM226_23*S26)
  CM324_24 = s.In[9,24]+s.m[24]*s.l[2,24]*s.l[2,24]+CM326_24*C25-s.dpt[2,23]*(C26*(FB126_24+FB128_24+FM2924_130)-S26*(\
   FB226_24+FB228_24*C27+FB230_24*C29-FB328_24*S27-FM2924_330*S29))+S25*(CM126_24*S26+CM226_24*C26)
  FF23_124 = FF124*C24-FF224*S24
  FF23_224 = FF124*S24+FF224*C24
  CF23_124 = CF124*C24-CF224*S24
  CF23_224 = CF124*S24+CF224*C24
  FM231_124 = FM124_1*C24-FM224_1*S24
  FM231_224 = FM124_1*S24+FM224_1*C24
  CM231_124 = CM124_1*C24-CM241_225*S24
  CM231_224 = CM124_1*S24+CM241_225*C24
  FM232_124 = FM124_2*C24-FM224_2*S24
  FM232_224 = FM124_2*S24+FM224_2*C24
  CM232_124 = CM124_2*C24-CM242_225*S24
  CM232_224 = CM124_2*S24+CM242_225*C24
  FM233_124 = FM124_3*C24-FM224_3*S24
  FM233_224 = FM124_3*S24+FM224_3*C24
  CM233_124 = CM124_3*C24-CM243_225*S24
  CM233_224 = CM124_3*S24+CM243_225*C24
  FM234_224 = FM124_4*S24+FM224_4*C24
  CM234_124 = CM124_4*C24-CM224_4*S24
  CM234_224 = CM124_4*S24+CM224_4*C24
  FM235_224 = FM124_5*S24+FM224_5*C24
  CM235_124 = CM124_5*C24-CM224_5*S24
  CM235_224 = CM124_5*S24+CM224_5*C24
  CM236_124 = C24*(CM256_126+s.In[1,24]*C24+FB324_6*s.l[2,24]+s.dpt[2,23]*(FM256_226*S25+FM326_6*C25))+S24*(s.In[5,24]*\
   S24-CM256_226*C25+CM326_6*S25)
  CM2323_124 = C24*(CM2523_126+s.In[1,24]*C24+s.m[24]*s.l[2,24]*s.l[2,24]*C24+s.dpt[2,23]*(C25*(s.m[26]*AlM325_23+\
   FB228_23*S27+FB230_23*S29+FB328_23*C27+FM2923_330*C29)+S25*(FM126_23*S26+FM226_23*C26)))+S24*(s.In[5,24]*S24-CM2523_226*C25+\
   CM326_23*S25)

# = = Block_0_2_0_2_0_11 = = 
 
# Backward Dynamics 

  FA134 = -(s.frc[1,34]-s.m[34]*(AlF134+BeF334*s.l[3,34]))
  FA234 = -(s.frc[2,34]-s.m[34]*(AlF234+BeF634*s.l[3,34]))
  FF134 = FA134+FA136+FF37_138
  FF234 = FA234+FA236*C35+FA238*C37-FA336*S35-FF37_338*S37
  FF334 = -(s.frc[3,34]-s.m[34]*(AlF333+BS934*s.l[3,34])-FA236*S35-FA238*S37-FA336*C35-FF37_338*C37)
  CF134 = -(s.trq[1,34]-CF35_136-CF37_138-s.In[1,34]*OpF134+FA234*s.l[3,34]+OM234*OM334*(s.In[5,34]-s.In[9,34])+\
   s.dpt[3,33]*(FA236*C35-FA336*S35)+s.dpt[3,34]*(FA238*C37-FF37_338*S37))
  CF234 = -(s.trq[2,34]-s.In[5,34]*OpF234-CF238*C37+CF336*S35-CF35_236*C35+CF37_338*S37-FA134*s.l[3,34]-FA136*\
   s.dpt[3,33]-FF37_138*s.dpt[3,34]-OM134*OM334*(s.In[1,34]-s.In[9,34]))
  CF334 = -(s.trq[3,34]-s.In[9,34]*OpF333-CF238*S37-CF336*C35-CF35_236*S35-CF37_338*C37+OM134*OM234*(s.In[1,34]-\
   s.In[5,34]))
  FB134_1 = s.m[34]*AlM134_1
  FB234_1 = s.m[34]*AlM234_1
  FM134_1 = FB134_1+FB136_1+FM371_138
  FM234_1 = FB234_1+FB236_1*C35+FB238_1*C37-FB336_1*S35-FM371_338*S37
  FM334_1 = s.m[34]*AlM333_1+FB236_1*S35+FB238_1*S37+FB336_1*C35+FM371_338*C37
  CM134_1 = CM351_136-FB234_1*s.l[3,34]-s.dpt[3,33]*(FB236_1*C35-FB336_1*S35)-s.dpt[3,34]*(FB238_1*C37-FM371_338*S37)
  CM234_1 = CM351_236*C35+FB134_1*s.l[3,34]+FB136_1*s.dpt[3,33]+FM371_138*s.dpt[3,34]
  FB134_2 = s.m[34]*AlM134_2
  FB234_2 = s.m[34]*AlM234_2
  FM134_2 = FB134_2+FB136_2+FM372_138
  FM234_2 = FB234_2+FB236_2*C35+FB238_2*C37-FB336_2*S35-FM372_338*S37
  FM334_2 = s.m[34]*AlM333_2+FB236_2*S35+FB238_2*S37+FB336_2*C35+FM372_338*C37
  CM134_2 = CM352_136-FB234_2*s.l[3,34]-s.dpt[3,33]*(FB236_2*C35-FB336_2*S35)-s.dpt[3,34]*(FB238_2*C37-FM372_338*S37)
  CM234_2 = CM352_236*C35+FB134_2*s.l[3,34]+FB136_2*s.dpt[3,33]+FM372_138*s.dpt[3,34]
  FB134_3 = s.m[34]*AlM134_3
  FB234_3 = s.m[34]*AlM234_3
  FM134_3 = FB134_3+FB136_3+FM373_138
  FM234_3 = FB234_3+FB236_3*C35+FB238_3*C37-FB336_3*S35-FM373_338*S37
  FM334_3 = s.m[34]*AlM333_3+FB236_3*S35+FB238_3*S37+FB336_3*C35+FM373_338*C37
  CM134_3 = CM353_136-FB234_3*s.l[3,34]-s.dpt[3,33]*(FB236_3*C35-FB336_3*S35)-s.dpt[3,34]*(FB238_3*C37-FM373_338*S37)
  CM234_3 = CM353_236*C35+FB134_3*s.l[3,34]+FB136_3*s.dpt[3,33]+FM373_138*s.dpt[3,34]
  FB134_4 = s.m[34]*(AlM134_4+OpM234_4*s.l[3,34])
  FB234_4 = s.m[34]*(AlM234_4-OpM134_4*s.l[3,34])
  FM134_4 = FB134_4+FB136_4+FM374_138
  FM234_4 = FB234_4+FB236_4*C35+FB238_4*C37-FB336_4*S35-FM374_338*S37
  FM334_4 = s.m[34]*AlM333_4+FB236_4*S35+FB238_4*S37+FB336_4*C35+FM374_338*C37
  CM134_4 = CM354_136+CM374_138+s.In[1,34]*OpM134_4-FB234_4*s.l[3,34]-s.dpt[3,33]*(FB236_4*C35-FB336_4*S35)-s.dpt[3,34]*\
   (FB238_4*C37-FM374_338*S37)
  CM234_4 = s.In[5,34]*OpM234_4+CM238_4*C37-CM336_4*S35+CM354_236*C35-CM374_338*S37+FB134_4*s.l[3,34]+FB136_4*\
   s.dpt[3,33]+FM374_138*s.dpt[3,34]
  CM334_4 = s.In[9,34]*OpM333_4+CM238_4*S37+CM336_4*C35+CM354_236*S35+CM374_338*C37
  FB134_5 = s.m[34]*(AlM134_5+OpM234_5*s.l[3,34])
  FB234_5 = s.m[34]*(AlM234_5-OpM134_5*s.l[3,34])
  FM134_5 = FB134_5+FB136_5+FM375_138
  FM234_5 = FB234_5+FB236_5*C35+FB238_5*C37-FB336_5*S35-FM375_338*S37
  FM334_5 = s.m[34]*AlM333_5+FB236_5*S35+FB238_5*S37+FB336_5*C35+FM375_338*C37
  CM134_5 = CM355_136+CM375_138+s.In[1,34]*OpM134_5-FB234_5*s.l[3,34]-s.dpt[3,33]*(FB236_5*C35-FB336_5*S35)-s.dpt[3,34]*\
   (FB238_5*C37-FM375_338*S37)
  CM234_5 = s.In[5,34]*OpM234_5+CM238_5*C37-CM336_5*S35+CM355_236*C35-CM375_338*S37+FB134_5*s.l[3,34]+FB136_5*\
   s.dpt[3,33]+FM375_138*s.dpt[3,34]
  CM334_5 = s.In[9,34]*OpM333_5+CM238_5*S37+CM336_5*C35+CM355_236*S35+CM375_338*C37
  FB134_6 = s.m[34]*(AlM134_6+OpM234_6*s.l[3,34])
  FB234_6 = s.m[34]*(AlM234_6-OpM134_6*s.l[3,34])
  FM134_6 = FB134_6+FB136_6+FM376_138
  FM234_6 = FB234_6+FB236_6*C35+FB238_6*C37-FB336_6*S35-FM376_338*S37
  FM334_6 = s.m[34]*AlM333_6+FB236_6*S35+FB238_6*S37+FB336_6*C35+FM376_338*C37
  CM134_6 = CM356_136+CM376_138+s.In[1,34]*OpM134_6-FB234_6*s.l[3,34]-s.dpt[3,33]*(FB236_6*C35-FB336_6*S35)-s.dpt[3,34]*\
   (FB238_6*C37-FM376_338*S37)
  CM234_6 = s.In[5,34]*OpM234_6+CM238_6*C37-CM336_6*S35+CM356_236*C35-CM376_338*S37+FB134_6*s.l[3,34]+FB136_6*\
   s.dpt[3,33]+FM376_138*s.dpt[3,34]
  CM334_6 = s.In[9,34]*OpM333_6+CM238_6*S37+CM336_6*C35+CM356_236*S35+CM376_338*C37
  FB134_31 = s.m[34]*(AlM134_31+OpM234_31*s.l[3,34])
  FB234_31 = s.m[34]*(AlM234_31-OpM134_31*s.l[3,34])
  FM134_31 = FB134_31+FB136_31+FM3731_138
  FM234_31 = FB234_31+FB236_31*C35+FB238_31*C37-FB336_31*S35-FM3731_338*S37
  CM134_31 = CM3531_136+CM3731_138+s.In[1,34]*OpM134_31-FB234_31*s.l[3,34]-s.dpt[3,33]*(FB236_31*C35-FB336_31*S35)-\
   s.dpt[3,34]*(FB238_31*C37-FM3731_338*S37)
  CM234_31 = s.In[5,34]*OpM234_31+CM238_31*C37-CM336_31*S35+CM3531_236*C35-CM3731_338*S37+FB134_31*s.l[3,34]+FB136_31*\
   s.dpt[3,33]+FM3731_138*s.dpt[3,34]
  CM334_31 = s.In[9,34]*OpM333_31+CM238_31*S37+CM336_31*C35+CM3531_236*S35+CM3731_338*C37
  FB134_32 = s.m[34]*(AlM134_32+OpM234_32*s.l[3,34])
  FB234_32 = s.m[34]*(AlM234_32-OpM134_32*s.l[3,34])
  CM134_32 = CM3532_136+CM3732_138+s.In[1,34]*OpM134_32-FB234_32*s.l[3,34]-s.dpt[3,33]*(FB236_32*C35-FB336_32*S35)-\
   s.dpt[3,34]*(FB238_32*C37-FM3732_338*S37)
  CM234_32 = s.In[5,34]*OpM234_32+CM238_32*C37-CM336_32*S35+CM3532_236*C35-CM3732_338*S37+FB134_32*s.l[3,34]+FB136_32*\
   s.dpt[3,33]+FM3732_138*s.dpt[3,34]
  CM334_32 = s.In[9,34]*C33+CM238_32*S37+CM336_32*C35+CM3532_236*S35+CM3732_338*C37
  CM334_33 = CM238_33*S37+CM336_33*C35+CM3533_236*S35+CM3733_338*C37
  CM334_34 = s.In[9,34]+s.In[9,36]*C35*C35+CM238_34*S37+S35*(q[36]*FB136_34+s.In[5,36]*S35+FB136_34*s.l[3,36])-C37*(\
   CM138_34*S38-CM338_34*C38)
  FF33_134 = FF134*C34-FF234*S34
  FF33_234 = FF134*S34+FF234*C34
  CF33_134 = CF134*C34-CF234*S34
  CF33_234 = CF134*S34+CF234*C34
  FM331_134 = FM134_1*C34-FM234_1*S34
  FM331_234 = FM134_1*S34+FM234_1*C34
  CM331_134 = CM134_1*C34-CM234_1*S34
  CM331_234 = CM134_1*S34+CM234_1*C34
  FM332_134 = FM134_2*C34-FM234_2*S34
  FM332_234 = FM134_2*S34+FM234_2*C34
  CM332_134 = CM134_2*C34-CM234_2*S34
  CM332_234 = CM134_2*S34+CM234_2*C34
  FM333_134 = FM134_3*C34-FM234_3*S34
  FM333_234 = FM134_3*S34+FM234_3*C34
  CM333_134 = CM134_3*C34-CM234_3*S34
  CM333_234 = CM134_3*S34+CM234_3*C34
  FM334_134 = FM134_4*C34-FM234_4*S34
  FM334_234 = FM134_4*S34+FM234_4*C34
  CM334_134 = CM134_4*C34-CM234_4*S34
  CM334_234 = CM134_4*S34+CM234_4*C34
  FM335_134 = FM134_5*C34-FM234_5*S34
  FM335_234 = FM134_5*S34+FM234_5*C34
  CM335_134 = CM134_5*C34-CM234_5*S34
  CM335_234 = CM134_5*S34+CM234_5*C34
  FM336_134 = FM134_6*C34-FM234_6*S34
  FM336_234 = FM134_6*S34+FM234_6*C34
  CM336_134 = CM134_6*C34-CM234_6*S34
  CM336_234 = CM134_6*S34+CM234_6*C34
  CM3331_134 = CM134_31*C34-CM234_31*S34
  CM3331_234 = CM134_31*S34+CM234_31*C34
  CM3332_134 = CM134_32*C34-CM234_32*S34
  CM3333_134 = C34*(CM3533_136+CM3733_138+s.In[1,34]*C34+s.m[34]*s.l[3,34]*s.l[3,34]*C34-s.dpt[3,33]*(FB236_33*C35-\
   FB336_33*S35)+s.dpt[3,34]*(s.m[38]*s.dpt[3,34]*C34*C37*C37-S37*(FB138_33*S38-FB338_33*C38)))-S34*(CM238_33*C37-CM336_33*S35+\
   CM3533_236*C35-CM3733_338*S37+FB136_33*s.dpt[3,33]+s.dpt[3,34]*(FB138_33*C38+FB338_33*S38)-S34*(s.In[5,34]+s.m[34]*s.l[3,34]\
   *s.l[3,34]))
  FA132 = -(s.frc[1,32]-s.m[32]*(AlF132+BeF232*s.l[2,32]))
  FA332 = -(s.frc[3,32]-s.m[32]*(AlF331+BeF832*s.l[2,32]))
  FF132 = FA132+FF33_134
  FF232 = -(s.frc[2,32]-s.m[32]*(AlF232+BS532*s.l[2,32])+FF334*S33-FF33_234*C33)
  FF332 = FA332+FF334*C33+FF33_234*S33
  CF132 = -(s.trq[1,32]-CF33_134-s.In[1,32]*OpF132-FA332*s.l[2,32]+OM232*OM332*(s.In[5,32]-s.In[9,32])-s.dpt[2,30]*(\
   FF334*C33+FF33_234*S33))
  CF232 = -(s.trq[2,32]-s.In[5,32]*OpF232+CF334*S33-CF33_234*C33-OM132*OM332*(s.In[1,32]-s.In[9,32]))
  CF332 = -(s.trq[3,32]-s.In[9,32]*OpF331-CF334*C33-CF33_234*S33+FA132*s.l[2,32]+FF33_134*s.dpt[2,30]+OM132*OM232*(\
   s.In[1,32]-s.In[5,32]))
  FB132_1 = s.m[32]*AlM132_1
  FB332_1 = s.m[32]*AlM331_1
  FM132_1 = FB132_1+FM331_134
  FM232_1 = s.m[32]*AlM232_1+FM331_234*C33-FM334_1*S33
  FM332_1 = FB332_1+FM331_234*S33+FM334_1*C33
  CM321_233 = CM331_234*C33-CM341_335*S33
  CM132_1 = CM331_134+FB332_1*s.l[2,32]+s.dpt[2,30]*(FM331_234*S33+FM334_1*C33)
  CM332_1 = CM331_234*S33+CM341_335*C33-FB132_1*s.l[2,32]-FM331_134*s.dpt[2,30]
  FB132_2 = s.m[32]*AlM132_2
  FB332_2 = s.m[32]*AlM331_2
  FM132_2 = FB132_2+FM332_134
  FM232_2 = s.m[32]*AlM232_2+FM332_234*C33-FM334_2*S33
  FM332_2 = FB332_2+FM332_234*S33+FM334_2*C33
  CM322_233 = CM332_234*C33-CM342_335*S33
  CM132_2 = CM332_134+FB332_2*s.l[2,32]+s.dpt[2,30]*(FM332_234*S33+FM334_2*C33)
  CM332_2 = CM332_234*S33+CM342_335*C33-FB132_2*s.l[2,32]-FM332_134*s.dpt[2,30]
  FB132_3 = s.m[32]*AlM132_3
  FB332_3 = s.m[32]*AlM331_3
  FM132_3 = FB132_3+FM333_134
  FM232_3 = s.m[32]*AlM232_3+FM333_234*C33-FM334_3*S33
  FM332_3 = FB332_3+FM333_234*S33+FM334_3*C33
  CM323_233 = CM333_234*C33-CM343_335*S33
  CM132_3 = CM333_134+FB332_3*s.l[2,32]+s.dpt[2,30]*(FM333_234*S33+FM334_3*C33)
  CM332_3 = CM333_234*S33+CM343_335*C33-FB132_3*s.l[2,32]-FM333_134*s.dpt[2,30]
  FB132_4 = s.m[32]*(AlM132_4-OpM331_4*s.l[2,32])
  FB332_4 = s.m[32]*(AlM331_4+OpM132_4*s.l[2,32])
  FM132_4 = FB132_4+FM334_134
  FM232_4 = s.m[32]*AlM232_4+FM334_234*C33-FM334_4*S33
  FM332_4 = FB332_4+FM334_234*S33+FM334_4*C33
  CM132_4 = CM334_134+s.In[1,32]*OpM132_4+FB332_4*s.l[2,32]+s.dpt[2,30]*(FM334_234*S33+FM334_4*C33)
  CM232_4 = s.In[5,32]*OpM232_4+CM334_234*C33-CM334_4*S33
  CM332_4 = s.In[9,32]*OpM331_4+CM334_234*S33+CM334_4*C33-FB132_4*s.l[2,32]-FM334_134*s.dpt[2,30]
  FB132_5 = s.m[32]*(AlM132_5+s.l[2,32]*S31p6)
  FB332_5 = s.m[32]*(AlM331_5+OpM132_5*s.l[2,32])
  FM132_5 = FB132_5+FM335_134
  FM232_5 = s.m[32]*AlM232_5-FM334_5*S33+FM335_234*C33
  FM332_5 = FB332_5+FM334_5*C33+FM335_234*S33
  CM132_5 = CM335_134+s.In[1,32]*OpM132_5+FB332_5*s.l[2,32]+s.dpt[2,30]*(FM334_5*C33+FM335_234*S33)
  CM232_5 = s.In[5,32]*OpM232_5-CM334_5*S33+CM335_234*C33
  CM332_5 = CM334_5*C33+CM335_234*S33-FM335_134*s.dpt[2,30]-s.In[9,32]*S31p6-FB132_5*s.l[2,32]
  FB132_6 = s.m[32]*AlM132_6
  FB332_6 = s.m[32]*(AlM331_6+s.l[2,32]*C32)
  CM332_6 = CM334_6*C33+CM336_234*S33-FB132_6*s.l[2,32]-FM336_134*s.dpt[2,30]
  CM3231_333 = CM3331_234*S33+CM334_31*C33-s.dpt[2,30]*(FM134_31*C34-FM234_31*S34)
  CM332_32 = s.In[9,32]+s.m[32]*s.l[2,32]*s.l[2,32]+CM334_32*C33-s.dpt[2,30]*(C34*(FB134_32+FB136_32+FM3732_138)-S34*(\
   FB234_32+FB236_32*C35+FB238_32*C37-FB336_32*S35-FM3732_338*S37))+S33*(CM134_32*S34+CM234_32*C34)
  FF31_132 = FF132*C32-FF232*S32
  FF31_232 = FF132*S32+FF232*C32
  CF31_132 = CF132*C32-CF232*S32
  CF31_232 = CF132*S32+CF232*C32
  FM311_132 = FM132_1*C32-FM232_1*S32
  FM311_232 = FM132_1*S32+FM232_1*C32
  CM311_132 = CM132_1*C32-CM321_233*S32
  CM311_232 = CM132_1*S32+CM321_233*C32
  FM312_132 = FM132_2*C32-FM232_2*S32
  FM312_232 = FM132_2*S32+FM232_2*C32
  CM312_132 = CM132_2*C32-CM322_233*S32
  CM312_232 = CM132_2*S32+CM322_233*C32
  FM313_132 = FM132_3*C32-FM232_3*S32
  FM313_232 = FM132_3*S32+FM232_3*C32
  CM313_132 = CM132_3*C32-CM323_233*S32
  CM313_232 = CM132_3*S32+CM323_233*C32
  FM314_232 = FM132_4*S32+FM232_4*C32
  CM314_132 = CM132_4*C32-CM232_4*S32
  CM314_232 = CM132_4*S32+CM232_4*C32
  FM315_232 = FM132_5*S32+FM232_5*C32
  CM315_132 = CM132_5*C32-CM232_5*S32
  CM315_232 = CM132_5*S32+CM232_5*C32
  CM316_132 = C32*(CM336_134+s.In[1,32]*C32+FB332_6*s.l[2,32]+s.dpt[2,30]*(FM334_6*C33+FM336_234*S33))+S32*(s.In[5,32]*\
   S32+CM334_6*S33-CM336_234*C33)
  CM3131_132 = C32*(CM3331_134+s.In[1,32]*C32+s.m[32]*s.l[2,32]*s.l[2,32]*C32+s.dpt[2,30]*(C33*(s.m[34]*AlM333_31+\
   FB236_31*S35+FB238_31*S37+FB336_31*C35+FM3731_338*C37)+S33*(FM134_31*S34+FM234_31*C34)))+S32*(s.In[5,32]*S32-CM3331_234*C33+\
   CM334_31*S33)

# = = Block_0_2_0_3_0_1 = = 
 
# Backward Dynamics 

  FA16 = -(s.frc[1,6]-s.m[6]*(AlF15+BeF36*s.l[3,6]))
  FA26 = -(s.frc[2,6]-s.m[6]*(AlF26+BeF66*s.l[3,6]))
  FF16 = FA16+FF115+FF17+FF23_124+FF31_132
  FF26 = FA26+FF215*C15+FF23_224*C23+FF27*C7-FF315*S15+FF31_232*C31-FF324*S23-FF332*S31-FF37*S7
  FF36 = -(s.frc[3,6]-s.m[6]*(AlF36+BS96*s.l[3,6])-FF215*S15-FF23_224*S23-FF27*S7-FF315*C15-FF31_232*S31-FF324*C23-FF332\
   *C31-FF37*C7)
  CF16 = -(s.trq[1,6]-CF115-CF17-CF23_124-CF31_132-s.In[1,6]*OpF15+FA26*s.l[3,6]+OM26*OM36*(s.In[5,6]-s.In[9,6])-\
   s.dpt[2,10]*(FF23_224*S23+FF324*C23)-s.dpt[2,12]*(FF31_232*S31+FF332*C31)-s.dpt[2,1]*(FF27*S7+FF37*C7)-s.dpt[2,4]*(FF215*S15\
   +FF315*C15)+s.dpt[3,1]*(FF27*C7-FF37*S7)+s.dpt[3,4]*(FF215*C15-FF315*S15))
  CF26 = -(s.trq[2,6]-s.In[5,6]*OpF26-CF215*C15-CF23_224*C23-CF27*C7+CF315*S15-CF31_232*C31+CF324*S23+CF332*S31+CF37*S7-\
   FA16*s.l[3,6]-FF115*s.dpt[3,4]-FF17*s.dpt[3,1]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,10]*(FF23_224*S23+FF324*C23)+\
   s.dpt[1,12]*(FF31_232*S31+FF332*C31)+s.dpt[1,1]*(FF27*S7+FF37*C7)+s.dpt[1,4]*(FF215*S15+FF315*C15))
  CF36 = -(s.trq[3,6]-s.In[9,6]*OpF36-CF215*S15-CF23_224*S23-CF27*S7-CF315*C15-CF31_232*S31-CF324*C23-CF332*C31-CF37*C7+\
   FF115*s.dpt[2,4]+FF17*s.dpt[2,1]+FF23_124*s.dpt[2,10]+FF31_132*s.dpt[2,12]+OM16*OM26*(s.In[1,6]-s.In[5,6])-s.dpt[1,10]*(\
   FF23_224*C23-FF324*S23)-s.dpt[1,12]*(FF31_232*C31-FF332*S31)-s.dpt[1,1]*(FF27*C7-FF37*S7)-s.dpt[1,4]*(FF215*C15-FF315*S15))
  FB16_1 = s.m[6]*AlM15_1
  FB26_1 = s.m[6]*AlM26_1
  FM16_1 = FB16_1+FM115_1+FM17_1+FM231_124+FM311_132
  FM26_1 = FB26_1+FM215_1*C15+FM231_224*C23+FM27_1*C7+FM311_232*C31-FM315_1*S15-FM324_1*S23-FM332_1*S31-FM37_1*S7
  FM36_1 = s.m[6]*AlM36_1+FM215_1*S15+FM231_224*S23+FM27_1*S7+FM311_232*S31+FM315_1*C15+FM324_1*C23+FM332_1*C31+FM37_1*\
   C7
  CM16_1 = CM115_1+CM17_1+CM231_124+CM311_132-FB26_1*s.l[3,6]+s.dpt[2,10]*(FM231_224*S23+FM324_1*C23)+s.dpt[2,12]*(\
   FM311_232*S31+FM332_1*C31)+s.dpt[2,1]*(FM27_1*S7+FM37_1*C7)+s.dpt[2,4]*(FM215_1*S15+FM315_1*C15)-s.dpt[3,1]*(FM27_1*C7-\
   FM37_1*S7)-s.dpt[3,4]*(FM215_1*C15-FM315_1*S15)
  CM26_1 = CM151_216*C15+CM231_224*C23+CM311_232*C31-CM315_1*S15-CM324_1*S23-CM332_1*S31-CM37_1*S7+CM71_28*C7+FB16_1*\
   s.l[3,6]+FM115_1*s.dpt[3,4]+FM17_1*s.dpt[3,1]-s.dpt[1,10]*(FM231_224*S23+FM324_1*C23)-s.dpt[1,12]*(FM311_232*S31+FM332_1*C31\
   )-s.dpt[1,1]*(FM27_1*S7+FM37_1*C7)-s.dpt[1,4]*(FM215_1*S15+FM315_1*C15)
  CM36_1 = CM151_216*S15+CM231_224*S23+CM311_232*S31+CM315_1*C15+CM324_1*C23+CM332_1*C31+CM37_1*C7+CM71_28*S7-FM115_1*\
   s.dpt[2,4]-FM17_1*s.dpt[2,1]-FM231_124*s.dpt[2,10]-FM311_132*s.dpt[2,12]+s.dpt[1,10]*(FM231_224*C23-FM324_1*S23)+s.dpt[1,12]\
   *(FM311_232*C31-FM332_1*S31)+s.dpt[1,1]*(FM27_1*C7-FM37_1*S7)+s.dpt[1,4]*(FM215_1*C15-FM315_1*S15)
  FB16_2 = s.m[6]*AlM15_2
  FB26_2 = s.m[6]*AlM26_2
  FM16_2 = FB16_2+FM115_2+FM17_2+FM232_124+FM312_132
  FM26_2 = FB26_2+FM215_2*C15+FM232_224*C23+FM27_2*C7+FM312_232*C31-FM315_2*S15-FM324_2*S23-FM332_2*S31-FM37_2*S7
  FM36_2 = s.m[6]*AlM36_2+FM215_2*S15+FM232_224*S23+FM27_2*S7+FM312_232*S31+FM315_2*C15+FM324_2*C23+FM332_2*C31+FM37_2*\
   C7
  CM16_2 = CM115_2+CM17_2+CM232_124+CM312_132-FB26_2*s.l[3,6]+s.dpt[2,10]*(FM232_224*S23+FM324_2*C23)+s.dpt[2,12]*(\
   FM312_232*S31+FM332_2*C31)+s.dpt[2,1]*(FM27_2*S7+FM37_2*C7)+s.dpt[2,4]*(FM215_2*S15+FM315_2*C15)-s.dpt[3,1]*(FM27_2*C7-\
   FM37_2*S7)-s.dpt[3,4]*(FM215_2*C15-FM315_2*S15)
  CM26_2 = CM152_216*C15+CM232_224*C23+CM312_232*C31-CM315_2*S15-CM324_2*S23-CM332_2*S31-CM37_2*S7+CM72_28*C7+FB16_2*\
   s.l[3,6]+FM115_2*s.dpt[3,4]+FM17_2*s.dpt[3,1]-s.dpt[1,10]*(FM232_224*S23+FM324_2*C23)-s.dpt[1,12]*(FM312_232*S31+FM332_2*C31\
   )-s.dpt[1,1]*(FM27_2*S7+FM37_2*C7)-s.dpt[1,4]*(FM215_2*S15+FM315_2*C15)
  CM36_2 = CM152_216*S15+CM232_224*S23+CM312_232*S31+CM315_2*C15+CM324_2*C23+CM332_2*C31+CM37_2*C7+CM72_28*S7-FM115_2*\
   s.dpt[2,4]-FM17_2*s.dpt[2,1]-FM232_124*s.dpt[2,10]-FM312_132*s.dpt[2,12]+s.dpt[1,10]*(FM232_224*C23-FM324_2*S23)+s.dpt[1,12]\
   *(FM312_232*C31-FM332_2*S31)+s.dpt[1,1]*(FM27_2*C7-FM37_2*S7)+s.dpt[1,4]*(FM215_2*C15-FM315_2*S15)
  FB16_3 = -s.m[6]*S5
  FB26_3 = s.m[6]*C5*S6
  CM16_3 = CM115_3+CM17_3+CM233_124+CM313_132-FB26_3*s.l[3,6]+s.dpt[2,10]*(FM233_224*S23+FM324_3*C23)+s.dpt[2,12]*(\
   FM313_232*S31+FM332_3*C31)+s.dpt[2,1]*(FM27_3*S7+FM37_3*C7)+s.dpt[2,4]*(FM215_3*S15+FM315_3*C15)-s.dpt[3,1]*(FM27_3*C7-\
   FM37_3*S7)-s.dpt[3,4]*(FM215_3*C15-FM315_3*S15)
  CM26_3 = CM153_216*C15+CM233_224*C23+CM313_232*C31-CM315_3*S15-CM324_3*S23-CM332_3*S31-CM37_3*S7+CM73_28*C7+FB16_3*\
   s.l[3,6]+FM115_3*s.dpt[3,4]+FM17_3*s.dpt[3,1]-s.dpt[1,10]*(FM233_224*S23+FM324_3*C23)-s.dpt[1,12]*(FM313_232*S31+FM332_3*C31\
   )-s.dpt[1,1]*(FM27_3*S7+FM37_3*C7)-s.dpt[1,4]*(FM215_3*S15+FM315_3*C15)
  CM36_3 = CM153_216*S15+CM233_224*S23+CM313_232*S31+CM315_3*C15+CM324_3*C23+CM332_3*C31+CM37_3*C7+CM73_28*S7-FM115_3*\
   s.dpt[2,4]-FM17_3*s.dpt[2,1]-FM233_124*s.dpt[2,10]-FM313_132*s.dpt[2,12]+s.dpt[1,10]*(FM233_224*C23-FM324_3*S23)+s.dpt[1,12]\
   *(FM313_232*C31-FM332_3*S31)+s.dpt[1,1]*(FM27_3*C7-FM37_3*S7)+s.dpt[1,4]*(FM215_3*C15-FM315_3*S15)
  CM16_4 = CM115_4+CM17_4+CM234_124+CM314_132-s.In[1,6]*S5-s.m[6]*s.l[3,6]*s.l[3,6]*S5+s.dpt[2,10]*(FM234_224*S23+\
   FM324_4*C23)+s.dpt[2,12]*(FM314_232*S31+FM332_4*C31)+s.dpt[2,1]*(FM27_4*S7+FM37_4*C7)+s.dpt[2,4]*(FM215_4*S15+FM315_4*C15)-\
   s.dpt[3,1]*(FM27_4*C7-FM37_4*S7)-s.dpt[3,4]*(FM215_4*C15-FM315_4*S15)
  CM26_4 = CM154_216*C15+CM234_224*C23+CM314_232*C31-CM315_4*S15-CM324_4*S23-CM332_4*S31-CM37_4*S7+CM74_28*C7+FM115_4*\
   s.dpt[3,4]+FM17_4*s.dpt[3,1]+OpM26_4*(s.In[5,6]+s.m[6]*s.l[3,6]*s.l[3,6])-s.dpt[1,10]*(FM234_224*S23+FM324_4*C23)-\
   s.dpt[1,12]*(FM314_232*S31+FM332_4*C31)-s.dpt[1,1]*(FM27_4*S7+FM37_4*C7)-s.dpt[1,4]*(FM215_4*S15+FM315_4*C15)
  CM36_4 = s.In[9,6]*OpM36_4+CM154_216*S15+CM234_224*S23+CM314_232*S31+CM315_4*C15+CM324_4*C23+CM332_4*C31+CM37_4*C7+\
   CM74_28*S7-FM115_4*s.dpt[2,4]-FM17_4*s.dpt[2,1]+s.dpt[1,10]*(FM234_224*C23-FM324_4*S23)+s.dpt[1,12]*(FM314_232*C31-FM332_4*\
   S31)+s.dpt[1,1]*(FM27_4*C7-FM37_4*S7)+s.dpt[1,4]*(FM215_4*C15-FM315_4*S15)-s.dpt[2,10]*(FM124_4*C24-FM224_4*S24)-s.dpt[2,12]\
   *(FM132_4*C32-FM232_4*S32)
  CM16_5 = CM115_5+CM17_5+CM235_124+CM315_132+s.dpt[2,10]*(FM235_224*S23+FM324_5*C23)+s.dpt[2,12]*(FM315_232*S31+FM332_5\
   *C31)+s.dpt[2,1]*(FM27_5*S7+FM37_5*C7)+s.dpt[2,4]*(FM215_5*S15+FM315_5*C15)-s.dpt[3,1]*(FM27_5*C7-FM37_5*S7)-s.dpt[3,4]*(\
   FM215_5*C15-FM315_5*S15)
  CM16_6 = s.In[1,6]+CM115_6+CM17_6+CM236_124+CM316_132+s.m[6]*s.l[3,6]*s.l[3,6]+s.dpt[2,10]*(C23*(FB324_6+FM256_226*S25\
   +FM326_6*C25)+S23*(C24*(s.m[24]*AlM224_6+FM256_226*C25-FM326_6*S25)+S24*(FB124_6+FM256_126)))+s.dpt[2,12]*(C31*(FB332_6+\
   FM334_6*C33+FM336_234*S33)+S31*(C32*(s.m[32]*AlM232_6-FM334_6*S33+FM336_234*C33)+S32*(FB132_6+FM336_134)))+s.dpt[2,1]*(\
   FM27_6*S7+FM37_6*C7)+s.dpt[2,4]*(FM215_6*S15+FM315_6*C15)-s.dpt[3,1]*(FM27_6*C7-FM37_6*S7)-s.dpt[3,4]*(FM215_6*C15-FM315_6*\
   S15)
  FF5_26 = FF26*C6-FF36*S6
  FF5_36 = FF26*S6+FF36*C6
  CF5_26 = CF26*C6-CF36*S6
  FM51_26 = FM26_1*C6-FM36_1*S6
  FM51_36 = FM26_1*S6+FM36_1*C6
  CM51_26 = CM26_1*C6-CM36_1*S6
  FM52_36 = FM26_2*S6+FM36_2*C6
  CM52_26 = CM26_2*C6-CM36_2*S6
  CM53_26 = CM26_3*C6-CM36_3*S6
  CM54_26 = CM26_4*C6-CM36_4*S6
  CM55_26 = C6*(CM155_216*C15+CM235_224*C23+CM315_232*C31-CM315_5*S15-CM324_5*S23-CM332_5*S31-CM37_5*S7+CM75_28*C7+\
   FM115_5*s.dpt[3,4]+FM17_5*s.dpt[3,1]-s.dpt[1,10]*(FM235_224*S23+FM324_5*C23)-s.dpt[1,12]*(FM315_232*S31+FM332_5*C31)-\
   s.dpt[1,1]*(FM27_5*S7+FM37_5*C7)-s.dpt[1,4]*(FM215_5*S15+FM315_5*C15)+C6*(s.In[5,6]+s.m[6]*s.l[3,6]*s.l[3,6]))+S6*(s.In[9,6]\
   *S6-CM155_216*S15-CM235_224*S23-CM315_232*S31-CM315_5*C15-CM324_5*C23-CM332_5*C31-CM37_5*C7-CM75_28*S7+FM115_5*s.dpt[2,4]+\
   FM17_5*s.dpt[2,1]-s.dpt[1,10]*(FM235_224*C23-FM324_5*S23)-s.dpt[1,12]*(FM315_232*C31-FM332_5*S31)-s.dpt[1,1]*(FM27_5*C7-\
   FM37_5*S7)-s.dpt[1,4]*(FM215_5*C15-FM315_5*S15)+s.dpt[2,10]*(FM124_5*C24-FM224_5*S24)+s.dpt[2,12]*(FM132_5*C32-FM232_5*S32))
  FF4_15 = FF16*C5+FF5_36*S5
  FF4_35 = -(FF16*S5-FF5_36*C5)
  CF4_35 = -(CF16*S5-C5*(CF26*S6+CF36*C6))
  FM41_15 = FM16_1*C5+FM51_36*S5
  FM41_35 = -(FM16_1*S5-FM51_36*C5)
  CM41_35 = -(CM16_1*S5-C5*(CM26_1*S6+CM36_1*C6))
  FM42_35 = -(FM16_2*S5-FM52_36*C5)
  CM42_35 = -(CM16_2*S5-C5*(CM26_2*S6+CM36_2*C6))
  FM43_35 = C5*(C6*(s.m[6]*C5*C6+FM215_3*S15+FM233_224*S23+FM27_3*S7+FM313_232*S31+FM315_3*C15+FM324_3*C23+FM332_3*C31+\
   FM37_3*C7)+S6*(FB26_3+FM215_3*C15+FM233_224*C23+FM27_3*C7+FM313_232*C31-FM315_3*S15-FM324_3*S23-FM332_3*S31-FM37_3*S7))-S5*(\
   FB16_3+FM115_3+FM17_3+FM233_124+FM313_132)
  CM43_35 = -(CM16_3*S5-C5*(CM26_3*S6+CM36_3*C6))
  CM44_35 = -(CM16_4*S5-C5*(CM26_4*S6+CM36_4*C6))
  FF3_14 = FF4_15*C4-FF5_26*S4
  FF3_24 = FF4_15*S4+FF5_26*C4
  FM31_14 = FM41_15*C4-FM51_26*S4
  FM31_24 = FM41_15*S4+FM51_26*C4
  FM32_24 = C4*(FM26_2*C6-FM36_2*S6)+S4*(FM16_2*C5+FM52_36*S5)

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  M[1,1] = FM31_14
  M[1,2] = FM31_24
  M[1,3] = FM41_35
  M[1,4] = CM41_35
  M[1,5] = CM51_26
  M[1,6] = CM16_1
  M[1,7] = CM17_1
  M[1,8] = CM81_39
  M[1,9] = CM91_110
  M[1,10] = CM210_1
  M[1,11] = CM111_112
  M[1,12] = FB312_1
  M[1,15] = CM115_1
  M[1,16] = CM161_317
  M[1,17] = CM171_118
  M[1,18] = CM218_1
  M[1,19] = CM191_120
  M[1,20] = FB320_1
  M[1,23] = CM231_124
  M[1,24] = CM324_1
  M[1,25] = CM251_126
  M[1,26] = CM261_327
  M[1,27] = CM271_128
  M[1,28] = FB328_1
  M[1,31] = CM311_132
  M[1,32] = CM332_1
  M[1,33] = CM331_134
  M[1,34] = CM341_335
  M[1,35] = CM351_136
  M[1,36] = FB336_1
  M[2,1] = FM31_24
  M[2,2] = FM32_24
  M[2,3] = FM42_35
  M[2,4] = CM42_35
  M[2,5] = CM52_26
  M[2,6] = CM16_2
  M[2,7] = CM17_2
  M[2,8] = CM82_39
  M[2,9] = CM92_110
  M[2,10] = CM210_2
  M[2,11] = CM112_112
  M[2,12] = FB312_2
  M[2,15] = CM115_2
  M[2,16] = CM162_317
  M[2,17] = CM172_118
  M[2,18] = CM218_2
  M[2,19] = CM192_120
  M[2,20] = FB320_2
  M[2,23] = CM232_124
  M[2,24] = CM324_2
  M[2,25] = CM252_126
  M[2,26] = CM262_327
  M[2,27] = CM272_128
  M[2,28] = FB328_2
  M[2,31] = CM312_132
  M[2,32] = CM332_2
  M[2,33] = CM332_134
  M[2,34] = CM342_335
  M[2,35] = CM352_136
  M[2,36] = FB336_2
  M[3,1] = FM41_35
  M[3,2] = FM42_35
  M[3,3] = FM43_35
  M[3,4] = CM43_35
  M[3,5] = CM53_26
  M[3,6] = CM16_3
  M[3,7] = CM17_3
  M[3,8] = CM83_39
  M[3,9] = CM93_110
  M[3,10] = CM210_3
  M[3,11] = CM113_112
  M[3,12] = FB312_3
  M[3,15] = CM115_3
  M[3,16] = CM163_317
  M[3,17] = CM173_118
  M[3,18] = CM218_3
  M[3,19] = CM193_120
  M[3,20] = FB320_3
  M[3,23] = CM233_124
  M[3,24] = CM324_3
  M[3,25] = CM253_126
  M[3,26] = CM263_327
  M[3,27] = CM273_128
  M[3,28] = FB328_3
  M[3,31] = CM313_132
  M[3,32] = CM332_3
  M[3,33] = CM333_134
  M[3,34] = CM343_335
  M[3,35] = CM353_136
  M[3,36] = FB336_3
  M[4,1] = CM41_35
  M[4,2] = CM42_35
  M[4,3] = CM43_35
  M[4,4] = CM44_35
  M[4,5] = CM54_26
  M[4,6] = CM16_4
  M[4,7] = CM17_4
  M[4,8] = CM84_39
  M[4,9] = CM94_110
  M[4,10] = CM210_4
  M[4,11] = CM114_112
  M[4,12] = FB312_4
  M[4,13] = CM134_114
  M[4,14] = CM214_4
  M[4,15] = CM115_4
  M[4,16] = CM164_317
  M[4,17] = CM174_118
  M[4,18] = CM218_4
  M[4,19] = CM194_120
  M[4,20] = FB320_4
  M[4,21] = CM214_122
  M[4,22] = CM222_4
  M[4,23] = CM234_124
  M[4,24] = CM324_4
  M[4,25] = CM254_126
  M[4,26] = CM326_4
  M[4,27] = CM274_128
  M[4,28] = FB328_4
  M[4,29] = CM294_130
  M[4,30] = CM230_4
  M[4,31] = CM314_132
  M[4,32] = CM332_4
  M[4,33] = CM334_134
  M[4,34] = CM334_4
  M[4,35] = CM354_136
  M[4,36] = FB336_4
  M[4,37] = CM374_138
  M[4,38] = CM238_4
  M[5,1] = CM51_26
  M[5,2] = CM52_26
  M[5,3] = CM53_26
  M[5,4] = CM54_26
  M[5,5] = CM55_26
  M[5,6] = CM16_5
  M[5,7] = CM17_5
  M[5,8] = CM85_39
  M[5,9] = CM95_110
  M[5,10] = CM210_5
  M[5,11] = CM115_112
  M[5,12] = FB312_5
  M[5,13] = CM135_114
  M[5,14] = CM214_5
  M[5,15] = CM115_5
  M[5,16] = CM165_317
  M[5,17] = CM175_118
  M[5,18] = CM218_5
  M[5,19] = CM195_120
  M[5,20] = FB320_5
  M[5,21] = CM215_122
  M[5,22] = CM222_5
  M[5,23] = CM235_124
  M[5,24] = CM324_5
  M[5,25] = CM255_126
  M[5,26] = CM326_5
  M[5,27] = CM275_128
  M[5,28] = FB328_5
  M[5,29] = CM295_130
  M[5,30] = CM230_5
  M[5,31] = CM315_132
  M[5,32] = CM332_5
  M[5,33] = CM335_134
  M[5,34] = CM334_5
  M[5,35] = CM355_136
  M[5,36] = FB336_5
  M[5,37] = CM375_138
  M[5,38] = CM238_5
  M[6,1] = CM16_1
  M[6,2] = CM16_2
  M[6,3] = CM16_3
  M[6,4] = CM16_4
  M[6,5] = CM16_5
  M[6,6] = CM16_6
  M[6,7] = CM17_6
  M[6,8] = CM86_39
  M[6,9] = CM96_110
  M[6,10] = CM210_6
  M[6,11] = CM116_112
  M[6,12] = FB312_6
  M[6,13] = CM136_114
  M[6,14] = CM214_6
  M[6,15] = CM115_6
  M[6,16] = CM166_317
  M[6,17] = CM176_118
  M[6,18] = CM218_6
  M[6,19] = CM196_120
  M[6,20] = FB320_6
  M[6,21] = CM216_122
  M[6,22] = CM222_6
  M[6,23] = CM236_124
  M[6,24] = CM324_6
  M[6,25] = CM256_126
  M[6,26] = CM326_6
  M[6,27] = CM276_128
  M[6,28] = FB328_6
  M[6,29] = CM296_130
  M[6,30] = CM230_6
  M[6,31] = CM316_132
  M[6,32] = CM332_6
  M[6,33] = CM336_134
  M[6,34] = CM334_6
  M[6,35] = CM356_136
  M[6,36] = FB336_6
  M[6,37] = CM376_138
  M[6,38] = CM238_6
  M[7,1] = CM17_1
  M[7,2] = CM17_2
  M[7,3] = CM17_3
  M[7,4] = CM17_4
  M[7,5] = CM17_5
  M[7,6] = CM17_6
  M[7,7] = CM17_7
  M[7,8] = CM87_39
  M[7,9] = CM97_110
  M[7,10] = CM210_7
  M[7,11] = CM117_112
  M[7,12] = FB312_7
  M[7,13] = CM137_114
  M[7,14] = CM214_7
  M[8,1] = CM81_39
  M[8,2] = CM82_39
  M[8,3] = CM83_39
  M[8,4] = CM84_39
  M[8,5] = CM85_39
  M[8,6] = CM86_39
  M[8,7] = CM87_39
  M[8,8] = CM88_39
  M[8,9] = CM98_110
  M[8,10] = CM210_8
  M[8,11] = CM118_112
  M[8,12] = FB312_8
  M[8,13] = CM138_114
  M[8,14] = CM214_8
  M[9,1] = CM91_110
  M[9,2] = CM92_110
  M[9,3] = CM93_110
  M[9,4] = CM94_110
  M[9,5] = CM95_110
  M[9,6] = CM96_110
  M[9,7] = CM97_110
  M[9,8] = CM98_110
  M[9,9] = CM99_110
  M[9,10] = CM210_9
  M[9,11] = CM119_112
  M[9,12] = FB312_9
  M[9,13] = CM139_114
  M[9,14] = CM214_9
  M[10,1] = CM210_1
  M[10,2] = CM210_2
  M[10,3] = CM210_3
  M[10,4] = CM210_4
  M[10,5] = CM210_5
  M[10,6] = CM210_6
  M[10,7] = CM210_7
  M[10,8] = CM210_8
  M[10,9] = CM210_9
  M[10,10] = CM210_10
  M[10,13] = CM1310_114
  M[10,14] = CM214_10
  M[11,1] = CM111_112
  M[11,2] = CM112_112
  M[11,3] = CM113_112
  M[11,4] = CM114_112
  M[11,5] = CM115_112
  M[11,6] = CM116_112
  M[11,7] = CM117_112
  M[11,8] = CM118_112
  M[11,9] = CM119_112
  M[11,11] = CM1111_112
  M[12,1] = FB312_1
  M[12,2] = FB312_2
  M[12,3] = FB312_3
  M[12,4] = FB312_4
  M[12,5] = FB312_5
  M[12,6] = FB312_6
  M[12,7] = FB312_7
  M[12,8] = FB312_8
  M[12,9] = FB312_9
  M[12,12] = s.m[12]
  M[13,4] = CM134_114
  M[13,5] = CM135_114
  M[13,6] = CM136_114
  M[13,7] = CM137_114
  M[13,8] = CM138_114
  M[13,9] = CM139_114
  M[13,10] = CM1310_114
  M[13,13] = CM1313_114
  M[14,4] = CM214_4
  M[14,5] = CM214_5
  M[14,6] = CM214_6
  M[14,7] = CM214_7
  M[14,8] = CM214_8
  M[14,9] = CM214_9
  M[14,10] = CM214_10
  M[14,14] = s.In[5,14]
  M[15,1] = CM115_1
  M[15,2] = CM115_2
  M[15,3] = CM115_3
  M[15,4] = CM115_4
  M[15,5] = CM115_5
  M[15,6] = CM115_6
  M[15,15] = CM115_15
  M[15,16] = CM1615_317
  M[15,17] = CM1715_118
  M[15,18] = CM218_15
  M[15,19] = CM1915_120
  M[15,20] = FB320_15
  M[15,21] = CM2115_122
  M[15,22] = CM222_15
  M[16,1] = CM161_317
  M[16,2] = CM162_317
  M[16,3] = CM163_317
  M[16,4] = CM164_317
  M[16,5] = CM165_317
  M[16,6] = CM166_317
  M[16,15] = CM1615_317
  M[16,16] = CM1616_317
  M[16,17] = CM1716_118
  M[16,18] = CM218_16
  M[16,19] = CM1916_120
  M[16,20] = FB320_16
  M[16,21] = CM2116_122
  M[16,22] = CM222_16
  M[17,1] = CM171_118
  M[17,2] = CM172_118
  M[17,3] = CM173_118
  M[17,4] = CM174_118
  M[17,5] = CM175_118
  M[17,6] = CM176_118
  M[17,15] = CM1715_118
  M[17,16] = CM1716_118
  M[17,17] = CM1717_118
  M[17,18] = CM218_17
  M[17,19] = CM1917_120
  M[17,20] = FB320_17
  M[17,21] = CM2117_122
  M[17,22] = CM222_17
  M[18,1] = CM218_1
  M[18,2] = CM218_2
  M[18,3] = CM218_3
  M[18,4] = CM218_4
  M[18,5] = CM218_5
  M[18,6] = CM218_6
  M[18,15] = CM218_15
  M[18,16] = CM218_16
  M[18,17] = CM218_17
  M[18,18] = CM218_18
  M[18,21] = CM2118_122
  M[18,22] = CM222_18
  M[19,1] = CM191_120
  M[19,2] = CM192_120
  M[19,3] = CM193_120
  M[19,4] = CM194_120
  M[19,5] = CM195_120
  M[19,6] = CM196_120
  M[19,15] = CM1915_120
  M[19,16] = CM1916_120
  M[19,17] = CM1917_120
  M[19,19] = CM1919_120
  M[20,1] = FB320_1
  M[20,2] = FB320_2
  M[20,3] = FB320_3
  M[20,4] = FB320_4
  M[20,5] = FB320_5
  M[20,6] = FB320_6
  M[20,15] = FB320_15
  M[20,16] = FB320_16
  M[20,17] = FB320_17
  M[20,20] = s.m[20]
  M[21,4] = CM214_122
  M[21,5] = CM215_122
  M[21,6] = CM216_122
  M[21,15] = CM2115_122
  M[21,16] = CM2116_122
  M[21,17] = CM2117_122
  M[21,18] = CM2118_122
  M[21,21] = CM2121_122
  M[22,4] = CM222_4
  M[22,5] = CM222_5
  M[22,6] = CM222_6
  M[22,15] = CM222_15
  M[22,16] = CM222_16
  M[22,17] = CM222_17
  M[22,18] = CM222_18
  M[22,22] = s.In[5,22]
  M[23,1] = CM231_124
  M[23,2] = CM232_124
  M[23,3] = CM233_124
  M[23,4] = CM234_124
  M[23,5] = CM235_124
  M[23,6] = CM236_124
  M[23,23] = CM2323_124
  M[23,24] = CM2423_325
  M[23,25] = CM2523_126
  M[23,26] = CM326_23
  M[23,27] = CM2723_128
  M[23,28] = FB328_23
  M[23,29] = CM2923_130
  M[23,30] = CM230_23
  M[24,1] = CM324_1
  M[24,2] = CM324_2
  M[24,3] = CM324_3
  M[24,4] = CM324_4
  M[24,5] = CM324_5
  M[24,6] = CM324_6
  M[24,23] = CM2423_325
  M[24,24] = CM324_24
  M[24,25] = CM2524_126
  M[24,26] = CM326_24
  M[24,27] = CM2724_128
  M[24,28] = FB328_24
  M[24,29] = CM2924_130
  M[24,30] = CM230_24
  M[25,1] = CM251_126
  M[25,2] = CM252_126
  M[25,3] = CM253_126
  M[25,4] = CM254_126
  M[25,5] = CM255_126
  M[25,6] = CM256_126
  M[25,23] = CM2523_126
  M[25,24] = CM2524_126
  M[25,25] = CM2525_126
  M[25,26] = CM326_25
  M[25,27] = CM2725_128
  M[25,28] = FB328_25
  M[25,29] = CM2925_130
  M[25,30] = CM230_25
  M[26,1] = CM261_327
  M[26,2] = CM262_327
  M[26,3] = CM263_327
  M[26,4] = CM326_4
  M[26,5] = CM326_5
  M[26,6] = CM326_6
  M[26,23] = CM326_23
  M[26,24] = CM326_24
  M[26,25] = CM326_25
  M[26,26] = CM326_26
  M[26,29] = CM2926_130
  M[26,30] = CM230_26
  M[27,1] = CM271_128
  M[27,2] = CM272_128
  M[27,3] = CM273_128
  M[27,4] = CM274_128
  M[27,5] = CM275_128
  M[27,6] = CM276_128
  M[27,23] = CM2723_128
  M[27,24] = CM2724_128
  M[27,25] = CM2725_128
  M[27,27] = CM2727_128
  M[28,1] = FB328_1
  M[28,2] = FB328_2
  M[28,3] = FB328_3
  M[28,4] = FB328_4
  M[28,5] = FB328_5
  M[28,6] = FB328_6
  M[28,23] = FB328_23
  M[28,24] = FB328_24
  M[28,25] = FB328_25
  M[28,28] = s.m[28]
  M[29,4] = CM294_130
  M[29,5] = CM295_130
  M[29,6] = CM296_130
  M[29,23] = CM2923_130
  M[29,24] = CM2924_130
  M[29,25] = CM2925_130
  M[29,26] = CM2926_130
  M[29,29] = CM2929_130
  M[30,4] = CM230_4
  M[30,5] = CM230_5
  M[30,6] = CM230_6
  M[30,23] = CM230_23
  M[30,24] = CM230_24
  M[30,25] = CM230_25
  M[30,26] = CM230_26
  M[30,30] = s.In[5,30]
  M[31,1] = CM311_132
  M[31,2] = CM312_132
  M[31,3] = CM313_132
  M[31,4] = CM314_132
  M[31,5] = CM315_132
  M[31,6] = CM316_132
  M[31,31] = CM3131_132
  M[31,32] = CM3231_333
  M[31,33] = CM3331_134
  M[31,34] = CM334_31
  M[31,35] = CM3531_136
  M[31,36] = FB336_31
  M[31,37] = CM3731_138
  M[31,38] = CM238_31
  M[32,1] = CM332_1
  M[32,2] = CM332_2
  M[32,3] = CM332_3
  M[32,4] = CM332_4
  M[32,5] = CM332_5
  M[32,6] = CM332_6
  M[32,31] = CM3231_333
  M[32,32] = CM332_32
  M[32,33] = CM3332_134
  M[32,34] = CM334_32
  M[32,35] = CM3532_136
  M[32,36] = FB336_32
  M[32,37] = CM3732_138
  M[32,38] = CM238_32
  M[33,1] = CM331_134
  M[33,2] = CM332_134
  M[33,3] = CM333_134
  M[33,4] = CM334_134
  M[33,5] = CM335_134
  M[33,6] = CM336_134
  M[33,31] = CM3331_134
  M[33,32] = CM3332_134
  M[33,33] = CM3333_134
  M[33,34] = CM334_33
  M[33,35] = CM3533_136
  M[33,36] = FB336_33
  M[33,37] = CM3733_138
  M[33,38] = CM238_33
  M[34,1] = CM341_335
  M[34,2] = CM342_335
  M[34,3] = CM343_335
  M[34,4] = CM334_4
  M[34,5] = CM334_5
  M[34,6] = CM334_6
  M[34,31] = CM334_31
  M[34,32] = CM334_32
  M[34,33] = CM334_33
  M[34,34] = CM334_34
  M[34,37] = CM3734_138
  M[34,38] = CM238_34
  M[35,1] = CM351_136
  M[35,2] = CM352_136
  M[35,3] = CM353_136
  M[35,4] = CM354_136
  M[35,5] = CM355_136
  M[35,6] = CM356_136
  M[35,31] = CM3531_136
  M[35,32] = CM3532_136
  M[35,33] = CM3533_136
  M[35,35] = CM3535_136
  M[36,1] = FB336_1
  M[36,2] = FB336_2
  M[36,3] = FB336_3
  M[36,4] = FB336_4
  M[36,5] = FB336_5
  M[36,6] = FB336_6
  M[36,31] = FB336_31
  M[36,32] = FB336_32
  M[36,33] = FB336_33
  M[36,36] = s.m[36]
  M[37,4] = CM374_138
  M[37,5] = CM375_138
  M[37,6] = CM376_138
  M[37,31] = CM3731_138
  M[37,32] = CM3732_138
  M[37,33] = CM3733_138
  M[37,34] = CM3734_138
  M[37,37] = CM3737_138
  M[38,4] = CM238_4
  M[38,5] = CM238_5
  M[38,6] = CM238_6
  M[38,31] = CM238_31
  M[38,32] = CM238_32
  M[38,33] = CM238_33
  M[38,34] = CM238_34
  M[38,38] = s.In[5,38]
  c[1] = FF3_14
  c[2] = FF3_24
  c[3] = FF4_35
  c[4] = CF4_35
  c[5] = CF5_26
  c[6] = CF16
  c[7] = CF17
  c[8] = CF8_39
  c[9] = CF9_110
  c[10] = CF210
  c[11] = CF11_112
  c[12] = FA312
  c[13] = CF13_114
  c[14] = CF214
  c[15] = CF115
  c[16] = CF16_317
  c[17] = CF17_118
  c[18] = CF218
  c[19] = CF19_120
  c[20] = FA320
  c[21] = CF21_122
  c[22] = CF222
  c[23] = CF23_124
  c[24] = CF324
  c[25] = CF25_126
  c[26] = CF326
  c[27] = CF27_128
  c[28] = FA328
  c[29] = CF29_130
  c[30] = CF230
  c[31] = CF31_132
  c[32] = CF332
  c[33] = CF33_134
  c[34] = CF334
  c[35] = CF35_136
  c[36] = FA336
  c[37] = CF37_138
  c[38] = CF238

# ====== END Task 0 ====== 

  

