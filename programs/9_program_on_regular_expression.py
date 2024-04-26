"""
Get data from sample_data.txt,
extract info using regular expression
"""

print("Get data from sample_data.txt")
print("-"*20)
# -----------

my_log_file_handle = open(r"../log/sample_data.txt", "r")
log_file_content = my_log_file_handle.readlines()
print(log_file_content)

print("#"*40, end="\n\n")
# ###############################

print("Check whether it is IP address line or not")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")


# COMMENT
"""
Regular Expression

IDENTIFIERS
------------
\d -> to tell any ONE digit b/n 0 to 9
\D -> to tell any ONE non-digit. i.e, except 0 to 9
. -> to tell any ONE any character
\. -> strictly DOT
[.] -> strictly DOT
[0-9] -> to tell any ONE digit b/n 0 to 9
------------

QUANTIFIERS
------------
\d{3} -> it tell \d 3 numbers
\d{1,3} -> it tells it can be 1 to 3 numbers
[0-9]{3} -> it tells [0-9]  3 times
------------

MODIFIERS
------------
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 time
------------
"""

print("#"*40, end="\n\n")
# ###############################
print("Extract IP")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT
"""
put () to IP address pattern to capture the value
-> this is called GROUPing
-> each Group has index number starting from 1
"""

print("#"*40, end="\n\n")
# ###############################
print("Extract IP, DATE")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
"""
26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
[0-9]\d # Strictly 2 digits
\d[0-9] # Strictly 2 digits

\d{1,2} # minimum 1 digit, maximum 2 digits
[0-9]{1,2} # minimum 1 digit, maximum 2 digits
\d?\d # minimum 1 digit, maximum 2 digits
[0-9]?[0-9] # minimum 1 digit, maximum 2 digits
\d?[0-9] # minimum 1 digit, maximum 2 digits
[0-9]?\d # minimum 1 digit, maximum 2 digits
---

Apr
---
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
---

"""

print("#"*40, end="\n\n")
# ###############################
print("Extract IP, DATE, PICS: PARTIAL OUTPUT-1")
print("complete image name is not coming")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(\w+\.(jpg|gif)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)

# COMMENT
"""
[0-9a-zA-Z_] -> \w
[^0-9a-zA-Z_] -> \W # ^ ->Excluding characters in this list

"""

print("#"*40, end="\n\n")
# ###############################

print("Extract IP, DATE, PICS: PARTIAL OUTPUT-2")
print("No Image lines are not coming")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(jpg|gif)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)

# COMMENT
"""
MODIFIERS
------------

GREEDY: Try to get more if possible
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 time

NON-GREEDY: try to give more to others
*? -> 0 or more times
+? -> 1 or more times
?? -> 0 or 1 time

------------

"""

print("#"*40, end="\n\n")
# ###############################


print("THIS IS 100% NOT WORKING")
print("Extract IP, DATE, PICS: PARTIAL OUTPUT-3")
print("Making image pattern optional to consider no images lines as well")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(jpg|gif))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)

# COMMENT
"""
Making 
(\w+\.(jpg|gif))?
optional to match lines which are not having image names 
"""

print("#"*40, end="\n\n")
# ###############################

print("Extract IP, DATE, PICS")
print("We are trying to provide more and more and more information/land-marks")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(jpg|gif)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img)

# COMMENT
"""
\s -> one space
\S -> except space any character
"""

print("#"*40, end="\n\n")
# ###############################
print("Extract IP, DATE, PICS, URL")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(jpg|gif)))?.*(http[s]?://[a-zA-Z_0-9./]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url)

# COMMENT
"""
http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-zA-Z_0-9./]+


http[s]? -> s is optional
https? -> s is optional
(https)? -> extract word 'https' is optional
[https]? -> Any one character in this group of chacters which is optional

[httttttttttttttps]
Matches below characters
h
t
p
s

[0xy4]
Matches below characters
0
x
y
4

"""

print("#"*40, end="\n\n")
# ###############################