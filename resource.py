#coding=utf-8
import numpy as np
class Resource():
    '''
    计算资源
    '''
    r_num = 0
    def __init__(self):
        self.r_id = Resource.r_num
        Resource.r_num += 1
        # RAT resource available time
        self.RAT = 0.0