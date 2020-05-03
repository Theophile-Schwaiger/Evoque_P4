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
#	==> Generation Date : Sat May  2 22:51:37 2020
#
#	==> Project name : Complete_Vehicle_New_Dimensions
#	==> using XML input file 
#
#	==> Number of joints : 65
#
#	==> Function : F18 : Constraints Quadratic Velocity Terms (Jdqd)
#	==> Flops complexity : 2254
#
#	==> Generation Time :  0.050 seconds
#	==> Post-Processing :  0.050 seconds
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
#
  RL_17_183 = RO_7_110*s.dpt[1,19]+RO_7_49*s.dpt[2,19]
  RL_17_283 = RO_7_210*s.dpt[1,19]+RO_7_59*s.dpt[2,19]
  RL_17_383 = RO_7_310*s.dpt[1,19]+RO_7_69*s.dpt[2,19]
#
  RL_25_191 = RO_7_110*s.dpt[1,20]+RO_7_49*s.dpt[2,20]+RO_7_710*s.dpt[3,20]
  RL_25_291 = RO_7_210*s.dpt[1,20]+RO_7_59*s.dpt[2,20]+RO_7_810*s.dpt[3,20]
  RL_25_391 = RO_7_310*s.dpt[1,20]+RO_7_69*s.dpt[2,20]+RO_7_910*s.dpt[3,20]

# = = Block_0_1_0_0_0_3 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_7_711 = -(RO_7_49*S11-RO_7_710*C11)
  RO_7_811 = -(RO_7_59*S11-RO_7_810*C11)
  RO_7_911 = -(RO_7_69*S11-RO_7_910*C11)
  RL_7_111 = RO_7_49*s.dpt[2,17]+RO_7_710*s.dpt[3,17]
  RL_7_211 = RO_7_59*s.dpt[2,17]+RO_7_810*s.dpt[3,17]
  RL_7_311 = RO_7_69*s.dpt[2,17]+RO_7_910*s.dpt[3,17]
  RL_7_112 = RO_7_711*q[12]
  RL_7_212 = RO_7_811*q[12]
  RL_7_312 = RO_7_911*q[12]
  RL_7_173 = RO_7_711*s.dpt[3,21]
  RL_7_273 = RO_7_811*s.dpt[3,21]
  RL_7_373 = RO_7_911*s.dpt[3,21]

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
#
  RL_18_184 = RO_4_118*s.dpt[1,26]+RO_4_417*s.dpt[2,26]
  RL_18_284 = RO_4_218*s.dpt[1,26]+RO_4_517*s.dpt[2,26]
  RL_18_384 = RO_4_318*s.dpt[1,26]+RO_4_617*s.dpt[2,26]
#
  RL_27_193 = RO_4_118*s.dpt[1,27]+RO_4_417*s.dpt[2,27]+RO_4_718*s.dpt[3,27]
  RL_27_293 = RO_4_218*s.dpt[1,27]+RO_4_517*s.dpt[2,27]+RO_4_818*s.dpt[3,27]
  RL_27_393 = RO_4_318*s.dpt[1,27]+RO_4_617*s.dpt[2,27]+RO_4_918*s.dpt[3,27]

# = = Block_0_1_0_0_0_6 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_4_719 = -(RO_4_417*S19-RO_4_718*C19)
  RO_4_819 = -(RO_4_517*S19-RO_4_818*C19)
  RO_4_919 = -(RO_4_617*S19-RO_4_918*C19)
  RL_4_119 = RO_4_417*s.dpt[2,24]+RO_4_718*s.dpt[3,24]
  RL_4_219 = RO_4_517*s.dpt[2,24]+RO_4_818*s.dpt[3,24]
  RL_4_319 = RO_4_617*s.dpt[2,24]+RO_4_918*s.dpt[3,24]
  RL_4_120 = RO_4_719*q[20]
  RL_4_220 = RO_4_819*q[20]
  RL_4_320 = RO_4_919*q[20]
  RL_4_170 = RO_4_719*s.dpt[3,28]
  RL_4_270 = RO_4_819*s.dpt[3,28]
  RL_4_370 = RO_4_919*s.dpt[3,28]

# = = Block_0_1_0_0_0_8 = = 
 
# Constraints and Constraints Jacobian 

#
  RL_8_174 = -s.dpt[2,30]*S24
  RL_8_274 = s.dpt[2,30]*C23*C24
  RL_8_374 = s.dpt[2,30]*S23*C24

# = = Block_0_1_0_0_0_9 = = 
 
# Constraints and Constraints Jacobian 

#
  RL_11_177 = -s.dpt[2,31]*S26
  RL_11_277 = s.dpt[2,31]*C25*C26
  RL_11_377 = s.dpt[2,31]*S25*C26

# = = Block_0_1_0_0_0_10 = = 
 
# Constraints and Constraints Jacobian 

#
  RL_12_178 = -s.dpt[2,32]*S28
  RL_12_278 = s.dpt[2,32]*C27*C28
  RL_12_378 = s.dpt[2,32]*S27*C28

# = = Block_0_1_0_0_0_11 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_1_230 = C29*S30
  RO_1_330 = S29*S30
  RO_1_530 = C29*C30
  RO_1_630 = S29*C30
  RO_1_431 = -S30*C31
  RO_1_531 = RO_1_530*C31-S29*S31
  RO_1_631 = RO_1_630*C31+C29*S31
  RO_1_731 = S30*S31
  RO_1_831 = -(RO_1_530*S31+S29*C31)
  RO_1_931 = -(RO_1_630*S31-C29*C31)
  RO_1_132 = -(RO_1_731*S32-C30*C32)
  RO_1_232 = RO_1_230*C32-RO_1_831*S32
  RO_1_332 = RO_1_330*C32-RO_1_931*S32
  RO_1_732 = RO_1_731*C32+C30*S32
  RO_1_832 = RO_1_230*S32+RO_1_831*C32
  RO_1_932 = RO_1_330*S32+RO_1_931*C32
  RO_1_133 = RO_1_132*C33+RO_1_431*S33
  RO_1_233 = RO_1_232*C33+RO_1_531*S33
  RO_1_333 = RO_1_332*C33+RO_1_631*S33
  RO_1_433 = -(RO_1_132*S33-RO_1_431*C33)
  RO_1_533 = -(RO_1_232*S33-RO_1_531*C33)
  RO_1_633 = -(RO_1_332*S33-RO_1_631*C33)
  RL_1_131 = -s.dpt[2,33]*S30
  RL_1_231 = RO_1_530*s.dpt[2,33]
  RL_1_331 = RO_1_630*s.dpt[2,33]
