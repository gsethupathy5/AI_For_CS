# Created by asetti2002 at 2024/04/25 20:43
# leetgo: 1.4.3
# https://leetcode.com/problems/simplified-fractions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    res.append(f"{j}/{i}")
        return res
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().simplifiedFractions(n)
    print("\noutput:", serialize(ans, "string[]"))
