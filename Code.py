import numpy as np
import math

class cellulair_automata():
    def __init__(self):
        #Deze variablen staan nu op de standaardwaarden zodat het 
        #programma geen errors geeft maar kunnen bij de subclasses 
        #ingevoerd worden op wat ze moeten zijn.
        self.dimensions = 1
        self.gridlength = 1
        self.grid = np.zeros(shape=[self.dimensions]*self.gridlength)
               
    
    def evolueer_cel(self, coord_lijst):
        #Deze functie bestaat puur en alleen om door de child objecten overschreven te worden.
        nieuwe_toestand = 1
        return nieuwe_toestand

    def evolueer(self, iterations=1):
        d = self.dimensions
        n = self.gridlength
        nieuwe_grid = np.zeros(shape=[n]*d)
        nieuwe_grid[(0,)*d] = self.evolueer_cel([0]*d)
        for x in range(1, n**d):
            coord_lijst = []
            lengte_getal = math.floor(math.log(x, n))
            rest = x
            for z in range(lengte_getal + 1):
                quotient = rest // n**(lengte_getal - z)
                coord_lijst.append(quotient)
                rest = rest - quotient * n**(lengte_getal - z)
            while len(coord_lijst) < d:
                coord_lijst.insert(0, 0)
            nieuwe_grid[tuple(coord_lijst)] = self.evolueer_cel(coord_lijst)
        
        self.grid = nieuwe_grid
    
#------------------------------------------------------------------------------ 
       
class regel_30(cellulair_automata):
    def __init__(self, startgrid):
        #dit is een 1d CA ookwel regel 30 genoemnd
        #de randvoorwaarde is rondje
        self.dimensions = 1
        self.gridlength = len(startgrid)+2
        self.grid = -1*np.ones(shape=[self.gridlength]*self.dimensions)
        self.regel = '00011110'
        
        #start invullen
        for i in range(1,self.gridlength-1):
            self.grid[i] = int(startgrid[i-1])
        
    def evolueer_cel(self, coord_lijst):
        midden = self.grid[tuple(coord_lijst)]
        nieuwe_toestand = midden
        
        #skip als rand
        if midden == -1:
            return -1
    
        links = self.grid[tuple([coord_lijst[0]-1])]
        rechts = self.grid[tuple([coord_lijst[0]+1])]
        
        #randvoorwaarden
        if links == -1:
            links = self.grid[-2]
        if rechts == -1:
            rechts = self.grid[1]     
    
        #regels
        binary = str(int(links))+str(int(midden))+str(int(rechts))
        deci = int(binary, 2)
        nieuwe_toestand = int(self.regel[-(deci+1)])

        return nieuwe_toestand
        
        
#------------------------------------------------------------------------------ 
 
class simple_life(cellulair_automata):
    def __init__(self, startgrid, regelint=30, randvoorwaarden=2):
        #dit is een 1d CA ookwel regel 30 genoemnd
        #de randvoorwaarde is rondje
        self.dimensions = 1
        self.gridlength = len(startgrid)+2
        self.grid = -1*np.ones(shape=[self.gridlength]*self.dimensions)
        self.randvoorwaarden = randvoorwaarden
        
        #start invullen
        for i in range(1,self.gridlength-1):
            self.grid[i] = int(startgrid[i-1])
            
        #regelint to binairy
        binary = np.base_repr(regelint, base=2 )
        desiredlength = 8
        pudding = desiredlength - len(binary)
        binary = pudding*'0' + binary
        self.regel = binary
        
    def evolueer_cel(self, coord_lijst):
        midden = self.grid[tuple(coord_lijst)]
        nieuwe_toestand = midden
        
        #skip als rand
        if midden == -1:
            return -1
    
        links = self.grid[tuple([coord_lijst[0]-1])]
        rechts = self.grid[tuple([coord_lijst[0]+1])]
        
        #randvoorwaarden
        if self.randvoorwaarden == 0:
            #rondje
            if links == -1:
                links = self.grid[-2]
            if rechts == -1:
                rechts = self.grid[1]
        elif self.randvoorwaarden == 1:
            #standaard 1
            if links == -1:
                links = 1
            if rechts == -1:
                rechts = 1
        elif self.randvoorwaarden == 2:
            #standaard 0
            if links == -1:
                links = 0
            if rechts == -1:
                rechts = 0
        else:
            print('De randvoorwaarden moet 0, 1 of 2 zijn. fuck u')
             
    
        #regels
        binary = str(int(links))+str(int(midden))+str(int(rechts))
        deci = int(binary, 2)
        nieuwe_toestand = int(self.regel[-(deci+1)])

        return nieuwe_toestand
    
#------------------------------------------------------------------------------  
    
    
# class game_of_life(cellulair_automata):
#     def __init__(self,startgrid):
#         self.dimensions     = 2
#         self.grid           = startgrid
#         self.lisofneighbours = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,-1]]
#         return
#     def regels(self,coordinaten):
#         print('this is the game of life')
#         nieuwetoestand = 0
#         return nieuwetoestand
        
#-----------------------------------------------------------------------------    
#testcode om het verschil tussen de automata te laten zien

x = cellulair_automata() 
y = regel_30('000010000')
z = simple_life('000010000', 204)
for i in range(10):
    z.evolueer()
    print(z.grid)
print('als je evenveel struggled met regels omzetten naar decimaal is hier een handig linkje: https://www.binaryhexconverter.com/binary-to-decimal-converter')


