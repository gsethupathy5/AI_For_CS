# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-array-by-parity-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortArrayByParityII(nums)
    print("\noutput:", serialize(ans, "integer[]"))
