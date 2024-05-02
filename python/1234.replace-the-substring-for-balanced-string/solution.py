# Created by asetti2002 at 2024/04/25 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def balancedString(self, s: str) -> int:
        import collections
        count = collections.Counter(s)
        n = len(s)
        res = left = 0
        target = n // 4
        for right, char in enumerate(s):
            count[char] -= 1
            while left < n and all(count[c] <= target for c in 'QWER'):
                res = min(res, right - left + 1) if res != 0 else right - left + 1
                count[s[left]] += 1
                left += 1
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().balancedString(s)
    print("\noutput:", serialize(ans, "integer"))
