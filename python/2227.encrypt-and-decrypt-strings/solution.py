# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/encrypt-and-decrypt-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        

    def encrypt(self, word1: str) -> str:
        

    def decrypt(self, word2: str) -> int:
        

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    keys: List[str] = deserialize("List[str]", constructor_params[0])
    values: List[str] = deserialize("List[str]", constructor_params[1])
    dictionary: List[str] = deserialize("List[str]", constructor_params[2])
    obj = Encrypter(keys, values, dictionary)

    for i in range(1, len(ops)):
        match ops[i]:
            case "encrypt":
                method_params = split_array(params[i])
                word1: str = deserialize("str", method_params[0])
                ans = serialize(obj.encrypt(word1))
                output.append(ans)
            case "decrypt":
                method_params = split_array(params[i])
                word2: str = deserialize("str", method_params[0])
                ans = serialize(obj.decrypt(word2))
                output.append(ans)

    print("\noutput:", join_array(output))
