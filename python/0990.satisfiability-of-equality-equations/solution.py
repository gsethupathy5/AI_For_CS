# Created by asetti2002 at 2024/04/25 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
        
        uf = {chr(i): chr(i) for i in range(97, 123)}
        
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])
        
        return all(find(eq[0]) != find(eq[3]) if eq[1:3] == "!=" else find(eq[0]) == find(eq[3]) for eq in equations)
# @lc code=end

if __name__ == "__main__":
    equations: List[str] = deserialize("List[str]", read_line())
    ans = Solution().equationsPossible(equations)
    print("\noutput:", serialize(ans, "boolean"))
