# Created by asetti2002 at 2024/05/01 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    lower: int = deserialize("int", read_line())
    upper: int = deserialize("int", read_line())
    ans = Solution().countFairPairs(nums, lower, upper)
    print("\noutput:", serialize(ans, "long"))
