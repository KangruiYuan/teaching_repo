import math
import time

import numpy as np


def normalize(x):  # 单位化向量
    norm = math.sqrt(sum(e**2 for e in x))
    return x / norm


def sign(a):  # 符号函数
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


def f(x):
    return 3 * np.cos(x[0] * x[1]) + x[0] + x[1] ** 2


def boundary(x):
    return np.clip(x, -4, 4)


time_start = time.time()  # 计时器

eta = 0.999  # 步长调整比例
iter = 100  # 迭代次数
step = 1  # 初始搜索步长
d0 = 5  # 触须间距
k = 2  # 变量维数
x = boundary(np.random.rand(k))  # 随机生成天牛质心坐标
global_best = 100
global_best_x = (0, 0)
for i in range(iter):  # 开始迭代
    dir = np.random.rand(k)
    dir = normalize(dir)
    xl = boundary(x + d0 * dir / 2)
    xr = boundary(x - d0 * dir / 2)
    fl = f(xl)
    fr = f(xr)
    x = boundary(x - step * dir * sign(fl - fr))
    step *= eta
    if f(x) < global_best:
        global_best_x = x
        global_best = f(x)

    print(global_best_x, global_best)

time_end = time.time()
print("time cost", time_end - time_start, "s")
