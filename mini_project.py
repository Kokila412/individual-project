import random

list_of_words=["banana","apple","condition","chopper","luffy","durian"
               ,"tofu","kokila","nail","phone"]

selected_word = random.choice(list_of_words)
total_chance = len(list_of_words)
guessed=""
print(len(selected_word),"lettered word",selected_word)
while total_chance>0:
    a=input("enter a char:")
    fail=0
    count=0
    temp=1
    for char in selected_word: 
          if a in selected_word:
               count+=1
          if a == char:
             guessed=guessed+a
             print(guessed)
          else:
              fail=fail+1
              print("-",fail)
    if guessed==selected_word:
              break
    if fail==len(selected_word):
        total_chance -= 1

if total_chance==0:
    print("failed")

