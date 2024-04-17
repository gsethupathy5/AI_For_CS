# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, rects: List[List[int]]):
        

    def pick(self) -> List[int]:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    rects: List[List[int]] = deserialize("List[List[int]]", constructor_params[0])
    rectsSize: int = deserialize("int", constructor_params[1])
    obj = Solution(rects, rectsSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "pick":
                ans = serialize(obj.pick())
                output.append(ans)

    print("\noutput:", join_array(output))
