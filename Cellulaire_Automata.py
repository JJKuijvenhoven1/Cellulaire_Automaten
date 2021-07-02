import numpy as np #numpy wordt gebruikt voor arrays
import matplotlib as mpl #matplotlib wordt gebruikt voor het visualiseren
import time #time wordt gebruikt om tijd tussen de generaties te maken

#al deze dingen zijn voor de UI 
mpl.use('TKagg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as Tk


#dit is de standaard klasse waarvan alle CA's afgeleid zullen zijn.
class cellulair_automaton():
    def __init__(self,dimensions,startgrid,randvoorwaarden,burenlijst,toestanden,regelcode):
        
        #de randvoorwaarden codatie is: -2 voor neumann, -1 voor periodiek en 0123... enz zijn voor de hele rand die toestand
        #sla alle relevante variablen op
        self.dimensions = dimensions
        self.gridlength = len(startgrid) #dit is later nodig
        self.grid = startgrid
        self.randvoorwaarden = randvoorwaarden
        self.burenlijst = burenlijst
        self.regelcode = regelcode
        self.toestanden = toestanden
        
        #visualisatie init
        #ik weet ook niet precies hoe, maar het werkt
        if dimensions in [1,2]:
            self.visual = Tk.Tk()
            self.visual.title('visualisatie')    
                
               
            self.scale = plt.Normalize(-1,self.toestanden[-1],False)
            
            fig = plt.figure()
            plt.axis('off')
            fig.canvas.manager.set_window_title('startpositie')
    
            self.canvas = FigureCanvasTkAgg(fig, master=self.visual)
            self.visualiseer()
            self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
            
        

    def evolueer(self, iterations=1):
        d = self.dimensions
        n = self.gridlength
        for i in range(iterations): #voor als we meerdere generaties in een keer willen doen
            nieuwe_grid = np.empty(shape=[n] * d) #maak een empty grid in de vorm van self.grid
            #deze code loopt langs elke cel in het grid en vult het lege grid met de evolueer_cel van het echte grid
            grid_met_index = np.nditer(self.grid, flags=["multi_index"])
            for x in grid_met_index:
                nieuwe_grid[grid_met_index.multi_index] = self.evolueer_cel(list(grid_met_index.multi_index))

            #update
            self.grid = nieuwe_grid
    
    def evolueer_cel(self, coords):
        mycell = int(self.grid[tuple(coords)]) 
        buurtoestanden = self.buurtoestanden_en_randvoorwaarden(coords) #dit is voor alle ca gelijk
        return self.regels_toepassen(buurtoestanden, mycell) #dit wordt overschreven door de child klassen
    
    def buurtoestanden_en_randvoorwaarden(self, coords):
        #hier bepalen wat de toetstanden van onze buren zijn
        buurtoestanden = []
        for buurcoords in self.burenlijst:
            #special case ranvoorwaarden == periodiek
            if self.randvoorwaarden == -1:
                #oke de tactiek is om uit te rekenen waar het bijbehorende periodieke vakje is
                #dus alleen de coordinaat waarmee je over de rand gaat moet naar de andere kant loopen
                cirkelcoords = [0]*self.dimensions
                for i in range(len(buurcoords)):
                    cirkelcoords[i] = (coords[i]+buurcoords[i])%self.gridlength #modulo zorgt ervoor dat je altijd binnen het grid blijft
                buurtoestanden.append(int(self.grid[tuple(np.array(cirkelcoords))])) #voeg de toestand toe
            #end specialcase    
            #normalcase    
            else:
                #reset randvoorwaarde
                isoutofrange = False #dit is om te checken of we van de buurtoestanden gebruik hebben gemaakt
                #we checken eerst of de coords wel binnen het grid vallen
                for i in range(len(buurcoords)):
                    #we doen het voor elke individuele coordinaat
                    if (buurcoords[i]+coords[i]) >= self.gridlength or (buurcoords[i]+coords[i])<= -1:
                        #dit betekent dat de ranvoorwaarden in werking gaan
                        isoutofrange = True #niet meer de normale dingen doen
                        for toestand in self.toestanden: #dit codeert voor randvoorwaarden 0123... enz
                            if self.randvoorwaarden == toestand: 
                                buurtoestanden.append(toestand)
                                break #als een coordinaat outofrange is dan hoeven we de rest niet te checken
                            elif self.randvoorwaarden == -2: #dit codeert Neuman: de randen zijn jou waarde
                                buurtoestanden.append(self.grid[tuple(np.array(coords))])
                                break
                
                if not isoutofrange: #als geen randvoorwaarde dan normale manier
                    buurtoestanden.append(int(self.grid[tuple(np.array(buurcoords) + np.array(coords))]))
            #end normalcase
        #end for loop
        return buurtoestanden

    def regels_toepassen(self,buurtoestanden,mycell):
        #deze bestaat om overschreven te worden.
        return 1
    
    def visualiseer(self):
        '''we onderscheiden hier drie gevallen: 1 dimensie, 2 dimensies en meer dan twee dimensies.
        de visualisatie code in __init__ regelt de meeste dingen we hoeven hier alleen im naar de 
        nieuwe waarde te zetten en canvas.draw aan te roepen. 
        parameters: self
        return: void'''
        
        
        if self.dimensions == 1:
            visual_grid = np.reshape(self.grid, (1,self.gridlength))
            
            self.im = plt.imshow(visual_grid, norm=self.scale)
            self.canvas.draw()
            
        elif self.dimensions == 2:
            
            self.im = plt.imshow(self.grid, norm=self.scale)
            self.canvas.draw()
            
        else:
            print(self.grid)
            print('---------------------')

        
    def evolueer_en_visualiseer(self, iterations=1,timeperframe=0.5, showevery=1):
        '''deze code alterneert tussen visualiseren en volueren zodat je makkelijk de evoluties
        kan weergeven
        parameters: iterations(hoe vaak), timeperframe, showevery(dit kan gebruikt worden om frames te skippen voor snelheid)'''
        self.visualiseer()
        
        for i in range(iterations):
            
            self.evolueer()
            time.sleep(timeperframe)
            if i%showevery == 0:
                self.visualiseer()
            

# ------------------------------------------------------------------------------
class symmetrische_CA(cellulair_automaton):
            
    def regels_toepassen(self, buurtoestanden, mycell):
        '''dit is de symmetrische versie van regels toepassen. we tellen per toestand hoeveel van
        onze buren zich in die toestand bevinden. Dit vullen we samen met onze eigen toestand in 
        de regelmatrix in om zo de nieuwe toestand te krijgen.
        parameters: buurtoestanden(een geordende lijst met daarin de toestanden van de buren), mycell(de toestand van de cell)
        return: nieuwe toestand van de cel'''
        hoeveelvandezetoestand = []
        for toestand in self.toestanden:
            hoeveelvandezetoestand.append(0)
        
        for buur_t in buurtoestanden:
            for t in self.toestanden:
                if buur_t == t:
                    hoeveelvandezetoestand[t]+= 1
        #invullen in codering
        hoeveelvandezetoestand.pop(0)
        codepos = tuple(hoeveelvandezetoestand + [mycell])
        return int(self.regelcode[codepos])
        
       

class game_of_life(symmetrische_CA):
    def __init__(self,startgrid,randvoorwaarden):
        '''deze klasse is enkel en alleen een set standaardwaarden. Deze standaardwaarden
        maken John conways game of life.'''
        dimensions = 2
        burenlijst = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
        toestanden = [0,1]
        regelcode = np.array([[0,0],[0,0],[0,1],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0]])
        super(game_of_life,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)
        
