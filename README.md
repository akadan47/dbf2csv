# dbf2csv

Small command line utility to convert simple *.DBF files to *.CSV

### Install

    pip install dbf2csv



### Usage

	dbf2csv [-h] [-v] [-ie INPUT_ENCODING] [-oe OUTPUT_ENCODING]
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
	  -ie INPUT_ENCODING, --input-encoding INPUT_ENCODING
							charset of *.dbf files (default: cp850)
	  -oe OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
							charset of *.csv files (default: utf8)
	  -q {minimal,all,non-numeric,none}, --quoting-mode {minimal,all,non-numeric,none}
							quoting mode for csv files (default: minimal)
	  -d DELIMITER_CHAR, --delimiter-char DELIMITER_CHAR
							delimiter char for csv files (default: ",")
	  -e ESCAPE_CHAR, --escape-char ESCAPE_CHAR
							escape char for csv files (default: "\")



### Example

	dbf2csv input.dbf > output.csv
	
	# Grep output
	dbf2csv file.dbf | grep <filter_string>
	
	# Convert all *.dbf files from current dir, tab-delimited CSV
	dbf2csv . output/ -d $'\t'
	
	# Convert all *.dbf files from input dir to output dir, with charset conversion, quote all fields
	dbf2csv /path/to/input/dir/ /path/to/output/dir/ -ie cp866 -oe cp1251 -q all
	
