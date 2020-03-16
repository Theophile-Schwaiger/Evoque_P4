# -*- coding: utf-8 -*-

#ext_forces.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#Last update on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain


import numpy as np
from math import cos, pi


def user_ExtForces(PxF,RxF,VxF,OMxF,AxF,OMPxF,mbs,tsim,ixF):
    """ Compute the external force for a given force point

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
    Kp = mbs.user_model['Fext']['K']
    Dp = mbs.user_model['Fext']['D']
    R0 = mbs.user_model['Fext']['R0']
 
    
    Fz = 0.0
    Fx=0.0
    Fy=0.0
    Fz=0.0
    Mx=0.0
    My=0.0
    Mz=0.0

    if ixF == mbs.extforce_id["ExtForce_0"] or ixF == mbs.extforce_id["ExtForce_1"] or ixF == mbs.extforce_id["ExtForce_2"] or ixF == mbs.extforce_id["ExtForce_3"]:
        e = PxF[3] - (RxF[2,2]*R0)
        #e = PxF[3] - R0
 
        ed = VxF[3]
        
        if mbs.process == 2:
            
            if e < 0:
                Fz = Kp*abs(e) + Dp*abs(ed)
            if e > 0:
            
                Fz = -(Kp*abs(e) + Dp*abs(ed))
        
        else:
            
            if e < 0:
                
                #Fz = -Kp*e - Dp*ed 
                Fz = -Kp*e + Dp*abs(ed)

                
            else:
                
                Fz = 0
                
    
    idpt=mbs.xfidpt[ixF]
    #dxF = mbs.dpt[1:,idpt]
    dxF=np.array([0,0,-(PxF[3]/RxF[2,2])])
    Swr=np.zeros(9+1)
    Swr[1:]=np.r_[Fx,Fy,Fz,Mx,My,Mz,dxF]
        
    return Swr
