# Created by asetti2002 at 2024/05/01 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/naming-a-company/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    ideas: List[str] = deserialize("List[str]", read_line())
    ans = Solution().distinctNames(ideas)
    print("\noutput:", serialize(ans, "long"))
