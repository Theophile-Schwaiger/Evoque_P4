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
#	==> Function : F 2 : Inverse Dynamics : RNEA
#	==> Flops complexity : 1405
#
#	==> Generation Time :  0.020 seconds
#	==> Post-Processing :  0.010 seconds
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

# = = Block_0_1_0_0_0_0 = = 
 
# Forward Kinematics 

  ALPHA33 = qdd[3]-s.g[3]
  ALPHA14 = qdd[1]*C4+qdd[2]*S4
  ALPHA24 = -(qdd[1]*S4-qdd[2]*C4)
  OM35 = qd[4]*C5
  OMp35 = -(qd[4]*qd[5]*S5-qdd[4]*C5)
  ALPHA25 = ALPHA24*C5+ALPHA33*S5
  ALPHA35 = -(ALPHA24*S5-ALPHA33*C5)
  OM16 = qd[5]*C6-OM35*S6
  OM26 = qd[6]+qd[4]*S5
  OM36 = qd[5]*S6+OM35*C6
  OMp16 = C6*(qdd[5]-qd[6]*OM35)-S6*(OMp35+qd[5]*qd[6])
  OMp26 = qdd[6]+qd[4]*qd[5]*C5+qdd[4]*S5
  OMp36 = C6*(OMp35+qd[5]*qd[6])+S6*(qdd[5]-qd[6]*OM35)
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
  ALPHA16 = ALPHA14*C6-ALPHA35*S6
  ALPHA36 = ALPHA14*S6+ALPHA35*C6
  OM17 = qd[7]+OM16
  OM27 = OM26*C7+OM36*S7
  OM37 = -(OM26*S7-OM36*C7)
  OMp17 = qdd[7]+OMp16
  OMp27 = C7*(OMp26+qd[7]*OM36)+S7*(OMp36-qd[7]*OM26)
  OMp37 = C7*(OMp36-qd[7]*OM26)-S7*(OMp26+qd[7]*OM36)
  BS57 = -(OM17*OM17+OM37*OM37)
  BETA27 = OM17*OM27-OMp37
  BETA87 = OMp17+OM27*OM37
  ALPHA17 = ALPHA16+BETA26*s.dpt[2,1]+BETA36*s.dpt[3,1]+BS16*s.dpt[1,1]
  ALPHA27 = C7*(ALPHA25+BETA46*s.dpt[1,1]+BETA66*s.dpt[3,1]+BS56*s.dpt[2,1])+S7*(ALPHA36+BETA76*s.dpt[1,1]+BETA86*\
   s.dpt[2,1]+BS96*s.dpt[3,1])
  ALPHA37 = C7*(ALPHA36+BETA76*s.dpt[1,1]+BETA86*s.dpt[2,1]+BS96*s.dpt[3,1])-S7*(ALPHA25+BETA46*s.dpt[1,1]+BETA66*\
   s.dpt[3,1]+BS56*s.dpt[2,1])
  OM18 = OM17*C8+OM27*S8
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OMp18 = C8*(OMp17+qd[8]*OM27)+S8*(OMp27-qd[8]*OM17)
  ALPHA18 = C8*(ALPHA17+BETA27*s.dpt[2,14])+S8*(ALPHA27+BS57*s.dpt[2,14])
  ALPHA28 = C8*(ALPHA27+BS57*s.dpt[2,14])-S8*(ALPHA17+BETA27*s.dpt[2,14])
  ALPHA38 = ALPHA37+BETA87*s.dpt[2,14]
  OM19 = qd[9]+OM18
  OM110 = qd[10]+OM16
  OM210 = OM26*C10+OM36*S10
  OM310 = -(OM26*S10-OM36*C10)
  OMp110 = qdd[10]+OMp16
  OMp210 = C10*(OMp26+qd[10]*OM36)+S10*(OMp36-qd[10]*OM26)
  OMp310 = C10*(OMp36-qd[10]*OM26)-S10*(OMp26+qd[10]*OM36)
  BS510 = -(OM110*OM110+OM310*OM310)
  BETA210 = OM110*OM210-OMp310
  BETA810 = OMp110+OM210*OM310
  ALPHA110 = ALPHA16+BETA26*s.dpt[2,4]+BETA36*s.dpt[3,4]+BS16*s.dpt[1,4]
  ALPHA210 = C10*(ALPHA25+BETA46*s.dpt[1,4]+BETA66*s.dpt[3,4]+BS56*s.dpt[2,4])+S10*(ALPHA36+BETA76*s.dpt[1,4]+BETA86*\
   s.dpt[2,4]+BS96*s.dpt[3,4])
  ALPHA310 = C10*(ALPHA36+BETA76*s.dpt[1,4]+BETA86*s.dpt[2,4]+BS96*s.dpt[3,4])-S10*(ALPHA25+BETA46*s.dpt[1,4]+BETA66*\
   s.dpt[3,4]+BS56*s.dpt[2,4])
  OM111 = OM110*C11+OM210*S11
  OM211 = -(OM110*S11-OM210*C11)
  OM311 = qd[11]+OM310
  OMp111 = C11*(OMp110+qd[11]*OM210)+S11*(OMp210-qd[11]*OM110)
  ALPHA111 = C11*(ALPHA110+BETA210*s.dpt[2,19])+S11*(ALPHA210+BS510*s.dpt[2,19])
  ALPHA211 = C11*(ALPHA210+BS510*s.dpt[2,19])-S11*(ALPHA110+BETA210*s.dpt[2,19])
  ALPHA311 = ALPHA310+BETA810*s.dpt[2,19]
  OM112 = qd[12]+OM111
  OM113 = qd[13]+OM16
  OM213 = OM26*C13+OM36*S13
  OM313 = -(OM26*S13-OM36*C13)
  OMp113 = qdd[13]+OMp16
  OMp213 = C13*(OMp26+qd[13]*OM36)+S13*(OMp36-qd[13]*OM26)
  OMp313 = C13*(OMp36-qd[13]*OM26)-S13*(OMp26+qd[13]*OM36)
  BS513 = -(OM113*OM113+OM313*OM313)
  BETA213 = OM113*OM213-OMp313
  BETA813 = OMp113+OM213*OM313
  ALPHA113 = ALPHA16+BETA26*s.dpt[2,9]+BETA36*s.dpt[3,9]+BS16*s.dpt[1,9]
  ALPHA213 = C13*(ALPHA25+BETA46*s.dpt[1,9]+BETA66*s.dpt[3,9]+BS56*s.dpt[2,9])+S13*(ALPHA36+BETA76*s.dpt[1,9]+BETA86*\
   s.dpt[2,9]+BS96*s.dpt[3,9])
  ALPHA313 = C13*(ALPHA36+BETA76*s.dpt[1,9]+BETA86*s.dpt[2,9]+BS96*s.dpt[3,9])-S13*(ALPHA25+BETA46*s.dpt[1,9]+BETA66*\
   s.dpt[3,9]+BS56*s.dpt[2,9])
  OM114 = qd[14]+OM113
  OM214 = OM213*C14+OM313*S14
  OM314 = -(OM213*S14-OM313*C14)
  OMp114 = qdd[14]+OMp113
  BS114 = -(OM214*OM214+OM314*OM314)
  BETA414 = OM114*OM214+C14*(OMp313-qd[14]*OM213)-S14*(OMp213+qd[14]*OM313)
  BETA714 = OM114*OM314-C14*(OMp213+qd[14]*OM313)-S14*(OMp313-qd[14]*OM213)
  ALPHA114 = ALPHA113+BETA213*s.dpt[2,24]
  ALPHA214 = C14*(ALPHA213+BS513*s.dpt[2,24])+S14*(ALPHA313+BETA813*s.dpt[2,24])
  ALPHA314 = C14*(ALPHA313+BETA813*s.dpt[2,24])-S14*(ALPHA213+BS513*s.dpt[2,24])
  OM115 = qd[15]+OM114
  OM116 = qd[16]+OM16
  OM216 = OM26*C16+OM36*S16
  OM316 = -(OM26*S16-OM36*C16)
  OMp116 = qdd[16]+OMp16
  OMp216 = C16*(OMp26+qd[16]*OM36)+S16*(OMp36-qd[16]*OM26)
  OMp316 = C16*(OMp36-qd[16]*OM26)-S16*(OMp26+qd[16]*OM36)
  BS516 = -(OM116*OM116+OM316*OM316)
  BETA216 = OM116*OM216-OMp316
  BETA816 = OMp116+OM216*OM316
  ALPHA116 = ALPHA16+BETA26*s.dpt[2,11]+BETA36*s.dpt[3,11]+BS16*s.dpt[1,11]
  ALPHA216 = C16*(ALPHA25+BETA46*s.dpt[1,11]+BETA66*s.dpt[3,11]+BS56*s.dpt[2,11])+S16*(ALPHA36+BETA76*s.dpt[1,11]+BETA86\
   *s.dpt[2,11]+BS96*s.dpt[3,11])
  ALPHA316 = C16*(ALPHA36+BETA76*s.dpt[1,11]+BETA86*s.dpt[2,11]+BS96*s.dpt[3,11])-S16*(ALPHA25+BETA46*s.dpt[1,11]+BETA66\
   *s.dpt[3,11]+BS56*s.dpt[2,11])
  OM117 = qd[17]+OM116
  OM217 = OM216*C17+OM316*S17
  OM317 = -(OM216*S17-OM316*C17)
  OMp117 = qdd[17]+OMp116
  BS117 = -(OM217*OM217+OM317*OM317)
  BETA417 = OM117*OM217+C17*(OMp316-qd[17]*OM216)-S17*(OMp216+qd[17]*OM316)
  BETA717 = OM117*OM317-C17*(OMp216+qd[17]*OM316)-S17*(OMp316-qd[17]*OM216)
  ALPHA117 = ALPHA116+BETA216*s.dpt[2,30]
  ALPHA217 = C17*(ALPHA216+BS516*s.dpt[2,30])+S17*(ALPHA316+BETA816*s.dpt[2,30])
  ALPHA317 = C17*(ALPHA316+BETA816*s.dpt[2,30])-S17*(ALPHA216+BS516*s.dpt[2,30])
  OM118 = qd[18]+OM117
 
