# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    numbers: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(numbers, target)
    print("\noutput:", serialize(ans, "integer[]"))
