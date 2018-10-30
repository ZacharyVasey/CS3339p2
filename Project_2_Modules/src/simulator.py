##################################################################################
#    Class Simulator
##################################################################################
import copy
class Simulator (object):
	
	def __init__(self, opCodeStr, isInstr, insType, data, rmRegNum, shamNum, rnRegNum, rdRtRegNum, immNum,
	             addrNum, shiftNum, litInstr, memLines, numLinesText):
		# Set up cycle sequence list.
		self.cycles = [] # Holds list of cycles, each with state data.  Each CC results in new cycle.
		# Set up BinData column copies.
		self.opCodeStr = opCodeStr
		self.isInstr = isInstr
		self.insType = insType
		self.data = data
		self.rmRegNum = rmRegNum
		self.shamNum = shamNum
		self.rnRegNum = rnRegNum
		self.rdRtRegNum = rdRtRegNum
		self.immNum = immNum
		self.addrNum = addrNum
		self.shiftNum = shiftNum
		self.litInstr = litInstr
		self.memLines = memLines
		self.numLinesText = numLinesText
	###############################################################################
	#   Class Cycle:  a single cycle, and the register/data states at that time.
	###############################################################################
	# NESTED CLASS
	class Cycle(object):
		def __init__(self):
			self.PC = 0
			self.regState = [0] * 32
			self.datState = []
	###############################################################################
	###############################################################################
	def doADD(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print '\tInside doADD - memLines[x]:', self.memLines[x]     # TESTPRINT
		# print 'Testing ADD'             #TESTPRINT
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		# print '\trd:', self.rd          #TESTPRINT
		self.rn = self.rnRegNum[x]  # Get op1 register number.
		# print '\trn:', self.rn          #TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]  # Get op1 value.
		# print '\trnVal:', self.rnVal    #TESTPRINT
		self.rm = self.rmRegNum[x]  # Get op2 register number.
		# print '\trm:', self.rm          #TESTPRINT
		self.rmVal = self.nextCyc.regState[self.rm]  # Get op2 value.
		# print '\trmVal:', self.rmVal    #TESTPRINT
		self.rdVal = self.rnVal + self.rmVal  # Get value to save to register.
		# print '\trdVal:', self.rdVal    #TESTPRINT
		nc.regState[self.rd] = self.rdVal
	###############################################################################
	###############################################################################
	def doSUB(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		self.rn = self.rnRegNum[x]  # Get op1 register number.
		self.rnVal = self.nextCyc.regState[self.rn]  # Get op1 value.
		self.rm = self.rmRegNum[x]  # Get op2 register number.
		self.rmVal = self.nextCyc.regState[self.rm]  # Get op2 value.
		self.rdVal = self.rnVal - self.rmVal  # Get value to save to register.
		nc.regState[self.rd] = self.rdVal
	###############################################################################
	###############################################################################
	def doLSL(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print 'Testing LSL...'          #TESTPRINT
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		# print '\trd:', self.rd          #TESTPRINT
		self.rn = self.rnRegNum[x]  # Get src register number.
		# print '\trn:', self.rn          #TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]  # Get src value.
		# print '\trnVal:', self.rnVal    #TESTPRINT
		self.shiftVal = self.shamNum[x]  # Get shift amount.
		# print '\tshiftVal:', self.shiftVal  #TESTPRINT
		self.rdVal = self.rnVal << self.shiftVal
		# print '\trdVal:', self.rdVal        #TESTPRINT
		nc.regState[self.rd] = self.rdVal
	###############################################################################
	###############################################################################
	def doLSR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		self.rn = self.rnRegNum[x]  # Get src register number.
		self.rnVal = self.nextCyc.regState[self.rn]  # Get src value.
		self.shiftVal = self.shamNum[x]  # Get shift amount.
		self.rdVal = self.rnVal >> self.shiftVal
		nc.regState[self.rd] = self.rdVal
	###############################################################################
	###############################################################################
	def doAND(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print 'Testing AND...'              # TESTPRINT
		self.rd = self.rdRtRegNum[x]
		self.rdVal = self.nextCyc.regState[self.rd]
		# print '\trd:', self.rd              # TESTPRINT
		# print '\trdVal:', self.rdVal        # TESTPRINT
		self.rn = self.rnRegNum[x]
		# print '\trn:', self.rn              # TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]
		# print '\trnVal:', bin(self.rnVal)   # TESTPRINT
		self.rm = self.rmRegNum[x]
		# print '\trm:', self.rm              # TESTPRINT
		self.rmVal = self.nextCyc.regState[self.rm]
		# print '\trmVal:', bin(self.rmVal)        # TESTPRINT
		self.thisNum = self.rmVal & self.rnVal
		# print '\trdVal:', self.thisNum      # TESTPRINT
		nc.regState[self.rd] = self.thisNum
	###############################################################################
	###############################################################################
	def doORR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]
		self.rdVal = self.nextCyc.regState[self.rd]
		self.rn = self.rnRegNum[x]
		self.rnVal = self.nextCyc.regState[self.rn]
		self.rm = self.rmRegNum[x]
		self.rmVal = self.nextCyc.regState[self.rm]
		self.thisNum = self.rmVal | self.rnVal
		nc.regState[self.rd] = self.thisNum
	###############################################################################
	###############################################################################
	def doEOR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]
		self.rdVal = self.nextCyc.regState[self.rd]
		self.rn = self.rnRegNum[x]
		self.rnVal = self.nextCyc.regState[self.rn]
		self.rm = self.rmRegNum[x]
		self.rmVal = self.nextCyc.regState[self.rm]
		self.thisNum = self.rmVal ^ self.rnVal
		nc.regState[self.rd] = self.thisNum
	###############################################################################
	###############################################################################
	def doASR(self, nc, x):
		pass
	###############################################################################
	###############################################################################
	def doADDI(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print 'Cycle ' + str(x + 1) + ':   ' + self.litInstr[x]  # TESTPRINT
		# print '\tInside doADD...'       # TESTPRINT
		# print '\t\tmemLines[x]:', self.memLines[x]  # TESTPRINT
		# Get immediate value.
		self.immVal = self.immNum[x]
		# print 'imm: ' + str(self.immVal)  # TESTPRINT
		# Get dest register number and value.
		self.rd = self.rdRtRegNum[x]
		# print 'rd: ' + str(self.rd)  # TESTPRINT
		# print 'rdVal: ' + str(self.nextCyc.regState[self.rd])  # TESTPRINT
		# Get src register value.
		self.rn = self.rnRegNum[x]
		# print 'rn: ' + str(self.rn)  # TESTPRINT
		self.rnVal = nc.regState[self.rn]
		# print 'rnVal: ' + str(self.nextCyc.regState[self.rn])    # TESTPRINT
		# Do the math:  rd = rn + imm
		# There's a lot going on here:  The current cycle (nextCyc) has 32 register files: regState[].
		# We want a specific dest register, IDed by rdRtRegNum[x]:  self.nextCyc.regState[self.rdRtRegNum[x]]
		# One of the operands is currently stored in the register file.  We get that specific src register the
		# same way.  In nextCyc, we need a specific register of the 32, IDed by rnRegNum[].
		# Finally, we have the easy immediate: NOT in a register file, but in immNum[].
		nc.regState[self.rd] = self.rnVal + self.immVal
		# print '\t\tnc.PC:', nc.PC   # TESTPRINT
		# print '\t\tself.nextCyc.PC:', self.nextCyc.PC       # TESTPRINT
	###############################################################################
	###############################################################################
	def doSUBI(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.immVal = self.immNum[x]
		# print 'imm: ' + str(self.immVal)  # TESTPRINT
		self.rd = self.rdRtRegNum[x]
		# print 'rd: ' + str(self.rd)  # TESTPRINT
		# print 'rdVal: ' + str(self.nextCyc.regState[self.rd])  # TESTPRINT
		self.rn = self.rnRegNum[x]
		# print 'rn: ' + str(self.rn)  # TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]
		nc.regState[self.rd] = self.rnVal - self.immVal
	###############################################################################
	###############################################################################
	def doCBNZ(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		rd = self.rdRtRegNum[x]
		rdVal = nc.regState[rd]
		addr = self.addrNum[x]
		# print 'Testing CBNZ...'
		# print '\tpc:', nc.PC
		# print '\trd:', rd
		# print '\trdVal:', self.rdVal
		# print '\taddr:', addr
		# addr *= 4
		# print '\taddr *= 4:', addr
		if rdVal != 0:      # If test value != 0, return the offset to adjust the instruction index.
			return addr
		else:
			return 0
	# ###############################################################################
	###############################################################################
	def doNOP(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
	# TESTPRINT
	# print 'nextCyc.regState[self.rd]: ' + str(self.nextCyc.regState[self.rd])
	###############################################################################
	###############################################################################
	# def procIns(self, nc, ops, x):
	# 	# ######################################### R
	# 	if ops == 'ADD':
	# 		self.doADD(nc, x)
	# 	elif ops == 'SUB':
	# 		self.doSUB(nc, x)
	# 	elif ops == 'LSL':
	# 		self.doLSL(nc, x)
	# 	elif ops == 'LSR':
	# 		self.doLSR(nc, x)
	# 	elif ops == 'AND':
	# 		self.doAND(nc, x)
	# 	elif ops == 'ORR':
	# 		self.doORR(nc, x)
	# 	elif ops == 'EOR':
	# 		self.doEOR(nc, x)
	# 	elif ops == 'ASR':
	# 		pass
	# 	######################################### I
	# 	elif ops == 'ADDI':
	# 		self.doADDI(nc, x)
	# 		# self.doADDI(self.nextCyc, x)
	# 	elif ops == 'SUBI':
	# 		self.doSUBI(nc, x)
	# 	######################################### D
	# 	elif ops == 'LDUR':
	# 		pass
	# 	elif ops == 'STUR':
	# 		pass
	# 	######################################### CB
	# 	elif ops == 'CBZ':
	# 		pass
	# 	elif ops == 'CBNZ':
	# 		rd = self.rdRtRegNum[x]
	# 		rdVal = nc.regState[rd]
	# 		addr = self.addrNum[x]
	# 		# print 'Inside CBNZ...'
	# 		# print '\trd:', rd
	# 		# print '\trdVal:', rdVal
	# 		# print '\taddr:', addr
	#
	# 	######################################### IM
	# 	elif ops == 'MOVZ':
	# 		pass
	# 	elif ops == 'MOVK':
	# 		pass
	# 	######################################### B
	# 	elif ops == 'B':
	# 		pass
	# 	elif ops == 'NOP':
	# 		self.doNOP(nc, x)
	
			
	###############################################################################
	#   run:  operates the simulator, which processes each instruction, one cycle
	#   at a time.  Makes copy of old cycle[i - 1], modifies that copy, and then
	#   saves it to the list of cycles.
	###############################################################################
	# FUNCTIONS
	def run(self):
		print "\n>>>>>>>>>>> INSIDE SIMULATOR.run(): YOU WILL BE SIMULATED >>>>>>>>>>>>>>>>> "  # TESTPRINT
		self.nextCyc = self.Cycle()     # Create first EMPTY cycle (empty regState[]).  Not appended to cycles[].
		
		
		self.x = 0
		while (self.x < self.numLinesText):
			print 'In while loop...', self.x, ' ... ', self.litInstr[self.x], ' ... ', self.memLines[self.x]
			self.nextCyc = copy.deepcopy(self.nextCyc)
			if self.opCodeStr[self.x] == 'ADDI':
				self.doADDI(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'SUBI':
				self.doSUBI(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'NOP':
				self.doNOP(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'CBNZ':
				y = self.doCBNZ(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
				print 'Inside CBNZ...'
				print '\ty:', y
				print '\ty += x:', y + self.x
				if y != 0:
					self.x += y
					continue
					
			self.x += 1
			
			print 'Testing cycles:'
			for cyc in self.cycles:
				print cyc.PC
			
			
		
		
		
		
		
		
		
		
		
		# self.x = 0      #  Start instruction index at 0.
		# while (self.x < self.numLinesText):     # Shouldn't reach end of file, but worst case scenario.
		# 	print 'Testing while loop...', self.x, ' ... ', self.opCodeStr[self.x]    # TESTPRINT
		# 	self.nextCyc = copy.deepcopy(self.nextCyc)  # Make copy of that, with NEW instance.
		# 	print 'Testing current cyc:'
		#
		# 	if self.insType[self.x] == 'BREAK':
		# 		break
		# 	# ######################################### R
		# 	elif self.opCodeStr[self.x] in ['ADD', 'SUB', 'LSL', 'LSR', 'AND', 'ORR', 'EOR', 'ASR']:
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 	######################################### I
		# 	elif self.opCodeStr[self.x] in ['ADDI', 'SUBI']:
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 	######################################### D
		# 	elif self.opCodeStr[self.x] in ['LDUR', 'STUR']:
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 	######################################### CB
		# 	elif self.opCodeStr[self.x] in ['CBZ', 'CBNZ']:
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 		print 'Inside run()... testing CBNZ'
		# 		rd = self.rdRtRegNum[self.x]
		# 		rdVal = self.nextCyc.regState[rd]
		# 		ofs = self.addrNum[self.x]
		# 		y = self.x
		# 		print '\trd:', rd
		# 		print '\trdVal:', rdVal
		# 		print '\ty = x:', y
		# 		print '\toffset:', ofs
		# 		y += ofs
		# 		print '\ty += ofs:', y
		# 		# if rdVal != 0:
		# 		# 	x += ofs
		# 		if rdVal != 0:
		# 			self.x = y
		# 			self.cycles.append(self.nextCyc)
		# 			break
		#
		# 	######################################### IM
		# 	elif self.opCodeStr[self.x] in ['MOVZ','MOVK']:
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 	######################################### B
		# 	elif self.opCodeStr[self.x] == 'B':
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 	######################################### MISC
		# 	elif self.opCodeStr[self.x] == 'NOP':
		# 		self.procIns(self.nextCyc, self.opCodeStr[self.x], self.x)
		# 	elif self.opCodeStr[self.x] == 'DATA':
		# 		print 'Error: you reached DATA in Simulator().run.  You should have reached BREAK first.'
		# 	elif self.opCodeStr[self.x] == '':
		# 		pass
		# 	else:
		# 		print "You should not be here."
		# 	self.cycles.append(self.nextCyc)    # Slap latest cycle to the list.
		# 	self.x += 1






			
		# TEST RUN() DOWN HERE
		self.printCycles()
		print ">>>>>>>>>>> EXITING SIMULATOR.run(): YOU HAVE BEEN SIMULATED >>>>>>>>>>>>>>>>> \n" # TESPRINT
	def printCycle(self, clockCycle):
		'Takes an element in the cycle Register and prints it.'
		print
		print '======================================================================='
		print 'Cycle ' + str(clockCycle + 1) + ':  ' + str(self.cycles[clockCycle].PC) + self.opCodeStr[clockCycle-1]
		print '\nRegisters:'
		z = 0
		for x in range(0, 4):   # Prints all registers 4 rows x 8 columns
			line = 'r' + str(z).zfill(2) + ':\t'
			for y in range (0, 8):
				line += str(self.cycles[clockCycle].regState[y + z]) + '\t'
			print line
			z += 8
		print '\nData:'

	def printCycles(self):
		for x, cycle in enumerate(self.cycles):
			self.printCycle(x)
			

			



