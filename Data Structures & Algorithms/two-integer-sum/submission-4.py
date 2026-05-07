class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicionario = {}
        for i in range(len(nums)):            
            complemento = target - nums[i]            
            if complemento in dicionario:                
                return [dicionario[complemento], i]
            dicionario[nums[i]] = i