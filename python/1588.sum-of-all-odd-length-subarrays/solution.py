# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumOddLengthSubarrays(arr)
    print("\noutput:", serialize(ans, "integer"))
