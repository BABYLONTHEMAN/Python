# 15_dictionary_inventory.py
# dictionary = list but with names instead of index numbers
# list index: zhmarakan[0]
# dict key:   bag["gold"]

bag = {
    "gold": 10,
    "stone": 4,
    "apple": 2
}

print(bag)
print("gold haya -> " + str(bag["gold"]))

# add more gold
bag["gold"] = bag["gold"] + 5
print("gold dwai zyad krdn -> " + str(bag["gold"]))

# new item, keyaka peshtr nya, python drwsty akat
bag["diamond"] = 1
print(bag)

# loop over dictionary
for naw, bzhmer in bag.items():
    print(naw + " = " + str(bzhmer))

# OUTPUT idea:
# {'gold': 10, 'stone': 4, 'apple': 2}
# gold haya -> 10
# gold dwai zyad krdn -> 15
# {'gold': 15, 'stone': 4, 'apple': 2, 'diamond': 1}
# gold = 15
# stone = 4
# apple = 2
# diamond = 1
