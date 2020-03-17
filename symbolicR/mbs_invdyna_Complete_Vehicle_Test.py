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
#	==> Function : F 2 : Inverse Dynamics : RNEA
#	==> Flops complexity : 1585
#
#	==> Generation Time :  0.020 seconds
#	==> Post-Processing :  0.020 seconds
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
  C12 = np.cos(q[12])
  S12 = np.sin(q[12])
  C13 = np.cos(q[13])
  S13 = np.sin(q[13])
  C14 = np.cos(q[14])
  S14 = np.sin(q[14])

# = = Block_0_0_0_0_0_4 = = 
 
# Trigonometric Variables  

  C15 = np.cos(q[15])
  S15 = np.sin(q[15])
  C16 = np.cos(q[16])
  S16 = np.sin(q[16])
  C17 = np.cos(q[17])
  S17 = np.sin(q[17])
  C18 = np.cos(q[18])
  S18 = np.sin(q[18])

# = = Block_0_0_0_0_0_5 = = 
 
# Trigonometric Variables  

  C19 = np.cos(q[19])
  S19 = np.sin(q[19])
  C20 = np.cos(q[20])
  S20 = np.sin(q[20])
  C21 = np.cos(q[21])
  S21 = np.sin(q[21])
  C22 = np.cos(q[22])
  S22 = np.sin(q[22])

# = = Block_0_1_0_0_0_0 = = 
 
