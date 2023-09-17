class GestionFichyeTeks:
    def __init__(self, chemen_fichye):
        self.chemen_fichye = chemen_fichye

    def li_fichye(self):
        try:
            with open(self.chemen_fichye, 'r') as fichye:
                kontni = fichye.read()
            return kontni
        except FileNotFoundError:
            return "Fichye a pa jwenn."

    def afiche_fichye(self):
        kontni = self.li_fichye()
        print("Kontni fichye tèks la se:\n", kontni)

    def modifye_fichye(self, ajoute_teks, endeks=None):
        kontni = self.li_fichye()
        if endeks is None:
            kontni += ajoute_teks
        else:
            kontni = kontni[:endeks] + ajoute_teks + kontni[endeks:]
        with open(self.chemen_fichye, 'w') as fichye:
            fichye.write(kontni)

    def netwaye_fichye(self):
        kontni = self.li_fichye()
        kontni = kontni.strip()
        kontni = ''.join(e for e in kontni if e.isalnum() or e.isspace())
        with open(self.chemen_fichye, 'w') as fichye:
            fichye.write(kontni)

    def sove_fichye(self, kontni_modifye):
        with open(self.chemen_fichye, 'w') as fichye:
            fichye.write(kontni_modifye)


# Komanse pwogram la
while True:
    print("\nChwazi yon opsyon:")
    print("1. Li Fichye Teks")
    print("2. Afiche Teks")
    print("3. Modifye Teks")
    print("4. Netwaye Teks")
    print("5. Sove Teks")
    print("6. Kwoke")

    opsyon = input("Antre nimewo opsyon ou: ")

    if opsyon == '1':
        chemen = input("Antre chemen fichye tèks la: ")
        gestion_fichye = GestionFichyeTeks(chemen)
        kontni = gestion_fichye.li_fichye()
        print("Kontni fichye tèks la se:\n", kontni)
    elif opsyon == '2':
        gestion_fichye.afiche_fichye()
    elif opsyon == '3':
        ajoute = input("Antre tèks ou vle ajoute: ")
        endeks = int(input("Antre endèks (si genyen) oswa kite sa kòm 0: "))
        gestion_fichye.modifye_fichye(ajoute, endeks)
        print("Tèks la modifye.")
    elif opsyon == '4':
        gestion_fichye.netwaye_fichye()
        print("Tèks la netwaye.")
    elif opsyon == '5':
        kontni_modifye = input("Antre tèks ou vle sove: ")
        gestion_fichye.sove_fichye(kontni_modifye)
        print("Tèks la sove nan fichye a.")
    elif opsyon == '6':
        break
    else:
        print("Opsiyon pa valab. Tann yon lòt opsyon.")
