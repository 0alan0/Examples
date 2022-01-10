from __future__ import print_function

    # package.module
    # ~~~~~~~~~~~~~~
    #
    # 舒尔特方格 25 / 36 / 49 / 64
    #
    # # 5 * 5如下， 即25个元素打乱后取值即可。


import random

def schulte(n):
    # '''return n*n'''

    # 打乱数字
    
    max = n * n
    numbers = list(range(1, max+1))
    random.shuffle(numbers)


    # 格式化输出
    print()
    print('-' * n*5)
    i = 0
    while i < max:
        print('|\t', end='')
        for x in numbers[i: i+n]:
            print(x, '\t', end='')
        print('|')
        i += n
    print('-' * n*5)

schulte(int(input()))
