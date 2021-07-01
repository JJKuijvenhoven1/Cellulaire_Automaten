
from tkinter import *
import tkinter as tk
import numpy as np
import Cellulaire_Automata as ca

   
root = Tk()
root.title("Root")
root.geometry("800x400")


#Game of Life
def new_GoL_window(lengte, iteraties, randvoorwaarde, showevery):
    window = tk.Toplevel(root)
    window.title("Game of Life window")
    window.geometry("500x500")
    startgrid = np.zeros([lengte]*2)
    frame = Frame(window)
    Grid.rowconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N+S+E+W)
    grid = Frame(frame)
    grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
    Grid.rowconfigure(frame, 7, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)

    een = "yellow"
    nul = "cyan"

    def click(btn, x, y):
        if btn["bg"] == een:
            btn["bg"] = nul
            startgrid[x,y-2] = 0
        else:
            btn["bg"] = een
            startgrid[x,y-2] = 1

    def magie(lengte=10):
        for x in range(lengte):
            for y in range(2, lengte+2):
                btn = Button(frame, bg=nul, text=str(x) + " " + str(y-2))
                btn.grid(column=y, row=x, sticky=N+S+E+W)
                btn["command"] = lambda btn=btn, x=x, y=y: click(btn, x, y)

        for y in range(lengte+2):
            Grid.columnconfigure(frame, y, weight=1)
            
        for x in range(lengte):
            Grid.rowconfigure(frame, x, weight=1)

        return frame

    magie(lengte)    

    def enter_gol(sg, it, rv, se):
        gol = ca.game_of_life(sg, randvoorwaarden=rv)
        gol.evolueer_en_visualiseer(iterations=it, showevery=se)
    
    enter_GoL = Button(frame, bg="red", text="Enter")
    enter_GoL.grid(column=0, row=0, sticky=N+S+E+W)
    enter_GoL["command"] = lambda startgrid=startgrid, iteraties=iteraties, randvoorwaarde=randvoorwaarde, showevery=showevery: enter_gol(startgrid, iteraties, randvoorwaarde, showevery)


#regel 30
def new_regel30_window(lengte, iteraties, randvoorwaarde, showevery):
    window = Toplevel(root)
    window.title("Regel 30 window")
    window.geometry("700x200")
    startgrid = np.zeros([lengte])
    Grid.columnconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 0, weight=1)
    
    def click_r30(btn, x):
        if btn["bg"] == "cyan":
            btn["bg"] = "yellow"
            startgrid[x-2] = 1
        elif btn["bg"] == "yellow":
            btn["bg"] = "cyan"
            startgrid[x-2] = 0
    
    def magie_r30(lengte):
        for x in range(2,lengte+2):
            btn = Button(window, bg="cyan", text=str(x-2))
            btn.grid(column=x, row=0, sticky=N+S+E+W)
            btn["command"] = lambda btn=btn, x=x: click_r30(btn, x)
            
        for y in range(lengte+2):
            Grid.columnconfigure(window, y, weight=1)
        
        return window
    
    magie_r30(lengte)
    
    def enter_r30(sg, it, rv, se):
        CAr30 = ca.regel30(startgrid=sg, randvoorwaarden=rv)
        CAr30.evolueer_en_visualiseer(iterations=it, showevery=se)
        
    
    enter_R30 = Button(window, bg="red", text="Enter")
    enter_R30.grid(column=0, row=0, sticky=N+S+E+W)
    enter_R30["command"] = lambda startgrid=startgrid, iteraties=iteraties, randvoorwaarde=randvoorwaarde, showevery=showevery: enter_r30(startgrid, iteraties, randvoorwaarde, showevery)

        
