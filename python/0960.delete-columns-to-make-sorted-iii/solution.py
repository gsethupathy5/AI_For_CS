# Created by asetti2002 at 2024/04/25 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        
        for j in range(1, n):
            for i in range(j):
                if all(row[i] <= row[j] for row in strs):
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return n - max(dp)
# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minDeletionSize(strs)
    print("\noutput:", serialize(ans, "integer"))
