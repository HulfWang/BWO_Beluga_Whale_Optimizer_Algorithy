'''

% ----------------------- README ------------------------------------------
%     最后一次修改   ：2024/2/8
%                       欢迎关注₍^.^₎♡
%     项目           ：白鲸优化算法BWO
%     内容来源文献   ：Zhong Changting, Li Gang, Meng Zeng. Beluga whale
%        optimization: A novel nature-inspired metaheuristic algorithm [J].
%        Knowledge-Based Systems, 2022, 251.
%     微信公众号     ：KAU的云实验台(可咨询定制)
%     CSDN/知乎      ：KAU的云实验台
%     付费代码(更全) ：https://mbd.pub/o/author-a2iWlGtpZA==
%     免费代码       ：公众号后台回复"资源"
% -------------------------------------------------------------------------

'''

import numpy as np
from matplotlib import pyplot as plt
import math
import random
import copy
import benchmarks
import BWO

''' --------------------------- 参数设置 ----------------------------------'''
SearchAgents_no = 200  # 种群量级
Function_name = 'F9'  # 测试函数
Max_iteration = 500   # 迭代次数

''' ------------------------ 获取测试函数细节 F1~F23 ----------------------------------'''
#func_details = benchmarks.getFunctionDetails(Function_name)
func_details1= benchmarks.getFunctionSet(Function_name)
lb = func_details1[1]
ub = func_details1[2]
dim = func_details1[3]
fobj = getattr(benchmarks, Function_name) # 获取函数求解

''' ------------------------ 白鲸求解 ----------------------------------'''
# x = BWO.BWO(fobj, lb, ub, dim, SearchAgents_no, Max_iteration)

#因为智能优化算法具有不稳定性，需要多次求解取平均值来获得普遍答案
time=5

output_arr =np.zeros(time)
# output_arr =[1,2,3,4,5]

for i in range(5):
    x = BWO.BWO(fobj, lb, ub, dim, SearchAgents_no, Max_iteration)
    print(x.best)
    output_arr[i] = x.best

print(output_arr)
mean_value=np.mean(output_arr)
print(mean_value)

#求得多个结果的方差
squa_diff =0
temp=0
for i in range(len(output_arr)):
    squa_diff=(output_arr[i]-mean_value)*(output_arr[i]-mean_value)
    temp=squa_diff+temp

squa_diff=temp/time
print(squa_diff)

''' ------------------------ 求解结果 ----------------------------------'''
IterCurve = x.convergence
Best_fitness = x.best
Best_Pos = x.bestIndividual

''' ------------------------ 绘图 ----------------------------------'''
part1 = ['BWO',Function_name]
name1 = ' '.join(part1)
plt.figure(1)
plt.semilogy(IterCurve, 'r-', linewidth=2)
plt.xlabel('Iteration', fontsize='medium')
plt.ylabel("Fitness", fontsize='medium')
plt.grid()
plt.title(name1, fontsize='large')
label = [name1]
plt.legend(label, loc='upper right')
plt.savefig('./BWO_Python.jpg')
plt.show()

