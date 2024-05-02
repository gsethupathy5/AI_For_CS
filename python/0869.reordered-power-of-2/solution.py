# Created by asetti2002 at 2024/04/25 19:33
# leetgo: 1.4.3
# https://leetcode.com/problems/reordered-power-of-2/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def checkPower(num):
            return bin(num).count('1') == 1
        
        return any(checkPower(int(''.join(num))) for num in permutations(str(n)))
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().reorderedPowerOf2(n)
    print("\noutput:", serialize(ans, "boolean"))