# Backward Dynamics 

  Fs218 = -(s.frc[2,18]-s.m[18]*(C18*(ALPHA217+BETA417*s.dpt[1,34])+S18*(ALPHA317+BETA717*s.dpt[1,34])))
  Fs318 = -(s.frc[3,18]-s.m[18]*(C18*(ALPHA317+BETA717*s.dpt[1,34])-S18*(ALPHA217+BETA417*s.dpt[1,34])))
  Cq118 = -(s.trq[1,18]-s.In[1,18]*(qdd[18]+OMp117))
  Cq218 = -(s.trq[2,18]+s.In[1,18]*OM118*(OM217*S18-OM317*C18))
  Cq318 = -(s.trq[3,18]+s.In[1,18]*OM118*(OM217*C18+OM317*S18))
  Fs217 = -(s.frc[2,17]-s.m[17]*(ALPHA217+BETA417*s.l[1,17]))
  Fs317 = -(s.frc[3,17]-s.m[17]*(ALPHA317+BETA717*s.l[1,17]))
  Fq117 = -(s.frc[1,17]+s.frc[1,18]-s.m[17]*(ALPHA117+BS117*s.l[1,17])-s.m[18]*(ALPHA117+BS117*s.dpt[1,34]))
  Fq217 = Fs217+Fs218*C18-Fs318*S18
  Fq317 = Fs317+Fs218*S18+Fs318*C18
  Cq117 = -(s.trq[1,17]-Cq118-s.In[1,17]*OMp117)
  Cq217 = -(s.trq[2,17]-s.In[1,17]*OM117*OM317-Cq218*C18+Cq318*S18+Fs317*s.l[1,17]+s.dpt[1,34]*(Fs218*S18+Fs318*C18))
  Cq317 = -(s.trq[3,17]+s.In[1,17]*OM117*OM217-Cq218*S18-Cq318*C18-Fs217*s.l[1,17]-s.dpt[1,34]*(Fs218*C18-Fs318*S18))
  Fs116 = -(s.frc[1,16]-s.m[16]*(ALPHA116+BETA216*s.l[2,16]))
  Fs316 = -(s.frc[3,16]-s.m[16]*(ALPHA316+BETA816*s.l[2,16]))
  Fq116 = Fq117+Fs116
  Fq216 = -(s.frc[2,16]-s.m[16]*(ALPHA216+BS516*s.l[2,16])-Fq217*C17+Fq317*S17)
  Fq316 = Fs316+Fq217*S17+Fq317*C17
  Cq116 = -(s.trq[1,16]-Cq117-s.In[1,16]*OMp116-s.In[9,16]*OM216*OM316-Fs316*s.l[2,16]-s.dpt[2,30]*(Fq217*S17+Fq317*C17)\
   )
  Cq216 = -(s.trq[2,16]-Cq217*C17+Cq317*S17-OM116*OM316*(s.In[1,16]-s.In[9,16]))
  Cq316 = -(s.trq[3,16]+s.In[1,16]*OM116*OM216-s.In[9,16]*OMp316-Cq217*S17-Cq317*C17+Fq117*s.dpt[2,30]+Fs116*s.l[2,16])
  Fs215 = -(s.frc[2,15]-s.m[15]*(C15*(ALPHA214+BETA414*s.dpt[1,26])+S15*(ALPHA314+BETA714*s.dpt[1,26])))
  Fs315 = -(s.frc[3,15]-s.m[15]*(C15*(ALPHA314+BETA714*s.dpt[1,26])-S15*(ALPHA214+BETA414*s.dpt[1,26])))
  Cq115 = -(s.trq[1,15]-s.In[1,15]*(qdd[15]+OMp114))
  Cq215 = -(s.trq[2,15]+s.In[1,15]*OM115*(OM214*S15-OM314*C15))
  Cq315 = -(s.trq[3,15]+s.In[1,15]*OM115*(OM214*C15+OM314*S15))
  Fs214 = -(s.frc[2,14]-s.m[14]*(ALPHA214+BETA414*s.l[1,14]))
  Fs314 = -(s.frc[3,14]-s.m[14]*(ALPHA314+BETA714*s.l[1,14]))
  Fq114 = -(s.frc[1,14]+s.frc[1,15]-s.m[14]*(ALPHA114+BS114*s.l[1,14])-s.m[15]*(ALPHA114+BS114*s.dpt[1,26]))
  Fq214 = Fs214+Fs215*C15-Fs315*S15
  Fq314 = Fs314+Fs215*S15+Fs315*C15
  Cq114 = -(s.trq[1,14]-Cq115-s.In[1,14]*OMp114)
  Cq214 = -(s.trq[2,14]-s.In[1,14]*OM114*OM314-Cq215*C15+Cq315*S15+Fs314*s.l[1,14]+s.dpt[1,26]*(Fs215*S15+Fs315*C15))
  Cq314 = -(s.trq[3,14]+s.In[1,14]*OM114*OM214-Cq215*S15-Cq315*C15-Fs214*s.l[1,14]-s.dpt[1,26]*(Fs215*C15-Fs315*S15))
  Fs113 = -(s.frc[1,13]-s.m[13]*(ALPHA113+BETA213*s.l[2,13]))
  Fs313 = -(s.frc[3,13]-s.m[13]*(ALPHA313+BETA813*s.l[2,13]))
  Fq113 = Fq114+Fs113
  Fq213 = -(s.frc[2,13]-s.m[13]*(ALPHA213+BS513*s.l[2,13])-Fq214*C14+Fq314*S14)
  Fq313 = Fs313+Fq214*S14+Fq314*C14
  Cq113 = -(s.trq[1,13]-Cq114-s.In[1,13]*OMp113-s.In[9,13]*OM213*OM313-Fs313*s.l[2,13]-s.dpt[2,24]*(Fq214*S14+Fq314*C14)\
   )
  Cq213 = -(s.trq[2,13]-Cq214*C14+Cq314*S14-OM113*OM313*(s.In[1,13]-s.In[9,13]))
  Cq313 = -(s.trq[3,13]+s.In[1,13]*OM113*OM213-s.In[9,13]*OMp313-Cq214*S14-Cq314*C14+Fq114*s.dpt[2,24]+Fs113*s.l[2,13])
  Fs212 = -(s.frc[2,12]-s.m[12]*(ALPHA211*C12+ALPHA311*S12))
  Fs312 = -(s.frc[3,12]+s.m[12]*(ALPHA211*S12-ALPHA311*C12))
  Cq112 = -(s.trq[1,12]-s.In[1,12]*(qdd[12]+OMp111))
  Cq212 = -(s.trq[2,12]+s.In[1,12]*OM112*(OM211*S12-OM311*C12))
  Cq312 = -(s.trq[3,12]+s.In[1,12]*OM112*(OM211*C12+OM311*S12))
  Fs111 = -(s.frc[1,11]-s.m[11]*(ALPHA111+s.l[3,11]*(OM111*OM311+C11*(OMp210-qd[11]*OM110)-S11*(OMp110+qd[11]*OM210))))
  Fs211 = -(s.frc[2,11]-s.m[11]*(ALPHA211-s.l[3,11]*(OMp111-OM211*OM311)))
  Fq111 = -(s.frc[1,12]-Fs111-s.m[12]*ALPHA111)
  Fq211 = Fs211+Fs212*C12-Fs312*S12
  Fq311 = -(s.frc[3,11]-s.m[11]*(ALPHA311-s.l[3,11]*(OM111*OM111+OM211*OM211))-Fs212*S12-Fs312*C12)
  Cq111 = -(s.trq[1,11]-Cq112-s.In[1,11]*OMp111-s.In[9,11]*OM211*OM311+Fs211*s.l[3,11])
  Cq211 = -(s.trq[2,11]-Cq212*C12+Cq312*S12-Fs111*s.l[3,11]-OM111*OM311*(s.In[1,11]-s.In[9,11]))
  Cq311 = -(s.trq[3,11]+s.In[1,11]*OM111*OM211-s.In[9,11]*(qdd[11]+OMp310)-Cq212*S12-Cq312*C12)
  Fs110 = -(s.frc[1,10]-s.m[10]*(ALPHA110+BETA210*s.l[2,10]))
  Fs310 = -(s.frc[3,10]-s.m[10]*(ALPHA310+BETA810*s.l[2,10]))
  Fq110 = Fs110+Fq111*C11-Fq211*S11
  Fq210 = -(s.frc[2,10]-s.m[10]*(ALPHA210+BS510*s.l[2,10])-Fq111*S11-Fq211*C11)
  Fq310 = Fq311+Fs310
  Cq110 = -(s.trq[1,10]-s.In[1,10]*OMp110-Cq111*C11+Cq211*S11-Fq311*s.dpt[2,19]-Fs310*s.l[2,10])
  Cq210 = -(s.trq[2,10]-s.In[1,10]*OM110*OM310-Cq111*S11-Cq211*C11)
  Cq310 = -(s.trq[3,10]-Cq311+s.In[1,10]*OM110*OM210+Fs110*s.l[2,10]+s.dpt[2,19]*(Fq111*C11-Fq211*S11))
  Fs29 = -(s.frc[2,9]-s.m[9]*(ALPHA28*C9+ALPHA38*S9))
  Fs39 = -(s.frc[3,9]+s.m[9]*(ALPHA28*S9-ALPHA38*C9))
  Cq19 = -(s.trq[1,9]-s.In[1,9]*(qdd[9]+OMp18))
  Cq29 = -(s.trq[2,9]+s.In[1,9]*OM19*(OM28*S9-OM38*C9))
  Cq39 = -(s.trq[3,9]+s.In[1,9]*OM19*(OM28*C9+OM38*S9))
  Fs18 = -(s.frc[1,8]-s.m[8]*(ALPHA18+s.l[3,8]*(OM18*OM38+C8*(OMp27-qd[8]*OM17)-S8*(OMp17+qd[8]*OM27))))
  Fs28 = -(s.frc[2,8]-s.m[8]*(ALPHA28-s.l[3,8]*(OMp18-OM28*OM38)))
  Fq18 = -(s.frc[1,9]-Fs18-s.m[9]*ALPHA18)
  Fq28 = Fs28+Fs29*C9-Fs39*S9
  Fq38 = -(s.frc[3,8]-s.m[8]*(ALPHA38-s.l[3,8]*(OM18*OM18+OM28*OM28))-Fs29*S9-Fs39*C9)
  Cq18 = -(s.trq[1,8]-Cq19-s.In[1,8]*OMp18-s.In[9,8]*OM28*OM38+Fs28*s.l[3,8])
  Cq28 = -(s.trq[2,8]-Cq29*C9+Cq39*S9-Fs18*s.l[3,8]-OM18*OM38*(s.In[1,8]-s.In[9,8]))
  Cq38 = -(s.trq[3,8]+s.In[1,8]*OM18*OM28-s.In[9,8]*(qdd[8]+OMp37)-Cq29*S9-Cq39*C9)
  Fs17 = -(s.frc[1,7]-s.m[7]*(ALPHA17+BETA27*s.l[2,7]))
  Fs37 = -(s.frc[3,7]-s.m[7]*(ALPHA37+BETA87*s.l[2,7]))
  Fq17 = Fs17+Fq18*C8-Fq28*S8
  Fq27 = -(s.frc[2,7]-s.m[7]*(ALPHA27+BS57*s.l[2,7])-Fq18*S8-Fq28*C8)
  Fq37 = Fq38+Fs37
  Cq17 = -(s.trq[1,7]-s.In[1,7]*OMp17-Cq18*C8+Cq28*S8-Fq38*s.dpt[2,14]-Fs37*s.l[2,7])
  Cq27 = -(s.trq[2,7]-s.In[1,7]*OM17*OM37-Cq18*S8-Cq28*C8)
  Cq37 = -(s.trq[3,7]-Cq38+s.In[1,7]*OM17*OM27+Fs17*s.l[2,7]+s.dpt[2,14]*(Fq18*C8-Fq28*S8))
  Fs16 = -(s.frc[1,6]-s.m[6]*(ALPHA16+BETA36*s.l[3,6]))
  Fs26 = -(s.frc[2,6]-s.m[6]*(ALPHA25+BETA66*s.l[3,6]))
  Fq16 = Fq110+Fq113+Fq116+Fq17+Fs16
  Fq26 = Fs26+Fq210*C10+Fq213*C13+Fq216*C16+Fq27*C7-Fq310*S10-Fq313*S13-Fq316*S16-Fq37*S7
  Fq36 = -(s.frc[3,6]-s.m[6]*(ALPHA36+BS96*s.l[3,6])-Fq210*S10-Fq213*S13-Fq216*S16-Fq27*S7-Fq310*C10-Fq313*C13-Fq316*C16\
   -Fq37*C7)
  Cq16 = -(s.trq[1,6]-Cq110-Cq113-Cq116-Cq17-s.In[1,6]*OMp16+Fs26*s.l[3,6]+OM26*OM36*(s.In[5,6]-s.In[9,6])-s.dpt[2,11]*(\
   Fq216*S16+Fq316*C16)-s.dpt[2,1]*(Fq27*S7+Fq37*C7)-s.dpt[2,4]*(Fq210*S10+Fq310*C10)-s.dpt[2,9]*(Fq213*S13+Fq313*C13)+\
   s.dpt[3,11]*(Fq216*C16-Fq316*S16)+s.dpt[3,1]*(Fq27*C7-Fq37*S7)+s.dpt[3,4]*(Fq210*C10-Fq310*S10)+s.dpt[3,9]*(Fq213*C13-Fq313*\
   S13))
  Cq26 = -(s.trq[2,6]-s.In[5,6]*OMp26-Cq210*C10-Cq213*C13-Cq216*C16-Cq27*C7+Cq310*S10+Cq313*S13+Cq316*S16+Cq37*S7-Fq110*\
   s.dpt[3,4]-Fq113*s.dpt[3,9]-Fq116*s.dpt[3,11]-Fq17*s.dpt[3,1]-Fs16*s.l[3,6]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,11]*(\
   Fq216*S16+Fq316*C16)+s.dpt[1,1]*(Fq27*S7+Fq37*C7)+s.dpt[1,4]*(Fq210*S10+Fq310*C10)+s.dpt[1,9]*(Fq213*S13+Fq313*C13))
  Cq36 = -(s.trq[3,6]-s.In[9,6]*OMp36-Cq210*S10-Cq213*S13-Cq216*S16-Cq27*S7-Cq310*C10-Cq313*C13-Cq316*C16-Cq37*C7+Fq110*\
   s.dpt[2,4]+Fq113*s.dpt[2,9]+Fq116*s.dpt[2,11]+Fq17*s.dpt[2,1]+OM16*OM26*(s.In[1,6]-s.In[5,6])-s.dpt[1,11]*(Fq216*C16-Fq316*\
   S16)-s.dpt[1,1]*(Fq27*C7-Fq37*S7)-s.dpt[1,4]*(Fq210*C10-Fq310*S10)-s.dpt[1,9]*(Fq213*C13-Fq313*S13))
  Fq15 = Fq16*C6+Fq36*S6
  Fq35 = -(Fq16*S6-Fq36*C6)
  Cq15 = Cq16*C6+Cq36*S6
  Fq24 = Fq26*C5-Fq35*S5
  Fq34 = Fq26*S5+Fq35*C5
  Cq34 = Cq26*S5-C5*(Cq16*S6-Cq36*C6)
  Fq13 = Fq15*C4-Fq24*S4
  Fq23 = Fq15*S4+Fq24*C4

# = = Block_0_2_0_0_0_0 = = 
 
# Symbolic Outputs  

  Qq[1] = Fq13
  Qq[2] = Fq23
  Qq[3] = Fq34
  Qq[4] = Cq34
  Qq[5] = Cq15
  Qq[6] = Cq26
  Qq[7] = Cq17
  Qq[8] = Cq38
  Qq[9] = Cq19
  Qq[10] = Cq110
  Qq[11] = Cq311
  Qq[12] = Cq112
  Qq[13] = Cq113
  Qq[14] = Cq114
  Qq[15] = Cq115
  Qq[16] = Cq116
  Qq[17] = Cq117
  Qq[18] = Cq118

# ====== END Task 0 ====== 

  

