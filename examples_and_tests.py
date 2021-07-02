import Cellulaire_Automata as CA
#import GUI #gui importen start de UI op zodra je het programma runt
import numpy as np

#------------------------------------------------------------------------------
#UNIT TESTS
#------------------------------------------------------------------------------

# glider = np.array([[0,1,0,0,0,0,0,0,0,0],
#                   [0,0,1,0,0,0,0,0,0,0],
#                   [1,1,1,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   ])
# glidergof = CA.game_of_life(glider,-1)
# glidergof.evolueer_en_visualiseer(30,0.4)
# glidergof.visual.mainloop()
'''Hier testen we de basic game of life functies met rondgaande randvoorwaarden'''


# loafer = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                     ])
# loafergof = CA.game_of_life(loafer, 0)
# loafergof.evolueer_en_visualiseer(30,0.4)
# loafergof.visual.mainloop()
'''hier testen we de rand = 0 randvoorwaarde. De Loafer sterf tegen de rand aan.'''


# opdrachtvoorbeeld = np.array([0,0,0,0,1,0,0,0,0])
# opdrachtvoorbeeldr30 = CA.regel30(opdrachtvoorbeeld, 0)
# opdrachtvoorbeeldr30.evolueer_en_visualiseer(10,1)
'''hier zien we dat de regel30 uit het voorbeeld goed werkt.'''


# driedee = np.array([
#                     [[0,0,0],[0,0,0],[0,0,0]],
#                     [[0,0,0],[0,1,0],[0,0,0]],
#                     [[0,0,0],[0,0,0],[0,0,0]],
#                     ])
# driedeeburen = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
# driedeeregels = np.array([[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])
# driedeeCA = CA.symmetrische_CA(3, driedee, 0, driedeeburen, [0,1], driedeeregels)
# driedeeCA.evolueer_en_visualiseer(5)
'''dit is een super basic 3 dimensionaal Cellulaiprintr automaton om aan te tonen dat het werkt. het zou zich moeten opvullen
via een zeer basic patroon namelijk als een van buren 1 is wordt ik dat ook. De buren zijn daarbij ingesteld als alles 
waar elke kubus een vlak mee deelt, ofwel niet schuin. '''


#vierdee = np.array([
#                    [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],
#                    [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],
#                    [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],
#                    ])
#vierdeeburen = [[1,0,0,0],[-1,0,0,0],[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]]
#vierdeeregels = np.array([[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])
#vierdeeCA = CA.symmetrische_CA(4, vierdee, 0, vierdeeburen, [0,1], vierdeeregels)
#vierdeeCA.evolueer_en_visualiseer(5)
'''Hier weer hetzelfde super basic cellulair automaton alleen dan in vier dimensies. Hieraan kunnen we goed zien dat het 
snel te complext wordt om nog nuttig te zijn als we in hogere dimensies gaan werken'''


'''op de hierboven beschreven unit tests hebben we nog een klasse gebaseerd, de simpele hoger dimensionale CA die voor 
een gegeven dimensie precies zon CA maakt.'''


#vijfdee = CA.simpele_hoger_dimensionaale_CA(5)
#vijfdee.evolueer_en_visualiseer(5)
'''wat we zien is dat 5d erg slecht te visualiseren valt. Wat verder ook opvalt is dat elke dimensie die je toevoegt 
ervoor zorgt dat je een extra stap nodig hebt om alle posities 1 te maken.'''


#string_theory = CA.simpele_hoger_dimensionaale_CA(10)
#string_theory.evolueer_en_visualiseer(1)
'''en hier zien we het probleem met hogere dimensies nog eens verder uit gebreid. als eerste is visualisatie
problematisch en als tweede wordt de rekentijd erg hoog. dit heeft lengte 3 maar vanwege de hoge dimensie
is het aantal vakje gelijk aan 3**10 = 59049!!!'''


# bb_regels = np.zeros((9,9,3))
# for x in range(9):
#     for y in range(1,9):
#         bb_regels[(x, y, 1)] = 2
#     bb_regels[(x,0,1)] = 1
# random = np.random.choice([0,1,2], size=[100]*2, p=[0.5, 0.48, 0.02])
# bosbrand = CA.symmetrische_CA(dimensions=2, startgrid=random, randvoorwaarden=0, 
#                               burenlijst=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]],
#                               toestanden=[0,1,2], regelcode = bb_regels)
# bosbrand.evolueer_en_visualiseer(iterations=15, timeperframe=1)
# bosbrand.visual.mainloop()
'''Hier hebben we een een heel naïef model van een bosbrand gemaakt, waarbij een levende boom met toestand 1 wordt weergegeven,
een brandende boom met toestand 2, en een dode boom (en ook de afwezigheid van een boom) met toestand 0. We bekijken dezelfde
buren als bij de game of life. De regels gaan als volgt: als je een levende boom bent en tenminste 1 van je buren staat in brand,
dan vlieg je zelf ook in brand. Anders blijf je leven. Als je in brand staat ga je de volgende generatie dood. Dode bomen blijven dood.
We maken elke keer een 100 bij 100 grid met die op random plekken 0, 1 en 2 zet, volgens de opgegeven kansen.'''


hexagon = CA.symmetrische_CA(dimensions=2, startgrid=dit, randvoorwaarden=-1, 
                             burenlijst=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]])
