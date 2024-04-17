# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/reverse-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    s: List[str] = deserialize("List[str]", read_line())
    reverseString(s)
    ans = s
    print("\noutput:", serialize(ans, "List[str]"))
