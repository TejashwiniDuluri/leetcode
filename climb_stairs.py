# Purpose: Given a staircase with n steps, find the number of ways to reach the top.

n = 1
1

n = 2
1+1
2

n = 3
1+1+1
1+2
2+1


n = 4
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2


n = 5
1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
1+2+2
2+1+2
2+2+1


def find_ways(n):

    # Suppose there are 5 steps to reach 5th step ypu need to climb one from 4th step or 2 from 3rd step
    # So, find_ways(5) = find_ways(4) + find_ways(3)
    # Similarly, find_ways(4) = find_ways(3) + find_ways(2)
    # find_ways(3) = find_ways(2) + find_ways(1)
    # find_ways(2) = 2
    # find_ways(1) = 1

    # ======================================
    # this is taking much time
    # if n < 2:
    #     return n
    # else:
    #     return find_ways(n-1) + find_ways(n-2)

    # ======================================
    # space complexity is O(n) as array is keep on increasing
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # result = [0]*(n+1)
    # result[1] = 1
    # result[2] = 2

    # if n >= 3:
    #     for i in range(3, n+1):
    #         result[i] = result[i-1] + result[i-2]

    # return result[n]
    # =======================================
    if n <= 2:
        return n
    else:
        prev_step = 2
        pre_prev_step = 1
        # steps = prev_step + pre_prev_step
        for i in range(3, n+1):
            steps = prev_step + pre_prev_step
            pre_prev_step = prev_step
            prev_step = steps
    return prev_step


print(find_ways(5))
