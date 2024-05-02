# Created by asetti2002 at 2024/04/25 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
        return count
# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minDeletionSize(strs)
    print("\noutput:", serialize(ans, "integer"))
