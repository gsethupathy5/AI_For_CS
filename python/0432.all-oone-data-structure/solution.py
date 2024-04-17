# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/all-oone-data-structure/

from typing import *
from leetgo_py import *

# @lc code=begin

class AllOne:

    def __init__(self):
        

    def inc(self, key: str) -> None:
        

    def dec(self, key: str) -> None:
        

    def getMaxKey(self) -> str:
        

    def getMinKey(self) -> str:
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = AllOne()

    for i in range(1, len(ops)):
        match ops[i]:
            case "inc":
                method_params = split_array(params[i])
                key: str = deserialize("str", method_params[0])
                obj.inc(key)
                output.append("null")
            case "dec":
                method_params = split_array(params[i])
                key: str = deserialize("str", method_params[0])
                obj.dec(key)
                output.append("null")
            case "getMaxKey":
                ans = serialize(obj.getMaxKey())
                output.append(ans)
            case "getMinKey":
                ans = serialize(obj.getMinKey())
                output.append(ans)

    print("\noutput:", join_array(output))
