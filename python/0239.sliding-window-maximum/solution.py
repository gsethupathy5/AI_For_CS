# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/sliding-window-maximum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSlidingWindow(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))