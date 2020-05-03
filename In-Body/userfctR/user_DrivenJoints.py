# -*- coding: utf-8 -*-

#driven_joint.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain
from math import sin,cos,pi
def user_DrivenJoints(mbs,tsim):
    """ Set the values of the driven joints directly in the mbs structure.

    :param mbs: The MbsData structure
    :param tsim: the simulation time
    
    """
    
    id_Crem = mbs.joint_id['Crem']

    id_AVG = mbs.joint_id['Roue_AVG']
    id_AVD = mbs.joint_id['Roue_AVD']
    id_ARG = mbs.joint_id['Roue_ARG']
    id_ARD = mbs.joint_id['Roue_ARD']
    
    #Comment utiliser les bosses
    #
    #Il faut travailler a vitesse constante car le but est de calculer le temps entre quand l essieu avant
    #rencontre la bosse et quand l essieu arriere la rencontre
    #Une fois qu on a calcule ce retard il faut retarder la deuxieme bosse de ce temps afin de simuler
    #le fait qu une seule bosse rencontre l essieu avant puis l essieu arriere un certain temps apres
    #
    # Exemple avec une v constante de 14 m/s
    #
    #La vitesse dans le pad est mise a un peu plus que 14 et celle dans le PID a 14 avec un grand kp pour minimiser 
    #la variation autour de cette vitesse cible
    #La distance entre les deux essieus est de 2.681 m donc en utilisant v = d/t on trouve un temps
    #de 0.1915 s
    #On connecte donc la bosse 1 a l essieu avant en ajoutant la hauteur de la bosse 1 au "e" de l essieu avant
    #On retarde l effet de la bosse 2 du retard calcule et on fait la meme chose pour l essieu arriere
    #
    #Si on veut deconnecter les bosses du chassis il suffit de ne pas additionner la hauteur des bosses aux "e"
    #des chassis sans rien toucher d autre
    #
    #Voila c est tout
    
################################################################################## debut bosses
################################################################################## debut bosse 1
    id_bosse1 = mbs.joint_id['Joint_7']
    
    if tsim <= 1:
        
        mbs.qdd[id_bosse1] = 0
        mbs.qd[id_bosse1]  = 0
        mbs.q[id_bosse1]   = 0
        
    if tsim > 1.0 and tsim <= (1+(2/7)): #en fait on laisse pile l intervalle de temps pour une demi periode pour avoir juste une bosse et pas un trou aussi
               
        mbs.qdd[id_bosse1] = 7*7*pi*pi*cos(tsim*pi*7)/10
        mbs.qd[id_bosse1]  = -7*pi*sin(tsim*pi*7)/10
        mbs.q[id_bosse1]   = (cos(tsim*pi*7) + 1)/10     # amplitude d un sinus c est 2 puis divise par 10 donc 20 cm de hauteur de bosse

        
    if tsim > (1+(2/7)):
                        
            mbs.qdd[id_bosse1] = 0
            mbs.qd[id_bosse1]  = 0
            mbs.q[id_bosse1]   = 0
################################################################################## debut bosse 2
    id_bosse2 = mbs.joint_id['Joint_30']
    retard = (2.681/14) #le retard en secondes de combien on va retarder la bosse numero 2 pour qu elle atteigne les roues arrieres en meme endroit que la bosse 1 atteint les roues avants
    #print(retard)
    
    if tsim <= (1.0 + retard):
        
        mbs.qdd[id_bosse2] = 0
        mbs.qd[id_bosse2]  = 0
        mbs.q[id_bosse2]   = 0
        
    if tsim > (1.0 + retard) and tsim <= ((1+(2/7)) + retard):
               
        mbs.qdd[id_bosse2] = 7*7*pi*pi*cos((tsim-retard)*pi*7)/10
        mbs.qd[id_bosse2]  = -7*pi*sin((tsim-retard)*pi*7)/10
        mbs.q[id_bosse2]   = (cos((tsim-retard)*pi*7) + 1)/10     # amplitude d un sinus c est 2 puis divise par 10 donc 20 cm de hauteur de bosse

        
    if tsim > ((1+(2/7)) + retard):
                        
            mbs.qdd[id_bosse2] = 0
            mbs.qd[id_bosse2]  = 0
            mbs.q[id_bosse2]   = 0
################################################################################## fin bosses
##    
##    for i in [id_AVG,id_AVD,id_ARG,id_ARD]:
##        
##        mbs.qdd[i] = 0
##        mbs.qd[i]  = 16
##        mbs.q[i]   = 16 * tsim
#     
###=============================================================================
### Accélération/Freinage
###=============================================================================
#    
##    if tsim > 1.0:
##        mbs.qdd[1] = -10.0
##        mbs.qd[1]  = -20.0 * tsim + 40
##        mbs.q[1]   = -10.0 * tsim * tsim + 40*tsim -20
##    else:
##        mbs.qdd[1] = 20.0
##        mbs.qd[1]  = 20.0 * tsim
##        mbs.q[1]   = 10.0 * tsim * tsim
#
###=============================================================================
#
#   
###=============================================================================
### Prise de virage
###=============================================================================
#    if mbs.qd0[1] != 0.0:
#
#        a = -0.03
#        b = 3.0
#    
#        if tsim > 0.2 and tsim < 2.3:
#        
#            mbs.qdd[id_Crem] = -a*b*b*sin(b*(tsim -0.2)+pi)
#            mbs.qd[id_Crem]  = a*b*cos(b*(tsim -0.2)+pi)
#            mbs.q[id_Crem]   = a*sin(b*(tsim -0.2)+pi)
#        else:
#            mbs.qdd[id_Crem] = 0
#            mbs.qd[id_Crem]  = 0
#            mbs.q[id_Crem]   = 0
#    
#
##    c = 0.01
##    t0 = 0.0
##    if tsim > 0.2:
##        if mbs.q[4] > -1.0 and mbs.q[mbs.joint_id['R3_dir_G']] < 0.75:
##            
##            mbs.qdd[id_Crem] = 0.0
##            mbs.qd[id_Crem]  = c
##            mbs.q[id_Crem]   = c*(tsim-0.2)
##            t0 = tsim
##        if mbs.q[4] > -1.0 and mbs.q[mbs.joint_id['R3_dir_G']] > 0.75:
##            mbs.qdd[id_Crem] = 0.0
##            mbs.qd[id_Crem]  = 0.0
##            mbs.q[id_Crem]   = 0.0
##           
##        else:
##            mbs.qdd[id_Crem] = 0.0
##            mbs.qd[id_Crem]  = -c
##            mbs.q[id_Crem]   = -c*(tsim-0.2) + c*(t0-0.2)
#
#            
#            
###=============================================================================


    
            
    return
