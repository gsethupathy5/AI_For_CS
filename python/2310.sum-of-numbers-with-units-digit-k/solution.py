# Created by asetti2002 at 2024/04/25 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        elif k == 0:
            return -1
        elif num % k == 0:
            return num // k
        else:
            return num // k + 1
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumNumbers(num, k)
    print("\noutput:", serialize(ans, "integer"))
