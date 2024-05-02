# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-xor/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countSetBits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        bits_num = countSetBits(num2)
        x = (2 ** bits_num) - 1
        return x
# @lc code=end

if __name__ == "__main__":
    num1: int = deserialize("int", read_line())
    num2: int = deserialize("int", read_line())
    ans = Solution().minimizeXor(num1, num2)
    print("\noutput:", serialize(ans, "integer"))
