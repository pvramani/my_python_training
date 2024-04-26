"""
From the given string, extract
IP
DATE
PICS
URL

Expected Output:
-----------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
-----------------
"""

print("input data")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)
print(type(input_data))
print(repr(input_data))
print(len(input_data))

import sys
print("size of input data:", sys.getsizeof(input_data), " Bytes")

print("#"*40, end="\n\n")
# ###############################

print("Extract IP")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_1st_space = input_data.index(" ") # index of 1st space
ip = input_data[0:index_of_1st_space]
print(ip)

# >>> # index() Example
# >>> s = "WEL COME"
# >>> s.index('E') # it return index of 1st occurance of E'
# 1
# >>> s.index('E', 3) # start search for 'E' from index-3 onwards
# 7

print("#"*40, end="\n\n")
# ###############################
print("Extract DATE")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split()
print("Splitted Values:", sp, end="\n\n")

raw_date = sp[3] # '[26/Apr/2000:00:23:48'

# Remove '[' from '[26/Apr/2000:00:23:48'
raw_date = raw_date[1:] # '26/Apr/2000:00:23:48'

index_of_colon = raw_date.index(":")
dt = raw_date[:index_of_colon]
print(dt)

print("#"*40, end="\n\n")
# ###############################
print("Extract PICS")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split()
print("Splitted Values:", sp, end="\n\n")

raw_img = sp[6] # '/pics/wpaper.gif'
img = raw_img[6:]
print(img)

print("#"*40, end="\n\n")
# ###############################
print("Extract URL")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split()
print("Splitted Values:", sp, end="\n\n")

raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
url = raw_url[1:-1]
print(url)

print("#"*40, end="\n\n")
# ###############################