# det er en konstruktør som har to parameter, navnet sitt er artist og tittel.
class Sang:
    def __init__(self,artist,tittel):
        self._artist=artist
        self._tittel=tittel
        # Det kalles bare self._tittel og self._artist.
    def spill(self):
        print( 'Spiller'+"<"+self._tittel+'--'+self._artist+'>')
        # Her trenges det to forskjellige lister fordi hvert ord i tekststrengen(navn!) blir bedt om å bli sammenlignet med hvert del av artistsnavn.
        #   nyartistlist representerer deler av navn
        # gammelartistlist representerer deler av artistnavnene i innsatsvariabelen.
    def sjekk_artist(self,navn):
        nyArtistList=[]
        gammelArtistList=[]
        for i in navn.split():
            nyArtistList.append(i)

        for i in self._artist.split():
            gammelArtistList.append(i)
#Ved å bruke while løkken kan hver navn delene sammenlignes med artistsnavn
        
        teller=0
        while teller<len(nyArtistList):

          if nyArtistList[teller]  not in gammelArtistList:
              teller+=1
          else:
              teller=len(nyArtistList)
              return True
        return False
#  det er to variabler.det kreves de må sammenlignes uavhenging  av små og store bokstaver.Derfor representerer de to variabelen(variabel1 og variabel2) upper versjion av ny tittel
# og den gamle(_self._tittel innsatsvariabel)
    def sjekk_tittel(self,tittel):
        variabel1=self._tittel.upper()
        variabel2=tittel.upper()
        if variabel1==variabel2:
            return True
        else:
            return False
#  det kalles de to metodene som opprettes før i klassen
    def sjekk_artist_og_tittel(self,navn,tittel):
        if self.sjekk_tittel(tittel)==True and self.sjekk_artist(navn)==True :
            return True
        else:
            return False

       
       

        
