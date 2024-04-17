# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/build-an-array-with-stack-operations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().buildArray(target, n)
    print("\noutput:", serialize(ans, "string[]"))
