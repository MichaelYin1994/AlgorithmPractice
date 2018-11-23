# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:39:08 2018

@author: XPS13
"""
import random
import time
import matplotlib.pyplot as plt
import seaborn as sns
from random import shuffle
sns.set(style='dark', font_scale=1.2, palette='deep', color_codes=True)

###############################################################################
class Sort(object):
    def __init__(self, array):
        self._array = array
        self._compares = 0
        self._arrayAccess = 0
        self._arraySize = len(self._array)
        
    def less(self, pos_1, pos_2):
        self._compares += 1
        return self._array[pos_1] <= self._array[pos_2]
        
    def exchange(self, pos_1, pos_2):
        tmp = self._array[pos_1]
        self._array[pos_1] = self._array[pos_2]
        self._array[pos_2] = tmp
        self._arrayAccess += 3
    
    def check(self):
        flag = False
        for i in range(0, len(self._array)-1):
            if self._array[i] <= self._array[i+1] :
                continue
            else:
                return flag
        flag = True
        return flag
###############################################################################
class SelectionSort(Sort):
    def __init__(self, array):
        super(SelectionSort, self).__init__(array)
    
    def sort(self):
        start = time.clock()
        for i in range(self._arraySize):
            minPos = i
            for j in range(i+1, self._arraySize):
                if self.less(j, minPos):
                    minPos = j
            if i != minPos:
                self.exchange(i, minPos)
        end = time.clock()
        print("=======================================================")
        print("Sorting results : ^^^", self.check())
        print("Running time is {}.".format(end-start))
        print("Total array access is {}.".format(self._arrayAccess))
        print("Total compares is {}.".format(self._compares))
        print("=======================================================")
        return self._array
###############################################################################
class InsertionSort(Sort):
    def __init__(self, array):
        super(InsertionSort, self).__init__(array)
    
    def sort(self):
        start = time.clock()
        for i in range(1, self._arraySize):
            for j in range(i, 0, -1):
                if self.less(j, j-1):
                    self.exchange(j-1, j)
        end = time.clock()
        print("=======================================================")
        print("Sorting results : ^^^", self.check())
        print("Running time is {}.".format(end-start))
        print("Total array access is {}.".format(self._arrayAccess))
        print("Total compares is {}.".format(self._compares))
        print("=======================================================")
        return self._array
###############################################################################
class ShellSort(Sort):
    def __init__(self, array):
        super(ShellSort, self).__init__(array)
    
    def sort(self):
        start = time.clock()
        # 生成最优的gap序列，其中gap初始的迭代值为1
        gap = 1
        while( gap < self._arraySize):
            gap = 3 * gap + 1
        
        # 对gap上的数据进行插入排序，终止条件为gap < 1，即是插排步长小于1
        while (gap >= 1):
            for i in range(gap, self._arraySize):
                for j in range(i, 0, -gap):
                    if self.less(j, j-gap):
                        self.exchange(j-gap, j)
            gap = gap // 3
        end = time.clock()
        print("=======================================================")
        print("Sorting results :{}".format(self.check()))
        print("Running time is {}.".format(end-start))
        print("Total array access is {}.".format(self._arrayAccess))
        print("Total compares is {}.".format(self._compares))
        print("=======================================================")
        
        return self._array
###############################################################################        
class MergeSort(Sort):
    def __init__(self, array):
        super(MergeSort, self).__init__(array)
        
    def merge(self, low, mid, high):
        aux = []
        i = low
        j = mid + 1
        for k in range(low, high+1):
            # Status 1：low的部分数组用完，j++即可
            if (i > mid):
                aux.append(self._array[j])
                j += 1
            # Status 2：high的部分数组用完，i++即可
            elif (j > high):
                aux.append(self._array[i])
                i += 1
            # Status 3：j数据比i数据要小，交换i与j元素的位置。但是不能
            # 保证第j+1位的情况，所以j += 1。并且要严格从aux数组取值！
            # 不能交换位置！
            elif (self._array[j] < self._array[i]):
                aux.append(self._array[j])
                j += 1
            else:
                # 移动低位
                aux.append(self._array[i])
                i += 1
        self._array[low:(high+1)] = aux
    
    def recursion_merge_sort(self, low, high):
        if (high <= low):
            return
        mid = low + (high - low) // 2
        self.recursion_merge_sort(low, mid)
        self.recursion_merge_sort(mid+1, high)
        self.merge(low, mid, high)
    
    def sort(self):
        low = 0
        high = self._arraySize - 1
        start = time.clock()
        self.recursion_merge_sort(low, high)
        end = time.clock()
        
        print("=======================================================")
        print("Sorting results :{}".format(self.check()))
        print("Running time is {}.".format(end-start))
        print("Total array access is {}.".format(self._arrayAccess))
        print("Total compares is {}.".format(self._compares))
        print("=======================================================")
        return self._array
###############################################################################
class QuickSort(Sort):
    def __init__(self, array):
        super(QuickSort, self).__init__(array)
    
    # 来自网上的partition方式
    def partition(self, low, high):
            leftmark = low + 1
            rightmark = high
            
            while (True):
                while leftmark <= rightmark and self.less(leftmark, low):
                    leftmark = leftmark + 1
                while self.less(low, rightmark) and rightmark >= leftmark:
                    rightmark = rightmark -1
                if rightmark < leftmark:
                    break
                else:
                    self.exchange(leftmark, rightmark)
            self.exchange(low, rightmark)
            return rightmark
    # 自己版本的partition方式
    def my_partition(self, low, high):
        left = low + 1
        right = high
        
        while(True):
            # 注意while这里的语句先执行left与right的判断，再进行less的比较
            # 为的是防止数组的越界
            while left <= right and self.less(left, low):
                left += 1
            while right >= left and self.less(low, right):
                right -= 1
            if right < left:
                break
            else:
                self.exchange(left, right)
        self.exchange(low, right)
        return right
    
    def recursion_sort(self, low, high):
        if low >= high:
            return
        splitPoint = self.my_partition(low, high)
        self.recursion_sort(low, splitPoint-1)
        self.recursion_sort(splitPoint+1, high)
    
    def sort(self):
        low = 0
        high = self._arraySize - 1
        start = time.time()
        self.recursion_sort(low, high)
        end = time.time()
        
        print("=======================================================")
        print("Sort method is {}".format(self.__class__))
        print("Running time is {}.".format(end-start))
        print("Sorting results :{}".format(self.check()))
        print("=======================================================")
        return self._array
###############################################################################    
class HeapSort(Sort):
    def __init__(self, array):
        super(HeapSort, self).__init__(array)
    
    # 下沉函数，让较大的父亲节点向下沉
    def sink(self, k):
        while(k * 2 <= self._arraySize):
            left = 2 * k + 1
            right = 2 * k + 2
            maxIndex = k
            # 改变self.less()的比较次序，就可以决定是构建最大堆还是最小堆
            if (left < self._arraySize and self.less(left, maxIndex)):
                maxIndex = left
            if (right < self._arraySize and self.less(right, maxIndex)):
                maxIndex = right
            if maxIndex == k:
                break
            self.exchange(k, maxIndex)
            # 继续下沉节点
            k = maxIndex
            
    def build_heap(self):
        # 从中间节点开始算其子节点，随后向下沉父亲节点
        # 从子树保证堆有序，那么整个堆就有序了
        for k in range(self._arraySize//2-1, -1, -1):
            self.sink(k)
    
    def sort(self):
        sortedArray = []
        self.build_heap()
        start = time.time()
        for i in range(self._arraySize-1, -1, -1):
            sortedArray.append(self._array[0])
            self.exchange(0, self._arraySize-1)
            del self._array[-1]
            self._arraySize -= 1
            self.sink(0)
        end = time.time()
        print("=======================================================")
        print("Sort method is {}".format(self.__class__))
        print("Running time is {}.".format(end-start))
        print("Sorting results :{}".format(self.check()))
        print("=======================================================")
        return sortedArray

###############################################################################
if __name__ == "__main__":
    # 生成测试数组并随机选择数组中的几个数
    testData = random.sample(range(0, 100000, 1), 30000)
    testData = testData + testData
    #testData = [random.choice(testData) for _ in testData]
    
    # 测试排序算法
    q = QuickSort(testData.copy())
    quickSortArray = q.sort()
    h = HeapSort(testData.copy())
    heapSortArray = h.sort()
    m = MergeSort(testData.copy())
    mergeSortArray = m.sort()
    