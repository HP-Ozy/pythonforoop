#Esempio di definizione di una classe con attributi e metodi:

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("Ciao, mi chiamo", self.nome, self.cognome)

persona = Persona("Mario", "Rossi")

print(persona.nome)
print(persona.cognome)
persona.saluta()
#Esempio di utilizzo dell'ereditarietà:

class Animale:
    def __init__(self, nome):
        self.nome = nome

    def emetti_suono(self):
        pass

class Cane(Animale):
    def emetti_suono(self):
        print("Woof!")

class Gatto(Animale):
    def emetti_suono(self):
        print("Meow!")

cane = Cane("Fido")
gatto = Gatto("Tom")
cane.emetti_suono()
gatto.emetti_suono()
#Esempio di incapsulamento e accesso ai dati privati:

class ContoBancario:
    def __init__(self, saldo_iniziale):
        self.__saldo = saldo_iniziale

    def deposito(self, importo):
        self.__saldo += importo

    def prelievo(self, importo):
        if self.__saldo >= importo:
            self.__saldo -= importo
        else:
            print("Saldo insufficiente!")

    def visualizza_saldo(self):
        print("Saldo attuale:", self.__saldo)

conto = ContoBancario(1000)
conto.deposito(500)
conto.prelievo(200)
conto.visualizza_saldo()
#Esempio di utilizzo di metodi di classe e attributi di classe:

class Automobile:
    carburante = "Benzina"

    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    @classmethod
    def cambia_carburante(cls, nuovo_carburante):
        cls.carburante = nuovo_carburante

    def descrizione(self):
        print(f"Auto: {self.marca} {self.modello}, Carburante: {self.carburante}")

auto1 = Automobile("Fiat", "Panda")
auto2 = Automobile("Toyota", "Corolla")
Automobile.cambia_carburante("Diesel")

auto1.descrizione()
auto2.descrizione()
