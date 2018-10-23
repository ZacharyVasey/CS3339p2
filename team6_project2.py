##################################################################################
#   Global Variables
##################################################################################
# TESTPRINT
print
print '**************************************************************'
testVar = 0
# FILE DATA
print 'HELLO ANNE'
oFile = '' # File Object
iFile = '' # File Object
outFile = ''  # OutFile name
inFile = ''  # Infile Name
inFileName = ''
outFileName = ''
finalText = ''  # Holds final text to write out to file.
machineCodeFile = ''  # Holds name of string of all binary data from input file.
numLinesText = 0  # Holds the number of lines in binary text file.
startMem = 96  # Holds beginning of memory address.
# LISTS
machineLines = []  # Holds RAW lines of binary text file, WITHOUT '\n' and '\t'
instrSpaced = []  # Holds formatted lines of binary lines.
opCodeStr = []  # Holds strings of opcodes, empty if data.
isInstr = []  # Holds whether each column is instruction or data.
insType = []  # Holds either: type of instruction (R, I, D, CB, IM, B, BREAK, NOP
data = []  # Holds decimal value for data, empty if instruction.
rmRegNum = []  # Holds register nums for Rm portion, empty if doesn't exist in instruction.
shamNum = []  # Holds register nums for shamt portion, empty if doesn't exist in instruction.
rnRegNum = []  # Holds register nums for Rn portion, empty if doesn't exist in instruction.
rdRtRegNum = []  # Holds register nums for Rd/Rt portion, empty if doesn't exist in instruction.
immNum = []  # Holds immediate value in instruction.
addrNum = []  # Holds numeric address in instruction.
shiftNum = []  # Holds shift in instruction.
memLines = []  # Holds memory address of each line.
# MASKS
rmMask = 0x1F0000  # Mask to extract Rn register (R1)
rnMask = 0x3E0  # Mask to extract Rd register (R2)
rdMask = 0x1F  # Mask to extract Rm register (R3)
shamMask = 0xFC00  # Mask to extract shamt register.0
immI = 0x3FFC00  # Mask to extract immediate from I-format instruction.
immIM = 0x1FFFE0  # Mask to extract immediate from IM-format instruction.
addrD = 0x1FF000  # Mask to extract address from D-format instruction.
addrCB = 0xFFFFE0  # Mask to extract address from CB-format instruction.
addrB = 0x3FFFFFF  # Mask to extract address from B-format instruction.
shiftMask = 0x600000  # Mask to extract shift.

