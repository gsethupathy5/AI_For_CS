# Created by asetti2002 at 2024/04/25 20:29
# leetgo: 1.4.3
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[1]].add(edge[0])
        
        def dfs(node):
            result = set()
            stack = [node]
            while stack:
                current = stack.pop()
                for parent in graph[current]:
                    result.add(parent)
                    stack.append(parent)
            return sorted(list(result))
        
        return [dfs(i) for i in range(n)]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getAncestors(n, edges)
    print("\noutput:", serialize(ans, "integer[][]"))
