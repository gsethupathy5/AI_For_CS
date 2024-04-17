# [2250. Count Number of Rectangles Containing Each Point][link] (Medium)

[link]: https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

You are given a 2D integer array `rectangles` where `rectangles[i] = [lᵢ, hᵢ]` indicates that `iᵗʰ`
rectangle has a length of `lᵢ` and a height of `hᵢ`. You are also given a 2D integer array `points`
where `points[j] = [xⱼ, yⱼ]` is a point with coordinates `(xⱼ, yⱼ)`.

The `iᵗʰ` rectangle has its **bottom-left corner** point at the coordinates `(0, 0)` and its **top-
right corner** point at `(lᵢ, hᵢ)`.

Return an integer array  `count` of length  `points.length` where  `count[j]` is the number of
rectangles that **contain** the  `jᵗʰ` point.

The `iᵗʰ` rectangle **contains** the `jᵗʰ` point if `0 <= xⱼ <= lᵢ` and `0 <= yⱼ <= hᵢ`. Note that
points that lie on the **edges** of a rectangle are also considered to be contained by that
rectangle.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/02/example1.png)

```
Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
Output: [2,1]
Explanation:
The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/02/example2.png)

```
Input: rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
Output: [1,3]
Explanation:
The first rectangle contains only the point (1, 1).
The second rectangle contains only the point (1, 1).
The third rectangle contains the points (1, 3) and (1, 1).
The number of rectangles that contain the point (1, 3) is 1.
The number of rectangles that contain the point (1, 1) is 3.
Therefore, we return [1, 3].
```

**Constraints:**

- `1 <= rectangles.length, points.length <= 5 * 10⁴`
- `rectangles[i].length == points[j].length == 2`
- `1 <= lᵢ, xⱼ <= 10⁹`
- `1 <= hᵢ, yⱼ <= 100`
- All the `rectangles` are **unique**.
- All the `points` are **unique**.
