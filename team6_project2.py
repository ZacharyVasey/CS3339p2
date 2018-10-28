##################################################################################
#    Class Simulator
##################################################################################
class Simulator (object):

	# NESTED CLASS
	class Cycle(object):
		def __init__(self):
			ID = 0
			litIns = ''
			regState = [0] * 32
			datState = []

	# DATA
	object.nextCyc = object.Cycle()  # Instance of Cycle, initialized to empty vals.
	object.cycList = []
	object.bin = ''

	def __init__(self, binData):
		'TESTPRINT: THIS IS THE SIMULATOR.  YOU WILL BE SIMULATED.'



	def run(self, binData):
		'TESTPRINT: RUN'
		bin = binData
		# Initialize first entry in cycle list.
		self.cycList.append(self.nextCyc)

		# #TESTPRINT
		# print 'Initial reg state:'
		# for i in self.nextCyc.regState:
		# 	print i

	# # FUNCTION
	# def printCycle(self, cycleRegister):
	# 	'Takes an element in the cycle Register and prints it.'
	# 	print
	# 	print '============================================================='
	# 	print 'Cycle 0' + 'ADD X1, X2, X3'
	# 	print '\nRegisters:'
	# 	print 'r00'
	# 	print '============================================================='








##################################################################################
#    Class BinData
##################################################################################
class BinData(object):
	def __init__(self):
		self.mySring = 'BinData object created'
		# FILE DATA
		self.inFile = ''     # Holds name of input file (via command line).
		self.outFile = ''     # Holds name of output file (via command line).
		self.finalText = ''     # Holds final text to write out to file.
		self.machineCodeFile = ''     # Holds name of string of all binary data from input file.
		self.numLinesText = 0   # Holds the number of lines in binary text file.
		self.PC = 96      # Holds beginning of memory address.
		# MASK DATA
		self.rmMask = 0x1F0000  # Mask to extract Rn register (R1)
		self.rnMask = 0x3E0     # Mask to extract Rd register (R2)
		self.rdMask = 0x1F      # Mask to extract Rm register (R3)
		self.shamMask = 0xFC00  # Mask to extract shamt register.
		self.imm_IM = 0x1FFFE0   # Mask to extract immediate from IM-format instruction.
		self.immI = 0x3FFC00    # Mask to extract immediate from I-format instruction.
		self.addrD = 0x1FF000   # Mask to extract address from D-format instruction.
		self.addrCB = 0xFFFFE0  # Mask to extract address from CB-format instruction.
		self.addrB = 0x3FFFFFF  # Mask to extract address from B-format instruction.
		self.shiftMask = 0x600000   # Mask to extract shift.
		# LIST DATA
		self.machineLines = []  # Holds RAW lines of binary text file, WITHOUT '\n' and '\t'
		self.instrSpaced = []   # Holds formatted lines of binary lines.
		self.opCodeStr = []     # Holds strings of opcodes, empty if data.
		self.isInstr = []       # Holds whether each column is instruction or data.
		self.insType = []       # Holds either: type of instruction (R, I, D, CB, IM, B, BREAK, NOP
		self.data = []          # Holds decimal value for data, empty if instruction.
		self.rmRegNum = []      # Holds register nums for Rm portion, empty if doesn't exist in instruction.
		self.shamNum = []       # Holds register nums for shamt portion, empty if doesn't exist in instruction.
		self.rnRegNum = []      # Holds register nums for Rn portion, empty if doesn't exist in instruction.
		self.rdRtRegNum = []      # Holds register nums for Rd/Rt portion, empty if doesn't exist in instruction.
		self.immNum = []        # Holds immediate value in instruction.
		self.addrNum = []       # Holds numeric address in instruction.
		self.shiftNum = []      # Holds shift in instruction.
		self.memLines = []      # Holds memory address of each line.
