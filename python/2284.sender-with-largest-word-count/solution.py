# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/sender-with-largest-word-count/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    messages: List[str] = deserialize("List[str]", read_line())
    senders: List[str] = deserialize("List[str]", read_line())
    ans = Solution().largestWordCount(messages, senders)
    print("\noutput:", serialize(ans, "string"))