#
  RL_9_175 = RO_1_133*s.dpt[1,36]+RO_1_732*s.dpt[3,36]
  RL_9_275 = RO_1_233*s.dpt[1,36]+RO_1_832*s.dpt[3,36]
  RL_9_375 = RO_1_333*s.dpt[1,36]+RO_1_932*s.dpt[3,36]
#
  RL_13_179 = RO_1_133*s.dpt[1,37]+RO_1_732*s.dpt[3,37]
  RL_13_279 = RO_1_233*s.dpt[1,37]+RO_1_832*s.dpt[3,37]
  RL_13_379 = RO_1_333*s.dpt[1,37]+RO_1_932*s.dpt[3,37]
#
  RL_23_189 = RO_1_133*s.dpt[1,38]+RO_1_433*s.dpt[2,38]+RO_1_732*s.dpt[3,38]
  RL_23_289 = RO_1_233*s.dpt[1,38]+RO_1_533*s.dpt[2,38]+RO_1_832*s.dpt[3,38]
  RL_23_389 = RO_1_333*s.dpt[1,38]+RO_1_633*s.dpt[2,38]+RO_1_932*s.dpt[3,38]

# = = Block_0_1_0_0_0_12 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_1_734 = -(RO_1_433*S34-RO_1_732*C34)
  RO_1_834 = -(RO_1_533*S34-RO_1_832*C34)
  RO_1_934 = -(RO_1_633*S34-RO_1_932*C34)
  RL_1_134 = RO_1_433*s.dpt[2,34]+RO_1_732*s.dpt[3,34]
  RL_1_234 = RO_1_533*s.dpt[2,34]+RO_1_832*s.dpt[3,34]
  RL_1_334 = RO_1_633*s.dpt[2,34]+RO_1_932*s.dpt[3,34]
  RL_1_135 = RO_1_734*q[35]
  RL_1_235 = RO_1_834*q[35]
  RL_1_335 = RO_1_934*q[35]
  RL_1_167 = RO_1_734*s.dpt[3,39]
  RL_1_267 = RO_1_834*s.dpt[3,39]
  RL_1_367 = RO_1_934*s.dpt[3,39]

# = = Block_0_1_0_0_0_14 = = 
 
# Constraints and Constraints Jacobian 

#
  RL_14_180 = -s.dpt[2,41]*S39
  RL_14_280 = s.dpt[2,41]*C38*C39
  RL_14_380 = s.dpt[2,41]*S38*C39

# = = Block_0_1_0_0_0_15 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_2_241 = C40*S41
  RO_2_341 = S40*S41
  RO_2_541 = C40*C41
  RO_2_641 = S40*C41
  RO_2_442 = -S41*C42
  RO_2_542 = RO_2_541*C42-S40*S42
  RO_2_642 = RO_2_641*C42+C40*S42
  RO_2_742 = S41*S42
  RO_2_842 = -(RO_2_541*S42+S40*C42)
  RO_2_942 = -(RO_2_641*S42-C40*C42)
  RO_2_143 = -(RO_2_742*S43-C41*C43)
  RO_2_243 = RO_2_241*C43-RO_2_842*S43
  RO_2_343 = RO_2_341*C43-RO_2_942*S43
  RO_2_743 = RO_2_742*C43+C41*S43
  RO_2_843 = RO_2_241*S43+RO_2_842*C43
  RO_2_943 = RO_2_341*S43+RO_2_942*C43
  RO_2_144 = RO_2_143*C44+RO_2_442*S44
  RO_2_244 = RO_2_243*C44+RO_2_542*S44
  RO_2_344 = RO_2_343*C44+RO_2_642*S44
  RO_2_444 = -(RO_2_143*S44-RO_2_442*C44)
  RO_2_544 = -(RO_2_243*S44-RO_2_542*C44)
  RO_2_644 = -(RO_2_343*S44-RO_2_642*C44)
  RL_2_142 = -s.dpt[2,42]*S41
  RL_2_242 = RO_2_541*s.dpt[2,42]
  RL_2_342 = RO_2_641*s.dpt[2,42]
#
  RL_10_176 = RO_2_144*s.dpt[1,44]+RO_2_743*s.dpt[3,44]
  RL_10_276 = RO_2_244*s.dpt[1,44]+RO_2_843*s.dpt[3,44]
  RL_10_376 = RO_2_344*s.dpt[1,44]+RO_2_943*s.dpt[3,44]
#
  RL_15_181 = RO_2_144*s.dpt[1,43]+RO_2_743*s.dpt[3,43]
  RL_15_281 = RO_2_244*s.dpt[1,43]+RO_2_843*s.dpt[3,43]
  RL_15_381 = RO_2_344*s.dpt[1,43]+RO_2_943*s.dpt[3,43]
#
  RL_21_187 = RO_2_144*s.dpt[1,47]+RO_2_444*s.dpt[2,47]+RO_2_743*s.dpt[3,47]
  RL_21_287 = RO_2_244*s.dpt[1,47]+RO_2_544*s.dpt[2,47]+RO_2_843*s.dpt[3,47]
  RL_21_387 = RO_2_344*s.dpt[1,47]+RO_2_644*s.dpt[2,47]+RO_2_943*s.dpt[3,47]

# = = Block_0_1_0_0_0_16 = = 
 
# Constraints and Constraints Jacobian 

#
  RO_2_745 = -(RO_2_444*S45-RO_2_743*C45)
  RO_2_845 = -(RO_2_544*S45-RO_2_843*C45)
  RO_2_945 = -(RO_2_644*S45-RO_2_943*C45)
  RL_2_145 = RO_2_444*s.dpt[2,45]+RO_2_743*s.dpt[3,45]
  RL_2_245 = RO_2_544*s.dpt[2,45]+RO_2_843*s.dpt[3,45]
  RL_2_345 = RO_2_644*s.dpt[2,45]+RO_2_943*s.dpt[3,45]
  RL_2_146 = RO_2_745*q[46]
  RL_2_246 = RO_2_845*q[46]
  RL_2_346 = RO_2_945*q[46]
  RL_2_168 = RO_2_745*s.dpt[3,48]
  RL_2_268 = RO_2_845*s.dpt[3,48]
  RL_2_368 = RO_2_945*s.dpt[3,48]

# = = Block_0_1_0_0_0_19 = = 
 
# Constraints and Constraints Jacobian 

#
  RL_16_182 = -s.dpt[2,52]*S50*C51
  RL_16_282 = s.dpt[2,52]*C50*C51
  RL_16_382 = s.dpt[2,52]*S51

# = = Block_0_1_0_0_0_20 = = 
 
# Constraints and Constraints Jacobian 

