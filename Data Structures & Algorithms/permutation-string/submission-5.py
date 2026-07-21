class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #restate the problem 
            #alright, from my understanding, if we are given two strings, then we are looking
            #to see if a set of contiguous characters in string 2 is a permutation of string 1
            #this means, is there a set of contiguous characters in string 2 that has the same 
            #frequency of characters as string 1 

        from collections import defaultdict

        freq_map_s1=defaultdict(int)
        freq_map_s2=defaultdict(int)

        #to start, I would first create a hashmap and store the frequency of characters of string 1 
        for c in s1: 
            freq_map_s1[c]+=1

        #now, I would iterate through the second string 
        #I think that I would maintain a sliding window
        #I'm adding each character of s2 to a hashmap
        #when the length of the window reaches the length of s1, then I compare the two frequency maps 
        #if it exceeds the length of s1, then I shrink the window by moving the left pointer forward
        #and adjusting the frequency map for s2 accordingly

        #this is better than the brute force solution, which would be to find all the substrings of s2,
        #and to compare the frequency of characters in each substring to that of s1
        #determining all the substrings would be a O(n^2) operation, since we would use each of the ncharacter
        #in s2 as a starting point, and iterate through the remaining n-1 characters

        #each element in the array is therefore processed at most twice - once when it's first
        #added to the sliding window, and once when its removed 
        #in the worst case then, processing the entire array is O(2n) which is O(n) since 2 is a constant

        #the space complexity would be O(1) since the hashmap can contain at most 26 characters (lowercase) 


        l=0
        
        for r in range(len(s2)):
            curr_char = s2[r]
            #add the element to the frequency map 
            freq_map_s2[curr_char]+=1 

            #before we add, if the size of the window it too big, we need to remove from the left side of the window 
            while r-l+1>len(s1):
                freq_map_s2[s2[l]]-=1
                #remove the left side 
                if freq_map_s2[s2[l]]==0: 
                    freq_map_s2.pop(s2[l])
                l+=1


            #if the length of the window matches the lenght of s1, comapre the frequency maps
            if r-l+1 == len(s1):
                if freq_map_s2==freq_map_s1:
                    return True
                
        return False

            



        # #this looks like a fixed window problem 

        # #what I would do is that I would add characters to the frequency map 
        # #once the size grows larger then the length of s1, I would first
        # #I would remove from the left 
        # #once the window reaches the size of s1, then I would compare frequency maps 

        # from collections import defaultdict 
        # #I would start by creating a frequency map for s1 
        # freq_map_s1 = defaultdict(int)
        # freq_map_s2 = defaultdict(int)

        # for c in s1:
        #     freq_map_s1[c]+=1

        # l=0
        
        # for r in range(len(s2)):
        #     #add the character to the frequency map for s2 
        #     curr_char = s2[r]
        #     freq_map_s2[curr_char]+=1

        #     #once the size is greater then 
        #     while r-l+1 > len(s1):
        #         #remove from the left 
        #         freq_map_s2[s2[l]]-=1

        #         if freq_map_s2[s2[l]]==0:
        #             freq_map_s2.pop(s2[l])

        #         l+=1

        #     if r-l+1==len(s1):
        #         #compare frequency maps
        #         if freq_map_s2 == freq_map_s1:
        #             return True 


        # return False
            

