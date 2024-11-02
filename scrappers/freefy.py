import requests
from payloads.freefy import getHeaders, cookies


"""
channel/discover
search?loader=search&query=nf
search?loader=searchPage&query=eminem
/api/v1/search/model/track?query=Arijit+sing&perPage=20&paginate=simple&page=3
"""



class freefy:
    def __init__(self):
        self.base_url = "https://freefy.app/api/v1"
    
    def search(self, query):
        url = f"{self.base_url}/search?loader=searchPage&query={query}"
        data = requests.get(url, cookies=cookies, headers=getHeaders())
        print(data.status_code)
        return data.json()

    def searchTracks(self, query, page):
        url = f"{self.base_url}/search/model/track?query={query}&perPage=20&paginate=simple&page={page}"
        data = requests.get(url, cookies=cookies, headers=getHeaders())

        return data.json()
    
    def discover(self):
        url = f"{self.base_url}/channel/discover"
        data = requests.get(url, cookies=cookies, headers=getHeaders())
        return data.json()