#
  RL_19_185 = -s.dpt[2,53]*S52*C53
  RL_19_285 = s.dpt[2,53]*C52*C53
  RL_19_385 = s.dpt[2,53]*S53

# = = Block_0_1_0_0_0_22 = = 
 
# Trigonometric Variables  

#
  S54p55 = C54*S55+S54*C55
  C54p55 = C54*C55-S54*S55
  S54p55p56 = C54p55*S56+S54p55*C56
  C54p55p56 = C54p55*C56-S54p55*S56
 
# Constraints and Constraints Jacobian 

  RL_20_186 = s.dpt[3,56]*S54p55p56*C57
  RL_20_286 = -s.dpt[3,56]*S57
  RL_20_386 = s.dpt[3,56]*C54p55p56*C57

# = = Block_0_1_0_0_0_23 = = 
 
# Trigonometric Variables  

#
  S54p58 = C54*S58+S54*C58
  C54p58 = C54*C58-S54*S58
 
# Constraints and Constraints Jacobian 

  RL_22_188 = s.dpt[3,57]*S54p58*C59
  RL_22_288 = -s.dpt[3,57]*S59
  RL_22_388 = s.dpt[3,57]*C54p58*C59

# = = Block_0_1_0_0_0_25 = = 
 
# Trigonometric Variables  

#
  S60p61 = C60*S61+S60*C61
  C60p61 = C60*C61-S60*S61
  S60p61p62 = C60p61*S62+S60p61*C62
  C60p61p62 = C60p61*C62-S60p61*S62
 
# Constraints and Constraints Jacobian 

  RL_26_192 = s.dpt[3,60]*S60p61p62*C63
  RL_26_292 = -s.dpt[3,60]*S63
  RL_26_392 = s.dpt[3,60]*C60p61p62*C63

# = = Block_0_1_0_0_0_26 = = 
 
# Trigonometric Variables  

#
  S60p64 = C60*S64+S60*C64
  C60p64 = C60*C64-S60*S64
 
# Constraints and Constraints Jacobian 

  RL_24_190 = s.dpt[3,61]*S60p64*C65
  RL_24_290 = -s.dpt[3,61]*S65
  RL_24_390 = s.dpt[3,61]*C60p64*C65

# = = Block_0_2_0_0_0_0 = = 
 
# Constraints Quadratic Terms 

#
  OM_1_230 = -qd[30]*S29
  OM_1_330 = qd[30]*C29
  Ompqp_1_230 = -qd[29]*qd[30]*C29
  Ompqp_1_330 = -qd[29]*qd[30]*S29
  OM_1_131 = qd[29]+qd[31]*C30
  OM_1_231 = OM_1_230+RO_1_230*qd[31]
  OM_1_331 = OM_1_330+RO_1_330*qd[31]
  OR_1_131 = -qd[30]*s.dpt[2,33]*C30
  OR_1_231 = OM_1_330*RL_1_131-RL_1_331*qd[29]
  OR_1_331 = -(OM_1_230*RL_1_131-RL_1_231*qd[29])
  Apqp_1_131 = OM_1_230*OR_1_331-OM_1_330*OR_1_231+Ompqp_1_230*RL_1_331-Ompqp_1_330*RL_1_231
  Apqp_1_231 = OM_1_330*OR_1_131-OR_1_331*qd[29]+Ompqp_1_330*RL_1_131
  Apqp_1_331 = -(OM_1_230*OR_1_131-OR_1_231*qd[29]+Ompqp_1_230*RL_1_131)
  OM_1_132 = OM_1_131+RO_1_431*qd[32]
  OM_1_232 = OM_1_231+RO_1_531*qd[32]
  OM_1_332 = OM_1_331+RO_1_631*qd[32]
  OM_1_133 = OM_1_132+RO_1_732*qd[33]
  OM_1_233 = OM_1_232+RO_1_832*qd[33]
  OM_1_333 = OM_1_332+RO_1_932*qd[33]
  Ompqp_1_133 = -(qd[30]*qd[31]*S30-qd[32]*(OM_1_231*RO_1_631-OM_1_331*RO_1_531)-qd[33]*(OM_1_232*RO_1_932-OM_1_332*\
   RO_1_832))
  Ompqp_1_233 = Ompqp_1_230+qd[31]*(OM_1_330*C30-RO_1_330*qd[29])-qd[32]*(OM_1_131*RO_1_631-OM_1_331*RO_1_431)-qd[33]*(\
   OM_1_132*RO_1_932-OM_1_332*RO_1_732)
  Ompqp_1_333 = Ompqp_1_330-qd[31]*(OM_1_230*C30-RO_1_230*qd[29])+qd[32]*(OM_1_131*RO_1_531-OM_1_231*RO_1_431)+qd[33]*(\
   OM_1_132*RO_1_832-OM_1_232*RO_1_732)
  OM_1_134 = OM_1_133+RO_1_133*qd[34]
  OM_1_234 = OM_1_233+RO_1_233*qd[34]
  OM_1_334 = OM_1_333+RO_1_333*qd[34]
  OR_1_134 = OM_1_233*RL_1_334-OM_1_333*RL_1_234
  OR_1_234 = -(OM_1_133*RL_1_334-OM_1_333*RL_1_134)
  OR_1_334 = OM_1_133*RL_1_234-OM_1_233*RL_1_134
  Ompqp_1_134 = Ompqp_1_133+qd[34]*(OM_1_233*RO_1_333-OM_1_333*RO_1_233)
  Ompqp_1_234 = Ompqp_1_233-qd[34]*(OM_1_133*RO_1_333-OM_1_333*RO_1_133)
  Ompqp_1_334 = Ompqp_1_333+qd[34]*(OM_1_133*RO_1_233-OM_1_233*RO_1_133)
  OR_1_135 = OM_1_234*RL_1_335-OM_1_334*RL_1_235
  OR_1_235 = -(OM_1_134*RL_1_335-OM_1_334*RL_1_135)
  OR_1_335 = OM_1_134*RL_1_235-OM_1_234*RL_1_135
  OR_1_167 = OM_1_234*RL_1_367-OM_1_334*RL_1_267
  OR_1_267 = -(OM_1_134*RL_1_367-OM_1_334*RL_1_167)
  OR_1_367 = OM_1_134*RL_1_267-OM_1_234*RL_1_167
  Apqp_1_167 = Apqp_1_131+OM_1_233*OR_1_334+OM_1_234*OR_1_335+OM_1_234*OR_1_367-OM_1_333*OR_1_234-OM_1_334*OR_1_235-\
   OM_1_334*OR_1_267+Ompqp_1_233*RL_1_334+Ompqp_1_234*RL_1_335+Ompqp_1_234*RL_1_367-Ompqp_1_333*RL_1_234-Ompqp_1_334*RL_1_235-\
   Ompqp_1_334*RL_1_267+(2.0)*qd[35]*(OM_1_234*RO_1_934-OM_1_334*RO_1_834)
  Apqp_1_267 = Apqp_1_231-OM_1_133*OR_1_334-OM_1_134*OR_1_335-OM_1_134*OR_1_367+OM_1_333*OR_1_134+OM_1_334*OR_1_135+\
   OM_1_334*OR_1_167-Ompqp_1_133*RL_1_334-Ompqp_1_134*RL_1_335-Ompqp_1_134*RL_1_367+Ompqp_1_333*RL_1_134+Ompqp_1_334*RL_1_135+\
   Ompqp_1_334*RL_1_167-(2.0)*qd[35]*(OM_1_134*RO_1_934-OM_1_334*RO_1_734)
  Apqp_1_367 = Apqp_1_331+OM_1_133*OR_1_234+OM_1_134*OR_1_235+OM_1_134*OR_1_267-OM_1_233*OR_1_134-OM_1_234*OR_1_135-\
   OM_1_234*OR_1_167+Ompqp_1_133*RL_1_234+Ompqp_1_134*RL_1_235+Ompqp_1_134*RL_1_267-Ompqp_1_233*RL_1_134-Ompqp_1_234*RL_1_135-\
   Ompqp_1_234*RL_1_167+(2.0)*qd[35]*(OM_1_134*RO_1_834-OM_1_234*RO_1_734)
