# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-palindrome-with-fixed-length/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    queries: List[int] = deserialize("List[int]", read_line())
    intLength: int = deserialize("int", read_line())
    ans = Solution().kthPalindrome(queries, intLength)
    print("\noutput:", serialize(ans, "long[]"))
