class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # What makes a palindrome is the mirrored string, so we need to have at least one center word
        # which can be any word, and then for the rest we need to consider only even letters
        # That is why we calculate module of 2 and throw away the rest, we don't care about a lingering letter
        # if we have 5 a's we only care about 4 because they are even. The fifth letter can either be throw away 
        # or considered our center
        
        # Complexity
        # Time O(n+m) we traverse the letters first counting them, then traverse the aggregate of the sums
        # Space O(n) we have a dictionary that grows with the amount of letters we have in it
        
        if  len(s) == 1:
            return 1
        
        dict = {}
        sum = 0
        center = 0
        
        # count the amount of characters 
        for letter in s:
            if not dict.get(letter):
                dict[letter] = 0
                
            dict[letter] += 1
        
        
        for letter in dict.keys():
            rest = dict[letter] % 2
            sum += dict[letter] - rest 

            if rest % 2 == 1 and not center:
                sum+=1
                center=1
                
        return sum