#
  OM_2_241 = -qd[41]*S40
  OM_2_341 = qd[41]*C40
  Ompqp_2_241 = -qd[40]*qd[41]*C40
  Ompqp_2_341 = -qd[40]*qd[41]*S40
  OM_2_142 = qd[40]+qd[42]*C41
  OM_2_242 = OM_2_241+RO_2_241*qd[42]
  OM_2_342 = OM_2_341+RO_2_341*qd[42]
  OR_2_142 = -qd[41]*s.dpt[2,42]*C41
  OR_2_242 = OM_2_341*RL_2_142-RL_2_342*qd[40]
  OR_2_342 = -(OM_2_241*RL_2_142-RL_2_242*qd[40])
  Apqp_2_142 = OM_2_241*OR_2_342-OM_2_341*OR_2_242+Ompqp_2_241*RL_2_342-Ompqp_2_341*RL_2_242
  Apqp_2_242 = OM_2_341*OR_2_142-OR_2_342*qd[40]+Ompqp_2_341*RL_2_142
  Apqp_2_342 = -(OM_2_241*OR_2_142-OR_2_242*qd[40]+Ompqp_2_241*RL_2_142)
  OM_2_143 = OM_2_142+RO_2_442*qd[43]
  OM_2_243 = OM_2_242+RO_2_542*qd[43]
  OM_2_343 = OM_2_342+RO_2_642*qd[43]
  OM_2_144 = OM_2_143+RO_2_743*qd[44]
  OM_2_244 = OM_2_243+RO_2_843*qd[44]
  OM_2_344 = OM_2_343+RO_2_943*qd[44]
  Ompqp_2_144 = -(qd[41]*qd[42]*S41-qd[43]*(OM_2_242*RO_2_642-OM_2_342*RO_2_542)-qd[44]*(OM_2_243*RO_2_943-OM_2_343*\
   RO_2_843))
  Ompqp_2_244 = Ompqp_2_241+qd[42]*(OM_2_341*C41-RO_2_341*qd[40])-qd[43]*(OM_2_142*RO_2_642-OM_2_342*RO_2_442)-qd[44]*(\
   OM_2_143*RO_2_943-OM_2_343*RO_2_743)
  Ompqp_2_344 = Ompqp_2_341-qd[42]*(OM_2_241*C41-RO_2_241*qd[40])+qd[43]*(OM_2_142*RO_2_542-OM_2_242*RO_2_442)+qd[44]*(\
   OM_2_143*RO_2_843-OM_2_243*RO_2_743)
  OM_2_145 = OM_2_144+RO_2_144*qd[45]
  OM_2_245 = OM_2_244+RO_2_244*qd[45]
  OM_2_345 = OM_2_344+RO_2_344*qd[45]
  OR_2_145 = OM_2_244*RL_2_345-OM_2_344*RL_2_245
  OR_2_245 = -(OM_2_144*RL_2_345-OM_2_344*RL_2_145)
  OR_2_345 = OM_2_144*RL_2_245-OM_2_244*RL_2_145
  Ompqp_2_145 = Ompqp_2_144+qd[45]*(OM_2_244*RO_2_344-OM_2_344*RO_2_244)
  Ompqp_2_245 = Ompqp_2_244-qd[45]*(OM_2_144*RO_2_344-OM_2_344*RO_2_144)
  Ompqp_2_345 = Ompqp_2_344+qd[45]*(OM_2_144*RO_2_244-OM_2_244*RO_2_144)
  OR_2_146 = OM_2_245*RL_2_346-OM_2_345*RL_2_246
  OR_2_246 = -(OM_2_145*RL_2_346-OM_2_345*RL_2_146)
  OR_2_346 = OM_2_145*RL_2_246-OM_2_245*RL_2_146
  OR_2_168 = OM_2_245*RL_2_368-OM_2_345*RL_2_268
  OR_2_268 = -(OM_2_145*RL_2_368-OM_2_345*RL_2_168)
  OR_2_368 = OM_2_145*RL_2_268-OM_2_245*RL_2_168
  Apqp_2_168 = Apqp_2_142+OM_2_244*OR_2_345+OM_2_245*OR_2_346+OM_2_245*OR_2_368-OM_2_344*OR_2_245-OM_2_345*OR_2_246-\
   OM_2_345*OR_2_268+Ompqp_2_244*RL_2_345+Ompqp_2_245*RL_2_346+Ompqp_2_245*RL_2_368-Ompqp_2_344*RL_2_245-Ompqp_2_345*RL_2_246-\
   Ompqp_2_345*RL_2_268+(2.0)*qd[46]*(OM_2_245*RO_2_945-OM_2_345*RO_2_845)
  Apqp_2_268 = Apqp_2_242-OM_2_144*OR_2_345-OM_2_145*OR_2_346-OM_2_145*OR_2_368+OM_2_344*OR_2_145+OM_2_345*OR_2_146+\
   OM_2_345*OR_2_168-Ompqp_2_144*RL_2_345-Ompqp_2_145*RL_2_346-Ompqp_2_145*RL_2_368+Ompqp_2_344*RL_2_145+Ompqp_2_345*RL_2_146+\
   Ompqp_2_345*RL_2_168-(2.0)*qd[46]*(OM_2_145*RO_2_945-OM_2_345*RO_2_745)
  Apqp_2_368 = Apqp_2_342+OM_2_144*OR_2_245+OM_2_145*OR_2_246+OM_2_145*OR_2_268-OM_2_244*OR_2_145-OM_2_245*OR_2_146-\
   OM_2_245*OR_2_168+Ompqp_2_144*RL_2_245+Ompqp_2_145*RL_2_246+Ompqp_2_145*RL_2_268-Ompqp_2_244*RL_2_145-Ompqp_2_245*RL_2_146-\
   Ompqp_2_245*RL_2_168+(2.0)*qd[46]*(OM_2_145*RO_2_845-OM_2_245*RO_2_745)
