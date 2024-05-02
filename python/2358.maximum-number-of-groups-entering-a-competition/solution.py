# Created by asetti2002 at 2024/05/01 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        groups = 1
        for i in range(1, len(grades)):
            if sum(grades[:i]) < sum(grades[i:i+1]) and len(grades[:i]) < len(grades[i:i+1]):
                groups += 1
        return groups
# @lc code=end

if __name__ == "__main__":
    grades: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumGroups(grades)
    print("\noutput:", serialize(ans, "integer"))
