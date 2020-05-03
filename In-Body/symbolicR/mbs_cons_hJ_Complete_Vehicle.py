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
#	==> Generation Date : Sun Mar 29 20:34:01 2020
#
#	==> Project name : Complete_Vehicle
#	==> using XML input file 
#
#	==> Number of joints : 38
#
#	==> Function : F 8 : Constraints Vector (h) and Jacobian Matrix (Jac) 
#	==> Flops complexity : 1028
#
#	==> Generation Time :  0.030 seconds
#	==> Post-Processing :  0.020 seconds
#
#-------------------------------------------------------------
#
import numpy as np  

def cons_hJ(h,Jac,s):   
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
  RL_7_28 = s.dpt[2,13]*C7
  RL_7_38 = s.dpt[2,13]*S7

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
  JT_7_246_7 = -(RL_7_311+RL_7_312+RL_7_346+RL_7_38)
  JT_7_346_7 = RL_7_211+RL_7_212+RL_7_246+RL_7_28
  JT_7_146_8 = -(RL_7_346*S7+C7*(RL_7_211+RL_7_212+RL_7_246)+S7*(RL_7_311+RL_7_312))
  JT_7_246_8 = C7*(RL_7_111+RL_7_112+RL_7_146)
  JT_7_346_8 = S7*(RL_7_111+RL_7_112+RL_7_146)
  JT_7_146_9 = RO_7_28*(RL_7_311+RL_7_312)-RO_7_38*(RL_7_211+RL_7_212)-RL_7_246*RO_7_38+RL_7_346*RO_7_28
  JT_7_246_9 = -(RL_7_346*C8-RO_7_38*(RL_7_111+RL_7_112+RL_7_146)+C8*(RL_7_311+RL_7_312))
  JT_7_346_9 = RL_7_246*C8-RO_7_28*(RL_7_111+RL_7_112+RL_7_146)+C8*(RL_7_211+RL_7_212)
  JT_7_146_10 = RO_7_59*(RL_7_311+RL_7_312)-RO_7_69*(RL_7_211+RL_7_212)-RL_7_246*RO_7_69+RL_7_346*RO_7_59
  JT_7_246_10 = RL_7_146*RO_7_69-RL_7_346*RO_7_49-RO_7_49*(RL_7_311+RL_7_312)+RO_7_69*(RL_7_111+RL_7_112)
  JT_7_346_10 = RO_7_49*(RL_7_211+RL_7_212)-RO_7_59*(RL_7_111+RL_7_112)-RL_7_146*RO_7_59+RL_7_246*RO_7_49
  JT_7_146_11 = RO_7_210*(RL_7_312+RL_7_346)-RO_7_310*(RL_7_212+RL_7_246)
  JT_7_246_11 = -(RO_7_110*(RL_7_312+RL_7_346)-RO_7_310*(RL_7_112+RL_7_146))
  JT_7_346_11 = RO_7_110*(RL_7_212+RL_7_246)-RO_7_210*(RL_7_112+RL_7_146)

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
  RL_4_216 = s.dpt[2,18]*C15
  RL_4_316 = s.dpt[2,18]*S15

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
  JT_4_243_15 = -(RL_4_316+RL_4_319+RL_4_320+RL_4_343)
  JT_4_343_15 = RL_4_216+RL_4_219+RL_4_220+RL_4_243
  JT_4_143_16 = -(RL_4_343*S15+C15*(RL_4_219+RL_4_220+RL_4_243)+S15*(RL_4_319+RL_4_320))
  JT_4_243_16 = C15*(RL_4_119+RL_4_120+RL_4_143)
  JT_4_343_16 = S15*(RL_4_119+RL_4_120+RL_4_143)
  JT_4_143_17 = RO_4_216*(RL_4_319+RL_4_320)-RO_4_316*(RL_4_219+RL_4_220)-RL_4_243*RO_4_316+RL_4_343*RO_4_216
  JT_4_243_17 = -(RL_4_343*C16-RO_4_316*(RL_4_119+RL_4_120+RL_4_143)+C16*(RL_4_319+RL_4_320))
  JT_4_343_17 = RL_4_243*C16-RO_4_216*(RL_4_119+RL_4_120+RL_4_143)+C16*(RL_4_219+RL_4_220)
  JT_4_143_18 = RO_4_517*(RL_4_319+RL_4_320)-RO_4_617*(RL_4_219+RL_4_220)-RL_4_243*RO_4_617+RL_4_343*RO_4_517
  JT_4_243_18 = RL_4_143*RO_4_617-RL_4_343*RO_4_417-RO_4_417*(RL_4_319+RL_4_320)+RO_4_617*(RL_4_119+RL_4_120)
  JT_4_343_18 = RO_4_417*(RL_4_219+RL_4_220)-RO_4_517*(RL_4_119+RL_4_120)-RL_4_143*RO_4_517+RL_4_243*RO_4_417
  JT_4_143_19 = RO_4_218*(RL_4_320+RL_4_343)-RO_4_318*(RL_4_220+RL_4_243)
  JT_4_243_19 = -(RO_4_118*(RL_4_320+RL_4_343)-RO_4_318*(RL_4_120+RL_4_143))
  JT_4_343_19 = RO_4_118*(RL_4_220+RL_4_243)-RO_4_218*(RL_4_120+RL_4_143)

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
  JT_1_125_24 = -s.dpt[2,23]*C24
  JT_1_225_24 = RL_1_125*C23
  JT_1_325_24 = RL_1_125*S23
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
  JT_1_240_23 = -(RL_1_325+RL_1_327+RL_1_328+RL_1_340)
  JT_1_340_23 = RL_1_225+RL_1_227+RL_1_228+RL_1_240
  JT_1_140_24 = JT_1_125_24-RL_1_227*C23-RL_1_228*C23-RL_1_240*C23-RL_1_327*S23-RL_1_328*S23-RL_1_340*S23
  JT_1_240_24 = JT_1_225_24+RL_1_127*C23+RL_1_128*C23+RL_1_140*C23
  JT_1_340_24 = JT_1_325_24+RL_1_127*S23+RL_1_128*S23+RL_1_140*S23
  JT_1_140_25 = RO_1_224*(RL_1_327+RL_1_328)-RO_1_324*(RL_1_227+RL_1_228)-RL_1_240*RO_1_324+RL_1_340*RO_1_224
  JT_1_240_25 = -(RL_1_340*C24-RO_1_324*(RL_1_127+RL_1_128+RL_1_140)+C24*(RL_1_327+RL_1_328))
  JT_1_340_25 = RL_1_240*C24-RO_1_224*(RL_1_127+RL_1_128+RL_1_140)+C24*(RL_1_227+RL_1_228)
  JT_1_140_26 = RO_1_825*(RL_1_327+RL_1_328)-RO_1_925*(RL_1_227+RL_1_228)-RL_1_240*RO_1_925+RL_1_340*RO_1_825
  JT_1_240_26 = RL_1_140*RO_1_925-RL_1_340*RO_1_725-RO_1_725*(RL_1_327+RL_1_328)+RO_1_925*(RL_1_127+RL_1_128)
  JT_1_340_26 = RO_1_725*(RL_1_227+RL_1_228)-RO_1_825*(RL_1_127+RL_1_128)-RL_1_140*RO_1_825+RL_1_240*RO_1_725
  JT_1_140_27 = RO_1_226*(RL_1_328+RL_1_340)-RO_1_326*(RL_1_228+RL_1_240)
  JT_1_240_27 = -(RO_1_126*(RL_1_328+RL_1_340)-RO_1_326*(RL_1_128+RL_1_140))
  JT_1_340_27 = RO_1_126*(RL_1_228+RL_1_240)-RO_1_226*(RL_1_128+RL_1_140)

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
  JT_2_133_32 = -s.dpt[2,30]*C32
  JT_2_233_32 = RL_2_133*C31
  JT_2_333_32 = RL_2_133*S31
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
  JT_2_241_31 = -(RL_2_333+RL_2_335+RL_2_336+RL_2_341)
  JT_2_341_31 = RL_2_233+RL_2_235+RL_2_236+RL_2_241
  JT_2_141_32 = JT_2_133_32-RL_2_235*C31-RL_2_236*C31-RL_2_241*C31-RL_2_335*S31-RL_2_336*S31-RL_2_341*S31
  JT_2_241_32 = JT_2_233_32+RL_2_135*C31+RL_2_136*C31+RL_2_141*C31
  JT_2_341_32 = JT_2_333_32+RL_2_135*S31+RL_2_136*S31+RL_2_141*S31
  JT_2_141_33 = RO_2_232*(RL_2_335+RL_2_336)-RO_2_332*(RL_2_235+RL_2_236)-RL_2_241*RO_2_332+RL_2_341*RO_2_232
  JT_2_241_33 = -(RL_2_341*C32-RO_2_332*(RL_2_135+RL_2_136+RL_2_141)+C32*(RL_2_335+RL_2_336))
  JT_2_341_33 = RL_2_241*C32-RO_2_232*(RL_2_135+RL_2_136+RL_2_141)+C32*(RL_2_235+RL_2_236)
  JT_2_141_34 = RO_2_833*(RL_2_335+RL_2_336)-RO_2_933*(RL_2_235+RL_2_236)-RL_2_241*RO_2_933+RL_2_341*RO_2_833
  JT_2_241_34 = RL_2_141*RO_2_933-RL_2_341*RO_2_733-RO_2_733*(RL_2_335+RL_2_336)+RO_2_933*(RL_2_135+RL_2_136)
  JT_2_341_34 = RO_2_733*(RL_2_235+RL_2_236)-RO_2_833*(RL_2_135+RL_2_136)-RL_2_141*RO_2_833+RL_2_241*RO_2_733
  JT_2_141_35 = RO_2_234*(RL_2_336+RL_2_341)-RO_2_334*(RL_2_236+RL_2_241)
  JT_2_241_35 = -(RO_2_134*(RL_2_336+RL_2_341)-RO_2_334*(RL_2_136+RL_2_141))
  JT_2_341_35 = RO_2_134*(RL_2_236+RL_2_241)-RO_2_234*(RL_2_136+RL_2_141)

