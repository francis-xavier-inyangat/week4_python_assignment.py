import re

parentFile = 'parentFile.txt'
emailList = 'emails.txt'
removeDelimeter = [',', ';']
def checkEmail(emailString):
    # .* Zero or more characters of any type. 
    if re.match("(.*)@(.*).(.*)", emailString):
        return True
    return False
def retrieveEmail(listData):
    file = open(emailList, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(parentFile, 'r') 
readInLines = file.readlines()
for itemLine in readInLines:
    item =str(itemLine)
    for delimeter in removeDelimeter:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(checkEmail(word)):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    retrieveEmail(uniqEmail)
else:
    print("No email found.")