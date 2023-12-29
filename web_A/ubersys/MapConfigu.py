from folium import Map, ClickForMarker,features


class Mapg():
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
        
        return Map(**args)