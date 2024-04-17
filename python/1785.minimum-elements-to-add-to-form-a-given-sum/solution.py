# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    goal: int = deserialize("int", read_line())
    ans = Solution().minElements(nums, limit, goal)
    print("\noutput:", serialize(ans, "integer"))
