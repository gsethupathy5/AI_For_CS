# Created by asetti2002 at 2024/04/25 19:38
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-range-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            a = max(nums[-1], nums[i] + 2 * k)
            b = min(nums[0] + 2 * k, nums[i + 1])
            ans = min(ans, a - b)
        return ans
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRangeII(nums, k)
    print("\noutput:", serialize(ans, "integer"))
