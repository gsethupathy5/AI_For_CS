# Created by asetti2002 at 2024/05/01 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums.sort()
        missing = 0
        for num in nums:
            if num <= missing:
                missing += num
            else:
                break
        return missing
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    value: int = deserialize("int", read_line())
    ans = Solution().findSmallestInteger(nums, value)
    print("\noutput:", serialize(ans, "integer"))
