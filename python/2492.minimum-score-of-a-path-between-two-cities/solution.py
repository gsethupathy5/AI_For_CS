# Created by asetti2002 at 2024/05/01 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        import heapq
        
        graph = {}
        for road in roads:
            a, b, dist = road
            if a not in graph:
                graph[a] = []
            graph[a].append((b, dist))
            if b not in graph:
                graph[b] = []
            graph[b].append((a, dist))
        
        min_score = [float('inf')] * (n + 1)
        min_score[1] = 0
        
        heap = [(0, 1)]
        while heap:
            cur_dist, cur_city = heapq.heappop(heap)
            if cur_dist > min_score[cur_city]:
                continue
            for next_city, next_dist in graph.get(cur_city, []):
                score = max(cur_dist, next_dist)
                if score < min_score[next_city]:
                    min_score[next_city] = score
                    heapq.heappush(heap, (score, next_city))
        
        return min_score[n]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minScore(n, roads)
    print("\noutput:", serialize(ans, "integer"))
