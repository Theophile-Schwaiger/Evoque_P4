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
#	==> Function : F18 : Constraints Quadratic Velocity Terms (Jdqd)
#	==> Flops complexity : 1366
#
#	==> Generation Time :  0.030 seconds
#	==> Post-Processing :  0.020 seconds
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

# = = Block_0_1_0_0_0_2 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_7_28 = C7*S8
  RO_7_38 = S7*S8
  RO_7_58 = C7*C8
  RO_7_68 = S7*C8
  RO_7_49 = -S8*C9
  RO_7_59 = RO_7_58*C9-S7*S9
  RO_7_69 = RO_7_68*C9+C7*S9
  RO_7_79 = S8*S9
  RO_7_89 = -(RO_7_58*S9+S7*C9)
  RO_7_99 = -(RO_7_68*S9-C7*C9)
  RO_7_110 = -(RO_7_79*S10-C10*C8)
  RO_7_210 = RO_7_28*C10-RO_7_89*S10
  RO_7_310 = RO_7_38*C10-RO_7_99*S10
  RO_7_710 = RO_7_79*C10+S10*C8
  RO_7_810 = RO_7_28*S10+RO_7_89*C10
  RO_7_910 = RO_7_38*S10+RO_7_99*C10

# = = Block_0_1_0_0_0_3 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_7_711 = -(RO_7_49*S11-RO_7_710*C11)
  RO_7_811 = -(RO_7_59*S11-RO_7_810*C11)
  RO_7_911 = -(RO_7_69*S11-RO_7_910*C11)
  RL_7_111 = RO_7_710*s.dpt[3,14]
  RL_7_211 = RO_7_810*s.dpt[3,14]
  RL_7_311 = RO_7_910*s.dpt[3,14]
  RL_7_112 = RO_7_711*q[12]
  RL_7_212 = RO_7_811*q[12]
  RL_7_312 = RO_7_911*q[12]
  RL_7_146 = RO_7_711*s.dpt[3,16]
  RL_7_246 = RO_7_811*s.dpt[3,16]
  RL_7_346 = RO_7_911*s.dpt[3,16]

# = = Block_0_1_0_0_0_5 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_4_216 = C15*S16
  RO_4_316 = S15*S16
  RO_4_516 = C15*C16
  RO_4_616 = S15*C16
  RO_4_417 = -S16*C17
  RO_4_517 = RO_4_516*C17-S15*S17
  RO_4_617 = RO_4_616*C17+C15*S17
  RO_4_717 = S16*S17
  RO_4_817 = -(RO_4_516*S17+S15*C17)
  RO_4_917 = -(RO_4_616*S17-C15*C17)
  RO_4_118 = -(RO_4_717*S18-C16*C18)
  RO_4_218 = RO_4_216*C18-RO_4_817*S18
  RO_4_318 = RO_4_316*C18-RO_4_917*S18
  RO_4_718 = RO_4_717*C18+C16*S18
  RO_4_818 = RO_4_216*S18+RO_4_817*C18
  RO_4_918 = RO_4_316*S18+RO_4_917*C18

# = = Block_0_1_0_0_0_6 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_4_719 = -(RO_4_417*S19-RO_4_718*C19)
  RO_4_819 = -(RO_4_517*S19-RO_4_818*C19)
  RO_4_919 = -(RO_4_617*S19-RO_4_918*C19)
  RL_4_119 = RO_4_718*s.dpt[3,19]
  RL_4_219 = RO_4_818*s.dpt[3,19]
  RL_4_319 = RO_4_918*s.dpt[3,19]
  RL_4_120 = RO_4_719*q[20]
  RL_4_220 = RO_4_819*q[20]
  RL_4_320 = RO_4_919*q[20]
  RL_4_143 = RO_4_719*s.dpt[3,21]
  RL_4_243 = RO_4_819*s.dpt[3,21]
  RL_4_343 = RO_4_919*s.dpt[3,21]

# = = Block_0_1_0_0_0_8 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_1_224 = C23*S24
  RO_1_324 = S23*S24
  RO_1_524 = C23*C24
  RO_1_624 = S23*C24
  RO_1_425 = -S24*C25
  RO_1_525 = RO_1_524*C25-S23*S25
  RO_1_625 = RO_1_624*C25+C23*S25
  RO_1_725 = S24*S25
  RO_1_825 = -(RO_1_524*S25+S23*C25)
  RO_1_925 = -(RO_1_624*S25-C23*C25)
  RO_1_126 = RO_1_425*S26+C24*C26
  RO_1_226 = RO_1_224*C26+RO_1_525*S26
  RO_1_326 = RO_1_324*C26+RO_1_625*S26
  RL_1_125 = -s.dpt[2,23]*S24
  RL_1_225 = RO_1_524*s.dpt[2,23]
  RL_1_325 = RO_1_624*s.dpt[2,23]
  PO_1_125 = RL_1_125+s.dpt[1,10]
  PO_1_225 = RL_1_225+s.dpt[2,10]
