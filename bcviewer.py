#!/usr/local/bin/python3

import sys
import time
from bcreader import *
from bcclasses import Block, BlockHeader

def parse(blockchain):
	print('Parsing the AidCoin blockchain...')
	continueParsing = True
	counter = 0
	blockchain.seek(0, 2)
	fSize = blockchain.tell() - 80 # Minus last block header size for partial file
	blockchain.seek(0, 0)
	
	while continueParsing:
		block = Block(blockchain)
		continueParsing = block.continueParsing
		if continueParsing:
			block.toString()
		counter+=1

	print('')
	print('Reached End of Field')
	print("Parsed %d blocks" % counter)

def main():
	start_time = time.time()
	if len(sys.argv) < 2:
            print('Usage: bcviewer.py filename')
	else:
		with open(sys.argv[1], 'rb') as blockchain:
			parse(blockchain)
	print("--- %s seconds to execute ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()



