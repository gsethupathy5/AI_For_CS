# Created by asetti2002 at 2024/04/25 20:26
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calculate_sum(divisor):
            total = 0
            for num in nums:
                total += -(-num // divisor)
            return total

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if calculate_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().smallestDivisor(nums, threshold)
    print("\noutput:", serialize(ans, "integer"))
