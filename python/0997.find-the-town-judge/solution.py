# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-town-judge/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    trust: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findJudge(n, trust)
    print("\noutput:", serialize(ans, "integer"))
