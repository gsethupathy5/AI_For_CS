# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/count-pairs-of-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countPairs(n, edges, queries)
    print("\noutput:", serialize(ans, "integer[]"))