#
  RL_9_148 = RO_1_126*s.dpt[1,27]+RO_1_725*s.dpt[3,27]
  RL_9_248 = RO_1_226*s.dpt[1,27]+RO_1_825*s.dpt[3,27]
  RL_9_348 = RO_1_326*s.dpt[1,27]+RO_1_925*s.dpt[3,27]
#
  RL_11_150 = RO_1_126*s.dpt[1,26]+RO_1_725*s.dpt[3,26]
  RL_11_250 = RO_1_226*s.dpt[1,26]+RO_1_825*s.dpt[3,26]
  RL_11_350 = RO_1_326*s.dpt[1,26]+RO_1_925*s.dpt[3,26]

# = = Block_0_1_0_0_0_9 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_1_727 = RO_1_725*C27-S27*(RO_1_425*C26-C24*S26)
  RO_1_827 = RO_1_825*C27+S27*(RO_1_224*S26-RO_1_525*C26)
  RO_1_927 = RO_1_925*C27+S27*(RO_1_324*S26-RO_1_625*C26)
  RL_1_127 = RO_1_725*s.dpt[3,24]
  RL_1_227 = RO_1_825*s.dpt[3,24]
  RL_1_327 = RO_1_925*s.dpt[3,24]
  RL_1_128 = RO_1_727*q[28]
  RL_1_228 = RO_1_827*q[28]
  RL_1_328 = RO_1_927*q[28]
  RL_1_140 = RO_1_727*s.dpt[3,28]
  RL_1_240 = RO_1_827*s.dpt[3,28]
  RL_1_340 = RO_1_927*s.dpt[3,28]

# = = Block_0_1_0_0_0_11 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_2_232 = C31*S32
  RO_2_332 = S31*S32
  RO_2_532 = C31*C32
  RO_2_632 = S31*C32
  RO_2_433 = -S32*C33
  RO_2_533 = RO_2_532*C33-S31*S33
  RO_2_633 = RO_2_632*C33+C31*S33
  RO_2_733 = S32*S33
  RO_2_833 = -(RO_2_532*S33+S31*C33)
  RO_2_933 = -(RO_2_632*S33-C31*C33)
  RO_2_134 = RO_2_433*S34+C32*C34
  RO_2_234 = RO_2_232*C34+RO_2_533*S34
  RO_2_334 = RO_2_332*C34+RO_2_633*S34
  RL_2_133 = -s.dpt[2,30]*S32
  RL_2_233 = RO_2_532*s.dpt[2,30]
  RL_2_333 = RO_2_632*s.dpt[2,30]
  PO_2_133 = RL_2_133+s.dpt[1,12]
  PO_2_233 = RL_2_233+s.dpt[2,12]
#
  RL_12_151 = RO_2_134*s.dpt[1,31]+RO_2_733*s.dpt[3,31]
  RL_12_251 = RO_2_234*s.dpt[1,31]+RO_2_833*s.dpt[3,31]
  RL_12_351 = RO_2_334*s.dpt[1,31]+RO_2_933*s.dpt[3,31]
#
  RL_14_153 = RO_2_134*s.dpt[1,32]+RO_2_733*s.dpt[3,32]
  RL_14_253 = RO_2_234*s.dpt[1,32]+RO_2_833*s.dpt[3,32]
  RL_14_353 = RO_2_334*s.dpt[1,32]+RO_2_933*s.dpt[3,32]

# = = Block_0_1_0_0_0_12 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_2_735 = RO_2_733*C35-S35*(RO_2_433*C34-C32*S34)
  RO_2_835 = RO_2_833*C35+S35*(RO_2_232*S34-RO_2_533*C34)
  RO_2_935 = RO_2_933*C35+S35*(RO_2_332*S34-RO_2_633*C34)
  RL_2_135 = RO_2_733*s.dpt[3,33]
  RL_2_235 = RO_2_833*s.dpt[3,33]
  RL_2_335 = RO_2_933*s.dpt[3,33]
  RL_2_136 = RO_2_735*q[36]
  RL_2_236 = RO_2_835*q[36]
  RL_2_336 = RO_2_935*q[36]
  RL_2_141 = RO_2_735*s.dpt[3,35]
  RL_2_241 = RO_2_835*s.dpt[3,35]
  RL_2_341 = RO_2_935*s.dpt[3,35]

