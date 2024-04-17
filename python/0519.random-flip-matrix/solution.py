# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/random-flip-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, m: int, n: int):
        

    def flip(self) -> List[int]:
        

    def reset(self) -> None:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    m: int = deserialize("int", constructor_params[0])
    n: int = deserialize("int", constructor_params[1])
    obj = Solution(m, n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "flip":
                ans = serialize(obj.flip())
                output.append(ans)
            case "reset":
                obj.reset()
                output.append("null")

    print("\noutput:", join_array(output))
