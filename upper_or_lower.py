import random
from art import logo
from database import data
from art import vs

def choice():
    a=input("do you wanna play y/n?").lower()
    if a=="y":
        choice()
    elif a=="n":
        print("program ended successfully!")
    else:
        print("enter a valid input")
    
def assign():
    return random.choice(data)
def display(guess):
    if choice():
        print(logo)
        person1=assign()
        person2=assign()
        print(f"Name:{person1['name']}, Desc:{person1['description']}")
        print(vs)
        print(f"Name:{person2['name']}, Desc:{person2['description']}")
        guess=input("enter the person who has large number of followers:")
        play_higher_or_lower(person1,person2,guess)
    
def play_higher_or_lower(p1,p2,userdata,maxvalue):
    maxvalue=0
    score=0
    p1followers=p1["follower_count"]
    p2followers=p2["follower_count"]
    
    if p1followers>p2followers:
        maxvalue=p1["name"]
    elif p2followers>p1followers:
        maxvalue=p2["name"]
    if maxvalue==userdata:
        score+=1
    else:
        choice()
    print("your score is",score)
