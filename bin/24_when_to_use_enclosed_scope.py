"""
When to use enclosed scope variable
"""

# Requirement: find total_no_of_logs_processed
# total_no_of_logs_processed = total_txt_log_file_processed + total_csv_log_file_processed

print("Using GLOBAL variable")
print("-"*20)
# -----------

total_no_of_logs_processed = 0

def txt_log_process_function():
    global total_no_of_logs_processed
    total_no_of_logs_processed = total_no_of_logs_processed + 1

def csv_log_process_function():
    global total_no_of_logs_processed
    total_no_of_logs_processed = total_no_of_logs_processed + 1

txt_log_process_function()
txt_log_process_function()
csv_log_process_function()
csv_log_process_function()

print("total_no_of_logs_processed:", total_no_of_logs_processed)

print("#"*40, end="\n\n")
# ###############################
print("Using ENCLOSED variable")
print("-"*20)
# -----------

def log_process_functions():

    total_no_of_logs_processed = 0

    def txt_log_process_function():
        nonlocal total_no_of_logs_processed
        total_no_of_logs_processed = total_no_of_logs_processed + 1

    def csv_log_process_function():
        nonlocal total_no_of_logs_processed
        total_no_of_logs_processed = total_no_of_logs_processed + 1

    def get_total_count():
        return total_no_of_logs_processed

    return [txt_log_process_function, csv_log_process_function, get_total_count]


received_data = log_process_functions()
# received_data = [txt_log_process_function, csv_log_process_function, get_total_count]
received_data[0]()
received_data[0]()
received_data[1]()
received_data[1]()

count = received_data[2]()
print("Count:", count)

print("#"*40, end="\n\n")
# ###############################