import json

# dBase adheres to the old (*old*) school file naming restrictions
# and will only write files with 3 character extensions. But we want 
# our JSON files to have the 4 character '.json' extension. Hence:

def main():
	path="drawer.jso"
	dest="drawer.json"

	# dBase appends an EOF character to the end of any file it generates
	# and that prevents Python from recognizing our JSON as valid.
	# This block removes that character so the following blocks will work.
	readFile = open(path, 'r')
	data = readFile.read()
	readFile.close()
	writeFile = open(dest, 'w')
	writeFile.write(data[0:-1])
	writeFile.close()

	# And now we can actually do the thing
	with open(file=dest, mode="r") as jso:
		object=json.load(jso)

	with open(file=dest, mode="w") as jsn:
		json.dump(object, jsn, indent=2)

	jso.close()
	jsn.close()

main()