# = = Block_0_2_0_0_0_0 = = 
 
# Constraints Quadratic Terms 

#
  OM_1_224 = -qd[24]*S23
  OM_1_324 = qd[24]*C23
  Ompqp_1_224 = -qd[23]*qd[24]*C23
  Ompqp_1_324 = -qd[23]*qd[24]*S23
  OM_1_125 = qd[23]+qd[25]*C24
  OM_1_225 = OM_1_224+RO_1_224*qd[25]
  OM_1_325 = OM_1_324+RO_1_324*qd[25]
  OR_1_125 = -qd[24]*s.dpt[2,23]*C24
  OR_1_225 = OM_1_324*RL_1_125-RL_1_325*qd[23]
  OR_1_325 = -(OM_1_224*RL_1_125-RL_1_225*qd[23])
  Apqp_1_125 = OM_1_224*OR_1_325-OM_1_324*OR_1_225+Ompqp_1_224*RL_1_325-Ompqp_1_324*RL_1_225
  Apqp_1_225 = OM_1_324*OR_1_125-OR_1_325*qd[23]+Ompqp_1_324*RL_1_125
  Apqp_1_325 = -(OM_1_224*OR_1_125-OR_1_225*qd[23]+Ompqp_1_224*RL_1_125)
  OM_1_126 = OM_1_125+RO_1_725*qd[26]
  OM_1_226 = OM_1_225+RO_1_825*qd[26]
  OM_1_326 = OM_1_325+RO_1_925*qd[26]
  Ompqp_1_126 = -(qd[24]*qd[25]*S24-qd[26]*(OM_1_225*RO_1_925-OM_1_325*RO_1_825))
  Ompqp_1_226 = Ompqp_1_224+qd[25]*(OM_1_324*C24-RO_1_324*qd[23])-qd[26]*(OM_1_125*RO_1_925-OM_1_325*RO_1_725)
  Ompqp_1_326 = Ompqp_1_324-qd[25]*(OM_1_224*C24-RO_1_224*qd[23])+qd[26]*(OM_1_125*RO_1_825-OM_1_225*RO_1_725)
  OM_1_127 = OM_1_126+RO_1_126*qd[27]
  OM_1_227 = OM_1_226+RO_1_226*qd[27]
  OM_1_327 = OM_1_326+RO_1_326*qd[27]
  OR_1_127 = OM_1_226*RL_1_327-OM_1_326*RL_1_227
  OR_1_227 = -(OM_1_126*RL_1_327-OM_1_326*RL_1_127)
  OR_1_327 = OM_1_126*RL_1_227-OM_1_226*RL_1_127
  Ompqp_1_127 = Ompqp_1_126+qd[27]*(OM_1_226*RO_1_326-OM_1_326*RO_1_226)
  Ompqp_1_227 = Ompqp_1_226-qd[27]*(OM_1_126*RO_1_326-OM_1_326*RO_1_126)
  Ompqp_1_327 = Ompqp_1_326+qd[27]*(OM_1_126*RO_1_226-OM_1_226*RO_1_126)
  OR_1_128 = OM_1_227*RL_1_328-OM_1_327*RL_1_228
  OR_1_228 = -(OM_1_127*RL_1_328-OM_1_327*RL_1_128)
  OR_1_328 = OM_1_127*RL_1_228-OM_1_227*RL_1_128
  OR_1_140 = OM_1_227*RL_1_340-OM_1_327*RL_1_240
  OR_1_240 = -(OM_1_127*RL_1_340-OM_1_327*RL_1_140)
  OR_1_340 = OM_1_127*RL_1_240-OM_1_227*RL_1_140
  Apqp_1_140 = Apqp_1_125+OM_1_226*OR_1_327+OM_1_227*OR_1_328+OM_1_227*OR_1_340-OM_1_326*OR_1_227-OM_1_327*OR_1_228-\
   OM_1_327*OR_1_240+Ompqp_1_226*RL_1_327+Ompqp_1_227*RL_1_328+Ompqp_1_227*RL_1_340-Ompqp_1_326*RL_1_227-Ompqp_1_327*RL_1_228-\
   Ompqp_1_327*RL_1_240+(2.0)*qd[28]*(OM_1_227*RO_1_927-OM_1_327*RO_1_827)
  Apqp_1_240 = Apqp_1_225-OM_1_126*OR_1_327-OM_1_127*OR_1_328-OM_1_127*OR_1_340+OM_1_326*OR_1_127+OM_1_327*OR_1_128+\
   OM_1_327*OR_1_140-Ompqp_1_126*RL_1_327-Ompqp_1_127*RL_1_328-Ompqp_1_127*RL_1_340+Ompqp_1_326*RL_1_127+Ompqp_1_327*RL_1_128+\
   Ompqp_1_327*RL_1_140-(2.0)*qd[28]*(OM_1_127*RO_1_927-OM_1_327*RO_1_727)
  Apqp_1_340 = Apqp_1_325+OM_1_126*OR_1_227+OM_1_127*OR_1_228+OM_1_127*OR_1_240-OM_1_226*OR_1_127-OM_1_227*OR_1_128-\
   OM_1_227*OR_1_140+Ompqp_1_126*RL_1_227+Ompqp_1_127*RL_1_228+Ompqp_1_127*RL_1_240-Ompqp_1_226*RL_1_127-Ompqp_1_227*RL_1_128-\
   Ompqp_1_227*RL_1_140+(2.0)*qd[28]*(OM_1_127*RO_1_827-OM_1_227*RO_1_727)
