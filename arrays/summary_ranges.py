

def get_summary_ranges(nums):
    start = 0
    end = 0
    result = []

    for i in range(1, len(nums)):
        if nums[i-1]+1 != nums[i]:
            if start == end:
                result.append(str(nums[end]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[end]))
            start = i
            end = i
        else:
            end = i
    if start == end:
        result.append(str(nums[end]))
    else:
        result.append(str(nums[start]) + "->" + str(nums[end]))

        # print(nums[i])
        # if nums[i-1]+1 == nums[i]:
        #     end = i
        # else:
        #     print("start", start)
        #     if start == end:
        #         result.append(str(nums[end]))
        #     else:
        #         result.append(str(nums[start]) + "->" + str(nums[end]))
        #     start = i
        #     end = i
    return result


nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]
print(get_summary_ranges(nums))
