# 17_function_return_vs_print.py
# print = show me now
# return = give answer back so I can use it later


def damage(enemy_health, hit_power):
    new_health = enemy_health - hit_power
    return new_health


def damage_print(enemy_health, hit_power):
    new_health = enemy_health - hit_power
    print(new_health)


orc_hp = 100

# return version
orc_hp = damage(orc_hp, 25)
print("orc hp after hit -> " + str(orc_hp))

orc_hp = damage(orc_hp, 40)
print("orc hp after second hit -> " + str(orc_hp))

print("--- print function test ---")

# print version only shows number, but does not give it back
x = damage_print(100, 25)
print("x is -> " + str(x))  # None, chonka function return nyia

# OUTPUT:
# orc hp after hit -> 75
# orc hp after second hit -> 35
# --- print function test ---
# 75
# x is -> None
