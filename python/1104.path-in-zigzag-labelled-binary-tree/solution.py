# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = label.bit_length()
        res = [label]
        while level > 1:
            label = 3 * 2 ** (level - 2) - label // 2 - 1
            res.insert(0, label)
            level -= 1
        return res
# @lc code=end

if __name__ == "__main__":
    label: int = deserialize("int", read_line())
    ans = Solution().pathInZigZagTree(label)
    print("\noutput:", serialize(ans, "integer[]"))
