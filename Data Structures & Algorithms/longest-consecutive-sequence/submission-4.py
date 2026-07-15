class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Restate the problem
            #So, to my understanding, I'm looking to extract the longest consecutive sequence
            #which means that each consecutive number must be one greater than the previous elements
            #but it doesn't matter if they are in consecutive order originally 

            #I then need to return the length 

            #brute force, i could iterate through each element
            #and for each one, look for the next consecutive element in the array? 

            # 0:0, 3:1, 2:2, 5:3, 4:4, 6:5, 1:6, 1:7 

            # #brute force solution 
            # #store the index of the next consecutive element in a hashmap 
            # #and then iterate through each consecutive sequence that can be formed? 
            # 2:4, 20:none, 

            # O(n^2)


            #how do we consider the start of a sequence?
            #we look for if there is no prev element in the array 

            #lets say we find a viable start to the sequence
            #its only a viable start if the number that precedes it 
            #does not exist in the array

            #so for example,
            #if we iterate through the entire array, and we look for nums-1
            #and it doesn't exist, we know we are at a viable start
            #in which case we would 

            #num --> index of previoous element 
            # 2:-1, 20:-1, 4:4, 10:-1, 3:0, 4:5, 5:6


            #start at 2. 

            numbers = set(nums)

            longest_length = 0

            #start by finding the viable starts of sequences 
            for num in nums:
                if num-1 not in numbers: 
                    #we are at a viable start to a sequence 
                    #does the next number exist? 
                    #next number is what? 
                    curr_length = 1
                    i = 1 
                    while num + i in numbers: 
                        curr_length+=1
                        i+=1
                    longest_length = max(curr_length, longest_length)

            return(longest_length)


            # 100, does 101 exist? no 
            # 200 --> does 201 exist? 
            # 1 does 2 exist? Yes
            #3 does 4 exist? Yes
            #2 does 3 exist? Yes 

            

