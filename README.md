## Blockchain Viewer
This is a basic blockchain viewer written in Python to parse and display the Bitcoin blockchain.

## Package Code
1. bcreader.py: Reads binary data from block files.
2. bcclasses.py: Provides classes to represent Blocks and Transactions on the blockchain.
3. bcviewer.py: Views the Bitcoin blockchain and lists transactions in a particular block.

## Package Sample Data
a. block1x5.dat - the first five MB of data from data file: blk00000.dat
b. block65x5.dat - the first 5 MB of data from data file: blk00065.dat

## Usage
> python bcviewer.py block1x5.dat
