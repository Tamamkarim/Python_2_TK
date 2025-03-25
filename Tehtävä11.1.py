#Toteuta seuraava luokkahierarkia 
#Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi. Kirjalla on 
#lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. 
#Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa 
#julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta 
#molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.


# Julkaisu-luokka
class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")

# Kirja-luokka
class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")

# Lehti-luokka
class lehti(julkaisu):
    def __init__(self, nimi, paa_toimittaja):
        super().__init__(nimi)
        self.paa_toimittaja = paa_toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paa_toimittaja}")

# Pääohjelma
if __name__ == "__main__":
    aku_ankka = lehti("Aku Ankka", "Aki Hyyppä")
    hytti_nro_6 = kirja("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    hytti_nro_6.tulosta_tiedot()


















