"""
pip install beautifulsoup4
get data from website and get log data and print
"""

print("Read and print website data")
print("-"*20)
# -----------

import urllib.request as u

my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
# web_content is bytes class
# use decode to convert to string
web_content = web_content.decode()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
# ###############################

print("Create object of Beautifulsoup class")
print("-"*20)
# -----------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
print(soup)

print("#"*40, end="\n\n")
# ###############################


print("log data")
print("-"*20)
# -----------

log_data = soup.body.pre.text

print(log_data, end="\n\n")

print(repr(log_data), end="\n\n")

print(type(log_data), end="\n\n")

print("#"*40, end="\n\n")
# ###############################