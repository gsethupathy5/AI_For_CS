# [1453. Maximum Number of Darts Inside of a Circular Dartboard][link] (Hard)

[link]: https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

Alice is throwing `n` darts on a very large wall. You are given an array `darts` where `darts[i] =
[xᵢ, yᵢ]` is the position of the `iᵗʰ` dart that Alice threw on the wall.

Bob knows the positions of the `n` darts on the wall. He wants to place a dartboard of radius `r` on
the wall so that the maximum number of darts that Alice throws lie on the dartboard.

Given the integer `r`, return the maximum number of darts that can lie on the dartboard.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/29/sample_1_1806.png)

```
Input: darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png)

```
Input: darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the
point (7,8).
```

**Constraints:**

- `1 <= darts.length <= 100`
- `darts[i].length == 2`
- `-10⁴ <= xᵢ, yᵢ <= 10⁴`
- All the `darts` are unique
- `1 <= r <= 5000`
