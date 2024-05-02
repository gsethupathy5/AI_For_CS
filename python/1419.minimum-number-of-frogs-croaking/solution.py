# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = 0
        res = 0
        for char in croakOfFrogs:
            if char == 'c':
                cnt += 1
                res = max(res, cnt)
            elif char == 'k' or char == 'a' or char == 'o' or char == 'r':
                index = "croak".index(char)
                if cnt == 0 or "croak"[index-1] != croakOfFrogs[croakOfFrogs.index(char) - cnt]:
                    return -1
                cnt -= 1
            else:
                return -1
        return res if cnt == 0 else -1
# @lc code=end

if __name__ == "__main__":
    croakOfFrogs: str = deserialize("str", read_line())
    ans = Solution().minNumberOfFrogs(croakOfFrogs)
    print("\noutput:", serialize(ans, "integer"))
