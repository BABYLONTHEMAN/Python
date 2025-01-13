def vowel(s):
    forwardka = '' #test letters back and forth
    backwardka = ''
    vowelakan = 'aoeiu'
    countVowel =0
    #vowelakan = vowelakan.lower()
    for i in s:
        if i in vowelakan:
            countVowel = countVowel +1
            forwardka = i + forwardka
            print('for > '+ forwardka)
            backwardka = backwardka + i
            print('back >' + backwardka)
    return countVowel
    
inp = 'Hello Worldsz'
print(vowel(inp))

# 3
#for > ooe
#back >eoo