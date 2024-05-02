# Created by asetti2002 at 2024/04/25 20:26
# leetgo: 1.4.3
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i, size in enumerate(groupSizes):
            if size in groups:
                groups[size].append(i)
            else:
                groups[size] = [i]
            if len(groups[size]) == size:
                groups[size] = []
        return [group for group in groups.values() if group]
# @lc code=end

if __name__ == "__main__":
    groupSizes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().groupThePeople(groupSizes)
    print("\noutput:", serialize(ans, "integer[][]"))
