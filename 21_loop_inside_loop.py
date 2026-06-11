List = ("abc", "def")

def word_function(pawn):
    while True:
        x = input("type >> ")
        for w in List:
            if "b" in w and x not in w and x != "klpa":
                print("word is ~>> " + w)
            elif "b" in w and x in w:
                print("you seen the code?")
        if x == "klpa":
            sure = input("sure? yes or no ")
            if sure in ["no", "No", "n", "N"]:
                print("okay let's continue")
            elif sure in ["yes", "yea", "y", "ye"]:
                print("passcode used fair enough")
            break

word_function(List)
