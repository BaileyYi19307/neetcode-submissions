class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #this looks like a fixed window problem 

        #what I would do is that I would add characters to the frequency map 
        #once the size grows larger then the length of s1, I would first
        #I would remove from the left 
        #once the window reaches the size of s1, then I would compare frequency maps 

        from collections import defaultdict 
        #I would start by creating a frequency map for s1 
        freq_map_s1 = defaultdict(int)
        freq_map_s2 = defaultdict(int)

        for c in s1:
            freq_map_s1[c]+=1

        l=0
        
        for r in range(len(s2)):
            #add the character to the frequency map for s2 
            curr_char = s2[r]
            freq_map_s2[curr_char]+=1


            #once the size is greater then 
            while r-l+1 > len(s1):
                #remove from the left 
                freq_map_s2[s2[l]]-=1

                if freq_map_s2[s2[l]]==0:
                    freq_map_s2.pop(s2[l])

                l+=1


            if r-l+1==len(s1):
                #compare frequency maps
                if freq_map_s2 == freq_map_s1:
                    return True 



        return False
            

