from sys import exc_info
import requests
from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
import logging as log
try:
    import ujson as json
except ImportError:
    import json



class Oxford:

    """
    simple python module to work with oxford dictionary api
    this module is still under development and bug reports are welcome and appreciated
    the api key and id packaged with this application are for testintg puporse only

    PS. some feature are not accessible using a developer app_id and api_key such
    as antonyms, synonyms and others
    """


    def __init__(self,app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.url =  "https://od-api.oxforddictionaries.com/api/v2/"


    def entries(self,word,language="en-gb"):
        """
        Use this to retrieve definitions, pronunciations, example sentences, grammatical informationand word origins.
        TIP: Entries ONLY works for dictionary headwords. You may need to use the Lemmas endpoint first to link an inflected form back to its headword (e.g., pixels --> pixel).
        """
        try:
            url = f"{self.url}entries/{language}/{word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)

    
    def lemmas(self,word,language = "en-gb"):
        """
        Use this to check if a word exists in the dictionary, or what 'root' form it links to (e.g., swimming > swim).
        The response tells you the possible lemmasfor a given inflected word.
        This can then be combined with other endpoints to retrieve more information.
        """
        try:
            url = f"{self.url}lemmas/{language}/{word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key}, timeout= self.timeout)
            return r.json()
        except HTTPError as hte:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout as t:
            log.error("Timeout", exc_info = True)
        except ConnectionError as ce:
            log.fatal("Connection error", exc_info=True)



    def search(self,word,lang="en-gb"):
        """
        Use this to find possible translations for a given word.
        """
        try:
            url = f"{self.url}search/thesaurus/{lang}?q={word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def translate(self,word,source_lang,target_lang = "en-gb"):
        """
        Use this to return translations for a given word.
        In the event that a word in the dataset does not have a direct translation, the response will be a definitionin the target language.
        """
        url = f"{self.url}translations/{source_lang}/{target_lang}/{word.lower()}"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def random_registers(self,lang = "en-gb"):
        """
        random registers
        """
        url = f"{self.url}registers/{lang}"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def dictionaries(self):
        """
        returns json list of all dictionaries/languages offered by oxford dictionary 
        """
        url = f"{self.url}languages"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def etymology(self,word,lang = "en-gb"):
        """
        return a json of query word etymology
        """
        url = f"{self.url}words/{lang}?q={word}&fields=etymologies"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def register(self,word,lang = "en-gb"):
        """
        returns json of words associationg the word argument
        """
        url = f"{self.url}words/{lang}?q={word}&fields=registers"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def synonyms(self,word):
        """
        returns a json of all possible synonyms(similar) for the word passed in argument
        """
        url = f"{self.url}thesaurus/en/{word}?fields=synonyms&strictMatch=false"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def antonyms(self,word):
        """
        returns a json of all possible antonyms(opposite) for the word passed in argument

        """
        url = f"{self.url}thesaurus/en/{word}?fields=antonyms&strictMatch=false"
        try:
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def get_word(self,word,language = "en"):

        """
        use this method to get the json 'result' only from an entry search
        """
        try:
            url = f"{self.url}entries/{language}/{word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()["results"][0]
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def define(self,word, language = "en"):
        """
        get the definination of a word 
        """
        try:
            url = f"{self.url}entries/{language}/{word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'][0]
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def pronunciations(self,word,language = "en"):
        """
        returns a pronunciation file link
        """
        try:
            url = f"{self.url}entries/{language}/{word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()["results"][0]["lexicalEntries"][0]['entries'][0]['pronunciations'][0]["audioFile"]
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)


    def etymologies(self,word,language = 'en'):
        """
        returns the etymology of the queried word
        """
        try:
            url = f"{self.url}entries/{language}/{word.lower()}"
            r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
            return r.json()["results"][0]["lexicalEntries"][0]['entries'][0]['etymologies'][0]#["audioFile"]
        except HTTPError:
            log.fatal("Couldn't connect to host", exc_info = True)
        except Timeout:
            log.error("Timeout", exc_info = True)
        except ConnectionError:
            log.fatal("Connection error", exc_info=True)

