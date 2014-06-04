from sys import exit

def gold_room():
	print "This room is foll of gold. How much do you take?"

	next = raw_input("> ")
	how_much = int(next)
	if how_much <= 0:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you'r not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print """The bear has a bunch of honey.\n
	The fat bear is in fron of another door.\n
	How are you going to move the bear.\n"""
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you than slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bar has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear get pissed off and chews your leg off")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea wha that means"

def cthulhu_room():
	print """Here you see the great evil Cthulhu.\n
	He, it, whatever stares at you and you go insane.\n
	Do you flee for your life of eat your head.\n"""

	next = raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print """You are in a dark room.\n
	There is a door to your right and left.\n
	Which one do you take?\n"""
	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()