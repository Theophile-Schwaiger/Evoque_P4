# -*- coding: utf-8 -*-

#user_dirdyn.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

import MBsysPy as Robotran
import numpy as np

def user_dirdyn_init(mbs, dd):
    # Example: Creating and storing a sensor in mbs then create a list to store
    #          the vertical velocity of the sensor. Two new fields are added to
    #          the MbsData instance to store the sensor and the list.
    #
    # import MBsysPy as Robotran # Should be done outside the function.
    #
    # mbs.my_sensor = Robotran.MbsSensor(mbs)
    # mbs.my_sensor_v = []
#    mbs.sensors.append(Robotran.MbsSensor(mbs, 1))    
    
    return

def user_dirdyn_loop(mbs, dd):
    # Example: The sensor, created in `user_dirdyn_init`, is computed (fields 
    #          are updated) and the vertical velocity is added in the list.
    #
    # mbs.mbs_sensor(mbs.my_sensor, mbs, 1)
    # mbs.my_sensor_v.append(mbs.my_sensor.V[3])
#    mbs.sensors[0].sensor(1)
#    mbs.sensors[1].sensor(2)

    
    return

def user_dirdyn_finish(mbs, dd):
    # Example: The velocities are saved to a file, then the fields created in 
    #          the MbsData instance during the function `user_dirdyn_init` are
    #          removed.
    #
    # import numpy as np # Should be done outside the function.
    # 
    # np.savetxt("myfile.txt", mbs.my_sensor_v)
    # del mbs.my_sensor, mbs.my_sensor_v
#    np.savetxt("sensor01.txt",mbs.sensors[0].P)                # on cree un fichier qui donne la hauteur de l essieu avant
#    np.savetxt("sensor02.txt",mbs.sensors[1].P)                # la meme pour l essieu arriere
    
    return
