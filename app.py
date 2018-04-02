file = open('mensplayers_byname.txt', "r")
outFile = open('MensPros/Italy','w')
for line in file:
    if "Italy" in line:
        #print(line)
        outFile.write(line)