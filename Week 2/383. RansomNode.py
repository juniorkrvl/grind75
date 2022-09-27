class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # We use a dictionary as a memory
        # to store the counter for all the letter in magazine
        # then we just count down the leters for each ransomNode letter
        # If there is one letter that is not in the magazine, then we return false
        # If we run out of letter from magazine, we also return false
        # Otherwise we can return true
        
        # Complexity
        # Time O(n+m) we traverse both the magazine and the ransomNote
        # Space O(1) we don't have any variable growing with the size of the input
        
        mem = defaultdict(int)
        
        for letter in magazine:
            mem[letter] += 1
            
        for letter in ransomNote:
            if mem[letter] > 0:
                mem[letter] -= 1
            else:
                return False
            
        return True