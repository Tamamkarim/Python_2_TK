import random

class Auto:
    def __init__(self, rek, huippu):
        self.rek = rek
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0    

    def kulje(self):
        self.nopeus = max(0, min(self.nopeus + random.randint(-10, 15), self.huippu))
        self.matka += self.nopeus

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje()

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"{auto.rek}: {auto.matka} km, nopeus: {auto.nopeus} km/h")
        print("-" * 30)

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

# Pääohjelma
autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
kisa = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"Tunti {tunnit}")
        kisa.tulosta_tilanne()

print(f"Kilpailu päättyi {tunnit} tunnin jälkeen!")
kisa.tulosta_tilanne()
