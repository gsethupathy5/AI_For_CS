# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/k-divisible-elements-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    p: int = deserialize("int", read_line())
    ans = Solution().countDistinct(nums, k, p)
    print("\noutput:", serialize(ans, "integer"))
