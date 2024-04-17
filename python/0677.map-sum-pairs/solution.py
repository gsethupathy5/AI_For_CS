# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/map-sum-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class MapSum:

    def __init__(self):
        

    def insert(self, key: str, val: int) -> None:
        

    def sum(self, prefix: str) -> int:
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MapSum()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                key: str = deserialize("str", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.insert(key, val)
                output.append("null")
            case "sum":
                method_params = split_array(params[i])
                prefix: str = deserialize("str", method_params[0])
                ans = serialize(obj.sum(prefix))
                output.append(ans)

    print("\noutput:", join_array(output))