#
  OM_2_232 = -qd[32]*S31
  OM_2_332 = qd[32]*C31
  Ompqp_2_232 = -qd[31]*qd[32]*C31
  Ompqp_2_332 = -qd[31]*qd[32]*S31
  OM_2_133 = qd[31]+qd[33]*C32
  OM_2_233 = OM_2_232+RO_2_232*qd[33]
  OM_2_333 = OM_2_332+RO_2_332*qd[33]
  OR_2_133 = -qd[32]*s.dpt[2,30]*C32
  OR_2_233 = OM_2_332*RL_2_133-RL_2_333*qd[31]
  OR_2_333 = -(OM_2_232*RL_2_133-RL_2_233*qd[31])
  Apqp_2_133 = OM_2_232*OR_2_333-OM_2_332*OR_2_233+Ompqp_2_232*RL_2_333-Ompqp_2_332*RL_2_233
  Apqp_2_233 = OM_2_332*OR_2_133-OR_2_333*qd[31]+Ompqp_2_332*RL_2_133
  Apqp_2_333 = -(OM_2_232*OR_2_133-OR_2_233*qd[31]+Ompqp_2_232*RL_2_133)
  OM_2_134 = OM_2_133+RO_2_733*qd[34]
  OM_2_234 = OM_2_233+RO_2_833*qd[34]
  OM_2_334 = OM_2_333+RO_2_933*qd[34]
  Ompqp_2_134 = -(qd[32]*qd[33]*S32-qd[34]*(OM_2_233*RO_2_933-OM_2_333*RO_2_833))
  Ompqp_2_234 = Ompqp_2_232+qd[33]*(OM_2_332*C32-RO_2_332*qd[31])-qd[34]*(OM_2_133*RO_2_933-OM_2_333*RO_2_733)
  Ompqp_2_334 = Ompqp_2_332-qd[33]*(OM_2_232*C32-RO_2_232*qd[31])+qd[34]*(OM_2_133*RO_2_833-OM_2_233*RO_2_733)
  OM_2_135 = OM_2_134+RO_2_134*qd[35]
  OM_2_235 = OM_2_234+RO_2_234*qd[35]
  OM_2_335 = OM_2_334+RO_2_334*qd[35]
  OR_2_135 = OM_2_234*RL_2_335-OM_2_334*RL_2_235
  OR_2_235 = -(OM_2_134*RL_2_335-OM_2_334*RL_2_135)
  OR_2_335 = OM_2_134*RL_2_235-OM_2_234*RL_2_135
  Ompqp_2_135 = Ompqp_2_134+qd[35]*(OM_2_234*RO_2_334-OM_2_334*RO_2_234)
  Ompqp_2_235 = Ompqp_2_234-qd[35]*(OM_2_134*RO_2_334-OM_2_334*RO_2_134)
  Ompqp_2_335 = Ompqp_2_334+qd[35]*(OM_2_134*RO_2_234-OM_2_234*RO_2_134)
  OR_2_136 = OM_2_235*RL_2_336-OM_2_335*RL_2_236
  OR_2_236 = -(OM_2_135*RL_2_336-OM_2_335*RL_2_136)
  OR_2_336 = OM_2_135*RL_2_236-OM_2_235*RL_2_136
  OR_2_141 = OM_2_235*RL_2_341-OM_2_335*RL_2_241
  OR_2_241 = -(OM_2_135*RL_2_341-OM_2_335*RL_2_141)
  OR_2_341 = OM_2_135*RL_2_241-OM_2_235*RL_2_141
  Apqp_2_141 = Apqp_2_133+OM_2_234*OR_2_335+OM_2_235*OR_2_336+OM_2_235*OR_2_341-OM_2_334*OR_2_235-OM_2_335*OR_2_236-\
   OM_2_335*OR_2_241+Ompqp_2_234*RL_2_335+Ompqp_2_235*RL_2_336+Ompqp_2_235*RL_2_341-Ompqp_2_334*RL_2_235-Ompqp_2_335*RL_2_236-\
   Ompqp_2_335*RL_2_241+(2.0)*qd[36]*(OM_2_235*RO_2_935-OM_2_335*RO_2_835)
  Apqp_2_241 = Apqp_2_233-OM_2_134*OR_2_335-OM_2_135*OR_2_336-OM_2_135*OR_2_341+OM_2_334*OR_2_135+OM_2_335*OR_2_136+\
   OM_2_335*OR_2_141-Ompqp_2_134*RL_2_335-Ompqp_2_135*RL_2_336-Ompqp_2_135*RL_2_341+Ompqp_2_334*RL_2_135+Ompqp_2_335*RL_2_136+\
   Ompqp_2_335*RL_2_141-(2.0)*qd[36]*(OM_2_135*RO_2_935-OM_2_335*RO_2_735)
  Apqp_2_341 = Apqp_2_333+OM_2_134*OR_2_235+OM_2_135*OR_2_236+OM_2_135*OR_2_241-OM_2_234*OR_2_135-OM_2_235*OR_2_136-\
   OM_2_235*OR_2_141+Ompqp_2_134*RL_2_235+Ompqp_2_135*RL_2_236+Ompqp_2_135*RL_2_241-Ompqp_2_234*RL_2_135-Ompqp_2_235*RL_2_136-\
   Ompqp_2_235*RL_2_141+(2.0)*qd[36]*(OM_2_135*RO_2_835-OM_2_235*RO_2_735)
