from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
        # det leses opplysningene fra liste til til liste i filen. 
        # Det er en ny variabel(spiller) som kaller sang klassen ved to parameter fra filen.
    def les_fil(self,filnavn):
        for linje in open(filnavn,"r"):
            linje=linje.strip()
            koloner=linje.split(";")
            spiller=Sang(koloner[1],koloner[0])
            self._sanger.append(spiller)
            #  det samles ny sang inn i listen med den metoden.
    def legg_til_sang(self,ny_sang):
        self._sanger.append(ny_sang)
        #  det fjernes en sang fra listen med den metoden
    def fjern_sang(self,sang):
        self._sanger.remove(sang)
        #  det kalles spill metoden som er i sang klassen.
    def spill_sang(self,sang):
        sang.spill()
        #  her det kalles spill metoden igjen med alle sangene i listen. derfor ble det brukt for_løkken.
    def spill_alle(self):
        for linje in self._sanger:
            linje.spill()
            # det kalles den andre metoden(sjekk_tittel) i sang klassen. det sammelignes enhver sangene i listen med den nye sangen. Når det returns True i sjekk_tittel metoden
            # kan det returns sangen.
    def finn_sang(self,tittel):
        for sang in self._sanger:
            if sang.sjekk_tittel(tittel):
                return sang
        return None
        # det opprettes en ny liste for å samle alle sangene til artisten. Ved å brukes den andre metoden i sang klassen kan det vurderes artist navn. Når navnet til artister er lik
        # adder sangen i listen.
    def hent_artist_utvalg(self,artistnavn):
        valgendeListe=[]
        for songlinje in self._sanger:
            if songlinje.sjekk_artist(artistnavn)==True:
                valgendeListe.append(songlinje)
        return valgendeListe

print(Spilleliste)
