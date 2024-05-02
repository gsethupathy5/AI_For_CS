# Created by asetti2002 at 2024/05/01 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/match-substring-after-replacement/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        def dfs(s, sub):
            if len(sub) == 0:
                return True
            if len(s) < len(sub):
                return False
            if sub[0] not in mapping:
                return any(dfs(s[i+1:], sub[1:]) for i in range(len(s)))
            for old, new in mapping[sub[0]]:
                if s.startswith(old):
                    if dfs(s[1:], sub[1:]):
                        return True
            return False
        
        mapping = {}
        for old, new in mappings:
            if old not in mapping:
                mapping[old] = set()
            mapping[old].add(new)
        
        return dfs(s, sub)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    sub: str = deserialize("str", read_line())
    mappings: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().matchReplacement(s, sub, mappings)
    print("\noutput:", serialize(ans, "boolean"))
