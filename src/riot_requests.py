import requests
from summoner import Summoner
from summoners import Summoners
from matches import Matches
from datetime import datetime
from match_info import MatchInfo


class RiotRequests:

    def __init__(self):
        self.BASE_API = "https://na1.api.riotgames.com/"
        self.SUMMONER_API = "lol/summoner/v3/summoners/by-name/"
        self.MATCHES_API = "lol/match/v3/matchlists/by-account/"
        self.MATCH_API = "lol/match/v3/matches/"
        self.API_KEY = "?api_key=RGAPI-3c6f83de-1cec-4e5b-9275-48d3ca13009f"


    def get_summoner(self):
        summoner_name = input("What user would you like to look for?\n")
        summoner = Summoner(requests.get(self.BASE_API + self.SUMMONER_API + summoner_name +
                                     self.API_KEY).text, self)
        Summoners.add_summoner(summoner)
        return summoner

    def get_matches(self, account_id, requester):
        requested_matches = requests.get(self.BASE_API + self.MATCHES_API + account_id + self.API_KEY).text
        matches = Matches()
        matches.add_matches(requested_matches, account_id, requester)
        return matches

    def get_match_info(self, match_id):
        requested_match_info = requests.get(self.BASE_API + self.MATCH_API + match_id + self.API_KEY).text
        return MatchInfo(requested_match_info)

    def print_status(self, message):
        print("[" + str(datetime.now()) + "] " + message)
