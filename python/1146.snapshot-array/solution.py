# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/snapshot-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class SnapshotArray:

    def __init__(self, length: int):
        

    def set(self, index: int, val: int) -> None:
        

    def snap(self) -> int:
        

    def get(self, index: int, snap_id: int) -> int:
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    length: int = deserialize("int", constructor_params[0])
    obj = SnapshotArray(length)

    for i in range(1, len(ops)):
        match ops[i]:
            case "set":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.set(index, val)
                output.append("null")
            case "snap":
                ans = serialize(obj.snap())
                output.append(ans)
            case "get":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                snap_id: int = deserialize("int", method_params[1])
                ans = serialize(obj.get(index, snap_id))
                output.append(ans)

    print("\noutput:", join_array(output))