#
  OM_4_216 = -qd[16]*S15
  OM_4_316 = qd[16]*C15
  OM_4_117 = qd[15]+qd[17]*C16
  OM_4_217 = OM_4_216+RO_4_216*qd[17]
  OM_4_317 = OM_4_316+RO_4_316*qd[17]
  OM_4_118 = OM_4_117+RO_4_417*qd[18]
  OM_4_218 = OM_4_217+RO_4_517*qd[18]
  OM_4_318 = OM_4_317+RO_4_617*qd[18]
  Ompqp_4_118 = -(qd[16]*qd[17]*S16-qd[18]*(OM_4_217*RO_4_617-OM_4_317*RO_4_517))
  Ompqp_4_218 = -(qd[15]*qd[16]*C15-qd[17]*(OM_4_316*C16-RO_4_316*qd[15])+qd[18]*(OM_4_117*RO_4_617-OM_4_317*RO_4_417))
  Ompqp_4_318 = -(qd[15]*qd[16]*S15+qd[17]*(OM_4_216*C16-RO_4_216*qd[15])-qd[18]*(OM_4_117*RO_4_517-OM_4_217*RO_4_417))
  OM_4_119 = OM_4_118+RO_4_118*qd[19]
  OM_4_219 = OM_4_218+RO_4_218*qd[19]
  OM_4_319 = OM_4_318+RO_4_318*qd[19]
  OR_4_119 = OM_4_218*RL_4_319-OM_4_318*RL_4_219
  OR_4_219 = -(OM_4_118*RL_4_319-OM_4_318*RL_4_119)
  OR_4_319 = OM_4_118*RL_4_219-OM_4_218*RL_4_119
  Ompqp_4_119 = Ompqp_4_118+qd[19]*(OM_4_218*RO_4_318-OM_4_318*RO_4_218)
  Ompqp_4_219 = Ompqp_4_218-qd[19]*(OM_4_118*RO_4_318-OM_4_318*RO_4_118)
  Ompqp_4_319 = Ompqp_4_318+qd[19]*(OM_4_118*RO_4_218-OM_4_218*RO_4_118)
  OR_4_120 = OM_4_219*RL_4_320-OM_4_319*RL_4_220
  OR_4_220 = -(OM_4_119*RL_4_320-OM_4_319*RL_4_120)
  OR_4_320 = OM_4_119*RL_4_220-OM_4_219*RL_4_120
  OR_4_143 = OM_4_219*RL_4_343-OM_4_319*RL_4_243
  OR_4_243 = -(OM_4_119*RL_4_343-OM_4_319*RL_4_143)
  OR_4_343 = OM_4_119*RL_4_243-OM_4_219*RL_4_143
  Apqp_4_143 = OM_4_218*OR_4_319+OM_4_219*OR_4_320+OM_4_219*OR_4_343-OM_4_318*OR_4_219-OM_4_319*OR_4_220-OM_4_319*\
   OR_4_243+Ompqp_4_218*RL_4_319+Ompqp_4_219*RL_4_320+Ompqp_4_219*RL_4_343-Ompqp_4_318*RL_4_219-Ompqp_4_319*RL_4_220-\
   Ompqp_4_319*RL_4_243+(2.0)*qd[20]*(OM_4_219*RO_4_919-OM_4_319*RO_4_819)
  Apqp_4_243 = -(OM_4_118*OR_4_319+OM_4_119*OR_4_320+OM_4_119*OR_4_343-OM_4_318*OR_4_119-OM_4_319*OR_4_120-OM_4_319*\
   OR_4_143+Ompqp_4_118*RL_4_319+Ompqp_4_119*RL_4_320+Ompqp_4_119*RL_4_343-Ompqp_4_318*RL_4_119-Ompqp_4_319*RL_4_120-\
   Ompqp_4_319*RL_4_143+qd[15]*qd[15]*s.dpt[2,18]*C15+(2.0)*qd[20]*(OM_4_119*RO_4_919-OM_4_319*RO_4_719))
  Apqp_4_343 = OM_4_118*OR_4_219+OM_4_119*OR_4_220+OM_4_119*OR_4_243-OM_4_218*OR_4_119-OM_4_219*OR_4_120-OM_4_219*\
   OR_4_143+Ompqp_4_118*RL_4_219+Ompqp_4_119*RL_4_220+Ompqp_4_119*RL_4_243-Ompqp_4_218*RL_4_119-Ompqp_4_219*RL_4_120-\
   Ompqp_4_219*RL_4_143-qd[15]*qd[15]*s.dpt[2,18]*S15+(2.0)*qd[20]*(OM_4_119*RO_4_819-OM_4_219*RO_4_719)
