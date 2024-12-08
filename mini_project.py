import random

list_of_words=["banana","pen","condition","chopper","luffy","durian"
               ,"tofu","kokila","nail","phone"]

selected_word = random.choice(list_of_words)
total_chance = 3
guessed=""
print("make your guess")
print("HINT! after first mistake find the number of - to find the number of letters")
count=0
while total_chance>0:
    a=input("enter a single character:").lower()
    if a is not a.isalpha():
      print("Please enter an alphabet")
    elif a not in selected_word:
          total_chance-=1
          print(f"you have {total_chance} chances left")
          print(f"so far you have guessed: {guessed} enter the next guessed character")
          if len(guessed)==0:
            print("-"*len(selected_word))
     elif a in selected_word:
          for i in range(len(selected_word)): 
                         if count==i:
                              guessed=guessed+a
                              print(guessed)
          count=count+1
     if guessed==selected_word:
       print("congrats!you have a strong intuition. the word is",guessed, "you win!")
       break
if total_chance==0:
    print("failed, the answer is",selected_word)

