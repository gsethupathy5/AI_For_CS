# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-string-with-swaps/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    pairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().smallestStringWithSwaps(s, pairs)
    print("\noutput:", serialize(ans, "string"))
