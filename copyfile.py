'''
A simple script for copying file from working directory to git folder for pushing.
'''

import shutil

original = r'C:\Users\kke99\Desktop\python\copyfile.py'
target = r'c:\Users\kke99\python\copyfile.py'
shutil.copyfile(original, target)
