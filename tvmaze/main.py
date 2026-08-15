import json
from urllib.request import urlopen
import urllib.parse



class Tvmaze:
    def __init__(self):
        self.baseUrl =  "https://www.tvmaze.com"
        

    def searchShow(self, showName):
        url = self.baseUrl + "/search/shows?"
        params = {'q':showName}
        url = url + urllib.parse.urlencode(params)
        #print(url)
        
        #response = requests.get(url, params=params)
        body = None
        with urlopen(url) as response:
            body = response.read()

        jsonOutput = json.loads(body)
        print(jsonOutput)
       

        

    def displayShowDetails(self):
        pass

    def displayEpisodes(self):
        pass

    def displayCast(self):
        pass

    def findEpisode(self):
        #By season or number
        pass

    def searchPerson(self):
        pass

    def similarShows(self):
        pass

    def Schedule(self):
        pass



t1 = Tvmaze()
t1.searchShow("girls")