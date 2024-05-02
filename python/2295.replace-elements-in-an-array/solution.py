# Created by asetti2002 at 2024/05/01 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/replace-elements-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        new_nums = nums.copy()
        for operation in operations:
            new_nums[new_nums.index(operation[0])] = operation[1]
        return new_nums
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    operations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().arrayChange(nums, operations)
    print("\noutput:", serialize(ans, "integer[]"))
