# Created by asetti2002 at 2024/05/01 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-greatness-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        
        for i in range(n):
            if nums[i] < nums[n // 2]:
                res += 1
        
        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximizeGreatness(nums)
    print("\noutput:", serialize(ans, "integer"))
