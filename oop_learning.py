'''
    Learning OOP from FreeCodeCamp

    https://www.freecodecamp.org/news/crash-course-object-oriented-programming-in-python/
'''

#=======================================================================================================================================================================================#

# class Soldier:
#     health = 5
#     armor = 2
#     num_weapons = 2

#     def take_damage(self, damage):
#         self.health -= damage

#     def get_speed(self):
#         speed = 10
#         speed -= self.armor
#         speed -= self.num_weapons
#         return speed

# soldier_one = Soldier()
# soldier_one.take_damage(2)
# print(soldier_one.health)

# print(soldier_one.get_speed())

# # print("Sure.")
# # print("Sure2.")
# # print("Sure3.")
# # print("Sure4.")
# # print("Sure5.")
# # print("Sure6.")

#=======================================================================================================================================================================================#

# class Soldier:
#     def __init__(self, armor, num_weapons):
#         self.armor = 2
#         self.num_weapons = 2

# soldier = Soldier(5,10)
# print(soldier.armor)
# print(soldier.num_weapons)

# class Wall():
#     def __init__(self):
#         self.height = 10

# south_wall = Wall()
# south_wall.height = 20 # only updates this instance of a wall
# print(south_wall.height)

# north_wall = Wall()
# print(north_wall.height) #prints 10

#=======================================================================================================================================================================================#

'''
    Pillars of Object Oriented Programming:
    1. Encapsulation
'''

'''
    1. Encapsulation
        - hides complexity, only care about inputs and outputs
        - functions are a basic example of this. We don't need to know how exactly a function works every time we use it, just what to expect for inputs and outputs
'''

class Wall():
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly from an instance of a Wall

        self.__height = height


        def get_height(self):
            return self.__height
