# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/subdomain-visit-count/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    cpdomains: List[str] = deserialize("List[str]", read_line())
    ans = Solution().subdomainVisits(cpdomains)
    print("\noutput:", serialize(ans, "string[]"))
