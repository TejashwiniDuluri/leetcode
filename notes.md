# reverse and array

swap first and last
swap second and second from last

# remove element from list in o(1)

pop(n) from list is o(n) so awap last element to that index element and remove as list.pop()

# iterate reversely on list

range(len(array) -1, -1, -1)

# product of array elemnts except element itself

first compute prefix prod from left using for loop , then compute suffix prod from right using another for loop

# find first occurance of substr in a string

string.find(substr)

# reverse a string in python with O(1) space complexity

You cannot reverse in place as python strings are immutable. So you have to convert it to a mutable structures like lists and join to form reversed strings. Or use some two pointer approach to form a new string but inplace modifications are not possible.

# zigzag string given a number of rows

declare a list of empty strings with num of rows length
traverse from top with index <= rows-1 then traverse up till index==0 and append to array of strings.
Start appending from top to bottom approach and then bottom to top approach

# roman to integers and integers to romans

always in romans, large value comes first and then smallest. i.e in below if you see VI consider it as 6 and IV consider it as 4. So if largest comes first add up else subtract and consider the value.  
di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# if there comes a problem to consider neighbours left and right, then go for left approach, then right approach and pick best from left and right

135 candy problem example

# when you are working with grids suppose like sudoku grids, Your square would be idenified as below

first square will have 9 elemnts as they fall in first square. How to represent first square is // by sqaue side i. eif your square size is 3, then 0/0 => grid can be identified as first sqaure like 0//3 =>0 and 0//3 =0 so it falls in 0th square.
this way we will index square grids as rows => 0, 1, 2 and columns => 0,1,2 so total there will be 9 square grids.
Identify your key to track sqauare as row//3 and col//3 because every row and col //3 will give 0 only for first square.

# Kadanes Algorithm

When you are asked to find the max subarray sum, maintain current sum and max sum
update current sum by max(curr, curr+curr elemnt in array)
update max sum by max(max sum, curr sum)

\*\* if you want to traverse array circularly then go for adding that array with array itself so that you will start at i and stop at i+len(nums)-1+i

# GCD is

48, 18 GCD is
48 % 18 => 12 so replace 48 with 18 and 18 with 12
18 % 12 => 6 => so replace 18 with 12 and 12 with 16
12 % 6 => 0 => so GCD is 6
stop when divisor is 0

a, b= b, a%b till b%=0

# LCD is

a\*b / gcd(a,b)

# Monototonic stack

Either you maintain increasing or decreasing order in the stack
