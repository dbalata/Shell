import os, sys

def ls():
	dirs = os.listdir()
	for d in dirs:
		print(d)

def handleInput(input):
	if   (input == ""): return
	elif (input == "ls"): ls()
	elif (input == "exit"): sys.exit()
	else: print("Unrecognized command.")

def main():
	os.chdir(os.environ["HOME"])
	while(True):
		handleInput(input('\u001b[36m' + os.getcwd() + " $ " + '\u001b[37m'))

if __name__ == '__main__':
	main()