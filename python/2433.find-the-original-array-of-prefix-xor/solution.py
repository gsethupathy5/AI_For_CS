# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    pref: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findArray(pref)
    print("\noutput:", serialize(ans, "integer[]"))
