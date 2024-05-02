# Created by asetti2002 at 2024/04/25 20:30
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1
        
        parent = list(range(n))
        rank = [0] * n
        cables = 0
        
        for connection in connections:
            x, y = connection
            if find(x) != find(y):
                union(x, y)
            else:
                cables += 1
        
        sets = len(set(find(x) for x in range(n))) - cables
        return sets - 1 if cables >= sets else -1
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().makeConnected(n, connections)
    print("\noutput:", serialize(ans, "integer"))
