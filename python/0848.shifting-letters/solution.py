# Created by asetti2002 at 2024/04/25 19:30
# leetgo: 1.4.3
# https://leetcode.com/problems/shifting-letters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shifts) % 26
        result = []
        for i, char in enumerate(s):
            shift = (ord(char) - ord('a') + total_shift) % 26
            result.append(chr(ord('a') + shift))
            total_shift = (total_shift - shifts[i]) % 26
        return "".join(result)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    shifts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().shiftingLetters(s, shifts)
    print("\noutput:", serialize(ans, "string"))