#
  OM_7_28 = -qd[8]*S7
  OM_7_38 = qd[8]*C7
  OM_7_19 = qd[7]+qd[9]*C8
  OM_7_29 = OM_7_28+RO_7_28*qd[9]
  OM_7_39 = OM_7_38+RO_7_38*qd[9]
  OM_7_110 = OM_7_19+RO_7_49*qd[10]
  OM_7_210 = OM_7_29+RO_7_59*qd[10]
  OM_7_310 = OM_7_39+RO_7_69*qd[10]
  Ompqp_7_110 = qd[10]*(OM_7_29*RO_7_69-OM_7_39*RO_7_59)-qd[8]*qd[9]*S8
  Ompqp_7_210 = -(qd[10]*(OM_7_19*RO_7_69-OM_7_39*RO_7_49)+qd[7]*qd[8]*C7-qd[9]*(OM_7_38*C8-RO_7_38*qd[7]))
  Ompqp_7_310 = qd[10]*(OM_7_19*RO_7_59-OM_7_29*RO_7_49)-qd[7]*qd[8]*S7-qd[9]*(OM_7_28*C8-RO_7_28*qd[7])
  OM_7_111 = OM_7_110+RO_7_110*qd[11]
  OM_7_211 = OM_7_210+RO_7_210*qd[11]
  OM_7_311 = OM_7_310+RO_7_310*qd[11]
  OR_7_111 = OM_7_210*RL_7_311-OM_7_310*RL_7_211
  OR_7_211 = -(OM_7_110*RL_7_311-OM_7_310*RL_7_111)
  OR_7_311 = OM_7_110*RL_7_211-OM_7_210*RL_7_111
  Ompqp_7_111 = Ompqp_7_110+qd[11]*(OM_7_210*RO_7_310-OM_7_310*RO_7_210)
  Ompqp_7_211 = Ompqp_7_210-qd[11]*(OM_7_110*RO_7_310-OM_7_310*RO_7_110)
  Ompqp_7_311 = Ompqp_7_310+qd[11]*(OM_7_110*RO_7_210-OM_7_210*RO_7_110)
  OR_7_112 = OM_7_211*RL_7_312-OM_7_311*RL_7_212
  OR_7_212 = -(OM_7_111*RL_7_312-OM_7_311*RL_7_112)
  OR_7_312 = OM_7_111*RL_7_212-OM_7_211*RL_7_112
  OR_7_146 = OM_7_211*RL_7_346-OM_7_311*RL_7_246
  OR_7_246 = -(OM_7_111*RL_7_346-OM_7_311*RL_7_146)
  OR_7_346 = OM_7_111*RL_7_246-OM_7_211*RL_7_146
  Apqp_7_146 = OM_7_210*OR_7_311+OM_7_211*OR_7_312+OM_7_211*OR_7_346-OM_7_310*OR_7_211-OM_7_311*OR_7_212-OM_7_311*\
   OR_7_246+Ompqp_7_210*RL_7_311+Ompqp_7_211*RL_7_312+Ompqp_7_211*RL_7_346-Ompqp_7_310*RL_7_211-Ompqp_7_311*RL_7_212-\
   Ompqp_7_311*RL_7_246+(2.0)*qd[12]*(OM_7_211*RO_7_911-OM_7_311*RO_7_811)
  Apqp_7_246 = -(OM_7_110*OR_7_311+OM_7_111*OR_7_312+OM_7_111*OR_7_346-OM_7_310*OR_7_111-OM_7_311*OR_7_112-OM_7_311*\
   OR_7_146+Ompqp_7_110*RL_7_311+Ompqp_7_111*RL_7_312+Ompqp_7_111*RL_7_346-Ompqp_7_310*RL_7_111-Ompqp_7_311*RL_7_112-\
   Ompqp_7_311*RL_7_146+(2.0)*qd[12]*(OM_7_111*RO_7_911-OM_7_311*RO_7_711)+qd[7]*qd[7]*s.dpt[2,13]*C7)
  Apqp_7_346 = OM_7_110*OR_7_211+OM_7_111*OR_7_212+OM_7_111*OR_7_246-OM_7_210*OR_7_111-OM_7_211*OR_7_112-OM_7_211*\
   OR_7_146+Ompqp_7_110*RL_7_211+Ompqp_7_111*RL_7_212+Ompqp_7_111*RL_7_246-Ompqp_7_210*RL_7_111-Ompqp_7_211*RL_7_112-\
   Ompqp_7_211*RL_7_146+(2.0)*qd[12]*(OM_7_111*RO_7_811-OM_7_211*RO_7_711)-qd[7]*qd[7]*s.dpt[2,13]*S7
