import random
sets = ['Heart', 'Diamond', 'Spade', 'Club']
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []
for set in sets:
	for number in numbers:
		cards.append(f"{set} {number}")

shuffledCards = list()
shuffledCards.extend(cards)
random.shuffle(shuffledCards)
shuffledCards1 = shuffledCards[:21]
for card in shuffledCards1:
	print(card)

print("\nChoose a card from the listed cards and write it down somewhere !")
print("I am going to find what card you chose :)")
print("\n")


def splitIntoThree(deck):
	num = 0
	deck1 = list()
	deck2 = list()
	deck3 = list()
	for card in deck :
		num += 1
		if num == 1:
			deck1.append(card)
		if num == 2:
			deck2.append(card)
		if num == 3:
			deck3.append(card)
		if num > 3:
			num = 1
			deck1.append(card)
	print("  Deck 1     |   Deck 2      |    Deck 3 ")
	for card1, card2, card3 in zip(deck1, deck2, deck3):
		print(card1, " "*(15-len(card1)), card2, " "*(15-len(card2)), card3)
	return deck1, deck2, deck3

split1 = splitIntoThree(shuffledCards1)
split1Deck1 = split1[0]
split1Deck2 = split1[1]
split1Deck3 = split1[2]

n = 1
while True:
	while True:
		if n>1:
			print("Invalid deck number ! (re-enter deck number)")
		else:
			print()
			print("Which deck the card you chose is ?\n(Enter the deck number)")
		deckNo = input()
		if deckNo == "1" or deckNo == "2" or deckNo == "3":
			deckNo = int(deckNo)
			break
		else:
			n += 1
			continue
	print()
	print("Are you sure that the card you chose is in this deck ?")

	if deckNo == 1:
		for card in split1Deck1:
			print(card)
	elif deckNo == 2:
		for card in split1Deck2:
			print(card)
	elif deckNo == 3:
		for card in split1Deck3:
			print(card)

	while True:
		print()
		confirm = input("(y/n)\n")
		if confirm.lower() == "y" or confirm.lower() == "n":
			break
		else:
			continue
	if confirm.lower() == "n":
		continue
	else:
		break

shuffledCards2 = list()

if deckNo == 1:
	shuffledCards2.extend(split1Deck2)
	shuffledCards2.extend(split1Deck1)
	shuffledCards2.extend(split1Deck3)
if deckNo == 2:
	shuffledCards2.extend(split1Deck1)
	shuffledCards2.extend(split1Deck2)
	shuffledCards2.extend(split1Deck3)
if deckNo == 3:
	shuffledCards2.extend(split1Deck2)
	shuffledCards2.extend(split1Deck3)
	shuffledCards2.extend(split1Deck1)

#######################################################################################

split2 = splitIntoThree(shuffledCards2)
split2Deck1 = split2[0]
split2Deck2 = split2[1]
split2Deck3 = split2[2]

n = 1
while True:
	while True:
		if n>1:
			print("Invalid deck number !")
		else:
			print()
			print("Which deck the card you chose is ?\n(Enter the deck number)")
		deckNo = input()
		if deckNo == "1" or deckNo == "2" or deckNo == "3":
			deckNo = int(deckNo)
			break
		else:
			continue
	print()
	print("Are you sure that the card you chose is in this deck ?")

	if deckNo == 1:
		for card in split2Deck1:
			print(card)
	elif deckNo == 2:
		for card in split2Deck2:
			print(card)
	elif deckNo == 3:
		for card in split2Deck3:
			print(card)

	while True:
		print()
		confirm = input("(y/n)\n")
		if confirm.lower() == "y" or confirm.lower() == "n":
			break
		else:
			continue
	if confirm.lower() == "n":
		n += 1
		continue
	else:
		break

shuffledCards3 = list()

if deckNo == 1:
	shuffledCards3.extend(split2Deck2)
	shuffledCards3.extend(split2Deck1)
	shuffledCards3.extend(split2Deck3)
if deckNo == 2:
	shuffledCards3.extend(split2Deck1)
	shuffledCards3.extend(split2Deck2)
	shuffledCards3.extend(split2Deck3)
if deckNo == 3:
	shuffledCards3.extend(split2Deck2)
	shuffledCards3.extend(split2Deck3)
	shuffledCards3.extend(split2Deck1)

#######################################################################################

split3 = splitIntoThree(shuffledCards3)
split3Deck1 = split3[0]
split3Deck2 = split3[1]
split3Deck3 = split3[2]

n = 1
while True:
	while True:
		if n>1:
			print("Invalid deck number !")
		else:
			print()
			print("Which deck the card you chose is ?\n(Enter the deck number)")
		deckNo = input()
		if deckNo == "1" or deckNo == "2" or deckNo == "3":
			deckNo = int(deckNo)
			break
		else:
			continue
	print()
	print("Are you sure that the card you chose is in this deck ?")

	if deckNo == 1:
		for card in split3Deck1:
			print(card)
	elif deckNo == 2:
		for card in split3Deck2:
			print(card)
	elif deckNo == 3:
		for card in split3Deck3:
			print(card)

	while True:
		print()
		confirm = input("(y/n)\n")
		if confirm.lower() == "y" or confirm.lower() == "n":
			break
		else:
			continue
	if confirm.lower() == "n":
		n += 1
		continue
	else:
		break

shuffledCards4 = list()

if deckNo == 1:
	shuffledCards4.extend(split3Deck2)
	shuffledCards4.extend(split3Deck1)
	shuffledCards4.extend(split3Deck3)
if deckNo == 2:
	shuffledCards4.extend(split3Deck1)
	shuffledCards4.extend(split3Deck2)
	shuffledCards4.extend(split3Deck3)
if deckNo == 3:
	shuffledCards4.extend(split3Deck2)
	shuffledCards4.extend(split3Deck3)
	shuffledCards4.extend(split3Deck1)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("The card you chose is :")
print(shuffledCards4[10])