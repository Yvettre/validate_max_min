#coding=utf-8
import copy
from abc import ABCMeta,abstractmethod

from utils import expected_time_to_compute
from task import Task
from resource import Resource
from dispatch import Dispatch

class Algorithm():
    __metaclass__ = ABCMeta
    def __init__(self, t_num, r_num):
        self.t_dict = {}
        self.r_dict = {}
        self.d_list = []# dispatch_list
        for i in xrange(t_num):
            t = Task()
            self.t_dict[t.t_id] = t
        for i in xrange(r_num):
            r = Resource()
            self.r_dict[r.r_id] = r
        # 尚未完成的任务集合
        self.t_dict_unsolved = copy.copy(self.t_dict)

    @abstractmethod
    def solve(self):
        pass

    def dump(self):
        max_time = 0.0
        r_run_time = {}
        for d in self.d_list:
            d.dump()
            if not r_run_time.has_key(d.r_id):
                r_run_time[d.r_id] = 0.0
            r_run_time[d.r_id] += d.compute_time
            if max_time < d.end_time:
                max_time = d.end_time
            print '-'*32
        print 'total time:', max_time
        for k, v in r_run_time.iteritems():
            print k, v