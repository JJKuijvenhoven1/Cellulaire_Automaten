import numpy as np
import matplotlib.pyplot as plt
import time

#dit is de standaard code waarvan alle CA's afgeleid zullen zijn.
class cellulair_automaton():
    def __init__(self,dimensions,startgrid,randvoorwaarden,burenlijst,toestanden,regelcode):
        
        #de randvoorwaarden codatie is: -1 voor cirkeltje en 0123... enz zijn voor de hele rand die toestand
        #save all relevant variables
        self.dimensions = dimensions
        self.gridlength = len(startgrid)
        self.grid = startgrid
        self.randvoorwaarden = randvoorwaarden
        self.burenlijst = burenlijst
        self.regelcode = regelcode
        self.toestanden = toestanden
   
    def evolueer(self, iterations=1):
        d = self.dimensions
        n = self.gridlength
        for i in range(iterations):
            nieuwe_grid = -2 * np.ones(shape=[n] * d)
            grid_met_index = np.nditer(self.grid, flags=["multi_index"])
            for x in grid_met_index:
                nieuwe_grid[grid_met_index.multi_index] = self.evolueer_cel(list(grid_met_index.multi_index))

            #update
            self.grid = nieuwe_grid
    
    def evolueer_cel(self, coords):
        mycell = int(self.grid[tuple(coords)])
        buurtoestanden = self.buurtoestanden_en_randvoorwaarden(coords)
        return self.regels_toepassen(buurtoestanden, mycell)
    
    def buurtoestanden_en_randvoorwaarden(self, coords):
        #hier bepalen wat de toetstanden van onze buren zijn
        #de randvoorwaarden codatie is: -1 voor cirkeltje en 0123... enz zijn voor de hele rand die toestand 
        buurtoestanden = []
        for buurcoords in self.burenlijst:
            #special case ranvoorwaarden == cirkeltje
            if self.randvoorwaarden == -1:
                #oke de tactiek is om uit te rekenen waar je cirkello.vakje is 
                cirkelcoords = [0]*self.dimensions
                for i in range(len(buurcoords)):
                    cirkelcoords[i] = (coords[i]+buurcoords[i])%self.gridlength
                buurtoestanden.append(int(self.grid[tuple(np.array(cirkelcoords))]))
            #end specialcase    
            #normalcase    
            else:
                #reset randvoorwaarde
                isoutofrange = False
                #we checken eerst of dit wel binnen het grid valt
                for i in range(len(buurcoords)):
                    #we doen het voor elke individuele coordinaat
                    if (buurcoords[i]+coords[i]) >= self.gridlength or (buurcoords[i]+coords[i])<= -1:
                        #dit betekent dat de ranvoorwaarden in werking gaan
                        isoutofrange = True
                        for toestand in self.toestanden:
                            if self.randvoorwaarden == toestand:
                                buurtoestanden.append(toestand)
                                break
                # nu de verandering doorvoeren als we binnen de perken waren
                if not isoutofrange:
                    buurtoestanden.append(int(self.grid[tuple(np.array(buurcoords) + np.array(coords))]))
            #end normalcase
        #end for loop
        return buurtoestanden

    def regels_toepassen(self,buurtoestanden,mycell):
        #deze bestaat om overschreven te worden.
        return 1
    
    def visualiseer(self):
        if self.dimensions == 1:
            
            visual_grid = np.reshape(self.grid, (1,self.gridlength))
            
            plt.axis('off')
            scale = plt.Normalize(-1,1,False)
            plt.imshow(visual_grid, norm=scale)
            plt.show()
        elif self.dimensions == 2:
            plt.axis('off')
            scale = plt.Normalize(-1,1,False)
            plt.imshow(self.grid, norm=scale)
            plt.show()
            
        else:
            print(self.grid)

        
    def evolueer_en_visualiseer(self, iterations=1,timeperframe=0.5, showinbetween=True, showevery=1):
        self.visualiseer()
        
        for i in range(iterations):
            
            self.evolueer()
            time.sleep(timeperframe)
            if showinbetween and i%showevery == 0:
                self.visualiseer()
            

