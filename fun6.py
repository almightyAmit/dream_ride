from sys import exit

def Dbz():
	print ("You have entered in Dragan Ball World")
	print ("Choose your favourate character and know what they mean")
	print ("Goku\nVegeta\nGohan")
	next = input("< ")
	if next.upper() == "GOKU":
		print (r"""The name “Goku” means "awakened to emptiness"; the Go syllable means "Enlightenment", and the Ku syllable means "Sky or Emptiness". Son (孫) is also a common Chinese surname.""")
	elif next.upper() == "VEGETA":
		print (r"""Vegeta's name is a pun of the word vegetable itself. Vegeta is the prince of the Saiyans, being the son of the Saiyan king also named Vegeta, which are both in turn from the Saiyan home planet of Vegeta.""")
	elif next.upper() == "GOHAN":
		print (r"""Gohan's name comes from the Japanese word "gohan" (ご飯?, lit. "cooked rice" or "meal of any sort"), a continuation of the naming scheme of foods by Toriyama. Rice, being a grain, is not normally considered to be a vegetable, even though it is a common food.""")
		
	else:
		print("This character is not in the list you dafuk!")
		

def T_J():
	print ("You have entered in TOM & JERRY World")
	print ("Choose one of them and know your personality")
	print ("Tom or Jerry")
	next = input("< ")
	if next.upper() == "TOM":
		print ("Tom was guard of his house ")
	elif next.upper() == "JERRY":
		print ("Jerry was thief \nYour childhood was a lie")
	else:
		print ("I don't understand what you wanna say")

def Ava():
	print("You have entered in AVATAR World")
	print ("Lets see which bending ability you have\nChoose any one of them")
	print ("Aang\nZuko\nKatara\nTope\nSukko")
	next = input("< ")
	if next.upper() == "AANG":
		print ("Congratulation! You have bending ability of 'Water'\n'Air'\n'Fire'\n'Earth")
	elif next.upper() == "ZUKO":
		print ("You have hidden bending ability of Fire, now you do not have to worry in winter ;)")
	elif next.upper() == "KATARA":
		print ("You can master the ability to control water flow")
	elif next.upper() == "TOPE":
		print ("You can make earthquake if you do not control your powe")
	elif next.upper() == "SUKKO":
		print ("You have quality of freaking out, just kiddin \nYou are good friend and very intelligent") 
	else:
		print ("I think you got specs? Have you wore it? Can't you see the options")

def start():
	print ("You somehow enter the world of cartoon")
	print ("You have three door, choose any one and get surprise")
	print ("Door 1\tDoor 2\tDoor 3")
	next = input ("< ") 
	if next.upper() == "DOOR 1":
		Dbz()
	elif next.upper() == "DOOR 2":
		T_J()
	elif next.upper() == "DOOR 3":
		Ava()
	else:
		print ("You need doctor checkup")
		exit(0)
	for i in range(0,201):
		print ("Boom!", end="")
	print ("\nAahaa atlast you are awake, you where dreaming from then, Lets go and have some snaks")
	exit(0)

start()




