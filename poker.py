import poker
from pokereval.hand_evaluator import HandEvaluator
import random
import argparse

def singleDeck():
	"""Returns a single shuffled deck"""
	deck = list(poker.Card)
	return random.shuffle(deck)

def calcFlopWins(decks, players, trials):
	"""
	Lets the user input a number of decks D, a number of players P, and a number of trials N. Then it plays N rounds of texas hold-em with P players and D decks. Returns the percentage of those N rounds in which the player with the best cards after the flop ended up winning the round. So specifically, for each round, after the flop it finds the player with the best cards, and sets total += 1 if that player wins the round, and total += 0 if that player doesn't win. Returns count / N.
	"""
	deck = [] #initialize empty deck
	count = 0 #number of times player with best cards after the flop wins the hand
	for x in len(decks): #append shuffled decks
		deck.append(singleDeck())
	while trials >= 0: #play selected number of hands
		flopBest = "" #initialize variables
		winner = ""
		board = []
		players = {}
		for x in len(players): #create hands and add them to dictionary
			players[x] = [deck.pop() for __ in range(2)]
		board.append([deck.pop() for __ in range(3)]) #create the flop
		for x in len(players): #find the winner after the flop
			score = 0
			if HandEvaluator.evaluate_hand(players[x], board) >= score:
				flopBest = players[x]
		board.append(deck.pop()) #create the turn
		board.append(deck.pop()) #create the river
		for x in len(players): #find the winner of the hand
			score = 0
			if HandEvaluator.evaluate_hand(players[x], board) >= score:
				winner = players[x]
		if flopBest == winner: #check if the winner of the hand was also on top after the flop
			count += 1
	return count / trials 
			
def main():
	parser = argparse.ArgumentParser(description=calcFlopWins.__doc__)
	parser.add_argument("decks", nargs="?", const=1, type=int)
	parser.add_argument("players", nargs="?", const=2, type=int)
	parser.add_argument("trials", nargs="?", const=1, type=int)
	args = parser.parse_args()
	calcFlopWins(args.decks, args.players, args.trials)
	
if __name__ == "__main__":
	main()