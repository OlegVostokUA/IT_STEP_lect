# ### CASE 1
#
# class Dragon:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     # def is_alive(self):
#     #     return self.health > 0
#
#     def get_damage(self, damage):
#         if damage >= self.health:
#             self.is_dead()
#             self.health = 0
#         else:
#             self.health -= damage
#             print(f'{self.name} give {damage} and have a {self.health}')
#         return self.health
#
#     def kick(self, other, damage):
#         other.get_damage(damage)
#
#     def is_dead(self):
#         print(f'Dragon {self.name} is dead :(((')

# ### CASE 2
# from random import randint
#
#
# class Dragon:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#
#     # def is_alive(self):
#     #     return self.health > 0
#
#     def get_damage(self, damage):
#         # shield = randint(1,4)
#         if damage >= self.health:
#             self.is_dead()
#             self.health = 0
#         else:
#             self.health -= damage
#             print(f'{self.name} give {damage} damage and have a {self.health} health')
#         return self.health
#
#     def kick(self, other, damage):
#         critical_kick = randint(1,4)
#         if critical_kick == 3:
#             damage *= 2
#             print('Crit!!!')
#         other.get_damage(damage)
#
#     def is_dead(self):
#         print(f'Dragon {self.name} is dead :(((')

### CASE 3
from random import randint


class Dragon:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    # def is_alive(self):
    #     return self.health > 0

    def get_damage(self, damage):
        shield = randint(1,4)
        if shield == 2:
            print(f'[#] {self.name} use Shield')
            damage = 0

        if damage >= self.health:
            self.is_dead()
            self.health = 0
        else:
            self.health -= damage
            print(f'[%] {self.name} give {damage} damage and have a {self.health} health')
        return self.health

    def kick(self, other, damage):
        print(f'[X] {self.name} attack {other.name}')
        critical_kick = randint(1,4)
        if critical_kick == 3:
            damage *= 2
            print(f'[!>] {self.name} use Crit!!!')
        other.get_damage(damage)

    def is_dead(self):
        print(f'[+] Dragon {self.name} is dead :(((')

d1 = Dragon('Smog', 100)
d2 = Dragon('Rog', 100)

d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)
d1.kick(d2, 10)

### CASE1 (func style)
# def main():
#     health = 100
#     finish = False
#     while not finish:
#         print(f'My health {health}. Hit me!')
#         damage = int(input())
#         health = health - damage
#         if health <= 0:
#             finish = True
#     print('You win!!!')
#
# main()

### CASE 2 (func style)
# from random import randint


# # dragon block
# def dragon_create():
#     global health
#     health = 100
#
# def dragon_is_alive():
#     return health > 0
#
# def dragon_get_damage(damage):
#     global health
#     ### shield variant
#     # shield_chance = randint(1, 4)
#     # print(shield_chance)
#     # if shield_chance == 4:
#     #     damage = 0
#     ### end shield variant
#     health = health - damage
#     if health < 0:
#         health = 0
#
# # main func
# def main():
#     dragon_create()
#     finish = False
#     while not finish:
#         print(f'My health {health}. Hit me!')
#         damage = int(input())
#         dragon_get_damage(damage)
#         if not dragon_is_alive():
#             finish = True
#     print('You win!!!')
#
# main()

