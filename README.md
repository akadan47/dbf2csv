# dbf2csv

Small command line utility to convert simple *.DBF files to *.CSV

##Install:

    pip install dbf2csv


##Usage:

	usage: dbf2csv [-h] [-v] [-ei INPUT_ENCODING] [-eo OUTPUT_ENCODING]
				   [-q {minimal,all,non-numeric,none}] [-d DELIMITER_CHAR]
				   [-e ESCAPE_CHAR]
				   input [output]
	
	small utility to convert simple *.DBF files to *.CSV
	
	positional arguments:
	  input
	  output
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -ei INPUT_ENCODING, --input-encoding INPUT_ENCODING
							charset of *.dbf files (default: cp850)
	  -eo OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
							charset of *.csv files (default: utf8)
	  -q {minimal,all,non-numeric,none}, --quoting-mode {minimal,all,non-numeric,none}
							quoting mode for csv files (default: minimal)
	  -d DELIMITER_CHAR, --delimiter-char DELIMITER_CHAR
							delimiter char for csv files (default: ",")
	  -e ESCAPE_CHAR, --escape-char ESCAPE_CHAR
							escape char for csv files (default: "\")


###Example:

	dbf2csv file.dbf > output.csv
	
	# Grep output
	dbf2csv file.dbf | grep <search_string>
	
	# Tab-delimited CSV
	dbf2csv . output/ -ei cp866 -d $'\t'
	
	# Quote all fields
	dbf2csv /path/to/input/dir/ /path/to/output/dir/ -ei cp866 -eo utf8 -q all
	