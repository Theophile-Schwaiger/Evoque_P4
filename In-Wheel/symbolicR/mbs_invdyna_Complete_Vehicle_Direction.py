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
#	==> Generation Date : Fri Apr  3 02:23:56 2020
#
#	==> Project name : Complete_Vehicle_Direction
#	==> using XML input file 
#
#	==> Number of joints : 41
#
#	==> Function : F 2 : Inverse Dynamics : RNEA
#	==> Flops complexity : 2734
#
#	==> Generation Time :  0.040 seconds
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
  C27 = np.cos(q[27])
  S27 = np.sin(q[27])

# = = Block_0_0_0_0_0_9 = = 
 
# Trigonometric Variables  

  C28 = np.cos(q[28])
  S28 = np.sin(q[28])

# = = Block_0_0_0_0_0_10 = = 
 
# Trigonometric Variables  

  C30 = np.cos(q[30])
  S30 = np.sin(q[30])
  C31 = np.cos(q[31])
  S31 = np.sin(q[31])

# = = Block_0_0_0_0_0_11 = = 
 
# Trigonometric Variables  

  C32 = np.cos(q[32])
  S32 = np.sin(q[32])
  C33 = np.cos(q[33])
  S33 = np.sin(q[33])
  C34 = np.cos(q[34])
  S34 = np.sin(q[34])
  C35 = np.cos(q[35])
  S35 = np.sin(q[35])
  C36 = np.cos(q[36])
  S36 = np.sin(q[36])

# = = Block_0_0_0_0_0_12 = = 
 
# Trigonometric Variables  

  C37 = np.cos(q[37])
  S37 = np.sin(q[37])

# = = Block_0_0_0_0_0_13 = = 
 