class simpele_hoger_dimensionaale_CA(symmetrische_CA):
    def __init__(self, dimensions):
        '''deze klasse is enkel en alleen een set standaardwaarden. Deze standaardwaarden
        maken een lengte drie in elke dimensie grid en vullen dat langzaam op door
        elke cel die met een vlak grenst aan een levende cel levend te maken.'''
        #maak een startgrid dat alleen maar nullen bevat behalve een 1 in het midden
        startgrid = 0
        for n in range(dimensions):
            startgrid =[startgrid,startgrid,startgrid]
        startgrid = np.array(startgrid)
        startgrid[tuple([1]*dimensions)] = 1       
        randvoorwaarden = 0
        #geautomatiseerde manier om de burenlijst op te stellen
        burenlijst = []
        for n in range(dimensions):
            buurpos = [0]*dimensions
            buurneg = [0]*dimensions
            buurpos[n] = 1
            buurneg[n] = -1    
            burenlijst += [buurpos,buurneg]
        toestanden = [0,1]
        regelcode = np.array([[0,1]] + [[1,1]]*len(burenlijst))

        
        super(simpele_hoger_dimensionaale_CA,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)

#------------------------------------------------------------------------------


class onsymmetrische_CA(cellulair_automaton):
    
    def regels_toepassen(self, buurtoestanden, mycell):
        '''Dit is de regels toepassen functie voor onsymmetrische CA"s. '''
        totaletoestand = 0
        for i in range(len(buurtoestanden)):
            totaletoestand += buurtoestanden[i]*(len(self.toestanden))**i
        return self.regelcode[totaletoestand]
    
    def regelconverter(self, integer):
        output = [0]*(len(self.toestanden)**len(self.burenlijst))
        binary = str(bin(integer))
        binary = binary[2:]
        for i in range(len(binary)):
            output[i]=int(binary[-i-1])
        return output

    
class customregel(onsymmetrische_CA):
    def __init__(self,startgrid,randvoorwaarden,regelcode):
        dimensions = 1
        burenlijst = [[1],[0],[-1]]
        toestanden = [0,1]
        super(customregel,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)
        self.regelcode = self.regelconverter(self.regelcode)
        

class regel30(onsymmetrische_CA):
    def __init__(self,startgrid,randvoorwaarden,UI=False,root=None):
        dimensions = 1
        burenlijst = [[1],[0],[-1]]
        toestanden = [0,1]
        regelcode = [0,1,1,1,1,0,0,0]
        super(regel30,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)



        