##################################################################################
#   Dissemble Class
#       Contains an instance of a text input of binary code, with each row in the
#       lists being an iteration of an instruction.  opt2 was not included in
#       instruction lists, for now.
##################################################################################
class Dissemble(object):
    def __init__(self):
        #TESTPRINT
        global testVar
        global inFileName
        global outFileName
        global iFile  # Holds name of input file (via command line).
        global oFile  # Holds name of output file (via command line).
        global finalText  # Holds final text to write out to file.
        global machineCodeFile  # Holds name of string of all binary data from input file.
        global numLinesText  # Holds the number of lines in binary text file.
        global startMem  # Holds beginning of memory address.
        # LISTS
        global machineLines  # Holds RAW lines of binary text file, WITHOUT '\n' and '\t'
        global instrSpaced  # Holds formatted lines of binary lines.
        global opCodeStr  # Holds strings of opcodes, empty if data.
        global isInstr  # Holds whether each column is instruction or data.
        global insType  # Holds either: type of instruction (R, I, D, CB, IM, B, BREAK, NOP
        global data  # Holds decimal value for data, empty if instruction.
        global rmRegNum  # Holds register nums for Rm portion, empty if doesn't exist in instruction.
        global shamNum  # Holds register nums for shamt portion, empty if doesn't exist in instruction.
        global rnRegNum  # Holds register nums for Rn portion, empty if doesn't exist in instruction.
        global rdRtRegNum  # Holds register nums for Rd/Rt portion, empty if doesn't exist in instruction.
        global immNum  # Holds immediate value in instruction.
        global addrNum  # Holds numeric address in instruction.
        global shiftNum  # Holds shift in instruction.
        global memLines  # Holds memory address of each line.
        # MASKS
        global rmMask  # Mask to extract Rn register (R1)
        global rnMask  # Mask to extract Rd register (R2)
        global rdMask  # Mask to extract Rm register (R3)
        global shamMask  # Mask to extract shamt register.0
        global immI  # Mask to extract immediate from I-format instruction.
        global immIM  # Mask to extract immediate from IM-format instruction.
        global addrD  # Mask to extract address from D-format instruction.
        global addrCB  # Mask to extract address from CB-format instruction.
        global addrB  # Mask to extract address from B-format instruction.
        global shiftMask  # Mask to extract shift.

    ##################################################################################
    #   openRead:  Opens binary text file and raw loads lines of binary code
    #   into machineCode list.
    ##################################################################################
    def openRead(self):  # Opens file and reads binary lines into list.
        with open(inFile) as machineCodeFile:  # Read in lines WITHOUT tabs.
            machineLines = machineCodeFile.readlines()
        machineLines = [x.strip() for x in machineLines]
        # TESTPRINT
        # print
        # print 'Testing openRead()...' + '\ninFile: ' + inFile
        # print 'machineLines[]: '
        # for item in machineLines:  # Print all raw binary lines in machineLines[].
        #     print item
        machineCodeFile.close()  # Clean up.

    ##################################################################################
    #   processElvBits:  Takes 1st 11 bits of each line.  Tests for
    #   opcode via range.  Populates opcode string list, instruction type list,
    #   and data type list.  If line has no instruction type, then instruction type
    #   list left empty to maintain column integrity - and vice versa.
    ##################################################################################
    def processElvBits(self):
        global numLinesText
        global startMem
        global machineLines
        global memLines
        global elvBin
        global elvDec

        # TESTPRINT
        print
        print 'Testing processLinesBin()...'
        print 'numLinesText: ' + str(numLinesText)
        print 'First eleven bits, binary & decimal:'
        k = startMem
        for line in machineLines:
            # Count lines
            numLinesText += 1
            # Populate memory.
            memLines.append(k)
            # Get the first bits in bin & dec.
            elvBin = line[0:11]
            elvDec = int(elvBin, 2)
            print '\tElvDec: ' + str(selfDec)
            # TESTPRINT
            # print elvBin + '  -  '  + str(elvDec)
            if (elvDec >= 160 and elvDec <= 191):
                isInstr.append(True)
                opCodeStr.append("B")
                insType.append("B")
                data.append('')
            elif (elvDec == 1104):
                isInstr.append(True)
                opCodeStr.append("AND")
                insType.append("R")
                data.append('')
            elif (elvDec == 1112):
                isInstr.append(True)
                opCodeStr.append("ADD")
                insType.append("R")
                data.append('')
            elif (elvDec == 1160 or elvDec == 1161):
                isInstr.append(True)
                opCodeStr.append("ADDI")
                insType.append("I")
                data.append('')
            elif (elvDec == 1360):
                isInstr.append(True)
                opCodeStr.append("ORR")
                insType.append("R")
                data.append('')
            elif (elvDec == elvDec >= 1440 and elvDec <= 1447):
                isInstr.append(True)
                opCodeStr.append("CBZ")
                insType.append("CB")
                data.append('')
            elif (elvDec >= 1448 and elvDec <= 1455):
                isInstr.append(True)
                opCodeStr.append("CBNZ")
                insType.append("CB")
                data.append('')
            elif (elvDec == 1624):
                isInstr.append(True)
                opCodeStr.append("SUB")
                insType.append("R")
                data.append('')
            elif (elvDec == 1872):
                isInstr.append(True)
                opCodeStr.append("EOR")
                insType.append("R")
                data.append('')
            elif (elvDec == 1672 or elvDec == 1673):
                isInstr.append(True)
                opCodeStr.append("SUBI")
                insType.append("I")
                data.append('')
            elif (elvDec >= 1684 and elvDec <= 1687):
                isInstr.append(True)
                opCodeStr.append("MOVZ")
                insType.append("IM")
                data.append('')
            elif (elvDec >= 1940 and elvDec <= 1943):
                isInstr.append(True)
                opCodeStr.append("MOVK")
                insType.append("IM")
                data.append('')
            elif (elvDec == 1690):
                isInstr.append(True)
                opCodeStr.append("LSR")
                insType.append("R")
                data.append('')
            elif (elvDec == 1691):
                isInstr.append(True)
                opCodeStr.append("LSL")
                insType.append("R")
                data.append('')
            elif (elvDec == 1984):
                isInstr.append(True)
                opCodeStr.append("STUR")
                insType.append("D")
                data.append('')
            elif (elvDec == 1986):
                isInstr.append(True)
                opCodeStr.append("LDUR")
                insType.append("D")
                data.append('')
            elif (elvDec == 2038):
                isInstr.append(True)
                opCodeStr.append("BREAK")
                insType.append("BREAK")
                data.append('')
            # At this point no ops have been found to match ranges.
            elif (True):
                # Checking if entire line == 0 (NOP)
                if (int(line, 2) == 0):
                    # print "NOP @ line #" + str(k)
                    isInstr.append(True)
                    opCodeStr.append("NOP")
                    insType.append("NOP")
                    data.append('')
                # If line has no matching op, but != 0, then its data.
                else:
                    # print "Data @ line #" + str(k)
                    isInstr.append(False)
                    opCodeStr.append('')
                    insType.append("DATA")
                    data.append('')
            else:
                print "You shouldn't have come this far."
            k += 4

            # TESTPRINT
            print 'isInstr[]:  '
            print isInstr
            print 'opCodeStr[]:  '
            print opCodeStr
            print 'data[]:'
            print data
            print 'insType[]: '
            print insType
            print 'number of lines in machineLines: ' + str(numLinesText)
            print 'memory in memLines[]: ' + str(memLines)
    ##################################################################################
    #   processRegs:  Uses masks and instruction types to populate the register lists.
    #   Nonexistent registers left empty in their respective list elements.
    ##################################################################################
    def processRegs(self):
        # TESTPRINT
        # print
        # print 'Testing processRegs()...'
        k = 0
        for line in machineLines:
            # Grab binary line.
            tempBin = int(line, base=2)
            # Get Rm
            rmNum = ((tempBin & rmMask) >> 16)
            # Get sham
            shamNum = ((tempBin & shamMask) >> 10)
            # Get Rn
            rnNum = ((tempBin & rnMask) >> 5)
            # Get Rd/Rt
            rdRtNum = ((tempBin & rdMask) >> 0)
            # Get Immediate (I-format)
            immI = ((tempBin & immI) >> 10)
            # Get Immediate (IM-format)
            immIM = ((tempBin & immIM) >> 5)
            # Get Addr (D-Format)
            adD = ((tempBin & addrD) >> 12)
            # Get Addr (CB-Format)
            adCB = ((tempBin & addrCB) >> 5)
            # Get Addr (B-Format)
            adB = ((tempBin & addrB) >> 0)
            # Get op2
            # Get Shift
            shiftNum = ((tempBin & shiftMask) >> 21)
            # Test for R-Format
            if (insType[k] == 'R'):
                rmRegNum.append(rmNum)
                rnRegNum.append(rnNum)
                rdRtRegNum.append(rdRtNum)
                immNum.append('')
                addrNum.append('')
                shiftNum.append('')
                if (shamNum != 0):
                    shamNum.append(shamNum)
                else:
                    shamNum.append('')
            # Test for I-Format
            elif (insType[k] == "I"):
                rmRegNum.append('')
                rnRegNum.append(rnNum)
                rdRtRegNum.append(rdRtNum)
                # Determine if imm is +/-
                testBit = immI >> 11  # Grab leftmost bit of imm.
                if (testBit == 0):
                    immNum.append(int(immI))
                else:
                    immI = immI - 1
                    immI = immI ^ 0xFFF
                    immI = int(immI) * -1
                    immNum.append(int(immI))
                addrNum.append('')
                shiftNum.append('')
                shamNum.append('')
            # Test for D-Format
            elif (insType[k] == "D"):
                rmRegNum.append('')
                rnRegNum.append(rnNum)
                rdRtRegNum.append(rdRtNum)
                immNum.append('')
                addrNum.append(adD)
                shiftNum.append('')
                shamNum.append('')
            # Test for CB-Format
            elif (insType[k] == "CB"):
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append(rdRtNum)
                immNum.append('')
                testBit = adCB >> 18
                if (testBit == 0):
                    addrNum.append(adCB)
                else:
                    adCB = adCB - 1
                    adCB = adCB ^ 0b1111111111111111111
                    adCB = int(adCB) * -1
                    addrNum.append(adCB)
                shiftNum.append('')
                shamNum.append('')
            # Test for IM-Format
            elif (insType[k] == "IM"):
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append(rdRtNum)
                immNum.append(immIM)
                addrNum.append('')
                # Test for proper quadrant of movk, movz:
                if (shiftNum == 0):
                    shiftNum.append(0)
                elif (shiftNum == 1):
                    shiftNum.append(16)
                elif (shiftNum == 2):
                    shiftNum.append(32)
                else:
                    shiftNum.append(48)
                shamNum.append('')
            # Test for B-Format
            elif (insType[k] == "B"):
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append('')
                immNum.append('')
                # TESTPRINT
                # print "   adB: "
                # print bin(adB)
                testBit = adB >> 24
                if (testBit == 0):
                    addrNum.append(adB)
                else:
                    # TESTPRINT
                    # print "   neg adB: " + str(bin(adB))
                    adB = adB - 1
                    # print "   neg adB - 1: " + str(bin(adB))
                    adB = adB ^ 0b11111111111111111111111111
                    # print "   neg adB ^ F: " + str(bin(adB))
                    adB = int(adB) * -1
                    addrNum.append(adB)
                shiftNum.append('')
                shamNum.append('')
            # Test for BREAK
            elif (insType[k] == "BREAK"):
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append('')
                immNum.append('')
                addrNum.append('')
                shiftNum.append('')
                shamNum.append('')
            # Test for NOP
            elif (insType[k] == "NOP"):
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append('')
                immNum.append('')
                addrNum.append('')
                shiftNum.append('')
                shamNum.append('')
            # Test for Data
            elif (insType[k] == "DATA"):
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append('')
                immNum.append('')
                addrNum.append('')
                shiftNum.append('')
                shamNum.append('')
                testBin = tempBin >> 31
                # If data is negative.
                if (testBin == 1):
                    twoC = (0xFFFFFFFF ^ tempBin) + 1
                    dataVal = int(twoC) * -1
                    data[k] = dataVal
                # If data is positive...
                else:
                    # TESTPRINT
                    # print "Positive data at line #" + str(memLines[k])
                    data[k] = int(line, 2)
            else:
                print "Error: unknown data type."
                rmRegNum.append('')
                rnRegNum.append('')
                rdRtRegNum.append('')
                immNum.append('')
                addrNum.append('')
                shiftNum.append('')
                shamNum.append('')
            k += 1

    ##################################################################################
    #   getSpacedStr:  Takes 1st 11 bits, formats them, and populates
    #   spaced string list.
    ##################################################################################
    def getSpacedStr(self):
        # TESTPRINT
        # print
        # print 'Testing getSpacedStr()...'
        k = 0
        for instr in machineLines:
            # TESTPRINT
            # print instr
            if (isInstr[k] == True):
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
                instrSpaced.append(temp)
            else:
                instrSpaced.append('')
            k += 1

    # TESTPRINT
    # print 'test instrSpaced: ' + str(instrSpaced)
    ##################################################################################
    #   printAssem: iterates through the lists and prints assembley code.
    ##################################################################################
    def printAssem(self):
        # TESTPRINT
        # print
        # print 'Testing printAssem()...'
        global finalText
        k = 0
        for k in range(k, numLinesText):
            # Pull single line of binary data, spaced.
            line = ''
            if (isInstr[k] == True):
                # Memory address.
                line += instrSpaced[k]
            else:
                line += machineLines[k]

            line = line + '\t' + str(memLines[k])
            # Print R formats
            if (insType[k] == 'R'):
                line = line + '\t' + opCodeStr[k]
                if (shamNum[k] == ''):
                    line = line + '\t' + 'R' + str(rdRtRegNum[k]) + ', '
                else:
                    line = line + '\t' + 'R' + str(rmRegNum[k]) + ', '
                line = line + ' ' + 'R' + str(rnRegNum[k]) + ','
                # Does this R-format use shift?
                if (shamNum[k] == ''):
                    line = line + ' ' + 'R' + str(rmRegNum[k])
                else:
                    line = line + ' ' + '#' + str(shamNum[k])
            elif (insType[k] == 'I'):
                line = line + '\t' + opCodeStr[k]
                line = line + '\t' + 'R' + str(rdRtRegNum[k]) + ','
                line += ' R' + str(rnRegNum[k]) + ','
                line += ' #' + str(immNum[k])
            elif (insType[k] == 'D'):
                line += '\t' + opCodeStr[k]
                line += '\t' + 'R' + str(rdRtRegNum[k]) + ','
                line += ' ' + '[R' + str(rnRegNum[k]) + ', #'
                line += str(addrNum[k]) + ']'
            elif (insType[k] == "CB"):
                line += '\t' + opCodeStr[k]
                line += '\t' + 'R' + str(rdRtRegNum[k]) + ','
                line += ' ' + '#' + str(addrNum[k])
            elif (insType[k] == "B"):
                line += '\t' + opCodeStr[k]
                line += '\t' + "#" + str(addrNum[k])
            elif (insType[k] == "IM"):
                line += '\t' + opCodeStr[k]
                line += '\t' + "R" + str(rdRtRegNum[k]) + ','
                line += ' ' + str(immNum[k]) + ','
                line += ' ' + "LSL " + str(shiftNum[k])
            elif (insType[k] == 'BREAK'):
                line += '\t' + opCodeStr[k]
            elif (insType[k] == 'DATA'):
                line += '\t' + str(data[k])
            elif (insType[k] == "NOP"):
                line += '\t' + str(opCodeStr[k])
            finalText += line + '\n'
            print 'Final text, loop [' + str(k) + ']'
        # print line
        print finalText
        # print "At end of printAssem"

    ##################################################################################
    #   writeOut:  writes final product to text file.
    ##################################################################################
    def writeOut(self):
        oFile = open(outFile, 'w')
        oFile.write(finalText)
        oFile.close()

    ##################################################################################
    #   run:  processes provided text file.
    ##################################################################################
    def run(self):
        # Open inFile & store data to list.
        self.openRead()
        self.processElvBits()
        self.processRegs()
        self.getSpacedStr()
        self.printAssem()
        self.writeOut()


##################################################################################
#   main:  grabs arguments from command line.
##################################################################################
import sys, getopt
def main():
    global inFile
    global outFile
    diss = Dissemble()
    # TESTPRINT  (Get command line data.)
    # numCmdArgs = len(sys.argv)  # Store number of cmd args.
    # cmdArgList = str(sys.argv)  # Store list of cmd args.
    # print "Number of command line arguments: %d" % numCmdArgs
    # print "List of command line arguments: %s" % cmdArgList
    # Check command line data
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
            inFile = sys.argv[i + 1]
        elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
            outFile = sys.argv[i + 1] + '_dis.txt'
    # TESTPRINT
    # print "inFile: " + inFile
    # print "outFile: " + outFile
    # Store command line file names to class instance.
    # print
    # diss.iFile = inFile  # Save input file name to diss object.
    # diss.oFile = outFile  # Save output file name to diss object.
    # TESTPRINT
    # print "In diss instance, iFile is: " + diss.iFile
    # print "In diss instance, oFile is: " + diss.oFile
    diss.run()
    # TESTPRINT
    # print 'Here is your outFile: ' + outFile
    # print 'Here is your inFile: ' + inFile
    print
    print '***************************************************************'


if __name__ == "__main__":
    main()
