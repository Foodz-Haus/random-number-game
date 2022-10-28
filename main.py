""" First we will import random so we can get basically random numbers from the computer side"""
import random

comp = random.randint(0,10)
human = int(input("Enter a number from 0 to 10 \n"))
if comp == human:
    print("You think like the computer. Maybe you yourself is an computer. Are you real? Am I real?")
else:
    print("You ain't smart as the computer")