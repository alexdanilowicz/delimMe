# simple python script to convert input into comma seperated values, similar to delim.co
# great for SQL queries.
# Input: .txt file, values seperated by new line. Script adds double quotes and seperates by commas
# Output: with_commas_ORIGINAL_FILENAME.csv and with_commas_ORIGINAL_FILENAME.txt
#
# Author: Alexander Danilowicz
# January 2018
#
# Originally for use at Owler, but can be applied to any data that you're looking to convert to CSV

import sys # for reading the command line

def read_command_line():
	"""
	parses command line arguments, prints error if error
	calls convert
	"""

	if len(sys.argv) != 2:
		print("Usage: too many or too few arguments")
		print("Example usage: `python3 delimMe.py column.txt")

	column_file_name = str(sys.argv[1])

	sol_csv_file = "with_commas_" + column_file_name[:-4] + ".csv" #  get rid of .txt, create your solution file name
	sol_txt_file = "with_commas_" + column_file_name #  solution text file
	convert(sys.argv[1], sol_csv_file, sol_txt_file)


def convert(input, sol_filename, sol_txt_file):
	"""
	converts the input file into 2 output files
	input: .txt file seperated by lines, each line turns into "text",
	output: two output files: 1 in .txt format, 1 in .csv format
	"""

	# open your files
	input_f = open(input, 'r')
	sol_csv_f = open(sol_filename, 'wt')
	sol_txt_f = open(sol_txt_file, 'wt')

	lines = input_f.readlines()
	last = lines[-1] # get last line

	# loop through input file
	for line in lines:
		if line == "\n": # ignore blan lines
			continue
		no_new_line = line[:-1] # get rid of new line character
		csv_line = str("\"" + no_new_line + "\"") # append double quotes

		if line is last:
				sol_csv_f.write(csv_line) # no comma or newline
				sol_txt_f.write(csv_line) # no comma or newline
		else:
			# write it to both files
			sol_csv_f.write(csv_line + ", \n") # comma / and new line
			sol_txt_f.write(csv_line + ", \n") # comma / and new line

	
	# clean up
	input_f.close()
	sol_csv_f.close()
	sol_txt_f.close()

if __name__ == "__main__":
	read_command_line()