#
  OM_4_216 = -qd[16]*S15
  OM_4_316 = qd[16]*C15
  Apqp_4_216 = -qd[15]*qd[15]*s.dpt[2,23]*C15
  Apqp_4_316 = -qd[15]*qd[15]*s.dpt[2,23]*S15
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
  OR_4_170 = OM_4_219*RL_4_370-OM_4_319*RL_4_270
  OR_4_270 = -(OM_4_119*RL_4_370-OM_4_319*RL_4_170)
  OR_4_370 = OM_4_119*RL_4_270-OM_4_219*RL_4_170
  Apqp_4_170 = OM_4_218*OR_4_319+OM_4_219*OR_4_320+OM_4_219*OR_4_370-OM_4_318*OR_4_219-OM_4_319*OR_4_220-OM_4_319*\
   OR_4_270+Ompqp_4_218*RL_4_319+Ompqp_4_219*RL_4_320+Ompqp_4_219*RL_4_370-Ompqp_4_318*RL_4_219-Ompqp_4_319*RL_4_220-\
   Ompqp_4_319*RL_4_270+(2.0)*qd[20]*(OM_4_219*RO_4_919-OM_4_319*RO_4_819)
  Apqp_4_270 = Apqp_4_216-OM_4_118*OR_4_319-OM_4_119*OR_4_320-OM_4_119*OR_4_370+OM_4_318*OR_4_119+OM_4_319*OR_4_120+\
   OM_4_319*OR_4_170-Ompqp_4_118*RL_4_319-Ompqp_4_119*RL_4_320-Ompqp_4_119*RL_4_370+Ompqp_4_318*RL_4_119+Ompqp_4_319*RL_4_120+\
   Ompqp_4_319*RL_4_170-(2.0)*qd[20]*(OM_4_119*RO_4_919-OM_4_319*RO_4_719)
  Apqp_4_370 = Apqp_4_316+OM_4_118*OR_4_219+OM_4_119*OR_4_220+OM_4_119*OR_4_270-OM_4_218*OR_4_119-OM_4_219*OR_4_120-\
   OM_4_219*OR_4_170+Ompqp_4_118*RL_4_219+Ompqp_4_119*RL_4_220+Ompqp_4_119*RL_4_270-Ompqp_4_218*RL_4_119-Ompqp_4_219*RL_4_120-\
   Ompqp_4_219*RL_4_170+(2.0)*qd[20]*(OM_4_119*RO_4_819-OM_4_219*RO_4_719)
#
  OM_7_28 = -qd[8]*S7
  OM_7_38 = qd[8]*C7
  Apqp_7_28 = -qd[7]*qd[7]*s.dpt[2,16]*C7
  Apqp_7_38 = -qd[7]*qd[7]*s.dpt[2,16]*S7
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
  OR_7_173 = OM_7_211*RL_7_373-OM_7_311*RL_7_273
  OR_7_273 = -(OM_7_111*RL_7_373-OM_7_311*RL_7_173)
  OR_7_373 = OM_7_111*RL_7_273-OM_7_211*RL_7_173
  Apqp_7_173 = OM_7_210*OR_7_311+OM_7_211*OR_7_312+OM_7_211*OR_7_373-OM_7_310*OR_7_211-OM_7_311*OR_7_212-OM_7_311*\
   OR_7_273+Ompqp_7_210*RL_7_311+Ompqp_7_211*RL_7_312+Ompqp_7_211*RL_7_373-Ompqp_7_310*RL_7_211-Ompqp_7_311*RL_7_212-\
   Ompqp_7_311*RL_7_273+(2.0)*qd[12]*(OM_7_211*RO_7_911-OM_7_311*RO_7_811)
  Apqp_7_273 = Apqp_7_28-OM_7_110*OR_7_311-OM_7_111*OR_7_312-OM_7_111*OR_7_373+OM_7_310*OR_7_111+OM_7_311*OR_7_112+\
   OM_7_311*OR_7_173-Ompqp_7_110*RL_7_311-Ompqp_7_111*RL_7_312-Ompqp_7_111*RL_7_373+Ompqp_7_310*RL_7_111+Ompqp_7_311*RL_7_112+\
   Ompqp_7_311*RL_7_173-(2.0)*qd[12]*(OM_7_111*RO_7_911-OM_7_311*RO_7_711)
  Apqp_7_373 = Apqp_7_38+OM_7_110*OR_7_211+OM_7_111*OR_7_212+OM_7_111*OR_7_273-OM_7_210*OR_7_111-OM_7_211*OR_7_112-\
   OM_7_211*OR_7_173+Ompqp_7_110*RL_7_211+Ompqp_7_111*RL_7_212+Ompqp_7_111*RL_7_273-Ompqp_7_210*RL_7_111-Ompqp_7_211*RL_7_112-\
   Ompqp_7_211*RL_7_173+(2.0)*qd[12]*(OM_7_111*RO_7_811-OM_7_211*RO_7_711)
#
  OM_8_224 = -qd[24]*S23
  OM_8_324 = qd[24]*C23
  Ompqp_8_224 = -qd[23]*qd[24]*C23
  Ompqp_8_324 = -qd[23]*qd[24]*S23
  OR_8_174 = -qd[24]*s.dpt[2,30]*C24
  OR_8_274 = OM_8_324*RL_8_174-RL_8_374*qd[23]
  OR_8_374 = -(OM_8_224*RL_8_174-RL_8_274*qd[23])
#
  OR_9_175 = OM_1_233*RL_9_375-OM_1_333*RL_9_275
  OR_9_275 = -(OM_1_133*RL_9_375-OM_1_333*RL_9_175)
  OR_9_375 = OM_1_133*RL_9_275-OM_1_233*RL_9_175
