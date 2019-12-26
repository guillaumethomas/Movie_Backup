"""
https://rapidapi.com/blog/how-to-use-imdb-api/
"""
import requests
import json

class MovieAPI:
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey

    def title_request(self, title):
        params = {
                    "apikey" : self.apikey,
                    "t" : title.replace(" ", "+")
                }
        try:
            res = requests.request("GET", self.url, params=params).text
            #print(req)
            #res = json.load(req)
        except:
            res = None
        return res


if __name__ == "__main__":

    url = "http://www.omdbapi.com/"
    apikey = "d6b6b9d"
    title = "rambo last blood"

    req = MovieAPI(url, apikey)
    resp = req.title_request(title)
    print(resp)
    print(type(resp))
    json.load(resp)
