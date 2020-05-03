# -*- coding: utf-8 -*-

#cons_hJ.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

def user_cons_hJ(h,Jac,mbs,tsim):
    """ Function that compute the Jacobian and the h vector for the user constraints
    
    :param h: the constraint vector to return
    :param Jac: the jacobian matrix to return
    :param mbs: the Data structure
    """
    
    # Example: Compute the expression of h and Jac then assign the values.
    # h[1] = mbs.q[1]-mbs.q[2]*mbs.q[2]
    # Jac[1,1] =  1.
    # Jac[1,2] = -2*mbs.q[2].
    # IMPORTANT: NEVER REASSIGN H => h=np.array([0,mbs.q[1]-mbs.q[2]*mbs.q[2],0])
    #            NEVER REASSIGN Jac=>Jac=np.array([[0,0,0,0],[0,1,-2*mbs.q[2],0])
    #            Both command will change the values of h, Jac in this function 
    #            but they will not be modified outside the scope of this function.
    return
