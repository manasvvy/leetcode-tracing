class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans= []
        for i in range(len(nums)):
            leftSum = sum(nums[0:i])

            rightSum = sum(nums[i+1:])

            ans.append(abs(leftSum - rightSum))
        return ans
