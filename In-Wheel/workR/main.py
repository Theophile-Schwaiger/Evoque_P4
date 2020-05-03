#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    
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
import matplotlib.pyplot as plt
import numpy as np

#==============================================================================
# Project loading
#==============================================================================
mbs_data = Robotran.MbsData("../dataR/Model_In_Wheel.mbs")
print(mbs_data)

#==============================================================================
# Partitionning
#==============================================================================
mbs_data.process = 1
mbs_part = Robotran.MbsPart(mbs_data)
mbs_part.set_options(rowperm = 1, verbose = 1)
mbs_part.run()

#==============================================================================
# Static Equilibrium
#==============================================================================

mbs_data.process = 2
mbs_equil = Robotran.MbsEquil(mbs_data)
mbs_equil.set_options(save_anim = 1, senstol = 1e-4, compute_uxd = 0,resfilename = "equil1",itermax = 100)
mbs_equil.run()

#==============================================================================
# Direct Dynamics
#==============================================================================
mbs_data.process = 3
mbs_dirdyn = Robotran.MbsDirdyn(mbs_data)
mbs_dirdyn.set_options(dt0 = 1e-3, tf = 3.0, save2file = 1)
mbs_dirdyn.run()

#==============================================================================


sol = np.loadtxt('../resultsR/dirdyn_q.res')
q = sol[:,3]
t = sol[:,0]

fig = plt.figure(figsize=(13,6.5))
plt.title('Evolution de la hauteur du chassis',fontsize = 16)
plt.plot(t,q)
plt.axhline(y= q[-1],dashes = (3,2))
i = np.where(q == np.min(q))

anox = sol[i[0][0],0]

anoy = np.min(q)

plt.axhline(y= anoy,xmin = anox/t[-1] ,xmax = (anox+ (0.1*t[-1]))/t[-1] , color = 'black', linewidth = 1)

plt.margins(x=0)
plt.ylim(bottom=0)

plt.xlabel('Temps [s]',fontsize = 13)
plt.ylabel('Hauteur du chassis [m]',fontsize = 13)

plt.annotate("{:6.5f}".format(q[-1]), xy=(t[-1], q[-1]), xytext=(t[-1]*0.8, q[-1] +0.01),fontsize=14)

plt.annotate("(%4.3f,%6.5f)" % (anox,anoy), xy=(anox,anoy), xytext=(anox + (0.1*t[-1]), anoy), fontsize=14)
plt.show
#plt.savefig('Hauteur_Chassis.pdf',bbox_inches = "tight",dpi=fig.dpi)

