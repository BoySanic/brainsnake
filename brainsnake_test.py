import sys

class Operation:
	def __init__(self, o, c):
		self.opcode = o
		self.count = c

def compress(brainfuck):
	operList = []
	num = 0
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
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == "+"):
					count += 1
					num += 1
				if(brainfuck[x] == "-"):
					count -= 1
					num += 1
				if((brainfuck[x] == "+" or brainfuck[x] == "-") == False):
					break
		elif(char == "-"):
			for x in range(num, len(brainfuck)):
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
		o = Operation(char, count)
		operList.append(o)
		if(num == len(brainfuck)):
			return operList

def execute(operations):
	programcounter = 0
	pointer = 0
	cells = [0] * 32768
	char = ""
	loopdict = {

	}
	dictloop = {

	}
	while(True):
		x = operations[programcounter]
		if(x.opcode == ">"):
			pointer += x.count
		if(x.opcode == "<"):
			pointer -= x.count
		if(x.opcode == '+'):
			if(cells[pointer] + x.count > 255):
				cells[pointer] = 0 + (x.count - 1)
			else:
				cells[pointer] += x.count
		if(x.opcode == '-'):
			if(cells[pointer] - x.count < 0):
				cells[pointer] = 255 - (x.count - 1)
			else:
				cells[pointer] -= x.count
		if(x.opcode == '.'):
			sys.stdout.write(chr(cells[pointer]))
			sys.stdout.flush()
		if(x.opcode == '['):
			c = x.opcode
			p = programcounter
			i = 0
			if(dictloop.has_key(programcounter) != True):
				while(True):
					c = operations[p].opcode
					if(c == '['):
						i += 1
					if(c == ']'):
						i -= 1
					if(i == 0 and c == ']'):
						loopdict[p] = programcounter
						dictloop[programcounter] = p
						break
					p += 1
			if(cells[pointer] == 0):
				programcounter = dictloop[programcounter]
		if(x.opcode == ']'):

				if(cells[pointer] != 0):
					programcounter = loopdict[programcounter]
		if(programcounter == len(operations)):
			print("fucking")
			break
		programcounter += 1

def interpret(brainfuck):	
	programcounter = 0
	pointer = 0
	cells = [0] * 32768
	char = ""
	loopdict = {

	}
	dictloop = {

	}
	while(True):
		char = brainfuck[programcounter]
		if(char == '>'):
			pointer += 1
		if(char == '<'):
			pointer -= 1
		if(char == '+'):
			if(cells[pointer] == 255):
				cells[pointer] = 0
			else:
				cells[pointer] += 1
		if(char == '-'):
			if(cells[pointer] == 0):
				cells[pointer] = 255
			else:
				cells[pointer] -= 1
		if(char == '.'):
			sys.stdout.write(chr(cells[pointer]))
			sys.stdout.flush()
		if(char == ','):
			cells[pointer] = raw_input("What do you want to enter: ")
		if(char == '['):
			c = char
			p = programcounter
			i = 0
			if(dictloop.has_key(programcounter) != True):
				while(True):
					c = brainfuck[p]
					if(c == '['):
						i += 1
					if(c == ']'):
						i -= 1
					if(i == 0):
						loopdict[p] = programcounter
						dictloop[programcounter] = p
						break
					p += 1
			if(cells[pointer] == 0):
				programcounter = dictloop[programcounter]
		if(char == ']'):
				if(cells[pointer] != 0):
					programcounter = loopdict[programcounter]
		if(programcounter == len(brainfuck)):
			print("fucking")
			break
		programcounter += 1


def main():
	f = open(sys.argv[1])
	contents = f.read()
	operations = compress(contents)
	print("Finished compression")
	execute(operations)
	#o = interpret(contents)
main()