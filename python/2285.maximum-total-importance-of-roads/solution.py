# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-total-importance-of-roads/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumImportance(n, roads)
    print("\noutput:", serialize(ans, "long"))
