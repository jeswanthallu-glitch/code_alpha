Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... list=["dheeraj","hasini","varun","love","youtube"]
... word=random.choice(list)
... print("Welcome to the hangman game")
... display=["_"]*len(word)
... print("Word: "," ".join(display))
... guessed_letter=[]
... tries=6
... while tries>0:
... 	guess=input("\nEnter the letter :").lower()
... 	if len(guess)!=1 or not guess.isalpha():
... 		print("Enter the single alphabet")
... 		continue
... 	if guess in guessed_letter:
... 		print("You have already guessed the letter")
... 		continue
... 		
... 	guessed_letter.append(guess)
... 	if guess in word :
... 		print("Good guess")
... 	else:
... 		tries-=1
... 		print(f"wrong guess and you have {tries} tries left")
... 		
... 		
... 	display=[letter if letter in guessed_letter  else "_" for letter in word]
... 	print("Word:"," ".join(display))
... 	if "_" not in display:
... 			print("congragulation you have won the game")
... 			break
... else:
