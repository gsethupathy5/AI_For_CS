# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/throne-inheritance/

from typing import *
from leetgo_py import *

# @lc code=begin

class ThroneInheritance:

    def __init__(self, kingName: str):
        

    def birth(self, parentName: str, childName: str) -> None:
        

    def death(self, name: str) -> None:
        

    def getInheritanceOrder(self) -> List[str]:
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    kingName: str = deserialize("str", constructor_params[0])
    obj = ThroneInheritance(kingName)

    for i in range(1, len(ops)):
        match ops[i]:
            case "birth":
                method_params = split_array(params[i])
                parentName: str = deserialize("str", method_params[0])
                childName: str = deserialize("str", method_params[1])
                obj.birth(parentName, childName)
                output.append("null")
            case "death":
                method_params = split_array(params[i])
                name: str = deserialize("str", method_params[0])
                obj.death(name)
                output.append("null")
            case "getInheritanceOrder":
                ans = serialize(obj.getInheritanceOrder())
                output.append(ans)

    print("\noutput:", join_array(output))
