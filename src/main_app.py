from datetime import datetime
from riot_requests import RiotRequests


class LeagueClient:

    def get_timestamp(self):
        return "[" + str(datetime.now()) + "] "

    @staticmethod
    def run():
        riot_requests = RiotRequests()
        LeagueClient.print_status("Starting League Client...")
        summoner = riot_requests.get_summoner()
        summoner.print_summoner()
        print("\n")
        summoner.get_matches()
        summoner.get_current_match().print_match()
        summoner.get_current_match().get_match_info()

    @staticmethod
    def print_status(message):
        print("[" + str(datetime.now()) + "] " + message)


league_client = LeagueClient()
league_client.run()
