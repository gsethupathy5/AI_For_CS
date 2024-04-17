# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    finalSum: int = deserialize("int", read_line())
    ans = Solution().maximumEvenSplit(finalSum)
    print("\noutput:", serialize(ans, "long[]"))
