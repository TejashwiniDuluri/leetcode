class Solution:
    def countStudents(self, students, sandwiches) -> int:
        square_stud = 0
        circle_stud = 0

        for i in students:
            if i == 0:
                circle_stud += 1
            else:
                square_stud += 1

        # 1,0 => [1, 1, 1], [0,1,1]
        # This last cond will come
        for i in sandwiches:
            if i == 0 and circle_stud > 0:
                circle_stud -= 1
            elif i == 1 and square_stud > 0:
                square_stud -= 1
            else:
                break

        return circle_stud+square_stud


        # print(remaining_ones, remaining_zeros, students_length)
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]


#######
# students = [1, 1, 1, 0, 0, 1]
# sandwiches = [1, 0, 0, 0, 1, 1]

# 1,1 => [1,1,0,0,1], [0,0,0,1,1]
# 1,0 => [1,0,0,1,1], [0,0,0,1,1]
# 1,0 => [0,0,1,1, 1], [0,0,0,1,1]
# 0,0 => [0,1,1, 1], [0,0,1,1]
# 0,0 => [1,1, 1], [0,1,1]
# 1,0 => [1, 1, 1], [0,1,1]
########

obj = Solution()
print(obj.countStudents(students, sandwiches))