# Trigonometric Variables  

  C39 = np.cos(q[39])
  S39 = np.sin(q[39])
  C40 = np.cos(q[40])
  S40 = np.sin(q[40])

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
  BETA26 = BS26-OMp36
  BETA46 = BS26+OMp36
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
  ALPHA18 = C8*(ALPHA17+BETA27*s.dpt[2,14])+S8*(ALPHA27+BS57*s.dpt[2,14])
  ALPHA28 = C8*(ALPHA27+BS57*s.dpt[2,14])-S8*(ALPHA17+BETA27*s.dpt[2,14])
  ALPHA38 = ALPHA37+BETA87*s.dpt[2,14]
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
  ALPHA113 = ALPHA110+BETA310*s.dpt[3,16]
  ALPHA313 = C13*(ALPHA310+BS910*s.dpt[3,16])-S13*(ALPHA29+BETA610*s.dpt[3,16])
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
  ALPHA116 = C16*(ALPHA115+BETA215*s.dpt[2,20])+S16*(ALPHA215+BS515*s.dpt[2,20])
  ALPHA216 = C16*(ALPHA215+BS515*s.dpt[2,20])-S16*(ALPHA115+BETA215*s.dpt[2,20])
  ALPHA316 = ALPHA315+BETA815*s.dpt[2,20]
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
  ALPHA121 = ALPHA118+BETA318*s.dpt[3,22]
  ALPHA321 = C21*(ALPHA318+BS918*s.dpt[3,22])-S21*(ALPHA217+BETA618*s.dpt[3,22])
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
  OM325 = -(OM224*S25-OM324*C25)
  OMp125 = qdd[25]+OMp124
  OMp325 = C25*(OMp324-qd[25]*OM224)-S25*(OMp224+qd[25]*OM324)
  ALPHA125 = ALPHA124+BETA224*s.dpt[2,26]
  ALPHA225 = C25*(ALPHA224+BS524*s.dpt[2,26])+S25*(ALPHA323+BETA824*s.dpt[2,26])
  ALPHA325 = C25*(ALPHA323+BETA824*s.dpt[2,26])-S25*(ALPHA224+BS524*s.dpt[2,26])
  OM126 = OM125*C26-OM325*S26
  OM226 = qd[26]+OM224*C25+OM324*S25
  OMp126 = C26*(OMp125-qd[26]*OM325)-S26*(OMp325+qd[26]*OM125)
  OMp226 = qdd[26]+C25*(OMp224+qd[25]*OM324)+S25*(OMp324-qd[25]*OM224)
  ALPHA126 = ALPHA125*C26-ALPHA325*S26
  ALPHA326 = ALPHA125*S26+ALPHA325*C26
  OM127 = OM126*C27+OM226*S27
  OM227 = -(OM126*S27-OM226*C27)
  OM327 = qd[27]+OM125*S26+OM325*C26
  OMp127 = C27*(OMp126+qd[27]*OM226)+S27*(OMp226-qd[27]*OM126)
  OMp227 = C27*(OMp226-qd[27]*OM126)-S27*(OMp126+qd[27]*OM226)
  OMp327 = qdd[27]+C26*(OMp325+qd[26]*OM125)+S26*(OMp125-qd[26]*OM325)
  BS927 = -(OM127*OM127+OM227*OM227)
  BETA327 = OMp227+OM127*OM327
  BETA627 = OM227*OM327-OMp127
  ALPHA127 = ALPHA126*C27+ALPHA225*S27
  ALPHA227 = -(ALPHA126*S27-ALPHA225*C27)
  OM128 = qd[28]+OM127
  OM228 = OM227*C28+OM327*S28
  OM328 = -(OM227*S28-OM327*C28)
  OMp128 = qdd[28]+OMp127
  OMp228 = C28*(OMp227+qd[28]*OM327)+S28*(OMp327-qd[28]*OM227)
  OM130 = qd[30]+OM127
  OM330 = -(OM227*S30-OM327*C30)
  OMp130 = qdd[30]+OMp127
  OMp330 = C30*(OMp327-qd[30]*OM227)-S30*(OMp227+qd[30]*OM327)
  ALPHA130 = ALPHA127+BETA327*s.dpt[3,28]
  ALPHA330 = C30*(ALPHA326+BS927*s.dpt[3,28])-S30*(ALPHA227+BETA627*s.dpt[3,28])
  OM131 = OM130*C31-OM330*S31
  OM231 = qd[31]+OM227*C30+OM327*S30
  OM331 = OM130*S31+OM330*C31
  OM132 = qd[32]+OM16
  OM232 = OM26*C32+OM36*S32
  OMp132 = qdd[32]+OMp16
  OMp232 = C32*(OMp26+qd[32]*OM36)+S32*(OMp36-qd[32]*OM26)
  ALPHA132 = ALPHA15+BETA26*s.dpt[2,12]+BS16*s.dpt[1,12]
  ALPHA232 = C32*(ALPHA26+BETA46*s.dpt[1,12]+BS56*s.dpt[2,12])+S32*(ALPHA36+BETA76*s.dpt[1,12]+BETA86*s.dpt[2,12])
  ALPHA332 = C32*(ALPHA36+BETA76*s.dpt[1,12]+BETA86*s.dpt[2,12])-S32*(ALPHA26+BETA46*s.dpt[1,12]+BS56*s.dpt[2,12])
  OM133 = OM132*C33+OM232*S33
  OM233 = -(OM132*S33-OM232*C33)
  OM333 = qd[33]-OM26*S32+OM36*C32
  OMp133 = C33*(OMp132+qd[33]*OM232)+S33*(OMp232-qd[33]*OM132)
  OMp233 = C33*(OMp232-qd[33]*OM132)-S33*(OMp132+qd[33]*OM232)
  OMp333 = qdd[33]+C32*(OMp36-qd[32]*OM26)-S32*(OMp26+qd[32]*OM36)
  BS533 = -(OM133*OM133+OM333*OM333)
  BETA233 = OM133*OM233-OMp333
  BETA833 = OMp133+OM233*OM333
  ALPHA133 = ALPHA132*C33+ALPHA232*S33
  ALPHA233 = -(ALPHA132*S33-ALPHA232*C33)
  OM134 = qd[34]+OM133
  OM334 = -(OM233*S34-OM333*C34)
  OMp134 = qdd[34]+OMp133
  OMp334 = C34*(OMp333-qd[34]*OM233)-S34*(OMp233+qd[34]*OM333)
  ALPHA134 = ALPHA133+BETA233*s.dpt[2,33]
  ALPHA234 = C34*(ALPHA233+BS533*s.dpt[2,33])+S34*(ALPHA332+BETA833*s.dpt[2,33])
  ALPHA334 = C34*(ALPHA332+BETA833*s.dpt[2,33])-S34*(ALPHA233+BS533*s.dpt[2,33])
  OM135 = OM134*C35-OM334*S35
  OM235 = qd[35]+OM233*C34+OM333*S34
  OMp135 = C35*(OMp134-qd[35]*OM334)-S35*(OMp334+qd[35]*OM134)
  OMp235 = qdd[35]+C34*(OMp233+qd[34]*OM333)+S34*(OMp333-qd[34]*OM233)
  ALPHA135 = ALPHA134*C35-ALPHA334*S35
  ALPHA335 = ALPHA134*S35+ALPHA334*C35
  OM136 = OM135*C36+OM235*S36
  OM236 = -(OM135*S36-OM235*C36)
  OM336 = qd[36]+OM134*S35+OM334*C35
  OMp136 = C36*(OMp135+qd[36]*OM235)+S36*(OMp235-qd[36]*OM135)
  OMp236 = C36*(OMp235-qd[36]*OM135)-S36*(OMp135+qd[36]*OM235)
  OMp336 = qdd[36]+C35*(OMp334+qd[35]*OM134)+S35*(OMp134-qd[35]*OM334)
  BS936 = -(OM136*OM136+OM236*OM236)
  BETA336 = OMp236+OM136*OM336
  BETA636 = OM236*OM336-OMp136
  ALPHA136 = ALPHA135*C36+ALPHA234*S36
  ALPHA236 = -(ALPHA135*S36-ALPHA234*C36)
  OM137 = qd[37]+OM136
  OM237 = OM236*C37+OM336*S37
  OM337 = -(OM236*S37-OM336*C37)
  OMp137 = qdd[37]+OMp136
  OMp237 = C37*(OMp236+qd[37]*OM336)+S37*(OMp336-qd[37]*OM236)
  OM139 = qd[39]+OM136
  OM339 = -(OM236*S39-OM336*C39)
  OMp139 = qdd[39]+OMp136
  OMp339 = C39*(OMp336-qd[39]*OM236)-S39*(OMp236+qd[39]*OM336)
  ALPHA139 = ALPHA136+BETA336*s.dpt[3,37]
  ALPHA339 = C39*(ALPHA335+BS936*s.dpt[3,37])-S39*(ALPHA236+BETA636*s.dpt[3,37])
  OM140 = OM139*C40-OM339*S40
  OM240 = qd[40]+OM236*C39+OM336*S39
  OM340 = OM139*S40+OM339*C40
 
