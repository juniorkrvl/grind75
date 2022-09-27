class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        
        for number in nums:                      
            if not number in duplicates:
                duplicates[number] = 1
            else:                               
                duplicates[number] += 1            
                
            if number in duplicates and duplicates[number] > 1:
                return True
            
        return False