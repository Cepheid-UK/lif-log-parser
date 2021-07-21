import re
import csv

with open('input.log', 'r') as log:
    lines = log.readlines()

    hit = []
    tookHit = []

    for line in lines:
        
        regExp1 = re.compile("(have hit)")
        if (regExp1.search(line)):
            regExp3 = re.compile("(?<=\>)(\d*[0-9][.]\d*[0-9])")
            if (regExp3.search(line)):
                hit.append(re.search(regExp3,line).group())
        
        regExp2 = re.compile("(has hit)")
        if (regExp2.search(line)):
            regExp3 = re.compile("(?<=\>)(\d*[0-9][.]\d*[0-9])")
            if (regExp3.search(line)):
                tookHit.append(re.search(regExp3,line).group())
    
    with open("output.csv", "w", encoding="UTF8", newline="") as outputFile:
        writer = csv.writer(outputFile)
        
        totalHit = 0
        totalTookHit = 0
        
        for value in hit:
            totalHit += float(value)
        for value in tookHit:
            totalTookHit += float(value)
        
        writer.writerow([hit])
        writer.writerow([str(totalHit)])
        
        writer.writerow([tookHit])
        writer.writerow([str(totalTookHit)])

# to create exe:
# http://www.pyinstaller.org/