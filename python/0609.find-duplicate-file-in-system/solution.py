# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/find-duplicate-file-in-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    paths: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findDuplicate(paths)
    print("\noutput:", serialize(ans, "string[][]"))
