# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getMinSwaps(num, k)
    print("\noutput:", serialize(ans, "integer"))
