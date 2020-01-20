import Tkinter
import random

colour=['Red','Orange','Green','Pink','Black','Yellow','Orange','White','Purple']

score=0

timeleft=40
def GameStarter(event):
    if timeleft ==30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft>0:
        e.focus_set()

        if e.get().lower()== colour[1].lower():
            score=score+1
        
        e.delete(0,Tkinter.END)

        random.shuffle(colour)

        label.config(fg=str(colour[1]),  text=str(colour[0]))

        scoreLabel.config(text ="Score: "+ str(score))


root=Tkinter.Tk()

root.title("Game of Colors")

root.geometry("375x200")

instructions=Tkinter.Label(root , text ="Type the shown color of the shown text",font =('Helvetica',12))

instructions.pack()

scoreLabel=Tkinter.Label(root,text ="Press enter to start",font =('Helvetica',12))

scoreLabel.pack()

timeLabel=Tkinter.Label(root,text ="Time left: "+str(timeleft),font =('Helvetica',12))

timeLabel.pack()

label=Tkinter.Label(root,font =('Helvetica',60))
label.pack()

e=Tkinter.Entry(root)

root.bind('<Return>',GameStarter)
e.pack()

e.focus_set()

root.mainloop()
