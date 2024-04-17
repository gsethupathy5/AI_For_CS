# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/graph-connectivity-with-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    threshold: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().areConnected(n, threshold, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
