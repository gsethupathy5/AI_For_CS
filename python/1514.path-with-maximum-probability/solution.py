# Created by asetti2002 at 2024/04/25 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/path-with-maximum-probability/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        import heapq
        
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        pq = [(-1, start_node)]
        visited = set()
        
        while pq:
            prob, node = heapq.heappop(pq)
            if node == end_node:
                return -prob
            
            if node in visited:
                continue
                
            visited.add(node)
            
            for nei, nei_prob in graph[node]:
                if nei not in visited:
                    heapq.heappush(pq, (prob * nei_prob, nei))
        
        return 0.0
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    succProb: List[float] = deserialize("List[float]", read_line())
    start_node: int = deserialize("int", read_line())
    end_node: int = deserialize("int", read_line())
    ans = Solution().maxProbability(n, edges, succProb, start_node, end_node)
    print("\noutput:", serialize(ans, "double"))
