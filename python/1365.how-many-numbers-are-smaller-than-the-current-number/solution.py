# Created by asetti2002 at 2024/04/25 20:34
# leetgo: 1.4.3
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallerNumbersThanCurrent(nums)
    print("\noutput:", serialize(ans, "integer[]"))
