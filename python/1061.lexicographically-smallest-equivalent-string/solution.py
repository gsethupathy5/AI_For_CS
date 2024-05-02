# Created by asetti2002 at 2024/04/25 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        base = {ch: ch for ch in baseStr}

        def find(ch):
            if ch not in parent:
                parent[ch] = ch
            if parent[ch] != ch:
                parent[ch] = find(parent[ch])
            return parent[ch]

        def union(ch1, ch2):
            root1 = find(ch1)
            root2 = find(ch2)
            if root1 < root2:
                parent[root2] = root1
            else:
                parent[root1] = root2

        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        for ch in parent:
            find(ch)

        result = []
        for ch in baseStr:
            result.append(parent[ch])

        return ''.join(result)
# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    baseStr: str = deserialize("str", read_line())
    ans = Solution().smallestEquivalentString(s1, s2, baseStr)
    print("\noutput:", serialize(ans, "string"))
