from random import choice
def player(prev_play, opponent_history=[]):
	opponent_history.append(prev_play)
	win_move = {"R":"P", "P":"S", "S":"R"}

	#clear previous game history
	if prev_play == '':
		opponent_history = ['']

	#this beats mrugesh & quincy
	if len(opponent_history) > 1:
		guess = win_move[prev_play]
	else:
		guess = "P"

	return guess