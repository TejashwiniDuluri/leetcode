from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck) :
        # sorted_deck = sorted(deck)
        # deck_len = len(deck)
        
        # result = [0] * deck_len # 0 0 0 0 0 0 0
        
        # indexes = list(range(0, deck_len)) # 0 1 2 3 4 5 6 
                    
        # for i in range(deck_len):
        #     result[indexes.pop(0)] = sorted_deck[i]            
        #     if indexes:
        #         indexes.append(indexes.pop(0))

        # return result
        #############
        
        dq=deque()
        for card in reversed(sorted(deck)):
            dq.rotate()
            dq.appendleft(card)
            print(dq)
        return list(dq)
    
    
deck = [17,13,11,2,3,5,7]
obj = Solution()
print(obj.deckRevealedIncreasing(deck))
        