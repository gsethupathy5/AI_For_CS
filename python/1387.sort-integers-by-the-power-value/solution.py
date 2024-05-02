# Created by asetti2002 at 2024/04/25 20:35
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-integers-by-the-power-value/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                count += 1
            return count

        arr = []
        for i in range(lo, hi + 1):
            arr.append((power(i), i))

        arr.sort()
        return arr[k - 1][1]
# @lc code=end

if __name__ == "__main__":
    lo: int = deserialize("int", read_line())
    hi: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getKth(lo, hi, k)
    print("\noutput:", serialize(ans, "integer"))
