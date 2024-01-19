import os
from pathlib import Path
import shutil

ops=Path('/Volumes/Operations_0/Documents0')
count=0
txt='.txt'.lower()
for i in os.listdir(ops):
	directory=Path(ops/i)
	if os.path.isdir(directory)==True:
		if len(os.listdir(directory)) > 0:
			count+=1
			subs=[s.lower() for s in os.listdir(directory)]
			target=''.join([i,txt])
			dele=Path(directory/target)
			if target in subs and os.path.isdir(dele)==True:
				shutil.rmtree(Path(dele))
				print(' '.join([target,'removed\t',str(count)]))
			elif os.path.isdir(dele)==False:
				pass
					