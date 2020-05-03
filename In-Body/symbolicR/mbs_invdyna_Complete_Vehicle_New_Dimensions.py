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
#	==> Generation Date : Sun May  3 18:39:10 2020
#
#	==> Project name : Complete_Vehicle_New_Dimensions
#	==> using XML input file 
#
#	==> Number of joints : 67
#
#	==> Function : F 2 : Inverse Dynamics : RNEA
#	==> Flops complexity : 5085
#
#	==> Generation Time :  0.070 seconds
#	==> Post-Processing :  0.070 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def invdyna(phi,s,tsim):
  
  Qq = phi
  
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

# = = Block_0_1_0_0_0_0 = = 
 
# Forward Kinematics 

  ALPHA33 = qdd[3]-s.g[3]
  ALPHA14 = qdd[1]*C4+qdd[2]*S4
  ALPHA24 = -(qdd[1]*S4-qdd[2]*C4)
  OM35 = qd[4]*C5
  OMp35 = -(qd[4]*qd[5]*S5-qdd[4]*C5)
  ALPHA15 = ALPHA14*C5-ALPHA33*S5
  ALPHA35 = ALPHA14*S5+ALPHA33*C5
  OM16 = qd[6]-qd[4]*S5
  OM26 = qd[5]*C6+OM35*S6
  OM36 = -(qd[5]*S6-OM35*C6)
  OMp16 = qdd[6]-qd[4]*qd[5]*C5-qdd[4]*S5
  OMp26 = C6*(qdd[5]+qd[6]*OM35)+S6*(OMp35-qd[5]*qd[6])
  OMp36 = C6*(OMp35-qd[5]*qd[6])-S6*(qdd[5]+qd[6]*OM35)
  BS16 = -(OM26*OM26+OM36*OM36)
  BS26 = OM16*OM26
  BS36 = OM16*OM36
  BS56 = -(OM16*OM16+OM36*OM36)
  BS66 = OM26*OM36
  BS96 = -(OM16*OM16+OM26*OM26)
  BETA26 = BS26-OMp36
  BETA36 = BS36+OMp26
  BETA46 = BS26+OMp36
  BETA66 = BS66-OMp16
  BETA76 = BS36-OMp26
  BETA86 = BS66+OMp16
  ALPHA26 = ALPHA24*C6+ALPHA35*S6
  ALPHA36 = -(ALPHA24*S6-ALPHA35*C6)
  OM17 = qd[7]+OM16
  OM27 = OM26*C7+OM36*S7
  OM37 = -(OM26*S7-OM36*C7)
  OMp17 = qdd[7]+OMp16
  OMp27 = C7*(OMp26+qd[7]*OM36)+S7*(OMp36-qd[7]*OM26)
  OMp37 = C7*(OMp36-qd[7]*OM26)-S7*(OMp26+qd[7]*OM36)
  BS27 = OM17*OM27
  BS57 = -(OM17*OM17+OM37*OM37)
  BETA27 = BS27-OMp37
  BETA87 = OMp17+OM27*OM37
  ALPHA17 = ALPHA15+BETA26*s.dpt[2,1]+BS16*s.dpt[1,1]
  ALPHA27 = C7*(ALPHA26+BETA46*s.dpt[1,1]+BS56*s.dpt[2,1])+S7*(ALPHA36+BETA76*s.dpt[1,1]+BETA86*s.dpt[2,1])
  ALPHA37 = C7*(ALPHA36+BETA76*s.dpt[1,1]+BETA86*s.dpt[2,1])-S7*(ALPHA26+BETA46*s.dpt[1,1]+BS56*s.dpt[2,1])
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OMp28 = C8*(OMp27-qd[8]*OM17)-S8*(OMp17+qd[8]*OM27)
  OMp38 = qdd[8]+OMp37
  ALPHA18 = C8*(ALPHA17+BETA27*s.dpt[2,18])+S8*(ALPHA27+BS57*s.dpt[2,18])
  ALPHA28 = C8*(ALPHA27+BS57*s.dpt[2,18])-S8*(ALPHA17+BETA27*s.dpt[2,18])
  ALPHA38 = ALPHA37+BETA87*s.dpt[2,18]
  OM19 = qd[9]+OM17*C8+OM27*S8
  OM39 = -(OM28*S9-OM38*C9)
  OMp19 = qdd[9]+C8*(OMp17+qd[8]*OM27)+S8*(OMp27-qd[8]*OM17)
  OMp39 = C9*(OMp38-qd[9]*OM28)-S9*(OMp28+qd[9]*OM38)
  ALPHA29 = ALPHA28*C9+ALPHA38*S9
  ALPHA39 = -(ALPHA28*S9-ALPHA38*C9)
  OM110 = OM19*C10-OM39*S10
  OM210 = qd[10]+OM28*C9+OM38*S9
  OM310 = OM19*S10+OM39*C10
  OMp110 = C10*(OMp19-qd[10]*OM39)-S10*(OMp39+qd[10]*OM19)
  OMp210 = qdd[10]+C9*(OMp28+qd[9]*OM38)+S9*(OMp38-qd[9]*OM28)
  OMp310 = C10*(OMp39+qd[10]*OM19)+S10*(OMp19-qd[10]*OM39)
  BS510 = -(OM110*OM110+OM310*OM310)
  BS610 = OM210*OM310
  BS910 = -(OM110*OM110+OM210*OM210)
  BETA210 = OM110*OM210-OMp310
  BETA310 = OMp210+OM110*OM310
  BETA610 = BS610-OMp110
  BETA810 = BS610+OMp110
  ALPHA110 = ALPHA18*C10-ALPHA39*S10
  ALPHA310 = ALPHA18*S10+ALPHA39*C10
  OM111 = qd[11]+OM110
  OM211 = OM210*C11+OM310*S11
  OM311 = -(OM210*S11-OM310*C11)
  OMp111 = qdd[11]+OMp110
  OMp211 = C11*(OMp210+qd[11]*OM310)+S11*(OMp310-qd[11]*OM210)
  OM113 = qd[13]+OM110
  OM313 = -(OM210*S13-OM310*C13)
  OMp113 = qdd[13]+OMp110
  OMp313 = C13*(OMp310-qd[13]*OM210)-S13*(OMp210+qd[13]*OM310)
  ALPHA113 = ALPHA110+BETA210*s.dpt[2,20]+BETA310*s.dpt[3,20]
  ALPHA313 = C13*(ALPHA310+BETA810*s.dpt[2,20]+BS910*s.dpt[3,20])-S13*(ALPHA29+BETA610*s.dpt[3,20]+BS510*s.dpt[2,20])
  OM114 = OM113*C14-OM313*S14
  OM214 = qd[14]+OM210*C13+OM310*S13
  OM314 = OM113*S14+OM313*C14
  OM115 = qd[15]+OM16
  OM215 = OM26*C15+OM36*S15
  OM315 = -(OM26*S15-OM36*C15)
  OMp115 = qdd[15]+OMp16
  OMp215 = C15*(OMp26+qd[15]*OM36)+S15*(OMp36-qd[15]*OM26)
  OMp315 = C15*(OMp36-qd[15]*OM26)-S15*(OMp26+qd[15]*OM36)
  BS215 = OM115*OM215
  BS515 = -(OM115*OM115+OM315*OM315)
  BETA215 = BS215-OMp315
  BETA815 = OMp115+OM215*OM315
  ALPHA115 = ALPHA15+BETA26*s.dpt[2,4]+BS16*s.dpt[1,4]
  ALPHA215 = C15*(ALPHA26+BETA46*s.dpt[1,4]+BS56*s.dpt[2,4])+S15*(ALPHA36+BETA76*s.dpt[1,4]+BETA86*s.dpt[2,4])
  ALPHA315 = C15*(ALPHA36+BETA76*s.dpt[1,4]+BETA86*s.dpt[2,4])-S15*(ALPHA26+BETA46*s.dpt[1,4]+BS56*s.dpt[2,4])
  OM216 = -(OM115*S16-OM215*C16)
  OM316 = qd[16]+OM315
  OMp216 = C16*(OMp215-qd[16]*OM115)-S16*(OMp115+qd[16]*OM215)
  OMp316 = qdd[16]+OMp315
  ALPHA116 = C16*(ALPHA115+BETA215*s.dpt[2,25])+S16*(ALPHA215+BS515*s.dpt[2,25])
  ALPHA216 = C16*(ALPHA215+BS515*s.dpt[2,25])-S16*(ALPHA115+BETA215*s.dpt[2,25])
  ALPHA316 = ALPHA315+BETA815*s.dpt[2,25]
  OM117 = qd[17]+OM115*C16+OM215*S16
  OM317 = -(OM216*S17-OM316*C17)
  OMp117 = qdd[17]+C16*(OMp115+qd[16]*OM215)+S16*(OMp215-qd[16]*OM115)
  OMp317 = C17*(OMp316-qd[17]*OM216)-S17*(OMp216+qd[17]*OM316)
  ALPHA217 = ALPHA216*C17+ALPHA316*S17
  ALPHA317 = -(ALPHA216*S17-ALPHA316*C17)
  OM118 = OM117*C18-OM317*S18
  OM218 = qd[18]+OM216*C17+OM316*S17
  OM318 = OM117*S18+OM317*C18
  OMp118 = C18*(OMp117-qd[18]*OM317)-S18*(OMp317+qd[18]*OM117)
  OMp218 = qdd[18]+C17*(OMp216+qd[17]*OM316)+S17*(OMp316-qd[17]*OM216)
  OMp318 = C18*(OMp317+qd[18]*OM117)+S18*(OMp117-qd[18]*OM317)
  BS518 = -(OM118*OM118+OM318*OM318)
  BS618 = OM218*OM318
  BS918 = -(OM118*OM118+OM218*OM218)
  BETA218 = OM118*OM218-OMp318
  BETA318 = OMp218+OM118*OM318
  BETA618 = BS618-OMp118
  BETA818 = BS618+OMp118
  ALPHA118 = ALPHA116*C18-ALPHA317*S18
  ALPHA318 = ALPHA116*S18+ALPHA317*C18
  OM119 = qd[19]+OM118
  OM219 = OM218*C19+OM318*S19
  OM319 = -(OM218*S19-OM318*C19)
  OMp119 = qdd[19]+OMp118
  OMp219 = C19*(OMp218+qd[19]*OM318)+S19*(OMp318-qd[19]*OM218)
  OM121 = qd[21]+OM118
  OM321 = -(OM218*S21-OM318*C21)
  OMp121 = qdd[21]+OMp118
  OMp321 = C21*(OMp318-qd[21]*OM218)-S21*(OMp218+qd[21]*OM318)
  ALPHA121 = ALPHA118+BETA218*s.dpt[2,27]+BETA318*s.dpt[3,27]
  ALPHA321 = C21*(ALPHA318+BETA818*s.dpt[2,27]+BS918*s.dpt[3,27])-S21*(ALPHA217+BETA618*s.dpt[3,27]+BS518*s.dpt[2,27])
  OM122 = OM121*C22-OM321*S22
  OM222 = qd[22]+OM218*C21+OM318*S21
  OM322 = OM121*S22+OM321*C22
  OM123 = qd[23]+OM16
  OM223 = OM26*C23+OM36*S23
  ALPHA123 = ALPHA15+BETA26*s.dpt[2,6]+BETA36*s.dpt[3,6]+BS16*s.dpt[1,6]
  ALPHA223 = C23*(ALPHA26+BETA46*s.dpt[1,6]+BETA66*s.dpt[3,6]+BS56*s.dpt[2,6])+S23*(ALPHA36+BETA76*s.dpt[1,6]+BETA86*\
   s.dpt[2,6]+BS96*s.dpt[3,6])
  OM124 = OM123*C24+OM223*S24
  OM224 = -(OM123*S24-OM223*C24)
  OM324 = qd[24]-OM26*S23+OM36*C23
  OMp124 = C24*(qdd[23]+OMp16+qd[24]*OM223)-S24*(qd[24]*OM123-C23*(OMp26+qd[23]*OM36)-S23*(OMp36-qd[23]*OM26))
  OMp324 = qdd[24]+C23*(OMp36-qd[23]*OM26)-S23*(OMp26+qd[23]*OM36)
  OM125 = qd[25]+OM16
  OM225 = OM26*C25+OM36*S25
  ALPHA125 = ALPHA15+BETA26*s.dpt[2,8]+BETA36*s.dpt[3,8]+BS16*s.dpt[1,8]
  ALPHA225 = C25*(ALPHA26+BETA46*s.dpt[1,8]+BETA66*s.dpt[3,8]+BS56*s.dpt[2,8])+S25*(ALPHA36+BETA76*s.dpt[1,8]+BETA86*\
   s.dpt[2,8]+BS96*s.dpt[3,8])
  OM126 = OM125*C26+OM225*S26
  OM226 = -(OM125*S26-OM225*C26)
  OM326 = qd[26]-OM26*S25+OM36*C25
  OMp126 = C26*(qdd[25]+OMp16+qd[26]*OM225)-S26*(qd[26]*OM125-C25*(OMp26+qd[25]*OM36)-S25*(OMp36-qd[25]*OM26))
  OMp326 = qdd[26]+C25*(OMp36-qd[25]*OM26)-S25*(OMp26+qd[25]*OM36)
  OM127 = qd[27]+OM16
  OM227 = OM26*C27+OM36*S27
  ALPHA127 = ALPHA15+BETA26*s.dpt[2,9]+BETA36*s.dpt[3,9]+BS16*s.dpt[1,9]
  ALPHA227 = C27*(ALPHA26+BETA46*s.dpt[1,9]+BETA66*s.dpt[3,9]+BS56*s.dpt[2,9])+S27*(ALPHA36+BETA76*s.dpt[1,9]+BETA86*\
   s.dpt[2,9]+BS96*s.dpt[3,9])
  OM128 = OM127*C28+OM227*S28
  OM228 = -(OM127*S28-OM227*C28)
  OM328 = qd[28]-OM26*S27+OM36*C27
  OMp128 = C28*(qdd[27]+OMp16+qd[28]*OM227)-S28*(qd[28]*OM127-C27*(OMp26+qd[27]*OM36)-S27*(OMp36-qd[27]*OM26))
  OMp328 = qdd[28]+C27*(OMp36-qd[27]*OM26)-S27*(OMp26+qd[27]*OM36)
  OM129 = qd[29]+OM16
  OM229 = OM26*C29+OM36*S29
  OMp129 = qdd[29]+OMp16
  OMp229 = C29*(OMp26+qd[29]*OM36)+S29*(OMp36-qd[29]*OM26)
  ALPHA129 = ALPHA15+BETA26*s.dpt[2,10]+BS16*s.dpt[1,10]
  ALPHA229 = C29*(ALPHA26+BETA46*s.dpt[1,10]+BS56*s.dpt[2,10])+S29*(ALPHA36+BETA76*s.dpt[1,10]+BETA86*s.dpt[2,10])
  ALPHA329 = C29*(ALPHA36+BETA76*s.dpt[1,10]+BETA86*s.dpt[2,10])-S29*(ALPHA26+BETA46*s.dpt[1,10]+BS56*s.dpt[2,10])
  OM130 = OM129*C30+OM229*S30
  OM230 = -(OM129*S30-OM229*C30)
  OM330 = qd[30]-OM26*S29+OM36*C29
  OMp130 = C30*(OMp129+qd[30]*OM229)+S30*(OMp229-qd[30]*OM129)
  OMp230 = C30*(OMp229-qd[30]*OM129)-S30*(OMp129+qd[30]*OM229)
  OMp330 = qdd[30]+C29*(OMp36-qd[29]*OM26)-S29*(OMp26+qd[29]*OM36)
  BS530 = -(OM130*OM130+OM330*OM330)
  BETA230 = OM130*OM230-OMp330
  BETA830 = OMp130+OM230*OM330
  ALPHA130 = ALPHA129*C30+ALPHA229*S30
  ALPHA230 = -(ALPHA129*S30-ALPHA229*C30)
  OM131 = qd[31]+OM130
  OM331 = -(OM230*S31-OM330*C31)
  OMp131 = qdd[31]+OMp130
  OMp331 = C31*(OMp330-qd[31]*OM230)-S31*(OMp230+qd[31]*OM330)
  ALPHA131 = ALPHA130+BETA230*s.dpt[2,35]
  ALPHA231 = C31*(ALPHA230+BS530*s.dpt[2,35])+S31*(ALPHA329+BETA830*s.dpt[2,35])
  ALPHA331 = C31*(ALPHA329+BETA830*s.dpt[2,35])-S31*(ALPHA230+BS530*s.dpt[2,35])
  OM132 = OM131*C32-OM331*S32
  OM232 = qd[32]+OM230*C31+OM330*S31
  OMp132 = C32*(OMp131-qd[32]*OM331)-S32*(OMp331+qd[32]*OM131)
  OMp232 = qdd[32]+C31*(OMp230+qd[31]*OM330)+S31*(OMp330-qd[31]*OM230)
  ALPHA132 = ALPHA131*C32-ALPHA331*S32
  ALPHA332 = ALPHA131*S32+ALPHA331*C32
  OM133 = OM132*C33+OM232*S33
  OM233 = -(OM132*S33-OM232*C33)
  OM333 = qd[33]+OM131*S32+OM331*C32
  OMp133 = C33*(OMp132+qd[33]*OM232)+S33*(OMp232-qd[33]*OM132)
  OMp233 = C33*(OMp232-qd[33]*OM132)-S33*(OMp132+qd[33]*OM232)
  OMp333 = qdd[33]+C32*(OMp331+qd[32]*OM131)+S32*(OMp131-qd[32]*OM331)
  BS533 = -(OM133*OM133+OM333*OM333)
  BS633 = OM233*OM333
  BS933 = -(OM133*OM133+OM233*OM233)
  BETA233 = OM133*OM233-OMp333
  BETA333 = OMp233+OM133*OM333
  BETA633 = BS633-OMp133
  BETA833 = BS633+OMp133
  ALPHA133 = ALPHA132*C33+ALPHA231*S33
  ALPHA233 = -(ALPHA132*S33-ALPHA231*C33)
  OM134 = qd[34]+OM133
  OM234 = OM233*C34+OM333*S34
  OM334 = -(OM233*S34-OM333*C34)
  OMp134 = qdd[34]+OMp133
  OMp234 = C34*(OMp233+qd[34]*OM333)+S34*(OMp333-qd[34]*OM233)
  OM136 = qd[36]+OM133
  OM336 = -(OM233*S36-OM333*C36)
  OMp136 = qdd[36]+OMp133
  OMp336 = C36*(OMp333-qd[36]*OM233)-S36*(OMp233+qd[36]*OM333)
  ALPHA136 = ALPHA133+BETA233*s.dpt[2,37]+BETA333*s.dpt[3,37]
  ALPHA336 = C36*(ALPHA332+BETA833*s.dpt[2,37]+BS933*s.dpt[3,37])-S36*(ALPHA233+BETA633*s.dpt[3,37]+BS533*s.dpt[2,37])
  OM137 = OM136*C37-OM336*S37
  OM237 = qd[37]+OM233*C36+OM333*S36
  OM337 = OM136*S37+OM336*C37
  OM138 = qd[38]+OM16
  OM238 = OM26*C38+OM36*S38
  ALPHA138 = ALPHA15+BETA26*s.dpt[2,11]+BETA36*s.dpt[3,11]+BS16*s.dpt[1,11]
  ALPHA238 = C38*(ALPHA26+BETA46*s.dpt[1,11]+BETA66*s.dpt[3,11]+BS56*s.dpt[2,11])+S38*(ALPHA36+BETA76*s.dpt[1,11]+BETA86\
   *s.dpt[2,11]+BS96*s.dpt[3,11])
  OM139 = OM138*C39+OM238*S39
  OM239 = -(OM138*S39-OM238*C39)
  OM339 = qd[39]-OM26*S38+OM36*C38
  OMp139 = C39*(qdd[38]+OMp16+qd[39]*OM238)-S39*(qd[39]*OM138-C38*(OMp26+qd[38]*OM36)-S38*(OMp36-qd[38]*OM26))
  OMp339 = qdd[39]+C38*(OMp36-qd[38]*OM26)-S38*(OMp26+qd[38]*OM36)
  OM140 = qd[40]+OM16
  OM240 = OM26*C40+OM36*S40
  OMp140 = qdd[40]+OMp16
  OMp240 = C40*(OMp26+qd[40]*OM36)+S40*(OMp36-qd[40]*OM26)
  ALPHA140 = ALPHA15+BETA26*s.dpt[2,12]+BS16*s.dpt[1,12]
  ALPHA240 = C40*(ALPHA26+BETA46*s.dpt[1,12]+BS56*s.dpt[2,12])+S40*(ALPHA36+BETA76*s.dpt[1,12]+BETA86*s.dpt[2,12])
  ALPHA340 = C40*(ALPHA36+BETA76*s.dpt[1,12]+BETA86*s.dpt[2,12])-S40*(ALPHA26+BETA46*s.dpt[1,12]+BS56*s.dpt[2,12])
  OM141 = OM140*C41+OM240*S41
  OM241 = -(OM140*S41-OM240*C41)
  OM341 = qd[41]-OM26*S40+OM36*C40
  OMp141 = C41*(OMp140+qd[41]*OM240)+S41*(OMp240-qd[41]*OM140)
  OMp241 = C41*(OMp240-qd[41]*OM140)-S41*(OMp140+qd[41]*OM240)
  OMp341 = qdd[41]+C40*(OMp36-qd[40]*OM26)-S40*(OMp26+qd[40]*OM36)
  BS541 = -(OM141*OM141+OM341*OM341)
  BETA241 = OM141*OM241-OMp341
  BETA841 = OMp141+OM241*OM341
  ALPHA141 = ALPHA140*C41+ALPHA240*S41
  ALPHA241 = -(ALPHA140*S41-ALPHA240*C41)
  OM142 = qd[42]+OM141
  OM342 = -(OM241*S42-OM341*C42)
  OMp142 = qdd[42]+OMp141
  OMp342 = C42*(OMp341-qd[42]*OM241)-S42*(OMp241+qd[42]*OM341)
  ALPHA142 = ALPHA141+BETA241*s.dpt[2,44]
  ALPHA242 = C42*(ALPHA241+BS541*s.dpt[2,44])+S42*(ALPHA340+BETA841*s.dpt[2,44])
  ALPHA342 = C42*(ALPHA340+BETA841*s.dpt[2,44])-S42*(ALPHA241+BS541*s.dpt[2,44])
  OM143 = OM142*C43-OM342*S43
  OM243 = qd[43]+OM241*C42+OM341*S42
  OMp143 = C43*(OMp142-qd[43]*OM342)-S43*(OMp342+qd[43]*OM142)
  OMp243 = qdd[43]+C42*(OMp241+qd[42]*OM341)+S42*(OMp341-qd[42]*OM241)
  ALPHA143 = ALPHA142*C43-ALPHA342*S43
  ALPHA343 = ALPHA142*S43+ALPHA342*C43
  OM144 = OM143*C44+OM243*S44
  OM244 = -(OM143*S44-OM243*C44)
  OM344 = qd[44]+OM142*S43+OM342*C43
  OMp144 = C44*(OMp143+qd[44]*OM243)+S44*(OMp243-qd[44]*OM143)
  OMp244 = C44*(OMp243-qd[44]*OM143)-S44*(OMp143+qd[44]*OM243)
  OMp344 = qdd[44]+C43*(OMp342+qd[43]*OM142)+S43*(OMp142-qd[43]*OM342)
  BS544 = -(OM144*OM144+OM344*OM344)
  BS644 = OM244*OM344
  BS944 = -(OM144*OM144+OM244*OM244)
  BETA244 = OM144*OM244-OMp344
  BETA344 = OMp244+OM144*OM344
  BETA644 = BS644-OMp144
  BETA844 = BS644+OMp144
  ALPHA144 = ALPHA143*C44+ALPHA242*S44
  ALPHA244 = -(ALPHA143*S44-ALPHA242*C44)
  OM145 = qd[45]+OM144
  OM245 = OM244*C45+OM344*S45
  OM345 = -(OM244*S45-OM344*C45)
  OMp145 = qdd[45]+OMp144
  OMp245 = C45*(OMp244+qd[45]*OM344)+S45*(OMp344-qd[45]*OM244)
  OM147 = qd[47]+OM144
  OM347 = -(OM244*S47-OM344*C47)
  OMp147 = qdd[47]+OMp144
  OMp347 = C47*(OMp344-qd[47]*OM244)-S47*(OMp244+qd[47]*OM344)
  ALPHA147 = ALPHA144+BETA244*s.dpt[2,48]+BETA344*s.dpt[3,48]
  ALPHA347 = C47*(ALPHA343+BETA844*s.dpt[2,48]+BS944*s.dpt[3,48])-S47*(ALPHA244+BETA644*s.dpt[3,48]+BS544*s.dpt[2,48])
  OM148 = OM147*C48-OM347*S48
  OM248 = qd[48]+OM244*C47+OM344*S47
  OM348 = OM147*S48+OM347*C48
  BS549 = -(OM16*OM16+OM36*OM36)
  BETA249 = OM16*OM26-OMp36
  BETA849 = OMp16+OM26*OM36
  ALPHA149 = ALPHA15+q[49]*BETA26-(2.0)*qd[49]*OM36+BS16*s.dpt[1,13]
  ALPHA249 = qdd[49]+ALPHA26+q[49]*BS56+BETA46*s.dpt[1,13]
  ALPHA349 = ALPHA36+q[49]*BETA86+(2.0)*qd[49]*OM16+BETA76*s.dpt[1,13]
  OM250 = -(OM16*S50-OM26*C50)
  OM350 = qd[50]+OM36
  ALPHA250 = C50*(ALPHA249+BS549*s.dpt[2,52])-S50*(ALPHA149+BETA249*s.dpt[2,52])
  ALPHA350 = ALPHA349+BETA849*s.dpt[2,52]
  OM151 = qd[51]+OM16*C50+OM26*S50
  OM251 = OM250*C51+OM350*S51
  OM351 = -(OM250*S51-OM350*C51)
  OMp151 = qdd[51]+C50*(OMp16+qd[50]*OM26)+S50*(OMp26-qd[50]*OM16)
  OMp351 = C51*(qdd[50]+OMp36-qd[51]*OM250)-S51*(qd[51]*OM350+C50*(OMp26-qd[50]*OM16)-S50*(OMp16+qd[50]*OM26))
  OM252 = -(OM16*S52-OM26*C52)
  OM352 = qd[52]+OM36
  ALPHA252 = C52*(ALPHA249+BS549*s.dpt[2,53])-S52*(ALPHA149+BETA249*s.dpt[2,53])
  ALPHA352 = ALPHA349+BETA849*s.dpt[2,53]
  OM153 = qd[53]+OM16*C52+OM26*S52
  OM253 = OM252*C53+OM352*S53
  OM353 = -(OM252*S53-OM352*C53)
  OMp153 = qdd[53]+C52*(OMp16+qd[52]*OM26)+S52*(OMp26-qd[52]*OM16)
  OMp353 = C53*(qdd[52]+OMp36-qd[53]*OM252)-S53*(qd[53]*OM352+C52*(OMp26-qd[52]*OM16)-S52*(OMp16+qd[52]*OM26))
  OM154 = OM16*C54-OM36*S54
  OM254 = qd[54]+OM26
  OM354 = OM16*S54+OM36*C54
  OMp154 = C54*(OMp16-qd[54]*OM36)-S54*(OMp36+qd[54]*OM16)
  OMp254 = qdd[54]+OMp26
  OMp354 = C54*(OMp36+qd[54]*OM16)+S54*(OMp16-qd[54]*OM36)
  BS154 = -(OM254*OM254+OM354*OM354)
  BS254 = OM154*OM254
  BS554 = -(OM154*OM154+OM354*OM354)
  BETA254 = BS254-OMp354
  BETA454 = BS254+OMp354
  BETA754 = OM154*OM354-OMp254
  BETA854 = OMp154+OM254*OM354
  ALPHA154 = C54*(ALPHA15+BETA36*s.dpt[3,14]+BS16*s.dpt[1,14])-S54*(ALPHA36+BETA76*s.dpt[1,14]+BS96*s.dpt[3,14])
  ALPHA254 = ALPHA26+BETA46*s.dpt[1,14]+BETA66*s.dpt[3,14]
  ALPHA354 = C54*(ALPHA36+BETA76*s.dpt[1,14]+BS96*s.dpt[3,14])+S54*(ALPHA15+BETA36*s.dpt[3,14]+BS16*s.dpt[1,14])
  OM155 = OM154*C55-OM354*S55
  OM255 = qd[55]+OM254
  OM355 = OM154*S55+OM354*C55
  OMp155 = C55*(OMp154-qd[55]*OM354)-S55*(OMp354+qd[55]*OM154)
  OMp255 = qdd[55]+OMp254
  OMp355 = C55*(OMp354+qd[55]*OM154)+S55*(OMp154-qd[55]*OM354)
  BS155 = -(OM255*OM255+OM355*OM355)
  BS255 = OM155*OM255
  BS555 = -(OM155*OM155+OM355*OM355)
  BETA255 = BS255-OMp355
  BETA455 = BS255+OMp355
  BETA755 = OM155*OM355-OMp255
  BETA855 = OMp155+OM255*OM355
  ALPHA155 = ALPHA154*C55-ALPHA354*S55
  ALPHA355 = ALPHA154*S55+ALPHA354*C55
  OM256 = qd[56]+OM255
  OM356 = OM155*S56+OM355*C56
  ALPHA256 = ALPHA254+BETA455*s.dpt[1,57]+BS555*s.dpt[2,57]
  ALPHA356 = C56*(ALPHA355+BETA755*s.dpt[1,57]+BETA855*s.dpt[2,57])+S56*(ALPHA155+BETA255*s.dpt[2,57]+BS155*s.dpt[1,57])
  OM157 = qd[57]+OM155*C56-OM355*S56
  OM257 = OM256*C57+OM356*S57
  OM357 = -(OM256*S57-OM356*C57)
  OMp157 = qdd[57]+C56*(OMp155-qd[56]*OM355)-S56*(OMp355+qd[56]*OM155)
  OMp257 = C57*(qdd[56]+OMp255+qd[57]*OM356)-S57*(qd[57]*OM256-C56*(OMp355+qd[56]*OM155)-S56*(OMp155-qd[56]*OM355))
  OM258 = qd[58]+OM254
  OM358 = OM154*S58+OM354*C58
  ALPHA258 = ALPHA254+BETA454*s.dpt[1,56]+BS554*s.dpt[2,56]
  ALPHA358 = C58*(ALPHA354+BETA754*s.dpt[1,56]+BETA854*s.dpt[2,56])+S58*(ALPHA154+BETA254*s.dpt[2,56]+BS154*s.dpt[1,56])
  OM159 = qd[59]+OM154*C58-OM354*S58
  OM259 = OM258*C59+OM358*S59
  OM359 = -(OM258*S59-OM358*C59)
  OMp159 = qdd[59]+C58*(OMp154-qd[58]*OM354)-S58*(OMp354+qd[58]*OM154)
  OMp259 = C59*(qdd[58]+OMp254+qd[59]*OM358)-S59*(qd[59]*OM258-C58*(OMp354+qd[58]*OM154)-S58*(OMp154-qd[58]*OM354))
  OM160 = OM16*C60-OM36*S60
  OM260 = qd[60]+OM26
  OM360 = OM16*S60+OM36*C60
  OMp160 = C60*(OMp16-qd[60]*OM36)-S60*(OMp36+qd[60]*OM16)
  OMp260 = qdd[60]+OMp26
  OMp360 = C60*(OMp36+qd[60]*OM16)+S60*(OMp16-qd[60]*OM36)
  BS160 = -(OM260*OM260+OM360*OM360)
  BS260 = OM160*OM260
  BS560 = -(OM160*OM160+OM360*OM360)
  BETA260 = BS260-OMp360
  BETA460 = BS260+OMp360
  BETA760 = OM160*OM360-OMp260
  BETA860 = OMp160+OM260*OM360
  ALPHA160 = C60*(ALPHA15+BETA36*s.dpt[3,15]+BS16*s.dpt[1,15])-S60*(ALPHA36+BETA76*s.dpt[1,15]+BS96*s.dpt[3,15])
  ALPHA260 = ALPHA26+BETA46*s.dpt[1,15]+BETA66*s.dpt[3,15]
  ALPHA360 = C60*(ALPHA36+BETA76*s.dpt[1,15]+BS96*s.dpt[3,15])+S60*(ALPHA15+BETA36*s.dpt[3,15]+BS16*s.dpt[1,15])
  OM161 = OM160*C61-OM360*S61
  OM261 = qd[61]+OM260
  OM361 = OM160*S61+OM360*C61
  OMp161 = C61*(OMp160-qd[61]*OM360)-S61*(OMp360+qd[61]*OM160)
  OMp261 = qdd[61]+OMp260
  OMp361 = C61*(OMp360+qd[61]*OM160)+S61*(OMp160-qd[61]*OM360)
  BS161 = -(OM261*OM261+OM361*OM361)
  BS261 = OM161*OM261
  BS561 = -(OM161*OM161+OM361*OM361)
  BETA261 = BS261-OMp361
  BETA461 = BS261+OMp361
  BETA761 = OM161*OM361-OMp261
  BETA861 = OMp161+OM261*OM361
  ALPHA161 = ALPHA160*C61-ALPHA360*S61
  ALPHA361 = ALPHA160*S61+ALPHA360*C61
  OM262 = qd[62]+OM261
  OM362 = OM161*S62+OM361*C62
  ALPHA262 = ALPHA260+BETA461*s.dpt[1,61]+BS561*s.dpt[2,61]
  ALPHA362 = C62*(ALPHA361+BETA761*s.dpt[1,61]+BETA861*s.dpt[2,61])+S62*(ALPHA161+BETA261*s.dpt[2,61]+BS161*s.dpt[1,61])
  OM163 = qd[63]+OM161*C62-OM361*S62
  OM263 = OM262*C63+OM362*S63
  OM363 = -(OM262*S63-OM362*C63)
  OMp163 = qdd[63]+C62*(OMp161-qd[62]*OM361)-S62*(OMp361+qd[62]*OM161)
  OMp263 = C63*(qdd[62]+OMp261+qd[63]*OM362)-S63*(qd[63]*OM262-C62*(OMp361+qd[62]*OM161)-S62*(OMp161-qd[62]*OM361))
  OM264 = qd[64]+OM260
  OM364 = OM160*S64+OM360*C64
  ALPHA264 = ALPHA260+BETA460*s.dpt[1,60]+BS560*s.dpt[2,60]
  ALPHA364 = C64*(ALPHA360+BETA760*s.dpt[1,60]+BETA860*s.dpt[2,60])+S64*(ALPHA160+BETA260*s.dpt[2,60]+BS160*s.dpt[1,60])
  OM165 = qd[65]+OM160*C64-OM360*S64
  OM265 = OM264*C65+OM364*S65
  OM365 = -(OM264*S65-OM364*C65)
  OMp165 = qdd[65]+C64*(OMp160-qd[64]*OM360)-S64*(OMp360+qd[64]*OM160)
  OMp265 = C65*(qdd[64]+OMp260+qd[65]*OM364)-S65*(qd[65]*OM264-C64*(OMp360+qd[64]*OM160)-S64*(OMp160-qd[64]*OM360))
 
