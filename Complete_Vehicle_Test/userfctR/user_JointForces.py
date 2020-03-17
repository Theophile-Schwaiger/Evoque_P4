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
    
    
    # Example: damping in joint number 5
    # D = 0.5 # N/(m/s)
    # mbs.Qq[5] = -D * mbs.qd[5]
    
    return
