# Created by asetti2002 at 2024/04/25 19:25
# leetgo: 1.4.3
# https://leetcode.com/problems/friends-of-appropriate-ages/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or (b > 100 and a < 100))
        
        count = 0
        age_count = Counter(ages)
        
        for age1 in age_count:
            for age2 in age_count:
                if request(age1, age2):
                    count += age_count[age1] * (age_count[age2] - (age1 == age2))
        
        return count
# @lc code=end

if __name__ == "__main__":
    ages: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numFriendRequests(ages)
    print("\noutput:", serialize(ans, "integer"))
