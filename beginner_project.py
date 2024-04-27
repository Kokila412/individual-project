# a program where the user have to find the word with the hint given.the program will fill the dashes 
# when the letter us correct either randomly or in a sequential order
import random 
list=["rose","jasmine","tulip","dahlia","sunflower","marigold",
      "lily","lotus"]
print("HINT: it's a flower")
flower=random.choice(list)
guess=[]

chances=len(list)
if __name__=='__main__'
	for i in flower:
	guess.append("-")
	for i in guess:
	print(i, end=" ")
	try:
	while chances>0:
		print()
		ans=input("enter your input:")
		fail=0
		if not ans.isalpha():
			print("please, enter an alphabet")
		if len(ans)>1:
			print("enter only a single character")
		for i in range(len(flower)):
				if flower[i]==ans:
					guess[i]= flower[i]
				else:
					fail=fail+1
		for i in guess:
			print(i, end=" ")
		if "-" not in guess:
				print()
				print("congrats")
				break
		if fail==len(flower):
			chances=chances-1
	except KeyboardInterrupt:
		print()
		print("failed")
		exit()
