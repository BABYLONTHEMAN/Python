
zhmarakan = [10,50,100]

while True:
    halbena = input("zhmaraya halbena...")
    
    try:
        halbena = float(halbena)
        if halbena in (zhmarakan):
            print('OK '+ str(int(halbena)) + ' haya') #reWrite input as int   
        if halbena not in (zhmarakan) and halbena !=3.14: #boy katy 3.14 'tya nia 'sh nanwsetawa hamw jare boya (and) bakar bena
            print('tya nia ')
        if halbena not in (zhmarakan) and halbena == 3.14:
            print('PI nia ' + str(halbena))
    except ValueError:
        print('nya ')
        
        def a(a,b):
            x = a * b
            return x #without this line still works :)
        
        print(a(10,10))
#Output
#zhmaraya halbena...
#nya 
#100
#zhmaraya halbena...