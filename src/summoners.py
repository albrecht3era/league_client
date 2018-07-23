from summoner import Summoner


class Summoners:

    SUMMONERS = dict()

    @staticmethod
    def add_summoner(summoner: Summoner):
        Summoners.SUMMONERS[summoner.get_name()] = summoner

    @staticmethod
    def get_summoner(summoner_name):
        return Summoners.SUMMONERS[summoner_name]

    @staticmethod
    def get_summoners():
        return Summoners.SUMMONERS
