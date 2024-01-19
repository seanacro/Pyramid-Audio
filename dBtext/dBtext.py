import os
import shutil
from pathlib import Path
import time

# Original dBtext location and new location on the server
startPath=Path('path/to/where/the/files/are')
endPath=Path('path/to/where/the/files/need/to/go')

count=0
batchSize=100
batchNo=0
# So it turns out that if you don't break up this script into 
# batches, it'll eventually overwhelm whatever system resource
# is allocated to it and fail. ChatGPT told me to add the batch
# mechanism and lo & behold it worked. Thanks, Ai. I guess.
for b in range(0,len(os.listdir(startPath)),batchSize):
	batch=os.listdir(startPath)[b:b+batchSize]
	batchNo+=1
	for i in batch:
		# for i in os.listdir(startPath):
		# errant files have a way of finding their way where they don't belong. 
		# This makes sure we only process .txt files
		if i[-4:].lower()=='.txt'and len(i)==10:
			# folder name is the txt file sans extension.
			# file name is normalized as lowercase
			folder=i[:-4]
			file=i.lower()
			# source file location and target file location
			# and create the directory if it's not already there
			source=Path(startPath / i)
			destination=Path(endPath / folder)
			destination.mkdir(parents=True, exist_ok=True)
			# The actual final target path for the txt file
			target=Path(destination / file)
			# The line of this script that actually does what needs to be done. Copy the txt file. 
			shutil.copyfile(source,target)
			# print the target path so we get some output
			print(' '.join([str(target),'copied\t',str(count)]))
			count+=1
		else:
			pass
	print(' '.join(['\tBatch',str(batchNo)]))
	time.sleep(1)
# print out a summary of how many files got copied.
print(' '.join(['\n',str(count),'records copied']))
# It ended up being 20,771 records. If you'd been wondering.
