# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:44:16 2018

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
class QuickSort(Sort):
    def __init__(self, array):
        super(QuickSort, self).__init__(array)
    def partition(self, low, high):
        left = low + 1
        right = high
        
        while(True):
            while(left <= right and self.less(left, low)):
                left += 1
            while(right >= left and self.less(low, right)):
                right -= 1
            if right < left:
                break
            self.exchange(left, right)
        return right
        
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
class MergeSort(Sort):
    def __init__(self, array):
        super(MergeSort, self).__init__(array)

    def my_merge(self, low, mid, high):
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
        if (low >= high):
            return
        mid = low + (high - low) // 2
        self.recursion_merge_sort(low, mid)
        self.recursion_merge_sort(mid+1, high)
        self.my_merge(low, mid, high)
    
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
if __name__ == "__main__":
    # 生成测试数组并随机选择数组中的几个数
    testData = random.sample(range(0, 50, 1), 10)
    testData = testData + testData
    #testData = [random.choice(testData) for _ in testData]
    
    # 测试排序算法
    q = MergeSort(testData.copy())
    quickSortArray = q.sort()
