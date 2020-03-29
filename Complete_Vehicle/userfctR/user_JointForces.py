# -*- coding: utf-8 -*-

#joint_forces.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

def user_JointForces(mbs,tsim):
    """ Compute the force in the joint. It fills the Qq matrix.
    
    :param mbs: The mbs Data structure
    :param tsim: the simulation time
    
    """
    # cleaning previous forces
    mbs.Qq[1:] = 0
    
    
    K = mbs.user_model['Strut_AV']['K']
    D = mbs.user_model['Strut_AV']['D']
    L0 = mbs.user_model['Strut_AV']['L0']
    
    #a = 10
    
    for i in [12,20,28,36]:
    
        mbs.Qq[i] = -(K*(mbs.q[i]-L0) + D*mbs.qd[i])
    

    return
