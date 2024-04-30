import random
from art import logo
from database import data
from art import vs
score=0
def choice():
    a=input("do you wanna play y/n?").lower()
    if a=="y":
        display(score)
    elif a=="n":
        print("program ended successfully!")
    else:
        print("enter a valid input")
def assign():
    return random.choice(data)
def play_higher_or_lower(p1,p2,userdata):
    maxvalue=0
    p1followers=p1["follower_count"]
    p2followers=p2["follower_count"]
    
    if p1followers>p2followers:
        maxvalue=p1["name"]
    elif p2followers>p1followers:
        maxvalue=p2["name"]
    if maxvalue==userdata:
        return True
    else:
        return False
def display(score):
        playing=1
        if score==0:
            print(logo)
        person1=assign()
        person2=assign()
        while playing:
            while person1==person2:
                person2=assign()
            print(f"Name:{person1['name']}, Desc:{person1['description']}")
            print(vs)
            print(f"Name:{person2['name']}, Desc:{person2['description']}")
            guess=input("enter the person who has large number of followers:")
            if play_higher_or_lower(person1,person2,guess):
                score=score+1
                print("your score is",score)
            else:
                playing=0
            b=input("wanna keep guessing?").lower()
            if b=="y":
                display(score)
            else:
                print("program ended successfully")
                playing=0

choice()
