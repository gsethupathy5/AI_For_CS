# Created by asetti2002 at 2024/04/25 19:29
# leetgo: 1.4.3
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # Implementation of the splitIntoFibonacci function
        # Your code here

        return []
# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().splitIntoFibonacci(num)
    print("\noutput:", serialize(ans, "integer[]"))
