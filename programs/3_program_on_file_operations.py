"""
Get data from sample_data.txt, extract
IP
DATE
PICS
URL
and write extracted info to log_report.txt

Expected Output in log_report.txt:
-----------------
    IP                  DATE            PICS                    URL
123.123.123.123     26/Apr/2000     wpaper.gif          http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image            http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     5star2000.gif       http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif           http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.jpg         http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image            http://www.jafsoft.com/asctortf/
-----------------
"""
"""
Get data from sample_data.txt, extract
IP
DATE
PICS
URL
and write extracted info to log_report.txt

Expected Output in log_report.txt:
-----------------
    IP                  DATE            PICS                    URL
123.123.123.123     26/Apr/2000     wpaper.gif          http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image            http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     5star2000.gif       http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif           http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.jpg         http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image            http://www.jafsoft.com/asctortf/
-----------------
"""

print("Get data from sample_data.txt")
print("-"*20)
# -----------

my_log_file_handle = open(r"../log/sample_data.txt", "r")
log_file_content = my_log_file_handle.readlines()
print(log_file_content)

print("#"*40, end="\n\n")
# ###############################