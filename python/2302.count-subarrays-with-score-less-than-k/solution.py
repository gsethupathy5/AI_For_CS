# Created by asetti2002 at 2024/05/01 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_product = 1
        start = 0

        for end in range(len(nums)):
            prefix_product *= nums[end]

            while prefix_product >= k and start <= end:
                prefix_product /= nums[start]
                start += 1

            if prefix_product < k:
                res += end - start + 1

        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, k)
    print("\noutput:", serialize(ans, "long"))
