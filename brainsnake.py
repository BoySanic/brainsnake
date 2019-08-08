import sys
import numpy as np

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
	o = interpret(contents)
main()