# ------------------------------------------------------------------------------
class symmetrische_CA(cellulair_automaton):
            
    def regels_toepassen(self, buurtoestanden, mycell):
        hoeveelvandezetoestand = []
        for toestand in self.toestanden:
            hoeveelvandezetoestand.append(0)
        
        for buur_t in buurtoestanden:
            for t in self.toestanden:
                if buur_t == t:
                    hoeveelvandezetoestand[t]+= 1
        #codering 
        hoeveelvandezetoestand.pop(0)
        codepos = tuple(hoeveelvandezetoestand + [mycell])
        return int(self.regelcode[codepos])
        
       
#------------------------------------------------------------------------------
class game_of_life(symmetrische_CA):
    def __init__(self,startgrid,randvoorwaarden):
        dimensions = 2
        burenlijst = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
        toestanden = [0,1]
        regelcode = np.array([[0,0],[0,0],[0,1],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0]])
        super(game_of_life,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


class onsymmetrische_CA(cellulair_automaton):
    
    def regels_toepassen(self, buurtoestanden, mycell):
        totaletoestand = 0
        for i in range(len(buurtoestanden)):
            totaletoestand += buurtoestanden[i]*(len(self.toestanden))**i
        return self.regelcode[totaletoestand]

    
#------------------------------------------------------------------------------

class regel30(onsymmetrische_CA):
    def __init__(self,startgrid,randvoorwaarden):
        dimensions = 1
        burenlijst = [[1],[0],[-1]]
        toestanden = [0,1]
        regelcode = [0,1,1,1,1,0,0,0]
        super(regel30,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)
        
#------------------------------------------------------------------------------
glider = np.array([[0,1,0,0,0,0,0,0,0,0],
                 [0,0,1,0,0,0,0,0,0,0],
                 [1,1,1,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 ])
loafer = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   ])
a = game_of_life(glider,-1)
b = game_of_life(loafer, -1)

b.evolueer_en_visualiseer(30)



























# class onsym_1d_CA(onsymmetrische_CA):
#     def __init__(self, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode):
#         dimensions = 1
#         super(onsymmetrische_CA,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)
        
    


#------------------------------------------------------------------------------

# class symm_2d_CA(symmetrische_CA):
#     def __init__(self,startgrid,randvoorwaarden,burenlijst,toestanden,regelcode):
#         dimensions = 2
#         super(symm_2d_CA,self).__init__(dimensions, startgrid, randvoorwaarden, burenlijst, toestanden, regelcode)
    
#     def visualiseer(self):
#         plt.axis('off')
#         scale = plt.Normalize(-1,1,False)
                              
#         # plt.axis('tight')
#         # plt.axis('image')
#         plt.imshow(self.grid, norm=scale)
#         plt.show()
 
# class regel_30(cellulair_automata):
#     def __init__(self, startgrid):
#         # dit is een 1d CA ookwel regel 30 genoemnd
#         # de randvoorwaarde is rondje
#         self.dimensions = 1
#         self.gridlength = len(startgrid) + 2
#         self.grid = -1 * np.ones(shape=[self.gridlength] * self.dimensions)
#         self.regel = '00011110'

#         # start invullen
#         for i in range(1, self.gridlength - 1):
#             self.grid[i] = int(startgrid[i - 1])

#     def evolueer_cel(self, coord_lijst):
#         midden = self.grid[tuple(coord_lijst)]
#         nieuwe_toestand = midden

#         # skip als rand
#         if midden == -1:
#             return -1

#         links = self.grid[tuple([coord_lijst[0] - 1])]
#         rechts = self.grid[tuple([coord_lijst[0] + 1])]

