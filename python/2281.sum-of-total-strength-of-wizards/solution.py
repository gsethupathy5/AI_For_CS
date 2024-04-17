# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    strength: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalStrength(strength)
    print("\noutput:", serialize(ans, "integer"))
