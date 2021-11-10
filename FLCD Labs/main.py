from PIF import PIF
from Scanner import *
from SymbolTable import SymbolTable


class Main:

    def __init__(self):
        self.st = SymbolTable(17)
        self.pif = PIF()
        self.scanner = Scanner()

    def run(self):
        readFile()
        fileName = "p1.txt"
        exceptionMessage = ""

        with open(fileName, 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                tokens = self.scanner.tokenize(line.strip())
                extra=''
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords+separators+operators:
                        if tokens[i] == ' ': # ignore adding spaces to the pif
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif tokens[i] in self.scanner.cases and i<len(tokens)-1:
                        if re.match("[1-9]", tokens[i+1]):
                            self.pif.add(tokens[i][:-1], (-1, -1))
                            extra = tokens[i][-1]
                            continue
                        else:
                            exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(lineCounter) + "\n"
                    elif self.scanner.isIdentifier(tokens[i]):
                        id = self.st.add(tokens[i])
                        self.pif.add("id", id)
                    elif self.scanner.isConstant(tokens[i]):
                        const = self.st.add(extra+tokens[i])
                        extra = ''
                        self.pif.add("const", const)
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(lineCounter) + "\n"

        with open('symboltable.out', 'w') as writer:
            writer.write(str(self.st))

        with open('pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exceptionMessage == '':
            print("Lexically correct")
        else:
            print(exceptionMessage)


main = Main()
main.run()