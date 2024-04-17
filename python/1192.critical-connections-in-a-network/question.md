# [1192. Critical Connections in a Network][link] (Hard)

[link]: https://leetcode.com/problems/critical-connections-in-a-network/

There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server
`connections` forming a network where `connections[i] = [aᵢ, bᵢ]` represents a connection between
servers `aᵢ` and `bᵢ`. Any server can reach other servers directly or indirectly through the
network.

A critical connection is a connection that, if removed, will make some servers unable to reach some
other server.

Return all critical connections in the network in any order.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png)

```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```

**Example 2:**

```
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
```

**Constraints:**

- `2 <= n <= 10⁵`
- `n - 1 <= connections.length <= 10⁵`
- `0 <= aᵢ, bᵢ <= n - 1`
- `aᵢ != bᵢ`
- There are no repeated connections.
