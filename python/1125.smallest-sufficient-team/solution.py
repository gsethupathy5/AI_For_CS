# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-sufficient-team/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    req_skills: List[str] = deserialize("List[str]", read_line())
    people: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().smallestSufficientTeam(req_skills, people)
    print("\noutput:", serialize(ans, "integer[]"))