#
  OR_10_176 = OM_2_244*RL_10_376-OM_2_344*RL_10_276
  OR_10_276 = -(OM_2_144*RL_10_376-OM_2_344*RL_10_176)
  OR_10_376 = OM_2_144*RL_10_276-OM_2_244*RL_10_176
#
  OM_11_226 = -qd[26]*S25
  OM_11_326 = qd[26]*C25
  Ompqp_11_226 = -qd[25]*qd[26]*C25
  Ompqp_11_326 = -qd[25]*qd[26]*S25
  OR_11_177 = -qd[26]*s.dpt[2,31]*C26
  OR_11_277 = OM_11_326*RL_11_177-RL_11_377*qd[25]
  OR_11_377 = -(OM_11_226*RL_11_177-RL_11_277*qd[25])
#
  OM_12_228 = -qd[28]*S27
  OM_12_328 = qd[28]*C27
  Ompqp_12_228 = -qd[27]*qd[28]*C27
  Ompqp_12_328 = -qd[27]*qd[28]*S27
  OR_12_178 = -qd[28]*s.dpt[2,32]*C28
  OR_12_278 = OM_12_328*RL_12_178-RL_12_378*qd[27]
  OR_12_378 = -(OM_12_228*RL_12_178-RL_12_278*qd[27])
#
  OR_13_179 = OM_1_233*RL_13_379-OM_1_333*RL_13_279
  OR_13_279 = -(OM_1_133*RL_13_379-OM_1_333*RL_13_179)
  OR_13_379 = OM_1_133*RL_13_279-OM_1_233*RL_13_179
#
  OM_14_239 = -qd[39]*S38
  OM_14_339 = qd[39]*C38
  Ompqp_14_239 = -qd[38]*qd[39]*C38
  Ompqp_14_339 = -qd[38]*qd[39]*S38
  OR_14_180 = -qd[39]*s.dpt[2,41]*C39
  OR_14_280 = OM_14_339*RL_14_180-RL_14_380*qd[38]
  OR_14_380 = -(OM_14_239*RL_14_180-RL_14_280*qd[38])
#
  OR_15_181 = OM_2_244*RL_15_381-OM_2_344*RL_15_281
  OR_15_281 = -(OM_2_144*RL_15_381-OM_2_344*RL_15_181)
  OR_15_381 = OM_2_144*RL_15_281-OM_2_244*RL_15_181
#
  OM_16_151 = qd[51]*C50
  OM_16_251 = qd[51]*S50
  Ompqp_16_151 = -qd[50]*qd[51]*S50
  Ompqp_16_251 = qd[50]*qd[51]*C50
  OR_16_182 = OM_16_251*RL_16_382-RL_16_282*qd[50]
  OR_16_282 = -(OM_16_151*RL_16_382-RL_16_182*qd[50])
  OR_16_382 = qd[51]*s.dpt[2,52]*C51
#
  OR_17_183 = OM_7_210*RL_17_383-OM_7_310*RL_17_283
  OR_17_283 = -(OM_7_110*RL_17_383-OM_7_310*RL_17_183)
  OR_17_383 = OM_7_110*RL_17_283-OM_7_210*RL_17_183
#
  OR_18_184 = OM_4_218*RL_18_384-OM_4_318*RL_18_284
  OR_18_284 = -(OM_4_118*RL_18_384-OM_4_318*RL_18_184)
  OR_18_384 = OM_4_118*RL_18_284-OM_4_218*RL_18_184
#
  OM_19_153 = qd[53]*C52
  OM_19_253 = qd[53]*S52
  Ompqp_19_153 = -qd[52]*qd[53]*S52
  Ompqp_19_253 = qd[52]*qd[53]*C52
  OR_19_185 = OM_19_253*RL_19_385-RL_19_285*qd[52]
  OR_19_285 = -(OM_19_153*RL_19_385-RL_19_185*qd[52])
  OR_19_385 = qd[53]*s.dpt[2,53]*C53
#
  OM_20_255 = qd[54]+qd[55]
  OM_20_256 = OM_20_255+qd[56]
  OM_20_157 = qd[57]*C54p55p56
  OM_20_357 = -qd[57]*S54p55p56
  Ompqp_20_157 = -OM_20_256*qd[57]*S54p55p56
  Ompqp_20_357 = -OM_20_256*qd[57]*C54p55p56
  OR_20_186 = OM_20_256*RL_20_386-OM_20_357*RL_20_286
  OR_20_286 = -qd[57]*s.dpt[3,56]*C57
  OR_20_386 = OM_20_157*RL_20_286-OM_20_256*RL_20_186
#
  OR_21_187 = OM_2_244*RL_21_387-OM_2_344*RL_21_287
  OR_21_287 = -(OM_2_144*RL_21_387-OM_2_344*RL_21_187)
  OR_21_387 = OM_2_144*RL_21_287-OM_2_244*RL_21_187
#
  OM_22_258 = qd[54]+qd[58]
  OM_22_159 = qd[59]*C54p58
  OM_22_359 = -qd[59]*S54p58
  Ompqp_22_159 = -OM_22_258*qd[59]*S54p58
  Ompqp_22_359 = -OM_22_258*qd[59]*C54p58
  OR_22_188 = OM_22_258*RL_22_388-OM_22_359*RL_22_288
  OR_22_288 = -qd[59]*s.dpt[3,57]*C59
  OR_22_388 = OM_22_159*RL_22_288-OM_22_258*RL_22_188
#
  OR_23_189 = OM_1_233*RL_23_389-OM_1_333*RL_23_289
  OR_23_289 = -(OM_1_133*RL_23_389-OM_1_333*RL_23_189)
  OR_23_389 = OM_1_133*RL_23_289-OM_1_233*RL_23_189
#
  OM_24_264 = qd[60]+qd[64]
  OM_24_165 = qd[65]*C60p64
  OM_24_365 = -qd[65]*S60p64
  Ompqp_24_165 = -OM_24_264*qd[65]*S60p64
  Ompqp_24_365 = -OM_24_264*qd[65]*C60p64
  OR_24_190 = OM_24_264*RL_24_390-OM_24_365*RL_24_290
  OR_24_290 = -qd[65]*s.dpt[3,61]*C65
  OR_24_390 = OM_24_165*RL_24_290-OM_24_264*RL_24_190
#
  OR_25_191 = OM_7_210*RL_25_391-OM_7_310*RL_25_291
  OR_25_291 = -(OM_7_110*RL_25_391-OM_7_310*RL_25_191)
  OR_25_391 = OM_7_110*RL_25_291-OM_7_210*RL_25_191
