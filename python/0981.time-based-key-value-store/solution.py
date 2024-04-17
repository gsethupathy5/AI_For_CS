# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/time-based-key-value-store/

from typing import *
from leetgo_py import *

# @lc code=begin

class TimeMap:

    def __init__(self):
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        

    def get(self, key: str, timestamp: int) -> str:
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = TimeMap()

    for i in range(1, len(ops)):
        match ops[i]:
            case "set":
                method_params = split_array(params[i])
                key: str = deserialize("str", method_params[0])
                value: str = deserialize("str", method_params[1])
                timestamp: int = deserialize("int", method_params[2])
                obj.set(key, value, timestamp)
                output.append("null")
            case "get":
                method_params = split_array(params[i])
                key: str = deserialize("str", method_params[0])
                timestamp: int = deserialize("int", method_params[1])
                ans = serialize(obj.get(key, timestamp))
                output.append(ans)

    print("\noutput:", join_array(output))
