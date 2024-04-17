# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/solving-questions-with-brainpower/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    questions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().mostPoints(questions)
    print("\noutput:", serialize(ans, "long"))
