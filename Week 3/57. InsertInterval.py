class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # To solve this problem I add the new interval as the first item of the array
        # Then I compare both first intervals and check if they overlap, if yes, 
        # I just add the overlap back again in the array
        # and do the same thing with the next item
        # If they don't overlap, then I add the lowest interval in the result array
        # and the highest interval I add back to the array
        
        # Complexity
        # Time O(n) we traverse the whole list of intervals
        # Space O(1) we just add 1 element to the array and take it back 2 at each iteration 
        # we are not growing our input as we traverse the array
        
        result = []
        intervals.insert(0,newInterval)
        
        while len(intervals) > 1:
            
            new = intervals.pop(0)
            interval = intervals.pop(0)
            
            if new == interval:
                result.append(new)
                continue
            
            merge = self.merge(interval, new)
            
            if merge:
                intervals.insert(0,merge)
            else:
                result.append(min(interval,new))
                intervals.insert(0,max(interval,new))
            
            
        if len(intervals) == 1:
            result.append(intervals[0])
        
        return result
        
        
        

    def merge(self,current, new):
                       
        currentStart, currentEnd = current
        newStart, newEnd = new
        
        if newStart == currentStart and newEnd == currentEnd:
            return None
        
        if (newStart >= currentStart and newStart <= currentEnd) \
           or (currentStart >= newStart and currentStart <= newEnd):
            return [min(currentStart, newStart), max(currentEnd, newEnd)]
        
        return None
