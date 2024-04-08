from random import choice
def player(prev_play, opponent_history=[]):
	opponent_history.append(prev_play)
	win_move = {"R":"P", "P":"S", "S":"R"}

	#clear previous game history
	if prev_play == '':
		opponent_history = ['']

	#if the opponent has played the same move twice
	if len(opponent_history) > 2 and opponent_history[-2] == prev_play:
		if prev_play == "R":
			guess = "P"
		elif prev_play == "P":
			guess = "S"
		else:
			guess = "R"
	elif len(opponent_history) > 1:
		guess = win_move[prev_play]
	else:
		guess = choice(list(win_move.keys()))

	return guess