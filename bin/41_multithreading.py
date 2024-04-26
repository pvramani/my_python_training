"""
multithreading: We can split ONE-PROCESS into multiple pieces called THREADS
and run in PARALLEL so that we can increase SPEED of execution

In python multithreading is NOT-PARALLEL
then
what is the use of multithreading in python?

use of multithreading in python
- if one thread is waiting for some resource then
during that waiting time, another thread will get executed.
so this waiting time we can utilize
"""

print("WITHOUT using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()

def squares_function(my_list):
    for i in my_list:
        print("Square is:", i*i)


def cubes_function(my_list):
    for i in my_list:
        print("Cube is:", i*i*i)


L = [10, 20, 30, 40]
squares_function(L) # It will wait for function execution to complete
cubes_function(L) # It will wait for function execution to complete

end_time = time.time()

print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
# ###############################
print("Using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()

def squares_function(my_list):
    for i in my_list:
        print("Square is:", i*i)


def cubes_function(my_list):
    for i in my_list:
        print("Cube is:", i*i*i)


L = [10, 20, 30, 40]

from threading import  Thread

t1 = Thread(target=squares_function, args=(L,))
t2 = Thread(target=cubes_function, args=(L,))

t1.start() # It will NOT wait for function execution to complete, It will just call the function & goto next line
t2.start() # It will NOT wait for function execution to complete, It will just call the function & goto next line

# Since we need to find end_time, we need to wait for t1 & t2 to complete the execution
t1.join() # wait here till t1 completes the execution
t2.join() # wait here till t2 completes the execution

end_time = time.time()

print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
# ###############################
print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()

def squares_function(my_list):
    for i in my_list:
        print("Square is:", i*i)
        time.sleep(0.1) # Assume this is waiting for 0.1 sec for some resource


def cubes_function(my_list):
    for i in my_list:
        print("Cube is:", i*i*i)
        time.sleep(0.1)  # Assume this is waiting for 0.1 sec for some resource

L = [10, 20, 30, 40]
squares_function(L) # It will wait for function execution to complete
cubes_function(L) # It will wait for function execution to complete

end_time = time.time()

print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
# ###############################
print("WITH DELAY: Using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()

def squares_function(my_list):
    for i in my_list:
        print("Square is:", i*i)
        time.sleep(0.1)  # Assume this is waiting for 0.1 sec for some resource


def cubes_function(my_list):
    for i in my_list:
        print("Cube is:", i*i*i)
        time.sleep(0.1)  # Assume this is waiting for 0.1 sec for some resource


L = [10, 20, 30, 40]

from threading import  Thread

t1 = Thread(target=squares_function, args=(L,))
t2 = Thread(target=cubes_function, args=(L,))

t1.start() # It will NOT wait for function execution to complete, It will just call the function & goto next line
t2.start() # It will NOT wait for function execution to complete, It will just call the function & goto next line

# Since we need to find end_time, we need to wait for t1 & t2 to complete the execution
t1.join() # wait here till t1 completes the execution
t2.join() # wait here till t2 completes the execution

end_time = time.time()

print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
# ###############################