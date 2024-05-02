# Created by asetti2002 at 2024/05/01 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-arithmetic-triplets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        num_set = set(nums)
        for j in range(1, len(nums)):
            if nums[j] - diff in num_set and nums[j] + diff in num_set:
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    diff: int = deserialize("int", read_line())
    ans = Solution().arithmeticTriplets(nums, diff)
    print("\noutput:", serialize(ans, "integer"))
