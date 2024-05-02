# Created by asetti2002 at 2024/04/25 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/powerful-integers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = []
        for i in range(int(log(bound, x)) + 2):
            for j in range(int(log(bound, y)) + 2):
                value = x ** i + y ** j
                if value <= bound:
                    result.append(value)
        return list(set(result))
# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    bound: int = deserialize("int", read_line())
    ans = Solution().powerfulIntegers(x, y, bound)
    print("\noutput:", serialize(ans, "integer[]"))
