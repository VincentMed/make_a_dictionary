# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:53:06 2022

@author: Vincent Medrano
"""

# make a dictionary the contains 'Family' members
# (Family in quotes because I do not want real name or birthday... make them)
# at least 5 'immediate' family members.
# object for each member contains birthday (string), favorite color, 
# favorite recording artist(s)


from collections import OrderedDict


my_dict = {"Herman" : ["Birthday: January 20, 1920" , "Favorite Color: Red", "Favorite Artist: Ke$ha"],
           "Alicia" : ["Birthday: March 14, 1921", "Favorite Color: Blue", "Favorite Artist: Chipmunks"],
           "Vincent" : ["Birthday: December 17, 1951", "Favorite Color: Orange", "Favorite Artist: Tupac"],
           "Richard" : ["Birthday: January 9, 1952", "Favorite Color: Pink", "Favorite Artist: Depeche Mode"],
            "Blobber": ["Birthday: February 18, 1955", "Favorite Color: Green", "Favorite Artist: Ace of Base"],
            }
# 1. print the dictionary
print(my_dict)

# 2. add an entry for new member of the family (no recording artist)
my_dict["Whoopsie"] = "Birthday: June 20, 1920" , "Favorite Color: Red"

# 3 print values for member of the family
for key, value in my_dict.items():
    print(key, ': ', value)

# whose name string starts with whoever is first in the alphabet,
# sort dictionary list by keys alphabetically
my_dict = OrderedDict(sorted(my_dict.items()))

# assign a variable for first key in list
first_dict_item = list(my_dict.keys())[0]

print("First name in alphabet order is: " + first_dict_item)




