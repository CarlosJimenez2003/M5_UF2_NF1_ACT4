
class Treballador: #Definix la classe
    """La classe treballador es una classe per crear traballador amb parametres predefinits"""

    def __init__(self, nom="", tipus="BASE", nomina=0.0, hores=0): #Definiu el mètode d'inicialització. 
        self.nomTreballador = nom                           #Pren quatre paràmetres, on self representa la instància de la classe 
        self.tipusTreballador = tipus                       #i els altres són paràmetres que es poden proporcionar en crear una instància de la classe.
        self.nominaTreballador = nomina
        self.horesExtresTreballador = hores

    def set_nom(self, nom):                                         #Pren dos paràmetres, self que representa la instància de la classe i nom que és el nou valor que es vol assignar a l'atribut
        if len(nom) < 3:                                            #Verifica si la longitud del nom nou (nom) és menor que 3.
            raise Exception("El nom ha de tenir 3 o més caracters") #Si la longitud del nom és inferior a 3, es llança una excepció (error) amb el missatge indicat.
        self.nomTreballador = nom                                   #Si la longitud del nom és 3 o més, assigneu el nou valor (nom) a l'atribut nom Treballador de l'objecte.

    def get_nom(self):                     #s'utilitza per obtenir el valor actual de 
        return self.nomTreballador         #l'atribut nom Treballador de la instància de la classe.

    def set_nomina(self, euros):           #Aquest mètode set_nomina s'utilitza per establir 
        self.nominaTreballador = euros     #un valor nou per a l'atribut nominaTreballador

    def get_nomina(self):                  #aquest mètode get_nomina és un "getter" que permet obtenir el valor actual de l'atribut
        return self.nominaTreballador      #nomina Treballador de la instància de la classe sense permetre'n la modificació directa des de fora de la classe.

    def set_hores_extres(self, hores):     #set_hores_extres s'utilitza per establir un valor nou per a l'atribut horesExtresTreballador
        self.horesExtresTreballador = hores

    def get_hores_extres(self):            #aquest mètode get_hores_extres és un "getter" que permet obtenir el valor actual de l'atribut 
        return self.horesExtresTreballador #horesExtresTraballador de la instància de la classe sense permetre'n la modificació

    def set_tipus_treballador(self, tipus):                         #set_tipus_treballador s'utilitza per establir un nou valor per a l'atribut 
        if tipus in [self.DIRECTOR, self.SUBDIRECTOR, self.BASE]:   #tipus Treballador, però abans de fer-ho verifica si el nou tipus de treballador
            self.tipusTreballador = tipus                           #és un dels tipus vàlids. En cas contrari, se'n llança una excepció.
        else:
            raise Exception("Tipus de treballador no vàlid")

    def get_tipus_treballador(self):       #get_tipus_treballador permet obtenir el valor actual de l'atribut tipus Treballador de la instància 
        return self.tipusTreballador       #de la classe sense permetre'n la modificació directa des de fora de la classe.