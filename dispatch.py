#coding=utf-8
import numpy as np
from utils import expected_time_to_compute
class Dispatch():
    '''
    调度
    '''
    d_num = 0
    def __init__(self, t_id, r_id, start_time):
        self.t_id = t_id
        self.r_id = r_id
        self.start_time = start_time
        self.compute_time = expected_time_to_compute(t_id, r_id)
        self.end_time = start_time + self.compute_time
        self.d_id = Dispatch.d_num
        Dispatch.d_num += 1

    def dump(self):
        print 'd_id:', self.d_id
        print 't_id:', self.t_id
        print 'r_id:', self.r_id
        print 'start_time:', self.start_time
        print 'end_time:', self.end_time
        print 'compute_time:', self.compute_time