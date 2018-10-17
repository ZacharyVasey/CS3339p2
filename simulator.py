##################################################################################
#   
#	Simulator Class
#       Runs assembley code
#
##################################################################################
class Simulator:
	def ADD(self, arg1, arg2, arg3):
		#TESTPRINT
		print arg1
		print arg2
		print arg3
		arg1 = arg2 + arg3
		#TESTPRINT
		print arg1
	def ADDI(self, arg1, arg2, imm):
		arg1 = arg2 + imm
	def SUB(self, arg1, arg2, arg3):
		arg1 = arg2 - arg3
	def SUBI(self, arg1, arg2, imm):
		arg1 = arg2 - imm
	def LSL(self, arg1, arg2, shift):
		arg1 = arg2 * (2 ** shift)
		#can shift be negative?6
	def LSR(self, arg1, arg2, shift):
		arg1 = arg2 / (2 ** shift)
		#can shift be negative?
	def AND(self, arg1, arg2, arg3):
		#TESTPRINT
		print arg1
		print arg2
		print arg3
	def ORR(self, arg1, arg2, arg3):
		#Code
		print "hello"
	def EOR(self, arg1, arg2, arg3):
		#Code
		print "hello"
	def LDUR(self, arg1, arg2, mem):
		#Code
		print "hello"
	def SDUR(self, arg1, arg2, mem):
		#Code
		print "hello"
	def CBZ(self, arg1, offset):
		#Code
		print "hello"
	def CBNZ(self, arg1, offset):
		#Code
		print "hello"
	def MOVZ(self, arg1, val, shift):
		#Code
		print "hello"
	def MOVK(self, arg1, val, shift):
		#Code
		print "hello"
	def B(self, arg1):
		#Code
		print "hello"
	def NOP(self):
		#Code
		print "hello"
##############################################
def main():
	a = Simulator()
	b = 15
	c = 20
	a.ADD(b, c, 10)

if __name__ == "__main__":
	main()