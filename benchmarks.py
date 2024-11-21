# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:46:20 2016

@author: Hossam Faris
"""

import numpy
import math

# define the function blocks
def prod(it):
    p = 1
    for n in it:
        p *= n
    return p


def Ufun(x, a, k, m):
    y = k * ((x - a) ** m) * (x > a) + k * ((-x - a) ** m) * (x < (-a))
    return y

#sphere
def F1(x):
    s = numpy.sum(x ** 2)
    return s

#schwefel`s 2.22
def F2(x):
    o = sum(abs(x)) + prod(abs(x))
    return o

#schwefel`s 1.2
def F3(x):
    dim = len(x) + 1
    o = 0
    for i in range(1, dim):
        o = o + (numpy.sum(x[0:i])) ** 2
    return o

#schewefel`s 2.21
def F4(x):
    o = max(abs(x))
    return o

#Rosenbrock
def F5(x):
    dim = len(x)
    o = numpy.sum(
        100 * (x[1:dim] - (x[0 : dim - 1] ** 2)) ** 2 + (x[0 : dim - 1] - 1) ** 2
    )
    return o

#step
def F6(x):
    o = numpy.sum(abs((x + 0.5)) ** 2)
    return o

#quartic
def F7(x):
    dim = len(x)

    w = [i for i in range(len(x))]
    for i in range(0, dim):
        w[i] = i + 1
    o = numpy.sum(w * (x ** 4)) + numpy.random.uniform(0, 1)
    return o


#powell sum
def F8(x):
    dim = len(x)
    for i in range(1,dim):
        o = numpy.sum(abs(x) ** (i+1))
    return o

def F9(x):
    dim = len(x)
    for i in range(0, dim):
        o = numpy.sum(x**2) + (numpy.sum(0.5 * i * x)) ** 2 + (numpy.sum(0.5 * (i + 1) * x)) ** 4
        return o

def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {
        "F1": ["F1", -100, 100, 30],
        "F2": ["F2", -10, 10, 30],
        "F3": ["F3", -100, 100, 30],
        "F4": ["F4", -100, 100, 30],
        "F5": ["F5", -30, 30, 30],
        "F6": ["F6", -100, 100, 30],
        "F7": ["F7", -1.28, 1.28, 30],
        "F8": ["F8", -500, 500, 30],
        "F9": ["F9", -5.12, 5.12, 30],

    }
    return param.get(a, "nothing")


def getFunctionSet(function_name):
    # 假设您有一个将函数名映射到函数对象的字典
    # 注意：这个字典需要您自己定义，因为Python不会自动为您创建它
    # 这里的示例仅用于说明如何构造和使用这样的字典
    function_objects = {
        "F1": ["F1", -100, 100, 30],
        "F2": ["F2", -10, 10, 30],
        "F3": ["F3", -100, 100, 30],
        "F4": ["F4", -100, 100, 30],
        "F5": ["F5", -30, 30, 30],
        "F6": ["F6", -100, 100, 30],
        "F7": ["F7", -1.28, 1.28, 30],
        "F8": ["F8", -500, 500, 30],
        "F9": ["F9", -5.12, 5.12, 30],

    }
    # 检索函数对象
    return function_objects.get(function_name, None)




'''
# ESAs space mission design benchmarks https://www.esa.int/gsp/ACT/projects/gtop/
from fcmaes.astro import (
    MessFull,
    Messenger,
    Gtoc1,
    Cassini1,
    Cassini2,
    Rosetta,
    Tandem,
    Sagas,
)
def Ca1(x):
    return Cassini1().fun(x)
def Ca2(x):
    return Cassini2().fun(x)
def Ros(x):
    return Rosetta().fun(x)
def Tan(x):
    return Tandem(5).fun(x)
def Sag(x):
    return Sagas().fun(x)
def Mef(x):
    return MessFull().fun(x)
def Mes(x):
    return Messenger().fun(x)
def Gt1(x):
    return Gtoc1().fun(x)

def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {
        "F1": ["F1", -100, 100, 30],
        "F2": ["F2", -10, 10, 30],
        "F3": ["F3", -100, 100, 30],
        "F4": ["F4", -100, 100, 30],
        "F5": ["F5", -30, 30, 30],
        "F6": ["F6", -100, 100, 30],
        "F7": ["F7", -1.28, 1.28, 30],
        "F8": ["F8", -500, 500, 30],
        "F9": ["F9", -5.12, 5.12, 30],
        "F10": ["F10", -32, 32, 30],
        "F11": ["F11", -600, 600, 30],
        "F12": ["F12", -50, 50, 30],
        "F13": ["F13", -50, 50, 30],
        "F14": ["F14", -65.536, 65.536, 2],
        "F15": ["F15", -5, 5, 4],
        "F16": ["F16", -5, 5, 2],
        "F17": ["F17", -5, 15, 2],
        "F18": ["F18", -2, 2, 2],
        "F19": ["F19", 0, 1, 3],
        "F20": ["F20", 0, 1, 6],
        "F21": ["F21", 0, 10, 4],
        "F22": ["F22", 0, 10, 4],
        "F23": ["F23", 0, 10, 4],
        "Ca1": [
            "Ca1",
            Cassini1().bounds.lb,
            Cassini1().bounds.ub,
            len(Cassini1().bounds.lb),
        ],
        "Ca2": [
            "Ca2",
            Cassini2().bounds.lb,
            Cassini2().bounds.ub,
            len(Cassini2().bounds.lb),
        ],
        "Gt1": ["Gt1", Gtoc1().bounds.lb, Gtoc1().bounds.ub, len(Gtoc1().bounds.lb)],
        "Mes": [
            "Mes",
            Messenger().bounds.lb,
            Messenger().bounds.ub,
            len(Messenger().bounds.lb),
        ],
        "Mef": [
            "Mef",
            MessFull().bounds.lb,
            MessFull().bounds.ub,
            len(MessFull().bounds.lb),
        ],
        "Sag": ["Sag", Sagas().bounds.lb, Sagas().bounds.ub, len(Sagas().bounds.lb)],
        "Tan": [
            "Tan",
            Tandem(5).bounds.lb,
            Tandem(5).bounds.ub,
            len(Tandem(5).bounds.lb),
        ],
        "Ros": [
            "Ros",
            Rosetta().bounds.lb,
            Rosetta().bounds.ub,
            len(Rosetta().bounds.lb),
        ],
    }
    return param.get(a, "nothing")
'''