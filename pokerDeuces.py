from __future__ import division
from deuces import Evaluator
from deuces import Deck
import random
import argparse
from itertools import product

def keyMax(d):
	""" 
	Creates a list of the dict's keys and values 
	Returns the key with the max value
	"""  
	v=list(d.values())
	k=list(d.keys())
	return k[v.index(max(v))]

def calcFlopWins(players, trials):
	"""
	Lets the user input a number of a number of players P and a number of trials N. 
	Then it plays N rounds of texas hold-em with P players and 1 deck. 
	Returns the percentage of those N rounds in which the player with the best cards 
	after the flop ended up winning the round. So specifically, for each round, after 
	the flop it finds the player with the best cards, and sets total += 1 if that player wins 
	the round, and total += 0 if that player doesn't win. Returns count / N.
	"""
	evaluator = Evaluator()
	originalTrials = trials
	try:
		count = 0 #number of times player with best cards after the flop wins the hand
		while trials > 0: #play selected number of hands
			deck = Deck() #create deck object
			flopBest = 0 
			winner = 0
			board = []
			hands = {}
			for x in range(1, players + 1): #create hands and add them to dictionary
				hands[x] = deck.draw(2)
			board.extend(deck.draw(3)) #create the flop
			flopScore = {}
			for x in range(1, players + 1): #find the winner after the flop
				flopScore[x] = evaluator.evaluate(board, hands[x])
			flopBest = keyMax(flopScore)
			print("flopBest {}".format(flopBest))
			board.append(deck.draw(1)) #create the turn
			board.append(deck.draw(1)) #create the river
			finalScore = {}
			for x in range(1, players + 1): #find the winner of the hand
				finalScore[x] = evaluator.evaluate(board, hands[x])
			winner = keyMax(finalScore)
			if flopBest == winner: #check if the winner of the hand was also on top after the flop
				count += 1
			print("Winner {}".format(winner))
			print("count {}".format(count))
			trials -= 1
		return count / originalTrials
	except TypeError as e: #catch error from no args present
		print(e)
		pass
	except KeyError as e: #catch lookup table errors
		print(e)
		pass
			
def main():
	parser = argparse.ArgumentParser(description=calcFlopWins.__doc__)
	parser.add_argument("players", nargs="?", const=2, type=int)
	parser.add_argument("trials", nargs="?", const=1, type=int)
	args = parser.parse_args()
	print("count / trials = {}".format(calcFlopWins(args.players, args.trials)))
	
if __name__ == "__main__":
	main()