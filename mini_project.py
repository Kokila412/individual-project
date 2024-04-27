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
    temp=0
    for i in range(len(selected_word)): 
           if selected_word[i]==a:
                if len(guessed)==0:
                   guessed=guessed+a
                elif guessed[len(guessed)-1]==selected_word[i-1]:
                     if temp!=total_chance:
                      guessed=guessed+a
           else:
                print("-")
                fail=fail+1
    if fail==len(selected_word):
         print(total_chance,"chances left")
         print()
         temp=total_chance
         total_chance=total_chance-1
    else:
        print(guessed, end=" ")
        print()
    if guessed==selected_word:
       print(guessed)
       break
        
if total_chance==0:
    print("failed")

