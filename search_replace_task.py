"""
Search & Replace
Description:
	You need to write a method that takes in as an argument the location of a file on the filesystem.
	This is a text file that contains an old version of a program source code.
	It contains statements such as `print "hello world"`, that are no longer valid and need to be updated.
	You need to open such a file and update any such instances
	The broken statement you are updating is:
	A space
	An opening quote, either " or '
	A string, X
	A closing quote matching the opening one
	This should be converted to print("X")
	Maintain any characters before or after the statement
	Assume each open quote has an appropriate closing quote
	The print statements don't have any special formatting rules
When is the problem solved?
	A corrected file can be found at the location of the original, with ".new" at the end of the filename in place of ".old"
"""

def process_file():
    pass

if __name__ == "__main__":
    process_file("my_script.old")
