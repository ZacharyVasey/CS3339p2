import sys, getopt
from bin_data import BinData
from dissembler import Dissemble
from simulator import Simulator
def main():
	binData = BinData() # inData holds all the binary and assembled data.
	# Get command line data
	for i in range(len(sys.argv)):
		if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
			binData.inFile = sys.argv[i+1]
		elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
			binData.outFile = sys.argv[i+1] + '_dis.txt'
	# Initialize objects
	diss = Dissemble()
	diss.run(binData)
	sim = Simulator(binData.opCodeStr, binData.isInstr, binData.insType, binData.data, binData.rmRegNum,
	                binData.shamNum, binData.rnRegNum, binData.rdRtRegNum, binData.immNum, binData.addrNum,
	                binData.shiftNum, binData.litInstr, binData.memLines, binData.numLinesText)
	sim.run()
if __name__== "__main__":
	main()
