"""
About Virtual Environment
"""

# About Python Installation:
# OPTION-1:
# -----------------
# We can install multiple versions of python in one computer
        # In pycharm
            # -> settings->python-interpreter, we can select which version we want
        # In Command Line:
            # Similarly, if we want to execute program in command line then there also
            # we can select which python we want to use?
            # Example:
            #   c:\>c:\python312\python.exe test.py
            #   c:\>c:\python310\python.exe test.py
#####################################
# OPTION-2:
# Suppose i need to use
# c:\python312\
# for
# project-1, project-2
# -----------------
# We can install libraries/packages related project-1, project-2
# to same installation directory i.e c:\python312\
#####################################
# OPTION-3:
# Suppose i need to use
# c:\python312\
# for
# project-1, project-2
# -----------------
# project-1: We can create virtual environment for project-1,
#               install required libraries for project-1,
#               and use virtual environment-1 for project-1
#
# project-2: We can create another virtual environment for project-2,
#               install required libraries for project-2,
#               and use virtual environment-2 for project-2
#####################################
# How to create virtual environment?
# and
# How to use virtual environment?
# -----------------
# OPTION-1: Using pycharm
#       -> Settings -> python-interpreter -> create new virtual environment
# OPTION-2: Using command line
#       -> python -m venv myvenv2
#####################################