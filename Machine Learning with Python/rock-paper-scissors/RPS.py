from random import choice
def player(prev_play, opponent_history=[]):
	opponent_history.append(prev_play)
	win_move = {"R":"P", "P":"S", "S":"R"}

	#clear previous game history
	if prev_play == '':
		opponent_history = ['']

	
	if len(opponent_history)%5 == 0:
		random = ""
		for move in "RPS":
			if move != prev_play:
				random += move
		guess = choice(move)
	#this beats abbey
	elif len(opponent_history) > 3 and prev_play == opponent_history[-2] and prev_play == opponent_history[-3]:
		guess = prev_play
	#this beats mrugesh & quincy
	elif len(opponent_history) > 1:
		guess = win_move[prev_play]
	else:
		guess = "R"

	return guess