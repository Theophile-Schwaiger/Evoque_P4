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
mbs_data = Robotran.MbsData("../dataR/Complete_Vehicle_New_Dimensions.mbs")
print(mbs_data)

#==============================================================================
# Partitionning
#==============================================================================
mbs_data.process = 1
mbs_part = Robotran.MbsPart(mbs_data)
mbs_part.set_options(rowperm = 1, verbose = 1)
mbs_part.run()


##==============================================================================
## Direct Dynamics
##==============================================================================
mbs_data.process = 3
mbs_dirdyn = Robotran.MbsDirdyn(mbs_data)
mbs_dirdyn.set_options(dt0 = 1e-3, tf = 5    ,save2file = 1)
mbs_dirdyn.run()

#==============================================================================
#====Amortisseur avant prise de virage=========================================


sol = np.loadtxt('../resultsR/dirdyn_virage.res')
q = sol[:,20]
t = sol[:,0]

fig = plt.figure(figsize=(13,6.5))
plt.title('Hauteur des fusées droites en prise de virage',fontsize = 16)
plt.plot(t,q*1000,label='Fusée avant')


#plt.axhline(y= anoy,xmin = anox/t[-1] ,xmax = (anox+ (0.1*t[-1]))/t[-1] , color = 'black', linewidth = 1)
#plt.plot(1.5,100000,'--b')


plt.xlabel('Temps [s]',fontsize = 13)
plt.ylabel('Hauteur fusée [mm]',fontsize = 13)

plt.axvline(x=0.4,linestyle='--',color='red',label='virage droit')#ligne verticale des virages
plt.axvline(x=1.65,linestyle='--',color='black',label='virage gauche')

#plt.annotate("{:6.5f}".format(q[-1]), xy=(t[-1], q[-1]), xytext=(t[-1]*0.8, q[-1] +0.01),fontsize=14)

#plt.annotate("(%4.3f,%6.5f)" % (anox,anoy), xy=(anox,anoy), xytext=(anox + (0.1*t[-1]), anoy), fontsize=14)



#==============================================================================
#======Amortisseur arrière prise de virage ====================================

sol = np.loadtxt('../resultsR/dirdyn_virage.res')
q = sol[:,38]
t = sol[:,0]


plt.plot(t,q*1000,label='Fusée arrière')


#anox = sol[i[0][0],0]

#anoy = np.min(q)

#plt.axhline(y= anoy,xmin = anox/t[-1] ,xmax = (anox+ (0.1*t[-1]))/t[-1] , color = 'black', linewidth = 1)


plt.legend()
#plt.xlabel('Temps [s]',fontsize = 13)
#plt.ylabel('Compression amortisseur arrière [m]',fontsize = 13)

#plt.annotate("{:6.5f}".format(q[-1]), xy=(t[-1], q[-1]), xytext=(t[-1]*0.8, q[-1] +0.01),fontsize=14)

#plt.annotate("(%4.3f,%6.5f)" % (anox,anoy), xy=(anox,anoy), xytext=(anox + (0.1*t[-1]), anoy), fontsize=14)
plt.show()
fig.savefig('Virage.pdf',bbox_inches = "tight",dpi=fig.dpi)


#==============================================================================
#====Mise au repos=========================================


sol = np.loadtxt('../resultsR/dirdyn_repos.res')
q = sol[:,3]
t = sol[:,0]

fig = plt.figure(figsize=(13,6.5))
plt.title('Hauteur du chassis en mise au repos',fontsize = 16)
plt.plot(t,q*1000,)


#plt.axhline(y= anoy,xmin = anox/t[-1] ,xmax = (anox+ (0.1*t[-1]))/t[-1] , color = 'black', linewidth = 1)
#plt.plot(1.5,100000,'--b')


plt.xlabel('Temps [s]',fontsize = 13)
plt.ylabel('Hauteur [mm]',fontsize = 13)

#plt.axvline(x=0.5,linestyle='--',color='red',label='virage droit')#ligne verticale des virages
#plt.axvline(x=1.3,linestyle='--',color='black',label='virage gauche')

#plt.annotate("{:6.5f}".format(q[-1]), xy=(t[-1], q[-1]), xytext=(t[-1]*0.8, q[-1] +0.01),fontsize=14)

#plt.annotate("(%4.3f,%6.5f)" % (anox,anoy), xy=(anox,anoy), xytext=(anox + (0.1*t[-1]), anoy), fontsize=14)

plt.show()
fig.savefig('repos.pdf',bbox_inches = "tight",dpi=fig.dpi)

#==============================================================================
#====Repos Avant=========================================


sol = np.loadtxt('../resultsR/dirdyn_repos.res')
q = sol[:,20]
t = sol[:,0]

fig = plt.figure(figsize=(13,6.5))
plt.title('Hauteur des fusées droites en mise au repos',fontsize = 16)
plt.plot(t,q*1000,label='Fusée avant')


#plt.axhline(y= anoy,xmin = anox/t[-1] ,xmax = (anox+ (0.1*t[-1]))/t[-1] , color = 'black', linewidth = 1)
#plt.plot(1.5,100000,'--b')


plt.xlabel('Temps [s]',fontsize = 13)
plt.ylabel('Hauteur fusée [mm]',fontsize = 13)

#plt.axvline(x=0.5,linestyle='--',color='red',label='virage droit')#ligne verticale des virages
#plt.axvline(x=1.3,linestyle='--',color='black',label='virage gauche')

#plt.annotate("{:6.5f}".format(q[-1]), xy=(t[-1], q[-1]), xytext=(t[-1]*0.8, q[-1] +0.01),fontsize=14)

#plt.annotate("(%4.3f,%6.5f)" % (anox,anoy), xy=(anox,anoy), xytext=(anox + (0.1*t[-1]), anoy), fontsize=14)



#==============================================================================
#====== Repos arrière ====================================

sol = np.loadtxt('../resultsR/dirdyn_repos.res')
q = sol[:,38]
t = sol[:,0]


plt.plot(t,q*1000,label='fusée arrière')


#anox = sol[i[0][0],0]

#anoy = np.min(q)

#plt.axhline(y= anoy,xmin = anox/t[-1] ,xmax = (anox+ (0.1*t[-1]))/t[-1] , color = 'black', linewidth = 1)


plt.legend()
#plt.xlabel('Temps [s]',fontsize = 13)
#plt.ylabel('Compression amortisseur arrière [m]',fontsize = 13)

#plt.annotate("{:6.5f}".format(q[-1]), xy=(t[-1], q[-1]), xytext=(t[-1]*0.8, q[-1] +0.01),fontsize=14)

#plt.annotate("(%4.3f,%6.5f)" % (anox,anoy), xy=(anox,anoy), xytext=(anox + (0.1*t[-1]), anoy), fontsize=14)
plt.show()
fig.savefig('repos_avar.pdf',bbox_inches = "tight",dpi=fig.dpi)


