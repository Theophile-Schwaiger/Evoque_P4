# -*- coding: utf-8 -*-

#link_forces.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

def user_LinkForces(Z,Zd,mbs,tsim,identity):
    """ Compute the link force for a given link id
    
    :param Z: the position between the two anchor points
    :param Zd: the velocity between the two ancho points
    :param mbs: the mbs Data structure
    :param tsim: the simulation time
    :param identity: the identity of the link
    
    """
    
    if identity == mbs.link_id['Link_AVG']:
        
        
        Kr = mbs.user_model['Link_AVG']['K']
        Da  = mbs.user_model['Link_AVG']['D']
        Z0 = mbs.user_model['Link_AVG']['L0']
        Flink= (Kr*(Z-Z0) + Da*Zd)
        
    if identity == mbs.link_id['Link_AVD']:
        
        
        Kr = mbs.user_model['Link_AVD']['K']
        Da  = mbs.user_model['Link_AVD']['D']
        Z0 = mbs.user_model['Link_AVD']['L0']
        Flink= (Kr*(Z-Z0) + Da*Zd)
        
    if identity == mbs.link_id['Link_ARG']:
        
        
        Kr = mbs.user_model['Link_AR']['K']
        Da  = mbs.user_model['Link_AR']['D']
        Z0 = mbs.user_model['Link_AR']['L0']
        Flink= (Kr*(Z-Z0) + Da*Zd)
        
    if identity == mbs.link_id['Link_ARD']:
        
        
        Kr = mbs.user_model['Link_AR']['K']
        Da  = mbs.user_model['Link_AR']['D']
        Z0 = mbs.user_model['Link_AR']['L0']
        Flink= (Kr*(Z-Z0) + Da*Zd)
    
    # Example: linear spring
    # k = 1000 #N/m
    # Z0= 0.1  #m
    # Flink = k*(Z-Z0)
    
    return Flink
