# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    answerKey: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxConsecutiveAnswers(answerKey, k)
    print("\noutput:", serialize(ans, "integer"))
