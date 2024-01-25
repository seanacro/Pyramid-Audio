import os
import re
from pathlib import Path

# We have a lot of unorganized files sitting various
# directories. I'd already set them aside but this 
# organized as many of them as possible into the new dBtext
# folder. 

misc=Path("O:/Documents0")
dest=Path("O:/Documents0")

count=0
for i in os.listdir(misc):
  match=re.search(r'(^(?=.{5}$)[11-13]\d{4})',i)
  if match:
    match=match.group()
    for file in os.listdir(Path(misc/match)):
      print(file)
      dir=re.search(r'(^[11-13]\d{5})',file)
      if dir:
        dir=dir.group()
        directory=Path(misc/dir)
        os.system('move ' + '"' + str(Path(misc/match/file)) + '" ' + '"' + str(directory) + '"')
      count+=1
      print(count)
    # directory=Path(dest/match)
    # directory.mkdir(parents=True, exist_ok=True)
    # i=Path(misc,i)
    # os.system('move ' + '"' + str(i) + '" ' + '"' + str(directory) + '"')
    # count+=1
    # print(count)
    # print(i)
      
# lol so I put some stuff where it doesn't belong
# and had to write more code to fix that.
# Don't test in prod, kids.