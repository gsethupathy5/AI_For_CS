# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-duplicate-folders-in-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    paths: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().deleteDuplicateFolder(paths)
    print("\noutput:", serialize(ans, "string[][]"))
