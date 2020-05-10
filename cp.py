import sys
import os

args = sys.argv
#There is not a path of the file
if len(args) == 1 or len(args) == 2:
    print("need input and output paths")
    sys.exit(1)

filepath_in = args[1]
filepath_out = args[2]

#get directory from the output path
pathsp = filepath_out.split('/')
path_file = pathsp.pop(-1)
filepath_out = '/'.join(pathsp)

#if there is not the directory, it is made
os.makedirs(filepath_out, exist_ok=True)

pathsp.append(path_file)
filepath_out = '/'.join(pathsp)

fp_in = open(filepath_in, 'r')
fp_out = open(filepath_out, 'w')

#read and copy the context
for line in fp_in.readlines():
    fp_out.writelines(line)
fp_in.close()
fp_out.close()
