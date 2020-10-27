from tkinter import *
import os

HEIGHT = 720
WIDTH = 960


class First_Page:
    # MAINWINDOW INTERFACE
    def __init__(self):
        self.mainwindow = Tk()  # créer une première fenêtre (fenêtre principale)
        icon = PhotoImage(file='images.png')  # file ou est le icon
        # ajout des options pour le icon
        self.mainwindow.iconphoto(False, icon)
        self.mainwindow.backgroundImage = PhotoImage(file='./background.png')
        self.mainwindow.backgroundLable = Label(
            self.mainwindow, image=self.mainwindow.backgroundImage)
        self.mainwindow.backgroundLable.place(relwidth=1, relheight=1)
        self.mainwindow.title("BNF")  # personnalisation de la fenêtre
        self.mainwindow.maxsize(WIDTH, HEIGHT)
        self.mainwindow.minsize(WIDTH, HEIGHT)
        self.mainwindow.geometry("960x720")
        # créer la boite (frame)  Pour centrer les 2 textes au centre de la page
        self.frame = Frame(self.mainwindow, bg='#192576')
        self.window1_widgets()
        # ajouter le frame et le expand
        self.frame.pack(expand=YES)


# MAIN PAGE ANGLAIS


    def buildToolsOptionFrame(self, title, but1Title, but2Title, but3Title):
        # detruire les frames dans les widgets
        for widget in self.frame.winfo_children(): # detruire les frames
            widget.destroy()
        # se qui va etre montre apres le destroy
        self.toolsOption(title, but1Title, but2Title, but3Title)

# PROFIT EN FRANCAIS
    def fr_clearFrame_profit(self):
        # detruire les frames dans les widgets
        for widget in self.frame.winfo_children():  # detruire les frames
            widget.destroy()
        # se qui va etre montre apres le destroy    
        self.fr_profit()  
# PAGE ACCUEIL
    def window1_widgets(self):
        self.window1_title("Welcome to BNF")
        self.window1_subtitle("choose your language")
        self.window1_button1("English")
        self.window1_button2("Francais")

    def toolsOption(self, title, but1Title, but2Title, but3Title):
        self.window2_title(title)
        self.window2_button1(but1Title)
        self.window2_button2(but2Title)
        self.window2_button3(but3Title)

    def window1_title(self, txt):
        # label pour l'organisation et la présentation du texte
        label_mainwindow = Label(self.frame, text=txt, font=(
            "impact, 40"), bg='#192576', fg='White')
        label_mainwindow.pack() 

    def window1_subtitle(self, txt):
        label_subtitle = Label(self.frame, text=txt, font=(
            "impact, 20"), bg='#192576', fg='White')
        label_subtitle.pack()

    def window1_button1(self, txt):
        button1_mainwindow = Button(self.frame, command=lambda: self.buildToolsOptionFrame("Choose an option", "Calculate\na\nprofit", "Calculate\n......\n....", "Calculate\n......\n...."), text=txt, font=(
            "impact, 30"), bg='#3C435C', fg='white') 
        button1_mainwindow.pack(pady=0, side=LEFT) 

    def window1_button2(self, txt):
        button2_mainwindow = Button(self.frame, command=lambda: self.buildToolsOptionFrame("Choisi une option", "Calcule\nton\nprofit", "Calcule\n......\n....", "Calcule\n......\n...."), text=txt, font=(
            "impact, 30"), bg='#3C435C', fg='white')  
        button2_mainwindow.pack(pady=0, side=RIGHT,)


# PAGE PROFIT PAR DEF


    def window2_title(self, txt):
        # label pour l'organisation et la présentation du texte
        label_window2 = Label(self.frame, text=txt, font=(
            "impact, 40"), bg='#192576', fg='White')
        label_window2.pack()

    def window2_button1(self, txt):
        button1_window2 = Button(self.frame, command=self.fr_clearFrame_profit, text=txt, font=(
            "impact, 22"), bg='#3C435C', fg='white')
        button1_window2.pack(pady=5, side=LEFT)

    def window2_button2(self, txt):
        button2_window2 = Button(self.frame, text=txt, font=(
            "impact, 22"), bg='#3C435C', fg='white')
        button2_window2.pack(pady=5, side=RIGHT)

    def window2_button3(self, txt):
        button3_window2 = Button(self.frame, text=txt, font=(
            "impact, 22"), bg='#3C435C', fg='white')
        button3_window2.pack(pady=5, side=TOP)

    def fr_profit(self):
        self.interface_label_saisie1("Entre le montant investi: ")
        self.interface_saisie1("...")
        self.interface_label_saisie2("Entre ton benefice par mois en %: ")
        self.interface_saisie2("...")
        self.interface_label_saisie3(
            "Entre le nombre de mois que tu a investi: ")
        self.interface_saisie3("...")
        self.interface_profit_boutton1("Entrer")

# boite de saisie investi
    def interface_label_saisie1(self, txt):
        label_saisie1 = Label(self.frame, text=txt, font=(
            "impact, 20"))  
        label_saisie1.pack()

    def interface_saisie1(self, txt):
        saisie1 = Entry(self.frame, width=10, font=(
            "impact, 20"))
        saisie1.insert(0, txt)  # On insère une valeur par défaut
        saisie1.pack()

# boite de saisie2 benefice en %
    def interface_label_saisie2(self, txt):
        label_saisie2 = Label(self.frame, text=txt, font=(
            "impact, 20"))
        label_saisie2.pack()

    def interface_saisie2(self, txt):
        saisie2 = Entry(self.frame, width=10, font=(
            "impact, 20"))
        saisie2.insert(0, txt)  # On insère une valeur par défaut
        saisie2.pack()

# Nombre de mois d'investisement
    def interface_label_saisie3(self, txt):
        label_saisie3 = Label(self.frame, text=txt, font=(
            "impact, 20"))
        label_saisie3.pack()

    def interface_saisie3(self, txt):
        saisie3 = Entry(self.frame, width=10, font=(
            "impact, 20"))
        saisie3.insert(0, txt)  # On insère une valeur par défaut 0
        saisie3.pack()

    def interface_profit_boutton1(self, txt):
        button1_profit = Button(self.frame, text=txt, font=(
            "impact, 22"), bg='#3C435C', fg='white')
        button1_profit.pack(pady=5, side=TOP)


# pour lancer l'interface
app = First_Page()
app.mainwindow.mainloop()
