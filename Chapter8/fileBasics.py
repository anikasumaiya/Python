
import os

# New path create
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "fun.txt")

# File read and print 
with open(file_path, "r") as file:
    print(file.read())
