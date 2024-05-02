# Created by asetti2002 at 2024/04/25 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-common-supersequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(X, Y, m, n):
            if m == 0 or n == 0:
                return 0
            elif X[m-1] == Y[n-1]:
                return 1 + lcs(X, Y, m-1, n-1)
            else:
                return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
        
        def shortestSequence(X, Y, m, n):
            index = lcs(X, Y, m, n)
            result = ""
            i = m
            j = n
            while i > 0 and j > 0:
                if X[i-1] == Y[j-1]:
                    result += X[i-1]
                    i -= 1
                    j -= 1
                elif lcs(X, Y, i-1, j) > lcs(X, Y, i, j-1):
                    result += X[i-1]
                    i -= 1
                else:
                    result += Y[j-1]
                    j -= 1
            while i > 0:
                result += X[i-1]
                i -= 1
            while j > 0:
                result += Y[j-1]
                j -= 1
            return result[::-1]
        
        return shortestSequence(str1, str2, len(str1), len(str2))
# @lc code=end

if __name__ == "__main__":
    str1: str = deserialize("str", read_line())
    str2: str = deserialize("str", read_line())
    ans = Solution().shortestCommonSupersequence(str1, str2)
    print("\noutput:", serialize(ans, "string"))
