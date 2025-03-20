#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, 
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, 
# että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def siirry_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.kerros_ylös()
        while self.nykyinen > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero + 1} kerrokseen {kohdekerros}.")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissinumero.")

    def palohälytys(self):
        print("🚨 Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"Hissi {i + 1} menee pohjakerrokseen.")
            hissi.siirry_kerrokseen(self.alin)


# Pääohjelma
talo = Talo(1, 10, 3)

# Ajetaan hissiä 1 viidenteen kerrokseen ja takaisin ensimmäiseen kerrokseen
talo.aja_hissiä(0, 5)
talo.aja_hissiä(0, 1)

# Ajetaan hissiä 2 kymmenenteen kerrokseen
talo.aja_hissiä(1, 10)

# Palohälytys!
talo.palohälytys()

