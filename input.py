class Input:
    @classmethod
    def numeric(cls, errorMessage, minDigit = None, maxDigit = None):
        while True:
            while True:
                try:
                    value = int(input())
                except ValueError or TypeError:
                    print(errorMessage)
                else: break
            if minDigit != None and len(str(value)) < minDigit:
                print(errorMessage)
            elif maxDigit != None and len(str(value)) > maxDigit:
                print(errorMessage)
            else: return value