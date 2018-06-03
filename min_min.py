#coding=utf-8
import numpy as np

from algorithm import Algorithm
from dispatch import Dispatch
from utils import expected_time_to_compute

class MinMin(Algorithm):
    def solve(self):
        while self.t_dict_unsolved:
            print 'tasks remain:', len(self.t_dict_unsolved)
            min_EMCT = {
                't_id': 0, 
                'r_id': 0, 
                'start_time': np.inf,
                'end_time': np.inf
            }
            for t in self.t_dict_unsolved.itervalues():
                # 找到所有任务的最小完成时间
                t.EMCT['end_time'] = np.inf
                for r in self.r_dict.itervalues():
                    # 找到任务t的最小完成时间
                    ETC = expected_time_to_compute(
                        t.t_id, r.r_id)
                    ECT = ETC + r.RAT
                    if ECT < t.EMCT['end_time']:
                        t.EMCT['r_id'] = r.r_id
                        t.EMCT['start_time'] = r.RAT
                        t.EMCT['end_time'] = ECT
                if t.EMCT['end_time'] < min_EMCT['end_time']:
                    min_EMCT['start_time'] = t.EMCT['start_time']
                    min_EMCT['end_time'] = t.EMCT['end_time']
                    min_EMCT['r_id'] = t.EMCT['r_id']
                    min_EMCT['t_id'] = t.t_id
            # 执行调度
            d = Dispatch(
                min_EMCT['t_id'],
                min_EMCT['r_id'],
                min_EMCT['start_time']
            )
            self.d_list.append(d)
            self.r_dict[min_EMCT['r_id']].RAT = min_EMCT['end_time']
            # 删除任务
            self.t_dict_unsolved.pop(min_EMCT['t_id'])