class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #1. Restate the problem 
            # what I want to do is I want to first 
            #1. Find anagrams of each other 
            #2. Group them all together


        #2. State my assumptions 
            #My first inutition is that I can use the frequency counts as a key
            #in the hashmap
            #so if i iterate through each string in the array 
            #I create a frequency map, and store the string in it 
            #wait but I can't store a list or a dictionary as a key though 
            #what can I store as a key? a tuple? 
            #my first inutition is to use frequency as a key, but i know i cant
            #instead, i can make a tuple of the frequency of the 26 letters in the alphabet 

            #once I have a key, value pair, i would then just put the values in a new array and return that
            freq_count = defaultdict(list)

            for string in strs:
                key = [0]*26
                for c in string:
                    key[ord(c)-ord('a')]+=1
                freq_count[tuple(key)].append(string)

            return list(freq_count.values())






        #3. Data structure + algorithm 


        #4. Time complexity and space complexity
