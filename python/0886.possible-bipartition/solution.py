# Created by asetti2002 at 2024/04/25 19:35
# leetgo: 1.4.3
# https://leetcode.com/problems/possible-bipartition/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        from collections import defaultdict
        
        graph = defaultdict(list)
        group = [0] * (n+1)
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(person, g):
            if group[person] != 0:
                return group[person] == g
            
            group[person] = g
            for other in graph[person]:
                if not dfs(other, -g):
                    return False
            return True
        
        for i in range(1, n+1):
            if group[i] == 0 and not dfs(i, 1):
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    dislikes: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().possibleBipartition(n, dislikes)
    print("\noutput:", serialize(ans, "boolean"))
