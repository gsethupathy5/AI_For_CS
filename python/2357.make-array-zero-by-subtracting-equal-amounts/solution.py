# Created by asetti2002 at 2024/05/01 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_num = min(filter(None, nums))
        count = 0
        for num in nums:
            if num > 0:
                count += num // min_num
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
