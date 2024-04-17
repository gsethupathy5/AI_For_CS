# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/generate-random-point-in-a-circle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        

    def randPoint(self) -> List[float]:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    radius: float = deserialize("float", constructor_params[0])
    x_center: float = deserialize("float", constructor_params[1])
    y_center: float = deserialize("float", constructor_params[2])
    obj = Solution(radius, x_center, y_center)

    for i in range(1, len(ops)):
        match ops[i]:
            case "randPoint":
                ans = serialize(obj.randPoint())
                output.append(ans)

    print("\noutput:", join_array(output))