#         # randvoorwaarden
#         if links == -1:
#             links = self.grid[-2]
#         if rechts == -1:
#             rechts = self.grid[1]

#             # regels
#         binary = str(int(links)) + str(int(midden)) + str(int(rechts))
#         deci = int(binary, 2)
#         nieuwe_toestand = int(self.regel[-(deci + 1)])

#         return nieuwe_toestand


# # ------------------------------------------------------------------------------

# class simple_life(cellulair_automata):
#     def __init__(self, startgrid, regelint=30, randvoorwaarden=0):
#         # dit is een 1d CA ookwel regel 30 genoemnd
#         # de randvoorwaarde is rondje
#         self.dimensions = 1
#         self.gridlength = len(startgrid) + 2
#         self.grid = -1 * np.ones(shape=[self.gridlength] * self.dimensions)
#         self.randvoorwaarden = randvoorwaarden

#         # start invullen
#         for i in range(1, self.gridlength - 1):
#             self.grid[i] = int(startgrid[i - 1])

#         # regelint to binairy
#         binary = np.base_repr(regelint, base=2)
#         desiredlength = 8
#         pudding = desiredlength - len(binary)
#         binary = pudding * '0' + binary
#         self.regel = binary

#     def evolueer_cel(self, coord_lijst):
#         midden = self.grid[tuple(coord_lijst)]
#         nieuwe_toestand = midden

#         # skip als rand
#         if midden == -1:
#             return -1

#         links = self.grid[tuple([coord_lijst[0] - 1])]
#         rechts = self.grid[tuple([coord_lijst[0] + 1])]

#         # randvoorwaarden
#         if self.randvoorwaarden == 0:
#             # rondje
#             if links == -1:
#                 links = self.grid[-2]
#             if rechts == -1:
#                 rechts = self.grid[1]
#         elif self.randvoorwaarden == 1:
#             # standaard 1
#             if links == -1:
#                 links = 1
#             if rechts == -1:
#                 rechts = 1
#         elif self.randvoorwaarden == 2:
#             # standaard 0
#             if links == -1:
#                 links = 0
#             if rechts == -1:
#                 rechts = 0
#         else:
#             print('De randvoorwaarden moet 0, 1 of 2 zijn. fuck u')

#         # regels
#         binary = str(int(links)) + str(int(midden)) + str(int(rechts))
#         deci = int(binary, 2)
#         nieuwe_toestand = int(self.regel[-(deci + 1)])

#         return nieuwe_toestand



# # ------------------------------------------------------------------------------
# class kut_game2d(cellulair_automata):
#     def __init__(self, startgrid, birth=[3], death=[0, 1, 4, 5, 6, 7, 8], randvoorwaarden=1,
#                  burenlijst=[[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]):
#         self.dimensions = 2
#         self.gridlength = len(startgrid) + 2
#         # we accepteren geen buren die 2 vakjes ver weg zijn. lekker puh
#         self.burenlijst = burenlijst
#         self.randvoorwaarden = randvoorwaarden
#         self.birth = birth
#         self.death = death
#         regels = [0, 1] * (len(burenlijst) + 1)
#         for i in birth:
#             regels[2 * i] = 1
#         for j in death:
#             regels[2 * j + 1] = 0
#         self.regels = regels

#         if len(regels) / 2 - 1 != len(burenlijst):
#             print('jonathan boos :(')

#         # start toestand invullen.
#         self.grid = -1*np.ones(shape=[len(startgrid)+2]*2)
#         self.grid[1:-1,1:-1] = startgrid

#     def evolueer_cel(self, coord_lijst):
#         midden = self.grid[tuple(coord_lijst)]
#         # skip
#         if midden == -1:
#             return -1

#         buurtoestanden = []
#         for buurcoords in self.burenlijst:
#             buurtoestanden.append(self.grid[tuple(np.array(buur) + np.array(coord_lijst))])

