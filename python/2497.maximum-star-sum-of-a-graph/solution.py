# Created by asetti2002 at 2024/05/01 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        import collections
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        ans = 0
        for node in range(len(vals)):
            sum_val = vals[node]
            neighbors = 0
            for neighbor in graph[node]:
                sum_val += vals[neighbor]
                neighbors += 1
            if neighbors <= 1:
                continue
            ans = max(ans, sum_val)
        
        return ans
# @lc code=end

if __name__ == "__main__":
    vals: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxStarSum(vals, edges, k)
    print("\noutput:", serialize(ans, "integer"))
