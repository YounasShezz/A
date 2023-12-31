from folium import Map as MM, ClickForMarker,features
from openrouteservice import  Client, optimization
#import openrouteservice as ors

class Map(MM):
    def __init__(self,**args):
        self.__key = "5b3ce3597851110001cf6248ba3731fdcaf24a8590b3de1441910"
        self.cly = Client(key=self.__key)
        super().__init__(**args)
        

        









"""class Mapg():
    def __init__(self):
        self.config = {"location" : [0,0],"height":"100%" ,"width" : '100%', "zoom" : 0,"event": None}
        self.mapConfig = {x for x in self.config.keys()}
    

    def correctConfig(self, s):
        s = {x for x in s.keys()}
        if len(s.difference(self.mapConfig)):
            return False

        return True

    def getMap(self,**args):

        if not self.correctConfig(args):
            return Map(**self.config)
        
        return Map(**args)"""