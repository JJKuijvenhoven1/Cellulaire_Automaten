class cellulair_automata():
    def __init__(self, dimensions, startgrid, listofneighbours):
        self.dimensions     = dimensions
        self.grid           = startgrid
        self.lisofneighbours = listofneighbours
        return
    
    def regels(self):
        print('this is an ordinary celluair automaton')
        return
    
    def evolueer(self):
        self.regels()
        return
    
    
class game_of_life(cellulair_automata):
    def __init__(self,startgrid):
        self.dimensions     = 2
        self.grid           = startgrid
        self.lisofneighbours = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,-1]]
        return
    def regels(self):
        print('this is the game of life')
        
        

x = game_of_life(None)
x.evolueer()
y = cellulair_automata(None,None,None)
y.evolueer()  