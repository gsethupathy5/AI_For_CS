# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/design-authentication-manager/

from typing import *
from leetgo_py import *

# @lc code=begin

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    timeToLive: int = deserialize("int", constructor_params[0])
    obj = AuthenticationManager(timeToLive)

    for i in range(1, len(ops)):
        match ops[i]:
            case "generate":
                method_params = split_array(params[i])
                tokenId: str = deserialize("str", method_params[0])
                currentTime: int = deserialize("int", method_params[1])
                obj.generate(tokenId, currentTime)
                output.append("null")
            case "renew":
                method_params = split_array(params[i])
                tokenId: str = deserialize("str", method_params[0])
                currentTime: int = deserialize("int", method_params[1])
                obj.renew(tokenId, currentTime)
                output.append("null")
            case "countUnexpiredTokens":
                method_params = split_array(params[i])
                currentTime: int = deserialize("int", method_params[0])
                ans = serialize(obj.countUnexpiredTokens(currentTime))
                output.append(ans)

    print("\noutput:", join_array(output))
