# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[str] = deserialize("List[str]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestNumber(nums, k)
    print("\noutput:", serialize(ans, "string"))
