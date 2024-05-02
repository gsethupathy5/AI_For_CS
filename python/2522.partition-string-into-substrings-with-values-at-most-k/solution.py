# Created by asetti2002 at 2024/05/01 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if any(int(d) > k for d in s):
            return -1
        count = 1
        cur_val = int(s[0])
        for i in range(1, len(s)):
            if cur_val + int(s[i]) > k:
                cur_val = int(s[i])
                count += 1
            else:
                cur_val += int(s[i])
        return count
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumPartition(s, k)
    print("\noutput:", serialize(ans, "integer"))
