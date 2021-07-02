import Cellulaire_Automata as CA
import numpy as np
matrix = np.array([[0,1,0,0,0,0,0,0,0,0],
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
gol = CA.game_of_life(startgrid=matrix,randvoorwaarden=0)
gol.evolueer(iterations=1)
gol.visualiseer()
gol.evolueer_en_visualiseer(iterations=10,timeperframe=0.5,showevery=1)
gol.visual.mainloop()



# import GUI #gui importen start de UI op


matrix = np.array([[0,1,0,0,0,0,0,0,0,0],
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







#------------------------------------------------------------------------------
#Tests and examples
#------------------------------------------------------------------------------













# glider = [[0,1,0,0,0,0,0,0,0,0],
#                   [0,0,1,0,0,0,0,0,0,0],
#                   [1,1,1,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0,0],
#                   ]
# glidergof = CA.game_of_life(glider,-1) #gof = game of life
# glidergof.evolueer_en_visualiseer(30,0.4)
# glidergof.visual.mainloop()
# #Hier testen we de basic game of life functies met rondgaande randvoorwaarden

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
# #hier testen we de rand = 0 randvoorwaarde. De Loafer sterf tegen de rand aan.

# opdrachtvoorbeeld = np.array([0,0,0,0,1,0,0,0,0])
# opdrachtvoorbeeldr30 = CA.regel30(opdrachtvoorbeeld, 0)
# opdrachtvoorbeeldr30.evolueer_en_visualiseer(10,1)
# # hier zien we dat de regel30 uit het voorbeeld goed werkt. 

# driedee = np.array([
#                     [[0,0,0],[0,0,0],[0,0,0]],
#                     [[0,0,0],[0,1,0],[0,0,0]],
#                     [[0,0,0],[0,0,0],[0,0,0]],
#                     ])
# driedeeburen = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
# driedeeregels = np.array([[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])
# driedeeCA = CA.symmetrische_CA(3, driedee, 0, driedeeburen, [0,1], driedeeregels)
# driedeeCA.evolueer_en_visualiseer(5)
# #dit is een super basic 3 dimensionaal Cellulaiprintr automaton om aan te tonen dat het werkt. het zou zich moeten opvullen
# # via een zeer basic patroon namelijk als een van buren 1 is wordt ik dat ook. De buren zijn daarbij ingesteld als alles 
# #waar elke kubus een vlak mee deelt, ofwel niet schuin. 

# vierdee = np.array([
#                     [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],
#                     [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],
#                     [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],
#                     ])
# vierdeeburen = [[1,0,0,0],[-1,0,0,0],[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]]
# vierdeeregels = np.array([[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])
# vierdeeCA = CA.symmetrische_CA(4, vierdee, 0, vierdeeburen, [0,1], vierdeeregels)
# vierdeeCA.evolueer_en_visualiseer(5)
# #Hier weer hetzelfde super basic cellulair automaton alleen dan in vier dimensies. Hieraan kunnen we goed zien dat het 
# #snel te complext wordt om nog nuttig te zijn als we in hogere dimensies gaan werken

# #op de hierboven beschreven unit tests hebben we nog een klasse gebaseerd, de simpele hoger dimensionale CA die voor 
# #een gegeven dimensie precies zon CA maakt.

vijfdee = CA.simpele_hoger_dimensionaale_CA('vijf')
vijfdee.evolueer_en_visualiseer(5)
# # wat we zien is dat 5d erg slecht te visualiseren valt. Wat verder ook opvalt is dat elke dimensie die je toevoegt 
# # ervoor zorgt dat je een extra stap nodig hebt om alle posities 1 te maken.

# string_theory = CA.simpele_hoger_dimensionaale_CA(10)
# string_theory.evolueer_en_visualiseer(1)
# #en hier zien we het probleem met hogere dimensies nog eens verder uit gebreid. als eerste is visualisatie
# #problematisch en als tweede wordt de rekentijd erg hoog. dit heeft lengte 3 maar vanwege de hoge dimensie
# #is het aantal vakje gelijk aan 3**10 = 59049!!!

# custom1dCA = CA.customregel(np.array([0,0,0,0,1,0,0,0,0]),0,30)
# custom1dCA.evolueer_en_visualiseer(15,0.4)