class MungLang():
    def __init__(self, name="뭉선후"):
        if len(name) < 3: raise Exception("아 이건 이름이 될 수 없음")

        self.name = name[:3]
        self.lastName = name[0]
        self.firstName = name[1:]

        self.tokens = []
        self.tapes = [0]
        self.header = 0
        self.readingPosition = 0
        self.holding = 0

        self.inputQueue = []

        print(f"{self.name}, 생일축하해!")
        
    def run(self, code: str):
        self.tokens = code.replace("\n", " ").split(" ")

        while (self.readingPosition < len(self.tokens)):
            token = self.tokens[self.readingPosition]

            # 포인터 오른쪽으로 이동
            if token == f"{self.name}생일축하해": 
                # self.readingPosition += 1
                self.__movePointerRight()
            
            elif token == f"{self.name}생일축하":
                # self.readingPosition += 1
                self.__movePointerLeft()
            
            elif token == f"{self.name}생일축":
                self.holding = self.tapes[self.header]
            
            elif token == f"{self.name}생일":
                self.tapes[self.header] += self.holding
                self.holding = 0
            
            elif token == f"{self.name}생":
                print(chr(self.tapes[self.header]), end="")
            
            # 뭉선후
            elif token == f"{self.name}":
                while self.tokens[self.readingPosition] != "바보": self.readingPosition -= 1
                # self.readingPosition += 1

            # 뭉선
            elif token == f"{self.name[:2]}":
                if self.tapes[self.header] != 0: self.readingPosition += 1
            
            # 뭉
            elif token == f"{self.name[:1]}":
                self.readingPosition += 1
                self.holding = self.__calculate()

            elif token in ["따삐에"]: break

            elif token == "여기부터->": 
                while "<-여기까지주석임" not in self.tokens[self.readingPosition]: self.readingPosition += 1
                self.readingPosition += 1
            
            elif token == "이것좀들어줘":
                data = ord(input()[0])
                self.holding = data

            elif token in ["", "바보"]: pass

            else: print(f"{self.tokens[self.readingPosition]}..? 이해못해서 넘길게용 힛", end="")

            self.readingPosition += 1
        print("\n뭉선후, 내년 생일도 축하해!")
        

    def __calculate(self):
        code = self.tokens[self.readingPosition]

        if "선후르" not in code: raise Exception("아 이거 숫자 아님")
        
        number = 0

        number += code.count("뭉")
        number -= code.count("옴")
        
        if "!" in code:
            self.readingPosition += 1
            
            return number * self.__calculate()

        
        return number
    
    def __movePointerRight(self, number: int = 1):
        for i in range((self.header + 1) + number - len(self.tapes)):
            self.tapes.append(0)
        self.header += number
    
    def __movePointerLeft(self, number: int = 1):
        
        self.header = self.header - number
        if self.header < 0: raise Exception("왼쪽으로 넘어감 뿌엑")
