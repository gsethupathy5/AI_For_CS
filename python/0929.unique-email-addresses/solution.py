# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-email-addresses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    emails: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numUniqueEmails(emails)
    print("\noutput:", serialize(ans, "integer"))
