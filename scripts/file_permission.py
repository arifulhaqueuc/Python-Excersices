

from os.path import isfile

filename = "react dev sources.txt"

print("Asking for permission")


if isfile(filename):
	f = open(filename)
	print("File named %s found" % filename)
	f.close()
else: 
	print("Nof file named %s found" % filename)

print("Job done")	

