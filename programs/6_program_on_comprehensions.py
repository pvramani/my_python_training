"""
Using comprehensions
1) extract ip and keep it in ips_list
2) extract date and keep it in dates_list
3) extract pics and keep it in pics_list
4) extract url and keep it in urls_list

create dictionary using above 4 lists
D = {0: [ip,dt,img,url], 1: [ip,dt,img,url],}

write to json file -> comprehension_report.json
"""

print("Get data from sample_data.txt")
print("-"*20)
# -----------

my_log_file_handle = open(r"../log/sample_data.txt", "r")
log_file_content = my_log_file_handle.readlines()
print(log_file_content)
my_log_file_handle.close()

print("#"*40, end="\n\n")
# ###############################


print("ips_list")
print("-"*20)
# -----------

ips_list = [each_line.split()[0] for each_line in log_file_content if each_line.startswith("123")]
print(ips_list)

# for each_line in log_file_content:
#     if each_line.startswith("123"):
#         sp = each_line.split()
#         ip = sp[0]

print("#"*40, end="\n\n")
# ###############################
print("dates_list")
print("-"*20)
# -----------

dates_list = [each_line.split()[3][1:][:each_line.split()[3][1:].index(":")]  for each_line in log_file_content if each_line.startswith("123")]
print(dates_list)

# for each_line in log_file_content:
#     if each_line.startswith("123"):
#         sp = each_line.split()
#         raw_date = sp[3] # each_line.split()[3]
#         raw_date = raw_date[1:] # each_line.split()[3][1:]
#         index_of_colon = raw_date.index(":") # each_line.split()[3][1:].index(":")
#         dt = raw_date[:index_of_colon] # each_line.split()[3][1:][:each_line.split()[3][1:].index(":")]

print("#"*40, end="\n\n")
# ###############################
print("nested if in list comprehensions")
print("-"*20)
# -----------

L = [10, 20, 30, 40]
print("L is:", L)

# add 100 if > 20 else add 200

new_L = [i+100 if i > 20 else i+200 for i in L if i%2 == 0]
print("new_L:", new_L)

print("#"*40, end="\n\n")
# ###############################
print("nested if with list comprehensions and without list comprehension")
print("-"*20)
# -----------

L = [10, 20, 30, 40]
print("L is:", L)

# add 100 if > 20 else add 200

new_L = [i+100 if i > 20 else i+200 for i in L if i%2 == 0]
print("new_L:", new_L)

new_L =[]
for i in L:
    if i%2 ==0:
        if i>20:
            new_L.append(i+100)
        else:
            new_L.append(i+200)

print(new_L)

print("#"*40, end="\n\n")
# ###############################
print("pics_list")
print("-"*20)
# -----------

pics_list = [each_line.split()[6][6:] if each_line.split()[6].startswith("/pics/") else "No Image" for each_line in log_file_content if each_line.startswith("123")]
print(pics_list)

# for each_line in log_file_content:
#     if each_line.startswith("123"):
#         sp = each_line.split()
#         raw_img = sp[6] # each_line.split()[6]
#         if raw_img.startswith("/pics/"): # each_line.split()[6].startswith("/pics/")
#             img = raw_img[6:] # each_line.split()[6][6:]
#         else:
#             img = "No Image"

print("#"*40, end="\n\n")
# ###############################
print("urls_list")
print("-"*20)
# -----------

urls_list = [each_line.split()[10][1:-1] for each_line in log_file_content if each_line.startswith("123")]
print(urls_list)

# for each_line in log_file_content:
#     if each_line.startswith("123"):
#         sp = each_line.split()
#         raw_url = sp[10] # each_line.split()[10]
#         url = raw_url[1:-1] # each_line.split()[10][1:-1]

print("#"*40, end="\n\n")
# ###############################
print("Make pair")
print("-"*20)
# -----------

# ips_list = [ip1, ip2, ip3]
# dates_list = [dt1, dt2, dt3]
# pics_list = [img1, img2, img3]
# urls_list = [url1, url2, url3]

# zip example
# >>> L = [10, 20]
# >>> M = ["A", "B"]
# >>> z = zip(L, M)
# >>> list(z)
# [(10, 'A'), (20, 'B')]
# >>>

zip_object = zip(ips_list, dates_list, pics_list, urls_list)
zip_list = list(zip_object)
print("zip_list:", zip_list)


print("#"*40, end="\n\n")
# ###############################
print("Create dictionary")
print("-"*20)
# -----------

# D = {0: [ip,dt,img,url], 1: [ip,dt,img,url],}

my_dictionary = dict(enumerate(zip_list))
print(my_dictionary)

# Enumerate Example
# >>> L = [(), (), ()]
# >>> M = [(0,()), (1, ()), (2, ())]
# >>> dict(M)
# {0: (), 1: (), 2: ()}
# >>>
# >>> # To make index/value pair, we can use 'enumerate' function
# >>> e = enumerate(L)
# >>> list(e)
# [(0, ()), (1, ()), (2, ())]
# >>> dict(enumerate(L))
# {0: (), 1: (), 2: ()}

print("#"*40, end="\n\n")
# ###############################
print("write to json file -> comprehension_report.json")
print("-"*20)
# -----------

my_file_handle = open("comprehension_report.json", "w")

import json
json.dump(my_dictionary, my_file_handle)

my_file_handle.close()

print("""
Created
comprehension_report.json
please check
""")
print("#"*40, end="\n\n")
# ###############################