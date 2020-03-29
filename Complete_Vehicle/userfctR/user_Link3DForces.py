# -*- coding: utf-8 -*-

#link3D_forces.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#Last update on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain


import numpy as np

def user_Link3DForces(PxF,RxF,VxF,OMxF,AxF,OMPxF,mbs,tsim,ixF):
    """ DEPRECATED Compute the link force for a given link id

    :param PxF: the position of the point
    :param RxF: the rotation matrix of the point
    :param VxF: the velocity vector of the point
    :param OMxF: the angular velocity of the point
    :param AxF: the acceleration vector of the point
    :param OMPxF: the angular acceleration of the point
    :param mbs: the Data structure
    :param tsim: the simulation time
    :param ixF: the index of the force point
    
    """
    
    
    Fx=0.0
    Fy=0.0
    Fz=0.0
    Mx=0.0
    My=0.0
    Mz=0.0
    #==========================================================================
    # BEGIN OF USER CODE
    #==========================================================================
    # No example, should not be used
    #==========================================================================
    # END OF USER CODE
    #==========================================================================
    Swr=np.zeros(7)
    Swr[1:7]=np.r_[Fx,Fy,Fz,Mx,My,Mz]
    
    return Swr
