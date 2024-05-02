# Created by asetti2002 at 2024/04/25 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-string-with-swaps/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        import collections
        
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
        
        uf = {i:i for i in range(len(s))}
        
        for x, y in pairs:
            union(x, y)
        
        groups = collections.defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(s[i])
        
        for group in groups:
            groups[group].sort(reverse=True)
        
        res = []
        for i in range(len(s)):
            res.append(groups[find(i)].pop())
        
        return "".join(res)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    pairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().smallestStringWithSwaps(s, pairs)
    print("\noutput:", serialize(ans, "string"))
