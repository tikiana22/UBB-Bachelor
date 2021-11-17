from Grammar import Grammar


class UI:

    def __init__(self):
        self.grammar = None

    def readGrammar(self):
        self.grammar = Grammar.fromFile('g1.txt')
        print("Done")

    def printNonTerminals(self):
        print(self.grammar.N)

    def printTerminals(self):
        print(self.grammar.E)

    def printProductions(self):
        print(self.grammar.P)


    def printProductionsForNonTerminal(self):
        print(">>Nonterminal:")
        nonterm = input()
        print(self.grammar.getProductionsFor(nonterm))
    
    def checkCFG(self):
        pass
 

    def __displayMenu(self):
        print("1.Read Grammar")
        print("2.Print nonterminals")
        print("3.Print terminals")
        print("4.Print productions")
        print("5.Print productions for a given nonterminal")
        print("6.Check CFG")

    def run(self):
        cmds = {'1':self.readGrammar,'2':self.printNonTerminals,'3':self.printTerminals,'4':self.printProductions,
                '5':self.printProductionsForNonTerminal,'6':self.checkCFG}

        exit = False
        while not exit:
            self.__displayMenu()
            print(">>")
            cmd = input()
            if cmd in cmds.keys():
                cmds[cmd]()
            elif cmd=="exit":
                exit = True
            else:
                continue