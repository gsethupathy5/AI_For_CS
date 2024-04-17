# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    requests: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxSumRangeQuery(nums, requests)
    print("\noutput:", serialize(ans, "integer"))
