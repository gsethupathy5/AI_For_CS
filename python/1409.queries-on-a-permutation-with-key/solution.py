# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/queries-on-a-permutation-with-key/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    queries: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().processQueries(queries, m)
    print("\noutput:", serialize(ans, "integer[]"))
