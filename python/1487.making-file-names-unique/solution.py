# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/making-file-names-unique/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    names: List[str] = deserialize("List[str]", read_line())
    ans = Solution().getFolderNames(names)
    print("\noutput:", serialize(ans, "string[]"))
