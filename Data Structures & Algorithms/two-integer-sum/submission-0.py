class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        empt = []

        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                val = nums[i] + nums[j]
                if val != target:
                    continue
                else:
                    empt.append(i)
                    empt.append(j)

        return empt
        