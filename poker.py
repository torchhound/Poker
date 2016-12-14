from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator
import random
import argparse
from itertools import product

def singleDeck():
	"""Returns a single unshuffled deck"""
	deck = []
	base = list(product(range(2, 15), range(1, 5)))
	for args in base:
		deck.append(Card(*args))
	return deck

def calcFlopWins(decks, players, trials):
	"""
	Lets the user input a number of decks D, a number of players P, and a number of trials N. Then it plays N rounds of texas hold-em with P players and D decks. Returns the percentage of those N rounds in which the player with the best cards after the flop ended up winning the round. So specifically, for each round, after the flop it finds the player with the best cards, and sets total += 1 if that player wins the round, and total += 0 if that player doesn't win. Returns count / N.
	"""
	try:
		count = 0 #number of times player with best cards after the flop wins the hand
		while trials >= 0: #play selected number of hands
			deck = [] #initialize empty deck
			for x in range(decks): #append shuffled deck(s)
				deck.extend(singleDeck())
			random.shuffle(deck) #shuffle deck
			flopBest = "" 
			winner = ""
			board = []
			hands = {}
			for x in range(players): #create hands and add them to dictionary
				hands[x] = [deck.pop() for __ in range(2)]
			for __ in range(3):
				board.append(deck.pop()) #create the flop
			for __ in range(2): #add padding because evaluate_hand only accepts 2, 5, or 7 arguments
				board.append(Card(3, 2))
			for x in range(players): #find the winner after the flop
				score = 0
				print(len(hands[x]), len(board))
				if HandEvaluator.evaluate_hand(hands[x], board) >= score:
					flopBest = hands[x]
			for __ in range(2): #remove padding
				del board[-1]
			board.append(deck.pop()) #create the turn
			board.append(deck.pop()) #create the river
			for x in range(players): #find the winner of the hand
				score = 0
				if HandEvaluator.evaluate_hand(hands[x], board) >= score:
					winner = hands[x]
			if flopBest == winner: #check if the winner of the hand was also on top after the flop
				count += 1
		return count / trials
	except TypeError as e: #catch error from no args present
		print("No args present")
		pass
	#except Exception as e:
	#	print("other error")
	#	pass
			
def main():
	parser = argparse.ArgumentParser(description=calcFlopWins.__doc__)
	parser.add_argument("decks", nargs="?", const=1, type=int)
	parser.add_argument("players", nargs="?", const=2, type=int)
	parser.add_argument("trials", nargs="?", const=1, type=int)
	args = parser.parse_args()
	print("count / trials = {}".format(calcFlopWins(args.decks, args.players, args.trials)))
	
if __name__ == "__main__":
	main()