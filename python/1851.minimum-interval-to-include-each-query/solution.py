# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-interval-to-include-each-query/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minInterval(intervals, queries)
    print("\noutput:", serialize(ans, "integer[]"))