# Forward Kinematics 

  ALPHA33 = qdd[3]-s.g[3]
  ALPHA24 = qdd[2]*C4+ALPHA33*S4
  ALPHA34 = -(qdd[2]*S4-ALPHA33*C4)
  OM15 = qd[4]*C5
  OMp15 = -(qd[4]*qd[5]*S5-qdd[4]*C5)
  ALPHA15 = qdd[1]*C5-ALPHA34*S5
  ALPHA35 = qdd[1]*S5+ALPHA34*C5
  OM16 = qd[5]*S6+OM15*C6
  OM26 = qd[5]*C6-OM15*S6
  OM36 = qd[6]+qd[4]*S5
  OMp16 = C6*(OMp15+qd[5]*qd[6])+S6*(qdd[5]-qd[6]*OM15)
  OMp26 = C6*(qdd[5]-qd[6]*OM15)-S6*(OMp15+qd[5]*qd[6])
  OMp36 = qdd[6]+qd[4]*qd[5]*C5+qdd[4]*S5
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
  ALPHA16 = ALPHA15*C6+ALPHA24*S6
  ALPHA26 = -(ALPHA15*S6-ALPHA24*C6)
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
  ALPHA27 = C7*(ALPHA26+BETA46*s.dpt[1,1]+BETA66*s.dpt[3,1]+BS56*s.dpt[2,1])+S7*(ALPHA35+BETA76*s.dpt[1,1]+BETA86*\
   s.dpt[2,1]+BS96*s.dpt[3,1])
  ALPHA37 = C7*(ALPHA35+BETA76*s.dpt[1,1]+BETA86*s.dpt[2,1]+BS96*s.dpt[3,1])-S7*(ALPHA26+BETA46*s.dpt[1,1]+BETA66*\
   s.dpt[3,1]+BS56*s.dpt[2,1])
  OM18 = OM17*C8+OM27*S8
  OM28 = -(OM17*S8-OM27*C8)
  OM38 = qd[8]+OM37
  OMp18 = C8*(OMp17+qd[8]*OM27)+S8*(OMp27-qd[8]*OM17)
  OMp28 = C8*(OMp27-qd[8]*OM17)-S8*(OMp17+qd[8]*OM27)
  OMp38 = qdd[8]+OMp37
  ALPHA18 = C8*(ALPHA17+BETA27*s.dpt[2,13])+S8*(ALPHA27+BS57*s.dpt[2,13])
  ALPHA28 = C8*(ALPHA27+BS57*s.dpt[2,13])-S8*(ALPHA17+BETA27*s.dpt[2,13])
  ALPHA38 = ALPHA37+BETA87*s.dpt[2,13]
  OM19 = qd[9]+OM18
  OM39 = -(OM28*S9-OM38*C9)
  ALPHA39 = -(ALPHA28*S9-ALPHA38*C9)
  OM110 = OM19*C10-OM39*S10
  OM111 = qd[11]+OM16
  OM211 = OM26*C11+OM36*S11
  OM311 = -(OM26*S11-OM36*C11)
  OMp111 = qdd[11]+OMp16
  OMp211 = C11*(OMp26+qd[11]*OM36)+S11*(OMp36-qd[11]*OM26)
  OMp311 = C11*(OMp36-qd[11]*OM26)-S11*(OMp26+qd[11]*OM36)
  BS511 = -(OM111*OM111+OM311*OM311)
  BETA211 = OM111*OM211-OMp311
  BETA811 = OMp111+OM211*OM311
  ALPHA111 = ALPHA16+BETA26*s.dpt[2,4]+BETA36*s.dpt[3,4]+BS16*s.dpt[1,4]
  ALPHA211 = C11*(ALPHA26+BETA46*s.dpt[1,4]+BETA66*s.dpt[3,4]+BS56*s.dpt[2,4])+S11*(ALPHA35+BETA76*s.dpt[1,4]+BETA86*\
   s.dpt[2,4]+BS96*s.dpt[3,4])
  ALPHA311 = C11*(ALPHA35+BETA76*s.dpt[1,4]+BETA86*s.dpt[2,4]+BS96*s.dpt[3,4])-S11*(ALPHA26+BETA46*s.dpt[1,4]+BETA66*\
   s.dpt[3,4]+BS56*s.dpt[2,4])
  OM112 = OM111*C12+OM211*S12
  OM212 = -(OM111*S12-OM211*C12)
  OM312 = qd[12]+OM311
  OMp112 = C12*(OMp111+qd[12]*OM211)+S12*(OMp211-qd[12]*OM111)
  OMp212 = C12*(OMp211-qd[12]*OM111)-S12*(OMp111+qd[12]*OM211)
  OMp312 = qdd[12]+OMp311
  ALPHA112 = C12*(ALPHA111+BETA211*s.dpt[2,17])+S12*(ALPHA211+BS511*s.dpt[2,17])
  ALPHA212 = C12*(ALPHA211+BS511*s.dpt[2,17])-S12*(ALPHA111+BETA211*s.dpt[2,17])
  ALPHA312 = ALPHA311+BETA811*s.dpt[2,17]
  OM113 = qd[13]+OM112
  OM313 = -(OM212*S13-OM312*C13)
  ALPHA313 = -(ALPHA212*S13-ALPHA312*C13)
  OM114 = OM113*C14-OM313*S14
  OM115 = qd[15]+OM16
  OM215 = OM26*C15+OM36*S15
  OM315 = -(OM26*S15-OM36*C15)
  OMp115 = qdd[15]+OMp16
  OMp215 = C15*(OMp26+qd[15]*OM36)+S15*(OMp36-qd[15]*OM26)
  OMp315 = C15*(OMp36-qd[15]*OM26)-S15*(OMp26+qd[15]*OM36)
  BS515 = -(OM115*OM115+OM315*OM315)
  BETA215 = OM115*OM215-OMp315
  BETA815 = OMp115+OM215*OM315
  ALPHA115 = ALPHA16+BETA26*s.dpt[2,9]+BETA36*s.dpt[3,9]+BS16*s.dpt[1,9]
  ALPHA215 = C15*(ALPHA26+BETA46*s.dpt[1,9]+BETA66*s.dpt[3,9]+BS56*s.dpt[2,9])+S15*(ALPHA35+BETA76*s.dpt[1,9]+BETA86*\
   s.dpt[2,9]+BS96*s.dpt[3,9])
  ALPHA315 = C15*(ALPHA35+BETA76*s.dpt[1,9]+BETA86*s.dpt[2,9]+BS96*s.dpt[3,9])-S15*(ALPHA26+BETA46*s.dpt[1,9]+BETA66*\
   s.dpt[3,9]+BS56*s.dpt[2,9])
  OM116 = qd[16]+OM115
  OM216 = OM215*C16+OM315*S16
  OM316 = -(OM215*S16-OM315*C16)
  OMp116 = qdd[16]+OMp115
  OMp216 = C16*(OMp215+qd[16]*OM315)+S16*(OMp315-qd[16]*OM215)
  OMp316 = C16*(OMp315-qd[16]*OM215)-S16*(OMp215+qd[16]*OM315)
  BS116 = -(OM216*OM216+OM316*OM316)
  BETA416 = OMp316+OM116*OM216
  BETA716 = OM116*OM316-OMp216
  ALPHA116 = ALPHA115+BETA215*s.dpt[2,21]
  ALPHA216 = C16*(ALPHA215+BS515*s.dpt[2,21])+S16*(ALPHA315+BETA815*s.dpt[2,21])
  ALPHA316 = C16*(ALPHA315+BETA815*s.dpt[2,21])-S16*(ALPHA215+BS515*s.dpt[2,21])
  OM117 = qd[17]+OM116
  OM317 = -(OM216*S17-OM316*C17)
  ALPHA117 = ALPHA116+BS116*s.dpt[1,23]
  ALPHA317 = C17*(ALPHA316+BETA716*s.dpt[1,23])-S17*(ALPHA216+BETA416*s.dpt[1,23])
  OM118 = OM117*C18-OM317*S18
  OM119 = qd[19]+OM16
  OM219 = OM26*C19+OM36*S19
  OM319 = -(OM26*S19-OM36*C19)
  OMp119 = qdd[19]+OMp16
  OMp219 = C19*(OMp26+qd[19]*OM36)+S19*(OMp36-qd[19]*OM26)
  OMp319 = C19*(OMp36-qd[19]*OM26)-S19*(OMp26+qd[19]*OM36)
  BS519 = -(OM119*OM119+OM319*OM319)
  BETA219 = OM119*OM219-OMp319
  BETA819 = OMp119+OM219*OM319
  ALPHA119 = ALPHA16+BETA26*s.dpt[2,11]+BETA36*s.dpt[3,11]+BS16*s.dpt[1,11]
  ALPHA219 = C19*(ALPHA26+BETA46*s.dpt[1,11]+BETA66*s.dpt[3,11]+BS56*s.dpt[2,11])+S19*(ALPHA35+BETA76*s.dpt[1,11]+BETA86\
   *s.dpt[2,11]+BS96*s.dpt[3,11])
  ALPHA319 = C19*(ALPHA35+BETA76*s.dpt[1,11]+BETA86*s.dpt[2,11]+BS96*s.dpt[3,11])-S19*(ALPHA26+BETA46*s.dpt[1,11]+BETA66\
   *s.dpt[3,11]+BS56*s.dpt[2,11])
  OM120 = qd[20]+OM119
  OM220 = OM219*C20+OM319*S20
  OM320 = -(OM219*S20-OM319*C20)
  OMp120 = qdd[20]+OMp119
  OMp220 = C20*(OMp219+qd[20]*OM319)+S20*(OMp319-qd[20]*OM219)
  OMp320 = C20*(OMp319-qd[20]*OM219)-S20*(OMp219+qd[20]*OM319)
  BS120 = -(OM220*OM220+OM320*OM320)
  BETA420 = OMp320+OM120*OM220
  BETA720 = OM120*OM320-OMp220
  ALPHA120 = ALPHA119+BETA219*s.dpt[2,27]
  ALPHA220 = C20*(ALPHA219+BS519*s.dpt[2,27])+S20*(ALPHA319+BETA819*s.dpt[2,27])
  ALPHA320 = C20*(ALPHA319+BETA819*s.dpt[2,27])-S20*(ALPHA219+BS519*s.dpt[2,27])
  OM121 = qd[21]+OM120
  OM321 = -(OM220*S21-OM320*C21)
  ALPHA121 = ALPHA120+BS120*s.dpt[1,31]
  ALPHA321 = C21*(ALPHA320+BETA720*s.dpt[1,31])-S21*(ALPHA220+BETA420*s.dpt[1,31])
  OM122 = OM121*C22-OM321*S22
 
