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
#	==> Generation Date : Sat Mar 28 19:52:49 2020
#
#	==> Project name : Complete_Vehicle
#	==> using XML input file 
#
#	==> Number of joints : 38
#
#	==> Function : F 2 : Inverse Dynamics : RNEA
#	==> Flops complexity : 2585
#
#	==> Generation Time :  0.030 seconds
#	==> Post-Processing :  0.030 seconds
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
  BS57 = -(OM17*OM17+OM37*OM37)
  BETA27 = OM17*OM27-OMp37
  BETA87 = OMp17+OM27*OM37
  ALPHA17 = ALPHA15+BETA26*s.dpt[2,1]+BETA36*s.dpt[3,1]+BS16*s.dpt[1,1]
  ALPHA27 = C7*(ALPHA26+BETA46*s.dpt[1,1]+BETA66*s.dpt[3,1]+BS56*s.dpt[2,1])+S7*(ALPHA36+BETA76*s.dpt[1,1]+BETA86*\
   s.dpt[2,1]+BS96*s.dpt[3,1])
  ALPHA37 = C7*(ALPHA36+BETA76*s.dpt[1,1]+BETA86*s.dpt[2,1]+BS96*s.dpt[3,1])-S7*(ALPHA26+BETA46*s.dpt[1,1]+BETA66*\
   s.dpt[3,1]+BS56*s.dpt[2,1])
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OMp28 = C8*(OMp27-qd[8]*OM17)-S8*(OMp17+qd[8]*OM27)
  OMp38 = qdd[8]+OMp37
  ALPHA18 = C8*(ALPHA17+BETA27*s.dpt[2,13])+S8*(ALPHA27+BS57*s.dpt[2,13])
  ALPHA28 = C8*(ALPHA27+BS57*s.dpt[2,13])-S8*(ALPHA17+BETA27*s.dpt[2,13])
  ALPHA38 = ALPHA37+BETA87*s.dpt[2,13]
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
  BS910 = -(OM110*OM110+OM210*OM210)
  BETA310 = OMp210+OM110*OM310
  BETA610 = OM210*OM310-OMp110
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
  ALPHA313 = -(ALPHA29*S13-ALPHA310*C13)
  OM114 = OM113*C14-OM313*S14
  OM214 = qd[14]+OM210*C13+OM310*S13
  OM314 = OM113*S14+OM313*C14
  OM115 = qd[15]+OM16
  OM215 = OM26*C15+OM36*S15
  OM315 = -(OM26*S15-OM36*C15)
  OMp115 = qdd[15]+OMp16
  OMp215 = C15*(OMp26+qd[15]*OM36)+S15*(OMp36-qd[15]*OM26)
  OMp315 = C15*(OMp36-qd[15]*OM26)-S15*(OMp26+qd[15]*OM36)
  BS515 = -(OM115*OM115+OM315*OM315)
  BETA215 = OM115*OM215-OMp315
  BETA815 = OMp115+OM215*OM315
  ALPHA115 = ALPHA15+BETA26*s.dpt[2,4]+BETA36*s.dpt[3,4]+BS16*s.dpt[1,4]
  ALPHA215 = C15*(ALPHA26+BETA46*s.dpt[1,4]+BETA66*s.dpt[3,4]+BS56*s.dpt[2,4])+S15*(ALPHA36+BETA76*s.dpt[1,4]+BETA86*\
   s.dpt[2,4]+BS96*s.dpt[3,4])
  ALPHA315 = C15*(ALPHA36+BETA76*s.dpt[1,4]+BETA86*s.dpt[2,4]+BS96*s.dpt[3,4])-S15*(ALPHA26+BETA46*s.dpt[1,4]+BETA66*\
   s.dpt[3,4]+BS56*s.dpt[2,4])
  OM216 = -(OM115*S16-OM215*C16)
  OM316 = qd[16]+OM315
  OMp216 = C16*(OMp215-qd[16]*OM115)-S16*(OMp115+qd[16]*OM215)
  OMp316 = qdd[16]+OMp315
  ALPHA116 = C16*(ALPHA115+BETA215*s.dpt[2,18])+S16*(ALPHA215+BS515*s.dpt[2,18])
  ALPHA216 = C16*(ALPHA215+BS515*s.dpt[2,18])-S16*(ALPHA115+BETA215*s.dpt[2,18])
  ALPHA316 = ALPHA315+BETA815*s.dpt[2,18]
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
  BS918 = -(OM118*OM118+OM218*OM218)
  BETA318 = OMp218+OM118*OM318
  BETA618 = OM218*OM318-OMp118
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
  ALPHA321 = -(ALPHA217*S21-ALPHA318*C21)
  OM122 = OM121*C22-OM321*S22
  OM222 = qd[22]+OM218*C21+OM318*S21
  OM322 = OM121*S22+OM321*C22
  OM123 = qd[23]+OM16
  OM223 = OM26*C23+OM36*S23
  OMp123 = qdd[23]+OMp16
  OMp223 = C23*(OMp26+qd[23]*OM36)+S23*(OMp36-qd[23]*OM26)
  ALPHA123 = ALPHA15+BETA26*s.dpt[2,10]+BS16*s.dpt[1,10]
  ALPHA223 = C23*(ALPHA26+BETA46*s.dpt[1,10]+BS56*s.dpt[2,10])+S23*(ALPHA36+BETA76*s.dpt[1,10]+BETA86*s.dpt[2,10])
  ALPHA323 = C23*(ALPHA36+BETA76*s.dpt[1,10]+BETA86*s.dpt[2,10])-S23*(ALPHA26+BETA46*s.dpt[1,10]+BS56*s.dpt[2,10])
  OM124 = OM123*C24+OM223*S24
  OM224 = -(OM123*S24-OM223*C24)
  OM324 = qd[24]-OM26*S23+OM36*C23
  OMp124 = C24*(OMp123+qd[24]*OM223)+S24*(OMp223-qd[24]*OM123)
  OMp224 = C24*(OMp223-qd[24]*OM123)-S24*(OMp123+qd[24]*OM223)
  OMp324 = qdd[24]+C23*(OMp36-qd[23]*OM26)-S23*(OMp26+qd[23]*OM36)
  BS524 = -(OM124*OM124+OM324*OM324)
  BETA224 = OM124*OM224-OMp324
  BETA824 = OMp124+OM224*OM324
  ALPHA124 = ALPHA123*C24+ALPHA223*S24
  ALPHA224 = -(ALPHA123*S24-ALPHA223*C24)
  OM125 = qd[25]+OM124
  OM225 = OM224*C25+OM324*S25
  OMp125 = qdd[25]+OMp124
  OMp225 = C25*(OMp224+qd[25]*OM324)+S25*(OMp324-qd[25]*OM224)
  ALPHA125 = ALPHA124+BETA224*s.dpt[2,23]
  ALPHA225 = C25*(ALPHA224+BS524*s.dpt[2,23])+S25*(ALPHA323+BETA824*s.dpt[2,23])
  ALPHA325 = C25*(ALPHA323+BETA824*s.dpt[2,23])-S25*(ALPHA224+BS524*s.dpt[2,23])
  OM126 = OM125*C26+OM225*S26
  OM226 = -(OM125*S26-OM225*C26)
  OM326 = qd[26]-OM224*S25+OM324*C25
  OMp126 = C26*(OMp125+qd[26]*OM225)+S26*(OMp225-qd[26]*OM125)
  OMp226 = C26*(OMp225-qd[26]*OM125)-S26*(OMp125+qd[26]*OM225)
  OMp326 = qdd[26]+C25*(OMp324-qd[25]*OM224)-S25*(OMp224+qd[25]*OM324)
  BS926 = -(OM126*OM126+OM226*OM226)
  BETA326 = OMp226+OM126*OM326
  BETA626 = OM226*OM326-OMp126
  ALPHA126 = ALPHA125*C26+ALPHA225*S26
  ALPHA226 = -(ALPHA125*S26-ALPHA225*C26)
  OM127 = qd[27]+OM126
  OM227 = OM226*C27+OM326*S27
  OM327 = -(OM226*S27-OM326*C27)
  OMp127 = qdd[27]+OMp126
  OMp227 = C27*(OMp226+qd[27]*OM326)+S27*(OMp326-qd[27]*OM226)
  OM129 = qd[29]+OM126
  OM329 = -(OM226*S29-OM326*C29)
  OMp129 = qdd[29]+OMp126
  OMp329 = C29*(OMp326-qd[29]*OM226)-S29*(OMp226+qd[29]*OM326)
  ALPHA129 = ALPHA126+BETA326*s.dpt[3,25]
  ALPHA329 = C29*(ALPHA325+BS926*s.dpt[3,25])-S29*(ALPHA226+BETA626*s.dpt[3,25])
  OM130 = OM129*C30-OM329*S30
  OM230 = qd[30]+OM226*C29+OM326*S29
  OM330 = OM129*S30+OM329*C30
  OM131 = qd[31]+OM16
  OM231 = OM26*C31+OM36*S31
  OMp131 = qdd[31]+OMp16
  OMp231 = C31*(OMp26+qd[31]*OM36)+S31*(OMp36-qd[31]*OM26)
  ALPHA131 = ALPHA15+BETA26*s.dpt[2,12]+BS16*s.dpt[1,12]
  ALPHA231 = C31*(ALPHA26+BETA46*s.dpt[1,12]+BS56*s.dpt[2,12])+S31*(ALPHA36+BETA76*s.dpt[1,12]+BETA86*s.dpt[2,12])
  ALPHA331 = C31*(ALPHA36+BETA76*s.dpt[1,12]+BETA86*s.dpt[2,12])-S31*(ALPHA26+BETA46*s.dpt[1,12]+BS56*s.dpt[2,12])
  OM132 = OM131*C32+OM231*S32
  OM232 = -(OM131*S32-OM231*C32)
  OM332 = qd[32]-OM26*S31+OM36*C31
  OMp132 = C32*(OMp131+qd[32]*OM231)+S32*(OMp231-qd[32]*OM131)
  OMp232 = C32*(OMp231-qd[32]*OM131)-S32*(OMp131+qd[32]*OM231)
  OMp332 = qdd[32]+C31*(OMp36-qd[31]*OM26)-S31*(OMp26+qd[31]*OM36)
  BS532 = -(OM132*OM132+OM332*OM332)
  BETA232 = OM132*OM232-OMp332
  BETA832 = OMp132+OM232*OM332
  ALPHA132 = ALPHA131*C32+ALPHA231*S32
  ALPHA232 = -(ALPHA131*S32-ALPHA231*C32)
  OM133 = qd[33]+OM132
  OM233 = OM232*C33+OM332*S33
  OMp133 = qdd[33]+OMp132
  OMp233 = C33*(OMp232+qd[33]*OM332)+S33*(OMp332-qd[33]*OM232)
  ALPHA133 = ALPHA132+BETA232*s.dpt[2,30]
  ALPHA233 = C33*(ALPHA232+BS532*s.dpt[2,30])+S33*(ALPHA331+BETA832*s.dpt[2,30])
  ALPHA333 = C33*(ALPHA331+BETA832*s.dpt[2,30])-S33*(ALPHA232+BS532*s.dpt[2,30])
  OM134 = OM133*C34+OM233*S34
  OM234 = -(OM133*S34-OM233*C34)
  OM334 = qd[34]-OM232*S33+OM332*C33
  OMp134 = C34*(OMp133+qd[34]*OM233)+S34*(OMp233-qd[34]*OM133)
  OMp234 = C34*(OMp233-qd[34]*OM133)-S34*(OMp133+qd[34]*OM233)
  OMp334 = qdd[34]+C33*(OMp332-qd[33]*OM232)-S33*(OMp232+qd[33]*OM332)
  BS934 = -(OM134*OM134+OM234*OM234)
  BETA334 = OMp234+OM134*OM334
  BETA634 = OM234*OM334-OMp134
  ALPHA134 = ALPHA133*C34+ALPHA233*S34
  ALPHA234 = -(ALPHA133*S34-ALPHA233*C34)
  OM135 = qd[35]+OM134
  OM235 = OM234*C35+OM334*S35
  OM335 = -(OM234*S35-OM334*C35)
  OMp135 = qdd[35]+OMp134
  OMp235 = C35*(OMp234+qd[35]*OM334)+S35*(OMp334-qd[35]*OM234)
  OM137 = qd[37]+OM134
  OM337 = -(OM234*S37-OM334*C37)
  OMp137 = qdd[37]+OMp134
  OMp337 = C37*(OMp334-qd[37]*OM234)-S37*(OMp234+qd[37]*OM334)
  ALPHA137 = ALPHA134+BETA334*s.dpt[3,34]
  ALPHA337 = C37*(ALPHA333+BS934*s.dpt[3,34])-S37*(ALPHA234+BETA634*s.dpt[3,34])
  OM138 = OM137*C38-OM337*S38
  OM238 = qd[38]+OM234*C37+OM334*S37
  OM338 = OM137*S38+OM337*C38
 
