from MungLang import MungLang

# customize
NAME = "뭉선후"
EXTENSION = "mung"


# function
def getCode(stringList: list):
    result = ""
    for string in stringList: result += string
    return result


f = open(f"./code.{EXTENSION}", "r", encoding="UTF8")
try:
    language = MungLang(NAME)
    code = getCode(f.readlines())
    # print(code)
    language.run(code)
except:
    pass
finally:
    f.close()