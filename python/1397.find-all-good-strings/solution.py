# Created by asetti2002 at 2024/04/25 20:38
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-good-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
  
        def buildKMP(pat):
            m = len(pat)
            kmp = [0] * (m + 1)
            i, j = 0, -1
            kmp[0] = -1
            while i < m:
                while j >= 0 and pat[i] != pat[j]:
                    j = kmp[j]
                i += 1
                j += 1
                kmp[i] = j
            return kmp
        
        kmp = buildKMP(evil)
        def dfs(i, pre, prefixMatched, s1Pre, s2Pre):
            if prefixMatched:
                return 0
            
            if i == n:
                return 1
            
            a, b = 'a', 'z'
            if i < len(s1):
                a = s1[i]
            if i < len(s2):
                b = s2[i]
            
            res = 0
            for c in range(ord(a), ord(b) + 1):
                matchLength = prefixMatched
                while matchLength >= 0 and chr(c) != evil[matchLength]: 
                    matchLength = kmp[matchLength]
                if matchLength + 1 == len(evil):
                    continue
                
                prefixMatched = matchLength + 1 == len(evil)
                res += dfs(i + 1, pre * 26 + c - ord('a'), prefixMatched, s1 == s1[:i] + chr(c), s2Pre & (s2[:i] == s2Pre))
                res = res % MOD
            return res
        
        return dfs(0, 0, False, '', True) - 1

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    evil: str = deserialize("str", read_line())
    ans = Solution().findGoodStrings(n, s1, s2, evil)
    print("\noutput:", serialize(ans, "integer"))
