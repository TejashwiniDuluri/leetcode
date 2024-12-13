from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        # first parse from left and see if your right neighbour is greater so give him extra than current
        # second parse from right and see if your left child is greater so assign him extra than right neighbour

        ratings_len = len(ratings)
        candies = [1] * ratings_len
        for i in range(1, ratings_len):
            if ratings[i-1] < ratings[i]:
                candies[i] += candies[i-1]
        
        for i in range(ratings_len-2, -1, -1):              
            if ratings[i] > ratings[i+1]:
                # right[i] += right[i+1]                
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        print()
        return sum(candies)
        # results = []
        # for i, j in zip(left, right):
        #     results.append(max(i, j))
        
        # return sum(results)


ratings = [1,0,2]
ratings =[1,2,2]
ratings = [1,2,87,87,87,2,1]
ratings =[1,3,2,2,1]
obj = Solution()
print(obj.candy(ratings))
        