#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
#  ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo 
# tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi 
# aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet 
# talon luomiseksi ja talon 
# hisseillä ajelemiseksi.


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
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero + 1} kerrokseen {kohdekerros}.")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissinumero.")


# Pääohjelma
talo = Talo(1, 10, 3)

# Ajetaan hissiä 1 viidenteen kerrokseen ja takaisin ensimmäiseen kerrokseen
talo.aja_hissiä(0, 5)
talo.aja_hissiä(0, 1)

# Ajetaan hissiä 2 kymmenenteen kerrokseen
talo.aja_hissiä(1, 10)
