class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        ta1 = 0
        ta2 = 0
                    
        for ta in numbers:
            if (target - ta) in numbers:
                ta1 = ta
                ta2 = target - ta
                break
        
        if ta1 == ta2:
            return [ idx + 1 for idx, value in enumerate(numbers) if value == ta1]
        
        else:
            idx_1_list = [ idx + 1 for idx, value in enumerate(numbers) if value == ta1]
            idx_2_list = [ idx + 1 for idx, value in enumerate(numbers) if value == ta2]
            return idx_1_list + idx_2_list