# Backward Dynamics 

  Fs141 = -(s.frc[1,41]-s.m[41]*(ALPHA15+q[41]*BETA26-(2.0)*qd[41]*OM36+BS16*s.dpt[1,13]))
  Fs241 = -(s.frc[2,41]-s.m[41]*(qdd[41]+ALPHA26+q[41]*BS56+BETA46*s.dpt[1,13]))
  Fs341 = -(s.frc[3,41]-s.m[41]*(ALPHA36+q[41]*BETA86+(2.0)*qd[41]*OM16+BETA76*s.dpt[1,13]))
  Fs140 = -(s.frc[1,40]-s.m[40]*(ALPHA139*C40-ALPHA339*S40))
  Fs240 = -(s.frc[2,40]-s.m[40]*(C39*(ALPHA236+BETA636*s.dpt[3,37])+S39*(ALPHA335+BS936*s.dpt[3,37])))
  Fs340 = -(s.frc[3,40]-s.m[40]*(ALPHA139*S40+ALPHA339*C40))
  Cq140 = -(s.trq[1,40]-s.In[1,40]*(C40*(OMp139-qd[40]*OM339)-S40*(OMp339+qd[40]*OM139))+OM240*OM340*(s.In[5,40]-\
   s.In[9,40]))
  Cq240 = -(s.trq[2,40]-s.In[5,40]*(qdd[40]+C39*(OMp236+qd[39]*OM336)+S39*(OMp336-qd[39]*OM236))-OM140*OM340*(s.In[1,40]\
   -s.In[9,40]))
  Cq340 = -(s.trq[3,40]-s.In[9,40]*(C40*(OMp339+qd[40]*OM139)+S40*(OMp139-qd[40]*OM339))+OM140*OM240*(s.In[1,40]-\
   s.In[5,40]))
  Fq139 = Fs140*C40+Fs340*S40
  Fq339 = -(Fs140*S40-Fs340*C40)
  Cq139 = Cq140*C40+Cq340*S40
  Cq339 = -(Cq140*S40-Cq340*C40)
  Fs138 = -(s.frc[1,38]-s.m[38]*(ALPHA136+q[38]*(OMp237+OM137*OM337)+(2.0)*qd[38]*OM237+BETA336*s.dpt[3,36]+s.l[3,38]*(OMp237\
   +OM137*OM337)))
  Fs238 = -(s.frc[2,38]+s.m[38]*(q[38]*(OMp137-OM237*OM337)+(2.0)*qd[38]*OM137+s.l[3,38]*(OMp137-OM237*OM337)-C37*(ALPHA236+\
   BETA636*s.dpt[3,36])-S37*(ALPHA335+BS936*s.dpt[3,36])))
  Fs338 = -(s.frc[3,38]-s.m[38]*(qdd[38]-q[38]*(OM137*OM137+OM237*OM237)-s.l[3,38]*(OM137*OM137+OM237*OM237)+C37*(\
   ALPHA335+BS936*s.dpt[3,36])-S37*(ALPHA236+BETA636*s.dpt[3,36])))
  Cq338 = -(s.trq[3,38]-s.In[9,38]*(C37*(OMp336-qd[37]*OM236)-S37*(OMp236+qd[37]*OM336))+OM137*OM237*(s.In[1,38]-\
   s.In[5,38]))
  Cq137 = -(s.trq[1,38]+q[38]*Fs238-s.In[1,38]*OMp137+Fs238*s.l[3,38]+OM237*OM337*(s.In[5,38]-s.In[9,38]))
  Cq237 = -(s.trq[2,38]-q[38]*Fs138-s.In[5,38]*OMp237-Fs138*s.l[3,38]-OM137*OM337*(s.In[1,38]-s.In[9,38]))
  Fs136 = -(s.frc[1,36]-s.m[36]*(ALPHA136+BETA336*s.l[3,36]))
  Fs236 = -(s.frc[2,36]-s.m[36]*(ALPHA236+BETA636*s.l[3,36]))
  Fq136 = Fq139+Fs136+Fs138
  Fq236 = Fs236-Fq339*S39+Fs238*C37+Fs240*C39-Fs338*S37
  Fq336 = -(s.frc[3,36]-s.m[36]*(ALPHA335+BS936*s.l[3,36])-Fq339*C39-Fs238*S37-Fs240*S39-Fs338*C37)
  Cq136 = -(s.trq[1,36]-Cq137-Cq139-s.In[1,36]*OMp136+Fs236*s.l[3,36]+OM236*OM336*(s.In[5,36]-s.In[9,36])+s.dpt[3,36]*(\
   Fs238*C37-Fs338*S37)-s.dpt[3,37]*(Fq339*S39-Fs240*C39))
  Cq236 = -(s.trq[2,36]-s.In[5,36]*OMp236-Cq237*C37-Cq240*C39+Cq338*S37+Cq339*S39-Fq139*s.dpt[3,37]-Fs136*s.l[3,36]-\
   Fs138*s.dpt[3,36]-OM136*OM336*(s.In[1,36]-s.In[9,36]))
  Cq336 = -(s.trq[3,36]-s.In[9,36]*OMp336-Cq237*S37-Cq240*S39-Cq338*C37-Cq339*C39+OM136*OM236*(s.In[1,36]-s.In[5,36]))
  Fq135 = Fq136*C36-Fq236*S36
  Fq235 = Fq136*S36+Fq236*C36
  Cq135 = Cq136*C36-Cq236*S36
  Cq235 = Cq136*S36+Cq236*C36
  Fq134 = Fq135*C35+Fq336*S35
  Fq334 = -(Fq135*S35-Fq336*C35)
  Cq134 = Cq135*C35+Cq336*S35
  Cq334 = -(Cq135*S35-Cq336*C35)
  Fs133 = -(s.frc[1,33]-s.m[33]*(ALPHA133+BETA233*s.l[2,33]))
  Fs333 = -(s.frc[3,33]-s.m[33]*(ALPHA332+BETA833*s.l[2,33]))
  Fq133 = Fq134+Fs133
  Fq233 = -(s.frc[2,33]-s.m[33]*(ALPHA233+BS533*s.l[2,33])-Fq235*C34+Fq334*S34)
  Fq333 = Fs333+Fq235*S34+Fq334*C34
  Cq133 = -(s.trq[1,33]-Cq134-s.In[1,33]*OMp133-s.In[9,33]*OM233*OM333-Fs333*s.l[2,33]-s.dpt[2,33]*(Fq235*S34+Fq334*C34)\
   )
  Cq233 = -(s.trq[2,33]-Cq235*C34+Cq334*S34-OM133*OM333*(s.In[1,33]-s.In[9,33]))
  Cq333 = -(s.trq[3,33]+s.In[1,33]*OM133*OM233-s.In[9,33]*OMp333-Cq235*S34-Cq334*C34+Fq134*s.dpt[2,33]+Fs133*s.l[2,33])
  Fq132 = Fq133*C33-Fq233*S33
  Fq232 = Fq133*S33+Fq233*C33
  Cq132 = Cq133*C33-Cq233*S33
  Cq232 = Cq133*S33+Cq233*C33
  Fs131 = -(s.frc[1,31]-s.m[31]*(ALPHA130*C31-ALPHA330*S31))
  Fs231 = -(s.frc[2,31]-s.m[31]*(C30*(ALPHA227+BETA627*s.dpt[3,28])+S30*(ALPHA326+BS927*s.dpt[3,28])))
  Fs331 = -(s.frc[3,31]-s.m[31]*(ALPHA130*S31+ALPHA330*C31))
  Cq131 = -(s.trq[1,31]-s.In[1,31]*(C31*(OMp130-qd[31]*OM330)-S31*(OMp330+qd[31]*OM130))+OM231*OM331*(s.In[5,31]-\
   s.In[9,31]))
  Cq231 = -(s.trq[2,31]-s.In[5,31]*(qdd[31]+C30*(OMp227+qd[30]*OM327)+S30*(OMp327-qd[30]*OM227))-OM131*OM331*(s.In[1,31]\
   -s.In[9,31]))
  Cq331 = -(s.trq[3,31]-s.In[9,31]*(C31*(OMp330+qd[31]*OM130)+S31*(OMp130-qd[31]*OM330))+OM131*OM231*(s.In[1,31]-\
   s.In[5,31]))
  Fq130 = Fs131*C31+Fs331*S31
  Fq330 = -(Fs131*S31-Fs331*C31)
  Cq130 = Cq131*C31+Cq331*S31
  Cq330 = -(Cq131*S31-Cq331*C31)
  Fs129 = -(s.frc[1,29]-s.m[29]*(ALPHA127+q[29]*(OMp228+OM128*OM328)+(2.0)*qd[29]*OM228+BETA327*s.dpt[3,27]+s.l[3,29]*(OMp228\
   +OM128*OM328)))
  Fs229 = -(s.frc[2,29]+s.m[29]*(q[29]*(OMp128-OM228*OM328)+(2.0)*qd[29]*OM128+s.l[3,29]*(OMp128-OM228*OM328)-C28*(ALPHA227+\
   BETA627*s.dpt[3,27])-S28*(ALPHA326+BS927*s.dpt[3,27])))
  Fs329 = -(s.frc[3,29]-s.m[29]*(qdd[29]-q[29]*(OM128*OM128+OM228*OM228)-s.l[3,29]*(OM128*OM128+OM228*OM228)+C28*(\
   ALPHA326+BS927*s.dpt[3,27])-S28*(ALPHA227+BETA627*s.dpt[3,27])))
  Cq329 = -(s.trq[3,29]-s.In[9,29]*(C28*(OMp327-qd[28]*OM227)-S28*(OMp227+qd[28]*OM327))+OM128*OM228*(s.In[1,29]-\
   s.In[5,29]))
  Cq128 = -(s.trq[1,29]+q[29]*Fs229-s.In[1,29]*OMp128+Fs229*s.l[3,29]+OM228*OM328*(s.In[5,29]-s.In[9,29]))
  Cq228 = -(s.trq[2,29]-q[29]*Fs129-s.In[5,29]*OMp228-Fs129*s.l[3,29]-OM128*OM328*(s.In[1,29]-s.In[9,29]))
  Fs127 = -(s.frc[1,27]-s.m[27]*(ALPHA127+BETA327*s.l[3,27]))
  Fs227 = -(s.frc[2,27]-s.m[27]*(ALPHA227+BETA627*s.l[3,27]))
  Fq127 = Fq130+Fs127+Fs129
  Fq227 = Fs227-Fq330*S30+Fs229*C28+Fs231*C30-Fs329*S28
  Fq327 = -(s.frc[3,27]-s.m[27]*(ALPHA326+BS927*s.l[3,27])-Fq330*C30-Fs229*S28-Fs231*S30-Fs329*C28)
  Cq127 = -(s.trq[1,27]-Cq128-Cq130-s.In[1,27]*OMp127+Fs227*s.l[3,27]+OM227*OM327*(s.In[5,27]-s.In[9,27])+s.dpt[3,27]*(\
   Fs229*C28-Fs329*S28)-s.dpt[3,28]*(Fq330*S30-Fs231*C30))
  Cq227 = -(s.trq[2,27]-s.In[5,27]*OMp227-Cq228*C28-Cq231*C30+Cq329*S28+Cq330*S30-Fq130*s.dpt[3,28]-Fs127*s.l[3,27]-\
   Fs129*s.dpt[3,27]-OM127*OM327*(s.In[1,27]-s.In[9,27]))
  Cq327 = -(s.trq[3,27]-s.In[9,27]*OMp327-Cq228*S28-Cq231*S30-Cq329*C28-Cq330*C30+OM127*OM227*(s.In[1,27]-s.In[5,27]))
  Fq126 = Fq127*C27-Fq227*S27
  Fq226 = Fq127*S27+Fq227*C27
  Cq126 = Cq127*C27-Cq227*S27
  Cq226 = Cq127*S27+Cq227*C27
  Fq125 = Fq126*C26+Fq327*S26
  Fq325 = -(Fq126*S26-Fq327*C26)
  Cq125 = Cq126*C26+Cq327*S26
  Cq325 = -(Cq126*S26-Cq327*C26)
  Fs124 = -(s.frc[1,24]-s.m[24]*(ALPHA124+BETA224*s.l[2,24]))
  Fs324 = -(s.frc[3,24]-s.m[24]*(ALPHA323+BETA824*s.l[2,24]))
  Fq124 = Fq125+Fs124
  Fq224 = -(s.frc[2,24]-s.m[24]*(ALPHA224+BS524*s.l[2,24])-Fq226*C25+Fq325*S25)
  Fq324 = Fs324+Fq226*S25+Fq325*C25
  Cq124 = -(s.trq[1,24]-Cq125-s.In[1,24]*OMp124-s.In[9,24]*OM224*OM324-Fs324*s.l[2,24]-s.dpt[2,26]*(Fq226*S25+Fq325*C25)\
   )
  Cq224 = -(s.trq[2,24]-Cq226*C25+Cq325*S25-OM124*OM324*(s.In[1,24]-s.In[9,24]))
  Cq324 = -(s.trq[3,24]+s.In[1,24]*OM124*OM224-s.In[9,24]*OMp324-Cq226*S25-Cq325*C25+Fq125*s.dpt[2,26]+Fs124*s.l[2,24])
  Fq123 = Fq124*C24-Fq224*S24
  Fq223 = Fq124*S24+Fq224*C24
  Cq123 = Cq124*C24-Cq224*S24
  Cq223 = Cq124*S24+Cq224*C24
  Fs122 = -(s.frc[1,22]-s.m[22]*(ALPHA121*C22-ALPHA321*S22))
  Fs222 = -(s.frc[2,22]-s.m[22]*(C21*(ALPHA217+BETA618*s.dpt[3,22])+S21*(ALPHA318+BS918*s.dpt[3,22])))
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
  Fs120 = -(s.frc[1,20]-s.m[20]*(ALPHA118+q[20]*(OMp219+OM119*OM319)+(2.0)*qd[20]*OM219+BETA318*s.dpt[3,21]+s.l[3,20]*(OMp219\
   +OM119*OM319)))
  Fs220 = -(s.frc[2,20]+s.m[20]*(q[20]*(OMp119-OM219*OM319)+(2.0)*qd[20]*OM119+s.l[3,20]*(OMp119-OM219*OM319)-C19*(ALPHA217+\
   BETA618*s.dpt[3,21])-S19*(ALPHA318+BS918*s.dpt[3,21])))
  Fs320 = -(s.frc[3,20]-s.m[20]*(qdd[20]-q[20]*(OM119*OM119+OM219*OM219)-s.l[3,20]*(OM119*OM119+OM219*OM219)+C19*(\
   ALPHA318+BS918*s.dpt[3,21])-S19*(ALPHA217+BETA618*s.dpt[3,21])))
  Cq320 = -(s.trq[3,20]-s.In[9,20]*(C19*(OMp318-qd[19]*OM218)-S19*(OMp218+qd[19]*OM318))+OM119*OM219*(s.In[1,20]-\
   s.In[5,20]))
  Cq119 = -(s.trq[1,20]+q[20]*Fs220-s.In[1,20]*OMp119+Fs220*s.l[3,20]+OM219*OM319*(s.In[5,20]-s.In[9,20]))
  Cq219 = -(s.trq[2,20]-q[20]*Fs120-s.In[5,20]*OMp219-Fs120*s.l[3,20]-OM119*OM319*(s.In[1,20]-s.In[9,20]))
  Fs118 = -(s.frc[1,18]-s.m[18]*(ALPHA118+BETA318*s.l[3,18]))
  Fs218 = -(s.frc[2,18]-s.m[18]*(ALPHA217+BETA618*s.l[3,18]))
  Fq118 = Fq121+Fs118+Fs120
  Fq218 = Fs218-Fq321*S21+Fs220*C19+Fs222*C21-Fs320*S19
  Fq318 = -(s.frc[3,18]-s.m[18]*(ALPHA318+BS918*s.l[3,18])-Fq321*C21-Fs220*S19-Fs222*S21-Fs320*C19)
  Cq118 = -(s.trq[1,18]-Cq119-Cq121-s.In[1,18]*OMp118+Fs218*s.l[3,18]+OM218*OM318*(s.In[5,18]-s.In[9,18])+s.dpt[3,21]*(\
   Fs220*C19-Fs320*S19)-s.dpt[3,22]*(Fq321*S21-Fs222*C21))
  Cq218 = -(s.trq[2,18]-s.In[5,18]*OMp218-Cq219*C19-Cq222*C21+Cq320*S19+Cq321*S21-Fq121*s.dpt[3,22]-Fs118*s.l[3,18]-\
   Fs120*s.dpt[3,21]-OM118*OM318*(s.In[1,18]-s.In[9,18]))
  Cq318 = -(s.trq[3,18]-s.In[9,18]*OMp318-Cq219*S19-Cq222*S21-Cq320*C19-Cq321*C21+OM118*OM218*(s.In[1,18]-s.In[5,18]))
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
  Cq115 = -(s.trq[1,15]-s.In[1,15]*OMp115-Cq117*C16+Cq216*S16-Fq316*s.dpt[2,20]-Fs315*s.l[2,15])
  Cq215 = -(s.trq[2,15]-s.In[1,15]*OM115*OM315-Cq117*S16-Cq216*C16+Fs315*s.l[1,15])
  Cq315 = -(s.trq[3,15]-Cq316+s.In[1,15]*OM115*OM215+Fs115*s.l[2,15]-Fs215*s.l[1,15]+s.dpt[2,20]*(Fq117*C16-Fq216*S16))
  Fs114 = -(s.frc[1,14]-s.m[14]*(ALPHA113*C14-ALPHA313*S14))
  Fs214 = -(s.frc[2,14]-s.m[14]*(C13*(ALPHA29+BETA610*s.dpt[3,16])+S13*(ALPHA310+BS910*s.dpt[3,16])))
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
  Fs112 = -(s.frc[1,12]-s.m[12]*(ALPHA110+q[12]*(OMp211+OM111*OM311)+(2.0)*qd[12]*OM211+BETA310*s.dpt[3,15]+s.l[3,12]*(OMp211\
   +OM111*OM311)))
  Fs212 = -(s.frc[2,12]+s.m[12]*(q[12]*(OMp111-OM211*OM311)+(2.0)*qd[12]*OM111+s.l[3,12]*(OMp111-OM211*OM311)-C11*(ALPHA29+\
   BETA610*s.dpt[3,15])-S11*(ALPHA310+BS910*s.dpt[3,15])))
  Fs312 = -(s.frc[3,12]-s.m[12]*(qdd[12]-q[12]*(OM111*OM111+OM211*OM211)-s.l[3,12]*(OM111*OM111+OM211*OM211)+C11*(\
   ALPHA310+BS910*s.dpt[3,15])-S11*(ALPHA29+BETA610*s.dpt[3,15])))
  Cq312 = -(s.trq[3,12]-s.In[9,12]*(C11*(OMp310-qd[11]*OM210)-S11*(OMp210+qd[11]*OM310))+OM111*OM211*(s.In[1,12]-\
   s.In[5,12]))
  Cq111 = -(s.trq[1,12]+q[12]*Fs212-s.In[1,12]*OMp111+Fs212*s.l[3,12]+OM211*OM311*(s.In[5,12]-s.In[9,12]))
  Cq211 = -(s.trq[2,12]-q[12]*Fs112-s.In[5,12]*OMp211-Fs112*s.l[3,12]-OM111*OM311*(s.In[1,12]-s.In[9,12]))
  Fs110 = -(s.frc[1,10]-s.m[10]*(ALPHA110+BETA310*s.l[3,10]))
  Fs210 = -(s.frc[2,10]-s.m[10]*(ALPHA29+BETA610*s.l[3,10]))
  Fq110 = Fq113+Fs110+Fs112
  Fq210 = Fs210-Fq313*S13+Fs212*C11+Fs214*C13-Fs312*S11
  Fq310 = -(s.frc[3,10]-s.m[10]*(ALPHA310+BS910*s.l[3,10])-Fq313*C13-Fs212*S11-Fs214*S13-Fs312*C11)
  Cq110 = -(s.trq[1,10]-Cq111-Cq113-s.In[1,10]*OMp110+Fs210*s.l[3,10]+OM210*OM310*(s.In[5,10]-s.In[9,10])+s.dpt[3,15]*(\
   Fs212*C11-Fs312*S11)-s.dpt[3,16]*(Fq313*S13-Fs214*C13))
  Cq210 = -(s.trq[2,10]-s.In[5,10]*OMp210-Cq211*C11-Cq214*C13+Cq312*S11+Cq313*S13-Fq113*s.dpt[3,16]-Fs110*s.l[3,10]-\
   Fs112*s.dpt[3,15]-OM110*OM310*(s.In[1,10]-s.In[9,10]))
  Cq310 = -(s.trq[3,10]-s.In[9,10]*OMp310-Cq211*S11-Cq214*S13-Cq312*C11-Cq313*C13+OM110*OM210*(s.In[1,10]-s.In[5,10]))
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
  Cq17 = -(s.trq[1,7]-s.In[1,7]*OMp17-Cq19*C8+Cq28*S8-Fq38*s.dpt[2,14]-Fs37*s.l[2,7])
  Cq27 = -(s.trq[2,7]-s.In[1,7]*OM17*OM37-Cq19*S8-Cq28*C8+Fs37*s.l[1,7])
  Cq37 = -(s.trq[3,7]-Cq38+s.In[1,7]*OM17*OM27+Fs17*s.l[2,7]-Fs27*s.l[1,7]+s.dpt[2,14]*(Fq19*C8-Fq28*S8))
  Fs16 = -(s.frc[1,6]-s.m[6]*(ALPHA15+s.l[3,6]*(BS36+OMp26)))
  Fs26 = -(s.frc[2,6]-s.m[6]*(ALPHA26+s.l[3,6]*(BS66-OMp16)))
  Fq16 = Fq115+Fq123+Fq132+Fq17+Fs141+Fs16
  Fq26 = Fs241+Fs26+Fq215*C15+Fq223*C23+Fq232*C32+Fq27*C7-Fq315*S15-Fq324*S23-Fq333*S32-Fq37*S7
  Fq36 = -(s.frc[3,6]-Fs341-s.m[6]*(ALPHA36-s.l[3,6]*(OM16*OM16+OM26*OM26))-Fq215*S15-Fq223*S23-Fq232*S32-Fq27*S7-Fq315*\
   C15-Fq324*C23-Fq333*C32-Fq37*C7)
  Cq16 = -(s.trq[1,41]+s.trq[1,6]-Cq115-Cq123-Cq132-Cq17-q[41]*Fs341-s.In[1,6]*OMp16+Fs26*s.l[3,6]+OM26*OM36*(s.In[5,6]-\
   s.In[9,6])-s.dpt[2,10]*(Fq223*S23+Fq324*C23)-s.dpt[2,12]*(Fq232*S32+Fq333*C32)-s.dpt[2,1]*(Fq27*S7+Fq37*C7)-s.dpt[2,4]*(\
   Fq215*S15+Fq315*C15))
  Cq26 = -(s.trq[2,41]+s.trq[2,6]-s.In[5,6]*OMp26-Cq215*C15-Cq223*C23-Cq232*C32-Cq27*C7+Cq315*S15+Cq324*S23+Cq333*S32+\
   Cq37*S7-Fs16*s.l[3,6]+Fs341*s.dpt[1,13]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,10]*(Fq223*S23+Fq324*C23)+s.dpt[1,12]*(Fq232\
   *S32+Fq333*C32)+s.dpt[1,1]*(Fq27*S7+Fq37*C7)+s.dpt[1,4]*(Fq215*S15+Fq315*C15))
  Cq36 = -(s.trq[3,41]+s.trq[3,6]+q[41]*Fs141-s.In[9,6]*OMp36-Cq215*S15-Cq223*S23-Cq232*S32-Cq27*S7-Cq315*C15-Cq324*C23-\
   Cq333*C32-Cq37*C7+Fq115*s.dpt[2,4]+Fq123*s.dpt[2,10]+Fq132*s.dpt[2,12]+Fq17*s.dpt[2,1]-Fs241*s.dpt[1,13]+OM16*OM26*(\
   s.In[1,6]-s.In[5,6])-s.dpt[1,10]*(Fq223*C23-Fq324*S23)-s.dpt[1,12]*(Fq232*C32-Fq333*S32)-s.dpt[1,1]*(Fq27*C7-Fq37*S7)-\
   s.dpt[1,4]*(Fq215*C15-Fq315*S15))
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
  Qq[26] = Cq226
  Qq[27] = Cq327
  Qq[28] = Cq128
  Qq[29] = Fs329
  Qq[30] = Cq130
  Qq[31] = Cq231
  Qq[32] = Cq132
  Qq[33] = Cq333
  Qq[34] = Cq134
  Qq[35] = Cq235
  Qq[36] = Cq336
  Qq[37] = Cq137
  Qq[38] = Fs338
  Qq[39] = Cq139
  Qq[40] = Cq240
  Qq[41] = Fs241

# ====== END Task 0 ====== 

  

