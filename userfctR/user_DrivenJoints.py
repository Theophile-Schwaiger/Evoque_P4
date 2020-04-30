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
    
    # Example: joint 5 under constant acceleration with non-zero initial 
    #          coordinate (mbs.q0) and velocity (mbs.qd0). 
    # mbs.qdd[5] = 2
    # mbs.qd[5]  = mbs.qd0[5] + mbs.qdd[5]*tsim
    # mbs.q[5]   = mbs.q0[5]  + mbs.qd0[5]*tsim + 0.5 * mbs.qdd[5]*tsim*tsim

############# IMPLEMENTATION PID ###############


   # id_AVG = mbs.joint_id['Roue_AVG']
   # id_AVD = mbs.joint_id['Roue_AVD']
   # id_ARG = mbs.joint_id['Roue_ARG']
   # id_ARD = mbs.joint_id['Roue_ARD']

   # u= [id_AVG,id_AVD,id_ARG,id_ARD] #Couple d'entree des roues
   # kp= 2 #constante du PID a determiner experimentalement
   # yref= 10 # vitesse voulue [m/s]
   # y= mbs.qd[1 ]#vitesse prise au chassis

     # u=kp*(yref-y)

   # for i in u:
    #    mbs.qdd[i] = 0
    #    mbs.qd[i]  = kp * (yref-y)
    #    mbs.q[i]   = kp * (yref-y) * tsim


###################################################

    #if tsim > 1.0:
        #mbs.qdd[1] = -10.0
        #mbs.qd[1]  = -20.0 * tsim + 40
        #mbs.q[1]   = -10.0 * tsim * tsim + 40*tsim -20
    #else:
     #   mbs.qdd[1] = 20.0
     #   mbs.qd[1]  = 20.0 * tsim
     #   mbs.q[1]   = 10.0 * tsim * tsim
    
    id_Crem = mbs.joint_id['Crem']
    
#    if tsim <= 0.5:
#        
#        mbs.qdd[id_Crem] = 0
#        mbs.qd[id_Crem]  = 0
#        mbs.q[id_Crem]   = 0
#        
#    if tsim > 0.5 and tsim <= 1.0:
#               
#        mbs.qdd[id_Crem] = 0
#        mbs.qd[id_Crem]  = -0.03
#        mbs.q[id_Crem]   = -0.03 * (tsim-0.5)
#
#        
#    if tsim > 1.0:
#        if mbs.q[id_Crem] > 0.0 and mbs.q[id_Crem] <= 0.015 :
#            
#            mbs.qdd[id_Crem] = 0
#            mbs.qd[id_Crem]  = 0
#            mbs.q[id_Crem]   = 0
#           
#        else:
#                        
#            mbs.qdd[id_Crem] = 0
#            mbs.qd[id_Crem]  = 0.03
#            mbs.q[id_Crem]   = 0.03 * (tsim-1.0) -0.015

    
    
   # a = -0.02
    #b = 3.0
    
    #if tsim > 0.2:
        
      #  mbs.qdd[id_Crem] = -a*b*b*sin(b*(tsim -0.2)+pi)
      #  mbs.qd[id_Crem]  = a*b*cos(b*(tsim -0.2)+pi)
       # mbs.q[id_Crem]   = a*sin(b*(tsim -0.2)+pi)
    #else:
     #   mbs.qdd[id_Crem] = 0
    #    mbs.qd[id_Crem]  = 0
     #   mbs.q[id_Crem]   = 0


   # mbs.qdd[1] = 0.0
   # mbs.qd[1]  = 10.0
   # mbs.q[1]   = 10.0 * tsim
    


    
            
    return
