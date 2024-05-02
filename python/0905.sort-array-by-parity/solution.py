# Created by asetti2002 at 2024/04/25 19:37
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-array-by-parity/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortArrayByParity(nums)
    print("\noutput:", serialize(ans, "integer[]"))
