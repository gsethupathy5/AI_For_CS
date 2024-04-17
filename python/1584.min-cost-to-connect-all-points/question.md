# [1584. Min Cost to Connect All Points][link] (Medium)

[link]: https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where
`points[i] = [xᵢ, yᵢ]`.

The cost of connecting two points `[xᵢ, yᵢ]` and `[xⱼ, yⱼ]` is the **manhattan distance** between
them: `|xᵢ - xⱼ| + |yᵢ - yⱼ|`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is **exactly
one** simple path between any two points.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Constraints:**

- `1 <= points.length <= 1000`
- `-10⁶ <= xᵢ, yᵢ <= 10⁶`
- All pairs `(xᵢ, yᵢ)` are distinct.
