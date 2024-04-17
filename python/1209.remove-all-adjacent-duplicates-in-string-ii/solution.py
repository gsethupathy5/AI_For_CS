# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().removeDuplicates(s, k)
    print("\noutput:", serialize(ans, "string"))
