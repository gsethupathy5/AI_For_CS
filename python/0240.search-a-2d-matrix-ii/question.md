# [240. Search a 2D Matrix II][link] (Medium)

[link]: https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix
`matrix`. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
target = 5
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
target = 20
Output: false
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10⁹ <= matrix[i][j] <= 10⁹`
- All the integers in each row are **sorted** in ascending order.
- All the integers in each column are **sorted** in ascending order.
- `-10⁹ <= target <= 10⁹`