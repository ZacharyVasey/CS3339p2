import sys, getopt
from bin_data import BinData
from dissembler import Dissemble
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
if __name__== "__main__":
	main()