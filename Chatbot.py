
>>> import random
... print("Chatbot : I am your chatbot how can i help you")
... print("Type bye to end the Chatbot")
... hii=["Hello ","yes i am here","Welcome to chatbot"]
... how_are_you=["I am fine ","I am a code ","but i am fine","Almost fine","by gods grace fine"]
... bye=["Byee","Nice to meet you","Take care","Every moment is  memorable to  me"]
... default_question=["Can you please tell me again ","Sorry i cant understand","I cannnot answer the question  you asked"]
... 
... while True:
... 	user=input("You :").lower()
... 	if user=="hii" or user=="hello":
... 		print("Chatbot :",random.choice(hii))
... 	elif user=="how_are_you" or user=="how_r_u":
... 		print("Chatbot :",random.choice(how_are_you))
... 	elif user=="name": 
... 		print("Chatbot : My name is Personal robot")
... 	elif user=="age":
... 		print("Chatbot : I cant tell my age")
... 	elif user=="creator":
... 		print("Chatbot : I was created by python")
... 	elif user=="bye" or user=="byee":
... 		print("Chatbot :",random.choice(bye))
... 		break
... 	else:
