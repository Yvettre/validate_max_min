#coding=utf-8
import numpy as np
class Task(object):
    '''
    计算任务
    '''
    t_num = 0
    def __init__(self):
        self.t_id = Task.t_num
        Task.t_num += 1
        self.EMCT = {
            'r_id': 0,
            'start_time': np.inf,
            'end_time': np.inf
        }# 最小完成时间的资源id和开始与结束时间