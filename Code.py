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
        
    
    def evolueer(self):
        #deze functie wordt door alle subclasses gebruikt en looped door elke entry
        #van het grid en voert op dat vakje de functie regels uit
        self.regels([0])
        
    
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