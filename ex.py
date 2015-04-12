#!/usr/bin/python

import sys

def main():
	var = sys.argv[1]
	var1 = sys.argv[2]

	f = open(var, 'rU')
	f1 = open(var1, 'wb')
	for i in f:
		f1.write(i)

	f1.close()
	f.close()
	f2 = open(var1,'rU')
	print 'Reading file...\n', var1
	print '-----------------------------------------------------------------------------------------'
	print f2.read()
	f2.close()

if __name__ == '__main__':
	main()
