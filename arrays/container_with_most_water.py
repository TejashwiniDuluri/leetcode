

def most_water(height):
    # brute force
    # area = 0

    # for i in range(0, len(height)-1):
    #     length = 0
    #     curr_area = 0
    #     for j in range(i+1, len(height)):
    #         curr_height = min(height[i], height[j])
    #         length = j-i
    #         curr_area = curr_height*length

    #     if curr_area > area:
    #         area = curr_area
    # return area

    # greedy

    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        if curr_area > area:
            area = curr_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]
print(most_water(height))
