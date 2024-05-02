# Created by asetti2002 at 2024/05/01 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/shifting-letters-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        result = ""
        shift_sum = 0
        for i in range(len(s) - 1, -1, -1):
            shift_sum = (shift_sum + shifts[i][2]) % 26
            result = chr(((ord(s[i]) - ord('a') + shift_sum) % 26) + ord('a')) + result
        return result
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    shifts: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shiftingLetters(s, shifts)
    print("\noutput:", serialize(ans, "string"))
