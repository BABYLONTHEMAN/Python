naw = "aha "
taman = 70

prsyar = " 7alaty darwni am kasa chona??! "
rsta = " am kasay nawi hatwa 7alaty darwniakay ..."
hamwy = (naw + str(taman))
print (naw + str(taman))
#print (prsyar)
halat = input(prsyar)
okya = "shet nia"
okNya = "sheta tawaw nia"
if halat in ("OK", "yes"," basha"):
    print(hamwy + rsta + okya)
elif halat in ("sheta","Not", "shet"):
    print(hamwy + rsta + okNya)
elif halat == "":
    print("kas nazane sheta ya na ")