# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/count-good-triplets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().countGoodTriplets(arr, a, b, c)
    print("\noutput:", serialize(ans, "integer"))
