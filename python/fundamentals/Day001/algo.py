def removeBlanks(str_input):
    newStr = ""
    for i in range (len(str_input)):
        if not str_input[i] == ' ':
            newStr += str_input[i]

    return newStr
result = removeBlanks("Today is Monday")
print(result)