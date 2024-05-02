# Created by asetti2002 at 2024/04/25 20:26
# leetgo: 1.4.3
# https://leetcode.com/problems/palindrome-partitioning-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().palindromePartition(s, k)
    print("\noutput:", serialize(ans, "integer"))
