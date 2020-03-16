# -*- coding: utf-8 -*-

#user_dirdyn.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

def user_equil_init(mbs, eq):
    
    
    return

def user_equil_loop(mbs, eq):
    
    
    return

def user_equil_finish(mbs, eq):
    
    
    return

def user_equil_fxe(mbs, f):
    """ This function is used to add user-defined equilibrium equation to the system.
    
    The equilibrium process, if successuful, will reach f[1:]=0.
    
    The values assigned to f have to be floats (not integers).
    
    Parameters
    ----------
    mbs: MBsysPy.MbsData
        Instance of the multibody system.
    f: numpy.ndarray
        Numpy array containing the residue of the user equilibrium equations.
        The residues are filled in f[1:MbsEquil.nxe] (the array is oversized to
        the number of equilibrium variable: MbsEquil.nx).
    
    Examples
    --------
    # In this example at the equilibrium the value of the fifth generalized is 0:
    f[1] = mbs.q[5] 
    # Here we use an user function from an external module
    import my_external_module # Should be done outside the function.
    f[2] = my_external_module.my function(mbs) 
    
    """
    
    
    return
