
[[2,1,3],[6,5,4],[7,8,9]]
13

[[-19,57],[-40,-5]]
-59



== 0
0,1
==1


== n
n,n-1
0<i<n
i-1,i,i+1

def find_min_path(n, array):
    min_path = 0
    for i in range(n):
        if i==0 and i==n:
            min_path = i
        if i==0 and i<n-1:
            min_path =  array[i]   