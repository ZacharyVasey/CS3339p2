##################################################################################
#    Class Simulator
##################################################################################
import copy
class Simulator (object):
	
	def __init__(self, opCodeStr, isInstr, insType, data, rmRegNum, shamNum, rnRegNum, rdRtRegNum, immNum,
	             addrNum, shiftNum, litInstr):
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
	###############################################################################
	#   Class Cycle:  a single cycle, and the register/data states at that time.
	###############################################################################
	# NESTED CLASS
	class Cycle(object):
		def __init__(self):
			self.ID = 0  # TESTPRINT: not sure we need this???
			self.PC = 96    # Assumed starting point.
			self.litIns = ''    # TESTPRINT:  Not sure we need this either???
			self.regState = [0] * 32
			self.datState = []
	###############################################################################
	#   run:  operates the simulator, which processes each instruction, one cycle
	#   at a time.  Makes copy of old cycle[i - 1], modifies that copy, and then
	#   saves it to the list of cycles.
	###############################################################################
	# FUNCTIONS
	def run(self):
		print "\n>>>>>>>>>>> INSIDE SIMULATOR.run(): YOU WILL BE SIMULATED >>>>>>>>>>>>>>>>> "  # TESTPRINT
		
		for x, ins in enumerate(self.insType):
			
			if ins == 'BREAK':
				break
			if x == 0:  # If this is FIRST entry into cycles[]...
				self.nextCyc = self.Cycle() # Create EMPTY cycle.
			else:   # If there is a previous cycle with register states...
				self.nextCyc = copy.deepcopy(self.cycles[x-1])  # Make copy of that, with NEW instance.
				self.nextCyc.PC += 4    # Increment PC to next instruction.
			
			# R-Format Instruction
			if self.opCodeStr[x] == 'ADD':
				self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rnRegNum[x]] + \
				                                            self.nextCyc.regState[self.rmRegNum[x]]
				# self.nextCyc.regState[self.rd] = self.rnRegNum[x] + self.rmRegNum[x]
			elif self.opCodeStr[x] == 'SUB':
				self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rnRegNum[x]] - \
				                                 self.nextCyc.regState[self.rmRegNum[x]]
			# elif self.opCodeStr[x] == 'LSL':
			# 	self.nextCyc.regState[self.rd] = (self.rnRegNum[x] % (1 << 64)) << self.shamNum[x]
			# elif self.opCodeStr[x] == 'LSR':
			# 	self.nextCyc.regState[self.rd] = (self.rnRegNum[x] % (1 << 64)) >> self.shamNum[x]
			# elif self.opCodeStr[x] == 'AND':
			# 	self.nextCyc.regState[self.rd] = self.rnRegNum[x] & self.rmRegNum[x]
			# elif self.opCodeStr[x] == 'ORR':
			# 	self.nextCyc.regState[self.rd] = self.rnRegNum[x] | self.rmRegNum[x]
			# elif self.opCodeStr[x] == 'EOR':
			# 	self.nextCyc.regState[self.rd] = self.rnRegNum[x] ^ self.rmRegNum[x]
			# elif self.opCodeStr[x] == 'ASR':
			# 	self.nextCyc.regState[self.rd] = self.rnRegNum[x]  >> self.shamNum[x]
			# I-Format Instructions
			elif self.opCodeStr[x] == 'ADDI':
				# print 'Cycle ' + str(x + 1) + ':   ' + self.litInstr[x]  # TESTPRINT
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
				self.rnVal = self.nextCyc.regState[self.rn]
				# print 'rnVal: ' + str(self.nextCyc.regState[self.rn])    # TESTPRINT
				# Do the math:  rd = rn + imm
				# There's a lot going on here:  The current cycle (nextCyc) has 32 register files: regState[].
				# We want a specific dest register, IDed by rdRtRegNum[x]:  self.nextCyc.regState[self.rdRtRegNum[x]]
				# One of the operands is currently stored in the register file.  We get that specific src register the
				# same way.  In nextCyc, we need a specific register of the 32, IDed by rnRegNum[].
				# Finally, we have the easy immediate: NOT in a register file, but in immNum[].
				self.nextCyc.regState[self.rd] = self.rnVal + self.immVal
				# TESTPRINT
				# print 'nextCyc.regState[self.rd]: ' + str(self.nextCyc.regState[self.rd])
				pass
			elif self.opCodeStr[x] == 'SUBI':
				self.immVal = self.immNum[x]
				# print 'imm: ' + str(self.immVal)  # TESTPRINT
				self.rd = self.rdRtRegNum[x]
				# print 'rd: ' + str(self.rd)  # TESTPRINT
				# print 'rdVal: ' + str(self.nextCyc.regState[self.rd])  # TESTPRINT
				self.rn = self.rnRegNum[x]
				# print 'rn: ' + str(self.rn)  # TESTPRINT
				self.rnVal = self.nextCyc.regState[self.rn]
				self.nextCyc.regState[self.rd] = self.rnVal - self.immVal
			# # D-Format Instruction
			# elif self.opCodeStr[x] == 'LDUR':
			# 	self.nextCyc.regState[self.rdRtRegNum[x]] = self.rnRegNum[x] + self.addrNum[x]
			# elif self.opCodeStr[x] == 'STUR':
			# 	pass
			# # CB-Format
			# elif self.opCodeStr[x] == 'CBZ':
			# 	if(self.rdRtRegNum[x] == 0):
			# 		self.nextCyc.PC = self.addrNum[x]
			# elif self.opCodeStr[x] == 'CBNZ':
			# 	if (self.rdRtRegNum[x] != 0):
			# 		self.nextCyc.PC = self.addrNum[x]
			# # IM-Format
			# elif self.opCodeStr[x] == 'MOVZ':
			# 	self.nextCyc.regState[self.rdRtRegNum[x]] = self.immNum[x] ** (16 * self.shiftNum[x])
			# elif self.opCodeStr[x] == 'MOVK':
			# 	MASK_BIT_0 = 0xFFFFFFFFFFFF0000
			# 	MASK_BIT_1 = 0xFFFFFFFF0000FFFF
			# 	MASK_BIT_2 = 0xFFFF0000FFFFFFFF
			# 	MASK_BIT_3 = 0x0000FFFFFFFFFFFF
			# 	if(self.shiftNum[x] == 0):
			# 		self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rdRtRegNum[x]] & MASK_BIT_0
			# 	elif(self.shiftNum[x] == 1):
			# 		self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rdRtRegNum[x]] & MASK_BIT_1
			# 	elif (self.shiftNum[x] == 2):
			# 		self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rdRtRegNum[x]] & MASK_BIT_2
			# 	else:
			# 		self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rdRtRegNum[x]] & MASK_BIT_3
			# 	self.nextCyc.regState[self.rdRtRegNum[x]] = self.nextCyc.regState[self.rdRtRegNum[x]] + (2 ** (16 * self.shiftNum[x]))
			#
			# B-Format
			elif self.opCodeStr[x] == 'B':
				self.nextCyc.PC = self.addrNum[x]   #????
			# # Non-Ins-Format
			# elif self.opCodeStr[x] == 'NOP':
			# 	pass
			elif self.opCodeStr[x] == 'DATA':
				print 'Error: you reached DATA in Simulator().run.  You should have reached BREAK first.'
			elif self.opCodeStr[x] == '':
				pass
			else:
				print "You should not be here."
			self.cycles.append(self.nextCyc)    # Slap latest cycle to the list.
			
		# TEST RUN() DOWN HERE
		self.printCycles()
		print ">>>>>>>>>>> EXITING SIMULATOR.run(): YOU HAVE BEEN SIMULATED >>>>>>>>>>>>>>>>> \n\n"  # TESTPRINT
	def printCycle(self, clockCycle):
		'Takes an element in the cycle Register and prints it.'
		print
		print '======================================================================='
		print 'Cycle ' + str(clockCycle + 1) + ':  ' + str(self.cycles[clockCycle].PC) + '\t\t' + self.litInstr[clockCycle]
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

			