#Algemeen 1D
def new_1D_window(lengte, iteraties, randvoorwaarde, showevery):
    window = Toplevel(root)
    window.title("1D window")
    window.geometry("700x100")
    startgrid = np.zeros([lengte])
    Grid.columnconfigure(window, 0, weight=1)
    Grid.rowconfigure(window, 0, weight=1)
    
    def click_1D(btn, x):
        if btn["bg"] == "cyan":
            btn["bg"] = "yellow"
            startgrid[x-2] = 1
            print(startgrid)
        elif btn["bg"] == "yellow":
            btn["bg"] = "cyan"
            startgrid[x-2] = 0
            print(startgrid)
    
    def magie_1D(lengte):
        for x in range(2,lengte+2):
            btn = Button(window, bg="cyan", text=str(x-2))
            btn.grid(column=x, row=0, sticky=N+S+E+W)
            btn["command"] = lambda btn=btn, x=x: click_1D(btn, x)
            
        
        return window
    
    magie_1D(lengte)
    
    regel_var = StringVar()
    regel_invoer = Entry(window, textvariable=regel_var)
    regel_invoer.grid(row=2, column=0)
    regel_label = Label(window, text="Welke regel wil je gebruiken? ")
    regel_label.grid(row=1, column=0)
    
    def enter_1D(sg, it, rv, se, regel):
        custom = ca.customregel(startgrid=sg, randvoorwaarden=rv, regelcode=regel)
        custom.evolueer_en_visualiseer(iterations=it, showevery=se)
        
    
    Enter_1D = Button(window, bg="red", text="Enter")
    Enter_1D.grid(column=0, row=0, sticky=N+S+E+W)
    Enter_1D["command"] = lambda startgrid=startgrid, iteraties=iteraties, randvoorwaarde=randvoorwaarde, showevery=showevery, regel=regel_var.get(): enter_1D(startgrid, iteraties, randvoorwaarde, showevery, regel)
    
    for y in range(lengte+2):
        Grid.columnconfigure(window, y, weight=1)
    

    


#randvoorwaarden
rvtitel = Label(root, text="Welke randvoorwaarde wil je? ")
rvtitel.grid(row=0, column=0, sticky=W)
randvoorwaarde_var = IntVar()
periodiek = Radiobutton(root, text="Periodiek", variable=randvoorwaarde_var, value=-1)
periodiek.grid(row=1, column=0, sticky=W)
dirichlet0 = Radiobutton(root, text="Dirichlet met 0", variable=randvoorwaarde_var, value=0)
dirichlet0.grid(row=2, column=0, sticky=W)
dirichlet1 = Radiobutton(root, text="Dirichlet met 1", variable=randvoorwaarde_var, value=1)
dirichlet1.grid(row=3, column=0, sticky=W)
vonNeumann = Radiobutton(root, text="Von Neumann", variable=randvoorwaarde_var, value=-2)
vonNeumann.grid(row=4, column=0, sticky=W)

#lengte
lengte_var = StringVar()
lengte_invoer = Entry(root, textvariable=lengte_var)
lengte_invoer.grid(row=5, column=1)
lengte_label = Label(root, text="Wat wordt de lengte van je grid? ")
lengte_label.grid(row=4, column=1)

#welke automaat
welke_automaat = IntVar()
welke_automtaat_label = Label(root, text="Welk automaton wil je gebruiken? ")
welke_automtaat_label.grid(row=6, column=0)
GoL = Radiobutton(root, text="Game of Life", variable=welke_automaat, value=0)
GoL.grid(row=7, column=0, sticky=W)
r30 = Radiobutton(root, text="Regel 30", variable=welke_automaat, value=1)
r30.grid(row=8, column=0, sticky=W)
eenD = Radiobutton(root, text="Algemene 1D automaat", variable=welke_automaat, value=2)
eenD.grid(row=9, column=0, sticky=W)

#aantal iteraties
iteratie_var = StringVar()
iteratie_invoer = Entry(root, textvariable=iteratie_var)
iteratie_invoer.grid(row=1, column=1)
iteratie_label = Label(root, text="Hoeveel iteraties wil je uitvoeren? ")
iteratie_label.grid(row=0, column=1)

#show every
showevery_var = StringVar()
showevery_invoer = Entry(root, textvariable=showevery_var)
showevery_invoer.grid(row=3, column=1)
showevery_label = Label(root, text="Om de hoeveel iteraties moet het afgebeeld worden? ")
showevery_label.grid(row=2, column=1)



#submit button
def submit():
    if welke_automaat.get() == 0:
        new_GoL_window(int(lengte_var.get()), int(iteratie_var.get()), randvoorwaarde_var.get(), int(showevery_var.get()))
    elif welke_automaat.get() == 1:
        new_regel30_window(int(lengte_var.get()), int(iteratie_var.get()), randvoorwaarde_var.get(), int(showevery_var.get()))
    elif welke_automaat.get() == 2:
        new_1D_window(int(lengte_var.get()), int(iteratie_var.get()), randvoorwaarde_var.get(), int(showevery_var.get()))
        

btnSubmit = Button(root, text="Submit", bg="red", command=submit)
btnSubmit.grid(row=8, column=1)
root.mainloop()
