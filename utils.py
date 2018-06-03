#coding=utf-8
import numpy as np
def expected_time_to_compute(t_id, r_id):
    '''
    任务t_id在资源r_id上的预测执行时间[0, 1]
    '''
    return 10*(np.cos((t_id+0.5) * (r_id+0.5) + 0.5)**2)