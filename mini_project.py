import random

list_of_words=["banana","pen","condition","chopper","luffy","durian"
               ,"tofu","kokila","nail","phone"]

selected_word = random.choice(list_of_words)
total_chance = len(list_of_words)
guessed=""
print("make your guess")
print("HINT! after first mistake find the number of - to find the number of letters")
count=0
while total_chance>0:
    a=input("enter a char:")
    fail=0
    for i in range(len(selected_word)): 
           if selected_word[i]==a:
                if len(guessed)==0:
                   guessed=guessed+a
                elif guessed[len(guessed)-1]==selected_word[i-1]:
                     if count==i:
                      guessed=guessed+a
           else:
                print("-")
                fail=fail+1
    count=count+1
    if fail==len(selected_word):
         total_chance=total_chance-1
         print("entered letter is not in the word,try again",total_chance,"chances left")
         print()
         count=count-1
    else:
        print(guessed, end=" ")
        print()
    if guessed==selected_word:
       print("congrats!you have a strong intuition. the word is",guessed, "you win!")
       break
        
if total_chance==0:
    print("failed, the answer is",selected_word)

