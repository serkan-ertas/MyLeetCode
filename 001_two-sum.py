class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if(complement in numHash):
                return [index,numHash[complement]]
            numHash[nums[index]] = index
        return []