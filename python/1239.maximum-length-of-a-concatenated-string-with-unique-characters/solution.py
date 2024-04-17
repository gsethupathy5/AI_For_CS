# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maxLength(arr)
    print("\noutput:", serialize(ans, "integer"))
