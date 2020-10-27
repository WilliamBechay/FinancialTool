from tkinter import *
import os

HEIGHT = 720 
WIDTH = 960

class First_Page:
#MAINWINDOW INTERFACE
    def __init__(self):
        self.mainwindow = Tk()#créer une première fenêtre (fenêtre principale)
        icon = PhotoImage(file = 'images.png') #file ou est le icon 
        self.mainwindow.iconphoto(False, icon) #ajout des options pour le icon
        self.mainwindow.background_image = PhotoImage(file='./background.png')
        self.mainwindow.background_lable = Label(self.mainwindow,image=self.mainwindow.background_image)
        self.mainwindow.background_lable.place(x=0,relwidth=1, relheight=1)
        self.mainwindow.title("BNF")#personnalisation de la fenêtre
        self.mainwindow.maxsize(WIDTH , HEIGHT)#La taille max ne peut pas depasser ces valeurs
        self.mainwindow.minsize(WIDTH, HEIGHT)#La taille mini ne peut pas dépasser ces valeurs
        self.mainwindow.geometry("960x720")#la taille par defaut
        self.frame = Frame(self.mainwindow, bg='#192576')#créer la boite (frame)  Pour centrer les 2 textes au centre de la page   
        self.window1_widgets()
        self.frame.pack(expand=YES)#ajouter le frame



#NETTOYER LES PAGES
#MAIN PAGE ANGLAIS 
    def en_clearFrame(self):
        # detruire les frames dans les widgets 
        for widget in self.frame.winfo_children(): #detruire les frames
           widget.destroy()
        self.en_window2_widgets()# se qui va etre montre apres le destroy
#MAIN PAGE FRANCAIS 
    def fr_clearFrame(self):
        #detruire les frames dans les widgets 
        for widget in self.frame.winfo_children(): #detruire les frames
           widget.destroy()
        self.fr_window2_widgets()#se qui va etre montre apres le destroy
#PROFIT EN FRANCAIS
    def fr_clearFrame_profit(self):
        # detruire les frames dans les widgets 
        for widget in self.frame.winfo_children(): #detruire les frames
           widget.destroy()
        self.fr_profit()# se qui va etre montre apres le destroy




#PAGE ACCUEIL
    def window1_widgets(self):
        self.window1_title("Welcome to BNF")
        self.window1_subtitle("choose your language")
        self.window1_button1("English")
        self.window1_button2("Francais")
    def window1_title(self, txt):
        label_mainwindow = Label(self.frame, text=txt,font=("impact, 40"), bg='#192576', fg='White')#label est une variable est pour l'organisation et la présentation du texte 
        label_mainwindow.pack()#pour afficher le label
    def window1_subtitle(self, txt):    
        label_subtitle = Label(self.frame, text=txt,font=("impact, 20"), bg='#192576', fg='White')#ajouter un second texte(soustitre)
        label_subtitle.pack()
    def window1_button1(self, txt):
        button1_mainwindow = Button(self.frame,command=self.en_clearFrame, text=txt, font=("impact, 30"), bg='#3C435C', fg='white')#ajouter un bouton1 
        button1_mainwindow.pack(pady=0 ,side=LEFT)#afficher bouton1 
    def window1_button2(self, txt):
        button2_mainwindow = Button(self.frame,command=self.fr_clearFrame,text=txt, font=("impact, 30"), bg='#3C435C', fg='white')#ajouter un bouton2
        button2_mainwindow.pack(pady=0 ,side=RIGHT,)#afficher bouton2 




#PAGE INTERFACE
#PAGE EN ANGLAIS
    def en_window2_widgets(self):
        self.window2_title("Choose an option")
        self.window2_button1("Calculate\na\nprofit")
        self.window2_button2("Calculate\n......\n...." )
        self.window2_button3("Calculate\n......\n...." )
#PAGE EN FRANCAIS
    def fr_window2_widgets(self):
        self.window2_title("Choisi une option")
        self.window2_button1("Calcule\nton\nprofit")
        self.window2_button2("Calcule\n......\n...." )
        self.window2_button3("Calcule\n......\n...." )
#PAGE PROFIT PAR DEF
    def window2_title(self, txt):
        label_window2 = Label(self.frame, text=txt,font=("impact, 40"), bg='#192576', fg='White')#label est une variable est pour l'organisation et la présentation du texte 
        label_window2.pack()#pour afficher le label
    def window2_button1(self, txt):
        button1_window2 = Button(self.frame,command=self.fr_clearFrame_profit, text=txt, font=("impact, 22"), bg='#3C435C', fg='white')#ajouter un bouton1 
        button1_window2.pack(pady=5 ,side=LEFT)#afficher bouton1 
    def window2_button2(self, txt):
        button2_window2 = Button(self.frame,text=txt, font=("impact, 22"), bg='#3C435C', fg='white')#ajouter un bouton2
        button2_window2.pack(pady=5 ,side=RIGHT)#affcher bouton2 
    def window2_button3(self, txt):
        button3_window2 = Button(self.frame,text=txt, font=("impact, 22"), bg='#3C435C', fg='white')#ajouter un bouton2
        button3_window2.pack(pady=5 ,side=TOP)#affcher bouton2 





    def fr_profit(self):
        self.interface_label_saisie1("Entre le montant investi: ")
        self.interface_saisie1("...")
        self.interface_label_saisie2("Entre ton benefice par mois en %: ")
        self.interface_saisie2("...")
        self.interface_label_saisie3("Entre le nombre de mois que tu a investi: ")
        self.interface_saisie3("...")
        self.interface_profit_boutton1("Entrer")
    
    def interface_label_saisie1(self,txt):
    #boite de saisie investi
        label_saisie1 = Label(self.frame, text= txt,font=("impact, 20")) # On crée un label   
        label_saisie1.pack()# On affiche le label dans la fenêtre 
    def interface_saisie1(self, txt):
        saisie1 = Entry(self.frame, width=10 ,font=("impact, 20"))# On crée un Entry  
        saisie1.insert(0, txt)# On insère une valeur par défaut 
        saisie1.pack()# On affiche le Entry dans la fenêtre
    def interface_label_saisie2(self, txt):
    #boite de saisie2 benefice en %
        label_saisie2 = Label(self.frame, text= txt,font=("impact, 20"))    # On crée un label  
        label_saisie2.pack()# On affiche le label dans la fenêtre 
    def interface_saisie2(self, txt):
    # On crée un Entry  
        saisie2 = Entry(self.frame, width=10 ,font=("impact, 20"))# On crée un Entry  
        saisie2.insert(0, txt)# On insère une valeur par défaut 
        saisie2.pack()# On affiche le Entry dans la fenêtre    
    def interface_label_saisie3(self, txt):
    #boite de saisie benefice en %
        label_saisie3 = Label(self.frame, text= txt,font=("impact, 20"))    # On crée un label 
        label_saisie3.pack()# On affiche le label dans la fenêtre 
    def interface_saisie3(self, txt):
    # On crée un Entry  
        saisie3 = Entry(self.frame, width=10 ,font=("impact, 20"))# On crée un Entry  
        saisie3.insert(0, txt)# On insère une valeur par défaut 
        saisie3.pack()# On affiche le Entry dans la fenêtre
    def interface_profit_boutton1(self, txt):
        button1_profit = Button(self.frame,text=txt, font=("impact, 22"), bg='#3C435C', fg='white')#ajouter un bouton2
        button1_profit.pack(pady=5 ,side=TOP)#affcher bouton2 

        
#pour lancer l'interface
app = First_Page()
app.mainwindow.mainloop()
