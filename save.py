def saveNew(name, score):
    file = open("save.txt", "a")
    file.write(name + " ")
    file.write(str(score) + " ")
    file.close()

def emptyMemory():
    file = open("save.txt", "w")
    file.close()

def getAllScores():
    file = open("save.txt", "r")
    data = file.read()
    data = data.split()
    for i in range(len(data)):
        if i%2 == 1:
            data[i] = int(data[i])

    file.close()
    return data

def getAllScoresSorted():
    data = getAllScores()
    i = 0
    dataTuples = []
    while i < len(data):
        dataTuples.append((data[i], data[i+1]))
        i += 2

    dataTuples.sort(key=lambda tup: tup[1], reverse=True)
    return dataTuples

# emptyMemory()
# saveNew("Audrey", 2800)
# saveNew("Greg", 42)
# saveNew("Adam", 984)
# saveNew("Antoine", 4064)
# saveNew("Manu", 1000000000)
# print(getAllScoresSorted())
# [('Manu', 1000000000), ('Antoine', 4064), ('Audrey', 2800), ('Adam', 984), ('Greg', 42)]
