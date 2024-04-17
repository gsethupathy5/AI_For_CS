# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-original-array-from-doubled-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    changed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findOriginalArray(changed)
    print("\noutput:", serialize(ans, "integer[]"))
