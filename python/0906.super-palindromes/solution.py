# Created by asetti2002 at 2024/04/25 19:38
# leetgo: 1.4.3
# https://leetcode.com/problems/super-palindromes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        count = 0
        left = int(left)
        right = int(right)

        for i in range(10**5):
            s = str(i)
            l = int(s + s[::-1])
            if l * l > right:
                break
            if l * l >= left and is_palindrome(str(l * l)):
                count += 1

            for j in range(10):
                s = str(i)
                l = int(s + str(j) + s[::-1])
                if l * l > right:
                    break
                if l * l >= left and is_palindrome(str(l * l)):
                    count += 1

        return count
# @lc code=end

if __name__ == "__main__":
    left: str = deserialize("str", read_line())
    right: str = deserialize("str", read_line())
    ans = Solution().superpalindromesInRange(left, right)
    print("\noutput:", serialize(ans, "integer"))
