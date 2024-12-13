
# https://www.youtube.com/watch?v=H232aocj7bQ&t=860s&ab_channel=NikhilLohia

class Solution:

    def permutations(self, nums, temp_list, result_list):
        if len(temp_list) == len(nums):
            # take copy instead of referring to it
            result_list.append(temp_list[:])
            # print(result_list)
            return result_list

        for i in nums:
            if i in temp_list:
                continue
            temp_list.append(i)
            self.permutations(nums, temp_list[:], result_list)
            temp_list.pop()

        return result_list

    def repeated_permutations(self, nums, temp_list, result_list, repeated_elem):
        if len(temp_list) == len(nums):
            # take copy instead of referring to it
            result_list.append(temp_list[:])
            # print(result_list)
            return result_list

        for i in nums:
            if len(temp_list) == 0 and i in repeated_elem:
                continue
            temp_list.append(i)
            if len(temp_list) == 1:
                repeated_elem.append(i)
            self.repeated_permutations(
                nums, temp_list[:], result_list, repeated_elem)
            temp_list.pop()

        return result_list

    def permute(self, nums):
        result_list = []
        repeated_elem = []
        # result_list = self.permutations(nums, [], result_list)
        result_list = self.repeated_permutations(
            nums, [], result_list, repeated_elem)
        return list(result_list)

    def next_permutation(self, nums):

        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i = i-1  # => pivot
        if i < 0:
            nums.reverse()
        else:
            # find successor
            successor = 0
            for succ in range(len(nums)-1, i, -1):
                if nums[succ] > nums[i]:
                    successor = succ
                    break
            nums[i], nums[successor] = nums[successor], nums[i]
            start, end = i+1, len(nums)
            nums[start:end] = nums[start:end][::-1]
        return nums


"""
[1,2,3,5,3,4]

[1,2,3,5,4,3] => [1,2,5,3,4,3]
[1,2,3,5,4,2] => [1,2,]
[1,2,4,2,5,3] => [1,2,4,3,5,2]

find decreasing sequence and before element would be pivot.
second largest element to decreasing seq and swap with pivot.
reverse the decreasing sequence picked now
"""

# nums = [1, 2, 3]
# nums = [3, 2, 1]
# nums = [1, 1, 5]
# nums = [2, 3, 1]
nums = [1, 1, 2]
obj = Solution()
print(obj.permute(nums))
# print(obj.next_permutation(nums))


"""
1   => [1] 
    backtrack([1,2,3], [1], []) 
        1 => 1 already exist skip
        2 => [1,2]
        backtrack([1,2,3], [1,2], []) 
            1 => 1 already exist skip
            2 => 2 already exist skip
            3 => [1,2,3]
            backtrack([1,2,3], [1,2,3], []) 
                return and add to results_list [[1,2,3]]                 ***********
            [1,2] ------------------------------------------------------ after remove
        [1] -------------------------------------------------------------after remove
        3 => [1,3]
        backtrack([1,2,3], [1,3], []) 
            1 => 1 already exist skip
            2 => [1,3,2]
            backtrack([1,2,3], [1,3,2], []) 
                return and add to results_list [[1,3,2]]                 *************
            [1,3]--------------------------------------------------------after remove
            3 => 3 already exist skip
        [1]--------------------------------------------------------------after remove
    []-------------------------------------------------------------------after remove

2 => [2]
    repeat with 2 first    
"""
