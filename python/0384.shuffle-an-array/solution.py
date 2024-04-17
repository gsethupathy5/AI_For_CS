# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/shuffle-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, nums: List[int]):
        

    def reset(self) -> List[int]:
        

    def shuffle(self) -> List[int]:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums: List[int] = deserialize("List[int]", constructor_params[0])
    obj = Solution(nums)

    for i in range(1, len(ops)):
        match ops[i]:
            case "reset":
                ans = serialize(obj.reset())
                output.append(ans)
            case "shuffle":
                ans = serialize(obj.shuffle())
                output.append(ans)

    print("\noutput:", join_array(output))
