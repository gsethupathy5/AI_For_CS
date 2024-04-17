# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/random-pick-index/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def __init__(self, nums: List[int]):
        

    def pick(self, target: int) -> int:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums: List[int] = deserialize("List[int]", constructor_params[0])
    numsSize: int = deserialize("int", constructor_params[1])
    obj = Solution(nums, numsSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "pick":
                method_params = split_array(params[i])
                target: int = deserialize("int", method_params[0])
                ans = serialize(obj.pick(target))
                output.append(ans)

    print("\noutput:", join_array(output))
