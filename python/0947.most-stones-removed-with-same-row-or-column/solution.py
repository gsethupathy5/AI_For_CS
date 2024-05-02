# Created by asetti2002 at 2024/04/25 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x, y):
            visited.add((x, y))
            for i in rows[x]:
                if (x, i) not in visited:
                    dfs(x, i)
            for j in cols[y]:
                if (j, y) not in visited:
                    dfs(j, y)

        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)

        visited = set()
        components = 0
        for i, (x, y) in enumerate(stones):
            if (x, y) not in visited:
                components += 1
                dfs(x, y)
        
        return len(stones) - components
# @lc code=end

if __name__ == "__main__":
    stones: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().removeStones(stones)
    print("\noutput:", serialize(ans, "integer"))
