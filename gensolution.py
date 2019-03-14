import subprocess
import pickle
import os

BASEBALL_EXE = './baseball'

solutions = {}

for file in os.listdir('testcases'):
	if '.txt' not in file:
		continue
	solutions[file] = {}
	p = subprocess.Popen([BASEBALL_EXE], stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf8')
	output = p.communicate(open(os.path.join('testcases', file)).read())[0].split('\n')
	for line in output:
		c = line.split()
		if len(c) == 0:
			continue
		solutions[file][c[0]] = (c[2] != 'not')

pickle.dump(solutions, open('solutions.pickle', 'wb'))