# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/random-pick-with-weight/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, w: List[int]):
        

    def pickIndex(self) -> int:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    w: List[int] = deserialize("List[int]", constructor_params[0])
    wSize: int = deserialize("int", constructor_params[1])
    obj = Solution(w, wSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "pickIndex":
                ans = serialize(obj.pickIndex())
                output.append(ans)

    print("\noutput:", join_array(output))
