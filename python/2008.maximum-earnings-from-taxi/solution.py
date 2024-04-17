# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-earnings-from-taxi/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rides: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTaxiEarnings(n, rides)
    print("\noutput:", serialize(ans, "long"))
