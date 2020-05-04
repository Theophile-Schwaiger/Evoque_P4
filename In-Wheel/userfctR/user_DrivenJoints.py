# -*- coding: utf-8 -*-

#driven_joint.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain
from math import sin,cos,pi
import numpy as np

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def sweep(t):
    """ Compute the value of a force sweep function at the given time.
    The sweep function has a sinusoidal shape with constant amplitude
    and a varying frequency. This function enables to consider linear
    variation of the frequency between f0 and f1 defined at time t0 and t1.

	:param t: the time instant when to compute the function.
	:param t0: the time instant when to specify f0.
	:param f0: the frequency at time t0.
	:param t1: the time instant when to specify f1.
	:param f1: the frequency at time t1.
	:param Fmax: the semi-amplitude of the function.

	:return Fext: the value of the sweep function.
    """
    t0=1
    t1=4 #a accorder avec le temps de simulation dans main.py
    f0=0.1
    f1=100
    Amax=0.025  # est-ce trop ?
    w=(f1-f0)/(t1-t0)
    arg=2 * pi * (f0 + w * (t / 2)) * t
    
    if t<t0 :
        Pertudd=0
        Pertud=0
        Pertu=0

    else :
        Pertudd= 2*pi*Amax*w * cos(arg) - 4*pi*pi *Amax*(f0 + w *t)*(f0 + w *t) * sin(arg)#-4*pi*pi*sin(2*pi*t)/20
        Pertud= 2 * pi * Amax * (f0 + w *t) *cos(arg) #2*pi*cos(2*pi*t)/20
        Pertu = (Amax * sin(arg))+Amax  #sin(2*pi*t)/20 +(1/20) 
        #Amax * sin(2 * pi * (f0 + ((f1 - f0) / (t1 - t0)) * (t / 2)) * t)
    
    return np.array([Pertu, Pertud, Pertudd])

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
    
    

#    
#    for i in [id_AVG,id_AVD,id_ARG,id_ARD]:
#        
#        mbs.qdd[i] = 0
#        mbs.qd[i]  = 16
#        mbs.q[i]   = 16 * tsim
     
##=============================================================================
## Accélération/Freinage
##=============================================================================
    
#    if tsim > 1.0:
#        mbs.qdd[1] = -10.0
#        mbs.qd[1]  = -20.0 * tsim + 40
#        mbs.q[1]   = -10.0 * tsim * tsim + 40*tsim -20
#    else:
#        mbs.qdd[1] = 20.0
#        mbs.qd[1]  = 20.0 * tsim
#        mbs.q[1]   = 10.0 * tsim * tsim

##=============================================================================
## Banc d'essai
##=============================================================================
    
    
    if mbs.process == 4 : ##### Banc ##########
        id_Bosse = mbs.joint_id['Joint_7']
    
        if tsim <= 1:
        
            mbs.qdd[id_Bosse] = 0
            mbs.qd[id_Bosse]  = 0
            mbs.q[id_Bosse]   = 0
        
        if tsim > 1 :
        
            tab=sweep(tsim)
               
            mbs.qdd[id_Bosse] = tab[2]
            mbs.qd[id_Bosse]  = tab[1]
            mbs.q[id_Bosse]   = tab[0]
    

################################################################################## debut bosses
################################################################################## debut bosse 1
    else :
        
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
   
##=============================================================================
## Prise de virage
##=============================================================================

#    if mbs.qd0[1] != 0.0:
#
 #       a = -0.03
  #      b = 3.0
   # 
   #     if tsim > 0.2 and tsim < 2.3:
   #     
   #         mbs.qdd[id_Crem] = -a*b*b*sin(b*(tsim -0.2)+pi)
   #         mbs.qd[id_Crem]  = a*b*cos(b*(tsim -0.2)+pi)
   #         mbs.q[id_Crem]   = a*sin(b*(tsim -0.2)+pi)
   #     else:
   #         mbs.qdd[id_Crem] = 0
   #         mbs.qd[id_Crem]  = 0
   #         mbs.q[id_Crem]   = 0
    

#    c = 0.01
#    t0 = 0.0
#    if tsim > 0.2:
#        if mbs.q[4] > -1.0 and mbs.q[mbs.joint_id['R3_dir_G']] < 0.75:
#            
#            mbs.qdd[id_Crem] = 0.0
#            mbs.qd[id_Crem]  = c
#            mbs.q[id_Crem]   = c*(tsim-0.2)
#            t0 = tsim
#        if mbs.q[4] > -1.0 and mbs.q[mbs.joint_id['R3_dir_G']] > 0.75:
#            mbs.qdd[id_Crem] = 0.0
#            mbs.qd[id_Crem]  = 0.0
#            mbs.q[id_Crem]   = 0.0
#           
#        else:
#            mbs.qdd[id_Crem] = 0.0
#            mbs.qd[id_Crem]  = -c
#            mbs.q[id_Crem]   = -c*(tsim-0.2) + c*(t0-0.2)

            
            
##=============================================================================


    
            
    return
