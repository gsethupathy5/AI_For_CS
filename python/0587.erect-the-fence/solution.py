# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/erect-the-fence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    trees: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().outerTrees(trees)
    print("\noutput:", serialize(ans, "integer[][]"))
