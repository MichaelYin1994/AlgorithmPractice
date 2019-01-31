# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 09:41:53 2018

@author: XPS13
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wordLength_1 = len(word1)
        wordLength_2 = len(word2)
       
        if wordLength_1 == 0:
            return wordLength_2
        elif wordLength_2 == 0:
            return wordLength_1
        
        # Initializing the dp matrix
        element = [None] * (wordLength_1 + 1)
        dp = []
        for ind, item in enumerate(range((wordLength_2 + 1))):
            element[0] = ind
            dp.append(element.copy())
        dp[0] = list(range(wordLength_1 + 1))
        
        # Fill the elements of the dp matrix
        for y in range(1, wordLength_2 + 1):
            for x in range(1, wordLength_1 + 1):
                if word1[x-1] == word2[y-1]:
                    tmp = 0
                else:
                    tmp = 2
                dp[y][x] = min(dp[y-1][x] + 1, dp[y][x-1] + 1, dp[y-1][x-1] + tmp)
        return dp[-1][-1]
       
if __name__ == "__main__":
    word1 = "intention"
    word2 = "excution"
   
    s = Solution()
    res = s.minDistance(word1, word2)