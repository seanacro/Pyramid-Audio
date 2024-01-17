import os
import shutil
from pathlib import Path

# Original dBtext location and new location on the server
startPath=Path('path/to/original/files')
endPath=Path('path/to/target/directory')

count=0
for i in os.listdir(startPath):
  # errant files have a way of finding their way where they don't belong. 
  # This makes sure we only process .txt files
  if i[-4:].lower()=='.txt':
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
    print(target)
    count+=1
  else:
    pass
# print out a summary of how many files got copied.
print(' '.join(['\n',str(count),'records']))
