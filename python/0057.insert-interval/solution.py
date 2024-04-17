# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/insert-interval/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    newInterval: List[int] = deserialize("List[int]", read_line())
    ans = Solution().insert(intervals, newInterval)
    print("\noutput:", serialize(ans, "integer[][]"))
