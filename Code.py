import numpy as np
import math
import matplotlib.pyplot as plt


class cellulair_automata():
    def __init__(self):
        # Deze variablen staan nu op de standaardwaarden zodat het
        # programma geen errors geeft maar kunnen bij de subclasses
        # ingevoerd worden op wat ze moeten zijn.
        self.dimensions = 1
        self.gridlength = 1
        self.grid = -1 * np.ones(shape=[self.dimensions] * self.gridlength)

    def evolueer_cel(self, coord_lijst):
        # Deze functie bestaat puur en alleen om door de child objecten overschreven te worden.
        nieuwe_toestand = 1
        return nieuwe_toestand

    def evolueer(self, iterations=1):
        for i in range(iterations):
            d = self.dimensions
            n = self.gridlength
            nieuwe_grid = -2 * np.ones(shape=[n] * d)
            nieuwe_grid[(0,) * d] = self.evolueer_cel([0] * d)
            for x in range(1, n ** d):
                coord_lijst = []
                lengte_getal = math.floor(math.log(x, n))
                rest = x
                for z in range(lengte_getal + 1):
                    quotient = rest // n ** (lengte_getal - z)
                    coord_lijst.append(quotient)
                    rest = rest - quotient * n ** (lengte_getal - z)
                while len(coord_lijst) < d:
                    coord_lijst.insert(0, 0)
                nieuwe_grid[tuple(coord_lijst)] = self.evolueer_cel(coord_lijst)

            self.grid = nieuwe_grid
    
    def visualiseer(self):
        pass
        
    def evolueer_en_visualiseer(self, iterations=1,showinbetween=True):
        self.visualiseer()
        for i in range(iterations):
            self.evolueer()
            if showinbetween:
                self.visualiseer()
        self.visualiseer()
        
        
        

# ------------------------------------------------------------------------------

class regel_30(cellulair_automata):
    def __init__(self, startgrid):
        # dit is een 1d CA ookwel regel 30 genoemnd
        # de randvoorwaarde is rondje
        self.dimensions = 1
        self.gridlength = len(startgrid) + 2
        self.grid = -1 * np.ones(shape=[self.gridlength] * self.dimensions)
        self.regel = '00011110'

        # start invullen
        for i in range(1, self.gridlength - 1):
            self.grid[i] = int(startgrid[i - 1])

    def evolueer_cel(self, coord_lijst):
        midden = self.grid[tuple(coord_lijst)]
        nieuwe_toestand = midden

        # skip als rand
        if midden == -1:
            return -1

        links = self.grid[tuple([coord_lijst[0] - 1])]
        rechts = self.grid[tuple([coord_lijst[0] + 1])]

        # randvoorwaarden
        if links == -1:
            links = self.grid[-2]
        if rechts == -1:
            rechts = self.grid[1]

            # regels
        binary = str(int(links)) + str(int(midden)) + str(int(rechts))
        deci = int(binary, 2)
        nieuwe_toestand = int(self.regel[-(deci + 1)])

        return nieuwe_toestand


# ------------------------------------------------------------------------------

class simple_life(cellulair_automata):
    def __init__(self, startgrid, regelint=30, randvoorwaarden=0):
        # dit is een 1d CA ookwel regel 30 genoemnd
        # de randvoorwaarde is rondje
        self.dimensions = 1
        self.gridlength = len(startgrid) + 2
        self.grid = -1 * np.ones(shape=[self.gridlength] * self.dimensions)
        self.randvoorwaarden = randvoorwaarden

        # start invullen
        for i in range(1, self.gridlength - 1):
            self.grid[i] = int(startgrid[i - 1])

        # regelint to binairy
        binary = np.base_repr(regelint, base=2)
        desiredlength = 8
        pudding = desiredlength - len(binary)
        binary = pudding * '0' + binary
        self.regel = binary

    def evolueer_cel(self, coord_lijst):
        midden = self.grid[tuple(coord_lijst)]
        nieuwe_toestand = midden

        # skip als rand
        if midden == -1:
            return -1

        links = self.grid[tuple([coord_lijst[0] - 1])]
        rechts = self.grid[tuple([coord_lijst[0] + 1])]

        # randvoorwaarden
        if self.randvoorwaarden == 0:
            # rondje
            if links == -1:
                links = self.grid[-2]
            if rechts == -1:
                rechts = self.grid[1]
        elif self.randvoorwaarden == 1:
            # standaard 1
            if links == -1:
                links = 1
            if rechts == -1:
                rechts = 1
        elif self.randvoorwaarden == 2:
            # standaard 0
            if links == -1:
                links = 0
            if rechts == -1:
                rechts = 0
        else:
            print('De randvoorwaarden moet 0, 1 of 2 zijn. fuck u')

        # regels
        binary = str(int(links)) + str(int(midden)) + str(int(rechts))
        deci = int(binary, 2)
        nieuwe_toestand = int(self.regel[-(deci + 1)])

        return nieuwe_toestand


