class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most frequent elements within the array 
        #2 most frequent elemnts in the array 

        from collections import defaultdict
        #so one thing I'm noticing is that, the maximum frequency any of the elements in the array
        #can have is the length of the list #so, in the first example given, that would be 6

        #I would initialize an empty array of size 6, and I know that the indices would represent frequencies 
        #I would then iterate through nums, and for each element, essentially place them int these buckets 

        #so '

        ## DONT DO THIS THIS ISN"T CREATING INDEPENDENT LISTS 
        #frequency_buckets = [[]] * len(nums) 
        #be very careful, the frequency here can be + 1
        frequency_buckets = [[] for _ in range(len(nums)+1)]
        counts = defaultdict(int) 

        for num in nums: 
            counts[num]+=1

        print(frequency_buckets)
        #iterate through counts 
        for num, frequency in counts.items():
            print(num,frequency)
            frequency_buckets[frequency].append(num)

        res=[]
        #would then iterate through frequency buckets backwards until I have k elements

        #iterate through the frequency buckets backwards
        for i in range(len(frequency_buckets)-1,-1,-1):
            bucket = frequency_buckets[i]
            for num in bucket:
                if len(res)==k:
                    return res
                else:
                    res.append(num)

        return res
        



        #i would then walk through this array backwards until I've stored k elements as a result and return that 

        #The space complexity would be O(n) for first iterating throuogh the nums and placing them buckets
        #and O(n) for walking backwards through this frequency array so O(n) overall

        #The space complexity would also be O(n)



        #Restate the problem: 
            #so what I'm trying to do, is I'm trying to determine the top k most frequent elemnts within the array
            #so for example, if 3 appears the most, and k is 1, I would be returning 3

        #Assumptions: 
            #For this, I feel like I would need a frequency map
            #and then {1:1, 2:2, 3:3}
            #i'm trying to think of, once I have the frequency map, how do I know which ones are the most frequent
            #without sorting them 
            #time complexity of python's sort 
