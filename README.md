#Poker

Lets the user input a number of decks D, a number of players P, and a number of trials N. Then it plays N rounds of texas hold-em with P players and D decks. Returns the percentage of those N rounds in which the player with the best cards after the flop ended up winning the round. So specifically, for each round, after the flop it finds the player with the best cards, and sets total += 1 if that player wins the round, and total += 0 if that player doesn't win. Returns count / N.
