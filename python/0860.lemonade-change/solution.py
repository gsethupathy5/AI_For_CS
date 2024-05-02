# Created by asetti2002 at 2024/04/25 19:32
# leetgo: 1.4.3
# https://leetcode.com/problems/lemonade-change/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
# @lc code=end

if __name__ == "__main__":
    bills: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lemonadeChange(bills)
    print("\noutput:", serialize(ans, "boolean"))
