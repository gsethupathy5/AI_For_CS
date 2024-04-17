# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().constructDistancedSequence(n)
    print("\noutput:", serialize(ans, "integer[]"))
