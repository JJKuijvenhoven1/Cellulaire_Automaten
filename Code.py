class cellulair_automata():
    def __init__(self):
        #Deze variablen staan nu op de standaardwaarden zodat het 
        #programma geen errors geeft maar kunnen bij de subclasses 
        #ingevoerd worden op wat ze moeten zijn.
        self.dimensions     = 1
        self.grid           = [0]
        self.lisofneighbours = [0]
        
    
    def regels(self,coordinaten):
        #Deze functie bestaat puur en alleen om door de child objecten overschreven te worden.
        print('this is the base celluair automaton')
        nieuwetoestand = 0
        return nieuwetoestand #we returnen de nieuwe toestand van het inputvakje
        
    
    def evolueer_cel(coord_tuple, regels, grid, nieuwe_generatie):
    nieuwe_generatie[coord_tuple] = 1

    def evolueer(d, n, regels, grid):
        nieuwe_generatie = np.zeros(shape=[n]*d)
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
            evolueer_cel(coord_tuple, regels, grid, nieuwe_generatie)
        return nieuwe_generatie
        
    
#------------------------------------------------------------------------------    
    
    
class game_of_life(cellulair_automata):
    def __init__(self,startgrid):
        self.dimensions     = 2
        self.grid           = startgrid
        self.lisofneighbours = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,-1]]
        return
    def regels(self,coordinaten):
        print('this is the game of life')
        nieuwetoestand = 0
        return nieuwetoestand
        
#-----------------------------------------------------------------------------    
#testcode om het verschil tussen de automata te laten zien
x = game_of_life([[0]])
x.evolueer()
y = cellulair_automata()
y.evolueer()  
