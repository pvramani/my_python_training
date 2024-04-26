"""
Write a function which takes one argument i,e log_file_path
and that function should extract info and it should return
extracted info in list of tuples

Finally expectation is
if we call function like

received_value = log_process_function("sample_data.txt")
and if we print received_value then we should data like this

[
(123.123.123.123,     26/Apr/2000,     wpaper.gif,          http://www.jafsoft.com/asctortf/),
(123.123.123.123,     26/Apr/2000,     No Image,            http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF),
(123.123.123.123,     26/Apr/2000,     5star2000.gif,       http://www.jafsoft.com/asctortf/),
(123.123.123.123,     26/Apr/2000,     5star.gif,           http://www.jafsoft.com/asctortf/),
(123.123.123.123,     26/Apr/2000,     a2hlogo.jpg,         http://www.jafsoft.com/asctortf/),
(123.123.123.123,     26/Apr/2000,     No Image,            http://www.jafsoft.com/asctortf/),
]
"""