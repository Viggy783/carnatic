class Carnatic:

    def __init__(self, aro, avaro):
        self.aro = aro
        self.avaro = avaro

    def test(self):
        print(self.aro)
        print(self.avaro)
    
    def ascending(self, pattern):
        for i in range(5):
            for j in range(len(pattern)):
                print(self.aro[i + (pattern[j] - 1)], end = " ")
            print("||\n")  
    
    def descending(self, pattern):
        for i in range(5):
            for j in range(len(pattern)):
                print(self.avaro[i + (pattern[j] - 1)], end = " ")
            print("||\n")

    def scale(self, pattern):
        self.ascending(pattern)
        self.descending(pattern)

    def thaalam4(self): #misra jaathi jhumpa thaalam
        pattern = [1, 2, 3, 1, 2, 1, 2, 3, 4]
        self.scale(pattern)  
        
    

#assumption that avarohanam is reverse of arohanam
arohanam = input("\n\n\n----\ninput arohanam (e.g. S R G M P D N S)\t").split()
avarohanam = arohanam[::-1]

carnatic = Carnatic(arohanam, avarohanam)
carnatic.thaalam4()
