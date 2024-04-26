import random

list_of_words=["banana","apple","condition","chopper","luffy","durian"
               ,"tofu","kokila","nail","phone"]

selected_word = random.choice(list_of_words)
total_chance = len(list_of_words)
guessed=""
while total_chance>0:
    fail=0
    for char in selected_word:
          a=print(input("enter a char:"))
          if a==char:
            guessed=guessed+a
            print(guessed)
          else:
              print("-")
              fail += 1
              total_chance -= 1
    if total_chance==0:
        print("failed")
  
