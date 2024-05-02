# Created by asetti2002 at 2024/05/01 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/count-days-spent-together/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def get_days(month, day):
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(days_in_month[:int(month) - 1]) + int(day)

        start = max(get_days(arriveAlice[:2], arriveAlice[3:]), get_days(arriveBob[:2], arriveBob[3:]))
        end = min(get_days(leaveAlice[:2], leaveAlice[3:]), get_days(leaveBob[:2], leaveBob[3:]))

        return max(0, end - start + 1)
# @lc code=end

if __name__ == "__main__":
    arriveAlice: str = deserialize("str", read_line())
    leaveAlice: str = deserialize("str", read_line())
    arriveBob: str = deserialize("str", read_line())
    leaveBob: str = deserialize("str", read_line())
    ans = Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print("\noutput:", serialize(ans, "integer"))
