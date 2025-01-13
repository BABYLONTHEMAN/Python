import random

zhmarakan = [30,40,50]
naw = 'qala'
#input() always returns a string 
while True: 
    nwsin = input(" bzanm zhmaraka azani?")
    try: # here we trying to convert the user_input 'nwsin' into number
        nwsin = float(nwsin) #pey alein nwsin zhmaraya
        if nwsin in zhmarakan:
            print(" OK zanit "+ str(nwsin))
        else:
            print(" xoy nia nawzai " + str(nwsin) + " nia")
        if nwsin ==3.14:
            print(" PI nia ")
        
    except ValueError: #ERR cuz the user_input 'nwsin' was not the number so triggered the error,
                       #now we back to the origin string domain cuz the input() always returns a string as we said before 
                       #ValueError is a Built_In_exception stuff like 'SyntaxError', 'SystemError'
        if nwsin.lower() =="exit":
            break
        else:
            print('letter entered, try number or exit to quit...')