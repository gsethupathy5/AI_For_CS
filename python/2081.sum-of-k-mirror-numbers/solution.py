# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-k-mirror-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().kMirror(k, n)
    print("\noutput:", serialize(ans, "long"))
