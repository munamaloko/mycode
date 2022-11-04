#!/usr/bin/env python3

heroes= {"flash":
                   {"speed": "fastest", 
                    "intelligence": "lowest", 
                    "strength": "lowest"}, 
         "batman":
                   {"speed": "slowest", 
                    "intelligence": "highest", 
                    "strength": "money"}, 
         "superman":
                   {"speed": "fast", 
                    "intelligence": "average", 
                     "strength": "strongest"}}

#char_name= input("which character do you want? (Flash...)")

#print(char_name)


print(f"Flash is {heroes['flash']['speed']}!")
print(heroes["superman"]["strength"])
print(f"Superman is " +heroes['superman']['strength'] + "!")
print(heroes["batman"]["strength"])
print(f"Batman has the ultimate super power: {heroes['batman']['strength']}")
