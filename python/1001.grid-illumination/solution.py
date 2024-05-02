# Created by asetti2002 at 2024/04/25 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/grid-illumination/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        pass
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    lamps: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().gridIllumination(n, lamps, queries)
    print("\noutput:", serialize(ans, "integer[]"))
