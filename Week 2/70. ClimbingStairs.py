class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        # This is alike fibonnaci sequence
        # To find  a nth step we need to ask what could have been our previous steps
        
        # Complexity
        # Time O(n) we go from 2 to n+1
        # Space O(n) we have a memory that has the size of n+1 
        
        mem = [0] * (n+1)
        mem[0] = 1
        mem[1] = 1
        
        for stair in range(2, n+1):
            mem[stair] = mem[stair-1] + mem[stair-2] 
        
        return mem[-1]