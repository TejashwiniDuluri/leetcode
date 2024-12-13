class Solution:
    def flipAndInvertImage(self, image):
        di = {0: 1, 1: 0}
        for ind, li in enumerate(image):
            for in_ind, val in enumerate(li):
                li[in_ind] = di[val]

            image[ind] = li[::-1]

        return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
obj = Solution()
print(obj.flipAndInvertImage(image))
