# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    artifacts: List[List[int]] = deserialize("List[List[int]]", read_line())
    dig: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().digArtifacts(n, artifacts, dig)
    print("\noutput:", serialize(ans, "integer"))
