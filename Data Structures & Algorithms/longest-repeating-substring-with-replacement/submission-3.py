class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #k here is our restraint, determines if our window is valid 

        #State my assumption
        #So the goal of the problem, is that I am looking for the longest substring that
        #is the same character
        #however, one caveat, is that I am allowed up to k times to change characters in the string 
        #in order to create this longest substring of the same character
        #knowing that, the goal is to see how long of a substring I can get 

        max_length = 0 #possible if an empty string is passed in 
        max_freq = 0 

        from collections import defaultdict
        freq_map = defaultdict(int)


        l=0

        #iterate through the characters
        for r in range(len(s)):

            #add it to the frequency map 
            freq_map[s[r]]+=1

            #what's the count of the most frequent character so far? 
            max_freq = max(max_freq,freq_map[s[r]])

            window_size = r-l+1

            #if the window is invalid, we want to shrink it 
            while window_size-max_freq>k:
                #shrink our window 
                #remove from the freq_map 
                freq_map[s[l]]-=1

                #update the left pointer
                l+=1

                #shrink window size
                window_size -=1
                
                #update max_freq 
                max_freq = max(max_freq,freq_map[s[r]])

            max_length = max(max_length, window_size)

        return max_length


