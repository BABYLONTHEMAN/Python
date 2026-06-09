# 18_save_load_json_inventory.py
# json = save your dictionary/list into a file
# imagine game inventory save system

import json

bag = {
    "gold": 50,
    "wood": 12,
    "stone": 8
}

# save bag to file
with open("save_bag.json", "w") as file:
    json.dump(bag, file, indent=4)

print("bag saved")

# load bag back from file
with open("save_bag.json", "r") as file:
    loaded_bag = json.load(file)

print("loaded bag -> ")
print(loaded_bag)

loaded_bag["gold"] = loaded_bag["gold"] + 100
print("after reward gold -> " + str(loaded_bag["gold"]))

# OUTPUT idea:
# bag saved
# loaded bag ->
# {'gold': 50, 'wood': 12, 'stone': 8}
# after reward gold -> 150

# NOTE:
# this creates save_bag.json near your python file
# like real game save/load baby version
