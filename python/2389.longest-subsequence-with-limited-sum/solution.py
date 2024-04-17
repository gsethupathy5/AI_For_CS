# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().answerQueries(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
