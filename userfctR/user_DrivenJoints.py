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
    mbs.q[8]   = 0#mbs.q0[5]  + mbs.qd0[5]*tsim + 0.5 * mbs.qdd[5]*tsim*tsim
    
    return
