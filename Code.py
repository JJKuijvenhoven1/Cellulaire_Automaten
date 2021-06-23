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
               
    
    def evolueer_cel(self, coord_tuple):
        #Deze functie bestaat puur en alleen om door de child objecten overschreven te worden.
        nieuwe_toestand = 1
        return nieuwe_toestand

    def evolueer(self, iterations=1):
        d = self.dimensions
        n = self.gridlength
        nieuwe_grid = np.zeros(shape=[n]*d)
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
            coord_tuple = tuple(coord_lijst)
            nieuwe_grid[coord_tuple] = self.evolueer_cel(coord_tuple)
        
        self.grid = nieuwe_grid
    
#------------------------------------------------------------------------------ 
       
class regel_30(cellulair_automata):
    def __init__(self, startgrid):
        #dit is een 1d CA ookwel regel 30 genoemnd
        self.dimensions = 1
        self.gridlength = len(startgrid)
        self.grid = np.zeros(shape=[self.gridlength]*self.dimensions)
        self.regel = '00011110'
        
    def evolueer_cel(self, coordtuple):
        nieuwe_toestand = 0
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
x.evolueer()  
y = regel_30('10010101010101')
print(y.grid)
y.evolueer()