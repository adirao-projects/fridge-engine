import numpy as np
from numba import jit, njit, vectorize

#F=ma
#assume 1 unit = 1m
#s=ut+(1/2)*a*1


@njit
def gravity_loop(entity, rat=1, grav=9.81):
    entity.loc_y = entity.loc_y - (1/2)*grav

def posiiton_check(positon, pos_area):
    
    x = position[0]-((position[0]-1) not in pos_area[0])    
    
    return ()