# Created by asetti2002 at 2024/04/25 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/tuple-with-same-product/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        import collections
        res = 0
        count = collections.Counter()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res += 8 * count[nums[i] * nums[j]]
                count[nums[i] * nums[j]] += 1
        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().tupleSameProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
