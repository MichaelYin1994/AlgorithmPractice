# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:44:11 2018

@author: XPS13
"""
# 字典不停的找对应的值，键是与target差的值，值是序号
class Solution_1(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict.keys():
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
class Solution(object):
    def less(self, pos_1, pos_2):
        return self._array[pos_1] <= self._array[pos_2]
    
    def sort(self, low, high):
        if low >= high:
            return
        splitPoint = self.partition(low, high)
        self.sort(low, splitPoint-1)
        self.sort(splitPoint+1, high)
    
    def exchange(self, pos_1, pos_2):
        tmp = self._array[pos_1]
        self._array[pos_1] = self._array[pos_2]
        self._array[pos_2] = tmp
        
        tmp = self._index[pos_1]
        self._index[pos_1] = self._index[pos_2]
        self._index[pos_2] = tmp
        
    def partition(self, low, high):
        left = low + 1
        right = high
        
        while(True):
            while( left <= right and self.less(left, low)):
                left += 1
            while( right >= left and self.less(low, right)):
                right -= 1
            if left > right:
                break
            self.exchange(left, right)
        self.exchange(right, low)
        return right
    
    def binary_search(self, low, high, target, array):
        while(low <= high):
            mid = low + (high - low) // 2
            if array[mid] < target:
                low = mid + 1
            elif array[mid] > target:
                high = mid - 1
            elif array[mid] == target:
                return mid
        return None
    
    def twoSum(self, nums, target):
        self._array = nums
        self._arraySize = len(self._array)
        self._index = list(range(self._arraySize))
        self.sort(0, self._arraySize-1)
        
        for ind, item in enumerate(self._array):
            searchAim = target - item
            ret = self.binary_search(ind+1, self._arraySize, searchAim, self._array)
            if ret == None:
                continue
            else:
                break
        ret = [ind, self._index[ret]]
        ret.sort()
        return ret

if __name__ == "__main__":
    a = [9, 1, 7, 3, 12, 4, 51, 34]      
    s = Solution_1()
    ret = s.twoSum(a, 13)
        