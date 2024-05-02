# Created by asetti2002 at 2024/05/01 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-total-importance-of-roads/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for road in roads:
            a, b = road
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        values = [-1] * n
        
        def dfs(node, val):
            visited[node] = True
            values[node] = val
            importance = 0
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    importance += val + dfs(neighbor, n - val)
            return importance
        
        return dfs(0, n)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumImportance(n, roads)
    print("\noutput:", serialize(ans, "long"))