##################################################################################
#    Class Dissemble
##################################################################################
class Dissemble(object):
	def __init__(self):
		'TESTPRINT:  this is my dissemble documentation.'
	##################################################################################
	#   openRead:  Opens binary text file and raw loads lines of binary code
	#   into machineCode list.
	##################################################################################
	def openRead(self, binData):     # Opens file and reads binary lines into list.
		with open(binData.inFile) as binData.machineCodeFile:      # 18-20 read in lines WITHOUT tabs.
			binData.machineLines = binData.machineCodeFile.readlines()
		binData.machineLines = [x.strip() for x in binData.machineLines]
		# TESTPRINT
		# print
		# print 'Testing openRead()...' + '\ninFile: ' + binData.inFile
		# print 'machineCode[]: '
		# for item in binData.machineLines:  # Print all raw binary lines in machineLines[].
		# 	print item
		binData.machineCodeFile.close()    # Clean up.
	##################################################################################
	#   processElvBits:  Takes 1st 11 bits of each line.  Tests for
	#   opcode via range.  Populates opcode string list, instruction type list,
	#   and data type list.  If line has no instruction type, then instruction type
	#   list left empty to maintain column integrity - and vice versa.
	##################################################################################
	def processElvBits(self, binData):
		#TESTPRINT
		# print
		# print 'Testing processLinesBin()...'
		# print 'First eleven bits, binary & decimal:'
		k = binData.PC
		for line in binData.machineLines:
			# Count lines
			binData.numLinesText += 1
			# Populate memory.
			binData.memLines.append(k)
			# Get the first bits in bin & dec.
			elvBin = line[0:11]
			elvDec = int(elvBin, 2)
			# TESTPRINT
			# print elvBin + '  -  '  + str(elvDec)
			if (elvDec >= 160 and elvDec <= 191):
				binData.isInstr.append(True)
				binData.opCodeStr.append("B")
				binData.insType.append("B")
				binData.data.append('')
			elif (elvDec == 1104):
				binData.isInstr.append(True)
				binData.opCodeStr.append("AND")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1112):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ADD")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1160 or elvDec == 1161):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ADDI")
				binData.insType.append("I")
				binData.data.append('')
			elif (elvDec == 1360):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ORR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == elvDec >= 1440 and elvDec <= 1447):
				binData.isInstr.append(True)
				binData.opCodeStr.append("CBZ")
				binData.insType.append("CB")
				binData.data.append('')
			elif (elvDec >= 1448 and elvDec <= 1455):
				binData.isInstr.append(True)
				binData.opCodeStr.append("CBNZ")
				binData.insType.append("CB")
				binData.data.append('')
			elif (elvDec == 1624):
				binData.isInstr.append(True)
				binData.opCodeStr.append("SUB")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1872):
				binData.isInstr.append(True)
				binData.opCodeStr.append("EOR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1672 or elvDec == 1673):
				binData.isInstr.append(True)
				binData.opCodeStr.append("SUBI")
				binData.insType.append("I")
				binData.data.append('')
			elif (elvDec >= 1684 and elvDec <= 1687):
				binData.isInstr.append(True)
				binData.opCodeStr.append("MOVZ")
				binData.insType.append("IM")
				binData.data.append('')
			elif (elvDec >= 1940 and elvDec <= 1943):
				binData.isInstr.append(True)
				binData.opCodeStr.append("MOVK")
				binData.insType.append("IM")
				binData.data.append('')
			elif (elvDec == 1690):
				binData.isInstr.append(True)
				binData.opCodeStr.append("LSR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1691):
				binData.isInstr.append(True)
				binData.opCodeStr.append("LSL")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1984):
				binData.isInstr.append(True)
				binData.opCodeStr.append("STUR")
				binData.insType.append("D")
				binData.data.append('')
			elif (elvDec == 1986):
				binData.isInstr.append(True)
				binData.opCodeStr.append("LDUR")
				binData.insType.append("D")
				binData.data.append('')
			elif (elvDec == 2038):
				binData.isInstr.append(True)
				binData.opCodeStr.append("BREAK")
				binData.insType.append("BREAK")
				binData.data.append('')
			# At this point no ops have been found to match ranges.
			elif (True):
				# Checking if entire line == 0 (NOP)
				if (int(line, 2) == 0):
					# print "NOP @ line #" + str(k)
					binData.isInstr.append(True)
					binData.opCodeStr.append("NOP")
					binData.insType.append("NOP")
					binData.data.append('')
				# If line has no matching op, but != 0, then its data.
				else:
					# print "Data @ line #" + str(k)
					binData.isInstr.append(False)
					binData.opCodeStr.append('')
					binData.insType.append("DATA")
					binData.data.append('')
			else:
				print "You shouldn't have come this far."
			k += 4
		# TESTPRINT
		# print 'isInstr[]:  '
		# print binData.isInstr
		# print 'opCodeStr[]:  '
		# print binData.opCodeStr
		# print 'data[]:'
		# print binData.data
		# print 'insType[]: '
		# print binData.insType
		# print 'number of lines in machineLines: ' + str(binData.numLinesText)
		# print 'memory in memLines[]: ' + str(binData.memLines)
	##################################################################################
	#   processRegs:  Uses masks and instruction types to populate the register lists.
	#   Nonexistent registers left empty in their respective list elements.
	##################################################################################
	def processRegs(self, binData):
		# TESTPRINT
		# print
		# print 'Testing processRegs()...'
		k = 0
		for line in binData.machineLines:
			# Grab binary line.
			tempBin = int(line, base=2)
			# Get Rm
			rmNum = ((tempBin & binData.rmMask) >> 16)
			# Get sham
			shamNum = ((tempBin & binData.shamMask) >> 10)
			# Get Rn
			rnNum = ((tempBin & binData.rnMask) >> 5)
			# Get Rd/Rt
			rdRtNum = ((tempBin & binData.rdMask) >> 0)
			# Get Immediate (I-format)
			immI = ((tempBin & binData.immI) >> 10)
			# Get Immediate (IM-format)
			immIM = ((tempBin & binData.imm_IM) >> 5)
			# Get Addr (D-Format)
			adD = ((tempBin & binData.addrD) >> 12)
			# Get Addr (CB-Format)
			adCB = ((tempBin & binData.addrCB) >> 5)
			# Get Addr (B-Format)
			adB = ((tempBin & binData.addrB) >> 0)
			# Get op2
			# Get Shift
			shiftNum = ((tempBin & binData.shiftMask) >> 21)
			# Test for R-Format
			if (binData.insType[k] == 'R'):
				binData.rmRegNum.append(rmNum)
				binData.rnRegNum.append(rnNum)
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				if (shamNum != 0):
					binData.shamNum.append(shamNum)
				else:
					binData.shamNum.append('')
			# Test for I-Format
			elif (binData.insType[k] == "I"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append(rnNum)
				binData.rdRtRegNum.append(rdRtNum)
				# Determine if imm is +/-
				testBit = immI >> 11    # Grab leftmost bit of imm.
				if (testBit == 0):
					binData.immNum.append(int(immI))
				else:
					immI = immI - 1
					immI = immI ^ 0xFFF
					immI = int(immI) * -1
					binData.immNum.append(int(immI))
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for D-Format
			elif (binData.insType[k] == "D"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append(rnNum)
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append('')
				binData.addrNum.append(adD)
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for CB-Format
			elif (binData.insType[k] == "CB"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append('')
				testBit = adCB >> 18
				if (testBit == 0):
					binData.addrNum.append(adCB)
				else:
					adCB = adCB - 1
					adCB = adCB ^ 0b1111111111111111111
					adCB = int(adCB) * -1
					binData.addrNum.append(adCB)
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for IM-Format
			elif (binData.insType[k] == "IM"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append(immIM)
				binData.addrNum.append('')
				# Test for proper quadrant of movk, movz:
				if (shiftNum == 0):
					binData.shiftNum.append(0)
				elif (shiftNum == 1):
					binData.shiftNum.append(16)
				elif (shiftNum == 2):
					binData.shiftNum.append(32)
				else:
					binData.shiftNum.append(48)
				binData.shamNum.append('')
			# Test for B-Format
			elif (binData.insType[k] == "B"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				#TESTPRINT
				# print "   adB: "
				# print bin(adB)
				testBit = adB >> 24
				if (testBit == 0):
					binData.addrNum.append(adB)
				else:
					# TESTPRINT
					# print "   neg adB: " + str(bin(adB))
					adB = adB - 1
					# print "   neg adB - 1: " + str(bin(adB))
					adB = adB ^ 0b11111111111111111111111111
					# print "   neg adB ^ F: " + str(bin(adB))
					adB = int(adB) * -1
					binData.addrNum.append(adB)
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for BREAK
			elif (binData.insType[k] == "BREAK"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for NOP
			elif (binData.insType[k] == "NOP"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for Data
			elif (binData.insType[k] == "DATA"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
				testBin = tempBin >> 31
				# If data is negative.
				if (testBin == 1):
					twoC = (0xFFFFFFFF ^ tempBin) + 1
					dataVal = int(twoC) * -1
					binData.data[k] = dataVal
				# If data is positive...
				else:
					# TESTPRINT
					# print "Positive data at line #" + str(binData.memLines[k])
					binData.data[k] = int(line, 2)
			else:
				print "Error: unknown data type."
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			k += 1
	##################################################################################
	#   getSpacedStr:  Takes 1st 11 bits, formats them, and populates
	#   spaced string list.
	##################################################################################
	def getSpacedStr(self, binData):
		# TESTPRINT
		# print
		# print 'Testing getSpacedStr()...'
		k = 0
		for instr in binData.machineLines:
			# TESTPRINT
			# print instr
			if (binData.isInstr[k] == True):
				temp = "" + instr[0:8]
				temp = temp + " "
				temp = temp + instr[8:11]
				temp = temp + " "
				temp = temp + instr[11:16]
				temp = temp + " "
				temp = temp + instr[16:21]
				temp = temp + " "
				temp = temp + instr[21:26]
				temp = temp + " "
				temp = temp + instr[26:32]
				binData.instrSpaced.append(temp)
			else:
				binData.instrSpaced.append('')
			k += 1
		# TESTPRINT
		# print 'test instrSpaced: ' + str(binData.instrSpaced)
	##################################################################################
	#   printAssem: iterates through the lists and prints assembley code.
	##################################################################################
	def printAssem(self, binData):
		# TESTPRINT
		# print
		# print 'Testing printAssem()...'
		k = 0
		for k in range(k, binData.numLinesText):
			# Pull single line of binary data, spaced.
			line = ''
			if (binData.isInstr[k] == True):
				# Memory address.
				line += binData.instrSpaced[k]
			else:
				line += binData.machineLines[k]
			line = line + '\t' + str(binData.memLines[k])

			# Print R formats
			if (binData.insType[k] == 'R'):
				line = line + '\t' + binData.opCodeStr[k]
				if(binData.shamNum[k] == ''):
					line = line + '\t' + 'R' + str(binData.rdRtRegNum[k]) + ', '
				else:
					line = line + '\t' + 'R' + str(binData.rmRegNum[k]) + ', '
				line = line + ' ' + 'R' + str(binData.rnRegNum[k]) + ','
				# Does this R-format use shift?
				if (binData.shamNum[k] == ''):
					line = line + ' ' + 'R' + str(binData.rmRegNum[k])
				else:
					line = line + ' ' + '#' + str(binData.shamNum[k])
			elif (binData.insType[k] == 'I'):
				line = line + '\t' + binData.opCodeStr[k]
				line = line + '\t' + 'R' + str(binData.rdRtRegNum[k]) + ','
				line += ' R' + str(binData.rnRegNum[k]) + ','
				line += ' #' + str(binData.immNum[k])
			elif (binData.insType[k] == 'D'):
				line += '\t' + binData.opCodeStr[k]
				line += '\t' + 'R' + str(binData.rdRtRegNum[k]) + ','
				line += ' ' + '[R' + str(binData.rnRegNum[k]) +', #'
				line += str(binData.addrNum[k]) + ']'
			elif (binData.insType[k] == "CB"):
				line += '\t' + binData.opCodeStr[k]
				line += '\t' + 'R' + str(binData.rdRtRegNum[k]) + ','
				line += ' ' + '#' + str(binData.addrNum[k])
			elif (binData.insType[k] == "B"):
				line += '\t' + binData.opCodeStr[k]
				line += '\t' + "#" + str(binData.addrNum[k])
			elif (binData.insType[k] == "IM"):
				line += '\t' + binData.opCodeStr[k]
				line += '\t' + "R" + str(binData.rdRtRegNum[k]) +','
				line += ' ' + str(binData.immNum[k]) + ','
				line += ' ' + "LSL " + str(binData.shiftNum[k])
			elif (binData.insType[k] == 'BREAK'):
				line += '\t' + binData.opCodeStr[k]
			elif (binData.insType[k] == 'DATA'):
				line += '\t' + str(binData.data[k])
			elif (binData.insType[k] == "NOP"):
				line += '\t' + str(binData.opCodeStr[k])
			binData.finalText += line + '\n'
			# print line
		print binData.finalText
	##################################################################################
	#   writeOut:  writes final product to text file.
	##################################################################################
	def writeOut(self, binData):
		outFile = open(binData.outFile, 'w')
		outFile.write(binData.finalText)
		outFile.close()
	##################################################################################
	#   run:  processes provided text file.
	##################################################################################
	def run(self, binData):
	# Open inFile & store data to list.
		self.openRead(binData)
		self.processElvBits(binData)
		self.processRegs(binData)
		self.getSpacedStr(binData)
		self.printAssem(binData)
		self.writeOut(binData)
##################################################################################
#   main:  grabs arguments from command line.
##################################################################################
import sys, getopt
def main():
	binData = BinData()
	diss = Dissemble()
	# Get command line data
	# TESTPRINT
	# numCmdArgs = len(sys.argv)  # Store number of cmd args.
	# cmdArgList = str(sys.argv)  # Store list of cmd args.
	# print "Number of command line arguments: %d" % numCmdArgs
	# print "List of command line arguments: %s" % cmdArgList
	# Check command line data
	for i in range(len(sys.argv)):
		if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
			binData.inFile = sys.argv[i+1]
		elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
			binData.outFile = sys.argv[i+1] + '_dis.txt'
	# TESTPRINT
	# print "inFile: " + inFile
	# print "outFile: " + outFile
	# Store command line file names to class instance.
	# TESTPRINT
	# print "In diss instance, iFile is: " + diss.iFile
	# print "In diss instance, oFile is: " + diss.oFile
	diss.run(binData)
	sim = Simulator(binData)
if __name__== "__main__":
	main()