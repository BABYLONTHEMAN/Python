# 19_class_player_monster.py
# class = blueprint / mold
# object = one real thing made from that blueprint

class Fighter:
    def __init__(self, naw, health, damage):
        self.naw = naw
        self.health = health
        self.damage = damage

    def hit(self, enemy):
        enemy.health = enemy.health - self.damage
        print(self.naw + " hit " + enemy.naw)
        print(enemy.naw + " health -> " + str(enemy.health))

    def alive(self):
        return self.health > 0


player = Fighter("qala", 100, 25)
monster = Fighter("orc", 80, 15)

player.hit(monster)
monster.hit(player)
player.hit(monster)

if monster.alive():
    print(monster.naw + " still alive")
else:
    print(monster.naw + " dead")

# OUTPUT idea:
# qala hit orc
# orc health -> 55
# orc hit qala
# qala health -> 85
# qala hit orc
# orc health -> 30
# orc still alive

# monkey brain note:
# self.naw means THIS fighter's name
# enemy.health means the other guy health
