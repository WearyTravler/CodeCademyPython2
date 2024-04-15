"""
Description:
Author:  
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %ss in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

name = input("What is your name: ")
feeling = input("Give me a feeling: ")
adjective1 = input("Give me an adjective: ")
animal1 = input("Give me an animal: ")
object1 = input("Give me an object: ")
dance = input("Give me a type of dance: ")
musical_instrument = input("Give me a musical instrument: ")
adjective2 = input("Give me another adjective: ")
person = input("Give me a person: ")
place = input("Give me a place: ")
food = input("Give me a food: ")
year = input("Give me a year: ")


print(STORY % (name, feeling, adjective1, animal1, object1, dance, musical_instrument, animal1, adjective2, name, person, name, place, name, food, name, year, animal1 ))

















