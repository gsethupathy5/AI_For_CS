# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/compare-version-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    version1: str = deserialize("str", read_line())
    version2: str = deserialize("str", read_line())
    ans = Solution().compareVersion(version1, version2)
    print("\noutput:", serialize(ans, "integer"))
