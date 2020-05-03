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
#	==> Generation Date : Sun May  3 18:39:11 2020
#
#	==> Project name : Complete_Vehicle_New_Dimensions
#	==> using XML input file 
#
#	==> Number of joints : 67
#
#	==> Function : F 1 : Direct Dynamics (Semi-Explicit formulation) : RNEA
#	==> Flops complexity : 19872
#
#	==> Generation Time :  0.240 seconds
#	==> Post-Processing :  0.420 seconds
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

# = = Block_0_0_0_0_0_9 = = 
 
# Trigonometric Variables  

  C25 = np.cos(q[25])
  S25 = np.sin(q[25])
  C26 = np.cos(q[26])
  S26 = np.sin(q[26])

# = = Block_0_0_0_0_0_10 = = 
 
# Trigonometric Variables  

  C27 = np.cos(q[27])
  S27 = np.sin(q[27])
  C28 = np.cos(q[28])
  S28 = np.sin(q[28])

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

# = = Block_0_0_0_0_0_12 = = 
 
# Trigonometric Variables  

  C34 = np.cos(q[34])
  S34 = np.sin(q[34])

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C36 = np.cos(q[36])
  S36 = np.sin(q[36])
  C37 = np.cos(q[37])
  S37 = np.sin(q[37])

# = = Block_0_0_0_0_0_14 = = 
 
# Trigonometric Variables  

  C38 = np.cos(q[38])
  S38 = np.sin(q[38])
  C39 = np.cos(q[39])
  S39 = np.sin(q[39])

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

# = = Block_0_0_0_0_0_16 = = 
 
# Trigonometric Variables  

  C45 = np.cos(q[45])
  S45 = np.sin(q[45])

# = = Block_0_0_0_0_0_17 = = 
 
# Trigonometric Variables  

  C47 = np.cos(q[47])
  S47 = np.sin(q[47])
  C48 = np.cos(q[48])
  S48 = np.sin(q[48])

# = = Block_0_0_0_0_0_19 = = 
 
# Trigonometric Variables  

  C50 = np.cos(q[50])
  S50 = np.sin(q[50])
  C51 = np.cos(q[51])
  S51 = np.sin(q[51])

# = = Block_0_0_0_0_0_20 = = 
 
# Trigonometric Variables  

  C52 = np.cos(q[52])
  S52 = np.sin(q[52])
  C53 = np.cos(q[53])
  S53 = np.sin(q[53])

# = = Block_0_0_0_0_0_21 = = 
 
# Trigonometric Variables  

  C54 = np.cos(q[54])
  S54 = np.sin(q[54])

# = = Block_0_0_0_0_0_22 = = 
 
# Trigonometric Variables  

  C55 = np.cos(q[55])
  S55 = np.sin(q[55])
  C56 = np.cos(q[56])
  S56 = np.sin(q[56])
  C57 = np.cos(q[57])
  S57 = np.sin(q[57])

# = = Block_0_0_0_0_0_23 = = 
 
# Trigonometric Variables  

  C58 = np.cos(q[58])
  S58 = np.sin(q[58])
  C59 = np.cos(q[59])
  S59 = np.sin(q[59])

# = = Block_0_0_0_0_0_24 = = 
 
# Trigonometric Variables  

  C60 = np.cos(q[60])
  S60 = np.sin(q[60])

# = = Block_0_0_0_0_0_25 = = 
 
# Trigonometric Variables  

  C61 = np.cos(q[61])
  S61 = np.sin(q[61])
  C62 = np.cos(q[62])
  S62 = np.sin(q[62])
  C63 = np.cos(q[63])
  S63 = np.sin(q[63])

# = = Block_0_0_0_0_0_26 = = 
 
# Trigonometric Variables  

  C64 = np.cos(q[64])
  S64 = np.sin(q[64])
  C65 = np.cos(q[65])
  S65 = np.sin(q[65])

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
  AlM26_3 = C5*S6
  AlM36_3 = C5*C6
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
  BS27 = OM17*OM27
  BS57 = -(OM17*OM17+OM37*OM37)
  BeF27 = BS27-OpF37
  BeF87 = OpF15+OM27*OM37
  AlF17 = AlF15+BS16*s.dpt[1,1]+BeF26*s.dpt[2,1]
  AlF27 = C7*(AlF26+BS56*s.dpt[2,1]+BeF46*s.dpt[1,1])+S7*(AlF36+BeF76*s.dpt[1,1]+BeF86*s.dpt[2,1])
  AlF37 = C7*(AlF36+BeF76*s.dpt[1,1]+BeF86*s.dpt[2,1])-S7*(AlF26+BS56*s.dpt[2,1]+BeF46*s.dpt[1,1])
  AlM27_1 = AlM26_1*C7+AlM36_1*S7
  AlM37_1 = -(AlM26_1*S7-AlM36_1*C7)
  AlM27_2 = AlM26_2*C7+AlM36_2*S7
  AlM37_2 = -(AlM26_2*S7-AlM36_2*C7)
  AlM27_3 = S6p7*C5
  AlM37_3 = C6p7*C5
  OpM27_4 = S6p7*C5
  OpM37_4 = C6p7*C5
  AlM17_4 = -OpM36_4*s.dpt[2,1]
  AlM27_4 = OpM36_4*s.dpt[1,1]*C7-S7*(OpM26_4*s.dpt[1,1]+s.dpt[2,1]*S5)
  AlM37_4 = -(OpM36_4*s.dpt[1,1]*S7+C7*(OpM26_4*s.dpt[1,1]+s.dpt[2,1]*S5))
  AlM17_5 = s.dpt[2,1]*S6
  AlM27_5 = -s.dpt[1,1]*S6p7
  AlM37_5 = -s.dpt[1,1]*C6p7
  AlM27_6 = s.dpt[2,1]*S7
  AlM37_6 = s.dpt[2,1]*C7
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OpF18 = C8*(OpF15+qd[8]*OM27)+S8*(OpF27-qd[8]*OM17)
  OpF28 = C8*(OpF27-qd[8]*OM17)-S8*(OpF15+qd[8]*OM27)
  AlF18 = C8*(AlF17+BeF27*s.dpt[2,18])+S8*(AlF27+BS57*s.dpt[2,18])
  AlF28 = C8*(AlF27+BS57*s.dpt[2,18])-S8*(AlF17+BeF27*s.dpt[2,18])
  AlF38 = AlF37+BeF87*s.dpt[2,18]
  AlM18_1 = AlM15_1*C8+AlM27_1*S8
  AlM28_1 = -(AlM15_1*S8-AlM27_1*C8)
  AlM18_2 = AlM15_2*C8+AlM27_2*S8
  AlM28_2 = -(AlM15_2*S8-AlM27_2*C8)
  AlM18_3 = AlM27_3*S8-S5*C8
  AlM28_3 = AlM27_3*C8+S5*S8
  OpM18_4 = OpM27_4*S8-S5*C8
  OpM28_4 = OpM27_4*C8+S5*S8
  AlM18_4 = AlM27_4*S8+C8*(AlM17_4-OpM37_4*s.dpt[2,18])
  AlM28_4 = AlM27_4*C8-S8*(AlM17_4-OpM37_4*s.dpt[2,18])
  AlM38_4 = AlM37_4-s.dpt[2,18]*S5
  OpM18_5 = C6p7*S8
  OpM28_5 = C6p7*C8
  AlM18_5 = AlM27_5*S8+C8*(AlM17_5+s.dpt[2,18]*S6p7)
  AlM28_5 = AlM27_5*C8-S8*(AlM17_5+s.dpt[2,18]*S6p7)
  AlM18_6 = AlM27_6*S8
  AlM28_6 = AlM27_6*C8
  AlM38_6 = AlM37_6+s.dpt[2,18]
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
  AlM29_7 = s.dpt[2,18]*S9
  AlM39_7 = s.dpt[2,18]*C9
  OM110 = OM19*C10-OM39*S10
  OM210 = qd[10]+OM28*C9+OM38*S9
  OM310 = OM19*S10+OM39*C10
  OpF110 = C10*(OpF18-qd[10]*OM39)-S10*(OpF39+qd[10]*OM19)
  OpF310 = C10*(OpF39+qd[10]*OM19)+S10*(OpF18-qd[10]*OM39)
  BS510 = -(OM110*OM110+OM310*OM310)
  BS610 = OM210*OM310
  BS910 = -(OM110*OM110+OM210*OM210)
  BeF210 = OM110*OM210-OpF310
  BeF310 = OpF29+OM110*OM310
  BeF610 = BS610-OpF110
  BeF810 = BS610+OpF110
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
  BS215 = OM115*OM215
  BS515 = -(OM115*OM115+OM315*OM315)
  BeF215 = BS215-OpF315
  BeF815 = OpF15+OM215*OM315
  AlF115 = AlF15+BS16*s.dpt[1,4]+BeF26*s.dpt[2,4]
  AlF215 = C15*(AlF26+BS56*s.dpt[2,4]+BeF46*s.dpt[1,4])+S15*(AlF36+BeF76*s.dpt[1,4]+BeF86*s.dpt[2,4])
  AlF315 = C15*(AlF36+BeF76*s.dpt[1,4]+BeF86*s.dpt[2,4])-S15*(AlF26+BS56*s.dpt[2,4]+BeF46*s.dpt[1,4])
  AlM215_1 = AlM26_1*C15+AlM36_1*S15
  AlM315_1 = -(AlM26_1*S15-AlM36_1*C15)
  AlM215_2 = AlM26_2*C15+AlM36_2*S15
  AlM315_2 = -(AlM26_2*S15-AlM36_2*C15)
  AlM215_3 = S15p6*C5
  AlM315_3 = C15p6*C5
  OpM215_4 = S15p6*C5
  OpM315_4 = C15p6*C5
  AlM115_4 = -OpM36_4*s.dpt[2,4]
  AlM215_4 = OpM36_4*s.dpt[1,4]*C15-S15*(OpM26_4*s.dpt[1,4]+s.dpt[2,4]*S5)
  AlM315_4 = -(OpM36_4*s.dpt[1,4]*S15+C15*(OpM26_4*s.dpt[1,4]+s.dpt[2,4]*S5))
  AlM115_5 = s.dpt[2,4]*S6
  AlM215_5 = -s.dpt[1,4]*S15p6
  AlM315_5 = -s.dpt[1,4]*C15p6
  AlM215_6 = s.dpt[2,4]*S15
  AlM315_6 = s.dpt[2,4]*C15
  OM216 = -(OM115*S16-OM215*C16)
  OM316 = qd[16]+OM315
  OpF116 = C16*(OpF15+qd[16]*OM215)+S16*(OpF215-qd[16]*OM115)
  OpF216 = C16*(OpF215-qd[16]*OM115)-S16*(OpF15+qd[16]*OM215)
  AlF116 = C16*(AlF115+BeF215*s.dpt[2,25])+S16*(AlF215+BS515*s.dpt[2,25])
  AlF216 = C16*(AlF215+BS515*s.dpt[2,25])-S16*(AlF115+BeF215*s.dpt[2,25])
  AlF316 = AlF315+BeF815*s.dpt[2,25]
  AlM116_1 = AlM15_1*C16+AlM215_1*S16
  AlM216_1 = -(AlM15_1*S16-AlM215_1*C16)
  AlM116_2 = AlM15_2*C16+AlM215_2*S16
  AlM216_2 = -(AlM15_2*S16-AlM215_2*C16)
  AlM116_3 = AlM215_3*S16-C16*S5
  AlM216_3 = AlM215_3*C16+S16*S5
  OpM116_4 = OpM215_4*S16-C16*S5
  OpM216_4 = OpM215_4*C16+S16*S5
  AlM116_4 = AlM215_4*S16+C16*(AlM115_4-OpM315_4*s.dpt[2,25])
  AlM216_4 = AlM215_4*C16-S16*(AlM115_4-OpM315_4*s.dpt[2,25])
  AlM316_4 = AlM315_4-s.dpt[2,25]*S5
  OpM116_5 = C15p6*S16
  OpM216_5 = C15p6*C16
  AlM116_5 = AlM215_5*S16+C16*(AlM115_5+s.dpt[2,25]*S15p6)
  AlM216_5 = AlM215_5*C16-S16*(AlM115_5+s.dpt[2,25]*S15p6)
  AlM116_6 = AlM215_6*S16
  AlM216_6 = AlM215_6*C16
  AlM316_6 = AlM315_6+s.dpt[2,25]
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
  AlM217_15 = s.dpt[2,25]*S17
  AlM317_15 = s.dpt[2,25]*C17
  OM118 = OM117*C18-OM317*S18
  OM218 = qd[18]+OM216*C17+OM316*S17
  OM318 = OM117*S18+OM317*C18
  OpF118 = C18*(OpF116-qd[18]*OM317)-S18*(OpF317+qd[18]*OM117)
  OpF318 = C18*(OpF317+qd[18]*OM117)+S18*(OpF116-qd[18]*OM317)
  BS518 = -(OM118*OM118+OM318*OM318)
  BS618 = OM218*OM318
  BS918 = -(OM118*OM118+OM218*OM218)
  BeF218 = OM118*OM218-OpF318
  BeF318 = OpF217+OM118*OM318
  BeF618 = BS618-OpF118
  BeF818 = BS618+OpF118
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
  OpF323 = C23*(OpF36-qd[23]*OM26)-S23*(OpF26+qd[23]*OM36)
  AlF123 = AlF15+BS16*s.dpt[1,6]+BeF26*s.dpt[2,6]+BeF36*s.dpt[3,6]
  AlF223 = C23*(AlF26+BS56*s.dpt[2,6]+BeF46*s.dpt[1,6]+BeF66*s.dpt[3,6])+S23*(AlF36+BS96*s.dpt[3,6]+BeF76*s.dpt[1,6]+\
   BeF86*s.dpt[2,6])
  AlM223_1 = AlM26_1*C23+AlM36_1*S23
  AlM223_2 = AlM26_2*C23+AlM36_2*S23
  AlM223_3 = S23p6*C5
  OpM323_4 = C23p6*C5
  AlM123_4 = OpM26_4*s.dpt[3,6]-OpM36_4*s.dpt[2,6]
  AlM223_4 = C23*(OpM36_4*s.dpt[1,6]+s.dpt[3,6]*S5)-S23*(OpM26_4*s.dpt[1,6]+s.dpt[2,6]*S5)
  AlM123_5 = s.dpt[2,6]*S6+s.dpt[3,6]*C6
  AlM223_5 = -s.dpt[1,6]*S23p6
  AlM223_6 = s.dpt[2,6]*S23-s.dpt[3,6]*C23
  OM124 = OM123*C24+OM223*S24
  OM224 = -(OM123*S24-OM223*C24)
  OM324 = qd[24]-OM26*S23+OM36*C23
  OpF124 = C24*(OpF15+qd[24]*OM223)-S24*(qd[24]*OM123-C23*(OpF26+qd[23]*OM36)-S23*(OpF36-qd[23]*OM26))
  OpM124_4 = S23p6*S24*C5-C24*S5
  OpM124_5 = C23p6*S24

# = = Block_0_1_0_1_0_9 = = 
 
# Trigonometric Variables  

  S25p6 = C25*S6+S25*C6
  C25p6 = C25*C6-S25*S6
 
# Forward Kinematics 

  OM125 = qd[25]+OM16
  OM225 = OM26*C25+OM36*S25
  OpF325 = C25*(OpF36-qd[25]*OM26)-S25*(OpF26+qd[25]*OM36)
  AlF125 = AlF15+BS16*s.dpt[1,8]+BeF26*s.dpt[2,8]+BeF36*s.dpt[3,8]
  AlF225 = C25*(AlF26+BS56*s.dpt[2,8]+BeF46*s.dpt[1,8]+BeF66*s.dpt[3,8])+S25*(AlF36+BS96*s.dpt[3,8]+BeF76*s.dpt[1,8]+\
   BeF86*s.dpt[2,8])
  AlM225_1 = AlM26_1*C25+AlM36_1*S25
  AlM225_2 = AlM26_2*C25+AlM36_2*S25
  AlM225_3 = S25p6*C5
  OpM325_4 = C25p6*C5
  AlM125_4 = OpM26_4*s.dpt[3,8]-OpM36_4*s.dpt[2,8]
  AlM225_4 = C25*(OpM36_4*s.dpt[1,8]+s.dpt[3,8]*S5)-S25*(OpM26_4*s.dpt[1,8]+s.dpt[2,8]*S5)
  AlM125_5 = s.dpt[2,8]*S6+s.dpt[3,8]*C6
  AlM225_5 = -s.dpt[1,8]*S25p6
  AlM225_6 = s.dpt[2,8]*S25-s.dpt[3,8]*C25
  OM126 = OM125*C26+OM225*S26
  OM226 = -(OM125*S26-OM225*C26)
  OM326 = qd[26]-OM26*S25+OM36*C25
  OpF126 = C26*(OpF15+qd[26]*OM225)-S26*(qd[26]*OM125-C25*(OpF26+qd[25]*OM36)-S25*(OpF36-qd[25]*OM26))
  OpM126_4 = S25p6*S26*C5-C26*S5
  OpM126_5 = C25p6*S26

# = = Block_0_1_0_1_0_10 = = 
 
# Trigonometric Variables  

  S27p6 = C27*S6+S27*C6
  C27p6 = C27*C6-S27*S6
 
# Forward Kinematics 

  OM127 = qd[27]+OM16
  OM227 = OM26*C27+OM36*S27
  OpF327 = C27*(OpF36-qd[27]*OM26)-S27*(OpF26+qd[27]*OM36)
  AlF127 = AlF15+BS16*s.dpt[1,9]+BeF26*s.dpt[2,9]+BeF36*s.dpt[3,9]
  AlF227 = C27*(AlF26+BS56*s.dpt[2,9]+BeF46*s.dpt[1,9]+BeF66*s.dpt[3,9])+S27*(AlF36+BS96*s.dpt[3,9]+BeF76*s.dpt[1,9]+\
   BeF86*s.dpt[2,9])
  AlM227_1 = AlM26_1*C27+AlM36_1*S27
  AlM227_2 = AlM26_2*C27+AlM36_2*S27
  AlM227_3 = S27p6*C5
  OpM327_4 = C27p6*C5
  AlM127_4 = OpM26_4*s.dpt[3,9]-OpM36_4*s.dpt[2,9]
  AlM227_4 = C27*(OpM36_4*s.dpt[1,9]+s.dpt[3,9]*S5)-S27*(OpM26_4*s.dpt[1,9]+s.dpt[2,9]*S5)
  AlM127_5 = s.dpt[2,9]*S6+s.dpt[3,9]*C6
  AlM227_5 = -s.dpt[1,9]*S27p6
  AlM227_6 = s.dpt[2,9]*S27-s.dpt[3,9]*C27
  OM128 = OM127*C28+OM227*S28
  OM228 = -(OM127*S28-OM227*C28)
  OM328 = qd[28]-OM26*S27+OM36*C27
  OpF128 = C28*(OpF15+qd[28]*OM227)-S28*(qd[28]*OM127-C27*(OpF26+qd[27]*OM36)-S27*(OpF36-qd[27]*OM26))
  OpM128_4 = S27p6*S28*C5-C28*S5
  OpM128_5 = C27p6*S28

# = = Block_0_1_0_1_0_11 = = 
 
# Trigonometric Variables  

  S29p6 = C29*S6+S29*C6
  C29p6 = C29*C6-S29*S6
 
# Forward Kinematics 

  OM129 = qd[29]+OM16
  OM229 = OM26*C29+OM36*S29
  OpF229 = C29*(OpF26+qd[29]*OM36)+S29*(OpF36-qd[29]*OM26)
  OpF329 = C29*(OpF36-qd[29]*OM26)-S29*(OpF26+qd[29]*OM36)
  AlF129 = AlF15+BS16*s.dpt[1,10]+BeF26*s.dpt[2,10]
  AlF229 = C29*(AlF26+BS56*s.dpt[2,10]+BeF46*s.dpt[1,10])+S29*(AlF36+BeF76*s.dpt[1,10]+BeF86*s.dpt[2,10])
  AlF329 = C29*(AlF36+BeF76*s.dpt[1,10]+BeF86*s.dpt[2,10])-S29*(AlF26+BS56*s.dpt[2,10]+BeF46*s.dpt[1,10])
  AlM229_1 = AlM26_1*C29+AlM36_1*S29
  AlM329_1 = -(AlM26_1*S29-AlM36_1*C29)
  AlM229_2 = AlM26_2*C29+AlM36_2*S29
  AlM329_2 = -(AlM26_2*S29-AlM36_2*C29)
  AlM229_3 = S29p6*C5
  AlM329_3 = C29p6*C5
  OpM229_4 = S29p6*C5
  OpM329_4 = C29p6*C5
  AlM129_4 = -OpM36_4*s.dpt[2,10]
  AlM229_4 = OpM36_4*s.dpt[1,10]*C29-S29*(OpM26_4*s.dpt[1,10]+s.dpt[2,10]*S5)
  AlM329_4 = -(OpM36_4*s.dpt[1,10]*S29+C29*(OpM26_4*s.dpt[1,10]+s.dpt[2,10]*S5))
  AlM129_5 = s.dpt[2,10]*S6
  AlM229_5 = -s.dpt[1,10]*S29p6
  AlM329_5 = -s.dpt[1,10]*C29p6
  AlM229_6 = s.dpt[2,10]*S29
  AlM329_6 = s.dpt[2,10]*C29
  OM130 = OM129*C30+OM229*S30
  OM230 = -(OM129*S30-OM229*C30)
  OM330 = qd[30]-OM26*S29+OM36*C29
  OpF130 = C30*(OpF15+qd[30]*OM229)+S30*(OpF229-qd[30]*OM129)
  OpF230 = C30*(OpF229-qd[30]*OM129)-S30*(OpF15+qd[30]*OM229)
  BS530 = -(OM130*OM130+OM330*OM330)
  BeF230 = OM130*OM230-OpF329
  BeF830 = OpF130+OM230*OM330
  AlF130 = AlF129*C30+AlF229*S30
  AlF230 = -(AlF129*S30-AlF229*C30)
  AlM130_1 = AlM15_1*C30+AlM229_1*S30
  AlM230_1 = -(AlM15_1*S30-AlM229_1*C30)
  AlM130_2 = AlM15_2*C30+AlM229_2*S30
  AlM230_2 = -(AlM15_2*S30-AlM229_2*C30)
  AlM130_3 = AlM229_3*S30-C30*S5
  AlM230_3 = AlM229_3*C30+S30*S5
  OpM130_4 = OpM229_4*S30-C30*S5
  OpM230_4 = OpM229_4*C30+S30*S5
  AlM130_4 = AlM129_4*C30+AlM229_4*S30
  AlM230_4 = -(AlM129_4*S30-AlM229_4*C30)
  OpM130_5 = C29p6*S30
  OpM230_5 = C29p6*C30
  AlM130_5 = AlM129_5*C30+AlM229_5*S30
  AlM230_5 = -(AlM129_5*S30-AlM229_5*C30)
  AlM130_6 = AlM229_6*S30
  AlM230_6 = AlM229_6*C30
  OM131 = qd[31]+OM130
  OM331 = -(OM230*S31-OM330*C31)
  OpF231 = C31*(OpF230+qd[31]*OM330)+S31*(OpF329-qd[31]*OM230)
  OpF331 = C31*(OpF329-qd[31]*OM230)-S31*(OpF230+qd[31]*OM330)
  AlF131 = AlF130+BeF230*s.dpt[2,35]
  AlF231 = C31*(AlF230+BS530*s.dpt[2,35])+S31*(AlF329+BeF830*s.dpt[2,35])
  AlF331 = C31*(AlF329+BeF830*s.dpt[2,35])-S31*(AlF230+BS530*s.dpt[2,35])
  AlM231_1 = AlM230_1*C31+AlM329_1*S31
  AlM331_1 = -(AlM230_1*S31-AlM329_1*C31)
  AlM231_2 = AlM230_2*C31+AlM329_2*S31
  AlM331_2 = -(AlM230_2*S31-AlM329_2*C31)
  AlM231_3 = AlM230_3*C31+AlM329_3*S31
  AlM331_3 = -(AlM230_3*S31-AlM329_3*C31)
  OpM231_4 = OpM230_4*C31+OpM329_4*S31
  OpM331_4 = -(OpM230_4*S31-OpM329_4*C31)
  AlM131_4 = AlM130_4-OpM329_4*s.dpt[2,35]
  AlM231_4 = AlM230_4*C31+S31*(AlM329_4+OpM130_4*s.dpt[2,35])
  AlM331_4 = -(AlM230_4*S31-C31*(AlM329_4+OpM130_4*s.dpt[2,35]))
  OpM231_5 = OpM230_5*C31-S29p6*S31
  OpM331_5 = -(OpM230_5*S31+S29p6*C31)
  AlM131_5 = AlM130_5+s.dpt[2,35]*S29p6
  AlM231_5 = AlM230_5*C31+S31*(AlM329_5+OpM130_5*s.dpt[2,35])
  AlM331_5 = -(AlM230_5*S31-C31*(AlM329_5+OpM130_5*s.dpt[2,35]))
  OpM231_6 = -S30*C31
  OpM331_6 = S30*S31
  AlM231_6 = AlM230_6*C31+S31*(AlM329_6+s.dpt[2,35]*C30)
  AlM331_6 = -(AlM230_6*S31-C31*(AlM329_6+s.dpt[2,35]*C30))
  OpM231_29 = -S30*C31
  OpM331_29 = S30*S31
  AlM231_29 = s.dpt[2,35]*C30*S31
  AlM331_29 = s.dpt[2,35]*C30*C31
  OM132 = OM131*C32-OM331*S32
  OM232 = qd[32]+OM230*C31+OM330*S31
  OpF132 = C32*(OpF130-qd[32]*OM331)-S32*(OpF331+qd[32]*OM131)
  OpF332 = C32*(OpF331+qd[32]*OM131)+S32*(OpF130-qd[32]*OM331)
  AlF132 = AlF131*C32-AlF331*S32
  AlF332 = AlF131*S32+AlF331*C32
  AlM132_1 = AlM130_1*C32-AlM331_1*S32
  AlM332_1 = AlM130_1*S32+AlM331_1*C32
  AlM132_2 = AlM130_2*C32-AlM331_2*S32
  AlM332_2 = AlM130_2*S32+AlM331_2*C32
  AlM132_3 = AlM130_3*C32-AlM331_3*S32
  AlM332_3 = AlM130_3*S32+AlM331_3*C32
  OpM132_4 = OpM130_4*C32-OpM331_4*S32
  OpM332_4 = OpM130_4*S32+OpM331_4*C32
  AlM132_4 = AlM131_4*C32-AlM331_4*S32
  AlM332_4 = AlM131_4*S32+AlM331_4*C32
  OpM132_5 = OpM130_5*C32-OpM331_5*S32
  OpM332_5 = OpM130_5*S32+OpM331_5*C32
  AlM132_5 = AlM131_5*C32-AlM331_5*S32
  AlM332_5 = AlM131_5*S32+AlM331_5*C32
  OpM132_6 = -(OpM331_6*S32-C30*C32)
  OpM332_6 = OpM331_6*C32+C30*S32
  AlM132_6 = AlM130_6*C32-AlM331_6*S32
  AlM332_6 = AlM130_6*S32+AlM331_6*C32
  OpM132_29 = -(OpM331_29*S32-C30*C32)
  OpM332_29 = OpM331_29*C32+C30*S32
  AlM132_29 = -AlM331_29*S32
  AlM332_29 = AlM331_29*C32
  OpM132_30 = -C31*S32
  OpM332_30 = C31*C32
  AlM132_30 = -s.dpt[2,35]*C32
  AlM332_30 = -s.dpt[2,35]*S32
  OM133 = OM132*C33+OM232*S33
  OM233 = -(OM132*S33-OM232*C33)
  OM333 = qd[33]+OM131*S32+OM331*C32
  OpF133 = C33*(OpF132+qd[33]*OM232)+S33*(OpF231-qd[33]*OM132)
  OpF233 = C33*(OpF231-qd[33]*OM132)-S33*(OpF132+qd[33]*OM232)
  BS533 = -(OM133*OM133+OM333*OM333)
  BS633 = OM233*OM333
  BS933 = -(OM133*OM133+OM233*OM233)
  BeF233 = OM133*OM233-OpF332
  BeF333 = OpF233+OM133*OM333
  BeF633 = BS633-OpF133
  BeF833 = BS633+OpF133
  AlF133 = AlF132*C33+AlF231*S33
  AlF233 = -(AlF132*S33-AlF231*C33)
  AlM133_1 = AlM132_1*C33+AlM231_1*S33
  AlM233_1 = -(AlM132_1*S33-AlM231_1*C33)
  AlM133_2 = AlM132_2*C33+AlM231_2*S33
  AlM233_2 = -(AlM132_2*S33-AlM231_2*C33)
  AlM133_3 = AlM132_3*C33+AlM231_3*S33
  AlM233_3 = -(AlM132_3*S33-AlM231_3*C33)
  OpM133_4 = OpM132_4*C33+OpM231_4*S33
  OpM233_4 = -(OpM132_4*S33-OpM231_4*C33)
  AlM133_4 = AlM132_4*C33+AlM231_4*S33
  AlM233_4 = -(AlM132_4*S33-AlM231_4*C33)
  OpM133_5 = OpM132_5*C33+OpM231_5*S33
  OpM233_5 = -(OpM132_5*S33-OpM231_5*C33)
  AlM133_5 = AlM132_5*C33+AlM231_5*S33
  AlM233_5 = -(AlM132_5*S33-AlM231_5*C33)
  OpM133_6 = OpM132_6*C33+OpM231_6*S33
  OpM233_6 = -(OpM132_6*S33-OpM231_6*C33)
  AlM133_6 = AlM132_6*C33+AlM231_6*S33
  AlM233_6 = -(AlM132_6*S33-AlM231_6*C33)
  OpM133_29 = OpM132_29*C33+OpM231_29*S33
  OpM233_29 = -(OpM132_29*S33-OpM231_29*C33)
  AlM133_29 = AlM132_29*C33+AlM231_29*S33
  AlM233_29 = -(AlM132_29*S33-AlM231_29*C33)
  OpM133_30 = OpM132_30*C33+S31*S33
  OpM233_30 = -(OpM132_30*S33-S31*C33)
  AlM133_30 = AlM132_30*C33
  AlM233_30 = -AlM132_30*S33
  OpM133_31 = C32*C33
  OpM233_31 = -C32*S33

# = = Block_0_1_0_1_0_14 = = 
 
# Trigonometric Variables  

  S38p6 = C38*S6+S38*C6
  C38p6 = C38*C6-S38*S6
 
# Forward Kinematics 

  OM138 = qd[38]+OM16
  OM238 = OM26*C38+OM36*S38
  OpF338 = C38*(OpF36-qd[38]*OM26)-S38*(OpF26+qd[38]*OM36)
  AlF138 = AlF15+BS16*s.dpt[1,11]+BeF26*s.dpt[2,11]+BeF36*s.dpt[3,11]
  AlF238 = C38*(AlF26+BS56*s.dpt[2,11]+BeF46*s.dpt[1,11]+BeF66*s.dpt[3,11])+S38*(AlF36+BS96*s.dpt[3,11]+BeF76*\
   s.dpt[1,11]+BeF86*s.dpt[2,11])
  AlM238_1 = AlM26_1*C38+AlM36_1*S38
  AlM238_2 = AlM26_2*C38+AlM36_2*S38
  AlM238_3 = S38p6*C5
  OpM338_4 = C38p6*C5
  AlM138_4 = OpM26_4*s.dpt[3,11]-OpM36_4*s.dpt[2,11]
  AlM238_4 = C38*(OpM36_4*s.dpt[1,11]+s.dpt[3,11]*S5)-S38*(OpM26_4*s.dpt[1,11]+s.dpt[2,11]*S5)
  AlM138_5 = s.dpt[2,11]*S6+s.dpt[3,11]*C6
  AlM238_5 = -s.dpt[1,11]*S38p6
  AlM238_6 = s.dpt[2,11]*S38-s.dpt[3,11]*C38
  OM139 = OM138*C39+OM238*S39
  OM239 = -(OM138*S39-OM238*C39)
  OM339 = qd[39]-OM26*S38+OM36*C38
  OpF139 = C39*(OpF15+qd[39]*OM238)-S39*(qd[39]*OM138-C38*(OpF26+qd[38]*OM36)-S38*(OpF36-qd[38]*OM26))
  OpM139_4 = S38p6*S39*C5-C39*S5
  OpM139_5 = C38p6*S39

# = = Block_0_1_0_1_0_15 = = 
 
# Trigonometric Variables  

  S40p6 = C40*S6+S40*C6
  C40p6 = C40*C6-S40*S6
 
# Forward Kinematics 

  OM140 = qd[40]+OM16
  OM240 = OM26*C40+OM36*S40
  OpF240 = C40*(OpF26+qd[40]*OM36)+S40*(OpF36-qd[40]*OM26)
  OpF340 = C40*(OpF36-qd[40]*OM26)-S40*(OpF26+qd[40]*OM36)
  AlF140 = AlF15+BS16*s.dpt[1,12]+BeF26*s.dpt[2,12]
  AlF240 = C40*(AlF26+BS56*s.dpt[2,12]+BeF46*s.dpt[1,12])+S40*(AlF36+BeF76*s.dpt[1,12]+BeF86*s.dpt[2,12])
  AlF340 = C40*(AlF36+BeF76*s.dpt[1,12]+BeF86*s.dpt[2,12])-S40*(AlF26+BS56*s.dpt[2,12]+BeF46*s.dpt[1,12])
  AlM240_1 = AlM26_1*C40+AlM36_1*S40
  AlM340_1 = -(AlM26_1*S40-AlM36_1*C40)
  AlM240_2 = AlM26_2*C40+AlM36_2*S40
  AlM340_2 = -(AlM26_2*S40-AlM36_2*C40)
  AlM240_3 = S40p6*C5
  AlM340_3 = C40p6*C5
  OpM240_4 = S40p6*C5
  OpM340_4 = C40p6*C5
  AlM140_4 = -OpM36_4*s.dpt[2,12]
  AlM240_4 = OpM36_4*s.dpt[1,12]*C40-S40*(OpM26_4*s.dpt[1,12]+s.dpt[2,12]*S5)
  AlM340_4 = -(OpM36_4*s.dpt[1,12]*S40+C40*(OpM26_4*s.dpt[1,12]+s.dpt[2,12]*S5))
  AlM140_5 = s.dpt[2,12]*S6
  AlM240_5 = -s.dpt[1,12]*S40p6
  AlM340_5 = -s.dpt[1,12]*C40p6
  AlM240_6 = s.dpt[2,12]*S40
  AlM340_6 = s.dpt[2,12]*C40
  OM141 = OM140*C41+OM240*S41
  OM241 = -(OM140*S41-OM240*C41)
  OM341 = qd[41]-OM26*S40+OM36*C40
  OpF141 = C41*(OpF15+qd[41]*OM240)+S41*(OpF240-qd[41]*OM140)
  OpF241 = C41*(OpF240-qd[41]*OM140)-S41*(OpF15+qd[41]*OM240)
  BS541 = -(OM141*OM141+OM341*OM341)
  BeF241 = OM141*OM241-OpF340
  BeF841 = OpF141+OM241*OM341
  AlF141 = AlF140*C41+AlF240*S41
  AlF241 = -(AlF140*S41-AlF240*C41)
  AlM141_1 = AlM15_1*C41+AlM240_1*S41
  AlM241_1 = -(AlM15_1*S41-AlM240_1*C41)
  AlM141_2 = AlM15_2*C41+AlM240_2*S41
  AlM241_2 = -(AlM15_2*S41-AlM240_2*C41)
  AlM141_3 = AlM240_3*S41-C41*S5
  AlM241_3 = AlM240_3*C41+S41*S5
  OpM141_4 = OpM240_4*S41-C41*S5
  OpM241_4 = OpM240_4*C41+S41*S5
  AlM141_4 = AlM140_4*C41+AlM240_4*S41
  AlM241_4 = -(AlM140_4*S41-AlM240_4*C41)
  OpM141_5 = C40p6*S41
  OpM241_5 = C40p6*C41
  AlM141_5 = AlM140_5*C41+AlM240_5*S41
  AlM241_5 = -(AlM140_5*S41-AlM240_5*C41)
  AlM141_6 = AlM240_6*S41
  AlM241_6 = AlM240_6*C41
  OM142 = qd[42]+OM141
  OM342 = -(OM241*S42-OM341*C42)
  OpF242 = C42*(OpF241+qd[42]*OM341)+S42*(OpF340-qd[42]*OM241)
  OpF342 = C42*(OpF340-qd[42]*OM241)-S42*(OpF241+qd[42]*OM341)
  AlF142 = AlF141+BeF241*s.dpt[2,44]
  AlF242 = C42*(AlF241+BS541*s.dpt[2,44])+S42*(AlF340+BeF841*s.dpt[2,44])
  AlF342 = C42*(AlF340+BeF841*s.dpt[2,44])-S42*(AlF241+BS541*s.dpt[2,44])
  AlM242_1 = AlM241_1*C42+AlM340_1*S42
  AlM342_1 = -(AlM241_1*S42-AlM340_1*C42)
  AlM242_2 = AlM241_2*C42+AlM340_2*S42
  AlM342_2 = -(AlM241_2*S42-AlM340_2*C42)
  AlM242_3 = AlM241_3*C42+AlM340_3*S42
  AlM342_3 = -(AlM241_3*S42-AlM340_3*C42)
  OpM242_4 = OpM241_4*C42+OpM340_4*S42
  OpM342_4 = -(OpM241_4*S42-OpM340_4*C42)
  AlM142_4 = AlM141_4-OpM340_4*s.dpt[2,44]
  AlM242_4 = AlM241_4*C42+S42*(AlM340_4+OpM141_4*s.dpt[2,44])
  AlM342_4 = -(AlM241_4*S42-C42*(AlM340_4+OpM141_4*s.dpt[2,44]))
  OpM242_5 = OpM241_5*C42-S40p6*S42
  OpM342_5 = -(OpM241_5*S42+S40p6*C42)
  AlM142_5 = AlM141_5+s.dpt[2,44]*S40p6
  AlM242_5 = AlM241_5*C42+S42*(AlM340_5+OpM141_5*s.dpt[2,44])
  AlM342_5 = -(AlM241_5*S42-C42*(AlM340_5+OpM141_5*s.dpt[2,44]))
  OpM242_6 = -S41*C42
  OpM342_6 = S41*S42
  AlM242_6 = AlM241_6*C42+S42*(AlM340_6+s.dpt[2,44]*C41)
  AlM342_6 = -(AlM241_6*S42-C42*(AlM340_6+s.dpt[2,44]*C41))
  OpM242_40 = -S41*C42
  OpM342_40 = S41*S42
  AlM242_40 = s.dpt[2,44]*C41*S42
  AlM342_40 = s.dpt[2,44]*C41*C42
  OM143 = OM142*C43-OM342*S43
  OM243 = qd[43]+OM241*C42+OM341*S42
  OpF143 = C43*(OpF141-qd[43]*OM342)-S43*(OpF342+qd[43]*OM142)
  OpF343 = C43*(OpF342+qd[43]*OM142)+S43*(OpF141-qd[43]*OM342)
  AlF143 = AlF142*C43-AlF342*S43
  AlF343 = AlF142*S43+AlF342*C43
  AlM143_1 = AlM141_1*C43-AlM342_1*S43
  AlM343_1 = AlM141_1*S43+AlM342_1*C43
  AlM143_2 = AlM141_2*C43-AlM342_2*S43
  AlM343_2 = AlM141_2*S43+AlM342_2*C43
  AlM143_3 = AlM141_3*C43-AlM342_3*S43
  AlM343_3 = AlM141_3*S43+AlM342_3*C43
  OpM143_4 = OpM141_4*C43-OpM342_4*S43
  OpM343_4 = OpM141_4*S43+OpM342_4*C43
  AlM143_4 = AlM142_4*C43-AlM342_4*S43
  AlM343_4 = AlM142_4*S43+AlM342_4*C43
  OpM143_5 = OpM141_5*C43-OpM342_5*S43
  OpM343_5 = OpM141_5*S43+OpM342_5*C43
  AlM143_5 = AlM142_5*C43-AlM342_5*S43
  AlM343_5 = AlM142_5*S43+AlM342_5*C43
  OpM143_6 = -(OpM342_6*S43-C41*C43)
  OpM343_6 = OpM342_6*C43+C41*S43
  AlM143_6 = AlM141_6*C43-AlM342_6*S43
  AlM343_6 = AlM141_6*S43+AlM342_6*C43
  OpM143_40 = -(OpM342_40*S43-C41*C43)
  OpM343_40 = OpM342_40*C43+C41*S43
  AlM143_40 = -AlM342_40*S43
  AlM343_40 = AlM342_40*C43
  OpM143_41 = -C42*S43
  OpM343_41 = C42*C43
  AlM143_41 = -s.dpt[2,44]*C43
  AlM343_41 = -s.dpt[2,44]*S43
  OM144 = OM143*C44+OM243*S44
  OM244 = -(OM143*S44-OM243*C44)
  OM344 = qd[44]+OM142*S43+OM342*C43
  OpF144 = C44*(OpF143+qd[44]*OM243)+S44*(OpF242-qd[44]*OM143)
  OpF244 = C44*(OpF242-qd[44]*OM143)-S44*(OpF143+qd[44]*OM243)
  BS544 = -(OM144*OM144+OM344*OM344)
  BS644 = OM244*OM344
  BS944 = -(OM144*OM144+OM244*OM244)
  BeF244 = OM144*OM244-OpF343
  BeF344 = OpF244+OM144*OM344
  BeF644 = BS644-OpF144
  BeF844 = BS644+OpF144
  AlF144 = AlF143*C44+AlF242*S44
  AlF244 = -(AlF143*S44-AlF242*C44)
  AlM144_1 = AlM143_1*C44+AlM242_1*S44
  AlM244_1 = -(AlM143_1*S44-AlM242_1*C44)
  AlM144_2 = AlM143_2*C44+AlM242_2*S44
  AlM244_2 = -(AlM143_2*S44-AlM242_2*C44)
  AlM144_3 = AlM143_3*C44+AlM242_3*S44
  AlM244_3 = -(AlM143_3*S44-AlM242_3*C44)
  OpM144_4 = OpM143_4*C44+OpM242_4*S44
  OpM244_4 = -(OpM143_4*S44-OpM242_4*C44)
  AlM144_4 = AlM143_4*C44+AlM242_4*S44
  AlM244_4 = -(AlM143_4*S44-AlM242_4*C44)
  OpM144_5 = OpM143_5*C44+OpM242_5*S44
  OpM244_5 = -(OpM143_5*S44-OpM242_5*C44)
  AlM144_5 = AlM143_5*C44+AlM242_5*S44
  AlM244_5 = -(AlM143_5*S44-AlM242_5*C44)
  OpM144_6 = OpM143_6*C44+OpM242_6*S44
  OpM244_6 = -(OpM143_6*S44-OpM242_6*C44)
  AlM144_6 = AlM143_6*C44+AlM242_6*S44
  AlM244_6 = -(AlM143_6*S44-AlM242_6*C44)
  OpM144_40 = OpM143_40*C44+OpM242_40*S44
  OpM244_40 = -(OpM143_40*S44-OpM242_40*C44)
  AlM144_40 = AlM143_40*C44+AlM242_40*S44
  AlM244_40 = -(AlM143_40*S44-AlM242_40*C44)
  OpM144_41 = OpM143_41*C44+S42*S44
  OpM244_41 = -(OpM143_41*S44-S42*C44)
  AlM144_41 = AlM143_41*C44
  AlM244_41 = -AlM143_41*S44
  OpM144_42 = C43*C44
  OpM244_42 = -C43*S44

# = = Block_0_1_0_1_0_18 = = 
 
# Forward Kinematics 

  BS549 = -(OM16*OM16+OM36*OM36)
  BeF249 = OM16*OM26-OpF36
  BeF849 = OpF15+OM26*OM36
  AlF149 = AlF15+q[49]*BeF26-(2.0)*qd[49]*OM36+BS16*s.dpt[1,13]
  AlF249 = AlF26+q[49]*BS56+BeF46*s.dpt[1,13]
  AlF349 = AlF36+q[49]*BeF86+(2.0)*qd[49]*OM16+BeF76*s.dpt[1,13]
  AlM149_4 = -q[49]*OpM36_4
  AlM249_4 = OpM36_4*s.dpt[1,13]
  AlM349_4 = -(q[49]*S5+OpM26_4*s.dpt[1,13])
  AlM149_5 = q[49]*S6
  AlM249_5 = -s.dpt[1,13]*S6
  AlM349_5 = -s.dpt[1,13]*C6

# = = Block_0_1_0_1_0_21 = = 
 
# Forward Kinematics 

  OM154 = OM16*C54-OM36*S54
  OM254 = qd[54]+OM26
  OM354 = OM16*S54+OM36*C54
  OpF154 = C54*(OpF15-qd[54]*OM36)-S54*(OpF36+qd[54]*OM16)
  OpF354 = C54*(OpF36+qd[54]*OM16)+S54*(OpF15-qd[54]*OM36)
  BS154 = -(OM254*OM254+OM354*OM354)
  BS254 = OM154*OM254
  BS554 = -(OM154*OM154+OM354*OM354)
  BeF254 = BS254-OpF354
  BeF454 = BS254+OpF354
  BeF754 = OM154*OM354-OpF26
  BeF854 = OpF154+OM254*OM354
  AlF154 = C54*(AlF15+BS16*s.dpt[1,14]+BeF36*s.dpt[3,14])-S54*(AlF36+BS96*s.dpt[3,14]+BeF76*s.dpt[1,14])
  AlF254 = AlF26+BeF46*s.dpt[1,14]+BeF66*s.dpt[3,14]
  AlF354 = C54*(AlF36+BS96*s.dpt[3,14]+BeF76*s.dpt[1,14])+S54*(AlF15+BS16*s.dpt[1,14]+BeF36*s.dpt[3,14])
  AlM154_1 = AlM15_1*C54-AlM36_1*S54
  AlM354_1 = AlM15_1*S54+AlM36_1*C54
  AlM154_2 = AlM15_2*C54-AlM36_2*S54
  AlM354_2 = AlM15_2*S54+AlM36_2*C54
  AlM154_3 = -(AlM36_3*S54+C54*S5)
  AlM354_3 = AlM36_3*C54-S54*S5
  OpM154_4 = -(OpM36_4*S54+C54*S5)
  OpM354_4 = OpM36_4*C54-S54*S5
  AlM154_4 = OpM26_4*(s.dpt[1,14]*S54+s.dpt[3,14]*C54)
  AlM254_4 = OpM36_4*s.dpt[1,14]+s.dpt[3,14]*S5
  AlM354_4 = -OpM26_4*(s.dpt[1,14]*C54-s.dpt[3,14]*S54)
  OpM154_5 = S54*S6
  OpM354_5 = -C54*S6
  AlM154_5 = C6*(s.dpt[1,14]*S54+s.dpt[3,14]*C54)
  AlM254_5 = -s.dpt[1,14]*S6
  AlM354_5 = -C6*(s.dpt[1,14]*C54-s.dpt[3,14]*S54)

# = = Block_0_1_0_1_0_24 = = 
 
# Forward Kinematics 

  OM160 = OM16*C60-OM36*S60
  OM260 = qd[60]+OM26
  OM360 = OM16*S60+OM36*C60
  OpF160 = C60*(OpF15-qd[60]*OM36)-S60*(OpF36+qd[60]*OM16)
  OpF360 = C60*(OpF36+qd[60]*OM16)+S60*(OpF15-qd[60]*OM36)
  BS160 = -(OM260*OM260+OM360*OM360)
  BS260 = OM160*OM260
  BS560 = -(OM160*OM160+OM360*OM360)
  BeF260 = BS260-OpF360
  BeF460 = BS260+OpF360
  BeF760 = OM160*OM360-OpF26
  BeF860 = OpF160+OM260*OM360
  AlF160 = C60*(AlF15+BS16*s.dpt[1,15]+BeF36*s.dpt[3,15])-S60*(AlF36+BS96*s.dpt[3,15]+BeF76*s.dpt[1,15])
  AlF260 = AlF26+BeF46*s.dpt[1,15]+BeF66*s.dpt[3,15]
  AlF360 = C60*(AlF36+BS96*s.dpt[3,15]+BeF76*s.dpt[1,15])+S60*(AlF15+BS16*s.dpt[1,15]+BeF36*s.dpt[3,15])
  AlM160_1 = AlM15_1*C60-AlM36_1*S60
  AlM360_1 = AlM15_1*S60+AlM36_1*C60
  AlM160_2 = AlM15_2*C60-AlM36_2*S60
  AlM360_2 = AlM15_2*S60+AlM36_2*C60
  AlM160_3 = -(AlM36_3*S60+S5*C60)
  AlM360_3 = AlM36_3*C60-S5*S60
  OpM160_4 = -(OpM36_4*S60+S5*C60)
  OpM360_4 = OpM36_4*C60-S5*S60
  AlM160_4 = OpM26_4*(s.dpt[1,15]*S60+s.dpt[3,15]*C60)
  AlM260_4 = OpM36_4*s.dpt[1,15]+s.dpt[3,15]*S5
  AlM360_4 = -OpM26_4*(s.dpt[1,15]*C60-s.dpt[3,15]*S60)
  OpM160_5 = S60*S6
  OpM360_5 = -C60*S6
  AlM160_5 = C6*(s.dpt[1,15]*S60+s.dpt[3,15]*C60)
  AlM260_5 = -s.dpt[1,15]*S6
  AlM360_5 = -C6*(s.dpt[1,15]*C60-s.dpt[3,15]*S60)

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
  AlF113 = AlF110+BeF210*s.dpt[2,20]+BeF310*s.dpt[3,20]
  AlF313 = C13*(AlF310+BS910*s.dpt[3,20]+BeF810*s.dpt[2,20])-S13*(AlF29+BS510*s.dpt[2,20]+BeF610*s.dpt[3,20])
  AlM313_1 = -(AlM29_1*S13-AlM310_1*C13)
  AlM313_2 = -(AlM29_2*S13-AlM310_2*C13)
  AlM313_3 = -(AlM29_3*S13-AlM310_3*C13)
  OpM313_4 = -(OpM29_4*S13-OpM310_4*C13)
  AlM113_4 = AlM110_4+OpM29_4*s.dpt[3,20]-OpM310_4*s.dpt[2,20]
  AlM313_4 = C13*(AlM310_4+OpM110_4*s.dpt[2,20])-S13*(AlM29_4-OpM110_4*s.dpt[3,20])
  OpM313_5 = -(OpM29_5*S13-OpM310_5*C13)
  AlM113_5 = AlM110_5+OpM29_5*s.dpt[3,20]-OpM310_5*s.dpt[2,20]
  AlM313_5 = C13*(AlM310_5+OpM110_5*s.dpt[2,20])-S13*(AlM29_5-OpM110_5*s.dpt[3,20])
  OpM313_6 = -(OpM29_6*S13-OpM310_6*C13)
  AlM113_6 = AlM110_6+OpM29_6*s.dpt[3,20]-OpM310_6*s.dpt[2,20]
  AlM313_6 = C13*(AlM310_6+OpM110_6*s.dpt[2,20])-S13*(AlM29_6-OpM110_6*s.dpt[3,20])
  OpM313_7 = -(OpM29_7*S13-OpM310_7*C13)
  AlM113_7 = AlM110_7+OpM29_7*s.dpt[3,20]-OpM310_7*s.dpt[2,20]
  AlM313_7 = C13*(AlM310_7+OpM110_7*s.dpt[2,20])-S13*(AlM29_7-OpM110_7*s.dpt[3,20])
  OpM313_8 = OpM310_8*C13-S13*S9
  AlM113_8 = -(OpM310_8*s.dpt[2,20]-s.dpt[3,20]*S9)
  AlM313_8 = OpM110_8*(s.dpt[2,20]*C13+s.dpt[3,20]*S13)
  OpM313_9 = S10*C13
  AlM113_9 = -s.dpt[2,20]*S10
  AlM313_9 = C10*(s.dpt[2,20]*C13+s.dpt[3,20]*S13)
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
  AlF121 = AlF118+BeF218*s.dpt[2,27]+BeF318*s.dpt[3,27]
  AlF321 = C21*(AlF318+BS918*s.dpt[3,27]+BeF818*s.dpt[2,27])-S21*(AlF217+BS518*s.dpt[2,27]+BeF618*s.dpt[3,27])
  AlM321_1 = -(AlM217_1*S21-AlM318_1*C21)
  AlM321_2 = -(AlM217_2*S21-AlM318_2*C21)
  AlM321_3 = -(AlM217_3*S21-AlM318_3*C21)
  OpM321_4 = -(OpM217_4*S21-OpM318_4*C21)
  AlM121_4 = AlM118_4+OpM217_4*s.dpt[3,27]-OpM318_4*s.dpt[2,27]
  AlM321_4 = C21*(AlM318_4+OpM118_4*s.dpt[2,27])-S21*(AlM217_4-OpM118_4*s.dpt[3,27])
  OpM321_5 = -(OpM217_5*S21-OpM318_5*C21)
  AlM121_5 = AlM118_5+OpM217_5*s.dpt[3,27]-OpM318_5*s.dpt[2,27]
  AlM321_5 = C21*(AlM318_5+OpM118_5*s.dpt[2,27])-S21*(AlM217_5-OpM118_5*s.dpt[3,27])
  OpM321_6 = -(OpM217_6*S21-OpM318_6*C21)
  AlM121_6 = AlM118_6+OpM217_6*s.dpt[3,27]-OpM318_6*s.dpt[2,27]
  AlM321_6 = C21*(AlM318_6+OpM118_6*s.dpt[2,27])-S21*(AlM217_6-OpM118_6*s.dpt[3,27])
  OpM321_15 = -(OpM217_15*S21-OpM318_15*C21)
  AlM121_15 = AlM118_15+OpM217_15*s.dpt[3,27]-OpM318_15*s.dpt[2,27]
  AlM321_15 = C21*(AlM318_15+OpM118_15*s.dpt[2,27])-S21*(AlM217_15-OpM118_15*s.dpt[3,27])
  OpM321_16 = OpM318_16*C21-S17*S21
  AlM121_16 = -(OpM318_16*s.dpt[2,27]-s.dpt[3,27]*S17)
  AlM321_16 = OpM118_16*(s.dpt[2,27]*C21+s.dpt[3,27]*S21)
  OpM321_17 = S18*C21
  AlM121_17 = -s.dpt[2,27]*S18
  AlM321_17 = C18*(s.dpt[2,27]*C21+s.dpt[3,27]*S21)
  OM122 = OM121*C22-OM321*S22
  OM222 = qd[22]+OM218*C21+OM318*S21
  OM322 = OM121*S22+OM321*C22

# = = Block_0_1_0_2_0_12 = = 
 
# Forward Kinematics 

  OM134 = qd[34]+OM133
  OM234 = OM233*C34+OM333*S34
  OM334 = -(OM233*S34-OM333*C34)
  OpF234 = C34*(OpF233+qd[34]*OM333)+S34*(OpF332-qd[34]*OM233)
  OpM234_4 = OpM233_4*C34+OpM332_4*S34
  OpM234_5 = OpM233_5*C34+OpM332_5*S34
  OpM234_6 = OpM233_6*C34+OpM332_6*S34
  OpM234_29 = OpM233_29*C34+OpM332_29*S34
  OpM234_30 = OpM233_30*C34+OpM332_30*S34
  OpM234_31 = OpM233_31*C34+S32*S34
  OpM234_32 = C33*C34

# = = Block_0_1_0_2_0_13 = = 
 
# Forward Kinematics 

  OM136 = qd[36]+OM133
  OM336 = -(OM233*S36-OM333*C36)
  OpF336 = C36*(OpF332-qd[36]*OM233)-S36*(OpF233+qd[36]*OM333)
  AlF136 = AlF133+BeF233*s.dpt[2,37]+BeF333*s.dpt[3,37]
  AlF336 = C36*(AlF332+BS933*s.dpt[3,37]+BeF833*s.dpt[2,37])-S36*(AlF233+BS533*s.dpt[2,37]+BeF633*s.dpt[3,37])
  AlM336_1 = -(AlM233_1*S36-AlM332_1*C36)
  AlM336_2 = -(AlM233_2*S36-AlM332_2*C36)
  AlM336_3 = -(AlM233_3*S36-AlM332_3*C36)
  OpM336_4 = -(OpM233_4*S36-OpM332_4*C36)
  AlM136_4 = AlM133_4+OpM233_4*s.dpt[3,37]-OpM332_4*s.dpt[2,37]
  AlM336_4 = C36*(AlM332_4+OpM133_4*s.dpt[2,37])-S36*(AlM233_4-OpM133_4*s.dpt[3,37])
  OpM336_5 = -(OpM233_5*S36-OpM332_5*C36)
  AlM136_5 = AlM133_5+OpM233_5*s.dpt[3,37]-OpM332_5*s.dpt[2,37]
  AlM336_5 = C36*(AlM332_5+OpM133_5*s.dpt[2,37])-S36*(AlM233_5-OpM133_5*s.dpt[3,37])
  OpM336_6 = -(OpM233_6*S36-OpM332_6*C36)
  AlM136_6 = AlM133_6+OpM233_6*s.dpt[3,37]-OpM332_6*s.dpt[2,37]
  AlM336_6 = C36*(AlM332_6+OpM133_6*s.dpt[2,37])-S36*(AlM233_6-OpM133_6*s.dpt[3,37])
  OpM336_29 = -(OpM233_29*S36-OpM332_29*C36)
  AlM136_29 = AlM133_29+OpM233_29*s.dpt[3,37]-OpM332_29*s.dpt[2,37]
  AlM336_29 = C36*(AlM332_29+OpM133_29*s.dpt[2,37])-S36*(AlM233_29-OpM133_29*s.dpt[3,37])
  OpM336_30 = -(OpM233_30*S36-OpM332_30*C36)
  AlM136_30 = AlM133_30+OpM233_30*s.dpt[3,37]-OpM332_30*s.dpt[2,37]
  AlM336_30 = C36*(AlM332_30+OpM133_30*s.dpt[2,37])-S36*(AlM233_30-OpM133_30*s.dpt[3,37])
  OpM336_31 = -(OpM233_31*S36-S32*C36)
  AlM136_31 = OpM233_31*s.dpt[3,37]-s.dpt[2,37]*S32
  AlM336_31 = OpM133_31*(s.dpt[2,37]*C36+s.dpt[3,37]*S36)
  OpM336_32 = -C33*S36
  AlM136_32 = s.dpt[3,37]*C33
  AlM336_32 = S33*(s.dpt[2,37]*C36+s.dpt[3,37]*S36)
  OM137 = OM136*C37-OM336*S37
  OM237 = qd[37]+OM233*C36+OM333*S36
  OM337 = OM136*S37+OM336*C37

# = = Block_0_1_0_2_0_16 = = 
 
# Forward Kinematics 

  OM145 = qd[45]+OM144
  OM245 = OM244*C45+OM344*S45
  OM345 = -(OM244*S45-OM344*C45)
  OpF245 = C45*(OpF244+qd[45]*OM344)+S45*(OpF343-qd[45]*OM244)
  OpM245_4 = OpM244_4*C45+OpM343_4*S45
  OpM245_5 = OpM244_5*C45+OpM343_5*S45
  OpM245_6 = OpM244_6*C45+OpM343_6*S45
  OpM245_40 = OpM244_40*C45+OpM343_40*S45
  OpM245_41 = OpM244_41*C45+OpM343_41*S45
  OpM245_42 = OpM244_42*C45+S43*S45
  OpM245_43 = C44*C45

# = = Block_0_1_0_2_0_17 = = 
 
# Forward Kinematics 

  OM147 = qd[47]+OM144
  OM347 = -(OM244*S47-OM344*C47)
  OpF347 = C47*(OpF343-qd[47]*OM244)-S47*(OpF244+qd[47]*OM344)
  AlF147 = AlF144+BeF244*s.dpt[2,48]+BeF344*s.dpt[3,48]
  AlF347 = C47*(AlF343+BS944*s.dpt[3,48]+BeF844*s.dpt[2,48])-S47*(AlF244+BS544*s.dpt[2,48]+BeF644*s.dpt[3,48])
  AlM347_1 = -(AlM244_1*S47-AlM343_1*C47)
  AlM347_2 = -(AlM244_2*S47-AlM343_2*C47)
  AlM347_3 = -(AlM244_3*S47-AlM343_3*C47)
  OpM347_4 = -(OpM244_4*S47-OpM343_4*C47)
  AlM147_4 = AlM144_4+OpM244_4*s.dpt[3,48]-OpM343_4*s.dpt[2,48]
  AlM347_4 = C47*(AlM343_4+OpM144_4*s.dpt[2,48])-S47*(AlM244_4-OpM144_4*s.dpt[3,48])
  OpM347_5 = -(OpM244_5*S47-OpM343_5*C47)
  AlM147_5 = AlM144_5+OpM244_5*s.dpt[3,48]-OpM343_5*s.dpt[2,48]
  AlM347_5 = C47*(AlM343_5+OpM144_5*s.dpt[2,48])-S47*(AlM244_5-OpM144_5*s.dpt[3,48])
  OpM347_6 = -(OpM244_6*S47-OpM343_6*C47)
  AlM147_6 = AlM144_6+OpM244_6*s.dpt[3,48]-OpM343_6*s.dpt[2,48]
  AlM347_6 = C47*(AlM343_6+OpM144_6*s.dpt[2,48])-S47*(AlM244_6-OpM144_6*s.dpt[3,48])
  OpM347_40 = -(OpM244_40*S47-OpM343_40*C47)
  AlM147_40 = AlM144_40+OpM244_40*s.dpt[3,48]-OpM343_40*s.dpt[2,48]
  AlM347_40 = C47*(AlM343_40+OpM144_40*s.dpt[2,48])-S47*(AlM244_40-OpM144_40*s.dpt[3,48])
  OpM347_41 = -(OpM244_41*S47-OpM343_41*C47)
  AlM147_41 = AlM144_41+OpM244_41*s.dpt[3,48]-OpM343_41*s.dpt[2,48]
  AlM347_41 = C47*(AlM343_41+OpM144_41*s.dpt[2,48])-S47*(AlM244_41-OpM144_41*s.dpt[3,48])
  OpM347_42 = -(OpM244_42*S47-S43*C47)
  AlM147_42 = OpM244_42*s.dpt[3,48]-s.dpt[2,48]*S43
  AlM347_42 = OpM144_42*(s.dpt[2,48]*C47+s.dpt[3,48]*S47)
  OpM347_43 = -C44*S47
  AlM147_43 = s.dpt[3,48]*C44
  AlM347_43 = S44*(s.dpt[2,48]*C47+s.dpt[3,48]*S47)
  OM148 = OM147*C48-OM347*S48
  OM248 = qd[48]+OM244*C47+OM344*S47
  OM348 = OM147*S48+OM347*C48

# = = Block_0_1_0_2_0_19 = = 
 
# Forward Kinematics 

  OM250 = -(OM16*S50-OM26*C50)
  OM350 = qd[50]+OM36
  OpF150 = C50*(OpF15+qd[50]*OM26)+S50*(OpF26-qd[50]*OM16)
  AlF250 = C50*(AlF249+BS549*s.dpt[2,52])-S50*(AlF149+BeF249*s.dpt[2,52])
  AlF350 = AlF349+BeF849*s.dpt[2,52]
  AlM250_1 = -(AlM15_1*S50-AlM26_1*C50)
  AlM250_2 = -(AlM15_2*S50-AlM26_2*C50)
  AlM250_3 = AlM26_3*C50+S50*S5
  OpM150_4 = OpM26_4*S50-C50*S5
  AlM250_4 = AlM249_4*C50-S50*(AlM149_4-OpM36_4*s.dpt[2,52])
  AlM350_4 = AlM349_4-s.dpt[2,52]*S5
  OpM150_5 = S50*C6
  AlM250_5 = AlM249_5*C50-S50*(AlM149_5+s.dpt[2,52]*S6)
  AlM350_6 = q[49]+s.dpt[2,52]
  OM151 = qd[51]+OM16*C50+OM26*S50
  OM251 = OM250*C51+OM350*S51
  OM351 = -(OM250*S51-OM350*C51)
  OpF351 = C51*(OpF36-qd[51]*OM250)-S51*(qd[51]*OM350+C50*(OpF26-qd[50]*OM16)-S50*(OpF15+qd[50]*OM26))
  OpM351_4 = OpM36_4*C51-S51*(OpM26_4*C50+S50*S5)
  OpM351_5 = -(C50*S51*C6+C51*S6)
  OpM351_6 = S50*S51

# = = Block_0_1_0_2_0_20 = = 
 
# Forward Kinematics 

  OM252 = -(OM16*S52-OM26*C52)
  OM352 = qd[52]+OM36
  OpF152 = C52*(OpF15+qd[52]*OM26)+S52*(OpF26-qd[52]*OM16)
  AlF252 = C52*(AlF249+BS549*s.dpt[2,53])-S52*(AlF149+BeF249*s.dpt[2,53])
  AlF352 = AlF349+BeF849*s.dpt[2,53]
  AlM252_1 = -(AlM15_1*S52-AlM26_1*C52)
  AlM252_2 = -(AlM15_2*S52-AlM26_2*C52)
  AlM252_3 = AlM26_3*C52+S52*S5
  OpM152_4 = OpM26_4*S52-C52*S5
  AlM252_4 = AlM249_4*C52-S52*(AlM149_4-OpM36_4*s.dpt[2,53])
  AlM352_4 = AlM349_4-s.dpt[2,53]*S5
  OpM152_5 = S52*C6
  AlM252_5 = AlM249_5*C52-S52*(AlM149_5+s.dpt[2,53]*S6)
  AlM352_6 = q[49]+s.dpt[2,53]
  OM153 = qd[53]+OM16*C52+OM26*S52
  OM253 = OM252*C53+OM352*S53
  OM353 = -(OM252*S53-OM352*C53)
  OpF353 = C53*(OpF36-qd[53]*OM252)-S53*(qd[53]*OM352+C52*(OpF26-qd[52]*OM16)-S52*(OpF15+qd[52]*OM26))
  OpM353_4 = OpM36_4*C53-S53*(OpM26_4*C52+S52*S5)
  OpM353_5 = -(C52*S53*C6+C53*S6)
  OpM353_6 = S52*S53

# = = Block_0_1_0_2_0_22 = = 
 
# Trigonometric Variables  

  S54p55 = C54*S55+S54*C55
  C54p55 = C54*C55-S54*S55
  S54p55p56 = C54p55*S56+S54p55*C56
  C54p55p56 = C54p55*C56-S54p55*S56
 
# Forward Kinematics 

  OM155 = OM154*C55-OM354*S55
  OM255 = qd[55]+OM254
  OM355 = OM154*S55+OM354*C55
  OpF155 = C55*(OpF154-qd[55]*OM354)-S55*(OpF354+qd[55]*OM154)
  OpF355 = C55*(OpF354+qd[55]*OM154)+S55*(OpF154-qd[55]*OM354)
  BS155 = -(OM255*OM255+OM355*OM355)
  BS255 = OM155*OM255
  BS555 = -(OM155*OM155+OM355*OM355)
  BeF255 = BS255-OpF355
  BeF455 = BS255+OpF355
  BeF755 = OM155*OM355-OpF26
  BeF855 = OpF155+OM255*OM355
  AlF155 = AlF154*C55-AlF354*S55
  AlF355 = AlF154*S55+AlF354*C55
  AlM155_1 = AlM154_1*C55-AlM354_1*S55
  AlM355_1 = AlM154_1*S55+AlM354_1*C55
  AlM155_2 = AlM154_2*C55-AlM354_2*S55
  AlM355_2 = AlM154_2*S55+AlM354_2*C55
  AlM155_3 = AlM154_3*C55-AlM354_3*S55
  AlM355_3 = AlM154_3*S55+AlM354_3*C55
  OpM155_4 = OpM154_4*C55-OpM354_4*S55
  OpM355_4 = OpM154_4*S55+OpM354_4*C55
  AlM155_4 = AlM154_4*C55-AlM354_4*S55
  AlM355_4 = AlM154_4*S55+AlM354_4*C55
  OpM155_5 = S54p55*S6
  OpM355_5 = -C54p55*S6
  AlM155_5 = AlM154_5*C55-AlM354_5*S55
  AlM355_5 = AlM154_5*S55+AlM354_5*C55
  OM256 = qd[56]+OM255
  OM356 = OM155*S56+OM355*C56
  OpF156 = C56*(OpF155-qd[56]*OM355)-S56*(OpF355+qd[56]*OM155)
  AlF256 = AlF254+BS555*s.dpt[2,57]+BeF455*s.dpt[1,57]
  AlF356 = C56*(AlF355+BeF755*s.dpt[1,57]+BeF855*s.dpt[2,57])+S56*(AlF155+BS155*s.dpt[1,57]+BeF255*s.dpt[2,57])
  AlM356_1 = AlM155_1*S56+AlM355_1*C56
  AlM356_2 = AlM155_2*S56+AlM355_2*C56
  AlM356_3 = AlM155_3*S56+AlM355_3*C56
  OpM156_4 = OpM155_4*C56-OpM355_4*S56
  AlM256_4 = AlM254_4+OpM355_4*s.dpt[1,57]
  AlM356_4 = C56*(AlM355_4+OpM155_4*s.dpt[2,57]-OpM26_4*s.dpt[1,57])+S56*(AlM155_4-OpM355_4*s.dpt[2,57])
  OpM156_5 = S54p55p56*S6
  AlM256_5 = AlM254_5+OpM355_5*s.dpt[1,57]
  AlM356_5 = C56*(AlM355_5+OpM155_5*s.dpt[2,57]-s.dpt[1,57]*C6)+S56*(AlM155_5-OpM355_5*s.dpt[2,57])
  AlM256_6 = -(s.dpt[3,14]-s.dpt[1,57]*S54p55)
  AlM356_6 = s.dpt[2,57]*C54p55p56
  AlM356_54 = -s.dpt[1,57]*C56
  AlM356_55 = -s.dpt[1,57]*C56
  OM157 = qd[57]+OM155*C56-OM355*S56
  OM257 = OM256*C57+OM356*S57
  OM357 = -(OM256*S57-OM356*C57)
  OpF257 = C57*(OpF26+qd[57]*OM356)-S57*(qd[57]*OM256-C56*(OpF355+qd[56]*OM155)-S56*(OpF155-qd[56]*OM355))
  OpM257_4 = OpM26_4*C57+S57*(OpM155_4*S56+OpM355_4*C56)
  OpM257_5 = -(C54p55p56*S57*S6-C57*C6)
  OpM257_6 = S54p55p56*S57

# = = Block_0_1_0_2_0_23 = = 
 
# Trigonometric Variables  

  S54p58 = C54*S58+S54*C58
  C54p58 = C54*C58-S54*S58
 
# Forward Kinematics 

  OM258 = qd[58]+OM254
  OM358 = OM154*S58+OM354*C58
  OpF158 = C58*(OpF154-qd[58]*OM354)-S58*(OpF354+qd[58]*OM154)
  AlF258 = AlF254+BS554*s.dpt[2,56]+BeF454*s.dpt[1,56]
  AlF358 = C58*(AlF354+BeF754*s.dpt[1,56]+BeF854*s.dpt[2,56])+S58*(AlF154+BS154*s.dpt[1,56]+BeF254*s.dpt[2,56])
  AlM358_1 = AlM154_1*S58+AlM354_1*C58
  AlM358_2 = AlM154_2*S58+AlM354_2*C58
  AlM358_3 = AlM154_3*S58+AlM354_3*C58
  OpM158_4 = OpM154_4*C58-OpM354_4*S58
  AlM258_4 = AlM254_4+OpM354_4*s.dpt[1,56]
  AlM358_4 = C58*(AlM354_4+OpM154_4*s.dpt[2,56]-OpM26_4*s.dpt[1,56])+S58*(AlM154_4-OpM354_4*s.dpt[2,56])
  OpM158_5 = S54p58*S6
  AlM258_5 = AlM254_5+OpM354_5*s.dpt[1,56]
  AlM358_5 = C58*(AlM354_5+OpM154_5*s.dpt[2,56]-s.dpt[1,56]*C6)+S58*(AlM154_5-OpM354_5*s.dpt[2,56])
  AlM258_6 = -(s.dpt[3,14]-s.dpt[1,56]*S54)
  AlM358_6 = s.dpt[2,56]*C54p58
  AlM358_54 = -s.dpt[1,56]*C58
  OM159 = qd[59]+OM154*C58-OM354*S58
  OM259 = OM258*C59+OM358*S59
  OM359 = -(OM258*S59-OM358*C59)
  OpF259 = C59*(OpF26+qd[59]*OM358)-S59*(qd[59]*OM258-C58*(OpF354+qd[58]*OM154)-S58*(OpF154-qd[58]*OM354))
  OpM259_4 = OpM26_4*C59+S59*(OpM154_4*S58+OpM354_4*C58)
  OpM259_5 = -(C54p58*S59*S6-C59*C6)
  OpM259_6 = S54p58*S59

# = = Block_0_1_0_2_0_25 = = 
 
# Trigonometric Variables  

  S60p61 = C60*S61+S60*C61
  C60p61 = C60*C61-S60*S61
  S60p61p62 = C60p61*S62+S60p61*C62
  C60p61p62 = C60p61*C62-S60p61*S62
 
# Forward Kinematics 

  OM161 = OM160*C61-OM360*S61
  OM261 = qd[61]+OM260
  OM361 = OM160*S61+OM360*C61
  OpF161 = C61*(OpF160-qd[61]*OM360)-S61*(OpF360+qd[61]*OM160)
  OpF361 = C61*(OpF360+qd[61]*OM160)+S61*(OpF160-qd[61]*OM360)
  BS161 = -(OM261*OM261+OM361*OM361)
  BS261 = OM161*OM261
  BS561 = -(OM161*OM161+OM361*OM361)
  BeF261 = BS261-OpF361
  BeF461 = BS261+OpF361
  BeF761 = OM161*OM361-OpF26
  BeF861 = OpF161+OM261*OM361
  AlF161 = AlF160*C61-AlF360*S61
  AlF361 = AlF160*S61+AlF360*C61
  AlM161_1 = AlM160_1*C61-AlM360_1*S61
  AlM361_1 = AlM160_1*S61+AlM360_1*C61
  AlM161_2 = AlM160_2*C61-AlM360_2*S61
  AlM361_2 = AlM160_2*S61+AlM360_2*C61
  AlM161_3 = AlM160_3*C61-AlM360_3*S61
  AlM361_3 = AlM160_3*S61+AlM360_3*C61
  OpM161_4 = OpM160_4*C61-OpM360_4*S61
  OpM361_4 = OpM160_4*S61+OpM360_4*C61
  AlM161_4 = AlM160_4*C61-AlM360_4*S61
  AlM361_4 = AlM160_4*S61+AlM360_4*C61
  OpM161_5 = S60p61*S6
  OpM361_5 = -C60p61*S6
  AlM161_5 = AlM160_5*C61-AlM360_5*S61
  AlM361_5 = AlM160_5*S61+AlM360_5*C61
  OM262 = qd[62]+OM261
  OM362 = OM161*S62+OM361*C62
  OpF162 = C62*(OpF161-qd[62]*OM361)-S62*(OpF361+qd[62]*OM161)
  AlF262 = AlF260+BS561*s.dpt[2,61]+BeF461*s.dpt[1,61]
  AlF362 = C62*(AlF361+BeF761*s.dpt[1,61]+BeF861*s.dpt[2,61])+S62*(AlF161+BS161*s.dpt[1,61]+BeF261*s.dpt[2,61])
  AlM362_1 = AlM161_1*S62+AlM361_1*C62
  AlM362_2 = AlM161_2*S62+AlM361_2*C62
  AlM362_3 = AlM161_3*S62+AlM361_3*C62
  OpM162_4 = OpM161_4*C62-OpM361_4*S62
  AlM262_4 = AlM260_4+OpM361_4*s.dpt[1,61]
  AlM362_4 = C62*(AlM361_4+OpM161_4*s.dpt[2,61]-OpM26_4*s.dpt[1,61])+S62*(AlM161_4-OpM361_4*s.dpt[2,61])
  OpM162_5 = S60p61p62*S6
  AlM262_5 = AlM260_5+OpM361_5*s.dpt[1,61]
  AlM362_5 = C62*(AlM361_5+OpM161_5*s.dpt[2,61]-s.dpt[1,61]*C6)+S62*(AlM161_5-OpM361_5*s.dpt[2,61])
  AlM262_6 = -(s.dpt[3,15]-s.dpt[1,61]*S60p61)
  AlM362_6 = s.dpt[2,61]*C60p61p62
  AlM362_60 = -s.dpt[1,61]*C62
  AlM362_61 = -s.dpt[1,61]*C62
  OM163 = qd[63]+OM161*C62-OM361*S62
  OM263 = OM262*C63+OM362*S63
  OM363 = -(OM262*S63-OM362*C63)
  OpF263 = C63*(OpF26+qd[63]*OM362)-S63*(qd[63]*OM262-C62*(OpF361+qd[62]*OM161)-S62*(OpF161-qd[62]*OM361))
  OpM263_4 = OpM26_4*C63+S63*(OpM161_4*S62+OpM361_4*C62)
  OpM263_5 = -(C60p61p62*S63*S6-C63*C6)
  OpM263_6 = S60p61p62*S63

# = = Block_0_1_0_2_0_26 = = 
 
# Trigonometric Variables  

  S60p64 = C60*S64+S60*C64
  C60p64 = C60*C64-S60*S64
 
# Forward Kinematics 

  OM264 = qd[64]+OM260
  OM364 = OM160*S64+OM360*C64
  OpF164 = C64*(OpF160-qd[64]*OM360)-S64*(OpF360+qd[64]*OM160)
  AlF264 = AlF260+BS560*s.dpt[2,60]+BeF460*s.dpt[1,60]
  AlF364 = C64*(AlF360+BeF760*s.dpt[1,60]+BeF860*s.dpt[2,60])+S64*(AlF160+BS160*s.dpt[1,60]+BeF260*s.dpt[2,60])
  AlM364_1 = AlM160_1*S64+AlM360_1*C64
  AlM364_2 = AlM160_2*S64+AlM360_2*C64
  AlM364_3 = AlM160_3*S64+AlM360_3*C64
  OpM164_4 = OpM160_4*C64-OpM360_4*S64
  AlM264_4 = AlM260_4+OpM360_4*s.dpt[1,60]
  AlM364_4 = C64*(AlM360_4+OpM160_4*s.dpt[2,60]-OpM26_4*s.dpt[1,60])+S64*(AlM160_4-OpM360_4*s.dpt[2,60])
  OpM164_5 = S60p64*S6
  AlM264_5 = AlM260_5+OpM360_5*s.dpt[1,60]
  AlM364_5 = C64*(AlM360_5+OpM160_5*s.dpt[2,60]-s.dpt[1,60]*C6)+S64*(AlM160_5-OpM360_5*s.dpt[2,60])
  AlM264_6 = -(s.dpt[3,15]-s.dpt[1,60]*S60)
  AlM364_6 = s.dpt[2,60]*C60p64
  AlM364_60 = -s.dpt[1,60]*C64
  OM165 = qd[65]+OM160*C64-OM360*S64
  OM265 = OM264*C65+OM364*S65
  OM365 = -(OM264*S65-OM364*C65)
  OpF265 = C65*(OpF26+qd[65]*OM364)-S65*(qd[65]*OM264-C64*(OpF360+qd[64]*OM160)-S64*(OpF160-qd[64]*OM360))
  OpM265_4 = OpM26_4*C65+S65*(OpM160_4*S64+OpM360_4*C64)
  OpM265_5 = -(C60p64*S65*S6-C65*C6)
  OpM265_6 = S60p64*S65

# = = Block_0_2_0_1_0_3 = = 
 
# Backward Dynamics 

  FA112 = -(s.frc[1,12]-s.m[12]*(AlF110+q[12]*(OpF211+OM111*OM311)+(2.0)*qd[12]*OM211+BeF210*s.dpt[2,19]+BeF310*s.dpt[3,19]+\
   s.l[3,12]*(OpF211+OM111*OM311)))
  FA212 = -(s.frc[2,12]+s.m[12]*(q[12]*(OpF110-OM211*OM311)+(2.0)*qd[12]*OM111+s.l[3,12]*(OpF110-OM211*OM311)-C11*(AlF29+\
   BS510*s.dpt[2,19]+BeF610*s.dpt[3,19])-S11*(AlF310+BS910*s.dpt[3,19]+BeF810*s.dpt[2,19])))
  FA312 = -(s.frc[3,12]-s.m[12]*(C11*(AlF310+BS910*s.dpt[3,19]+BeF810*s.dpt[2,19])-S11*(AlF29+BS510*s.dpt[2,19]+BeF610*\
   s.dpt[3,19])-(q[12]+s.l[3,12])*(OM111*OM111+OM211*OM211)))
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
  FB112_4 = s.m[12]*(AlM110_4+q[12]*OpM211_4+OpM211_4*s.l[3,12]+OpM29_4*s.dpt[3,19]-OpM310_4*s.dpt[2,19])
  FB212_4 = -s.m[12]*(OpM110_4*(q[12]+s.l[3,12])-C11*(AlM29_4-OpM110_4*s.dpt[3,19])-S11*(AlM310_4+OpM110_4*s.dpt[2,19]))
  FB312_4 = s.m[12]*(C11*(AlM310_4+OpM110_4*s.dpt[2,19])-S11*(AlM29_4-OpM110_4*s.dpt[3,19]))
  CM312_4 = -s.In[9,12]*(OpM29_4*S11-OpM310_4*C11)
  FB112_5 = s.m[12]*(AlM110_5+q[12]*OpM211_5+OpM211_5*s.l[3,12]+OpM29_5*s.dpt[3,19]-OpM310_5*s.dpt[2,19])
  FB212_5 = -s.m[12]*(OpM110_5*(q[12]+s.l[3,12])-C11*(AlM29_5-OpM110_5*s.dpt[3,19])-S11*(AlM310_5+OpM110_5*s.dpt[2,19]))
  FB312_5 = s.m[12]*(C11*(AlM310_5+OpM110_5*s.dpt[2,19])-S11*(AlM29_5-OpM110_5*s.dpt[3,19]))
  CM312_5 = -s.In[9,12]*(OpM29_5*S11-OpM310_5*C11)
  FB112_6 = s.m[12]*(AlM110_6+q[12]*OpM211_6+OpM211_6*s.l[3,12]+OpM29_6*s.dpt[3,19]-OpM310_6*s.dpt[2,19])
  FB212_6 = -s.m[12]*(OpM110_6*(q[12]+s.l[3,12])-C11*(AlM29_6-OpM110_6*s.dpt[3,19])-S11*(AlM310_6+OpM110_6*s.dpt[2,19]))
  FB312_6 = s.m[12]*(C11*(AlM310_6+OpM110_6*s.dpt[2,19])-S11*(AlM29_6-OpM110_6*s.dpt[3,19]))
  CM312_6 = -s.In[9,12]*(OpM29_6*S11-OpM310_6*C11)
  FB112_7 = s.m[12]*(AlM110_7+q[12]*OpM211_7+OpM211_7*s.l[3,12]+OpM29_7*s.dpt[3,19]-OpM310_7*s.dpt[2,19])
  FB212_7 = -s.m[12]*(OpM110_7*(q[12]+s.l[3,12])-C11*(AlM29_7-OpM110_7*s.dpt[3,19])-S11*(AlM310_7+OpM110_7*s.dpt[2,19]))
  FB312_7 = s.m[12]*(C11*(AlM310_7+OpM110_7*s.dpt[2,19])-S11*(AlM29_7-OpM110_7*s.dpt[3,19]))
  CM312_7 = -s.In[9,12]*(OpM29_7*S11-OpM310_7*C11)
  FB112_8 = s.m[12]*(OpM211_8*(q[12]+s.l[3,12])-OpM310_8*s.dpt[2,19]+s.dpt[3,19]*S9)
  FB212_8 = -s.m[12]*OpM110_8*(q[12]+s.l[3,12]-s.dpt[2,19]*S11+s.dpt[3,19]*C11)
  FB312_8 = s.m[12]*OpM110_8*(s.dpt[2,19]*C11+s.dpt[3,19]*S11)
  CM312_8 = s.In[9,12]*(OpM310_8*C11-S11*S9)
  FB112_9 = s.m[12]*(OpM211_9*(q[12]+s.l[3,12])-s.dpt[2,19]*S10)
  FB212_9 = -s.m[12]*C10*(q[12]+s.l[3,12]-s.dpt[2,19]*S11+s.dpt[3,19]*C11)
  FB312_9 = s.m[12]*C10*(s.dpt[2,19]*C11+s.dpt[3,19]*S11)
  CM312_9 = s.In[9,12]*S10*C11
  FB112_10 = s.m[12]*(s.dpt[3,19]+q[12]*C11+s.l[3,12]*C11)
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

# = = Block_0_2_0_1_0_4 = = 
 
# Backward Dynamics 

  FA114 = -(s.frc[1,14]-s.m[14]*(AlF113*C14-AlF313*S14))
  FA214 = -(s.frc[2,14]-s.m[14]*(C13*(AlF29+BS510*s.dpt[2,20]+BeF610*s.dpt[3,20])+S13*(AlF310+BS910*s.dpt[3,20]+BeF810*\
   s.dpt[2,20])))
  FA314 = -(s.frc[3,14]-s.m[14]*(AlF113*S14+AlF313*C14))
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
  FB114_4 = s.m[14]*(AlM113_4*C14-AlM313_4*S14)
  FB214_4 = s.m[14]*(C13*(AlM29_4-OpM110_4*s.dpt[3,20])+S13*(AlM310_4+OpM110_4*s.dpt[2,20]))
  FB314_4 = s.m[14]*(AlM113_4*S14+AlM313_4*C14)
  CM114_4 = s.In[1,14]*(OpM110_4*C14-OpM313_4*S14)
  CM214_4 = s.In[5,14]*(OpM29_4*C13+OpM310_4*S13)
  CM314_4 = s.In[9,14]*(OpM110_4*S14+OpM313_4*C14)
  FB114_5 = s.m[14]*(AlM113_5*C14-AlM313_5*S14)
  FB214_5 = s.m[14]*(C13*(AlM29_5-OpM110_5*s.dpt[3,20])+S13*(AlM310_5+OpM110_5*s.dpt[2,20]))
  FB314_5 = s.m[14]*(AlM113_5*S14+AlM313_5*C14)
  CM114_5 = s.In[1,14]*(OpM110_5*C14-OpM313_5*S14)
  CM214_5 = s.In[5,14]*(OpM29_5*C13+OpM310_5*S13)
  CM314_5 = s.In[9,14]*(OpM110_5*S14+OpM313_5*C14)
  FB114_6 = s.m[14]*(AlM113_6*C14-AlM313_6*S14)
  FB214_6 = s.m[14]*(C13*(AlM29_6-OpM110_6*s.dpt[3,20])+S13*(AlM310_6+OpM110_6*s.dpt[2,20]))
  FB314_6 = s.m[14]*(AlM113_6*S14+AlM313_6*C14)
  CM114_6 = s.In[1,14]*(OpM110_6*C14-OpM313_6*S14)
  CM214_6 = s.In[5,14]*(OpM29_6*C13+OpM310_6*S13)
  CM314_6 = s.In[9,14]*(OpM110_6*S14+OpM313_6*C14)
  FB114_7 = s.m[14]*(AlM113_7*C14-AlM313_7*S14)
  FB214_7 = s.m[14]*(C13*(AlM29_7-OpM110_7*s.dpt[3,20])+S13*(AlM310_7+OpM110_7*s.dpt[2,20]))
  FB314_7 = s.m[14]*(AlM113_7*S14+AlM313_7*C14)
  CM114_7 = s.In[1,14]*(OpM110_7*C14-OpM313_7*S14)
  CM214_7 = s.In[5,14]*(OpM29_7*C13+OpM310_7*S13)
  CM314_7 = s.In[9,14]*(OpM110_7*S14+OpM313_7*C14)
  FB114_8 = s.m[14]*(AlM113_8*C14-AlM313_8*S14)
  FB214_8 = s.m[14]*OpM110_8*(s.dpt[2,20]*S13-s.dpt[3,20]*C13)
  FB314_8 = s.m[14]*(AlM113_8*S14+AlM313_8*C14)
  CM114_8 = s.In[1,14]*(OpM110_8*C14-OpM313_8*S14)
  CM214_8 = s.In[5,14]*(OpM310_8*S13+C13*S9)
  CM314_8 = s.In[9,14]*(OpM110_8*S14+OpM313_8*C14)
  FB114_9 = s.m[14]*(AlM113_9*C14-AlM313_9*S14)
  FB214_9 = s.m[14]*C10*(s.dpt[2,20]*S13-s.dpt[3,20]*C13)
  FB314_9 = s.m[14]*(AlM113_9*S14+AlM313_9*C14)
  CM114_9 = -s.In[1,14]*(OpM313_9*S14-C10*C14)
  CM214_9 = s.In[5,14]*S10*S13
  CM314_9 = s.In[9,14]*(OpM313_9*C14+C10*S14)
  CM114_10 = s.In[1,14]*S13*S14
  CM214_10 = s.In[5,14]*C13
  CM314_10 = -s.In[9,14]*S13*C14
  FF13_114 = FA114*C14+FA314*S14
  FF13_314 = -(FA114*S14-FA314*C14)
  CF13_114 = CF114*C14+CF314*S14
  CF13_314 = -(CF114*S14-CF314*C14)
  FM131_114 = FB114_1*C14+FB314_1*S14
  FM131_314 = -(FB114_1*S14-FB314_1*C14)
  FM132_114 = FB114_2*C14+FB314_2*S14
  FM132_314 = -(FB114_2*S14-FB314_2*C14)
  FM133_114 = FB114_3*C14+FB314_3*S14
  FM133_314 = -(FB114_3*S14-FB314_3*C14)
  FM134_114 = FB114_4*C14+FB314_4*S14
  FM134_314 = -(FB114_4*S14-FB314_4*C14)
  CM134_114 = CM114_4*C14+CM314_4*S14
  CM134_314 = -(CM114_4*S14-CM314_4*C14)
  FM135_114 = FB114_5*C14+FB314_5*S14
  FM135_314 = -(FB114_5*S14-FB314_5*C14)
  CM135_114 = CM114_5*C14+CM314_5*S14
  CM135_314 = -(CM114_5*S14-CM314_5*C14)
  FM136_114 = FB114_6*C14+FB314_6*S14
  FM136_314 = -(FB114_6*S14-FB314_6*C14)
  CM136_114 = CM114_6*C14+CM314_6*S14
  CM136_314 = -(CM114_6*S14-CM314_6*C14)
  FM137_114 = FB114_7*C14+FB314_7*S14
  FM137_314 = -(FB114_7*S14-FB314_7*C14)
  CM137_114 = CM114_7*C14+CM314_7*S14
  CM137_314 = -(CM114_7*S14-CM314_7*C14)
  FM138_114 = FB114_8*C14+FB314_8*S14
  FM138_314 = -(FB114_8*S14-FB314_8*C14)
  CM138_114 = CM114_8*C14+CM314_8*S14
  CM138_314 = -(CM114_8*S14-CM314_8*C14)
  FM139_114 = FB114_9*C14+FB314_9*S14
  FM139_314 = -(FB114_9*S14-FB314_9*C14)
  CM139_114 = CM114_9*C14+CM314_9*S14
  CM139_314 = -(CM114_9*S14-CM314_9*C14)
  CM1310_114 = CM114_10*C14+CM314_10*S14
  CM1313_114 = s.In[1,14]*C14*C14+s.In[9,14]*S14*S14

# = = Block_0_2_0_1_0_6 = = 
 
# Backward Dynamics 

  FA120 = -(s.frc[1,20]-s.m[20]*(AlF118+q[20]*(OpF219+OM119*OM319)+(2.0)*qd[20]*OM219+BeF218*s.dpt[2,26]+BeF318*s.dpt[3,26]+\
   s.l[3,20]*(OpF219+OM119*OM319)))
  FA220 = -(s.frc[2,20]+s.m[20]*(q[20]*(OpF118-OM219*OM319)+(2.0)*qd[20]*OM119+s.l[3,20]*(OpF118-OM219*OM319)-C19*(AlF217+\
   BS518*s.dpt[2,26]+BeF618*s.dpt[3,26])-S19*(AlF318+BS918*s.dpt[3,26]+BeF818*s.dpt[2,26])))
  FA320 = -(s.frc[3,20]-s.m[20]*(C19*(AlF318+BS918*s.dpt[3,26]+BeF818*s.dpt[2,26])-S19*(AlF217+BS518*s.dpt[2,26]+BeF618*\
   s.dpt[3,26])-(q[20]+s.l[3,20])*(OM119*OM119+OM219*OM219)))
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
  FB120_4 = s.m[20]*(AlM118_4+q[20]*OpM219_4+OpM217_4*s.dpt[3,26]+OpM219_4*s.l[3,20]-OpM318_4*s.dpt[2,26])
  FB220_4 = -s.m[20]*(OpM118_4*(q[20]+s.l[3,20])-C19*(AlM217_4-OpM118_4*s.dpt[3,26])-S19*(AlM318_4+OpM118_4*s.dpt[2,26])\
   )
  FB320_4 = s.m[20]*(C19*(AlM318_4+OpM118_4*s.dpt[2,26])-S19*(AlM217_4-OpM118_4*s.dpt[3,26]))
  CM320_4 = -s.In[9,20]*(OpM217_4*S19-OpM318_4*C19)
  FB120_5 = s.m[20]*(AlM118_5+q[20]*OpM219_5+OpM217_5*s.dpt[3,26]+OpM219_5*s.l[3,20]-OpM318_5*s.dpt[2,26])
  FB220_5 = -s.m[20]*(OpM118_5*(q[20]+s.l[3,20])-C19*(AlM217_5-OpM118_5*s.dpt[3,26])-S19*(AlM318_5+OpM118_5*s.dpt[2,26])\
   )
  FB320_5 = s.m[20]*(C19*(AlM318_5+OpM118_5*s.dpt[2,26])-S19*(AlM217_5-OpM118_5*s.dpt[3,26]))
  CM320_5 = -s.In[9,20]*(OpM217_5*S19-OpM318_5*C19)
  FB120_6 = s.m[20]*(AlM118_6+q[20]*OpM219_6+OpM217_6*s.dpt[3,26]+OpM219_6*s.l[3,20]-OpM318_6*s.dpt[2,26])
  FB220_6 = -s.m[20]*(OpM118_6*(q[20]+s.l[3,20])-C19*(AlM217_6-OpM118_6*s.dpt[3,26])-S19*(AlM318_6+OpM118_6*s.dpt[2,26])\
   )
  FB320_6 = s.m[20]*(C19*(AlM318_6+OpM118_6*s.dpt[2,26])-S19*(AlM217_6-OpM118_6*s.dpt[3,26]))
  CM320_6 = -s.In[9,20]*(OpM217_6*S19-OpM318_6*C19)
  FB120_15 = s.m[20]*(AlM118_15+q[20]*OpM219_15+OpM217_15*s.dpt[3,26]+OpM219_15*s.l[3,20]-OpM318_15*s.dpt[2,26])
  FB220_15 = -s.m[20]*(OpM118_15*(q[20]+s.l[3,20])-C19*(AlM217_15-OpM118_15*s.dpt[3,26])-S19*(AlM318_15+OpM118_15*\
   s.dpt[2,26]))
  FB320_15 = s.m[20]*(C19*(AlM318_15+OpM118_15*s.dpt[2,26])-S19*(AlM217_15-OpM118_15*s.dpt[3,26]))
  CM320_15 = -s.In[9,20]*(OpM217_15*S19-OpM318_15*C19)
  FB120_16 = s.m[20]*(OpM219_16*(q[20]+s.l[3,20])-OpM318_16*s.dpt[2,26]+s.dpt[3,26]*S17)
  FB220_16 = -s.m[20]*OpM118_16*(q[20]+s.l[3,20]-s.dpt[2,26]*S19+s.dpt[3,26]*C19)
  FB320_16 = s.m[20]*OpM118_16*(s.dpt[2,26]*C19+s.dpt[3,26]*S19)
  CM320_16 = s.In[9,20]*(OpM318_16*C19-S17*S19)
  FB120_17 = s.m[20]*(OpM219_17*(q[20]+s.l[3,20])-s.dpt[2,26]*S18)
  FB220_17 = -s.m[20]*C18*(q[20]+s.l[3,20]-s.dpt[2,26]*S19+s.dpt[3,26]*C19)
  FB320_17 = s.m[20]*C18*(s.dpt[2,26]*C19+s.dpt[3,26]*S19)
  CM320_17 = s.In[9,20]*S18*C19
  FB120_18 = s.m[20]*(s.dpt[3,26]+q[20]*C19+s.l[3,20]*C19)
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

# = = Block_0_2_0_1_0_7 = = 
 
# Backward Dynamics 

  FA122 = -(s.frc[1,22]-s.m[22]*(AlF121*C22-AlF321*S22))
  FA222 = -(s.frc[2,22]-s.m[22]*(C21*(AlF217+BS518*s.dpt[2,27]+BeF618*s.dpt[3,27])+S21*(AlF318+BS918*s.dpt[3,27]+BeF818*\
   s.dpt[2,27])))
  FA322 = -(s.frc[3,22]-s.m[22]*(AlF121*S22+AlF321*C22))
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
  FB122_4 = s.m[22]*(AlM121_4*C22-AlM321_4*S22)
  FB222_4 = s.m[22]*(C21*(AlM217_4-OpM118_4*s.dpt[3,27])+S21*(AlM318_4+OpM118_4*s.dpt[2,27]))
  FB322_4 = s.m[22]*(AlM121_4*S22+AlM321_4*C22)
  CM122_4 = s.In[1,22]*(OpM118_4*C22-OpM321_4*S22)
  CM222_4 = s.In[5,22]*(OpM217_4*C21+OpM318_4*S21)
  CM322_4 = s.In[9,22]*(OpM118_4*S22+OpM321_4*C22)
  FB122_5 = s.m[22]*(AlM121_5*C22-AlM321_5*S22)
  FB222_5 = s.m[22]*(C21*(AlM217_5-OpM118_5*s.dpt[3,27])+S21*(AlM318_5+OpM118_5*s.dpt[2,27]))
  FB322_5 = s.m[22]*(AlM121_5*S22+AlM321_5*C22)
  CM122_5 = s.In[1,22]*(OpM118_5*C22-OpM321_5*S22)
  CM222_5 = s.In[5,22]*(OpM217_5*C21+OpM318_5*S21)
  CM322_5 = s.In[9,22]*(OpM118_5*S22+OpM321_5*C22)
  FB122_6 = s.m[22]*(AlM121_6*C22-AlM321_6*S22)
  FB222_6 = s.m[22]*(C21*(AlM217_6-OpM118_6*s.dpt[3,27])+S21*(AlM318_6+OpM118_6*s.dpt[2,27]))
  FB322_6 = s.m[22]*(AlM121_6*S22+AlM321_6*C22)
  CM122_6 = s.In[1,22]*(OpM118_6*C22-OpM321_6*S22)
  CM222_6 = s.In[5,22]*(OpM217_6*C21+OpM318_6*S21)
  CM322_6 = s.In[9,22]*(OpM118_6*S22+OpM321_6*C22)
  FB122_15 = s.m[22]*(AlM121_15*C22-AlM321_15*S22)
  FB222_15 = s.m[22]*(C21*(AlM217_15-OpM118_15*s.dpt[3,27])+S21*(AlM318_15+OpM118_15*s.dpt[2,27]))
  FB322_15 = s.m[22]*(AlM121_15*S22+AlM321_15*C22)
  CM122_15 = s.In[1,22]*(OpM118_15*C22-OpM321_15*S22)
  CM222_15 = s.In[5,22]*(OpM217_15*C21+OpM318_15*S21)
  CM322_15 = s.In[9,22]*(OpM118_15*S22+OpM321_15*C22)
  FB122_16 = s.m[22]*(AlM121_16*C22-AlM321_16*S22)
  FB222_16 = s.m[22]*OpM118_16*(s.dpt[2,27]*S21-s.dpt[3,27]*C21)
  FB322_16 = s.m[22]*(AlM121_16*S22+AlM321_16*C22)
  CM122_16 = s.In[1,22]*(OpM118_16*C22-OpM321_16*S22)
  CM222_16 = s.In[5,22]*(OpM318_16*S21+S17*C21)
  CM322_16 = s.In[9,22]*(OpM118_16*S22+OpM321_16*C22)
  FB122_17 = s.m[22]*(AlM121_17*C22-AlM321_17*S22)
  FB222_17 = s.m[22]*C18*(s.dpt[2,27]*S21-s.dpt[3,27]*C21)
  FB322_17 = s.m[22]*(AlM121_17*S22+AlM321_17*C22)
  CM122_17 = -s.In[1,22]*(OpM321_17*S22-C18*C22)
  CM222_17 = s.In[5,22]*S18*S21
  CM322_17 = s.In[9,22]*(OpM321_17*C22+C18*S22)
  CM122_18 = s.In[1,22]*S21*S22
  CM222_18 = s.In[5,22]*C21
  CM322_18 = -s.In[9,22]*S21*C22
  FF21_122 = FA122*C22+FA322*S22
  FF21_322 = -(FA122*S22-FA322*C22)
  CF21_122 = CF122*C22+CF322*S22
  CF21_322 = -(CF122*S22-CF322*C22)
  FM211_122 = FB122_1*C22+FB322_1*S22
  FM211_322 = -(FB122_1*S22-FB322_1*C22)
  FM212_122 = FB122_2*C22+FB322_2*S22
  FM212_322 = -(FB122_2*S22-FB322_2*C22)
  FM213_122 = FB122_3*C22+FB322_3*S22
  FM213_322 = -(FB122_3*S22-FB322_3*C22)
  FM214_122 = FB122_4*C22+FB322_4*S22
  FM214_322 = -(FB122_4*S22-FB322_4*C22)
  CM214_122 = CM122_4*C22+CM322_4*S22
  CM214_322 = -(CM122_4*S22-CM322_4*C22)
  FM215_122 = FB122_5*C22+FB322_5*S22
  FM215_322 = -(FB122_5*S22-FB322_5*C22)
  CM215_122 = CM122_5*C22+CM322_5*S22
  CM215_322 = -(CM122_5*S22-CM322_5*C22)
  FM216_122 = FB122_6*C22+FB322_6*S22
  FM216_322 = -(FB122_6*S22-FB322_6*C22)
  CM216_122 = CM122_6*C22+CM322_6*S22
  CM216_322 = -(CM122_6*S22-CM322_6*C22)
  FM2115_122 = FB122_15*C22+FB322_15*S22
  FM2115_322 = -(FB122_15*S22-FB322_15*C22)
  CM2115_122 = CM122_15*C22+CM322_15*S22
  CM2115_322 = -(CM122_15*S22-CM322_15*C22)
  FM2116_122 = FB122_16*C22+FB322_16*S22
  FM2116_322 = -(FB122_16*S22-FB322_16*C22)
  CM2116_122 = CM122_16*C22+CM322_16*S22
  CM2116_322 = -(CM122_16*S22-CM322_16*C22)
  FM2117_122 = FB122_17*C22+FB322_17*S22
  FM2117_322 = -(FB122_17*S22-FB322_17*C22)
  CM2117_122 = CM122_17*C22+CM322_17*S22
  CM2117_322 = -(CM122_17*S22-CM322_17*C22)
  CM2118_122 = CM122_18*C22+CM322_18*S22
  CM2121_122 = s.In[1,22]*C22*C22+s.In[9,22]*S22*S22

# = = Block_0_2_0_1_0_12 = = 
 
# Backward Dynamics 

  FA135 = -(s.frc[1,35]-s.m[35]*(AlF133+q[35]*(OpF234+OM134*OM334)+(2.0)*qd[35]*OM234+BeF233*s.dpt[2,36]+BeF333*s.dpt[3,36]+\
   s.l[3,35]*(OpF234+OM134*OM334)))
  FA235 = -(s.frc[2,35]+s.m[35]*(q[35]*(OpF133-OM234*OM334)+(2.0)*qd[35]*OM134+s.l[3,35]*(OpF133-OM234*OM334)-C34*(AlF233+\
   BS533*s.dpt[2,36]+BeF633*s.dpt[3,36])-S34*(AlF332+BS933*s.dpt[3,36]+BeF833*s.dpt[2,36])))
  FA335 = -(s.frc[3,35]-s.m[35]*(C34*(AlF332+BS933*s.dpt[3,36]+BeF833*s.dpt[2,36])-S34*(AlF233+BS533*s.dpt[2,36]+BeF633*\
   s.dpt[3,36])-(q[35]+s.l[3,35])*(OM134*OM134+OM234*OM234)))
  CF335 = -(s.trq[3,35]-s.In[9,35]*(C34*(OpF332-qd[34]*OM233)-S34*(OpF233+qd[34]*OM333))+OM134*OM234*(s.In[1,35]-\
   s.In[5,35]))
  FB135_1 = s.m[35]*AlM133_1
  FB235_1 = s.m[35]*(AlM233_1*C34+AlM332_1*S34)
  FB335_1 = -s.m[35]*(AlM233_1*S34-AlM332_1*C34)
  FB135_2 = s.m[35]*AlM133_2
  FB235_2 = s.m[35]*(AlM233_2*C34+AlM332_2*S34)
  FB335_2 = -s.m[35]*(AlM233_2*S34-AlM332_2*C34)
  FB135_3 = s.m[35]*AlM133_3
  FB235_3 = s.m[35]*(AlM233_3*C34+AlM332_3*S34)
  FB335_3 = -s.m[35]*(AlM233_3*S34-AlM332_3*C34)
  FB135_4 = s.m[35]*(AlM133_4+q[35]*OpM234_4+OpM233_4*s.dpt[3,36]+OpM234_4*s.l[3,35]-OpM332_4*s.dpt[2,36])
  FB235_4 = -s.m[35]*(OpM133_4*(q[35]+s.l[3,35])-C34*(AlM233_4-OpM133_4*s.dpt[3,36])-S34*(AlM332_4+OpM133_4*s.dpt[2,36])\
   )
  FB335_4 = s.m[35]*(C34*(AlM332_4+OpM133_4*s.dpt[2,36])-S34*(AlM233_4-OpM133_4*s.dpt[3,36]))
  CM335_4 = -s.In[9,35]*(OpM233_4*S34-OpM332_4*C34)
  FB135_5 = s.m[35]*(AlM133_5+q[35]*OpM234_5+OpM233_5*s.dpt[3,36]+OpM234_5*s.l[3,35]-OpM332_5*s.dpt[2,36])
  FB235_5 = -s.m[35]*(OpM133_5*(q[35]+s.l[3,35])-C34*(AlM233_5-OpM133_5*s.dpt[3,36])-S34*(AlM332_5+OpM133_5*s.dpt[2,36])\
   )
  FB335_5 = s.m[35]*(C34*(AlM332_5+OpM133_5*s.dpt[2,36])-S34*(AlM233_5-OpM133_5*s.dpt[3,36]))
  CM335_5 = -s.In[9,35]*(OpM233_5*S34-OpM332_5*C34)
  FB135_6 = s.m[35]*(AlM133_6+q[35]*OpM234_6+OpM233_6*s.dpt[3,36]+OpM234_6*s.l[3,35]-OpM332_6*s.dpt[2,36])
  FB235_6 = -s.m[35]*(OpM133_6*(q[35]+s.l[3,35])-C34*(AlM233_6-OpM133_6*s.dpt[3,36])-S34*(AlM332_6+OpM133_6*s.dpt[2,36])\
   )
  FB335_6 = s.m[35]*(C34*(AlM332_6+OpM133_6*s.dpt[2,36])-S34*(AlM233_6-OpM133_6*s.dpt[3,36]))
  CM335_6 = -s.In[9,35]*(OpM233_6*S34-OpM332_6*C34)
  FB135_29 = s.m[35]*(AlM133_29+q[35]*OpM234_29+OpM233_29*s.dpt[3,36]+OpM234_29*s.l[3,35]-OpM332_29*s.dpt[2,36])
  FB235_29 = -s.m[35]*(OpM133_29*(q[35]+s.l[3,35])-C34*(AlM233_29-OpM133_29*s.dpt[3,36])-S34*(AlM332_29+OpM133_29*\
   s.dpt[2,36]))
  FB335_29 = s.m[35]*(C34*(AlM332_29+OpM133_29*s.dpt[2,36])-S34*(AlM233_29-OpM133_29*s.dpt[3,36]))
  CM335_29 = -s.In[9,35]*(OpM233_29*S34-OpM332_29*C34)
  FB135_30 = s.m[35]*(AlM133_30+q[35]*OpM234_30+OpM233_30*s.dpt[3,36]+OpM234_30*s.l[3,35]-OpM332_30*s.dpt[2,36])
  FB235_30 = -s.m[35]*(OpM133_30*(q[35]+s.l[3,35])-C34*(AlM233_30-OpM133_30*s.dpt[3,36])-S34*(AlM332_30+OpM133_30*\
   s.dpt[2,36]))
  FB335_30 = s.m[35]*(C34*(AlM332_30+OpM133_30*s.dpt[2,36])-S34*(AlM233_30-OpM133_30*s.dpt[3,36]))
  CM335_30 = -s.In[9,35]*(OpM233_30*S34-OpM332_30*C34)
  FB135_31 = s.m[35]*(q[35]*OpM234_31+OpM233_31*s.dpt[3,36]+OpM234_31*s.l[3,35]-s.dpt[2,36]*S32)
  FB235_31 = -s.m[35]*OpM133_31*(q[35]+s.l[3,35]-s.dpt[2,36]*S34+s.dpt[3,36]*C34)
  FB335_31 = s.m[35]*OpM133_31*(s.dpt[2,36]*C34+s.dpt[3,36]*S34)
  CM335_31 = -s.In[9,35]*(OpM233_31*S34-S32*C34)
  FB135_32 = s.m[35]*(OpM234_32*(q[35]+s.l[3,35])+s.dpt[3,36]*C33)
  FB235_32 = -s.m[35]*S33*(q[35]+s.l[3,35]-s.dpt[2,36]*S34+s.dpt[3,36]*C34)
  FB335_32 = s.m[35]*S33*(s.dpt[2,36]*C34+s.dpt[3,36]*S34)
  CM335_32 = -s.In[9,35]*C33*S34
  FB135_33 = -s.m[35]*(s.dpt[2,36]-q[35]*S34-s.l[3,35]*S34)
  FB235_34 = -s.m[35]*(q[35]+s.l[3,35])
  CF34_135 = -(s.trq[1,35]+q[35]*FA235-s.In[1,35]*OpF133+FA235*s.l[3,35]+OM234*OM334*(s.In[5,35]-s.In[9,35]))
  CF34_235 = -(s.trq[2,35]-q[35]*FA135-s.In[5,35]*OpF234-FA135*s.l[3,35]-OM134*OM334*(s.In[1,35]-s.In[9,35]))
  CM341_135 = -FB235_1*(q[35]+s.l[3,35])
  CM341_235 = FB135_1*(q[35]+s.l[3,35])
  CM342_135 = -FB235_2*(q[35]+s.l[3,35])
  CM342_235 = FB135_2*(q[35]+s.l[3,35])
  CM343_135 = -FB235_3*(q[35]+s.l[3,35])
  CM343_235 = FB135_3*(q[35]+s.l[3,35])
  CM344_135 = s.In[1,35]*OpM133_4-FB235_4*s.l[3,35]-q[35]*FB235_4
  CM344_235 = q[35]*FB135_4+s.In[5,35]*OpM234_4+FB135_4*s.l[3,35]
  CM345_135 = s.In[1,35]*OpM133_5-FB235_5*s.l[3,35]-q[35]*FB235_5
  CM345_235 = q[35]*FB135_5+s.In[5,35]*OpM234_5+FB135_5*s.l[3,35]
  CM346_135 = s.In[1,35]*OpM133_6-FB235_6*s.l[3,35]-q[35]*FB235_6
  CM346_235 = q[35]*FB135_6+s.In[5,35]*OpM234_6+FB135_6*s.l[3,35]
  CM3429_135 = s.In[1,35]*OpM133_29-FB235_29*s.l[3,35]-q[35]*FB235_29
  CM3429_235 = q[35]*FB135_29+s.In[5,35]*OpM234_29+FB135_29*s.l[3,35]
  CM3430_135 = s.In[1,35]*OpM133_30-FB235_30*s.l[3,35]-q[35]*FB235_30
  CM3430_235 = q[35]*FB135_30+s.In[5,35]*OpM234_30+FB135_30*s.l[3,35]
  CM3431_135 = s.In[1,35]*OpM133_31-FB235_31*s.l[3,35]-q[35]*FB235_31
  CM3431_235 = q[35]*FB135_31+s.In[5,35]*OpM234_31+FB135_31*s.l[3,35]
  CM3432_135 = s.In[1,35]*S33-FB235_32*s.l[3,35]-q[35]*FB235_32
  CM3432_235 = q[35]*FB135_32+s.In[5,35]*OpM234_32+FB135_32*s.l[3,35]
  CM3434_135 = s.In[1,35]-q[35]*FB235_34-FB235_34*s.l[3,35]

# = = Block_0_2_0_1_0_13 = = 
 
# Backward Dynamics 

  FA137 = -(s.frc[1,37]-s.m[37]*(AlF136*C37-AlF336*S37))
  FA237 = -(s.frc[2,37]-s.m[37]*(C36*(AlF233+BS533*s.dpt[2,37]+BeF633*s.dpt[3,37])+S36*(AlF332+BS933*s.dpt[3,37]+BeF833*\
   s.dpt[2,37])))
  FA337 = -(s.frc[3,37]-s.m[37]*(AlF136*S37+AlF336*C37))
  CF137 = -(s.trq[1,37]-s.In[1,37]*(C37*(OpF133-qd[37]*OM336)-S37*(OpF336+qd[37]*OM136))+OM237*OM337*(s.In[5,37]-\
   s.In[9,37]))
  CF237 = -(s.trq[2,37]-s.In[5,37]*(C36*(OpF233+qd[36]*OM333)+S36*(OpF332-qd[36]*OM233))-OM137*OM337*(s.In[1,37]-\
   s.In[9,37]))
  CF337 = -(s.trq[3,37]-s.In[9,37]*(C37*(OpF336+qd[37]*OM136)+S37*(OpF133-qd[37]*OM336))+OM137*OM237*(s.In[1,37]-\
   s.In[5,37]))
  FB137_1 = s.m[37]*(AlM133_1*C37-AlM336_1*S37)
  FB237_1 = s.m[37]*(AlM233_1*C36+AlM332_1*S36)
  FB337_1 = s.m[37]*(AlM133_1*S37+AlM336_1*C37)
  FB137_2 = s.m[37]*(AlM133_2*C37-AlM336_2*S37)
  FB237_2 = s.m[37]*(AlM233_2*C36+AlM332_2*S36)
  FB337_2 = s.m[37]*(AlM133_2*S37+AlM336_2*C37)
  FB137_3 = s.m[37]*(AlM133_3*C37-AlM336_3*S37)
  FB237_3 = s.m[37]*(AlM233_3*C36+AlM332_3*S36)
  FB337_3 = s.m[37]*(AlM133_3*S37+AlM336_3*C37)
  FB137_4 = s.m[37]*(AlM136_4*C37-AlM336_4*S37)
  FB237_4 = s.m[37]*(C36*(AlM233_4-OpM133_4*s.dpt[3,37])+S36*(AlM332_4+OpM133_4*s.dpt[2,37]))
  FB337_4 = s.m[37]*(AlM136_4*S37+AlM336_4*C37)
  CM137_4 = s.In[1,37]*(OpM133_4*C37-OpM336_4*S37)
  CM237_4 = s.In[5,37]*(OpM233_4*C36+OpM332_4*S36)
  CM337_4 = s.In[9,37]*(OpM133_4*S37+OpM336_4*C37)
  FB137_5 = s.m[37]*(AlM136_5*C37-AlM336_5*S37)
  FB237_5 = s.m[37]*(C36*(AlM233_5-OpM133_5*s.dpt[3,37])+S36*(AlM332_5+OpM133_5*s.dpt[2,37]))
  FB337_5 = s.m[37]*(AlM136_5*S37+AlM336_5*C37)
  CM137_5 = s.In[1,37]*(OpM133_5*C37-OpM336_5*S37)
  CM237_5 = s.In[5,37]*(OpM233_5*C36+OpM332_5*S36)
  CM337_5 = s.In[9,37]*(OpM133_5*S37+OpM336_5*C37)
  FB137_6 = s.m[37]*(AlM136_6*C37-AlM336_6*S37)
  FB237_6 = s.m[37]*(C36*(AlM233_6-OpM133_6*s.dpt[3,37])+S36*(AlM332_6+OpM133_6*s.dpt[2,37]))
  FB337_6 = s.m[37]*(AlM136_6*S37+AlM336_6*C37)
  CM137_6 = s.In[1,37]*(OpM133_6*C37-OpM336_6*S37)
  CM237_6 = s.In[5,37]*(OpM233_6*C36+OpM332_6*S36)
  CM337_6 = s.In[9,37]*(OpM133_6*S37+OpM336_6*C37)
  FB137_29 = s.m[37]*(AlM136_29*C37-AlM336_29*S37)
  FB237_29 = s.m[37]*(C36*(AlM233_29-OpM133_29*s.dpt[3,37])+S36*(AlM332_29+OpM133_29*s.dpt[2,37]))
  FB337_29 = s.m[37]*(AlM136_29*S37+AlM336_29*C37)
  CM137_29 = s.In[1,37]*(OpM133_29*C37-OpM336_29*S37)
  CM237_29 = s.In[5,37]*(OpM233_29*C36+OpM332_29*S36)
  CM337_29 = s.In[9,37]*(OpM133_29*S37+OpM336_29*C37)
  FB137_30 = s.m[37]*(AlM136_30*C37-AlM336_30*S37)
  FB237_30 = s.m[37]*(C36*(AlM233_30-OpM133_30*s.dpt[3,37])+S36*(AlM332_30+OpM133_30*s.dpt[2,37]))
  FB337_30 = s.m[37]*(AlM136_30*S37+AlM336_30*C37)
  CM137_30 = s.In[1,37]*(OpM133_30*C37-OpM336_30*S37)
  CM237_30 = s.In[5,37]*(OpM233_30*C36+OpM332_30*S36)
  CM337_30 = s.In[9,37]*(OpM133_30*S37+OpM336_30*C37)
  FB137_31 = s.m[37]*(AlM136_31*C37-AlM336_31*S37)
  FB237_31 = s.m[37]*OpM133_31*(s.dpt[2,37]*S36-s.dpt[3,37]*C36)
  FB337_31 = s.m[37]*(AlM136_31*S37+AlM336_31*C37)
  CM137_31 = s.In[1,37]*(OpM133_31*C37-OpM336_31*S37)
  CM237_31 = s.In[5,37]*(OpM233_31*C36+S32*S36)
  CM337_31 = s.In[9,37]*(OpM133_31*S37+OpM336_31*C37)
  FB137_32 = s.m[37]*(AlM136_32*C37-AlM336_32*S37)
  FB237_32 = s.m[37]*S33*(s.dpt[2,37]*S36-s.dpt[3,37]*C36)
  FB337_32 = s.m[37]*(AlM136_32*S37+AlM336_32*C37)
  CM137_32 = -s.In[1,37]*(OpM336_32*S37-S33*C37)
  CM237_32 = s.In[5,37]*C33*C36
  CM337_32 = s.In[9,37]*(OpM336_32*C37+S33*S37)
  CM137_33 = -s.In[1,37]*C36*S37
  CM237_33 = s.In[5,37]*S36
  CM337_33 = s.In[9,37]*C36*C37
  FF36_137 = FA137*C37+FA337*S37
  FF36_337 = -(FA137*S37-FA337*C37)
  CF36_137 = CF137*C37+CF337*S37
  CF36_337 = -(CF137*S37-CF337*C37)
  FM361_137 = FB137_1*C37+FB337_1*S37
  FM361_337 = -(FB137_1*S37-FB337_1*C37)
  FM362_137 = FB137_2*C37+FB337_2*S37
  FM362_337 = -(FB137_2*S37-FB337_2*C37)
  FM363_137 = FB137_3*C37+FB337_3*S37
  FM363_337 = -(FB137_3*S37-FB337_3*C37)
  FM364_137 = FB137_4*C37+FB337_4*S37
  FM364_337 = -(FB137_4*S37-FB337_4*C37)
  CM364_137 = CM137_4*C37+CM337_4*S37
  CM364_337 = -(CM137_4*S37-CM337_4*C37)
  FM365_137 = FB137_5*C37+FB337_5*S37
  FM365_337 = -(FB137_5*S37-FB337_5*C37)
  CM365_137 = CM137_5*C37+CM337_5*S37
  CM365_337 = -(CM137_5*S37-CM337_5*C37)
  FM366_137 = FB137_6*C37+FB337_6*S37
  FM366_337 = -(FB137_6*S37-FB337_6*C37)
  CM366_137 = CM137_6*C37+CM337_6*S37
  CM366_337 = -(CM137_6*S37-CM337_6*C37)
  FM3629_137 = FB137_29*C37+FB337_29*S37
  FM3629_337 = -(FB137_29*S37-FB337_29*C37)
  CM3629_137 = CM137_29*C37+CM337_29*S37
  CM3629_337 = -(CM137_29*S37-CM337_29*C37)
  FM3630_137 = FB137_30*C37+FB337_30*S37
  FM3630_337 = -(FB137_30*S37-FB337_30*C37)
  CM3630_137 = CM137_30*C37+CM337_30*S37
  CM3630_337 = -(CM137_30*S37-CM337_30*C37)
  FM3631_137 = FB137_31*C37+FB337_31*S37
  FM3631_337 = -(FB137_31*S37-FB337_31*C37)
  CM3631_137 = CM137_31*C37+CM337_31*S37
  CM3631_337 = -(CM137_31*S37-CM337_31*C37)
  FM3632_137 = FB137_32*C37+FB337_32*S37
  FM3632_337 = -(FB137_32*S37-FB337_32*C37)
  CM3632_137 = CM137_32*C37+CM337_32*S37
  CM3632_337 = -(CM137_32*S37-CM337_32*C37)
  CM3633_137 = CM137_33*C37+CM337_33*S37
  CM3636_137 = s.In[1,37]*C37*C37+s.In[9,37]*S37*S37

# = = Block_0_2_0_1_0_16 = = 
 
# Backward Dynamics 

  FA146 = -(s.frc[1,46]-s.m[46]*(AlF144+q[46]*(OpF245+OM145*OM345)+(2.0)*qd[46]*OM245+BeF244*s.dpt[2,47]+BeF344*s.dpt[3,47]+\
   s.l[3,46]*(OpF245+OM145*OM345)))
  FA246 = -(s.frc[2,46]+s.m[46]*(q[46]*(OpF144-OM245*OM345)+(2.0)*qd[46]*OM145+s.l[3,46]*(OpF144-OM245*OM345)-C45*(AlF244+\
   BS544*s.dpt[2,47]+BeF644*s.dpt[3,47])-S45*(AlF343+BS944*s.dpt[3,47]+BeF844*s.dpt[2,47])))
  FA346 = -(s.frc[3,46]-s.m[46]*(C45*(AlF343+BS944*s.dpt[3,47]+BeF844*s.dpt[2,47])-S45*(AlF244+BS544*s.dpt[2,47]+BeF644*\
   s.dpt[3,47])-(q[46]+s.l[3,46])*(OM145*OM145+OM245*OM245)))
  CF346 = -(s.trq[3,46]-s.In[9,46]*(C45*(OpF343-qd[45]*OM244)-S45*(OpF244+qd[45]*OM344))+OM145*OM245*(s.In[1,46]-\
   s.In[5,46]))
  FB146_1 = s.m[46]*AlM144_1
  FB246_1 = s.m[46]*(AlM244_1*C45+AlM343_1*S45)
  FB346_1 = -s.m[46]*(AlM244_1*S45-AlM343_1*C45)
  FB146_2 = s.m[46]*AlM144_2
  FB246_2 = s.m[46]*(AlM244_2*C45+AlM343_2*S45)
  FB346_2 = -s.m[46]*(AlM244_2*S45-AlM343_2*C45)
  FB146_3 = s.m[46]*AlM144_3
  FB246_3 = s.m[46]*(AlM244_3*C45+AlM343_3*S45)
  FB346_3 = -s.m[46]*(AlM244_3*S45-AlM343_3*C45)
  FB146_4 = s.m[46]*(AlM144_4+q[46]*OpM245_4+OpM244_4*s.dpt[3,47]+OpM245_4*s.l[3,46]-OpM343_4*s.dpt[2,47])
  FB246_4 = -s.m[46]*(OpM144_4*(q[46]+s.l[3,46])-C45*(AlM244_4-OpM144_4*s.dpt[3,47])-S45*(AlM343_4+OpM144_4*s.dpt[2,47])\
   )
  FB346_4 = s.m[46]*(C45*(AlM343_4+OpM144_4*s.dpt[2,47])-S45*(AlM244_4-OpM144_4*s.dpt[3,47]))
  CM346_4 = -s.In[9,46]*(OpM244_4*S45-OpM343_4*C45)
  FB146_5 = s.m[46]*(AlM144_5+q[46]*OpM245_5+OpM244_5*s.dpt[3,47]+OpM245_5*s.l[3,46]-OpM343_5*s.dpt[2,47])
  FB246_5 = -s.m[46]*(OpM144_5*(q[46]+s.l[3,46])-C45*(AlM244_5-OpM144_5*s.dpt[3,47])-S45*(AlM343_5+OpM144_5*s.dpt[2,47])\
   )
  FB346_5 = s.m[46]*(C45*(AlM343_5+OpM144_5*s.dpt[2,47])-S45*(AlM244_5-OpM144_5*s.dpt[3,47]))
  CM346_5 = -s.In[9,46]*(OpM244_5*S45-OpM343_5*C45)
  FB146_6 = s.m[46]*(AlM144_6+q[46]*OpM245_6+OpM244_6*s.dpt[3,47]+OpM245_6*s.l[3,46]-OpM343_6*s.dpt[2,47])
  FB246_6 = -s.m[46]*(OpM144_6*(q[46]+s.l[3,46])-C45*(AlM244_6-OpM144_6*s.dpt[3,47])-S45*(AlM343_6+OpM144_6*s.dpt[2,47])\
   )
  FB346_6 = s.m[46]*(C45*(AlM343_6+OpM144_6*s.dpt[2,47])-S45*(AlM244_6-OpM144_6*s.dpt[3,47]))
  CM346_6 = -s.In[9,46]*(OpM244_6*S45-OpM343_6*C45)
  FB146_40 = s.m[46]*(AlM144_40+q[46]*OpM245_40+OpM244_40*s.dpt[3,47]+OpM245_40*s.l[3,46]-OpM343_40*s.dpt[2,47])
  FB246_40 = -s.m[46]*(OpM144_40*(q[46]+s.l[3,46])-C45*(AlM244_40-OpM144_40*s.dpt[3,47])-S45*(AlM343_40+OpM144_40*\
   s.dpt[2,47]))
  FB346_40 = s.m[46]*(C45*(AlM343_40+OpM144_40*s.dpt[2,47])-S45*(AlM244_40-OpM144_40*s.dpt[3,47]))
  CM346_40 = -s.In[9,46]*(OpM244_40*S45-OpM343_40*C45)
  FB146_41 = s.m[46]*(AlM144_41+q[46]*OpM245_41+OpM244_41*s.dpt[3,47]+OpM245_41*s.l[3,46]-OpM343_41*s.dpt[2,47])
  FB246_41 = -s.m[46]*(OpM144_41*(q[46]+s.l[3,46])-C45*(AlM244_41-OpM144_41*s.dpt[3,47])-S45*(AlM343_41+OpM144_41*\
   s.dpt[2,47]))
  FB346_41 = s.m[46]*(C45*(AlM343_41+OpM144_41*s.dpt[2,47])-S45*(AlM244_41-OpM144_41*s.dpt[3,47]))
  CM346_41 = -s.In[9,46]*(OpM244_41*S45-OpM343_41*C45)
  FB146_42 = s.m[46]*(q[46]*OpM245_42+OpM244_42*s.dpt[3,47]+OpM245_42*s.l[3,46]-s.dpt[2,47]*S43)
  FB246_42 = -s.m[46]*OpM144_42*(q[46]+s.l[3,46]-s.dpt[2,47]*S45+s.dpt[3,47]*C45)
  FB346_42 = s.m[46]*OpM144_42*(s.dpt[2,47]*C45+s.dpt[3,47]*S45)
  CM346_42 = -s.In[9,46]*(OpM244_42*S45-S43*C45)
  FB146_43 = s.m[46]*(OpM245_43*(q[46]+s.l[3,46])+s.dpt[3,47]*C44)
  FB246_43 = -s.m[46]*S44*(q[46]+s.l[3,46]-s.dpt[2,47]*S45+s.dpt[3,47]*C45)
  FB346_43 = s.m[46]*S44*(s.dpt[2,47]*C45+s.dpt[3,47]*S45)
  CM346_43 = -s.In[9,46]*C44*S45
  FB146_44 = -s.m[46]*(s.dpt[2,47]-q[46]*S45-s.l[3,46]*S45)
  FB246_45 = -s.m[46]*(q[46]+s.l[3,46])
  CF45_146 = -(s.trq[1,46]+q[46]*FA246-s.In[1,46]*OpF144+FA246*s.l[3,46]+OM245*OM345*(s.In[5,46]-s.In[9,46]))
  CF45_246 = -(s.trq[2,46]-q[46]*FA146-s.In[5,46]*OpF245-FA146*s.l[3,46]-OM145*OM345*(s.In[1,46]-s.In[9,46]))
  CM451_146 = -FB246_1*(q[46]+s.l[3,46])
  CM451_246 = FB146_1*(q[46]+s.l[3,46])
  CM452_146 = -FB246_2*(q[46]+s.l[3,46])
  CM452_246 = FB146_2*(q[46]+s.l[3,46])
  CM453_146 = -FB246_3*(q[46]+s.l[3,46])
  CM453_246 = FB146_3*(q[46]+s.l[3,46])
  CM454_146 = s.In[1,46]*OpM144_4-FB246_4*s.l[3,46]-q[46]*FB246_4
  CM454_246 = q[46]*FB146_4+s.In[5,46]*OpM245_4+FB146_4*s.l[3,46]
  CM455_146 = s.In[1,46]*OpM144_5-FB246_5*s.l[3,46]-q[46]*FB246_5
  CM455_246 = q[46]*FB146_5+s.In[5,46]*OpM245_5+FB146_5*s.l[3,46]
  CM456_146 = s.In[1,46]*OpM144_6-FB246_6*s.l[3,46]-q[46]*FB246_6
  CM456_246 = q[46]*FB146_6+s.In[5,46]*OpM245_6+FB146_6*s.l[3,46]
  CM4540_146 = s.In[1,46]*OpM144_40-FB246_40*s.l[3,46]-q[46]*FB246_40
  CM4540_246 = q[46]*FB146_40+s.In[5,46]*OpM245_40+FB146_40*s.l[3,46]
  CM4541_146 = s.In[1,46]*OpM144_41-FB246_41*s.l[3,46]-q[46]*FB246_41
  CM4541_246 = q[46]*FB146_41+s.In[5,46]*OpM245_41+FB146_41*s.l[3,46]
  CM4542_146 = s.In[1,46]*OpM144_42-FB246_42*s.l[3,46]-q[46]*FB246_42
  CM4542_246 = q[46]*FB146_42+s.In[5,46]*OpM245_42+FB146_42*s.l[3,46]
  CM4543_146 = s.In[1,46]*S44-FB246_43*s.l[3,46]-q[46]*FB246_43
  CM4543_246 = q[46]*FB146_43+s.In[5,46]*OpM245_43+FB146_43*s.l[3,46]
  CM4545_146 = s.In[1,46]-q[46]*FB246_45-FB246_45*s.l[3,46]

# = = Block_0_2_0_1_0_17 = = 
 
# Backward Dynamics 

  FA148 = -(s.frc[1,48]-s.m[48]*(AlF147*C48-AlF347*S48))
  FA248 = -(s.frc[2,48]-s.m[48]*(C47*(AlF244+BS544*s.dpt[2,48]+BeF644*s.dpt[3,48])+S47*(AlF343+BS944*s.dpt[3,48]+BeF844*\
   s.dpt[2,48])))
  FA348 = -(s.frc[3,48]-s.m[48]*(AlF147*S48+AlF347*C48))
  CF148 = -(s.trq[1,48]-s.In[1,48]*(C48*(OpF144-qd[48]*OM347)-S48*(OpF347+qd[48]*OM147))+OM248*OM348*(s.In[5,48]-\
   s.In[9,48]))
  CF248 = -(s.trq[2,48]-s.In[5,48]*(C47*(OpF244+qd[47]*OM344)+S47*(OpF343-qd[47]*OM244))-OM148*OM348*(s.In[1,48]-\
   s.In[9,48]))
  CF348 = -(s.trq[3,48]-s.In[9,48]*(C48*(OpF347+qd[48]*OM147)+S48*(OpF144-qd[48]*OM347))+OM148*OM248*(s.In[1,48]-\
   s.In[5,48]))
  FB148_1 = s.m[48]*(AlM144_1*C48-AlM347_1*S48)
  FB248_1 = s.m[48]*(AlM244_1*C47+AlM343_1*S47)
  FB348_1 = s.m[48]*(AlM144_1*S48+AlM347_1*C48)
  FB148_2 = s.m[48]*(AlM144_2*C48-AlM347_2*S48)
  FB248_2 = s.m[48]*(AlM244_2*C47+AlM343_2*S47)
  FB348_2 = s.m[48]*(AlM144_2*S48+AlM347_2*C48)
  FB148_3 = s.m[48]*(AlM144_3*C48-AlM347_3*S48)
  FB248_3 = s.m[48]*(AlM244_3*C47+AlM343_3*S47)
  FB348_3 = s.m[48]*(AlM144_3*S48+AlM347_3*C48)
  FB148_4 = s.m[48]*(AlM147_4*C48-AlM347_4*S48)
  FB248_4 = s.m[48]*(C47*(AlM244_4-OpM144_4*s.dpt[3,48])+S47*(AlM343_4+OpM144_4*s.dpt[2,48]))
  FB348_4 = s.m[48]*(AlM147_4*S48+AlM347_4*C48)
  CM148_4 = s.In[1,48]*(OpM144_4*C48-OpM347_4*S48)
  CM248_4 = s.In[5,48]*(OpM244_4*C47+OpM343_4*S47)
  CM348_4 = s.In[9,48]*(OpM144_4*S48+OpM347_4*C48)
  FB148_5 = s.m[48]*(AlM147_5*C48-AlM347_5*S48)
  FB248_5 = s.m[48]*(C47*(AlM244_5-OpM144_5*s.dpt[3,48])+S47*(AlM343_5+OpM144_5*s.dpt[2,48]))
  FB348_5 = s.m[48]*(AlM147_5*S48+AlM347_5*C48)
  CM148_5 = s.In[1,48]*(OpM144_5*C48-OpM347_5*S48)
  CM248_5 = s.In[5,48]*(OpM244_5*C47+OpM343_5*S47)
  CM348_5 = s.In[9,48]*(OpM144_5*S48+OpM347_5*C48)
  FB148_6 = s.m[48]*(AlM147_6*C48-AlM347_6*S48)
  FB248_6 = s.m[48]*(C47*(AlM244_6-OpM144_6*s.dpt[3,48])+S47*(AlM343_6+OpM144_6*s.dpt[2,48]))
  FB348_6 = s.m[48]*(AlM147_6*S48+AlM347_6*C48)
  CM148_6 = s.In[1,48]*(OpM144_6*C48-OpM347_6*S48)
  CM248_6 = s.In[5,48]*(OpM244_6*C47+OpM343_6*S47)
  CM348_6 = s.In[9,48]*(OpM144_6*S48+OpM347_6*C48)
  FB148_40 = s.m[48]*(AlM147_40*C48-AlM347_40*S48)
  FB248_40 = s.m[48]*(C47*(AlM244_40-OpM144_40*s.dpt[3,48])+S47*(AlM343_40+OpM144_40*s.dpt[2,48]))
  FB348_40 = s.m[48]*(AlM147_40*S48+AlM347_40*C48)
  CM148_40 = s.In[1,48]*(OpM144_40*C48-OpM347_40*S48)
  CM248_40 = s.In[5,48]*(OpM244_40*C47+OpM343_40*S47)
  CM348_40 = s.In[9,48]*(OpM144_40*S48+OpM347_40*C48)
  FB148_41 = s.m[48]*(AlM147_41*C48-AlM347_41*S48)
  FB248_41 = s.m[48]*(C47*(AlM244_41-OpM144_41*s.dpt[3,48])+S47*(AlM343_41+OpM144_41*s.dpt[2,48]))
  FB348_41 = s.m[48]*(AlM147_41*S48+AlM347_41*C48)
  CM148_41 = s.In[1,48]*(OpM144_41*C48-OpM347_41*S48)
  CM248_41 = s.In[5,48]*(OpM244_41*C47+OpM343_41*S47)
  CM348_41 = s.In[9,48]*(OpM144_41*S48+OpM347_41*C48)
  FB148_42 = s.m[48]*(AlM147_42*C48-AlM347_42*S48)
  FB248_42 = s.m[48]*OpM144_42*(s.dpt[2,48]*S47-s.dpt[3,48]*C47)
  FB348_42 = s.m[48]*(AlM147_42*S48+AlM347_42*C48)
  CM148_42 = s.In[1,48]*(OpM144_42*C48-OpM347_42*S48)
  CM248_42 = s.In[5,48]*(OpM244_42*C47+S43*S47)
  CM348_42 = s.In[9,48]*(OpM144_42*S48+OpM347_42*C48)
  FB148_43 = s.m[48]*(AlM147_43*C48-AlM347_43*S48)
  FB248_43 = s.m[48]*S44*(s.dpt[2,48]*S47-s.dpt[3,48]*C47)
  FB348_43 = s.m[48]*(AlM147_43*S48+AlM347_43*C48)
  CM148_43 = -s.In[1,48]*(OpM347_43*S48-S44*C48)
  CM248_43 = s.In[5,48]*C44*C47
  CM348_43 = s.In[9,48]*(OpM347_43*C48+S44*S48)
  CM148_44 = -s.In[1,48]*C47*S48
  CM248_44 = s.In[5,48]*S47
  CM348_44 = s.In[9,48]*C47*C48
  FF47_148 = FA148*C48+FA348*S48
  FF47_348 = -(FA148*S48-FA348*C48)
  CF47_148 = CF148*C48+CF348*S48
  CF47_348 = -(CF148*S48-CF348*C48)
  FM471_148 = FB148_1*C48+FB348_1*S48
  FM471_348 = -(FB148_1*S48-FB348_1*C48)
  FM472_148 = FB148_2*C48+FB348_2*S48
  FM472_348 = -(FB148_2*S48-FB348_2*C48)
  FM473_148 = FB148_3*C48+FB348_3*S48
  FM473_348 = -(FB148_3*S48-FB348_3*C48)
  FM474_148 = FB148_4*C48+FB348_4*S48
  FM474_348 = -(FB148_4*S48-FB348_4*C48)
  CM474_148 = CM148_4*C48+CM348_4*S48
  CM474_348 = -(CM148_4*S48-CM348_4*C48)
  FM475_148 = FB148_5*C48+FB348_5*S48
  FM475_348 = -(FB148_5*S48-FB348_5*C48)
  CM475_148 = CM148_5*C48+CM348_5*S48
  CM475_348 = -(CM148_5*S48-CM348_5*C48)
  FM476_148 = FB148_6*C48+FB348_6*S48
  FM476_348 = -(FB148_6*S48-FB348_6*C48)
  CM476_148 = CM148_6*C48+CM348_6*S48
  CM476_348 = -(CM148_6*S48-CM348_6*C48)
  FM4740_148 = FB148_40*C48+FB348_40*S48
  FM4740_348 = -(FB148_40*S48-FB348_40*C48)
  CM4740_148 = CM148_40*C48+CM348_40*S48
  CM4740_348 = -(CM148_40*S48-CM348_40*C48)
  FM4741_148 = FB148_41*C48+FB348_41*S48
  FM4741_348 = -(FB148_41*S48-FB348_41*C48)
  CM4741_148 = CM148_41*C48+CM348_41*S48
  CM4741_348 = -(CM148_41*S48-CM348_41*C48)
  FM4742_148 = FB148_42*C48+FB348_42*S48
  FM4742_348 = -(FB148_42*S48-FB348_42*C48)
  CM4742_148 = CM148_42*C48+CM348_42*S48
  CM4742_348 = -(CM148_42*S48-CM348_42*C48)
  FM4743_148 = FB148_43*C48+FB348_43*S48
  FM4743_348 = -(FB148_43*S48-FB348_43*C48)
  CM4743_148 = CM148_43*C48+CM348_43*S48
  CM4743_348 = -(CM148_43*S48-CM348_43*C48)
  CM4744_148 = CM148_44*C48+CM348_44*S48
  CM4747_148 = s.In[1,48]*C48*C48+s.In[9,48]*S48*S48

# = = Block_0_2_0_1_0_19 = = 
 
# Backward Dynamics 

  FA151 = -(s.frc[1,51]+s.m[51]*(s.l[2,51]*(OpF351-OM151*OM251)-C50*(AlF149+BeF249*s.dpt[2,52])-S50*(AlF249+BS549*\
   s.dpt[2,52])))
  FA251 = -(s.frc[2,51]-s.m[51]*(AlF250*C51+AlF350*S51-s.l[2,51]*(OM151*OM151+OM351*OM351)))
  FA351 = -(s.frc[3,51]+s.m[51]*(AlF250*S51-AlF350*C51-s.l[2,51]*(OpF150+OM251*OM351)))
  CF151 = -(s.trq[1,51]-s.In[1,51]*OpF150-s.In[9,51]*OM251*OM351-FA351*s.l[2,51])
  CF251 = -(s.trq[2,51]-OM151*OM351*(s.In[1,51]-s.In[9,51]))
  CF351 = -(s.trq[3,51]+s.In[1,51]*OM151*OM251-s.In[9,51]*OpF351+FA151*s.l[2,51])
  FB151_1 = s.m[51]*(AlM15_1*C50+AlM26_1*S50)
  FB251_1 = s.m[51]*(AlM250_1*C51+AlM36_1*S51)
  FB351_1 = -s.m[51]*(AlM250_1*S51-AlM36_1*C51)
  CM151_1 = FB351_1*s.l[2,51]
  CM351_1 = -FB151_1*s.l[2,51]
  FB151_2 = s.m[51]*(AlM15_2*C50+AlM26_2*S50)
  FB251_2 = s.m[51]*(AlM250_2*C51+AlM36_2*S51)
  FB351_2 = -s.m[51]*(AlM250_2*S51-AlM36_2*C51)
  CM151_2 = FB351_2*s.l[2,51]
  CM351_2 = -FB151_2*s.l[2,51]
  FB151_3 = s.m[51]*(AlM26_3*S50-C50*S5)
  FB251_3 = s.m[51]*(AlM250_3*C51+AlM36_3*S51)
  FB351_3 = -s.m[51]*(AlM250_3*S51-AlM36_3*C51)
  CM151_3 = FB351_3*s.l[2,51]
  CM351_3 = -FB151_3*s.l[2,51]
  FB151_4 = s.m[51]*(AlM249_4*S50-OpM351_4*s.l[2,51]+C50*(AlM149_4-OpM36_4*s.dpt[2,52]))
  FB251_4 = s.m[51]*(AlM250_4*C51+AlM350_4*S51)
  FB351_4 = -s.m[51]*(AlM250_4*S51-AlM350_4*C51-OpM150_4*s.l[2,51])
  CM151_4 = s.In[1,51]*OpM150_4+FB351_4*s.l[2,51]
  CM351_4 = s.In[9,51]*OpM351_4-FB151_4*s.l[2,51]
  FB151_5 = s.m[51]*(AlM249_5*S50-OpM351_5*s.l[2,51]+C50*(AlM149_5+s.dpt[2,52]*S6))
  FB251_5 = s.m[51]*(AlM250_5*C51+AlM349_5*S51)
  FB351_5 = -s.m[51]*(AlM250_5*S51-AlM349_5*C51-OpM150_5*s.l[2,51])
  CM151_5 = s.In[1,51]*OpM150_5+FB351_5*s.l[2,51]
  CM351_5 = s.In[9,51]*OpM351_5-FB151_5*s.l[2,51]
  FB151_6 = -s.m[51]*OpM351_6*s.l[2,51]
  FB251_6 = s.m[51]*AlM350_6*S51
  FB351_6 = s.m[51]*(AlM350_6*C51+s.l[2,51]*C50)
  CM151_6 = s.In[1,51]*C50+FB351_6*s.l[2,51]
  CM351_6 = s.In[9,51]*OpM351_6-FB151_6*s.l[2,51]
  CM151_49 = -s.m[51]*s.l[2,51]*C50*S51
  CM151_51 = s.In[1,51]+s.m[51]*s.l[2,51]*s.l[2,51]
  FF50_251 = FA251*C51-FA351*S51
  FF50_351 = FA251*S51+FA351*C51
  CF50_251 = CF251*C51-CF351*S51
  CF50_351 = CF251*S51+CF351*C51
  FM501_251 = FB251_1*C51-FB351_1*S51
  FM501_351 = FB251_1*S51+FB351_1*C51
  CM501_251 = -CM351_1*S51
  CM501_351 = CM351_1*C51
  FM502_251 = FB251_2*C51-FB351_2*S51
  FM502_351 = FB251_2*S51+FB351_2*C51
  CM502_251 = -CM351_2*S51
  CM502_351 = CM351_2*C51
  FM503_251 = FB251_3*C51-FB351_3*S51
  FM503_351 = FB251_3*S51+FB351_3*C51
  CM503_251 = -CM351_3*S51
  CM503_351 = CM351_3*C51
  FM504_251 = FB251_4*C51-FB351_4*S51
  FM504_351 = FB251_4*S51+FB351_4*C51
  CM504_251 = -CM351_4*S51
  CM504_351 = CM351_4*C51
  FM505_251 = FB251_5*C51-FB351_5*S51
  FM505_351 = FB251_5*S51+FB351_5*C51
  CM505_251 = -CM351_5*S51
  CM505_351 = CM351_5*C51
  FM506_351 = FB251_6*S51+FB351_6*C51
  CM506_351 = CM351_6*C51
  CM5049_351 = -s.m[51]*s.l[2,51]*S50*C51
  CM5050_351 = C51*C51*(s.In[9,51]+s.m[51]*s.l[2,51]*s.l[2,51])

# = = Block_0_2_0_1_0_20 = = 
 
# Backward Dynamics 

  FA153 = -(s.frc[1,53]+s.m[53]*(s.l[2,53]*(OpF353-OM153*OM253)-C52*(AlF149+BeF249*s.dpt[2,53])-S52*(AlF249+BS549*\
   s.dpt[2,53])))
  FA253 = -(s.frc[2,53]-s.m[53]*(AlF252*C53+AlF352*S53-s.l[2,53]*(OM153*OM153+OM353*OM353)))
  FA353 = -(s.frc[3,53]+s.m[53]*(AlF252*S53-AlF352*C53-s.l[2,53]*(OpF152+OM253*OM353)))
  CF153 = -(s.trq[1,53]-s.In[1,53]*OpF152-s.In[9,53]*OM253*OM353-FA353*s.l[2,53])
  CF253 = -(s.trq[2,53]-OM153*OM353*(s.In[1,53]-s.In[9,53]))
  CF353 = -(s.trq[3,53]+s.In[1,53]*OM153*OM253-s.In[9,53]*OpF353+FA153*s.l[2,53])
  FB153_1 = s.m[53]*(AlM15_1*C52+AlM26_1*S52)
  FB253_1 = s.m[53]*(AlM252_1*C53+AlM36_1*S53)
  FB353_1 = -s.m[53]*(AlM252_1*S53-AlM36_1*C53)
  CM153_1 = FB353_1*s.l[2,53]
  CM353_1 = -FB153_1*s.l[2,53]
  FB153_2 = s.m[53]*(AlM15_2*C52+AlM26_2*S52)
  FB253_2 = s.m[53]*(AlM252_2*C53+AlM36_2*S53)
  FB353_2 = -s.m[53]*(AlM252_2*S53-AlM36_2*C53)
  CM153_2 = FB353_2*s.l[2,53]
  CM353_2 = -FB153_2*s.l[2,53]
  FB153_3 = s.m[53]*(AlM26_3*S52-C52*S5)
  FB253_3 = s.m[53]*(AlM252_3*C53+AlM36_3*S53)
  FB353_3 = -s.m[53]*(AlM252_3*S53-AlM36_3*C53)
  CM153_3 = FB353_3*s.l[2,53]
  CM353_3 = -FB153_3*s.l[2,53]
  FB153_4 = s.m[53]*(AlM249_4*S52-OpM353_4*s.l[2,53]+C52*(AlM149_4-OpM36_4*s.dpt[2,53]))
  FB253_4 = s.m[53]*(AlM252_4*C53+AlM352_4*S53)
  FB353_4 = -s.m[53]*(AlM252_4*S53-AlM352_4*C53-OpM152_4*s.l[2,53])
  CM153_4 = s.In[1,53]*OpM152_4+FB353_4*s.l[2,53]
  CM353_4 = s.In[9,53]*OpM353_4-FB153_4*s.l[2,53]
  FB153_5 = s.m[53]*(AlM249_5*S52-OpM353_5*s.l[2,53]+C52*(AlM149_5+s.dpt[2,53]*S6))
  FB253_5 = s.m[53]*(AlM252_5*C53+AlM349_5*S53)
  FB353_5 = -s.m[53]*(AlM252_5*S53-AlM349_5*C53-OpM152_5*s.l[2,53])
  CM153_5 = s.In[1,53]*OpM152_5+FB353_5*s.l[2,53]
  CM353_5 = s.In[9,53]*OpM353_5-FB153_5*s.l[2,53]
  FB153_6 = -s.m[53]*OpM353_6*s.l[2,53]
  FB253_6 = s.m[53]*AlM352_6*S53
  FB353_6 = s.m[53]*(AlM352_6*C53+s.l[2,53]*C52)
  CM153_6 = s.In[1,53]*C52+FB353_6*s.l[2,53]
  CM353_6 = s.In[9,53]*OpM353_6-FB153_6*s.l[2,53]
  CM153_49 = -s.m[53]*s.l[2,53]*C52*S53
  CM153_53 = s.In[1,53]+s.m[53]*s.l[2,53]*s.l[2,53]
  FF52_253 = FA253*C53-FA353*S53
  FF52_353 = FA253*S53+FA353*C53
  CF52_253 = CF253*C53-CF353*S53
  CF52_353 = CF253*S53+CF353*C53
  FM521_253 = FB253_1*C53-FB353_1*S53
  FM521_353 = FB253_1*S53+FB353_1*C53
  CM521_253 = -CM353_1*S53
  CM521_353 = CM353_1*C53
  FM522_253 = FB253_2*C53-FB353_2*S53
  FM522_353 = FB253_2*S53+FB353_2*C53
  CM522_253 = -CM353_2*S53
  CM522_353 = CM353_2*C53
  FM523_253 = FB253_3*C53-FB353_3*S53
  FM523_353 = FB253_3*S53+FB353_3*C53
  CM523_253 = -CM353_3*S53
  CM523_353 = CM353_3*C53
  FM524_253 = FB253_4*C53-FB353_4*S53
  FM524_353 = FB253_4*S53+FB353_4*C53
  CM524_253 = -CM353_4*S53
  CM524_353 = CM353_4*C53
  FM525_253 = FB253_5*C53-FB353_5*S53
  FM525_353 = FB253_5*S53+FB353_5*C53
  CM525_253 = -CM353_5*S53
  CM525_353 = CM353_5*C53
  FM526_353 = FB253_6*S53+FB353_6*C53
  CM526_353 = CM353_6*C53
  CM5249_353 = -s.m[53]*s.l[2,53]*S52*C53
  CM5252_353 = C53*C53*(s.In[9,53]+s.m[53]*s.l[2,53]*s.l[2,53])

# = = Block_0_2_0_1_0_22 = = 
 
# Backward Dynamics 

  FA157 = -(s.frc[1,57]-s.m[57]*(s.l[3,57]*(OpF257+OM157*OM357)+C56*(AlF155+BS155*s.dpt[1,57]+BeF255*s.dpt[2,57])-S56*(\
   AlF355+BeF755*s.dpt[1,57]+BeF855*s.dpt[2,57])))
  FA257 = -(s.frc[2,57]-s.m[57]*(AlF256*C57+AlF356*S57-s.l[3,57]*(OpF156-OM257*OM357)))
  FA357 = -(s.frc[3,57]+s.m[57]*(AlF256*S57-AlF356*C57+s.l[3,57]*(OM157*OM157+OM257*OM257)))
  CF157 = -(s.trq[1,57]-s.In[1,57]*OpF156+s.In[5,57]*OM257*OM357+FA257*s.l[3,57])
  CF257 = -(s.trq[2,57]-s.In[1,57]*OM157*OM357-s.In[5,57]*OpF257-FA157*s.l[3,57])
  CF357 = -(s.trq[3,57]+OM157*OM257*(s.In[1,57]-s.In[5,57]))
  FB157_1 = s.m[57]*(AlM155_1*C56-AlM355_1*S56)
  FB257_1 = s.m[57]*(AlM26_1*C57+AlM356_1*S57)
  FB357_1 = -s.m[57]*(AlM26_1*S57-AlM356_1*C57)
  CM157_1 = -FB257_1*s.l[3,57]
  CM257_1 = FB157_1*s.l[3,57]
  FB157_2 = s.m[57]*(AlM155_2*C56-AlM355_2*S56)
  FB257_2 = s.m[57]*(AlM26_2*C57+AlM356_2*S57)
  FB357_2 = -s.m[57]*(AlM26_2*S57-AlM356_2*C57)
  CM157_2 = -FB257_2*s.l[3,57]
  CM257_2 = FB157_2*s.l[3,57]
  FB157_3 = s.m[57]*(AlM155_3*C56-AlM355_3*S56)
  FB257_3 = s.m[57]*(AlM26_3*C57+AlM356_3*S57)
  FB357_3 = -s.m[57]*(AlM26_3*S57-AlM356_3*C57)
  CM157_3 = -FB257_3*s.l[3,57]
  CM257_3 = FB157_3*s.l[3,57]
  FB157_4 = s.m[57]*(OpM257_4*s.l[3,57]+C56*(AlM155_4-OpM355_4*s.dpt[2,57])-S56*(AlM355_4+OpM155_4*s.dpt[2,57]-OpM26_4*\
   s.dpt[1,57]))
  FB257_4 = s.m[57]*(AlM256_4*C57+AlM356_4*S57-OpM156_4*s.l[3,57])
  FB357_4 = -s.m[57]*(AlM256_4*S57-AlM356_4*C57)
  CM157_4 = s.In[1,57]*OpM156_4-FB257_4*s.l[3,57]
  CM257_4 = s.In[5,57]*OpM257_4+FB157_4*s.l[3,57]
  FB157_5 = s.m[57]*(OpM257_5*s.l[3,57]+C56*(AlM155_5-OpM355_5*s.dpt[2,57])-S56*(AlM355_5+OpM155_5*s.dpt[2,57]-\
   s.dpt[1,57]*C6))
  FB257_5 = s.m[57]*(AlM256_5*C57+AlM356_5*S57-OpM156_5*s.l[3,57])
  FB357_5 = -s.m[57]*(AlM256_5*S57-AlM356_5*C57)
  CM157_5 = s.In[1,57]*OpM156_5-FB257_5*s.l[3,57]
  CM257_5 = s.In[5,57]*OpM257_5+FB157_5*s.l[3,57]
  FB157_6 = s.m[57]*(OpM257_6*s.l[3,57]-s.dpt[2,57]*S54p55p56)
  FB257_6 = s.m[57]*(AlM256_6*C57+AlM356_6*S57-s.l[3,57]*C54p55p56)
  FB357_6 = -s.m[57]*(AlM256_6*S57-AlM356_6*C57)
  CM157_6 = s.In[1,57]*C54p55p56-FB257_6*s.l[3,57]
  CM257_6 = s.In[5,57]*OpM257_6+FB157_6*s.l[3,57]
  FB157_54 = s.m[57]*(s.dpt[1,57]*S56+s.l[3,57]*C57)
  CM157_54 = -s.m[57]*AlM356_54*s.l[3,57]*S57
  FB157_55 = s.m[57]*(s.dpt[1,57]*S56+s.l[3,57]*C57)
  CM157_55 = -s.m[57]*AlM356_55*s.l[3,57]*S57
  CM157_57 = s.In[1,57]+s.m[57]*s.l[3,57]*s.l[3,57]
  FF56_257 = FA257*C57-FA357*S57
  FF56_357 = FA257*S57+FA357*C57
  CF56_257 = CF257*C57-CF357*S57
  CF56_357 = CF257*S57+CF357*C57
  FM561_257 = FB257_1*C57-FB357_1*S57
  FM561_357 = FB257_1*S57+FB357_1*C57
  CM561_257 = CM257_1*C57
  CM561_357 = CM257_1*S57
  FM562_257 = FB257_2*C57-FB357_2*S57
  FM562_357 = FB257_2*S57+FB357_2*C57
  CM562_257 = CM257_2*C57
  CM562_357 = CM257_2*S57
  FM563_257 = FB257_3*C57-FB357_3*S57
  FM563_357 = FB257_3*S57+FB357_3*C57
  CM563_257 = CM257_3*C57
  CM563_357 = CM257_3*S57
  FM564_257 = FB257_4*C57-FB357_4*S57
  FM564_357 = FB257_4*S57+FB357_4*C57
  CM564_257 = CM257_4*C57
  CM564_357 = CM257_4*S57
  FM565_257 = FB257_5*C57-FB357_5*S57
  FM565_357 = FB257_5*S57+FB357_5*C57
  CM565_257 = CM257_5*C57
  CM565_357 = CM257_5*S57
  FM566_257 = FB257_6*C57-FB357_6*S57
  FM566_357 = FB257_6*S57+FB357_6*C57
  CM566_257 = CM257_6*C57
  CM566_357 = CM257_6*S57
  CM5654_257 = C57*(s.In[5,57]*C57+FB157_54*s.l[3,57])
  CM5655_257 = C57*(s.In[5,57]*C57+FB157_55*s.l[3,57])
  CM5656_257 = C57*C57*(s.In[5,57]+s.m[57]*s.l[3,57]*s.l[3,57])
  FA155 = -(s.frc[1,55]-s.m[55]*(AlF155+BS155*s.l[1,55]+BeF255*s.l[2,55]))
  FA255 = -(s.frc[2,55]-s.m[55]*(AlF254+BS555*s.l[2,55]+BeF455*s.l[1,55]))
  FA355 = -(s.frc[3,55]-s.m[55]*(AlF355+BeF755*s.l[1,55]+BeF855*s.l[2,55]))
  FF155 = FA155+FA157*C56+FF56_357*S56
  FF355 = FA355-FA157*S56+FF56_357*C56
  CF155 = -(s.trq[1,55]+s.In[5,55]*OM255*OM355-CF157*C56-CF56_357*S56-FA355*s.l[2,55]+s.dpt[2,57]*(FA157*S56-FF56_357*\
   C56))
  CF255 = -(s.trq[2,55]-CF56_257-s.In[5,55]*OpF26+FA355*s.l[1,55]-s.dpt[1,57]*(FA157*S56-FF56_357*C56))
  CF355 = -(s.trq[3,55]-s.In[5,55]*OM155*OM255+CF157*S56-CF56_357*C56+FA155*s.l[2,55]-FA255*s.l[1,55]-FF56_257*\
   s.dpt[1,57]+s.dpt[2,57]*(FA157*C56+FF56_357*S56))
  FB155_1 = s.m[55]*AlM155_1
  FB255_1 = s.m[55]*AlM26_1
  FB355_1 = s.m[55]*AlM355_1
  FM155_1 = FB155_1+FB157_1*C56+FM561_357*S56
  FM355_1 = FB355_1-FB157_1*S56+FM561_357*C56
  CM155_1 = CM157_1*C56+CM561_357*S56+FB355_1*s.l[2,55]-s.dpt[2,57]*(FB157_1*S56-FM561_357*C56)
  CM255_1 = CM561_257-FB355_1*s.l[1,55]+s.dpt[1,57]*(FB157_1*S56-FM561_357*C56)
  CM355_1 = -(CM157_1*S56-CM561_357*C56+FB155_1*s.l[2,55]-FB255_1*s.l[1,55]-FM561_257*s.dpt[1,57]+s.dpt[2,57]*(FB157_1*\
   C56+FM561_357*S56))
  FB155_2 = s.m[55]*AlM155_2
  FB255_2 = s.m[55]*AlM26_2
  FB355_2 = s.m[55]*AlM355_2
  FM155_2 = FB155_2+FB157_2*C56+FM562_357*S56
  FM355_2 = FB355_2-FB157_2*S56+FM562_357*C56
  CM155_2 = CM157_2*C56+CM562_357*S56+FB355_2*s.l[2,55]-s.dpt[2,57]*(FB157_2*S56-FM562_357*C56)
  CM255_2 = CM562_257-FB355_2*s.l[1,55]+s.dpt[1,57]*(FB157_2*S56-FM562_357*C56)
  CM355_2 = -(CM157_2*S56-CM562_357*C56+FB155_2*s.l[2,55]-FB255_2*s.l[1,55]-FM562_257*s.dpt[1,57]+s.dpt[2,57]*(FB157_2*\
   C56+FM562_357*S56))
  FB155_3 = s.m[55]*AlM155_3
  FB255_3 = s.m[55]*AlM26_3
  FB355_3 = s.m[55]*AlM355_3
  FM155_3 = FB155_3+FB157_3*C56+FM563_357*S56
  FM355_3 = FB355_3-FB157_3*S56+FM563_357*C56
  CM155_3 = CM157_3*C56+CM563_357*S56+FB355_3*s.l[2,55]-s.dpt[2,57]*(FB157_3*S56-FM563_357*C56)
  CM255_3 = CM563_257-FB355_3*s.l[1,55]+s.dpt[1,57]*(FB157_3*S56-FM563_357*C56)
  CM355_3 = -(CM157_3*S56-CM563_357*C56+FB155_3*s.l[2,55]-FB255_3*s.l[1,55]-FM563_257*s.dpt[1,57]+s.dpt[2,57]*(FB157_3*\
   C56+FM563_357*S56))
  FB155_4 = s.m[55]*(AlM155_4-OpM355_4*s.l[2,55])
  FB255_4 = s.m[55]*(AlM254_4+OpM355_4*s.l[1,55])
  FB355_4 = s.m[55]*(AlM355_4+OpM155_4*s.l[2,55]-OpM26_4*s.l[1,55])
  FM155_4 = FB155_4+FB157_4*C56+FM564_357*S56
  FM355_4 = FB355_4-FB157_4*S56+FM564_357*C56
  CM155_4 = CM157_4*C56+CM564_357*S56+FB355_4*s.l[2,55]-s.dpt[2,57]*(FB157_4*S56-FM564_357*C56)
  CM255_4 = CM564_257+s.In[5,55]*OpM26_4-FB355_4*s.l[1,55]+s.dpt[1,57]*(FB157_4*S56-FM564_357*C56)
  CM355_4 = -(CM157_4*S56-CM564_357*C56+FB155_4*s.l[2,55]-FB255_4*s.l[1,55]-FM564_257*s.dpt[1,57]+s.dpt[2,57]*(FB157_4*\
   C56+FM564_357*S56))
  FB155_5 = s.m[55]*(AlM155_5-OpM355_5*s.l[2,55])
  FB255_5 = s.m[55]*(AlM254_5+OpM355_5*s.l[1,55])
  FB355_5 = s.m[55]*(AlM355_5+OpM155_5*s.l[2,55]-s.l[1,55]*C6)
  FM155_5 = FB155_5+FB157_5*C56+FM565_357*S56
  FM355_5 = FB355_5-FB157_5*S56+FM565_357*C56
  CM155_5 = CM157_5*C56+CM565_357*S56+FB355_5*s.l[2,55]-s.dpt[2,57]*(FB157_5*S56-FM565_357*C56)
  CM255_5 = CM565_257+s.In[5,55]*C6-FB355_5*s.l[1,55]+s.dpt[1,57]*(FB157_5*S56-FM565_357*C56)
  CM355_5 = -(CM157_5*S56-CM565_357*C56+FB155_5*s.l[2,55]-FB255_5*s.l[1,55]-FM565_257*s.dpt[1,57]+s.dpt[2,57]*(FB157_5*\
   C56+FM565_357*S56))
  FB255_6 = -s.m[55]*(s.dpt[3,14]-s.l[1,55]*S54p55)
  FB355_6 = s.m[55]*s.l[2,55]*C54p55
  CM155_6 = CM157_6*C56+CM566_357*S56+FB355_6*s.l[2,55]-s.dpt[2,57]*(FB157_6*S56-FM566_357*C56)
  CM255_6 = CM566_257-FB355_6*s.l[1,55]+s.dpt[1,57]*(FB157_6*S56-FM566_357*C56)
  CM355_6 = s.m[55]*s.l[2,55]*s.l[2,55]*S54p55-CM157_6*S56+CM566_357*C56+FB255_6*s.l[1,55]+FM566_257*s.dpt[1,57]-\
   s.dpt[2,57]*(FB157_6*C56+FM566_357*S56)
  CM255_54 = s.In[5,55]+CM5654_257+s.m[55]*s.l[1,55]*s.l[1,55]-s.dpt[1,57]*(s.m[57]*AlM356_54*C56-FB157_54*S56)
  CM255_55 = s.In[5,55]+CM5655_257+s.m[55]*s.l[1,55]*s.l[1,55]-s.dpt[1,57]*(s.m[57]*AlM356_55*C56-FB157_55*S56)

# = = Block_0_2_0_1_0_23 = = 
 
# Backward Dynamics 

  FA159 = -(s.frc[1,59]-s.m[59]*(s.l[3,59]*(OpF259+OM159*OM359)+C58*(AlF154+BS154*s.dpt[1,56]+BeF254*s.dpt[2,56])-S58*(\
   AlF354+BeF754*s.dpt[1,56]+BeF854*s.dpt[2,56])))
  FA259 = -(s.frc[2,59]-s.m[59]*(AlF258*C59+AlF358*S59-s.l[3,59]*(OpF158-OM259*OM359)))
  FA359 = -(s.frc[3,59]+s.m[59]*(AlF258*S59-AlF358*C59+s.l[3,59]*(OM159*OM159+OM259*OM259)))
  CF159 = -(s.trq[1,59]-s.In[1,59]*OpF158+s.In[5,59]*OM259*OM359+FA259*s.l[3,59])
  CF259 = -(s.trq[2,59]-s.In[1,59]*OM159*OM359-s.In[5,59]*OpF259-FA159*s.l[3,59])
  CF359 = -(s.trq[3,59]+OM159*OM259*(s.In[1,59]-s.In[5,59]))
  FB159_1 = s.m[59]*(AlM154_1*C58-AlM354_1*S58)
  FB259_1 = s.m[59]*(AlM26_1*C59+AlM358_1*S59)
  FB359_1 = -s.m[59]*(AlM26_1*S59-AlM358_1*C59)
  CM159_1 = -FB259_1*s.l[3,59]
  CM259_1 = FB159_1*s.l[3,59]
  FB159_2 = s.m[59]*(AlM154_2*C58-AlM354_2*S58)
  FB259_2 = s.m[59]*(AlM26_2*C59+AlM358_2*S59)
  FB359_2 = -s.m[59]*(AlM26_2*S59-AlM358_2*C59)
  CM159_2 = -FB259_2*s.l[3,59]
  CM259_2 = FB159_2*s.l[3,59]
  FB159_3 = s.m[59]*(AlM154_3*C58-AlM354_3*S58)
  FB259_3 = s.m[59]*(AlM26_3*C59+AlM358_3*S59)
  FB359_3 = -s.m[59]*(AlM26_3*S59-AlM358_3*C59)
  CM159_3 = -FB259_3*s.l[3,59]
  CM259_3 = FB159_3*s.l[3,59]
  FB159_4 = s.m[59]*(OpM259_4*s.l[3,59]+C58*(AlM154_4-OpM354_4*s.dpt[2,56])-S58*(AlM354_4+OpM154_4*s.dpt[2,56]-OpM26_4*\
   s.dpt[1,56]))
  FB259_4 = s.m[59]*(AlM258_4*C59+AlM358_4*S59-OpM158_4*s.l[3,59])
  FB359_4 = -s.m[59]*(AlM258_4*S59-AlM358_4*C59)
  CM159_4 = s.In[1,59]*OpM158_4-FB259_4*s.l[3,59]
  CM259_4 = s.In[5,59]*OpM259_4+FB159_4*s.l[3,59]
  FB159_5 = s.m[59]*(OpM259_5*s.l[3,59]+C58*(AlM154_5-OpM354_5*s.dpt[2,56])-S58*(AlM354_5+OpM154_5*s.dpt[2,56]-\
   s.dpt[1,56]*C6))
  FB259_5 = s.m[59]*(AlM258_5*C59+AlM358_5*S59-OpM158_5*s.l[3,59])
  FB359_5 = -s.m[59]*(AlM258_5*S59-AlM358_5*C59)
  CM159_5 = s.In[1,59]*OpM158_5-FB259_5*s.l[3,59]
  CM259_5 = s.In[5,59]*OpM259_5+FB159_5*s.l[3,59]
  FB159_6 = s.m[59]*(OpM259_6*s.l[3,59]-s.dpt[2,56]*S54p58)
  FB259_6 = s.m[59]*(AlM258_6*C59+AlM358_6*S59-s.l[3,59]*C54p58)
  FB359_6 = -s.m[59]*(AlM258_6*S59-AlM358_6*C59)
  CM159_6 = s.In[1,59]*C54p58-FB259_6*s.l[3,59]
  CM259_6 = s.In[5,59]*OpM259_6+FB159_6*s.l[3,59]
  FB159_54 = s.m[59]*(s.dpt[1,56]*S58+s.l[3,59]*C59)
  CM159_54 = -s.m[59]*AlM358_54*s.l[3,59]*S59
  CM159_59 = s.In[1,59]+s.m[59]*s.l[3,59]*s.l[3,59]
  FF58_259 = FA259*C59-FA359*S59
  FF58_359 = FA259*S59+FA359*C59
  CF58_259 = CF259*C59-CF359*S59
  CF58_359 = CF259*S59+CF359*C59
  FM581_259 = FB259_1*C59-FB359_1*S59
  FM581_359 = FB259_1*S59+FB359_1*C59
  CM581_259 = CM259_1*C59
  CM581_359 = CM259_1*S59
  FM582_259 = FB259_2*C59-FB359_2*S59
  FM582_359 = FB259_2*S59+FB359_2*C59
  CM582_259 = CM259_2*C59
  CM582_359 = CM259_2*S59
  FM583_259 = FB259_3*C59-FB359_3*S59
  FM583_359 = FB259_3*S59+FB359_3*C59
  CM583_259 = CM259_3*C59
  CM583_359 = CM259_3*S59
  FM584_259 = FB259_4*C59-FB359_4*S59
  FM584_359 = FB259_4*S59+FB359_4*C59
  CM584_259 = CM259_4*C59
  CM584_359 = CM259_4*S59
  FM585_259 = FB259_5*C59-FB359_5*S59
  FM585_359 = FB259_5*S59+FB359_5*C59
  CM585_259 = CM259_5*C59
  CM585_359 = CM259_5*S59
  FM586_259 = FB259_6*C59-FB359_6*S59
  FM586_359 = FB259_6*S59+FB359_6*C59
  CM586_259 = CM259_6*C59
  CM586_359 = CM259_6*S59
  CM5854_259 = C59*(s.In[5,59]*C59+FB159_54*s.l[3,59])
  CM5858_259 = C59*C59*(s.In[5,59]+s.m[59]*s.l[3,59]*s.l[3,59])

# = = Block_0_2_0_1_0_25 = = 
 
# Backward Dynamics 

  FA163 = -(s.frc[1,63]-s.m[63]*(s.l[3,63]*(OpF263+OM163*OM363)+C62*(AlF161+BS161*s.dpt[1,61]+BeF261*s.dpt[2,61])-S62*(\
   AlF361+BeF761*s.dpt[1,61]+BeF861*s.dpt[2,61])))
  FA263 = -(s.frc[2,63]-s.m[63]*(AlF262*C63+AlF362*S63-s.l[3,63]*(OpF162-OM263*OM363)))
  FA363 = -(s.frc[3,63]+s.m[63]*(AlF262*S63-AlF362*C63+s.l[3,63]*(OM163*OM163+OM263*OM263)))
  CF163 = -(s.trq[1,63]-s.In[1,63]*OpF162+s.In[5,63]*OM263*OM363+FA263*s.l[3,63])
  CF263 = -(s.trq[2,63]-s.In[1,63]*OM163*OM363-s.In[5,63]*OpF263-FA163*s.l[3,63])
  CF363 = -(s.trq[3,63]+OM163*OM263*(s.In[1,63]-s.In[5,63]))
  FB163_1 = s.m[63]*(AlM161_1*C62-AlM361_1*S62)
  FB263_1 = s.m[63]*(AlM26_1*C63+AlM362_1*S63)
  FB363_1 = -s.m[63]*(AlM26_1*S63-AlM362_1*C63)
  CM163_1 = -FB263_1*s.l[3,63]
  CM263_1 = FB163_1*s.l[3,63]
  FB163_2 = s.m[63]*(AlM161_2*C62-AlM361_2*S62)
  FB263_2 = s.m[63]*(AlM26_2*C63+AlM362_2*S63)
  FB363_2 = -s.m[63]*(AlM26_2*S63-AlM362_2*C63)
  CM163_2 = -FB263_2*s.l[3,63]
  CM263_2 = FB163_2*s.l[3,63]
  FB163_3 = s.m[63]*(AlM161_3*C62-AlM361_3*S62)
  FB263_3 = s.m[63]*(AlM26_3*C63+AlM362_3*S63)
  FB363_3 = -s.m[63]*(AlM26_3*S63-AlM362_3*C63)
  CM163_3 = -FB263_3*s.l[3,63]
  CM263_3 = FB163_3*s.l[3,63]
  FB163_4 = s.m[63]*(OpM263_4*s.l[3,63]+C62*(AlM161_4-OpM361_4*s.dpt[2,61])-S62*(AlM361_4+OpM161_4*s.dpt[2,61]-OpM26_4*\
   s.dpt[1,61]))
  FB263_4 = s.m[63]*(AlM262_4*C63+AlM362_4*S63-OpM162_4*s.l[3,63])
  FB363_4 = -s.m[63]*(AlM262_4*S63-AlM362_4*C63)
  CM163_4 = s.In[1,63]*OpM162_4-FB263_4*s.l[3,63]
  CM263_4 = s.In[5,63]*OpM263_4+FB163_4*s.l[3,63]
  FB163_5 = s.m[63]*(OpM263_5*s.l[3,63]+C62*(AlM161_5-OpM361_5*s.dpt[2,61])-S62*(AlM361_5+OpM161_5*s.dpt[2,61]-\
   s.dpt[1,61]*C6))
  FB263_5 = s.m[63]*(AlM262_5*C63+AlM362_5*S63-OpM162_5*s.l[3,63])
  FB363_5 = -s.m[63]*(AlM262_5*S63-AlM362_5*C63)
  CM163_5 = s.In[1,63]*OpM162_5-FB263_5*s.l[3,63]
  CM263_5 = s.In[5,63]*OpM263_5+FB163_5*s.l[3,63]
  FB163_6 = s.m[63]*(OpM263_6*s.l[3,63]-s.dpt[2,61]*S60p61p62)
  FB263_6 = s.m[63]*(AlM262_6*C63+AlM362_6*S63-s.l[3,63]*C60p61p62)
  FB363_6 = -s.m[63]*(AlM262_6*S63-AlM362_6*C63)
  CM163_6 = s.In[1,63]*C60p61p62-FB263_6*s.l[3,63]
  CM263_6 = s.In[5,63]*OpM263_6+FB163_6*s.l[3,63]
  FB163_60 = s.m[63]*(s.dpt[1,61]*S62+s.l[3,63]*C63)
  CM163_60 = -s.m[63]*AlM362_60*s.l[3,63]*S63
  FB163_61 = s.m[63]*(s.dpt[1,61]*S62+s.l[3,63]*C63)
  CM163_61 = -s.m[63]*AlM362_61*s.l[3,63]*S63
  CM163_63 = s.In[1,63]+s.m[63]*s.l[3,63]*s.l[3,63]
  FF62_263 = FA263*C63-FA363*S63
  FF62_363 = FA263*S63+FA363*C63
  CF62_263 = CF263*C63-CF363*S63
  CF62_363 = CF263*S63+CF363*C63
  FM621_263 = FB263_1*C63-FB363_1*S63
  FM621_363 = FB263_1*S63+FB363_1*C63
  CM621_263 = CM263_1*C63
  CM621_363 = CM263_1*S63
  FM622_263 = FB263_2*C63-FB363_2*S63
  FM622_363 = FB263_2*S63+FB363_2*C63
  CM622_263 = CM263_2*C63
  CM622_363 = CM263_2*S63
  FM623_263 = FB263_3*C63-FB363_3*S63
  FM623_363 = FB263_3*S63+FB363_3*C63
  CM623_263 = CM263_3*C63
  CM623_363 = CM263_3*S63
  FM624_263 = FB263_4*C63-FB363_4*S63
  FM624_363 = FB263_4*S63+FB363_4*C63
  CM624_263 = CM263_4*C63
  CM624_363 = CM263_4*S63
  FM625_263 = FB263_5*C63-FB363_5*S63
  FM625_363 = FB263_5*S63+FB363_5*C63
  CM625_263 = CM263_5*C63
  CM625_363 = CM263_5*S63
  FM626_263 = FB263_6*C63-FB363_6*S63
  FM626_363 = FB263_6*S63+FB363_6*C63
  CM626_263 = CM263_6*C63
  CM626_363 = CM263_6*S63
  CM6260_263 = C63*(s.In[5,63]*C63+FB163_60*s.l[3,63])
  CM6261_263 = C63*(s.In[5,63]*C63+FB163_61*s.l[3,63])
  CM6262_263 = C63*C63*(s.In[5,63]+s.m[63]*s.l[3,63]*s.l[3,63])
  FA161 = -(s.frc[1,61]-s.m[61]*(AlF161+BS161*s.l[1,61]+BeF261*s.l[2,61]))
  FA261 = -(s.frc[2,61]-s.m[61]*(AlF260+BS561*s.l[2,61]+BeF461*s.l[1,61]))
  FA361 = -(s.frc[3,61]-s.m[61]*(AlF361+BeF761*s.l[1,61]+BeF861*s.l[2,61]))
  FF161 = FA161+FA163*C62+FF62_363*S62
  FF361 = FA361-FA163*S62+FF62_363*C62
  CF161 = -(s.trq[1,61]+s.In[5,61]*OM261*OM361-CF163*C62-CF62_363*S62-FA361*s.l[2,61]+s.dpt[2,61]*(FA163*S62-FF62_363*\
   C62))
  CF261 = -(s.trq[2,61]-CF62_263-s.In[5,61]*OpF26+FA361*s.l[1,61]-s.dpt[1,61]*(FA163*S62-FF62_363*C62))
  CF361 = -(s.trq[3,61]-s.In[5,61]*OM161*OM261+CF163*S62-CF62_363*C62+FA161*s.l[2,61]-FA261*s.l[1,61]-FF62_263*\
   s.dpt[1,61]+s.dpt[2,61]*(FA163*C62+FF62_363*S62))
  FB161_1 = s.m[61]*AlM161_1
  FB261_1 = s.m[61]*AlM26_1
  FB361_1 = s.m[61]*AlM361_1
  FM161_1 = FB161_1+FB163_1*C62+FM621_363*S62
  FM361_1 = FB361_1-FB163_1*S62+FM621_363*C62
  CM161_1 = CM163_1*C62+CM621_363*S62+FB361_1*s.l[2,61]-s.dpt[2,61]*(FB163_1*S62-FM621_363*C62)
  CM261_1 = CM621_263-FB361_1*s.l[1,61]+s.dpt[1,61]*(FB163_1*S62-FM621_363*C62)
  CM361_1 = -(CM163_1*S62-CM621_363*C62+FB161_1*s.l[2,61]-FB261_1*s.l[1,61]-FM621_263*s.dpt[1,61]+s.dpt[2,61]*(FB163_1*\
   C62+FM621_363*S62))
  FB161_2 = s.m[61]*AlM161_2
  FB261_2 = s.m[61]*AlM26_2
  FB361_2 = s.m[61]*AlM361_2
  FM161_2 = FB161_2+FB163_2*C62+FM622_363*S62
  FM361_2 = FB361_2-FB163_2*S62+FM622_363*C62
  CM161_2 = CM163_2*C62+CM622_363*S62+FB361_2*s.l[2,61]-s.dpt[2,61]*(FB163_2*S62-FM622_363*C62)
  CM261_2 = CM622_263-FB361_2*s.l[1,61]+s.dpt[1,61]*(FB163_2*S62-FM622_363*C62)
  CM361_2 = -(CM163_2*S62-CM622_363*C62+FB161_2*s.l[2,61]-FB261_2*s.l[1,61]-FM622_263*s.dpt[1,61]+s.dpt[2,61]*(FB163_2*\
   C62+FM622_363*S62))
  FB161_3 = s.m[61]*AlM161_3
  FB261_3 = s.m[61]*AlM26_3
  FB361_3 = s.m[61]*AlM361_3
  FM161_3 = FB161_3+FB163_3*C62+FM623_363*S62
  FM361_3 = FB361_3-FB163_3*S62+FM623_363*C62
  CM161_3 = CM163_3*C62+CM623_363*S62+FB361_3*s.l[2,61]-s.dpt[2,61]*(FB163_3*S62-FM623_363*C62)
  CM261_3 = CM623_263-FB361_3*s.l[1,61]+s.dpt[1,61]*(FB163_3*S62-FM623_363*C62)
  CM361_3 = -(CM163_3*S62-CM623_363*C62+FB161_3*s.l[2,61]-FB261_3*s.l[1,61]-FM623_263*s.dpt[1,61]+s.dpt[2,61]*(FB163_3*\
   C62+FM623_363*S62))
  FB161_4 = s.m[61]*(AlM161_4-OpM361_4*s.l[2,61])
  FB261_4 = s.m[61]*(AlM260_4+OpM361_4*s.l[1,61])
  FB361_4 = s.m[61]*(AlM361_4+OpM161_4*s.l[2,61]-OpM26_4*s.l[1,61])
  FM161_4 = FB161_4+FB163_4*C62+FM624_363*S62
  FM361_4 = FB361_4-FB163_4*S62+FM624_363*C62
  CM161_4 = CM163_4*C62+CM624_363*S62+FB361_4*s.l[2,61]-s.dpt[2,61]*(FB163_4*S62-FM624_363*C62)
  CM261_4 = CM624_263+s.In[5,61]*OpM26_4-FB361_4*s.l[1,61]+s.dpt[1,61]*(FB163_4*S62-FM624_363*C62)
  CM361_4 = -(CM163_4*S62-CM624_363*C62+FB161_4*s.l[2,61]-FB261_4*s.l[1,61]-FM624_263*s.dpt[1,61]+s.dpt[2,61]*(FB163_4*\
   C62+FM624_363*S62))
  FB161_5 = s.m[61]*(AlM161_5-OpM361_5*s.l[2,61])
  FB261_5 = s.m[61]*(AlM260_5+OpM361_5*s.l[1,61])
  FB361_5 = s.m[61]*(AlM361_5+OpM161_5*s.l[2,61]-s.l[1,61]*C6)
  FM161_5 = FB161_5+FB163_5*C62+FM625_363*S62
  FM361_5 = FB361_5-FB163_5*S62+FM625_363*C62
  CM161_5 = CM163_5*C62+CM625_363*S62+FB361_5*s.l[2,61]-s.dpt[2,61]*(FB163_5*S62-FM625_363*C62)
  CM261_5 = CM625_263+s.In[5,61]*C6-FB361_5*s.l[1,61]+s.dpt[1,61]*(FB163_5*S62-FM625_363*C62)
  CM361_5 = -(CM163_5*S62-CM625_363*C62+FB161_5*s.l[2,61]-FB261_5*s.l[1,61]-FM625_263*s.dpt[1,61]+s.dpt[2,61]*(FB163_5*\
   C62+FM625_363*S62))
  FB261_6 = -s.m[61]*(s.dpt[3,15]-s.l[1,61]*S60p61)
  FB361_6 = s.m[61]*s.l[2,61]*C60p61
  CM161_6 = CM163_6*C62+CM626_363*S62+FB361_6*s.l[2,61]-s.dpt[2,61]*(FB163_6*S62-FM626_363*C62)
  CM261_6 = CM626_263-FB361_6*s.l[1,61]+s.dpt[1,61]*(FB163_6*S62-FM626_363*C62)
  CM361_6 = s.m[61]*s.l[2,61]*s.l[2,61]*S60p61-CM163_6*S62+CM626_363*C62+FB261_6*s.l[1,61]+FM626_263*s.dpt[1,61]-\
   s.dpt[2,61]*(FB163_6*C62+FM626_363*S62)
  CM261_60 = s.In[5,61]+CM6260_263+s.m[61]*s.l[1,61]*s.l[1,61]-s.dpt[1,61]*(s.m[63]*AlM362_60*C62-FB163_60*S62)
  CM261_61 = s.In[5,61]+CM6261_263+s.m[61]*s.l[1,61]*s.l[1,61]-s.dpt[1,61]*(s.m[63]*AlM362_61*C62-FB163_61*S62)

# = = Block_0_2_0_1_0_26 = = 
 
# Backward Dynamics 

  FA165 = -(s.frc[1,65]-s.m[65]*(s.l[3,65]*(OpF265+OM165*OM365)+C64*(AlF160+BS160*s.dpt[1,60]+BeF260*s.dpt[2,60])-S64*(\
   AlF360+BeF760*s.dpt[1,60]+BeF860*s.dpt[2,60])))
  FA265 = -(s.frc[2,65]-s.m[65]*(AlF264*C65+AlF364*S65-s.l[3,65]*(OpF164-OM265*OM365)))
  FA365 = -(s.frc[3,65]+s.m[65]*(AlF264*S65-AlF364*C65+s.l[3,65]*(OM165*OM165+OM265*OM265)))
  CF165 = -(s.trq[1,65]-s.In[1,65]*OpF164+s.In[5,65]*OM265*OM365+FA265*s.l[3,65])
  CF265 = -(s.trq[2,65]-s.In[1,65]*OM165*OM365-s.In[5,65]*OpF265-FA165*s.l[3,65])
  CF365 = -(s.trq[3,65]+OM165*OM265*(s.In[1,65]-s.In[5,65]))
  FB165_1 = s.m[65]*(AlM160_1*C64-AlM360_1*S64)
  FB265_1 = s.m[65]*(AlM26_1*C65+AlM364_1*S65)
  FB365_1 = -s.m[65]*(AlM26_1*S65-AlM364_1*C65)
  CM165_1 = -FB265_1*s.l[3,65]
  CM265_1 = FB165_1*s.l[3,65]
  FB165_2 = s.m[65]*(AlM160_2*C64-AlM360_2*S64)
  FB265_2 = s.m[65]*(AlM26_2*C65+AlM364_2*S65)
  FB365_2 = -s.m[65]*(AlM26_2*S65-AlM364_2*C65)
  CM165_2 = -FB265_2*s.l[3,65]
  CM265_2 = FB165_2*s.l[3,65]
  FB165_3 = s.m[65]*(AlM160_3*C64-AlM360_3*S64)
  FB265_3 = s.m[65]*(AlM26_3*C65+AlM364_3*S65)
  FB365_3 = -s.m[65]*(AlM26_3*S65-AlM364_3*C65)
  CM165_3 = -FB265_3*s.l[3,65]
  CM265_3 = FB165_3*s.l[3,65]
  FB165_4 = s.m[65]*(OpM265_4*s.l[3,65]+C64*(AlM160_4-OpM360_4*s.dpt[2,60])-S64*(AlM360_4+OpM160_4*s.dpt[2,60]-OpM26_4*\
   s.dpt[1,60]))
  FB265_4 = s.m[65]*(AlM264_4*C65+AlM364_4*S65-OpM164_4*s.l[3,65])
  FB365_4 = -s.m[65]*(AlM264_4*S65-AlM364_4*C65)
  CM165_4 = s.In[1,65]*OpM164_4-FB265_4*s.l[3,65]
  CM265_4 = s.In[5,65]*OpM265_4+FB165_4*s.l[3,65]
  FB165_5 = s.m[65]*(OpM265_5*s.l[3,65]+C64*(AlM160_5-OpM360_5*s.dpt[2,60])-S64*(AlM360_5+OpM160_5*s.dpt[2,60]-\
   s.dpt[1,60]*C6))
  FB265_5 = s.m[65]*(AlM264_5*C65+AlM364_5*S65-OpM164_5*s.l[3,65])
  FB365_5 = -s.m[65]*(AlM264_5*S65-AlM364_5*C65)
  CM165_5 = s.In[1,65]*OpM164_5-FB265_5*s.l[3,65]
  CM265_5 = s.In[5,65]*OpM265_5+FB165_5*s.l[3,65]
  FB165_6 = s.m[65]*(OpM265_6*s.l[3,65]-s.dpt[2,60]*S60p64)
  FB265_6 = s.m[65]*(AlM264_6*C65+AlM364_6*S65-s.l[3,65]*C60p64)
  FB365_6 = -s.m[65]*(AlM264_6*S65-AlM364_6*C65)
  CM165_6 = s.In[1,65]*C60p64-FB265_6*s.l[3,65]
  CM265_6 = s.In[5,65]*OpM265_6+FB165_6*s.l[3,65]
  FB165_60 = s.m[65]*(s.dpt[1,60]*S64+s.l[3,65]*C65)
  CM165_60 = -s.m[65]*AlM364_60*s.l[3,65]*S65
  CM165_65 = s.In[1,65]+s.m[65]*s.l[3,65]*s.l[3,65]
  FF64_265 = FA265*C65-FA365*S65
  FF64_365 = FA265*S65+FA365*C65
  CF64_265 = CF265*C65-CF365*S65
  CF64_365 = CF265*S65+CF365*C65
  FM641_265 = FB265_1*C65-FB365_1*S65
  FM641_365 = FB265_1*S65+FB365_1*C65
  CM641_265 = CM265_1*C65
  CM641_365 = CM265_1*S65
  FM642_265 = FB265_2*C65-FB365_2*S65
  FM642_365 = FB265_2*S65+FB365_2*C65
  CM642_265 = CM265_2*C65
  CM642_365 = CM265_2*S65
  FM643_265 = FB265_3*C65-FB365_3*S65
  FM643_365 = FB265_3*S65+FB365_3*C65
  CM643_265 = CM265_3*C65
  CM643_365 = CM265_3*S65
  FM644_265 = FB265_4*C65-FB365_4*S65
  FM644_365 = FB265_4*S65+FB365_4*C65
  CM644_265 = CM265_4*C65
  CM644_365 = CM265_4*S65
  FM645_265 = FB265_5*C65-FB365_5*S65
  FM645_365 = FB265_5*S65+FB365_5*C65
  CM645_265 = CM265_5*C65
  CM645_365 = CM265_5*S65
  FM646_265 = FB265_6*C65-FB365_6*S65
  FM646_365 = FB265_6*S65+FB365_6*C65
  CM646_265 = CM265_6*C65
  CM646_365 = CM265_6*S65
  CM6460_265 = C65*(s.In[5,65]*C65+FB165_60*s.l[3,65])
  CM6464_265 = C65*C65*(s.In[5,65]+s.m[65]*s.l[3,65]*s.l[3,65])

# = = Block_0_2_0_2_0_2 = = 
 
# Backward Dynamics 

  FA110 = -(s.frc[1,10]-s.m[10]*(AlF110+BeF310*s.l[3,10]))
  FA210 = -(s.frc[2,10]-s.m[10]*(AlF29+BeF610*s.l[3,10]))
  FF110 = FA110+FA112+FF13_114
  FF210 = FA210+FA212*C11+FA214*C13-FA312*S11-FF13_314*S13
  FF310 = -(s.frc[3,10]-s.m[10]*(AlF310+BS910*s.l[3,10])-FA212*S11-FA214*S13-FA312*C11-FF13_314*C13)
  CF110 = -(s.trq[1,10]-CF11_112-CF13_114-s.In[1,10]*OpF110+FA210*s.l[3,10]+OM210*OM310*(s.In[5,10]-s.In[9,10])-\
   s.dpt[2,19]*(FA212*S11+FA312*C11)-s.dpt[2,20]*(FA214*S13+FF13_314*C13)+s.dpt[3,19]*(FA212*C11-FA312*S11)+s.dpt[3,20]*(FA214*\
   C13-FF13_314*S13))
  CF210 = -(s.trq[2,10]-s.In[5,10]*OpF29-CF11_212*C11+CF13_314*S13-CF214*C13+CF312*S11-FA110*s.l[3,10]-FA112*s.dpt[3,19]\
   -FF13_114*s.dpt[3,20]-OM110*OM310*(s.In[1,10]-s.In[9,10]))
  CF310 = -(s.trq[3,10]-s.In[9,10]*OpF310-CF11_212*S11-CF13_314*C13-CF214*S13-CF312*C11+FA112*s.dpt[2,19]+FF13_114*\
   s.dpt[2,20]+OM110*OM210*(s.In[1,10]-s.In[5,10]))
  FB110_1 = s.m[10]*AlM110_1
  FB210_1 = s.m[10]*AlM29_1
  FM110_1 = FB110_1+FB112_1+FM131_114
  FM210_1 = FB210_1+FB212_1*C11+FB214_1*C13-FB312_1*S11-FM131_314*S13
  FM310_1 = s.m[10]*AlM310_1+FB212_1*S11+FB214_1*S13+FB312_1*C11+FM131_314*C13
  CM110_1 = CM111_112-FB210_1*s.l[3,10]+s.dpt[2,19]*(FB212_1*S11+FB312_1*C11)+s.dpt[2,20]*(FB214_1*S13+FM131_314*C13)-\
   s.dpt[3,19]*(FB212_1*C11-FB312_1*S11)-s.dpt[3,20]*(FB214_1*C13-FM131_314*S13)
  CM210_1 = CM111_212*C11+FB110_1*s.l[3,10]+FB112_1*s.dpt[3,19]+FM131_114*s.dpt[3,20]
  CM310_1 = CM111_212*S11-FB112_1*s.dpt[2,19]-FM131_114*s.dpt[2,20]
  FB110_2 = s.m[10]*AlM110_2
  FB210_2 = s.m[10]*AlM29_2
  FM110_2 = FB110_2+FB112_2+FM132_114
  FM210_2 = FB210_2+FB212_2*C11+FB214_2*C13-FB312_2*S11-FM132_314*S13
  FM310_2 = s.m[10]*AlM310_2+FB212_2*S11+FB214_2*S13+FB312_2*C11+FM132_314*C13
  CM110_2 = CM112_112-FB210_2*s.l[3,10]+s.dpt[2,19]*(FB212_2*S11+FB312_2*C11)+s.dpt[2,20]*(FB214_2*S13+FM132_314*C13)-\
   s.dpt[3,19]*(FB212_2*C11-FB312_2*S11)-s.dpt[3,20]*(FB214_2*C13-FM132_314*S13)
  CM210_2 = CM112_212*C11+FB110_2*s.l[3,10]+FB112_2*s.dpt[3,19]+FM132_114*s.dpt[3,20]
  CM310_2 = CM112_212*S11-FB112_2*s.dpt[2,19]-FM132_114*s.dpt[2,20]
  FB110_3 = s.m[10]*AlM110_3
  FB210_3 = s.m[10]*AlM29_3
  FM110_3 = FB110_3+FB112_3+FM133_114
  FM210_3 = FB210_3+FB212_3*C11+FB214_3*C13-FB312_3*S11-FM133_314*S13
  FM310_3 = s.m[10]*AlM310_3+FB212_3*S11+FB214_3*S13+FB312_3*C11+FM133_314*C13
  CM110_3 = CM113_112-FB210_3*s.l[3,10]+s.dpt[2,19]*(FB212_3*S11+FB312_3*C11)+s.dpt[2,20]*(FB214_3*S13+FM133_314*C13)-\
   s.dpt[3,19]*(FB212_3*C11-FB312_3*S11)-s.dpt[3,20]*(FB214_3*C13-FM133_314*S13)
  CM210_3 = CM113_212*C11+FB110_3*s.l[3,10]+FB112_3*s.dpt[3,19]+FM133_114*s.dpt[3,20]
  CM310_3 = CM113_212*S11-FB112_3*s.dpt[2,19]-FM133_114*s.dpt[2,20]
  FB110_4 = s.m[10]*(AlM110_4+OpM29_4*s.l[3,10])
  FB210_4 = s.m[10]*(AlM29_4-OpM110_4*s.l[3,10])
  FM110_4 = FB110_4+FB112_4+FM134_114
  FM210_4 = FB210_4+FB212_4*C11+FB214_4*C13-FB312_4*S11-FM134_314*S13
  FM310_4 = s.m[10]*AlM310_4+FB212_4*S11+FB214_4*S13+FB312_4*C11+FM134_314*C13
  CM110_4 = CM114_112+CM134_114+s.In[1,10]*OpM110_4-FB210_4*s.l[3,10]+s.dpt[2,19]*(FB212_4*S11+FB312_4*C11)+s.dpt[2,20]*\
   (FB214_4*S13+FM134_314*C13)-s.dpt[3,19]*(FB212_4*C11-FB312_4*S11)-s.dpt[3,20]*(FB214_4*C13-FM134_314*S13)
  CM210_4 = s.In[5,10]*OpM29_4+CM114_212*C11-CM134_314*S13+CM214_4*C13-CM312_4*S11+FB110_4*s.l[3,10]+FB112_4*s.dpt[3,19]\
   +FM134_114*s.dpt[3,20]
  CM310_4 = s.In[9,10]*OpM310_4+CM114_212*S11+CM134_314*C13+CM214_4*S13+CM312_4*C11-FB112_4*s.dpt[2,19]-FM134_114*\
   s.dpt[2,20]
  FB110_5 = s.m[10]*(AlM110_5+OpM29_5*s.l[3,10])
  FB210_5 = s.m[10]*(AlM29_5-OpM110_5*s.l[3,10])
  FM110_5 = FB110_5+FB112_5+FM135_114
  FM210_5 = FB210_5+FB212_5*C11+FB214_5*C13-FB312_5*S11-FM135_314*S13
  FM310_5 = s.m[10]*AlM310_5+FB212_5*S11+FB214_5*S13+FB312_5*C11+FM135_314*C13
  CM110_5 = CM115_112+CM135_114+s.In[1,10]*OpM110_5-FB210_5*s.l[3,10]+s.dpt[2,19]*(FB212_5*S11+FB312_5*C11)+s.dpt[2,20]*\
   (FB214_5*S13+FM135_314*C13)-s.dpt[3,19]*(FB212_5*C11-FB312_5*S11)-s.dpt[3,20]*(FB214_5*C13-FM135_314*S13)
  CM210_5 = s.In[5,10]*OpM29_5+CM115_212*C11-CM135_314*S13+CM214_5*C13-CM312_5*S11+FB110_5*s.l[3,10]+FB112_5*s.dpt[3,19]\
   +FM135_114*s.dpt[3,20]
  CM310_5 = s.In[9,10]*OpM310_5+CM115_212*S11+CM135_314*C13+CM214_5*S13+CM312_5*C11-FB112_5*s.dpt[2,19]-FM135_114*\
   s.dpt[2,20]
  FB110_6 = s.m[10]*(AlM110_6+OpM29_6*s.l[3,10])
  FB210_6 = s.m[10]*(AlM29_6-OpM110_6*s.l[3,10])
  FM110_6 = FB110_6+FB112_6+FM136_114
  FM210_6 = FB210_6+FB212_6*C11+FB214_6*C13-FB312_6*S11-FM136_314*S13
  FM310_6 = s.m[10]*AlM310_6+FB212_6*S11+FB214_6*S13+FB312_6*C11+FM136_314*C13
  CM110_6 = CM116_112+CM136_114+s.In[1,10]*OpM110_6-FB210_6*s.l[3,10]+s.dpt[2,19]*(FB212_6*S11+FB312_6*C11)+s.dpt[2,20]*\
   (FB214_6*S13+FM136_314*C13)-s.dpt[3,19]*(FB212_6*C11-FB312_6*S11)-s.dpt[3,20]*(FB214_6*C13-FM136_314*S13)
  CM210_6 = s.In[5,10]*OpM29_6+CM116_212*C11-CM136_314*S13+CM214_6*C13-CM312_6*S11+FB110_6*s.l[3,10]+FB112_6*s.dpt[3,19]\
   +FM136_114*s.dpt[3,20]
  CM310_6 = s.In[9,10]*OpM310_6+CM116_212*S11+CM136_314*C13+CM214_6*S13+CM312_6*C11-FB112_6*s.dpt[2,19]-FM136_114*\
   s.dpt[2,20]
  FB110_7 = s.m[10]*(AlM110_7+OpM29_7*s.l[3,10])
  FB210_7 = s.m[10]*(AlM29_7-OpM110_7*s.l[3,10])
  CM110_7 = CM117_112+CM137_114+s.In[1,10]*OpM110_7-FB210_7*s.l[3,10]+s.dpt[2,19]*(FB212_7*S11+FB312_7*C11)+s.dpt[2,20]*\
   (FB214_7*S13+FM137_314*C13)-s.dpt[3,19]*(FB212_7*C11-FB312_7*S11)-s.dpt[3,20]*(FB214_7*C13-FM137_314*S13)
  CM210_7 = s.In[5,10]*OpM29_7+CM117_212*C11-CM137_314*S13+CM214_7*C13-CM312_7*S11+FB110_7*s.l[3,10]+FB112_7*s.dpt[3,19]\
   +FM137_114*s.dpt[3,20]
  CM310_7 = s.In[9,10]*OpM310_7+CM117_212*S11+CM137_314*C13+CM214_7*S13+CM312_7*C11-FB112_7*s.dpt[2,19]-FM137_114*\
   s.dpt[2,20]
  CM110_8 = CM118_112+CM138_114+s.In[1,10]*OpM110_8+s.m[10]*OpM110_8*s.l[3,10]*s.l[3,10]+s.dpt[2,19]*(FB212_8*S11+\
   FB312_8*C11)+s.dpt[2,20]*(FB214_8*S13+FM138_314*C13)-s.dpt[3,19]*(FB212_8*C11-FB312_8*S11)-s.dpt[3,20]*(FB214_8*C13-\
   FM138_314*S13)
  CM210_8 = CM118_212*C11-CM138_314*S13+CM214_8*C13-CM312_8*S11+FB112_8*s.dpt[3,19]+FM138_114*s.dpt[3,20]+S9*(s.In[5,10]\
   +s.m[10]*s.l[3,10]*s.l[3,10])
  CM310_8 = s.In[9,10]*OpM310_8+CM118_212*S11+CM138_314*C13+CM214_8*S13+CM312_8*C11-FB112_8*s.dpt[2,19]-FM138_114*\
   s.dpt[2,20]
  CM210_9 = CM119_212*C11-CM139_314*S13+CM214_9*C13-CM312_9*S11+FB112_9*s.dpt[3,19]+FM139_114*s.dpt[3,20]
  CM210_10 = s.In[5,10]+s.In[9,12]*S11*S11+s.m[10]*s.l[3,10]*s.l[3,10]+s.m[14]*s.dpt[3,20]*s.dpt[3,20]+CM214_10*C13+\
   FB112_10*s.dpt[3,19]+C11*(q[12]*FB112_10+s.In[5,12]*C11+FB112_10*s.l[3,12])+S13*(CM114_10*S14-CM314_10*C14)
  FF9_110 = FF110*C10+FF310*S10
  FF9_310 = -(FF110*S10-FF310*C10)
  CF9_110 = CF110*C10+CF310*S10
  CF9_310 = -(CF110*S10-CF310*C10)
  FM91_110 = FM110_1*C10+FM310_1*S10
  FM91_310 = -(FM110_1*S10-FM310_1*C10)
  CM91_110 = CM110_1*C10+CM310_1*S10
  CM91_310 = -(CM110_1*S10-CM310_1*C10)
  FM92_110 = FM110_2*C10+FM310_2*S10
  FM92_310 = -(FM110_2*S10-FM310_2*C10)
  CM92_110 = CM110_2*C10+CM310_2*S10
  CM92_310 = -(CM110_2*S10-CM310_2*C10)
  FM93_110 = FM110_3*C10+FM310_3*S10
  FM93_310 = -(FM110_3*S10-FM310_3*C10)
  CM93_110 = CM110_3*C10+CM310_3*S10
  CM93_310 = -(CM110_3*S10-CM310_3*C10)
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
  CM99_110 = C10*(CM119_112+CM139_114+s.In[1,10]*C10+s.m[10]*s.l[3,10]*s.l[3,10]*C10+s.dpt[2,19]*(FB212_9*S11+FB312_9*\
   C11)+s.dpt[2,20]*(FB214_9*S13+FM139_314*C13)-s.dpt[3,19]*(FB212_9*C11-FB312_9*S11)-s.dpt[3,20]*(FB214_9*C13-FM139_314*S13))+\
   S10*(s.In[9,10]*S10+CM119_212*S11+CM139_314*C13+CM214_9*S13+CM312_9*C11-FB112_9*s.dpt[2,19]-FM139_114*s.dpt[2,20])
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
  FA17 = -(s.frc[1,7]-s.m[7]*(AlF17+BeF27*s.l[2,7]-s.l[1,7]*(OM27*OM27+OM37*OM37)))
  FA27 = -(s.frc[2,7]-s.m[7]*(AlF27+BS57*s.l[2,7]+s.l[1,7]*(BS27+OpF37)))
  FA37 = -(s.frc[3,7]-s.m[7]*(AlF37+BeF87*s.l[2,7]-s.l[1,7]*(OpF27-OM17*OM37)))
  FF17 = FA17-FF8_29*S8+FF9_110*C8
  FF27 = FA27+FF8_29*C8+FF9_110*S8
  FF37 = FA37+FF8_39
  CF17 = -(s.trq[1,7]-s.In[1,7]*OpF15+CF8_29*S8-CF9_110*C8-FA37*s.l[2,7]-FF8_39*s.dpt[2,18])
  CF27 = -(s.trq[2,7]-s.In[1,7]*OM17*OM37-CF8_29*C8-CF9_110*S8+FA37*s.l[1,7])
  CF37 = -(s.trq[3,7]-CF8_39+s.In[1,7]*OM17*OM27+FA17*s.l[2,7]-FA27*s.l[1,7]-s.dpt[2,18]*(FF8_29*S8-FF9_110*C8))
  FB17_1 = s.m[7]*AlM15_1
  FB27_1 = s.m[7]*AlM27_1
  FB37_1 = s.m[7]*AlM37_1
  FM17_1 = FB17_1-FM81_29*S8+FM91_110*C8
  FM27_1 = FB27_1+FM81_29*C8+FM91_110*S8
  FM37_1 = FB37_1+FM81_39
  CM17_1 = -(CM81_29*S8-CM91_110*C8-FB37_1*s.l[2,7]-FM81_39*s.dpt[2,18])
  CM27_1 = CM81_29*C8+CM91_110*S8-FB37_1*s.l[1,7]
  CM37_1 = CM81_39-FB17_1*s.l[2,7]+FB27_1*s.l[1,7]+s.dpt[2,18]*(FM81_29*S8-FM91_110*C8)
  FB17_2 = s.m[7]*AlM15_2
  FB27_2 = s.m[7]*AlM27_2
  FB37_2 = s.m[7]*AlM37_2
  FM17_2 = FB17_2-FM82_29*S8+FM92_110*C8
  FM27_2 = FB27_2+FM82_29*C8+FM92_110*S8
  FM37_2 = FB37_2+FM82_39
  CM17_2 = -(CM82_29*S8-CM92_110*C8-FB37_2*s.l[2,7]-FM82_39*s.dpt[2,18])
  CM27_2 = CM82_29*C8+CM92_110*S8-FB37_2*s.l[1,7]
  CM37_2 = CM82_39-FB17_2*s.l[2,7]+FB27_2*s.l[1,7]+s.dpt[2,18]*(FM82_29*S8-FM92_110*C8)
  FB17_3 = -s.m[7]*S5
  FB27_3 = s.m[7]*AlM27_3
  FB37_3 = s.m[7]*AlM37_3
  FM17_3 = FB17_3-FM83_29*S8+FM93_110*C8
  FM27_3 = FB27_3+FM83_29*C8+FM93_110*S8
  FM37_3 = FB37_3+FM83_39
  CM17_3 = -(CM83_29*S8-CM93_110*C8-FB37_3*s.l[2,7]-FM83_39*s.dpt[2,18])
  CM27_3 = CM83_29*C8+CM93_110*S8-FB37_3*s.l[1,7]
  CM37_3 = CM83_39-FB17_3*s.l[2,7]+FB27_3*s.l[1,7]+s.dpt[2,18]*(FM83_29*S8-FM93_110*C8)
  FB17_4 = s.m[7]*(AlM17_4-OpM37_4*s.l[2,7])
  FB27_4 = s.m[7]*(AlM27_4+OpM37_4*s.l[1,7])
  FB37_4 = s.m[7]*(AlM37_4-OpM27_4*s.l[1,7]-s.l[2,7]*S5)
  FM27_4 = FB27_4+FM84_29*C8+FM94_110*S8
  FM37_4 = FB37_4+FM84_39
  CM17_4 = -(s.In[1,7]*S5+CM84_29*S8-CM94_110*C8-FB37_4*s.l[2,7]-FM84_39*s.dpt[2,18])
  CM27_4 = CM84_29*C8+CM94_110*S8-FB37_4*s.l[1,7]
  CM37_4 = CM84_39-FB17_4*s.l[2,7]+FB27_4*s.l[1,7]+s.dpt[2,18]*(FM84_29*S8-FM94_110*C8)
  FB17_5 = s.m[7]*(AlM17_5+s.l[2,7]*S6p7)
  FB27_5 = s.m[7]*(AlM27_5-s.l[1,7]*S6p7)
  FB37_5 = s.m[7]*(AlM37_5-s.l[1,7]*C6p7)
  FM27_5 = FB27_5+FM85_29*C8+FM95_110*S8
  FM37_5 = FB37_5+FM85_39
  CM17_5 = -(CM85_29*S8-CM95_110*C8-FB37_5*s.l[2,7]-FM85_39*s.dpt[2,18])
  CM27_5 = CM85_29*C8+CM95_110*S8-FB37_5*s.l[1,7]
  CM37_5 = CM85_39-FB17_5*s.l[2,7]+FB27_5*s.l[1,7]+s.dpt[2,18]*(FM85_29*S8-FM95_110*C8)
  FB37_6 = s.m[7]*(AlM37_6+s.l[2,7])
  CM17_6 = s.In[1,7]+CM96_110*C8+FB37_6*s.l[2,7]+FM86_39*s.dpt[2,18]-S8*(CM210_6*C9-CM96_310*S9)
  CM17_7 = s.In[1,7]+s.m[7]*s.l[2,7]*s.l[2,7]+CM97_110*C8+s.dpt[2,18]*(C9*(C10*(s.m[10]*AlM310_7+FB212_7*S11+FB214_7*S13\
   +FB312_7*C11+FM137_314*C13)-S10*(FB110_7+FB112_7+FM137_114))+S9*(FB210_7+FB212_7*C11+FB214_7*C13-FB312_7*S11-FM137_314*S13))\
   -S8*(CM210_7*C9-CM97_310*S9)

# = = Block_0_2_0_2_0_5 = = 
 
# Backward Dynamics 

  FA118 = -(s.frc[1,18]-s.m[18]*(AlF118+BeF318*s.l[3,18]))
  FA218 = -(s.frc[2,18]-s.m[18]*(AlF217+BeF618*s.l[3,18]))
  FF118 = FA118+FA120+FF21_122
  FF218 = FA218+FA220*C19+FA222*C21-FA320*S19-FF21_322*S21
  FF318 = -(s.frc[3,18]-s.m[18]*(AlF318+BS918*s.l[3,18])-FA220*S19-FA222*S21-FA320*C19-FF21_322*C21)
  CF118 = -(s.trq[1,18]-CF19_120-CF21_122-s.In[1,18]*OpF118+FA218*s.l[3,18]+OM218*OM318*(s.In[5,18]-s.In[9,18])-\
   s.dpt[2,26]*(FA220*S19+FA320*C19)-s.dpt[2,27]*(FA222*S21+FF21_322*C21)+s.dpt[3,26]*(FA220*C19-FA320*S19)+s.dpt[3,27]*(FA222*\
   C21-FF21_322*S21))
  CF218 = -(s.trq[2,18]-s.In[5,18]*OpF217-CF19_220*C19+CF21_322*S21-CF222*C21+CF320*S19-FA118*s.l[3,18]-FA120*\
   s.dpt[3,26]-FF21_122*s.dpt[3,27]-OM118*OM318*(s.In[1,18]-s.In[9,18]))
  CF318 = -(s.trq[3,18]-s.In[9,18]*OpF318-CF19_220*S19-CF21_322*C21-CF222*S21-CF320*C19+FA120*s.dpt[2,26]+FF21_122*\
   s.dpt[2,27]+OM118*OM218*(s.In[1,18]-s.In[5,18]))
  FB118_1 = s.m[18]*AlM118_1
  FB218_1 = s.m[18]*AlM217_1
  FM118_1 = FB118_1+FB120_1+FM211_122
  FM218_1 = FB218_1+FB220_1*C19+FB222_1*C21-FB320_1*S19-FM211_322*S21
  FM318_1 = s.m[18]*AlM318_1+FB220_1*S19+FB222_1*S21+FB320_1*C19+FM211_322*C21
  CM118_1 = CM191_120-FB218_1*s.l[3,18]+s.dpt[2,26]*(FB220_1*S19+FB320_1*C19)+s.dpt[2,27]*(FB222_1*S21+FM211_322*C21)-\
   s.dpt[3,26]*(FB220_1*C19-FB320_1*S19)-s.dpt[3,27]*(FB222_1*C21-FM211_322*S21)
  CM218_1 = CM191_220*C19+FB118_1*s.l[3,18]+FB120_1*s.dpt[3,26]+FM211_122*s.dpt[3,27]
  CM318_1 = CM191_220*S19-FB120_1*s.dpt[2,26]-FM211_122*s.dpt[2,27]
  FB118_2 = s.m[18]*AlM118_2
  FB218_2 = s.m[18]*AlM217_2
  FM118_2 = FB118_2+FB120_2+FM212_122
  FM218_2 = FB218_2+FB220_2*C19+FB222_2*C21-FB320_2*S19-FM212_322*S21
  FM318_2 = s.m[18]*AlM318_2+FB220_2*S19+FB222_2*S21+FB320_2*C19+FM212_322*C21
  CM118_2 = CM192_120-FB218_2*s.l[3,18]+s.dpt[2,26]*(FB220_2*S19+FB320_2*C19)+s.dpt[2,27]*(FB222_2*S21+FM212_322*C21)-\
   s.dpt[3,26]*(FB220_2*C19-FB320_2*S19)-s.dpt[3,27]*(FB222_2*C21-FM212_322*S21)
  CM218_2 = CM192_220*C19+FB118_2*s.l[3,18]+FB120_2*s.dpt[3,26]+FM212_122*s.dpt[3,27]
  CM318_2 = CM192_220*S19-FB120_2*s.dpt[2,26]-FM212_122*s.dpt[2,27]
  FB118_3 = s.m[18]*AlM118_3
  FB218_3 = s.m[18]*AlM217_3
  FM118_3 = FB118_3+FB120_3+FM213_122
  FM218_3 = FB218_3+FB220_3*C19+FB222_3*C21-FB320_3*S19-FM213_322*S21
  FM318_3 = s.m[18]*AlM318_3+FB220_3*S19+FB222_3*S21+FB320_3*C19+FM213_322*C21
  CM118_3 = CM193_120-FB218_3*s.l[3,18]+s.dpt[2,26]*(FB220_3*S19+FB320_3*C19)+s.dpt[2,27]*(FB222_3*S21+FM213_322*C21)-\
   s.dpt[3,26]*(FB220_3*C19-FB320_3*S19)-s.dpt[3,27]*(FB222_3*C21-FM213_322*S21)
  CM218_3 = CM193_220*C19+FB118_3*s.l[3,18]+FB120_3*s.dpt[3,26]+FM213_122*s.dpt[3,27]
  CM318_3 = CM193_220*S19-FB120_3*s.dpt[2,26]-FM213_122*s.dpt[2,27]
  FB118_4 = s.m[18]*(AlM118_4+OpM217_4*s.l[3,18])
  FB218_4 = s.m[18]*(AlM217_4-OpM118_4*s.l[3,18])
  FM118_4 = FB118_4+FB120_4+FM214_122
  FM218_4 = FB218_4+FB220_4*C19+FB222_4*C21-FB320_4*S19-FM214_322*S21
  FM318_4 = s.m[18]*AlM318_4+FB220_4*S19+FB222_4*S21+FB320_4*C19+FM214_322*C21
  CM118_4 = CM194_120+CM214_122+s.In[1,18]*OpM118_4-FB218_4*s.l[3,18]+s.dpt[2,26]*(FB220_4*S19+FB320_4*C19)+s.dpt[2,27]*\
   (FB222_4*S21+FM214_322*C21)-s.dpt[3,26]*(FB220_4*C19-FB320_4*S19)-s.dpt[3,27]*(FB222_4*C21-FM214_322*S21)
  CM218_4 = s.In[5,18]*OpM217_4+CM194_220*C19-CM214_322*S21+CM222_4*C21-CM320_4*S19+FB118_4*s.l[3,18]+FB120_4*\
   s.dpt[3,26]+FM214_122*s.dpt[3,27]
  CM318_4 = s.In[9,18]*OpM318_4+CM194_220*S19+CM214_322*C21+CM222_4*S21+CM320_4*C19-FB120_4*s.dpt[2,26]-FM214_122*\
   s.dpt[2,27]
  FB118_5 = s.m[18]*(AlM118_5+OpM217_5*s.l[3,18])
  FB218_5 = s.m[18]*(AlM217_5-OpM118_5*s.l[3,18])
  FM118_5 = FB118_5+FB120_5+FM215_122
  FM218_5 = FB218_5+FB220_5*C19+FB222_5*C21-FB320_5*S19-FM215_322*S21
  FM318_5 = s.m[18]*AlM318_5+FB220_5*S19+FB222_5*S21+FB320_5*C19+FM215_322*C21
  CM118_5 = CM195_120+CM215_122+s.In[1,18]*OpM118_5-FB218_5*s.l[3,18]+s.dpt[2,26]*(FB220_5*S19+FB320_5*C19)+s.dpt[2,27]*\
   (FB222_5*S21+FM215_322*C21)-s.dpt[3,26]*(FB220_5*C19-FB320_5*S19)-s.dpt[3,27]*(FB222_5*C21-FM215_322*S21)
  CM218_5 = s.In[5,18]*OpM217_5+CM195_220*C19-CM215_322*S21+CM222_5*C21-CM320_5*S19+FB118_5*s.l[3,18]+FB120_5*\
   s.dpt[3,26]+FM215_122*s.dpt[3,27]
  CM318_5 = s.In[9,18]*OpM318_5+CM195_220*S19+CM215_322*C21+CM222_5*S21+CM320_5*C19-FB120_5*s.dpt[2,26]-FM215_122*\
   s.dpt[2,27]
  FB118_6 = s.m[18]*(AlM118_6+OpM217_6*s.l[3,18])
  FB218_6 = s.m[18]*(AlM217_6-OpM118_6*s.l[3,18])
  FM118_6 = FB118_6+FB120_6+FM216_122
  FM218_6 = FB218_6+FB220_6*C19+FB222_6*C21-FB320_6*S19-FM216_322*S21
  FM318_6 = s.m[18]*AlM318_6+FB220_6*S19+FB222_6*S21+FB320_6*C19+FM216_322*C21
  CM118_6 = CM196_120+CM216_122+s.In[1,18]*OpM118_6-FB218_6*s.l[3,18]+s.dpt[2,26]*(FB220_6*S19+FB320_6*C19)+s.dpt[2,27]*\
   (FB222_6*S21+FM216_322*C21)-s.dpt[3,26]*(FB220_6*C19-FB320_6*S19)-s.dpt[3,27]*(FB222_6*C21-FM216_322*S21)
  CM218_6 = s.In[5,18]*OpM217_6+CM196_220*C19-CM216_322*S21+CM222_6*C21-CM320_6*S19+FB118_6*s.l[3,18]+FB120_6*\
   s.dpt[3,26]+FM216_122*s.dpt[3,27]
  CM318_6 = s.In[9,18]*OpM318_6+CM196_220*S19+CM216_322*C21+CM222_6*S21+CM320_6*C19-FB120_6*s.dpt[2,26]-FM216_122*\
   s.dpt[2,27]
  FB118_15 = s.m[18]*(AlM118_15+OpM217_15*s.l[3,18])
  FB218_15 = s.m[18]*(AlM217_15-OpM118_15*s.l[3,18])
  CM118_15 = CM1915_120+CM2115_122+s.In[1,18]*OpM118_15-FB218_15*s.l[3,18]+s.dpt[2,26]*(FB220_15*S19+FB320_15*C19)+\
   s.dpt[2,27]*(FB222_15*S21+FM2115_322*C21)-s.dpt[3,26]*(FB220_15*C19-FB320_15*S19)-s.dpt[3,27]*(FB222_15*C21-FM2115_322*S21)
  CM218_15 = s.In[5,18]*OpM217_15+CM1915_220*C19-CM2115_322*S21+CM222_15*C21-CM320_15*S19+FB118_15*s.l[3,18]+FB120_15*\
   s.dpt[3,26]+FM2115_122*s.dpt[3,27]
  CM318_15 = s.In[9,18]*OpM318_15+CM1915_220*S19+CM2115_322*C21+CM222_15*S21+CM320_15*C19-FB120_15*s.dpt[2,26]-\
   FM2115_122*s.dpt[2,27]
  CM118_16 = CM1916_120+CM2116_122+s.In[1,18]*OpM118_16+s.m[18]*OpM118_16*s.l[3,18]*s.l[3,18]+s.dpt[2,26]*(FB220_16*S19+\
   FB320_16*C19)+s.dpt[2,27]*(FB222_16*S21+FM2116_322*C21)-s.dpt[3,26]*(FB220_16*C19-FB320_16*S19)-s.dpt[3,27]*(FB222_16*C21-\
   FM2116_322*S21)
  CM218_16 = CM1916_220*C19-CM2116_322*S21+CM222_16*C21-CM320_16*S19+FB120_16*s.dpt[3,26]+FM2116_122*s.dpt[3,27]+S17*(\
   s.In[5,18]+s.m[18]*s.l[3,18]*s.l[3,18])
  CM318_16 = s.In[9,18]*OpM318_16+CM1916_220*S19+CM2116_322*C21+CM222_16*S21+CM320_16*C19-FB120_16*s.dpt[2,26]-\
   FM2116_122*s.dpt[2,27]
  CM218_17 = CM1917_220*C19-CM2117_322*S21+CM222_17*C21-CM320_17*S19+FB120_17*s.dpt[3,26]+FM2117_122*s.dpt[3,27]
  CM218_18 = s.In[5,18]+s.In[9,20]*S19*S19+s.m[18]*s.l[3,18]*s.l[3,18]+s.m[22]*s.dpt[3,27]*s.dpt[3,27]+CM222_18*C21+\
   FB120_18*s.dpt[3,26]+C19*(q[20]*FB120_18+s.In[5,20]*C19+FB120_18*s.l[3,20])+S21*(CM122_18*S22-CM322_18*C22)
  FF17_118 = FF118*C18+FF318*S18
  FF17_318 = -(FF118*S18-FF318*C18)
  CF17_118 = CF118*C18+CF318*S18
  CF17_318 = -(CF118*S18-CF318*C18)
  FM171_118 = FM118_1*C18+FM318_1*S18
  FM171_318 = -(FM118_1*S18-FM318_1*C18)
  CM171_118 = CM118_1*C18+CM318_1*S18
  CM171_318 = -(CM118_1*S18-CM318_1*C18)
  FM172_118 = FM118_2*C18+FM318_2*S18
  FM172_318 = -(FM118_2*S18-FM318_2*C18)
  CM172_118 = CM118_2*C18+CM318_2*S18
  CM172_318 = -(CM118_2*S18-CM318_2*C18)
  FM173_118 = FM118_3*C18+FM318_3*S18
  FM173_318 = -(FM118_3*S18-FM318_3*C18)
  CM173_118 = CM118_3*C18+CM318_3*S18
  CM173_318 = -(CM118_3*S18-CM318_3*C18)
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
  CM1717_118 = C18*(CM1917_120+CM2117_122+s.In[1,18]*C18+s.m[18]*s.l[3,18]*s.l[3,18]*C18+s.dpt[2,26]*(FB220_17*S19+\
   FB320_17*C19)+s.dpt[2,27]*(FB222_17*S21+FM2117_322*C21)-s.dpt[3,26]*(FB220_17*C19-FB320_17*S19)-s.dpt[3,27]*(FB222_17*C21-\
   FM2117_322*S21))+S18*(s.In[9,18]*S18+CM1917_220*S19+CM2117_322*C21+CM222_17*S21+CM320_17*C19-FB120_17*s.dpt[2,26]-FM2117_122\
   *s.dpt[2,27])
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
  FA115 = -(s.frc[1,15]-s.m[15]*(AlF115+BeF215*s.l[2,15]-s.l[1,15]*(OM215*OM215+OM315*OM315)))
  FA215 = -(s.frc[2,15]-s.m[15]*(AlF215+BS515*s.l[2,15]+s.l[1,15]*(BS215+OpF315)))
  FA315 = -(s.frc[3,15]-s.m[15]*(AlF315+BeF815*s.l[2,15]-s.l[1,15]*(OpF215-OM115*OM315)))
  FF115 = FA115-FF16_217*S16+FF17_118*C16
  FF215 = FA215+FF16_217*C16+FF17_118*S16
  FF315 = FA315+FF16_317
  CF115 = -(s.trq[1,15]-s.In[1,15]*OpF15+CF16_217*S16-CF17_118*C16-FA315*s.l[2,15]-FF16_317*s.dpt[2,25])
  CF215 = -(s.trq[2,15]-s.In[1,15]*OM115*OM315-CF16_217*C16-CF17_118*S16+FA315*s.l[1,15])
  CF315 = -(s.trq[3,15]-CF16_317+s.In[1,15]*OM115*OM215+FA115*s.l[2,15]-FA215*s.l[1,15]-s.dpt[2,25]*(FF16_217*S16-\
   FF17_118*C16))
  FB115_1 = s.m[15]*AlM15_1
  FB215_1 = s.m[15]*AlM215_1
  FB315_1 = s.m[15]*AlM315_1
  FM115_1 = FB115_1-FM161_217*S16+FM171_118*C16
  FM215_1 = FB215_1+FM161_217*C16+FM171_118*S16
  FM315_1 = FB315_1+FM161_317
  CM115_1 = -(CM161_217*S16-CM171_118*C16-FB315_1*s.l[2,15]-FM161_317*s.dpt[2,25])
  CM215_1 = CM161_217*C16+CM171_118*S16-FB315_1*s.l[1,15]
  CM315_1 = CM161_317-FB115_1*s.l[2,15]+FB215_1*s.l[1,15]+s.dpt[2,25]*(FM161_217*S16-FM171_118*C16)
  FB115_2 = s.m[15]*AlM15_2
  FB215_2 = s.m[15]*AlM215_2
  FB315_2 = s.m[15]*AlM315_2
  FM115_2 = FB115_2-FM162_217*S16+FM172_118*C16
  FM215_2 = FB215_2+FM162_217*C16+FM172_118*S16
  FM315_2 = FB315_2+FM162_317
  CM115_2 = -(CM162_217*S16-CM172_118*C16-FB315_2*s.l[2,15]-FM162_317*s.dpt[2,25])
  CM215_2 = CM162_217*C16+CM172_118*S16-FB315_2*s.l[1,15]
  CM315_2 = CM162_317-FB115_2*s.l[2,15]+FB215_2*s.l[1,15]+s.dpt[2,25]*(FM162_217*S16-FM172_118*C16)
  FB115_3 = -s.m[15]*S5
  FB215_3 = s.m[15]*AlM215_3
  FB315_3 = s.m[15]*AlM315_3
  FM115_3 = FB115_3-FM163_217*S16+FM173_118*C16
  FM215_3 = FB215_3+FM163_217*C16+FM173_118*S16
  FM315_3 = FB315_3+FM163_317
  CM115_3 = -(CM163_217*S16-CM173_118*C16-FB315_3*s.l[2,15]-FM163_317*s.dpt[2,25])
  CM215_3 = CM163_217*C16+CM173_118*S16-FB315_3*s.l[1,15]
  CM315_3 = CM163_317-FB115_3*s.l[2,15]+FB215_3*s.l[1,15]+s.dpt[2,25]*(FM163_217*S16-FM173_118*C16)
  FB115_4 = s.m[15]*(AlM115_4-OpM315_4*s.l[2,15])
  FB215_4 = s.m[15]*(AlM215_4+OpM315_4*s.l[1,15])
  FB315_4 = s.m[15]*(AlM315_4-OpM215_4*s.l[1,15]-s.l[2,15]*S5)
  FM215_4 = FB215_4+FM164_217*C16+FM174_118*S16
  FM315_4 = FB315_4+FM164_317
  CM115_4 = -(s.In[1,15]*S5+CM164_217*S16-CM174_118*C16-FB315_4*s.l[2,15]-FM164_317*s.dpt[2,25])
  CM215_4 = CM164_217*C16+CM174_118*S16-FB315_4*s.l[1,15]
  CM315_4 = CM164_317-FB115_4*s.l[2,15]+FB215_4*s.l[1,15]+s.dpt[2,25]*(FM164_217*S16-FM174_118*C16)
  FB115_5 = s.m[15]*(AlM115_5+s.l[2,15]*S15p6)
  FB215_5 = s.m[15]*(AlM215_5-s.l[1,15]*S15p6)
  FB315_5 = s.m[15]*(AlM315_5-s.l[1,15]*C15p6)
  FM215_5 = FB215_5+FM165_217*C16+FM175_118*S16
  FM315_5 = FB315_5+FM165_317
  CM115_5 = -(CM165_217*S16-CM175_118*C16-FB315_5*s.l[2,15]-FM165_317*s.dpt[2,25])
  CM215_5 = CM165_217*C16+CM175_118*S16-FB315_5*s.l[1,15]
  CM315_5 = CM165_317-FB115_5*s.l[2,15]+FB215_5*s.l[1,15]+s.dpt[2,25]*(FM165_217*S16-FM175_118*C16)
  FB315_6 = s.m[15]*(AlM315_6+s.l[2,15])
  CM115_6 = s.In[1,15]+CM176_118*C16+FB315_6*s.l[2,15]+FM166_317*s.dpt[2,25]+S16*(CM176_318*S17-CM218_6*C17)
  CM115_15 = s.In[1,15]+s.m[15]*s.l[2,15]*s.l[2,15]+CM1715_118*C16+s.dpt[2,25]*(C17*(C18*(s.m[18]*AlM318_15+FB220_15*S19\
   +FB222_15*S21+FB320_15*C19+FM2115_322*C21)-S18*(FB118_15+FB120_15+FM2115_122))+S17*(FB218_15+FB220_15*C19+FB222_15*C21-\
   FB320_15*S19-FM2115_322*S21))+S16*(CM1715_318*S17-CM218_15*C17)

# = = Block_0_2_0_2_0_8 = = 
 
# Backward Dynamics 

  FA124 = -(s.frc[1,24]-s.m[24]*(AlF123*C24+AlF223*S24-s.l[2,24]*(OpF323-OM124*OM224)))
  FA224 = -(s.frc[2,24]+s.m[24]*(AlF123*S24-AlF223*C24+s.l[2,24]*(OM124*OM124+OM324*OM324)))
  FA324 = -(s.frc[3,24]-s.m[24]*(s.l[2,24]*(OpF124+OM224*OM324)+C23*(AlF36+BS96*s.dpt[3,6]+BeF76*s.dpt[1,6]+BeF86*\
   s.dpt[2,6])-S23*(AlF26+BS56*s.dpt[2,6]+BeF46*s.dpt[1,6]+BeF66*s.dpt[3,6])))
  CF124 = -(s.trq[1,24]-s.In[1,24]*OpF124-s.In[9,24]*OM224*OM324-FA324*s.l[2,24])
  CF224 = -(s.trq[2,24]-OM124*OM324*(s.In[1,24]-s.In[9,24]))
  CF324 = -(s.trq[3,24]+s.In[1,24]*OM124*OM224-s.In[9,24]*OpF323+FA124*s.l[2,24])
  FB124_1 = s.m[24]*(AlM15_1*C24+AlM223_1*S24)
  FB224_1 = -s.m[24]*(AlM15_1*S24-AlM223_1*C24)
  FB324_1 = -s.m[24]*(AlM26_1*S23-AlM36_1*C23)
  CM124_1 = FB324_1*s.l[2,24]
  CM324_1 = -FB124_1*s.l[2,24]
  FB124_2 = s.m[24]*(AlM15_2*C24+AlM223_2*S24)
  FB224_2 = -s.m[24]*(AlM15_2*S24-AlM223_2*C24)
  FB324_2 = -s.m[24]*(AlM26_2*S23-AlM36_2*C23)
  CM124_2 = FB324_2*s.l[2,24]
  CM324_2 = -FB124_2*s.l[2,24]
  FB124_3 = s.m[24]*(AlM223_3*S24-C24*S5)
  FB224_3 = s.m[24]*(AlM223_3*C24+S24*S5)
  FB324_3 = s.m[24]*C23p6*C5
  CM124_3 = FB324_3*s.l[2,24]
  CM324_3 = -FB124_3*s.l[2,24]
  FB124_4 = s.m[24]*(AlM123_4*C24+AlM223_4*S24-OpM323_4*s.l[2,24])
  FB224_4 = -s.m[24]*(AlM123_4*S24-AlM223_4*C24)
  FB324_4 = s.m[24]*(OpM124_4*s.l[2,24]-C23*(OpM26_4*s.dpt[1,6]+s.dpt[2,6]*S5)-S23*(OpM36_4*s.dpt[1,6]+s.dpt[3,6]*S5))
  CM124_4 = s.In[1,24]*OpM124_4+FB324_4*s.l[2,24]
  CM324_4 = s.In[9,24]*OpM323_4-FB124_4*s.l[2,24]
  FB124_5 = s.m[24]*(AlM123_5*C24+AlM223_5*S24+s.l[2,24]*S23p6)
  FB224_5 = -s.m[24]*(AlM123_5*S24-AlM223_5*C24)
  FB324_5 = s.m[24]*(OpM124_5*s.l[2,24]-s.dpt[1,6]*C23p6)
  CM124_5 = s.In[1,24]*OpM124_5+FB324_5*s.l[2,24]
  CM324_5 = -(s.In[9,24]*S23p6+FB124_5*s.l[2,24])
  FB324_6 = s.m[24]*(s.dpt[2,6]*C23+s.dpt[3,6]*S23+s.l[2,24]*C24)
  CM324_6 = -s.m[24]*AlM223_6*s.l[2,24]*S24
  CM324_24 = s.In[9,24]+s.m[24]*s.l[2,24]*s.l[2,24]
  FF23_124 = FA124*C24-FA224*S24
  FF23_224 = FA124*S24+FA224*C24
  CF23_124 = CF124*C24-CF224*S24
  CF23_224 = CF124*S24+CF224*C24
  FM231_124 = FB124_1*C24-FB224_1*S24
  FM231_224 = FB124_1*S24+FB224_1*C24
  CM231_124 = CM124_1*C24
  CM231_224 = CM124_1*S24
  FM232_124 = FB124_2*C24-FB224_2*S24
  FM232_224 = FB124_2*S24+FB224_2*C24
  CM232_124 = CM124_2*C24
  CM232_224 = CM124_2*S24
  FM233_124 = FB124_3*C24-FB224_3*S24
  FM233_224 = FB124_3*S24+FB224_3*C24
  CM233_124 = CM124_3*C24
  CM233_224 = CM124_3*S24
  FM234_124 = FB124_4*C24-FB224_4*S24
  FM234_224 = FB124_4*S24+FB224_4*C24
  CM234_124 = CM124_4*C24
  CM234_224 = CM124_4*S24
  FM235_124 = FB124_5*C24-FB224_5*S24
  FM235_224 = FB124_5*S24+FB224_5*C24
  CM235_124 = CM124_5*C24
  CM235_224 = CM124_5*S24
  FM236_224 = s.m[24]*AlM223_6
  CM236_124 = C24*(s.In[1,24]*C24+FB324_6*s.l[2,24])
  CM2323_124 = C24*C24*(s.In[1,24]+s.m[24]*s.l[2,24]*s.l[2,24])

# = = Block_0_2_0_2_0_9 = = 
 
# Backward Dynamics 

  FA126 = -(s.frc[1,26]-s.m[26]*(AlF125*C26+AlF225*S26-s.l[2,26]*(OpF325-OM126*OM226)))
  FA226 = -(s.frc[2,26]+s.m[26]*(AlF125*S26-AlF225*C26+s.l[2,26]*(OM126*OM126+OM326*OM326)))
  FA326 = -(s.frc[3,26]-s.m[26]*(s.l[2,26]*(OpF126+OM226*OM326)+C25*(AlF36+BS96*s.dpt[3,8]+BeF76*s.dpt[1,8]+BeF86*\
   s.dpt[2,8])-S25*(AlF26+BS56*s.dpt[2,8]+BeF46*s.dpt[1,8]+BeF66*s.dpt[3,8])))
  CF126 = -(s.trq[1,26]-s.In[1,26]*OpF126-s.In[9,26]*OM226*OM326-FA326*s.l[2,26])
  CF226 = -(s.trq[2,26]-OM126*OM326*(s.In[1,26]-s.In[9,26]))
  CF326 = -(s.trq[3,26]+s.In[1,26]*OM126*OM226-s.In[9,26]*OpF325+FA126*s.l[2,26])
  FB126_1 = s.m[26]*(AlM15_1*C26+AlM225_1*S26)
  FB226_1 = -s.m[26]*(AlM15_1*S26-AlM225_1*C26)
  FB326_1 = -s.m[26]*(AlM26_1*S25-AlM36_1*C25)
  CM126_1 = FB326_1*s.l[2,26]
  CM326_1 = -FB126_1*s.l[2,26]
  FB126_2 = s.m[26]*(AlM15_2*C26+AlM225_2*S26)
  FB226_2 = -s.m[26]*(AlM15_2*S26-AlM225_2*C26)
  FB326_2 = -s.m[26]*(AlM26_2*S25-AlM36_2*C25)
  CM126_2 = FB326_2*s.l[2,26]
  CM326_2 = -FB126_2*s.l[2,26]
  FB126_3 = s.m[26]*(AlM225_3*S26-C26*S5)
  FB226_3 = s.m[26]*(AlM225_3*C26+S26*S5)
  FB326_3 = s.m[26]*C25p6*C5
  CM126_3 = FB326_3*s.l[2,26]
  CM326_3 = -FB126_3*s.l[2,26]
  FB126_4 = s.m[26]*(AlM125_4*C26+AlM225_4*S26-OpM325_4*s.l[2,26])
  FB226_4 = -s.m[26]*(AlM125_4*S26-AlM225_4*C26)
  FB326_4 = s.m[26]*(OpM126_4*s.l[2,26]-C25*(OpM26_4*s.dpt[1,8]+s.dpt[2,8]*S5)-S25*(OpM36_4*s.dpt[1,8]+s.dpt[3,8]*S5))
  CM126_4 = s.In[1,26]*OpM126_4+FB326_4*s.l[2,26]
  CM326_4 = s.In[9,26]*OpM325_4-FB126_4*s.l[2,26]
  FB126_5 = s.m[26]*(AlM125_5*C26+AlM225_5*S26+s.l[2,26]*S25p6)
  FB226_5 = -s.m[26]*(AlM125_5*S26-AlM225_5*C26)
  FB326_5 = s.m[26]*(OpM126_5*s.l[2,26]-s.dpt[1,8]*C25p6)
  CM126_5 = s.In[1,26]*OpM126_5+FB326_5*s.l[2,26]
  CM326_5 = -(s.In[9,26]*S25p6+FB126_5*s.l[2,26])
  FB326_6 = s.m[26]*(s.dpt[2,8]*C25+s.dpt[3,8]*S25+s.l[2,26]*C26)
  CM326_6 = -s.m[26]*AlM225_6*s.l[2,26]*S26
  CM326_26 = s.In[9,26]+s.m[26]*s.l[2,26]*s.l[2,26]
  FF25_126 = FA126*C26-FA226*S26
  FF25_226 = FA126*S26+FA226*C26
  CF25_126 = CF126*C26-CF226*S26
  CF25_226 = CF126*S26+CF226*C26
  FM251_126 = FB126_1*C26-FB226_1*S26
  FM251_226 = FB126_1*S26+FB226_1*C26
  CM251_126 = CM126_1*C26
  CM251_226 = CM126_1*S26
  FM252_126 = FB126_2*C26-FB226_2*S26
  FM252_226 = FB126_2*S26+FB226_2*C26
  CM252_126 = CM126_2*C26
  CM252_226 = CM126_2*S26
  FM253_126 = FB126_3*C26-FB226_3*S26
  FM253_226 = FB126_3*S26+FB226_3*C26
  CM253_126 = CM126_3*C26
  CM253_226 = CM126_3*S26
  FM254_126 = FB126_4*C26-FB226_4*S26
  FM254_226 = FB126_4*S26+FB226_4*C26
  CM254_126 = CM126_4*C26
  CM254_226 = CM126_4*S26
  FM255_126 = FB126_5*C26-FB226_5*S26
  FM255_226 = FB126_5*S26+FB226_5*C26
  CM255_126 = CM126_5*C26
  CM255_226 = CM126_5*S26
  FM256_226 = s.m[26]*AlM225_6
  CM256_126 = C26*(s.In[1,26]*C26+FB326_6*s.l[2,26])
  CM2525_126 = C26*C26*(s.In[1,26]+s.m[26]*s.l[2,26]*s.l[2,26])

# = = Block_0_2_0_2_0_10 = = 
 
# Backward Dynamics 

  FA128 = -(s.frc[1,28]-s.m[28]*(AlF127*C28+AlF227*S28-s.l[2,28]*(OpF327-OM128*OM228)))
  FA228 = -(s.frc[2,28]+s.m[28]*(AlF127*S28-AlF227*C28+s.l[2,28]*(OM128*OM128+OM328*OM328)))
  FA328 = -(s.frc[3,28]-s.m[28]*(s.l[2,28]*(OpF128+OM228*OM328)+C27*(AlF36+BS96*s.dpt[3,9]+BeF76*s.dpt[1,9]+BeF86*\
   s.dpt[2,9])-S27*(AlF26+BS56*s.dpt[2,9]+BeF46*s.dpt[1,9]+BeF66*s.dpt[3,9])))
  CF128 = -(s.trq[1,28]-s.In[1,28]*OpF128-s.In[9,28]*OM228*OM328-FA328*s.l[2,28])
  CF228 = -(s.trq[2,28]-OM128*OM328*(s.In[1,28]-s.In[9,28]))
  CF328 = -(s.trq[3,28]+s.In[1,28]*OM128*OM228-s.In[9,28]*OpF327+FA128*s.l[2,28])
  FB128_1 = s.m[28]*(AlM15_1*C28+AlM227_1*S28)
  FB228_1 = -s.m[28]*(AlM15_1*S28-AlM227_1*C28)
  FB328_1 = -s.m[28]*(AlM26_1*S27-AlM36_1*C27)
  CM128_1 = FB328_1*s.l[2,28]
  CM328_1 = -FB128_1*s.l[2,28]
  FB128_2 = s.m[28]*(AlM15_2*C28+AlM227_2*S28)
  FB228_2 = -s.m[28]*(AlM15_2*S28-AlM227_2*C28)
  FB328_2 = -s.m[28]*(AlM26_2*S27-AlM36_2*C27)
  CM128_2 = FB328_2*s.l[2,28]
  CM328_2 = -FB128_2*s.l[2,28]
  FB128_3 = s.m[28]*(AlM227_3*S28-C28*S5)
  FB228_3 = s.m[28]*(AlM227_3*C28+S28*S5)
  FB328_3 = s.m[28]*C27p6*C5
  CM128_3 = FB328_3*s.l[2,28]
  CM328_3 = -FB128_3*s.l[2,28]
  FB128_4 = s.m[28]*(AlM127_4*C28+AlM227_4*S28-OpM327_4*s.l[2,28])
  FB228_4 = -s.m[28]*(AlM127_4*S28-AlM227_4*C28)
  FB328_4 = s.m[28]*(OpM128_4*s.l[2,28]-C27*(OpM26_4*s.dpt[1,9]+s.dpt[2,9]*S5)-S27*(OpM36_4*s.dpt[1,9]+s.dpt[3,9]*S5))
  CM128_4 = s.In[1,28]*OpM128_4+FB328_4*s.l[2,28]
  CM328_4 = s.In[9,28]*OpM327_4-FB128_4*s.l[2,28]
  FB128_5 = s.m[28]*(AlM127_5*C28+AlM227_5*S28+s.l[2,28]*S27p6)
  FB228_5 = -s.m[28]*(AlM127_5*S28-AlM227_5*C28)
  FB328_5 = s.m[28]*(OpM128_5*s.l[2,28]-s.dpt[1,9]*C27p6)
  CM128_5 = s.In[1,28]*OpM128_5+FB328_5*s.l[2,28]
  CM328_5 = -(s.In[9,28]*S27p6+FB128_5*s.l[2,28])
  FB328_6 = s.m[28]*(s.dpt[2,9]*C27+s.dpt[3,9]*S27+s.l[2,28]*C28)
  CM328_6 = -s.m[28]*AlM227_6*s.l[2,28]*S28
  CM328_28 = s.In[9,28]+s.m[28]*s.l[2,28]*s.l[2,28]
  FF27_128 = FA128*C28-FA228*S28
  FF27_228 = FA128*S28+FA228*C28
  CF27_128 = CF128*C28-CF228*S28
  CF27_228 = CF128*S28+CF228*C28
  FM271_128 = FB128_1*C28-FB228_1*S28
  FM271_228 = FB128_1*S28+FB228_1*C28
  CM271_128 = CM128_1*C28
  CM271_228 = CM128_1*S28
  FM272_128 = FB128_2*C28-FB228_2*S28
  FM272_228 = FB128_2*S28+FB228_2*C28
  CM272_128 = CM128_2*C28
  CM272_228 = CM128_2*S28
  FM273_128 = FB128_3*C28-FB228_3*S28
  FM273_228 = FB128_3*S28+FB228_3*C28
  CM273_128 = CM128_3*C28
  CM273_228 = CM128_3*S28
  FM274_128 = FB128_4*C28-FB228_4*S28
  FM274_228 = FB128_4*S28+FB228_4*C28
  CM274_128 = CM128_4*C28
  CM274_228 = CM128_4*S28
  FM275_128 = FB128_5*C28-FB228_5*S28
  FM275_228 = FB128_5*S28+FB228_5*C28
  CM275_128 = CM128_5*C28
  CM275_228 = CM128_5*S28
  FM276_228 = s.m[28]*AlM227_6
  CM276_128 = C28*(s.In[1,28]*C28+FB328_6*s.l[2,28])
  CM2727_128 = C28*C28*(s.In[1,28]+s.m[28]*s.l[2,28]*s.l[2,28])

# = = Block_0_2_0_2_0_11 = = 
 
# Backward Dynamics 

  FA133 = -(s.frc[1,33]-s.m[33]*(AlF133+BeF233*s.l[2,33]+BeF333*s.l[3,33]))
  FA233 = -(s.frc[2,33]-s.m[33]*(AlF233+BS533*s.l[2,33]+BeF633*s.l[3,33]))
  FA333 = -(s.frc[3,33]-s.m[33]*(AlF332+BS933*s.l[3,33]+BeF833*s.l[2,33]))
  FF133 = FA133+FA135+FF36_137
  FF233 = FA233+FA235*C34+FA237*C36-FA335*S34-FF36_337*S36
  FF333 = FA333+FA235*S34+FA237*S36+FA335*C34+FF36_337*C36
  CF133 = -(s.trq[1,33]-CF34_135-CF36_137-s.In[1,33]*OpF133+FA233*s.l[3,33]-FA333*s.l[2,33]+OM233*OM333*(s.In[5,33]-\
   s.In[9,33])-s.dpt[2,36]*(FA235*S34+FA335*C34)-s.dpt[2,37]*(FA237*S36+FF36_337*C36)+s.dpt[3,36]*(FA235*C34-FA335*S34)+\
   s.dpt[3,37]*(FA237*C36-FF36_337*S36))
  CF233 = -(s.trq[2,33]-s.In[5,33]*OpF233-CF237*C36+CF335*S34-CF34_235*C34+CF36_337*S36-FA133*s.l[3,33]-FA135*\
   s.dpt[3,36]-FF36_137*s.dpt[3,37]-OM133*OM333*(s.In[1,33]-s.In[9,33]))
  CF333 = -(s.trq[3,33]-s.In[9,33]*OpF332-CF237*S36-CF335*C34-CF34_235*S34-CF36_337*C36+FA133*s.l[2,33]+FA135*\
   s.dpt[2,36]+FF36_137*s.dpt[2,37]+OM133*OM233*(s.In[1,33]-s.In[5,33]))
  FB133_1 = s.m[33]*AlM133_1
  FB233_1 = s.m[33]*AlM233_1
  FB333_1 = s.m[33]*AlM332_1
  FM133_1 = FB133_1+FB135_1+FM361_137
  FM233_1 = FB233_1+FB235_1*C34+FB237_1*C36-FB335_1*S34-FM361_337*S36
  FM333_1 = FB333_1+FB235_1*S34+FB237_1*S36+FB335_1*C34+FM361_337*C36
  CM133_1 = CM341_135-FB233_1*s.l[3,33]+FB333_1*s.l[2,33]+s.dpt[2,36]*(FB235_1*S34+FB335_1*C34)+s.dpt[2,37]*(FB237_1*S36\
   +FM361_337*C36)-s.dpt[3,36]*(FB235_1*C34-FB335_1*S34)-s.dpt[3,37]*(FB237_1*C36-FM361_337*S36)
  CM233_1 = CM341_235*C34+FB133_1*s.l[3,33]+FB135_1*s.dpt[3,36]+FM361_137*s.dpt[3,37]
  CM333_1 = CM341_235*S34-FB133_1*s.l[2,33]-FB135_1*s.dpt[2,36]-FM361_137*s.dpt[2,37]
  FB133_2 = s.m[33]*AlM133_2
  FB233_2 = s.m[33]*AlM233_2
  FB333_2 = s.m[33]*AlM332_2
  FM133_2 = FB133_2+FB135_2+FM362_137
  FM233_2 = FB233_2+FB235_2*C34+FB237_2*C36-FB335_2*S34-FM362_337*S36
  FM333_2 = FB333_2+FB235_2*S34+FB237_2*S36+FB335_2*C34+FM362_337*C36
  CM133_2 = CM342_135-FB233_2*s.l[3,33]+FB333_2*s.l[2,33]+s.dpt[2,36]*(FB235_2*S34+FB335_2*C34)+s.dpt[2,37]*(FB237_2*S36\
   +FM362_337*C36)-s.dpt[3,36]*(FB235_2*C34-FB335_2*S34)-s.dpt[3,37]*(FB237_2*C36-FM362_337*S36)
  CM233_2 = CM342_235*C34+FB133_2*s.l[3,33]+FB135_2*s.dpt[3,36]+FM362_137*s.dpt[3,37]
  CM333_2 = CM342_235*S34-FB133_2*s.l[2,33]-FB135_2*s.dpt[2,36]-FM362_137*s.dpt[2,37]
  FB133_3 = s.m[33]*AlM133_3
  FB233_3 = s.m[33]*AlM233_3
  FB333_3 = s.m[33]*AlM332_3
  FM133_3 = FB133_3+FB135_3+FM363_137
  FM233_3 = FB233_3+FB235_3*C34+FB237_3*C36-FB335_3*S34-FM363_337*S36
  FM333_3 = FB333_3+FB235_3*S34+FB237_3*S36+FB335_3*C34+FM363_337*C36
  CM133_3 = CM343_135-FB233_3*s.l[3,33]+FB333_3*s.l[2,33]+s.dpt[2,36]*(FB235_3*S34+FB335_3*C34)+s.dpt[2,37]*(FB237_3*S36\
   +FM363_337*C36)-s.dpt[3,36]*(FB235_3*C34-FB335_3*S34)-s.dpt[3,37]*(FB237_3*C36-FM363_337*S36)
  CM233_3 = CM343_235*C34+FB133_3*s.l[3,33]+FB135_3*s.dpt[3,36]+FM363_137*s.dpt[3,37]
  CM333_3 = CM343_235*S34-FB133_3*s.l[2,33]-FB135_3*s.dpt[2,36]-FM363_137*s.dpt[2,37]
  FB133_4 = s.m[33]*(AlM133_4+OpM233_4*s.l[3,33]-OpM332_4*s.l[2,33])
  FB233_4 = s.m[33]*(AlM233_4-OpM133_4*s.l[3,33])
  FB333_4 = s.m[33]*(AlM332_4+OpM133_4*s.l[2,33])
  FM133_4 = FB133_4+FB135_4+FM364_137
  FM233_4 = FB233_4+FB235_4*C34+FB237_4*C36-FB335_4*S34-FM364_337*S36
  FM333_4 = FB333_4+FB235_4*S34+FB237_4*S36+FB335_4*C34+FM364_337*C36
  CM133_4 = CM344_135+CM364_137+s.In[1,33]*OpM133_4-FB233_4*s.l[3,33]+FB333_4*s.l[2,33]+s.dpt[2,36]*(FB235_4*S34+FB335_4\
   *C34)+s.dpt[2,37]*(FB237_4*S36+FM364_337*C36)-s.dpt[3,36]*(FB235_4*C34-FB335_4*S34)-s.dpt[3,37]*(FB237_4*C36-FM364_337*S36)
  CM233_4 = s.In[5,33]*OpM233_4+CM237_4*C36-CM335_4*S34+CM344_235*C34-CM364_337*S36+FB133_4*s.l[3,33]+FB135_4*\
   s.dpt[3,36]+FM364_137*s.dpt[3,37]
  CM333_4 = s.In[9,33]*OpM332_4+CM237_4*S36+CM335_4*C34+CM344_235*S34+CM364_337*C36-FB133_4*s.l[2,33]-FB135_4*\
   s.dpt[2,36]-FM364_137*s.dpt[2,37]
  FB133_5 = s.m[33]*(AlM133_5+OpM233_5*s.l[3,33]-OpM332_5*s.l[2,33])
  FB233_5 = s.m[33]*(AlM233_5-OpM133_5*s.l[3,33])
  FB333_5 = s.m[33]*(AlM332_5+OpM133_5*s.l[2,33])
  FM133_5 = FB133_5+FB135_5+FM365_137
  FM233_5 = FB233_5+FB235_5*C34+FB237_5*C36-FB335_5*S34-FM365_337*S36
  FM333_5 = FB333_5+FB235_5*S34+FB237_5*S36+FB335_5*C34+FM365_337*C36
  CM133_5 = CM345_135+CM365_137+s.In[1,33]*OpM133_5-FB233_5*s.l[3,33]+FB333_5*s.l[2,33]+s.dpt[2,36]*(FB235_5*S34+FB335_5\
   *C34)+s.dpt[2,37]*(FB237_5*S36+FM365_337*C36)-s.dpt[3,36]*(FB235_5*C34-FB335_5*S34)-s.dpt[3,37]*(FB237_5*C36-FM365_337*S36)
  CM233_5 = s.In[5,33]*OpM233_5+CM237_5*C36-CM335_5*S34+CM345_235*C34-CM365_337*S36+FB133_5*s.l[3,33]+FB135_5*\
   s.dpt[3,36]+FM365_137*s.dpt[3,37]
  CM333_5 = s.In[9,33]*OpM332_5+CM237_5*S36+CM335_5*C34+CM345_235*S34+CM365_337*C36-FB133_5*s.l[2,33]-FB135_5*\
   s.dpt[2,36]-FM365_137*s.dpt[2,37]
  FB133_6 = s.m[33]*(AlM133_6+OpM233_6*s.l[3,33]-OpM332_6*s.l[2,33])
  FB233_6 = s.m[33]*(AlM233_6-OpM133_6*s.l[3,33])
  FB333_6 = s.m[33]*(AlM332_6+OpM133_6*s.l[2,33])
  FM133_6 = FB133_6+FB135_6+FM366_137
  FM233_6 = FB233_6+FB235_6*C34+FB237_6*C36-FB335_6*S34-FM366_337*S36
  FM333_6 = FB333_6+FB235_6*S34+FB237_6*S36+FB335_6*C34+FM366_337*C36
  CM133_6 = CM346_135+CM366_137+s.In[1,33]*OpM133_6-FB233_6*s.l[3,33]+FB333_6*s.l[2,33]+s.dpt[2,36]*(FB235_6*S34+FB335_6\
   *C34)+s.dpt[2,37]*(FB237_6*S36+FM366_337*C36)-s.dpt[3,36]*(FB235_6*C34-FB335_6*S34)-s.dpt[3,37]*(FB237_6*C36-FM366_337*S36)
  CM233_6 = s.In[5,33]*OpM233_6+CM237_6*C36-CM335_6*S34+CM346_235*C34-CM366_337*S36+FB133_6*s.l[3,33]+FB135_6*\
   s.dpt[3,36]+FM366_137*s.dpt[3,37]
  CM333_6 = s.In[9,33]*OpM332_6+CM237_6*S36+CM335_6*C34+CM346_235*S34+CM366_337*C36-FB133_6*s.l[2,33]-FB135_6*\
   s.dpt[2,36]-FM366_137*s.dpt[2,37]
  FB133_29 = s.m[33]*(AlM133_29+OpM233_29*s.l[3,33]-OpM332_29*s.l[2,33])
  FB233_29 = s.m[33]*(AlM233_29-OpM133_29*s.l[3,33])
  FB333_29 = s.m[33]*(AlM332_29+OpM133_29*s.l[2,33])
  FM133_29 = FB133_29+FB135_29+FM3629_137
  FM233_29 = FB233_29+FB235_29*C34+FB237_29*C36-FB335_29*S34-FM3629_337*S36
  FM333_29 = FB333_29+FB235_29*S34+FB237_29*S36+FB335_29*C34+FM3629_337*C36
  CM133_29 = CM3429_135+CM3629_137+s.In[1,33]*OpM133_29-FB233_29*s.l[3,33]+FB333_29*s.l[2,33]+s.dpt[2,36]*(FB235_29*S34+\
   FB335_29*C34)+s.dpt[2,37]*(FB237_29*S36+FM3629_337*C36)-s.dpt[3,36]*(FB235_29*C34-FB335_29*S34)-s.dpt[3,37]*(FB237_29*C36-\
   FM3629_337*S36)
  CM233_29 = s.In[5,33]*OpM233_29+CM237_29*C36-CM335_29*S34+CM3429_235*C34-CM3629_337*S36+FB133_29*s.l[3,33]+FB135_29*\
   s.dpt[3,36]+FM3629_137*s.dpt[3,37]
  CM333_29 = s.In[9,33]*OpM332_29+CM237_29*S36+CM335_29*C34+CM3429_235*S34+CM3629_337*C36-FB133_29*s.l[2,33]-FB135_29*\
   s.dpt[2,36]-FM3629_137*s.dpt[2,37]
  FB133_30 = s.m[33]*(AlM133_30+OpM233_30*s.l[3,33]-OpM332_30*s.l[2,33])
  FB233_30 = s.m[33]*(AlM233_30-OpM133_30*s.l[3,33])
  FB333_30 = s.m[33]*(AlM332_30+OpM133_30*s.l[2,33])
  CM133_30 = CM3430_135+CM3630_137+s.In[1,33]*OpM133_30-FB233_30*s.l[3,33]+FB333_30*s.l[2,33]+s.dpt[2,36]*(FB235_30*S34+\
   FB335_30*C34)+s.dpt[2,37]*(FB237_30*S36+FM3630_337*C36)-s.dpt[3,36]*(FB235_30*C34-FB335_30*S34)-s.dpt[3,37]*(FB237_30*C36-\
   FM3630_337*S36)
  CM233_30 = s.In[5,33]*OpM233_30+CM237_30*C36-CM335_30*S34+CM3430_235*C34-CM3630_337*S36+FB133_30*s.l[3,33]+FB135_30*\
   s.dpt[3,36]+FM3630_137*s.dpt[3,37]
  CM333_30 = s.In[9,33]*OpM332_30+CM237_30*S36+CM335_30*C34+CM3430_235*S34+CM3630_337*C36-FB133_30*s.l[2,33]-FB135_30*\
   s.dpt[2,36]-FM3630_137*s.dpt[2,37]
  FB133_31 = s.m[33]*(OpM233_31*s.l[3,33]-s.l[2,33]*S32)
  CM133_31 = CM3431_135+CM3631_137+s.In[1,33]*OpM133_31+s.m[33]*OpM133_31*s.l[2,33]*s.l[2,33]+s.m[33]*OpM133_31*\
   s.l[3,33]*s.l[3,33]+s.dpt[2,36]*(FB235_31*S34+FB335_31*C34)+s.dpt[2,37]*(FB237_31*S36+FM3631_337*C36)-s.dpt[3,36]*(FB235_31*\
   C34-FB335_31*S34)-s.dpt[3,37]*(FB237_31*C36-FM3631_337*S36)
  CM233_31 = s.In[5,33]*OpM233_31+CM237_31*C36-CM335_31*S34+CM3431_235*C34-CM3631_337*S36+FB133_31*s.l[3,33]+FB135_31*\
   s.dpt[3,36]+FM3631_137*s.dpt[3,37]
  CM333_31 = s.In[9,33]*S32+CM237_31*S36+CM335_31*C34+CM3431_235*S34+CM3631_337*C36-FB133_31*s.l[2,33]-FB135_31*\
   s.dpt[2,36]-FM3631_137*s.dpt[2,37]
  FB133_32 = s.m[33]*s.l[3,33]*C33
  CM333_32 = CM237_32*S36+CM335_32*C34+CM3432_235*S34+CM3632_337*C36-FB133_32*s.l[2,33]-FB135_32*s.dpt[2,36]-FM3632_137*\
   s.dpt[2,37]
  CM333_33 = s.In[9,33]+s.In[9,35]*C34*C34+s.m[33]*s.l[2,33]*s.l[2,33]+s.m[37]*s.dpt[2,37]*s.dpt[2,37]+CM237_33*S36-\
   FB135_33*s.dpt[2,36]+S34*(q[35]*FB135_33+s.In[5,35]*S34+FB135_33*s.l[3,35])-C36*(CM137_33*S37-CM337_33*C37)
  FF32_133 = FF133*C33-FF233*S33
  FF32_233 = FF133*S33+FF233*C33
  CF32_133 = CF133*C33-CF233*S33
  CF32_233 = CF133*S33+CF233*C33
  FM321_133 = FM133_1*C33-FM233_1*S33
  FM321_233 = FM133_1*S33+FM233_1*C33
  CM321_133 = CM133_1*C33-CM233_1*S33
  CM321_233 = CM133_1*S33+CM233_1*C33
  FM322_133 = FM133_2*C33-FM233_2*S33
  FM322_233 = FM133_2*S33+FM233_2*C33
  CM322_133 = CM133_2*C33-CM233_2*S33
  CM322_233 = CM133_2*S33+CM233_2*C33
  FM323_133 = FM133_3*C33-FM233_3*S33
  FM323_233 = FM133_3*S33+FM233_3*C33
  CM323_133 = CM133_3*C33-CM233_3*S33
  CM323_233 = CM133_3*S33+CM233_3*C33
  FM324_133 = FM133_4*C33-FM233_4*S33
  FM324_233 = FM133_4*S33+FM233_4*C33
  CM324_133 = CM133_4*C33-CM233_4*S33
  CM324_233 = CM133_4*S33+CM233_4*C33
  FM325_133 = FM133_5*C33-FM233_5*S33
  FM325_233 = FM133_5*S33+FM233_5*C33
  CM325_133 = CM133_5*C33-CM233_5*S33
  CM325_233 = CM133_5*S33+CM233_5*C33
  FM326_133 = FM133_6*C33-FM233_6*S33
  FM326_233 = FM133_6*S33+FM233_6*C33
  CM326_133 = CM133_6*C33-CM233_6*S33
  CM326_233 = CM133_6*S33+CM233_6*C33
  FM3229_133 = FM133_29*C33-FM233_29*S33
  CM3229_133 = CM133_29*C33-CM233_29*S33
  CM3229_233 = CM133_29*S33+CM233_29*C33
  CM3230_133 = CM133_30*C33-CM233_30*S33
  CM3230_233 = CM133_30*S33+CM233_30*C33
  CM3231_233 = CM133_31*S33+CM233_31*C33
  CM3232_233 = C33*(s.In[5,33]*C33+CM237_32*C36-CM335_32*S34+CM3432_235*C34-CM3632_337*S36+FB133_32*s.l[3,33]+FB135_32*\
   s.dpt[3,36]+FM3632_137*s.dpt[3,37])+S33*(CM3432_135+CM3632_137+s.In[1,33]*S33+s.m[33]*s.l[2,33]*s.l[2,33]*S33+s.m[33]*\
   s.l[3,33]*s.l[3,33]*S33+s.dpt[2,36]*(FB235_32*S34+FB335_32*C34)+s.dpt[2,37]*(FB237_32*S36+FM3632_337*C36)-s.dpt[3,36]*(\
   FB235_32*C34-FB335_32*S34)-s.dpt[3,37]*(FB237_32*C36-FM3632_337*S36))
  FF31_132 = FF32_133*C32+FF333*S32
  FF31_332 = -(FF32_133*S32-FF333*C32)
  CF31_132 = CF32_133*C32+CF333*S32
  CF31_332 = -(CF32_133*S32-CF333*C32)
  FM311_132 = FM321_133*C32+FM333_1*S32
  FM311_332 = -(FM321_133*S32-FM333_1*C32)
  CM311_132 = CM321_133*C32+CM333_1*S32
  CM311_332 = -(CM321_133*S32-CM333_1*C32)
  FM312_132 = FM322_133*C32+FM333_2*S32
  FM312_332 = -(FM322_133*S32-FM333_2*C32)
  CM312_132 = CM322_133*C32+CM333_2*S32
  CM312_332 = -(CM322_133*S32-CM333_2*C32)
  FM313_132 = FM323_133*C32+FM333_3*S32
  FM313_332 = -(FM323_133*S32-FM333_3*C32)
  CM313_132 = CM323_133*C32+CM333_3*S32
  CM313_332 = -(CM323_133*S32-CM333_3*C32)
  FM314_132 = FM324_133*C32+FM333_4*S32
  FM314_332 = -(FM324_133*S32-FM333_4*C32)
  CM314_132 = CM324_133*C32+CM333_4*S32
  CM314_332 = -(CM324_133*S32-CM333_4*C32)
  FM315_132 = FM325_133*C32+FM333_5*S32
  FM315_332 = -(FM325_133*S32-FM333_5*C32)
  CM315_132 = CM325_133*C32+CM333_5*S32
  CM315_332 = -(CM325_133*S32-CM333_5*C32)
  FM316_132 = FM326_133*C32+FM333_6*S32
  FM316_332 = -(FM326_133*S32-FM333_6*C32)
  CM316_132 = CM326_133*C32+CM333_6*S32
  CM316_332 = -(CM326_133*S32-CM333_6*C32)
  CM3129_132 = CM3229_133*C32+CM333_29*S32
  CM3129_332 = -(CM3229_133*S32-CM333_29*C32)
  CM3130_132 = CM3230_133*C32+CM333_30*S32
  CM3131_132 = CM333_31*S32+C32*(CM133_31*C33-CM233_31*S33)
  FA130 = -(s.frc[1,30]-s.m[30]*(AlF130+BeF230*s.l[2,30]))
  FA330 = -(s.frc[3,30]-s.m[30]*(AlF329+BeF830*s.l[2,30]))
  FF130 = FA130+FF31_132
  FF230 = -(s.frc[2,30]-s.m[30]*(AlF230+BS530*s.l[2,30])+FF31_332*S31-FF32_233*C31)
  FF330 = FA330+FF31_332*C31+FF32_233*S31
  CF130 = -(s.trq[1,30]-CF31_132-s.In[1,30]*OpF130-s.In[9,30]*OM230*OM330-FA330*s.l[2,30]-s.dpt[2,35]*(FF31_332*C31+\
   FF32_233*S31))
  CF230 = -(s.trq[2,30]+CF31_332*S31-CF32_233*C31-OM130*OM330*(s.In[1,30]-s.In[9,30]))
  CF330 = -(s.trq[3,30]+s.In[1,30]*OM130*OM230-s.In[9,30]*OpF329-CF31_332*C31-CF32_233*S31+FA130*s.l[2,30]+FF31_132*\
   s.dpt[2,35])
  FB130_1 = s.m[30]*AlM130_1
  FB330_1 = s.m[30]*AlM329_1
  FM130_1 = FB130_1+FM311_132
  FM230_1 = s.m[30]*AlM230_1-FM311_332*S31+FM321_233*C31
  FM330_1 = FB330_1+FM311_332*C31+FM321_233*S31
  CM301_231 = -(CM311_332*S31-CM321_233*C31)
  CM130_1 = CM311_132+FB330_1*s.l[2,30]+s.dpt[2,35]*(FM311_332*C31+FM321_233*S31)
  CM330_1 = CM311_332*C31+CM321_233*S31-FB130_1*s.l[2,30]-FM311_132*s.dpt[2,35]
  FB130_2 = s.m[30]*AlM130_2
  FB330_2 = s.m[30]*AlM329_2
  FM130_2 = FB130_2+FM312_132
  FM230_2 = s.m[30]*AlM230_2-FM312_332*S31+FM322_233*C31
  FM330_2 = FB330_2+FM312_332*C31+FM322_233*S31
  CM302_231 = -(CM312_332*S31-CM322_233*C31)
  CM130_2 = CM312_132+FB330_2*s.l[2,30]+s.dpt[2,35]*(FM312_332*C31+FM322_233*S31)
  CM330_2 = CM312_332*C31+CM322_233*S31-FB130_2*s.l[2,30]-FM312_132*s.dpt[2,35]
  FB130_3 = s.m[30]*AlM130_3
  FB330_3 = s.m[30]*AlM329_3
  FM130_3 = FB130_3+FM313_132
  FM230_3 = s.m[30]*AlM230_3-FM313_332*S31+FM323_233*C31
  FM330_3 = FB330_3+FM313_332*C31+FM323_233*S31
  CM303_231 = -(CM313_332*S31-CM323_233*C31)
  CM130_3 = CM313_132+FB330_3*s.l[2,30]+s.dpt[2,35]*(FM313_332*C31+FM323_233*S31)
  CM330_3 = CM313_332*C31+CM323_233*S31-FB130_3*s.l[2,30]-FM313_132*s.dpt[2,35]
  FB130_4 = s.m[30]*(AlM130_4-OpM329_4*s.l[2,30])
  FB330_4 = s.m[30]*(AlM329_4+OpM130_4*s.l[2,30])
  FM130_4 = FB130_4+FM314_132
  FM230_4 = s.m[30]*AlM230_4-FM314_332*S31+FM324_233*C31
  FM330_4 = FB330_4+FM314_332*C31+FM324_233*S31
  CM304_231 = -(CM314_332*S31-CM324_233*C31)
  CM130_4 = CM314_132+s.In[1,30]*OpM130_4+FB330_4*s.l[2,30]+s.dpt[2,35]*(FM314_332*C31+FM324_233*S31)
  CM330_4 = s.In[9,30]*OpM329_4+CM314_332*C31+CM324_233*S31-FB130_4*s.l[2,30]-FM314_132*s.dpt[2,35]
  FB130_5 = s.m[30]*(AlM130_5+s.l[2,30]*S29p6)
  FB330_5 = s.m[30]*(AlM329_5+OpM130_5*s.l[2,30])
  FM130_5 = FB130_5+FM315_132
  FM230_5 = s.m[30]*AlM230_5-FM315_332*S31+FM325_233*C31
  FM330_5 = FB330_5+FM315_332*C31+FM325_233*S31
  CM305_231 = -(CM315_332*S31-CM325_233*C31)
  CM130_5 = CM315_132+s.In[1,30]*OpM130_5+FB330_5*s.l[2,30]+s.dpt[2,35]*(FM315_332*C31+FM325_233*S31)
  CM330_5 = CM315_332*C31+CM325_233*S31-FM315_132*s.dpt[2,35]-s.In[9,30]*S29p6-FB130_5*s.l[2,30]
  FB130_6 = s.m[30]*AlM130_6
  FB330_6 = s.m[30]*(AlM329_6+s.l[2,30]*C30)
  CM330_6 = CM316_332*C31+CM326_233*S31-FB130_6*s.l[2,30]-FM316_132*s.dpt[2,35]
  CM3029_331 = CM3129_332*C31+CM3229_233*S31-s.dpt[2,35]*(FM3229_133*C32+FM333_29*S32)
  CM330_30 = s.In[9,30]+s.m[30]*s.l[2,30]*s.l[2,30]+CM3230_233*S31-s.dpt[2,35]*(C32*(C33*(FB133_30+FB135_30+FM3630_137)-\
   S33*(FB233_30+FB235_30*C34+FB237_30*C36-FB335_30*S34-FM3630_337*S36))+S32*(FB333_30+FB235_30*S34+FB237_30*S36+FB335_30*C34+\
   FM3630_337*C36))-C31*(CM3230_133*S32-CM333_30*C32)
  FF29_130 = FF130*C30-FF230*S30
  FF29_230 = FF130*S30+FF230*C30
  CF29_130 = CF130*C30-CF230*S30
  CF29_230 = CF130*S30+CF230*C30
  FM291_130 = FM130_1*C30-FM230_1*S30
  FM291_230 = FM130_1*S30+FM230_1*C30
  CM291_130 = CM130_1*C30-CM301_231*S30
  CM291_230 = CM130_1*S30+CM301_231*C30
  FM292_130 = FM130_2*C30-FM230_2*S30
  FM292_230 = FM130_2*S30+FM230_2*C30
  CM292_130 = CM130_2*C30-CM302_231*S30
  CM292_230 = CM130_2*S30+CM302_231*C30
  FM293_130 = FM130_3*C30-FM230_3*S30
  FM293_230 = FM130_3*S30+FM230_3*C30
  CM293_130 = CM130_3*C30-CM303_231*S30
  CM293_230 = CM130_3*S30+CM303_231*C30
  FM294_230 = FM130_4*S30+FM230_4*C30
  CM294_130 = CM130_4*C30-CM304_231*S30
  CM294_230 = CM130_4*S30+CM304_231*C30
  FM295_230 = FM130_5*S30+FM230_5*C30
  CM295_130 = CM130_5*C30-CM305_231*S30
  CM295_230 = CM130_5*S30+CM305_231*C30
  CM296_130 = C30*(CM316_132+s.In[1,30]*C30+FB330_6*s.l[2,30]+s.dpt[2,35]*(FM316_332*C31+FM326_233*S31))+S30*(CM316_332*\
   S31-CM326_233*C31)
  CM2929_130 = C30*(CM3129_132+s.In[1,30]*C30+s.m[30]*s.l[2,30]*s.l[2,30]*C30-s.dpt[2,35]*(C31*(FM3229_133*S32-FM333_29*\
   C32)-S31*(FM133_29*S33+FM233_29*C33)))+S30*(CM3129_332*S31-CM3229_233*C31)

# = = Block_0_2_0_2_0_14 = = 
 
# Backward Dynamics 

  FA139 = -(s.frc[1,39]-s.m[39]*(AlF138*C39+AlF238*S39-s.l[2,39]*(OpF338-OM139*OM239)))
  FA239 = -(s.frc[2,39]+s.m[39]*(AlF138*S39-AlF238*C39+s.l[2,39]*(OM139*OM139+OM339*OM339)))
  FA339 = -(s.frc[3,39]-s.m[39]*(s.l[2,39]*(OpF139+OM239*OM339)+C38*(AlF36+BS96*s.dpt[3,11]+BeF76*s.dpt[1,11]+BeF86*\
   s.dpt[2,11])-S38*(AlF26+BS56*s.dpt[2,11]+BeF46*s.dpt[1,11]+BeF66*s.dpt[3,11])))
  CF139 = -(s.trq[1,39]-s.In[1,39]*OpF139-s.In[9,39]*OM239*OM339-FA339*s.l[2,39])
  CF239 = -(s.trq[2,39]-OM139*OM339*(s.In[1,39]-s.In[9,39]))
  CF339 = -(s.trq[3,39]+s.In[1,39]*OM139*OM239-s.In[9,39]*OpF338+FA139*s.l[2,39])
  FB139_1 = s.m[39]*(AlM15_1*C39+AlM238_1*S39)
  FB239_1 = -s.m[39]*(AlM15_1*S39-AlM238_1*C39)
  FB339_1 = -s.m[39]*(AlM26_1*S38-AlM36_1*C38)
  CM139_1 = FB339_1*s.l[2,39]
  CM339_1 = -FB139_1*s.l[2,39]
  FB139_2 = s.m[39]*(AlM15_2*C39+AlM238_2*S39)
  FB239_2 = -s.m[39]*(AlM15_2*S39-AlM238_2*C39)
  FB339_2 = -s.m[39]*(AlM26_2*S38-AlM36_2*C38)
  CM139_2 = FB339_2*s.l[2,39]
  CM339_2 = -FB139_2*s.l[2,39]
  FB139_3 = s.m[39]*(AlM238_3*S39-C39*S5)
  FB239_3 = s.m[39]*(AlM238_3*C39+S39*S5)
  FB339_3 = s.m[39]*C38p6*C5
  CM139_3 = FB339_3*s.l[2,39]
  CM339_3 = -FB139_3*s.l[2,39]
  FB139_4 = s.m[39]*(AlM138_4*C39+AlM238_4*S39-OpM338_4*s.l[2,39])
  FB239_4 = -s.m[39]*(AlM138_4*S39-AlM238_4*C39)
  FB339_4 = s.m[39]*(OpM139_4*s.l[2,39]-C38*(OpM26_4*s.dpt[1,11]+s.dpt[2,11]*S5)-S38*(OpM36_4*s.dpt[1,11]+s.dpt[3,11]*S5\
   ))
  CM139_4 = s.In[1,39]*OpM139_4+FB339_4*s.l[2,39]
  CM339_4 = s.In[9,39]*OpM338_4-FB139_4*s.l[2,39]
  FB139_5 = s.m[39]*(AlM138_5*C39+AlM238_5*S39+s.l[2,39]*S38p6)
  FB239_5 = -s.m[39]*(AlM138_5*S39-AlM238_5*C39)
  FB339_5 = s.m[39]*(OpM139_5*s.l[2,39]-s.dpt[1,11]*C38p6)
  CM139_5 = s.In[1,39]*OpM139_5+FB339_5*s.l[2,39]
  CM339_5 = -(s.In[9,39]*S38p6+FB139_5*s.l[2,39])
  FB339_6 = s.m[39]*(s.dpt[2,11]*C38+s.dpt[3,11]*S38+s.l[2,39]*C39)
  CM339_6 = -s.m[39]*AlM238_6*s.l[2,39]*S39
  CM339_39 = s.In[9,39]+s.m[39]*s.l[2,39]*s.l[2,39]
  FF38_139 = FA139*C39-FA239*S39
  FF38_239 = FA139*S39+FA239*C39
  CF38_139 = CF139*C39-CF239*S39
  CF38_239 = CF139*S39+CF239*C39
  FM381_139 = FB139_1*C39-FB239_1*S39
  FM381_239 = FB139_1*S39+FB239_1*C39
  CM381_139 = CM139_1*C39
  CM381_239 = CM139_1*S39
  FM382_139 = FB139_2*C39-FB239_2*S39
  FM382_239 = FB139_2*S39+FB239_2*C39
  CM382_139 = CM139_2*C39
  CM382_239 = CM139_2*S39
  FM383_139 = FB139_3*C39-FB239_3*S39
  FM383_239 = FB139_3*S39+FB239_3*C39
  CM383_139 = CM139_3*C39
  CM383_239 = CM139_3*S39
  FM384_139 = FB139_4*C39-FB239_4*S39
  FM384_239 = FB139_4*S39+FB239_4*C39
  CM384_139 = CM139_4*C39
  CM384_239 = CM139_4*S39
  FM385_139 = FB139_5*C39-FB239_5*S39
  FM385_239 = FB139_5*S39+FB239_5*C39
  CM385_139 = CM139_5*C39
  CM385_239 = CM139_5*S39
  FM386_239 = s.m[39]*AlM238_6
  CM386_139 = C39*(s.In[1,39]*C39+FB339_6*s.l[2,39])
  CM3838_139 = C39*C39*(s.In[1,39]+s.m[39]*s.l[2,39]*s.l[2,39])

# = = Block_0_2_0_2_0_15 = = 
 
# Backward Dynamics 

  FA144 = -(s.frc[1,44]-s.m[44]*(AlF144+BeF244*s.l[2,44]+BeF344*s.l[3,44]))
  FA244 = -(s.frc[2,44]-s.m[44]*(AlF244+BS544*s.l[2,44]+BeF644*s.l[3,44]))
  FA344 = -(s.frc[3,44]-s.m[44]*(AlF343+BS944*s.l[3,44]+BeF844*s.l[2,44]))
  FF144 = FA144+FA146+FF47_148
  FF244 = FA244+FA246*C45+FA248*C47-FA346*S45-FF47_348*S47
  FF344 = FA344+FA246*S45+FA248*S47+FA346*C45+FF47_348*C47
  CF144 = -(s.trq[1,44]-CF45_146-CF47_148-s.In[1,44]*OpF144+FA244*s.l[3,44]-FA344*s.l[2,44]+OM244*OM344*(s.In[5,44]-\
   s.In[9,44])-s.dpt[2,47]*(FA246*S45+FA346*C45)-s.dpt[2,48]*(FA248*S47+FF47_348*C47)+s.dpt[3,47]*(FA246*C45-FA346*S45)+\
   s.dpt[3,48]*(FA248*C47-FF47_348*S47))
  CF244 = -(s.trq[2,44]-s.In[5,44]*OpF244-CF248*C47+CF346*S45-CF45_246*C45+CF47_348*S47-FA144*s.l[3,44]-FA146*\
   s.dpt[3,47]-FF47_148*s.dpt[3,48]-OM144*OM344*(s.In[1,44]-s.In[9,44]))
  CF344 = -(s.trq[3,44]-s.In[9,44]*OpF343-CF248*S47-CF346*C45-CF45_246*S45-CF47_348*C47+FA144*s.l[2,44]+FA146*\
   s.dpt[2,47]+FF47_148*s.dpt[2,48]+OM144*OM244*(s.In[1,44]-s.In[5,44]))
  FB144_1 = s.m[44]*AlM144_1
  FB244_1 = s.m[44]*AlM244_1
  FB344_1 = s.m[44]*AlM343_1
  FM144_1 = FB144_1+FB146_1+FM471_148
  FM244_1 = FB244_1+FB246_1*C45+FB248_1*C47-FB346_1*S45-FM471_348*S47
  FM344_1 = FB344_1+FB246_1*S45+FB248_1*S47+FB346_1*C45+FM471_348*C47
  CM144_1 = CM451_146-FB244_1*s.l[3,44]+FB344_1*s.l[2,44]+s.dpt[2,47]*(FB246_1*S45+FB346_1*C45)+s.dpt[2,48]*(FB248_1*S47\
   +FM471_348*C47)-s.dpt[3,47]*(FB246_1*C45-FB346_1*S45)-s.dpt[3,48]*(FB248_1*C47-FM471_348*S47)
  CM244_1 = CM451_246*C45+FB144_1*s.l[3,44]+FB146_1*s.dpt[3,47]+FM471_148*s.dpt[3,48]
  CM344_1 = CM451_246*S45-FB144_1*s.l[2,44]-FB146_1*s.dpt[2,47]-FM471_148*s.dpt[2,48]
  FB144_2 = s.m[44]*AlM144_2
  FB244_2 = s.m[44]*AlM244_2
  FB344_2 = s.m[44]*AlM343_2
  FM144_2 = FB144_2+FB146_2+FM472_148
  FM244_2 = FB244_2+FB246_2*C45+FB248_2*C47-FB346_2*S45-FM472_348*S47
  FM344_2 = FB344_2+FB246_2*S45+FB248_2*S47+FB346_2*C45+FM472_348*C47
  CM144_2 = CM452_146-FB244_2*s.l[3,44]+FB344_2*s.l[2,44]+s.dpt[2,47]*(FB246_2*S45+FB346_2*C45)+s.dpt[2,48]*(FB248_2*S47\
   +FM472_348*C47)-s.dpt[3,47]*(FB246_2*C45-FB346_2*S45)-s.dpt[3,48]*(FB248_2*C47-FM472_348*S47)
  CM244_2 = CM452_246*C45+FB144_2*s.l[3,44]+FB146_2*s.dpt[3,47]+FM472_148*s.dpt[3,48]
  CM344_2 = CM452_246*S45-FB144_2*s.l[2,44]-FB146_2*s.dpt[2,47]-FM472_148*s.dpt[2,48]
  FB144_3 = s.m[44]*AlM144_3
  FB244_3 = s.m[44]*AlM244_3
  FB344_3 = s.m[44]*AlM343_3
  FM144_3 = FB144_3+FB146_3+FM473_148
  FM244_3 = FB244_3+FB246_3*C45+FB248_3*C47-FB346_3*S45-FM473_348*S47
  FM344_3 = FB344_3+FB246_3*S45+FB248_3*S47+FB346_3*C45+FM473_348*C47
  CM144_3 = CM453_146-FB244_3*s.l[3,44]+FB344_3*s.l[2,44]+s.dpt[2,47]*(FB246_3*S45+FB346_3*C45)+s.dpt[2,48]*(FB248_3*S47\
   +FM473_348*C47)-s.dpt[3,47]*(FB246_3*C45-FB346_3*S45)-s.dpt[3,48]*(FB248_3*C47-FM473_348*S47)
  CM244_3 = CM453_246*C45+FB144_3*s.l[3,44]+FB146_3*s.dpt[3,47]+FM473_148*s.dpt[3,48]
  CM344_3 = CM453_246*S45-FB144_3*s.l[2,44]-FB146_3*s.dpt[2,47]-FM473_148*s.dpt[2,48]
  FB144_4 = s.m[44]*(AlM144_4+OpM244_4*s.l[3,44]-OpM343_4*s.l[2,44])
  FB244_4 = s.m[44]*(AlM244_4-OpM144_4*s.l[3,44])
  FB344_4 = s.m[44]*(AlM343_4+OpM144_4*s.l[2,44])
  FM144_4 = FB144_4+FB146_4+FM474_148
  FM244_4 = FB244_4+FB246_4*C45+FB248_4*C47-FB346_4*S45-FM474_348*S47
  FM344_4 = FB344_4+FB246_4*S45+FB248_4*S47+FB346_4*C45+FM474_348*C47
  CM144_4 = CM454_146+CM474_148+s.In[1,44]*OpM144_4-FB244_4*s.l[3,44]+FB344_4*s.l[2,44]+s.dpt[2,47]*(FB246_4*S45+FB346_4\
   *C45)+s.dpt[2,48]*(FB248_4*S47+FM474_348*C47)-s.dpt[3,47]*(FB246_4*C45-FB346_4*S45)-s.dpt[3,48]*(FB248_4*C47-FM474_348*S47)
  CM244_4 = s.In[5,44]*OpM244_4+CM248_4*C47-CM346_4*S45+CM454_246*C45-CM474_348*S47+FB144_4*s.l[3,44]+FB146_4*\
   s.dpt[3,47]+FM474_148*s.dpt[3,48]
  CM344_4 = s.In[9,44]*OpM343_4+CM248_4*S47+CM346_4*C45+CM454_246*S45+CM474_348*C47-FB144_4*s.l[2,44]-FB146_4*\
   s.dpt[2,47]-FM474_148*s.dpt[2,48]
  FB144_5 = s.m[44]*(AlM144_5+OpM244_5*s.l[3,44]-OpM343_5*s.l[2,44])
  FB244_5 = s.m[44]*(AlM244_5-OpM144_5*s.l[3,44])
  FB344_5 = s.m[44]*(AlM343_5+OpM144_5*s.l[2,44])
  FM144_5 = FB144_5+FB146_5+FM475_148
  FM244_5 = FB244_5+FB246_5*C45+FB248_5*C47-FB346_5*S45-FM475_348*S47
  FM344_5 = FB344_5+FB246_5*S45+FB248_5*S47+FB346_5*C45+FM475_348*C47
  CM144_5 = CM455_146+CM475_148+s.In[1,44]*OpM144_5-FB244_5*s.l[3,44]+FB344_5*s.l[2,44]+s.dpt[2,47]*(FB246_5*S45+FB346_5\
   *C45)+s.dpt[2,48]*(FB248_5*S47+FM475_348*C47)-s.dpt[3,47]*(FB246_5*C45-FB346_5*S45)-s.dpt[3,48]*(FB248_5*C47-FM475_348*S47)
  CM244_5 = s.In[5,44]*OpM244_5+CM248_5*C47-CM346_5*S45+CM455_246*C45-CM475_348*S47+FB144_5*s.l[3,44]+FB146_5*\
   s.dpt[3,47]+FM475_148*s.dpt[3,48]
  CM344_5 = s.In[9,44]*OpM343_5+CM248_5*S47+CM346_5*C45+CM455_246*S45+CM475_348*C47-FB144_5*s.l[2,44]-FB146_5*\
   s.dpt[2,47]-FM475_148*s.dpt[2,48]
  FB144_6 = s.m[44]*(AlM144_6+OpM244_6*s.l[3,44]-OpM343_6*s.l[2,44])
  FB244_6 = s.m[44]*(AlM244_6-OpM144_6*s.l[3,44])
  FB344_6 = s.m[44]*(AlM343_6+OpM144_6*s.l[2,44])
  FM144_6 = FB144_6+FB146_6+FM476_148
  FM244_6 = FB244_6+FB246_6*C45+FB248_6*C47-FB346_6*S45-FM476_348*S47
  FM344_6 = FB344_6+FB246_6*S45+FB248_6*S47+FB346_6*C45+FM476_348*C47
  CM144_6 = CM456_146+CM476_148+s.In[1,44]*OpM144_6-FB244_6*s.l[3,44]+FB344_6*s.l[2,44]+s.dpt[2,47]*(FB246_6*S45+FB346_6\
   *C45)+s.dpt[2,48]*(FB248_6*S47+FM476_348*C47)-s.dpt[3,47]*(FB246_6*C45-FB346_6*S45)-s.dpt[3,48]*(FB248_6*C47-FM476_348*S47)
  CM244_6 = s.In[5,44]*OpM244_6+CM248_6*C47-CM346_6*S45+CM456_246*C45-CM476_348*S47+FB144_6*s.l[3,44]+FB146_6*\
   s.dpt[3,47]+FM476_148*s.dpt[3,48]
  CM344_6 = s.In[9,44]*OpM343_6+CM248_6*S47+CM346_6*C45+CM456_246*S45+CM476_348*C47-FB144_6*s.l[2,44]-FB146_6*\
   s.dpt[2,47]-FM476_148*s.dpt[2,48]
  FB144_40 = s.m[44]*(AlM144_40+OpM244_40*s.l[3,44]-OpM343_40*s.l[2,44])
  FB244_40 = s.m[44]*(AlM244_40-OpM144_40*s.l[3,44])
  FB344_40 = s.m[44]*(AlM343_40+OpM144_40*s.l[2,44])
  FM144_40 = FB144_40+FB146_40+FM4740_148
  FM244_40 = FB244_40+FB246_40*C45+FB248_40*C47-FB346_40*S45-FM4740_348*S47
  FM344_40 = FB344_40+FB246_40*S45+FB248_40*S47+FB346_40*C45+FM4740_348*C47
  CM144_40 = CM4540_146+CM4740_148+s.In[1,44]*OpM144_40-FB244_40*s.l[3,44]+FB344_40*s.l[2,44]+s.dpt[2,47]*(FB246_40*S45+\
   FB346_40*C45)+s.dpt[2,48]*(FB248_40*S47+FM4740_348*C47)-s.dpt[3,47]*(FB246_40*C45-FB346_40*S45)-s.dpt[3,48]*(FB248_40*C47-\
   FM4740_348*S47)
  CM244_40 = s.In[5,44]*OpM244_40+CM248_40*C47-CM346_40*S45+CM4540_246*C45-CM4740_348*S47+FB144_40*s.l[3,44]+FB146_40*\
   s.dpt[3,47]+FM4740_148*s.dpt[3,48]
  CM344_40 = s.In[9,44]*OpM343_40+CM248_40*S47+CM346_40*C45+CM4540_246*S45+CM4740_348*C47-FB144_40*s.l[2,44]-FB146_40*\
   s.dpt[2,47]-FM4740_148*s.dpt[2,48]
  FB144_41 = s.m[44]*(AlM144_41+OpM244_41*s.l[3,44]-OpM343_41*s.l[2,44])
  FB244_41 = s.m[44]*(AlM244_41-OpM144_41*s.l[3,44])
  FB344_41 = s.m[44]*(AlM343_41+OpM144_41*s.l[2,44])
  CM144_41 = CM4541_146+CM4741_148+s.In[1,44]*OpM144_41-FB244_41*s.l[3,44]+FB344_41*s.l[2,44]+s.dpt[2,47]*(FB246_41*S45+\
   FB346_41*C45)+s.dpt[2,48]*(FB248_41*S47+FM4741_348*C47)-s.dpt[3,47]*(FB246_41*C45-FB346_41*S45)-s.dpt[3,48]*(FB248_41*C47-\
   FM4741_348*S47)
  CM244_41 = s.In[5,44]*OpM244_41+CM248_41*C47-CM346_41*S45+CM4541_246*C45-CM4741_348*S47+FB144_41*s.l[3,44]+FB146_41*\
   s.dpt[3,47]+FM4741_148*s.dpt[3,48]
  CM344_41 = s.In[9,44]*OpM343_41+CM248_41*S47+CM346_41*C45+CM4541_246*S45+CM4741_348*C47-FB144_41*s.l[2,44]-FB146_41*\
   s.dpt[2,47]-FM4741_148*s.dpt[2,48]
  FB144_42 = s.m[44]*(OpM244_42*s.l[3,44]-s.l[2,44]*S43)
  CM144_42 = CM4542_146+CM4742_148+s.In[1,44]*OpM144_42+s.m[44]*OpM144_42*s.l[2,44]*s.l[2,44]+s.m[44]*OpM144_42*\
   s.l[3,44]*s.l[3,44]+s.dpt[2,47]*(FB246_42*S45+FB346_42*C45)+s.dpt[2,48]*(FB248_42*S47+FM4742_348*C47)-s.dpt[3,47]*(FB246_42*\
   C45-FB346_42*S45)-s.dpt[3,48]*(FB248_42*C47-FM4742_348*S47)
  CM244_42 = s.In[5,44]*OpM244_42+CM248_42*C47-CM346_42*S45+CM4542_246*C45-CM4742_348*S47+FB144_42*s.l[3,44]+FB146_42*\
   s.dpt[3,47]+FM4742_148*s.dpt[3,48]
  CM344_42 = s.In[9,44]*S43+CM248_42*S47+CM346_42*C45+CM4542_246*S45+CM4742_348*C47-FB144_42*s.l[2,44]-FB146_42*\
   s.dpt[2,47]-FM4742_148*s.dpt[2,48]
  FB144_43 = s.m[44]*s.l[3,44]*C44
  CM344_43 = CM248_43*S47+CM346_43*C45+CM4543_246*S45+CM4743_348*C47-FB144_43*s.l[2,44]-FB146_43*s.dpt[2,47]-FM4743_148*\
   s.dpt[2,48]
  CM344_44 = s.In[9,44]+s.In[9,46]*C45*C45+s.m[44]*s.l[2,44]*s.l[2,44]+s.m[48]*s.dpt[2,48]*s.dpt[2,48]+CM248_44*S47-\
   FB146_44*s.dpt[2,47]+S45*(q[46]*FB146_44+s.In[5,46]*S45+FB146_44*s.l[3,46])-C47*(CM148_44*S48-CM348_44*C48)
  FF43_144 = FF144*C44-FF244*S44
  FF43_244 = FF144*S44+FF244*C44
  CF43_144 = CF144*C44-CF244*S44
  CF43_244 = CF144*S44+CF244*C44
  FM431_144 = FM144_1*C44-FM244_1*S44
  FM431_244 = FM144_1*S44+FM244_1*C44
  CM431_144 = CM144_1*C44-CM244_1*S44
  CM431_244 = CM144_1*S44+CM244_1*C44
  FM432_144 = FM144_2*C44-FM244_2*S44
  FM432_244 = FM144_2*S44+FM244_2*C44
  CM432_144 = CM144_2*C44-CM244_2*S44
  CM432_244 = CM144_2*S44+CM244_2*C44
  FM433_144 = FM144_3*C44-FM244_3*S44
  FM433_244 = FM144_3*S44+FM244_3*C44
  CM433_144 = CM144_3*C44-CM244_3*S44
  CM433_244 = CM144_3*S44+CM244_3*C44
  FM434_144 = FM144_4*C44-FM244_4*S44
  FM434_244 = FM144_4*S44+FM244_4*C44
  CM434_144 = CM144_4*C44-CM244_4*S44
  CM434_244 = CM144_4*S44+CM244_4*C44
  FM435_144 = FM144_5*C44-FM244_5*S44
  FM435_244 = FM144_5*S44+FM244_5*C44
  CM435_144 = CM144_5*C44-CM244_5*S44
  CM435_244 = CM144_5*S44+CM244_5*C44
  FM436_144 = FM144_6*C44-FM244_6*S44
  FM436_244 = FM144_6*S44+FM244_6*C44
  CM436_144 = CM144_6*C44-CM244_6*S44
  CM436_244 = CM144_6*S44+CM244_6*C44
  FM4340_144 = FM144_40*C44-FM244_40*S44
  CM4340_144 = CM144_40*C44-CM244_40*S44
  CM4340_244 = CM144_40*S44+CM244_40*C44
  CM4341_144 = CM144_41*C44-CM244_41*S44
  CM4341_244 = CM144_41*S44+CM244_41*C44
  CM4342_244 = CM144_42*S44+CM244_42*C44
  CM4343_244 = C44*(s.In[5,44]*C44+CM248_43*C47-CM346_43*S45+CM4543_246*C45-CM4743_348*S47+FB144_43*s.l[3,44]+FB146_43*\
   s.dpt[3,47]+FM4743_148*s.dpt[3,48])+S44*(CM4543_146+CM4743_148+s.In[1,44]*S44+s.m[44]*s.l[2,44]*s.l[2,44]*S44+s.m[44]*\
   s.l[3,44]*s.l[3,44]*S44+s.dpt[2,47]*(FB246_43*S45+FB346_43*C45)+s.dpt[2,48]*(FB248_43*S47+FM4743_348*C47)-s.dpt[3,47]*(\
   FB246_43*C45-FB346_43*S45)-s.dpt[3,48]*(FB248_43*C47-FM4743_348*S47))
  FF42_143 = FF344*S43+FF43_144*C43
  FF42_343 = FF344*C43-FF43_144*S43
  CF42_143 = CF344*S43+CF43_144*C43
  CF42_343 = CF344*C43-CF43_144*S43
  FM421_143 = FM344_1*S43+FM431_144*C43
  FM421_343 = FM344_1*C43-FM431_144*S43
  CM421_143 = CM344_1*S43+CM431_144*C43
  CM421_343 = CM344_1*C43-CM431_144*S43
  FM422_143 = FM344_2*S43+FM432_144*C43
  FM422_343 = FM344_2*C43-FM432_144*S43
  CM422_143 = CM344_2*S43+CM432_144*C43
  CM422_343 = CM344_2*C43-CM432_144*S43
  FM423_143 = FM344_3*S43+FM433_144*C43
  FM423_343 = FM344_3*C43-FM433_144*S43
  CM423_143 = CM344_3*S43+CM433_144*C43
  CM423_343 = CM344_3*C43-CM433_144*S43
  FM424_143 = FM344_4*S43+FM434_144*C43
  FM424_343 = FM344_4*C43-FM434_144*S43
  CM424_143 = CM344_4*S43+CM434_144*C43
  CM424_343 = CM344_4*C43-CM434_144*S43
  FM425_143 = FM344_5*S43+FM435_144*C43
  FM425_343 = FM344_5*C43-FM435_144*S43
  CM425_143 = CM344_5*S43+CM435_144*C43
  CM425_343 = CM344_5*C43-CM435_144*S43
  FM426_143 = FM344_6*S43+FM436_144*C43
  FM426_343 = FM344_6*C43-FM436_144*S43
  CM426_143 = CM344_6*S43+CM436_144*C43
  CM426_343 = CM344_6*C43-CM436_144*S43
  CM4240_143 = CM344_40*S43+CM4340_144*C43
  CM4240_343 = CM344_40*C43-CM4340_144*S43
  CM4241_143 = CM344_41*S43+CM4341_144*C43
  CM4242_143 = CM344_42*S43+C43*(CM144_42*C44-CM244_42*S44)
  FA141 = -(s.frc[1,41]-s.m[41]*(AlF141+BeF241*s.l[2,41]))
  FA341 = -(s.frc[3,41]-s.m[41]*(AlF340+BeF841*s.l[2,41]))
  FF141 = FA141+FF42_143
  FF241 = -(s.frc[2,41]-s.m[41]*(AlF241+BS541*s.l[2,41])+FF42_343*S42-FF43_244*C42)
  FF341 = FA341+FF42_343*C42+FF43_244*S42
  CF141 = -(s.trq[1,41]-CF42_143-s.In[1,41]*OpF141-s.In[9,41]*OM241*OM341-FA341*s.l[2,41]-s.dpt[2,44]*(FF42_343*C42+\
   FF43_244*S42))
  CF241 = -(s.trq[2,41]+CF42_343*S42-CF43_244*C42-OM141*OM341*(s.In[1,41]-s.In[9,41]))
  CF341 = -(s.trq[3,41]+s.In[1,41]*OM141*OM241-s.In[9,41]*OpF340-CF42_343*C42-CF43_244*S42+FA141*s.l[2,41]+FF42_143*\
   s.dpt[2,44])
  FB141_1 = s.m[41]*AlM141_1
  FB341_1 = s.m[41]*AlM340_1
  FM141_1 = FB141_1+FM421_143
  FM241_1 = s.m[41]*AlM241_1-FM421_343*S42+FM431_244*C42
  FM341_1 = FB341_1+FM421_343*C42+FM431_244*S42
  CM411_242 = -(CM421_343*S42-CM431_244*C42)
  CM141_1 = CM421_143+FB341_1*s.l[2,41]+s.dpt[2,44]*(FM421_343*C42+FM431_244*S42)
  CM341_1 = CM421_343*C42+CM431_244*S42-FB141_1*s.l[2,41]-FM421_143*s.dpt[2,44]
  FB141_2 = s.m[41]*AlM141_2
  FB341_2 = s.m[41]*AlM340_2
  FM141_2 = FB141_2+FM422_143
  FM241_2 = s.m[41]*AlM241_2-FM422_343*S42+FM432_244*C42
  FM341_2 = FB341_2+FM422_343*C42+FM432_244*S42
  CM412_242 = -(CM422_343*S42-CM432_244*C42)
  CM141_2 = CM422_143+FB341_2*s.l[2,41]+s.dpt[2,44]*(FM422_343*C42+FM432_244*S42)
  CM341_2 = CM422_343*C42+CM432_244*S42-FB141_2*s.l[2,41]-FM422_143*s.dpt[2,44]
  FB141_3 = s.m[41]*AlM141_3
  FB341_3 = s.m[41]*AlM340_3
  FM141_3 = FB141_3+FM423_143
  FM241_3 = s.m[41]*AlM241_3-FM423_343*S42+FM433_244*C42
  FM341_3 = FB341_3+FM423_343*C42+FM433_244*S42
  CM413_242 = -(CM423_343*S42-CM433_244*C42)
  CM141_3 = CM423_143+FB341_3*s.l[2,41]+s.dpt[2,44]*(FM423_343*C42+FM433_244*S42)
  CM341_3 = CM423_343*C42+CM433_244*S42-FB141_3*s.l[2,41]-FM423_143*s.dpt[2,44]
  FB141_4 = s.m[41]*(AlM141_4-OpM340_4*s.l[2,41])
  FB341_4 = s.m[41]*(AlM340_4+OpM141_4*s.l[2,41])
  FM141_4 = FB141_4+FM424_143
  FM241_4 = s.m[41]*AlM241_4-FM424_343*S42+FM434_244*C42
  FM341_4 = FB341_4+FM424_343*C42+FM434_244*S42
  CM414_242 = -(CM424_343*S42-CM434_244*C42)
  CM141_4 = CM424_143+s.In[1,41]*OpM141_4+FB341_4*s.l[2,41]+s.dpt[2,44]*(FM424_343*C42+FM434_244*S42)
  CM341_4 = s.In[9,41]*OpM340_4+CM424_343*C42+CM434_244*S42-FB141_4*s.l[2,41]-FM424_143*s.dpt[2,44]
  FB141_5 = s.m[41]*(AlM141_5+s.l[2,41]*S40p6)
  FB341_5 = s.m[41]*(AlM340_5+OpM141_5*s.l[2,41])
  FM141_5 = FB141_5+FM425_143
  FM241_5 = s.m[41]*AlM241_5-FM425_343*S42+FM435_244*C42
  FM341_5 = FB341_5+FM425_343*C42+FM435_244*S42
  CM415_242 = -(CM425_343*S42-CM435_244*C42)
  CM141_5 = CM425_143+s.In[1,41]*OpM141_5+FB341_5*s.l[2,41]+s.dpt[2,44]*(FM425_343*C42+FM435_244*S42)
  CM341_5 = CM425_343*C42+CM435_244*S42-FM425_143*s.dpt[2,44]-s.In[9,41]*S40p6-FB141_5*s.l[2,41]
  FB141_6 = s.m[41]*AlM141_6
  FB341_6 = s.m[41]*(AlM340_6+s.l[2,41]*C41)
  CM341_6 = CM426_343*C42+CM436_244*S42-FB141_6*s.l[2,41]-FM426_143*s.dpt[2,44]
  CM4140_342 = CM4240_343*C42+CM4340_244*S42-s.dpt[2,44]*(FM344_40*S43+FM4340_144*C43)
  CM341_41 = s.In[9,41]+s.m[41]*s.l[2,41]*s.l[2,41]+CM4341_244*S42-s.dpt[2,44]*(C43*(C44*(FB144_41+FB146_41+FM4741_148)-\
   S44*(FB244_41+FB246_41*C45+FB248_41*C47-FB346_41*S45-FM4741_348*S47))+S43*(FB344_41+FB246_41*S45+FB248_41*S47+FB346_41*C45+\
   FM4741_348*C47))+C42*(CM344_41*C43-CM4341_144*S43)
  FF40_141 = FF141*C41-FF241*S41
  FF40_241 = FF141*S41+FF241*C41
  CF40_141 = CF141*C41-CF241*S41
  CF40_241 = CF141*S41+CF241*C41
  FM401_141 = FM141_1*C41-FM241_1*S41
  FM401_241 = FM141_1*S41+FM241_1*C41
  CM401_141 = CM141_1*C41-CM411_242*S41
  CM401_241 = CM141_1*S41+CM411_242*C41
  FM402_141 = FM141_2*C41-FM241_2*S41
  FM402_241 = FM141_2*S41+FM241_2*C41
  CM402_141 = CM141_2*C41-CM412_242*S41
  CM402_241 = CM141_2*S41+CM412_242*C41
  FM403_141 = FM141_3*C41-FM241_3*S41
  FM403_241 = FM141_3*S41+FM241_3*C41
  CM403_141 = CM141_3*C41-CM413_242*S41
  CM403_241 = CM141_3*S41+CM413_242*C41
  FM404_241 = FM141_4*S41+FM241_4*C41
  CM404_141 = CM141_4*C41-CM414_242*S41
  CM404_241 = CM141_4*S41+CM414_242*C41
  FM405_241 = FM141_5*S41+FM241_5*C41
  CM405_141 = CM141_5*C41-CM415_242*S41
  CM405_241 = CM141_5*S41+CM415_242*C41
  CM406_141 = C41*(CM426_143+s.In[1,41]*C41+FB341_6*s.l[2,41]+s.dpt[2,44]*(FM426_343*C42+FM436_244*S42))+S41*(CM426_343*\
   S42-CM436_244*C42)
  CM4040_141 = C41*(CM4240_143+s.In[1,41]*C41+s.m[41]*s.l[2,41]*s.l[2,41]*C41+s.dpt[2,44]*(C42*(FM344_40*C43-FM4340_144*\
   S43)+S42*(FM144_40*S44+FM244_40*C44)))+S41*(CM4240_343*S42-CM4340_244*C42)

# = = Block_0_2_0_2_0_18 = = 
 
# Backward Dynamics 

  FF149 = -(s.frc[1,49]-s.m[49]*AlF149-FA151*C50-FA153*C52+FF50_251*S50+FF52_253*S52)
  FF249 = -(s.frc[2,49]-s.m[49]*AlF249-FA151*S50-FA153*S52-FF50_251*C50-FF52_253*C52)
  FF349 = -(s.frc[3,49]-FF50_351-FF52_353-s.m[49]*AlF349)
  FM149_1 = s.m[49]*AlM15_1+FB151_1*C50+FB153_1*C52-FM501_251*S50-FM521_253*S52
  FM249_1 = s.m[49]*AlM26_1+FB151_1*S50+FB153_1*S52+FM501_251*C50+FM521_253*C52
  FM349_1 = FM501_351+FM521_353+s.m[49]*AlM36_1
  FM149_2 = s.m[49]*AlM15_2+FB151_2*C50+FB153_2*C52-FM502_251*S50-FM522_253*S52
  FM249_2 = s.m[49]*AlM26_2+FB151_2*S50+FB153_2*S52+FM502_251*C50+FM522_253*C52
  FM349_2 = FM502_351+FM522_353+s.m[49]*AlM36_2
  FM149_3 = FB153_3*C52-FM523_253*S52-s.m[49]*S5+FB151_3*C50-FM503_251*S50
  FM249_3 = s.m[49]*AlM26_3+FB151_3*S50+FB153_3*S52+FM503_251*C50+FM523_253*C52
  FM349_3 = FM503_351+FM523_353+s.m[49]*AlM36_3
  FM249_4 = s.m[49]*AlM249_4+FB151_4*S50+FB153_4*S52+FM504_251*C50+FM524_253*C52
  FM349_4 = FM504_351+FM524_353+s.m[49]*AlM349_4
  FM249_5 = s.m[49]*AlM249_5+FB151_5*S50+FB153_5*S52+FM505_251*C50+FM525_253*C52
  FM349_5 = FM505_351+FM525_353+s.m[49]*AlM349_5
  FM249_6 = FB151_6*S50+FB153_6*S52+C50*(FB251_6*C51-FB351_6*S51)+C52*(FB253_6*C53-FB353_6*S53)
  FM249_49 = s.m[49]+s.m[51]+s.m[53]

# = = Block_0_2_0_2_0_21 = = 
 
# Backward Dynamics 

  FA154 = -(s.frc[1,54]-s.m[54]*(AlF154+BS154*s.l[1,54]+BeF254*s.l[2,54]))
  FA254 = -(s.frc[2,54]-s.m[54]*(AlF254+BS554*s.l[2,54]+BeF454*s.l[1,54]))
  FA354 = -(s.frc[3,54]-s.m[54]*(AlF354+BeF754*s.l[1,54]+BeF854*s.l[2,54]))
  FF154 = FA154+FA159*C58+FF155*C55+FF355*S55+FF58_359*S58
  FF254 = FA254+FA255+FF56_257+FF58_259
  FF354 = FA354-FA159*S58-FF155*S55+FF355*C55+FF58_359*C58
  CF154 = -(s.trq[1,54]+s.In[5,54]*OM254*OM354-CF155*C55-CF159*C58-CF355*S55-CF58_359*S58-FA354*s.l[2,54]+s.dpt[2,56]*(\
   FA159*S58-FF58_359*C58))
  CF254 = -(s.trq[2,54]-CF255-CF58_259-s.In[5,54]*OpF26+FA354*s.l[1,54]-s.dpt[1,56]*(FA159*S58-FF58_359*C58))
  CF354 = -(s.trq[3,54]-s.In[5,54]*OM154*OM254+CF155*S55+CF159*S58-CF355*C55-CF58_359*C58+FA154*s.l[2,54]-FA254*\
   s.l[1,54]-FF58_259*s.dpt[1,56]+s.dpt[2,56]*(FA159*C58+FF58_359*S58))
  FB154_1 = s.m[54]*AlM154_1
  FB254_1 = s.m[54]*AlM26_1
  FB354_1 = s.m[54]*AlM354_1
  FM154_1 = FB154_1+FB159_1*C58+FM155_1*C55+FM355_1*S55+FM581_359*S58
  FM254_1 = FB254_1+FB255_1+FM561_257+FM581_259
  FM354_1 = FB354_1-FB159_1*S58-FM155_1*S55+FM355_1*C55+FM581_359*C58
  CM154_1 = CM155_1*C55+CM159_1*C58+CM355_1*S55+CM581_359*S58+FB354_1*s.l[2,54]-s.dpt[2,56]*(FB159_1*S58-FM581_359*C58)
  CM254_1 = CM255_1+CM581_259-FB354_1*s.l[1,54]+s.dpt[1,56]*(FB159_1*S58-FM581_359*C58)
  CM354_1 = -(CM155_1*S55+CM159_1*S58-CM355_1*C55-CM581_359*C58+FB154_1*s.l[2,54]-FB254_1*s.l[1,54]-FM581_259*\
   s.dpt[1,56]+s.dpt[2,56]*(FB159_1*C58+FM581_359*S58))
  FB154_2 = s.m[54]*AlM154_2
  FB254_2 = s.m[54]*AlM26_2
  FB354_2 = s.m[54]*AlM354_2
  FM154_2 = FB154_2+FB159_2*C58+FM155_2*C55+FM355_2*S55+FM582_359*S58
  FM254_2 = FB254_2+FB255_2+FM562_257+FM582_259
  FM354_2 = FB354_2-FB159_2*S58-FM155_2*S55+FM355_2*C55+FM582_359*C58
  CM154_2 = CM155_2*C55+CM159_2*C58+CM355_2*S55+CM582_359*S58+FB354_2*s.l[2,54]-s.dpt[2,56]*(FB159_2*S58-FM582_359*C58)
  CM254_2 = CM255_2+CM582_259-FB354_2*s.l[1,54]+s.dpt[1,56]*(FB159_2*S58-FM582_359*C58)
  CM354_2 = -(CM155_2*S55+CM159_2*S58-CM355_2*C55-CM582_359*C58+FB154_2*s.l[2,54]-FB254_2*s.l[1,54]-FM582_259*\
   s.dpt[1,56]+s.dpt[2,56]*(FB159_2*C58+FM582_359*S58))
  FB154_3 = s.m[54]*AlM154_3
  FB254_3 = s.m[54]*AlM26_3
  FB354_3 = s.m[54]*AlM354_3
  FM154_3 = FB154_3+FB159_3*C58+FM155_3*C55+FM355_3*S55+FM583_359*S58
  FM254_3 = FB254_3+FB255_3+FM563_257+FM583_259
  FM354_3 = FB354_3-FB159_3*S58-FM155_3*S55+FM355_3*C55+FM583_359*C58
  CM154_3 = CM155_3*C55+CM159_3*C58+CM355_3*S55+CM583_359*S58+FB354_3*s.l[2,54]-s.dpt[2,56]*(FB159_3*S58-FM583_359*C58)
  CM254_3 = CM255_3+CM583_259-FB354_3*s.l[1,54]+s.dpt[1,56]*(FB159_3*S58-FM583_359*C58)
  CM354_3 = -(CM155_3*S55+CM159_3*S58-CM355_3*C55-CM583_359*C58+FB154_3*s.l[2,54]-FB254_3*s.l[1,54]-FM583_259*\
   s.dpt[1,56]+s.dpt[2,56]*(FB159_3*C58+FM583_359*S58))
  FB154_4 = s.m[54]*(AlM154_4-OpM354_4*s.l[2,54])
  FB254_4 = s.m[54]*(AlM254_4+OpM354_4*s.l[1,54])
  FB354_4 = s.m[54]*(AlM354_4+OpM154_4*s.l[2,54]-OpM26_4*s.l[1,54])
  FM154_4 = FB154_4+FB159_4*C58+FM155_4*C55+FM355_4*S55+FM584_359*S58
  FM254_4 = FB254_4+FB255_4+FM564_257+FM584_259
  FM354_4 = FB354_4-FB159_4*S58-FM155_4*S55+FM355_4*C55+FM584_359*C58
  CM154_4 = CM155_4*C55+CM159_4*C58+CM355_4*S55+CM584_359*S58+FB354_4*s.l[2,54]-s.dpt[2,56]*(FB159_4*S58-FM584_359*C58)
  CM254_4 = CM255_4+CM584_259+s.In[5,54]*OpM26_4-FB354_4*s.l[1,54]+s.dpt[1,56]*(FB159_4*S58-FM584_359*C58)
  CM354_4 = -(CM155_4*S55+CM159_4*S58-CM355_4*C55-CM584_359*C58+FB154_4*s.l[2,54]-FB254_4*s.l[1,54]-FM584_259*\
   s.dpt[1,56]+s.dpt[2,56]*(FB159_4*C58+FM584_359*S58))
  FB154_5 = s.m[54]*(AlM154_5-OpM354_5*s.l[2,54])
  FB254_5 = s.m[54]*(AlM254_5+OpM354_5*s.l[1,54])
  FB354_5 = s.m[54]*(AlM354_5+OpM154_5*s.l[2,54]-s.l[1,54]*C6)
  FM154_5 = FB154_5+FB159_5*C58+FM155_5*C55+FM355_5*S55+FM585_359*S58
  FM254_5 = FB254_5+FB255_5+FM565_257+FM585_259
  FM354_5 = FB354_5-FB159_5*S58-FM155_5*S55+FM355_5*C55+FM585_359*C58
  CM154_5 = CM155_5*C55+CM159_5*C58+CM355_5*S55+CM585_359*S58+FB354_5*s.l[2,54]-s.dpt[2,56]*(FB159_5*S58-FM585_359*C58)
  CM254_5 = CM255_5+CM585_259+s.In[5,54]*C6-FB354_5*s.l[1,54]+s.dpt[1,56]*(FB159_5*S58-FM585_359*C58)
  CM354_5 = -(CM155_5*S55+CM159_5*S58-CM355_5*C55-CM585_359*C58+FB154_5*s.l[2,54]-FB254_5*s.l[1,54]-FM585_259*\
   s.dpt[1,56]+s.dpt[2,56]*(FB159_5*C58+FM585_359*S58))
  FB254_6 = -s.m[54]*(s.dpt[3,14]-s.l[1,54]*S54)
  FB354_6 = s.m[54]*s.l[2,54]*C54
  CM254_6 = CM255_6+CM586_259-FB354_6*s.l[1,54]+s.dpt[1,56]*(FB159_6*S58-FM586_359*C58)
  CM254_54 = s.In[5,54]+CM255_54+CM5854_259+s.m[54]*s.l[1,54]*s.l[1,54]-s.dpt[1,56]*(s.m[59]*AlM358_54*C58-FB159_54*S58)

# = = Block_0_2_0_2_0_24 = = 
 
# Backward Dynamics 

  FA160 = -(s.frc[1,60]-s.m[60]*(AlF160+BS160*s.l[1,60]+BeF260*s.l[2,60]))
  FA260 = -(s.frc[2,60]-s.m[60]*(AlF260+BS560*s.l[2,60]+BeF460*s.l[1,60]))
  FA360 = -(s.frc[3,60]-s.m[60]*(AlF360+BeF760*s.l[1,60]+BeF860*s.l[2,60]))
  FF160 = FA160+FA165*C64+FF161*C61+FF361*S61+FF64_365*S64
  FF260 = FA260+FA261+FF62_263+FF64_265
  FF360 = FA360-FA165*S64-FF161*S61+FF361*C61+FF64_365*C64
  CF160 = -(s.trq[1,60]+s.In[5,60]*OM260*OM360-CF161*C61-CF165*C64-CF361*S61-CF64_365*S64-FA360*s.l[2,60]+s.dpt[2,60]*(\
   FA165*S64-FF64_365*C64))
  CF260 = -(s.trq[2,60]-CF261-CF64_265-s.In[5,60]*OpF26+FA360*s.l[1,60]-s.dpt[1,60]*(FA165*S64-FF64_365*C64))
  CF360 = -(s.trq[3,60]-s.In[5,60]*OM160*OM260+CF161*S61+CF165*S64-CF361*C61-CF64_365*C64+FA160*s.l[2,60]-FA260*\
   s.l[1,60]-FF64_265*s.dpt[1,60]+s.dpt[2,60]*(FA165*C64+FF64_365*S64))
  FB160_1 = s.m[60]*AlM160_1
  FB260_1 = s.m[60]*AlM26_1
  FB360_1 = s.m[60]*AlM360_1
  FM160_1 = FB160_1+FB165_1*C64+FM161_1*C61+FM361_1*S61+FM641_365*S64
  FM260_1 = FB260_1+FB261_1+FM621_263+FM641_265
  FM360_1 = FB360_1-FB165_1*S64-FM161_1*S61+FM361_1*C61+FM641_365*C64
  CM160_1 = CM161_1*C61+CM165_1*C64+CM361_1*S61+CM641_365*S64+FB360_1*s.l[2,60]-s.dpt[2,60]*(FB165_1*S64-FM641_365*C64)
  CM260_1 = CM261_1+CM641_265-FB360_1*s.l[1,60]+s.dpt[1,60]*(FB165_1*S64-FM641_365*C64)
  CM360_1 = -(CM161_1*S61+CM165_1*S64-CM361_1*C61-CM641_365*C64+FB160_1*s.l[2,60]-FB260_1*s.l[1,60]-FM641_265*\
   s.dpt[1,60]+s.dpt[2,60]*(FB165_1*C64+FM641_365*S64))
  FB160_2 = s.m[60]*AlM160_2
  FB260_2 = s.m[60]*AlM26_2
  FB360_2 = s.m[60]*AlM360_2
  FM160_2 = FB160_2+FB165_2*C64+FM161_2*C61+FM361_2*S61+FM642_365*S64
  FM260_2 = FB260_2+FB261_2+FM622_263+FM642_265
  FM360_2 = FB360_2-FB165_2*S64-FM161_2*S61+FM361_2*C61+FM642_365*C64
  CM160_2 = CM161_2*C61+CM165_2*C64+CM361_2*S61+CM642_365*S64+FB360_2*s.l[2,60]-s.dpt[2,60]*(FB165_2*S64-FM642_365*C64)
  CM260_2 = CM261_2+CM642_265-FB360_2*s.l[1,60]+s.dpt[1,60]*(FB165_2*S64-FM642_365*C64)
  CM360_2 = -(CM161_2*S61+CM165_2*S64-CM361_2*C61-CM642_365*C64+FB160_2*s.l[2,60]-FB260_2*s.l[1,60]-FM642_265*\
   s.dpt[1,60]+s.dpt[2,60]*(FB165_2*C64+FM642_365*S64))
  FB160_3 = s.m[60]*AlM160_3
  FB260_3 = s.m[60]*AlM26_3
  FB360_3 = s.m[60]*AlM360_3
  FM160_3 = FB160_3+FB165_3*C64+FM161_3*C61+FM361_3*S61+FM643_365*S64
  FM260_3 = FB260_3+FB261_3+FM623_263+FM643_265
  FM360_3 = FB360_3-FB165_3*S64-FM161_3*S61+FM361_3*C61+FM643_365*C64
  CM160_3 = CM161_3*C61+CM165_3*C64+CM361_3*S61+CM643_365*S64+FB360_3*s.l[2,60]-s.dpt[2,60]*(FB165_3*S64-FM643_365*C64)
  CM260_3 = CM261_3+CM643_265-FB360_3*s.l[1,60]+s.dpt[1,60]*(FB165_3*S64-FM643_365*C64)
  CM360_3 = -(CM161_3*S61+CM165_3*S64-CM361_3*C61-CM643_365*C64+FB160_3*s.l[2,60]-FB260_3*s.l[1,60]-FM643_265*\
   s.dpt[1,60]+s.dpt[2,60]*(FB165_3*C64+FM643_365*S64))
  FB160_4 = s.m[60]*(AlM160_4-OpM360_4*s.l[2,60])
  FB260_4 = s.m[60]*(AlM260_4+OpM360_4*s.l[1,60])
  FB360_4 = s.m[60]*(AlM360_4+OpM160_4*s.l[2,60]-OpM26_4*s.l[1,60])
  FM160_4 = FB160_4+FB165_4*C64+FM161_4*C61+FM361_4*S61+FM644_365*S64
  FM260_4 = FB260_4+FB261_4+FM624_263+FM644_265
  FM360_4 = FB360_4-FB165_4*S64-FM161_4*S61+FM361_4*C61+FM644_365*C64
  CM160_4 = CM161_4*C61+CM165_4*C64+CM361_4*S61+CM644_365*S64+FB360_4*s.l[2,60]-s.dpt[2,60]*(FB165_4*S64-FM644_365*C64)
  CM260_4 = CM261_4+CM644_265+s.In[5,60]*OpM26_4-FB360_4*s.l[1,60]+s.dpt[1,60]*(FB165_4*S64-FM644_365*C64)
  CM360_4 = -(CM161_4*S61+CM165_4*S64-CM361_4*C61-CM644_365*C64+FB160_4*s.l[2,60]-FB260_4*s.l[1,60]-FM644_265*\
   s.dpt[1,60]+s.dpt[2,60]*(FB165_4*C64+FM644_365*S64))
  FB160_5 = s.m[60]*(AlM160_5-OpM360_5*s.l[2,60])
  FB260_5 = s.m[60]*(AlM260_5+OpM360_5*s.l[1,60])
  FB360_5 = s.m[60]*(AlM360_5+OpM160_5*s.l[2,60]-s.l[1,60]*C6)
  FM160_5 = FB160_5+FB165_5*C64+FM161_5*C61+FM361_5*S61+FM645_365*S64
  FM260_5 = FB260_5+FB261_5+FM625_263+FM645_265
  FM360_5 = FB360_5-FB165_5*S64-FM161_5*S61+FM361_5*C61+FM645_365*C64
  CM160_5 = CM161_5*C61+CM165_5*C64+CM361_5*S61+CM645_365*S64+FB360_5*s.l[2,60]-s.dpt[2,60]*(FB165_5*S64-FM645_365*C64)
  CM260_5 = CM261_5+CM645_265+s.In[5,60]*C6-FB360_5*s.l[1,60]+s.dpt[1,60]*(FB165_5*S64-FM645_365*C64)
  CM360_5 = -(CM161_5*S61+CM165_5*S64-CM361_5*C61-CM645_365*C64+FB160_5*s.l[2,60]-FB260_5*s.l[1,60]-FM645_265*\
   s.dpt[1,60]+s.dpt[2,60]*(FB165_5*C64+FM645_365*S64))
  FB260_6 = -s.m[60]*(s.dpt[3,15]-s.l[1,60]*S60)
  FB360_6 = s.m[60]*s.l[2,60]*C60
  CM260_6 = CM261_6+CM646_265-FB360_6*s.l[1,60]+s.dpt[1,60]*(FB165_6*S64-FM646_365*C64)
  CM260_60 = s.In[5,60]+CM261_60+CM6460_265+s.m[60]*s.l[1,60]*s.l[1,60]-s.dpt[1,60]*(s.m[65]*AlM364_60*C64-FB165_60*S64)

# = = Block_0_2_0_3_0_1 = = 
 
# Backward Dynamics 

  FA16 = -(s.frc[1,6]-s.m[6]*(AlF15+BeF36*s.l[3,6]))
  FA26 = -(s.frc[2,6]-s.m[6]*(AlF26+BeF66*s.l[3,6]))
  FF16 = FA16+FF115+FF149+FF17+FF23_124+FF25_126+FF27_128+FF29_130+FF38_139+FF40_141+FF154*C54+FF160*C60+FF354*S54+FF360\
   *S60
  FF26 = FA26+FF249+FF254+FF260-FA324*S23-FA326*S25-FA328*S27-FA339*S38+FF215*C15+FF23_224*C23+FF25_226*C25+FF27*C7+\
   FF27_228*C27+FF29_230*C29-FF315*S15-FF330*S29-FF341*S40-FF37*S7+FF38_239*C38+FF40_241*C40
  FF36 = -(s.frc[3,6]-FF349-s.m[6]*(AlF36+BS96*s.l[3,6])-FA324*C23-FA326*C25-FA328*C27-FA339*C38+FF154*S54+FF160*S60-\
   FF215*S15-FF23_224*S23-FF25_226*S25-FF27*S7-FF27_228*S27-FF29_230*S29-FF315*C15-FF330*C29-FF341*C40-FF354*C54-FF360*C60-FF37\
   *C7-FF38_239*S38-FF40_241*S40)
  CF16 = -(s.trq[1,49]+s.trq[1,6]-CF115-CF17-CF23_124-CF25_126-CF27_128-CF29_130-CF38_139-CF40_141-q[49]*FF349-s.In[1,6]\
   *OpF15-CF151*C50-CF153*C52-CF154*C54-CF160*C60-CF354*S54-CF360*S60+CF50_251*S50+CF52_253*S52+FA26*s.l[3,6]+FF254*s.dpt[3,14]\
   +FF260*s.dpt[3,15]-FF50_351*s.dpt[2,52]-FF52_353*s.dpt[2,53]+OM26*OM36*(s.In[5,6]-s.In[9,6])-s.dpt[2,10]*(FF29_230*S29+FF330\
   *C29)-s.dpt[2,11]*(FA339*C38+FF38_239*S38)-s.dpt[2,12]*(FF341*C40+FF40_241*S40)-s.dpt[2,1]*(FF27*S7+FF37*C7)-s.dpt[2,4]*(\
   FF215*S15+FF315*C15)-s.dpt[2,6]*(FA324*C23+FF23_224*S23)-s.dpt[2,8]*(FA326*C25+FF25_226*S25)-s.dpt[2,9]*(FA328*C27+FF27_228*\
   S27)-s.dpt[3,11]*(FA339*S38-FF38_239*C38)-s.dpt[3,6]*(FA324*S23-FF23_224*C23)-s.dpt[3,8]*(FA326*S25-FF25_226*C25)-s.dpt[3,9]\
   *(FA328*S27-FF27_228*C27))
  CF26 = -(s.trq[2,49]+s.trq[2,6]-CF254-CF260-s.In[5,6]*OpF26-CF151*S50-CF153*S52-CF215*C15-CF23_224*C23-CF25_226*C25-\
   CF27*C7-CF27_228*C27-CF29_230*C29+CF315*S15+CF324*S23+CF326*S25+CF328*S27+CF330*S29+CF339*S38+CF341*S40+CF37*S7-CF38_239*C38\
   -CF40_241*C40-CF50_251*C50-CF52_253*C52-FA16*s.l[3,6]-FF23_124*s.dpt[3,6]-FF25_126*s.dpt[3,8]-FF27_128*s.dpt[3,9]+FF349*\
   s.dpt[1,13]-FF38_139*s.dpt[3,11]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,10]*(FF29_230*S29+FF330*C29)+s.dpt[1,11]*(FA339*C38\
   +FF38_239*S38)+s.dpt[1,12]*(FF341*C40+FF40_241*S40)-s.dpt[1,14]*(FF154*S54-FF354*C54)-s.dpt[1,15]*(FF160*S60-FF360*C60)+\
   s.dpt[1,1]*(FF27*S7+FF37*C7)+s.dpt[1,4]*(FF215*S15+FF315*C15)+s.dpt[1,6]*(FA324*C23+FF23_224*S23)+s.dpt[1,8]*(FA326*C25+\
   FF25_226*S25)+s.dpt[1,9]*(FA328*C27+FF27_228*S27)-s.dpt[3,14]*(FF154*C54+FF354*S54)-s.dpt[3,15]*(FF160*C60+FF360*S60))
  CF36 = -(s.trq[3,49]+s.trq[3,6]-CF50_351-CF52_353+q[49]*FF149-s.In[9,6]*OpF36+CF154*S54+CF160*S60-CF215*S15-CF23_224*\
   S23-CF25_226*S25-CF27*S7-CF27_228*S27-CF29_230*S29-CF315*C15-CF324*C23-CF326*C25-CF328*C27-CF330*C29-CF339*C38-CF341*C40-\
   CF354*C54-CF360*C60-CF37*C7-CF38_239*S38-CF40_241*S40+FF115*s.dpt[2,4]+FF17*s.dpt[2,1]+FF23_124*s.dpt[2,6]-FF249*s.dpt[1,13]\
   -FF254*s.dpt[1,14]+FF25_126*s.dpt[2,8]-FF260*s.dpt[1,15]+FF27_128*s.dpt[2,9]+FF29_130*s.dpt[2,10]+FF38_139*s.dpt[2,11]+\
   FF40_141*s.dpt[2,12]+OM16*OM26*(s.In[1,6]-s.In[5,6])-s.dpt[1,10]*(FF29_230*C29-FF330*S29)+s.dpt[1,11]*(FA339*S38-FF38_239*\
   C38)+s.dpt[1,12]*(FF341*S40-FF40_241*C40)-s.dpt[1,1]*(FF27*C7-FF37*S7)-s.dpt[1,4]*(FF215*C15-FF315*S15)+s.dpt[1,6]*(FA324*\
   S23-FF23_224*C23)+s.dpt[1,8]*(FA326*S25-FF25_226*C25)+s.dpt[1,9]*(FA328*S27-FF27_228*C27)+s.dpt[2,52]*(FA151*C50-FF50_251*\
   S50)+s.dpt[2,53]*(FA153*C52-FF52_253*S52))
  FB16_1 = s.m[6]*AlM15_1
  FB26_1 = s.m[6]*AlM26_1
  FM16_1 = FB16_1+FM115_1+FM149_1+FM17_1+FM231_124+FM251_126+FM271_128+FM291_130+FM381_139+FM401_141+FM154_1*C54+FM160_1\
   *C60+FM354_1*S54+FM360_1*S60
  FM26_1 = FB26_1+FM249_1+FM254_1+FM260_1-FB324_1*S23-FB326_1*S25-FB328_1*S27-FB339_1*S38+FM215_1*C15+FM231_224*C23+\
   FM251_226*C25+FM271_228*C27+FM27_1*C7+FM291_230*C29-FM315_1*S15-FM330_1*S29-FM341_1*S40-FM37_1*S7+FM381_239*C38+FM401_241*\
   C40
  FM36_1 = FM349_1+s.m[6]*AlM36_1+FB324_1*C23+FB326_1*C25+FB328_1*C27+FB339_1*C38-FM154_1*S54-FM160_1*S60+FM215_1*S15+\
   FM231_224*S23+FM251_226*S25+FM271_228*S27+FM27_1*S7+FM291_230*S29+FM315_1*C15+FM330_1*C29+FM341_1*C40+FM354_1*C54+FM360_1*\
   C60+FM37_1*C7+FM381_239*S38+FM401_241*S40
  CM16_1 = CM115_1+CM17_1+CM231_124+CM251_126+CM271_128+CM291_130+CM381_139+CM401_141+q[49]*FM349_1+CM151_1*C50+CM153_1*\
   C52+CM154_1*C54+CM160_1*C60+CM354_1*S54+CM360_1*S60-CM501_251*S50-CM521_253*S52-FB26_1*s.l[3,6]-FM254_1*s.dpt[3,14]-FM260_1*\
   s.dpt[3,15]+FM501_351*s.dpt[2,52]+FM521_353*s.dpt[2,53]+s.dpt[2,10]*(FM291_230*S29+FM330_1*C29)+s.dpt[2,11]*(FB339_1*C38+\
   FM381_239*S38)+s.dpt[2,12]*(FM341_1*C40+FM401_241*S40)+s.dpt[2,1]*(FM27_1*S7+FM37_1*C7)+s.dpt[2,4]*(FM215_1*S15+FM315_1*C15)\
   +s.dpt[2,6]*(FB324_1*C23+FM231_224*S23)+s.dpt[2,8]*(FB326_1*C25+FM251_226*S25)+s.dpt[2,9]*(FB328_1*C27+FM271_228*S27)+\
   s.dpt[3,11]*(FB339_1*S38-FM381_239*C38)+s.dpt[3,6]*(FB324_1*S23-FM231_224*C23)+s.dpt[3,8]*(FB326_1*S25-FM251_226*C25)+\
   s.dpt[3,9]*(FB328_1*S27-FM271_228*C27)
  CM26_1 = CM254_1+CM260_1+CM151_1*S50+CM153_1*S52+CM215_1*C15+CM231_224*C23+CM251_226*C25+CM271_228*C27+CM27_1*C7+\
   CM291_230*C29-CM315_1*S15-CM324_1*S23-CM326_1*S25-CM328_1*S27-CM330_1*S29-CM339_1*S38-CM341_1*S40-CM37_1*S7+CM381_239*C38+\
   CM401_241*C40+CM501_251*C50+CM521_253*C52+FB16_1*s.l[3,6]+FM231_124*s.dpt[3,6]+FM251_126*s.dpt[3,8]+FM271_128*s.dpt[3,9]-\
   FM349_1*s.dpt[1,13]+FM381_139*s.dpt[3,11]-s.dpt[1,10]*(FM291_230*S29+FM330_1*C29)-s.dpt[1,11]*(FB339_1*C38+FM381_239*S38)-\
   s.dpt[1,12]*(FM341_1*C40+FM401_241*S40)+s.dpt[1,14]*(FM154_1*S54-FM354_1*C54)+s.dpt[1,15]*(FM160_1*S60-FM360_1*C60)-\
   s.dpt[1,1]*(FM27_1*S7+FM37_1*C7)-s.dpt[1,4]*(FM215_1*S15+FM315_1*C15)-s.dpt[1,6]*(FB324_1*C23+FM231_224*S23)-s.dpt[1,8]*(\
   FB326_1*C25+FM251_226*S25)-s.dpt[1,9]*(FB328_1*C27+FM271_228*S27)+s.dpt[3,14]*(FM154_1*C54+FM354_1*S54)+s.dpt[3,15]*(FM160_1\
   *C60+FM360_1*S60)
  CM36_1 = CM501_351+CM521_353-q[49]*FM149_1-CM154_1*S54-CM160_1*S60+CM215_1*S15+CM231_224*S23+CM251_226*S25+CM271_228*\
   S27+CM27_1*S7+CM291_230*S29+CM315_1*C15+CM324_1*C23+CM326_1*C25+CM328_1*C27+CM330_1*C29+CM339_1*C38+CM341_1*C40+CM354_1*C54+\
   CM360_1*C60+CM37_1*C7+CM381_239*S38+CM401_241*S40-FM115_1*s.dpt[2,4]-FM17_1*s.dpt[2,1]-FM231_124*s.dpt[2,6]+FM249_1*\
   s.dpt[1,13]-FM251_126*s.dpt[2,8]+FM254_1*s.dpt[1,14]+FM260_1*s.dpt[1,15]-FM271_128*s.dpt[2,9]-FM291_130*s.dpt[2,10]-\
   FM381_139*s.dpt[2,11]-FM401_141*s.dpt[2,12]+s.dpt[1,10]*(FM291_230*C29-FM330_1*S29)-s.dpt[1,11]*(FB339_1*S38-FM381_239*C38)-\
   s.dpt[1,12]*(FM341_1*S40-FM401_241*C40)+s.dpt[1,1]*(FM27_1*C7-FM37_1*S7)+s.dpt[1,4]*(FM215_1*C15-FM315_1*S15)-s.dpt[1,6]*(\
   FB324_1*S23-FM231_224*C23)-s.dpt[1,8]*(FB326_1*S25-FM251_226*C25)-s.dpt[1,9]*(FB328_1*S27-FM271_228*C27)-s.dpt[2,52]*(\
   FB151_1*C50-FM501_251*S50)-s.dpt[2,53]*(FB153_1*C52-FM521_253*S52)
  FB16_2 = s.m[6]*AlM15_2
  FB26_2 = s.m[6]*AlM26_2
  FM16_2 = FB16_2+FM115_2+FM149_2+FM17_2+FM232_124+FM252_126+FM272_128+FM292_130+FM382_139+FM402_141+FM154_2*C54+FM160_2\
   *C60+FM354_2*S54+FM360_2*S60
  FM26_2 = FB26_2+FM249_2+FM254_2+FM260_2-FB324_2*S23-FB326_2*S25-FB328_2*S27-FB339_2*S38+FM215_2*C15+FM232_224*C23+\
   FM252_226*C25+FM272_228*C27+FM27_2*C7+FM292_230*C29-FM315_2*S15-FM330_2*S29-FM341_2*S40-FM37_2*S7+FM382_239*C38+FM402_241*\
   C40
  FM36_2 = FM349_2+s.m[6]*AlM36_2+FB324_2*C23+FB326_2*C25+FB328_2*C27+FB339_2*C38-FM154_2*S54-FM160_2*S60+FM215_2*S15+\
   FM232_224*S23+FM252_226*S25+FM272_228*S27+FM27_2*S7+FM292_230*S29+FM315_2*C15+FM330_2*C29+FM341_2*C40+FM354_2*C54+FM360_2*\
   C60+FM37_2*C7+FM382_239*S38+FM402_241*S40
  CM16_2 = CM115_2+CM17_2+CM232_124+CM252_126+CM272_128+CM292_130+CM382_139+CM402_141+q[49]*FM349_2+CM151_2*C50+CM153_2*\
   C52+CM154_2*C54+CM160_2*C60+CM354_2*S54+CM360_2*S60-CM502_251*S50-CM522_253*S52-FB26_2*s.l[3,6]-FM254_2*s.dpt[3,14]-FM260_2*\
   s.dpt[3,15]+FM502_351*s.dpt[2,52]+FM522_353*s.dpt[2,53]+s.dpt[2,10]*(FM292_230*S29+FM330_2*C29)+s.dpt[2,11]*(FB339_2*C38+\
   FM382_239*S38)+s.dpt[2,12]*(FM341_2*C40+FM402_241*S40)+s.dpt[2,1]*(FM27_2*S7+FM37_2*C7)+s.dpt[2,4]*(FM215_2*S15+FM315_2*C15)\
   +s.dpt[2,6]*(FB324_2*C23+FM232_224*S23)+s.dpt[2,8]*(FB326_2*C25+FM252_226*S25)+s.dpt[2,9]*(FB328_2*C27+FM272_228*S27)+\
   s.dpt[3,11]*(FB339_2*S38-FM382_239*C38)+s.dpt[3,6]*(FB324_2*S23-FM232_224*C23)+s.dpt[3,8]*(FB326_2*S25-FM252_226*C25)+\
   s.dpt[3,9]*(FB328_2*S27-FM272_228*C27)
  CM26_2 = CM254_2+CM260_2+CM151_2*S50+CM153_2*S52+CM215_2*C15+CM232_224*C23+CM252_226*C25+CM272_228*C27+CM27_2*C7+\
   CM292_230*C29-CM315_2*S15-CM324_2*S23-CM326_2*S25-CM328_2*S27-CM330_2*S29-CM339_2*S38-CM341_2*S40-CM37_2*S7+CM382_239*C38+\
   CM402_241*C40+CM502_251*C50+CM522_253*C52+FB16_2*s.l[3,6]+FM232_124*s.dpt[3,6]+FM252_126*s.dpt[3,8]+FM272_128*s.dpt[3,9]-\
   FM349_2*s.dpt[1,13]+FM382_139*s.dpt[3,11]-s.dpt[1,10]*(FM292_230*S29+FM330_2*C29)-s.dpt[1,11]*(FB339_2*C38+FM382_239*S38)-\
   s.dpt[1,12]*(FM341_2*C40+FM402_241*S40)+s.dpt[1,14]*(FM154_2*S54-FM354_2*C54)+s.dpt[1,15]*(FM160_2*S60-FM360_2*C60)-\
   s.dpt[1,1]*(FM27_2*S7+FM37_2*C7)-s.dpt[1,4]*(FM215_2*S15+FM315_2*C15)-s.dpt[1,6]*(FB324_2*C23+FM232_224*S23)-s.dpt[1,8]*(\
   FB326_2*C25+FM252_226*S25)-s.dpt[1,9]*(FB328_2*C27+FM272_228*S27)+s.dpt[3,14]*(FM154_2*C54+FM354_2*S54)+s.dpt[3,15]*(FM160_2\
   *C60+FM360_2*S60)
  CM36_2 = CM502_351+CM522_353-q[49]*FM149_2-CM154_2*S54-CM160_2*S60+CM215_2*S15+CM232_224*S23+CM252_226*S25+CM272_228*\
   S27+CM27_2*S7+CM292_230*S29+CM315_2*C15+CM324_2*C23+CM326_2*C25+CM328_2*C27+CM330_2*C29+CM339_2*C38+CM341_2*C40+CM354_2*C54+\
   CM360_2*C60+CM37_2*C7+CM382_239*S38+CM402_241*S40-FM115_2*s.dpt[2,4]-FM17_2*s.dpt[2,1]-FM232_124*s.dpt[2,6]+FM249_2*\
   s.dpt[1,13]-FM252_126*s.dpt[2,8]+FM254_2*s.dpt[1,14]+FM260_2*s.dpt[1,15]-FM272_128*s.dpt[2,9]-FM292_130*s.dpt[2,10]-\
   FM382_139*s.dpt[2,11]-FM402_141*s.dpt[2,12]+s.dpt[1,10]*(FM292_230*C29-FM330_2*S29)-s.dpt[1,11]*(FB339_2*S38-FM382_239*C38)-\
   s.dpt[1,12]*(FM341_2*S40-FM402_241*C40)+s.dpt[1,1]*(FM27_2*C7-FM37_2*S7)+s.dpt[1,4]*(FM215_2*C15-FM315_2*S15)-s.dpt[1,6]*(\
   FB324_2*S23-FM232_224*C23)-s.dpt[1,8]*(FB326_2*S25-FM252_226*C25)-s.dpt[1,9]*(FB328_2*S27-FM272_228*C27)-s.dpt[2,52]*(\
   FB151_2*C50-FM502_251*S50)-s.dpt[2,53]*(FB153_2*C52-FM522_253*S52)
  FB16_3 = -s.m[6]*S5
  FB26_3 = s.m[6]*AlM26_3
  CM16_3 = CM115_3+CM17_3+CM233_124+CM253_126+CM273_128+CM293_130+CM383_139+CM403_141+q[49]*FM349_3+CM151_3*C50+CM153_3*\
   C52+CM154_3*C54+CM160_3*C60+CM354_3*S54+CM360_3*S60-CM503_251*S50-CM523_253*S52-FB26_3*s.l[3,6]-FM254_3*s.dpt[3,14]-FM260_3*\
   s.dpt[3,15]+FM503_351*s.dpt[2,52]+FM523_353*s.dpt[2,53]+s.dpt[2,10]*(FM293_230*S29+FM330_3*C29)+s.dpt[2,11]*(FB339_3*C38+\
   FM383_239*S38)+s.dpt[2,12]*(FM341_3*C40+FM403_241*S40)+s.dpt[2,1]*(FM27_3*S7+FM37_3*C7)+s.dpt[2,4]*(FM215_3*S15+FM315_3*C15)\
   +s.dpt[2,6]*(FB324_3*C23+FM233_224*S23)+s.dpt[2,8]*(FB326_3*C25+FM253_226*S25)+s.dpt[2,9]*(FB328_3*C27+FM273_228*S27)+\
   s.dpt[3,11]*(FB339_3*S38-FM383_239*C38)+s.dpt[3,6]*(FB324_3*S23-FM233_224*C23)+s.dpt[3,8]*(FB326_3*S25-FM253_226*C25)+\
   s.dpt[3,9]*(FB328_3*S27-FM273_228*C27)
  CM26_3 = CM254_3+CM260_3+CM151_3*S50+CM153_3*S52+CM215_3*C15+CM233_224*C23+CM253_226*C25+CM273_228*C27+CM27_3*C7+\
   CM293_230*C29-CM315_3*S15-CM324_3*S23-CM326_3*S25-CM328_3*S27-CM330_3*S29-CM339_3*S38-CM341_3*S40-CM37_3*S7+CM383_239*C38+\
   CM403_241*C40+CM503_251*C50+CM523_253*C52+FB16_3*s.l[3,6]+FM233_124*s.dpt[3,6]+FM253_126*s.dpt[3,8]+FM273_128*s.dpt[3,9]-\
   FM349_3*s.dpt[1,13]+FM383_139*s.dpt[3,11]-s.dpt[1,10]*(FM293_230*S29+FM330_3*C29)-s.dpt[1,11]*(FB339_3*C38+FM383_239*S38)-\
   s.dpt[1,12]*(FM341_3*C40+FM403_241*S40)+s.dpt[1,14]*(FM154_3*S54-FM354_3*C54)+s.dpt[1,15]*(FM160_3*S60-FM360_3*C60)-\
   s.dpt[1,1]*(FM27_3*S7+FM37_3*C7)-s.dpt[1,4]*(FM215_3*S15+FM315_3*C15)-s.dpt[1,6]*(FB324_3*C23+FM233_224*S23)-s.dpt[1,8]*(\
   FB326_3*C25+FM253_226*S25)-s.dpt[1,9]*(FB328_3*C27+FM273_228*S27)+s.dpt[3,14]*(FM154_3*C54+FM354_3*S54)+s.dpt[3,15]*(FM160_3\
   *C60+FM360_3*S60)
  CM36_3 = CM503_351+CM523_353-q[49]*FM149_3-CM154_3*S54-CM160_3*S60+CM215_3*S15+CM233_224*S23+CM253_226*S25+CM273_228*\
   S27+CM27_3*S7+CM293_230*S29+CM315_3*C15+CM324_3*C23+CM326_3*C25+CM328_3*C27+CM330_3*C29+CM339_3*C38+CM341_3*C40+CM354_3*C54+\
   CM360_3*C60+CM37_3*C7+CM383_239*S38+CM403_241*S40-FM115_3*s.dpt[2,4]-FM17_3*s.dpt[2,1]-FM233_124*s.dpt[2,6]+FM249_3*\
   s.dpt[1,13]-FM253_126*s.dpt[2,8]+FM254_3*s.dpt[1,14]+FM260_3*s.dpt[1,15]-FM273_128*s.dpt[2,9]-FM293_130*s.dpt[2,10]-\
   FM383_139*s.dpt[2,11]-FM403_141*s.dpt[2,12]+s.dpt[1,10]*(FM293_230*C29-FM330_3*S29)-s.dpt[1,11]*(FB339_3*S38-FM383_239*C38)-\
   s.dpt[1,12]*(FM341_3*S40-FM403_241*C40)+s.dpt[1,1]*(FM27_3*C7-FM37_3*S7)+s.dpt[1,4]*(FM215_3*C15-FM315_3*S15)-s.dpt[1,6]*(\
   FB324_3*S23-FM233_224*C23)-s.dpt[1,8]*(FB326_3*S25-FM253_226*C25)-s.dpt[1,9]*(FB328_3*S27-FM273_228*C27)-s.dpt[2,52]*(\
   FB151_3*C50-FM503_251*S50)-s.dpt[2,53]*(FB153_3*C52-FM523_253*S52)
  CM16_4 = CM115_4+CM17_4+CM234_124+CM254_126+CM274_128+CM294_130+CM384_139+CM404_141+q[49]*FM349_4-s.In[1,6]*S5-s.m[6]*\
   s.l[3,6]*s.l[3,6]*S5+CM151_4*C50+CM153_4*C52+CM154_4*C54+CM160_4*C60+CM354_4*S54+CM360_4*S60-CM504_251*S50-CM524_253*S52-\
   FM254_4*s.dpt[3,14]-FM260_4*s.dpt[3,15]+FM504_351*s.dpt[2,52]+FM524_353*s.dpt[2,53]+s.dpt[2,10]*(FM294_230*S29+FM330_4*C29)+\
   s.dpt[2,11]*(FB339_4*C38+FM384_239*S38)+s.dpt[2,12]*(FM341_4*C40+FM404_241*S40)+s.dpt[2,1]*(FM27_4*S7+FM37_4*C7)+s.dpt[2,4]*\
   (FM215_4*S15+FM315_4*C15)+s.dpt[2,6]*(FB324_4*C23+FM234_224*S23)+s.dpt[2,8]*(FB326_4*C25+FM254_226*S25)+s.dpt[2,9]*(FB328_4*\
   C27+FM274_228*S27)+s.dpt[3,11]*(FB339_4*S38-FM384_239*C38)+s.dpt[3,6]*(FB324_4*S23-FM234_224*C23)+s.dpt[3,8]*(FB326_4*S25-\
   FM254_226*C25)+s.dpt[3,9]*(FB328_4*S27-FM274_228*C27)
  CM26_4 = CM254_4+CM260_4+s.In[5,6]*OpM26_4+s.m[6]*OpM26_4*s.l[3,6]*s.l[3,6]+CM151_4*S50+CM153_4*S52+CM215_4*C15+\
   CM234_224*C23+CM254_226*C25+CM274_228*C27+CM27_4*C7+CM294_230*C29-CM315_4*S15-CM324_4*S23-CM326_4*S25-CM328_4*S27-CM330_4*\
   S29-CM339_4*S38-CM341_4*S40-CM37_4*S7+CM384_239*C38+CM404_241*C40+CM504_251*C50+CM524_253*C52+FM234_124*s.dpt[3,6]+FM254_126\
   *s.dpt[3,8]+FM274_128*s.dpt[3,9]-FM349_4*s.dpt[1,13]+FM384_139*s.dpt[3,11]-s.dpt[1,10]*(FM294_230*S29+FM330_4*C29)-\
   s.dpt[1,11]*(FB339_4*C38+FM384_239*S38)-s.dpt[1,12]*(FM341_4*C40+FM404_241*S40)+s.dpt[1,14]*(FM154_4*S54-FM354_4*C54)+\
   s.dpt[1,15]*(FM160_4*S60-FM360_4*C60)-s.dpt[1,1]*(FM27_4*S7+FM37_4*C7)-s.dpt[1,4]*(FM215_4*S15+FM315_4*C15)-s.dpt[1,6]*(\
   FB324_4*C23+FM234_224*S23)-s.dpt[1,8]*(FB326_4*C25+FM254_226*S25)-s.dpt[1,9]*(FB328_4*C27+FM274_228*S27)+s.dpt[3,14]*(\
   FM154_4*C54+FM354_4*S54)+s.dpt[3,15]*(FM160_4*C60+FM360_4*S60)
  CM36_4 = CM504_351+CM524_353-q[49]*(s.m[49]*AlM149_4+FB151_4*C50+FB153_4*C52-FM504_251*S50-FM524_253*S52)+s.In[9,6]*\
   OpM36_4-CM154_4*S54-CM160_4*S60+CM215_4*S15+CM234_224*S23+CM254_226*S25+CM274_228*S27+CM27_4*S7+CM294_230*S29+CM315_4*C15+\
   CM324_4*C23+CM326_4*C25+CM328_4*C27+CM330_4*C29+CM339_4*C38+CM341_4*C40+CM354_4*C54+CM360_4*C60+CM37_4*C7+CM384_239*S38+\
   CM404_241*S40-FM234_124*s.dpt[2,6]+FM249_4*s.dpt[1,13]-FM254_126*s.dpt[2,8]+FM254_4*s.dpt[1,14]+FM260_4*s.dpt[1,15]-\
   FM274_128*s.dpt[2,9]-FM384_139*s.dpt[2,11]+s.dpt[1,10]*(FM294_230*C29-FM330_4*S29)-s.dpt[1,11]*(FB339_4*S38-FM384_239*C38)-\
   s.dpt[1,12]*(FM341_4*S40-FM404_241*C40)+s.dpt[1,1]*(FM27_4*C7-FM37_4*S7)+s.dpt[1,4]*(FM215_4*C15-FM315_4*S15)-s.dpt[1,6]*(\
   FB324_4*S23-FM234_224*C23)-s.dpt[1,8]*(FB326_4*S25-FM254_226*C25)-s.dpt[1,9]*(FB328_4*S27-FM274_228*C27)-s.dpt[2,10]*(\
   FM130_4*C30-FM230_4*S30)-s.dpt[2,12]*(FM141_4*C41-FM241_4*S41)-s.dpt[2,1]*(FB17_4-FM84_29*S8+FM94_110*C8)-s.dpt[2,4]*(\
   FB115_4-FM164_217*S16+FM174_118*C16)-s.dpt[2,52]*(FB151_4*C50-FM504_251*S50)-s.dpt[2,53]*(FB153_4*C52-FM524_253*S52)
  CM16_5 = CM115_5+CM17_5+CM235_124+CM255_126+CM275_128+CM295_130+CM385_139+CM405_141+q[49]*FM349_5+CM151_5*C50+CM153_5*\
   C52+CM154_5*C54+CM160_5*C60+CM354_5*S54+CM360_5*S60-CM505_251*S50-CM525_253*S52-FM254_5*s.dpt[3,14]-FM260_5*s.dpt[3,15]+\
   FM505_351*s.dpt[2,52]+FM525_353*s.dpt[2,53]+s.dpt[2,10]*(FM295_230*S29+FM330_5*C29)+s.dpt[2,11]*(FB339_5*C38+FM385_239*S38)+\
   s.dpt[2,12]*(FM341_5*C40+FM405_241*S40)+s.dpt[2,1]*(FM27_5*S7+FM37_5*C7)+s.dpt[2,4]*(FM215_5*S15+FM315_5*C15)+s.dpt[2,6]*(\
   FB324_5*C23+FM235_224*S23)+s.dpt[2,8]*(FB326_5*C25+FM255_226*S25)+s.dpt[2,9]*(FB328_5*C27+FM275_228*S27)+s.dpt[3,11]*(\
   FB339_5*S38-FM385_239*C38)+s.dpt[3,6]*(FB324_5*S23-FM235_224*C23)+s.dpt[3,8]*(FB326_5*S25-FM255_226*C25)+s.dpt[3,9]*(FB328_5\
   *S27-FM275_228*C27)
  CM16_6 = s.In[1,6]+CM115_6+CM17_6+CM236_124+CM256_126+CM276_128+CM296_130+CM386_139+CM406_141+q[49]*(FM506_351+\
   FM526_353+q[49]*s.m[49])+s.m[6]*s.l[3,6]*s.l[3,6]+CM151_6*C50+CM153_6*C52+CM351_6*S50*S51+CM353_6*S52*S53+FM506_351*\
   s.dpt[2,52]+FM526_353*s.dpt[2,53]+s.dpt[2,10]*(C29*(FB330_6+FM316_332*C31+FM326_233*S31)+S29*(C30*(s.m[30]*AlM230_6-\
   FM316_332*S31+FM326_233*C31)+S30*(FB130_6+FM316_132)))+s.dpt[2,11]*(FB339_6*C38+FM386_239*S38)+s.dpt[2,12]*(C40*(FB341_6+\
   FM426_343*C42+FM436_244*S42)+S40*(C41*(s.m[41]*AlM241_6-FM426_343*S42+FM436_244*C42)+S41*(FB141_6+FM426_143)))+s.dpt[2,1]*(\
   C7*(FB37_6+FM86_39)+S7*(s.m[7]*AlM27_6+C8*(FM210_6*C9-FM96_310*S9)+S8*(FM110_6*C10+FM310_6*S10)))+s.dpt[2,4]*(C15*(FB315_6+\
   FM166_317)+S15*(s.m[15]*AlM215_6-C16*(FM176_318*S17-FM218_6*C17)+S16*(FM118_6*C18+FM318_6*S18)))+s.dpt[2,6]*(FB324_6*C23+\
   FM236_224*S23)+s.dpt[2,8]*(FB326_6*C25+FM256_226*S25)+s.dpt[2,9]*(FB328_6*C27+FM276_228*S27)+s.dpt[3,11]*(FB339_6*S38-\
   FM386_239*C38)-s.dpt[3,14]*(FB254_6+FB255_6+FM566_257+FM586_259)-s.dpt[3,15]*(FB260_6+FB261_6+FM626_263+FM646_265)+\
   s.dpt[3,6]*(FB324_6*S23-FM236_224*C23)+s.dpt[3,8]*(FB326_6*S25-FM256_226*C25)+s.dpt[3,9]*(FB328_6*S27-FM276_228*C27)+C54*(\
   CM155_6*C55+CM159_6*C58+CM355_6*S55+CM586_359*S58+FB354_6*s.l[2,54]-s.dpt[2,56]*(FB159_6*S58-FM586_359*C58))+S54*(s.m[54]*\
   s.l[2,54]*s.l[2,54]*S54-CM155_6*S55-CM159_6*S58+CM355_6*C55+CM586_359*C58+FB254_6*s.l[1,54]+FM586_259*s.dpt[1,56]-\
   s.dpt[2,56]*(FB159_6*C58+FM586_359*S58))+C60*(CM161_6*C61+CM165_6*C64+CM361_6*S61+CM646_365*S64+FB360_6*s.l[2,60]-\
   s.dpt[2,60]*(FB165_6*S64-FM646_365*C64))+S60*(s.m[60]*s.l[2,60]*s.l[2,60]*S60-CM161_6*S61-CM165_6*S64+CM361_6*C61+CM646_365*\
   C64+FB260_6*s.l[1,60]+FM646_265*s.dpt[1,60]-s.dpt[2,60]*(FB165_6*C64+FM646_365*S64))
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
  CM55_26 = C6*(CM254_5+CM260_5+s.In[5,6]*C6+s.m[6]*s.l[3,6]*s.l[3,6]*C6+CM151_5*S50+CM153_5*S52+CM215_5*C15+CM235_224*\
   C23+CM255_226*C25+CM275_228*C27+CM27_5*C7+CM295_230*C29-CM315_5*S15-CM324_5*S23-CM326_5*S25-CM328_5*S27-CM330_5*S29-CM339_5*\
   S38-CM341_5*S40-CM37_5*S7+CM385_239*C38+CM405_241*C40+CM505_251*C50+CM525_253*C52+FM235_124*s.dpt[3,6]+FM255_126*s.dpt[3,8]+\
   FM275_128*s.dpt[3,9]-FM349_5*s.dpt[1,13]+FM385_139*s.dpt[3,11]-s.dpt[1,10]*(FM295_230*S29+FM330_5*C29)-s.dpt[1,11]*(FB339_5*\
   C38+FM385_239*S38)-s.dpt[1,12]*(FM341_5*C40+FM405_241*S40)+s.dpt[1,14]*(FM154_5*S54-FM354_5*C54)+s.dpt[1,15]*(FM160_5*S60-\
   FM360_5*C60)-s.dpt[1,1]*(FM27_5*S7+FM37_5*C7)-s.dpt[1,4]*(FM215_5*S15+FM315_5*C15)-s.dpt[1,6]*(FB324_5*C23+FM235_224*S23)-\
   s.dpt[1,8]*(FB326_5*C25+FM255_226*S25)-s.dpt[1,9]*(FB328_5*C27+FM275_228*S27)+s.dpt[3,14]*(FM154_5*C54+FM354_5*S54)+\
   s.dpt[3,15]*(FM160_5*C60+FM360_5*S60))-S6*(CM505_351+CM525_353-q[49]*(s.m[49]*AlM149_5+FB151_5*C50+FB153_5*C52-FM505_251*S50\
   -FM525_253*S52)-s.In[9,6]*S6-CM154_5*S54-CM160_5*S60+CM215_5*S15+CM235_224*S23+CM255_226*S25+CM275_228*S27+CM27_5*S7+\
   CM295_230*S29+CM315_5*C15+CM324_5*C23+CM326_5*C25+CM328_5*C27+CM330_5*C29+CM339_5*C38+CM341_5*C40+CM354_5*C54+CM360_5*C60+\
   CM37_5*C7+CM385_239*S38+CM405_241*S40-FM235_124*s.dpt[2,6]+FM249_5*s.dpt[1,13]+FM254_5*s.dpt[1,14]-FM255_126*s.dpt[2,8]+\
   FM260_5*s.dpt[1,15]-FM275_128*s.dpt[2,9]-FM385_139*s.dpt[2,11]+s.dpt[1,10]*(FM295_230*C29-FM330_5*S29)-s.dpt[1,11]*(FB339_5*\
   S38-FM385_239*C38)-s.dpt[1,12]*(FM341_5*S40-FM405_241*C40)+s.dpt[1,1]*(FM27_5*C7-FM37_5*S7)+s.dpt[1,4]*(FM215_5*C15-FM315_5*\
   S15)-s.dpt[1,6]*(FB324_5*S23-FM235_224*C23)-s.dpt[1,8]*(FB326_5*S25-FM255_226*C25)-s.dpt[1,9]*(FB328_5*S27-FM275_228*C27)-\
   s.dpt[2,10]*(FM130_5*C30-FM230_5*S30)-s.dpt[2,12]*(FM141_5*C41-FM241_5*S41)-s.dpt[2,1]*(FB17_5-FM85_29*S8+FM95_110*C8)-\
   s.dpt[2,4]*(FB115_5-FM165_217*S16+FM175_118*C16)-s.dpt[2,52]*(FB151_5*C50-FM505_251*S50)-s.dpt[2,53]*(FB153_5*C52-FM525_253*\
   S52))
  FF4_15 = FF16*C5+FF5_36*S5
  FF4_35 = -(FF16*S5-FF5_36*C5)
  CF4_35 = -(CF16*S5-C5*(CF26*S6+CF36*C6))
  FM41_15 = FM16_1*C5+FM51_36*S5
  FM41_35 = -(FM16_1*S5-FM51_36*C5)
  CM41_35 = -(CM16_1*S5-C5*(CM26_1*S6+CM36_1*C6))
  FM42_35 = -(FM16_2*S5-FM52_36*C5)
  CM42_35 = -(CM16_2*S5-C5*(CM26_2*S6+CM36_2*C6))
  FM43_35 = C5*(C6*(FM349_3+s.m[6]*AlM36_3+FB324_3*C23+FB326_3*C25+FB328_3*C27+FB339_3*C38-FM154_3*S54-FM160_3*S60+\
   FM215_3*S15+FM233_224*S23+FM253_226*S25+FM273_228*S27+FM27_3*S7+FM293_230*S29+FM315_3*C15+FM330_3*C29+FM341_3*C40+FM354_3*\
   C54+FM360_3*C60+FM37_3*C7+FM383_239*S38+FM403_241*S40)+S6*(FB26_3+FM249_3+FM254_3+FM260_3-FB324_3*S23-FB326_3*S25-FB328_3*\
   S27-FB339_3*S38+FM215_3*C15+FM233_224*C23+FM253_226*C25+FM273_228*C27+FM27_3*C7+FM293_230*C29-FM315_3*S15-FM330_3*S29-\
   FM341_3*S40-FM37_3*S7+FM383_239*C38+FM403_241*C40))-S5*(FB16_3+FM115_3+FM149_3+FM17_3+FM233_124+FM253_126+FM273_128+\
   FM293_130+FM383_139+FM403_141+FM154_3*C54+FM160_3*C60+FM354_3*S54+FM360_3*S60)
  CM43_35 = -(CM16_3*S5-C5*(CM26_3*S6+CM36_3*C6))
  CM44_35 = -(CM16_4*S5-C5*(CM26_4*S6+CM36_4*C6))
  FF3_14 = FF4_15*C4-FF5_26*S4
  FF3_24 = FF4_15*S4+FF5_26*C4
  FM31_14 = FM41_15*C4-FM51_26*S4
  FM31_24 = FM41_15*S4+FM51_26*C4
  FM32_24 = C4*(FM26_2*C6-FM36_2*S6)+S4*(FM16_2*C5+FM52_36*S5)

# = = Block_0_2_0_3_0_27 = = 
 
# Backward Dynamics 

  FA366 = -(s.frc[3,66]+s.m[66]*s.g[3])

# = = Block_0_2_0_3_0_28 = = 
 
# Backward Dynamics 

  FA367 = -(s.frc[3,67]+s.m[67]*s.g[3])

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
  M[1,26] = CM326_1
  M[1,27] = CM271_128
  M[1,28] = CM328_1
  M[1,29] = CM291_130
  M[1,30] = CM330_1
  M[1,31] = CM311_132
  M[1,32] = CM321_233
  M[1,33] = CM333_1
  M[1,34] = CM341_135
  M[1,35] = FB335_1
  M[1,38] = CM381_139
  M[1,39] = CM339_1
  M[1,40] = CM401_141
  M[1,41] = CM341_1
  M[1,42] = CM421_143
  M[1,43] = CM431_244
  M[1,44] = CM344_1
  M[1,45] = CM451_146
  M[1,46] = FB346_1
  M[1,49] = FM249_1
  M[1,50] = CM501_351
  M[1,51] = CM151_1
  M[1,52] = CM521_353
  M[1,53] = CM153_1
  M[1,54] = CM254_1
  M[1,55] = CM255_1
  M[1,56] = CM561_257
  M[1,57] = CM157_1
  M[1,58] = CM581_259
  M[1,59] = CM159_1
  M[1,60] = CM260_1
  M[1,61] = CM261_1
  M[1,62] = CM621_263
  M[1,63] = CM163_1
  M[1,64] = CM641_265
  M[1,65] = CM165_1
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
  M[2,26] = CM326_2
  M[2,27] = CM272_128
  M[2,28] = CM328_2
  M[2,29] = CM292_130
  M[2,30] = CM330_2
  M[2,31] = CM312_132
  M[2,32] = CM322_233
  M[2,33] = CM333_2
  M[2,34] = CM342_135
  M[2,35] = FB335_2
  M[2,38] = CM382_139
  M[2,39] = CM339_2
  M[2,40] = CM402_141
  M[2,41] = CM341_2
  M[2,42] = CM422_143
  M[2,43] = CM432_244
  M[2,44] = CM344_2
  M[2,45] = CM452_146
  M[2,46] = FB346_2
  M[2,49] = FM249_2
  M[2,50] = CM502_351
  M[2,51] = CM151_2
  M[2,52] = CM522_353
  M[2,53] = CM153_2
  M[2,54] = CM254_2
  M[2,55] = CM255_2
  M[2,56] = CM562_257
  M[2,57] = CM157_2
  M[2,58] = CM582_259
  M[2,59] = CM159_2
  M[2,60] = CM260_2
  M[2,61] = CM261_2
  M[2,62] = CM622_263
  M[2,63] = CM163_2
  M[2,64] = CM642_265
  M[2,65] = CM165_2
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
  M[3,26] = CM326_3
  M[3,27] = CM273_128
  M[3,28] = CM328_3
  M[3,29] = CM293_130
  M[3,30] = CM330_3
  M[3,31] = CM313_132
  M[3,32] = CM323_233
  M[3,33] = CM333_3
  M[3,34] = CM343_135
  M[3,35] = FB335_3
  M[3,38] = CM383_139
  M[3,39] = CM339_3
  M[3,40] = CM403_141
  M[3,41] = CM341_3
  M[3,42] = CM423_143
  M[3,43] = CM433_244
  M[3,44] = CM344_3
  M[3,45] = CM453_146
  M[3,46] = FB346_3
  M[3,49] = FM249_3
  M[3,50] = CM503_351
  M[3,51] = CM151_3
  M[3,52] = CM523_353
  M[3,53] = CM153_3
  M[3,54] = CM254_3
  M[3,55] = CM255_3
  M[3,56] = CM563_257
  M[3,57] = CM157_3
  M[3,58] = CM583_259
  M[3,59] = CM159_3
  M[3,60] = CM260_3
  M[3,61] = CM261_3
  M[3,62] = CM623_263
  M[3,63] = CM163_3
  M[3,64] = CM643_265
  M[3,65] = CM165_3
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
  M[4,28] = CM328_4
  M[4,29] = CM294_130
  M[4,30] = CM330_4
  M[4,31] = CM314_132
  M[4,32] = CM324_233
  M[4,33] = CM333_4
  M[4,34] = CM344_135
  M[4,35] = FB335_4
  M[4,36] = CM364_137
  M[4,37] = CM237_4
  M[4,38] = CM384_139
  M[4,39] = CM339_4
  M[4,40] = CM404_141
  M[4,41] = CM341_4
  M[4,42] = CM424_143
  M[4,43] = CM434_244
  M[4,44] = CM344_4
  M[4,45] = CM454_146
  M[4,46] = FB346_4
  M[4,47] = CM474_148
  M[4,48] = CM248_4
  M[4,49] = FM249_4
  M[4,50] = CM504_351
  M[4,51] = CM151_4
  M[4,52] = CM524_353
  M[4,53] = CM153_4
  M[4,54] = CM254_4
  M[4,55] = CM255_4
  M[4,56] = CM564_257
  M[4,57] = CM157_4
  M[4,58] = CM584_259
  M[4,59] = CM159_4
  M[4,60] = CM260_4
  M[4,61] = CM261_4
  M[4,62] = CM624_263
  M[4,63] = CM163_4
  M[4,64] = CM644_265
  M[4,65] = CM165_4
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
  M[5,28] = CM328_5
  M[5,29] = CM295_130
  M[5,30] = CM330_5
  M[5,31] = CM315_132
  M[5,32] = CM325_233
  M[5,33] = CM333_5
  M[5,34] = CM345_135
  M[5,35] = FB335_5
  M[5,36] = CM365_137
  M[5,37] = CM237_5
  M[5,38] = CM385_139
  M[5,39] = CM339_5
  M[5,40] = CM405_141
  M[5,41] = CM341_5
  M[5,42] = CM425_143
  M[5,43] = CM435_244
  M[5,44] = CM344_5
  M[5,45] = CM455_146
  M[5,46] = FB346_5
  M[5,47] = CM475_148
  M[5,48] = CM248_5
  M[5,49] = FM249_5
  M[5,50] = CM505_351
  M[5,51] = CM151_5
  M[5,52] = CM525_353
  M[5,53] = CM153_5
  M[5,54] = CM254_5
  M[5,55] = CM255_5
  M[5,56] = CM565_257
  M[5,57] = CM157_5
  M[5,58] = CM585_259
  M[5,59] = CM159_5
  M[5,60] = CM260_5
  M[5,61] = CM261_5
  M[5,62] = CM625_263
  M[5,63] = CM163_5
  M[5,64] = CM645_265
  M[5,65] = CM165_5
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
  M[6,28] = CM328_6
  M[6,29] = CM296_130
  M[6,30] = CM330_6
  M[6,31] = CM316_132
  M[6,32] = CM326_233
  M[6,33] = CM333_6
  M[6,34] = CM346_135
  M[6,35] = FB335_6
  M[6,36] = CM366_137
  M[6,37] = CM237_6
  M[6,38] = CM386_139
  M[6,39] = CM339_6
  M[6,40] = CM406_141
  M[6,41] = CM341_6
  M[6,42] = CM426_143
  M[6,43] = CM436_244
  M[6,44] = CM344_6
  M[6,45] = CM456_146
  M[6,46] = FB346_6
  M[6,47] = CM476_148
  M[6,48] = CM248_6
  M[6,49] = FM249_6
  M[6,50] = CM506_351
  M[6,51] = CM151_6
  M[6,52] = CM526_353
  M[6,53] = CM153_6
  M[6,54] = CM254_6
  M[6,55] = CM255_6
  M[6,56] = CM566_257
  M[6,57] = CM157_6
  M[6,58] = CM586_259
  M[6,59] = CM159_6
  M[6,60] = CM260_6
  M[6,61] = CM261_6
  M[6,62] = CM626_263
  M[6,63] = CM163_6
  M[6,64] = CM646_265
  M[6,65] = CM165_6
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
  M[24,1] = CM324_1
  M[24,2] = CM324_2
  M[24,3] = CM324_3
  M[24,4] = CM324_4
  M[24,5] = CM324_5
  M[24,6] = CM324_6
  M[24,24] = CM324_24
  M[25,1] = CM251_126
  M[25,2] = CM252_126
  M[25,3] = CM253_126
  M[25,4] = CM254_126
  M[25,5] = CM255_126
  M[25,6] = CM256_126
  M[25,25] = CM2525_126
  M[26,1] = CM326_1
  M[26,2] = CM326_2
  M[26,3] = CM326_3
  M[26,4] = CM326_4
  M[26,5] = CM326_5
  M[26,6] = CM326_6
  M[26,26] = CM326_26
  M[27,1] = CM271_128
  M[27,2] = CM272_128
  M[27,3] = CM273_128
  M[27,4] = CM274_128
  M[27,5] = CM275_128
  M[27,6] = CM276_128
  M[27,27] = CM2727_128
  M[28,1] = CM328_1
  M[28,2] = CM328_2
  M[28,3] = CM328_3
  M[28,4] = CM328_4
  M[28,5] = CM328_5
  M[28,6] = CM328_6
  M[28,28] = CM328_28
  M[29,1] = CM291_130
  M[29,2] = CM292_130
  M[29,3] = CM293_130
  M[29,4] = CM294_130
  M[29,5] = CM295_130
  M[29,6] = CM296_130
  M[29,29] = CM2929_130
  M[29,30] = CM3029_331
  M[29,31] = CM3129_132
  M[29,32] = CM3229_233
  M[29,33] = CM333_29
  M[29,34] = CM3429_135
  M[29,35] = FB335_29
  M[29,36] = CM3629_137
  M[29,37] = CM237_29
  M[30,1] = CM330_1
  M[30,2] = CM330_2
  M[30,3] = CM330_3
  M[30,4] = CM330_4
  M[30,5] = CM330_5
  M[30,6] = CM330_6
  M[30,29] = CM3029_331
  M[30,30] = CM330_30
  M[30,31] = CM3130_132
  M[30,32] = CM3230_233
  M[30,33] = CM333_30
  M[30,34] = CM3430_135
  M[30,35] = FB335_30
  M[30,36] = CM3630_137
  M[30,37] = CM237_30
  M[31,1] = CM311_132
  M[31,2] = CM312_132
  M[31,3] = CM313_132
  M[31,4] = CM314_132
  M[31,5] = CM315_132
  M[31,6] = CM316_132
  M[31,29] = CM3129_132
  M[31,30] = CM3130_132
  M[31,31] = CM3131_132
  M[31,32] = CM3231_233
  M[31,33] = CM333_31
  M[31,34] = CM3431_135
  M[31,35] = FB335_31
  M[31,36] = CM3631_137
  M[31,37] = CM237_31
  M[32,1] = CM321_233
  M[32,2] = CM322_233
  M[32,3] = CM323_233
  M[32,4] = CM324_233
  M[32,5] = CM325_233
  M[32,6] = CM326_233
  M[32,29] = CM3229_233
  M[32,30] = CM3230_233
  M[32,31] = CM3231_233
  M[32,32] = CM3232_233
  M[32,33] = CM333_32
  M[32,34] = CM3432_135
  M[32,35] = FB335_32
  M[32,36] = CM3632_137
  M[32,37] = CM237_32
  M[33,1] = CM333_1
  M[33,2] = CM333_2
  M[33,3] = CM333_3
  M[33,4] = CM333_4
  M[33,5] = CM333_5
  M[33,6] = CM333_6
  M[33,29] = CM333_29
  M[33,30] = CM333_30
  M[33,31] = CM333_31
  M[33,32] = CM333_32
  M[33,33] = CM333_33
  M[33,36] = CM3633_137
  M[33,37] = CM237_33
  M[34,1] = CM341_135
  M[34,2] = CM342_135
  M[34,3] = CM343_135
  M[34,4] = CM344_135
  M[34,5] = CM345_135
  M[34,6] = CM346_135
  M[34,29] = CM3429_135
  M[34,30] = CM3430_135
  M[34,31] = CM3431_135
  M[34,32] = CM3432_135
  M[34,34] = CM3434_135
  M[35,1] = FB335_1
  M[35,2] = FB335_2
  M[35,3] = FB335_3
  M[35,4] = FB335_4
  M[35,5] = FB335_5
  M[35,6] = FB335_6
  M[35,29] = FB335_29
  M[35,30] = FB335_30
  M[35,31] = FB335_31
  M[35,32] = FB335_32
  M[35,35] = s.m[35]
  M[36,4] = CM364_137
  M[36,5] = CM365_137
  M[36,6] = CM366_137
  M[36,29] = CM3629_137
  M[36,30] = CM3630_137
  M[36,31] = CM3631_137
  M[36,32] = CM3632_137
  M[36,33] = CM3633_137
  M[36,36] = CM3636_137
  M[37,4] = CM237_4
  M[37,5] = CM237_5
  M[37,6] = CM237_6
  M[37,29] = CM237_29
  M[37,30] = CM237_30
  M[37,31] = CM237_31
  M[37,32] = CM237_32
  M[37,33] = CM237_33
  M[37,37] = s.In[5,37]
  M[38,1] = CM381_139
  M[38,2] = CM382_139
  M[38,3] = CM383_139
  M[38,4] = CM384_139
  M[38,5] = CM385_139
  M[38,6] = CM386_139
  M[38,38] = CM3838_139
  M[39,1] = CM339_1
  M[39,2] = CM339_2
  M[39,3] = CM339_3
  M[39,4] = CM339_4
  M[39,5] = CM339_5
  M[39,6] = CM339_6
  M[39,39] = CM339_39
  M[40,1] = CM401_141
  M[40,2] = CM402_141
  M[40,3] = CM403_141
  M[40,4] = CM404_141
  M[40,5] = CM405_141
  M[40,6] = CM406_141
  M[40,40] = CM4040_141
  M[40,41] = CM4140_342
  M[40,42] = CM4240_143
  M[40,43] = CM4340_244
  M[40,44] = CM344_40
  M[40,45] = CM4540_146
  M[40,46] = FB346_40
  M[40,47] = CM4740_148
  M[40,48] = CM248_40
  M[41,1] = CM341_1
  M[41,2] = CM341_2
  M[41,3] = CM341_3
  M[41,4] = CM341_4
  M[41,5] = CM341_5
  M[41,6] = CM341_6
  M[41,40] = CM4140_342
  M[41,41] = CM341_41
  M[41,42] = CM4241_143
  M[41,43] = CM4341_244
  M[41,44] = CM344_41
  M[41,45] = CM4541_146
  M[41,46] = FB346_41
  M[41,47] = CM4741_148
  M[41,48] = CM248_41
  M[42,1] = CM421_143
  M[42,2] = CM422_143
  M[42,3] = CM423_143
  M[42,4] = CM424_143
  M[42,5] = CM425_143
  M[42,6] = CM426_143
  M[42,40] = CM4240_143
  M[42,41] = CM4241_143
  M[42,42] = CM4242_143
  M[42,43] = CM4342_244
  M[42,44] = CM344_42
  M[42,45] = CM4542_146
  M[42,46] = FB346_42
  M[42,47] = CM4742_148
  M[42,48] = CM248_42
  M[43,1] = CM431_244
  M[43,2] = CM432_244
  M[43,3] = CM433_244
  M[43,4] = CM434_244
  M[43,5] = CM435_244
  M[43,6] = CM436_244
  M[43,40] = CM4340_244
  M[43,41] = CM4341_244
  M[43,42] = CM4342_244
  M[43,43] = CM4343_244
  M[43,44] = CM344_43
  M[43,45] = CM4543_146
  M[43,46] = FB346_43
  M[43,47] = CM4743_148
  M[43,48] = CM248_43
  M[44,1] = CM344_1
  M[44,2] = CM344_2
  M[44,3] = CM344_3
  M[44,4] = CM344_4
  M[44,5] = CM344_5
  M[44,6] = CM344_6
  M[44,40] = CM344_40
  M[44,41] = CM344_41
  M[44,42] = CM344_42
  M[44,43] = CM344_43
  M[44,44] = CM344_44
  M[44,47] = CM4744_148
  M[44,48] = CM248_44
  M[45,1] = CM451_146
  M[45,2] = CM452_146
  M[45,3] = CM453_146
  M[45,4] = CM454_146
  M[45,5] = CM455_146
  M[45,6] = CM456_146
  M[45,40] = CM4540_146
  M[45,41] = CM4541_146
  M[45,42] = CM4542_146
  M[45,43] = CM4543_146
  M[45,45] = CM4545_146
  M[46,1] = FB346_1
  M[46,2] = FB346_2
  M[46,3] = FB346_3
  M[46,4] = FB346_4
  M[46,5] = FB346_5
  M[46,6] = FB346_6
  M[46,40] = FB346_40
  M[46,41] = FB346_41
  M[46,42] = FB346_42
  M[46,43] = FB346_43
  M[46,46] = s.m[46]
  M[47,4] = CM474_148
  M[47,5] = CM475_148
  M[47,6] = CM476_148
  M[47,40] = CM4740_148
  M[47,41] = CM4741_148
  M[47,42] = CM4742_148
  M[47,43] = CM4743_148
  M[47,44] = CM4744_148
  M[47,47] = CM4747_148
  M[48,4] = CM248_4
  M[48,5] = CM248_5
  M[48,6] = CM248_6
  M[48,40] = CM248_40
  M[48,41] = CM248_41
  M[48,42] = CM248_42
  M[48,43] = CM248_43
  M[48,44] = CM248_44
  M[48,48] = s.In[5,48]
  M[49,1] = FM249_1
  M[49,2] = FM249_2
  M[49,3] = FM249_3
  M[49,4] = FM249_4
  M[49,5] = FM249_5
  M[49,6] = FM249_6
  M[49,49] = FM249_49
  M[49,50] = CM5049_351
  M[49,51] = CM151_49
  M[49,52] = CM5249_353
  M[49,53] = CM153_49
  M[50,1] = CM501_351
  M[50,2] = CM502_351
  M[50,3] = CM503_351
  M[50,4] = CM504_351
  M[50,5] = CM505_351
  M[50,6] = CM506_351
  M[50,49] = CM5049_351
  M[50,50] = CM5050_351
  M[51,1] = CM151_1
  M[51,2] = CM151_2
  M[51,3] = CM151_3
  M[51,4] = CM151_4
  M[51,5] = CM151_5
  M[51,6] = CM151_6
  M[51,49] = CM151_49
  M[51,51] = CM151_51
  M[52,1] = CM521_353
  M[52,2] = CM522_353
  M[52,3] = CM523_353
  M[52,4] = CM524_353
  M[52,5] = CM525_353
  M[52,6] = CM526_353
  M[52,49] = CM5249_353
  M[52,52] = CM5252_353
  M[53,1] = CM153_1
  M[53,2] = CM153_2
  M[53,3] = CM153_3
  M[53,4] = CM153_4
  M[53,5] = CM153_5
  M[53,6] = CM153_6
  M[53,49] = CM153_49
  M[53,53] = CM153_53
  M[54,1] = CM254_1
  M[54,2] = CM254_2
  M[54,3] = CM254_3
  M[54,4] = CM254_4
  M[54,5] = CM254_5
  M[54,6] = CM254_6
  M[54,54] = CM254_54
  M[54,55] = CM255_54
  M[54,56] = CM5654_257
  M[54,57] = CM157_54
  M[54,58] = CM5854_259
  M[54,59] = CM159_54
  M[55,1] = CM255_1
  M[55,2] = CM255_2
  M[55,3] = CM255_3
  M[55,4] = CM255_4
  M[55,5] = CM255_5
  M[55,6] = CM255_6
  M[55,54] = CM255_54
  M[55,55] = CM255_55
  M[55,56] = CM5655_257
  M[55,57] = CM157_55
  M[56,1] = CM561_257
  M[56,2] = CM562_257
  M[56,3] = CM563_257
  M[56,4] = CM564_257
  M[56,5] = CM565_257
  M[56,6] = CM566_257
  M[56,54] = CM5654_257
  M[56,55] = CM5655_257
  M[56,56] = CM5656_257
  M[57,1] = CM157_1
  M[57,2] = CM157_2
  M[57,3] = CM157_3
  M[57,4] = CM157_4
  M[57,5] = CM157_5
  M[57,6] = CM157_6
  M[57,54] = CM157_54
  M[57,55] = CM157_55
  M[57,57] = CM157_57
  M[58,1] = CM581_259
  M[58,2] = CM582_259
  M[58,3] = CM583_259
  M[58,4] = CM584_259
  M[58,5] = CM585_259
  M[58,6] = CM586_259
  M[58,54] = CM5854_259
  M[58,58] = CM5858_259
  M[59,1] = CM159_1
  M[59,2] = CM159_2
  M[59,3] = CM159_3
  M[59,4] = CM159_4
  M[59,5] = CM159_5
  M[59,6] = CM159_6
  M[59,54] = CM159_54
  M[59,59] = CM159_59
  M[60,1] = CM260_1
  M[60,2] = CM260_2
  M[60,3] = CM260_3
  M[60,4] = CM260_4
  M[60,5] = CM260_5
  M[60,6] = CM260_6
  M[60,60] = CM260_60
  M[60,61] = CM261_60
  M[60,62] = CM6260_263
  M[60,63] = CM163_60
  M[60,64] = CM6460_265
  M[60,65] = CM165_60
  M[61,1] = CM261_1
  M[61,2] = CM261_2
  M[61,3] = CM261_3
  M[61,4] = CM261_4
  M[61,5] = CM261_5
  M[61,6] = CM261_6
  M[61,60] = CM261_60
  M[61,61] = CM261_61
  M[61,62] = CM6261_263
  M[61,63] = CM163_61
  M[62,1] = CM621_263
  M[62,2] = CM622_263
  M[62,3] = CM623_263
  M[62,4] = CM624_263
  M[62,5] = CM625_263
  M[62,6] = CM626_263
  M[62,60] = CM6260_263
  M[62,61] = CM6261_263
  M[62,62] = CM6262_263
  M[63,1] = CM163_1
  M[63,2] = CM163_2
  M[63,3] = CM163_3
  M[63,4] = CM163_4
  M[63,5] = CM163_5
  M[63,6] = CM163_6
  M[63,60] = CM163_60
  M[63,61] = CM163_61
  M[63,63] = CM163_63
  M[64,1] = CM641_265
  M[64,2] = CM642_265
  M[64,3] = CM643_265
  M[64,4] = CM644_265
  M[64,5] = CM645_265
  M[64,6] = CM646_265
  M[64,60] = CM6460_265
  M[64,64] = CM6464_265
  M[65,1] = CM165_1
  M[65,2] = CM165_2
  M[65,3] = CM165_3
  M[65,4] = CM165_4
  M[65,5] = CM165_5
  M[65,6] = CM165_6
  M[65,60] = CM165_60
  M[65,65] = CM165_65
  M[66,66] = s.m[66]
  M[67,67] = s.m[67]
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
  c[28] = CF328
  c[29] = CF29_130
  c[30] = CF330
  c[31] = CF31_132
  c[32] = CF32_233
  c[33] = CF333
  c[34] = CF34_135
  c[35] = FA335
  c[36] = CF36_137
  c[37] = CF237
  c[38] = CF38_139
  c[39] = CF339
  c[40] = CF40_141
  c[41] = CF341
  c[42] = CF42_143
  c[43] = CF43_244
  c[44] = CF344
  c[45] = CF45_146
  c[46] = FA346
  c[47] = CF47_148
  c[48] = CF248
  c[49] = FF249
  c[50] = CF50_351
  c[51] = CF151
  c[52] = CF52_353
  c[53] = CF153
  c[54] = CF254
  c[55] = CF255
  c[56] = CF56_257
  c[57] = CF157
  c[58] = CF58_259
  c[59] = CF159
  c[60] = CF260
  c[61] = CF261
  c[62] = CF62_263
  c[63] = CF163
  c[64] = CF64_265
  c[65] = CF165
  c[66] = FA366
  c[67] = FA367

# ====== END Task 0 ====== 

  

