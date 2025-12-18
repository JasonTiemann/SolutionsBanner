import re

svg = "./Website Banner.svg" #Target 89

file = open(svg, "r")
while True:
    line = file.readline()
    if not line:
        break
    
    if ("<path" in line):
        match = re.search(r" d=\"([^\"]*)Z\"", line)
        if (match):
            path = match.group(1)
            length = path.count(' ') + 1
            print(line[:35])
            print(length)
        else:
            print(line)
    else:
        print(line)