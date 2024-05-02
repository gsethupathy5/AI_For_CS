# Created by asetti2002 at 2024/04/25 20:39
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 1
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            min_val = max(min_val, 1 - cur_sum)
        
        return min_val
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minStartValue(nums)
    print("\noutput:", serialize(ans, "integer"))
