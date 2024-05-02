# Created by asetti2002 at 2024/05/01 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/count-special-integers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if len(set(str(i))) == len(str(i)):
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countSpecialNumbers(n)
    print("\noutput:", serialize(ans, "integer"))
