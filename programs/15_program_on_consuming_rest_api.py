# pip install requests

"""
Access API using 'requests' library
"""

print("Access API using 'requests' library")
print("-"*20)
# ----------------

import requests

try:
    api_response = requests.get("http://127.0.0.1:5000/getlogdata")
    api_data = api_response.json()
    print(api_data)
except:
    print("""
    Not able to access API. 
    Please make sure to run 14_program_on_rest_api.py
    """)
    exit()  # Terminate the program

print("#"*40, end="\n\n")
######################################

print("Dummy weather report")
print("-"*20)
# ----------------

import requests

try:
    api_response = requests.get("https://demoqa.com/utilities/weather/city/bangalore")
    api_data = api_response.json()
    print(api_data)
except:
    print("""
    Currently not able to access weather API
    """)


print("#"*40, end="\n\n")
######################################