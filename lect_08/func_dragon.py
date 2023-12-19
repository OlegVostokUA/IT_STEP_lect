
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

