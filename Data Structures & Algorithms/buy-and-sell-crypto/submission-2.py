class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #want to buy high and sell low 
        #if the next one is lower, move the left one 
        #if the right one is higher, move the right one 
        l=0
        r=1

        max_profit=0

        while r<len(prices):
            #if right is smaller than left, update left
            #take the difference btwn the two 
            #store in max
            if prices[r]<prices[l]:
                l=r
            

            profit=prices[r]-prices[l]
            max_profit=max(profit,max_profit)
            r+=1

        return max_profit