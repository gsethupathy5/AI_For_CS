# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    favoriteCompanies: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().peopleIndexes(favoriteCompanies)
    print("\noutput:", serialize(ans, "integer[]"))
