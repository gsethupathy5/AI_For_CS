# Created by asetti2002 at 2024/04/25 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/sequential-digits/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def generate(digits, current):
            num = int("".join(str(d) for d in current))
            if num > high:
                return
            if num >= low:
                result.append(num)
            if current[-1] < 9:
                current.append(current[-1] + 1)
                generate(digits, current)
            return
        
        result = []
        for i in range(1, 9):
            generate(i, [i])
        
        return sorted(result)
# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().sequentialDigits(low, high)
    print("\noutput:", serialize(ans, "integer[]"))
