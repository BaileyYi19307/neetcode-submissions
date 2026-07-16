class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Restate the problem
    


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


            #time complexity
                #we have to iterate through each of the n elements in the array nums O(n)
                #the lookups, because we are using a set, are all O(1) time 
                #so the time complexity is O(n)

                #we are creating a set of size N, so the space complexity is O(n)

