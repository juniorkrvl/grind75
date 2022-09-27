# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # Since the versions are ordered, we can solve this using a binary search
        # but it is not an array so we use the number of the version instead
        
        # Complexity
        # Time O(logn) we are using binary search so the time complexity is going to be logn, we are halving the number
        # by each iteration
        # Space O(1) We don't have any variable that grows with the input
        
        left = 1
        right = n+1
        res = -1
               
        while left <= right:
            mid = (left+right) // 2
            
            if isBadVersion(mid):
                res = mid
                right = mid-1
            else:
                left = mid+1
                
        return res