# Backward Dynamics 

  Fs367 = -(s.frc[3,67]-s.m[67]*(qdd[67]-s.g[3]))
  Fs366 = -(s.frc[3,66]-s.m[66]*(qdd[66]-s.g[3]))
  Fs165 = -(s.frc[1,65]-s.m[65]*(s.l[3,65]*(OMp265+OM165*OM365)+C64*(ALPHA160+BETA260*s.dpt[2,60]+BS160*s.dpt[1,60])-S64\
   *(ALPHA360+BETA760*s.dpt[1,60]+BETA860*s.dpt[2,60])))
  Fs265 = -(s.frc[2,65]-s.m[65]*(ALPHA264*C65+ALPHA364*S65-s.l[3,65]*(OMp165-OM265*OM365)))
  Fs365 = -(s.frc[3,65]+s.m[65]*(ALPHA264*S65-ALPHA364*C65+s.l[3,65]*(OM165*OM165+OM265*OM265)))
  Cq165 = -(s.trq[1,65]-s.In[1,65]*OMp165+s.In[5,65]*OM265*OM365+Fs265*s.l[3,65])
  Cq265 = -(s.trq[2,65]-s.In[1,65]*OM165*OM365-s.In[5,65]*OMp265-Fs165*s.l[3,65])
  Cq365 = -(s.trq[3,65]+OM165*OM265*(s.In[1,65]-s.In[5,65]))
  Fq264 = Fs265*C65-Fs365*S65
  Fq364 = Fs265*S65+Fs365*C65
  Cq264 = Cq265*C65-Cq365*S65
  Cq364 = Cq265*S65+Cq365*C65
  Fs163 = -(s.frc[1,63]-s.m[63]*(s.l[3,63]*(OMp263+OM163*OM363)+C62*(ALPHA161+BETA261*s.dpt[2,61]+BS161*s.dpt[1,61])-S62\
   *(ALPHA361+BETA761*s.dpt[1,61]+BETA861*s.dpt[2,61])))
  Fs263 = -(s.frc[2,63]-s.m[63]*(ALPHA262*C63+ALPHA362*S63-s.l[3,63]*(OMp163-OM263*OM363)))
  Fs363 = -(s.frc[3,63]+s.m[63]*(ALPHA262*S63-ALPHA362*C63+s.l[3,63]*(OM163*OM163+OM263*OM263)))
  Cq163 = -(s.trq[1,63]-s.In[1,63]*OMp163+s.In[5,63]*OM263*OM363+Fs263*s.l[3,63])
  Cq263 = -(s.trq[2,63]-s.In[1,63]*OM163*OM363-s.In[5,63]*OMp263-Fs163*s.l[3,63])
  Cq363 = -(s.trq[3,63]+OM163*OM263*(s.In[1,63]-s.In[5,63]))
  Fq262 = Fs263*C63-Fs363*S63
  Fq362 = Fs263*S63+Fs363*C63
  Cq262 = Cq263*C63-Cq363*S63
  Cq362 = Cq263*S63+Cq363*C63
  Fs161 = -(s.frc[1,61]-s.m[61]*(ALPHA161+BETA261*s.l[2,61]+BS161*s.l[1,61]))
  Fs261 = -(s.frc[2,61]-s.m[61]*(ALPHA260+BETA461*s.l[1,61]+BS561*s.l[2,61]))
  Fs361 = -(s.frc[3,61]-s.m[61]*(ALPHA361+BETA761*s.l[1,61]+BETA861*s.l[2,61]))
  Fq161 = Fs161+Fq362*S62+Fs163*C62
  Fq361 = Fs361+Fq362*C62-Fs163*S62
  Cq161 = -(s.trq[1,61]+s.In[5,61]*OM261*OM361-Cq163*C62-Cq362*S62-Fs361*s.l[2,61]-s.dpt[2,61]*(Fq362*C62-Fs163*S62))
  Cq261 = -(s.trq[2,61]-Cq262-s.In[5,61]*OMp261+Fs361*s.l[1,61]+s.dpt[1,61]*(Fq362*C62-Fs163*S62))
  Cq361 = -(s.trq[3,61]-s.In[5,61]*OM161*OM261+Cq163*S62-Cq362*C62-Fq262*s.dpt[1,61]+Fs161*s.l[2,61]-Fs261*s.l[1,61]+\
   s.dpt[2,61]*(Fq362*S62+Fs163*C62))
  Fs160 = -(s.frc[1,60]-s.m[60]*(ALPHA160+BETA260*s.l[2,60]+BS160*s.l[1,60]))
  Fs260 = -(s.frc[2,60]-s.m[60]*(ALPHA260+BETA460*s.l[1,60]+BS560*s.l[2,60]))
  Fs360 = -(s.frc[3,60]-s.m[60]*(ALPHA360+BETA760*s.l[1,60]+BETA860*s.l[2,60]))
  Fq160 = Fs160+Fq161*C61+Fq361*S61+Fq364*S64+Fs165*C64
  Fq260 = Fq262+Fq264+Fs260+Fs261
  Fq360 = Fs360-Fq161*S61+Fq361*C61+Fq364*C64-Fs165*S64
  Cq160 = -(s.trq[1,60]+s.In[5,60]*OM260*OM360-Cq161*C61-Cq165*C64-Cq361*S61-Cq364*S64-Fs360*s.l[2,60]-s.dpt[2,60]*(\
   Fq364*C64-Fs165*S64))
  Cq260 = -(s.trq[2,60]-Cq261-Cq264-s.In[5,60]*OMp260+Fs360*s.l[1,60]+s.dpt[1,60]*(Fq364*C64-Fs165*S64))
  Cq360 = -(s.trq[3,60]-s.In[5,60]*OM160*OM260+Cq161*S61+Cq165*S64-Cq361*C61-Cq364*C64-Fq264*s.dpt[1,60]+Fs160*s.l[2,60]\
   -Fs260*s.l[1,60]+s.dpt[2,60]*(Fq364*S64+Fs165*C64))
  Fs159 = -(s.frc[1,59]-s.m[59]*(s.l[3,59]*(OMp259+OM159*OM359)+C58*(ALPHA154+BETA254*s.dpt[2,56]+BS154*s.dpt[1,56])-S58\
   *(ALPHA354+BETA754*s.dpt[1,56]+BETA854*s.dpt[2,56])))
  Fs259 = -(s.frc[2,59]-s.m[59]*(ALPHA258*C59+ALPHA358*S59-s.l[3,59]*(OMp159-OM259*OM359)))
  Fs359 = -(s.frc[3,59]+s.m[59]*(ALPHA258*S59-ALPHA358*C59+s.l[3,59]*(OM159*OM159+OM259*OM259)))
  Cq159 = -(s.trq[1,59]-s.In[1,59]*OMp159+s.In[5,59]*OM259*OM359+Fs259*s.l[3,59])
  Cq259 = -(s.trq[2,59]-s.In[1,59]*OM159*OM359-s.In[5,59]*OMp259-Fs159*s.l[3,59])
  Cq359 = -(s.trq[3,59]+OM159*OM259*(s.In[1,59]-s.In[5,59]))
  Fq258 = Fs259*C59-Fs359*S59
  Fq358 = Fs259*S59+Fs359*C59
  Cq258 = Cq259*C59-Cq359*S59
  Cq358 = Cq259*S59+Cq359*C59
  Fs157 = -(s.frc[1,57]-s.m[57]*(s.l[3,57]*(OMp257+OM157*OM357)+C56*(ALPHA155+BETA255*s.dpt[2,57]+BS155*s.dpt[1,57])-S56\
   *(ALPHA355+BETA755*s.dpt[1,57]+BETA855*s.dpt[2,57])))
  Fs257 = -(s.frc[2,57]-s.m[57]*(ALPHA256*C57+ALPHA356*S57-s.l[3,57]*(OMp157-OM257*OM357)))
  Fs357 = -(s.frc[3,57]+s.m[57]*(ALPHA256*S57-ALPHA356*C57+s.l[3,57]*(OM157*OM157+OM257*OM257)))
  Cq157 = -(s.trq[1,57]-s.In[1,57]*OMp157+s.In[5,57]*OM257*OM357+Fs257*s.l[3,57])
  Cq257 = -(s.trq[2,57]-s.In[1,57]*OM157*OM357-s.In[5,57]*OMp257-Fs157*s.l[3,57])
  Cq357 = -(s.trq[3,57]+OM157*OM257*(s.In[1,57]-s.In[5,57]))
  Fq256 = Fs257*C57-Fs357*S57
  Fq356 = Fs257*S57+Fs357*C57
  Cq256 = Cq257*C57-Cq357*S57
  Cq356 = Cq257*S57+Cq357*C57
  Fs155 = -(s.frc[1,55]-s.m[55]*(ALPHA155+BETA255*s.l[2,55]+BS155*s.l[1,55]))
  Fs255 = -(s.frc[2,55]-s.m[55]*(ALPHA254+BETA455*s.l[1,55]+BS555*s.l[2,55]))
  Fs355 = -(s.frc[3,55]-s.m[55]*(ALPHA355+BETA755*s.l[1,55]+BETA855*s.l[2,55]))
  Fq155 = Fs155+Fq356*S56+Fs157*C56
  Fq355 = Fs355+Fq356*C56-Fs157*S56
  Cq155 = -(s.trq[1,55]+s.In[5,55]*OM255*OM355-Cq157*C56-Cq356*S56-Fs355*s.l[2,55]-s.dpt[2,57]*(Fq356*C56-Fs157*S56))
  Cq255 = -(s.trq[2,55]-Cq256-s.In[5,55]*OMp255+Fs355*s.l[1,55]+s.dpt[1,57]*(Fq356*C56-Fs157*S56))
  Cq355 = -(s.trq[3,55]-s.In[5,55]*OM155*OM255+Cq157*S56-Cq356*C56-Fq256*s.dpt[1,57]+Fs155*s.l[2,55]-Fs255*s.l[1,55]+\
   s.dpt[2,57]*(Fq356*S56+Fs157*C56))
  Fs154 = -(s.frc[1,54]-s.m[54]*(ALPHA154+BETA254*s.l[2,54]+BS154*s.l[1,54]))
  Fs254 = -(s.frc[2,54]-s.m[54]*(ALPHA254+BETA454*s.l[1,54]+BS554*s.l[2,54]))
  Fs354 = -(s.frc[3,54]-s.m[54]*(ALPHA354+BETA754*s.l[1,54]+BETA854*s.l[2,54]))
  Fq154 = Fs154+Fq155*C55+Fq355*S55+Fq358*S58+Fs159*C58
  Fq254 = Fq256+Fq258+Fs254+Fs255
  Fq354 = Fs354-Fq155*S55+Fq355*C55+Fq358*C58-Fs159*S58
  Cq154 = -(s.trq[1,54]+s.In[5,54]*OM254*OM354-Cq155*C55-Cq159*C58-Cq355*S55-Cq358*S58-Fs354*s.l[2,54]-s.dpt[2,56]*(\
   Fq358*C58-Fs159*S58))
  Cq254 = -(s.trq[2,54]-Cq255-Cq258-s.In[5,54]*OMp254+Fs354*s.l[1,54]+s.dpt[1,56]*(Fq358*C58-Fs159*S58))
  Cq354 = -(s.trq[3,54]-s.In[5,54]*OM154*OM254+Cq155*S55+Cq159*S58-Cq355*C55-Cq358*C58-Fq258*s.dpt[1,56]+Fs154*s.l[2,54]\
   -Fs254*s.l[1,54]+s.dpt[2,56]*(Fq358*S58+Fs159*C58))
  Fs153 = -(s.frc[1,53]+s.m[53]*(s.l[2,53]*(OMp353-OM153*OM253)-C52*(ALPHA149+BETA249*s.dpt[2,53])-S52*(ALPHA249+BS549*\
   s.dpt[2,53])))
  Fs253 = -(s.frc[2,53]-s.m[53]*(ALPHA252*C53+ALPHA352*S53-s.l[2,53]*(OM153*OM153+OM353*OM353)))
  Fs353 = -(s.frc[3,53]+s.m[53]*(ALPHA252*S53-ALPHA352*C53-s.l[2,53]*(OMp153+OM253*OM353)))
  Cq153 = -(s.trq[1,53]-s.In[1,53]*OMp153-s.In[9,53]*OM253*OM353-Fs353*s.l[2,53])
  Cq253 = -(s.trq[2,53]-OM153*OM353*(s.In[1,53]-s.In[9,53]))
  Cq353 = -(s.trq[3,53]+s.In[1,53]*OM153*OM253-s.In[9,53]*OMp353+Fs153*s.l[2,53])
  Fq252 = Fs253*C53-Fs353*S53
  Fq352 = Fs253*S53+Fs353*C53
  Cq252 = Cq253*C53-Cq353*S53
  Cq352 = Cq253*S53+Cq353*C53
  Fs151 = -(s.frc[1,51]+s.m[51]*(s.l[2,51]*(OMp351-OM151*OM251)-C50*(ALPHA149+BETA249*s.dpt[2,52])-S50*(ALPHA249+BS549*\
   s.dpt[2,52])))
  Fs251 = -(s.frc[2,51]-s.m[51]*(ALPHA250*C51+ALPHA350*S51-s.l[2,51]*(OM151*OM151+OM351*OM351)))
  Fs351 = -(s.frc[3,51]+s.m[51]*(ALPHA250*S51-ALPHA350*C51-s.l[2,51]*(OMp151+OM251*OM351)))
  Cq151 = -(s.trq[1,51]-s.In[1,51]*OMp151-s.In[9,51]*OM251*OM351-Fs351*s.l[2,51])
  Cq251 = -(s.trq[2,51]-OM151*OM351*(s.In[1,51]-s.In[9,51]))
  Cq351 = -(s.trq[3,51]+s.In[1,51]*OM151*OM251-s.In[9,51]*OMp351+Fs151*s.l[2,51])
  Fq250 = Fs251*C51-Fs351*S51
  Fq350 = Fs251*S51+Fs351*C51
  Cq250 = Cq251*C51-Cq351*S51
  Cq350 = Cq251*S51+Cq351*C51
  Fq149 = -(s.frc[1,49]-s.m[49]*ALPHA149+Fq250*S50+Fq252*S52-Fs151*C50-Fs153*C52)
  Fq249 = -(s.frc[2,49]-s.m[49]*ALPHA249-Fq250*C50-Fq252*C52-Fs151*S50-Fs153*S52)
  Fq349 = -(s.frc[3,49]-Fq350-Fq352-s.m[49]*ALPHA349)
  Fs148 = -(s.frc[1,48]-s.m[48]*(ALPHA147*C48-ALPHA347*S48))
  Fs248 = -(s.frc[2,48]-s.m[48]*(C47*(ALPHA244+BETA644*s.dpt[3,48]+BS544*s.dpt[2,48])+S47*(ALPHA343+BETA844*s.dpt[2,48]+\
   BS944*s.dpt[3,48])))
  Fs348 = -(s.frc[3,48]-s.m[48]*(ALPHA147*S48+ALPHA347*C48))
  Cq148 = -(s.trq[1,48]-s.In[1,48]*(C48*(OMp147-qd[48]*OM347)-S48*(OMp347+qd[48]*OM147))+OM248*OM348*(s.In[5,48]-\
   s.In[9,48]))
  Cq248 = -(s.trq[2,48]-s.In[5,48]*(qdd[48]+C47*(OMp244+qd[47]*OM344)+S47*(OMp344-qd[47]*OM244))-OM148*OM348*(s.In[1,48]\
   -s.In[9,48]))
  Cq348 = -(s.trq[3,48]-s.In[9,48]*(C48*(OMp347+qd[48]*OM147)+S48*(OMp147-qd[48]*OM347))+OM148*OM248*(s.In[1,48]-\
   s.In[5,48]))
  Fq147 = Fs148*C48+Fs348*S48
  Fq347 = -(Fs148*S48-Fs348*C48)
  Cq147 = Cq148*C48+Cq348*S48
  Cq347 = -(Cq148*S48-Cq348*C48)
  Fs146 = -(s.frc[1,46]-s.m[46]*(ALPHA144+q[46]*(OMp245+OM145*OM345)+(2.0)*qd[46]*OM245+BETA244*s.dpt[2,47]+BETA344*\
   s.dpt[3,47]+s.l[3,46]*(OMp245+OM145*OM345)))
  Fs246 = -(s.frc[2,46]+s.m[46]*(q[46]*(OMp145-OM245*OM345)+(2.0)*qd[46]*OM145+s.l[3,46]*(OMp145-OM245*OM345)-C45*(ALPHA244+\
   BETA644*s.dpt[3,47]+BS544*s.dpt[2,47])-S45*(ALPHA343+BETA844*s.dpt[2,47]+BS944*s.dpt[3,47])))
  Fs346 = -(s.frc[3,46]-s.m[46]*(qdd[46]-q[46]*(OM145*OM145+OM245*OM245)-s.l[3,46]*(OM145*OM145+OM245*OM245)+C45*(\
   ALPHA343+BETA844*s.dpt[2,47]+BS944*s.dpt[3,47])-S45*(ALPHA244+BETA644*s.dpt[3,47]+BS544*s.dpt[2,47])))
  Cq346 = -(s.trq[3,46]-s.In[9,46]*(C45*(OMp344-qd[45]*OM244)-S45*(OMp244+qd[45]*OM344))+OM145*OM245*(s.In[1,46]-\
   s.In[5,46]))
  Cq145 = -(s.trq[1,46]+q[46]*Fs246-s.In[1,46]*OMp145+Fs246*s.l[3,46]+OM245*OM345*(s.In[5,46]-s.In[9,46]))
  Cq245 = -(s.trq[2,46]-q[46]*Fs146-s.In[5,46]*OMp245-Fs146*s.l[3,46]-OM145*OM345*(s.In[1,46]-s.In[9,46]))
  Fs144 = -(s.frc[1,44]-s.m[44]*(ALPHA144+BETA244*s.l[2,44]+BETA344*s.l[3,44]))
  Fs244 = -(s.frc[2,44]-s.m[44]*(ALPHA244+BETA644*s.l[3,44]+BS544*s.l[2,44]))
  Fs344 = -(s.frc[3,44]-s.m[44]*(ALPHA343+BETA844*s.l[2,44]+BS944*s.l[3,44]))
  Fq144 = Fq147+Fs144+Fs146
  Fq244 = Fs244-Fq347*S47+Fs246*C45+Fs248*C47-Fs346*S45
  Fq344 = Fs344+Fq347*C47+Fs246*S45+Fs248*S47+Fs346*C45
  Cq144 = -(s.trq[1,44]-Cq145-Cq147-s.In[1,44]*OMp144+Fs244*s.l[3,44]-Fs344*s.l[2,44]+OM244*OM344*(s.In[5,44]-s.In[9,44]\
   )-s.dpt[2,47]*(Fs246*S45+Fs346*C45)-s.dpt[2,48]*(Fq347*C47+Fs248*S47)+s.dpt[3,47]*(Fs246*C45-Fs346*S45)-s.dpt[3,48]*(Fq347*\
   S47-Fs248*C47))
  Cq244 = -(s.trq[2,44]-s.In[5,44]*OMp244-Cq245*C45-Cq248*C47+Cq346*S45+Cq347*S47-Fq147*s.dpt[3,48]-Fs144*s.l[3,44]-\
   Fs146*s.dpt[3,47]-OM144*OM344*(s.In[1,44]-s.In[9,44]))
  Cq344 = -(s.trq[3,44]-s.In[9,44]*OMp344-Cq245*S45-Cq248*S47-Cq346*C45-Cq347*C47+Fq147*s.dpt[2,48]+Fs144*s.l[2,44]+\
   Fs146*s.dpt[2,47]+OM144*OM244*(s.In[1,44]-s.In[5,44]))
  Fq143 = Fq144*C44-Fq244*S44
  Fq243 = Fq144*S44+Fq244*C44
  Cq143 = Cq144*C44-Cq244*S44
  Cq243 = Cq144*S44+Cq244*C44
  Fq142 = Fq143*C43+Fq344*S43
  Fq342 = -(Fq143*S43-Fq344*C43)
  Cq142 = Cq143*C43+Cq344*S43
  Cq342 = -(Cq143*S43-Cq344*C43)
  Fs141 = -(s.frc[1,41]-s.m[41]*(ALPHA141+BETA241*s.l[2,41]))
  Fs341 = -(s.frc[3,41]-s.m[41]*(ALPHA340+BETA841*s.l[2,41]))
  Fq141 = Fq142+Fs141
  Fq241 = -(s.frc[2,41]-s.m[41]*(ALPHA241+BS541*s.l[2,41])-Fq243*C42+Fq342*S42)
  Fq341 = Fs341+Fq243*S42+Fq342*C42
  Cq141 = -(s.trq[1,41]-Cq142-s.In[1,41]*OMp141-s.In[9,41]*OM241*OM341-Fs341*s.l[2,41]-s.dpt[2,44]*(Fq243*S42+Fq342*C42)\
   )
  Cq241 = -(s.trq[2,41]-Cq243*C42+Cq342*S42-OM141*OM341*(s.In[1,41]-s.In[9,41]))
  Cq341 = -(s.trq[3,41]+s.In[1,41]*OM141*OM241-s.In[9,41]*OMp341-Cq243*S42-Cq342*C42+Fq142*s.dpt[2,44]+Fs141*s.l[2,41])
  Fq140 = Fq141*C41-Fq241*S41
  Fq240 = Fq141*S41+Fq241*C41
  Cq140 = Cq141*C41-Cq241*S41
  Cq240 = Cq141*S41+Cq241*C41
  Fs139 = -(s.frc[1,39]-s.m[39]*(ALPHA138*C39+ALPHA238*S39-s.l[2,39]*(OMp339-OM139*OM239)))
  Fs239 = -(s.frc[2,39]+s.m[39]*(ALPHA138*S39-ALPHA238*C39+s.l[2,39]*(OM139*OM139+OM339*OM339)))
  Fs339 = -(s.frc[3,39]-s.m[39]*(s.l[2,39]*(OMp139+OM239*OM339)+C38*(ALPHA36+BETA76*s.dpt[1,11]+BETA86*s.dpt[2,11]+BS96*\
   s.dpt[3,11])-S38*(ALPHA26+BETA46*s.dpt[1,11]+BETA66*s.dpt[3,11]+BS56*s.dpt[2,11])))
  Cq139 = -(s.trq[1,39]-s.In[1,39]*OMp139-s.In[9,39]*OM239*OM339-Fs339*s.l[2,39])
  Cq239 = -(s.trq[2,39]-OM139*OM339*(s.In[1,39]-s.In[9,39]))
  Cq339 = -(s.trq[3,39]+s.In[1,39]*OM139*OM239-s.In[9,39]*OMp339+Fs139*s.l[2,39])
  Fq138 = Fs139*C39-Fs239*S39
  Fq238 = Fs139*S39+Fs239*C39
  Cq138 = Cq139*C39-Cq239*S39
  Cq238 = Cq139*S39+Cq239*C39
  Fs137 = -(s.frc[1,37]-s.m[37]*(ALPHA136*C37-ALPHA336*S37))
  Fs237 = -(s.frc[2,37]-s.m[37]*(C36*(ALPHA233+BETA633*s.dpt[3,37]+BS533*s.dpt[2,37])+S36*(ALPHA332+BETA833*s.dpt[2,37]+\
   BS933*s.dpt[3,37])))
  Fs337 = -(s.frc[3,37]-s.m[37]*(ALPHA136*S37+ALPHA336*C37))
  Cq137 = -(s.trq[1,37]-s.In[1,37]*(C37*(OMp136-qd[37]*OM336)-S37*(OMp336+qd[37]*OM136))+OM237*OM337*(s.In[5,37]-\
   s.In[9,37]))
  Cq237 = -(s.trq[2,37]-s.In[5,37]*(qdd[37]+C36*(OMp233+qd[36]*OM333)+S36*(OMp333-qd[36]*OM233))-OM137*OM337*(s.In[1,37]\
   -s.In[9,37]))
  Cq337 = -(s.trq[3,37]-s.In[9,37]*(C37*(OMp336+qd[37]*OM136)+S37*(OMp136-qd[37]*OM336))+OM137*OM237*(s.In[1,37]-\
   s.In[5,37]))
  Fq136 = Fs137*C37+Fs337*S37
  Fq336 = -(Fs137*S37-Fs337*C37)
  Cq136 = Cq137*C37+Cq337*S37
  Cq336 = -(Cq137*S37-Cq337*C37)
  Fs135 = -(s.frc[1,35]-s.m[35]*(ALPHA133+q[35]*(OMp234+OM134*OM334)+(2.0)*qd[35]*OM234+BETA233*s.dpt[2,36]+BETA333*\
   s.dpt[3,36]+s.l[3,35]*(OMp234+OM134*OM334)))
  Fs235 = -(s.frc[2,35]+s.m[35]*(q[35]*(OMp134-OM234*OM334)+(2.0)*qd[35]*OM134+s.l[3,35]*(OMp134-OM234*OM334)-C34*(ALPHA233+\
   BETA633*s.dpt[3,36]+BS533*s.dpt[2,36])-S34*(ALPHA332+BETA833*s.dpt[2,36]+BS933*s.dpt[3,36])))
  Fs335 = -(s.frc[3,35]-s.m[35]*(qdd[35]-q[35]*(OM134*OM134+OM234*OM234)-s.l[3,35]*(OM134*OM134+OM234*OM234)+C34*(\
   ALPHA332+BETA833*s.dpt[2,36]+BS933*s.dpt[3,36])-S34*(ALPHA233+BETA633*s.dpt[3,36]+BS533*s.dpt[2,36])))
  Cq335 = -(s.trq[3,35]-s.In[9,35]*(C34*(OMp333-qd[34]*OM233)-S34*(OMp233+qd[34]*OM333))+OM134*OM234*(s.In[1,35]-\
   s.In[5,35]))
  Cq134 = -(s.trq[1,35]+q[35]*Fs235-s.In[1,35]*OMp134+Fs235*s.l[3,35]+OM234*OM334*(s.In[5,35]-s.In[9,35]))
  Cq234 = -(s.trq[2,35]-q[35]*Fs135-s.In[5,35]*OMp234-Fs135*s.l[3,35]-OM134*OM334*(s.In[1,35]-s.In[9,35]))
  Fs133 = -(s.frc[1,33]-s.m[33]*(ALPHA133+BETA233*s.l[2,33]+BETA333*s.l[3,33]))
  Fs233 = -(s.frc[2,33]-s.m[33]*(ALPHA233+BETA633*s.l[3,33]+BS533*s.l[2,33]))
  Fs333 = -(s.frc[3,33]-s.m[33]*(ALPHA332+BETA833*s.l[2,33]+BS933*s.l[3,33]))
  Fq133 = Fq136+Fs133+Fs135
  Fq233 = Fs233-Fq336*S36+Fs235*C34+Fs237*C36-Fs335*S34
  Fq333 = Fs333+Fq336*C36+Fs235*S34+Fs237*S36+Fs335*C34
  Cq133 = -(s.trq[1,33]-Cq134-Cq136-s.In[1,33]*OMp133+Fs233*s.l[3,33]-Fs333*s.l[2,33]+OM233*OM333*(s.In[5,33]-s.In[9,33]\
   )-s.dpt[2,36]*(Fs235*S34+Fs335*C34)-s.dpt[2,37]*(Fq336*C36+Fs237*S36)+s.dpt[3,36]*(Fs235*C34-Fs335*S34)-s.dpt[3,37]*(Fq336*\
   S36-Fs237*C36))
  Cq233 = -(s.trq[2,33]-s.In[5,33]*OMp233-Cq234*C34-Cq237*C36+Cq335*S34+Cq336*S36-Fq136*s.dpt[3,37]-Fs133*s.l[3,33]-\
   Fs135*s.dpt[3,36]-OM133*OM333*(s.In[1,33]-s.In[9,33]))
  Cq333 = -(s.trq[3,33]-s.In[9,33]*OMp333-Cq234*S34-Cq237*S36-Cq335*C34-Cq336*C36+Fq136*s.dpt[2,37]+Fs133*s.l[2,33]+\
   Fs135*s.dpt[2,36]+OM133*OM233*(s.In[1,33]-s.In[5,33]))
  Fq132 = Fq133*C33-Fq233*S33
  Fq232 = Fq133*S33+Fq233*C33
  Cq132 = Cq133*C33-Cq233*S33
  Cq232 = Cq133*S33+Cq233*C33
  Fq131 = Fq132*C32+Fq333*S32
  Fq331 = -(Fq132*S32-Fq333*C32)
  Cq131 = Cq132*C32+Cq333*S32
  Cq331 = -(Cq132*S32-Cq333*C32)
  Fs130 = -(s.frc[1,30]-s.m[30]*(ALPHA130+BETA230*s.l[2,30]))
  Fs330 = -(s.frc[3,30]-s.m[30]*(ALPHA329+BETA830*s.l[2,30]))
  Fq130 = Fq131+Fs130
  Fq230 = -(s.frc[2,30]-s.m[30]*(ALPHA230+BS530*s.l[2,30])-Fq232*C31+Fq331*S31)
  Fq330 = Fs330+Fq232*S31+Fq331*C31
  Cq130 = -(s.trq[1,30]-Cq131-s.In[1,30]*OMp130-s.In[9,30]*OM230*OM330-Fs330*s.l[2,30]-s.dpt[2,35]*(Fq232*S31+Fq331*C31)\
   )
  Cq230 = -(s.trq[2,30]-Cq232*C31+Cq331*S31-OM130*OM330*(s.In[1,30]-s.In[9,30]))
  Cq330 = -(s.trq[3,30]+s.In[1,30]*OM130*OM230-s.In[9,30]*OMp330-Cq232*S31-Cq331*C31+Fq131*s.dpt[2,35]+Fs130*s.l[2,30])
  Fq129 = Fq130*C30-Fq230*S30
  Fq229 = Fq130*S30+Fq230*C30
  Cq129 = Cq130*C30-Cq230*S30
  Cq229 = Cq130*S30+Cq230*C30
  Fs128 = -(s.frc[1,28]-s.m[28]*(ALPHA127*C28+ALPHA227*S28-s.l[2,28]*(OMp328-OM128*OM228)))
  Fs228 = -(s.frc[2,28]+s.m[28]*(ALPHA127*S28-ALPHA227*C28+s.l[2,28]*(OM128*OM128+OM328*OM328)))
  Fs328 = -(s.frc[3,28]-s.m[28]*(s.l[2,28]*(OMp128+OM228*OM328)+C27*(ALPHA36+BETA76*s.dpt[1,9]+BETA86*s.dpt[2,9]+BS96*\
   s.dpt[3,9])-S27*(ALPHA26+BETA46*s.dpt[1,9]+BETA66*s.dpt[3,9]+BS56*s.dpt[2,9])))
  Cq128 = -(s.trq[1,28]-s.In[1,28]*OMp128-s.In[9,28]*OM228*OM328-Fs328*s.l[2,28])
  Cq228 = -(s.trq[2,28]-OM128*OM328*(s.In[1,28]-s.In[9,28]))
  Cq328 = -(s.trq[3,28]+s.In[1,28]*OM128*OM228-s.In[9,28]*OMp328+Fs128*s.l[2,28])
  Fq127 = Fs128*C28-Fs228*S28
  Fq227 = Fs128*S28+Fs228*C28
  Cq127 = Cq128*C28-Cq228*S28
  Cq227 = Cq128*S28+Cq228*C28
  Fs126 = -(s.frc[1,26]-s.m[26]*(ALPHA125*C26+ALPHA225*S26-s.l[2,26]*(OMp326-OM126*OM226)))
  Fs226 = -(s.frc[2,26]+s.m[26]*(ALPHA125*S26-ALPHA225*C26+s.l[2,26]*(OM126*OM126+OM326*OM326)))
  Fs326 = -(s.frc[3,26]-s.m[26]*(s.l[2,26]*(OMp126+OM226*OM326)+C25*(ALPHA36+BETA76*s.dpt[1,8]+BETA86*s.dpt[2,8]+BS96*\
   s.dpt[3,8])-S25*(ALPHA26+BETA46*s.dpt[1,8]+BETA66*s.dpt[3,8]+BS56*s.dpt[2,8])))
  Cq126 = -(s.trq[1,26]-s.In[1,26]*OMp126-s.In[9,26]*OM226*OM326-Fs326*s.l[2,26])
  Cq226 = -(s.trq[2,26]-OM126*OM326*(s.In[1,26]-s.In[9,26]))
  Cq326 = -(s.trq[3,26]+s.In[1,26]*OM126*OM226-s.In[9,26]*OMp326+Fs126*s.l[2,26])
  Fq125 = Fs126*C26-Fs226*S26
  Fq225 = Fs126*S26+Fs226*C26
  Cq125 = Cq126*C26-Cq226*S26
  Cq225 = Cq126*S26+Cq226*C26
  Fs124 = -(s.frc[1,24]-s.m[24]*(ALPHA123*C24+ALPHA223*S24-s.l[2,24]*(OMp324-OM124*OM224)))
  Fs224 = -(s.frc[2,24]+s.m[24]*(ALPHA123*S24-ALPHA223*C24+s.l[2,24]*(OM124*OM124+OM324*OM324)))
  Fs324 = -(s.frc[3,24]-s.m[24]*(s.l[2,24]*(OMp124+OM224*OM324)+C23*(ALPHA36+BETA76*s.dpt[1,6]+BETA86*s.dpt[2,6]+BS96*\
   s.dpt[3,6])-S23*(ALPHA26+BETA46*s.dpt[1,6]+BETA66*s.dpt[3,6]+BS56*s.dpt[2,6])))
  Cq124 = -(s.trq[1,24]-s.In[1,24]*OMp124-s.In[9,24]*OM224*OM324-Fs324*s.l[2,24])
  Cq224 = -(s.trq[2,24]-OM124*OM324*(s.In[1,24]-s.In[9,24]))
  Cq324 = -(s.trq[3,24]+s.In[1,24]*OM124*OM224-s.In[9,24]*OMp324+Fs124*s.l[2,24])
  Fq123 = Fs124*C24-Fs224*S24
  Fq223 = Fs124*S24+Fs224*C24
  Cq123 = Cq124*C24-Cq224*S24
  Cq223 = Cq124*S24+Cq224*C24
  Fs122 = -(s.frc[1,22]-s.m[22]*(ALPHA121*C22-ALPHA321*S22))
  Fs222 = -(s.frc[2,22]-s.m[22]*(C21*(ALPHA217+BETA618*s.dpt[3,27]+BS518*s.dpt[2,27])+S21*(ALPHA318+BETA818*s.dpt[2,27]+\
   BS918*s.dpt[3,27])))
  Fs322 = -(s.frc[3,22]-s.m[22]*(ALPHA121*S22+ALPHA321*C22))
  Cq122 = -(s.trq[1,22]-s.In[1,22]*(C22*(OMp121-qd[22]*OM321)-S22*(OMp321+qd[22]*OM121))+OM222*OM322*(s.In[5,22]-\
   s.In[9,22]))
  Cq222 = -(s.trq[2,22]-s.In[5,22]*(qdd[22]+C21*(OMp218+qd[21]*OM318)+S21*(OMp318-qd[21]*OM218))-OM122*OM322*(s.In[1,22]\
   -s.In[9,22]))
  Cq322 = -(s.trq[3,22]-s.In[9,22]*(C22*(OMp321+qd[22]*OM121)+S22*(OMp121-qd[22]*OM321))+OM122*OM222*(s.In[1,22]-\
   s.In[5,22]))
  Fq121 = Fs122*C22+Fs322*S22
  Fq321 = -(Fs122*S22-Fs322*C22)
  Cq121 = Cq122*C22+Cq322*S22
  Cq321 = -(Cq122*S22-Cq322*C22)
  Fs120 = -(s.frc[1,20]-s.m[20]*(ALPHA118+q[20]*(OMp219+OM119*OM319)+(2.0)*qd[20]*OM219+BETA218*s.dpt[2,26]+BETA318*\
   s.dpt[3,26]+s.l[3,20]*(OMp219+OM119*OM319)))
  Fs220 = -(s.frc[2,20]+s.m[20]*(q[20]*(OMp119-OM219*OM319)+(2.0)*qd[20]*OM119+s.l[3,20]*(OMp119-OM219*OM319)-C19*(ALPHA217+\
   BETA618*s.dpt[3,26]+BS518*s.dpt[2,26])-S19*(ALPHA318+BETA818*s.dpt[2,26]+BS918*s.dpt[3,26])))
  Fs320 = -(s.frc[3,20]-s.m[20]*(qdd[20]-q[20]*(OM119*OM119+OM219*OM219)-s.l[3,20]*(OM119*OM119+OM219*OM219)+C19*(\
   ALPHA318+BETA818*s.dpt[2,26]+BS918*s.dpt[3,26])-S19*(ALPHA217+BETA618*s.dpt[3,26]+BS518*s.dpt[2,26])))
  Cq320 = -(s.trq[3,20]-s.In[9,20]*(C19*(OMp318-qd[19]*OM218)-S19*(OMp218+qd[19]*OM318))+OM119*OM219*(s.In[1,20]-\
   s.In[5,20]))
  Cq119 = -(s.trq[1,20]+q[20]*Fs220-s.In[1,20]*OMp119+Fs220*s.l[3,20]+OM219*OM319*(s.In[5,20]-s.In[9,20]))
  Cq219 = -(s.trq[2,20]-q[20]*Fs120-s.In[5,20]*OMp219-Fs120*s.l[3,20]-OM119*OM319*(s.In[1,20]-s.In[9,20]))
  Fs118 = -(s.frc[1,18]-s.m[18]*(ALPHA118+BETA318*s.l[3,18]))
  Fs218 = -(s.frc[2,18]-s.m[18]*(ALPHA217+BETA618*s.l[3,18]))
  Fq118 = Fq121+Fs118+Fs120
  Fq218 = Fs218-Fq321*S21+Fs220*C19+Fs222*C21-Fs320*S19
  Fq318 = -(s.frc[3,18]-s.m[18]*(ALPHA318+BS918*s.l[3,18])-Fq321*C21-Fs220*S19-Fs222*S21-Fs320*C19)
  Cq118 = -(s.trq[1,18]-Cq119-Cq121-s.In[1,18]*OMp118+Fs218*s.l[3,18]+OM218*OM318*(s.In[5,18]-s.In[9,18])-s.dpt[2,26]*(\
   Fs220*S19+Fs320*C19)-s.dpt[2,27]*(Fq321*C21+Fs222*S21)+s.dpt[3,26]*(Fs220*C19-Fs320*S19)-s.dpt[3,27]*(Fq321*S21-Fs222*C21))
  Cq218 = -(s.trq[2,18]-s.In[5,18]*OMp218-Cq219*C19-Cq222*C21+Cq320*S19+Cq321*S21-Fq121*s.dpt[3,27]-Fs118*s.l[3,18]-\
   Fs120*s.dpt[3,26]-OM118*OM318*(s.In[1,18]-s.In[9,18]))
  Cq318 = -(s.trq[3,18]-s.In[9,18]*OMp318-Cq219*S19-Cq222*S21-Cq320*C19-Cq321*C21+Fq121*s.dpt[2,27]+Fs120*s.dpt[2,26]+\
   OM118*OM218*(s.In[1,18]-s.In[5,18]))
  Fq117 = Fq118*C18+Fq318*S18
  Fq317 = -(Fq118*S18-Fq318*C18)
  Cq117 = Cq118*C18+Cq318*S18
  Cq317 = -(Cq118*S18-Cq318*C18)
  Fq216 = Fq218*C17-Fq317*S17
  Fq316 = Fq218*S17+Fq317*C17
  Cq216 = Cq218*C17-Cq317*S17
  Cq316 = Cq218*S17+Cq317*C17
  Fs115 = -(s.frc[1,15]-s.m[15]*(ALPHA115+BETA215*s.l[2,15]-s.l[1,15]*(OM215*OM215+OM315*OM315)))
  Fs215 = -(s.frc[2,15]-s.m[15]*(ALPHA215+BS515*s.l[2,15]+s.l[1,15]*(BS215+OMp315)))
  Fs315 = -(s.frc[3,15]-s.m[15]*(ALPHA315+BETA815*s.l[2,15]-s.l[1,15]*(OMp215-OM115*OM315)))
  Fq115 = Fs115+Fq117*C16-Fq216*S16
  Fq215 = Fs215+Fq117*S16+Fq216*C16
  Fq315 = Fq316+Fs315
  Cq115 = -(s.trq[1,15]-s.In[1,15]*OMp115-Cq117*C16+Cq216*S16-Fq316*s.dpt[2,25]-Fs315*s.l[2,15])
  Cq215 = -(s.trq[2,15]-s.In[1,15]*OM115*OM315-Cq117*S16-Cq216*C16+Fs315*s.l[1,15])
  Cq315 = -(s.trq[3,15]-Cq316+s.In[1,15]*OM115*OM215+Fs115*s.l[2,15]-Fs215*s.l[1,15]+s.dpt[2,25]*(Fq117*C16-Fq216*S16))
  Fs114 = -(s.frc[1,14]-s.m[14]*(ALPHA113*C14-ALPHA313*S14))
  Fs214 = -(s.frc[2,14]-s.m[14]*(C13*(ALPHA29+BETA610*s.dpt[3,20]+BS510*s.dpt[2,20])+S13*(ALPHA310+BETA810*s.dpt[2,20]+\
   BS910*s.dpt[3,20])))
  Fs314 = -(s.frc[3,14]-s.m[14]*(ALPHA113*S14+ALPHA313*C14))
  Cq114 = -(s.trq[1,14]-s.In[1,14]*(C14*(OMp113-qd[14]*OM313)-S14*(OMp313+qd[14]*OM113))+OM214*OM314*(s.In[5,14]-\
   s.In[9,14]))
  Cq214 = -(s.trq[2,14]-s.In[5,14]*(qdd[14]+C13*(OMp210+qd[13]*OM310)+S13*(OMp310-qd[13]*OM210))-OM114*OM314*(s.In[1,14]\
   -s.In[9,14]))
  Cq314 = -(s.trq[3,14]-s.In[9,14]*(C14*(OMp313+qd[14]*OM113)+S14*(OMp113-qd[14]*OM313))+OM114*OM214*(s.In[1,14]-\
   s.In[5,14]))
  Fq113 = Fs114*C14+Fs314*S14
  Fq313 = -(Fs114*S14-Fs314*C14)
  Cq113 = Cq114*C14+Cq314*S14
  Cq313 = -(Cq114*S14-Cq314*C14)
  Fs112 = -(s.frc[1,12]-s.m[12]*(ALPHA110+q[12]*(OMp211+OM111*OM311)+(2.0)*qd[12]*OM211+BETA210*s.dpt[2,19]+BETA310*\
   s.dpt[3,19]+s.l[3,12]*(OMp211+OM111*OM311)))
  Fs212 = -(s.frc[2,12]+s.m[12]*(q[12]*(OMp111-OM211*OM311)+(2.0)*qd[12]*OM111+s.l[3,12]*(OMp111-OM211*OM311)-C11*(ALPHA29+\
   BETA610*s.dpt[3,19]+BS510*s.dpt[2,19])-S11*(ALPHA310+BETA810*s.dpt[2,19]+BS910*s.dpt[3,19])))
  Fs312 = -(s.frc[3,12]-s.m[12]*(qdd[12]-q[12]*(OM111*OM111+OM211*OM211)-s.l[3,12]*(OM111*OM111+OM211*OM211)+C11*(\
   ALPHA310+BETA810*s.dpt[2,19]+BS910*s.dpt[3,19])-S11*(ALPHA29+BETA610*s.dpt[3,19]+BS510*s.dpt[2,19])))
  Cq312 = -(s.trq[3,12]-s.In[9,12]*(C11*(OMp310-qd[11]*OM210)-S11*(OMp210+qd[11]*OM310))+OM111*OM211*(s.In[1,12]-\
   s.In[5,12]))
  Cq111 = -(s.trq[1,12]+q[12]*Fs212-s.In[1,12]*OMp111+Fs212*s.l[3,12]+OM211*OM311*(s.In[5,12]-s.In[9,12]))
  Cq211 = -(s.trq[2,12]-q[12]*Fs112-s.In[5,12]*OMp211-Fs112*s.l[3,12]-OM111*OM311*(s.In[1,12]-s.In[9,12]))
  Fs110 = -(s.frc[1,10]-s.m[10]*(ALPHA110+BETA310*s.l[3,10]))
  Fs210 = -(s.frc[2,10]-s.m[10]*(ALPHA29+BETA610*s.l[3,10]))
  Fq110 = Fq113+Fs110+Fs112
  Fq210 = Fs210-Fq313*S13+Fs212*C11+Fs214*C13-Fs312*S11
  Fq310 = -(s.frc[3,10]-s.m[10]*(ALPHA310+BS910*s.l[3,10])-Fq313*C13-Fs212*S11-Fs214*S13-Fs312*C11)
  Cq110 = -(s.trq[1,10]-Cq111-Cq113-s.In[1,10]*OMp110+Fs210*s.l[3,10]+OM210*OM310*(s.In[5,10]-s.In[9,10])-s.dpt[2,19]*(\
   Fs212*S11+Fs312*C11)-s.dpt[2,20]*(Fq313*C13+Fs214*S13)+s.dpt[3,19]*(Fs212*C11-Fs312*S11)-s.dpt[3,20]*(Fq313*S13-Fs214*C13))
  Cq210 = -(s.trq[2,10]-s.In[5,10]*OMp210-Cq211*C11-Cq214*C13+Cq312*S11+Cq313*S13-Fq113*s.dpt[3,20]-Fs110*s.l[3,10]-\
   Fs112*s.dpt[3,19]-OM110*OM310*(s.In[1,10]-s.In[9,10]))
  Cq310 = -(s.trq[3,10]-s.In[9,10]*OMp310-Cq211*S11-Cq214*S13-Cq312*C11-Cq313*C13+Fq113*s.dpt[2,20]+Fs112*s.dpt[2,19]+\
   OM110*OM210*(s.In[1,10]-s.In[5,10]))
  Fq19 = Fq110*C10+Fq310*S10
  Fq39 = -(Fq110*S10-Fq310*C10)
  Cq19 = Cq110*C10+Cq310*S10
  Cq39 = -(Cq110*S10-Cq310*C10)
  Fq28 = Fq210*C9-Fq39*S9
  Fq38 = Fq210*S9+Fq39*C9
  Cq28 = Cq210*C9-Cq39*S9
  Cq38 = Cq210*S9+Cq39*C9
  Fs17 = -(s.frc[1,7]-s.m[7]*(ALPHA17+BETA27*s.l[2,7]-s.l[1,7]*(OM27*OM27+OM37*OM37)))
  Fs27 = -(s.frc[2,7]-s.m[7]*(ALPHA27+BS57*s.l[2,7]+s.l[1,7]*(BS27+OMp37)))
  Fs37 = -(s.frc[3,7]-s.m[7]*(ALPHA37+BETA87*s.l[2,7]-s.l[1,7]*(OMp27-OM17*OM37)))
  Fq17 = Fs17+Fq19*C8-Fq28*S8
  Fq27 = Fs27+Fq19*S8+Fq28*C8
  Fq37 = Fq38+Fs37
  Cq17 = -(s.trq[1,7]-s.In[1,7]*OMp17-Cq19*C8+Cq28*S8-Fq38*s.dpt[2,18]-Fs37*s.l[2,7])
  Cq27 = -(s.trq[2,7]-s.In[1,7]*OM17*OM37-Cq19*S8-Cq28*C8+Fs37*s.l[1,7])
  Cq37 = -(s.trq[3,7]-Cq38+s.In[1,7]*OM17*OM27+Fs17*s.l[2,7]-Fs27*s.l[1,7]+s.dpt[2,18]*(Fq19*C8-Fq28*S8))
  Fs16 = -(s.frc[1,6]-s.m[6]*(ALPHA15+BETA36*s.l[3,6]))
  Fs26 = -(s.frc[2,6]-s.m[6]*(ALPHA26+BETA66*s.l[3,6]))
  Fq16 = Fq115+Fq123+Fq125+Fq127+Fq129+Fq138+Fq140+Fq149+Fq17+Fs16+Fq154*C54+Fq160*C60+Fq354*S54+Fq360*S60
  Fq26 = Fq249+Fq254+Fq260+Fs26+Fq215*C15+Fq223*C23+Fq225*C25+Fq227*C27+Fq229*C29+Fq238*C38+Fq240*C40+Fq27*C7-Fq315*S15-\
   Fq330*S29-Fq341*S40-Fq37*S7-Fs324*S23-Fs326*S25-Fs328*S27-Fs339*S38
  Fq36 = -(s.frc[3,6]-Fq349-s.m[6]*(ALPHA36+BS96*s.l[3,6])+Fq154*S54+Fq160*S60-Fq215*S15-Fq223*S23-Fq225*S25-Fq227*S27-\
   Fq229*S29-Fq238*S38-Fq240*S40-Fq27*S7-Fq315*C15-Fq330*C29-Fq341*C40-Fq354*C54-Fq360*C60-Fq37*C7-Fs324*C23-Fs326*C25-Fs328*\
   C27-Fs339*C38)
  Cq16 = -(s.trq[1,49]+s.trq[1,6]-Cq115-Cq123-Cq125-Cq127-Cq129-Cq138-Cq140-Cq17-q[49]*Fq349-s.In[1,6]*OMp16-Cq151*C50-\
   Cq153*C52-Cq154*C54-Cq160*C60+Cq250*S50+Cq252*S52-Cq354*S54-Cq360*S60+Fq254*s.dpt[3,14]+Fq260*s.dpt[3,15]-Fq350*s.dpt[2,52]-\
   Fq352*s.dpt[2,53]+Fs26*s.l[3,6]+OM26*OM36*(s.In[5,6]-s.In[9,6])-s.dpt[2,10]*(Fq229*S29+Fq330*C29)-s.dpt[2,11]*(Fq238*S38+\
   Fs339*C38)-s.dpt[2,12]*(Fq240*S40+Fq341*C40)-s.dpt[2,1]*(Fq27*S7+Fq37*C7)-s.dpt[2,4]*(Fq215*S15+Fq315*C15)-s.dpt[2,6]*(Fq223\
   *S23+Fs324*C23)-s.dpt[2,8]*(Fq225*S25+Fs326*C25)-s.dpt[2,9]*(Fq227*S27+Fs328*C27)+s.dpt[3,11]*(Fq238*C38-Fs339*S38)+\
   s.dpt[3,6]*(Fq223*C23-Fs324*S23)+s.dpt[3,8]*(Fq225*C25-Fs326*S25)+s.dpt[3,9]*(Fq227*C27-Fs328*S27))
  Cq26 = -(s.trq[2,49]+s.trq[2,6]-Cq254-Cq260-s.In[5,6]*OMp26-Cq151*S50-Cq153*S52-Cq215*C15-Cq223*C23-Cq225*C25-Cq227*\
   C27-Cq229*C29-Cq238*C38-Cq240*C40-Cq250*C50-Cq252*C52-Cq27*C7+Cq315*S15+Cq324*S23+Cq326*S25+Cq328*S27+Cq330*S29+Cq339*S38+\
   Cq341*S40+Cq37*S7-Fq123*s.dpt[3,6]-Fq125*s.dpt[3,8]-Fq127*s.dpt[3,9]-Fq138*s.dpt[3,11]+Fq349*s.dpt[1,13]-Fs16*s.l[3,6]-OM16*\
   OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,10]*(Fq229*S29+Fq330*C29)+s.dpt[1,11]*(Fq238*S38+Fs339*C38)+s.dpt[1,12]*(Fq240*S40+Fq341*\
   C40)-s.dpt[1,14]*(Fq154*S54-Fq354*C54)-s.dpt[1,15]*(Fq160*S60-Fq360*C60)+s.dpt[1,1]*(Fq27*S7+Fq37*C7)+s.dpt[1,4]*(Fq215*S15+\
   Fq315*C15)+s.dpt[1,6]*(Fq223*S23+Fs324*C23)+s.dpt[1,8]*(Fq225*S25+Fs326*C25)+s.dpt[1,9]*(Fq227*S27+Fs328*C27)-s.dpt[3,14]*(\
   Fq154*C54+Fq354*S54)-s.dpt[3,15]*(Fq160*C60+Fq360*S60))
  Cq36 = -(s.trq[3,49]+s.trq[3,6]-Cq350-Cq352+q[49]*Fq149-s.In[9,6]*OMp36+Cq154*S54+Cq160*S60-Cq215*S15-Cq223*S23-Cq225*\
   S25-Cq227*S27-Cq229*S29-Cq238*S38-Cq240*S40-Cq27*S7-Cq315*C15-Cq324*C23-Cq326*C25-Cq328*C27-Cq330*C29-Cq339*C38-Cq341*C40-\
   Cq354*C54-Cq360*C60-Cq37*C7+Fq115*s.dpt[2,4]+Fq123*s.dpt[2,6]+Fq125*s.dpt[2,8]+Fq127*s.dpt[2,9]+Fq129*s.dpt[2,10]+Fq138*\
   s.dpt[2,11]+Fq140*s.dpt[2,12]+Fq17*s.dpt[2,1]-Fq249*s.dpt[1,13]-Fq254*s.dpt[1,14]-Fq260*s.dpt[1,15]+OM16*OM26*(s.In[1,6]-\
   s.In[5,6])-s.dpt[1,10]*(Fq229*C29-Fq330*S29)-s.dpt[1,11]*(Fq238*C38-Fs339*S38)-s.dpt[1,12]*(Fq240*C40-Fq341*S40)-s.dpt[1,1]*\
   (Fq27*C7-Fq37*S7)-s.dpt[1,4]*(Fq215*C15-Fq315*S15)-s.dpt[1,6]*(Fq223*C23-Fs324*S23)-s.dpt[1,8]*(Fq225*C25-Fs326*S25)-\
   s.dpt[1,9]*(Fq227*C27-Fs328*S27)-s.dpt[2,52]*(Fq250*S50-Fs151*C50)-s.dpt[2,53]*(Fq252*S52-Fs153*C52))
  Fq25 = Fq26*C6-Fq36*S6
  Fq35 = Fq26*S6+Fq36*C6
  Cq25 = Cq26*C6-Cq36*S6
  Fq14 = Fq16*C5+Fq35*S5
  Fq34 = -(Fq16*S5-Fq35*C5)
  Cq34 = -(Cq16*S5-C5*(Cq26*S6+Cq36*C6))
  Fq13 = Fq14*C4-Fq25*S4
  Fq23 = Fq14*S4+Fq25*C4

