#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test visioconférence

    test de commit et pull sur la master branch

       Universite catholique de Louvain
       CEREM : Centre for research in mechatronics
       http://www.robotran.be  
       Contact : info@robotran.be
    
    
       Main script template for complete model:
       -----------------------------------------------
        This template loads the data file *.mbs and execute:
         - the coordinate partitioning module
         - the direct dynamic module (time integration of equations of motion).
         - the equilibrium module
         - the modal module
         - the inverse dynamic module
         - the solverkin module
        It have to be adapted and completed by the user.
     
        (c) Universite catholique de Louvain
        
"""

#==============================================================================
# Packages loading
#==============================================================================
try:
    import MBsysPy as Robotran
except:
    raise ImportError("MBsysPy not found/installed."
                      "See: https://www.robotran.eu/howto/install"
                     )

#==============================================================================
# Project loading
#==============================================================================
mbs_data = Robotran.MbsData("../dataR/Complete_Vehicle_Test.mbs")
print(mbs_data)

#==============================================================================
# Partitionning
#==============================================================================
mbs_data.process = 1
mbs_part = Robotran.MbsPart(mbs_data)
mbs_part.set_options(rowperm = 1, verbose = 1)
mbs_part.run()

#==============================================================================
# Direct Dynamics
#==============================================================================
mbs_data.process = 3
mbs_dirdyn = Robotran.MbsDirdyn(mbs_data)
mbs_dirdyn.set_options(dt0 = 1e-3, tf = 4.0, save2file = 1)
mbs_dirdyn.run()



