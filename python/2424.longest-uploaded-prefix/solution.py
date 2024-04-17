# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-uploaded-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class LUPrefix:

    def __init__(self, n: int):
        

    def upload(self, video: int) -> None:
        

    def longest(self) -> int:
        

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = LUPrefix(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "upload":
                method_params = split_array(params[i])
                video: int = deserialize("int", method_params[0])
                obj.upload(video)
                output.append("null")
            case "longest":
                ans = serialize(obj.longest())
                output.append(ans)

    print("\noutput:", join_array(output))
