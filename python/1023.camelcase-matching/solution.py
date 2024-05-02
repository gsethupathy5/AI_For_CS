# Created by asetti2002 at 2024/04/25 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/camelcase-matching/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for word in queries:
            i, j = 0, 0
            match = True
            while i < len(word) and j < len(pattern):
                if word[i] == pattern[j]:
                    i += 1
                    j += 1
                elif word[i].isupper():
                    match = False
                    break
                else:
                    i += 1
            if j < len(pattern):
                match = False
            while i < len(word):
                if word[i].isupper():
                    match = False
                    break
                i += 1
            res.append(match)
        return res
# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    pattern: str = deserialize("str", read_line())
    ans = Solution().camelMatch(queries, pattern)
    print("\noutput:", serialize(ans, "boolean[]"))
