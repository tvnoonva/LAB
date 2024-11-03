import random
from QuickSort import QuickSort
from VladimirQuickSort import VladimirQuickSort
import sys
import time
sys.setrecursionlimit(10**9)

def createList(size):
    return random.sample(range(1, size+1), size)

def QsortTimeCheck(list, size):
    sort = QuickSort(list)
    start = time.time()
    sort.sorting(0, size-1)
    end = time.time()
    print(f"Quick sort 진행 시간 {end-start:.5f} sec")

def VsortTimeCheck(list, size, n):
    sort = VladimirQuickSort(list)
    sort.nSetter(n) #n값 교체
    start = time.time()
    sort.sorting(0, size-1)
    end = time.time()
    print(f"Vladimir 알고리즘 sort 진행 시간 {end-start:.5f} sec, n값은 {n}")

def testing(size):
    test = createList(size)
    print(f"============test case {size}==============")
    QsortTimeCheck(test.copy(), size)
    VsortTimeCheck(test.copy(), size, 17)
    VsortTimeCheck(test.copy(), size, 33)
    VsortTimeCheck(test.copy(), size, 65)
    VsortTimeCheck(test.copy(), size, 129)
    VsortTimeCheck(test.copy(), size, 257)
    VsortTimeCheck(test.copy(), size, 513)

if __name__ == '__main__':
    #test case 10k
    size = 10000
    testing(size)

    #test case 100k
    size = 100000
    testing(size)

    #test case 200k
    size = 200000
    testing(size)

    #test case 400k
    size = 400000
    testing(size)

    #test case 800k
    size = 800000
    testing(size)

    #test case 1600k
    size = 1600000
    testing(size)

    #test case 3200k
    size = 3200000
    testing(size)
    
    #test case 6400k
    size = 6400000
    testing(size)