# Backward Dynamics 

  Fs122 = -(s.frc[1,22]-s.m[22]*(ALPHA121*C22-ALPHA321*S22))
  Fs222 = -(s.frc[2,22]-s.m[22]*(C21*(ALPHA220+BETA420*s.dpt[1,31])+S21*(ALPHA320+BETA720*s.dpt[1,31])))
  Fs322 = -(s.frc[3,22]-s.m[22]*(ALPHA121*S22+ALPHA321*C22))
  Cq122 = -(s.trq[1,22]-s.In[1,22]*(C22*(qdd[21]+OMp120-qd[22]*OM321)-S22*(qd[22]*OM121+C21*(OMp320-qd[21]*OM220)-S21*(\
   OMp220+qd[21]*OM320))))
  Cq222 = -(s.trq[2,22]-s.In[1,22]*OM122*(OM121*S22+OM321*C22))
  Cq322 = -(s.trq[3,22]+s.In[1,22]*OM122*(qd[22]+OM220*C21+OM320*S21))
  Fq321 = -(Fs122*S22-Fs322*C22)
  Cq121 = Cq122*C22+Cq322*S22
  Cq321 = -(Cq122*S22-Cq322*C22)
  Fs220 = -(s.frc[2,20]-s.m[20]*(ALPHA220+BETA420*s.l[1,20]))
  Fs320 = -(s.frc[3,20]-s.m[20]*(ALPHA320+BETA720*s.l[1,20]))
  Fq120 = -(s.frc[1,20]-s.m[20]*(ALPHA120+BS120*s.l[1,20])-Fs122*C22-Fs322*S22)
  Fq220 = Fs220-Fq321*S21+Fs222*C21
  Fq320 = Fs320+Fq321*C21+Fs222*S21
  Cq120 = -(s.trq[1,20]-Cq121-s.In[1,20]*OMp120)
  Cq220 = -(s.trq[2,20]-s.In[1,20]*OM120*OM320-Cq222*C21+Cq321*S21+Fs320*s.l[1,20]+s.dpt[1,31]*(Fq321*C21+Fs222*S21))
  Cq320 = -(s.trq[3,20]+s.In[1,20]*OM120*OM220-Cq222*S21-Cq321*C21-Fs220*s.l[1,20]+s.dpt[1,31]*(Fq321*S21-Fs222*C21))
  Fs119 = -(s.frc[1,19]-s.m[19]*(ALPHA119+BETA219*s.l[2,19]))
  Fs319 = -(s.frc[3,19]-s.m[19]*(ALPHA319+BETA819*s.l[2,19]))
  Fq119 = Fq120+Fs119
  Fq219 = -(s.frc[2,19]-s.m[19]*(ALPHA219+BS519*s.l[2,19])-Fq220*C20+Fq320*S20)
  Fq319 = Fs319+Fq220*S20+Fq320*C20
  Cq119 = -(s.trq[1,19]-Cq120-s.In[1,19]*OMp119-s.In[9,19]*OM219*OM319-Fs319*s.l[2,19]-s.dpt[2,27]*(Fq220*S20+Fq320*C20)\
   )
  Cq219 = -(s.trq[2,19]-Cq220*C20+Cq320*S20-OM119*OM319*(s.In[1,19]-s.In[9,19]))
  Cq319 = -(s.trq[3,19]+s.In[1,19]*OM119*OM219-s.In[9,19]*OMp319-Cq220*S20-Cq320*C20+Fq120*s.dpt[2,27]+Fs119*s.l[2,19])
  Fs118 = -(s.frc[1,18]-s.m[18]*(ALPHA117*C18-ALPHA317*S18))
  Fs218 = -(s.frc[2,18]-s.m[18]*(C17*(ALPHA216+BETA416*s.dpt[1,23])+S17*(ALPHA316+BETA716*s.dpt[1,23])))
  Fs318 = -(s.frc[3,18]-s.m[18]*(ALPHA117*S18+ALPHA317*C18))
  Cq118 = -(s.trq[1,18]-s.In[1,18]*(C18*(qdd[17]+OMp116-qd[18]*OM317)-S18*(qd[18]*OM117+C17*(OMp316-qd[17]*OM216)-S17*(\
   OMp216+qd[17]*OM316))))
  Cq218 = -(s.trq[2,18]-s.In[1,18]*OM118*(OM117*S18+OM317*C18))
  Cq318 = -(s.trq[3,18]+s.In[1,18]*OM118*(qd[18]+OM216*C17+OM316*S17))
  Fq317 = -(Fs118*S18-Fs318*C18)
  Cq117 = Cq118*C18+Cq318*S18
  Cq317 = -(Cq118*S18-Cq318*C18)
  Fs216 = -(s.frc[2,16]-s.m[16]*(ALPHA216+BETA416*s.l[1,16]))
  Fs316 = -(s.frc[3,16]-s.m[16]*(ALPHA316+BETA716*s.l[1,16]))
  Fq116 = -(s.frc[1,16]-s.m[16]*(ALPHA116+BS116*s.l[1,16])-Fs118*C18-Fs318*S18)
  Fq216 = Fs216-Fq317*S17+Fs218*C17
  Fq316 = Fs316+Fq317*C17+Fs218*S17
  Cq116 = -(s.trq[1,16]-Cq117-s.In[1,16]*OMp116)
  Cq216 = -(s.trq[2,16]-s.In[1,16]*OM116*OM316-Cq218*C17+Cq317*S17+Fs316*s.l[1,16]+s.dpt[1,23]*(Fq317*C17+Fs218*S17))
  Cq316 = -(s.trq[3,16]+s.In[1,16]*OM116*OM216-Cq218*S17-Cq317*C17-Fs216*s.l[1,16]+s.dpt[1,23]*(Fq317*S17-Fs218*C17))
  Fs115 = -(s.frc[1,15]-s.m[15]*(ALPHA115+BETA215*s.l[2,15]))
  Fs315 = -(s.frc[3,15]-s.m[15]*(ALPHA315+BETA815*s.l[2,15]))
  Fq115 = Fq116+Fs115
  Fq215 = -(s.frc[2,15]-s.m[15]*(ALPHA215+BS515*s.l[2,15])-Fq216*C16+Fq316*S16)
  Fq315 = Fs315+Fq216*S16+Fq316*C16
  Cq115 = -(s.trq[1,15]-Cq116-s.In[1,15]*OMp115-s.In[9,15]*OM215*OM315-Fs315*s.l[2,15]-s.dpt[2,21]*(Fq216*S16+Fq316*C16)\
   )
  Cq215 = -(s.trq[2,15]-Cq216*C16+Cq316*S16-OM115*OM315*(s.In[1,15]-s.In[9,15]))
  Cq315 = -(s.trq[3,15]+s.In[1,15]*OM115*OM215-s.In[9,15]*OMp315-Cq216*S16-Cq316*C16+Fq116*s.dpt[2,21]+Fs115*s.l[2,15])
  Fs114 = -(s.frc[1,14]-s.m[14]*(ALPHA112*C14-ALPHA313*S14))
  Fs214 = -(s.frc[2,14]-s.m[14]*(ALPHA212*C13+ALPHA312*S13))
  Fs314 = -(s.frc[3,14]-s.m[14]*(ALPHA112*S14+ALPHA313*C14))
  Cq114 = -(s.trq[1,14]-s.In[1,14]*(C14*(qdd[13]+OMp112-qd[14]*OM313)-S14*(qd[14]*OM113+C13*(OMp312-qd[13]*OM212)-S13*(\
   OMp212+qd[13]*OM312))))
  Cq214 = -(s.trq[2,14]-s.In[1,14]*OM114*(OM113*S14+OM313*C14))
  Cq314 = -(s.trq[3,14]+s.In[1,14]*OM114*(qd[14]+OM212*C13+OM312*S13))
  Fq313 = -(Fs114*S14-Fs314*C14)
  Cq113 = Cq114*C14+Cq314*S14
  Cq313 = -(Cq114*S14-Cq314*C14)
  Fs112 = -(s.frc[1,12]-s.m[12]*(ALPHA112+s.l[3,12]*(OMp212+OM112*OM312)))
  Fs212 = -(s.frc[2,12]-s.m[12]*(ALPHA212-s.l[3,12]*(OMp112-OM212*OM312)))
  Fq112 = Fs112+Fs114*C14+Fs314*S14
  Fq212 = Fs212-Fq313*S13+Fs214*C13
  Fq312 = -(s.frc[3,12]-s.m[12]*(ALPHA312-s.l[3,12]*(OM112*OM112+OM212*OM212))-Fq313*C13-Fs214*S13)
  Cq112 = -(s.trq[1,12]-Cq113-s.In[1,12]*OMp112-s.In[9,12]*OM212*OM312+Fs212*s.l[3,12])
  Cq212 = -(s.trq[2,12]-Cq214*C13+Cq313*S13-Fs112*s.l[3,12]-OM112*OM312*(s.In[1,12]-s.In[9,12]))
  Cq312 = -(s.trq[3,12]+s.In[1,12]*OM112*OM212-s.In[9,12]*OMp312-Cq214*S13-Cq313*C13)
  Fs111 = -(s.frc[1,11]-s.m[11]*(ALPHA111+BETA211*s.l[2,11]))
  Fs311 = -(s.frc[3,11]-s.m[11]*(ALPHA311+BETA811*s.l[2,11]))
  Fq111 = Fs111+Fq112*C12-Fq212*S12
  Fq211 = -(s.frc[2,11]-s.m[11]*(ALPHA211+BS511*s.l[2,11])-Fq112*S12-Fq212*C12)
  Fq311 = Fq312+Fs311
  Cq111 = -(s.trq[1,11]-s.In[1,11]*OMp111-Cq112*C12+Cq212*S12-Fq312*s.dpt[2,17]-Fs311*s.l[2,11])
  Cq211 = -(s.trq[2,11]-s.In[1,11]*OM111*OM311-Cq112*S12-Cq212*C12)
  Cq311 = -(s.trq[3,11]-Cq312+s.In[1,11]*OM111*OM211+Fs111*s.l[2,11]+s.dpt[2,17]*(Fq112*C12-Fq212*S12))
  Fs110 = -(s.frc[1,10]-s.m[10]*(ALPHA18*C10-ALPHA39*S10))
  Fs210 = -(s.frc[2,10]-s.m[10]*(ALPHA28*C9+ALPHA38*S9))
  Fs310 = -(s.frc[3,10]-s.m[10]*(ALPHA18*S10+ALPHA39*C10))
  Cq110 = -(s.trq[1,10]-s.In[1,10]*(C10*(qdd[9]+OMp18-qd[10]*OM39)-S10*(qd[10]*OM19+C9*(OMp38-qd[9]*OM28)-S9*(OMp28+\
   qd[9]*OM38))))
  Cq210 = -(s.trq[2,10]-s.In[1,10]*OM110*(OM19*S10+OM39*C10))
  Cq310 = -(s.trq[3,10]+s.In[1,10]*OM110*(qd[10]+OM28*C9+OM38*S9))
  Fq39 = -(Fs110*S10-Fs310*C10)
  Cq19 = Cq110*C10+Cq310*S10
  Cq39 = -(Cq110*S10-Cq310*C10)
  Fs18 = -(s.frc[1,8]-s.m[8]*(ALPHA18+s.l[3,8]*(OMp28+OM18*OM38)))
  Fs28 = -(s.frc[2,8]-s.m[8]*(ALPHA28-s.l[3,8]*(OMp18-OM28*OM38)))
  Fq18 = Fs18+Fs110*C10+Fs310*S10
  Fq28 = Fs28-Fq39*S9+Fs210*C9
  Fq38 = -(s.frc[3,8]-s.m[8]*(ALPHA38-s.l[3,8]*(OM18*OM18+OM28*OM28))-Fq39*C9-Fs210*S9)
  Cq18 = -(s.trq[1,8]-Cq19-s.In[1,8]*OMp18-s.In[9,8]*OM28*OM38+Fs28*s.l[3,8])
  Cq28 = -(s.trq[2,8]-Cq210*C9+Cq39*S9-Fs18*s.l[3,8]-OM18*OM38*(s.In[1,8]-s.In[9,8]))
  Cq38 = -(s.trq[3,8]+s.In[1,8]*OM18*OM28-s.In[9,8]*OMp38-Cq210*S9-Cq39*C9)
  Fs17 = -(s.frc[1,7]-s.m[7]*(ALPHA17+BETA27*s.l[2,7]))
  Fs37 = -(s.frc[3,7]-s.m[7]*(ALPHA37+BETA87*s.l[2,7]))
  Fq17 = Fs17+Fq18*C8-Fq28*S8
  Fq27 = -(s.frc[2,7]-s.m[7]*(ALPHA27+BS57*s.l[2,7])-Fq18*S8-Fq28*C8)
  Fq37 = Fq38+Fs37
  Cq17 = -(s.trq[1,7]-s.In[1,7]*OMp17-Cq18*C8+Cq28*S8-Fq38*s.dpt[2,13]-Fs37*s.l[2,7])
  Cq27 = -(s.trq[2,7]-s.In[1,7]*OM17*OM37-Cq18*S8-Cq28*C8)
  Cq37 = -(s.trq[3,7]-Cq38+s.In[1,7]*OM17*OM27+Fs17*s.l[2,7]+s.dpt[2,13]*(Fq18*C8-Fq28*S8))
  Fs16 = -(s.frc[1,6]-s.m[6]*(ALPHA16+BETA36*s.l[3,6]))
  Fs26 = -(s.frc[2,6]-s.m[6]*(ALPHA26+BETA66*s.l[3,6]))
  Fq16 = Fq111+Fq115+Fq119+Fq17+Fs16
  Fq26 = Fs26+Fq211*C11+Fq215*C15+Fq219*C19+Fq27*C7-Fq311*S11-Fq315*S15-Fq319*S19-Fq37*S7
  Fq36 = -(s.frc[3,6]-s.m[6]*(ALPHA35+BS96*s.l[3,6])-Fq211*S11-Fq215*S15-Fq219*S19-Fq27*S7-Fq311*C11-Fq315*C15-Fq319*C19\
   -Fq37*C7)
  Cq16 = -(s.trq[1,6]-Cq111-Cq115-Cq119-Cq17-s.In[1,6]*OMp16+Fs26*s.l[3,6]+OM26*OM36*(s.In[5,6]-s.In[9,6])-s.dpt[2,11]*(\
   Fq219*S19+Fq319*C19)-s.dpt[2,1]*(Fq27*S7+Fq37*C7)-s.dpt[2,4]*(Fq211*S11+Fq311*C11)-s.dpt[2,9]*(Fq215*S15+Fq315*C15)+\
   s.dpt[3,11]*(Fq219*C19-Fq319*S19)+s.dpt[3,1]*(Fq27*C7-Fq37*S7)+s.dpt[3,4]*(Fq211*C11-Fq311*S11)+s.dpt[3,9]*(Fq215*C15-Fq315*\
   S15))
  Cq26 = -(s.trq[2,6]-s.In[5,6]*OMp26-Cq211*C11-Cq215*C15-Cq219*C19-Cq27*C7+Cq311*S11+Cq315*S15+Cq319*S19+Cq37*S7-Fq111*\
   s.dpt[3,4]-Fq115*s.dpt[3,9]-Fq119*s.dpt[3,11]-Fq17*s.dpt[3,1]-Fs16*s.l[3,6]-OM16*OM36*(s.In[1,6]-s.In[9,6])+s.dpt[1,11]*(\
   Fq219*S19+Fq319*C19)+s.dpt[1,1]*(Fq27*S7+Fq37*C7)+s.dpt[1,4]*(Fq211*S11+Fq311*C11)+s.dpt[1,9]*(Fq215*S15+Fq315*C15))
  Cq36 = -(s.trq[3,6]-s.In[9,6]*OMp36-Cq211*S11-Cq215*S15-Cq219*S19-Cq27*S7-Cq311*C11-Cq315*C15-Cq319*C19-Cq37*C7+Fq111*\
   s.dpt[2,4]+Fq115*s.dpt[2,9]+Fq119*s.dpt[2,11]+Fq17*s.dpt[2,1]+OM16*OM26*(s.In[1,6]-s.In[5,6])-s.dpt[1,11]*(Fq219*C19-Fq319*\
   S19)-s.dpt[1,1]*(Fq27*C7-Fq37*S7)-s.dpt[1,4]*(Fq211*C11-Fq311*S11)-s.dpt[1,9]*(Fq215*C15-Fq315*S15))
  Fq15 = Fq16*C6-Fq26*S6
  Fq25 = Fq16*S6+Fq26*C6
  Cq25 = Cq16*S6+Cq26*C6
  Fq14 = Fq15*C5+Fq36*S5
  Fq34 = -(Fq15*S5-Fq36*C5)
  Cq14 = Cq36*S5+C5*(Cq16*C6-Cq26*S6)
  Fq23 = Fq25*C4-Fq34*S4
  Fq33 = Fq25*S4+Fq34*C4

# = = Block_0_2_0_0_0_0 = = 
 
# Symbolic Outputs  

  Qq[1] = Fq14
  Qq[2] = Fq23
  Qq[3] = Fq33
  Qq[4] = Cq14
  Qq[5] = Cq25
  Qq[6] = Cq36
  Qq[7] = Cq17
  Qq[8] = Cq38
  Qq[9] = Cq19
  Qq[10] = Cq210
  Qq[11] = Cq111
  Qq[12] = Cq312
  Qq[13] = Cq113
  Qq[14] = Cq214
  Qq[15] = Cq115
  Qq[16] = Cq116
  Qq[17] = Cq117
  Qq[18] = Cq218
  Qq[19] = Cq119
  Qq[20] = Cq120
  Qq[21] = Cq121
  Qq[22] = Cq222

# ====== END Task 0 ====== 

  

