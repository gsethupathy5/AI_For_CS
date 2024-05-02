# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-valid-clock-times/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countTime(self, time: str) -> int:
        count = 0

        for h in range(24):
            for m in range(60):
                if (time[0] == '?' or int(time[0]) == h // 10) and \
                   (time[1] == '?' or int(time[1]) == h % 10) and \
                   (time[3] == '?' or int(time[3]) == m // 10) and \
                   (time[4] == '?' or int(time[4]) == m % 10):
                    count += 1

        return count
# @lc code=end

if __name__ == "__main__":
    time: str = deserialize("str", read_line())
    ans = Solution().countTime(time)
    print("\noutput:", serialize(ans, "integer"))
