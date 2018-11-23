# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:01:35 2018

@author: XPS13
"""

# 先判断Range，是不是在[-(2**31), 2**31-1]之间，随后再进行翻转
class Solution(object):
    def within_range(self, number):
        if number < -(2**31) or number > 2**31 - 1:
            return False
        else:
            return True
    def reverse(self, x):
        if x == 0:
            return 0
        ret = 0
        flag = 0 if x < 0 else 1
        if self.within_range(x):
            x = abs(x)
            while(x != 0):
                ret = ret * 10 + x % 10 
                x = x // 10
        else:
            return 0
        return ret if flag == 1 else -ret

x = 1534236469
sol = Solution()
s = sol.reverse(x)