# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/similar-string-groups/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(a, b):
            diff = [(x, y) for x, y in zip(a, b) if x != y]
            return len(diff) == 2 and diff[0] == diff[1][::-1]

        def dfs(node):
            for nei, sim in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        n = len(strs)
        n_word = len(strs[0])
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    graph[i].append((j, True))
                    graph[j].append((i, True))

        groups = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                groups += 1
                seen.add(i)
                dfs(i)

        return groups
# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numSimilarGroups(strs)
    print("\noutput:", serialize(ans, "integer"))
