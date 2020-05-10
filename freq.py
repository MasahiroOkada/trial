import sys
import collections

args = sys.argv
#There is not a path of the file
if len(args) == 1:
    print("need a path")
    sys.exit(1)
    
filepath = args[1]

fp = open(filepath, 'r', encoding="latin-1")
context = fp.read()
context_list = context.split('\n')
context_dict = collections.Counter(context_list)
context_dict_sorted = sorted(context_dict.items(), key=lambda x:x[1])

if len(context_dict_sorted) > 10:
    max_range = 11
else:
    max_range = len(context_dict_sorted) + 1

for x in range(1,max_range):
    print(" "*3 + str(context_dict_sorted[-x][1]) + " " + str(context_dict_sorted[-x][0]))