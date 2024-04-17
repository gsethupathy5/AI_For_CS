# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    quality: List[int] = deserialize("List[int]", read_line())
    wage: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().mincostToHireWorkers(quality, wage, k)
    print("\noutput:", serialize(ans, "double"))
