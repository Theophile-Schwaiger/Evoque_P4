# -*- coding: utf-8 -*-

#ext_forces.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#Last update on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain

try:
    import MBsysPy as Robotran
except:
    raise ImportError("MBsysPy not found/installed."
                      "See: https://www.robotran.eu/howto/install"
                     )

import numpy as np
from math import cos, pi
from mbs_tgc import *
import inspect
lines1 = inspect.getsource(mbs_tgc.tgc_car_kine_wheel)

print(lines1)
print('#######################################################################')
print('#######################################################################')

lines2 = inspect.getsource(mbs_tgc.tgc_bakker_contact)
print(lines2)

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
        Pw = PxF
        Pw[0] = 3.0

        Vw = VxF
        Vw[0] = 3.0

        OMw = OMxF
        OMw[0] = 3.0

        pen,rz,angslip,angcamb,slip,Pct,Vmct,Rt_ground,dxF = mbs_tgc.tgc_car_kine_wheel(Pw,RxF,Vw,OMw,R0)
        #e = PxF[3] - (RxF[2,2]*R0)
        e = - pen # pen = (RxF[2,2]*R0) - PxF[3]

        #ed = VxF[3]
        ed = Vmct[3]


        if mbs.process == 2:

            e = PxF[3] - (RxF[2,2]*R0)
            ed = VxF[3]

            if e < 0:
                Fz = Kp*abs(e) + Dp*abs(ed)
            if e > 0:

                Fz = -(Kp*abs(e) + Dp*abs(ed))

        else:

            if e < 0:

                if mbs.q[1] != 0:

                    Fz = -Kp*e + Dp*abs(ed)


                    Fwhl = np.array([0,Fx,Fy,Fz])

                    Mwhl = np.array([0,Mx,My,Mz])

                    mbs_tgc.tgc_bakker_contact(Fwhl,Mwhl,angslip,angcamb,slip)

                    Rt_ground = np.reshape(Rt_ground,(-1,4))

                    F = Fwhl[1:]
                    #print(F)
                    F = Rt_ground[1:,1:] @ F

                    M = Mwhl[1:]
                    M = Rt_ground[1:,1:] @ M

                    Fx = F[0]
                    Fy = F[1]
                    #Fz = F[2]

                    Mx = M[0]
                    My = M[1]
                    Mz = M[2]

                else:

                    Fz = -Kp*e + Dp*abs(ed)


            else:

                Fz = 0



    Swr=np.zeros(9+1)
    Swr[1:]=np.r_[Fx,Fy,Fz,Mx,My,Mz,dxF[1:]]

    return Swr
