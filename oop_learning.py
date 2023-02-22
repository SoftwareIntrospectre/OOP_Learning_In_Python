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
    2. Abstraction
    3. Inheritance
'''

'''
    1. Encapsulation
        - contains the logic into a "black box", only care about inputs and outputs
        - functions are a basic example of this. We don't need to know how exactly a function works every time we use it, just what to expect for inputs and outputs
'''

# class Wall():
#     def __init__(self, height):
#         # this stops us from accessing the __height
#         # property directly from an instance of a Wall

#         self.__height = height


#         def get_height(self):
#             return self.__height

# # results in an error (Which is good, because I want to prevent this behavior)
# #front_wall = Wall()
# #front_wall.__height = 10


'''
    2. Abstraction
        - handle complexity by hiding unnecessary details
            - as a process: extracting the essential details about an item(s)
                            while ignoring inessential details

            - as an entity: denotes a model, view, or some other focused representation
                            of the item(s)

                            
        - Not the same as Encapsulation
        - Not the same thing as Information Hiding (Me: LOL! Sure.)
        Abstraction vs. Encapsulation
            - Abstraction = technique TO IDENTIFY WHAT INFORMATION AND BEHAVIOR
                            that should be hidden and what should be exposed
            - Encapsulation = technique FOR ORGANIZING CODE to capture what should be hidden and what is intended to be visible    

                - article: https://web.archive.org/web/20210513154547/https://www.tonymarston.net/php-mysql/abstraction.txt
                "
                    CONCLUSIONS

                    Abstraction, information hiding, and encapsulation are very different,
                    but highly-related, concepts. One could argue that abstraction is a
                    technique that helps us identify which specific information should be
                    visible, and which information should be hidden. Encapsulation is then
                    the technique for packaging the information in such a way as to hide
                    what should be hidden, and make visible what is intended to be visible.

                    It is not hard to see how abstraction, information hiding, and
                    encapsulation became confused with one another. Further, one could
                    argue that, regardless of their "dictionary definitions," these terms
                    have evolved new meanings in the context of software engineering, e.g.,
                    in much the same way as "paradigm" has. (See, e.g., [Kuhn, 1962].)
                    However, a stronger argument can be made for keeping the concepts, and
                    thus the terms, distinct.
                "
                - read, re-read, and be able to explain this in my own words with examples
'''

# import random

# my_random_number = random.randrange(5)
# print(my_random_number)
# # I don't need to know how Python is generating a random number because I don't need to.
# # I pass in the range as an integer, and it does what I expect


'''
    3. Inheritance
        - Allows a child class to "inherit" the properties and methods of its parent class
        - When to use: only when EVERY instance of child class can be also considered
                       the same type as the parent class

            - Why: A child class inherits EVERYTHING from parent. 
                - If I only want to share SOME functionality, don't use Inheritance
                - "All cows are animals but not all animals are cows."
'''

# class Animal:
#     # parent "Animal Class"
#     pass

# class Cow(Animal):
#     # child class "Cow" inherits "Animal"
#     pass

'''
    in Python: use super() method to use parent class' constructor
    in Python: no limit to inheritance tree (powerful tool, but need to use wisely)
'''

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to give the cow some legs
        super().__init__(4)