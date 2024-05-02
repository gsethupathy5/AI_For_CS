# Created by asetti2002 at 2024/05/01 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        from collections import deque
        
        n = len(amount)
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def dfs(node, parent):
            best_profit = amount[node]
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                profit = dfs(neighbor, node)
                best_profit = max(best_profit, profit)
            return best_profit
        
        def find_max_profit(start):
            q = deque([(start, -1)])
            max_profit = amount[start]
            while q:
                node, parent = q.popleft()
                profit = amount[node]
                for neighbor in tree[node]:
                    if neighbor == parent:
                        continue
                    profit += dfs(neighbor, node)
                max_profit = max(max_profit, profit)
                for neighbor in tree[node]:
                    if neighbor != parent:
                        q.append((neighbor, node))
            return max_profit
        
        return find_max_profit(0)
# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    bob: int = deserialize("int", read_line())
    amount: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostProfitablePath(edges, bob, amount)
    print("\noutput:", serialize(ans, "integer"))
