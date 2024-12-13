
nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
# nums = [1, 5, 2, 3, 4]
nums = [1, 1, 2, 5, 2, 1, 0, 0, 1, 3]
# nums = [1, 1, 2, 3, 2, 1, 0, 0, 1, 3]

# nums = [0, 1]
# nums = [0]
# nums = [1, 2]
# Greedy approach
# nums = [2, 0, 0]

# nums = [0]


def jump_game(nums):
    if nums[0] == 0 and len(nums) > 1:
        return False
    if len(nums) == 1:
        return True

    length_of_array = len(nums)
    target = length_of_array - 1
    start = length_of_array - 2

    while start >= 0:
        if nums[start] >= target - start:
            target = start
        start = start-1

    return target == 0


def jump_game_min_steps():
    pass


# print(jump_game(nums))
print(jump_game_min_steps(nums))
