# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/gas-station/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    gas: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canCompleteCircuit(gas, cost)
    print("\noutput:", serialize(ans, "integer"))
