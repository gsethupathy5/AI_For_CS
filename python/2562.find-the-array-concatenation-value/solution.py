# Created by asetti2002 at 2024/05/01 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-array-concatenation-value/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_val = 0
        while len(nums) > 0:
            if len(nums) > 1:
                first = str(nums[0])
                last = str(nums[-1])
                concat_val += int(first + last)
                nums = nums[1:-1]
            else:
                concat_val += nums[0]
                nums = []
        return concat_val
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findTheArrayConcVal(nums)
    print("\noutput:", serialize(ans, "long"))
