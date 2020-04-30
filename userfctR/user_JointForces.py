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

    K1 = mbs.user_model['Strut_AV']['K']
    D1 = mbs.user_model['Strut_AV']['D']
    L01 = mbs.user_model['Strut_AV']['L0']
    
    idAVG = mbs.joint_id['Strut_AVG']
    idAVD = mbs.joint_id['Strut_AVD']
    idARG = mbs.joint_id['Strut_ARG']
    idARD = mbs.joint_id['Strut_ARD']
    
    for i in [idAVG,idAVD]:
    
        mbs.Qq[i] = -(K*(mbs.q[i]-L0) + D*mbs.qd[i])
        
    for i in [idARG,idARD]:
    
        mbs.Qq[i] = -(K1*(mbs.q[i]-L01) + D1*mbs.qd[i])

############# IMPLEMENTATION PID ###############

    id_AVG = mbs.joint_id['Roue_AVG']
    id_AVD = mbs.joint_id['Roue_AVD']
    id_ARG = mbs.joint_id['Roue_ARG']
    id_ARD = mbs.joint_id['Roue_ARD']

    u = [id_AVG, id_AVD, id_ARG, id_ARD]  # Couple d'entree des roues
    kp = 2  # constante du PID a determiner experimentalement
    yref = 5  # vitesse voulue [m/s]
    y = mbs.qd[1]  # vitesse prise au chassis

    # u=kp*(yref-y)

    for i in u:
        mbs.Qq[i] = kp*(yref-y)

###################################################
    

    return
