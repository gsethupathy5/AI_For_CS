# Created by asetti2002 at 2024/05/01 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-xor-after-operations/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumXOR(nums)
    print("\noutput:", serialize(ans, "integer"))
