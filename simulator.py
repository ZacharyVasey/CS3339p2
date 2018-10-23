#coverts binary to decimal. EX: bin_to_dec("1001011") = 75
def unsbin_to_dec(number = []):
	#init return value to 0
	decimal_number = 0
	# 5 ** 3 = 5 to the power of  3 = 125
	
	#this if is for error checking
	if(len(number) <= 0):
		return 0;
	
	#power = the highest binary digit in decimal EX if 1001011, power = 2 ** 6
	power = 2 ** (len(number) - 1)
	
	#traverse through the binary string number
	for i in number:
		#if it is one, add power to the final decimal number. Else do not
		if(i == '1'):
			decimal_number = decimal_number + power
		
		#reduce the power by two to switch to the next digit
		power = power / 2
		
	#return the decimal number
	return decimal_number
################################################################################
#coverts binary to decimal. EX: bin_to_dec("1001011") = 75
def sinbin_to_dec(number = []):
	#init return value to 0
	decimal_number = 0
	negative = False
	if(number[0] == "1"):
		negative = True
	if(not negative):
		return unsbin_to_dec(''.join(number[1:31]))
	else:
		temp = []
		inExtend = True
		count = 0
		while(inExtend):
			if(number[count] == "1" and number[count + 1] == "0"):
				inExtend = False
			count = count + 1
			if(count == (len(number) - 2) and number[count + 1] == "1"): #if -1
				return -1
		while(count < len(number)):
			temp.append(number[count])
			count = count + 1
		count = 0
		#TESTPRINT
		#print temp
		while(count < len(temp)):
			if(temp[count] == "0"):
				temp[count] = "1"
			else:
				temp[count] = "0"
			count = count + 1
		#TESTPRINT
		#print temp
		add_one_to_bin(temp)
		#TESTPRINT
		#print temp
		return -1 * unsbin_to_dec(''.join(temp))
	#return the decimal number
	return 0
#################################################################
def dec_to_unsbin(number = 0):
	temp = number
	#init return value to 0
	binary_number = []
	# 5 ** 3 = 5 to the power of  3 = 125
	power = 0
	while(2 ** power < temp):
		power = power + 1
	#if number is 62, power will equal 6. 2 ** 6 = 64
	while(power >= 0):
		if(temp >= (2 ** power)):
			temp = temp - (2 ** power)
			binary_number.append("1")
		else:
			binary_number.append("0")
		power = power - 1
	#reverse list
	binary_number_reversed = []
	count = len(binary_number)
	while(count > 0):
		binary_number_reversed.append(binary_number[count - 1])
		count = count - 1
	#return the binary number
	return ''.join(binary_number_reversed)
################################################################
def dec_to_sinbin32(number = 0):
	negative = False
	if(number < 0):
		temp = -1 * number
		negative = True
	else:
		temp = number
	#init return value to 0
	binary_number = []
	# 5 ** 3 = 5 to the power of  3 = 125
	power = 0
	while(2 ** power < temp):
		power = power + 1
	#if number is 62, power will equal 6. 2 ** 6 = 64
	while(power >= 0):
		if(temp >= (2 ** power)):
			temp = temp - (2 ** power)
			binary_number.append("1")
		else:
			binary_number.append("0")
		power = power - 1
	while(len(binary_number) != 32):
		binary_number.append("0")
	#reverse list
	binary_number_reversed = []
	count = len(binary_number)
	while(count > 0):
		binary_number_reversed.append(binary_number[count - 1])
		count = count - 1
	if(negative):
		count = 0 
		while(count < len(binary_number_reversed)): 
			if(binary_number_reversed[count] == "1"):
				binary_number_reversed[count] = "0"
			else:
				binary_number_reversed[count] = "1"
			count = count + 1
		add_one_to_bin(binary_number_reversed)
	#return the binary number
	return ''.join(binary_number_reversed)
################################################################
def add_one_to_bin(number = []):
	index = len(number) - 1
	while(index >= 0):
		if(number[index] == "1"):
			number[index] = "0"
		else:
			number[index] = "1"
			index = -1
		index = index - 1

#################################################################
def sub_one_from_bin(number = []):
	index = len(number) - 1
	while(index >= 0):
		if(number[index] == "0"):
			number[index] = "1"
		else:
			number[index] = "1"
			number[index] = "0"
			index = -1
		index = index - 1
####################################################################
##################################################################################
#   Simulator Class
#       Runs assembley code
##################################################################################
class Simulator:
	def ADD(self, arg1, arg2, arg3):
		arg1 = arg2 + arg3
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
		arg2bin = dec_to_sinbin32(arg2)
		arg3bin = dec_to_sinbin32(arg3)
		#TESTPRINT
		print arg2bin
		print arg3bin
		arg1bin = []
		count = 0
		while(count < len(arg2bin)):
			if(arg2bin[count] == "1" and arg3bin[count] == "1"):
				arg1bin.append("1")
			else:
				arg1bin.append("0")
			count = count + 1
		arg1 = sinbin_to_dec(arg1bin)
		print arg1
		print arg1bin
	def ORR(self, arg1, arg2, arg3):
		arg2bin = dec_to_sinbin32(arg2)
		arg3bin = dec_to_sinbin32(arg3)
		#TESTPRINT
		print arg2bin
		print arg3bin
		arg1bin = []
		count = 0
		while(count < len(arg2bin)):
			if(arg2bin[count] == "1" or arg3bin[count] == "1"):
				arg1bin.append("1")
			else:
				arg1bin.append("0")
			count = count + 1
		arg1 = sinbin_to_dec(arg1bin)
		print arg1
		print arg1bin
	def EOR(self, arg1, arg2, arg3):
		#Code
		print hello
	def LDUR(self, arg1, arg2, mem):
		#Code
		print hello
	def SDUR(self, arg1, arg2, mem):
		#Code
		print hello
	def CBZ(self, arg1, offset):
		#Code
		print hello
	def CBNZ(self, arg1, offset):
		#Code
		print hello
	def MOVZ(self, arg1, val, shift):
		#Code
		print hello
	def MOVK(self, arg1, val, shift):
		#Code
		print hello
	def B(self, arg1):
		#Code
		print hello
	def NOP():
		#Code
		print hello
##############################################
def main():
	a = Simulator()
	b = 15
	c = 20
	a.ADD(b, c, 10)
	a.AND(b, 10, 15)
	a.ORR(b, 10, 15)

if __name__ == "__main__":
	main()