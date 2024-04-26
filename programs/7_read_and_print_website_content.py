"""
Read and print website data
https://www.jafsoft.com/searchengines/log_sample.html
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