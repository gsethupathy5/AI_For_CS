# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    bits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isOneBitCharacter(bits)
    print("\noutput:", serialize(ans, "boolean"))
