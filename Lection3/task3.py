import json

def parseJsonFile(jsonFile):
    jsonString = ""
    with open(jsonFile, 'r') as file:
        for line in file.readlines():
            jsonString += line

    return json.loads(jsonString)


def extractKeys(dictInfo, dictKeysArray = []):

    for key, value in dictInfo.items():
        dictKeysArray.append(key)
        if type(value) == dict:
            extractKeys(value, dictKeysArray)

    return dictKeysArray


def searchByUserRequest(userRequest, dataToSearch, pathToKey = ""):

    for key, value in dataToSearch.items():
        if key == userRequest:
            pathToKey += " -> " + key
            print("{}: {}".format(pathToKey, value))
        elif type(value) == dict:
            searchByUserRequest(userRequest, value, pathToKey + " -> " + key if len(pathToKey) > 1 else pathToKey + key)


def main():

    jsonData = parseJsonFile('json.txt')
    
    print("Available keys in json: \n" + str(extractKeys(jsonData)))

    userRequest = input("Enter a request to search for information in a file (case sensitive): ")

    print("Your request is not in available keys!") if userRequest not in extractKeys(jsonData) else searchByUserRequest(userRequest, jsonData)

main()