# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    startPos: List[int] = deserialize("List[int]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().executeInstructions(n, startPos, s)
    print("\noutput:", serialize(ans, "integer[]"))
