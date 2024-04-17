# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/encode-and-decode-tinyurl/

from typing import *
from leetgo_py import *

# @lc code=begin

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    url: str = deserialize("str", read_line())
    ans = Solution().CodecDriver(url)
    print("\noutput:", serialize(ans, "string"))
