# Created by asetti2002 at 2024/04/25 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-town-judge/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        
        return -1
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    trust: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findJudge(n, trust)
    print("\noutput:", serialize(ans, "integer"))
