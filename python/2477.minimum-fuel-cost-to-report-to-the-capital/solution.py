# Created by asetti2002 at 2024/05/01 20:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list = collections.defaultdict(list)
        for road in roads:
            adj_list[road[0]].append(road[1])
        visited = set()
        
        def dfs(node):
            if node == 0:
                return 0
            visited.add(node)
            total_fuel = seats
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    total_fuel += dfs(neighbor)
            return total_fuel
        
        return dfs(0) - seats
# @lc code=end

if __name__ == "__main__":
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    seats: int = deserialize("int", read_line())
    ans = Solution().minimumFuelCost(roads, seats)
    print("\noutput:", serialize(ans, "long"))
