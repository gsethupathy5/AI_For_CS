# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-increasing-subsequence-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().lengthOfLIS(nums, k)
    print("\noutput:", serialize(ans, "integer"))
