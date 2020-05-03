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

   
##=============================================================================
## Prise de virage
##=============================================================================

    if mbs.qd0[1] != 0.0:

        a = -0.03
        b = 3.0
    
        if tsim > 0.2 and tsim < 2.3:
        
            mbs.qdd[id_Crem] = -a*b*b*sin(b*(tsim -0.2)+pi)
            mbs.qd[id_Crem]  = a*b*cos(b*(tsim -0.2)+pi)
            mbs.q[id_Crem]   = a*sin(b*(tsim -0.2)+pi)
        else:
            mbs.qdd[id_Crem] = 0
            mbs.qd[id_Crem]  = 0
            mbs.q[id_Crem]   = 0
    

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
