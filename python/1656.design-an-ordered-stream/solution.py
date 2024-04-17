# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/design-an-ordered-stream/

from typing import *
from leetgo_py import *

# @lc code=begin

class OrderedStream:

    def __init__(self, n: int):
        

    def insert(self, idKey: int, value: str) -> List[str]:
        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = OrderedStream(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                idKey: int = deserialize("int", method_params[0])
                value: str = deserialize("str", method_params[1])
                ans = serialize(obj.insert(idKey, value))
                output.append(ans)

    print("\noutput:", join_array(output))
