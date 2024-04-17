# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        

    def add(self, index: int, val: int) -> None:
        

    def count(self, tot: int) -> int:
        

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums1: List[int] = deserialize("List[int]", constructor_params[0])
    nums2: List[int] = deserialize("List[int]", constructor_params[1])
    obj = FindSumPairs(nums1, nums2)

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.add(index, val)
                output.append("null")
            case "count":
                method_params = split_array(params[i])
                tot: int = deserialize("int", method_params[0])
                ans = serialize(obj.count(tot))
                output.append(ans)

    print("\noutput:", join_array(output))
