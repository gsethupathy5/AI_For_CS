# Created by asetti2002 at 2024/05/01 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumScore(nums, edges)
    print("\noutput:", serialize(ans, "integer"))
