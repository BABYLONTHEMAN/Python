points = [(2,3,4) , (1,-2,8) , (-4,3,0) ,(100,-5,-2)]
points.sort(key = lambda x:x[2])
print(points)


#points = [(2,3,4) , (1,-2,8) , (-4,3,0) ,(100,-5,-2)] x 3 indexy haya wata x[2]
 #points = [(2,3) , (1,-2) , (-4,3) ,(100,-5)] x 2 indexy haya wata x[1] so on
while True:
    x=points
    x.sort(key=lambda x:x[0])
    print (x)
    
    prs = input("atawe dwbara ? -> ")
    if prs in ("yes","bale","a" ,"y" ,"ok" , "ya"):
       print(x)
    else:
        break

#klpa