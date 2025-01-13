rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
def bnwsa(rectangles):
    zor = 0
    for a ,b in rectangles:
        kam = min(a,b)          #'min' kamtrin la a,b agaretawa
        zor = max(zor,kam)      #'max' zortrin la a,b agaretawa
        #sum(1 for a,b in rectangles)zhmaray indexakan abzhere #output 4
        #but sum(1 for a,b in rectangles if ...) # zhmara 3 anwse, chonka la if'aka tanha 3 dana yaksana 
    bzhmera = sum(1 for a , b in rectangles if min(a,b) ==zor) #sum(1 for a,b in rectangles) zhmaray indexakan abzhera #4
    return bzhmera
#calling function
eshka = bnwsa(rectangles)
print(eshka)

#3 