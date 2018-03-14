
"""
Task: Menu driven operations on a tar archive.

Steps:
1. Open the tar file.
2. Present the menu and get the user selection.
3. If you press 1, the program prompts you for the file
name in the archive to extract the current directory
to and then extracts the file.
4. If you press 2, the program prompts you for the file
name and then displays the file information.
5. If you press 3, the program lists all the files in the
archive.

"""


import tarfile, sys
try:
 #open tarfile
 tar = tarfile.open(sys.argv[1], "r:tar")
 #present menu and get selection
 selection = raw_input("Enter\n\
 1 to extract a file\n\
 2 to display information on a file in the archive\n\
 3 to list all the files in the archive\n\n")
 
 
 #perform actions based on selection above
 if selection == "1":
 filename = raw_input("enter the
filename to extract: ")
 tar.extract(filename)
 elif selection == "2":
 filename = raw_input("enter the
filename to inspect: ")



for tarinfo in tar:
 if tarinfo.name == filename:
 print "\n\
 Filename:\t\t", tarinfo.name, "\n\
 Size:\t\t", tarinfo.size, "bytes\n\
 elif selection == "3":
 print tar.list(verbose=True)
except:
 print "There was a problem running the
program"




