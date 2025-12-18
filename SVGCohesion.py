import re

svgs = [
    "Solutions Banner.svg",
    "Website Banner.svg",
    # "Automation Banner.svg",
    # "Custom Banner.svg",
    # "SEO Banner.svg",
    # "Gamification Banner.svg"
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
            match = re.search(r"<path d=\"([^\"]*)\"", line)
            if (match):
                path = match.group(1)
                fileReplacements[svg].append(path)
                length = path.count(' ') + 1
                if (length > longestPath):
                    longestPath = length
                    longestPathSVG = line
                    
print(longestPath)

for svg in svgs:
    file = open(svg, "r")
    fileText = file.read()
    file.close()
    for replacement in fileReplacements[svg]:
        if (replacement.count(',') + 1 == longestPath):
            continue
        originalPath = replacement
        firstNeutralNode = re.search(" (.+ )", replacement).group(1)
        insertLocation = replacement.index(firstNeutralNode)
        while replacement.count(',') + 1 < longestPath:
            replacement = replacement[:insertLocation] + firstNeutralNode + replacement[insertLocation:]
        fileText = fileText.replace(originalPath, replacement)

    file = open(svg, "w")
    file.write(fileText)
    file.close()
    