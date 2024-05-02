# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-deletions-on-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def deleteString(self, s: str) -> int:
        cnt = 1
        while cnt * 2 <= len(s) and s[:cnt] == s[cnt:cnt * 2]:
            cnt += 1
        return min(cnt, len(s))
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().deleteString(s)
    print("\noutput:", serialize(ans, "integer"))
