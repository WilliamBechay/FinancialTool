def def_float_obli(x) :
    while True:
        number = input(x+"\n")
        try:
            val = float(number)
            #demende une valuer > 0 
            if val <= 0:
                print("Erreur : Veillez entrer un nombre positif plus grand que 0 \n")
                continue
            return number
        except ValueError:
            print("Erreur : Veillez entrer un chiffre et non une lettre \n")