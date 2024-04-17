# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/substring-xor-queries/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().substringXorQueries(s, queries)
    print("\noutput:", serialize(ans, "integer[][]"))
