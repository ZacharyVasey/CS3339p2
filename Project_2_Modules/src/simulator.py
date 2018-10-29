##################################################################################
#    Class Simulator
##################################################################################
import copy
class Simulator (object):
	
	def __init__(self, opCodeStr, isInstr, insType, data, rmRegNum, shamNum, rnRegNum, rdRtRegNum, immNum,
	             addrNum, shiftNum, litInstr, memLines):
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
	###############################################################################
	#   Class Cycle:  a single cycle, and the register/data states at that time.
	###############################################################################
	# NESTED CLASS
	class Cycle(object):
		def __init__(self):
			self.PC = 96    # Assumed starting point.
			self.regState = [0] * 32
			self.datState = []
	###############################################################################
	###############################################################################
	def testOpCodeStr(self, opStr):
		if opStr == 'ADD':
			pass
		elif opStr == 'SUB':
			pass
		elif opStr == 'LSL':
			pass
		elif opStr == 'LSR':
			pass
		elif opStr == 'AND':
			pass
		elif opStr == 'ORR':
			pass
		elif opStr == 'EOR':
			pass
		elif opStr == 'ADDI':
			pass
		elif opStr == 'SUBI':
			pass
		elif opStr == 'LDUR':
			pass
		elif opStr == 'STUR':
			pass
		elif opStr == 'CBNZ':
			pass
		elif opStr == 'MOVK':
			pass
		elif opStr == 'MOVZ':
			pass
		elif opStr == 'B':
			pass
		elif opStr == 'NOP':
			pass
		elif opStr == 'DATA':
			pass
		elif opStr == 'BREAK':
			pass
		else:
			pass
		
		
	
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
			# print '\tCurrent register value at r10: ' + str(self.nextCyc.regState[10])  # TESTPRINT
			# print '\tIn binary: ' + str(bin(self.nextCyc.regState[10]))     # TESTPRINT
			
			# R-Format Instruction
			if self.opCodeStr[x] == 'ADD':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				# print 'Testing ADD'             #TESTPRINT
				self.rd = self.rdRtRegNum[x]    # Get dest register number.
				# print '\trd:', self.rd          #TESTPRINT
				self.rn = self.rnRegNum[x]      # Get op1 register number.
				# print '\trn:', self.rn          #TESTPRINT
				self.rnVal = self.nextCyc.regState[self.rn]     # Get op1 value.
				# print '\trnVal:', self.rnVal    #TESTPRINT
				self.rm = self.rmRegNum[x]      # Get op2 register number.
				# print '\trm:', self.rm          #TESTPRINT
				self.rmVal = self.nextCyc.regState[self.rm]     # Get op2 value.
				# print '\trmVal:', self.rmVal    #TESTPRINT
				self.rdVal = self.rnVal + self.rmVal  # Get value to save to register.
				# print '\trdVal:', self.rdVal    #TESTPRINT
				self.nextCyc.regState[self.rd] = self.rdVal
			elif self.opCodeStr[x] == 'SUB':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				self.rd = self.rdRtRegNum[x]    # Get dest register number.
				self.rn = self.rnRegNum[x]      # Get op1 register number.
				self.rnVal = self.nextCyc.regState[self.rn]     # Get op1 value.
				self.rm = self.rmRegNum[x]      # Get op2 register number.
				self.rmVal = self.nextCyc.regState[self.rm]     # Get op2 value.
				self.rdVal = self.rnVal - self.rmVal  # Get value to save to register.
				self.nextCyc.regState[self.rd] = self.rdVal
			elif self.opCodeStr[x] == 'LSL':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				# print 'Testing LSL...'          #TESTPRINT
				self.rd = self.rdRtRegNum[x]    # Get dest register number.
				# print '\trd:', self.rd          #TESTPRINT
				self.rn = self.rnRegNum[x]      # Get src register number.
				# print '\trn:', self.rn          #TESTPRINT
				self.rnVal = self.nextCyc.regState[self.rn]      # Get src value.
				# print '\trnVal:', self.rnVal    #TESTPRINT
				self.shiftVal = self.shamNum[x]     # Get shift amount.
				# print '\tshiftVal:', self.shiftVal  #TESTPRINT
				self.rdVal = self.rnVal << self.shiftVal
				# print '\trdVal:', self.rdVal        #TESTPRINT
				self.nextCyc.regState[self.rd] = self.rdVal
			elif self.opCodeStr[x] == 'LSR':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				self.rd = self.rdRtRegNum[x]    # Get dest register number.
				self.rn = self.rnRegNum[x]      # Get src register number.
				self.rnVal = self.nextCyc.regState[self.rn]      # Get src value.
				self.shiftVal = self.shamNum[x]     # Get shift amount.
				self.rdVal = self.rnVal >> self.shiftVal
				self.nextCyc.regState[self.rd] = self.rdVal
			elif self.opCodeStr[x] == 'AND':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
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
				self.nextCyc.regState[self.rd] = self.thisNum
			elif self.opCodeStr[x] == 'ORR':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				self.rd = self.rdRtRegNum[x]
				self.rdVal = self.nextCyc.regState[self.rd]
				self.rn = self.rnRegNum[x]
				self.rnVal = self.nextCyc.regState[self.rn]
				self.rm = self.rmRegNum[x]
				self.rmVal = self.nextCyc.regState[self.rm]
				self.thisNum = self.rmVal | self.rnVal
				self.nextCyc.regState[self.rd] = self.thisNum
			elif self.opCodeStr[x] == 'EOR':
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				self.rd = self.rdRtRegNum[x]
				self.rdVal = self.nextCyc.regState[self.rd]
				self.rn = self.rnRegNum[x]
				self.rnVal = self.nextCyc.regState[self.rn]
				self.rm = self.rmRegNum[x]
				self.rmVal = self.nextCyc.regState[self.rm]
				self.thisNum = self.rmVal ^ self.rnVal
				self.nextCyc.regState[self.rd] = self.thisNum
			elif self.opCodeStr[x] == 'ASR':  ##############################################################
				pass
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
				self.nextCyc.PC += 4  # Increment PC to next instruction.
				self.immVal = self.immNum[x]
				# print 'imm: ' + str(self.immVal)  # TESTPRINT
				self.rd = self.rdRtRegNum[x]
				# print 'rd: ' + str(self.rd)  # TESTPRINT
				# print 'rdVal: ' + str(self.nextCyc.regState[self.rd])  # TESTPRINT
				self.rn = self.rnRegNum[x]
				# print 'rn: ' + str(self.rn)  # TESTPRINT
				self.rnVal = self.nextCyc.regState[self.rn]
				self.nextCyc.regState[self.rd] = self.rnVal - self.immVal
			# D-Format Instruction
			elif self.opCodeStr[x] == 'LDUR':   ##############################################################
				pass
			elif self.opCodeStr[x] == 'STUR':   ##############################################################
				pass
			# CB-Format
			elif self.opCodeStr[x] == 'CBZ':
				pass
				
			elif self.opCodeStr[x] == 'CBNZ':
				print 'Testing CBNZ...'
				print '\tpc:', self.nextCyc.PC
				rd = self.rdRtRegNum[x]
				print '\trd:', rd
				self.rdVal = self.nextCyc.regState[self.rd]
				print '\trdVal:', self.rdVal
				addr = self.addrNum[x]
				print '\taddr:', addr
				addr *= 4
				print '\taddr *= 4:', addr

			# IM-Format
			elif self.opCodeStr[x] == 'MOVZ':   ##############################################################
				pass
			elif self.opCodeStr[x] == 'MOVK':   ##############################################################
				pass
			# B-Format
			elif self.opCodeStr[x] == 'B':      ##############################################################
				pass
			# MISC
			elif self.opCodeStr[x] == 'NOP':
				pass
			elif self.opCodeStr[x] == 'DATA':   ##############################################################
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

			