#
  OM_26_261 = qd[60]+qd[61]
  OM_26_262 = OM_26_261+qd[62]
  OM_26_163 = qd[63]*C60p61p62
  OM_26_363 = -qd[63]*S60p61p62
  Ompqp_26_163 = -OM_26_262*qd[63]*S60p61p62
  Ompqp_26_363 = -OM_26_262*qd[63]*C60p61p62
  OR_26_192 = OM_26_262*RL_26_392-OM_26_363*RL_26_292
  OR_26_292 = -qd[63]*s.dpt[3,60]*C63
  OR_26_392 = OM_26_163*RL_26_292-OM_26_262*RL_26_192
#
  OR_27_193 = OM_4_218*RL_27_393-OM_4_318*RL_27_293
  OR_27_293 = -(OM_4_118*RL_27_393-OM_4_318*RL_27_193)
  OR_27_393 = OM_4_118*RL_27_293-OM_4_218*RL_27_193

# = = Block_0_2_0_0_0_1 = = 
 
# Constraints Quadratic Terms 

#
  jdqd13 = OM_8_224*OR_8_374-OM_8_324*OR_8_274+Ompqp_8_224*RL_8_374-Ompqp_8_324*RL_8_274-(Apqp_1_131+OM_1_233*OR_9_375-\
   OM_1_333*OR_9_275+Ompqp_1_233*RL_9_375-Ompqp_1_333*RL_9_275)
  jdqd14 = OM_8_324*OR_8_174-OR_8_374*qd[23]+Ompqp_8_324*RL_8_174-(Apqp_1_231-OM_1_133*OR_9_375+OM_1_333*OR_9_175-\
   Ompqp_1_133*RL_9_375+Ompqp_1_333*RL_9_175)
  jdqd15 = -(Apqp_1_331+OM_1_133*OR_9_275-OM_1_233*OR_9_175+OM_8_224*OR_8_174-OR_8_274*qd[23]+Ompqp_1_133*RL_9_275-\
   Ompqp_1_233*RL_9_175+Ompqp_8_224*RL_8_174)
#
  jdqd16 = Apqp_2_142-OM_11_226*OR_11_377+OM_11_326*OR_11_277+OM_2_244*OR_10_376-OM_2_344*OR_10_276-Ompqp_11_226*\
   RL_11_377+Ompqp_11_326*RL_11_277+Ompqp_2_244*RL_10_376-Ompqp_2_344*RL_10_276
  jdqd17 = Apqp_2_242-OM_11_326*OR_11_177-OM_2_144*OR_10_376+OM_2_344*OR_10_176+OR_11_377*qd[25]-Ompqp_11_326*RL_11_177-\
   Ompqp_2_144*RL_10_376+Ompqp_2_344*RL_10_176
  jdqd18 = Apqp_2_342+OM_11_226*OR_11_177+OM_2_144*OR_10_276-OM_2_244*OR_10_176-OR_11_277*qd[25]+Ompqp_11_226*RL_11_177+\
   Ompqp_2_144*RL_10_276-Ompqp_2_244*RL_10_176
#
  jdqd19 = OM_12_228*OR_12_378-OM_12_328*OR_12_278+Ompqp_12_228*RL_12_378-Ompqp_12_328*RL_12_278-(Apqp_1_131+OM_1_233*\
   OR_13_379-OM_1_333*OR_13_279+Ompqp_1_233*RL_13_379-Ompqp_1_333*RL_13_279)
  jdqd20 = OM_12_328*OR_12_178-OR_12_378*qd[27]+Ompqp_12_328*RL_12_178-(Apqp_1_231-OM_1_133*OR_13_379+OM_1_333*OR_13_179\
   -Ompqp_1_133*RL_13_379+Ompqp_1_333*RL_13_179)
  jdqd21 = -(Apqp_1_331+OM_12_228*OR_12_178+OM_1_133*OR_13_279-OM_1_233*OR_13_179-OR_12_278*qd[27]+Ompqp_12_228*\
   RL_12_178+Ompqp_1_133*RL_13_279-Ompqp_1_233*RL_13_179)
#
  jdqd22 = OM_14_239*OR_14_380-OM_14_339*OR_14_280+Ompqp_14_239*RL_14_380-Ompqp_14_339*RL_14_280-(Apqp_2_142+OM_2_244*\
   OR_15_381-OM_2_344*OR_15_281+Ompqp_2_244*RL_15_381-Ompqp_2_344*RL_15_281)
  jdqd23 = OM_14_339*OR_14_180-OR_14_380*qd[38]+Ompqp_14_339*RL_14_180-(Apqp_2_242-OM_2_144*OR_15_381+OM_2_344*OR_15_181\
   -Ompqp_2_144*RL_15_381+Ompqp_2_344*RL_15_181)
  jdqd24 = -(Apqp_2_342+OM_14_239*OR_14_180+OM_2_144*OR_15_281-OM_2_244*OR_15_181-OR_14_280*qd[38]+Ompqp_14_239*\
   RL_14_180+Ompqp_2_144*RL_15_281-Ompqp_2_244*RL_15_181)
#
  jdqd25 = OM_16_251*OR_16_382-OM_7_210*OR_17_383+OM_7_310*OR_17_283-OR_16_282*qd[50]+Ompqp_16_251*RL_16_382-Ompqp_7_210\
   *RL_17_383+Ompqp_7_310*RL_17_283
  jdqd26 = -(Apqp_7_28+OM_16_151*OR_16_382-OM_7_110*OR_17_383+OM_7_310*OR_17_183-OR_16_182*qd[50]+Ompqp_16_151*RL_16_382\
   -Ompqp_7_110*RL_17_383+Ompqp_7_310*RL_17_183)
  jdqd27 = OM_16_151*OR_16_282-OM_16_251*OR_16_182+Ompqp_16_151*RL_16_282-Ompqp_16_251*RL_16_182-(Apqp_7_38+OM_7_110*\
   OR_17_283-OM_7_210*OR_17_183+Ompqp_7_110*RL_17_283-Ompqp_7_210*RL_17_183)
#
  jdqd28 = OM_4_218*OR_18_384-OM_4_318*OR_18_284+Ompqp_4_218*RL_18_384-Ompqp_4_318*RL_18_284-(OM_19_253*OR_19_385-\
   OR_19_285*qd[52]+Ompqp_19_253*RL_19_385)
  jdqd29 = Apqp_4_216+OM_19_153*OR_19_385-OM_4_118*OR_18_384+OM_4_318*OR_18_184-OR_19_185*qd[52]+Ompqp_19_153*RL_19_385-\
   Ompqp_4_118*RL_18_384+Ompqp_4_318*RL_18_184
  jdqd30 = Apqp_4_316-OM_19_153*OR_19_285+OM_19_253*OR_19_185+OM_4_118*OR_18_284-OM_4_218*OR_18_184-Ompqp_19_153*\
   RL_19_285+Ompqp_19_253*RL_19_185+Ompqp_4_118*RL_18_284-Ompqp_4_218*RL_18_184
