import re

svgs = [
    "Solutions Banner.svg",
    "Websites Banner.svg",
    "Automation Banner.svg",
    "Custom Banner.svg",
    "SEO Banner.svg",
    "Gamification Banner.svg"
]

longestPath = 0
longestPathSVG = ""
fileReplacements = {}

for svg in svgs:
    file = open(svg, "r")
    fileReplacements[svg] = []
    while True:
        line = file.readline()
        if not line:
            break
        
        if ("<path" in line):
            match = re.search(r"<path d=\"([^\"]*)\"", line, re.IGNORECASE)
            if (match):
                path = match.group(1)
                fileReplacements[svg].append(path)
                length = path.count(",") + 1
                print(length)
                if (length > longestPath):
                    longestPath = length
                    longestPathSVG = line
                    
print(longestPath)

for svg in svgs:
    file = open(svg, "r")
    fileText = file.read()
    for replacement in fileReplacements[svg]:
        originalPath = replacement
        pathSplit = replacement.split(',')
        pathEnd = pathSplit[-1]
        pathSplit = pathSplit[:-1]
        while len(pathSplit) < longestPath:
            pathSplit.append(pathSplit[-1])
        lengthenedPath = ','.join(pathSplit) + ',' + pathEnd
        fileText = fileText.replace(originalPath, lengthenedPath)
    file.close()

    file = open(svg, "w")
    file.write(fileText)
    file.close()
    