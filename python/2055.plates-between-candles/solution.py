# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/plates-between-candles/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().platesBetweenCandles(s, queries)
    print("\noutput:", serialize(ans, "integer[]"))