# = = Block_0_1_0_0_1_0 = = 
 
# Constraints and Constraints Jacobian 

#
  h_1 = -(PO_1_125+RL_1_127+RL_1_128+RL_1_140-s.dpt[1,5])
  h_2 = -(PO_1_225+RL_1_227+RL_1_228+RL_1_240-s.dpt[2,5])
  h_3 = -(RL_1_325+RL_1_327+RL_1_328+RL_1_340-s.dpt[3,5])
#
  h_4 = PO_2_133+RL_2_135+RL_2_136+RL_2_141-s.dpt[1,7]
  h_5 = PO_2_233+RL_2_235+RL_2_236+RL_2_241-s.dpt[2,7]
  h_6 = RL_2_333+RL_2_335+RL_2_336+RL_2_341-s.dpt[3,7]
#
  h_7 = RL_4_119+RL_4_120+RL_4_143-s.dpt[1,2]+s.dpt[1,4]
  h_8 = RL_4_216+RL_4_219+RL_4_220+RL_4_243-s.dpt[2,2]+s.dpt[2,4]
  h_9 = RL_4_316+RL_4_319+RL_4_320+RL_4_343-s.dpt[3,2]+s.dpt[3,4]
#
  h_10 = -(RL_7_111+RL_7_112+RL_7_146+s.dpt[1,1]-s.dpt[1,3])
  h_11 = -(RL_7_211+RL_7_212+RL_7_246+RL_7_28+s.dpt[2,1]-s.dpt[2,3])
  h_12 = -(RL_7_311+RL_7_312+RL_7_346+RL_7_38+s.dpt[3,1]-s.dpt[3,3])
