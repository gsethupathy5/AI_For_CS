# Created by asetti2002 at 2024/04/25 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/flower-planting-with-no-adjacent/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Your solution here
        pass
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    paths: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().gardenNoAdj(n, paths)
    print("\noutput:", serialize(ans, "integer[]"))
