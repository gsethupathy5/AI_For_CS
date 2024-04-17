# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

from typing import *
from leetgo_py import *

# @lc code=begin

class DataStream:

    def __init__(self, value: int, k: int):
        

    def consec(self, num: int) -> bool:
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    value: int = deserialize("int", constructor_params[0])
    k: int = deserialize("int", constructor_params[1])
    obj = DataStream(value, k)

    for i in range(1, len(ops)):
        match ops[i]:
            case "consec":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                ans = serialize(obj.consec(num))
                output.append(ans)

    print("\noutput:", join_array(output))