#
  OR_9_148 = OM_1_226*RL_9_348-OM_1_326*RL_9_248
  OR_9_248 = -(OM_1_126*RL_9_348-OM_1_326*RL_9_148)
  OR_9_348 = OM_1_126*RL_9_248-OM_1_226*RL_9_148
  VI_9_148 = OR_1_125+OR_9_148
  VI_9_248 = OR_1_225+OR_9_248
  VI_9_348 = OR_1_325+OR_9_348
#
  OR_11_150 = OM_1_226*RL_11_350-OM_1_326*RL_11_250
  OR_11_250 = -(OM_1_126*RL_11_350-OM_1_326*RL_11_150)
  OR_11_350 = OM_1_126*RL_11_250-OM_1_226*RL_11_150
  VI_11_150 = OR_11_150+OR_1_125
  VI_11_250 = OR_11_250+OR_1_225
  VI_11_350 = OR_11_350+OR_1_325
#
  OR_12_151 = OM_2_234*RL_12_351-OM_2_334*RL_12_251
  OR_12_251 = -(OM_2_134*RL_12_351-OM_2_334*RL_12_151)
  OR_12_351 = OM_2_134*RL_12_251-OM_2_234*RL_12_151
  VI_12_151 = OR_12_151+OR_2_133
  VI_12_251 = OR_12_251+OR_2_233
  VI_12_351 = OR_12_351+OR_2_333
#
  OR_14_153 = OM_2_234*RL_14_353-OM_2_334*RL_14_253
  OR_14_253 = -(OM_2_134*RL_14_353-OM_2_334*RL_14_153)
  OR_14_353 = OM_2_134*RL_14_253-OM_2_234*RL_14_153
  VI_14_153 = OR_14_153+OR_2_133
  VI_14_253 = OR_14_253+OR_2_233
  VI_14_353 = OR_14_353+OR_2_333

