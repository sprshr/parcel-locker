class Input:
    @classmethod
    def numeric(cls, errorMessage, minDigit = None, maxDigit = None):
        while True:
            try:
                value = int(input())
            except ValueError or TypeError:
                print(errorMessage)
                continue
            if minDigit != None and len(str(value)) < minDigit:
                print(errorMessage)
                continue
            elif maxDigit != None and len(str(value)) > maxDigit:
                print(errorMessage)
                continue
            else:
                return value

    @classmethod
    def text(cls, errorMessage:str):
        while True: 
            value = input()
            if len(value) <= 0:
                print(errorMessage)
            else: return value