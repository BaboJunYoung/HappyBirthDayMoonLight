from MoonLang import MoonLang

# customize
NAME = "뭉선후"


# function
def getCode(stringList: list):
    result = ""
    for string in stringList: result += string
    return result


f = open("./code.txt", "r", encoding="UTF8")
try:
    language = MoonLang(NAME)
    code = getCode(f.readlines())
    # print(code)
    language.run(code)
except:
    pass
finally:
    f.close()