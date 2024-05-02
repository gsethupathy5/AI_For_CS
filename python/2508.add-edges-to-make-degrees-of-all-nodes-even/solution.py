# Created by asetti2002 at 2024/05/01 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        def isEvenDegree(node_count, edge_count):
            deg = [0] * (node_count + 1)
            for edge in edges:
                deg[edge[0]] += 1
                deg[edge[1]] += 1
            
            result = 0
            for i in range(1, node_count + 1):
                if deg[i] % 2 != 0:
                    result += 1
            
            return result == 0 or result == 2
        
        return isEvenDegree(n, len(edges))
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isPossible(n, edges)
    print("\noutput:", serialize(ans, "boolean"))