#
  Plp11 = -(PO_1_125+RL_9_148-s.dpt[1,9])
  Plp21 = -(PO_1_225+RL_9_248-s.dpt[2,9])
  Plp31 = -(RL_1_325+RL_9_348-s.dpt[3,9])
  h_13 = (0.50)*(Plp11*Plp11+Plp21*Plp21+Plp31*Plp31-s.lrod[1]*s.lrod[1])
#
  Jacu_13_23 = Plp21*(RL_1_325+RL_9_348)-Plp31*(RL_1_225+RL_9_248)
  Jac_13_24 = -(Plp11*(JT_1_125_24-RL_9_248*C23-RL_9_348*S23)+Plp21*(JT_1_225_24+RL_9_148*C23)+Plp31*(JT_1_325_24+\
   RL_9_148*S23))
  Jac_13_25 = Plp11*(RL_9_248*RO_1_324-RL_9_348*RO_1_224)-Plp21*(RL_9_148*RO_1_324-RL_9_348*C24)+Plp31*(RL_9_148*\
   RO_1_224-RL_9_248*C24)
  Jac_13_26 = Plp11*(RL_9_248*RO_1_925-RL_9_348*RO_1_825)-Plp21*(RL_9_148*RO_1_925-RL_9_348*RO_1_725)+Plp31*(RL_9_148*\
   RO_1_825-RL_9_248*RO_1_725)
