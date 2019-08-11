#don't use this one wam

import sys
import numpy as np

class Operation:
	def __init__(self, o, c):
		self.opcode = o
		self.count = c

def compress(brainfuck):
	operList1 = []
	operList2 = []
	num = 0
	i = 0
	length = len(brainfuck)
	print(len(brainfuck))
	while(True):
		count = 0
		char = brainfuck[num]
		if(char == ">"):
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == ">"):
					count += 1
					num += 1
				if(brainfuck[x] == "<"):
					count -= 1
					num += 1
				if((brainfuck[x] == "<" or brainfuck[x] == ">") == False):
					break

		elif(char == "<"):
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == "<"):
					count += 1
					num += 1
				if(brainfuck[x] == ">"):
					count -= 1
					num += 1
				if((brainfuck[x] == "<" or brainfuck[x] == ">") == False):
					break
		elif(char == "+"):
			for x in range(num, length):
				if(brainfuck[x] == "+"):
					count += 1
					num += 1
				if(brainfuck[x] == "-"):
					count -= 1
					num += 1
				if((brainfuck[x] == "+" or brainfuck[x] == "-") == False):
					break
		elif(char == "-"):
			for x in range(num, length):
				if(brainfuck[x] == "+"):
					count -= 1
					num += 1
				if(brainfuck[x] == "-"):
					count += 1
					num += 1
				if((brainfuck[x] == "+" or brainfuck[x] == "-") == False):
					break
		elif(char == "."):
			count += 1
			num += 1
		elif(char == ","):
			count += 1
			num += 1
		elif(char == "["):
			count += 1
			num += 1
		elif(char == "]"):
			count += 1
			num += 1
		else:
			num += 1
		#raw_input()
		operList1.append(char)
		operList2.append(count)

		if(num == length):
			return operList1, operList2
#list of operations
#operation = opcode and count
#array of operations
#operation = array, opcode and count
#[[opcode, count],[opcode, count]]
def execute(opcodes, counts):
	programcounter = 0
	pointer = 0
	cells = [0] * 32768
	length = len(opcodes)
	char = ""
	loopcount = 0
	loopdict = {

	}
	dictloop = {

	}
	while(True):
		char = opcodes[programcounter]
		count = counts[programcounter]
		if(char == '['):
			c = char
			p = programcounter
			i = 0
			while(True):
				c = opcodes[p]
				if(c == '['):
					i += 1
				if(c == ']'):
					i -= 1
				if(i == 0):
					loopdict[p] = programcounter
					dictloop[programcounter] = p
					break
				p += 1
		programcounter += 1
		if(programcounter == length - 1):
			print("Got pairs")
			break
	programcounter = 0
	while(True):
		loopcount += 1
		opcode = opcodes[programcounter]
		count = counts[programcounter]
		if(opcode == ">"):
			pointer += count
		elif(opcode == "<"):
			pointer -= count
		elif(opcode == '+'):
			if(cells[pointer] + count > 255):
				cells[pointer] = 0 + (count - 1)
			else:
				cells[pointer] += count
		elif(opcode == '-'):
			if(cells[pointer] - count < 0):
				cells[pointer] = 255 - (count - 1)
			else:
				cells[pointer] -= count
		elif(opcode == '.'):
			sys.stdout.write(chr(cells[pointer]))
			sys.stdout.flush()
		elif(opcode == '['):
			if(cells[pointer] == 0):
				programcounter = dictloop[programcounter]
		elif(opcode == ']'):
			if(cells[pointer] != 0):
				programcounter = loopdict[programcounter]
		if(programcounter == length - 1):
			print(loopcount)
			break
		programcounter += 1
def main():
	f = open(sys.argv[1])
	contents = f.read()
	opcodes, counts = compress(contents)
	print("Finished compression")
	execute(opcodes, counts)
	#o = interpret(contents)
main()