# Backward Dynamics 

  Fs138 = -(s.frc[1,38]-s.m[38]*(ALPHA137*C38-ALPHA337*S38))
  Fs238 = -(s.frc[2,38]-s.m[38]*(C37*(ALPHA234+BETA634*s.dpt[3,34])+S37*(ALPHA333+BS934*s.dpt[3,34])))
  Fs338 = -(s.frc[3,38]-s.m[38]*(ALPHA137*S38+ALPHA337*C38))
  Cq138 = -(s.trq[1,38]-s.In[1,38]*(C38*(OMp137-qd[38]*OM337)-S38*(OMp337+qd[38]*OM137))+OM238*OM338*(s.In[5,38]-\
   s.In[9,38]))
  Cq238 = -(s.trq[2,38]-s.In[5,38]*(qdd[38]+C37*(OMp234+qd[37]*OM334)+S37*(OMp334-qd[37]*OM234))-OM138*OM338*(s.In[1,38]\
   -s.In[9,38]))
  Cq338 = -(s.trq[3,38]-s.In[9,38]*(C38*(OMp337+qd[38]*OM137)+S38*(OMp137-qd[38]*OM337))+OM138*OM238*(s.In[1,38]-\
   s.In[5,38]))
  Fq137 = Fs138*C38+Fs338*S38
  Fq337 = -(Fs138*S38-Fs338*C38)
  Cq137 = Cq138*C38+Cq338*S38
  Cq337 = -(Cq138*S38-Cq338*C38)
  Fs136 = -(s.frc[1,36]-s.m[36]*(ALPHA134+q[36]*(OMp235+OM135*OM335)+(2.0)*qd[36]*OM235+BETA334*s.dpt[3,33]+s.l[3,36]*(OMp235\
   +OM135*OM335)))
  Fs236 = -(s.frc[2,36]+s.m[36]*(q[36]*(OMp135-OM235*OM335)+(2.0)*qd[36]*OM135+s.l[3,36]*(OMp135-OM235*OM335)-C35*(ALPHA234+\
   BETA634*s.dpt[3,33])-S35*(ALPHA333+BS934*s.dpt[3,33])))
  Fs336 = -(s.frc[3,36]-s.m[36]*(qdd[36]-q[36]*(OM135*OM135+OM235*OM235)-s.l[3,36]*(OM135*OM135+OM235*OM235)+C35*(\
   ALPHA333+BS934*s.dpt[3,33])-S35*(ALPHA234+BETA634*s.dpt[3,33])))
  Cq336 = -(s.trq[3,36]-s.In[9,36]*(C35*(OMp334-qd[35]*OM234)-S35*(OMp234+qd[35]*OM334))+OM135*OM235*(s.In[1,36]-\
   s.In[5,36]))
  Cq135 = -(s.trq[1,36]+q[36]*Fs236-s.In[1,36]*OMp135+Fs236*s.l[3,36]+OM235*OM335*(s.In[5,36]-s.In[9,36]))
  Cq235 = -(s.trq[2,36]-q[36]*Fs136-s.In[5,36]*OMp235-Fs136*s.l[3,36]-OM135*OM335*(s.In[1,36]-s.In[9,36]))
  Fs134 = -(s.frc[1,34]-s.m[34]*(ALPHA134+BETA334*s.l[3,34]))
  Fs234 = -(s.frc[2,34]-s.m[34]*(ALPHA234+BETA634*s.l[3,34]))
  Fq134 = Fq137+Fs134+Fs136
  Fq234 = Fs234-Fq337*S37+Fs236*C35+Fs238*C37-Fs336*S35
  Fq334 = -(s.frc[3,34]-s.m[34]*(ALPHA333+BS934*s.l[3,34])-Fq337*C37-Fs236*S35-Fs238*S37-Fs336*C35)
  Cq134 = -(s.trq[1,34]-Cq135-Cq137-s.In[1,34]*OMp134+Fs234*s.l[3,34]+OM234*OM334*(s.In[5,34]-s.In[9,34])+s.dpt[3,33]*(\
   Fs236*C35-Fs336*S35)-s.dpt[3,34]*(Fq337*S37-Fs238*C37))
  Cq234 = -(s.trq[2,34]-s.In[5,34]*OMp234-Cq235*C35-Cq238*C37+Cq336*S35+Cq337*S37-Fq137*s.dpt[3,34]-Fs134*s.l[3,34]-\
   Fs136*s.dpt[3,33]-OM134*OM334*(s.In[1,34]-s.In[9,34]))
  Cq334 = -(s.trq[3,34]-s.In[9,34]*OMp334-Cq235*S35-Cq238*S37-Cq336*C35-Cq337*C37+OM134*OM234*(s.In[1,34]-s.In[5,34]))
  Fq133 = Fq134*C34-Fq234*S34
  Fq233 = Fq134*S34+Fq234*C34
  Cq133 = Cq134*C34-Cq234*S34
  Cq233 = Cq134*S34+Cq234*C34
  Fs132 = -(s.frc[1,32]-s.m[32]*(ALPHA132+BETA232*s.l[2,32]))
  Fs332 = -(s.frc[3,32]-s.m[32]*(ALPHA331+BETA832*s.l[2,32]))
  Fq132 = Fq133+Fs132
  Fq232 = -(s.frc[2,32]-s.m[32]*(ALPHA232+BS532*s.l[2,32])-Fq233*C33+Fq334*S33)
  Fq332 = Fs332+Fq233*S33+Fq334*C33
  Cq132 = -(s.trq[1,32]-Cq133-s.In[1,32]*OMp132-Fs332*s.l[2,32]+OM232*OM332*(s.In[5,32]-s.In[9,32])-s.dpt[2,30]*(Fq233*\
   S33+Fq334*C33))
  Cq232 = -(s.trq[2,32]-s.In[5,32]*OMp232-Cq233*C33+Cq334*S33-OM132*OM332*(s.In[1,32]-s.In[9,32]))
  Cq332 = -(s.trq[3,32]-s.In[9,32]*OMp332-Cq233*S33-Cq334*C33+Fq133*s.dpt[2,30]+Fs132*s.l[2,32]+OM132*OM232*(s.In[1,32]-\
   s.In[5,32]))
  Fq131 = Fq132*C32-Fq232*S32
  Fq231 = Fq132*S32+Fq232*C32
  Cq131 = Cq132*C32-Cq232*S32
  Cq231 = Cq132*S32+Cq232*C32
  Fs130 = -(s.frc[1,30]-s.m[30]*(ALPHA129*C30-ALPHA329*S30))
  Fs230 = -(s.frc[2,30]-s.m[30]*(C29*(ALPHA226+BETA626*s.dpt[3,25])+S29*(ALPHA325+BS926*s.dpt[3,25])))
  Fs330 = -(s.frc[3,30]-s.m[30]*(ALPHA129*S30+ALPHA329*C30))
  Cq130 = -(s.trq[1,30]-s.In[1,30]*(C30*(OMp129-qd[30]*OM329)-S30*(OMp329+qd[30]*OM129))+OM230*OM330*(s.In[5,30]-\
   s.In[9,30]))
  Cq230 = -(s.trq[2,30]-s.In[5,30]*(qdd[30]+C29*(OMp226+qd[29]*OM326)+S29*(OMp326-qd[29]*OM226))-OM130*OM330*(s.In[1,30]\
   -s.In[9,30]))
  Cq330 = -(s.trq[3,30]-s.In[9,30]*(C30*(OMp329+qd[30]*OM129)+S30*(OMp129-qd[30]*OM329))+OM130*OM230*(s.In[1,30]-\
   s.In[5,30]))
  Fq129 = Fs130*C30+Fs330*S30
  Fq329 = -(Fs130*S30-Fs330*C30)
  Cq129 = Cq130*C30+Cq330*S30
  Cq329 = -(Cq130*S30-Cq330*C30)
  Fs128 = -(s.frc[1,28]-s.m[28]*(ALPHA126+q[28]*(OMp227+OM127*OM327)+(2.0)*qd[28]*OM227+BETA326*s.dpt[3,24]+s.l[3,28]*(OMp227\
   +OM127*OM327)))
  Fs228 = -(s.frc[2,28]+s.m[28]*(q[28]*(OMp127-OM227*OM327)+(2.0)*qd[28]*OM127+s.l[3,28]*(OMp127-OM227*OM327)-C27*(ALPHA226+\
   BETA626*s.dpt[3,24])-S27*(ALPHA325+BS926*s.dpt[3,24])))
  Fs328 = -(s.frc[3,28]-s.m[28]*(qdd[28]-q[28]*(OM127*OM127+OM227*OM227)-s.l[3,28]*(OM127*OM127+OM227*OM227)+C27*(\
   ALPHA325+BS926*s.dpt[3,24])-S27*(ALPHA226+BETA626*s.dpt[3,24])))
  Cq328 = -(s.trq[3,28]-s.In[9,28]*(C27*(OMp326-qd[27]*OM226)-S27*(OMp226+qd[27]*OM326))+OM127*OM227*(s.In[1,28]-\
   s.In[5,28]))
  Cq127 = -(s.trq[1,28]+q[28]*Fs228-s.In[1,28]*OMp127+Fs228*s.l[3,28]+OM227*OM327*(s.In[5,28]-s.In[9,28]))
  Cq227 = -(s.trq[2,28]-q[28]*Fs128-s.In[5,28]*OMp227-Fs128*s.l[3,28]-OM127*OM327*(s.In[1,28]-s.In[9,28]))
  Fs126 = -(s.frc[1,26]-s.m[26]*(ALPHA126+BETA326*s.l[3,26]))
  Fs226 = -(s.frc[2,26]-s.m[26]*(ALPHA226+BETA626*s.l[3,26]))
  Fq126 = Fq129+Fs126+Fs128
  Fq226 = Fs226-Fq329*S29+Fs228*C27+Fs230*C29-Fs328*S27
  Fq326 = -(s.frc[3,26]-s.m[26]*(ALPHA325+BS926*s.l[3,26])-Fq329*C29-Fs228*S27-Fs230*S29-Fs328*C27)
  Cq126 = -(s.trq[1,26]-Cq127-Cq129-s.In[1,26]*OMp126+Fs226*s.l[3,26]+OM226*OM326*(s.In[5,26]-s.In[9,26])+s.dpt[3,24]*(\
   Fs228*C27-Fs328*S27)-s.dpt[3,25]*(Fq329*S29-Fs230*C29))
  Cq226 = -(s.trq[2,26]-s.In[5,26]*OMp226-Cq227*C27-Cq230*C29+Cq328*S27+Cq329*S29-Fq129*s.dpt[3,25]-Fs126*s.l[3,26]-\
   Fs128*s.dpt[3,24]-OM126*OM326*(s.In[1,26]-s.In[9,26]))
  Cq326 = -(s.trq[3,26]-s.In[9,26]*OMp326-Cq227*S27-Cq230*S29-Cq328*C27-Cq329*C29+OM126*OM226*(s.In[1,26]-s.In[5,26]))
  Fq125 = Fq126*C26-Fq226*S26
  Fq225 = Fq126*S26+Fq226*C26
  Cq125 = Cq126*C26-Cq226*S26
  Cq225 = Cq126*S26+Cq226*C26
  Fs124 = -(s.frc[1,24]-s.m[24]*(ALPHA124+BETA224*s.l[2,24]))
  Fs324 = -(s.frc[3,24]-s.m[24]*(ALPHA323+BETA824*s.l[2,24]))
  Fq124 = Fq125+Fs124
  Fq224 = -(s.frc[2,24]-s.m[24]*(ALPHA224+BS524*s.l[2,24])-Fq225*C25+Fq326*S25)
  Fq324 = Fs324+Fq225*S25+Fq326*C25
  Cq124 = -(s.trq[1,24]-Cq125-s.In[1,24]*OMp124-Fs324*s.l[2,24]+OM224*OM324*(s.In[5,24]-s.In[9,24])-s.dpt[2,23]*(Fq225*\
   S25+Fq326*C25))
  Cq224 = -(s.trq[2,24]-s.In[5,24]*OMp224-Cq225*C25+Cq326*S25-OM124*OM324*(s.In[1,24]-s.In[9,24]))
  Cq324 = -(s.trq[3,24]-s.In[9,24]*OMp324-Cq225*S25-Cq326*C25+Fq125*s.dpt[2,23]+Fs124*s.l[2,24]+OM124*OM224*(s.In[1,24]-\
   s.In[5,24]))
  Fq123 = Fq124*C24-Fq224*S24
  Fq223 = Fq124*S24+Fq224*C24
  Cq123 = Cq124*C24-Cq224*S24
  Cq223 = Cq124*S24+Cq224*C24
  Fs122 = -(s.frc[1,22]-s.m[22]*(ALPHA118*C22-ALPHA321*S22))
  Fs222 = -(s.frc[2,22]-s.m[22]*(ALPHA217*C21+ALPHA318*S21))
  Fs322 = -(s.frc[3,22]-s.m[22]*(ALPHA118*S22+ALPHA321*C22))
  Cq122 = -(s.trq[1,22]-s.In[1,22]*(C22*(OMp121-qd[22]*OM321)-S22*(OMp321+qd[22]*OM121))+OM222*OM322*(s.In[5,22]-\
   s.In[9,22]))
  Cq222 = -(s.trq[2,22]-s.In[5,22]*(qdd[22]+C21*(OMp218+qd[21]*OM318)+S21*(OMp318-qd[21]*OM218))-OM122*OM322*(s.In[1,22]\
   -s.In[9,22]))
  Cq322 = -(s.trq[3,22]-s.In[9,22]*(C22*(OMp321+qd[22]*OM121)+S22*(OMp121-qd[22]*OM321))+OM122*OM222*(s.In[1,22]-\
   s.In[5,22]))
  Fq321 = -(Fs122*S22-Fs322*C22)
  Cq121 = Cq122*C22+Cq322*S22
  Cq321 = -(Cq122*S22-Cq322*C22)
  Fs120 = -(s.frc[1,20]-s.m[20]*(ALPHA118+q[20]*(OMp219+OM119*OM319)+(2.0)*qd[20]*OM219+BETA318*s.dpt[3,19]+s.l[3,20]*(OMp219\
   +OM119*OM319)))
  Fs220 = -(s.frc[2,20]+s.m[20]*(q[20]*(OMp119-OM219*OM319)+(2.0)*qd[20]*OM119+s.l[3,20]*(OMp119-OM219*OM319)-C19*(ALPHA217+\
   BETA618*s.dpt[3,19])-S19*(ALPHA318+BS918*s.dpt[3,19])))
  Fs320 = -(s.frc[3,20]-s.m[20]*(qdd[20]-q[20]*(OM119*OM119+OM219*OM219)-s.l[3,20]*(OM119*OM119+OM219*OM219)+C19*(\
   ALPHA318+BS918*s.dpt[3,19])-S19*(ALPHA217+BETA618*s.dpt[3,19])))
  Cq320 = -(s.trq[3,20]-s.In[9,20]*(C19*(OMp318-qd[19]*OM218)-S19*(OMp218+qd[19]*OM318))+OM119*OM219*(s.In[1,20]-\
   s.In[5,20]))
  Cq119 = -(s.trq[1,20]+q[20]*Fs220-s.In[1,20]*OMp119+Fs220*s.l[3,20]+OM219*OM319*(s.In[5,20]-s.In[9,20]))
  Cq219 = -(s.trq[2,20]-q[20]*Fs120-s.In[5,20]*OMp219-Fs120*s.l[3,20]-OM119*OM319*(s.In[1,20]-s.In[9,20]))
  Fs118 = -(s.frc[1,18]-s.m[18]*(ALPHA118+BETA318*s.l[3,18]))
  Fs218 = -(s.frc[2,18]-s.m[18]*(ALPHA217+BETA618*s.l[3,18]))
  Fq118 = Fs118+Fs120+Fs122*C22+Fs322*S22
  Fq218 = Fs218-Fq321*S21+Fs220*C19+Fs222*C21-Fs320*S19
  Fq318 = -(s.frc[3,18]-s.m[18]*(ALPHA318+BS918*s.l[3,18])-Fq321*C21-Fs220*S19-Fs222*S21-Fs320*C19)
  Cq118 = -(s.trq[1,18]-Cq119-Cq121-s.In[1,18]*OMp118-s.In[9,18]*OM218*OM318+Fs218*s.l[3,18]+s.dpt[3,19]*(Fs220*C19-\
   Fs320*S19))
  Cq218 = -(s.trq[2,18]-Cq219*C19-Cq222*C21+Cq320*S19+Cq321*S21-Fs118*s.l[3,18]-Fs120*s.dpt[3,19]-OM118*OM318*(\
   s.In[1,18]-s.In[9,18]))
  Cq318 = -(s.trq[3,18]+s.In[1,18]*OM118*OM218-s.In[9,18]*OMp318-Cq219*S19-Cq222*S21-Cq320*C19-Cq321*C21)
  Fq117 = Fq118*C18+Fq318*S18
  Fq317 = -(Fq118*S18-Fq318*C18)
  Cq117 = Cq118*C18+Cq318*S18
  Cq317 = -(Cq118*S18-Cq318*C18)
  Fq216 = Fq218*C17-Fq317*S17
  Fq316 = Fq218*S17+Fq317*C17
  Cq216 = Cq218*C17-Cq317*S17
  Cq316 = Cq218*S17+Cq317*C17
  Fs115 = -(s.frc[1,15]-s.m[15]*(ALPHA115+BETA215*s.l[2,15]))
  Fs315 = -(s.frc[3,15]-s.m[15]*(ALPHA315+BETA815*s.l[2,15]))
  Fq115 = Fs115+Fq117*C16-Fq216*S16
  Fq215 = -(s.frc[2,15]-s.m[15]*(ALPHA215+BS515*s.l[2,15])-Fq117*S16-Fq216*C16)
  Fq315 = Fq316+Fs315
  Cq115 = -(s.trq[1,15]-s.In[1,15]*OMp115-s.In[9,15]*OM215*OM315-Cq117*C16+Cq216*S16-Fq316*s.dpt[2,18]-Fs315*s.l[2,15])
  Cq215 = -(s.trq[2,15]-Cq117*S16-Cq216*C16-OM115*OM315*(s.In[1,15]-s.In[9,15]))
  Cq315 = -(s.trq[3,15]-Cq316+s.In[1,15]*OM115*OM215-s.In[9,15]*OMp315+Fs115*s.l[2,15]+s.dpt[2,18]*(Fq117*C16-Fq216*S16)\
   )
  Fs114 = -(s.frc[1,14]-s.m[14]*(ALPHA110*C14-ALPHA313*S14))
  Fs214 = -(s.frc[2,14]-s.m[14]*(ALPHA29*C13+ALPHA310*S13))
  Fs314 = -(s.frc[3,14]-s.m[14]*(ALPHA110*S14+ALPHA313*C14))
  Cq114 = -(s.trq[1,14]-s.In[1,14]*(C14*(OMp113-qd[14]*OM313)-S14*(OMp313+qd[14]*OM113))+OM214*OM314*(s.In[5,14]-\
   s.In[9,14]))
  Cq214 = -(s.trq[2,14]-s.In[5,14]*(qdd[14]+C13*(OMp210+qd[13]*OM310)+S13*(OMp310-qd[13]*OM210))-OM114*OM314*(s.In[1,14]\
   -s.In[9,14]))
  Cq314 = -(s.trq[3,14]-s.In[9,14]*(C14*(OMp313+qd[14]*OM113)+S14*(OMp113-qd[14]*OM313))+OM114*OM214*(s.In[1,14]-\
   s.In[5,14]))
  Fq313 = -(Fs114*S14-Fs314*C14)
  Cq113 = Cq114*C14+Cq314*S14
  Cq313 = -(Cq114*S14-Cq314*C14)
  Fs112 = -(s.frc[1,12]-s.m[12]*(ALPHA110+q[12]*(OMp211+OM111*OM311)+(2.0)*qd[12]*OM211+BETA310*s.dpt[3,14]+s.l[3,12]*(OMp211\
   +OM111*OM311)))
  Fs212 = -(s.frc[2,12]+s.m[12]*(q[12]*(OMp111-OM211*OM311)+(2.0)*qd[12]*OM111+s.l[3,12]*(OMp111-OM211*OM311)-C11*(ALPHA29+\
   BETA610*s.dpt[3,14])-S11*(ALPHA310+BS910*s.dpt[3,14])))
  Fs312 = -(s.frc[3,12]-s.m[12]*(qdd[12]-q[12]*(OM111*OM111+OM211*OM211)-s.l[3,12]*(OM111*OM111+OM211*OM211)+C11*(\
   ALPHA310+BS910*s.dpt[3,14])-S11*(ALPHA29+BETA610*s.dpt[3,14])))
  Cq312 = -(s.trq[3,12]-s.In[9,12]*(C11*(OMp310-qd[11]*OM210)-S11*(OMp210+qd[11]*OM310))+OM111*OM211*(s.In[1,12]-\
   s.In[5,12]))
  Cq111 = -(s.trq[1,12]+q[12]*Fs212-s.In[1,12]*OMp111+Fs212*s.l[3,12]+OM211*OM311*(s.In[5,12]-s.In[9,12]))
  Cq211 = -(s.trq[2,12]-q[12]*Fs112-s.In[5,12]*OMp211-Fs112*s.l[3,12]-OM111*OM311*(s.In[1,12]-s.In[9,12]))
  Fs110 = -(s.frc[1,10]-s.m[10]*(ALPHA110+BETA310*s.l[3,10]))
  Fs210 = -(s.frc[2,10]-s.m[10]*(ALPHA29+BETA610*s.l[3,10]))
  Fq110 = Fs110+Fs112+Fs114*C14+Fs314*S14
  Fq210 = Fs210-Fq313*S13+Fs212*C11+Fs214*C13-Fs312*S11
  Fq310 = -(s.frc[3,10]-s.m[10]*(ALPHA310+BS910*s.l[3,10])-Fq313*C13-Fs212*S11-Fs214*S13-Fs312*C11)
  Cq110 = -(s.trq[1,10]-Cq111-Cq113-s.In[1,10]*OMp110-s.In[9,10]*OM210*OM310+Fs210*s.l[3,10]+s.dpt[3,14]*(Fs212*C11-\
   Fs312*S11))
  Cq210 = -(s.trq[2,10]-Cq211*C11-Cq214*C13+Cq312*S11+Cq313*S13-Fs110*s.l[3,10]-Fs112*s.dpt[3,14]-OM110*OM310*(\
   s.In[1,10]-s.In[9,10]))
  Cq310 = -(s.trq[3,10]+s.In[1,10]*OM110*OM210-s.In[9,10]*OMp310-Cq211*S11-Cq214*S13-Cq312*C11-Cq313*C13)
  Fq19 = Fq110*C10+Fq310*S10
  Fq39 = -(Fq110*S10-Fq310*C10)
  Cq19 = Cq110*C10+Cq310*S10
  Cq39 = -(Cq110*S10-Cq310*C10)
  Fq28 = Fq210*C9-Fq39*S9
  Fq38 = Fq210*S9+Fq39*C9
  Cq28 = Cq210*C9-Cq39*S9
  Cq38 = Cq210*S9+Cq39*C9
  Fs17 = -(s.frc[1,7]-s.m[7]*(ALPHA17+BETA27*s.l[2,7]))
  Fs37 = -(s.frc[3,7]-s.m[7]*(ALPHA37+BETA87*s.l[2,7]))
  Fq17 = Fs17+Fq19*C8-Fq28*S8
  Fq27 = -(s.frc[2,7]-s.m[7]*(ALPHA27+BS57*s.l[2,7])-Fq19*S8-Fq28*C8)
  Fq37 = Fq38+Fs37
  Cq17 = -(s.trq[1,7]-s.In[1,7]*OMp17-s.In[9,7]*OM27*OM37-Cq19*C8+Cq28*S8-Fq38*s.dpt[2,13]-Fs37*s.l[2,7])
  Cq27 = -(s.trq[2,7]-Cq19*S8-Cq28*C8-OM17*OM37*(s.In[1,7]-s.In[9,7]))
  Cq37 = -(s.trq[3,7]-Cq38+s.In[1,7]*OM17*OM27-s.In[9,7]*OMp37+Fs17*s.l[2,7]+s.dpt[2,13]*(Fq19*C8-Fq28*S8))
  Fs16 = -(s.frc[1,6]-s.m[6]*(ALPHA15+BETA36*s.l[3,6]))
  Fs26 = -(s.frc[2,6]-s.m[6]*(ALPHA26+BETA66*s.l[3,6]))
  Fq16 = Fq115+Fq123+Fq131+Fq17+Fs16
  Fq26 = Fs26+Fq215*C15+Fq223*C23+Fq231*C31+Fq27*C7-Fq315*S15-Fq324*S23-Fq332*S31-Fq37*S7
  Fq36 = -(s.frc[3,6]-s.m[6]*(ALPHA36+BS96*s.l[3,6])-Fq215*S15-Fq223*S23-Fq231*S31-Fq27*S7-Fq315*C15-Fq324*C23-Fq332*C31\
   -Fq37*C7)
  Cq16 = -(s.trq[1,6]-Cq115-Cq123-Cq131-Cq17-s.In[1,6]*OMp16+Fs26*s.l[3,6]+OM26*OM36*(s.In[5,6]-s.In[9,6])-s.dpt[2,10]*(\
   Fq223*S23+Fq324*C23)-s.dpt[2,12]*(Fq231*S31+Fq332*C31)-s.dpt[2,1]*(Fq27*S7+Fq37*C7)-s.dpt[2,4]*(Fq215*S15+Fq315*C15)+\
   s.dpt[3,1]*(Fq27*C7-Fq37*S7)+s.dpt[3,4]*(Fq215*C15-Fq315*S15))
  Cq26 = -(s.trq[2,6]-s.In[5,6]*OMp26-Cq215*C15-Cq223*C23-Cq231*C31-Cq27*C7+Cq315*S15+Cq324*S23+Cq332*S31+Cq37*S7-Fq115*\
   s.dpt[3,4]-Fq17*s.dpt[3,1]-Fs16*s.l[3,6]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,10]*(Fq223*S23+Fq324*C23)+s.dpt[1,12]*(\
   Fq231*S31+Fq332*C31)+s.dpt[1,1]*(Fq27*S7+Fq37*C7)+s.dpt[1,4]*(Fq215*S15+Fq315*C15))
  Cq36 = -(s.trq[3,6]-s.In[9,6]*OMp36-Cq215*S15-Cq223*S23-Cq231*S31-Cq27*S7-Cq315*C15-Cq324*C23-Cq332*C31-Cq37*C7+Fq115*\
   s.dpt[2,4]+Fq123*s.dpt[2,10]+Fq131*s.dpt[2,12]+Fq17*s.dpt[2,1]+OM16*OM26*(s.In[1,6]-s.In[5,6])-s.dpt[1,10]*(Fq223*C23-Fq324*\
   S23)-s.dpt[1,12]*(Fq231*C31-Fq332*S31)-s.dpt[1,1]*(Fq27*C7-Fq37*S7)-s.dpt[1,4]*(Fq215*C15-Fq315*S15))
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
  Qq[28] = Fs328
  Qq[29] = Cq129
  Qq[30] = Cq230
  Qq[31] = Cq131
  Qq[32] = Cq332
  Qq[33] = Cq133
  Qq[34] = Cq334
  Qq[35] = Cq135
  Qq[36] = Fs336
  Qq[37] = Cq137
  Qq[38] = Cq238

# ====== END Task 0 ====== 

  

