#!/usr/bin/python

import sys

def translate(s):
	
	for l in s:
		if l == 'a' and 'i' and 'o' and 'u' and ' ':
			print l
		else:
			print l+'o'+l
	 

def main():
	var = raw_input('Enter message to be encripted: ')
	translate(var)

if __name__ == '__main__':
	main()
