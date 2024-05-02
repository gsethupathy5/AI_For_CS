# Created by asetti2002 at 2024/04/25 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/day-of-the-year/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def dayOfYear(self, date: str) -> int:
        return int(date.split('-')[1]) + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30][:int(date.split('-')[1])-1]) + (1 if int(date.split('-')[0]) % 4 == 0 and (int(date.split('-')[0]) % 100 != 0 or int(date.split('-')[0]) % 400 == 0) and int(date.split('-')[1]) > 2 else 0)
# @lc code=end

if __name__ == "__main__":
    date: str = deserialize("str", read_line())
    ans = Solution().dayOfYear(date)
    print("\noutput:", serialize(ans, "integer"))
