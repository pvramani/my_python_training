"""
Read/Write: text files like .txt, .csv etc

We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect

We have functions for all 3 steps
Step-1: Connect to file
    - open()
Step-2: Read/Write
    - For Writing: 1) write 2) writelines 3) print-function
    - For Reading: 1) read 2) readline 3) readlines
Step-3: Disconnect
    - close()
"""

print("All write operations")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
# my_file_handle = open("provide file name / file path", "provide mode")
my_file_handle = open("my_out_file.txt", "w")
# my_file_handle = open(r"C:\python_training\bin\my_out_file.txt", "w")
# mode 'w': Write only
# mode 'w': It will create new file
# mode 'w': IMPORTANT: It will erase existing content of the file

# mode 'r': Readonly mode and it will not create new file
# mode 'a': Append mode, It will create new file only if file not present
# modes 'w+', 'a+', 'r+': It is Read & Write Mode

# Step-2: Write
# -----------

# Our data
x = 10
y = "python"

# Convert other type of data to string because 1) write & 2) writelines
# expects data in strings
x = str(x)

# 1) Write: It takes one argument i.e string
my_file_handle.write(x+"\n")
my_file_handle.write(y+"\n")

# 2) writelines: It takes collection of values like list/tuple etc
my_values = [x+"\n", y+"\n"]
my_file_handle.writelines(my_values)

# 3) print function
print(x, y, 20, "Java", sep="\n", file=my_file_handle)

# Step-3: Disconnect
# -----------
my_file_handle.close()

print("""
All write operations are completed
Please check my_out_file.txt
""")

print("#"*40, end="\n\n")
# ###############################
print("Reading from file using: read()")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
file_content = my_file_handle.read() # returns complete content in string
print("file_content:", file_content)
print("file_content in raw format:", repr(file_content))

# Step-3: Disconnect
# -----------
my_file_handle.close()

print("#"*40, end="\n\n")
# ###############################
print("Reading from file using: readlines()")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
file_content = my_file_handle.readlines() # returns complete content in list
print("file_content:", file_content)

# Step-3: Disconnect
# -----------
my_file_handle.close()

print("#"*40, end="\n\n")
# ###############################
print("Reading from file using: readline()")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
file_content = my_file_handle.readline() # returns one line
print("one Line:", file_content)

file_content = my_file_handle.readline() # returns one line
print("Next Line:", file_content)

file_content = my_file_handle.readline() # returns one line
print("Next Line:", file_content)

# Step-3: Disconnect
# -----------
my_file_handle.close()

print("#"*40, end="\n\n")
# ###############################