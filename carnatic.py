# to input pattern, 1 denotes first note of scale, 2 denotes 2nd note, etc
# 0 denotes "","

class Carnatic:

    def __init__(self, aro, avaro, tha):
        self.aro = aro
        self.avaro = avaro
        self.thaalam = tha
        self.printThaalam(tha)

    def test(self):
        print(self.aro)
        print(self.avaro)
    
    def ascending(self, pattern):
        for i in range(5):
            for j in range(len(pattern)):
                if pattern[j] == 0: #comma
                    print(",", end = " ")
                    continue

                print(self.aro[i + (pattern[j] - 1)], end = " ")
            print("||\n")  
            
    
    def descending(self, pattern):
        print("---")
        for i in range(5):
            for j in range(len(pattern)):
                if pattern[j] == 0: #comma
                    print(", ", end = " ")
                    continue

                print(self.avaro[i + (pattern[j] - 1)], end = " ")
            print("||\n")  

    def scale(self, pattern):
        self.ascending(pattern)
        self.descending(pattern)

    def printThaalam(self, thaalam):
        thaalamList = {
            "0": None,
            "1": [1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4], #chaturasrajaati dhruva thaalam
            "2": [1, 2, 3, 2, 1, 2, 1, 2, 3, 4], #chathurasra jaati matya thaalam
            "3": [1, 2, 1, 2, 3, 4],
            "4": [1, 2, 3, 1, 2, 1, 2, 3, 4, 0],
            "5": [1, 2, 3, 1, 2, 3, 4],
            "6": [1, 2, 0, 3, 0, 1, 0, 2, 3, 0, 4, 0, 4, 0],
            "7": [1, 2, 3, 4],
            "8": [1, 0, 2, 0, 3, 0, 4, 5, 6]
        }

        self.scale(thaalamList[thaalam])

    def customThaalam(self):
        pattern = input("\ninput thaalam pattern (e.g. 1 2 3 1 2 1 2 3 4)\t").split()
        self.scale(pattern)
    

#assumption that avarohanam is reverse of arohanam
arohanam = input("\n\n\n----\ninput arohanam (e.g. S R G M P D N S)\t").split()
avarohanam = arohanam[::-1]
print(avarohanam)
thaalam = input('\ninput thaalam number (e.g. 4)\t')
carnatic = Carnatic(arohanam, avarohanam, tha=thaalam)
