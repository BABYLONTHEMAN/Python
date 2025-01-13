matrix = [[1,2,3],[3,1,2],[2,3,1]]
n = len(matrix)
print(n)

out = sorted(matrix)
xout = (0)
if xout != list(range(3, n -2)):   #list(range(n, n+1)) #output: 3 
    xout = list(range(1, n+2))
    print(out)
    print(xout)
#3
#[[1, 2, 3], [2, 3, 1], [3, 1, 2]]
#[1, 2, 3, 4]