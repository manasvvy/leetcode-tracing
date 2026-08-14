class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        nums = [num for row in mat for num in row]

        ans = []
        for i in range(r):
            ans.append(nums[i * c:(i + 1) * c])

        return ans
