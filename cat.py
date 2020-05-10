import sys

def cat():
    args = sys.argv
    #There is not a path of the file
    if len(args) == 1:
        print("need a path")
        return 1

    filepath = args[1]
    #There is not a path of the file
    if filepath.startswith('-'):
        print("need a path")
        return 1

    #recognize the options(-n)
    options = [options for options in args if options.startswith('-')]

# --number option
    if '-n' in options or '--number' in options:
        return cat_option_n(filepath)
# no option        
    else:
        fp = open(filepath, 'r')
        for line in fp.readlines():
            line = line.replace('\n','')
            print(line)
        fp.close()

    return 0

# --number option
def cat_option_n(filepath):
    fp = open(filepath, 'r')
    line_number = 1
    for line in fp.readlines():
        #line number & line
        line = line.replace("\n","")
        print(str(line_number).rjust(6, ' ')+line)

        line_number = line_number + 1
    fp.close()
    return 0

cat()