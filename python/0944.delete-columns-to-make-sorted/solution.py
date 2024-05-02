# Created by asetti2002 at 2024/04/25 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-columns-to-make-sorted/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(1 for col in zip(*strs) if list(col) != sorted(col))
# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minDeletionSize(strs)
    print("\noutput:", serialize(ans, "integer"))
