def fileRead():
    with open('what_to_study.txt') as f:
        lines = f.readlines()
        return lines

def fileAppend(text):
    file1 = open("what_to_study.txt", "a")  # append mode
    file1.write(text+'\n')
    file1.close()


def fileDeleteLine(pos):
    # list to store file lines
    lines = []
    # read file
    with open(r"what_to_study.txt", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines() 

# Write file
    with open(r"what_to_study.txt", 'w') as fp:
    # iterate each line
        for number, line in enumerate(lines):
            # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            if number not in [pos]:
                fp.write(line)                     