# = = Block_0_2_0_0_0_0 = = 
 
# Symbolic Outputs  

  Qq[1] = Fq13
  Qq[2] = Fq23
  Qq[3] = Fq34
  Qq[4] = Cq34
  Qq[5] = Cq25
  Qq[6] = Cq16
  Qq[7] = Cq17
  Qq[8] = Cq38
  Qq[9] = Cq19
  Qq[10] = Cq210
  Qq[11] = Cq111
  Qq[12] = Fs312
  Qq[13] = Cq113
  Qq[14] = Cq214
  Qq[15] = Cq115
  Qq[16] = Cq316
  Qq[17] = Cq117
  Qq[18] = Cq218
  Qq[19] = Cq119
  Qq[20] = Fs320
  Qq[21] = Cq121
  Qq[22] = Cq222
  Qq[23] = Cq123
  Qq[24] = Cq324
  Qq[25] = Cq125
  Qq[26] = Cq326
  Qq[27] = Cq127
  Qq[28] = Cq328
  Qq[29] = Cq129
  Qq[30] = Cq330
  Qq[31] = Cq131
  Qq[32] = Cq232
  Qq[33] = Cq333
  Qq[34] = Cq134
  Qq[35] = Fs335
  Qq[36] = Cq136
  Qq[37] = Cq237
  Qq[38] = Cq138
  Qq[39] = Cq339
  Qq[40] = Cq140
  Qq[41] = Cq341
  Qq[42] = Cq142
  Qq[43] = Cq243
  Qq[44] = Cq344
  Qq[45] = Cq145
  Qq[46] = Fs346
  Qq[47] = Cq147
  Qq[48] = Cq248
  Qq[49] = Fq249
  Qq[50] = Cq350
  Qq[51] = Cq151
  Qq[52] = Cq352
  Qq[53] = Cq153
  Qq[54] = Cq254
  Qq[55] = Cq255
  Qq[56] = Cq256
  Qq[57] = Cq157
  Qq[58] = Cq258
  Qq[59] = Cq159
  Qq[60] = Cq260
  Qq[61] = Cq261
  Qq[62] = Cq262
  Qq[63] = Cq163
  Qq[64] = Cq264
  Qq[65] = Cq165
  Qq[66] = Fs366
  Qq[67] = Fs367

# ====== END Task 0 ====== 

  

