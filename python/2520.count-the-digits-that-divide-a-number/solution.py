# Created by asetti2002 at 2024/05/01 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for digit in str(num):
            if int(digit) != 0 and num % int(digit) == 0:
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().countDigits(num)
    print("\noutput:", serialize(ans, "integer"))
