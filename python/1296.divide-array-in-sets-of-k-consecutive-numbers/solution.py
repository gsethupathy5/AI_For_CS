# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().isPossibleDivide(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
