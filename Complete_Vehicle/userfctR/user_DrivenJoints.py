# -*- coding: utf-8 -*-

#driven_joint.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

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
    
    
#    for i in [14,22,30,38]:
#        
#        mbs.qdd[i] = 0
#        mbs.qd[i]  = 2.89
#        mbs.q[i]   = 2.89 * tsim
     
#    if tsim <0.5 :
#        
#        mbs.qdd[8] = 0
#        mbs.qd[8]  = 0
#        mbs.q[8]   = 1.4*tsim
#        
#        mbs.qdd[16] = 0
#        mbs.qd[16]  = 0
#        mbs.q[16]   = 0.8*tsim
#    else:
#        
#        mbs.qdd[8] = 0
#        mbs.qd[8]  = 0
#        mbs.q[8]   = 0.7
#        
#        mbs.qdd[16] = 0
#        mbs.qd[16]  = 0
#        mbs.q[16]   = 0.4
        
   
    if tsim > 1.0:
        mbs.qdd[1] = -10.0
        mbs.qd[1]  = -20.0 * tsim + 40
        mbs.q[1]   = -10.0 * tsim * tsim + 40*tsim -20
    else:
        mbs.qdd[1] = 20.0
        mbs.qd[1]  = 20.0 * tsim
        mbs.q[1]   = 10.0 * tsim * tsim

            
    return