# = = Block_0_2_0_0_0_1 = = 
 
# Constraints Quadratic Terms 

#
  jdqd13 = VI_9_148*VI_9_148+VI_9_248*VI_9_248+VI_9_348*VI_9_348+(Apqp_1_225-OM_1_126*OR_9_348+OM_1_326*OR_9_148-\
   Ompqp_1_126*RL_9_348+Ompqp_1_326*RL_9_148)*(PO_1_225+RL_9_248-s.dpt[2,9])+(PO_1_125+RL_9_148-s.dpt[1,9])*(Apqp_1_125+\
   OM_1_226*OR_9_348-OM_1_326*OR_9_248+Ompqp_1_226*RL_9_348-Ompqp_1_326*RL_9_248)+(RL_1_325+RL_9_348-s.dpt[3,9])*(Apqp_1_325+\
   OM_1_126*OR_9_248-OM_1_226*OR_9_148+Ompqp_1_126*RL_9_248-Ompqp_1_226*RL_9_148)
#
  jdqd14 = VI_11_150*VI_11_150+VI_11_250*VI_11_250+VI_11_350*VI_11_350+(Apqp_1_225-OM_1_126*OR_11_350+OM_1_326*OR_11_150\
   -Ompqp_1_126*RL_11_350+Ompqp_1_326*RL_11_150)*(PO_1_225+RL_11_250-s.dpt[2,6])+(PO_1_125+RL_11_150-s.dpt[1,6])*(Apqp_1_125+\
   OM_1_226*OR_11_350-OM_1_326*OR_11_250+Ompqp_1_226*RL_11_350-Ompqp_1_326*RL_11_250)+(RL_11_350+RL_1_325-s.dpt[3,6])*(\
   Apqp_1_325+OM_1_126*OR_11_250-OM_1_226*OR_11_150+Ompqp_1_126*RL_11_250-Ompqp_1_226*RL_11_150)
#
  jdqd15 = VI_12_151*VI_12_151+VI_12_251*VI_12_251+VI_12_351*VI_12_351+(Apqp_2_233-OM_2_134*OR_12_351+OM_2_334*OR_12_151\
   -Ompqp_2_134*RL_12_351+Ompqp_2_334*RL_12_151)*(PO_2_233+RL_12_251-s.dpt[2,11])+(PO_2_133+RL_12_151-s.dpt[1,11])*(Apqp_2_133+\
   OM_2_234*OR_12_351-OM_2_334*OR_12_251+Ompqp_2_234*RL_12_351-Ompqp_2_334*RL_12_251)+(RL_12_351+RL_2_333-s.dpt[3,11])*(\
   Apqp_2_333+OM_2_134*OR_12_251-OM_2_234*OR_12_151+Ompqp_2_134*RL_12_251-Ompqp_2_234*RL_12_151)
#
  jdqd16 = VI_14_153*VI_14_153+VI_14_253*VI_14_253+VI_14_353*VI_14_353+(Apqp_2_233-OM_2_134*OR_14_353+OM_2_334*OR_14_153\
   -Ompqp_2_134*RL_14_353+Ompqp_2_334*RL_14_153)*(PO_2_233+RL_14_253-s.dpt[2,8])+(PO_2_133+RL_14_153-s.dpt[1,8])*(Apqp_2_133+\
   OM_2_234*OR_14_353-OM_2_334*OR_14_253+Ompqp_2_234*RL_14_353-Ompqp_2_334*RL_14_253)+(RL_14_353+RL_2_333-s.dpt[3,8])*(\
   Apqp_2_333+OM_2_134*OR_14_253-OM_2_234*OR_14_153+Ompqp_2_134*RL_14_253-Ompqp_2_234*RL_14_153)

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  Jdqd[1] = -Apqp_1_140
  Jdqd[2] = -Apqp_1_240
  Jdqd[3] = -Apqp_1_340
  Jdqd[4] = Apqp_2_141
  Jdqd[5] = Apqp_2_241
  Jdqd[6] = Apqp_2_341
  Jdqd[7] = Apqp_4_143
  Jdqd[8] = Apqp_4_243
  Jdqd[9] = Apqp_4_343
  Jdqd[10] = -Apqp_7_146
  Jdqd[11] = -Apqp_7_246
  Jdqd[12] = -Apqp_7_346
  Jdqd[13] = jdqd13
  Jdqd[14] = jdqd14
  Jdqd[15] = jdqd15
  Jdqd[16] = jdqd16

# ====== END Task 0 ====== 

  