#
  Plp12 = -(PO_1_125+RL_11_150-s.dpt[1,6])
  Plp22 = -(PO_1_225+RL_11_250-s.dpt[2,6])
  Plp32 = -(RL_11_350+RL_1_325-s.dpt[3,6])
  h_14 = (0.50)*(Plp12*Plp12+Plp22*Plp22+Plp32*Plp32-s.lrod[2]*s.lrod[2])
#
  Jacu_14_23 = Plp22*(RL_11_350+RL_1_325)-Plp32*(RL_11_250+RL_1_225)
  Jac_14_24 = -(Plp12*(JT_1_125_24-RL_11_250*C23-RL_11_350*S23)+Plp22*(JT_1_225_24+RL_11_150*C23)+Plp32*(JT_1_325_24+\
   RL_11_150*S23))
  Jac_14_25 = Plp12*(RL_11_250*RO_1_324-RL_11_350*RO_1_224)-Plp22*(RL_11_150*RO_1_324-RL_11_350*C24)+Plp32*(RL_11_150*\
   RO_1_224-RL_11_250*C24)
  Jac_14_26 = Plp12*(RL_11_250*RO_1_925-RL_11_350*RO_1_825)-Plp22*(RL_11_150*RO_1_925-RL_11_350*RO_1_725)+Plp32*(\
   RL_11_150*RO_1_825-RL_11_250*RO_1_725)
#
  Plp13 = PO_2_133+RL_12_151-s.dpt[1,11]
  Plp23 = PO_2_233+RL_12_251-s.dpt[2,11]
  Plp33 = RL_12_351+RL_2_333-s.dpt[3,11]
  h_15 = (0.50)*(Plp13*Plp13+Plp23*Plp23+Plp33*Plp33-s.lrod[3]*s.lrod[3])
#
  Jacu_15_31 = (RL_12_251+RL_2_233)*Plp33-Plp23*(RL_12_351+RL_2_333)
  Jac_15_32 = Plp13*(JT_2_133_32-RL_12_251*C31-RL_12_351*S31)+Plp23*(JT_2_233_32+RL_12_151*C31)+Plp33*(JT_2_333_32+\
   RL_12_151*S31)
  Jac_15_33 = -(Plp13*(RL_12_251*RO_2_332-RL_12_351*RO_2_232)-Plp23*(RL_12_151*RO_2_332-RL_12_351*C32)+Plp33*(RL_12_151*\
   RO_2_232-RL_12_251*C32))
  Jac_15_34 = -(Plp13*(RL_12_251*RO_2_933-RL_12_351*RO_2_833)-Plp23*(RL_12_151*RO_2_933-RL_12_351*RO_2_733)+Plp33*(\
   RL_12_151*RO_2_833-RL_12_251*RO_2_733))
#
  Plp14 = PO_2_133+RL_14_153-s.dpt[1,8]
  Plp24 = PO_2_233+RL_14_253-s.dpt[2,8]
  Plp34 = RL_14_353+RL_2_333-s.dpt[3,8]
  h_16 = (0.50)*(Plp14*Plp14+Plp24*Plp24+Plp34*Plp34-s.lrod[4]*s.lrod[4])
#
  Jacu_16_31 = (RL_14_253+RL_2_233)*Plp34-Plp24*(RL_14_353+RL_2_333)
  Jac_16_32 = Plp14*(JT_2_133_32-RL_14_253*C31-RL_14_353*S31)+Plp24*(JT_2_233_32+RL_14_153*C31)+Plp34*(JT_2_333_32+\
   RL_14_153*S31)
  Jac_16_33 = -(Plp14*(RL_14_253*RO_2_332-RL_14_353*RO_2_232)-Plp24*(RL_14_153*RO_2_332-RL_14_353*C32)+Plp34*(RL_14_153*\
   RO_2_232-RL_14_253*C32))
  Jac_16_34 = -(Plp14*(RL_14_253*RO_2_933-RL_14_353*RO_2_833)-Plp24*(RL_14_153*RO_2_933-RL_14_353*RO_2_733)+Plp34*(\
   RL_14_153*RO_2_833-RL_14_253*RO_2_733))

# = = Block_0_3_0_0_0_0 = = 
 
