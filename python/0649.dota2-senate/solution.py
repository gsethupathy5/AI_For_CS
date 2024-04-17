# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/dota2-senate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    senate: str = deserialize("str", read_line())
    ans = Solution().predictPartyVictory(senate)
    print("\noutput:", serialize(ans, "string"))
