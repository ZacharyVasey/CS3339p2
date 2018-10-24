##################################################################################
#    Class Simulator
##################################################################################
class Simulator (object):

	def __init__(self):
		self.cycles = [] # Holds list of cycles, each with state data.  Each CC results in new cycle.
		self.nextCyc = self.Cycle() # Create first instance of cycle (all initialized to 0).
		self.cycles.append(self.nextCyc)

	# NESTED CLASS
	class Cycle(object):
		def __init__(self):
			self.ID = 0
			self.litIns = ''
			self.regState = [0] * 32
			self.datState = []

	def run(self):
		self.printCycle(0)

	# FUNCTION
	def printCycle(self, clockCycle):
		'Takes an element in the cycle Register and prints it.'
		print
		print '======================================================================='
		print 'Cycle ' + str(clockCycle) + ':' + '\t\tADD X1, X2, X3'
		print '\nRegisters:'
		line = ''
		for x in range(0, 8):
			line += str(self.cycles[clockCycle].regState[x]) + '\t\t'
		print 'r00:\t\t' + line
		line = ''
		for x in range(8, 16):
			line += str(self.cycles[clockCycle].regState[x]) + '\t\t'
		print 'r08:\t\t' + line
		line = ''
		for x in range(16, 24):
			line += str(self.cycles[clockCycle].regState[x]) + '\t\t'
		print 'r16:\t\t' + line
		line = ''
		for x in range(24, 32):
			line += str(self.cycles[clockCycle].regState[x]) + '\t\t'
		print 'r24:\t\t' + line
		
		print '\nData:'
		



		print '\n======================================================================='

thisCyc = Simulator()
thisCyc.run()