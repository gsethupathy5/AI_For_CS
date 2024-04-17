# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    score: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().sortTheStudents(score, k)
    print("\noutput:", serialize(ans, "integer[][]"))
