#coding=utf-8

from min_min import MinMin
from max_min import MaxMin

def main():
    task_num = 10   # 任务数
    resource_num = 2   # 资源数
    algo_flag = 'MinMin'  # 算法名称

    # 初始化算法
    if algo_flag == 'MinMin':
        algo = MinMin(task_num, resource_num)
    elif algo_flag == 'MaxMin':
        algo = MaxMin(task_num, resource_num)
    else:
        print "error argvs!"
        return
    
    algo.solve()  # 执行算法
    algo.dump()   # 打印结果

if __name__ == '__main__':
    main()