# ------------------------------------------------------------------------------


class game_of_life(cellulair_automata):
    def __init__(self, startgrid):
        self.dimensions = 2
        self.gridlength = len(startgrid) + 2
        self.burenlijst = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

        # start toestand invullen.
        row = np.array([-1] * (self.gridlength - 2))
        collumn = np.array([-1] * self.gridlength)
        startgrid = np.vstack([startgrid, row])
        startgrid = np.vstack([row, startgrid])
        startgrid = startgrid.transpose()
        startgrid = np.vstack([startgrid, collumn])
        startgrid = np.vstack([collumn, startgrid])
        startgrid = startgrid.transpose()
        self.grid = startgrid

    def evolueer_cel(self, coord_lijst):
        midden = self.grid[tuple(coord_lijst)]
        # skip
        if midden == -1:
            return -1

        buurtoestanden = []
        for buur in self.burenlijst:
            buurtoestanden.append(self.grid[tuple(np.array(buur) + np.array(coord_lijst))])

        # randvoorwaarden
        for i in range(len(buurtoestanden)):
            if buurtoestanden[i] == -1:
                buurtoestanden[i] = 0

        # regels
        aantallevendeburen = 0
        for buurtoestand in buurtoestanden:
            if buurtoestand == 1:
                aantallevendeburen += 1

        if (aantallevendeburen >= 4 or aantallevendeburen <= 1) and midden == 1:
            # DIE
            return 0
        elif aantallevendeburen == 3 and midden == 0:
            # wordt geboren
            return 1
        else:
            # stay the same
            return midden


# ------------------------------------------------------------------------------
class kut_game2d(cellulair_automata):
    def __init__(self, startgrid, birth=[3], death=[0, 1, 4, 5, 6, 7, 8], randvoorwaarden=1,
                 burenlijst=[[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]):
        self.dimensions = 2
        self.gridlength = len(startgrid) + 2
        # we accepteren geen buren die 2 vakjes ver weg zijn. lekker puh
        self.burenlijst = burenlijst
        self.randvoorwaarden = randvoorwaarden
        self.birth = birth
        self.death = death
        regels = [0, 1] * (len(burenlijst) + 1)
        for i in birth:
            regels[2 * i] = 1
        for j in death:
            regels[2 * j + 1] = 0
        self.regels = regels

        if len(regels) / 2 - 1 != len(burenlijst):
            print('jonathan boos :(')

        # start toestand invullen.
        row = np.array([-1] * (self.gridlength - 2))
        collumn = np.array([-1] * self.gridlength)
        startgrid = np.vstack([startgrid, row])
        startgrid = np.vstack([row, startgrid])
        startgrid = startgrid.transpose()
        startgrid = np.vstack([startgrid, collumn])
        startgrid = np.vstack([collumn, startgrid])
        startgrid = startgrid.transpose()
        self.grid = startgrid

    def evolueer_cel(self, coord_lijst):
        midden = self.grid[tuple(coord_lijst)]
        # skip
        if midden == -1:
            return -1

        buurtoestanden = []
        for buur in self.burenlijst:
            buurtoestanden.append(self.grid[tuple(np.array(buur) + np.array(coord_lijst))])

        # randvoorwaarden
        if self.randvoorwaarden == 0:
            # cirkeltje
            print('HUILEN')
            for i in range(len(buurtoestanden)):
                if buurtoestanden[i] == -1:
                    buurtoestanden[i] = 'cry yourself to sleep'
        elif self.randvoorwaarden == 1:
            # alles 0
            for i in range(len(buurtoestanden)):
                if buurtoestanden[i] == -1:
                    buurtoestanden[i] = 0
        elif self.randvoorwaarden == 2:
            # alles 1
            for i in range(len(buurtoestanden)):
                if buurtoestanden[i] == -1:
                    buurtoestanden[i] = 1
        else:
            print('dit is geen goede randvoorwaarde. Kies 0, 1 of 2')

        # regels
        aantallevendeburen = 0
        for buurtoestand in buurtoestanden:
            if buurtoestand == 1:
                aantallevendeburen += 1
                # plz geef uitleg:...
        positie = 2 * aantallevendeburen + int(midden)

        return int(self.regels[positie])
    
    def visualiseer(self):
        self.grid
        plt.imshow(self.grid)


# -----------------------------------------------------------------------------
# testcode om het verschil tussen de automata te laten zien

x = cellulair_automata()
y = regel_30('000010000')
z = simple_life('1000000000000000', 50)
a = game_of_life(np.array([
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]))
b = kut_game2d(np.array([
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]))

b.evolueer_en_visualiseer(10)

