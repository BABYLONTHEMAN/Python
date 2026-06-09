# 16_list_of_dicts_npc_shop.py
# list of dictionaries = many small boxes
# each NPC/item is one dictionary

shop = [
    {"naw": "sword", "price": 100, "damage": 25},
    {"naw": "axe", "price": 80, "damage": 30},
    {"naw": "apple", "price": 5, "heal": 10}
]

print("--- SHOP ITEMS ---")

for item in shop:
    print(item["naw"] + " price -> " + str(item["price"]))

print("\n--- expensive stuff ---")

for item in shop:
    if item["price"] >= 80:
        print(item["naw"] + " qimata, price = " + str(item["price"]))

print("\n--- search one item ---")

search = "axe"

for item in shop:
    if item["naw"] == search:
        print("found -> " + item["naw"])
        print(item)

# OUTPUT idea:
# --- SHOP ITEMS ---
# sword price -> 100
# axe price -> 80
# apple price -> 5
#
# --- expensive stuff ---
# sword qimata, price = 100
# axe qimata, price = 80
#
# --- search one item ---
# found -> axe
# {'naw': 'axe', 'price': 80, 'damage': 30}
