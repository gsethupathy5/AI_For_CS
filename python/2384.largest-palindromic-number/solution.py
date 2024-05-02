# Created by asetti2002 at 2024/05/01 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-palindromic-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestPalindromic(self, num: str) -> str:
        digits = sorted(num, reverse=True)
        result = []
        for digit in digits:
            if digit == '0' and not result:
                return '0'
            if digit != '0':
                result.append(digit)
        mid = ''
        for digit in result:
            if digit != '0' and digit == digits[len(digits) // 2]:
                mid = digit
            else:
                result.append(digit)
        return ''.join(result) + mid + ''.join(result[::-1])
# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().largestPalindromic(num)
    print("\noutput:", serialize(ans, "string"))
