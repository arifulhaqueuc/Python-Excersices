import subprocess


def my_function():
	"""this function will take a file name as input, and then will print the number of lines in that file"""
	print("please input the file name:")
	file_name = str(input())

	try:
		data = file_name
		command = "wc -l"
		instruc = command + " "+ data
		print("Counting the number of lines in " + data + ":")
		subprocess.call(instruc, shell=True)
	except:
		print("No file found")


if __name__ == "__main__":
	my_function()
