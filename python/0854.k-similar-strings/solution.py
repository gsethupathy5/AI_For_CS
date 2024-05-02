# Created by asetti2002 at 2024/04/25 19:31
# leetgo: 1.4.3
# https://leetcode.com/problems/k-similar-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        from collections import deque
        q = deque([(s1, 0)])
        seen = set([s1])
        while q:
            s, cnt = q.popleft()
            if s == s2:
                return cnt
            for i in range(len(s)):
                if s[i] != s2[i]:
                    break
            for j in range(i + 1, len(s)):
                if s[j] == s2[i]:
                    ns = list(s)
                    ns[i], ns[j] = ns[j], ns[i]
                    ns = "".join(ns)
                    if ns not in seen:
                        seen.add(ns)
                        q.append((ns, cnt + 1))
# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().kSimilarity(s1, s2)
    print("\noutput:", serialize(ans, "integer"))
