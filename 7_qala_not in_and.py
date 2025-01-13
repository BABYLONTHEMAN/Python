naw = 'qala'

zhmarakan = [10,50,100]


while True:
    halbena = input("zhmaraya halbena...")
    halbena = float(halbena)
    try:
        
        if halbena in (zhmarakan):
            print('OK '+ str(int(halbena)) + ' haya') #reWrite input as int   
        if halbena not in (zhmarakan) and halbena !=3.14: #boy katy 3.14 'tya nia 'sh nanwsetawa hamw jare boya (and) bakar bena
            print('tya nia ')
        if halbena not in (zhmarakan) and halbena == 3.14:
            print('PI nia ' + str(halbena))
    except ValueError:
        print('nya ')
#......................................................
        #OUTPUT....................
	#zhmaraya halbena...
	#10
	#OK 10 haya
	#zhmaraya halbena...
	#99
	#tya nia 
	#zhmaraya halbena...
	#3.144
	#tya nia 
	#zhmaraya halbena...
	#3.14
	#PI nia 3.14
	#zhmaraya halbena...

