
import stat, sys, os, string, commands

"""
Search for files and show permissions
Steps:
1. Get the search pattern from the user.
2. Perform the search.
3. Print a listing of files found.
4. Using the stat module, get permissions for
each file found.
5. Present the results to the user.
"""


#Getting search pattern from user and assigning it to a list

try:

	#run a 'find' command and assign results to a variable
	pattern = raw_input("Enter the file pattern to search for:\n")
	commandString = "find " + pattern
	commandOutput = commands.getoutput(commandString)
	findResults = string.split(commandOutput, "\n")

	#output find results, along with permissions
	print "Files:"
	print commandOutput
	print "================================"


	for file in findResults:
		mode = stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
		print "\nPermissions for file ", file, + ":"



	for level in "USR", "GRP", "OTH":
		for perm in "R", "W", "X":
			if mode & getattr(stat,"S_I"+perm+level):
				print level, " has ", perm, " permission"
			else:
				print level, " does NOT have ", perm, "permission"
except:
	print "There was a problem - check the message above"	
