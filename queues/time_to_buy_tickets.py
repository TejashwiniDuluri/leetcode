class Solution:
    def timeRequiredToBuy(self, tickets, k):
        seconds = 0
        tick_len = len(tickets)

        # tickets_to_buy = tickets[k]
        value = 0

        # while(tickets_to_buy):
        for i in range(tick_len):

            if i == k:
                value = tickets[i]

            # tickets[i] = tickets[i] - 1
            # seconds = seconds+1

        print(tickets, seconds, value)

        for i in range(tick_len):
            print(i, tickets[i], seconds, "before")
            if i == k:
                seconds = seconds + tickets[i]

            # before elements
            if i < k:
                # print("less")
                if tickets[i] > value:
                    # print("g")
                    seconds = seconds + value
                elif tickets[i] <= value:
                    # print("le")
                    seconds = seconds + tickets[i]

            if i > k:
                if tickets[i] > value:
                    seconds = seconds + value - 1
                elif tickets[i] < value:
                    seconds = seconds + tickets[i]
                elif tickets[i] == value:
                    seconds = seconds + value-1
            print(i, tickets[i], seconds, "after")
            print("=====")

        return seconds


tickets = [2, 3, 2]
k = 2
tickets = [5, 1, 1, 1]
k = 0
# tickets = [84, 49, 5, 24, 70, 77, 87, 8]
# k = 3
# tickets = [1, 10]
# k = 0
tickets = [2, 3, 2]
k = 2

obj = Solution()
print(obj.timeRequiredToBuy(tickets, k))
