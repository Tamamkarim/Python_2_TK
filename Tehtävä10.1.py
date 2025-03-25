#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen 
# numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi 
# on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun 
# h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta 
# 'kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut
#  metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi 
# sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi
#  kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.



# Hissi-luokka
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin
# Metodit
    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")
# Metodit
    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")
# Metodit
    def siirry_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.kerros_ylös()
        while self.nykyinen > kohde:
            self.kerros_alas()

# Testataan hissiä
h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