# Symbolic Outputs  

  h[1] = h_1
  h[2] = h_2
  h[3] = h_3
  h[4] = h_4
  h[5] = h_5
  h[6] = h_6
  h[7] = h_7
  h[8] = h_8
  h[9] = h_9
  h[10] = h_10
  h[11] = h_11
  h[12] = h_12
  h[13] = h_13
  h[14] = h_14
  h[15] = h_15
  h[16] = h_16
  Jac[1,24] = -JT_1_140_24
  Jac[1,25] = -JT_1_140_25
  Jac[1,26] = -JT_1_140_26
  Jac[1,27] = -JT_1_140_27
  Jac[1,28] = -RO_1_727
  Jac[2,23] = -JT_1_240_23
  Jac[2,24] = -JT_1_240_24
  Jac[2,25] = -JT_1_240_25
  Jac[2,26] = -JT_1_240_26
  Jac[2,27] = -JT_1_240_27
  Jac[2,28] = -RO_1_827
  Jac[3,23] = -JT_1_340_23
  Jac[3,24] = -JT_1_340_24
  Jac[3,25] = -JT_1_340_25
  Jac[3,26] = -JT_1_340_26
  Jac[3,27] = -JT_1_340_27
  Jac[3,28] = -RO_1_927
  Jac[4,32] = JT_2_141_32
  Jac[4,33] = JT_2_141_33
  Jac[4,34] = JT_2_141_34
  Jac[4,35] = JT_2_141_35
  Jac[4,36] = RO_2_735
  Jac[5,31] = JT_2_241_31
  Jac[5,32] = JT_2_241_32
  Jac[5,33] = JT_2_241_33
  Jac[5,34] = JT_2_241_34
  Jac[5,35] = JT_2_241_35
  Jac[5,36] = RO_2_835
  Jac[6,31] = JT_2_341_31
  Jac[6,32] = JT_2_341_32
  Jac[6,33] = JT_2_341_33
  Jac[6,34] = JT_2_341_34
  Jac[6,35] = JT_2_341_35
  Jac[6,36] = RO_2_935
  Jac[7,16] = JT_4_143_16
  Jac[7,17] = JT_4_143_17
  Jac[7,18] = JT_4_143_18
  Jac[7,19] = JT_4_143_19
  Jac[7,20] = RO_4_719
  Jac[8,15] = JT_4_243_15
  Jac[8,16] = JT_4_243_16
  Jac[8,17] = JT_4_243_17
  Jac[8,18] = JT_4_243_18
  Jac[8,19] = JT_4_243_19
  Jac[8,20] = RO_4_819
  Jac[9,15] = JT_4_343_15
  Jac[9,16] = JT_4_343_16
  Jac[9,17] = JT_4_343_17
  Jac[9,18] = JT_4_343_18
  Jac[9,19] = JT_4_343_19
  Jac[9,20] = RO_4_919
  Jac[10,8] = -JT_7_146_8
  Jac[10,9] = -JT_7_146_9
  Jac[10,10] = -JT_7_146_10
  Jac[10,11] = -JT_7_146_11
  Jac[10,12] = -RO_7_711
  Jac[11,7] = -JT_7_246_7
  Jac[11,8] = -JT_7_246_8
  Jac[11,9] = -JT_7_246_9
  Jac[11,10] = -JT_7_246_10
  Jac[11,11] = -JT_7_246_11
  Jac[11,12] = -RO_7_811
  Jac[12,7] = -JT_7_346_7
  Jac[12,8] = -JT_7_346_8
  Jac[12,9] = -JT_7_346_9
  Jac[12,10] = -JT_7_346_10
  Jac[12,11] = -JT_7_346_11
  Jac[12,12] = -RO_7_911
  Jac[13,23] = Jacu_13_23
  Jac[13,24] = Jac_13_24
  Jac[13,25] = Jac_13_25
  Jac[13,26] = Jac_13_26
  Jac[14,23] = Jacu_14_23
  Jac[14,24] = Jac_14_24
  Jac[14,25] = Jac_14_25
  Jac[14,26] = Jac_14_26
  Jac[15,31] = Jacu_15_31
  Jac[15,32] = Jac_15_32
  Jac[15,33] = Jac_15_33
  Jac[15,34] = Jac_15_34
  Jac[16,31] = Jacu_16_31
  Jac[16,32] = Jac_16_32
  Jac[16,33] = Jac_16_33
  Jac[16,34] = Jac_16_34

# ====== END Task 0 ====== 

  