#
  jdqd31 = -(Apqp_2_142+OM_20_255*OM_20_255*s.dpt[1,55]*C54p55-OM_20_256*OR_20_386+OM_20_357*OR_20_286+OM_2_244*\
   OR_21_387-OM_2_344*OR_21_287+Ompqp_20_357*RL_20_286+Ompqp_2_244*RL_21_387-Ompqp_2_344*RL_21_287)
  jdqd32 = -(Apqp_2_242+OM_20_157*OR_20_386-OM_20_357*OR_20_186-OM_2_144*OR_21_387+OM_2_344*OR_21_187+Ompqp_20_157*\
   RL_20_386-Ompqp_20_357*RL_20_186-Ompqp_2_144*RL_21_387+Ompqp_2_344*RL_21_187)
  jdqd33 = OM_20_157*OR_20_286+OM_20_255*OM_20_255*s.dpt[1,55]*S54p55-OM_20_256*OR_20_186+Ompqp_20_157*RL_20_286-(\
   Apqp_2_342+OM_2_144*OR_21_287-OM_2_244*OR_21_187+Ompqp_2_144*RL_21_287-Ompqp_2_244*RL_21_187)
#
  jdqd34 = OM_22_258*OR_22_388-OM_22_359*OR_22_288-Ompqp_22_359*RL_22_288-qd[54]*qd[54]*s.dpt[1,54]*C54-(Apqp_1_131+\
   OM_1_233*OR_23_389-OM_1_333*OR_23_289+Ompqp_1_233*RL_23_389-Ompqp_1_333*RL_23_289)
  jdqd35 = -(Apqp_1_231-OM_1_133*OR_23_389+OM_1_333*OR_23_189+OM_22_159*OR_22_388-OM_22_359*OR_22_188-Ompqp_1_133*\
   RL_23_389+Ompqp_1_333*RL_23_189+Ompqp_22_159*RL_22_388-Ompqp_22_359*RL_22_188)
  jdqd36 = OM_22_159*OR_22_288-OM_22_258*OR_22_188+Ompqp_22_159*RL_22_288+qd[54]*qd[54]*s.dpt[1,54]*S54-(Apqp_1_331+\
   OM_1_133*OR_23_289-OM_1_233*OR_23_189+Ompqp_1_133*RL_23_289-Ompqp_1_233*RL_23_189)
#
  jdqd37 = OM_24_264*OR_24_390-OM_24_365*OR_24_290-OM_7_210*OR_25_391+OM_7_310*OR_25_291-Ompqp_24_365*RL_24_290-\
   Ompqp_7_210*RL_25_391+Ompqp_7_310*RL_25_291-qd[60]*qd[60]*s.dpt[1,58]*C60
  jdqd38 = -(Apqp_7_28+OM_24_165*OR_24_390-OM_24_365*OR_24_190-OM_7_110*OR_25_391+OM_7_310*OR_25_191+Ompqp_24_165*\
   RL_24_390-Ompqp_24_365*RL_24_190-Ompqp_7_110*RL_25_391+Ompqp_7_310*RL_25_191)
  jdqd39 = OM_24_165*OR_24_290-OM_24_264*OR_24_190+Ompqp_24_165*RL_24_290+qd[60]*qd[60]*s.dpt[1,58]*S60-(Apqp_7_38+\
   OM_7_110*OR_25_291-OM_7_210*OR_25_191+Ompqp_7_110*RL_25_291-Ompqp_7_210*RL_25_191)
#
  jdqd40 = -(OM_26_261*OM_26_261*s.dpt[1,59]*C60p61-OM_26_262*OR_26_392+OM_26_363*OR_26_292+OM_4_218*OR_27_393-OM_4_318*\
   OR_27_293+Ompqp_26_363*RL_26_292+Ompqp_4_218*RL_27_393-Ompqp_4_318*RL_27_293)
  jdqd41 = -(Apqp_4_216+OM_26_163*OR_26_392-OM_26_363*OR_26_192-OM_4_118*OR_27_393+OM_4_318*OR_27_193+Ompqp_26_163*\
   RL_26_392-Ompqp_26_363*RL_26_192-Ompqp_4_118*RL_27_393+Ompqp_4_318*RL_27_193)
  jdqd42 = OM_26_163*OR_26_292+OM_26_261*OM_26_261*s.dpt[1,59]*S60p61-OM_26_262*OR_26_192+Ompqp_26_163*RL_26_292-(\
   Apqp_4_316+OM_4_118*OR_27_293-OM_4_218*OR_27_193+Ompqp_4_118*RL_27_293-Ompqp_4_218*RL_27_193)

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  Jdqd[1] = -Apqp_1_167
  Jdqd[2] = -Apqp_1_267
  Jdqd[3] = -Apqp_1_367
  Jdqd[4] = Apqp_2_168
  Jdqd[5] = Apqp_2_268
  Jdqd[6] = Apqp_2_368
  Jdqd[7] = Apqp_4_170
  Jdqd[8] = Apqp_4_270
  Jdqd[9] = Apqp_4_370
  Jdqd[10] = -Apqp_7_173
  Jdqd[11] = -Apqp_7_273
  Jdqd[12] = -Apqp_7_373
  Jdqd[13] = jdqd13
  Jdqd[14] = jdqd14
  Jdqd[15] = jdqd15
  Jdqd[16] = jdqd16
  Jdqd[17] = jdqd17
  Jdqd[18] = jdqd18
  Jdqd[19] = jdqd19
  Jdqd[20] = jdqd20
  Jdqd[21] = jdqd21
  Jdqd[22] = jdqd22
  Jdqd[23] = jdqd23
  Jdqd[24] = jdqd24
  Jdqd[25] = jdqd25
  Jdqd[26] = jdqd26
  Jdqd[27] = jdqd27
  Jdqd[28] = jdqd28
  Jdqd[29] = jdqd29
  Jdqd[30] = jdqd30
  Jdqd[31] = jdqd31
  Jdqd[32] = jdqd32
  Jdqd[33] = jdqd33
  Jdqd[34] = jdqd34
  Jdqd[35] = jdqd35
  Jdqd[36] = jdqd36
  Jdqd[37] = jdqd37
  Jdqd[38] = jdqd38
  Jdqd[39] = jdqd39
  Jdqd[40] = jdqd40
  Jdqd[41] = jdqd41
  Jdqd[42] = jdqd42

# ====== END Task 0 ====== 

  

