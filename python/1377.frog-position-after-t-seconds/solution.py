# Created by asetti2002 at 2024/04/25 20:36
# leetgo: 1.4.3
# https://leetcode.com/problems/frog-position-after-t-seconds/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        prob = [0] * (n + 1)
        prob[1] = 1.0
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for _ in range(t):
            new_prob = [0] * (n + 1)
            for node in range(1, n + 1):
                if prob[node] > 0:
                    neighbors = [neighbor for neighbor in graph[node] if prob[neighbor] == 0]
                    if neighbors:
                        for neighbor in neighbors:
                            new_prob[neighbor] += prob[node] / len(neighbors)
                    else:
                        new_prob[node] += prob[node]
            prob = new_prob
        
        return prob[target]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    t: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().frogPosition(n, edges, t, target)
    print("\noutput:", serialize(ans, "double"))
