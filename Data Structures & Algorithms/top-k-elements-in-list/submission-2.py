class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most frequent elements within the array 
        #2 most frequent elemnts in the array 


        #Restate the problem: 
            #so what I'm trying to do, is I'm trying to determine the top k most frequent elemnts within the array
            #so for example, if 3 appears the most, and k is 1, I would be returning 3

        #Assumptions: 
            #For this, I feel like I would need a frequency map
            #and then {1:1, 2:2, 3:3}
            #i'm trying to think of, once I have the frequency map, how do I know which ones are the most frequent
            #without sorting them 
            #time complexity of python's sort 

            from collections import defaultdict
            counts = defaultdict(int)


            for num in nums: 
                counts[num]+=1

            print(sorted(counts, key = lambda x: counts[x]))
            return sorted(counts, key = lambda x: counts[x])[len(counts)-k:]
