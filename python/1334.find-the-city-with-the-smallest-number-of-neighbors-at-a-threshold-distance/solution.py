# Created by asetti2002 at 2024/04/25 20:32
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        import heapq
        
        graph = {i: {} for i in range(n)}
        for fromi, toi, weighti in edges:
            graph[fromi][toi] = weighti
            graph[toi][fromi] = weighti
        
        def dijkstra(start):
            dist = {node: float('inf') for node in graph}
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for neighbor, weight in graph[node].items():
                    if (new_dist := d + weight) < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
            return sum(1 for d in dist.values() if d <= distanceThreshold)
        
        min_city = None
        min_count = float('inf')
        for i in range(n):
            count = dijkstra(i)
            if count <= min_count:
                min_city = i
                min_count = count
        return min_city
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    distanceThreshold: int = deserialize("int", read_line())
    ans = Solution().findTheCity(n, edges, distanceThreshold)
    print("\noutput:", serialize(ans, "integer"))
