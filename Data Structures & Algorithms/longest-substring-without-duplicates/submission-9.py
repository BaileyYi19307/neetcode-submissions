class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #find the length of longest substring without duplicate characters 
        #substring is contiguous sequence of characters within a string 



        #1 restate the question, so from my understanding, I'm looking for 
        #a substring - so a sequence of consecutive characters - that contain no duplicates
        #and the goal is to contain the length of the longest ones


        #Brute force, I think that the brute force solution would require iterating through
        #every single substring - so using each character as a starting point, and then iterating 
        #through based off of that multiple times 
        #this would take O(n^2) time complexity 

        #Instead, I think that we can use a sliding window 
        #Our window would keep growing on the right side as we encounter unique elements
        #but then as soon as we reach a duplicate, we would shrink the left side unitl that
        #duplicate it removed 
        #This would require iterating over each character at most once, so the time complexity would be O(n) 

        from collections import defaultdict 

        max_length = 1
        freq_map = defaultdict(int)
        l=0

        if len(s) ==0:
            return 0

        for r in range(len(s)):
            #we can add the character to our frequency map 

            freq_map[s[r]]+=1
            #we've reached a duplicate
            #we want to shrink the window from the left side until the duplicate is gone 
            while freq_map[s[r]]>1:
                #remove the left element from the frequency map 
                freq_map[s[l]]-=1
                l+=1
            
            max_length = max(max_length,r-l+1)
            

            
        return max_length

