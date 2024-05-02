# Created by asetti2002 at 2024/04/25 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/equal-rational-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def to_float(s):
            if '.' not in s:
                return int(s)
            parts = s.split('.')
            non_repeat = 0 if not parts[1] else int(parts[1])
            repeat = 0
            if '(' in parts[1]:
                idx = parts[1].index('(')
                non_repeat = int(parts[1][:idx])
                repeat = int(parts[1][idx + 1: -1])
                repeat = repeat * 10 ** (len(parts[1]) - idx - 2)
            return int(parts[0]) + (non_repeat + repeat/(10 ** (len(str(repeat))))) / (10 ** len(str(non_repeat + repeat)))

        return abs(to_float(s) - to_float(t)) < 1e-9
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isRationalEqual(s, t)
    print("\noutput:", serialize(ans, "boolean"))
