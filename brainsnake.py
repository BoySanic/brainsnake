import sys



def interpret(brainfuck):	
	programcounter = 0
	pointer = 0
	cells = [0] * 32768
	inLoop = False
	ignoreNext = False
	char = ""
	loopdict = {

	}
	while(True):
		char = brainfuck[programcounter]
		#print(char)
		if(char == '>'):
				pointer += 1
				#print(pointer)
		if(char == '<'):
			pointer -= 1
			#print(pointer)
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
			print(cells[pointer])
		if(char == ','):
			cells[pointer] = raw_input("What do you want to enter: ")
		if(char == '['):
			#find matching closing bracket
			c = char
			p = programcounter
			i = 0
			while(True):
				c = brainfuck[p]
				if(c == '['):
					i += 1
				if(c == ']'):
					i -= 1
				if(i == 0):
					print("The closing bracket is at %s" % p)
					loopdict[p] = programcounter
					print(loopdict)	
					break
				p += 1
			#append to dict
			if(cells[pointer] == 0):
				#print("Woah we're leaving a loop")
				i = 0
				while(True):
					c = brainfuck[programcounter]
					if(c == '['):
						i += 1
					if(c == ']'):
						i -= 1
					if(i == 0):
						break
					programcounter += 1
		if(char == ']'):
			#print("We going back?")
			if(ignoreNext != True):
				if(cells[pointer] != 0):
					#print("Yes" + str(programcounter))
					programcounter = loopdict[programcounter]
					#print(char + str(programcounter))
				#else:
					#print("Nah" + str(programcounter))
		if(programcounter == len(brainfuck)):
			print("fucking")
			break
		print("DEBUG: programcounter=%i pointer=%i cells[pointer] = %i, char=%s" % (programcounter, pointer, cells[pointer], char))
		programcounter += 1
		#raw_input()


def main():
	f = open(sys.argv[1])
	contents = f.read()
	o = interpret(contents)
main()