# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    people: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().reconstructQueue(people)
    print("\noutput:", serialize(ans, "integer[][]"))
