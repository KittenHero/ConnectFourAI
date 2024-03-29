class DefaultEval:
	def __init__(self, player):
		self.player = player
		if self.player.startswith('r'):
			self.opponent = 'yellow'
		else:
			self.opponent = 'red'
		self.max = 10000
		self.min = - self.max

	def __call__(self, state):
		if state.game_over:
			return (1 - (state.winner != self.player) * 2) * self.max
		return self.default_score(state, state.player(self.player)) - self.default_score(state, state.player(self.opponent))
	
	@staticmethod
	def default_score(state, player):
		consec = [state.count_consec(i, player) for i in range(1, 4)]
		return consec[0] + 10 * consec[1] + 80 * consec[2]
