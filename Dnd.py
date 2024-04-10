import functions.py
import random


#Generates name for warlock
warlock1 = ["Zarg", "Vil","Varth","Mor","Gul","Dorn","Hor", "Vorn","Zil","Org"]
warlock2 = ["a","e","i","o","u","y","oa","ua","ia","'"]
warlock3 = ["thrax","vax","vixis", "dan","grol","zal","x","dol","xill","ks","lich"]
warlockName = warlock1[random.randint(0,9)]+warlock2[random.randint(0,9)]+warlock3[random.randint(0,9)]

#Generates Demon Name
demon1 = ["Far", "Kor", "Yixx", "Lak", "Gulk", "Pul", "Gak", "Muck", "Sikk", "Schall"]
demon2 = ["Virilliath", "Zilliax", "Noctus","Gulffus","Adolphus", "Alnor", "Orrgus", "Gorgus"]
demonName = demon1[random.randint(0,9)]+"'"+demon2[random.randint(0,7)]

print("Welcome to 'Apocalypse!' An evil sorcerer,", warlockName,"threatens to destroy the kingdom of Gorroth, and in the hills of Ghomshief lies a cave where he begins a dark ritual to summon the demon",demonName+".")

#Determines player's default class. While loop lets them confirm their class, and select another class if need be.
print("It is up to you to stop him, hero, lest the universe fall into the hands of evil once more.")
while True:
     playerClassName = input("To begin your journey, select one of the following classes: Cleric, Mage, Thief, Warrior.\n").lower()
     if playerClassName not in Characters.keys():
         print(failedInput)
         continue
     else:
        while True:
            print("You have selected", playerClassName.title()+", is that correct? Y/n")
            confirmed = input().lower()
            if confirmed == "y":
                print("Welcome,",playerClassName.title()+", let us begin your journey...")
                break
            elif confirmed == "n":
                print("Please select another class, then.")
                break
            else:
                print(failedInput)
                continue
        if confirmed == "y":
            break
        else:
            continue
         

