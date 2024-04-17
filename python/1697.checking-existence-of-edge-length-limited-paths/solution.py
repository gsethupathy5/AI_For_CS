# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edgeList: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().distanceLimitedPathsExist(n, edgeList, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
