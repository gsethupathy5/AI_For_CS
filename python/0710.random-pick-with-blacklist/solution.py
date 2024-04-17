# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/random-pick-with-blacklist/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        

    def pick(self) -> int:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    blacklist: List[int] = deserialize("List[int]", constructor_params[1])
    blacklistSize: int = deserialize("int", constructor_params[2])
    obj = Solution(n, blacklist, blacklistSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "pick":
                ans = serialize(obj.pick())
                output.append(ans)

    print("\noutput:", join_array(output))
