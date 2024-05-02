# Created by asetti2002 at 2024/04/25 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            else:
                if k % 2 == 0:
                    break
                if i > 0 and abs(nums[i-1]) < abs(nums[i]):
                    nums[i-1] = -nums[i-1]
                else:
                    nums[i] = -nums[i]
                break
            i += 1
        return sum(nums)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().largestSumAfterKNegations(nums, k)
    print("\noutput:", serialize(ans, "integer"))