#         # randvoorwaarden
#         if self.randvoorwaarden == 0:
#             # cirkeltje
#             print('HUILEN')
#             for i in range(len(buurtoestanden)):
#                 if buurtoestanden[i] == -1:
#                     buurtoestanden[i] = 'cry yourself to sleep'
#         elif self.randvoorwaarden == 1:
#             # alles 0
#             for i in range(len(buurtoestanden)):
#                 if buurtoestanden[i] == -1:
#                     buurtoestanden[i] = 0
#         elif self.randvoorwaarden == 2:
#             # alles 1
#             for i in range(len(buurtoestanden)):
#                 if buurtoestanden[i] == -1:
#                     buurtoestanden[i] = 1
#         else:
#             print('dit is geen goede randvoorwaarde. Kies 0, 1 of 2')

#         # regels
#         aantallevendeburen = 0
#         for buurtoestand in buurtoestanden:
#             if buurtoestand == 1:
#                 aantallevendeburen += 1
#         # plz geef uitleg:...
#         positie = 2 * aantallevendeburen + int(midden)

#         return int(self.regels[positie])
    
#     def visualiseer(self):
        
#         plt.axis('off')
#         scale = plt.Normalize(-1,1,False)
                              
#         # plt.axis('tight')
#         # plt.axis('image')
#         plt.imshow(self.grid, norm=scale)
#         plt.show()



# # ------------------------------------------------------------------------------


# class game_of_life(kut_game2d):
#     def __init__(self, startgrid):
#         self.dimensions = 2
#         self.gridlength = len(startgrid) + 2
#         self.burenlijst = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

#         # start toestand invullen.
#         row = np.array([-1] * (self.gridlength - 2))
#         collumn = np.array([-1] * self.gridlength)
#         startgrid = np.vstack([startgrid, row])
#         startgrid = np.vstack([row, startgrid])
#         startgrid = startgrid.transpose()
#         startgrid = np.vstack([startgrid, collumn])
#         startgrid = np.vstack([collumn, startgrid])
#         startgrid = startgrid.transpose()
#         self.grid = startgrid

#     def evolueer_cel(self, coord_lijst):
#         midden = self.grid[tuple(coord_lijst)]
#         # skip
#         if midden == -1:
#             return -1

#         buurtoestanden = []
#         for buur in self.burenlijst:
#             buurtoestanden.append(self.grid[tuple(np.array(buur) + np.array(coord_lijst))])

#         # randvoorwaarden
#         for i in range(len(buurtoestanden)):
#             if buurtoestanden[i] == -1:
#                 buurtoestanden[i] = 0

#         # regels
#         aantallevendeburen = 0
#         for buurtoestand in buurtoestanden:
#             if buurtoestand == 1:
#                 aantallevendeburen += 1

#         if (aantallevendeburen >= 4 or aantallevendeburen <= 1) and midden == 1:
#             # DIE
#             return 0
#         elif aantallevendeburen == 3 and midden == 0:
#             # wordt geboren
#             return 1
#         else:
#             # stay the same
#             return midden
# # -----------------------------------------------------------------------------
# def tree_dimensions(cellulair_automata):
#     def __init__(self):
#         pass
# #------------------------------------------------------------------------------
# # testcode om het verschil tussen de automata te laten zien
# size = 50
# dim = 2
# start = np.random.choice([0,1], size=[size]*dim,p=[.9,.1])

# for i in range(50):
#     print (i)
#     if i >10:
#         break
# print( [1,1]+[2,2])
# # x = cellulair_automata()
# # y = regel_30('000010000')
# # z = simple_life('1000000000000000', 50)
# # a = game_of_life(np.ones([10]*2))
# # b = kut_game2d(start, birth=[0,1],death=[4,5],burenlijst=[[0,-1],[-1,-1],[1,-1],[-1,0],[-1,1]])

# # b.evolueer_en_visualiseer(60,0.2,1,1)

