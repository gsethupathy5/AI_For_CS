# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countTriplets(arr)
    print("\noutput:", serialize(ans, "integer"))
