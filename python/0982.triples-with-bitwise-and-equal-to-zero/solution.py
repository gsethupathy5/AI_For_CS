# Created by asetti2002 at 2024/04/25 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] & nums[j] & nums[k] == 0:
                        count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countTriplets(nums)
    print("\noutput:", serialize(ans, "integer"))
