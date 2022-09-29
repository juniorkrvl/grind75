class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # To find the maximum subarray we need to sum each number with the next
        # while the sum is greater than the number, otherwise we drop the number and continue with
        # the next number in the array
        
        # e.g for an input like
        # [20,1,-3,4,-1,2,1,-5,4]       
        # we start from 20 and sum with 1, the result is 21. 21 is greater than 1 so we can replace it
        # and move on.
        # [20,21,-3,4,-1,2,1,-5,4]
        # We do the same thing from the 21 and -3. 21 - 3 = 18. 18 is greater than -3 so we replace it
        # [20,21,18,4,-1,2,1,-5,4] and so on... until we have
        # [20,21,18,22,21,23,24,19,23]

        # while we are doing this, we keep track of the highest sum, and in the end we return it.
        
        
        # Complexity
        # Time O(n) we traverse the whole array
        # Space O(1) we keep only two variables in memory
        
        max = nums[0]
        previous = nums[0]
        
        for n in range(1,len(nums)):
            sum = previous + nums[n]
            
            if sum > nums[n]:
                previous = sum
            else:
                previous = nums[n]
                
            if previous > max:
                max = previous
                
        return max
            
