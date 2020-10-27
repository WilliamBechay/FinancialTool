

#PAGE MAIN INTERFACE
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
#PAGE PROFIT EN FRANCAIS
def fr_profit(self):
        self.interface_label_saisie1("Entre le montant investi: ")
        self.interface_saisie1("...")
        self.interface_label_saisie2("Entre ton benefice par mois en %: ")
        self.interface_saisie2("...")
        self.interface_label_saisie3("Entre le nombre de mois que tu a investi: ")
        self.interface_saisie3("...")
        self.interface_profit_boutton1("Entrer")
    